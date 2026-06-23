# -*- coding: utf-8 -*-
"""
기말고사 대비 '시험지' 폴더(주제별 선별 5문제) PNG 정제.
refine_pngs.py / refine_lecture_pngs.py 와 동일 파이프라인:
  (1) content-bbox autocrop : 바깥 여백 제거(내부 들여쓰기·수식 보존) — C1 해결
  (2) 컬럼 reflow           : 오른쪽 컬럼으로 밀려난 가로 밴드를 좌측 마진으로 평행이동 — C2 해결
  (3) dirty 후보 판정(보고) : 내부 세로갭 ≥ GAP_FLAG
원본은 _png_원본백업/시험지/<폴더명>/ 에 1회 백업하고, 정제는 항상 그 백업(pristine)에서
읽어 처리 → 멱등(재실행해도 동일), 백업은 절대 덮어쓰지 않음.
"""
import os, glob, shutil
import numpy as np
from PIL import Image, ImageOps

ROOT = r"C:\Users\Hyunjun\Desktop\현준대학\확랜"
DEST = os.path.join(ROOT, "기말고사 대비")
BACKUP = os.path.join(DEST, "_png_원본백업", "시험지")

FOLDERS = [
    "L09_CLT_표본평균_5문제_시험지",
    "L01-06_중간범위_5문제_시험지",
    "L07_파생분포_합성곱_5문제_시험지",
    "L08_공분산_조건부기댓값_5문제_시험지",
]

THR = 240          # gray < THR → 잉크
K = 3              # 한 행/열 잉크 ≥ K 이어야 '내용'
PAD = 14           # 크롭 후 사방 흰 여백
GAPBAND = 22       # 가로 밴드 분리 빈 행 수
GAP_FLAG = 70      # 내부 세로갭 → dirty 후보
REFLOW_FLOOR = 180 # 본 강의 실측: 우측컬럼/들여쓴블록=off≥208, 중앙정렬 단독수식=off≤156 분리

# 눈으로 확인해 깨끗하다고 판정된 파일(문단/구분선 여백 때문에 갭만 큼) — 후보 제외.
REVIEWED_CLEAN = {
    "Q03_L09_IPSRP_7.3.5.png", "Q05_L09_IPSRP_7.3.4.png",
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


def reflow(im):
    """오른쪽 컬럼으로 밀려난 가로 밴드를 좌측 마진으로 평행이동(세로 위치 보존)."""
    g = np.asarray(im.convert("L"))
    H, W = g.shape
    ink = g < THR
    rowc = ink.sum(axis=1) >= K
    colany = ink.sum(axis=0) >= K
    xs = np.where(colany)[0]
    if not xs.size:
        return im, False
    gmin = int(xs[0])
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


def process(backup_path, out_path):
    im = Image.open(backup_path)
    if im.mode not in ("L", "RGB"):
        im = im.convert("RGB")
    before = im.size
    im = crop_tight(im)
    im, did = reflow(im)
    if did:
        im = crop_tight(im)
    fill = 255 if im.mode == "L" else (255, 255, 255)
    im = ImageOps.expand(im, border=PAD, fill=fill)
    tmp = out_path + ".tmp.png"
    im.save(tmp); os.replace(tmp, out_path)
    return before, im.size, did, internal_gap(im)


def main():
    total = reflowed = 0
    flagged = []
    for folder in FOLDERS:
        src_dir = os.path.join(DEST, folder)
        bdir = os.path.join(BACKUP, folder)
        os.makedirs(bdir, exist_ok=True)
        for out_path in sorted(glob.glob(os.path.join(src_dir, "*.png"))):
            total += 1
            name = os.path.basename(out_path)
            bpath = os.path.join(bdir, name)
            if not os.path.exists(bpath):                 # 최초 1회: pristine 백업
                shutil.copy2(out_path, bpath)
            before, after, did, gap = process(bpath, out_path)
            tag = "reflow" if did else "      "
            print(f"  [{tag}] {folder[:8]} {name:30s} {before[0]}x{before[1]} -> {after[0]}x{after[1]}  gap={gap}")
            if did:
                reflowed += 1
            if gap >= GAP_FLAG and name not in REVIEWED_CLEAN:
                flagged.append((folder, name, after, gap))
    print(f"\n정제 {total}장 · 컬럼 reflow {reflowed}장 · dirty 후보 {len(flagged)}장")
    rep = os.path.join(DEST, "_재크롭_후보_시험지.md")
    out = ["# 시험지 폴더 수동 재크롭 후보 (autocrop·reflow로 못 고침)", "",
           f"> 판정: 내부 세로 여백 갭 ≥ {GAP_FLAG}px. 원본은 `_png_원본백업/시험지/`.", "",
           "| 폴더 | 파일 | 크기 | 내부갭px |", "|---|---|---|---|"]
    for f, nm, sz, gp in flagged:
        out.append(f"| {f} | {nm} | {sz[0]}x{sz[1]} | {gp} |")
    if not flagged:
        out.append("| (없음) | | | |")
    open(rep, "w", encoding="utf-8").write("\n".join(out) + "\n")
    print("후보 ->", rep)


if __name__ == "__main__":
    main()
