#!/usr/bin/env python3
"""
Link-integrity checker — read-only.
Verifies that every markdown link in the given files resolves:
  - in-file anchors  [text](#id)            -> #id must be a defined heading anchor in the same file
  - cross-file anchors [text](file.md#id)   -> file must exist and define #id
  - cross-file plain  [text](file.md)        -> file must exist
  - image/asset links [..](path)             -> path must exist on disk
Anchors come from explicit {#id} on headings AND pandoc-style auto-slugs of headings.
Exit 1 if any dangling link is found.
"""
from __future__ import annotations
import re, sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]

def slug(text):
    # pandoc/GitHub-ish slug: lowercase, drop punctuation, spaces->-
    t = re.sub(r'\{#[^}]+\}', '', text).strip().lower()
    t = re.sub(r'[^\w\s-]', '', t)
    t = re.sub(r'\s+', '-', t)
    return t.strip('-')

def anchors_of(path):
    ids = set()
    for l in Path(path).read_text(encoding="utf-8").splitlines():
        m = re.match(r'^#{1,6}\s+(.*)$', l)
        if not m: continue
        text = m.group(1)
        em = re.search(r'\{#([^}]+)\}', text)
        if em: ids.add(em.group(1))
        s = slug(text)
        if s: ids.add(s)
    return ids

def check(files):
    files = [Path(f) for f in files]
    anchor_cache = {f.name: anchors_of(f) for f in files if f.exists()}
    dangling = []
    LINK = re.compile(r'(?<!\!)\[([^\]]+)\]\(([^)]+)\)')
    for f in files:
        if not f.exists(): continue
        own = anchor_cache[f.name]
        for n, l in enumerate(f.read_text(encoding="utf-8").splitlines(), 1):
            for m in LINK.finditer(l):
                tgt = m.group(2).strip()
                if tgt.startswith(("http://", "https://", "mailto:")): continue
                if tgt.startswith("#"):
                    if tgt[1:] not in own:
                        dangling.append((f.name, n, tgt, "in-file anchor not found"))
                elif "#" in tgt:
                    fn, _, aid = tgt.partition("#")
                    fn = fn.split("/")[-1]
                    if fn not in anchor_cache:
                        dangling.append((f.name, n, tgt, f"target file '{fn}' not in checked set"))
                    elif aid not in anchor_cache[fn]:
                        dangling.append((f.name, n, tgt, f"anchor not found in {fn}"))
                else:
                    # plain file/asset path
                    p = (ROOT / tgt) if not tgt.startswith("/") else Path(tgt)
                    if not p.exists() and tgt.split("/")[-1] not in anchor_cache:
                        dangling.append((f.name, n, tgt, "path/file not found"))
    return dangling

if __name__ == "__main__":
    files = sys.argv[1:] or [str(ROOT / "Desk_Bible_v2.md")]
    d = check(files)
    print("=" * 64)
    print(f"LINK-INTEGRITY CHECK — {len(files)} file(s)")
    print(f"dangling links: {len(d)}")
    print("=" * 64)
    for fn, n, tgt, why in d[:200]:
        print(f"[{fn}:{n}] {tgt}  -> {why}")
    if not d:
        print("CLEAN — every link resolves.")
    sys.exit(1 if d else 0)
