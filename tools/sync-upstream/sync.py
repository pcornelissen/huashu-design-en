#!/usr/bin/env python3
"""Sync this repo from the upstream Chinese huashu-design repo.

Pipeline:
  1. Clone/fetch upstream into .upstream-clone (gitignored).
  2. For each file at upstream HEAD:
       - text file with CJK → translate (cache hit reuses prior translation).
       - text file without CJK → copy as-is.
       - binary file → copy as-is.
  3. Files removed upstream are removed here too.
  4. Update upstream-state.json with the new HEAD SHA.

The translation cache is keyed by sha256 of the upstream file's bytes, so any
upstream change to a file triggers a re-translation; everything else is stable.

Requires:  ANTHROPIC_API_KEY env var, and `pip install anthropic`.
Run from repo root:  python tools/sync-upstream/sync.py
"""
from __future__ import annotations

import hashlib
import json
import os
import shutil
import subprocess
import sys
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[2]
TOOLS_DIR = REPO_ROOT / "tools" / "sync-upstream"
STATE_FILE = TOOLS_DIR / "upstream-state.json"
CACHE_FILE = TOOLS_DIR / "translation-cache.json"
REPLACEMENTS_FILE = TOOLS_DIR / "replacements.json"
CLONE_DIR = TOOLS_DIR / ".upstream-clone"

TRANSLATABLE_EXTS = {
    ".md", ".html", ".htm", ".js", ".mjs", ".cjs", ".jsx", ".ts", ".tsx",
    ".py", ".sh", ".json", ".css", ".svg", ".txt", ".yml", ".yaml",
}
# Extensionless files we still treat as text (config files with comments).
TRANSLATABLE_FILENAMES = {".gitignore", ".gitattributes", ".editorconfig", "Dockerfile", "Makefile"}
# Files that we never touch even if upstream has them — pipeline-internal paths.
SKIP_PATHS = {"tools/sync-upstream", ".upstream-clone"}

CJK_RE = __import__("re").compile(r"[一-鿿㐀-䶿]")

TRANSLATE_PROMPT = """You are translating a file from a Chinese open-source project (huashu-design, an HTML-native design skill for Claude Code) into English.

Rules:
1. Translate ALL Chinese text to natural, fluent English. Keep technical terminology accurate.
2. Preserve the file's structure EXACTLY: code, markup, indentation, line breaks, frontmatter, JSON/YAML keys, HTML tags/attributes, JS/Python syntax, markdown formatting.
3. Translate Chinese in: prose, comments, string literals, HTML text content, alt text, JSON values that are user-facing strings, SVG text elements.
4. Do NOT translate: identifiers (variable/function/class names, JSON/YAML keys), URLs, file paths, code logic, regex patterns, ASCII art, language codes (e.g. "zh-CN"), emoji.
5. Where bilingual lines exist (Chinese + English already side by side), keep ONLY the English.
6. Where a phrase is a brand name or product name in Chinese pinyin (e.g. "Huashu"), keep the pinyin.
7. Output ONLY the translated file content. No explanations, no markdown code fences around the whole output, no preamble.

File path (for context): {path}

--- BEGIN FILE ---
{content}
--- END FILE ---"""


def has_cjk(text: str) -> bool:
    return bool(CJK_RE.search(text))


def file_hash(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def load_json(path: Path, default):
    if path.exists():
        return json.loads(path.read_text(encoding="utf-8"))
    return default


def save_json(path: Path, data) -> None:
    path.write_text(json.dumps(data, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")


def run(cmd: list[str], cwd: Path | None = None) -> str:
    return subprocess.run(cmd, cwd=cwd, check=True, capture_output=True, text=True).stdout


def ensure_clone(upstream_url: str) -> Path:
    if CLONE_DIR.exists():
        run(["git", "fetch", "--quiet", "origin"], cwd=CLONE_DIR)
        run(["git", "reset", "--quiet", "--hard", "origin/HEAD"], cwd=CLONE_DIR)
    else:
        CLONE_DIR.parent.mkdir(parents=True, exist_ok=True)
        run(["git", "clone", "--quiet", upstream_url, str(CLONE_DIR)])
    return CLONE_DIR


def list_upstream_files(clone: Path) -> list[str]:
    out = run(["git", "ls-files"], cwd=clone)
    return [line for line in out.splitlines() if line]


def translate(content: str, path: str, client) -> str:
    msg = client.messages.create(
        model="claude-opus-4-7",
        max_tokens=64000,
        messages=[{"role": "user", "content": TRANSLATE_PROMPT.format(path=path, content=content)}],
    )
    return "".join(b.text for b in msg.content if getattr(b, "type", None) == "text")


def is_skipped(path: str) -> bool:
    return any(path == p or path.startswith(p + "/") for p in SKIP_PATHS)


def load_replacements() -> list[tuple[str, str]]:
    if not REPLACEMENTS_FILE.exists():
        return []
    data = json.loads(REPLACEMENTS_FILE.read_text(encoding="utf-8"))
    return [(r["find"], r["replace"]) for r in data.get("replacements", [])]


def apply_replacements(text: str, rules: list[tuple[str, str]]) -> str:
    for find, replace in rules:
        text = text.replace(find, replace)
    return text


def main() -> int:
    force = "--force" in sys.argv
    state = load_json(STATE_FILE, {"upstream_url": "https://github.com/alchaincyf/huashu-design.git", "last_synced_sha": None})
    cache = load_json(CACHE_FILE, {})

    clone = ensure_clone(state["upstream_url"])
    new_sha = run(["git", "rev-parse", "HEAD"], cwd=clone).strip()
    if state.get("last_synced_sha") == new_sha and not force:
        print(f"Already synced to {new_sha}. Nothing to do.  (use --force to re-materialise files, e.g. after editing replacements.json)")
        return 0

    upstream_files = set(list_upstream_files(clone))
    print(f"Upstream HEAD: {new_sha}")
    print(f"Upstream tracked files: {len(upstream_files)}")

    client = None
    needs_translation = False

    # Pass 1: identify what needs translating, fail fast if API key missing.
    pending = []
    for rel in upstream_files:
        if is_skipped(rel):
            continue
        src = clone / rel
        if not src.is_file():
            continue
        data = src.read_bytes()
        ext = src.suffix.lower()
        if ext in TRANSLATABLE_EXTS or src.name in TRANSLATABLE_FILENAMES:
            try:
                text = data.decode("utf-8")
            except UnicodeDecodeError:
                continue
            if has_cjk(text):
                h = file_hash(data)
                if h not in cache:
                    pending.append((rel, text, h))
                    needs_translation = True

    if needs_translation:
        if not os.environ.get("ANTHROPIC_API_KEY"):
            print("ERROR: ANTHROPIC_API_KEY is not set, but the following files need translation:", file=sys.stderr)
            for rel, _, _ in pending:
                print(f"  - {rel}", file=sys.stderr)
            return 1
        try:
            from anthropic import Anthropic
        except ImportError:
            print("ERROR: 'anthropic' package not installed.  pip install anthropic", file=sys.stderr)
            return 1
        client = Anthropic()
        print(f"Translating {len(pending)} new/changed file(s)…")
        for i, (rel, text, h) in enumerate(pending, 1):
            print(f"  [{i}/{len(pending)}] {rel}")
            cache[h] = translate(text, rel, client)
            save_json(CACHE_FILE, cache)  # checkpoint after each, in case of crash

    # Pass 2: materialise files in repo.
    rules = load_replacements()
    written = copied = removed = 0
    for rel in upstream_files:
        if is_skipped(rel):
            continue
        src = clone / rel
        dst = REPO_ROOT / rel
        if not src.is_file():
            continue
        dst.parent.mkdir(parents=True, exist_ok=True)
        data = src.read_bytes()
        ext = src.suffix.lower()
        if ext in TRANSLATABLE_EXTS or src.name in TRANSLATABLE_FILENAMES:
            try:
                text = data.decode("utf-8")
            except UnicodeDecodeError:
                dst.write_bytes(data)
                copied += 1
                continue
            if has_cjk(text):
                content = cache[file_hash(data)]
                dst.write_text(apply_replacements(content, rules), encoding="utf-8")
                written += 1
            else:
                dst.write_text(apply_replacements(text, rules), encoding="utf-8")
                copied += 1
        else:
            dst.write_bytes(data)
            copied += 1

    # Detect deletions: anything tracked here that upstream no longer has.
    repo_tracked = run(["git", "ls-files"], cwd=REPO_ROOT).splitlines() if (REPO_ROOT / ".git").exists() else []
    for rel in repo_tracked:
        if is_skipped(rel) or rel in {"LICENSE", ".gitignore"}:
            continue
        if rel.startswith(("tools/", ".github/")):
            continue
        if rel not in upstream_files:
            target = REPO_ROOT / rel
            if target.exists():
                target.unlink()
                removed += 1

    state["last_synced_sha"] = new_sha
    save_json(STATE_FILE, state)
    save_json(CACHE_FILE, cache)

    print(f"Done.  translated/cached: {written}   copied: {copied}   removed: {removed}")
    print("Review the diff with `git status` / `git diff`, then commit.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
