#!/usr/bin/env python3
"""
Render the first page of each highlighted paper's PDF as a PNG thumbnail,
then update data/publications.yaml with the image: path.

Usage: python3 gen_figs.py
"""
import os, shutil, yaml, fitz  # fitz = pymupdf

YAML_PATH   = "data/publications.yaml"
STATIC_ROOT = "static/static"   # maps to /static/ in Hugo
FIGS_DIR    = os.path.join(STATIC_ROOT, "pub/figs")
DPI         = 150                # resolution for thumbnail rendering

os.makedirs(FIGS_DIR, exist_ok=True)

with open(YAML_PATH) as f:
    raw = f.read()
data = yaml.safe_load(raw)

changed = False
for paper in data["papers"]:
    if not paper.get("highlight"):
        continue
    links = paper.get("links") or {}
    pdf_rel = links.get("pdf", "")
    if not pdf_rel:
        print(f"  [skip] no PDF: {paper['title'][:60]}")
        continue

    # PDF paths in YAML are Hugo-relative: "static/pub/papers/foo.pdf"
    # On disk they live under static/static/, so strip the leading "static/"
    pdf_path = os.path.join(STATIC_ROOT, pdf_rel.removeprefix("static/"))
    if not os.path.exists(pdf_path):
        print(f"  [skip] file not found: {pdf_path}")
        continue

    # Output PNG name derived from PDF basename
    base = os.path.splitext(os.path.basename(pdf_rel))[0]
    png_name = f"{base}.png"
    png_abs   = os.path.join(FIGS_DIR, png_name)
    # Hugo serves static/static/... as /static/...
    png_hugo  = f"static/pub/figs/{png_name}"

    if paper.get("image") == png_hugo and os.path.exists(png_abs):
        print(f"  [ok]   already exists: {png_name}")
        continue

    doc  = fitz.open(pdf_path)
    page = doc[0]
    mat  = fitz.Matrix(DPI / 72, DPI / 72)
    pix  = page.get_pixmap(matrix=mat, colorspace=fitz.csRGB)
    pix.save(png_abs)
    doc.close()

    paper["image"] = png_hugo
    changed = True
    print(f"  [done] {png_name}  ({paper['title'][:60]})")

if changed:
    with open(YAML_PATH, "w") as f:
        yaml.dump(data, f, allow_unicode=True, sort_keys=False, default_flow_style=False)
    print("\nUpdated data/publications.yaml")
else:
    print("\nNo changes needed.")
