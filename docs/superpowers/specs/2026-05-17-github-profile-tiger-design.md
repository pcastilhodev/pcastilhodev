# GitHub Profile — Full Pixel Art Tiger Design

**Date:** 2026-05-17  
**User:** pcastilhodev (Pedro)  
**Repo:** github.com/pcastilhodev/pcastilhodev  

---

## Overview

A full pixel art themed GitHub profile README centered around a **tropical forest tiger** aesthetic. Every visual element follows the same pixel art retro-gaming style and tropical color palette. The profile should feel like opening a game screen — cohesive, alive, and impressive at first scroll.

---

## Color Palette

| Name | Hex | Usage |
|---|---|---|
| Forest Deep | `#0d1f17` | Card backgrounds, dark fills |
| Forest Dark | `#1a3a2a` | Page background tone, empty graph squares |
| Forest Mid | `#2d6a4f` | Tree layers, secondary text |
| Leaf Green | `#52b788` | Contribution graph low |
| Tiger Orange | `#f4a261` | Primary accent — borders, icons, tiger |
| Solar Gold | `#e9c46a` | Titles, headings, highlights |
| Near Black | `#0d0d0d` | Text contrast, sprite outlines |

---

## Section 1 — Animated Banner

**File:** `assets/banner.svg`  
**Dimensions:** 900×300px  
**Format:** SVG with CSS keyframe animations, hosted via GitHub Pages to avoid GitHub's SVG animation restrictions.

**Scene composition:**
- Background layers (parallax depth): dark forest silhouette → mid-layer trees → foreground leaves/vines
- Ground: pixel art grass with tropical flowers (orange/yellow, matching tiger palette)
- **Tiger:** center-left, lying down in a majestic resting pose, tail swinging in a loop (4-frame animation)
- Ambient animations: leaves drifting down slowly, 2–3 butterflies crossing the scene, subtle light-ray flicker through canopy
- Top-right corner: `pcastilhodev` in pixel font with orange `#f4a261` underline

**Animation loops:** all indefinite, natural speed (leaves ~8s, butterflies ~12s, tail ~1.5s)

**Hosting:** GitHub Pages enabled on the repo, SVG served from `https://pcastilhodev.github.io/pcastilhodev/assets/banner.svg`. README references this URL so animations render for all visitors.

---

## Section 2 — Dividers

**File:** `assets/divider.svg` (reused between all sections)  
**Dimensions:** 900×12px  
**Content:** repeating pixel art pattern of tropical leaves/vines in greens and orange, subtle horizontal stripe

---

## Section 3 — About Me

Uses [readme-typing-svg](https://github.com/DenverCoder1/readme-typing-svg) to display animated typewriter text:

```
Lines (cycling):
  "Olá, eu sou o Pedro! 🐅"
  "Desenvolvedor de Software @ TOTVS"
  "Graduando em Sistemas de Informação — IFG 🇧🇷"
  "Construindo coisas. Aprendendo sempre."
```

**Config:** font size 22px, color `#f4a261`, dark background, cursor enabled, center-aligned.

---

## Section 4 — Tech Stack

Three grouped rows of `shields.io` badges. Style: `flat-square`, color scheme matches tiger palette.

**Badge style:** `?style=flat-square&logo=<name>&logoColor=%23f4a261&labelColor=%231a3a2a&color=%230d1f17`

**Linguagens:**
- JavaScript, Java, Python

**Ferramentas:**
- Git, GitHub, IntelliJ IDEA, VS Code

**Estudando agora:**
- Harness Engineering

---

## Section 5 — GitHub Stats Cards

Three cards from [github-readme-stats](https://github.com/anuraghazra/github-readme-stats):

1. **Stats card** (left, ~49% width): stars, commits, PRs, issues, contributed-to count
2. **Streak card** (right, ~49% width): current streak, longest streak, total contributions — via [streak-stats](https://github.com/DenverCoder1/github-readme-streak-stats)
3. **Top languages card** (full width): most used languages bar chart

**Shared theme parameters:**
```
bg_color=0d1f17
border_color=f4a261
title_color=e9c46a
text_color=f4a261
icon_color=52b788
hide_border=false
border_radius=0
```

`border_radius=0` gives the flat, pixel-perfect retro look.

---

## Section 6 — Tiger on Contribution Graph

**File generated:** `assets/tiger-contrib.svg` (auto-committed by Actions)

**Mechanism:** Custom Python script (`scripts/generate_tiger_contrib.py`) run via GitHub Actions. It fetches contribution data from the GitHub GraphQL API, renders the grid as SVG, and overlays the animated tiger sprite walking across it. This approach gives full control over sprite and colors without depending on third-party actions that don't support custom sprites.

**Tiger sprite:**
- Size: 8×8px per frame
- Frames: 4-frame walk cycle (right-facing)
- Colors: `#f4a261` body, `#0d0d0d` stripes, `#e9c46a` belly
- Stored in repo as `assets/tiger-sprite.svg` (sprite sheet, 4 frames horizontal)

**Contribution graph colors (overriding snk defaults):**
| Level | Color |
|---|---|
| 0 (empty) | `#1a3a2a` |
| 1 | `#52b788` |
| 2 | `#74c69d` |
| 3 | `#f4a261` |
| 4 | `#e9c46a` |

**GitHub Actions workflow:** `.github/workflows/tiger-contrib.yml`
- Trigger: `schedule: cron '0 0 * * *'` + `workflow_dispatch`
- Steps: checkout → generate SVG (snk action with custom config) → commit & push `assets/tiger-contrib.svg`

---

## File Structure

```
pcastilhodev/          (repo root)
├── README.md
├── assets/
│   ├── banner.svg          # main animated banner
│   ├── divider.svg         # section divider strip
│   ├── tiger-sprite.svg    # sprite sheet (4-frame walk cycle, hand-crafted SVG pixel art)
│   └── tiger-contrib.svg   # auto-generated by Actions (do not edit manually)
├── scripts/
│   └── generate_tiger_contrib.py  # fetches GitHub API + renders SVG
└── .github/
    └── workflows/
        └── tiger-contrib.yml
```

---

## README Structure (final assembly)

```markdown
<div align="center">
  <img src="https://pcastilhodev.github.io/pcastilhodev/assets/banner.svg" />
</div>

<img src="assets/divider.svg" />

<div align="center">
  <!-- readme-typing-svg about me -->
</div>

<img src="assets/divider.svg" />

<!-- Tech stack badges (3 rows) -->

<img src="assets/divider.svg" />

<!-- Stats cards (left + right, then full-width languages) -->

<img src="assets/divider.svg" />

<div align="center">
  <img src="assets/tiger-contrib.svg" />
</div>
```

---

## Technical Constraints & Decisions

- **SVG animations:** GitHub strips CSS animations in READMEs when served from raw.githubusercontent.com. Solution: enable GitHub Pages on the repo and reference the Pages URL. This is the standard workaround used by high-quality profile repos.
- **snk fork:** We adapt the existing snk action rather than building from scratch. Only the sprite and color config change — the graph-walking logic is proven and maintained.
- **No external hosting dependencies:** all assets live in the repo itself. The only external services are github-readme-stats (widely used, stable) and readme-typing-svg (same).
- **Maintenance burden:** zero after setup. GitHub Actions updates the tiger-contrib SVG daily automatically.

---

## Success Criteria

- [ ] Banner renders with animations visible on the GitHub profile page
- [ ] All 5 sections are visually cohesive (same palette, same pixel art style)
- [ ] Tiger walks on the contribution graph and updates daily
- [ ] Stats cards display real data with the tropical dark theme
- [ ] Profile loads without broken images or missing assets
