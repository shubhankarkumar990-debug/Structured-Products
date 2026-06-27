# V1.0.1 CHANGE LOG — FINAL

**Package:** Desk Bible Ecosystem V1.0.1 Semantic Errata  
**Date:** 2026-06-27  
**Baseline:** V1.0 (frozen 2026-06-26, hardened 2026-06-27)  
**Status:** FINAL (package closure)  
**Supersedes:** `v1_0_1_change_log.md`

---

## New Documents Added

| Document | Purpose |
|----------|---------|
| `v1_0_1_errata_addendum_final.md` | 9 confirmed errata with exact corrected text (supersedes `v1_0_1_errata_addendum.md`) |
| `correlation_convention_framework_final.md` | Canonical convention for correlation direction language |
| `raw_vs_hedged_position_note_final.md` | Desk position qualifier standard |
| `worked_example_sanity_checklist_final.md` | QA checklist for worked examples |
| `market_convention_guide_final.md` | 10 commonly confused market conventions |
| `v1_0_1_change_log_final.md` | This document |
| `v1_0_1_review_only_register_final.md` | 5 items for optional clarification (2 promoted to errata) |
| `v1_0_1_accept_as_is_register_final.md` | 6 items confirmed correct |
| `v1_0_1_errata_verdict_final.md` | Final classification and verdict |
| `v1_0_1_package_closure_memo.md` | Package closure decisions and rationale |

---

## Errata Items (Confirmed Corrections)

| ID | File | Line(s) | Change | Type |
|:--:|------|:-------:|--------|:----:|
| E-01a | Desk_Bible_v2.md | 17352 | FTD: "short credit correlation" → "long credit correlation" + convention note | Label correction |
| E-01b | Desk_Bible_v2.md | 17524 | FTD: "short correlation" → "long correlation" + structural note | Label correction |
| E-01c | Desk_Bible_v2.md | 17951 | FTD table row: "Short correlation (unambiguous)" → "Long correlation (MTM: risk falls as ρ rises)" | Label correction |
| E-02 | Desk_Bible_v2.md | 17526 | Worst-of: "short correlation" → "long correlation" + structural note | Label correction |
| E-03 | part6_sections_10_11.md | 102 | "desk (which sold protection via the short put)" → correct ownership + add hedged qualifier | Factual correction |
| E-04a | part6_sections_10_11.md | 110 | Add "(net/hedged position)" qualifier to ELN long correlation | Qualifier addition |
| E-04b | infrastructure_encyclopedia_v1.md | 4290 | Add "raw (unhedged)" qualifier + mention hedged direction | Qualifier addition |
| E-05 | Desk_Bible_v2.md | 22565 | "65%: above strike (100%)" → "65%: below strike (100%), physical delivery" | Arithmetic correction |
| E-06 | Desk_Bible_v2.md | 22605 | "long single-stock vol + short basket vol = long correlation" → "= short correlation" | Label correction |
| E-07 | Desk_Bible_v2.md | 1069 | "(3 × 2) = -56" → "(3 × (−2)) = -50 − 6 = -56" | Sign correction |
| E-08 | interview_system_v2_2.md | 356 | WOAC: "SHORT correlation: benefit from high" → "long correlation" + structural note | Label correction (promoted from R-01) |
| E-09 | Desk_Bible_v2.md | 17952-17955 | NTD table rows 2-5: inverted labels → all SHORT correlation with explanations | Label correction (promoted from R-02) |

---

## Changes from Pre-Closure Package

| Change | Detail |
|--------|--------|
| R-01 **promoted** to E-08 | Same self-contradiction pattern as E-01/E-02. Cross-artifact consistency requires correction. |
| R-02 **promoted** to E-09 | NTD table labels contradict risk table in same chapter. Same-table inconsistency after E-01c. |
| Errata count | 7 → 9 items (10 → 15 line corrections) |
| Review-only count | 7 → 5 items |
| Artifact count | 3 → 4 (added interview_system_v2_2.md) |
| E-05 arithmetic | Corrected share delivery calculation to €324,870 (714 × €455) |

---

## Review-Only Items (Optional Clarifications)

| ID | File | Line(s) | Recommendation |
|:--:|------|:-------:|---------------|
| R-01 | Desk_Bible_v2.md | 22483 | Add "net/hedged" qualifier (was R-03) |
| R-02 | Desk_Bible_v2.md | 22536-22545 | Add strike to terms table (was R-04) |
| R-03 | Desk_Bible_v2.md | Credit examples | Add recovery convention note (was R-05) |
| R-04 | Desk_Bible_v2.md | 1060-1061 | Add sign convention footnote (was R-06) |
| R-05 | Desk_Bible_v2.md | 13960 | Correct Q4 coupon or accept rounding (was R-07) |

---

## Accept-As-Is Items (No Change)

| ID | Description | Rationale |
|:--:|------------|-----------|
| A-01 | Solutions Manual convention mixing | Individually correct |
| A-02 | Atlas economic descriptions | Avoids labels entirely |
| A-03 | FTD/NTD confusion pair | Correct, label-free |
| A-04 | Independent stocks simplification | Standard pedagogy |
| A-05 | Continuous barrier conventions | Covered in Encyclopedia |
| A-06 | Day count / quarterly conventions | Shown in tables |

---

## Frozen Artifacts — Status

| Artifact | V1.0 Status | V1.0.1 Status |
|----------|:----------:|:------------:|
| Desk_Bible_v2.md | FROZEN | FROZEN — errata in addendum (E-01 through E-07, E-09) |
| part6_sections_10_11.md | FROZEN | FROZEN — errata in addendum (E-03, E-04a) |
| infrastructure_encyclopedia_v1.md | FROZEN | FROZEN — errata in addendum (E-04b) |
| interview_system_v2_2.md | FROZEN | FROZEN — errata in addendum (E-08) |
| solutions_manual.md | FROZEN | FROZEN — no changes (A-01) |
| product_dna_atlas.md | FROZEN | FROZEN — no changes (A-02) |
| complexity_registry.yaml | FROZEN | FROZEN — no changes |
| product_comparison_matrix.md | FROZEN | FROZEN — no changes |
| publication_taxonomy.yaml | FROZEN | FROZEN — no changes |
| All other production/* | FROZEN | FROZEN — no changes |

**No frozen V1.0 file has been modified. All corrections exist only in the V1.0.1 errata addendum.**

---

*V1.0.1 Change Log | FINAL (package closure) | 2026-06-27*
