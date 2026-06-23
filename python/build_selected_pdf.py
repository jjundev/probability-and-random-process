"""
Lectures 1-6 기준으로 풀이 가능 문제만 추려서 새 PDF를 만든다.

노트 커버리지(Lectures 1~6):
- 확률공리, 조건부, 베이즈, 독립
- RV, PMF, CDF
- 이산분포: Bernoulli / Uniform(disc) / Binomial / Geometric  (이항계수 포함)
- 기댓값, 분산, 표준편차, Linearity, functions of RV
- Joint PMF, Marginal PMF, Conditional PMF, 독립 RV
- Total probability / expectation theorem for RVs, Memoryless
- Continuous RV, PDF, CDF
- Exponential RV, Gaussian RV (standardization, Q-function)

노트에 없는 것:
- Poisson, Multinomial, Erlang, Laplacian, Mixed RV
- Covariance, Correlation, Bivariate Gaussian
- Continuous joint/marginal/conditional
- 일반 Counting (순열/조합), Convolution, MGF
- MATLAB
"""

import fitz

BASE = "Probability_and_Stochastic_Processes_Problems/"
CH1 = BASE + "Chapter_01_Problems_pages_47-52.pdf"
CH2 = BASE + "Chapter_02_Problems_pages_75-79.pdf"
CH3 = BASE + "Chapter_03_Problems_pages_124-135.pdf"
CH4 = BASE + "Chapter_04_Problems_pages_172-179.pdf"
CH5 = BASE + "Chapter_05_Problems_pages_224-235.pdf"
OUT = "Selected_Problems_Lectures_1_6.pdf"

COL = 265.0
WHITE = (1, 1, 1)


def fit_rect(page, x0, y0, x1, y1):
    return fitz.Rect(x0, y0, x1, y1) & page.rect


def redact(page, x0, y0, x1, y1):
    page.add_redact_annot(fit_rect(page, x0, y0, x1, y1), fill=WHITE)


def apply(page):
    page.apply_redactions()


def find_header_y(page, text="Problems"):
    rects = page.search_for(text)
    return min(r.y0 for r in rects) if rects else None


def strip_top_preamble(page, fallback=380):
    """Page 상단의 Problems 섹션 헤더 위쪽(이전 섹션 본문) 제거"""
    hy = find_header_y(page) or fallback
    redact(page, 0, 30, page.rect.width, hy - 6)
    apply(page)


# ------------------------- Chapter 1 -------------------------
def process_ch1(d):
    strip_top_preamble(d[0], 380)
    # Page 5: 1.7.1 (우측 y=278.1부터) 제거
    p5 = d[5]
    redact(p5, COL, 275, p5.rect.width, p5.rect.height)
    apply(p5)


# ------------------------- Chapter 2 -------------------------
# 유지: 2.1.1~2.1.12, 2.2.2, 2.3.1, 2.3.2, 2.3.4, 2.3.5, 2.4.1, 2.4.2, 2.4.4
# 제거: 2.2.1, 2.2.3~2.2.13, 2.3.3, 2.4.3, 2.5.x
def process_ch2(d):
    strip_top_preamble(d[0], 180)

    # Page 2: 2.2.1(좌 112~194) 제거, 2.2.2(좌 194~346) 유지, 2.2.3/2.2.4(좌 346~end) 제거, 우측 전체(2.2.5~2.2.11) 제거
    p2 = d[2]
    redact(p2, 0, 109, COL, 192)
    redact(p2, 0, 343, COL, p2.rect.height)
    redact(p2, COL, 0, p2.rect.width, p2.rect.height)
    apply(p2)

    # Page 3: 좌 [0, 407)(2.2.12, 2.2.13) 제거, 2.3.1/2.3.2 유지
    #         우 [0, 255)(2.3.3) 제거, 2.3.4/2.3.5 유지
    p3 = d[3]
    redact(p3, 0, 0, COL, 404)
    redact(p3, COL, 0, p3.rect.width, 252)
    apply(p3)

    # Page 4: 2.4.3(좌 354~457) 제거, 2.5.1(좌 516~end) 제거, 우측 전체 제거
    p4 = d[4]
    redact(p4, 0, 351, COL, 454)
    redact(p4, 0, 513, COL, p4.rect.height)
    redact(p4, COL, 0, p4.rect.width, p4.rect.height)
    apply(p4)


# ------------------------- Chapter 3 -------------------------
# 유지: 3.2~3.8 대부분
# 제거: 3.3.10 (Poisson), 3.5.3 (Poisson), 3.9.x (MATLAB, 일부 Poisson)
def process_ch3(d):
    strip_top_preamble(d[0], 180)

    # Page 2 우측 [183.7, 331.0) — 3.3.10 (Poisson)
    p2 = d[2]
    redact(p2, COL, 180, p2.rect.width, 328)
    apply(p2)

    # Page 5 좌측 [72.4, 235.6) — 3.5.3 (Poisson)
    p5 = d[5]
    redact(p5, 0, 69, COL, 232)
    apply(p5)

    # Page 10 우측 [367.0, end) — 3.9.1~3.9.4 (MATLAB)
    p10 = d[10]
    redact(p10, COL, 364, p10.rect.width, p10.rect.height)
    apply(p10)
    # Page 11은 호출측에서 제외 (3.9.5~3.9.9 전부 MATLAB)


# ------------------------- Chapter 4 -------------------------
# 유지: 4.2~4.6 (Erlang 제외)
# 제거: 4.5.6, 4.5.7 (Erlang), 4.5.16~4.5.18 (Erlang), 4.7.x (Mixed RV), 4.8.x (MATLAB)
def process_ch4(d):
    strip_top_preamble(d[0], 150)

    # Page 2: 4.5.6 (좌 [519, end)) 제거, 4.5.7 (우 [52, 123)) 제거
    p2 = d[2]
    redact(p2, 0, 516, COL, p2.rect.height)
    redact(p2, COL, 0, p2.rect.width, 120)
    apply(p2)

    # Page 3: 4.5.16~4.5.18 (좌 [140.3, 582.3)) 제거
    p3 = d[3]
    redact(p3, 0, 137, COL, 579)
    apply(p3)

    # Page 6: 4.7.1~4.7.6 (좌 [112, end)) 제거, 우측 전체 (4.7.7~4.7.9, 4.8.1, 4.8.2) 제거
    p6 = d[6]
    redact(p6, 0, 109, COL, p6.rect.height)
    redact(p6, COL, 0, p6.rect.width, p6.rect.height)
    apply(p6)
    # Page 7 (4.8.3, 4.8.4) 호출측에서 제외


# ------------------------- Chapter 5 -------------------------
# 유지: 5.2.1~5.2.9, 5.3.1, 5.3.2, 5.3.4, 5.3.5  (discrete joint/marginal PMF)
# 제거: 5.1.x (joint CDF continuous), 5.3.3/5.3.6 (Poisson), 5.4~5.11 (continuous joint / covariance / multinomial / MATLAB)
def process_ch5(d):
    # Page 0 전체 제외 (호출측)

    # Page 1: 좌 [0, 355)(5.1.4~5.1.6) 제거, 5.2.1부터 유지, 우측 유지(5.2.3~5.2.6)
    p1 = d[1]
    redact(p1, 0, 0, COL, 352)
    apply(p1)

    # Page 2: 좌측 전체 유지 (5.2.7~5.2.9)
    #         우측 [234, 355)(5.3.3 Poisson) 제거, [540, end)(5.3.6 Poisson) 제거
    p2 = d[2]
    redact(p2, COL, 231, p2.rect.width, 352)
    redact(p2, COL, 540, p2.rect.width, p2.rect.height)
    apply(p2)
    # Page 3 이후 전부 호출측에서 제외


def main():
    out = fitz.open()

    d1 = fitz.open(CH1)
    process_ch1(d1)
    out.insert_pdf(d1)
    d1.close()

    d2 = fitz.open(CH2)
    process_ch2(d2)
    out.insert_pdf(d2)
    d2.close()

    d3 = fitz.open(CH3)
    process_ch3(d3)
    out.insert_pdf(d3, from_page=0, to_page=10)  # p11 제외
    d3.close()

    d4 = fitz.open(CH4)
    process_ch4(d4)
    out.insert_pdf(d4, from_page=0, to_page=6)  # p7 제외
    d4.close()

    d5 = fitz.open(CH5)
    process_ch5(d5)
    out.insert_pdf(d5, from_page=1, to_page=2)  # p0, p3~p11 제외
    d5.close()

    out.save(OUT, garbage=4, deflate=True)
    out.close()
    print(f"Wrote {OUT}  ({len(fitz.open(OUT))} pages)")


if __name__ == "__main__":
    main()
