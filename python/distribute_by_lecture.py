"""
Stage 3: classification.json 을 따라 problems_png/<id>.png 를
problems_by_lecture/<LectureNN_stem>/<id>.png 로 복사.

값 정상화: int ∈ [1,7] 만 강의 폴더로, 나머지(null/이상값)는 _Unclassified/.
"""

import os
import json
import glob
import shutil
import re

BASE = "Introduction to Probability, Statistics, and Random Processes"
PNG_DIR = os.path.join(BASE, "problems_png")
OUT = os.path.join(BASE, "problems_by_lecture")
CLASS_JSON = os.path.join(BASE, "classification.json")
NOTES = "notes"


def lecture_stems():
    out = {}
    for pdf in sorted(glob.glob(os.path.join(NOTES, "Lecture*.pdf"))):
        stem = os.path.splitext(os.path.basename(pdf))[0]
        m = re.match(r'Lecture(\d+)', stem)
        if m:
            n = int(m.group(1))
            out[n] = stem
    return out


def main():
    with open(CLASS_JSON, encoding='utf-8') as f:
        cls = json.load(f)

    stems = lecture_stems()
    # Create folders 1..7 + _Unclassified
    os.makedirs(OUT, exist_ok=True)
    for n, stem in stems.items():
        os.makedirs(os.path.join(OUT, stem), exist_ok=True)
    unclassified_dir = os.path.join(OUT, "_Unclassified")
    os.makedirs(unclassified_dir, exist_ok=True)

    counts = {stem: 0 for stem in stems.values()}
    counts["_Unclassified"] = 0
    missing_png = []

    for pid, n in cls.items():
        src = os.path.join(PNG_DIR, f"{pid}.png")
        if not os.path.exists(src):
            missing_png.append(pid)
            continue
        if isinstance(n, int) and 1 <= n <= 7 and n in stems:
            dst_dir = os.path.join(OUT, stems[n])
            label = stems[n]
        else:
            dst_dir = unclassified_dir
            label = "_Unclassified"
        shutil.copy2(src, os.path.join(dst_dir, f"{pid}.png"))
        counts[label] += 1

    print("Distribution:")
    for label in sorted(counts):
        print(f"  {label}: {counts[label]}")
    if missing_png:
        print(f"\nMissing source PNGs: {missing_png}")
    total = sum(counts.values())
    print(f"\nTotal distributed: {total}")


if __name__ == '__main__':
    main()
