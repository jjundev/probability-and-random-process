"""
02_Conditioning_Bayes_Independence.pdf 의 정제판을 만든다.

원본은 Ch1 pages 2-5 (1.3.5+ 1.4 + 1.5 + 1.6 + 1.7) + Ch2 pages 0-2, 4 (2.1, 2.4) (~36문제).
유사 유형은 묶고, Easy 대표 + Moderate 위주 + Difficult 약간으로 정제.

출력: problems/02_Conditioning_Bayes_Independence_Refined.pdf
"""

import os
import re
import fitz

BASE = "Probability_and_Stochastic_Processes_Problems/"
CH1 = BASE + "Chapter_01_Problems_pages_47-52.pdf"
CH2 = BASE + "Chapter_02_Problems_pages_75-79.pdf"
OUT = "problems/02_Conditioning_Bayes_Independence_Refined.pdf"

COL = 265.0
TOP_Y = 50
WHITE = (1, 1, 1)

KEEP_CH1 = {
    # 1.4 Conditional probability
    '1.4.1',                     # 핸드오프 표 conditional (Easy 대표)
    '1.4.5',                     # Mendel 콩 유전 (Moderate 대표)
    '1.4.8',                     # Lyme/HGE 진드기 (Difficult)
    # 1.5 Total prob / Bayes
    '1.5.2',                     # 통화요금 geometric (Easy 대표)
    '1.5.3',                     # 셀룰러 표 채우기 (Difficult)
    # 1.6 Independence
    '1.6.2',                     # 등확률+ME+독립 (Easy 대표)
    '1.6.5',                     # A,B 상호배반 (Moderate 대표)
    '1.6.9',                     # pairwise vs full 독립 (Moderate 핵심개념)
    '1.6.11',                    # (A^c, B) 독립 증명 (Difficult)
}

KEEP_CH2 = {
    # 2.1 Sequential / Bayes
    '2.1.3',                     # 자유투 OT 트리 (Easy 대표)
    '2.1.5',                     # HIV 검사 Bayes (Moderate 고전)
    '2.1.8',                     # 심장 결손 Bayes 5파트 (Moderate)
    '2.1.11',                    # Strogatz 식물 (Moderate 직관)
    '2.1.12',                    # 어부 geometric 트리 (Moderate)
    # 2.4 Reliability
    '2.4.1',                     # 6-component 시스템 P[W] (Moderate 대표)
    '2.4.2',                     # 셀룰러 코딩 error/deletion (Moderate)
    '2.4.4',                     # 2.4.1 follow-up (Difficult)
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

    # Ch1 pages 2-5: 1.3.5+, 1.4, 1.5, 1.6, 1.7
    d1 = fitz.open(CH1)
    process_chapter(d1, [2, 3, 4, 5], KEEP_CH1, '1', has_prior_excluded_pages=True)
    out.insert_pdf(d1, from_page=2, to_page=5)
    d1.close()

    # Ch2 pages 0-2 (2.1, 2.2 dropped) + page 4 (2.4)
    d2 = fitz.open(CH2)
    strip_chapter_intro(d2[0])
    process_chapter(d2, [0, 1, 2], KEEP_CH2, '2', has_prior_excluded_pages=False)
    process_chapter(d2, [4], KEEP_CH2, '2', has_prior_excluded_pages=True)
    out.insert_pdf(d2, from_page=0, to_page=2)
    out.insert_pdf(d2, from_page=4, to_page=4)
    d2.close()

    out_path = _resolve_out_path(OUT)
    out.save(out_path, garbage=4, deflate=True)
    out.close()

    d = fitz.open(out_path)
    print(f"Wrote {out_path} ({len(d)} pages, {os.path.getsize(out_path)//1024}KB)")
    d.close()


if __name__ == '__main__':
    main()
