# -*- coding: utf-8 -*-
"""
Lecture 08 (Further Topics on RV Part 2: 공분산·조건부기댓값/분산·총분산법칙·랜덤합) 선별 5문항 기말대비 시험지 PDF.
포맷은 L11_MAP_LMS_5문제_시험지/build_exam.py 와 동일(가로 A4, 표지 1p + 문제당 1p,
하단 절반은 풀이 공간, Malgun, 네이비 배너 + 떠올릴 개념/문항 목차 2단).
"""
import os
import re
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

TITLE = "선별 5문항 — Lecture 08 공분산·조건부기댓값/분산·총분산법칙·랜덤합 (★=핵심)"

# 떠올릴 개념 (otherwise=0 명시)
CONCEPTS = [
    "공분산: Cov(X,Y) = E[XY] − E[X]E[Y];  상관계수 ρ = Cov(X,Y)/(σ_X σ_Y) ∈ [−1,1]",
    "공분산 쌍선형성: Cov(aX+bY, Z) = a·Cov(X,Z)+b·Cov(Y,Z);  Var(aX+bY)=a²VarX+b²VarY+2ab·Cov",
    "조건부기댓값: E[X | Y=y] = ∫ x f_{X|Y}(x|y) dx,  단 f_{X|Y}(x|y)=f_{X,Y}(x,y)/f_Y(y)",
    "전기댓값정리(반복기댓값): E[X] = E[ E[X | Y] ]  (안쪽은 y의 함수, 바깥쪽은 Y로 평균)",
    "총분산법칙: Var(X) = E[ Var(X | Y) ] + Var( E[X | Y] )",
    "랜덤합 S = Σ_{i=1}^N X_i (N⊥X_i, iid):  E[S]=E[N]E[X],  Var(S)=E[N]Var(X)+Var(N)(E[X])²",
    "결합정규: 선형결합도 정규 / 조건부도 정규  X|Y=y ~ N(μ_X+ρ(σ_X/σ_Y)(y−μ_Y), (1−ρ²)σ_X²)",
    "모든 PMF/PDF는 명시 구간 밖에서 otherwise = 0",
]

# (파일, tag, bank, num, topic)  — 난이도 ■(네모)=difficult 3개 + 무표시 IPSRP 2개, ◆(다이아)=experts 제외
# 주: 랜덤합·전기댓값정리 전용 문제는 은행에 Poisson 기반밖에 없어(=강의 미개설) 제외. 두 주제는 표지 개념으로 커버.
ITEMS = [
    ("Q01_L08_PSP_5.9.5.png", "L08", "PSP", "5.9.5", "[■] 결합정규 PDF에서 Cov·상관계수 ρ·Var·독립성 — Cov=E[XY]−E[X]E[Y] ★"),
    ("Q02_L08_IPSRP_5.4.36.png", "L08", "IPSRP", "5.4.36", "[무] 결합정규 선형결합 P(X+2Y≤3)·Cov(X−Y, X+2Y) — 공분산 쌍선형성·선형결합정규"),
    ("Q03_L08_PSP_7.5.6.png", "L08", "PSP", "7.5.6", "[■] 조건부PDF f_{X|Y}·E[X|Y=y] 정의대로 — 조건부기댓값 핵심 ★"),
    ("Q04_L08_PSP_7.5.7.png", "L08", "PSP", "7.5.7", "[■] 원판 균등 f_{Y|X}·E[Y|X=x] — 조건부기댓값(반복기댓값/총분산 연습)"),
    ("Q05_L08_IPSRP_5.4.38.png", "L08", "IPSRP", "5.4.38", "[무] 결합정규 E[Y|X=3]·Var(Y|X=2)·조건부확률 — 조건부정규·조건부분산 ★"),
]


def norm(s):
    """Malgun에 없는 글리프 정규화: 결합 모자(U+0302)→'^', Ŷ(U+0176)→'Y^', 빼기(U+2212)→'-'."""
    s = re.sub(r"(.)̂", r"\1^", s)   # X̂ V̂ Θ̂ → X^ V^ Θ^
    s = s.replace("Ŷ", "Y^").replace("ŷ", "y^")
    s = s.replace("−", "-")
    return s


def wrap(text, font, size, maxw):
    text = norm(text)
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
    c.drawString(M, H - 30, norm("확률·랜덤프로세스 기말대비    " + TITLE)[:96])
    by = H - 46 - 8 - 26
    c.setFillColorRGB(0.96, 0.95, 0.88); c.rect(M, by, W - 2 * M, 26, fill=1, stroke=0)
    c.setFillColorRGB(0.1, 0.1, 0.1); c.setFont(BODY, 9.5)
    c.drawString(M + 8, by + 8,
                 "①  공분산·상관계수는 E[XY]부터      ②  조건부 다루면 전기댓값/총분산법칙 떠올리기      ③  채점: origin 풀이 / /solve-problem")
    col_top = by - 20
    lx, rx = M, M + (W - 2 * M) / 2 + 12
    colw = (W - 2 * M) / 2 - 18
    c.setFillColorRGB(0, 0, 0); c.setFont(BOLD, 11)
    c.drawString(lx, col_top, "떠올릴 개념")
    c.setFont(BODY, 9.5); y = col_top - 16
    for b in CONCEPTS[:8]:
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
        c.drawString(rx, y, norm(f"[{idx}]  {tag} · {bank} {num} — {topic}"))
        y -= 12.5
    c.setFillColorRGB(0.3, 0.3, 0.3); c.setFont(BODY, 9)
    c.drawString(M, M, "한 문제당 1페이지 · 가로모드 · 풀이 공간 포함    |    권장: ★우선 → 나머지 → 채점·오답등록")
    c.showPage()


def draw_problem(c, idx, n, it, full_height=False):
    fn, tag, bank, num, topic = it
    path = os.path.join(HERE, fn)
    c.setFillColorRGB(0, 0, 0); c.setFont(BOLD, 11)
    c.drawString(M, H - M - 4, norm(f"[{idx}/{n}]   {tag} · {bank} {num}   —   {topic}"))
    c.setFillColorRGB(0.4, 0.4, 0.4); c.setFont(BODY, 10)
    c.drawRightString(W - M, H - M - 4, f"{idx} / {n}")
    rule_y = H - M - 15
    c.setStrokeColorRGB(0.7, 0.7, 0.7); c.setLineWidth(0.7); c.line(M, rule_y, W - M, rule_y)
    region_top = rule_y - 12
    avail_w = W - 2 * M
    # full_height=True: 풀이공간 상한 해제(세로로 긴 문제는 하단여백까지 사용). "— 풀이 —" 라벨 자리만 남김.
    img_max_h = (region_top - M - 18) if full_height else (region_top - H * SOLVE_MIN_FRAC)
    iw, ih = Image.open(path).size
    scale = min(avail_w / iw, img_max_h / ih)
    sw, sh = iw * scale, ih * scale
    x, y = M, region_top - sh
    c.drawImage(path, x, y, width=sw, height=sh, mask="auto")
    c.setFillColorRGB(0.78, 0.78, 0.78); c.setFont(BODY, 9)
    c.drawString(M, y - 16, "— 풀이 —")
    c.showPage()


def main():
    out = os.path.join(HERE, "문제_L08_공분산_조건부_5문제.pdf")
    c = canvas.Canvas(out, pagesize=(W, H))
    draw_cover(c, ITEMS)
    NO_HEIGHT_CAP = set()   # 5문제 모두 ih<=504로 길지 않음 → 전부 하단 절반 풀이공간 확보(cap 적용)
    for i, it in enumerate(ITEMS, 1):
        draw_problem(c, i, len(ITEMS), it, full_height=(it[3] in NO_HEIGHT_CAP))
    c.save()
    print(f"OK -> {out} ({len(ITEMS)+1} pages)")


if __name__ == "__main__":
    main()
