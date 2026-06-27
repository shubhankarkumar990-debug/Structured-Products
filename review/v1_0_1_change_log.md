# V1.0.1 CHANGE LOG

**Package:** Desk Bible Ecosystem V1.0.1 Semantic Errata  
**Date:** 2026-06-27  
**Baseline:** V1.0 (frozen 2026-06-26, hardened 2026-06-27)

---

## New Documents Added

| Document | Purpose |
|----------|---------|
| `v1_0_1_errata_addendum.md` | 7 confirmed errata with exact corrected text |
| `correlation_convention_framework.md` | Canonical convention for correlation direction language |
| `raw_vs_hedged_position_note.md` | Desk position qualifier standard |
| `worked_example_sanity_checklist.md` | QA checklist for worked examples |
| `market_convention_guide.md` | 10 commonly confused market conventions |
| `v1_0_1_change_log.md` | This document |
| `v1_0_1_review_only_register.md` | 7 items for optional clarification |
| `v1_0_1_accept_as_is_register.md` | 6 items confirmed correct |
| `v1_0_1_errata_verdict.md` | Final classification and verdict |

---

## Errata Items (Confirmed Corrections)

| ID | File | Line(s) | Change | Type |
|:--:|------|:-------:|--------|:----:|
| E-01a | Desk_Bible_v2.md | 17352 | FTD: "short credit correlation" → "long credit correlation" + convention note | Label correction |
| E-01b | Desk_Bible_v2.md | 17524 | FTD: "short correlation" → "long correlation" + structural note | Label correction |
| E-01c | Desk_Bible_v2.md | 17951 | FTD table row: "Short correlation (unambiguous)" → "Long correlation (MTM: benefits from high ρ)" | Label correction |
| E-02 | Desk_Bible_v2.md | 17526 | Worst-of: "short correlation" → "long correlation" + structural note | Label correction |
| E-03 | part6_sections_10_11.md | 102 | "desk (which sold protection via the short put)" → correct ownership + add hedged qualifier | Factual correction |
| E-04a | part6_sections_10_11.md | 110 | Add "(net/hedged position)" qualifier to ELN long correlation | Qualifier addition |
| E-04b | infrastructure_encyclopedia_v1.md | 4290 | Add "raw (unhedged)" qualifier + mention hedged direction | Qualifier addition |
| E-05 | Desk_Bible_v2.md | 22565 | "65%: above strike (100%)" → "65%: below strike (100%), physical delivery" | Arithmetic correction |
| E-06 | Desk_Bible_v2.md | 22605 | "long single-stock vol + short basket vol = long correlation" → "= short correlation" | Label correction |
| E-07 | Desk_Bible_v2.md | 1069 | "(3 × 2) = -56" → "(3 × (−2)) = -50 − 6 = -56" | Sign correction |

---

## Review-Only Items (Optional Clarifications)

| ID | File | Line(s) | Recommendation |
|:--:|------|:-------:|---------------|
| R-01 | interview_system_v2_2.md | 356 | Align WOAC label with MTM convention |
| R-02 | Desk_Bible_v2.md | 17949-17955 | Correct NTD table labels for all N values |
| R-03 | Desk_Bible_v2.md | 22483 | Add "net/hedged" qualifier |
| R-04 | Desk_Bible_v2.md | 22536-22545 | Add strike to terms table |
| R-05 | Desk_Bible_v2.md | Credit examples | Add recovery convention note |
| R-06 | Desk_Bible_v2.md | 1060-1061 | Add sign convention footnote |
| R-07 | Desk_Bible_v2.md | 13960 | Correct Q4 coupon or accept rounding |

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
| Desk_Bible_v2.md | FROZEN | FROZEN — errata in addendum |
| part6_sections_10_11.md | FROZEN | FROZEN — errata in addendum |
| infrastructure_encyclopedia_v1.md | FROZEN | FROZEN — errata in addendum |
| interview_system_v2_2.md | FROZEN | FROZEN — review-only item R-01 |
| solutions_manual.md | FROZEN | FROZEN — no changes |
| product_dna_atlas.md | FROZEN | FROZEN — no changes |
| complexity_registry.yaml | FROZEN | FROZEN — no changes |
| product_comparison_matrix.md | FROZEN | FROZEN — no changes |
| publication_taxonomy.yaml | FROZEN | FROZEN — no changes |
| All other production/* | FROZEN | FROZEN — no changes |

**No frozen V1.0 file has been modified. All corrections exist only in the V1.0.1 errata addendum.**

---

*V1.0.1 Change Log | FINAL | 2026-06-27*
