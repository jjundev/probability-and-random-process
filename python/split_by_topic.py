"""
Selected_Problems_Lectures_1_6.pdf를 4개 주제로 분리:
  01_Probabilistic_Model.pdf        : Lecture 1 (표본공간·공리)
  02_Conditioning_Bayes_Independence.pdf : Lecture 2
  03_Discrete_RV.pdf                : Lectures 3-4
  04_Continuous_RV.pdf              : Lectures 5-6

원본 챕터 PDF에서 각각 redaction 규칙을 달리 적용해서 4개 파일을 생성한다.
"""

import os
import fitz

BASE = "Probability_and_Stochastic_Processes_Problems/"
CH1 = BASE + "Chapter_01_Problems_pages_47-52.pdf"
CH2 = BASE + "Chapter_02_Problems_pages_75-79.pdf"
CH3 = BASE + "Chapter_03_Problems_pages_124-135.pdf"
CH4 = BASE + "Chapter_04_Problems_pages_172-179.pdf"
CH5 = BASE + "Chapter_05_Problems_pages_224-235.pdf"

OUT_DIR = "problems"
COL = 265.0
WHITE = (1, 1, 1)


def redact(page, x0, y0, x1, y1):
    rect = fitz.Rect(x0, y0, x1, y1) & page.rect
    page.add_redact_annot(rect, fill=WHITE)


def apply_red(page):
    page.apply_redactions()


def strip_preamble(page, fallback=380):
    rects = page.search_for("Problems")
    hy = min(r.y0 for r in rects) if rects else fallback
    redact(page, 0, 30, page.rect.width, hy - 6)
    apply_red(page)


# ============================================================
# 주제 1: Probabilistic Model  ── Ch1의 1.1, 1.2, 1.3
# ============================================================
def build_topic1():
    out = fitz.open()
    d = fitz.open(CH1)
    strip_preamble(d[0], 380)
    # page 2: 좌측 (1.3.5~1.3.9) 유지, 우측 상단 (1.3.10~1.3.14, y<337) 유지,
    #          우측 [337, end) 제거 (1.4.1, 1.4.2)
    p2 = d[2]
    redact(p2, COL, 335, p2.rect.width, p2.rect.height)
    apply_red(p2)
    out.insert_pdf(d, from_page=0, to_page=2)
    d.close()
    out.save(f"{OUT_DIR}/01_Probabilistic_Model.pdf", garbage=4, deflate=True)
    out.close()


# ============================================================
# 주제 2: Conditioning, Bayes, Independence
#   Ch1 1.4, 1.5, 1.6   (Ch1 pages 2 일부 + 3 + 4 + 5)
#   Ch2 2.1, 2.4.1, 2.4.2, 2.4.4
# ============================================================
def build_topic2():
    out = fitz.open()

    # --- Ch1 ---
    d1 = fitz.open(CH1)
    # page 2: 좌측 전체(1.3.5~1.3.9) 제거, 우측 [0, 337)(1.3.10~1.3.14) 제거
    p2 = d1[2]
    redact(p2, 0, 0, COL, p2.rect.height)
    redact(p2, COL, 0, p2.rect.width, 335)
    apply_red(p2)
    # page 5: 1.7.1 제거
    p5 = d1[5]
    redact(p5, COL, 275, p5.rect.width, p5.rect.height)
    apply_red(p5)
    out.insert_pdf(d1, from_page=2, to_page=5)
    d1.close()

    # --- Ch2 ---
    d2 = fitz.open(CH2)
    strip_preamble(d2[0], 180)
    # page 2: 좌측 [112, end)(2.2.1~2.2.4) 제거, 우측 전체(2.2.5~2.2.11) 제거
    #          좌측 [0, 112) 유지 (2.1.12 연속)
    p2 = d2[2]
    redact(p2, 0, 109, COL, p2.rect.height)
    redact(p2, COL, 0, p2.rect.width, p2.rect.height)
    apply_red(p2)
    # page 4: 2.4.3 제거, 2.5.x 제거
    p4 = d2[4]
    redact(p4, 0, 351, COL, 454)
    redact(p4, 0, 513, COL, p4.rect.height)
    redact(p4, COL, 0, p4.rect.width, p4.rect.height)
    apply_red(p4)
    out.insert_pdf(d2, from_page=0, to_page=2)  # 0,1,2
    out.insert_pdf(d2, from_page=4, to_page=4)  # page 3(2.2-2.3), 마지막 MATLAB 페이지 제외하고 page 4
    d2.close()

    out.save(f"{OUT_DIR}/02_Conditioning_Bayes_Independence.pdf",
             garbage=4, deflate=True)
    out.close()


# ============================================================
# 주제 3: Discrete RV
#   Ch2  2.2.2, 2.3.1/2/4/5    (Ch2 pages 2, 3 의 해당 부분만)
#   Ch3  전체 (3.3.10, 3.5.3, 3.9.x 제외)
#   Ch5  5.2.x, 5.3.1/2/4/5     (Ch5 pages 1~2)
# ============================================================
def build_topic3():
    out = fitz.open()

    # --- Ch2 page 2, 3 ---
    d2 = fitz.open(CH2)
    # page 2: 2.2.2만 유지  ->  좌측 [0, 192)=2.1.12연속+2.2.1 제거, 좌측 [343, end)=2.2.3,2.2.4 제거, 우측 전체 제거
    p2 = d2[2]
    redact(p2, 0, 0, COL, 192)
    redact(p2, 0, 343, COL, p2.rect.height)
    redact(p2, COL, 0, p2.rect.width, p2.rect.height)
    apply_red(p2)
    # page 3: 2.3.1, 2.3.2 (좌측 하단) + 2.3.4, 2.3.5 (우측 하단) 유지
    p3 = d2[3]
    redact(p3, 0, 0, COL, 404)           # 2.2.12, 2.2.13
    redact(p3, COL, 0, p3.rect.width, 252)  # 2.3.3
    apply_red(p3)
    out.insert_pdf(d2, from_page=2, to_page=3)
    d2.close()

    # --- Ch3 전체 (p11 제외) ---
    d3 = fitz.open(CH3)
    strip_preamble(d3[0], 180)
    # 3.3.10 제거
    p2 = d3[2]
    redact(p2, COL, 180, p2.rect.width, 328)
    apply_red(p2)
    # 3.5.3 제거
    p5 = d3[5]
    redact(p5, 0, 69, COL, 232)
    apply_red(p5)
    # 3.9.1~3.9.4 제거
    p10 = d3[10]
    redact(p10, COL, 364, p10.rect.width, p10.rect.height)
    apply_red(p10)
    out.insert_pdf(d3, from_page=0, to_page=10)
    d3.close()

    # --- Ch5 page 1, 2 ---
    d5 = fitz.open(CH5)
    p1 = d5[1]
    redact(p1, 0, 0, COL, 352)       # 5.1.4~5.1.6 제거
    apply_red(p1)
    p2 = d5[2]
    redact(p2, COL, 231, p2.rect.width, 352)            # 5.3.3 (Poisson) 제거
    redact(p2, COL, 540, p2.rect.width, p2.rect.height)  # 5.3.6 (Poisson) 제거
    apply_red(p2)
    out.insert_pdf(d5, from_page=1, to_page=2)
    d5.close()

    out.save(f"{OUT_DIR}/03_Discrete_RV.pdf", garbage=4, deflate=True)
    out.close()


# ============================================================
# 주제 4: Continuous RV
#   Ch4 전체 (Erlang·Mixed·MATLAB 제외)
# ============================================================
def build_topic4():
    out = fitz.open()
    d = fitz.open(CH4)
    strip_preamble(d[0], 150)
    # 4.5.6, 4.5.7 (Erlang) 제거
    p2 = d[2]
    redact(p2, 0, 516, COL, p2.rect.height)
    redact(p2, COL, 0, p2.rect.width, 120)
    apply_red(p2)
    # 4.5.16~4.5.18 (Erlang) 제거
    p3 = d[3]
    redact(p3, 0, 137, COL, 579)
    apply_red(p3)
    # 4.7.x (Mixed RV), 4.8.1, 4.8.2 (MATLAB) 제거
    p6 = d[6]
    redact(p6, 0, 109, COL, p6.rect.height)
    redact(p6, COL, 0, p6.rect.width, p6.rect.height)
    apply_red(p6)
    out.insert_pdf(d, from_page=0, to_page=6)  # p7 (4.8.3/4) 제외
    d.close()
    out.save(f"{OUT_DIR}/04_Continuous_RV.pdf", garbage=4, deflate=True)
    out.close()


def main():
    os.makedirs(OUT_DIR, exist_ok=True)
    build_topic1()
    build_topic2()
    build_topic3()
    build_topic4()
    # 요약
    for fn in ['01_Probabilistic_Model.pdf',
               '02_Conditioning_Bayes_Independence.pdf',
               '03_Discrete_RV.pdf',
               '04_Continuous_RV.pdf']:
        path = f"{OUT_DIR}/{fn}"
        d = fitz.open(path)
        print(f"{fn}: {len(d)} pages, {os.path.getsize(path)//1024}KB")
        d.close()


if __name__ == "__main__":
    main()
