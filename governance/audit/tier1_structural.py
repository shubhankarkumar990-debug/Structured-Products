#!/usr/bin/env python3
"""
Tier 1 structural audit of Desk_Bible_v2.md — read-only.
Checks: part structure, product numbering, cross-references, diagram embeds,
dual-lens parity, duplicate headings, per-product section signatures.
Emits a severity-ranked findings report. Touches nothing.
"""
from __future__ import annotations
import re, sys
from pathlib import Path
from collections import Counter, defaultdict

ROOT = Path(__file__).resolve().parents[2]
BIBLE = ROOT / "Desk_Bible_v2.md"
LINES = BIBLE.read_text(encoding="utf-8").splitlines()
N = len(LINES)

findings = []  # (severity, code, msg)
def add(sev, code, msg): findings.append((sev, code, msg))

# ---- heading index ---------------------------------------------------------
H = []  # (lineno, level, text)
for i, ln in enumerate(LINES, 1):
    m = re.match(r'^(#{1,6}) (.*)$', ln)
    if m:
        H.append((i, len(m.group(1)), m.group(2).strip()))

# ---- A. Level-1 part structure --------------------------------------------
l1 = [(i, t) for i, lvl, t in H if lvl == 1]
parts_seen = {}
for i, t in l1:
    m = re.match(r'^(?:PART|Part)\s+(\d+)', t)
    if m: parts_seen[int(m.group(1))] = (i, t)
for p in range(0, 8):
    if p not in parts_seen:
        # Part 6/7 content may exist at level-2; check
        has_content = any(re.match(rf'^{p}\.\d+', t) for _, lvl, t in H if lvl == 2)
        if has_content:
            add("S2", "STR-PARTBANNER",
                f"Part {p} content exists (## {p}.x) but has NO level-1 '# PART {p}' banner "
                f"— inconsistent with Parts 0–5 which all have one.")
        else:
            add("S2", "STR-PARTMISSING",
                f"Part {p} has neither a '# PART {p}' banner nor any '## {p}.x' content "
                f"— but it is referenced in front matter.")

# ---- B. Product numbering continuity --------------------------------------
prod = []  # (line, family, num, title)
for i, lvl, t in H:
    m = re.match(r'^5\.(\d+)\.(\d+)\s+(.*)$', t) if lvl == 3 else None
    if m: prod.append((i, int(m.group(1)), int(m.group(2)), m.group(3)))
fam = defaultdict(list)
for i, f, n_, title in prod: fam[f].append((n_, i, title))
total = 0
for f in sorted(fam):
    nums = sorted(x[0] for x in fam[f])
    total += len(nums)
    dupes = [n for n, c in Counter(nums).items() if c > 1]
    if dupes: add("S1", "STR-DUPNUM", f"Family 5.{f}: duplicate product numbers {dupes}.")
    gaps = [k for k in range(1, max(nums) + 1) if k not in nums]
    if gaps: add("S2", "STR-GAPNUM", f"Family 5.{f}: missing product numbers {gaps} (have 1..{max(nums)}).")
if total != 49:
    add("S2", "STR-PRODCOUNT", f"Product count = {total}, expected 49.")

# ---- C. Cross-references ---------------------------------------------------
prod_ids = {f"5.{f}.{n_}" for _, f, n_, _ in prod}
sec2 = {t.split()[0] for _, lvl, t in H if lvl == 2 and re.match(r'^\d+\.\d+', t)}
text = "\n".join(LINES)
# product refs like (5.6.12  or  5.5.4)
for m in re.finditer(r'\b5\.(\d+)\.(\d+)\b', text):
    pid = f"5.{m.group(1)}.{m.group(2)}"
    if pid not in prod_ids:
        add("S3", "XREF-PRODUCT", f"Reference to '{pid}' but no such product heading exists.")
# Part 7 / 7.5 references
for label in ("Part 7", "7.5"):
    if label.lower() in text.lower():
        cnt = len(re.findall(re.escape(label), text))
        if not any(t.startswith("7.") for t in sec2) and 7 not in parts_seen:
            add("S2", "XREF-PART7", f"Front matter references '{label}' ({cnt}x) but Part 7 does not exist in the document.")
            break

# ---- D. Diagram embeds -----------------------------------------------------
embeds = []  # (line, alt, path)
for i, ln in enumerate(LINES, 1):
    for m in re.finditer(r'!\[([^\]]*)\]\(([^)]+)\)', ln):
        embeds.append((i, m.group(1), m.group(2)))
missing = [(i, p) for i, a, p in embeds if not (ROOT / p).exists()]
for i, p in missing: add("S1", "IMG-MISSING", f"Line {i}: embedded image '{p}' not found on disk.")
pathcount = Counter(p for _, _, p in embeds)
for p, c in pathcount.items():
    if c > 1: add("S3", "IMG-DUP", f"Image '{p}' embedded {c}x (possible mis-calibration / copy-paste).")
on_disk = {str(p.relative_to(ROOT)) for p in ROOT.glob("assets/**/*.svg")}
embedded = {p for _, _, p in embeds}
orphans = sorted(on_disk - embedded)
for o in orphans: add("S4", "IMG-ORPHAN", f"SVG on disk never embedded: '{o}'.")

# ---- E. Dual-lens parity per product --------------------------------------
bounds = [i for i, _, _, _ in prod] + [next((i for i, lvl, t in H if lvl == 2 and t.startswith("6.1 ")), N)]
for idx, (i, f, n_, title) in enumerate(prod):
    start, end = i, bounds[idx + 1]
    block = "\n".join(LINES[start - 1:end - 1])
    need = {
        "investor lens": "THE INVESTOR LENS",
        "bank desk lens": "THE BANK LENS — Desk",
        "bank controls lens": "THE BANK LENS — Controls",
        "knowledge check": "Knowledge Check",
    }
    for label, marker in need.items():
        if marker not in block:
            add("S2", "PARITY", f"5.{f}.{n_} {title}: missing '{label}' ({marker}).")

# ---- F. Duplicate headings -------------------------------------------------
htext = Counter(t for _, _, t in H)
generic = {"Common Mistakes", "Lifecycle", "Knowledge Check", "Formal Definition",
           "Review Questions", "Scenario Questions", "Desk Question",
           # confirmed templated sub-headers reused across chapters (not splice dupes)
           "Why This Matters for Structured Products", "Desk Perspective",
           "Visual Learning Recommendations", "Dependency References",
           "Visual Specifications", "Visual Specifications (Publication Assets)"}
for t, c in htext.items():
    if c > 1 and t not in generic and not re.match(r'^§', t):
        # product-internal repeats of templated headers are fine; flag only suspicious ones
        if len(t) > 12 and not t.startswith(("§", "Group ", "Scenario", "Step")):
            add("S3", "DUP-HEADING", f"Heading '{t}' appears {c}x (check for splice duplication).")

# ---- G. Per-product section signature --------------------------------------
sigs = Counter()
for idx, (i, f, n_, title) in enumerate(prod):
    start, end = i, bounds[idx + 1]
    secs = tuple(sorted(int(m.group(1)) for ln in LINES[start - 1:end - 1]
                        for m in [re.match(r'^####\s+§(\d+)\.', ln)] if m))
    sigs[secs] += 1
# report the dominant signature and any deviations
if sigs:
    dom = sigs.most_common(1)[0][0]
    for idx, (i, f, n_, title) in enumerate(prod):
        start, end = i, bounds[idx + 1]
        secs = tuple(sorted(int(m.group(1)) for ln in LINES[start - 1:end - 1]
                            for m in [re.match(r'^####\s+§(\d+)\.', ln)] if m))
        if secs != dom:
            miss = sorted(set(dom) - set(secs)); extra = sorted(set(secs) - set(dom))
            add("S3", "SECSIG", f"5.{f}.{n_} {title}: section-number set deviates "
                f"(missing §{miss}, extra §{extra}).")

# ---- report ----------------------------------------------------------------
order = {"S1": 0, "S2": 1, "S3": 2, "S4": 3}
findings.sort(key=lambda x: (order[x[0]], x[1]))
counts = Counter(s for s, _, _ in findings)
print("=" * 70)
print("TIER 1 STRUCTURAL AUDIT — Desk_Bible_v2.md")
print(f"lines={N}  headings={len(H)}  products={total}  embeds={len(embeds)}")
print(f"findings: S1={counts['S1']} S2={counts['S2']} S3={counts['S3']} S4={counts['S4']}")
print("=" * 70)
for sev, code, msg in findings:
    print(f"[{sev}] {code}: {msg}")
if not findings:
    print("CLEAN — no structural findings.")
print("=" * 70)
print(f"dominant per-product section signature: §{list(sigs.most_common(1)[0][0]) if sigs else []}")
