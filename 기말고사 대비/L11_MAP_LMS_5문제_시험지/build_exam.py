# -*- coding: utf-8 -*-
"""
Lecture 11 (통계적추론 Part 2: MAP + LMS/MMSE) 선별 5문항 기말대비 시험지 PDF.
포맷은 L12_LLMS_5문제_시험지/build_exam.py 와 동일(가로 A4, 표지 1p + 문제당 1p,
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

TITLE = "선별 5문항 — Lecture 11 통계적추론 Part 2: MAP·LMS/MMSE 추정 (★=핵심)"

# 떠올릴 개념 (otherwise=0 명시)
CONCEPTS = [
    "LMS=MMSE 점추정: x̂_M(y) = E[X | Y=y]  (사후평균 = 최소 MSE 추정량)",
    "blind/사전추정: 데이터 없으면 x̂_B = E[X]  (사전평균)",
    "사건조건 MMSE: 구간 사건 A(예: X>1/2)만 알면 x̂ = E[X | A]",
    "최소 MSE: e*(y) = Var(X | Y=y) = E[(X − x̂_M(y))² | Y=y]",
    "조건부PDF 먼저: f_{X|Y}(x|y) = f_{X,Y}(x,y) / f_Y(y),  f_Y(y)=∫ f_{X,Y} dx",
    "MAP 점추정: θ̂_MAP = argmax_θ f_{Θ|X}(θ|x) ∝ f_{X|Θ}(x|θ)·f_Θ(θ) (사후 최대)",
    "ML 점추정: θ̂_ML = argmax_θ f_{X|Θ}(x|θ) (사전 무시); Θ가 균등(uniform)이면 MAP==ML",
    "모든 PMF/PDF는 명시 구간 밖에서 otherwise = 0",
]

# (파일, tag, bank, num, topic)  — 난이도 ■(네모)=difficult 4개 + ●(동그라미)=moderate 1개, ◆(다이아)=experts 제외
ITEMS = [
    ("Q01_L11_PSP_12.1.3.png", "L11", "PSP", "12.1.3", "[■] 결합PDF·주변 fX/fY·blind추정 x̂_B·사건조건 MMSE(X>1/2)"),
    ("Q02_L11_PSP_12.1.4.png", "L11", "PSP", "12.1.4", "[●] 조건부PDF·MMSE x̂_M(y)=E[X|Y=y] 양방향 핵심정의 ★"),
    ("Q03_L11_PSP_12.1.5.png", "L11", "PSP", "12.1.5", "[■] 조건부PDF·MMSE·최소MSE e*(0.5)=Var(X|Y=0.5)"),
    ("Q04_L11_PSP_12.1.6.png", "L11", "PSP", "12.1.6", "[■] 가우시안 신호+잡음·MMSE 추정량 Ẑ(Y)·MSE e ★"),
    ("Q05_L11_PSP_12.3.1.png", "L11", "PSP", "12.3.1", "[■] MAP 추정·MAP vs ML 동일여부 비교 ★"),
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
                 "①  베이즈로 사후 f_{Θ|X} 먼저      ②  MMSE=조건부평균 / MAP=argmax 사후 / ML=argmax likelihood      ③  채점: origin 풀이 / /solve-problem")
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
    out = os.path.join(HERE, "문제_L11_MAP_LMS_5문제.pdf")
    c = canvas.Canvas(out, pagesize=(W, H))
    draw_cover(c, ITEMS)
    NO_HEIGHT_CAP = set()   # 5문제 모두 ih<=486로 길지 않음 → 전부 하단 절반 풀이공간 확보(cap 적용)
    for i, it in enumerate(ITEMS, 1):
        draw_problem(c, i, len(ITEMS), it, full_height=(it[3] in NO_HEIGHT_CAP))
    c.save()
    print(f"OK -> {out} ({len(ITEMS)+1} pages)")


if __name__ == "__main__":
    main()
