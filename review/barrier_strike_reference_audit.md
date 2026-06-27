# BARRIER / STRIKE / REFERENCE-LEVEL AUDIT — V1.0 Review

**Workstream:** WS4 — Barrier/Strike/Reference-Level Audit  
**Scope:** All barrier mechanics, strike definitions, and reference-level claims  
**Date:** 2026-06-27  
**Status:** COMPLETE  

---

## Executive Summary

The V1.0 ecosystem's barrier and strike mechanics are semantically consistent across the vast majority of product chapters. Two findings were identified, both in the Desk Bible's WOAC chapter.

---

## FINDING BSR-01: WOAC worked example — "65% above strike (100%)" is mathematically wrong

**Severity:** HIGH  
**Artifact:** Desk_Bible_v2.md (FROZEN), line 22565

**Context:** WOAC worked example "What if" scenario. KI barrier = 60% (breached at 55%). The text then evaluates two maturity outcomes.

**Quoted text:**
> "If at maturity ASML finishes at 65%: above strike (100%), so principal returned + coupons"

**Problem:** 65% is NOT above 100%. The parenthetical explicitly states the strike is 100%, but then claims 65% is above it. This is arithmetically impossible.

**Interpretation analysis:**
1. If strike = 100% (as stated): ASML at 65% is BELOW strike → physical delivery, not principal returned. The entire outcome described is wrong.
2. If the author intended strike = 60% (equal to KI barrier): ASML at 65% > 60% → principal returned would be correct. But the parenthetical says "(100%)."
3. The physical delivery formula at line 22566 uses €700 (ASML initial price) as the denominator: "€500,000 / €700 = 714 shares." This implies the strike IS at the initial level (100%), confirming interpretation 1.

**Impact:** A reader working through the example will either (a) accept a mathematically false statement, or (b) lose trust in the material. Either outcome is pedagogically harmful.

**Erratum recommendation:** ERRATA REQUIRED. Either:
- Correct to: "If at maturity ASML finishes at 65%: below strike (100%), physical delivery" (and add the share calculation)
- Or, if the intended product has strike = KI barrier: correct the parenthetical to "(60%)" and revise the physical delivery formula at line 22566 accordingly

---

## FINDING BSR-02: WOAC worked example — strike not defined in terms

**Severity:** MEDIUM  
**Artifact:** Desk_Bible_v2.md (FROZEN), lines 22536-22545

**Context:** The WOAC worked example lists product terms:
- Notional: EUR 500,000
- Basket: Siemens, LVMH, ASML
- Maturity: 18 months
- Coupon: 3.0% per quarter with memory
- Autocall barrier: 100%
- Coupon barrier: 70%
- Knock-in barrier: 60% (continuous)
- No-call period: 6 months

**Problem:** The terms table does not include a "Strike" or "Redemption strike" level. The strike is referenced later at line 22565 as "(100%)" but was never defined in the terms. For a pedagogical worked example, omitting a key term that determines the maturity payoff is a gap.

**Cross-reference:** Other worked examples (RC at line 2963, Phoenix at line 3370) include the strike in their terms tables.

**Erratum recommendation:** REVIEW ONLY. Add "Strike: 100% of initial (for physical delivery determination)" to the WOAC terms table.

---

## Verified Barrier/Strike Mechanics

The following product chapters were checked for barrier/strike consistency:

| Product | Barrier/Strike Claim | Location | Status |
|---------|---------------------|----------|:------:|
| RC | "below barrier → knock-in → share delivery at strike" | Lines 2782-2993 | ✓ CORRECT |
| DRC | "below barrier → share delivery; discount entry lowers break-even" | Lines 3666-3876 | ✓ CORRECT |
| KODRC | "KO barrier voids the put if stock drops too fast" | Lines 4338-4355 | ✓ CORRECT |
| Phoenix | "coupon barrier (70%), KI barrier (60%), autocall barrier (100%)" | Lines 3370-3550 | ✓ CORRECT |
| Accumulator | "above strike: standard quantity; below strike: 2× gearing; above KO: terminates" | Lines 20495-20527 | ✓ CORRECT |
| CLN | "default event → recovery applied to principal" | Lines 16793-16811 | ✓ CORRECT |
| FTD | "first default → recovery of defaulted entity" | Lines 17510-17512 | ✓ CORRECT |
| PPN | "100% principal protection + call option upside" | Section 5.1.1 | ✓ CORRECT |

---

## Summary Table

| Finding | Description | Severity | Recommendation |
|:-------:|------------|:--------:|:--------------:|
| BSR-01 | 65% claimed above 100% strike | HIGH | ERRATA REQUIRED |
| BSR-02 | Strike undefined in WOAC terms | MEDIUM | REVIEW ONLY |

---

*Generated: 2026-06-27 | Workstream WS4 | Semantic Consistency Audit Task 4*
