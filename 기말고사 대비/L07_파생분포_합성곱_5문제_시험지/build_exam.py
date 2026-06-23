# -*- coding: utf-8 -*-
"""
Lecture 07 (Further Topics on RV Part 1: 파생분포·변수변환·합성곱) 선별 5문항 기말대비 시험지 PDF.
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

TITLE = "선별 5문항 — Lecture 07 파생분포·변수변환·합성곱(정규합) (★=핵심)"

# 떠올릴 개념 (otherwise=0 명시)
CONCEPTS = [
    "단조변환: g가 단조면 f_Y(y) = f_X(h(y))·|d/dy h(y)|,  h=g의 역함수 (야코비안 1변수판)",
    "비단조(예: Y=X²): 구간별 역함수 합산 또는 CDF법 F_Y(y)=P(g(X)≤y) 구한 뒤 미분",
    "CDF법 일반: 분포 구할 땐 F부터 → f_Y(y) = d/dy F_Y(y),  지지구간 경계 주의",
    "두 변수 Z=g(X,Y): 야코비안(2변수 역변환의 |det J|) 또는 CDF법으로 F_Z→f_Z",
    "max/min: F_{max}(z)=∏F(z), 독립이면 F_{min}(z)=1−∏(1−F(z))  (독립 가정 필수)",
    "독립 합 Z=X+Y의 PDF는 합성곱: f_Z(z) = ∫ f_X(x) f_Y(z−x) dx  (지지겹침 구간만)",
    "독립 정규의 합은 정규: 평균=평균합, 분산=분산합  (가중합 aX+bY도 정규)",
    "모든 PMF/PDF는 명시 구간 밖에서 otherwise = 0",
]

# (파일, tag, bank, num, topic)  — 난이도 ■(네모)=difficult 2개 + ●(동그라미)/무표기 IPSRP, ◆(다이아)=experts 제외
ITEMS = [
    ("Q01_L07_IPSRP_4.4.4.png",  "L07", "IPSRP", "4.4.4",  "[무] 단조변환 Y=e^{-X}(uniform): CDF·PDF·E[Y] — 야코비안 기본기"),
    ("Q02_L07_IPSRP_4.4.5.png",  "L07", "IPSRP", "4.4.5",  "[무] 비단조 Y=X²: CDF법으로 F_Y→f_Y·E[Y] ★"),
    ("Q03_L07_PSP_6.4.3.png",    "L07", "PSP",   "6.4.3",  "[■] 두 변수 함수 U=min(X,Y)·V=max(X,Y): 독립판정+CDF·PDF"),
    ("Q04_L07_PSP_6.5.4.png",    "L07", "PSP",   "6.5.4",  "[■] 독립 합 W=X+Y 합성곱: uniform×uniform→삼각분포 PDF"),
    ("Q05_L07_IPSRP_5.4.28.png", "L07", "IPSRP", "5.4.28", "[무] 독립 정규합 U=X+Y(N(0,1)): 조건부PDF·f_U(정규)·역조건·E/Var ★"),
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
                 "①  변환이 단조면 야코비안 공식, 비단조면 CDF법(F부터 → 미분)      ②  독립 합이면 합성곱 / 정규합은 정규      ③  채점: origin 풀이 / /solve-problem")
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
    out = os.path.join(HERE, "문제_L07_파생분포_5문제.pdf")
    c = canvas.Canvas(out, pagesize=(W, H))
    draw_cover(c, ITEMS)
    NO_HEIGHT_CAP = set()   # 5문제 모두 ih<=479로 길지 않음 → 전부 하단 절반 풀이공간 확보(cap 적용)
    for i, it in enumerate(ITEMS, 1):
        draw_problem(c, i, len(ITEMS), it, full_height=(it[3] in NO_HEIGHT_CAP))
    c.save()
    print(f"OK -> {out} ({len(ITEMS)+1} pages)")


if __name__ == "__main__":
    main()
