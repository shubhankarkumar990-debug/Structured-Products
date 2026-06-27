# V1.0.1 ERRATA ADDENDUM — FINAL

**Package:** Desk Bible Ecosystem V1.0.1 Semantic Errata  
**Effective:** 2026-06-27  
**Scope:** 9 confirmed errata items, 15 line-level corrections across 4 frozen artifacts  
**Canonical convention:** See `correlation_convention_framework_final.md`  
**Status:** FINAL (package closure)  
**Supersedes:** `v1_0_1_errata_addendum.md`

---

## How to Read This Addendum

Each erratum specifies:
- The frozen artifact and exact line number
- The V1.0 text (verbatim, quoted)
- The nature of the error
- The V1.0.1 corrected text
- Rationale

**No frozen V1.0 files are modified.** This addendum is a companion document that supersedes specific lines.

---

## E-01 — FTD Correlation Direction Label (Desk Bible, §1 ELI5)

**File:** `Desk_Bible_v2.md`  
**Line:** 17352  

**V1.0 text:**
> This is the key insight: **FTD investors are short credit correlation**, just as worst-of equity investors are short equity correlation (Section 1.6).

**Error:** The label "short credit correlation" contradicts the economic explanation in the same chapter (line 17524: "They profit when correlation is high"). Under the canonical MTM convention, profiting from high correlation = long correlation. The Interview System V2.2 (line 400), Interview System V1 (line 238), Product DNA Atlas (line 1269), and Solutions Manual (line 1279) all describe FTD as economically long correlation.

**V1.0.1 corrected text:**
> This is the key insight: **FTD investors are long credit correlation** — they benefit when default correlation is high (defaults either all happen or none do, reducing the probability of an isolated first default). The investor is *structurally* short correlation in the sense of having sold the correlation premium, but the economic sensitivity is long: rising correlation helps the FTD position. See the Correlation Convention Framework for the distinction between structural and MTM conventions.

**Rationale:** The economic explanation was already correct. Only the label was wrong under the canonical convention. The structural nuance is preserved via explicit labeling.

---

## E-01b — FTD Correlation Direction Label (Desk Bible, §11 Key Insight)

**File:** `Desk_Bible_v2.md`  
**Line:** 17524  

**V1.0 text:**
> **Key insight:** FTD investors are **short correlation**. They profit when correlation is high (defaults are rare because companies move together) and lose when correlation is low (independent defaults make the first default highly probable).

**Error:** Self-contradictory. "Short correlation" + "profit when correlation is high" teaches opposite directions in the same sentence.

**V1.0.1 corrected text:**
> **Key insight:** FTD investors are **long correlation** (under the MTM sensitivity convention). They profit when correlation is high (defaults are rare because companies move together) and lose when correlation is low (independent defaults make the first default highly probable). Note: the investor *structurally sold* the first-default premium, which some practitioners describe as "selling correlation." V1.0.1 uses the MTM convention — see Correlation Convention Framework.

**Rationale:** Aligns label with explanation. Preserves structural nuance.

---

## E-01c — FTD Direction in NTD Coupon Scaling Table

**File:** `Desk_Bible_v2.md`  
**Line:** 17951  

**V1.0 text:**
> | FTD (N=1) | 9.5% | Highest | Short correlation (unambiguous) |

**V1.0.1 corrected text:**
> | FTD (N=1) | 9.5% | Highest | Long correlation (MTM: risk falls as ρ rises) |

**Rationale:** Aligns with E-01/E-01b correction.

---

## E-02 — Worst-of Correlation Direction Label (Desk Bible)

**File:** `Desk_Bible_v2.md`  
**Line:** 17526  

**V1.0 text:**
> This parallels worst-of equity products (Section 1.6): worst-of investors are also short correlation — they profit when stocks move together and lose when stocks move independently.

**Error:** Same pattern as E-01. "Short correlation" + "profit when stocks move together" = self-contradiction.

**V1.0.1 corrected text:**
> This parallels worst-of equity products (Section 1.6): worst-of investors are also long correlation (MTM convention) — they profit when stocks move together and lose when stocks move independently. Like FTD investors, worst-of investors *structurally sold* the correlation premium, but the economic sensitivity is long: rising correlation reduces worst-of risk.

**Rationale:** Aligns label with explanation. Maintains parallel to FTD.

---

## E-03 — Part 6 Protection Ownership Misattribution

**File:** `production/part6_sections_10_11.md`  
**Line:** 102  

**V1.0 text:**
> The desk benefits when asset correlations increase. Worst-of products create long correlation exposure: when correlations are high, the basket moves together, reducing the probability that the worst performer hits the barrier. This benefits the desk (which sold protection via the short put).

**Error:** The parenthetical "(which sold protection via the short put)" is factually wrong. In worst-of structured notes:
- The **investor** sold the put (embedded short put in the note)
- The **desk** is long the put (bought protection from the investor)

Additionally, the sentence describes the desk's net/hedged position as "long correlation" without stating this is the hedged position.

**V1.0.1 corrected text:**
> The desk's **net (hedged)** position benefits when asset correlations increase. Worst-of products create long correlation exposure for the hedged desk: when correlations are high, the basket moves together, reducing the probability that the worst performer hits the barrier. This benefits the desk's hedged book. (Note: the **investor** sold the embedded put and is structurally short correlation; the desk is long the put and hedges its raw short-correlation exposure via dispersion trades to achieve a net long-correlation position.)

**Rationale:** Corrects position ownership. Adds raw/hedged qualifier. Preserves the original teaching intent about desk Greeks.

---

## E-04 — Part 6 vs Encyclopedia Reconciliation

### E-04a — Part 6 Qualifier

**File:** `production/part6_sections_10_11.md`  
**Line:** 110  

**V1.0 text:**
> | ELN (RC, FCN, Phoenix) | Short gamma, short vega, long correlation (worst-of) |

**V1.0.1 corrected text:**
> | ELN (RC, FCN, Phoenix) | Short gamma, short vega, long correlation (worst-of, **net/hedged** position) |

**Rationale:** The table describes "Typical Desk Greek Position," which is the hedged book. Adding "(net/hedged)" makes this explicit.

### E-04b — Encyclopedia Qualifier

**File:** `production/infrastructure_encyclopedia_v1.md`  
**Line:** 4290  

**V1.0 text:**
> | **Correlation Trade** | A trade that profits from changes in correlation between underlyings. Worst-of products are SHORT correlation (dealer profits if correlation falls) | ...

**V1.0.1 corrected text:**
> | **Correlation Trade** | A trade that profits from changes in correlation between underlyings. The desk's **raw (unhedged)** worst-of position is short correlation — the worst-of put value falls when correlation rises. After dispersion hedging, the desk is typically **net long** correlation. | ...

**Rationale:** Specifies that "short correlation" refers to the raw position. Adds the hedged direction for completeness. Resolves the contradiction with Part 6 without changing either artifact's fundamental claim.

---

## E-05 — WOAC "65% Above Strike (100%)" Error

**File:** `Desk_Bible_v2.md`  
**Line:** 22565  

**V1.0 text:**
> - If at maturity ASML finishes at 65%: above strike (100%), so principal returned + coupons

**Error:** 65% is not above 100%. The statement is mathematically false.

**V1.0.1 corrected text:**
> - If at maturity ASML finishes at 65%: **below strike (100%)**, so **physical delivery applies**. Shares delivered: €500,000 / €700 = 714 ASML shares. Worth 714 × (0.65 × €700) = €324,870. Loss: €175,130 (partially offset by coupons received).

**Rationale:** Corrects a false mathematical claim. The corrected text follows the same format as the 55% scenario on line 22566.

---

## E-06 — Dispersion Trade Direction Error

**File:** `Desk_Bible_v2.md`  
**Line:** 22605  

**V1.0 text:**
> | 6 | P3 | Dispersion hedging diagram | Flow | Bank's hedge: long single-stock vol + short basket vol = long correlation. Shows how the bank manages worst-of risk |

**Error:** Long single-stock vol + short basket vol is a dispersion trade, which profits when stocks diverge (low correlation). This is short correlation, not long. Contradicts line 22483 which correctly describes the same trade.

**V1.0.1 corrected text:**
> | 6 | P3 | Dispersion hedging diagram | Flow | Bank's hedge: long single-stock vol + short basket vol = **short** correlation (dispersion trade). Shows how the bank manages worst-of risk |

**Rationale:** Resolves a trade-legs-vs-label contradiction. Aligns with the same chapter's own description at line 22483.

---

## E-07 — Gamma Sign Error

**File:** `Desk_Bible_v2.md`  
**Line:** 1069  

**V1.0 text:**
> - **Gamma effect:** After the $2 drop, your Delta changed. New Delta ≈ -50 + (3 × 2) = -56. Your exposure to further drops has increased.

**Error:** The intermediate expression "3 × 2 = 6" yields −50 + 6 = −44, not −56. The stock dropped $2, so ΔS = −2. The correct intermediate step is 3 × (−2) = −6.

**V1.0.1 corrected text:**
> - **Gamma effect:** After the $2 drop, your Delta changed. New Delta ≈ -50 + (3 × (−2)) = -50 − 6 = **-56**. Your exposure to further drops has increased.

**Rationale:** Fixes the intermediate arithmetic so a student following step-by-step gets the correct result. The final answer is unchanged.

---

## E-08 — Interview System WOAC Correlation Self-Contradiction (PROMOTED from R-01)

**File:** `production/interview_system_v2_2.md`  
**Line:** 356  

**V1.0 text:**
> The investor is SHORT correlation: they benefit from high correlation (stocks move together, reducing worst-of risk) and lose from low correlation (independent moves increase the chance of one stock hitting the barrier).

**Error:** Same self-contradiction pattern as E-01 and E-02. The label "SHORT correlation" is immediately contradicted by "they benefit from high correlation." Under the canonical MTM convention, benefiting from high correlation = long correlation. Applying the correlation sanity check: label says SHORT, economics say benefits from rising → LONG. Label is wrong.

**Promotion justification:** This is the exact same error class as E-01/E-02, in the ecosystem's primary interview-preparation artifact. Leaving it uncorrected while correcting E-01/E-02 creates a cross-artifact inconsistency: a candidate would find "long correlation" for FTD (Desk Bible, corrected) but "short correlation" for WOAC (Interview System, uncorrected) — even though both products have the same investor correlation direction. The Interview System's own lines 400 and 407 correctly label FTD as "long correlation," creating an internal contradiction within the same artifact if line 356 remains uncorrected.

**V1.0.1 corrected text:**
> The investor is **long** correlation (MTM convention): they benefit from high correlation (stocks move together, reducing worst-of risk) and lose from low correlation (independent moves increase the chance of one stock hitting the barrier). The investor is *structurally* short — they sold the correlation premium embedded in the worst-of basket coupon.

**Note on line 358:** Line 358 lists "PLUS short correlation" as a Greek in the desk's risk profile. This is correct for the desk's raw position (the desk is long the worst-of put, whose value decreases with correlation) and does not require correction. The distinction: line 356 describes the *investor's* direction (corrected to long), while line 358 describes the *desk's raw* Greek (correctly short).

**Rationale:** Eliminates the last same-sentence self-contradiction in the ecosystem's correlation language. Aligns the Interview System with the Desk Bible corrections and the Correlation Convention Framework. Preserves the structural nuance via explicit labeling.

---

## E-09 — NTD Coupon Scaling Table Labels (PROMOTED from R-02)

**File:** `Desk_Bible_v2.md`  
**Lines:** 17952-17955  

**V1.0 text (rows 2-5 of the coupon scaling table):**

| Product | Coupon | Risk | Correlation Sensitivity |
|---------|:------:|:----:|:-----------------------:|
| 2TD (N=2) | 5.0% | Medium | Short at low ρ, reversal at high ρ |
| 3TD (N=3) | 2.5% | Lower | Reversal at moderate ρ |
| 4TD (N=4) | 1.0% | Low | Long correlation (approximately) |
| 5TD (N=5) | 0.3% | Lowest | Long correlation (unambiguous) |

**Error:** Under the canonical MTM convention, all NTD products (N≥2) are SHORT correlation — their risk increases as ρ rises. The risk analysis table at lines 17927-17932 in the same chapter confirms this: 2TD risk rises from LOW at ρ=0.1 to HIGH at ρ=0.95. The pattern holds for all N≥2.

The current labels for 4TD ("Long correlation") and 5TD ("Long correlation (unambiguous)") directly contradict the risk table. By the CDO analogy: 5TD ≈ super-senior tranche = SHORT correlation (losses cluster at high ρ, reaching the senior level).

The "reversal" labels for 2TD and 3TD are misleading: they imply a within-product direction flip that does not exist. Under MTM, 2TD risk monotonically increases with ρ at all levels. The "reversal" refers to the FTD-vs-NTD direction difference, not a non-monotonicity within 2TD.

**Promotion justification:** The labels teach the wrong correlation direction for high-N products and use ambiguous "reversal" language that contradicts the same chapter's risk table. With E-01c correcting the FTD row to "Long correlation," leaving 5TD as "Long correlation (unambiguous)" creates a same-table contradiction: two products with opposite economic behavior would carry the same label.

**V1.0.1 corrected text:**

| Product | Coupon | Risk | Correlation Sensitivity |
|---------|:------:|:----:|:-----------------------:|
| 2TD (N=2) | 5.0% | Medium | Short correlation (reversed from FTD: high ρ → clustered defaults → higher NTD risk) |
| 3TD (N=3) | 2.5% | Lower | Short correlation (reversal from FTD amplified at moderate ρ) |
| 4TD (N=4) | 1.0% | Low | Short correlation (high ρ → if defaults cluster, 4th-default threshold breached) |
| 5TD (N=5) | 0.3% | Lowest | Short correlation (high ρ → all-or-nothing → if one defaults, all do → 5TD triggered; ≈ CDO super-senior) |

**Rationale:** Aligns all rows with the MTM convention. Consistent with the risk analysis table at 17927-17932. Consistent with the Correlation Convention Framework which states "NTD (N≥2): SHORT correlation." Clarifies that "reversal" means the direction difference between FTD and NTD, not a within-product flip.

---

## Summary

| Erratum | Artifact | Line(s) | Error Type | Priority |
|:-------:|----------|:-------:|:----------:|:--------:|
| E-01 (a,b,c) | Desk Bible | 17352, 17524, 17951 | Correlation label self-contradiction | P1 |
| E-02 | Desk Bible | 17526 | Correlation label self-contradiction | P1 |
| E-03 | Part 6 | 102 | Position ownership + raw/hedged omission | P1 |
| E-04 (a,b) | Part 6 + Encyclopedia | 110, 4290 | Cross-artifact contradiction (raw vs hedged) | P1 |
| E-05 | Desk Bible | 22565 | Strike reference arithmetic error | P1 |
| E-06 | Desk Bible | 22605 | Dispersion trade direction error | P2 |
| E-07 | Desk Bible | 1069 | Gamma formula sign error | P2 |
| E-08 | Interview System V2.2 | 356 | Correlation label self-contradiction (promoted from R-01) | P1 |
| E-09 | Desk Bible | 17952-17955 | NTD table direction labels inverted (promoted from R-02) | P1 |

**Total scope:** 15 line-level corrections across 4 artifacts. No structural changes.

---

*V1.0.1 Errata Addendum | FINAL (package closure) | 2026-06-27*
