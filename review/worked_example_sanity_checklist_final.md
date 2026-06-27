# WORKED EXAMPLE SANITY CHECKLIST — V1.0.1 FINAL

**Purpose:** Reusable QA checklist for verifying worked examples in the Desk Bible ecosystem.  
**Usage:** Apply to every worked example before publication or erratum approval.  
**Status:** FINAL (package closure)  
**Supersedes:** `worked_example_sanity_checklist.md`

---

## Checklist

| # | Category | Check | Pass? |
|:-:|----------|-------|:-----:|
| 1 | **Formula** | Every formula matches its stated source (textbook, industry standard, or earlier chapter definition) | ☐ |
| 2 | **Intermediate arithmetic** | Every intermediate calculation step produces the value shown. No dropped signs, no wrong operator precedence | ☐ |
| 3 | **Final arithmetic** | The final answer matches the intermediate steps. No "correct answer from wrong steps" | ☐ |
| 4 | **Units** | All values carry correct units (%, $, bp, shares, contracts). No unit confusion (e.g., percentage vs decimal) | ☐ |
| 5 | **Sign convention** | All signs (positive/negative) are consistent with the stated position direction. Gamma × ΔS includes the sign of ΔS | ☐ |
| 6 | **Position convention** | Every position label (long/short, buy/sell) matches the economic description. No self-contradictory sentences | ☐ |
| 7 | **Raw vs hedged** | If the example references a desk position, it states whether raw or hedged | ☐ |
| 8 | **Economic intuition** | The economic explanation matches the arithmetic. If the answer says "investor profits," the numbers show positive P&L | ☐ |
| 9 | **Stress scenario** | At least one adverse scenario is shown with correct arithmetic and intuition | ☐ |
| 10 | **Opposite scenario** | The complementary outcome (e.g., if Scenario 1 is "stock rises," Scenario 2 is "stock falls") is present and correct | ☐ |
| 11 | **Cross-artifact consistency** | The same product/concept in other artifacts (Interview System, Atlas, Solutions Manual) does not contradict this example | ☐ |
| 12 | **Terms completeness** | Every parameter used in the calculation is defined in the terms table. No parameter referenced without definition | ☐ |
| 13 | **Barrier/strike clarity** | If barriers or strikes are referenced, they are numerically defined and consistently applied | ☐ |
| 14 | **Day count / frequency** | If applicable, the day count convention and payment frequency are stated and consistently applied | ☐ |
| 15 | **Correlation convention** | If correlation direction is mentioned, it uses the canonical MTM convention (or explicitly flags structural usage). See `correlation_convention_framework_final.md` | ☐ |

---

## How to Use

1. Fill in the checklist for each worked example.
2. Any failed check requires a correction or an explicit justification for why it is acceptable.
3. Attach the completed checklist to the review record for that example.

---

## Quick Sanity Tests

### Arithmetic Spot-Check
Pick the most complex formula in the example. Recalculate it from scratch using only the stated inputs. If you get a different number, investigate.

### Sign Spot-Check
For any formula involving ΔS (price change) or Δρ (correlation change):
- Verify the sign of ΔS/Δρ is included, not dropped
- Verify the sign of the Greek/sensitivity is correct for the stated position (long vs short)
- Verify the product (Greek × ΔS) has the correct sign for the stated P&L direction

### Intuition Spot-Check
Read the economic explanation without looking at the numbers. Predict the direction (profit/loss, increase/decrease). Then check whether the numbers confirm your prediction. If they don't, either the explanation or the arithmetic is wrong.

---

## Errata Items Caught by This Checklist

| Checklist # | Erratum | Error Caught |
|:-----------:|:-------:|-------------|
| 2, 5 | E-07 | Gamma sign dropped in intermediate step |
| 3, 8 | E-05 | "65% above 100%" — arithmetic impossible |
| 6 | E-01, E-02, E-08 | Label contradicts economic description |
| 7 | E-03, E-04a, E-04b | Raw/hedged omitted, causing cross-artifact contradiction |
| 12 | R-02 (now E-09) | NTD table labels contradicted risk table in same chapter |

---

*V1.0.1 Worked Example Sanity Checklist | FINAL (package closure) | 2026-06-27*
