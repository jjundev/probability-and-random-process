"""
03_Discrete_RV.pdf 의 정제판을 만든다.

원본은 Ch2(일부) + Ch3(전체) + Ch5(일부) 의 모든 풀이가능 문제를 포함 (~80문제).
유사 유형은 묶고, Easy 대표 + Moderate 위주 + Difficult 약간으로 ~38문제만 남긴다.

출력: problems/03_Discrete_RV_Refined.pdf
"""

import os
import re
import fitz

BASE = "Probability_and_Stochastic_Processes_Problems/"
CH2 = BASE + "Chapter_02_Problems_pages_75-79.pdf"
CH3 = BASE + "Chapter_03_Problems_pages_124-135.pdf"
CH5 = BASE + "Chapter_05_Problems_pages_224-235.pdf"
OUT = "problems/03_Discrete_RV_Refined.pdf"


def _resolve_out_path(path):
    """파일이 잠겨있으면 (1), (2)... 접미사를 붙여 새 경로 반환."""
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

COL = 265.0
TOP_Y = 50  # 페이지 헤더(번호·챕터명, y≈40) 위 보존
WHITE = (1, 1, 1)

KEEP_CH2 = {'2.2.2', '2.3.4', '2.3.5'}

KEEP_CH3 = {
    '3.2.2', '3.2.4', '3.2.5', '3.2.7', '3.2.11',
    '3.3.1', '3.3.2', '3.3.6', '3.3.9',
    '3.3.13', '3.3.14', '3.3.16', '3.3.18',
    '3.4.1', '3.4.2', '3.4.5',
    '3.5.4', '3.5.12', '3.5.14', '3.5.15', '3.5.16', '3.5.21',
    '3.6.1', '3.6.4', '3.6.5',
    '3.7.5', '3.7.6', '3.7.9',
    '3.8.1', '3.8.5', '3.8.8',
}

KEEP_CH5 = {'5.2.1', '5.2.3', '5.2.7', '5.3.1', '5.3.4'}


def redact(page, x0, y0, x1, y1):
    rect = fitz.Rect(x0, y0, x1, y1) & page.rect
    if not rect.is_empty:
        page.add_redact_annot(rect, fill=WHITE)


def get_headers(page, prefix):
    """문제 헤더(예: '3.2.5')를 (name, x, y) 형태로 반환. 좌/우 단의 margin x만 채택해 본문 인용을 걸러냄."""
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
    """페이지의 'Problems' 헤더 위쪽(챕터 본문 잔재)만 redact, 페이지 chrome(번호·제목)은 보존."""
    rects = page.search_for("Problems")
    if not rects:
        return
    hy = min(r.y0 for r in rects)
    redact(page, 0, TOP_Y, page.rect.width, hy - 6)
    page.apply_redactions()


def process_chapter(d, page_indices, keep_set, prefix, has_prior_excluded_pages):
    """해당 챕터의 page_indices 페이지에 대해 keep_set 외 문제를 redact.
    has_prior_excluded_pages=True 면 이전(제외된) 페이지에서 넘어온 overflow 가
    있을 가능성을 가정하여 첫 컬럼의 위 영역을 redact 한다.
    """
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


def main():
    os.makedirs(os.path.dirname(OUT), exist_ok=True)
    out = fitz.open()

    d2 = fitz.open(CH2)
    process_chapter(d2, [2, 3], KEEP_CH2, '2', has_prior_excluded_pages=True)
    out.insert_pdf(d2, from_page=2, to_page=3)
    d2.close()

    d3 = fitz.open(CH3)
    strip_chapter_intro(d3[0])
    process_chapter(d3, list(range(0, 11)), KEEP_CH3, '3', has_prior_excluded_pages=False)
    out.insert_pdf(d3, from_page=0, to_page=10)
    d3.close()

    d5 = fitz.open(CH5)
    process_chapter(d5, [1, 2], KEEP_CH5, '5', has_prior_excluded_pages=True)
    out.insert_pdf(d5, from_page=1, to_page=2)
    d5.close()

    out_path = _resolve_out_path(OUT)
    out.save(out_path, garbage=4, deflate=True)
    out.close()

    d = fitz.open(out_path)
    print(f"Wrote {out_path} ({len(d)} pages, {os.path.getsize(out_path)//1024}KB)")
    d.close()


if __name__ == '__main__':
    main()
