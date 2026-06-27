# SIGN CONVENTION AUDIT — V1.0 Review

**Workstream:** WS3 — Sign Convention Audit  
**Scope:** All formulas and worked examples — verify sign consistency  
**Date:** 2026-06-27  
**Status:** COMPLETE  

---

## Executive Summary

The V1.0 ecosystem's formulas and worked examples are overwhelmingly sign-correct. Two sign-related findings were identified in the Desk Bible's Greeks worked example, both in the same passage. All other worked examples (forward rates, variance swaps, ZCL accretion, digital cap-floor, range accrual, CLN recovery, SA-CCR/RAROC, accumulator/decumulator) verified correct.

---

## FINDING SGN-01: Gamma calculation drops negative sign on stock move

**Severity:** MEDIUM  
**Artifact:** Desk_Bible_v2.md (FROZEN), line 1069

**Context:** Greeks worked example. Trader has sold 100 ATM puts. Stock drops $2.

**Quoted text:**
> "Gamma effect: After the $2 drop, your Delta changed. New Delta ≈ -50 + (3 × 2) = -56."

**Problem:** The stock dropped $2, so ΔS = −2. The correct formula is:

New Delta = Old Delta + Gamma × ΔS = −50 + 3 × (−2) = −50 − 6 = −56

The written formula uses "3 × 2" (positive) instead of "3 × (−2)" (negative). The arithmetic as written:

−50 + (3 × 2) = −50 + 6 = **−44** (not −56)

The final answer (−56) is correct, but the intermediate expression produces −44, not −56. A student following the written formula step by step would get −44 and be confused.

**Root issue:** The sign of the stock move was dropped. "3 × 2" should be "3 × (−2)".

**Impact:** This teaches incorrect formula application. A student who memorizes "Gamma × magnitude" instead of "Gamma × ΔS (with sign)" will make sign errors in real calculations.

**Erratum recommendation:** ERRATA REQUIRED. Change the formula to: "New Delta ≈ −50 + (3 × (−2)) = −50 − 6 = −56."

---

## FINDING SGN-02: Position Gamma sign for short options

**Severity:** LOW  
**Artifact:** Desk_Bible_v2.md (FROZEN), line 1061

**Quoted text:**
> "Gamma | 3 | If the stock moves $1, your Delta changes by 3"

**Context:** The trader has SOLD 100 puts. For short options, position Gamma is negative (you sold convexity).

**Problem:** The table lists Gamma as +3 (positive) for a short-put position. Per-option Gamma is always positive, but the position Gamma for 100 short puts would be −100 × γ_per_option = negative.

**Mitigating factor:** The worked example's economic narrative is correct — the trader's delta becomes more negative after the stock drops, consistent with the short-put dynamics. The Gamma value of +3 could be interpreted as the absolute magnitude of delta change per dollar move, which is a valid desk convention (many risk systems display unsigned Gamma). The sign is handled implicitly in the calculation.

**Impact:** Low. The economic intuition taught is correct. The sign convention is non-standard but defensible as a desk practice shorthand.

**Erratum recommendation:** REVIEW ONLY. Adding a note that "Position Gamma for short options is negative; +3 represents the magnitude" would clarify.

---

## FINDING SGN-03: Delta sign for short puts

**Severity:** LOW  
**Artifact:** Desk_Bible_v2.md (FROZEN), line 1060

**Quoted text:**
> "Delta | -50 | If the stock rises $1, your position loses $50 (you are short puts)"

**Problem:** Short puts have POSITIVE delta under the standard Black-Scholes convention:
- Long put delta: −0.50 per option
- 100 short puts: position delta = −100 × (−0.50) = +50

A short-put position BENEFITS from stock rises (puts become less valuable), so "loses $50 when stock rises" is wrong for short puts.

**Mitigating factor:** The example consistently uses Delta = −50 throughout and the P&L calculations at lines 1067-1068 produce the correct economic outcome (losing money when the stock drops). The sign convention, while non-standard, is internally consistent within the example.

**Impact:** Low for the worked example in isolation (internally consistent). Higher risk if a student applies the same sign convention to other products.

**Erratum recommendation:** REVIEW ONLY. The entire example could be reworked with standard sign conventions, but this is a non-trivial edit that goes beyond erratum scope. A footnote explaining the convention would suffice.

---

## Verified Sign-Correct Examples

The following worked examples were independently recalculated and confirmed sign-correct:

| Example | Location | Status |
|---------|----------|:------:|
| Forward rate (1Y vs 2Y) | Lines 1296-1308 | ✓ CORRECT |
| Variance swap (vega notional conversion) | Lines 10223-10237 | ✓ CORRECT |
| ZCL accretion (4-year) | Lines 13028-13046 | ✓ CORRECT |
| Digital cap-floor (SOFR digital) | Lines 14416-14429 | ✓ CORRECT |
| Range accrual STEG (4 quarters) | Lines 15366-15380 | ✓ CORRECT |
| CLN recovery value | Lines 16793-16811 | ✓ CORRECT |
| SA-CCR EAD calculation | Lines 24366-24400 | ✓ CORRECT |
| RAROC calculation | Lines 24400-24428 | ✓ CORRECT |
| DRC scenarios (3 of 3) | Lines 3775-3823 | ✓ CORRECT |
| KODRC scenarios | Lines 4338-4355 | ✓ CORRECT |
| Accumulator scenarios | Lines 20495-20527 | ✓ CORRECT |
| Option on RC scenarios | Lines 20182-20204 | ✓ CORRECT |

---

## Summary Table

| Finding | Description | Severity | Recommendation |
|:-------:|------------|:--------:|:--------------:|
| SGN-01 | Gamma formula drops sign | MEDIUM | ERRATA REQUIRED |
| SGN-02 | Position Gamma unsigned | LOW | REVIEW ONLY |
| SGN-03 | Delta sign for short puts | LOW | REVIEW ONLY |

---

*Generated: 2026-06-27 | Workstream WS3 | Semantic Consistency Audit Task 4*
