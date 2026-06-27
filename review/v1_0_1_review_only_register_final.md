# V1.0.1 REVIEW-ONLY REGISTER — FINAL

**Purpose:** Items that warrant review but are not classified as errata. Each item may be corrected via optional clarifying note or left as-is with justification.  
**Status:** FINAL (package closure)  
**Supersedes:** `v1_0_1_review_only_register.md`

**Note:** Original R-01 (Interview System WOAC self-contradiction) and R-02 (NTD table labels) were promoted to errata required during package closure. See E-08 and E-09 in `v1_0_1_errata_addendum_final.md`. Remaining items renumbered R-01 through R-05.

---

## R-01 — "Bank Structurally Long Correlation" Ambiguity

*Previously R-03*

**File:** `Desk_Bible_v2.md`  
**Line:** 22483  

**V1.0 text:**
> The bank is structurally long correlation (benefits when stocks move together).

**Issue:** Does not specify whether this refers to the raw or hedged position. The same paragraph describes the dispersion hedge, implying this is the hedged/net position.

**Recommendation:** Add qualifier:
> The bank's **net (hedged)** position is typically long correlation (benefits when stocks move together).

**Priority:** Low. The paragraph's context makes the intent clear, but the qualifier prevents confusion if the sentence is read in isolation.

**Closure decision:** RETAIN AS REVIEW-ONLY. The sentence is in a dispersion-hedging context that makes the hedged interpretation clear. Not a self-contradiction — merely an omitted qualifier.

---

## R-02 — WOAC Strike Level Undefined

*Previously R-04*

**File:** `Desk_Bible_v2.md`  
**Lines:** 22536-22545  

**Issue:** The worked example terms table omits the strike level. The strike is referenced at line 22565 as 100% but was never defined.

**Recommendation:** Add to terms table:
> - Strike: 100% of initial (for maturity payoff determination)

**Priority:** Low. Supports E-05 correction by making the strike explicit.

**Closure decision:** RETAIN AS REVIEW-ONLY. The strike is implicit from context and can be inferred from E-05's corrected text. Not an error — a completeness improvement.

---

## R-03 — Recovery Rate Assumption

*Previously R-05*

**File:** `Desk_Bible_v2.md`  
**Locations:** Credit worked examples (CLN, FTD, NTD)

**Issue:** All credit examples assume 40% recovery without stating this is the standard ISDA convention.

**Recommendation:** Add one-line note to each credit worked example:
> *(40% recovery is the standard ISDA assumption for senior unsecured corporate debt. Actual recoveries range from <10% (e.g., Lehman: 8.6%) to >90%.)*

**Priority:** Low. The concept is covered in the Interview System V2.2 (line 412) and Solutions Manual.

**Closure decision:** RETAIN AS REVIEW-ONLY. This is a pedagogical enhancement, not an error correction.

---

## R-04 — Short Option Delta/Gamma Sign Convention

*Previously R-06*

**File:** `Desk_Bible_v2.md`  
**Lines:** 1060-1061  

**Issue:** The Greeks table lists Delta = −50 and Gamma = +3 for a short-put position. Under standard Black-Scholes convention, 100 short puts have positive position delta (+50) and negative position gamma (−3).

**Convention analysis:** The example uses the LONG option's Greeks (Delta = −0.50 per option × 100 = −50 total) without flipping the sign for the short position. This is non-standard but internally consistent — the P&L calculations at lines 1067-1068 produce the correct economic outcome.

**Recommendation:** Add footnote:
> *Note: The Greeks shown are the per-option values scaled by 100 contracts, before accounting for the short position. Position Greeks for the short would flip signs (Delta = +50, Gamma = −3). The worked example uses the unsigned convention for pedagogical clarity and adjusts signs in the P&L calculations.*

**Priority:** Low. The economic intuition taught is correct despite the non-standard sign convention.

**Closure decision:** RETAIN AS REVIEW-ONLY. The convention is internally consistent and the P&L is correct. E-07 already corrects the one place where the convention breaks down (the Gamma × ΔS intermediate step).

---

## R-05 — CRA SRT Q4 Coupon Discrepancy

*Previously R-07*

**File:** `Desk_Bible_v2.md`  
**Line:** 13960  

**V1.0 text:**
> | Q4 | 88 | 92 | $775,304 |

**Issue:** Using the stated formula (Max_Q × Days_In_Range / Total_Days):
- Max_Q = $60,000,000 × 5.40% / 4 = $810,000
- Q4 = $810,000 × 88/92 = $774,783

The table shows $775,304 — a discrepancy of $521. Q1-Q3 match the formula exactly.

**Analysis:** The discrepancy cannot be explained by any standard alternative day count convention (Act/360 direct, Act/365, different total days). Most likely a calculation or transcription error isolated to Q4.

**Year 1 total impact:** The stated total ($2,690,159) includes the inflated Q4 value. Corrected total: $2,689,637. The effective rate changes from 4.48% to 4.48% (difference rounds away at 2 decimal places).

**Recommendation:** Correct Q4 to $774,783 and Year 1 total to $2,689,637 for strict formula consistency. Alternatively, accept as-is since the effective rate rounds to the same value.

**Priority:** Low. The pedagogical impact is negligible.

**Closure decision:** RETAIN AS REVIEW-ONLY. The $521 discrepancy has zero impact on the effective rate at displayed precision. Correcting it is optional and does not affect any taught concept.

---

## Summary

| Item | Description | Recommendation | Priority | Origin |
|:----:|------------|:--------------:|:--------:|:------:|
| R-01 | Bank long correlation qualifier | Add "net/hedged" | Low | Was R-03 |
| R-02 | WOAC strike undefined | Add to terms table | Low | Was R-04 |
| R-03 | Recovery rate assumption | Add one-line note | Low | Was R-05 |
| R-04 | Short option sign convention | Add footnote | Low | Was R-06 |
| R-05 | CRA SRT Q4 discrepancy | Correct or accept | Low | Was R-07 |

---

## Promoted Items (No Longer in This Register)

| Original ID | Promoted To | Reason |
|:-----------:|:----------:|--------|
| R-01 | **E-08** | Same self-contradiction pattern as E-01/E-02. Cross-artifact consistency requires correction. |
| R-02 | **E-09** | NTD table labels inverted under MTM. Contradicts risk table in same chapter. Same-table inconsistency after E-01c. |

---

*V1.0.1 Review-Only Register | FINAL (package closure) | 2026-06-27*
