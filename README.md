# Spanish Coach — App Website

This is the source for the [Spanish Coach](https://jjabakker.github.io/spanish-coach-website/) website, built with [MkDocs](https://www.mkdocs.org) and the [Material theme](https://squidfunk.github.io/mkdocs-material/).

---

## Getting the Site Live (Step-by-Step)

### Step 1 — Create a GitHub repo

1. Go to [github.com/new](https://github.com/new)
2. Name it `spanish-coach-website`
3. Set it to **Public** (required for free GitHub Pages)
4. Click **Create repository**

### Step 2 — Update your details in mkdocs.yml

Open `mkdocs.yml` and replace every `jjabakker` placeholder with your actual GitHub username, and `6764284291` with your App Store app ID.

### Step 3 — Push the project to GitHub

```bash
cd spanish-coach-website
git init
git add .
git commit -m "Initial website"
git branch -M main
git remote add origin https://github.com/jjabakker/spanish-coach-website.git
git push -u origin main
```

### Step 4 — Enable GitHub Pages

1. In your GitHub repo, go to **Settings → Pages**
2. Under **Source**, select **Deploy from a branch**
3. Set the branch to **gh-pages** and folder to **/ (root)**
4. Click **Save**

The GitHub Actions workflow will automatically build and deploy the site every time you push to `main`. Your site will be live at:

```
https://jjabakker.github.io/spanish-coach-website/
```

---

## Adding Your Screenshots

1. Place your screenshot images in `docs/assets/images/screenshots/`
2. Recommended format: PNG, 390 × 844 px (iPhone 14 portrait)
3. Name them to match the paths in `docs/screenshots.md` (e.g. `screenshot-home.png`)

## Adding Your App Icon

Place your app icon at `docs/assets/images/app-icon.png` (512 × 512 px recommended).

## Embedding Your Video

In `docs/index.md`, replace `YOUR-VIDEO-ID` in the iframe `src` with your YouTube video ID. For a Vimeo video, use `https://player.vimeo.com/video/YOUR-VIDEO-ID`.

---

## Running Locally

```bash
pip install mkdocs-material
mkdocs serve
```

Then open [http://localhost:8000](http://localhost:8000) in your browser.

---

## Pages Checklist (App Store Requirements)

- [x] **Privacy Policy** — `docs/privacy-policy.md` ✅
- [x] **Support page** — `docs/support.md` ✅
- [x] Screenshots — `docs/screenshots.md`
- [x] Video embed — `docs/index.md`
- [x] Documentation — `docs/documentation/`

> Remember to update the Privacy Policy with your real contact details and mailing address before submitting to the App Store.
