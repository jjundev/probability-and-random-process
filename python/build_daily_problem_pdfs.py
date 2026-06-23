# -*- coding: utf-8 -*-
"""
일자별 문제 PDF 생성기 (가로 A4, 표지 1p + 문제당 1p, 태블릿 풀이용).

각 '기말고사 대비/6월 N일/' 폴더의 *.png 문제를 모아 '문제_6월N일.pdf' 생성.
- 방향 인식 스케일링: 세로형 문제는 좌측에 높이맞춤(우측이 풀이공간),
  가로형 문제는 폭맞춤(하단이 풀이공간). 항상 좌상단 정렬로 풀이공간 확보.
- 숫자 튜플 정렬, 정규식 파일명 파싱(복습 접두사 포함).
- 한글: Malgun Gothic.
재실행 가능(덮어쓰기).
"""
import os, re, glob
from PIL import Image
from reportlab.lib.pagesizes import A4, landscape
from reportlab.pdfgen import canvas
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont

ROOT = r"C:\Users\Hyunjun\Desktop\현준대학\확랜"
DEST = os.path.join(ROOT, "기말고사 대비")
W, H = landscape(A4)          # 842 x 595
M = 36                        # margin
SOLVE_MIN_FRAC = 0.5          # 페이지 세로의 최소 이 비율은 풀이공간으로 비움(이미지 높이 상한)

# ---- fonts ----
FONTS = r"C:\Windows\Fonts"
BODY, BOLD = "Malgun", "MalgunBd"
try:
    pdfmetrics.registerFont(TTFont(BODY, os.path.join(FONTS, "malgun.ttf")))
    pdfmetrics.registerFont(TTFont(BOLD, os.path.join(FONTS, "malgunbd.ttf")))
except Exception as e:
    print("WARN: malgun 등록 실패, Helvetica 폴백(한글 깨질 수 있음):", e)
    BODY = BOLD = "Helvetica"

LECMAP = {"01":"확률모델","02":"조건부·Bayes","03":"이산RV1","04":"이산RV2",
          "05":"연속RV1","06":"연속RV2","07":"Further1 변환·공분산",
          "08":"Further2 상관·전분산","09":"점근 CLT"}
NAME_RE = re.compile(r"^(복습)?L(\d{2})_([A-Za-z]+)_(.+)\.png$")


def num_key(num):
    try:
        return tuple(int(x) for x in num.split("."))
    except ValueError:
        return (10**9,)  # 비숫자는 뒤로


def parse_png(path):
    name = os.path.basename(path)
    m = NAME_RE.match(name)
    if not m:
        return None
    rev, lec, bank, num = bool(m.group(1)), m.group(2), m.group(3), m.group(4)
    tag = ("복습 L" + lec) if rev else ("L" + lec)
    topic = LECMAP.get(lec, lec)
    sortkey = (1 if rev else 0, int(lec), 0 if bank.upper() == "IPSRP" else 1, num_key(num))
    return dict(path=path, tag=tag, bank=bank, num=num, topic=topic, key=sortkey)


def read_md(folder):
    """오늘_복습.md에서 제목(H1)과 '떠올릴 개념' 불릿 추출(best-effort)."""
    p = os.path.join(folder, "오늘_복습.md")
    title, concepts = "", []
    if not os.path.exists(p):
        return title, concepts
    lines = open(p, encoding="utf-8").read().splitlines()
    cap = False
    for ln in lines:
        if not title and ln.startswith("# "):
            title = ln[2:].strip()
        if ln.startswith("##") and "떠올릴 개념" in ln:
            cap = True
            continue
        if cap and ln.startswith("## "):
            break
        if cap and ln.strip().startswith("- "):
            s = ln.strip()[2:].replace("**", "").replace("`", "")
            # malgun에 없는 일부 글리프 정규화(표지 힌트 가독성)
            for a, b in [("−", "-"), ("–", "-"), ("₋", "-"), ("ˣ", "x"),
                         ("₋∞", "-inf"), ("∫₋∞ˣ", "∫")]:
                s = s.replace(a, b)
            s = s.strip()
            if s:
                concepts.append(s)
    return title, concepts


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


def draw_cover(c, title, concepts, items):
    n = len(items)
    # title bar
    c.setFillColorRGB(0.13, 0.20, 0.34); c.rect(0, H - 46, W, 46, fill=1, stroke=0)
    c.setFillColorRGB(1, 1, 1); c.setFont(BOLD, 14)
    head = "확률·랜덤프로세스 기말대비    " + (title or "")
    c.drawString(M, H - 30, head[:90])
    # instruction banner
    by = H - 46 - 8 - 26
    c.setFillColorRGB(0.96, 0.95, 0.88); c.rect(M, by, W - 2 * M, 26, fill=1, stroke=0)
    c.setFillColorRGB(0.1, 0.1, 0.1); c.setFont(BODY, 9.5)
    c.drawString(M + 8, by + 8,
                 "①  오답노트.md 어제 오답부터 재풀이      ②  아래 신규 문제는 '상한'(시간 부족 시 신규만 이월)      ③  채점: origin 풀이 / /solve-problem")
    # two columns
    col_top = by - 20
    lx, rx = M, M + (W - 2 * M) / 2 + 12
    colw = (W - 2 * M) / 2 - 18
    c.setFillColorRGB(0, 0, 0); c.setFont(BOLD, 11)
    c.drawString(lx, col_top, "떠올릴 개념")
    c.setFont(BODY, 9.5); y = col_top - 16
    for b in concepts[:7]:
        for li, line in enumerate(wrap(b, BODY, 9.5, colw - 10)):
            if y < M + 24:
                break
            c.drawString(lx, y, ("• " if li == 0 else "   ") + line); y -= 12
    c.setFont(BOLD, 11); c.drawString(rx, col_top, f"문항 목차 (총 {n}문항)")
    c.setFont(BODY, 9.5); y = col_top - 16
    for idx, it in enumerate(items, 1):
        if y < M + 24:
            break
        c.drawString(rx, y, f"[{idx}]  {it['tag']} · {it['bank']} {it['num']} — {it['topic']}")
        y -= 12.5
    # footer
    c.setFillColorRGB(0.3, 0.3, 0.3); c.setFont(BODY, 9)
    c.drawString(M, M, "한 문제당 1페이지 · 가로모드 · 풀이 공간 포함    |    권장: 오답 30~40분 → 신규(상한) 90~120분 → 채점·오답등록")
    c.showPage()


def draw_problem(c, idx, n, it):
    c.setFillColorRGB(0, 0, 0); c.setFont(BOLD, 11)
    c.drawString(M, H - M - 4, f"[{idx}/{n}]   {it['tag']} · {it['bank']} {it['num']}   —   {it['topic']}")
    c.setFillColorRGB(0.4, 0.4, 0.4); c.setFont(BODY, 10)
    c.drawRightString(W - M, H - M - 4, f"{idx} / {n}")
    rule_y = H - M - 15
    c.setStrokeColorRGB(0.7, 0.7, 0.7); c.setLineWidth(0.7); c.line(M, rule_y, W - M, rule_y)
    # image region — 이미지 높이를 페이지 중앙선까지로 제한해 하단 절반은 항상 풀이공간
    region_top = rule_y - 12
    avail_w = W - 2 * M
    img_max_h = region_top - H * SOLVE_MIN_FRAC       # ≈ 234pt (하단 절반 확보)
    iw, ih = Image.open(it["path"]).size
    scale = min(avail_w / iw, img_max_h / ih)
    sw, sh = iw * scale, ih * scale
    x, y = M, region_top - sh
    c.drawImage(it["path"], x, y, width=sw, height=sh, mask="auto")
    # 풀이 공간 라벨(옅게): 항상 이미지 아래(하단 절반이 풀이공간)
    c.setFillColorRGB(0.78, 0.78, 0.78); c.setFont(BODY, 9)
    c.drawString(M, y - 16, "— 풀이 —")
    c.showPage()


def build_day(n):
    folder = os.path.join(DEST, f"6월 {n}일")
    if not os.path.isdir(folder):
        print(f"6월 {n}일: 폴더 없음, 건너뜀"); return
    items = [p for p in (parse_png(x) for x in glob.glob(os.path.join(folder, "*.png"))) if p]
    items.sort(key=lambda d: d["key"])
    if not items:
        print(f"6월 {n}일: PNG 없음, 건너뜀"); return
    title, concepts = read_md(folder)
    if not concepts:
        concepts = ["개념_*.pdf(슬라이드/치트시트)로 핵심 공식을 먼저 최종 점검한 뒤 풀이 시작"]
    out = os.path.join(folder, f"문제_6월{n}일.pdf")
    c = canvas.Canvas(out, pagesize=(W, H))
    draw_cover(c, title, concepts, items)
    for i, it in enumerate(items, 1):
        draw_problem(c, i, len(items), it)
    c.save()
    print(f"6월 {n}일: {len(items)}문제 → 문제_6월{n}일.pdf ({len(items)+1} pages)")


def main():
    for n in range(7, 17):
        build_day(n)


if __name__ == "__main__":
    main()
