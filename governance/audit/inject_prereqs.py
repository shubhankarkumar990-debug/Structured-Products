#!/usr/bin/env python3
"""Inject a linked 'Prerequisites' line under each Bible product chapter heading,
sourced from learning_dependency_graph.md. Idempotent."""
import re
from pathlib import Path

dep = Path("production/learning_dependency_graph.md").read_text(encoding="utf-8").splitlines()
rows=[]
for l in dep:
    m=re.match(r'^\|\s*(5\.\d+\.\d+)\s*\|\s*([^|]+?)\s*\|\s*\d+\s*\|\s*([^|]*?)\s*\|\s*([^|]*?)\s*\|', l)
    if m: rows.append((m.group(1), m.group(2).strip(), m.group(3).strip(), m.group(4).strip()))
# code -> section
code2sec={}
for sec,name,_,_ in rows:
    cm=re.search(r'\(([^)]+)\)\s*$', name)
    if cm: code2sec[cm.group(1).strip().upper()]=sec
def anchor(sec): return "sec-"+sec.replace(".","-")
# section -> prereq line
prereq_line={}
for sec,name,prereqs,concepts in rows:
    parts=[]
    if prereqs and prereqs!="—":
        for code in re.split(r'[,/]| and ', prereqs):
            code=code.strip().upper()
            if code in code2sec:
                tsec=code2sec[code]; parts.append(f"[{code}](#{anchor(tsec)})")
            elif code:
                parts.append(code)
    prod_links = " · ".join(parts) if parts else "none — a foundation product, start here"
    concept_txt = f" &nbsp;|&nbsp; **Key concepts:** {concepts}" if concepts else ""
    prereq_line[sec]=f"> **Prerequisites:** {prod_links}{concept_txt}"

# inject into Bible
B=Path("Desk_Bible_v2.md"); lines=B.read_text(encoding="utf-8").splitlines()
out=[]; i=0; n=0
while i<len(lines):
    out.append(lines[i])
    m=re.match(r'^### (5\.\d+\.\d+) .*\{#sec-[0-9-]+\}\s*$', lines[i])
    if m and m.group(1) in prereq_line:
        # skip if next non-blank already a prerequisites line
        nxt=i+1
        while nxt<len(lines) and lines[nxt].strip()=="": nxt+=1
        if nxt>=len(lines) or "**Prerequisites:**" not in lines[nxt]:
            out.append(""); out.append(prereq_line[m.group(1)]); n+=1
    i+=1
B.write_text("\n".join(out)+"\n", encoding="utf-8")
print(f"prereq lines injected: {n} | products mapped: {len(code2sec)}")
