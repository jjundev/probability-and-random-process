# -*- coding: utf-8 -*-
"""
problems_by_lecture/<LECTURE>/ 의 문제 PNG 정제.
기말고사 대비/refine_pngs.py 와 같은 파이프라인:
  (1) content-bbox autocrop  : 바깥 여백 제거(내부 들여쓰기·수식 보존) — C1 해결
  (2) 컬럼 reflow            : 오른쪽 컬럼으로 밀려난 가로 밴드를 좌측 마진으로 평행이동 — C2 해결
  (3) dirty 후보 판정(보고)  : 내부 세로갭 ≥ GAP_FLAG
추가:
  (0) dirty 수동 재크롭(restack): 그래프/해설/난이도범례 등 이물이 끼인 PNG는
      keep 블록(원본 y범위)만 골라 좌측정렬·수직결합 후 파이프라인에 태움.

원본은 problems_by_lecture/_png_원본백업/<LECTURE>/ 에 1회 백업하고, 정제는 항상
그 백업(pristine)에서 읽어 처리 → 멱등(재실행해도 동일), 백업은 절대 덮어쓰지 않음.
"""
import os, glob, shutil
import numpy as np
from PIL import Image, ImageOps

ROOT = r"C:\Users\Hyunjun\Desktop\현준대학\확랜"
BANK = os.path.join(ROOT, "Probability_and_Stochastic_Processes_Problems", "problems_by_lecture")
LECTURE = "Lecture10_Statistical_Inference_Part_1"
SRC = os.path.join(BANK, LECTURE)
BACKUP = os.path.join(BANK, "_png_원본백업", LECTURE)

THR = 240          # gray < THR → 잉크
K = 3              # 한 행/열 잉크 ≥ K 이어야 '내용'
PAD = 14           # 크롭 후 사방 흰 여백
GAPBAND = 22       # 가로 밴드 분리 빈 행 수
RESTACK_GAP = 22   # 재크롭 시 블록 사이 흰 간격
GAP_FLAG = 70      # 내부 세로갭 → dirty 후보

# dirty 수동 재크롭: 백업(pristine) 좌표 기준으로 '진짜 문제' 블록 y범위만 유지.
#   12.1.3 : (상단 본문 + a,b) + (하단 c~f). 가운데 이물(타문제 MMSE 조각·구분선·
#            [S01]조각·"Moderate/Difficult/Experts Only" 난이도범례)은 버림.
#   12.5.1 : 같은 문제이나 상단 헤더(~"...correlation ma-")와 본문("trix R_X..." 이하)
#            사이에 가로 구분선 + 168px 빈공간이 끼어 있어, 선·공백을 버리고 두 블록만 결합.
DIRTY_KEEP = {
    "12.1.3.png": [(18, 255), (870, 1068)],
    "12.5.1.png": [(19, 68), (236, 610)],
    "12.5.4.png": [(0, 390)],   # 본문만 유지, 맨 아래 문제구분 가로선(y403~) 제거
}

# 눈으로 확인해 깨끗하다고 판정(문단 여백/2단 reflow 잔여 여백 때문에 갭만 큼) — 후보 제외.
REVIEWED_CLEAN = {
    "12.2.1.png",   # 표 ↔ (a) 사이 정상 문단 여백(96px)
}


def bbox(g):
    ink = g < THR
    rows = ink.sum(axis=1) >= K
    cols = ink.sum(axis=0) >= K
    if not rows.any() or not cols.any():
        return None
    ys, xs = np.where(rows)[0], np.where(cols)[0]
    return int(xs[0]), int(ys[0]), int(xs[-1]), int(ys[-1])


def crop_tight(im):
    g = np.asarray(im.convert("L"))
    bb = bbox(g)
    if bb is None:
        return im
    l, t, r, b = bb
    return im.crop((l, t, r + 1, b + 1))


def restack(im, keep):
    """keep=[(y0,y1),...] 블록만 골라 각각 crop_tight(좌측정렬) 후 RESTACK_GAP 간격 수직결합."""
    blocks = [crop_tight(im.crop((0, y0, im.width, y1))) for (y0, y1) in keep]
    w = max(b.width for b in blocks)
    h = sum(b.height for b in blocks) + RESTACK_GAP * (len(blocks) - 1)
    fill = 255 if im.mode == "L" else (255, 255, 255)
    canvas = Image.new(im.mode, (w, h), fill)
    y = 0
    for b in blocks:
        canvas.paste(b, (0, y))
        y += b.height + RESTACK_GAP
    return canvas


def reflow(im):
    """오른쪽 컬럼으로 밀려난 가로 밴드를 좌측 마진으로 평행이동(세로 위치 보존).
    큰 이동량(>임계)만 옮겨 정상 들여쓰기는 보존. 옮기는 밴드는 우측-단독 밴드라 좌측내용 손실 없음."""
    g = np.asarray(im.convert("L"))
    H, W = g.shape
    ink = g < THR
    rowc = ink.sum(axis=1) >= K
    colany = ink.sum(axis=0) >= K
    xs = np.where(colany)[0]
    if not xs.size:
        return im, False
    gmin = int(xs[0])
    REFLOW_FLOOR = 180  # 본 강의 실측: 우측컬럼/들여쓴블록 = off≥208, 중앙정렬 단독수식 = off≤156.
                        # 120(원 파이프라인) 대신 180으로 두 군집을 분리 → 정상 중앙수식 보존.
    bands = []
    i = 0
    while i < H:
        if rowc[i]:
            j = i; blank = 0; last = i
            while j < H:
                if rowc[j]:
                    last = j; blank = 0
                else:
                    blank += 1
                    if blank >= GAPBAND:
                        break
                j += 1
            bands.append((i, last + 1)); i = j
        else:
            i += 1
    thr = max(REFLOW_FLOOR, int(0.22 * W))
    src = np.array(im)
    arr = src.copy()
    changed = False
    for t, b in bands:
        cols = ink[t:b].sum(axis=0) >= 1
        bxs = np.where(cols)[0]
        if not bxs.size:
            continue
        off = int(bxs[0]) - gmin
        if off > thr:
            arr[t:b, :] = 255
            arr[t:b, 0:W - off] = src[t:b, off:W]
            changed = True
    return (Image.fromarray(arr), True) if changed else (im, False)


def internal_gap(im):
    g = np.asarray(im.convert("L"))
    rows = (g < THR).sum(axis=1) >= K
    ys = np.where(rows)[0]
    if ys.size == 0:
        return 0
    mx = run = 0
    for y in range(int(ys[0]), int(ys[-1]) + 1):
        if not rows[y]:
            run += 1; mx = max(mx, run)
        else:
            run = 0
    return mx


def process(backup_path, out_path, name):
    im = Image.open(backup_path)
    if im.mode not in ("L", "RGB"):
        im = im.convert("RGB")
    before = im.size
    restacked = False
    if name in DIRTY_KEEP:
        im = restack(im, DIRTY_KEEP[name]); restacked = True
    im = crop_tight(im)
    im, did = reflow(im)
    if did:
        im = crop_tight(im)
    fill = 255 if im.mode == "L" else (255, 255, 255)
    im = ImageOps.expand(im, border=PAD, fill=fill)
    tmp = out_path + ".tmp.png"
    im.save(tmp); os.replace(tmp, out_path)
    return before, im.size, did, restacked, internal_gap(im)


def main():
    os.makedirs(BACKUP, exist_ok=True)
    total = reflowed = restacked_n = 0
    flagged = []
    for out_path in sorted(glob.glob(os.path.join(SRC, "*.png")),
                           key=lambda s: [int(x) for x in os.path.basename(s)[:-4].split(".")]):
        total += 1
        name = os.path.basename(out_path)
        bpath = os.path.join(BACKUP, name)
        if not os.path.exists(bpath):                 # 최초 1회: pristine 백업
            shutil.copy2(out_path, bpath)
        before, after, did, rst, gap = process(bpath, out_path, name)
        if did:
            reflowed += 1
        if rst:
            restacked_n += 1
        if gap >= GAP_FLAG and name not in REVIEWED_CLEAN:
            flagged.append((name, after, gap))
    print(f"정제 {total}장 · reflow {reflowed}장 · 재크롭 {restacked_n}장 · dirty 후보 {len(flagged)}장")
    rep = os.path.join(SRC, "_재크롭_후보.md")
    out = [f"# {LECTURE} 수동 재크롭 후보", "",
           f"> 판정: 내부 세로갭 ≥ {GAP_FLAG}px. 원본은 `_png_원본백업/{LECTURE}/`.", "",
           "| 파일 | 크기 | 내부갭px |", "|---|---|---|"]
    for nm, sz, gp in flagged:
        out.append(f"| {nm} | {sz[0]}x{sz[1]} | {gp} |")
    if not flagged:
        out.append("| (없음) | | |")
    open(rep, "w", encoding="utf-8").write("\n".join(out) + "\n")
    print("후보 ->", rep)


if __name__ == "__main__":
    main()
