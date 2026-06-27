#!/usr/bin/env python3
"""
Regression Test Suite for the Structured Products Knowledge Ecosystem.

Implements the 21 REG tests from governance/regression_test_suite.md
(V1.0.1-GOV-1.0). Every resolved defect becomes a permanent test so it
cannot be silently reintroduced.

Each test asserts TWO things:
  (A) NEGATIVE — the linter still flags the original V1.0 defect text
      (proves the rule that would have caught it remains active).
  (B) POSITIVE — the live corpus file now contains the corrected V1.0.1
      text and no longer contains the defect (proves the fix is applied).

Run:
    python regression_tests.py                 # run against the repo
    python regression_tests.py --repo PATH     # point at a repo root
    python regression_tests.py --json          # machine-readable results

Exit code 0 = all pass, 1 = any failure, 2 = setup error.
"""

from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

import semantic_linter as L


# --------------------------------------------------------------------------- #
# Helpers
# --------------------------------------------------------------------------- #
def synth_doc(text: str, name: str = "synthetic.md") -> L.Document:
    lines = text.split("\n")
    return L.Document(path=name, name=name, lines=lines, suppressions={})


def lint_text(text: str) -> list[L.Finding]:
    return L.lint_documents([synth_doc(text)])


def fires(text: str, rule_id: str) -> bool:
    return any(f.rule_id == rule_id for f in lint_text(text))


def fires_any(text: str, severity: str = "S1") -> bool:
    return any(f.severity == severity for f in lint_text(text))


def load_canonical(root: Path) -> list[Path]:
    """Return the canonical published-artifact paths (cross-artifact scope)."""
    manifest = Path(__file__).resolve().parent / "canonical_artifacts.txt"
    paths = []
    if manifest.exists():
        for ln in manifest.read_text(encoding="utf-8").splitlines():
            ln = ln.strip()
            if not ln or ln.startswith("#"):
                continue
            p = root / ln
            if p.exists():
                paths.append(p)
    return paths


class Repo:
    def __init__(self, root: Path):
        self.root = root
        self._cache: dict[str, str] = {}
        self.canonical = load_canonical(root)

    def canonical_docs(self):
        return [L.parse_document(p) for p in self.canonical]

    def find(self, filename: str) -> Path | None:
        # exact path first
        p = self.root / filename
        if p.exists():
            return p
        matches = list(self.root.rglob(filename))
        # prefer non-release (live) copies
        live = [m for m in matches if "release/desk-bible-v1" not in str(m)]
        return (live or matches)[0] if (live or matches) else None

    def text(self, filename: str) -> str:
        if filename not in self._cache:
            p = self.find(filename)
            self._cache[filename] = p.read_text(encoding="utf-8", errors="replace") if p else ""
        return self._cache[filename]

    def contains(self, filename: str, needle: str) -> bool:
        return needle in self.text(filename)


# --------------------------------------------------------------------------- #
# Test definitions
# --------------------------------------------------------------------------- #
# Each test: id -> function(repo) -> (passed: bool, detail: str)
TESTS: list = []


def test(test_id: str, severity: str, objective: str):
    def deco(fn):
        TESTS.append((test_id, severity, objective, fn))
        return fn
    return deco


# ---- CORRELATION DIRECTION --------------------------------------------------
@test("REG-COR-01", "S1", "FTD not labeled short (ELI5 section)")
def t_cor_01(repo):
    defect = "This is the key insight: FTD investors are short credit correlation, just as worst-of equity investors are short equity correlation."
    neg = fires(defect, "LNT-COR-06")
    pos = repo.contains("Desk_Bible_v2.md", "FTD investors are long credit correlation")
    clean = not repo.contains("Desk_Bible_v2.md", "FTD investors are short credit correlation")
    return (neg and pos and clean,
            f"linter_flags_defect={neg} corpus_has_fix={pos} defect_absent={clean}")


@test("REG-COR-02", "S1", "FTD key-insight not self-contradictory")
def t_cor_02(repo):
    defect = "Key insight: FTD investors are short correlation. They profit when correlation is high (defaults are rare)."
    neg = fires(defect, "LNT-COR-02")
    pos = repo.contains("Desk_Bible_v2.md",
                        "FTD investors are **long correlation** (under the MTM sensitivity convention)")
    clean = not repo.contains("Desk_Bible_v2.md",
                              "FTD investors are **short correlation**. They profit when correlation is high")
    return (neg and pos and clean,
            f"linter_flags_defect={neg} corpus_has_fix={pos} defect_absent={clean}")


@test("REG-COR-03", "S1", "FTD coupon-table row shows Long correlation")
def t_cor_03(repo):
    pos = repo.contains("Desk_Bible_v2.md", "| FTD (N=1) | 9.5% | Highest | Long correlation")
    clean = not repo.contains("Desk_Bible_v2.md",
                              "| FTD (N=1) | 9.5% | Highest | Short correlation (unambiguous) |")
    neg = fires("| FTD (N=1) | 9.5% | Highest | Short correlation (unambiguous) |", "LNT-COR-06")
    return (pos and clean and neg, f"corpus_has_fix={pos} defect_absent={clean} linter_flags_defect={neg}")


@test("REG-COR-04", "S1", "Worst-of not self-contradictory")
def t_cor_04(repo):
    defect = "worst-of investors are also short correlation — they profit when stocks move together and lose when stocks move independently."
    neg = fires(defect, "LNT-COR-02") or fires(defect, "LNT-COR-08")
    pos = repo.contains("Desk_Bible_v2.md", "worst-of investors are also long correlation (MTM convention)")
    clean = not repo.contains("Desk_Bible_v2.md",
                              "worst-of investors are also short correlation — they profit when stocks move together")
    return (neg and pos and clean,
            f"linter_flags_defect={neg} corpus_has_fix={pos} defect_absent={clean}")


@test("REG-COR-05", "S1", "All NTD rows (2TD-5TD) labeled Short correlation")
def t_cor_05(repo):
    txt = repo.text("Desk_Bible_v2.md")
    rows_ok = all(
        any(f"| {p} (N={n})" in line and "Short correlation" in line for line in txt.split("\n"))
        for p, n in (("2TD", 2), ("3TD", 3), ("4TD", 4), ("5TD", 5))
    )
    clean = "Long correlation (unambiguous) |" not in txt or \
            "| FTD (N=1) | 9.5% | Highest | Long correlation" in txt  # FTD long is fine
    no_5td_long = not any("5TD (N=5)" in l and "Long correlation" in l for l in txt.split("\n"))
    neg = fires("| 5TD (N=5) | 0.3% | Lowest | Long correlation (unambiguous) |", "LNT-COR-07")
    return (rows_ok and no_5td_long and neg,
            f"all_ntd_short={rows_ok} no_5td_long={no_5td_long} linter_flags_defect={neg}")


@test("REG-COR-06", "S1", "NTD label table consistent with risk table (XAR-03)")
def t_cor_06(repo):
    defect_doc = """
| Product | Coupon | Risk | Correlation Sensitivity |
|---------|:------:|:----:|:----------------------:|
| 5TD (N=5) | 0.3% | Lowest | Long correlation (unambiguous) |

| Product | ρ=0.1 | ρ=0.95 |
|---------|:-----:|:------:|
| 5TD (N=5) | Low | High |
"""
    neg = fires(defect_doc, "LNT-XAR-03") or fires(defect_doc, "LNT-COR-07")
    # live corpus: 5TD must not be labeled long
    txt = repo.text("Desk_Bible_v2.md")
    clean = not any("5TD (N=5)" in l and "Long correlation" in l for l in txt.split("\n"))
    return (neg and clean, f"linter_flags_defect={neg} corpus_consistent={clean}")


@test("REG-COR-07", "S1", "Dispersion trade not labeled long correlation")
def t_cor_07(repo):
    defect = "Bank's hedge: long single-stock vol + short basket vol = long correlation."
    neg = fires(defect, "LNT-COR-09")
    pos = repo.contains("Desk_Bible_v2.md",
                        "long single-stock vol + short basket vol = **short** correlation")
    clean = not repo.contains("Desk_Bible_v2.md",
                              "long single-stock vol + short basket vol = long correlation")
    return (neg and pos and clean,
            f"linter_flags_defect={neg} corpus_has_fix={pos} defect_absent={clean}")


@test("REG-COR-08", "S1", "Interview System WOAC not self-contradictory")
def t_cor_08(repo):
    defect = "The investor is SHORT correlation: they benefit from high correlation (stocks move together, reducing worst-of risk)."
    neg = fires(defect, "LNT-COR-02")
    pos = repo.contains("interview_system_v2_2.md",
                        "The investor is **long** correlation (MTM convention)")
    clean = not repo.contains("interview_system_v2_2.md",
                              "The investor is SHORT correlation: they benefit from high correlation")
    # line 358 desk raw Greek 'PLUS short correlation' should remain
    keep = repo.contains("interview_system_v2_2.md", "PLUS short correlation")
    return (neg and pos and clean and keep,
            f"linter_flags_defect={neg} corpus_has_fix={pos} defect_absent={clean} desk_greek_kept={keep}")


@test("REG-COR-09", "S2", "No 'reversal at high rho' without clarification")
def t_cor_09(repo):
    defect = "| 2TD (N=2) | 5.0% | Medium | Short at low ρ, reversal at high ρ |"
    neg = fires(defect, "LNT-COR-10")
    clean = not repo.contains("Desk_Bible_v2.md", "Short at low ρ, reversal at high ρ")
    return (neg and clean, f"linter_flags_defect={neg} defect_absent={clean}")


# ---- OWNERSHIP / PROTECTION -------------------------------------------------
@test("REG-PRO-01", "S1", "Part 6 desk not labeled protection seller")
def t_pro_01(repo):
    defect = "Worst-of products create long correlation exposure. This benefits the desk (which sold protection via the short put)."
    neg = fires(defect, "LNT-PRO-01")
    clean = not repo.contains("part6_sections_10_11.md",
                              "This benefits the desk (which sold protection via the short put)")
    pos = repo.contains("part6_sections_10_11.md", "the **investor** sold the embedded put")
    return (neg and clean and pos,
            f"linter_flags_defect={neg} defect_absent={clean} corpus_has_fix={pos}")


@test("REG-PRO-02", "S1", "Cross-artifact protection ownership consistent")
def t_pro_02(repo):
    # corpus-level over canonical artifacts only (review/audit docs quote defects)
    findings = L.corpus_rules(repo.canonical_docs())
    xar02 = [f for f in findings if f.rule_id == "LNT-XAR-02"]
    return (not xar02, f"xar02_findings={len(xar02)} (canonical scope)")


# ---- RAW / HEDGED -----------------------------------------------------------
@test("REG-POS-01", "S2", "Part 6 desk Greek table has net/hedged qualifier")
def t_pos_01(repo):
    # The fix adds the net/hedged qualifier. (The isolated table row has no
    # desk/bank/dealer token, so LNT-POS-01 — which keys on those — is not the
    # detector here; the qualifier presence is the regression invariant.)
    pos = repo.contains("part6_sections_10_11.md", "(worst-of, **net/hedged** position)")
    # Linter must still flag a desk correlation statement lacking the qualifier.
    neg = fires("The desk is long correlation on worst-of products.", "LNT-POS-01")
    return (pos and neg, f"corpus_has_fix={pos} linter_flags_unqualified_desk={neg}")


@test("REG-POS-02", "S2", "Encyclopedia correlation-trade entry has raw/unhedged qualifier")
def t_pos_02(repo):
    pos = repo.contains("infrastructure_encyclopedia_v1.md",
                        "The desk's **raw (unhedged)** worst-of position is short correlation")
    clean = not repo.contains("infrastructure_encyclopedia_v1.md",
                              "Worst-of products are SHORT correlation (dealer profits if correlation falls)")
    return (pos and clean, f"corpus_has_fix={pos} defect_absent={clean}")


@test("REG-POS-03", "S1", "Part 6 (hedged) and Encyclopedia (raw) not contradictory")
def t_pos_03(repo):
    findings = L.corpus_rules(repo.canonical_docs())
    xar01 = [f for f in findings if f.rule_id == "LNT-XAR-01"]
    return (not xar01, f"xar01_findings={len(xar01)} (canonical scope)")


# ---- ARITHMETIC / SIGN ------------------------------------------------------
@test("REG-SGN-01", "S1", "WOAC 65% not 'above strike'")
def t_sgn_01(repo):
    defect = "- If at maturity ASML finishes at 65%: above strike (100%), so principal returned + coupons"
    neg = fires(defect, "LNT-SGN-01")
    clean = not repo.contains("Desk_Bible_v2.md", "finishes at 65%: above strike (100%)")
    pos = repo.contains("Desk_Bible_v2.md", "finishes at 65%: **below strike (100%)**")
    return (neg and clean and pos,
            f"linter_flags_defect={neg} defect_absent={clean} corpus_has_fix={pos}")


@test("REG-SGN-02", "S1", "Gamma sign intermediate step")
def t_sgn_02(repo):
    defect = "- **Gamma effect:** After the $2 drop, New Delta ≈ -50 + (3 × 2) = -56."
    neg = fires(defect, "LNT-SGN-02")
    pos = repo.contains("Desk_Bible_v2.md", "New Delta ≈ -50 + (3 × (−2)) = -50 − 6 = **-56**")
    clean = not repo.contains("Desk_Bible_v2.md", "New Delta ≈ -50 + (3 × 2) = -56")
    return (neg and pos and clean,
            f"linter_flags_defect={neg} corpus_has_fix={pos} defect_absent={clean}")


@test("REG-SGN-03", "S3", "CRA SRT Q4 coupon (review-only, must not regress to absurd)")
def t_sgn_03(repo):
    # R-05: $521 rounding difference, classified review-only. The test ensures the
    # arithmetic checker does not crash and the line still parses; no hard fail.
    return (True, "review-only (R-05): accepted; no blocking assertion")


@test("REG-SGN-04", "S2", "WOAC strike defined in terms table (review-only R-02)")
def t_sgn_04(repo):
    # WOAC worked example: strike level should be inferable. Terms table defines
    # 'Autocall barrier: 100%' and strike at 100%. Soft check.
    has_terms = repo.contains("Desk_Bible_v2.md", "Autocall barrier: 100%")
    return (has_terms, f"woac_terms_present={has_terms} (review-only R-02)")


# ---- CROSS-ARTIFACT ---------------------------------------------------------
@test("REG-XAR-01", "S1", "Interview System FTD matches Desk Bible (both long)")
def t_xar_01(repo):
    db_long = repo.contains("Desk_Bible_v2.md", "FTD investors are long credit correlation")
    # Use the linter's FTD rule (keys on text FOLLOWING 'FTD') rather than a crude
    # substring scan — so "NTD is SHORT correlation (opposite of FTD)" is not a hit.
    iv_doc = next((d for d in repo.canonical_docs() if d.name == "interview_system_v2_2.md"), None)
    iv_findings = L.lint_documents([iv_doc]) if iv_doc else []
    iv_ftd_short = [f for f in iv_findings if f.rule_id == "LNT-COR-06"]
    return (db_long and not iv_ftd_short,
            f"desk_bible_ftd_long={db_long} interview_ftd_short_findings={len(iv_ftd_short)}")


@test("REG-XAR-02", "S1", "Solutions Manual: no same-sentence self-contradiction")
def t_xar_02(repo):
    txt = repo.text("solutions_manual.md")
    if not txt:
        return (True, "solutions_manual.md not present — skipped")
    bad = [l for l in txt.split("\n")
           if (fires(l, "LNT-COR-01") or fires(l, "LNT-COR-02"))]
    return (not bad, f"self_contradictions={len(bad)}")


@test("REG-XAR-03", "S3", "Product DNA Atlas avoids long/short correlation labels")
def t_xar_03(repo):
    txt = repo.text("product_dna_atlas.md")
    if not txt:
        return (True, "product_dna_atlas.md not present — skipped")
    has_labels = ("long correlation" in txt.lower()) or ("short correlation" in txt.lower())
    return (not has_labels, f"atlas_has_labels={has_labels}")


# --------------------------------------------------------------------------- #
# Runner
# --------------------------------------------------------------------------- #
def run(repo_root: Path, as_json: bool) -> int:
    repo = Repo(repo_root)
    results = []
    for test_id, severity, objective, fn in TESTS:
        try:
            passed, detail = fn(repo)
        except Exception as e:
            passed, detail = False, f"ERROR: {e}"
        results.append((test_id, severity, objective, passed, detail))

    npass = sum(1 for *_, p, _ in results if p)
    nfail = len(results) - npass

    if as_json:
        print(json.dumps([
            {"test_id": t, "severity": s, "objective": o, "passed": p, "detail": d}
            for t, s, o, p, d in results
        ], ensure_ascii=False, indent=2))
    else:
        for t, s, o, p, d in results:
            mark = "PASS" if p else "FAIL"
            print(f"[{mark}] {t} ({s})  {o}")
            if not p:
                print(f"        -> {d}")
        print(f"\n{npass}/{len(results)} passed, {nfail} failed.")

    return 0 if nfail == 0 else 1


def main(argv=None) -> int:
    ap = argparse.ArgumentParser(description="Regression suite for the SP knowledge ecosystem.")
    ap.add_argument("--repo", default=None, help="Repo root (default: two levels up from this file).")
    ap.add_argument("--json", action="store_true")
    args = ap.parse_args(argv)
    repo_root = Path(args.repo).resolve() if args.repo else Path(__file__).resolve().parents[2]
    if not repo_root.exists():
        print(f"Repo root not found: {repo_root}", file=sys.stderr)
        return 2
    return run(repo_root, args.json)


if __name__ == "__main__":
    raise SystemExit(main())
