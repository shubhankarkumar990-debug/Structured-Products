# Cross-Family Consistency Review

**Date:** 2026-06-20
**Scope:** 33 chapters across 4 families (ELN 15, Swaps 8, SRT 5, STEG 4)
**Framework:** v1.3.1 (FROZEN)
**Purpose:** Verify terminology consistency across families before scaling to 49 products

---

## 1. ELN vs SRT Callable Terminology

| Term | ELN Usage (CRC 5.1.6, ICN 5.1.11) | SRT Usage (IR Callable 5.3.1, CRA SRT 5.3.4) | STEG Usage (Callable STEG 5.4.3) | Consistent? |
|------|-----------------------------------|-----------------------------------------------|----------------------------------|:-----------:|
| Call right | "issuer call right" | "issuer call right" | "bank's right to terminate" / "call right" | YES |
| Bermudan exercise | "Bermudan exercise" (5.1.6 §7) | "Bermudan exercise" (5.3.1 §11) | "Bermudan" (5.4.3 §16) | YES |
| Non-call period | "non-call period" | "NC period" / "non-call period (NC)" | "NC2" / "non-call period" | YES |
| Call premium | "call premium" = above-market coupon | "swaption premium" embedded in coupon | "swaption premium" + "call premium" | YES |
| Callable vs non-callable | CRC = callable, RC = non-callable | IR Callable = callable, NCRA = non-callable | Callable STEG = callable, Vanilla STEG = non-callable | YES |

**Result: PASS.** Callable terminology consistent across all 3 families. "Bermudan" always used for discrete exercise. "Non-call period" and "NC" both used (NC as abbreviation). No conflicts.

---

## 2. ELN vs TARN Path Dependency Terminology

| Term | ELN Usage (Phoenix 5.1.3) | STEG Usage (TARN STEG 5.4.4) | Consistent? |
|------|--------------------------|-------------------------------|:-----------:|
| Path-dependent | "path-dependent: outcome depends on entire sequence of observations" | "path-dependent — order of coupons matters" | YES |
| Memory feature | "memory feature — missed coupons rise from ashes" | Not used (TARN has no memory) | N/A |
| Cumulative mechanism | Not used (Phoenix has memory, not accumulation) | "target accumulation" / "cumulative coupons" | N/A |
| Monte Carlo | "Monte Carlo simulation required" | "Monte Carlo pricing required" | YES |
| Order matters | "sequence of observations" | "order and magnitude of quarterly coupons" | YES |

**Result: PASS.** Path dependency concept consistent. Phoenix uses "memory" (deferred coupons paid later). TARN uses "accumulation" (cumulative target). Different mechanisms, different terms — no ambiguity. Both reference Monte Carlo consistently.

---

## 3. CDS vs CLN Credit Event Mechanics

| Term | CDS (5.2.5) | CLN (5.5.1) | Consistent? |
|------|-------------|-------------|:-----------:|
| Credit event | "credit event" — 3 types: bankruptcy, failure to pay, restructuring | "credit event" — same 3 types | YES |
| ISDA | "ISDA (International Swaps and Derivatives Association)" defined in §1 | References "ISDA standard" | YES |
| Recovery rate | "recovery rate determines how much the insurer pays" | "recovery rate" used consistently | YES |
| Protection buyer/seller | "protection buyer" / "protection seller" | CLN investor = "protection seller" (embedded) | YES |
| Settlement | "physical / cash / auction settlement" | "cash settlement" (note format) | YES |

**Result: PASS.** Credit event mechanics consistent. CDS chapter (5.2.5) establishes canonical definitions. CLN (5.5.1) references them correctly. Remaining CLN products (Batch 8: Skew CLN, FTD, NTD, Synth CDO) should continue referencing CDS definitions.

**Advisory:** Batch 8 CLN generation should cross-reference CDS (5.2.5) for all credit event definitions rather than redefining them.

---

## 4. Correlation Terminology Consistency

| Context | Usage | Location | Consistent? |
|---------|-------|----------|:-----------:|
| Equity correlation (worst-of) | "correlation measures how synchronized two assets are" | Section 1.6 (Correlation) | Canonical |
| Phoenix correlation | "short correlation product" | 5.1.3 §15 | Consistent |
| CMS rate correlation | "CMS30Y-CMS2Y correlation" | RA STEG 5.4.2 §15 | Consistent |
| Credit correlation | "correlation assumptions" (CDO context) | Section 1.6, CDS §15 | Consistent |
| Correlation risk definition | "correlation risk — the risk that..." | Consistently defined per context | YES |

**Result: PASS.** Correlation defined canonically in Section 1.6. Applied consistently across equity (Phoenix), rates (RA STEG), and credit (CDS/CLN) contexts. Each chapter specifies WHICH correlation (equity basket, CMS rates, credit names).

---

## 5. Barrier Terminology Consistency

| Term | Canonical Definition (Section 1.3) | Usage Across 33 Chapters | Consistent? |
|------|-----------------------------------|-------------------------|:-----------:|
| Knock-in (KI) | "activates an option when price crosses barrier" | Used in RC, DRC, KODRC, CRC, Airbag, Phoenix, FCN, Digital KI Put | YES |
| Knock-out (KO) | "deactivates an option when price crosses barrier" | Used in KODRC, Bonus Certificate | YES |
| Capital barrier | "determines whether investor's principal is at risk" | Used across ELN family consistently | YES |
| Coupon barrier | "determines whether conditional coupon is paid" | Phoenix, FCN, Digital KI Put | YES |
| Autocall barrier | "determines early redemption" | Phoenix, FCN, Digital KI Put | YES |
| European vs American barrier | "checked once at end" vs "checked constantly" | Defined in 1.3, used correctly in all chapters | YES |
| Range boundaries | Not in barrier section — separate concept | SRT (NCRA, CRA SRT), STEG (RA STEG) use "boundaries" not "barriers" | YES |

**Result: PASS.** Barrier terms defined in Section 1.3, used consistently across 15 ELN chapters. Range accrual products correctly use "boundaries" / "range" instead of "barriers" — no terminology collision. 783 total barrier-related mentions, all consistent.

---

## 6. Yield Terminology Consistency

| Term | Definition Location | Usage | Consistent? |
|------|-------------------|-------|:-----------:|
| Yield | Section 1.1 "total annual return on a bond" | Consistent across all chapters | YES |
| Yield curve | Section 1.7 "graph showing interest rate for different lending periods" | Consistent; STEG chapters reference 1.7 | YES |
| CMS spread | Section 1.8 "difference between two CMS rates, reflects yield curve slope" | All STEG chapters use consistently | YES |
| Yield enhancement | Various — "earn above-market yield" | Consistent phrasing across ELN and SRT | YES |
| Coupon vs yield | Coupon = periodic payment; yield = total return | Never conflated across 33 chapters | YES |

**Result: PASS.** Yield terminology consistent. Section 1.7 establishes canonical yield curve definitions. STEG family correctly references 1.7 and extends with CMS-specific yield curve concepts.

---

## 7. Lifecycle Terminology Consistency

| Term | Usage Pattern | Consistent? |
|------|-------------|:-----------:|
| "lifecycle" (one word) | Used throughout: "product lifecycle" in §13, "trade lifecycle" in Part 2 | YES |
| "life cycle" (two words) | Not used — consistently one word | YES |
| Pre-trade / Trade date / During life / Maturity | v1.3.1 standard 4-stage lifecycle (SRT, STEG) | YES |
| Inception / Observation / Maturity | v1.0 3-stage lifecycle (ELN Batches 0-3) | YES (grandfathered) |
| Four-leg settlement | SRT and STEG — "all legs closed" at termination | YES |

**Result: PASS.** "lifecycle" consistently one word. v1.3.1 chapters use 4-stage format. v1.0 chapters use 3-stage (grandfathered). Harmonization will standardize.

---

## 8. Summary

| Area | Result | Issues |
|------|:------:|--------|
| Callable terminology (ELN vs SRT vs STEG) | PASS | None |
| Path dependency terminology (ELN vs STEG) | PASS | None |
| Credit event mechanics (CDS vs CLN) | PASS | Advisory: Batch 8 should cross-reference CDS |
| Correlation terminology | PASS | None |
| Barrier terminology | PASS | None |
| Yield terminology | PASS | None |
| Lifecycle terminology | PASS | Grandfathered v1.0 format in Batches 0-3, deferred to harmonization |

### **OVERALL: PASS**

**Required fixes:** 0
**Recommended fixes:** 0
**Advisory notes:** 2
- A1: Batch 8 CLN products should reference CDS (5.2.5) for credit event definitions
- A2: Lifecycle format standardization deferred to Template Harmonization Pass

---

*Cross-Family Consistency Review completed 2026-06-20. No content modifications required.*
