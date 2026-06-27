#!/usr/bin/env python3
"""
Full-document integrity sweep of Desk_Bible_v2.md — read-only.
Error classes NOT covered by the semantic linter or Tier-1 structural audit:
  markdown table integrity, empty-header tables (render-killers),
  placeholder/leak tokens, broken embeds, unbalanced inline markup,
  encoding/mojibake, doubled words, dangling links.
Emits a severity-ranked report. Touches nothing.
"""
from __future__ import annotations
import re, sys
from pathlib import Path
from collections import Counter

ROOT = Path(__file__).resolve().parents[2]
BIBLE = ROOT / "Desk_Bible_v2.md"
LINES = BIBLE.read_text(encoding="utf-8").splitlines()

findings = []
def add(sev, code, line, msg): findings.append((sev, code, line, msg))

# ---------- 1. Markdown table integrity ----------
# A pipe table: header row, separator row (---), then data rows.
def is_sep(l): return bool(re.match(r'^\s*\|?\s*:?-{2,}.*$', l)) and set(l.strip()) <= set('|:- ')
def cells(l):
    s = l.strip()
    if s.startswith('|'): s = s[1:]
    if s.endswith('|'): s = s[:-1]
    return [c.strip() for c in s.split('|')]

i = 0
in_code = False
tables = 0
while i < len(LINES):
    l = LINES[i]
    if l.strip().startswith('```'):
        in_code = not in_code; i += 1; continue
    if not in_code and '|' in l and i + 1 < len(LINES) and is_sep(LINES[i+1]) and '|' in LINES[i+1]:
        # table starts
        hdr = cells(l); ncol = len(hdr); sepc = len(cells(LINES[i+1]))
        tables += 1
        start = i + 1
        if sepc != ncol:
            add("S2", "TBL-SEPCOL", start, f"table separator has {sepc} cols, header has {ncol}.")
        if all(h == '' for h in hdr):
            add("S3", "TBL-EMPTYHDR", start, f"table header row entirely empty ({ncol} cols) — pandoc render risk.")
        j = i + 2
        while j < len(LINES) and '|' in LINES[j] and LINES[j].strip() and not LINES[j].strip().startswith('```'):
            rc = len(cells(LINES[j]))
            if rc != ncol:
                add("S2", "TBL-ROWCOL", j + 1, f"data row has {rc} cells, header has {ncol}: {LINES[j].strip()[:70]}")
            j += 1
        i = j; continue
    i += 1

# ---------- 2. Placeholder / leak tokens ----------
LEAK = [r'\bTODO\b', r'\bTKTK?\b', r'\bTBD\b', r'\bFIXME\b', r'\bXXX+\b',
        r'\blorem ipsum\b', r'\[placeholder\]', r'\bplaceholder\b',
        r'\bINSERT[ _]', r'\bdraft only\b', r'<<[^>]+>>', r'\{\{[^}]+\}\}']
for n, l in enumerate(LINES, 1):
    for pat in LEAK:
        if re.search(pat, l, re.I):
            add("S2", "LEAK", n, f"placeholder/leak token /{pat}/: {l.strip()[:80]}")

# ---------- 3. Broken embeds & dangling links ----------
for n, l in enumerate(LINES, 1):
    for m in re.finditer(r'!\[([^\]]*)\]\(([^)]+)\)', l):
        if not (ROOT / m.group(2)).exists():
            add("S1", "IMG-MISSING", n, f"image not found: {m.group(2)}")
    # markdown link with empty target
    for m in re.finditer(r'(?<!\!)\[([^\]]+)\]\(\s*\)', l):
        add("S3", "LINK-EMPTY", n, f"empty link target: [{m.group(1)}]()")

# ---------- 4. Encoding / mojibake ----------
MOJI = ['Ã©', 'Ã¨', 'â‚¬', 'â€”', 'â€™', 'â€œ', 'â€\x9d', 'Â£', 'Â§', 'ï¿½', 'M-bM-']
for n, l in enumerate(LINES, 1):
    for tok in MOJI:
        if tok in l:
            add("S1", "MOJIBAKE", n, f"mojibake '{tok}': {l.strip()[:80]}")

# ---------- 5. Unbalanced inline markup (bold / code) ----------
in_code = False
for n, l in enumerate(LINES, 1):
    if l.strip().startswith('```'): in_code = not in_code; continue
    if in_code: continue
    if l.count('`') % 2 == 1 and '``' not in l:
        add("S3", "MD-BACKTICK", n, f"odd number of backticks: {l.strip()[:70]}")
    # bold ** count must be even
    if l.count('**') % 2 == 1:
        add("S3", "MD-BOLD", n, f"unbalanced ** : {l.strip()[:70]}")

# ---------- 6. Doubled words ----------
DBL = re.compile(r'\b(\w+)\s+\1\b', re.I)
ALLOW = {'that', 'had', 'is', 'the', 'a', 'no', 's', 'long', 'short', 'very', 'sic', 'do', 'wagga', 'boola', 'pago', 'bora', 'aye', 'di', 'so',
         'modified', 'mod'}  # "Modified Modified Restructuring (MMR / Mod Mod R)" is a real ISDA term
in_code = False
for n, l in enumerate(LINES, 1):
    if l.strip().startswith('```'): in_code = not in_code; continue
    if in_code or l.strip().startswith('|') or l.strip().startswith('!['): continue
    for m in DBL.finditer(l):
        w = m.group(1).lower()
        if w not in ALLOW and not w.isdigit() and len(w) > 2:
            add("S3", "DBLWORD", n, f"doubled word '{m.group(1)} {m.group(1)}': …{l[max(0,m.start()-20):m.end()+20].strip()}…")

# ---------- report ----------
order = {"S1": 0, "S2": 1, "S3": 2}
findings.sort(key=lambda x: (order[x[0]], x[1], x[2]))
c = Counter(s for s, *_ in findings)
print("=" * 72)
print("FULL-DOCUMENT INTEGRITY SWEEP — Desk_Bible_v2.md")
print(f"lines={len(LINES)}  tables_scanned={tables}")
print(f"findings: S1={c['S1']} S2={c['S2']} S3={c['S3']}")
print("=" * 72)
for sev, code, line, msg in findings:
    print(f"[{sev}] {code} L{line}: {msg}")
if not findings:
    print("CLEAN — no integrity findings.")
