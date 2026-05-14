#!/usr/bin/env python3
"""
Spanish Coach — Screenshot Annotation Script
Usage: python3 annotate.py
Reads screenshots from INPUT_DIR, adds callout circles, saves to OUTPUT_DIR.
Edit the ANNOTATIONS dict below to configure callouts for each screenshot.
"""

from PIL import Image, ImageDraw, ImageFont
import os

INPUT_DIR = os.path.expanduser("~/Desktop/Spanish Coach Screenshots")
OUTPUT_DIR = os.path.join(os.path.dirname(__file__), "docs/assets/images/guide")

# ── Annotation definitions ────────────────────────────────────────────────────
# Each entry: "filename" -> list of (x, y, label, number)
# x, y are as fractions of image width/height (0.0–1.0) so they work at any resolution
# label is shown in the legend on the page (not on the image)
# number is the callout circle number

ANNOTATIONS = {
    "Spanish Coach Main Screen.png": [
        (0.12, 0.09, "Progress & statistics",        1),
        (0.22, 0.09, "Learning history",             2),
        (0.78, 0.09, "Settings",                     3),
        (0.88, 0.09, "Reference library",            4),
        (0.50, 0.30, "Self Study — tap to enter",    5),
        (0.50, 0.44, "Guided Lessons — tap to enter",6),
    ],
    "Self Study Screen.png": [
        (0.12, 0.07, "Back to main screen",          1),
        (0.88, 0.07, "Settings",                     2),
        (0.50, 0.23, "Verbs — conjugation practice", 3),
        (0.50, 0.40, "Nouns — articles and forms",   4),
        (0.50, 0.57, "Words & Phrases",              5),
    ],
    "Verbs Coach Screen.png": [
        (0.85, 0.07, "Help",                         1),
        (0.95, 0.07, "Settings",                     2),
        (0.50, 0.18, "Select verbs — filter your verb set",    3),
        (0.50, 0.25, "Select tenses — choose which tenses to practise", 4),
        (0.50, 0.37, "Conjugation tables — browse all forms",  5),
        (0.50, 0.44, "Word meanings — translations and definitions", 6),
        (0.50, 0.54, "Word Meanings test",           7),
        (0.50, 0.61, "Conjugation drill",            8),
        (0.50, 0.68, "Recognition test",             9),
        (0.50, 0.75, "Past participle (Participio)", 10),
        (0.50, 0.82, "Gerund (Gerundio)",            11),
        (0.50, 0.89, "Preterite (Indefinido)",       12),
    ],
    "Select Verbs - Criteria.png": [
        (0.27, 0.15, "Criteria tab — filter by level, frequency, scenario", 1),
        (0.72, 0.15, "Verb Groups tab — select by named group",             2),
        (0.50, 0.30, "CEFR Level — tap to set A1–C2 levels",               3),
        (0.50, 0.42, "Frequency — tap to set how common the verbs are",     4),
        (0.50, 0.54, "Scenario — tap to filter by topic",                   5),
        (0.50, 0.66, "Matching — shows how many verbs match your filters",  6),
    ],
    "Select Verbs - Scenario selection.png": [
        (0.50, 0.10, "Total verbs in this category",  1),
        (0.88, 0.17, "None — tap to deselect all",    2),
        (0.88, 0.25, "Tap a checkbox to toggle a scenario on/off", 3),
    ],
    "Select Verbs - Overview of selected verbs.png": [
        (0.50, 0.10, "Search — type to filter the verb list", 1),
        (0.94, 0.50, "Alphabetical index — tap a letter to jump", 2),
        (0.50, 0.40, "Verb list with English translations",      3),
    ],
}

# ── Drawing settings ──────────────────────────────────────────────────────────
CIRCLE_RADIUS_FRAC = 0.028   # fraction of image width
FONT_SIZE_FRAC     = 0.022
BG_COLOR           = (255, 80, 0, 230)    # orange
TEXT_COLOR         = (255, 255, 255, 255) # white
BORDER_COLOR       = (255, 255, 255, 200)
BORDER_WIDTH       = 2

def annotate(img_path, callouts, out_path):
    img = Image.open(img_path).convert("RGBA")
    w, h = img.size
    overlay = Image.new("RGBA", img.size, (0, 0, 0, 0))
    draw = ImageDraw.Draw(overlay)

    r = int(w * CIRCLE_RADIUS_FRAC)
    font_size = max(16, int(w * FONT_SIZE_FRAC))

    try:
        font = ImageFont.truetype("/System/Library/Fonts/Helvetica.ttc", font_size)
    except Exception:
        font = ImageFont.load_default()

    for (fx, fy, label, num) in callouts:
        cx = int(fx * w)
        cy = int(fy * h)
        # filled circle
        draw.ellipse([cx-r, cy-r, cx+r, cy+r], fill=BG_COLOR)
        # border
        draw.ellipse([cx-r, cy-r, cx+r, cy+r], outline=BORDER_COLOR, width=BORDER_WIDTH)
        # number
        text = str(num)
        bbox = draw.textbbox((0, 0), text, font=font)
        tw = bbox[2] - bbox[0]
        th = bbox[3] - bbox[1]
        draw.text((cx - tw/2, cy - th/2 - bbox[1]), text, fill=TEXT_COLOR, font=font)

    composite = Image.alpha_composite(img, overlay).convert("RGB")
    composite.save(out_path, "PNG")
    print(f"  ✓ {os.path.basename(out_path)}")

def main():
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    for filename, callouts in ANNOTATIONS.items():
        src = os.path.join(INPUT_DIR, filename)
        if not os.path.exists(src):
            print(f"  ⚠ Not found: {filename}")
            continue
        # slugify filename for output
        slug = filename.lower().replace(" ", "-").replace(".", "-").rstrip("-png") + ".png"
        dst = os.path.join(OUTPUT_DIR, slug)
        annotate(src, callouts, dst)
    print(f"\nDone — annotated images saved to:\n  {OUTPUT_DIR}")

if __name__ == "__main__":
    main()
