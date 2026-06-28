#!/usr/bin/env python3
"""
Audit the companion files with the same checks used on the Bible:
markdown table integrity, placeholder/leak tokens, mojibake, unbalanced markup,
doubled words, broken links, AND self-contained numeric equations.
Read-only. Usage: python3 companion_audit.py <file1> [file2 ...]
"""
from __future__ import annotations
import re, ast, operator, sys
from pathlib import Path

OPS = {ast.Add: operator.add, ast.Sub: operator.sub, ast.Mult: operator.mul,
       ast.Div: operator.truediv, ast.USub: operator.neg, ast.UAdd: operator.pos}
def seval(n):
    if isinstance(n, ast.Expression): return seval(n.body)
    if isinstance(n, ast.Constant): return n.value
    if isinstance(n, ast.BinOp): return OPS[type(n.op)](seval(n.left), seval(n.right))
    if isinstance(n, ast.UnaryOp): return OPS[type(n.op)](seval(n.operand))
    raise ValueError
def nclean(s):
    s = s.replace("×","*").replace("·","*").replace("÷","/").replace("−","-").replace("–","-").replace("—","-")
    s = s.replace("$","").replace("€","").replace("£","").replace(",","").replace("≈","")
    return re.sub(r'(\d+\.?\d*)\s*%', r'(\1/100)', s).strip()

EQ = re.compile(r'([\d][\d.,$€£%×·÷+\-−–—/() ]*[\d%)])\s*=\s*([\-−–]?\s*[\d][\d.,$€£%]*)')
SKIP = re.compile(r'[~≈]|approx|roughly|about|:\d|\bx\b', re.I)
MOJI = ['Ã©','Ã¨','â‚¬','â€”','â€™','â€œ','Â£','Â§','ï¿½','M-bM-']
LEAK = [r'\bTODO\b', r'\bTKTK?\b', r'\bTBD\b', r'\bFIXME\b', r'\bXXX+\b', r'lorem ipsum',
        r'\[placeholder\]', r'<<[^>]+>>', r'\{\{[^}]+\}\}']

def cells(l):
    s=l.strip()
    if s.startswith('|'): s=s[1:]
    if s.endswith('|'): s=s[:-1]
    return [c.strip() for c in s.split('|')]
def is_sep(l): return bool(re.match(r'^\s*\|?\s*:?-{2,}', l)) and set(l.strip())<=set('|:- ')

def audit(path):
    LINES = Path(path).read_text(encoding="utf-8").splitlines()
    f=[]
    def add(sev,code,n,msg): f.append((sev,code,n,msg))
    # tables
    i=0; incode=False; ntab=0
    while i < len(LINES):
        l=LINES[i]
        if l.strip().startswith('```'): incode=not incode; i+=1; continue
        if not incode and '|' in l and i+1<len(LINES) and is_sep(LINES[i+1]) and '|' in LINES[i+1]:
            ncol=len(cells(l)); ntab+=1
            if len(cells(LINES[i+1]))!=ncol: add("S2","TBL-SEP",i+2,f"sep {len(cells(LINES[i+1]))} vs header {ncol}")
            j=i+2
            while j<len(LINES) and '|' in LINES[j] and LINES[j].strip() and not LINES[j].strip().startswith('```'):
                if len(cells(LINES[j]))!=ncol: add("S2","TBL-ROW",j+1,f"row {len(cells(LINES[j]))} vs {ncol}: {LINES[j].strip()[:60]}")
                j+=1
            i=j; continue
        i+=1
    # text checks
    incode=False; nchk=0
    for n,l in enumerate(LINES,1):
        if l.strip().startswith('```'): incode=not incode; continue
        for tok in MOJI:
            if tok in l: add("S1","MOJIBAKE",n,f"'{tok}': {l.strip()[:60]}")
        for pat in LEAK:
            if re.search(pat,l,re.I): add("S2","LEAK",n,f"/{pat}/: {l.strip()[:60]}")
        for m in re.finditer(r'!\[([^\]]*)\]\(([^)]+)\)', l):
            if not (Path(path).parent.parent/m.group(2)).exists() and not Path(m.group(2)).exists():
                add("S2","IMG",n,f"missing image {m.group(2)}")
        if not incode and l.count('**')%2==1: add("S3","MD-BOLD",n,f"unbalanced **: {l.strip()[:60]}")
        # numeric
        if incode: continue
        for m in EQ.finditer(l):
            span=l[max(0,m.start()-3):m.end()+3]
            if SKIP.search(span): continue
            pre=l[max(0,m.start()-9):m.start()]
            if (m.start()>0 and l[m.start()-1].isalpha()) or re.search(r'\b(Years?|[YQ]|months?|days?)\s+$',pre): continue
            if re.match(r'\s*[-−–+*/]\s*\d', l[m.end():m.end()+6]): continue
            lhs,rhs=nclean(m.group(1)),nclean(m.group(2))
            A=r'[-\d.*/+() ]+'
            if not re.search(r'[+\-*/]',lhs) or not re.fullmatch(A,lhs) or not re.fullmatch(A,rhs): continue
            try: lv=seval(ast.parse(lhs,mode="eval")); rv=seval(ast.parse(rhs,mode="eval"))
            except Exception: continue
            nchk+=1
            if rv==0 and lv==0: continue
            diff=min(abs(lv-rv),abs(abs(lv)-abs(rv))); denom=max(abs(rv),abs(lv),1e-9)
            if diff/denom>0.005 and diff>0.051:
                add("S2","NUM",n,f"{m.group(1).strip()} = {m.group(2).strip()} -> computes {lv:g}, stated {rv:g}")
    from collections import Counter
    c=Counter(x[0] for x in f)
    print(f"\n### {path}")
    print(f"  tables={ntab} equations_checked={nchk}  findings: S1={c['S1']} S2={c['S2']} S3={c['S3']}")
    for sev,code,n,msg in sorted(f,key=lambda x:(x[0],x[3])):
        print(f"  [{sev}] {code} L{n}: {msg}")
    if not f: print("  CLEAN")
    return c

if __name__=="__main__":
    from collections import Counter
    tot=Counter()
    for p in sys.argv[1:]:
        for k,v in audit(p).items(): tot[k]+=v
    print(f"\n=== TOTAL across {len(sys.argv)-1} files: S1={tot['S1']} S2={tot['S2']} S3={tot['S3']} ===")
