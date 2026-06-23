"""
Pishro-Nik 교재 "Introduction to Probability, Statistics, and Random Processes"
의 5개 챕터 PDF(3/4/5/6/7장)에서 각 End-of-Chapter Problem을 개별 PNG으로 추출.

설계: grill-yourself + grill-review 결과 반영 (Blocker 3건 + Advisory 3건 모두 반영).
출력: Introduction to Probability, Statistics, and Random Processes/problems_png/<sec>.<n>.png
"""

import os
import re
import glob
import fitz
from PIL import Image

BASE = "Introduction to Probability, Statistics, and Random Processes"
SRC = os.path.join(BASE, "origin")
OUT = os.path.join(BASE, "problems_png")

DPI = 200
SCALE = DPI / 72.0
HEADER_PT = 25
FOOTER_PT = 30
TOP_PAD = 6

SECTION_RE = re.compile(r'(\d+(?:\.\d+)+)\s+(?:End of\s+)?Chapter Problems')
PROBLEM_RE = re.compile(r'^Problem\s+(\d+)$')
TRAILER_TEXT = "The print version of the book"


def find_section_prefix(doc):
    for p_idx in range(len(doc)):
        m = SECTION_RE.search(doc[p_idx].get_text())
        if m:
            return m.group(1)
    return None


def find_problem_headers(doc):
    out = []
    for p_idx in range(len(doc)):
        page = doc[p_idx]
        for b in page.get_text('dict')['blocks']:
            if 'lines' not in b:
                continue
            for ln in b['lines']:
                for sp in ln['spans']:
                    t = sp['text'].strip()
                    m = PROBLEM_RE.fullmatch(t)
                    if m:
                        out.append((p_idx, sp['bbox'][1], int(m.group(1))))
    out.sort(key=lambda x: (x[0], x[1]))
    return out


def find_trailer(doc):
    for p_idx in range(len(doc)):
        rects = doc[p_idx].search_for(TRAILER_TEXT)
        if rects:
            y = min(r.y0 for r in rects)
            return p_idx, y
    return None


def normalize_prefix(prefix):
    return prefix[:-2] if prefix.endswith(".0") else prefix


def render_region(doc, p_start, y_start, p_end, y_end):
    mat = fitz.Matrix(SCALE, SCALE)
    images = []
    p = p_start
    while p <= p_end:
        page = doc[p]
        W, H = page.rect.width, page.rect.height
        if p == p_start and p == p_end:
            top, bot = y_start, y_end
        elif p == p_start:
            top, bot = y_start, H - FOOTER_PT
        elif p == p_end:
            if y_end <= HEADER_PT + TOP_PAD:
                p += 1
                continue
            top, bot = HEADER_PT, y_end
        else:
            top, bot = HEADER_PT, H - FOOTER_PT

        if bot - top < 2:
            p += 1
            continue

        clip = fitz.Rect(0, top, W, bot)
        pix = page.get_pixmap(matrix=mat, clip=clip, colorspace=fitz.csRGB)
        img = Image.frombytes("RGB", (pix.width, pix.height), pix.samples)
        images.append(img)
        p += 1

    if not images:
        return None

    canvas_w = max(im.width for im in images)
    canvas_h = sum(im.height for im in images)
    canvas = Image.new("RGB", (canvas_w, canvas_h), (255, 255, 255))
    y = 0
    for im in images:
        x = (canvas_w - im.width) // 2
        canvas.paste(im, (x, y))
        y += im.height
    return canvas


def process_pdf(pdf_path):
    doc = fitz.open(pdf_path)
    fname = os.path.basename(pdf_path)
    prefix = find_section_prefix(doc)
    if prefix is None:
        print(f"  [SKIP] no section heading: {fname}")
        doc.close()
        return 0

    headers = find_problem_headers(doc)
    if not headers:
        print(f"  [SKIP] no Problem headers: {fname}")
        doc.close()
        return 0

    trailer = find_trailer(doc)
    if trailer is not None:
        last_p_eff, last_y_eff = trailer[0], trailer[1] - TOP_PAD
    else:
        last_p_eff = len(doc) - 1
        last_y_eff = doc[last_p_eff].rect.height - FOOTER_PT

    name_prefix = normalize_prefix(prefix)
    count = 0
    for i, (p, y, n) in enumerate(headers):
        y_start = max(0, y - TOP_PAD)
        if i + 1 < len(headers):
            p_end = headers[i + 1][0]
            y_end = headers[i + 1][1] - TOP_PAD
        else:
            p_end = last_p_eff
            y_end = last_y_eff

        img = render_region(doc, p, y_start, p_end, y_end)
        if img is None:
            print(f"  [WARN] empty render: {name_prefix}.{n}")
            continue
        out_path = os.path.join(OUT, f"{name_prefix}.{n}.png")
        img.save(out_path)
        count += 1

    doc.close()
    return count


def main():
    os.makedirs(OUT, exist_ok=True)
    total = 0
    for pdf in sorted(glob.glob(os.path.join(SRC, "*.pdf"))):
        print(f"Processing {os.path.basename(pdf)}...")
        n = process_pdf(pdf)
        print(f"  -> {n} PNGs")
        total += n
    print(f"\nTotal: {total} PNG files in {OUT}")


if __name__ == '__main__':
    main()
