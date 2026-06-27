# ERRATA CANDIDATE LIST — V1.0.1 Planning

**Workstream:** WS9 — Errata Candidate List  
**Scope:** All findings from WS1-WS8, classified by disposition  
**Date:** 2026-06-27  
**Status:** COMPLETE  

---

## Classification Key

| Disposition | Meaning |
|:-----------:|---------|
| **ERRATA REQUIRED** | Must be corrected in V1.0.1. Teaches wrong intuition, contains factual error, or creates irreconcilable cross-artifact contradiction |
| **REVIEW ONLY** | Worth reviewing but not blocking. Ambiguous, could benefit from clarification, but not wrong per se |
| **ACCEPT AS-IS** | Correct or defensible under standard practice. No action needed |
| **OUT OF SCOPE** | Not a semantic/correctness issue (e.g., formatting, style preference) |

---

## ERRATA REQUIRED (7 items)

### E-01: FTD correlation direction label (Desk Bible)
- **Source:** CDA-01
- **Location:** Desk_Bible_v2.md, lines 17352, 17524, 17951
- **Error:** "FTD investors are short correlation. They profit when correlation is high." Label contradicts own explanation. All other artifacts (Interview System, Atlas, Solutions Manual) correctly say FTD is LONG correlation.
- **Fix:** Change "short correlation" to "long correlation" or add convention preamble. Correct the NTD coupon scaling table at 17951.
- **Priority:** P1

### E-02: Worst-of investor correlation direction label (Desk Bible)
- **Source:** CDA-02
- **Location:** Desk_Bible_v2.md, line 17526
- **Error:** "worst-of investors are also short correlation — they profit when stocks move together." Same self-contradiction as E-01.
- **Fix:** Change "short correlation" to "long correlation" or align with convention preamble.
- **Priority:** P1

### E-03: Part 6 protection seller misattribution
- **Source:** CDA-03, SCA-01
- **Location:** production/part6_sections_10_11.md, line 102
- **Error:** "the desk (which sold protection via the short put)" — the INVESTOR sold the put, not the desk. Factual error about position ownership.
- **Fix:** Change to "the desk (which benefits from the investor's short put position)" or "the desk (which holds the long side of the investor's embedded short put)."
- **Priority:** P1

### E-04: Part 6 vs Encyclopedia contradiction on desk worst-of direction
- **Source:** CDA-03
- **Location:** Part 6 line 102 ("long correlation") vs Encyclopedia line 4290 ("SHORT correlation")
- **Error:** Two frozen canonical artifacts make directly opposing claims about the desk's worst-of correlation direction.
- **Fix:** Both artifacts must specify raw vs hedged position. Part 6: add "(hedged position)" qualifier. Encyclopedia: add "(raw/unhedged position)" qualifier.
- **Priority:** P1

### E-05: WOAC "65% above strike (100%)" arithmetic error
- **Source:** BSR-01
- **Location:** Desk_Bible_v2.md, line 22565
- **Error:** "If at maturity ASML finishes at 65%: above strike (100%), so principal returned." 65% is not above 100%. Mathematically wrong.
- **Fix:** Either correct to "below strike" with physical delivery calculation, or change strike to the KI barrier level (60%) if that was the intent.
- **Priority:** P1

### E-06: Dispersion trade direction error (Desk Bible)
- **Source:** CDA-06
- **Location:** Desk_Bible_v2.md, line 22605
- **Error:** "long single-stock vol + short basket vol = long correlation." This trade is SHORT correlation, not long. Contradicts line 22390 which correctly describes the opposite trade as "buying correlation."
- **Fix:** Change "long correlation" to "short correlation" OR reverse the trade legs to "long basket vol + short single-stock vol."
- **Priority:** P2

### E-07: Gamma formula sign error (Desk Bible)
- **Source:** SGN-01
- **Location:** Desk_Bible_v2.md, line 1069
- **Error:** "New Delta ≈ -50 + (3 × 2) = -56." The expression "3 × 2 = 6" yields -50 + 6 = -44, not -56. Should be "3 × (-2) = -6."
- **Fix:** Change "(3 × 2)" to "(3 × (-2))" or "−6."
- **Priority:** P2

---

## REVIEW ONLY (6 items)

### R-01: Interview System V2.2 WOAC self-contradiction
- **Source:** CDA-04
- **Location:** production/interview_system_v2_2.md, line 356
- **Description:** Same self-contradiction pattern as E-01/E-02: labels WOAC investor "short correlation" then describes "benefit from high correlation." Especially confusing because lines 400/407 in the same artifact correctly label FTD as "long correlation."
- **Recommendation:** Should be corrected if the Desk Bible labels are corrected (E-01/E-02), to maintain cross-artifact consistency.

### R-02: NTD correlation table labels for high-N products
- **Source:** CDA-05
- **Location:** Desk_Bible_v2.md, lines 17954-17955
- **Description:** Labels 4TD and 5TD as "long correlation" which appears to conflict with the risk analysis table at 17927-17932 showing risk increases at high correlation for high-N products.
- **Recommendation:** Review in context of convention preamble. May be correct under structural convention.

### R-03: "Bank structurally long correlation" — raw vs hedged ambiguity
- **Source:** SCA-02, HA-03
- **Location:** Desk_Bible_v2.md, line 22483
- **Description:** Describes desk as "structurally long correlation" without specifying this is the hedged position.
- **Recommendation:** Add "(after hedging)" or "(net position)."

### R-04: WOAC strike level undefined in terms table
- **Source:** BSR-02, SCA-03
- **Location:** Desk_Bible_v2.md, lines 22536-22545
- **Description:** Product terms omit the strike level. Referenced at line 22565 as 100% but never defined.
- **Recommendation:** Add "Strike: 100% of initial" to terms.

### R-05: Recovery rate assumption ungrounded
- **Source:** HA-02
- **Location:** Desk_Bible_v2.md, credit worked examples
- **Description:** All credit examples assume 40% recovery without stating this is ISDA convention.
- **Recommendation:** Add one-line note per example.

### R-06: Gamma and Delta signs for short options
- **Source:** SGN-02, SGN-03
- **Location:** Desk_Bible_v2.md, lines 1060-1061
- **Description:** Position Gamma stated as positive (+3) and Delta as negative (-50) for short puts. Non-standard but internally consistent.
- **Recommendation:** Add footnote explaining convention.

---

## ACCEPT AS-IS (6 items)

### A-01: Solutions Manual convention mixing
- **Source:** CDA-07
- **Description:** Uses structural ("sells correlation") and MTM ("suffers when correlations drop") in separate sentences. Individually correct, no same-sentence contradiction.

### A-02: Product DNA Atlas correlation descriptions
- **Source:** CDA-08
- **Description:** Uses correct economic descriptions without directional labels. Avoids the labeling trap entirely.

### A-03: FTD/NTD confusion pair avoids label
- **Source:** IIA-02
- **Description:** Correctly describes economics without committing to "long/short." Safest approach given the convention confusion.

### A-04: "Independent stocks" simplification in Interview System
- **Source:** IIA-03
- **Description:** Zero-correlation formula is standard pedagogy, immediately corrected by correlation discussion.

### A-05: Continuous barrier observation conventions
- **Source:** HA-04
- **Description:** Standard industry assumptions. Covered in Infrastructure Encyclopedia §6.1.

### A-06: Day count and quarterly conventions
- **Source:** HA-05, HA-06
- **Description:** Covered in Desk Bible Foundations. Sequential reading provides prerequisite.

---

## OUT OF SCOPE (1 item)

### O-01: CRA SRT Q4 coupon minor arithmetic discrepancy
- **Location:** Desk_Bible_v2.md, line 13960
- **Description:** Q4 coupon listed as $775,304. Calculated value using Max_Q × (Days_In / Total_Days) = $810,000 × (88/92) = $774,783. Discrepancy of ~$521. Likely rounding or alternative calculation method.
- **Disposition:** OUT OF SCOPE for semantic audit. The discrepancy is <0.1% and does not affect pedagogical understanding. Flagged in red team report for completeness.

---

## Priority Summary

| Priority | Count | Description |
|:--------:|:-----:|-------------|
| P1 | 5 | Self-contradictions, factual errors, cross-artifact contradictions |
| P2 | 2 | Formula/label errors that could mislead but don't create cross-artifact conflict |
| Review | 6 | Ambiguities worth clarifying |
| Accept | 6 | Correct or standard practice |
| OOS | 1 | Minor arithmetic |

---

## V1.0.1 Erratum Package Recommendation

The V1.0.1 erratum should include:

1. **Correlation Convention Preamble** (new content): Define structural vs MTM conventions. Declare canonical convention. Provide mapping table.
2. **FTD/Worst-of label corrections** (E-01, E-02): Change "short" to "long" or align with declared convention.
3. **Part 6 position ownership fix** (E-03): Correct "sold protection" to "bought protection."
4. **Part 6/Encyclopedia qualifier** (E-04): Add raw/hedged position context to both.
5. **WOAC strike error fix** (E-05): Correct the "65% above 100%" claim.
6. **Dispersion direction fix** (E-06): Correct "long" to "short" correlation for the dispersion trade.
7. **Gamma formula fix** (E-07): Add negative sign to stock move.

Total scope: 7 targeted corrections + 1 new preamble section. No structural changes to any artifact.

---

*Generated: 2026-06-27 | Workstream WS9 | Semantic Consistency Audit Task 4*
