# INTERVIEW INTUITION AUDIT — V1.0 Review

**Workstream:** WS8 — Interview-Intuition Audit  
**Scope:** Interview System V2.2 semantic clarity and correctness for interview prep  
**Date:** 2026-06-27  
**Status:** COMPLETE  

---

## Executive Summary

The Interview System V2.2 is the ecosystem's primary interview-preparation artifact. It contains 13 product treatments across 4 tiers (Elevator, Technical, Desk, Senior) plus 25 confusion pairs and 10 infrastructure confusion pairs.

**Overall assessment:** The Interview System V2.2 is semantically sound and interview-ready with one significant exception: the WOAC correlation direction self-contradiction (CDA-04). All other product treatments correctly teach the intended intuition.

---

## FINDING IIA-01: WOAC "short correlation" self-contradiction

**Severity:** HIGH  
**Artifact:** production/interview_system_v2_2.md (FROZEN), line 356

**Fully documented in:** `correlation_direction_audit.md` (Finding CDA-04)

**Interview impact:** A candidate who memorizes "WOAC investor is SHORT correlation" from line 356 will give the wrong answer if asked "Does the WOAC investor benefit from high or low correlation?" The same sentence says "they benefit from high correlation" — which is the LONG correlation answer. The candidate faces a contradictory source.

**Compounding risk:** Lines 400 and 407 correctly state FTD is LONG correlation. Since the WOAC investor and FTD investor have the same directional sensitivity (both benefit from high correlation), a well-prepared candidate who noticed both would be confused by the inconsistency.

**Erratum recommendation:** ERRATA REQUIRED (covered in WS2).

---

## FINDING IIA-02: Confusion Pair 16 — FTD vs NTD description avoids labeling

**Severity:** LOW  
**Artifact:** production/interview_system_v2_2.md (FROZEN), line 986

**Quoted text:**
> "FTD vs NTD | Correlation reversal. Low corr increases FTD risk; high corr increases NTD risk."

**Assessment:** This description correctly states the ECONOMIC EFFECT without using "long" or "short" labels. This is actually the safest approach given the convention confusion elsewhere.

However, in an interview setting, a candidate may be asked "Is FTD long or short correlation?" This confusion pair does not prepare the candidate to answer that question — it only teaches the underlying economics.

**Erratum recommendation:** ACCEPT AS-IS. The economic description is correct and avoids the labeling trap. The Tier 2 treatment at line 400 provides the explicit "FTD is LONG correlation" answer.

---

## FINDING IIA-03: WOAC Tier 2 — "independent stocks" ambiguity

**Severity:** LOW  
**Artifact:** production/interview_system_v2_2.md (FROZEN), line 354

**Quoted text:**
> "In a WOAC with N independent stocks, barrier breach probability ≈ 1 − (1−P)^N"

**Problem:** The formula assumes stocks are INDEPENDENT (zero correlation). In reality, WOAC stocks are never independent — they have positive correlation. The formula is pedagogically useful as a simplification but the word "independent" is doing double duty:
1. Mathematical sense: independent random variables (correlation = 0)
2. Practical sense: stocks that can move independently of each other

The Tier 2 text immediately follows with the correlation explanation (line 354-356), which addresses this. But the formula itself implicitly assumes zero correlation, which the next sentence says is the WORST case.

**Erratum recommendation:** ACCEPT AS-IS. The simplification is pedagogically standard and immediately corrected by the correlation discussion.

---

## FINDING IIA-04: Infrastructure cross-references — verified consistent

**Severity:** NONE (verification pass)

Each product's "Infrastructure cross-references" section (§6.x references) was checked against the Part 6 content. All references point to valid subsections and the content described matches.

Spot-checked products: RC, Phoenix, WOAC, FTD, Accumulator, CRA SRT.

---

## FINDING IIA-05: Tier progression — verified pedagogically sound

**Severity:** NONE (verification pass)

The 4-tier structure (Elevator → Technical → Desk → Senior) was verified for all 13 products in the Top 13 + Next 16 treatment:

| Criterion | Result |
|-----------|:------:|
| Tier 1 avoids jargon not yet defined | ✓ |
| Tier 2 introduces quantitative concepts | ✓ |
| Tier 3 adds desk/operations reality | ✓ |
| Tier 4 adds regulatory/suitability/edge cases | ✓ |
| No tier references concepts from a higher tier | ✓ |

---

## Summary Table

| Finding | Description | Severity | Recommendation |
|:-------:|------------|:--------:|:--------------:|
| IIA-01 | WOAC correlation self-contradiction | HIGH | ERRATA REQUIRED |
| IIA-02 | FTD/NTD confusion pair avoids label | LOW | ACCEPT AS-IS |
| IIA-03 | "Independent stocks" simplification | LOW | ACCEPT AS-IS |
| IIA-04 | Infrastructure cross-refs consistent | NONE | VERIFIED ✓ |
| IIA-05 | Tier progression sound | NONE | VERIFIED ✓ |

---

*Generated: 2026-06-27 | Workstream WS8 | Semantic Consistency Audit Task 4*
