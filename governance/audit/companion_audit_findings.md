# Companion Files — Audit Findings

**Date:** 28 Jun 2026. **Tool:** `governance/audit/companion_audit.py` (read-only) — runs the Bible's integrity checks (table cell-count, placeholder/leak tokens, mojibake, unbalanced markup, broken links) plus the Tier-3 self-contained-equation numeric check on each companion.

## Scope

| File | Lines | Tables | Equations checked |
|------|------:|-------:|------------------:|
| `solutions_manual.md` | 2,081 | 65 | 0 |
| `product_comparison_matrix.md` | 816 | 21 | 0 |
| `product_dna_atlas.md` | 2,098 | 81 | 0 |
| `interview_system_v2_2.md` | 2,235 | 24 | 1 |
| `infrastructure_encyclopedia_v1.md` | 4,438 | 12 | 6 |

(Low equation counts in the matrix/atlas/solutions are expected — they are table- and prose-based, with few inline `A = B` equations. The integrity checks still cover every table and line.)

## Result: clean, with one minor imprecision

**Integrity: 0 findings across all five files** — no malformed tables (every data row matches its header column count), no placeholder/leak tokens, no mojibake, no unbalanced markup, no broken image links. The companion markdown is structurally sound and will convert cleanly.

**Numeric: 1 item, minor.**
`interview_system_v2_2.md` L1873 (a "Top Traps" aside on CDS recovery):
> "Assumed 40% recovery → Lehman actual 8.6% = 33% increase in loss severity."

The flag itself is a false positive (the checker read "8.6%" and "33%" as an equation; they are two separate quantities). But the underlying claim is imprecise:
- Loss severity = 1 − recovery. Assumed 1 − 0.40 = 60 %; actual 1 − 0.086 = 91.4 %.
- The increase is **31.4 percentage points** (absolute) or **+52 %** (relative) — not cleanly 33 %.

The "33 %" appears to loosely approximate the ~31-point recovery drop (40 % → 8.6 %). The concept (lower recovery ⇒ higher loss severity) is correct; only the figure is soft. **Severity: low** — an illustrative aside, not a worked example or a headline number.

*Suggested wording fix (optional):* "…Lehman actual 8.6 % → loss severity rises from 60 % to 91 %, a ~31-point jump (about 50 % worse)."

## Verdict

The companions are in good shape — clean integrity, sound tables, one soft figure worth a one-line wording tweak. They are safe to ship as-is or to fold into a combined edition.
