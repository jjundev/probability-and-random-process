# -*- coding: utf-8 -*-
"""
선별 10문항 기말대비 시험지 PDF.
포맷은 python/build_daily_problem_pdfs.py 와 동일(가로 A4, 표지 1p + 문제당 1p,
하단 절반은 풀이 공간, Malgun, 네이비 배너 + 떠올릴 개념/문항 목차 2단).
"""
import os
from PIL import Image
from reportlab.lib.pagesizes import A4, landscape
from reportlab.pdfgen import canvas
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont

HERE = os.path.dirname(os.path.abspath(__file__))
W, H = landscape(A4)          # 842 x 595
M = 36
SOLVE_MIN_FRAC = 0.5

FONTS = r"C:\Windows\Fonts"
BODY, BOLD = "Malgun", "MalgunBd"
pdfmetrics.registerFont(TTFont(BODY, os.path.join(FONTS, "malgun.ttf")))
pdfmetrics.registerFont(TTFont(BOLD, os.path.join(FONTS, "malgunbd.ttf")))

TITLE = "선별 12문항 — L05~L09 핵심 + 예측 보강 (★=기말 예측 시험지 직결)"

# 떠올릴 개념 (otherwise=0 명시)
CONCEPTS = [
    "혼합형 RV: F_X=C(x)+D(x), E[X]=∫x·c(x)dx + Σ x_k·a_k (도약높이 a_k)",
    "변환 Y=g(X): CDF 먼저 → 미분; 단조구간 f_Y=f_X(g⁻¹(y))·|d g⁻¹/dy|",
    "결합: 주변=합/적분, 조건부=결합/주변, 독립 ⟺ 결합=주변곱",
    "공분산 Cov=E[XY]-E[X]E[Y], ρ=Cov/(σ_X σ_Y), Var(X+Y)=VarX+VarY+2Cov",
    "조건부 기댓값 E[Y|X=x]=∫ y·f_{Y|X}(y|x) dy",
    "CLT: ΣXᵢ≈N(nμ, nσ²); 표본평균 E[Mₙ]=μ, Var(Mₙ)=σ²/n (WLLN)",
    "모든 PMF/PDF는 명시 구간 밖에서 otherwise = 0",
]

# (파일, tag, bank, num, topic)
ITEMS = [
    ("Q01_L05_IPSRP_4.4.13.png", "L05", "IPSRP", "4.4.13", "혼합RV·CDF분해·E[X]"),
    ("Q02_L06_IPSRP_5.4.1.png",  "L06", "IPSRP", "5.4.1",  "이산 결합PMF·주변·조건부·독립 ★"),
    ("Q03_L06_IPSRP_5.4.18.png", "L06", "IPSRP", "5.4.18", "결합PDF 종합·주변·조건부확률"),
    ("Q04_L06_PSP_5.5.1.png",    "L06", "PSP",   "5.5.1",  "결합PDF·주변·E[X]"),
    ("Q05_L06_IPSRP_5.4.20.png", "L06", "IPSRP", "5.4.20", "정규 N(0,1) 조건부 PDF·E·Var ★"),
    ("Q06_L07_PSP_6.2.1.png",    "L07", "PSP",   "6.2.1",  "변환 Y=X²·CDF·PDF"),
    ("Q07_L07_IPSRP_5.4.31.png", "L07", "IPSRP", "5.4.31", "공분산·상관계수 ★"),
    ("Q08_L07_PSP_5.7.5.png",    "L07", "PSP",   "5.7.5",  "상관계수로 Var(X+Y)"),
    ("Q09_L08_PSP_7.5.7.png",    "L08", "PSP",   "7.5.7",  "원판균등·조건부PDF·E[Y|X]"),
    ("Q10_L09_IPSRP_7.3.5.png",  "L09", "IPSRP", "7.3.5",  "CLT 정규근사 ★"),
    ("Q11_L09_PSP_10.1.2.png",   "L09", "PSP",   "10.1.2", "표본평균·CLT·WLLN ★"),
    ("Q12_L09_PSP_9.5.3.png",    "L09", "PSP",   "9.5.3",  "CLT 실전응용(지수·요금)"),
]


def wrap(text, font, size, maxw):
    lines, cur = [], ""
    for ch in text:
        if ch == "\n":
            lines.append(cur); cur = ""; continue
        if pdfmetrics.stringWidth(cur + ch, font, size) <= maxw:
            cur += ch
        else:
            lines.append(cur); cur = ch
    if cur:
        lines.append(cur)
    return lines


def draw_cover(c, items):
    n = len(items)
    c.setFillColorRGB(0.13, 0.20, 0.34); c.rect(0, H - 46, W, 46, fill=1, stroke=0)
    c.setFillColorRGB(1, 1, 1); c.setFont(BOLD, 14)
    c.drawString(M, H - 30, ("확률·랜덤프로세스 기말대비    " + TITLE)[:96])
    by = H - 46 - 8 - 26
    c.setFillColorRGB(0.96, 0.95, 0.88); c.rect(M, by, W - 2 * M, 26, fill=1, stroke=0)
    c.setFillColorRGB(0.1, 0.1, 0.1); c.setFont(BODY, 9.5)
    c.drawString(M + 8, by + 8,
                 "①  오답노트.md 어제 오답부터 재풀이      ②  ★ 표시는 기말 예측 시험지 직결 문항(우선)      ③  채점: origin 풀이 / /solve-problem")
    col_top = by - 20
    lx, rx = M, M + (W - 2 * M) / 2 + 12
    colw = (W - 2 * M) / 2 - 18
    c.setFillColorRGB(0, 0, 0); c.setFont(BOLD, 11)
    c.drawString(lx, col_top, "떠올릴 개념")
    c.setFont(BODY, 9.5); y = col_top - 16
    for b in CONCEPTS[:7]:
        for li, line in enumerate(wrap(b, BODY, 9.5, colw - 10)):
            if y < M + 24:
                break
            c.drawString(lx, y, ("• " if li == 0 else "   ") + line); y -= 12
    c.setFont(BOLD, 11); c.drawString(rx, col_top, f"문항 목차 (총 {n}문항)")
    c.setFont(BODY, 9.5); y = col_top - 16
    for idx, it in enumerate(items, 1):
        if y < M + 24:
            break
        tag, bank, num, topic = it[1], it[2], it[3], it[4]
        c.drawString(rx, y, f"[{idx}]  {tag} · {bank} {num} — {topic}")
        y -= 12.5
    c.setFillColorRGB(0.3, 0.3, 0.3); c.setFont(BODY, 9)
    c.drawString(M, M, "한 문제당 1페이지 · 가로모드 · 풀이 공간 포함    |    권장(75분): ★우선 → 나머지 → 채점·오답등록")
    c.showPage()


def draw_problem(c, idx, n, it):
    fn, tag, bank, num, topic = it
    path = os.path.join(HERE, fn)
    c.setFillColorRGB(0, 0, 0); c.setFont(BOLD, 11)
    c.drawString(M, H - M - 4, f"[{idx}/{n}]   {tag} · {bank} {num}   —   {topic}")
    c.setFillColorRGB(0.4, 0.4, 0.4); c.setFont(BODY, 10)
    c.drawRightString(W - M, H - M - 4, f"{idx} / {n}")
    rule_y = H - M - 15
    c.setStrokeColorRGB(0.7, 0.7, 0.7); c.setLineWidth(0.7); c.line(M, rule_y, W - M, rule_y)
    region_top = rule_y - 12
    avail_w = W - 2 * M
    img_max_h = region_top - H * SOLVE_MIN_FRAC
    iw, ih = Image.open(path).size
    scale = min(avail_w / iw, img_max_h / ih)
    sw, sh = iw * scale, ih * scale
    x, y = M, region_top - sh
    c.drawImage(path, x, y, width=sw, height=sh, mask="auto")
    c.setFillColorRGB(0.78, 0.78, 0.78); c.setFont(BODY, 9)
    c.drawString(M, y - 16, "— 풀이 —")
    c.showPage()


def main():
    out = os.path.join(HERE, "선별_12문제_시험지.pdf")
    c = canvas.Canvas(out, pagesize=(W, H))
    draw_cover(c, ITEMS)
    for i, it in enumerate(ITEMS, 1):
        draw_problem(c, i, len(ITEMS), it)
    c.save()
    print(f"OK -> {out} ({len(ITEMS)+1} pages)")


if __name__ == "__main__":
    main()
