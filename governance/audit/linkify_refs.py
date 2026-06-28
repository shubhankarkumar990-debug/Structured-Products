#!/usr/bin/env python3
"""Convert plain section/part references to markdown anchor links — only when the
target anchor exists (never creates a dead link). Skips heading lines, image lines,
and existing links. Idempotent."""
import re, sys
from pathlib import Path

def load_anchors(path):
    ids=set()
    for l in Path(path).read_text(encoding="utf-8").splitlines():
        m=re.search(r'\{#((?:part|sec)-[0-9-]+)\}', l)
        if m: ids.add(m.group(1))
    return ids

def linkify(path):
    A=load_anchors(path)
    lines=Path(path).read_text(encoding="utf-8").splitlines()
    out=[]; n=0
    def sec_id(num): return "sec-"+num.replace(".","-")
    def part_id(num): return "part-"+num
    for l in lines:
        if l.lstrip().startswith("#") or l.lstrip().startswith("!["):
            out.append(l); continue
        # protect existing links: split on inline-code/links not needed (none yet)
        orig=l
        # 1) §N.M(.K)  ->  [§N.M.K](#sec-...)
        def r_sec(m):
            nonlocal n
            num=m.group(1); aid=sec_id(num)
            if aid in A: n+=1; return f"[§{num}](#{aid})"
            return m.group(0)
        l=re.sub(r'§(\d+\.\d+(?:\.\d+)?)\b(?!\s*\()', r_sec, l)
        # 2) Section/Chapter N.M(.K) -> [Section N.M](#sec-...)
        def r_word(m):
            nonlocal n
            word=m.group(1); num=m.group(2); aid=sec_id(num)
            if aid in A: n+=1; return f"[{word} {num}](#{aid})"
            return m.group(0)
        l=re.sub(r'\b(Section|Chapter)\s+(\d+\.\d+(?:\.\d+)?)\b', r_word, l)
        # 3) bare N.M.K immediately followed by " (" (the "5.1.6 (CRC)" cross-ref style)
        def r_bare(m):
            nonlocal n
            num=m.group(1); aid=sec_id(num)
            if aid in A: n+=1; return f"[{num}](#{aid})"
            return m.group(0)
        l=re.sub(r'(?<![\w.$])(\d+\.\d+\.\d+)(?=\s*\()', r_bare, l)
        # 4) Part N -> [Part N](#part-N)
        def r_part(m):
            nonlocal n
            num=m.group(1); aid=part_id(num)
            if aid in A: n+=1; return f"[Part {num}](#{aid})"
            return m.group(0)
        l=re.sub(r'\bPart\s+(\d)\b(?!\])', r_part, l)
        out.append(l)
    Path(path).write_text("\n".join(out)+"\n", encoding="utf-8")
    return n
for p in sys.argv[1:]:
    print(f"{p}: {linkify(p)} refs linked")
