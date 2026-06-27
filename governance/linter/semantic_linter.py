#!/usr/bin/env python3
"""
Semantic Linter for the Structured Products Knowledge Ecosystem.

Implements all 22 rules from governance/semantic_linter_specification.md
(V1.0.1-GOV-1.0). Detects semantic defects: correlation-direction
self-contradictions, position/ownership errors, sign/arithmetic mistakes,
strike-vs-barrier confusions, cross-artifact inconsistencies, and missing
qualifiers.

Design goals:
  - Zero third-party dependencies (stdlib only) so it runs in any CI.
  - Deterministic, auditable output (JSON or text).
  - Documented false-positive suppression via inline comments:
        <!-- lint-disable LNT-COR-02 reason: describes structural convention -->
    A suppression applies to the line it is on and the next non-blank line.

Usage:
    python semantic_linter.py FILE [FILE ...]            # text report
    python semantic_linter.py --json FILE [FILE ...]     # JSON findings
    python semantic_linter.py --fail-on S1 FILE ...      # exit 1 if S1 found
    python semantic_linter.py --corpus DIR               # lint *.md under DIR

Exit codes:
    0  no findings at or above the --fail-on threshold
    1  findings at or above the threshold
    2  usage / IO error
"""

from __future__ import annotations

import argparse
import json
import re
import sys
from dataclasses import dataclass, asdict, field
from pathlib import Path
from typing import Callable, Iterable, Optional

SEVERITY_ORDER = {"S1": 1, "S2": 2, "S3": 3, "S4": 4}
SEVERITY_LABEL = {"S1": "BLOCK", "S2": "WARN", "S3": "INFO", "S4": "STYLE"}


# --------------------------------------------------------------------------- #
# Data model
# --------------------------------------------------------------------------- #
@dataclass
class Finding:
    rule_id: str
    severity: str
    file: str
    line: int
    matched_text: str
    message: str
    remediation: str
    regression_test: str = ""

    def to_dict(self) -> dict:
        return asdict(self)


@dataclass
class Document:
    """A parsed markdown artifact."""
    path: str
    name: str
    lines: list[str]              # 1-indexed access via self.line(n)
    suppressions: dict[int, set[str]] = field(default_factory=dict)

    def line(self, n: int) -> str:
        if 1 <= n <= len(self.lines):
            return self.lines[n - 1]
        return ""

    def window(self, n: int, before: int = 2, after: int = 2) -> str:
        """Context window: current line +/- neighbouring lines, joined by space."""
        lo = max(1, n - before)
        hi = min(len(self.lines), n + after)
        return " ".join(self.lines[lo - 1 : hi])

    def is_suppressed(self, line_no: int, rule_id: str) -> bool:
        return rule_id in self.suppressions.get(line_no, set())


SUPPRESS_RE = re.compile(
    r"<!--\s*lint-disable\s+(?P<rule>LNT-[A-Z]+-\d+)\s+reason:\s*(?P<reason>.+?)\s*-->",
    re.IGNORECASE,
)


def parse_document(path: Path) -> Document:
    text = path.read_text(encoding="utf-8", errors="replace")
    lines = text.split("\n")
    suppressions: dict[int, set[str]] = {}
    for i, ln in enumerate(lines, start=1):
        for m in SUPPRESS_RE.finditer(ln):
            rule = m.group("rule").upper()
            # Suppression covers its own line and the next non-blank line.
            suppressions.setdefault(i, set()).add(rule)
            j = i + 1
            while j <= len(lines) and lines[j - 1].strip() == "":
                j += 1
            if j <= len(lines):
                suppressions.setdefault(j, set()).add(rule)
    return Document(path=str(path), name=path.name, lines=lines, suppressions=suppressions)


# --------------------------------------------------------------------------- #
# Helpers
# --------------------------------------------------------------------------- #
def truncate(s: str, n: int = 160) -> str:
    s = s.strip()
    return s if len(s) <= n else s[: n - 1] + "…"


# Structured-note context markers (used by ownership rules to avoid flagging
# legitimate standalone-CDS desk-sold-protection statements).
STRUCTNOTE_MARKERS = re.compile(
    r"\b(RC|WOAC|CLN|FTD|reverse convertible|worst-of|autocall(?:able)?|"
    r"structured note|phoenix|FCN|ELN|barrier note)\b",
    re.IGNORECASE,
)
CDS_CONTEXT = re.compile(r"\b(CDS|credit default swap|standalone)\b", re.IGNORECASE)
STRUCTURALLY = re.compile(r"\bstructural(?:ly)?\b", re.IGNORECASE)
RAW_HEDGED = re.compile(r"\b(raw|unhedged|net|hedged)\b", re.IGNORECASE)


def eval_arith(expr: str) -> Optional[float]:
    """Safely evaluate a simple arithmetic expression. Returns None on failure.

    Normalises unicode operators and only permits digits, + - * / ( ) . and ws.
    """
    norm = (
        expr.replace("×", "*")  # ×
        .replace("⋅", "*")      # ⋅
        .replace("x", "*")
        .replace("X", "*")
        .replace("−", "-")      # − minus sign
        .replace("–", "-")      # – en dash
        .replace("—", "-")      # — em dash
        .replace("≈", "")       # ≈
        .replace("=", "")
    )
    if not re.fullmatch(r"[0-9+\-*/().\s]+", norm):
        return None
    if not re.search(r"[+\-*/]", norm):
        return None
    try:
        return eval(norm, {"__builtins__": {}}, {})  # noqa: S307 - sanitised above
    except Exception:
        return None


# --------------------------------------------------------------------------- #
# Per-line / per-window rules
# --------------------------------------------------------------------------- #
# Each rule is a function(doc, line_no) -> Optional[Finding].
RuleFn = Callable[[Document, int], Optional[Finding]]
LINE_RULES: list[tuple[str, str, str, RuleFn]] = []


def line_rule(rule_id: str, severity: str, reg_test: str):
    def deco(fn: RuleFn):
        LINE_RULES.append((rule_id, severity, reg_test, fn))
        return fn
    return deco


# ---- CATEGORY 1: CORRELATION DIRECTION --------------------------------------
@line_rule("LNT-COR-01", "S1", "REG-COR-01")
def lnt_cor_01(doc, n):
    win = doc.window(n)
    if STRUCTURALLY.search(win):
        return None
    # long correlation + negative outcome + rising correlation, same subject heuristic
    if re.search(
        r"long correlation.{0,200}?(harm|hurt|lose|los[es]|decrease|worsen|risk increases)"
        r".{0,80}?(correlation (?:rise|rises|high|increase|increases))",
        win, re.IGNORECASE | re.DOTALL,
    ):
        # crude same-subject filter: a different explicit subject between clauses
        return _mk(doc, n, "LNT-COR-01", "S1",
                   "Long correlation paired with loss from rising correlation (label/economics conflict)",
                   "Verify subject matches across clauses; if same subject, the label is wrong.",
                   "REG-COR-01")
    return None


@line_rule("LNT-COR-02", "S1", "REG-COR-02")
def lnt_cor_02(doc, n):
    line = doc.line(n)
    if STRUCTURALLY.search(line):
        return None
    # same-line: "short correlation ... profit/benefit ... high/rises"
    if re.search(
        r"short correlation.{0,200}?(benefit|profit|gain|improve|risk decreases)"
        r".{0,120}?(correlation (?:is )?(?:rise|rises|high|increase|increases)|"
        r"high correlation|move together|stocks move together)",
        line, re.IGNORECASE,
    ):
        return _mk(doc, n, "LNT-COR-02", "S1",
                   "Short correlation label contradicts benefit from rising correlation",
                   "Change to 'long correlation' or add 'structurally' qualifier.",
                   "REG-COR-02")
    # also catch reversed clause order: "benefit from high correlation ... SHORT correlation"
    if re.search(
        r"\bshort correlation\b.{0,180}?(they )?benefit.{0,60}?high correlation",
        line, re.IGNORECASE,
    ):
        return _mk(doc, n, "LNT-COR-02", "S1",
                   "Short correlation label contradicts benefit from high correlation",
                   "Change to 'long correlation' or add 'structurally' qualifier.",
                   "REG-COR-02")
    return None


@line_rule("LNT-COR-03", "S2", "REG-COR-03")
def lnt_cor_03(doc, n):
    win = doc.window(n)
    if STRUCTURALLY.search(win):
        return None
    if re.search(
        r"(sold|sell|selling).{0,120}?correlation (?:premium|risk|exposure)"
        r".{0,160}?(short|long) correlation",
        win, re.IGNORECASE | re.DOTALL,
    ):
        return _mk(doc, n, "LNT-COR-03", "S2",
                   "Premium-selling language with correlation label lacks 'structurally' qualifier",
                   "Add 'structurally' before 'short/long correlation'.",
                   "REG-COR-03")
    return None


@line_rule("LNT-COR-06", "S1", "REG-COR-01")
def lnt_cor_06(doc, n):
    line = doc.line(n)
    # Require FTD to be the SUBJECT labeled short, i.e. "FTD [investors] is/are
    # [credit] short correlation" — not "a portfolio of FTDs and NTDs where long
    # and short correlation positions offset" (FTD not the labeled subject).
    if re.search(
        r"\bFTD\b(?:\s+(?:investors?|note|basket|tranche|\(N=1\)))?\s+"
        r"(?:is|are)\s+(?:\w+\s+){0,2}?short (?:\w+ )?correlation",
        line, re.IGNORECASE,
    ):
        seg = line[max(0, line.lower().find("ftd")):]
        if STRUCTURALLY.search(seg):
            return None
        return _mk(doc, n, "LNT-COR-06", "S1",
                   "FTD labeled 'short correlation' without 'structurally' qualifier",
                   "Change to 'long correlation' (MTM) or add 'structurally'.",
                   "REG-COR-01")
    # Table-row form: "| FTD (N=1) | ... | Short correlation ... |"
    # Guard: a comparison line like "FTD is long correlation; the NTD is short
    # correlation" is correct — the 'short' belongs to the NTD, not the FTD.
    if re.search(r"\|\s*FTD\b.*\bshort correlation", line, re.IGNORECASE) \
            and not STRUCTURALLY.search(line) \
            and not re.search(r"FTD\b[^|]*\blong correlation", line, re.IGNORECASE):
        return _mk(doc, n, "LNT-COR-06", "S1",
                   "FTD table row labeled 'short correlation' (MTM: FTD is long correlation)",
                   "Change to 'long correlation' (MTM).",
                   "REG-COR-01")
    return None


@line_rule("LNT-COR-07", "S1", "REG-COR-05")
def lnt_cor_07(doc, n):
    line = doc.line(n)
    # NTD products (N>=2) must never be labeled long correlation.
    for m in re.finditer(r"\b([2-9]TD|NTD|nth-to-default)\b", line, re.IGNORECASE):
        seg = line[m.start(): m.start() + 100]
        mlong = re.search(r"long correlation", seg, re.IGNORECASE)
        if mlong:
            pre = seg[: mlong.start()]
            # Guard: skip (a) comparison sentences where FTD owns the 'long' label,
            # (b) where the NTD is already correctly labeled 'short' before it, and
            # (c) desk/bank raw-or-net position statements ("the desk is long
            # correlation where the investor is short") — those are POS-rule territory.
            if re.search(r"\bFTD\b", pre, re.IGNORECASE) or \
               re.search(r"short correlation", pre, re.IGNORECASE) or \
               re.search(r"\b(desk|bank|dealer|raw|net|hedged)\b", pre, re.IGNORECASE):
                continue
            return _mk(doc, n, "LNT-COR-07", "S1",
                       f"{m.group(1)} labeled 'long correlation' — NTD (N>=2) is short correlation under MTM",
                       "Change to 'short correlation'.",
                       "REG-COR-05")
    return None


@line_rule("LNT-COR-08", "S1", "REG-COR-08")
def lnt_cor_08(doc, n):
    win = doc.window(n, 1, 1)
    if STRUCTURALLY.search(win):
        return None
    if re.search(r"worst-of.{0,150}?investor.{0,80}?short correlation", win,
                 re.IGNORECASE | re.DOTALL):
        return _mk(doc, n, "LNT-COR-08", "S1",
                   "Worst-of investor labeled 'short correlation' without 'structurally'",
                   "Change to 'long correlation' or add 'structurally'.",
                   "REG-COR-08")
    # invert order: "investor ... short correlation ... worst-of"
    if re.search(r"investor.{0,80}?short correlation.{0,150}?worst-of", win,
                 re.IGNORECASE | re.DOTALL):
        return _mk(doc, n, "LNT-COR-08", "S1",
                   "Worst-of investor labeled 'short correlation' without 'structurally'",
                   "Change to 'long correlation' or add 'structurally'.",
                   "REG-COR-08")
    return None


@line_rule("LNT-COR-09", "S1", "REG-COR-07")
def lnt_cor_09(doc, n):
    line = doc.line(n)
    if re.search(
        r"long single-stock.{0,80}?short basket.{0,80}?long correlation",
        line, re.IGNORECASE,
    ):
        return _mk(doc, n, "LNT-COR-09", "S1",
                   "Dispersion trade (long single-stock vol + short basket vol) mislabeled 'long correlation'",
                   "Change 'long correlation' to 'short correlation'.",
                   "REG-COR-07")
    return None


@line_rule("LNT-COR-10", "S2", "REG-COR-09")
def lnt_cor_10(doc, n):
    line = doc.line(n)
    if not re.search(r"\b([2-9]TD|NTD|nth-to-default)\b", line, re.IGNORECASE):
        return None
    if re.search(r"\breversal\b.{0,40}?at (?:high|low|moderate) (?:ρ|rho)", line, re.IGNORECASE):
        # Allow if it clarifies FTD-vs-NTD difference.
        if re.search(r"reversal.{0,80}?(FTD|between FTD)", line, re.IGNORECASE):
            return None
        return _mk(doc, n, "LNT-COR-10", "S2",
                   "'Reversal at <level> rho' implies a within-product direction flip that does not exist",
                   "Clarify that 'reversal' means the FTD-vs-NTD direction difference.",
                   "REG-COR-09")
    return None


# ---- CATEGORY 2: POSITION / OWNERSHIP ---------------------------------------
@line_rule("LNT-POS-01", "S2", "REG-POS-01")
def lnt_pos_01(doc, n):
    # Single line only (a ±2-line window bleeds 'desk' across unrelated table rows).
    line = doc.line(n)
    # 'structurally' disambiguates the raw (pre-hedge) position, so it counts as a
    # qualifier here alongside raw/unhedged/net/hedged.
    if RAW_HEDGED.search(line) or STRUCTURALLY.search(line):
        return None
    # Exempt glossary/definition rows whose first cell IS the term being defined,
    # e.g. "| Long Correlation | Benefiting from herding — the desk profits ... |".
    if re.match(r"^\s*\|\s*(long|short)\s+correlation\s*\|", line, re.IGNORECASE):
        return None
    # Exempt quoted student-vocabulary examples, e.g. Saying "I'm long correlation".
    if re.search(r"['\"][^'\"]*\b(long|short) correlation\b[^'\"]*['\"]", line, re.IGNORECASE):
        return None
    if re.search(r"(desk|bank|dealer).{0,120}?(long|short) correlation", line, re.IGNORECASE):
        return _mk(doc, n, "LNT-POS-01", "S2",
                   "Desk correlation position stated without raw/unhedged or net/hedged qualifier",
                   "Add 'raw/unhedged' or 'net/hedged' qualifier.",
                   "REG-POS-01")
    return None


@line_rule("LNT-PRO-01", "S1", "REG-PRO-01")
def lnt_pro_01(doc, n):
    line = doc.line(n)
    if not re.search(r"(desk|bank|dealer)", line, re.IGNORECASE):
        return None
    if re.search(r"(desk|bank|dealer).{0,80}?(sold|sells|selling) (?:the )?protection",
                 line, re.IGNORECASE) or re.search(r"which sold protection", line, re.IGNORECASE):
        if CDS_CONTEXT.search(line):
            return None
        if STRUCTNOTE_MARKERS.search(line) or STRUCTNOTE_MARKERS.search(doc.window(n, 2, 0)):
            return _mk(doc, n, "LNT-PRO-01", "S1",
                       "Desk described as protection seller in a structured-note context",
                       "Investor sold protection; the desk bought protection (is long the put).",
                       "REG-PRO-01")
    return None


@line_rule("LNT-PRO-03", "S1", "REG-PRO-03")
def lnt_pro_03(doc, n):
    line = doc.line(n)
    # Require the desk to be described AS short the put (a position), not the noun
    # phrase "short put premium/value/option" (the premium on the embedded put).
    if re.search(
        r"(desk|bank|dealer)\b.{0,40}?\b(is|are|'s|was|were|remains?)?\s*short "
        r"(?:the )?put(?:\s+(?:position|exposure|leg))?\b",
        line, re.IGNORECASE,
    ):
        if re.search(r"short (?:the )?put\s+(premium|value|option|price)", line, re.IGNORECASE):
            return None  # noun phrase, not a position claim
        if re.search(r"hedging book|hedge book", line, re.IGNORECASE):
            return None
        if STRUCTNOTE_MARKERS.search(line) or STRUCTNOTE_MARKERS.search(doc.window(n, 2, 0)):
            return _mk(doc, n, "LNT-PRO-03", "S1",
                       "Desk described as short the put in a structured note (the desk is long the put)",
                       "In structured notes the desk is LONG the embedded put.",
                       "REG-PRO-03")
    return None


# ---- CATEGORY 3: SIGN / ARITHMETIC ------------------------------------------
@line_rule("LNT-SGN-01", "S1", "REG-SGN-01")
def lnt_sgn_01(doc, n):
    line = doc.line(n)
    # Tie the comparison to a named reference (strike/barrier) so unrelated
    # percentage pairs in prose ("70% of days ... spikes above 120%") don't fire.
    # "X% ... above [the] strike/barrier (Y%)" where X < Y  (false 'above' claim)
    for m in re.finditer(
        r"(\d+(?:\.\d+)?)\s*%[:\s][^.\n]{0,15}?\babove\b\s+(?:the\s+)?"
        r"(?:strike|barrier|level)\b[^.\n]{0,15}?\(?(\d+(?:\.\d+)?)\s*%",
        line, re.IGNORECASE,
    ):
        a, b = float(m.group(1)), float(m.group(2))
        if a < b:
            return _mk(doc, n, "LNT-SGN-01", "S1",
                       f"Arithmetic impossibility: {m.group(1)}% claimed 'above' the {m.group(2)}% reference",
                       "Correct the comparison direction (it is below, not above).",
                       "REG-SGN-01")
    # symmetrical: "X% ... below [the] strike/barrier (Y%)" where X > Y
    for m in re.finditer(
        r"(\d+(?:\.\d+)?)\s*%[:\s][^.\n]{0,15}?\bbelow\b\s+(?:the\s+)?"
        r"(?:strike|barrier|level)\b[^.\n]{0,15}?\(?(\d+(?:\.\d+)?)\s*%",
        line, re.IGNORECASE,
    ):
        a, b = float(m.group(1)), float(m.group(2))
        if a > b:
            return _mk(doc, n, "LNT-SGN-01", "S1",
                       f"Arithmetic impossibility: {m.group(1)}% claimed 'below' the {m.group(2)}% reference",
                       "Correct the comparison direction (it is above, not below).",
                       "REG-SGN-01")
    return None


# Arithmetic chain checker shared by LNT-SGN-02 and LNT-SGN-03.
#
# Strategy: split the line on '=' into segments, then for each consecutive pair
# compare the TRAILING numeric expression of the left segment with the LEADING
# numeric expression of the right segment. Segments that are not pure arithmetic
# (contain letters, $, %, commas-as-thousands, stray brackets) are skipped, so
# prose, ranges ("2-5 years"), and formulas with functions (ln, exp) never fire.
# A rounding tolerance keyed to the displayed precision prevents flagging
# legitimately rounded values (e.g. "184 / 360 = 0.51111").

_ARITH_CHARS = r"0-9.+\-*/×xX⋅()−–—\s"
_TRAILING_RE = re.compile(rf"[{_ARITH_CHARS}]+$")
_LEADING_RE = re.compile(rf"^[{_ARITH_CHARS}]+")


def _pure_eval(s: str) -> Optional[float]:
    s = s.strip().strip("*").strip()
    if not s or not re.search(r"\d", s):
        return None
    # Require a BINARY operator (digit, operator, then digit/paren) — so a bare
    # parenthesised signed number like "(-0.4695)" (the argument of N(.)) is not
    # mistaken for a computation.
    if not re.search(r"\d\s*[+*/×xX⋅\-]\s*[-−–(]?\s*[\d(]", s):
        return None
    if s.count("(") != s.count(")"):
        return None
    return eval_arith(s)


def _decimals(token: str) -> int:
    m = re.search(r"\.(\d+)", token)
    return len(m.group(1)) if m else 0


def _check_arith_chain(doc, n, rule_id, reg_test, require_keyword=None):
    raw_line = doc.line(n)
    if require_keyword and not re.search(require_keyword, raw_line, re.IGNORECASE):
        return None
    if "=" not in raw_line:
        return None
    # Strip thousands separators ("4,500" -> "4500") so comma grouping does not
    # truncate operands. Applied repeatedly for "1,400,000".
    line = raw_line
    for _ in range(4):
        line = re.sub(r"(\d),(\d{3})(?=\D|$)", r"\1\2", line)
    segments = line.split("=")
    for i in range(len(segments) - 1):
        left, right = segments[i], segments[i + 1]
        lt = _TRAILING_RE.search(left)
        ld = _LEADING_RE.search(right)
        if not lt or not ld:
            continue
        lhs = _pure_eval(lt.group(0))
        # right operand: numeric token at the start of the right segment
        rhs_token = ld.group(0).strip()
        rhs = _pure_eval(rhs_token)
        if rhs is None:
            # plain number (no operator) is fine as a stated result
            t = rhs_token.strip().strip("*").replace("−", "-").replace("–", "-").replace(" ", "")
            try:
                rhs = float(t)
            except ValueError:
                rhs = None
        if lhs is None or rhs is None:
            continue
        # Percent result: "= 24%" means 0.24 when compared to a ratio.
        after = right[ld.end():].lstrip()
        is_pct = after.startswith("%")
        if is_pct and abs(lhs) <= 1.5 and abs(rhs) > 1.5:
            rhs = rhs / 100.0
        # rounding tolerance: half a unit in the last displayed decimal place,
        # plus a small relative tolerance for long division results.
        dp = _decimals(rhs_token)
        abs_tol = 0.5 * (10 ** (-dp)) if dp else 0.5
        rel_tol = 2e-3 * max(1.0, abs(lhs))
        if abs(lhs - rhs) > max(abs_tol, rel_tol, 1e-6):
            return _mk(doc, n, rule_id, "S1",
                       f"Arithmetic mismatch: '{truncate(lt.group(0).strip(),40)}' = {lhs:g}, "
                       f"but stated {rhs:g}",
                       "Fix the intermediate step or the final answer (include operand signs).",
                       reg_test)
    return None


@line_rule("LNT-SGN-02", "S1", "REG-SGN-02")
def lnt_sgn_02(doc, n):
    # Gamma sign drop: arithmetic chain check restricted to gamma/delta context.
    return _check_arith_chain(doc, n, "LNT-SGN-02", "REG-SGN-02",
                              require_keyword=r"gamma|delta")


@line_rule("LNT-SGN-03", "S1", "REG-SGN-03")
def lnt_sgn_03(doc, n):
    # General intermediate-vs-final arithmetic consistency (skip gamma/delta;
    # those are owned by SGN-02 to avoid double-flagging).
    line = doc.line(n)
    if re.search(r"gamma|delta", line, re.IGNORECASE):
        return None
    return _check_arith_chain(doc, n, "LNT-SGN-03", "REG-SGN-03")


# ---- CATEGORY 4: STRIKE / BARRIER -------------------------------------------
@line_rule("LNT-STR-01", "S2", "REG-STR-01")
def lnt_str_01(doc, n):
    line = doc.line(n)
    # Word-boundaried verbs (so "across" never matches "cross") and a SINGULAR
    # "the strike" (not "all strikes" — a strip of option strikes is legitimate).
    if re.search(r"\b(hit|breach|touch|cross|observe)e?s?\b\s+(?:the\s+)?strike\b",
                 line, re.IGNORECASE) and not re.search(r"strikes\b", line, re.IGNORECASE):
        if re.search(r"at maturity|on the maturity|final|expiry|expiration", line, re.IGNORECASE):
            return None
        if re.search(r"during|observation period|intraday|continuously observ|knock",
                     line, re.IGNORECASE):
            return _mk(doc, n, "LNT-STR-01", "S2",
                       "'Hit/breach the strike' during the product's life — likely means the barrier",
                       "Change 'strike' to 'barrier' if describing during-life observation.",
                       "REG-STR-01")
    return None


# LNT-STR-02 (undefined strike in worked example) is table-structural; handled
# at document level in document_rules().


# --------------------------------------------------------------------------- #
# Document-level rules (tables, cross-table)
# --------------------------------------------------------------------------- #
def parse_md_tables(doc: Document):
    """Yield (header_line_no, header_cells, [(row_line_no, cells), ...])."""
    i = 1
    N = len(doc.lines)
    while i <= N:
        line = doc.line(i)
        if "|" in line and i + 1 <= N and re.match(r"^\s*\|?[\s:|-]+\|?\s*$", doc.line(i + 1)) \
                and "-" in doc.line(i + 1):
            header = [c.strip() for c in line.strip().strip("|").split("|")]
            rows = []
            j = i + 2
            while j <= N and "|" in doc.line(j) and doc.line(j).strip():
                cells = [c.strip() for c in doc.line(j).strip().strip("|").split("|")]
                rows.append((j, cells))
                j += 1
            yield (i, header, rows)
            i = j
        else:
            i += 1


def document_rules(doc: Document) -> list[Finding]:
    findings: list[Finding] = []

    # LNT-XAR-03: within-artifact label-table vs risk-table inconsistency for NTD.
    # Heuristic: find a coupon/correlation-sensitivity table and a risk-vs-rho table
    # in the same doc; if a product is labeled "long correlation" while the risk
    # table shows its risk rising with rho, flag.
    label_rows = {}   # product -> (line, direction)
    risk_rows = {}    # product -> (line, risk_low_rho, risk_high_rho)
    for hdr_line, header, rows in parse_md_tables(doc):
        hdr_join = " ".join(header).lower()
        if "correlation sensitivity" in hdr_join or "correlation" in hdr_join:
            corr_idx = next((k for k, h in enumerate(header)
                             if "correlation" in h.lower()), None)
            prod_idx = 0
            if corr_idx is not None:
                for rln, cells in rows:
                    if len(cells) <= corr_idx:
                        continue
                    prod = re.search(r"\b(FTD|[2-9]TD|NTD)\b", cells[prod_idx], re.IGNORECASE)
                    if prod:
                        label = cells[corr_idx].lower()
                        if "long correlation" in label:
                            label_rows[prod.group(1).upper()] = (rln, "long")
                        elif "short correlation" in label:
                            label_rows[prod.group(1).upper()] = (rln, "short")
        # risk-vs-rho table: header has rho columns
        if re.search(r"ρ|rho", hdr_join):
            # crude: detect low/high rho columns
            for rln, cells in rows:
                prod = re.search(r"\b(FTD|[2-9]TD|NTD)\b", cells[0], re.IGNORECASE)
                if prod and len(cells) >= 3:
                    risk_rows[prod.group(1).upper()] = (rln, cells)

    for prod, (lln, direction) in label_rows.items():
        # NTD (N>=2) labeled long is always wrong (also caught by COR-07, but this
        # is the cross-table consistency finding).
        if prod != "FTD" and direction == "long":
            findings.append(Finding(
                "LNT-XAR-03", "S1", doc.name, lln,
                truncate(doc.line(lln)),
                f"{prod} labeled 'long correlation' contradicts NTD risk-rises-with-rho behaviour",
                "Align the label table with the risk table (NTD N>=2 is short correlation).",
                "REG-COR-06"))

    return findings


# --------------------------------------------------------------------------- #
# Corpus-level cross-artifact rules
# --------------------------------------------------------------------------- #
def corpus_rules(docs: list[Document]) -> list[Finding]:
    findings: list[Finding] = []

    def find_lines(pattern, flags=re.IGNORECASE):
        hits = []
        rx = re.compile(pattern, flags)
        for d in docs:
            for i, ln in enumerate(d.lines, 1):
                if rx.search(ln):
                    hits.append((d, i, ln))
        return hits

    # LNT-XAR-02: ownership inconsistency — one artifact says desk sold protection
    # in a structured-note context (already flagged per-line by PRO-01); the corpus
    # rule confirms cross-artifact disagreement with investor-sold-protection.
    desk_sold = [(d, i, ln) for (d, i, ln) in find_lines(r"(desk|dealer|bank).{0,40}sold protection")
                 if STRUCTNOTE_MARKERS.search(ln) and not CDS_CONTEXT.search(ln)]
    investor_sold = find_lines(r"investor.{0,40}sold (?:the )?(?:embedded )?(?:put|protection)")
    if desk_sold and investor_sold:
        for d, i, ln in desk_sold:
            findings.append(Finding(
                "LNT-XAR-02", "S1", d.name, i, truncate(ln),
                "Desk-sold-protection conflicts with investor-sold-protection elsewhere in corpus",
                "In structured notes the investor sells protection; correct the desk wording.",
                "REG-PRO-02"))

    # LNT-XAR-01: same concept (worst-of correlation) labeled opposite across
    # artifacts without raw/hedged qualifiers.
    wo_long = [(d, i, ln) for (d, i, ln) in find_lines(r"worst-of.{0,60}long correlation")
               if not RAW_HEDGED.search(ln)]
    wo_short = [(d, i, ln) for (d, i, ln) in find_lines(r"worst-of.{0,60}short correlation")
                if not RAW_HEDGED.search(ln)]
    if wo_long and wo_short:
        for d, i, ln in (wo_long + wo_short):
            findings.append(Finding(
                "LNT-XAR-01", "S1", d.name, i, truncate(ln),
                "Worst-of correlation labeled opposite across artifacts without raw/hedged qualifier",
                "Add raw/unhedged or net/hedged qualifiers to both statements.",
                "REG-POS-03"))

    return findings


# --------------------------------------------------------------------------- #
# Engine
# --------------------------------------------------------------------------- #
def _mk(doc, n, rule_id, severity, message, remediation, reg_test) -> Optional[Finding]:
    if doc.is_suppressed(n, rule_id):
        return None
    return Finding(rule_id, severity, doc.name, n,
                   truncate(doc.line(n)), message, remediation, reg_test)


def lint_documents(docs: list[Document]) -> list[Finding]:
    findings: list[Finding] = []
    for doc in docs:
        for n in range(1, len(doc.lines) + 1):
            for rule_id, severity, reg_test, fn in LINE_RULES:
                if doc.is_suppressed(n, rule_id):
                    continue
                try:
                    f = fn(doc, n)
                except Exception as e:  # a rule bug should not crash the run
                    f = Finding(rule_id, severity, doc.name, n, "",
                                f"[linter-internal-error] {e}", "Report to maintainers", reg_test)
                if f:
                    findings.append(f)
        findings.extend(document_rules(doc))
    findings.extend(corpus_rules(docs))
    # de-duplicate (rule_id, file, line)
    seen = set()
    unique = []
    for f in sorted(findings, key=lambda x: (x.file, x.line, SEVERITY_ORDER.get(x.severity, 9))):
        key = (f.rule_id, f.file, f.line)
        if key in seen:
            continue
        seen.add(key)
        unique.append(f)
    return unique


# --------------------------------------------------------------------------- #
# CLI
# --------------------------------------------------------------------------- #
def collect_files(args) -> list[Path]:
    files: list[Path] = []
    if args.corpus:
        files.extend(sorted(Path(args.corpus).rglob("*.md")))
    for f in args.files:
        p = Path(f)
        if p.is_dir():
            files.extend(sorted(p.rglob("*.md")))
        else:
            files.append(p)
    # de-dup, keep order
    seen, out = set(), []
    for p in files:
        rp = p.resolve()
        if rp not in seen:
            seen.add(rp)
            out.append(p)
    return out


def main(argv: Optional[list[str]] = None) -> int:
    ap = argparse.ArgumentParser(description="Semantic linter for the SP knowledge ecosystem.")
    ap.add_argument("files", nargs="*", help="Markdown files or directories to lint.")
    ap.add_argument("--corpus", help="Directory to recursively lint (*.md).")
    ap.add_argument("--json", action="store_true", help="Emit JSON findings.")
    ap.add_argument("--fail-on", default="S1", choices=["S1", "S2", "S3", "S4", "none"],
                    help="Minimum severity that causes a non-zero exit (default S1).")
    args = ap.parse_args(argv)

    paths = collect_files(args)
    if not paths:
        print("No input files.", file=sys.stderr)
        return 2

    docs = []
    for p in paths:
        try:
            docs.append(parse_document(p))
        except OSError as e:
            print(f"Cannot read {p}: {e}", file=sys.stderr)
            return 2

    findings = lint_documents(docs)

    if args.json:
        print(json.dumps([f.to_dict() for f in findings], ensure_ascii=False, indent=2))
    else:
        if not findings:
            print(f"✓ Clean: {len(docs)} file(s), 0 findings.")
        else:
            for f in findings:
                print(f"[{f.severity}/{SEVERITY_LABEL[f.severity]}] {f.rule_id}  "
                      f"{f.file}:{f.line}  ({f.regression_test})")
                print(f"    {f.message}")
                print(f"    > {f.matched_text}")
                print(f"    fix: {f.remediation}")
        counts = {}
        for f in findings:
            counts[f.severity] = counts.get(f.severity, 0) + 1
        summary = ", ".join(f"{k}:{counts.get(k,0)}" for k in ("S1", "S2", "S3", "S4"))
        print(f"\nSummary: {len(findings)} finding(s) across {len(docs)} file(s) [{summary}]")

    if args.fail_on == "none":
        return 0
    threshold = SEVERITY_ORDER[args.fail_on]
    blocking = [f for f in findings if SEVERITY_ORDER.get(f.severity, 9) <= threshold]
    return 1 if blocking else 0


if __name__ == "__main__":
    raise SystemExit(main())
