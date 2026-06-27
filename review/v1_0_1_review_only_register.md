# V1.0.1 REVIEW-ONLY REGISTER

**Purpose:** Items that warrant review but are not classified as errata. Each item may be corrected via optional clarifying note or left as-is with justification.  
**Status:** FINAL  

---

## R-01 — Interview System WOAC Self-Contradiction

**File:** `production/interview_system_v2_2.md`  
**Line:** 356  

**V1.0 text:**
> The investor is SHORT correlation: they benefit from high correlation (stocks move together, reducing worst-of risk) and lose from low correlation.

**Issue:** Same self-contradiction pattern as E-01/E-02: labels investor "short correlation" then describes "benefit from high correlation."

**Convention analysis:** The label uses structural convention (investor sold the correlation premium → short). The explanation uses MTM convention (benefits from high ρ → long). Both are individually correct, but combining them in one sentence is confusing.

**Recommendation:** ALIGN WITH CANONICAL CONVENTION. Under V1.0.1's MTM default, change to:
> The investor is **long** correlation (MTM convention): they benefit from high correlation (stocks move together, reducing worst-of risk) and lose from low correlation. The investor is *structurally* short — they sold the correlation premium embedded in the basket coupon.

**Priority:** Should be corrected when E-01/E-02 are corrected, to maintain cross-artifact consistency. Without this change, the Interview System and Desk Bible would give opposite answers on the same question.

---

## R-02 — NTD Table Labels for High-N Products

**File:** `Desk_Bible_v2.md`  
**Lines:** 17949-17955  

**V1.0 text (coupon scaling table):**
| Product | Correlation Sensitivity |
|---------|:-----------------------:|
| FTD (N=1) | Short correlation (unambiguous) |
| 2TD (N=2) | Short at low ρ, reversal at high ρ |
| 3TD (N=3) | Reversal at moderate ρ |
| 4TD (N=4) | Long correlation (approximately) |
| 5TD (N=5) | Long correlation (unambiguous) |

**Issue:** Under the canonical MTM convention:
- FTD is LONG correlation (corrected in E-01c)
- ALL NTD products (N≥2) are SHORT correlation: higher ρ → defaults cluster → once first default occurs, subsequent defaults follow quickly → NTD risk increases
- The "reversal" refers to the direction flip between FTD and NTD, not a within-product non-monotonicity
- The labels for 4TD ("long") and 5TD ("long") appear inverted under MTM convention

**Convention analysis:**
The Desk Bible may have derived 5TD = "long" by reasoning "5TD is the opposite of FTD, and FTD is short, so 5TD must be long." Under the (incorrect) structural labeling of FTD as "short," this produced 5TD as "long." Once FTD is relabeled "long" (E-01c), the 5TD label should be re-examined.

**Risk table cross-check (lines 17927-17932):**
The risk analysis table shows 2TD risk as LOW at low ρ and HIGH at very high ρ. This means 2TD (and by extension all NTD) risk increases with ρ → SHORT correlation (MTM). The risk table is correct; the coupon scaling table labels are inconsistent with it.

**Recommendation:** Correct the coupon scaling table to:

| Product | Correlation Sensitivity |
|---------|:-----------------------:|
| FTD (N=1) | Long correlation (benefits from high ρ) |
| 2TD (N=2) | Short correlation (reversed from FTD: high ρ → clustered defaults → higher NTD risk) |
| 3TD (N=3) | Short correlation (reversal amplified) |
| 4TD (N=4) | Short correlation (high ρ → if defaults cluster, N-4 threshold breached) |
| 5TD (N=5) | Short correlation (high ρ → all-or-nothing → if one defaults, all do → 5TD triggered) |

**Priority:** Should be corrected alongside E-01c. The existing labels teach the wrong direction for high-N products.

---

## R-03 — "Bank Structurally Long Correlation" Ambiguity

**File:** `Desk_Bible_v2.md`  
**Line:** 22483  

**V1.0 text:**
> The bank is structurally long correlation (benefits when stocks move together).

**Issue:** Does not specify whether this refers to the raw or hedged position. The same paragraph describes the dispersion hedge, implying this is the hedged/net position.

**Recommendation:** Add qualifier:
> The bank's **net (hedged)** position is typically long correlation (benefits when stocks move together).

**Priority:** Low. The paragraph's context makes the intent clear, but the qualifier prevents confusion if the sentence is read in isolation.

---

## R-04 — WOAC Strike Level Undefined

**File:** `Desk_Bible_v2.md`  
**Lines:** 22536-22545  

**Issue:** The worked example terms table omits the strike level. The strike is referenced at line 22565 as 100% but was never defined.

**Recommendation:** Add to terms table:
> - Strike: 100% of initial (for maturity payoff determination)

**Priority:** Low. Supports E-05 correction by making the strike explicit.

---

## R-05 — Recovery Rate Assumption

**File:** `Desk_Bible_v2.md`  
**Locations:** Credit worked examples (CLN, FTD, NTD)

**Issue:** All credit examples assume 40% recovery without stating this is the standard ISDA convention.

**Recommendation:** Add one-line note to each credit worked example:
> *(40% recovery is the standard ISDA assumption for senior unsecured corporate debt. Actual recoveries range from <10% (e.g., Lehman: 8.6%) to >90%.)*

**Priority:** Low. The concept is covered in the Interview System V2.2 (line 412) and Solutions Manual.

---

## R-06 — Short Option Delta/Gamma Sign Convention

**File:** `Desk_Bible_v2.md`  
**Lines:** 1060-1061  

**Issue:** The Greeks table lists Delta = −50 and Gamma = +3 for a short-put position. Under standard Black-Scholes convention, 100 short puts have positive position delta (+50) and negative position gamma (−3).

**Convention analysis:** The example uses the LONG option's Greeks (Delta = −0.50 per option × 100 = −50 total) without flipping the sign for the short position. This is non-standard but internally consistent — the P&L calculations at lines 1067-1068 produce the correct economic outcome.

**Recommendation:** Add footnote:
> *Note: The Greeks shown are the per-option values scaled by 100 contracts, before accounting for the short position. Position Greeks for the short would flip signs (Delta = +50, Gamma = −3). The worked example uses the unsigned convention for pedagogical clarity and adjusts signs in the P&L calculations.*

**Priority:** Low. The economic intuition taught is correct despite the non-standard sign convention.

---

## R-07 — CRA SRT Q4 Coupon Discrepancy

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

---

## Summary

| Item | Description | Recommendation | Priority |
|:----:|------------|:--------------:|:--------:|
| R-01 | Interview System WOAC direction | Align with canonical convention | Medium |
| R-02 | NTD table for high-N products | Correct labels to MTM convention | Medium |
| R-03 | Bank long correlation qualifier | Add "net/hedged" | Low |
| R-04 | WOAC strike undefined | Add to terms table | Low |
| R-05 | Recovery rate assumption | Add one-line note | Low |
| R-06 | Short option sign convention | Add footnote | Low |
| R-07 | CRA SRT Q4 discrepancy | Correct or accept | Low |

---

*V1.0.1 Review-Only Register | FINAL | 2026-06-27*
