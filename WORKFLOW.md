# Website Update Workflow

This document covers the day-to-day workflow for editing the Spanish Coach website — updating screenshots, editing pages, previewing locally, and publishing to GitHub Pages.

The site is built with [MkDocs](https://www.mkdocs.org) and the [Material theme](https://squidfunk.github.io/mkdocs-material/). It's deployed automatically via GitHub Actions whenever you push to `main`.

---

## File layout

```
~/spanish-coach-website/
├── docs/
│   ├── index.md                 Home page
│   ├── screenshots.md           Screenshots gallery page
│   ├── privacy-policy.md
│   ├── support.md
│   ├── documentation/           Getting Started / Features / FAQ
│   ├── user-guide/              Deep User Guide (Verbs, Nouns, …)
│   ├── screenshots/             All screenshot PNGs live here
│   └── assets/
│       ├── css/extra.css        Custom styles
│       ├── js/nav-expand.js     Sidebar "Expand all" + page tagging
│       └── images/              App icon, App Store badge
├── mkdocs.yml                   Site config and navigation tree
├── .github/workflows/deploy.yml CI build & publish to GitHub Pages
└── WORKFLOW.md                  This file
```

---

## Updating a screenshot

The User Guide and Screenshots pages reference screenshots from a single folder: `docs/screenshots/`. To swap one out:

1. **Find the filename.** Open the page's `.md` file (under `docs/user-guide/...` or `docs/screenshots.md`) and look at the `<img src="…">`. The filename after the last `/` is the one to match.

2. **Capture a fresh screenshot.** From the iOS Simulator press `Cmd+S` (saves to Desktop), or AirDrop from a device. Aim for the same aspect ratio as the existing screenshots — iPhone portrait, about 390 × 844.

3. **Replace the file** in `docs/screenshots/` using the **exact same filename**. If you rename it, also update the `<img src="">` in the markdown.

4. **Preview locally** (see below) and force a browser refresh (`Cmd+Shift+R`) — images do not auto-reload.

5. **Commit and push.**

That's the whole process. No annotation step, no Python scripts, no label coordinates.

> **Note:** an older annotation pipeline using `annotate.py` (in the app repo) once produced numbered-overlay screenshots. It is no longer used — the User Guide pages describe UI elements by name (**Help**, **Settings**, **Select verbs**) which is enough, and the screenshots in `docs/screenshots/` are unannotated. If you ever want to point at a specific pixel-position element, the lightweight option is a tight crop of the relevant area as a separate screenshot.

---

## Editing a page

1. Find the page's markdown file under `docs/`.
2. Edit and save. `mkdocs serve` live-reloads markdown changes automatically.
3. If you add a new page, also register it in `mkdocs.yml` under `nav:`.

---

## Editing styling

Custom styles live in `docs/assets/css/extra.css`. The Material theme's CSS variables (set in the `:root` block at the top) control the colour palette site-wide.

If you change CSS, `mkdocs serve` should pick it up. If it doesn't, do a hard refresh (`Cmd+Shift+R`).

---

## Local preview

```bash
cd ~/spanish-coach-website
mkdocs serve
```

Open <http://127.0.0.1:8000/> in your browser. The server live-reloads on `.md` changes; for image and YAML front-matter changes you may need to:

- Hard refresh the browser: `Cmd+Shift+R`
- Or stop and restart `mkdocs serve` for nav-structure changes in `mkdocs.yml`

Stop the server with `Ctrl+C`.

If `mkdocs` isn't installed yet:

```bash
pip install mkdocs-material
```

---

## Publishing

GitHub Actions builds and deploys automatically on every push to `main`:

```bash
cd ~/spanish-coach-website
git add .
git commit -m "Describe what you changed"
git push origin main
```

Wait ~1–2 minutes, then check the live site at **<https://spanishcoach.nl/>**.

---

## Quick reference

| Task | Command |
|---|---|
| Start local preview | `cd ~/spanish-coach-website && mkdocs serve` |
| Force browser refresh | `Cmd+Shift+R` |
| Restart preview (nav changes) | `Ctrl+C`, then `mkdocs serve` |
| Commit and push | `git add . && git commit -m "…" && git push origin main` |
| Live site | <https://spanishcoach.nl/> |

---

## File locations

| What | Where |
|---|---|
| Screenshots | `docs/screenshots/` |
| User Guide pages | `docs/user-guide/` |
| Documentation pages | `docs/documentation/` |
| Custom CSS | `docs/assets/css/extra.css` |
| Custom JS | `docs/assets/js/nav-expand.js` |
| App icon / App Store badge | `docs/assets/images/` |
| Site config & nav | `mkdocs.yml` |
| Deploy workflow | `.github/workflows/deploy.yml` |
