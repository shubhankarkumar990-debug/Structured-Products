# CORRELATION DIRECTION AUDIT — V1.0 Semantic Consistency Review

**Workstream:** WS2 — Correlation Direction Audit  
**Scope:** Every correlation direction claim across all frozen canonical artifacts  
**Date:** 2026-06-27  
**Status:** COMPLETE  

---

## Executive Summary

The V1.0 ecosystem contains a **systemic correlation direction inconsistency** rooted in the conflation of two distinct conventions:

1. **Structural convention:** "short correlation" = the investor SOLD the correlation premium (earns yield by taking correlation risk)
2. **MTM sensitivity convention:** "short correlation" = the position LOSES value when correlation RISES

These conventions produce **opposite labels for the same position**. The Desk Bible and Interview System V2.2 use both conventions within single sentences, producing self-contradictory statements. Two canonical artifacts (Part 6 and Infrastructure Encyclopedia) directly contradict each other on the desk's worst-of correlation direction.

**Finding count:** 8 findings (3 HIGH severity, 3 MEDIUM, 2 LOW)

---

## Convention Framework

Before cataloging findings, the two conventions must be defined:

| Convention | "Long correlation" means | "Short correlation" means |
|:----------:|:------------------------:|:-------------------------:|
| **Structural** | Bought the correlation premium | Sold the correlation premium |
| **MTM Sensitivity** | P&L increases when correlation rises | P&L decreases when correlation rises |

**FTD investor under each convention:**
- Structural: investor SOLD credit protection on a basket → sold correlation premium → **SHORT** correlation
- MTM sensitivity: investor BENEFITS from high correlation (fewer independent defaults) → **LONG** correlation

The ecosystem uses both without declaring which is active. This is the root cause.

---

## FINDING CDA-01: FTD "short correlation" label contradicts own economic explanation (Desk Bible)

**Severity:** HIGH  
**Artifact:** Desk_Bible_v2.md (FROZEN)

**Location 1 — Line 17352:**
> "FTD investors are **short credit correlation**, just as worst-of equity investors are short equity correlation."

**Location 2 — Line 17524:**
> "FTD investors are **short correlation**. They profit when correlation is high (defaults are rare because companies move together) and lose when correlation is low."

**Problem:** The label "short correlation" is immediately followed by the description "they profit when correlation is high." Profiting from high correlation is the textbook definition of LONG correlation (MTM sensitivity). The label and the explanation within the same sentence teach opposite directions.

**Location 3 — Line 17951 (NTD chapter, coupon scaling table):**
> "FTD (N=1) | Short correlation (unambiguous)"

**Cross-artifact comparison:**
| Artifact | FTD Direction | Convention Used | Correct? |
|----------|:------------:|:---------------:|:--------:|
| Desk Bible (17352, 17524, 17951) | Short | Structural | Label defensible under structural; explanation contradicts label |
| Interview System V2.2 (line 400) | Long | MTM sensitivity | Correct ✓ |
| Interview System V2.2 (line 407) | Long | MTM sensitivity | Correct ✓ |
| Interview System V1 (line 238) | Long | MTM sensitivity | Correct ✓ |
| Interview System V1 (line 644) | Long | Full derivation | Correct ✓ |
| Product DNA Atlas (line 1269) | "Low correlation = higher risk" | Implicit MTM | Correct ✓ |
| Product DNA Atlas (line 2085) | "Low correlation = higher chance of first default" | Implicit MTM | Correct ✓ |
| Solutions Manual (line 1279) | "LOW correlation INCREASES risk" | Implicit MTM | Correct ✓ |

**Impact:** A reader of the Desk Bible who encounters "short correlation — they profit when correlation is high" will be confused. The Interview System gives the correct answer ("long correlation") for interview prep, but a candidate who studied the Desk Bible would answer "short" — which is wrong under the MTM convention universally used in interviews.

**Erratum recommendation:** ERRATA REQUIRED. The Desk Bible should either (a) relabel FTD as "long correlation" with a footnote explaining the structural convention, or (b) add a preamble defining both conventions and declaring which is in use.

---

## FINDING CDA-02: Worst-of investor "short correlation" label contradicts own explanation (Desk Bible)

**Severity:** HIGH  
**Artifact:** Desk_Bible_v2.md (FROZEN)

**Location — Line 17526:**
> "worst-of investors are also short correlation — they profit when stocks move together and lose when stocks move independently."

**Problem:** Identical to CDA-01. "Profiting when stocks move together" = benefiting from high correlation = LONG correlation (MTM). The label says SHORT, the explanation says LONG.

**Cross-reference:** Part 6 line 102 says the desk is "long correlation" on worst-of. The Solutions Manual (line 1477) says "WOAC suffers when correlations drop" — consistent with the investor being LONG correlation under MTM.

**Erratum recommendation:** ERRATA REQUIRED (same as CDA-01).

---

## FINDING CDA-03: Part 6 vs Encyclopedia — direct contradiction on desk worst-of direction

**Severity:** HIGH  
**Artifact 1:** production/part6_sections_10_11.md (FROZEN), line 102  
**Artifact 2:** production/infrastructure_encyclopedia_v1.md (FROZEN), line 4290

**Part 6 (line 102):**
> "The desk benefits when asset correlations increase. Worst-of products create **long correlation** exposure... This benefits the desk (which sold protection via the short put)."

**Encyclopedia (line 4290):**
> "Worst-of products are **SHORT correlation** (dealer profits if correlation falls)"

**Problem:** Two frozen canonical artifacts make directly opposing claims about the desk's correlation direction on worst-of products:
- Part 6: desk is LONG correlation (benefits when correlation rises)
- Encyclopedia: dealer is SHORT correlation (profits when correlation falls)

**Resolution analysis:** Both can be defensible under different readings:
- Part 6 may refer to the desk's HEDGED position (after buying correlation via dispersion)
- Encyclopedia may refer to the desk's RAW/UNHEDGED position (long the worst-of put = short correlation)

But neither artifact states its assumption, and a reader comparing them gets an irreconcilable contradiction.

**Additional error in Part 6 (line 102):** The parenthetical "(which sold protection via the short put)" is factually wrong. The INVESTOR sold the put (embedded in the note), not the desk. The desk is LONG the put. This misattributes position ownership.

**Erratum recommendation:** ERRATA REQUIRED. Both artifacts need to specify whether they describe the raw or hedged position. Part 6 line 102 must correct "sold protection via the short put" to "bought protection via the long put" or "holds the investor's short put exposure."

---

## FINDING CDA-04: Interview System V2.2 WOAC self-contradiction

**Severity:** MEDIUM  
**Artifact:** production/interview_system_v2_2.md (FROZEN)

**Location — Line 356:**
> "The investor is SHORT correlation: they benefit from high correlation (stocks move together, reducing worst-of risk) and lose from low correlation (independent moves increase the chance of one stock hitting the barrier)."

**Problem:** Same self-contradiction pattern as CDA-01 and CDA-02. Labels investor "SHORT correlation" then describes LONG correlation behavior ("benefit from high correlation"). A candidate reading this sentence learns a self-contradictory rule.

**Note:** The same artifact correctly labels FTD as "long correlation" at lines 400 and 407, creating an internal inconsistency: the WOAC investor and FTD investor have the SAME correlation sensitivity direction (both benefit from high correlation), yet the artifact labels WOAC "short" and FTD "long."

**Erratum recommendation:** ERRATA REQUIRED. Align WOAC direction with FTD direction, or define the convention difference explicitly.

---

## FINDING CDA-05: NTD "correlation reversal" table labels may invert direction for high-N products

**Severity:** MEDIUM  
**Artifact:** Desk_Bible_v2.md (FROZEN)

**Location — Lines 17951-17955 (coupon scaling table):**
> | FTD (N=1) | Short correlation (unambiguous) |
> | 2TD (N=2) | Short at low ρ, reversal at high ρ |
> | 4TD (N=4) | Long correlation (approximately) |
> | 5TD (N=5) | Long correlation (unambiguous) |

**Problem:** The table labels 5TD (last-to-default) as "long correlation (unambiguous)." Under MTM sensitivity:
- 5TD investor loses when ALL 5 companies default
- High correlation → if any company defaults, all default together → probability of all 5 defaulting INCREASES → higher risk for 5TD
- Therefore 5TD investor is hurt by high correlation → SHORT correlation (MTM)

The standard CDO analogy confirms: 5TD ≈ super-senior tranche = SHORT correlation. The label "long correlation" appears inverted.

However, under the structural convention used elsewhere in the Desk Bible: 5TD investor BOUGHT the correlation premium (paid a low coupon to take correlation risk) → arguably LONG structural correlation.

**Impact:** Moderate. The NTD chapter's own analysis table at lines 17927-17932 correctly shows that high-N products have increasing risk at high correlation, which is consistent with SHORT correlation (MTM). The summary table at 17951-17955 appears to contradict this.

**Erratum recommendation:** REVIEW ONLY. The labels are defensible under the structural convention but confusing when read alongside the risk analysis table. A clarifying footnote would resolve the ambiguity.

---

## FINDING CDA-06: Dispersion trade direction error (Desk Bible)

**Severity:** MEDIUM  
**Artifact:** Desk_Bible_v2.md (FROZEN)

**Location — Line 22605:**
> "Bank's hedge: **long single-stock vol + short basket vol = long correlation**"

**Problem:** Long single-stock vol + short basket vol is a dispersion trade. A dispersion trade profits when stocks move independently (low correlation) → it is SHORT correlation, not LONG.

The Desk Bible itself correctly describes the opposite trade at line 22483:
> "The trader hedges this by trading dispersion — buying single-stock volatility and selling basket volatility."

And at line 22390 (not in the WOAC chapter but referenced):
> "buying correlation (long basket vol, short single-stock vol)"

Line 22390 correctly states that LONG basket vol + SHORT single-stock vol = buying correlation (LONG correlation). Line 22605 describes the OPPOSITE trade legs (long single-stock + short basket) but assigns the SAME direction label ("long correlation"). One of these must be wrong — and line 22390 is correct, meaning line 22605 is wrong.

**Erratum recommendation:** ERRATA REQUIRED. Line 22605 should read "long single-stock vol + short basket vol = **short** correlation" or reverse the legs to match the label.

---

## FINDING CDA-07: Solutions Manual convention mixing (acceptable)

**Severity:** LOW  
**Artifact:** production/solutions_manual.md (FROZEN)

**Location — Lines 180, 1447, 1463, 1477:**
- Line 180: "client sells correlation risk on a basket" (structural = SHORT)
- Line 1447: "selling correlation risk" (structural = SHORT)
- Line 1477: "WOAC suffers when correlations drop" (MTM = LONG)
- Line 1870: "WOAC suffers most in dispersion events — when stocks decorrelate" (MTM = LONG)

**Problem:** The Solutions Manual uses the structural convention ("sells correlation") and the MTM description ("suffers when correlations drop") in separate sentences. The economic explanations are always correct. The reader could be confused by the implicit convention switch, but the descriptions are self-consistent within each sentence — unlike the Desk Bible where label and explanation contradict within the same sentence.

**Erratum recommendation:** ACCEPT AS-IS. The descriptions are individually correct and follow industry practice where both phrasings coexist. No self-contradiction within any single statement.

---

## FINDING CDA-08: Product DNA Atlas correlation descriptions (correct, no action)

**Severity:** LOW  
**Artifact:** production/product_dna_atlas.md (FROZEN)

The Atlas consistently uses correct economic descriptions without applying "long" or "short" labels:
- Line 1269 (FTD): "low correlation = higher risk" ✓
- Line 1298 (NTD): "high correlation INCREASES NTD risk (opposite of FTD)" ✓
- Line 1675 (WOAC): "Low correlation increases risk" ✓
- Line 1877 (CDO): "Low correlation = equity tranche risk high" ✓

**Erratum recommendation:** ACCEPT AS-IS. The Atlas avoids the label problem entirely by describing economics without directional labels.

---

## Summary Table

| Finding | Artifact | Severity | Recommendation |
|:-------:|----------|:--------:|:--------------:|
| CDA-01 | Desk Bible (FTD) | HIGH | ERRATA REQUIRED |
| CDA-02 | Desk Bible (worst-of) | HIGH | ERRATA REQUIRED |
| CDA-03 | Part 6 vs Encyclopedia | HIGH | ERRATA REQUIRED |
| CDA-04 | Interview System V2.2 (WOAC) | MEDIUM | ERRATA REQUIRED |
| CDA-05 | Desk Bible (NTD table) | MEDIUM | REVIEW ONLY |
| CDA-06 | Desk Bible (dispersion) | MEDIUM | ERRATA REQUIRED |
| CDA-07 | Solutions Manual | LOW | ACCEPT AS-IS |
| CDA-08 | Product DNA Atlas | LOW | ACCEPT AS-IS |

---

## Root Cause and V1.0.1 Recommendation

**Root cause:** The V1.0 ecosystem does not define a canonical correlation direction convention. Industry practice uses both "structural" and "MTM sensitivity" conventions interchangeably, and the Desk Bible adopted the structural convention for FTD/worst-of labels while providing MTM-convention economic explanations. The result is self-contradictory pedagogy.

**V1.0.1 recommendation:** Add a "Correlation Convention" section (either in the Desk Bible's Foundations chapter or as a standalone erratum appendix) that:
1. Defines both conventions explicitly
2. Declares which convention the ecosystem uses
3. Provides a mapping table (FTD: structural = short, MTM = long; etc.)
4. Corrects the self-contradictory sentences where label and explanation conflict

This is the single highest-priority erratum for V1.0.1.

---

*Generated: 2026-06-27 | Workstream WS2 | Semantic Consistency Audit Task 4*
