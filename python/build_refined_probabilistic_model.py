"""
01_Probabilistic_Model.pdf 의 정제판을 만든다.

원본은 Ch1 pages 0-2 (~22문제).
유사 유형은 묶고, Easy 대표 + Moderate + Difficult 약간으로 정제.

출력: problems/01_Probabilistic_Model_Refined.pdf
"""

import os
import re
import fitz

BASE = "Probability_and_Stochastic_Processes_Problems/"
CH1 = BASE + "Chapter_01_Problems_pages_47-52.pdf"
OUT = "problems/01_Probabilistic_Model_Refined.pdf"

COL = 265.0
TOP_Y = 50
WHITE = (1, 1, 1)

KEEP_CH1 = {
    '1.1.3',                     # Ricardo's pizza Venn (Easy 대표 — Quiz 의존 X)
    '1.2.2',                     # IC factory sample space + 다양 events (Easy 대표)
    '1.3.1',                     # P[B] 3 cases (Easy — 공리 기본)
    '1.3.2',                     # 두 dice joint events (Easy)
    '1.3.4',                     # T/F 개념 (Easy)
    '1.3.5',                     # 컴퓨터 프로그램 BF/LW (Easy 대표 — drop 1.3.6 유사)
    '1.3.10',                    # P[A∪B] 부등식 증명 (Moderate)
    '1.3.11',                    # union bound 귀납 증명 (Moderate)
    '1.3.12',                    # P[∅]=0 증명 (Difficult)
}


def redact(page, x0, y0, x1, y1):
    rect = fitz.Rect(x0, y0, x1, y1) & page.rect
    if not rect.is_empty:
        page.add_redact_annot(rect, fill=WHITE)


def get_headers(page, prefix):
    pat = re.compile(r'^(' + re.escape(prefix) + r'\.\d+\.\d+)')
    blocks = page.get_text('dict')['blocks']
    out = []
    for b in blocks:
        if 'lines' not in b:
            continue
        for ln in b['lines']:
            for sp in ln['spans']:
                t = sp['text'].strip()
                m = pat.match(t)
                if not m:
                    continue
                x = sp['bbox'][0]
                if 80 <= x <= 90 or 265 <= x <= 275:
                    out.append((m.group(1), x, sp['bbox'][1]))
    return out


def split_columns(headers):
    L = sorted([(n, y) for (n, x, y) in headers if x < COL], key=lambda t: t[1])
    R = sorted([(n, y) for (n, x, y) in headers if x >= COL], key=lambda t: t[1])
    return L, R


def strip_chapter_intro(page):
    """페이지의 'Problems' 섹션 헤더 위쪽(챕터 본문 잔재)만 redact, 페이지 chrome 보존."""
    # 'PROBLEMS' 페이지 chrome (y≈40) 와 'Problems' 섹션 헤더 둘 다 매치되므로
    # body 영역(y > TOP_Y)의 첫 번째 매치만 채택
    rects = [r for r in page.search_for("Problems") if r.y0 > TOP_Y]
    if not rects:
        return
    hy = min(r.y0 for r in rects)
    redact(page, 0, TOP_Y, page.rect.width, hy - 6)
    page.apply_redactions()


def process_chapter(d, page_indices, keep_set, prefix, has_prior_excluded_pages):
    cols_info = {}
    for p in page_indices:
        page = d[p]
        L, R = split_columns(get_headers(page, prefix))
        cols_info[(p, 'L')] = L
        cols_info[(p, 'R')] = R

    reading_order = [(p, col) for p in page_indices for col in ['L', 'R']]
    prev_col_last = {}
    last = '__EXCLUDED__' if has_prior_excluded_pages else None
    for key in reading_order:
        prev_col_last[key] = last
        items = cols_info[key]
        if items:
            last = items[-1][0]

    for p in page_indices:
        page = d[p]
        for col in ['L', 'R']:
            x0 = 0 if col == 'L' else COL
            x1 = COL if col == 'L' else page.rect.width
            items = cols_info[(p, col)]
            prev_p = prev_col_last[(p, col)]

            top_end = items[0][1] - 6 if items else page.rect.height
            if prev_p is not None and prev_p not in keep_set:
                redact(page, x0, TOP_Y, x1, top_end)

            for i, (name, y) in enumerate(items):
                if name not in keep_set:
                    y_end = items[i + 1][1] - 6 if i + 1 < len(items) else page.rect.height
                    redact(page, x0, y - 6, x1, y_end)

        page.apply_redactions()


def _resolve_out_path(path):
    if not os.path.exists(path):
        return path
    try:
        with open(path, 'r+b'):
            return path
    except (PermissionError, OSError):
        base, ext = os.path.splitext(path)
        i = 1
        while True:
            cand = f"{base} ({i}){ext}"
            if not os.path.exists(cand):
                return cand
            try:
                with open(cand, 'r+b'):
                    return cand
            except (PermissionError, OSError):
                i += 1


def main():
    os.makedirs(os.path.dirname(OUT), exist_ok=True)
    out = fitz.open()

    d = fitz.open(CH1)
    strip_chapter_intro(d[0])
    process_chapter(d, [0, 1, 2], KEEP_CH1, '1', has_prior_excluded_pages=False)
    out.insert_pdf(d, from_page=0, to_page=2)
    d.close()

    out_path = _resolve_out_path(OUT)
    out.save(out_path, garbage=4, deflate=True)
    out.close()

    d = fitz.open(out_path)
    print(f"Wrote {out_path} ({len(d)} pages, {os.path.getsize(out_path)//1024}KB)")
    d.close()


if __name__ == '__main__':
    main()
