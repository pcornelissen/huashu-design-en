> **English mirror.** This repository is a machine-translated, human-reviewed English version of [alchaincyf/huashu-design](https://github.com/alchaincyf/huashu-design). It is automatically synced from upstream — see [tools/sync-upstream](tools/sync-upstream/) for how that works. All credit, copyright, and authorship belong to the original author. The original "Personal Use Only" license applies unchanged — see [LICENSE](LICENSE).

<div align="center">

# Huashu Design

> *"Type. Hit enter. A finished design lands in your lap."*

[![License](https://img.shields.io/badge/License-Personal%20Use%20Only-orange.svg)](LICENSE)
[![Agent-Agnostic](https://img.shields.io/badge/Agent-Agnostic-blueviolet)](https://skills.sh)
[![Skills](https://img.shields.io/badge/skills.sh-Compatible-green)](https://skills.sh)

<br>

**Type one sentence to your agent — get back a design ready to ship.**

<br>

In 3 to 30 minutes, you can ship a **product launch animation**, a clickable App prototype, an editable PPT deck, or a print-grade infographic.

Not "decent for AI" quality — it looks like a real design team made it. Give the skill your brand assets (logo, color palette, UI screenshots) and it reads your brand's voice; give it nothing and the built-in 20 design vocabularies still keep you out of AI-slop territory.

**Every animation in this README was made by huashu-design itself.** No Figma, no After Effects — just a one-sentence prompt + skill run. Next product launch needs a promo video? Now you can make it too.

```
npx skills add pcornelissen/huashu-design-en
```

Cross-agent compatible — Claude Code, Cursor, Codex, OpenClaw, Hermes all work.

[See it work](#demo-gallery) · [Install](#install) · [What it does](#what-it-does) · [How it works](#core-mechanics) · [vs. Claude Design](#vs-claude-design)

</div>

---

<p align="center">
  <img src="https://github.com/alchaincyf/huashu-design/releases/download/v2.0/hero-animation-v10-en.gif" alt="huashu-design Hero · Type → pick direction → gallery unfolds → focus → brand reveal" width="100%">
</p>

<p align="center"><sub>
  ▲ 25 sec · Terminal → 4 directions → Gallery ripple → 4× Focus → Brand reveal<br>
  👉 <a href="https://www.huasheng.ai/huashu-design-hero/">Open the interactive HTML version with sound</a> ·
  <a href="https://github.com/alchaincyf/huashu-design/releases/download/v2.0/hero-animation-v10-en.mp4">Download MP4 (with BGM+SFX · 10MB)</a>
</sub></p>

---

## Install

```bash
npx skills add pcornelissen/huashu-design-en
```

Then just talk to Claude Code:

```
"Make a keynote deck on AI psychology — recommend 3 style directions to pick from."
"Build an iOS prototype for an AI Pomodoro app — 4 core screens, actually clickable."
"Turn this logic into a 60-second animation. Export MP4 and GIF."
"Run a 5-dimension expert review on this design."
```

No buttons, no panels, no Figma plugin.

---

## Star History

<p align="center">
  <a href="https://star-history.com/#alchaincyf/huashu-design&Date">
    <img src="https://api.star-history.com/svg?repos=alchaincyf/huashu-design&type=Date" alt="huashu-design Star History" width="80%">
  </a>
</p>

---

## What it does

| Capability | Deliverable | Typical time |
|------|--------|----------|
| Interactive prototype (App / Web) | Single-file HTML · real iPhone bezel · clickable · Playwright-verified | 10–15 min |
| Slide decks | HTML deck (browser presentation) + editable PPTX (text frames preserved) | 15–25 min |
| Timeline animation | MP4 (25fps / 60fps interpolation) + GIF (palette-optimized) + BGM | 8–12 min |
| Design variations | 3+ side-by-side · Tweaks live params · cross-dimension exploration | 10 min |
| Infographic / data viz | Print-quality typography · exports to PDF/PNG/SVG | 10 min |
| Design direction advisor | 5 schools × 20 design philosophies · 3 directions recommended · Demos generated in parallel | 5 min |
| 5-dimension expert critique | Radar chart + Keep/Fix/Quick Wins · actionable punch list | 3 min |

---

## Demo Gallery

### Design Direction Advisor

The fallback for vague briefs: pick 3 differentiated directions from 5 schools × 20 design philosophies, generate all 3 demos in parallel, let the user choose.

<p align="center"><img src="https://github.com/alchaincyf/huashu-design/releases/download/v2.0/w3-fallback-advisor.gif" width="100%"></p>

### iOS App Prototype

Pixel-accurate iPhone 15 Pro body (Dynamic Island / status bar / Home Indicator) · state-driven multi-screen navigation · real images pulled from Wikimedia/Met/Unsplash · Playwright click tests.

<p align="center"><img src="https://github.com/alchaincyf/huashu-design/releases/download/v2.0/c1-ios-prototype.gif" width="100%"></p>

### Motion Design Engine

Stage + Sprite time-slice model · `useTime` / `useSprite` / `interpolate` / `Easing` — four APIs cover every animation need · one command exports MP4 / GIF / 60fps-interpolated / BGM-scored finals.

<p align="center"><img src="https://github.com/alchaincyf/huashu-design/releases/download/v2.0/c3-motion-design.gif" width="100%"></p>

### HTML Slides → Editable PPTX

HTML decks for browser presentation · `html2pptx.js` reads DOM computed styles and translates each element into a real PowerPoint object · the export is **actual text frames** — double-click in PPT to edit.

<p align="center"><img src="https://github.com/alchaincyf/huashu-design/releases/download/v2.0/c2-slides-pptx.gif" width="100%"></p>

### Tweaks · Live Variation Switching

Colors / typography / information density parameterized · side panel toggle · pure-frontend + `localStorage` persistence · survives reload.

<p align="center"><img src="https://github.com/alchaincyf/huashu-design/releases/download/v2.0/c4-tweaks.gif" width="100%"></p>

### Infographic / Data Viz

Magazine-grade typography · precise CSS Grid columns · `text-wrap: pretty` typographic details · driven by real data · exports to vector PDF / 300dpi PNG / SVG.

<p align="center"><img src="https://github.com/alchaincyf/huashu-design/releases/download/v2.0/c5-infographic.gif" width="100%"></p>

### 5-Dimension Expert Critique

Philosophical coherence · visual hierarchy · execution craft · functionality · innovation — each scored 0–10 · radar-chart visualization · outputs Keep / Fix / Quick Wins punch list.

<p align="center"><img src="https://github.com/alchaincyf/huashu-design/releases/download/v2.0/c6-expert-review.gif" width="100%"></p>

### Junior Designer Workflow

No heroic one-shot attempts: start with assumptions + placeholders + reasoning, show it to the user early, then iterate. Fixing a misunderstanding early is 100× cheaper than fixing it late.

<p align="center"><img src="https://github.com/alchaincyf/huashu-design/releases/download/v2.0/w2-junior-designer.gif" width="100%"></p>

### Brand Asset Protocol · 5-step hard process

Mandatory whenever the task involves a specific brand: ask → search → download (three fallback paths) → grep color values → write `brand-spec.md`.

<p align="center"><img src="https://github.com/alchaincyf/huashu-design/releases/download/v2.0/w1-brand-protocol.gif" width="100%"></p>

---

## Showcase · Real Cases

### "Let's talk skills" · PM after-party deck

> **Live demo · [https://skill-huasheng.vercel.app](https://skill-huasheng.vercel.app)**

A 13-page HTML deck, **made entirely with huashu-design**:

- Black-background minimalist serif visual system (cover / about / hook / what / why / closing)
- Two 22-second cinematic demos with BGM + SFX (Nuwa skill workflow + Darwin skill workflow), each using a **completely independent visual language**:
  - **Nuwa**: 3D knowledge orbit + Pentagon distillation + SKILL.md typewriter + "21 minutes" hero reveal
  - **Darwin**: autoresearch loop spin + v1/v5 side-by-side diff + full-screen Hill-Climb curve + Ratchet gear lock
- Each cinematic shows a **complete static workflow dashboard** by default (the audience can see how the skill runs at any time); pressing ▶ triggers the animation, which fades back to the dashboard when done
- Embeds the 25-second hero animation from huasheng.ai (with a local-iframe fallback)
- Real data: 14,495 stargazers' real curve (pulled via the gh API) + DeepSeek V4 real specs (verified via WebSearch)
- Real AI assets: ran a 4×2 grid mega-image with `huashu-gpt-image`, then `extract_grid.py` cut out 8 separate transparent PNGs to float in the 3D orbit

**Pages worth referencing**:
- `/slides/slide-04b-nuwa-flow.html` · two-layer architecture: static dashboard + cinematic overlay
- `/slides/slide-06b-darwin-flow.html` · companion case with a fully independent visual language
- `/slides/slide-03b-deepseek-cover.html` · AI slop vs. real-designer perspective comparison page

For detailed cinematic patterns, see `references/cinematic-patterns.md`.

---

## Core Mechanics

### Brand Asset Protocol

The hardest rule in the skill. When the task touches a specific brand (Stripe, Linear, Anthropic, your own company, etc.), five steps are enforced:

| Step | Action | Purpose |
|------|------|------|
| 1 · Ask | Does the user have brand guidelines? | Respect existing resources |
| 2 · Search official brand pages | `<brand>.com/brand` · `brand.<brand>.com` · `<brand>.com/press` | Grab authoritative color values |
| 3 · Download assets | SVG file → full HTML of official site → eyedrop colors from product screenshots | Three fallback paths — fall through to the next as soon as one fails |
| 4 · grep extract color values | Pull every `#xxxxxx` from the assets, sort by frequency, filter out black/white/gray | **Never guess brand colors from memory** |
| 5 · Freeze to spec | Write `brand-spec.md` + CSS variables; every HTML references `var(--brand-*)` | Un-frozen knowledge evaporates |

A/B test (v1 vs v2, 6 agents each): **v2 reduced stability variance 5× compared to v1**. Stability of stability — that's the skill's real moat.

### Design Direction Advisor (Fallback)

Triggered when the brief is too vague to act on:

- Don't run on generic intuition — enter Fallback mode
- Recommend 3 differentiated directions from 5 schools × 20 design philosophies, **each from a different school**
- Each comes with flagship works, gestalt keywords, representative designer
- Generate 3 visual demos in parallel, let the user choose
- Once chosen, continue into the Junior Designer main flow

### Junior Designer Workflow

The default working mode across every task:

- Send the full question set to the user in one batch before starting; wait for all answers before moving
- Write assumptions + placeholders + reasoning comments directly into the HTML
- Show it to the user early (even if just gray blocks)
- Fill in real content → variations → Tweaks — show again at each of these three steps
- Manually eyeball the browser with Playwright before delivery

### Anti AI-slop Rules

Avoid the visual common denominator of AI output (purple gradients / emoji icons / rounded-corner + left border accent / SVG-drawn human faces / Inter as display). Use `text-wrap: pretty` + CSS Grid + carefully chosen serif display faces and oklch colors.

---

## vs. Claude Design

I'll be upfront: the Brand Asset Protocol's philosophy was lifted from system prompts circulating from Claude Design. That prompt hammers home a single idea — **great hi-fi design doesn't start from a blank page; it grows from existing design context**. That one principle is the difference between a 65-point design and a 90-point design.

Positioning differences:

| | Claude Design | huashu-design |
|---|---|---|
| Form | Web product (used in browser) | Skill (used in Claude Code) |
| Quota | Subscription quota | API usage · parallel agents not capped by quota |
| Output | In-canvas + Figma export | HTML / MP4 / GIF / editable PPTX / PDF |
| Interaction | GUI (click, drag, edit) | Conversation (talk, wait for the agent) |
| Complex animation | Limited | Stage + Sprite timeline · 60fps export |
| Cross-agent | Claude.ai exclusive | Any skill-compatible agent |

Claude Design is a **better graphics tool**. Huashu-design **makes the graphics-tool layer disappear**. Two paths, different audiences.

---

## Limitations

- **No layer-editable PPTX-to-Figma round-trip.** The output is HTML — screenshottable, recordable, image-exportable, but not draggable into Keynote for text-position tweaks.
- **Framer-Motion-tier complex animations are out of scope.** 3D, physics simulation, particle systems exceed the skill's boundaries.
- **Brand-from-zero design quality drops to 60–65 points.** Drawing hi-fi from nothing was always a last resort.

This is an 80-point skill, not a 100-point product. For people unwilling to open a graphical UI, an 80-point skill beats a 100-point product.

---

## Repository Structure

```
huashu-design/
├── SKILL.md                 # Main doc (read by agent)
├── README.md                # This file (read by user)
├── assets/                  # Starter Components
│   ├── animations.jsx       # Stage + Sprite + Easing + interpolate
│   ├── ios_frame.jsx        # iPhone 15 Pro bezel
│   ├── android_frame.jsx
│   ├── macos_window.jsx
│   ├── browser_window.jsx
│   ├── deck_stage.js        # HTML deck engine
│   ├── deck_index.html      # Multi-file deck assembler
│   ├── design_canvas.jsx    # Side-by-side variation display
│   ├── showcases/           # 24 prebuilt samples (8 scenes × 3 styles)
│   └── bgm-*.mp3            # 6 scene-specific background tracks
├── references/              # Drill-down docs by task
│   ├── animation-pitfalls.md
│   ├── design-styles.md     # Detailed library of 20 design philosophies
│   ├── slide-decks.md
│   ├── editable-pptx.md
│   ├── critique-guide.md
│   ├── video-export.md
│   └── ...
├── scripts/                 # Export toolchain
│   ├── render-video.js      # HTML → MP4
│   ├── convert-formats.sh   # MP4 → 60fps + GIF
│   ├── add-music.sh         # MP4 + BGM
│   ├── export_deck_pdf.mjs
│   ├── export_deck_pptx.mjs
│   ├── html2pptx.js
│   └── verify.py
└── demos/                   # 9 capability demos (c*/w*) — bilingual GIF/MP4/HTML + hero v10
```

---

## Origin Story

The day Anthropic launched Claude Design I played with it until 4 a.m. A few days later I realized I hadn't opened it once since — not because it's bad (it's the most polished product in the category) — but because I'd rather have an agent work in my terminal than open any graphical UI.

So I had an agent deconstruct Claude Design itself (including the system prompts circulating in the community, the brand asset protocol, the component mechanics), distill it into a structured spec, then write it up as a skill installed in my own Claude Code.

Thanks to Anthropic for writing the Claude Design prompts so clearly. This kind of derivative work, inspired by other products, is the new form of open-source culture in the AI era.

---

## License · Usage Rights

**Personal use is free and unrestricted** — studying, research, creating, building things for yourself, writing articles, side projects, posting on Weibo or WeChat Official Accounts. Use it freely, no need to ask.

**Enterprise / commercial use is restricted** — any company, team, or for-profit organization wanting to integrate this skill into a product, external service, or client deliverable **must obtain authorization from Huasheng first**. Including but not limited to:
- Using the skill as part of internal company tooling
- Using skill outputs as the primary creative method for external deliverables
- Building a commercial product on top of the skill
- Using it in paid client projects

**For commercial licensing contact**, see the social platforms below.

---

## Connect · Huasheng (Huashu)

Huasheng is an AI-native coder, independent developer, and AI content creator. Notable work: Cat Fill Light (App Store Top 1 in Paid category), *A Book on DeepSeek*, Nüwa.skill (GitHub 12k+ stars). Combined 300k+ followers across platforms.

| Platform | Handle | Link |
|---|---|---|
| X / Twitter | @AlchainHust | https://x.com/AlchainHust |
| WeChat Official Account | Huashu | Search "Huashu" in WeChat |
| Bilibili | Huashu | https://space.bilibili.com/14097567 |
| YouTube | Huashu | https://www.youtube.com/@Alchain |
| Xiaohongshu | Huashu | https://www.xiaohongshu.com/user/profile/5abc6f17e8ac2b109179dfdf |
| Official Site | huasheng.ai | https://www.huasheng.ai/ |
| Developer Hub | bookai.top | https://bookai.top |

For commercial licensing, collaborations, or sponsored content, DM Huasheng on any of the platforms above.
