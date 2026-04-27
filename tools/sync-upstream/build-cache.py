#!/usr/bin/env python3
"""One-shot: build translation-cache.json by pairing each upstream-CJK file's
sha256 hash with the already-translated content in this repo.

Run after the initial manual translation pass, so subsequent `sync.py` runs
hit the cache for unchanged upstream files.

  python tools/sync-upstream/build-cache.py
"""
from __future__ import annotations

import hashlib
import json
import re
import subprocess
import sys
from pathlib import Path

REPO = Path(__file__).resolve().parents[2]
TOOLS = REPO / "tools" / "sync-upstream"
CLONE = TOOLS / ".upstream-clone"
CACHE_FILE = TOOLS / "translation-cache.json"
STATE_FILE = TOOLS / "upstream-state.json"

CJK = re.compile(r"[一-鿿㐀-䶿]")
TRANSLATABLE_EXTS = {
    ".md", ".html", ".htm", ".js", ".mjs", ".cjs", ".jsx", ".ts", ".tsx",
    ".py", ".sh", ".json", ".css", ".svg", ".txt", ".yml", ".yaml",
}
TRANSLATABLE_FILENAMES = {".gitignore", ".gitattributes", ".editorconfig", "Dockerfile", "Makefile"}


def run(cmd, cwd=None):
    return subprocess.run(cmd, cwd=cwd, check=True, capture_output=True, text=True).stdout


def main() -> int:
    state = json.loads(STATE_FILE.read_text())
    if not CLONE.exists():
        print(f"Cloning upstream into {CLONE}…")
        run(["git", "clone", "--quiet", state["upstream_url"], str(CLONE)])
    sha = run(["git", "rev-parse", "HEAD"], cwd=CLONE).strip()
    if sha != state["last_synced_sha"]:
        print(f"WARNING: clone HEAD ({sha}) != upstream-state.last_synced_sha ({state['last_synced_sha']})")
        print("Resetting clone to the recorded SHA…")
        run(["git", "reset", "--quiet", "--hard", state["last_synced_sha"]], cwd=CLONE)

    cache: dict[str, str] = {}
    skipped: list[str] = []
    files = run(["git", "ls-files"], cwd=CLONE).splitlines()
    for rel in files:
        src = CLONE / rel
        if not src.is_file():
            continue
        if src.suffix.lower() not in TRANSLATABLE_EXTS and src.name not in TRANSLATABLE_FILENAMES:
            continue
        try:
            text = src.read_text(encoding="utf-8")
        except UnicodeDecodeError:
            continue
        if not CJK.search(text):
            continue
        translated_path = REPO / rel
        if not translated_path.is_file():
            skipped.append(f"{rel} (no translated file in repo)")
            continue
        translated = translated_path.read_text(encoding="utf-8")
        if CJK.search(translated):
            skipped.append(f"{rel} (translated file still contains CJK)")
            continue
        h = hashlib.sha256(src.read_bytes()).hexdigest()
        cache[h] = translated

    CACHE_FILE.write_text(json.dumps(cache, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    print(f"Cache populated: {len(cache)} entries → {CACHE_FILE.relative_to(REPO)}")
    if skipped:
        print(f"Skipped ({len(skipped)}):")
        for s in skipped:
            print(f"  - {s}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
