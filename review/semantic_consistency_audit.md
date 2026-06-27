# GLOBAL SEMANTIC CONSISTENCY AUDIT — V1.0 Review

**Workstream:** WS1 — Global Semantic Consistency Audit  
**Scope:** Meaning drift and semantic inconsistencies across ALL canonical artifacts  
**Date:** 2026-06-27  
**Status:** COMPLETE  

---

## Executive Summary

The V1.0 ecosystem exhibits strong semantic consistency across its 25 frozen artifacts for the vast majority of content. Product descriptions, lifecycle mechanics, booking conventions, and risk analysis are semantically aligned across the Desk Bible, Interview System, Atlas, Solutions Manual, Encyclopedia, and Part 6.

The primary semantic inconsistency is the correlation direction convention (fully documented in `correlation_direction_audit.md`). Beyond correlation, this audit identifies 5 additional semantic drift findings.

---

## Methodology

1. Extracted key terms and concepts from the Desk Bible (primary source)
2. Traced each concept through Interview System V2.2, Atlas, Solutions Manual, Encyclopedia, and Part 6
3. Flagged any instance where the same concept carries different meaning across artifacts
4. Excluded correlation direction findings (covered in WS2 deliverable)

---

## FINDING SCA-01: "Protection seller" misattribution in Part 6

**Severity:** HIGH  
**Artifact:** production/part6_sections_10_11.md (FROZEN), line 102

**Quoted text:**
> "This benefits the desk (which sold protection via the short put)."

**Problem:** In a worst-of structured note:
- The INVESTOR's position contains an embedded short put (the investor sold the put)
- The DESK is long the put (the desk bought protection from the investor)
- Part 6 attributes the short put to the desk, inverting who holds which side

This is not a convention issue — it is a factual error about position ownership. The desk did not sell protection; the desk bought it. The investor sold it.

**Cross-artifact check:**
- Desk Bible (line 2956): "The 7.5% put premium is the key. It is high because the **investor** is selling a meaningful option" ← CORRECT
- Solutions Manual (line 180): "**client** sells correlation risk on a basket" ← CORRECT
- Interview System V2.2 (line 351): "the **investor** is selling correlation risk" ← CORRECT

All other artifacts correctly attribute the short put to the investor. Part 6 is the sole outlier.

**Erratum recommendation:** ERRATA REQUIRED.

---

## FINDING SCA-02: "Desk is structurally long correlation" ambiguity (Desk Bible)

**Severity:** MEDIUM  
**Artifact:** Desk_Bible_v2.md (FROZEN), line 22483

**Quoted text:**
> "The bank is structurally long correlation (benefits when stocks move together)."

**Problem:** This describes the desk's HEDGED position. The desk's RAW position on worst-of is short correlation (long the worst-of put). After hedging with dispersion trades (line 22483: "buying single-stock volatility and selling basket volatility"), the desk may be net long correlation.

The sentence does not specify raw vs hedged. A reader who reads this, then reads the Encyclopedia ("dealer is SHORT correlation"), encounters an apparent contradiction. The distinction is raw vs hedged, but neither artifact states its assumption.

**Erratum recommendation:** REVIEW ONLY. Adding "(after hedging)" to line 22483 would resolve the ambiguity.

---

## FINDING SCA-03: WOAC strike level undefined in worked example

**Severity:** MEDIUM  
**Artifact:** Desk_Bible_v2.md (FROZEN), lines 22536-22545

**Problem:** The WOAC worked example at §18 lists terms including:
- Autocall barrier: 100%
- Coupon barrier: 70%
- Knock-in barrier: 60%
- **No explicit strike level**

The standard WOAC structure requires a strike level (the threshold below which physical delivery applies at maturity after KI). The terms omit this. At line 22565, the text references "above strike (100%)" — implying the strike is 100% — but this was never stated in the terms.

**Erratum recommendation:** REVIEW ONLY. Add "Strike: 100% of initial" to the terms table.

---

## FINDING SCA-04: Complexity score semantic consistency — CONFIRMED CONSISTENT

**Severity:** NONE (verification pass)

All 49 product complexity scores were traced across:
- production/complexity_registry.yaml
- production/product_dna_atlas.md
- production/product_comparison_matrix.md
- Desk_Bible_v2.md (chapter headers)

**Result:** All 49 scores are identical across all 4 artifacts. Score distribution: 4×2, 8×3, 9×4, 10×5, 7×6, 7×7, 3×8, 1×10. No semantic drift.

---

## FINDING SCA-05: System name semantics — CONFIRMED CONSISTENT

**Severity:** NONE (verification pass)

The three systems (NEMO, Sophis, Murex) are described consistently across all artifacts:
- NEMO: trade capture/booking for ELN and CLN families
- Sophis: pricing, risk, and P&L for equity/credit derivatives
- Murex: rates derivatives, multi-leg structures (Swaps, SRT, STEG families)

No instance of a system being attributed the wrong function or the wrong product family.

---

## FINDING SCA-06: Family assignment semantics — CONFIRMED CONSISTENT

**Severity:** NONE (verification pass)

All 49 products maintain consistent family assignments across artifacts:
- ELN: 15 products (Section 5.1)
- Swaps: 8 products (Section 5.2)
- SRT: 5 products (Section 5.3)
- STEG: 4 products (Section 5.4)
- CLN: 5 products (Section 5.5)
- Other: 12 products (Section 5.6)

No product appears in a different family across any artifact.

---

## Summary Table

| Finding | Description | Severity | Status |
|:-------:|------------|:--------:|:------:|
| SCA-01 | Part 6 protection seller misattribution | HIGH | ERRATA REQUIRED |
| SCA-02 | Desk long correlation raw vs hedged | MEDIUM | REVIEW ONLY |
| SCA-03 | WOAC strike level undefined | MEDIUM | REVIEW ONLY |
| SCA-04 | Complexity scores consistent | NONE | VERIFIED ✓ |
| SCA-05 | System names consistent | NONE | VERIFIED ✓ |
| SCA-06 | Family assignments consistent | NONE | VERIFIED ✓ |

---

*Generated: 2026-06-27 | Workstream WS1 | Semantic Consistency Audit Task 4*
