# -*- coding: utf-8 -*-
"""
기말고사 대비 PNG 정제 — (1) content-bbox autocrop + (2) 2단(컬럼) reflow.
- autocrop: 바깥 여백 제거(내부 들여쓰기·수식 보존).
- reflow: 교재 2단 레이아웃 때문에 '오른쪽 컬럼'으로 밀려난 가로 밴드를
  좌측 본문 마진으로 끌어옴(세로 위치는 보존 → 수식/줄간격 안 깨짐).
  단, 살짝 들여쓴 수식 등은 건드리지 않도록 큰 이동량(>임계)만 reflow.
- 원본은 _png_원본백업/ 에서 읽어 매번 깨끗하게 재처리(멱등).
- 다요소/ dirty crop(그래프·인접조각 혼입)은 reflow로 못 고치므로 후보 목록만 보고.
"""
import os, glob, shutil
import numpy as np
from PIL import Image, ImageOps

ROOT = r"C:\Users\Hyunjun\Desktop\현준대학\확랜"
DEST = os.path.join(ROOT, "기말고사 대비")
BACKUP = os.path.join(DEST, "_png_원본백업")
THR = 240
K = 3
PAD = 14
GAPBAND = 22        # 가로 밴드 분리 빈 행 수
GAP_FLAG = 70       # 내부 세로 갭 → dirty 후보
# 눈으로 확인해 깨끗하다고 판정된 파일(문단/구분선 여백 때문에 갭만 큼) — 후보에서 제외
REVIEWED_CLEAN = {
    "L08_PSP_7.6.3.png", "L09_IPSRP_7.3.2.png", "L09_IPSRP_7.3.4.png",
    "L09_IPSRP_7.3.5.png", "L06_PSP_5.5.1.png",
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
    """오른쪽 컬럼으로 밀려난 밴드를 좌측 마진으로 이동(세로 위치 보존)."""
    g = np.asarray(im.convert("L"))
    H, W = g.shape
    ink = g < THR
    rowc = ink.sum(axis=1) >= K
    colany = ink.sum(axis=0) >= K
    xs = np.where(colany)[0]
    if not xs.size:
        return im, False
    gmin = int(xs[0])
    # 가로 밴드 분리
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
    thr = max(120, int(0.22 * W))
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
    for n in range(7, 17):
        folder = os.path.join(DEST, f"6월 {n}일")
        if not os.path.isdir(folder):
            continue
        for out_path in sorted(glob.glob(os.path.join(folder, "*.png"))):
            total += 1
            name = os.path.basename(out_path)
            bdir = os.path.join(BACKUP, f"6월 {n}일")
            bpath = os.path.join(bdir, name)
            if not os.path.exists(bpath):                 # 최초 1회: 현재본을 원본으로 백업
                os.makedirs(bdir, exist_ok=True); shutil.copy2(out_path, bpath)
            before, after, did, gap = process(bpath, out_path)
            if did:
                reflowed += 1
            if gap >= GAP_FLAG and name not in REVIEWED_CLEAN:
                flagged.append((f"6월 {n}일", name, after, gap))
    print(f"정제 {total}장 · 컬럼 reflow {reflowed}장 · dirty 후보 {len(flagged)}장")
    rep = os.path.join(DEST, "_재크롭_후보.md")
    out = ["# 수동 재크롭 후보 (그래프·인접조각 혼입 등 — autocrop·reflow로 못 고침)", "",
           f"> 판정: 내부 세로 여백 갭 ≥ {GAP_FLAG}px. 원본은 `_png_원본백업/`.", "",
           "| 폴더 | 파일 | 크기 | 내부갭px |", "|---|---|---|---|"]
    for f, nm, sz, gp in flagged:
        out.append(f"| {f} | {nm} | {sz[0]}x{sz[1]} | {gp} |")
    if not flagged:
        out.append("| (없음) | | | |")
    open(rep, "w", encoding="utf-8").write("\n".join(out) + "\n")
    print("후보 ->", rep)


if __name__ == "__main__":
    main()
