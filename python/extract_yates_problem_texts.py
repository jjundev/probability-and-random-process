"""
Yates 문제 분류용 텍스트 추출. PNG 추출과 동일한 헤더 탐지 + 세그먼트 로직 재사용.
column-clipped reading-order 텍스트.

출력: Probability_and_Stochastic_Processes_Problems/problem_texts.json
"""

import os
import json
import glob
import fitz

from extract_yates_problems import (
    BASE, SRC, HEADER_PT, FOOTER_PT, TOP_PAD, COL_X,
    detect_chapter_num, find_problem_headers, find_trailer,
    col_x_bounds, build_segments,
)

PNG_DIR = os.path.join(BASE, "problems_png")
OUT = os.path.join(BASE, "problem_texts.json")


def extract_segment_text(doc, p, col, top, bot):
    page = doc[p]
    x0, x1 = col_x_bounds(col, page.rect.width)
    lines = []
    for b in page.get_text('dict')['blocks']:
        if 'lines' not in b:
            continue
        for ln in b['lines']:
            spans = ln['spans']
            if not spans:
                continue
            ly = min(sp['bbox'][1] for sp in spans)
            lx = min(sp['bbox'][0] for sp in spans)
            if not (top <= ly <= bot):
                continue
            if not (x0 <= lx < x1):
                continue
            sorted_spans = sorted(spans, key=lambda s: s['bbox'][0])
            line_text = ''.join(s['text'] for s in sorted_spans).strip()
            if line_text:
                lines.append((ly, lx, line_text))
    lines.sort(key=lambda t: (round(t[0], 1), t[1]))
    return '\n'.join(l[2] for l in lines)


def extract_problem_text(doc, start, end):
    page_heights = [doc[i].rect.height for i in range(len(doc))]
    segs = build_segments(len(doc), page_heights, start, end)
    parts = []
    for (p, c, top, bot) in segs:
        if bot - top < 2:
            continue
        t = extract_segment_text(doc, p, c, top, bot).strip()
        if t:
            parts.append(t)
    return '\n\n'.join(parts)


def process_pdf(pdf_path, out):
    doc = fitz.open(pdf_path)
    fname = os.path.basename(pdf_path)
    chapter = detect_chapter_num(fname)
    if chapter is None:
        doc.close()
        return

    headers = find_problem_headers(doc, chapter)
    if not headers:
        doc.close()
        return

    trailer = find_trailer(doc)
    if trailer is not None:
        last_p_eff, last_y_eff = trailer[0], trailer[1] - TOP_PAD
        last_col_eff = 'R'
    else:
        last_p_eff = len(doc) - 1
        last_y_eff = doc[last_p_eff].rect.height - FOOTER_PT
        last_col_eff = 'R'

    for i, (p, col, y, label) in enumerate(headers):
        start = (p, col, max(0, y - TOP_PAD))
        if i + 1 < len(headers):
            np_, nc_, ny_, _ = headers[i + 1]
            end = (np_, nc_, ny_ - TOP_PAD)
        else:
            end = (last_p_eff, last_col_eff, last_y_eff)
        txt = extract_problem_text(doc, start, end)
        out[label] = {
            "text": txt,
            "png": os.path.join(PNG_DIR, f"{label}.png").replace("\\", "/"),
        }
    doc.close()


def main():
    out = {}
    for pdf in sorted(glob.glob(os.path.join(SRC, "Chapter_*.pdf"))):
        print(f"  Processing {os.path.basename(pdf)}...")
        process_pdf(pdf, out)
    with open(OUT, 'w', encoding='utf-8') as f:
        json.dump(out, f, ensure_ascii=False, indent=2)
    print(f"\nTotal: {len(out)} problem texts in {OUT}")


if __name__ == '__main__':
    main()
