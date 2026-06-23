"""
Yates "Probability and Stochastic Processes" 13개 챕터 PDF에서
각 문제(X.Y.Z 형식)를 개별 PNG으로 추출.

2단(L/R) column-aware reading-order 합성. Blocker 수정: HEADER_PT=50으로
페이지 상단 chrome("PROBLEMS NNN" / "NNN CHAPTER X TITLE")을 안전하게 제외.

출력: Probability_and_Stochastic_Processes_Problems/problems_png/<X>.<Y>.<Z>.png
"""

import os
import re
import glob
import fitz
from PIL import Image

BASE = "Probability_and_Stochastic_Processes_Problems"
SRC = os.path.join(BASE, "origin")
OUT = os.path.join(BASE, "problems_png")

DPI = 200
SCALE = DPI / 72.0
HEADER_PT = 50
FOOTER_PT = 30
TOP_PAD = 6
COL_X = 265.0
HEADER_X_RANGES = [(78, 92), (263, 277)]
TRAILER_TEXT = "The print version of the book"


def detect_chapter_num(filename):
    m = re.search(r'Chapter_(\d+)_', filename)
    return int(m.group(1)) if m else None


def find_problem_headers(doc, chapter):
    pat = re.compile(rf'^{chapter}\.\d+\.\d+$')
    out = []
    for p_idx in range(len(doc)):
        for b in doc[p_idx].get_text('dict')['blocks']:
            if 'lines' not in b:
                continue
            for ln in b['lines']:
                for sp in ln['spans']:
                    t = sp['text'].strip()
                    if not pat.fullmatch(t):
                        continue
                    x = sp['bbox'][0]
                    y = sp['bbox'][1]
                    if not any(lo <= x <= hi for lo, hi in HEADER_X_RANGES):
                        continue
                    col = 'L' if x < COL_X else 'R'
                    out.append((p_idx, col, y, t))
    out.sort(key=lambda h: (h[0], 0 if h[1] == 'L' else 1, h[2]))
    return out


def find_trailer(doc):
    for p in range(len(doc)):
        rects = doc[p].search_for(TRAILER_TEXT)
        if rects:
            return p, min(r.y0 for r in rects)
    return None


def col_x_bounds(col, page_w):
    if col == 'L':
        return (0, COL_X)
    return (COL_X, page_w)


def reading_order_units(num_pages):
    for p in range(num_pages):
        for c in ['L', 'R']:
            yield (p, c)


def build_segments(num_pages, page_heights, start, end):
    """Walk reading order from start=(p,col,y_top) to end=(p,col,y_bot).
    Returns list of (page, col, top, bot).
    """
    p_s, col_s, y_s = start
    p_e, col_e, y_e = end

    segments = []
    started = False
    for (p, c) in reading_order_units(num_pages):
        if not started:
            if (p, c) == (p_s, col_s):
                started = True
                if (p, c) == (p_e, col_e):
                    segments.append((p, c, y_s, y_e))
                    return segments
                segments.append((p, c, y_s, page_heights[p] - FOOTER_PT))
            continue
        if (p, c) == (p_e, col_e):
            segments.append((p, c, HEADER_PT, y_e))
            return segments
        segments.append((p, c, HEADER_PT, page_heights[p] - FOOTER_PT))
    return segments


def render_problem(doc, start, end):
    page_heights = [doc[i].rect.height for i in range(len(doc))]
    segments = build_segments(len(doc), page_heights, start, end)
    mat = fitz.Matrix(SCALE, SCALE)
    images = []
    for (p, c, top, bot) in segments:
        if bot - top < 2:
            continue
        page = doc[p]
        x0, x1 = col_x_bounds(c, page.rect.width)
        clip = fitz.Rect(x0, top, x1, bot)
        pix = page.get_pixmap(matrix=mat, clip=clip, colorspace=fitz.csRGB)
        img = Image.frombytes("RGB", (pix.width, pix.height), pix.samples)
        images.append(img)

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
    chapter = detect_chapter_num(fname)
    if chapter is None:
        doc.close()
        return 0

    headers = find_problem_headers(doc, chapter)
    if not headers:
        doc.close()
        return 0

    trailer = find_trailer(doc)
    if trailer is not None:
        last_p_eff, last_y_eff = trailer[0], trailer[1] - TOP_PAD
        last_col_eff = 'R'
    else:
        last_p_eff = len(doc) - 1
        last_y_eff = doc[last_p_eff].rect.height - FOOTER_PT
        last_col_eff = 'R'

    count = 0
    for i, (p, col, y, label) in enumerate(headers):
        start = (p, col, max(0, y - TOP_PAD))
        if i + 1 < len(headers):
            np_, nc_, ny_, _ = headers[i + 1]
            end = (np_, nc_, ny_ - TOP_PAD)
        else:
            end = (last_p_eff, last_col_eff, last_y_eff)
        img = render_problem(doc, start, end)
        if img is None:
            print(f"  [WARN] empty: {label}")
            continue
        img.save(os.path.join(OUT, f"{label}.png"))
        count += 1
    doc.close()
    return count


def main():
    os.makedirs(OUT, exist_ok=True)
    total = 0
    for pdf in sorted(glob.glob(os.path.join(SRC, "Chapter_*.pdf"))):
        name = os.path.basename(pdf)
        n = process_pdf(pdf)
        print(f"  {name}: {n} PNGs")
        total += n
    print(f"\nTotal: {total} PNG files in {OUT}")


if __name__ == '__main__':
    main()
