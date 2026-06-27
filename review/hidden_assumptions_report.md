# HIDDEN ASSUMPTIONS REPORT — V1.0 Review

**Workstream:** WS7 — Hidden Assumptions Audit  
**Scope:** Unstated assumptions that affect correctness or interpretability  
**Date:** 2026-06-27  
**Status:** COMPLETE  

---

## Executive Summary

The V1.0 ecosystem contains 6 hidden assumptions — unstated premises that a reader must independently know (or guess) to correctly interpret the material. The most critical is the undefined correlation direction convention (WS2). The remaining findings are lower severity but affect pedagogical clarity.

---

## FINDING HA-01: Correlation direction convention is never defined

**Severity:** HIGH  
**Details:** Fully documented in `correlation_direction_audit.md` (CDA root cause section)

The ecosystem uses two distinct conventions for "long/short correlation" (structural vs MTM sensitivity) without ever defining either or declaring which is canonical. This is the root hidden assumption — it causes the self-contradictory labels identified in WS2.

**Erratum recommendation:** ERRATA REQUIRED (covered in WS2).

---

## FINDING HA-02: Recovery rate of 40% assumed without justification in credit chapters

**Severity:** MEDIUM  
**Artifact:** Desk_Bible_v2.md (FROZEN)

**Locations:**
- Line 16811 (CLN worked example): Recovery = 40%
- Line 17503 (FTD worked example): Recovery = 40%
- Line 17886 (NTD worked example): Recovery = 40%

**Problem:** All three credit worked examples assume a 40% recovery rate. This is the standard ISDA assumption for senior unsecured corporate debt, but:
1. The 40% figure is never justified or sourced
2. The examples do not state that this is a market convention, not a physical reality
3. The Interview System V2.2 (line 412) correctly notes that Lehman recovery was 8.6%, creating a ~31.4% gap from the assumed 40%

A reader who internalizes "recovery = 40%" without understanding it is a convention will be unprepared for real-world scenarios.

**Mitigating factor:** The Solutions Manual (line 1348) warns about recovery rate assumptions. The Desk Bible's FTD chapter does mention that actual recovery can deviate significantly.

**Erratum recommendation:** REVIEW ONLY. A one-line note in each credit worked example ("40% is the standard ISDA convention for senior unsecured; actual recovery rates vary from <10% to >90%") would close the gap.

---

## FINDING HA-03: "Desk position" ambiguity — raw vs hedged never declared

**Severity:** MEDIUM  
**Artifact:** Multiple (Desk Bible, Part 6, Encyclopedia)

**Problem:** When the ecosystem describes the "desk's position" or "desk Greeks," it is unstated whether this refers to:
1. The desk's **raw** position (the embedded options in the products sold)
2. The desk's **hedged/net** position (after delta, gamma, vega, and correlation hedging)

Examples:
- Part 6 line 110: "ELN... long correlation (worst-of)" — this appears to describe the hedged position
- Encyclopedia line 4290: "dealer profits if correlation falls" — this appears to describe the raw position
- Desk Bible line 22483: "bank is structurally long correlation" — appears hedged
- Desk Bible line 25388: "A desk can be delta-neutral and still have massive short gamma" — acknowledges the raw vs hedged distinction for gamma but not for correlation

**Impact:** A reader cannot resolve the Part 6 vs Encyclopedia contradiction without knowing which assumption each artifact makes.

**Erratum recommendation:** REVIEW ONLY. A "Desk Position Conventions" subsection in Part 6 defining "raw position = before hedging; net position = after hedging" would eliminate the ambiguity.

---

## FINDING HA-04: Continuous vs European barrier observation — assumption affects WOAC outcome

**Severity:** MEDIUM  
**Artifact:** Desk_Bible_v2.md (FROZEN), line 22544

**Quoted text:**
> "Knock-in barrier: 60% (continuous)"

**Problem:** The WOAC terms specify "continuous" barrier observation, which means the barrier is monitored at every moment during the product's life. This is correctly stated. However, the worked example's "What if" scenario at line 22563 implicitly assumes that after the barrier is breached, the maturity outcome depends on comparing the final level to a strike.

What is NOT stated:
1. Whether "continuous" means actual intraday monitoring or closing-price-only (industry practice varies)
2. Whether the barrier, once breached, is permanently activated (standard for KI) or can be "cured" by recovery
3. What happens if the barrier is breached intraday but the closing price is above the barrier

These assumptions matter for real-world payoff determination but are left to the reader's industry knowledge.

**Erratum recommendation:** ACCEPT AS-IS. These are standard industry conventions that a practitioner would know. Explaining them in every worked example would be excessive for the target audience. The Infrastructure Encyclopedia (§6.1) covers observation conventions.

---

## FINDING HA-05: Act/360 day count applied without explaining alternatives

**Severity:** LOW  
**Artifact:** Desk_Bible_v2.md (FROZEN), line 13951

**Context:** CRA SRT worked example specifies "Act/360" day count.

**Problem:** The example uses Act/360 without explaining that this is one of several possible day count conventions (Act/365, 30/360, Act/Act). The choice of day count affects coupon amounts. A reader unfamiliar with day count conventions would not understand why "90 days" in Q1 produces a different per-day rate than "92 days" in Q3.

**Mitigating factor:** Day count conventions are covered in the Desk Bible's Foundations section (Part 0). The worked example is in Section 5.3, which can reasonably assume the reader has read Part 0.

**Erratum recommendation:** ACCEPT AS-IS. Sequential reading order provides the prerequisite knowledge.

---

## FINDING HA-06: "Quarterly" payment frequency — actual day counts vary

**Severity:** LOW  
**Artifact:** Multiple worked examples

**Problem:** Several worked examples use "quarterly" payment frequency but show different total days per quarter (90, 91, 92). The assumption that quarters have different numbers of days is correct (calendar reality) but never explicitly stated. A reader who assumes all quarters have 90 days will get different coupon amounts.

**Mitigating factor:** All worked examples that show quarterly coupons include the actual day count in the table, making the assumption transparent by example even if not stated explicitly.

**Erratum recommendation:** ACCEPT AS-IS.

---

## Summary Table

| Finding | Description | Severity | Recommendation |
|:-------:|------------|:--------:|:--------------:|
| HA-01 | Correlation convention undefined | HIGH | ERRATA REQUIRED |
| HA-02 | Recovery rate 40% ungrounded | MEDIUM | REVIEW ONLY |
| HA-03 | Raw vs hedged position unstated | MEDIUM | REVIEW ONLY |
| HA-04 | Continuous barrier observation details | MEDIUM | ACCEPT AS-IS |
| HA-05 | Act/360 unexplained in context | LOW | ACCEPT AS-IS |
| HA-06 | Quarterly day count variation | LOW | ACCEPT AS-IS |

---

*Generated: 2026-06-27 | Workstream WS7 | Semantic Consistency Audit Task 4*
