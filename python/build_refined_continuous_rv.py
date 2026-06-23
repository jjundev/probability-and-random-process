"""
04_Continuous_RV.pdf 의 정제판을 만든다.

원본은 Ch4 pages 0-6 (Erlang/Mixed/MATLAB 제외 ~50문제).
유사 유형은 묶고, Easy 대표 + Moderate 위주 + Difficult 약간으로 정제.

출력: problems/04_Continuous_RV_Refined.pdf
"""

import os
import re
import fitz

BASE = "Probability_and_Stochastic_Processes_Problems/"
CH4 = BASE + "Chapter_04_Problems_pages_172-179.pdf"
OUT = "problems/04_Continuous_RV_Refined.pdf"

COL = 265.0
TOP_Y = 50
WHITE = (1, 1, 1)

KEEP_CH4 = {
    # 4.2 CDF
    '4.2.4',                     # multi-piece CDF W (Easy 대표 — drop 4.2.1/2 단순, 4.2.3 이론)
    # 4.3 PDF
    '4.3.1',                     # PDF cx → c, P, CDF (Easy 대표 — drop 4.3.2/3 follow-up)
    '4.3.4',                     # Rayleigh PDF → CDF (Moderate)
    # 4.4 E[X], Var, function of RV
    '4.4.1',                     # PDF 1/4 + Y=X² (Easy 대표 — h(E)/E[h], drop 4.4.2 유사)
    '4.4.6',                     # CDF (v+5)²/144 → E, Var, E[V³] (Moderate)
    # 4.5 Uniform / Exponential
    '4.5.2',                     # 저항기 전류 uniform (Easy 대표 — drop 4.5.1)
    '4.5.3',                     # 레이더 exponential (Easy 대표 — drop 4.5.4/5)
    '4.5.10',                    # uniform (-5,5) full PDF/CDF/moments (Moderate 종합)
    '4.5.13',                    # exponential PDF (Moderate 종합)
    '4.5.15',                    # 통화요금 plan A vs B exponential (Moderate 응용)
    '4.5.19',                    # E[X^n] = n!/λ^n 귀납 증명 (Difficult)
    # 4.6 Gaussian
    '4.6.1',                     # July NJ Gaussian (Easy 대표 — Q-table 기본)
    '4.6.3',                     # 다양한 Gaussian P (Easy — multi-case)
    '4.6.4',                     # μ inverse from condition (Easy — 거꾸로)
    '4.6.10',                    # 교수 chalkboard error Gaussian (Moderate)
    '4.6.11',                    # US 키 7'6" small probability (Moderate)
    '4.6.13',                    # Gaussian PDF integration to 1 증명 (Moderate)
    '4.6.14',                    # 주식 call option (Difficult)
}

PAGES = [0, 1, 2, 3, 4, 5]
PREAMBLE_PAGES = {0}


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


def process_chapter(d, page_indices, keep_set, prefix, has_prior_excluded_pages, preamble_pages=None):
    """preamble_pages: 상단 preamble(Problems heading 등)이 있는 페이지의 인덱스 set.
    이 페이지들은 column별 top overflow redaction을 건너뛰어 preamble을 보존한다.
    (preamble 자체는 별도로 strip_chapter_intro로 처리)
    """
    preamble_pages = preamble_pages or set()

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
            if p not in preamble_pages and prev_p is not None and prev_p not in keep_set:
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

    d = fitz.open(CH4)
    strip_chapter_intro(d[0])
    process_chapter(d, PAGES, KEEP_CH4, '4', has_prior_excluded_pages=False,
                    preamble_pages=PREAMBLE_PAGES)
    out.insert_pdf(d, from_page=PAGES[0], to_page=PAGES[-1])
    d.close()

    out_path = _resolve_out_path(OUT)
    out.save(out_path, garbage=4, deflate=True)
    out.close()

    d = fitz.open(out_path)
    print(f"Wrote {out_path} ({len(d)} pages, {os.path.getsize(out_path)//1024}KB)")
    d.close()


if __name__ == '__main__':
    main()
