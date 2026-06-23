"""
Stage 1: 분류를 위한 텍스트/시러버스 추출.

산출물:
- Introduction to Probability, Statistics, and Random Processes/problem_texts.json
- Introduction to Probability, Statistics, and Random Processes/lecture_syllabi.json

reading-order 보존을 위해 get_text("dict") 블록을 (y, x) 정렬해 재구성한다.
"""

import os
import re
import json
import glob
import fitz

BASE = "Introduction to Probability, Statistics, and Random Processes"
SRC = os.path.join(BASE, "origin")
PNG_DIR = os.path.join(BASE, "problems_png")
NOTES = "notes"

PROBLEM_TEXTS_OUT = os.path.join(BASE, "problem_texts.json")
LECTURE_SYLLABI_OUT = os.path.join(BASE, "lecture_syllabi.json")

SECTION_RE = re.compile(r'(\d+(?:\.\d+)+)\s+(?:End of\s+)?Chapter Problems')
PROBLEM_RE = re.compile(r'^Problem\s+(\d+)$')
TRAILER_TEXT = "The print version of the book"
TOP_PAD = 6
FOOTER_PT = 30


def find_section_prefix(doc):
    for p in range(len(doc)):
        m = SECTION_RE.search(doc[p].get_text())
        if m:
            return m.group(1)
    return None


def find_problem_headers(doc):
    out = []
    for p_idx in range(len(doc)):
        page = doc[p_idx]
        for b in page.get_text('dict')['blocks']:
            if 'lines' not in b:
                continue
            for ln in b['lines']:
                for sp in ln['spans']:
                    t = sp['text'].strip()
                    m = PROBLEM_RE.fullmatch(t)
                    if m:
                        out.append((p_idx, sp['bbox'][1], int(m.group(1))))
    out.sort(key=lambda x: (x[0], x[1]))
    return out


def find_trailer(doc):
    for p in range(len(doc)):
        rects = doc[p].search_for(TRAILER_TEXT)
        if rects:
            return p, min(r.y0 for r in rects)
    return None


def normalize_prefix(prefix):
    return prefix[:-2] if prefix.endswith(".0") else prefix


def extract_region_text(doc, p_start, y_start, p_end, y_end):
    """Reading-order text from spans inside region across pages."""
    parts = []
    for p in range(p_start, p_end + 1):
        page = doc[p]
        H = page.rect.height
        if p == p_start and p == p_end:
            top, bot = y_start, y_end
        elif p == p_start:
            top, bot = y_start, H
        elif p == p_end:
            top, bot = 0, y_end
        else:
            top, bot = 0, H

        if bot - top < 2:
            continue

        lines = []
        for b in page.get_text('dict')['blocks']:
            if 'lines' not in b:
                continue
            for ln in b['lines']:
                spans = ln['spans']
                if not spans:
                    continue
                ly = min(sp['bbox'][1] for sp in spans)
                if not (top <= ly <= bot):
                    continue
                sorted_spans = sorted(spans, key=lambda s: s['bbox'][0])
                line_text = ''.join(s['text'] for s in sorted_spans).strip()
                if line_text:
                    lx = min(sp['bbox'][0] for sp in spans)
                    lines.append((ly, lx, line_text))
        lines.sort(key=lambda t: (round(t[0], 1), t[1]))
        if lines:
            parts.append('\n'.join(l[2] for l in lines))
    return '\n\n'.join(parts)


def extract_problem_texts():
    out = {}
    for pdf_path in sorted(glob.glob(os.path.join(SRC, "*.pdf"))):
        doc = fitz.open(pdf_path)
        prefix = find_section_prefix(doc)
        if prefix is None:
            doc.close()
            continue
        name_prefix = normalize_prefix(prefix)
        headers = find_problem_headers(doc)
        trailer = find_trailer(doc)
        if trailer is not None:
            last_p, last_y = trailer[0], trailer[1] - TOP_PAD
        else:
            last_p = len(doc) - 1
            last_y = doc[last_p].rect.height - FOOTER_PT

        for i, (p, y, n) in enumerate(headers):
            y_start = max(0, y - TOP_PAD)
            if i + 1 < len(headers):
                p_end = headers[i + 1][0]
                y_end = headers[i + 1][1] - TOP_PAD
            else:
                p_end = last_p
                y_end = last_y
            txt = extract_region_text(doc, p, y_start, p_end, y_end).strip()
            pid = f"{name_prefix}.{n}"
            out[pid] = {
                "text": txt,
                "png": os.path.join(PNG_DIR, f"{pid}.png").replace("\\", "/"),
            }
        doc.close()
        print(f"  {os.path.basename(pdf_path)}: prefix={name_prefix}, problems={len(headers)}")
    return out


def extract_lecture_syllabi():
    out = {}
    for pdf in sorted(glob.glob(os.path.join(NOTES, "Lecture*.pdf"))):
        stem = os.path.splitext(os.path.basename(pdf))[0]
        m = re.match(r'(Lecture\d+)', stem)
        label = m.group(1) if m else stem
        d = fitz.open(pdf)
        full = '\n'.join(d[p].get_text() for p in range(len(d)))
        d.close()
        out[label] = {"stem": stem, "text": full}
        print(f"  {stem}: {len(full)} chars")
    return out


def main():
    print("Extracting problem texts...")
    problems = extract_problem_texts()
    with open(PROBLEM_TEXTS_OUT, 'w', encoding='utf-8') as f:
        json.dump(problems, f, ensure_ascii=False, indent=2)
    print(f"  -> {PROBLEM_TEXTS_OUT} ({len(problems)} entries)")

    print("\nExtracting lecture syllabi...")
    syllabi = extract_lecture_syllabi()
    with open(LECTURE_SYLLABI_OUT, 'w', encoding='utf-8') as f:
        json.dump(syllabi, f, ensure_ascii=False, indent=2)
    print(f"  -> {LECTURE_SYLLABI_OUT} ({len(syllabi)} entries)")


if __name__ == '__main__':
    main()
