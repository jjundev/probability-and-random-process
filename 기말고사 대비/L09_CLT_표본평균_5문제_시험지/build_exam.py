# -*- coding: utf-8 -*-
"""
Lecture 09 (Asymptotic Behavior of RVs: 표본평균·WLLN·CLT) 선별 5문항 기말대비 시험지 PDF.
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

TITLE = "선별 5문항 — Lecture 09 표본평균·WLLN·CLT(정규근사·연속성보정) (★=핵심)"

# 떠올릴 개념 (otherwise=0 명시)
CONCEPTS = [
    "표본평균 M_n=(X_1+...+X_n)/n:  E[M_n]=μ,  Var(M_n)=σ²/n  (n↑ 분산↓)",
    "WLLN(약한큰수): M_n -> μ (확률수렴, in prob.) — 임의 ε>0에 P(|M_n−μ|>ε)->0",
    "CLT: (ΣX_i − nμ)/(σ√n) -> N(0,1) (분포수렴) — 표본합·표본평균을 정규로 근사",
    "확률 계산: 표준화 후 Φ표(또는 Q=1−Φ)로 P(...) 환산, σ_{M_n}=σ/√n",
    "이산RV(예: 이항) 정규근사 시 연속성 보정 ±0.5 (예 P(K≤k)≈Φ((k+0.5−μ)/σ))",
    "이 과목 미출제: Chebyshev·MGF·강한LLN·a.s./Lʳ 수렴 (정규근사/표본평균만 사용)",
    "모든 PMF/PDF는 명시 구간 밖에서 otherwise = 0",
]

# (파일, tag, bank, num, topic)  — 표본평균E/Var → WLLN확률수렴 → CLT(연속·이산·연속성보정), ◆ 제외, ●/IPSRP
ITEMS = [
    ("Q01_L09_PSP_10.1.1.png", "L09", "PSP", "10.1.1", "[●] 표본평균 분산 Var[M_9]=σ²/9 · P[X_1>7] · CLT P[M_9>7]"),
    ("Q02_L09_IPSRP_7.3.7.png", "L09", "IPSRP", "7.3.7", "[ ] 측정 정밀도용 표본크기 n 결정 P(|M_n−q|≤0.1)≥0.95 — CLT 정규근사로(Chebyshev 미사용)"),
    ("Q03_L09_IPSRP_7.3.5.png", "L09", "IPSRP", "7.3.5", "[ ] CLT 표본합 정규근사: 7시간에 ≤40 job 처리확률 ★"),
    ("Q04_L09_PSP_9.5.2.png", "L09", "PSP", "9.5.2", "[●] CLT 이산(이항)근사·연속성보정: P[16≤K_100≤24] ★"),
    ("Q05_L09_IPSRP_7.3.4.png", "L09", "IPSRP", "7.3.4", "[ ] CLT 연속성보정 명시: 50명 중 주차>30대 확률"),
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
                 "①  표본평균이면 E=μ·Var=σ²/n      ②  확률 물으면 CLT 표준화→Φ(Q함수), 이산은 ±0.5 보정      ③  채점: origin 풀이 / /solve-problem")
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
    out = os.path.join(HERE, "문제_L09_CLT_표본평균_5문제.pdf")
    c = canvas.Canvas(out, pagesize=(W, H))
    draw_cover(c, ITEMS)
    NO_HEIGHT_CAP = set()   # 5문제 모두 가로형/짧음 → 전부 하단 절반 풀이공간 확보(cap 적용)
    for i, it in enumerate(ITEMS, 1):
        draw_problem(c, i, len(ITEMS), it, full_height=(it[3] in NO_HEIGHT_CAP))
    c.save()
    print(f"OK -> {out} ({len(ITEMS)+1} pages)")


if __name__ == "__main__":
    main()
