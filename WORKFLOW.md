# Website Update Workflow

This document describes the end-to-end process for updating the Spanish Coach website — from new screenshots through local testing to publishing on GitHub Pages.

---

## Overview

```
New screenshots
      ↓
Update annotate.py
      ↓
Run annotate.py  →  annotated images in docs/assets/images/guide/
      ↓
Update user guide pages (if needed)
      ↓
Test locally with mkdocs serve
      ↓
Commit & push → GitHub Actions rebuilds the site
```

---

## Step 1 — Add new screenshots

Place screenshots in the correct folder under:

```
~/Documents/spanish-coach-website/Screenshots/
```

Follow the existing folder structure, for example:

```
Screenshots/
  Spanish Coach.png
  Spanish Coach/
    Self Study/
      Self Study.png
      Verbs/
        Verbs Coach.png
        Setup/
          Select verbs/
            ...
```

---

## Step 2 — Update annotate.py

Open:

```
/Users/hans/Xcode/Spanish Coach/UtilitiesForSpanishCoach/src/Pictures/annotate.py
```

**If adding a new screen**, add an entry to both `FILES` and `ANNOTATIONS`:

```python
# In FILES:
"my-new-screen":
    "Spanish Coach/Path/To/Screenshot.png",

# In ANNOTATIONS:
"my-new-screen": [
    (0.08, 0.200, 1),   # describe what this points to
    (0.92, 0.200, 2),   # describe what this points to
],
```

**If a screenshot moved**, update the path in `FILES`.

### Finding the right label positions

Use the interactive label placer:

1. Open in your browser:
   ```
   /Users/hans/Xcode/Spanish Coach/UtilitiesForSpanishCoach/src/Pictures/label-placer.html
   ```
2. Load the screenshot
3. Click to place numbered labels
4. Copy the output and paste it into the `ANNOTATIONS` dict in `annotate.py`

---

## Step 3 — Run annotate.py

In Terminal:

```bash
cd "/Users/hans/Xcode/Spanish Coach/UtilitiesForSpanishCoach/src/Pictures"
.venv/bin/python annotate.py
```

Annotated images are written to:

```
~/Documents/spanish-coach-website/docs/assets/images/guide/
```

The script prints `✓ filename.png` for each success and `✗ MISSING: path` for any source file it cannot find.

---

## Step 4 — Update the user guide (if needed)

User guide pages live in:

```
~/Documents/spanish-coach-website/docs/user-guide/
```

If you added a new screen or changed label positions/count, update the corresponding `.md` file:

- The `<img src="...">` tag should reference the correct output filename
- The numbered list must match the labels in the image (same count, same order)

If you added a brand new page, also add it to the `nav:` section in `mkdocs.yml`.

---

## Step 5 — Test locally

Start the local preview server:

```bash
cd ~/Documents/spanish-coach-website
mkdocs serve
```

Open your browser at **http://127.0.0.1:8000/spanish-coach-website/**

The server live-reloads when you save any `.md` file. Images do **not** live-reload automatically — do **Cmd + Shift + R** in the browser after running `annotate.py` to force a refresh.

Stop the server with **Ctrl + C**.

---

## Step 6 — Commit and push to GitHub

When everything looks good locally:

```bash
cd ~/Documents/spanish-coach-website

# Stage everything
git add .

# Commit with a descriptive message
git commit -m "Describe what you changed"

# Push
git push origin main
```

GitHub Actions will automatically rebuild and deploy the site. Allow about 1–2 minutes, then check the live site at:

**https://jjabakker.github.io/spanish-coach-website/**

---

## Quick reference

| Task | Command |
|---|---|
| Run annotation script | `cd "/Users/hans/Xcode/Spanish Coach/UtilitiesForSpanishCoach/src/Pictures" && .venv/bin/python annotate.py` |
| Start local preview | `cd ~/Documents/spanish-coach-website && mkdocs serve` |
| Force browser refresh | **Cmd + Shift + R** |
| Commit and push | `git add . && git commit -m "message" && git push origin main` |
| Label placer tool | Open `label-placer.html` in browser |

---

## File locations

| What | Where |
|---|---|
| Source screenshots | `~/Documents/spanish-coach-website/Screenshots/` |
| Annotated output images | `~/Documents/spanish-coach-website/docs/assets/images/guide/` |
| User guide pages | `~/Documents/spanish-coach-website/docs/user-guide/` |
| Annotation script | `~/Xcode/Spanish Coach/UtilitiesForSpanishCoach/src/Pictures/annotate.py` |
| Label placer | `~/Xcode/Spanish Coach/UtilitiesForSpanishCoach/src/Pictures/label-placer.html` |
| Site config | `~/Documents/spanish-coach-website/mkdocs.yml` |
