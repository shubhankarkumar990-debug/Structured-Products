# Interview System V2.1 — Change Log

**Date**: 2026-06-25
**From**: Interview System V2.0 (production/interview_system_v2.md, 2,234 lines)
**To**: Interview System V2.1 (production/interview_system_v2_1.md, 2,235 lines)
**Driver**: Adversarial audit findings (audit/interview_system_v2_adversarial_audit.md)

---

## Summary

Targeted fix release. All changes driven by the 10-phase adversarial audit. No structural changes, no content additions, no architecture modifications. Every edit corrects a verified factual, arithmetic, or editorial error.

---

## Critical Fixes (1)

| ID | Finding | Location | Fix |
|:--:|---------|----------|-----|
| C-1 | IRS DV01 arithmetic: 25bp × 100bp ≠ $2.5M on $1M | Lines 222, 1867 | Clarified DV01 as $2,500/bp/$1M. Changed exposure statement to "$10M position, 100bp = ~$2.5M" — same memorable number, now dimensionally correct |

## High Fixes (6)

| ID | Finding | Location | Fix |
|:--:|---------|----------|-----|
| H-1 | KODRC Tier 2 construction contradicts Tier 1 economics | Line 427 | Changed "DRC + long down-and-out put" → "Discount bond + short down-and-out put". Added barrier behavior explanation |
| H-2 | IF.8 bid-offer reserve: question says "3% of option value" but answer applies % to notional | Line 1449 | Changed question to "3% of notional" to match worked answer |
| H-3 | IF.15 PPN: ZCB=$92 inconsistent with 8% rate environment (should be ~$68) | Line 1463 | Replaced with internally consistent numbers: 5% → ZCB=$78, participation=140%; 1% → ZCB=$95, participation=26.7% |
| H-4 | §3.1 day count title says "$55,556" but calculation produces $16,667 | Line 583 | Changed title to "the $16,667 difference" matching the actual worked example parameters |
| H-5 | MC.14 option (b) 225/40=5.625 duplicates correct answer (c) | Line 2041 | Changed (b) to "225/50" (=4.5, a plausible error using realized vol in denominator) |
| H-6 | Mini Cases MC.1-MC.8 namespace collision with Multiple Choice MC.1-MC.40 | Lines 2128-2135 | Renamed to MCS.1-MCS.8 |

## Medium Fixes (5)

| ID | Finding | Location | Fix |
|:--:|---------|----------|-----|
| M-1 | Technical Traps T.1-T.20 namespace collision with Technical Questions T.1-T.37 | Lines 1840-1900+ | Renamed to TT.1-TT.20. Updated section header and all cross-references |
| M-2 | Exercise 1 Q5: EUR notional ÷ CHF price = dimensional inconsistency | Lines 1023-1043 | Changed notional to CHF 1,000,000. Updated all EUR→CHF in Exercise 1 answers |
| M-3 | Booster Tier 1: "100% above cap" ambiguous — could mean 100% additional participation | Line 457 | Clarified: "1× (unleveraged) above cap — the extra call and short call offset, leaving only underlying position" |
| M-4 | Appendix "Product Questions" column contains infrastructure questions for infra roles | Line 2201 | Renamed column to "Core Questions". Cleaned up mixed IC/DS assignments for PC, Ops, Treasury, Legal, Credit Risk |
| M-5 | BT.10 correlation analogy incomplete — only explains low correlation scenario | Line 1983 | Extended: added high correlation scenario ("all go to same party — either all get sick or none do") |

## Low Fixes (1 of 3)

| ID | Finding | Decision | Fix |
|:--:|---------|----------|-----|
| L-1 | CDS/CommSwap conflated on single line | Implemented | Separated into distinct entry. CDS already fully covered in Top 10 — removed redundant "(covered in Top 10)" tag |
| L-2 | Abbreviated tracks §8.10-8.13 lack full 5-round depth | Skipped | Adequate for cross-functional roles. Expanding would add ~200 lines of content beyond audit scope |
| L-3 | VarSwap Tier 2 formula verification | N/A | Verified correct during audit. No fix needed |

---

## Quantitative Summary

| Metric | V2.0 | V2.1 | Delta |
|--------|:----:|:----:|:-----:|
| Total lines | 2,234 | 2,235 | +1 |
| Factual errors corrected | — | 3 | — |
| Arithmetic errors corrected | — | 2 | — |
| Namespace collisions resolved | — | 2 | — |
| Dimensional inconsistencies fixed | — | 2 | — |
| Ambiguities clarified | — | 2 | — |
| Duplicate answer options fixed | — | 1 | — |
| Editorial improvements | — | 1 | — |
| **Total fixes applied** | — | **13** | — |

**Nothing of educational value was removed.** All fixes either correct errors or improve clarity. No content was simplified, no depth was reduced, no sections were deleted.
