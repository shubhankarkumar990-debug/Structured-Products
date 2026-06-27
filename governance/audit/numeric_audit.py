#!/usr/bin/env python3
"""
Tier-3 numeric re-derivation audit — read-only.
Extracts self-contained arithmetic equations from the Bible and verifies each
computes correctly. Targets the class the linter/structure checks cannot see:
wrong coupon decompositions, payoff arithmetic, loss/gain maths.

Method: find substrings of the form  <expr> = <number>  where <expr> contains an
explicit operator (× + − / and parenthesised %), strip $ , % (dimensionless and
cancels across =), evaluate the LHS with a safe AST, compare to the stated RHS
within a rounding tolerance. Equations with ~ ≈ ranges or words are skipped
(not self-contained / intentionally approximate).
"""
from __future__ import annotations
import re, ast, operator
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
LINES = (ROOT / "Desk_Bible_v2.md").read_text(encoding="utf-8").splitlines()

OPS = {ast.Add: operator.add, ast.Sub: operator.sub, ast.Mult: operator.mul,
       ast.Div: operator.truediv, ast.USub: operator.neg, ast.UAdd: operator.pos}

def safe_eval(node):
    if isinstance(node, ast.Expression): return safe_eval(node.body)
    if isinstance(node, ast.Constant): return node.value
    if isinstance(node, ast.BinOp): return OPS[type(node.op)](safe_eval(node.left), safe_eval(node.right))
    if isinstance(node, ast.UnaryOp): return OPS[type(node.op)](safe_eval(node.operand))
    raise ValueError("bad node")

def clean(s):
    s = s.replace("×", "*").replace("·", "*").replace("÷", "/")
    s = s.replace("−", "-").replace("–", "-").replace("—", "-")
    s = s.replace("$", "").replace("€", "").replace("£", "").replace(",", "").replace("≈", "")
    # percent is dimensionless: convert "N%" -> "(N/100)" on BOTH sides so decimals & percents compare
    s = re.sub(r'(\d+\.?\d*)\s*%', r'(\1/100)', s)
    return s.strip()

# candidate equation: run of math chars containing an operator and a single '='
EQ = re.compile(r'([\d][\d.,$€£%×·÷+\-−–—/() ]*[\d%)])\s*=\s*([\-−–]?\s*[\d][\d.,$€£%]*)')
SKIP = re.compile(r'[~≈]|approx|roughly|about|×?\s*10\^|:\d|\bx\b', re.I)

findings = []
checked = 0
for n, line in enumerate(LINES, 1):
    # skip obvious non-arithmetic contexts
    for m in EQ.finditer(line):
        lhs_raw, rhs_raw = m.group(1), m.group(2)
        span = line[max(0, m.start()-3):m.end()+3]
        if SKIP.search(span):
            continue
        # skip year/period ranges like "Y2-5" or "Years 2-5 = 4 × …" (range, not subtraction)
        pre = line[max(0, m.start()-9):m.start()]
        if (m.start() > 0 and line[m.start()-1].isalpha()) or re.search(r'\b(Years?|[YQ]|months?|days?)\s+$', pre):
            continue
        # skip chained equations "… = 1 − 0.8153 = 18.5%" (RHS continues into another operator)
        if re.match(r'\s*[-−–+*/]\s*\d', line[m.end():m.end()+6]):
            continue
        lhs, rhs = clean(lhs_raw), clean(rhs_raw)
        ALLOWED = r'[-\d.*/+() ]+'
        if not re.search(r'[+\-*/]', lhs):          # LHS must contain an operator
            continue
        if not re.fullmatch(ALLOWED, lhs) or not re.fullmatch(ALLOWED, rhs):
            continue
        try:
            lv = safe_eval(ast.parse(lhs, mode="eval"))
            rv = safe_eval(ast.parse(rhs, mode="eval"))
        except Exception:
            continue
        checked += 1
        if rv == 0 and lv == 0:
            continue
        # match either signed or on magnitude (book sometimes annotates a loss with a leading −)
        d_signed = abs(lv - rv)
        d_abs = abs(abs(lv) - abs(rv))
        diff = min(d_signed, d_abs)
        denom = max(abs(rv), abs(lv), 1e-9)
        rel = diff / denom
        # tolerance: 0.5% relative OR 0.051 absolute (rounding at one decimal / 0.05%)
        if rel > 0.005 and diff > 0.051:
            findings.append((n, lhs_raw.strip() + " = " + rhs_raw.strip(),
                             f"LHS computes to {lv:g}, stated {rv:g}"))

print("=" * 72)
print("TIER-3 NUMERIC AUDIT — Desk_Bible_v2.md")
print(f"equations checked: {checked}   mismatches: {len(findings)}")
print("=" * 72)
for n, eq, msg in findings:
    print(f"[L{n}] {eq}   →  {msg}")
if not findings:
    print("CLEAN — every self-contained equation computes within tolerance.")
