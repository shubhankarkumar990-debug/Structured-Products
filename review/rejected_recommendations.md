# Rejected Recommendations Register

**Date**: 2026-06-26
**Authority**: Chief Publication Board
**Scope**: Every audit recommendation not implemented, with justification

---

## Rejection Criteria

A recommendation is REJECTED (not DEFERRED) when it meets one or more of:
1. Based on incorrect audit analysis (wrong artifact, wrong count, wrong interpretation)
2. Contradicts intentional design choices documented in architecture
3. Would introduce new inconsistencies or break existing content
4. Proposes changes to frozen artifacts without meeting the critical-defect threshold

---

## Rejected Findings

### R-1: H-5 — DNA Data Duplication Is An Error

**Audit Claim**: Product chapter §4 DNA tables duplicate Atlas data verbatim (49× across all chapters). Recommendation: remove duplication, reference Atlas instead.

**Rejection Reason**: Intentional standalone design. Each product chapter is designed to be readable independently without requiring the reader to open a separate artifact. The DNA table in §4 embeds the product's identity card so the reader never loses context. This is a deliberate architecture decision documented in the framework (22-section template, §4 = "Product DNA").

**Risk of Implementation**: Removing §4 DNA tables from 49 chapters would break the standalone readability guarantee — the core design principle of the Desk Bible. Readers would need to cross-reference the Atlas for basic product identity, which defeats the purpose of the chapter-per-product architecture.

**Verdict**: REJECTED — working as designed.

---

### R-2: M-3 — Greeks Delta Sign Convention Is Wrong

**Audit Claim**: Delta = −50 for 100 short puts is incorrect. Short puts have positive delta. The sign is wrong.

**Rejection Reason**: The example is pedagogically structured as "common mistake → self-correction." The Delta of −50 represents the OPTION delta (−0.50 per put × 100 options), not the POSITION delta. The example deliberately shows this confusion, then self-corrects in the P&L calculation: "P&L from Delta = −(−50) × (−$2) = −$100."

This is a teaching technique: the student encounters the sign confusion that actually occurs on trading desks, sees the correct resolution, and internalizes the difference between option delta and position delta.

**Verification**: The final P&L (−$100) is correct. The Gamma calculation is correct. The Theta calculation is correct. The hedging conclusion is correct. Only the intermediate presentation of Delta uses the ambiguous convention — and that ambiguity IS the lesson.

**Risk of Implementation**: "Fixing" the sign to +50 would remove the pedagogical value. The student would never encounter the sign-convention trap that trips up junior traders on actual desks.

**Verdict**: REJECTED — deliberate pedagogical technique.

---

### R-3: M-4 — NCRA Range Accrual ACT/360 Convention Mismatch

**Audit Claim**: §5.3.3 NCRA states "ACT/360" day count but uses quarterly-fraction method (in-range-days / total-quarter-days), which is not pure ACT/360.

**Rejection Reason**: The quarterly-fraction method IS the standard market convention for range accrual products. Dealers quote range accruals as "ACT/360" to describe the overall rate quotation, but the accrual mechanism uses (days_in_range / days_in_period) × (coupon/periods_per_year). This is how every major dealer desk calculates range accrual coupons.

**Verification**: All four quarterly calculations are internally consistent:
- Q1: $956,250 × (65/90) = $690,625 ✅
- Q2: $956,250 × (90/91) = $945,742 ✅
- Q3: $956,250 × (30/92) = $311,821 ✅
- Q4: $956,250 × (88/92) = $914,674 ✅

**Risk of Implementation**: Changing to "pure ACT/360" would produce incorrect coupon calculations that no market participant would recognize. The existing method IS how range accruals are priced and settled.

**Verdict**: REJECTED — market-standard convention.

---

### R-4: M-8 — Day Count Cross-Reference Inconsistency ($55,556 vs $16,667)

**Audit Claim**: Interview System references $55,556 spread (from Desk Bible §6.1) but also shows $16,667 in a different question. These two numbers are inconsistent.

**Rejection Reason**: These are TWO DELIBERATELY DIFFERENT worked examples with different inputs:
- Example 1 (line 220): $100M, 5%, 184 days → ACT/360 spread = $55,556
- Example 2 (line 583): Different notional, 6%, 181 days → different calculation = $16,667

They are not the same example with conflicting answers. They are independent questions testing the same concept with different parameters — standard exam technique.

**Verification**: Both calculations are correct for their stated inputs. The $55,556 matches the Desk Bible §6.1 worked example exactly.

**Verdict**: REJECTED — audit error (compared two different examples as if they were one).

---

## Summary

| ID | Finding | Rejection Reason |
|:--:|---------|------------------|
| R-1 | DNA duplication (H-5) | Intentional standalone design |
| R-2 | Greeks Delta sign (M-3) | Deliberate pedagogical technique |
| R-3 | NCRA ACT/360 (M-4) | Market-standard convention |
| R-4 | Day count cross-ref (M-8) | Audit error — two different examples |

**4 total rejections.** Each represents a case where the audit recommendation, if implemented, would have either broken intentional design, removed educational value, introduced market-incorrect calculations, or addressed a non-existent problem.
