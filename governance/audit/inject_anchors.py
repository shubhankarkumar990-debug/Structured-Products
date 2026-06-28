#!/usr/bin/env python3
"""Inject stable pandoc anchors {#id} on Part and numbered-section headings. Idempotent."""
import re, sys
from pathlib import Path
def anchor_id(m_part=None, nums=None):
    if m_part: return f"part-{m_part}"
    return "sec-" + "-".join(nums)
def process(path):
    lines = Path(path).read_text(encoding="utf-8").splitlines()
    out=[]; added=0
    for l in lines:
        if "{#" in l:                      # already anchored
            out.append(l); continue
        mp = re.match(r'^# (?:PART|Part) (\d+)\b', l)
        ms = re.match(r'^(#{2,3}) (\d+)\.(\d+)(?:\.(\d+))?\s', l)
        if mp:
            l = l.rstrip() + f" {{#part-{mp.group(1)}}}"; added+=1
        elif ms:
            nums=[g for g in ms.groups()[1:] if g]
            l = l.rstrip() + f" {{#sec-{'-'.join(nums)}}}"; added+=1
        out.append(l)
    Path(path).write_text("\n".join(out)+"\n", encoding="utf-8")
    return added
for p in sys.argv[1:]:
    n=process(p); print(f"{p}: {n} anchors added")
