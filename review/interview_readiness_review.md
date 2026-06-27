# Interview Readiness Review — Product DNA Atlas

**Date:** 2026-06-22
**Artifact:** `production/product_dna_atlas.md`
**Scope:** Can a candidate use this Atlas alone to prepare for structured products interviews?

---

## Executive Summary

The Atlas covers **all 49 products** with sufficient depth for entry-level to mid-level interview preparation. A candidate drilling from this document can name every product, state its building blocks, and identify its primary risk. Three gaps reduce interview effectiveness: (1) generic watch metrics on 35% of cards, (2) two broken summaries, and (3) no explicit interview question framing.

---

## Interview Scenario Assessment

### Scenario 1: "Walk me through product X"

**Atlas readiness: STRONG**

The 16-field DNA card contains everything needed:
- Building blocks (Thing #1) → structural description
- Primary Risk → risk discussion
- Primary Hedge → risk management angle
- Complexity Rationale → why this product exists on the complexity spectrum

**Gap:** No "elevator pitch" framing. A candidate must synthesize the one-line summary + building blocks into a verbal walkthrough. Products with vague one-liners (VarSwap, VLSP) make this harder.

**Products at risk:**

| Section | Product | Issue |
|---------|---------|-------|
| 5.1.7 | Airbag | Truncated summary — candidate reads broken text |
| 5.1.8 | Bonus | Truncated summary — same issue |
| 5.2.4 | VarSwap | "Pure vol exposure" — insufficient for walkthrough |
| 5.2.8 | VLSP | "Tailored rate hedge" — too generic |

| Impact | Effort | Priority |
|:------:|:------:|:--------:|
| HIGH | LOW | HIGH |

---

### Scenario 2: "What are the risks of product X?"

**Atlas readiness: EXCELLENT**

Primary Risk field is the strongest field across all 49 cards. Every risk is:
- Product-specific (no generic "market risk")
- Multi-factor (lists 2-3 distinct risk dimensions)
- Concrete (describes what actually goes wrong)

Best examples for interview:
- CDO: "Portfolio credit losses reaching tranche attachment point. Equity tranche = first loss."
- VarSwap: "Variance is convex — large moves cause outsized P&L"
- ACCUM: "Leveraged loss in falling market (double accumulation below strike)"

No gaps for this scenario.

| Impact | Effort | Priority |
|:------:|:------:|:--------:|
| — | — | NONE |

---

### Scenario 3: "How would you hedge product X?"

**Atlas readiness: GOOD**

Primary Hedge field covers all 49 products. Accessible for most:
- IRS: "Offsetting IRS, futures strip, swaption for optionality"
- CDS: "Offsetting CDS, basis trade (CDS vs bond spread), index hedge"
- FWD: "Offsetting forward, or underlying + funding position"

**Gap:** ~8 products use expert-only hedge language without context:

| Section | Product | Hedge Description | Barrier for Candidate |
|---------|---------|-------------------|-----------------------|
| 5.2.4 | VarSwap | "Replicating portfolio of OTM options" | What is OTM replication? |
| 5.4.2 | RA STEG | "CMS spread swap + digital option strip" | What do these do? |
| 5.4.4 | TARN STEG | "CMS spread options, target coupon modeling" | "Target coupon modeling" is opaque |
| 5.5.5 | CDO | "Correlation trading (base correlation)" | "Base correlation" is PhD-level |

A candidate who memorizes these verbatim without understanding will fail follow-up questions. Adding brief mechanism labels would close this gap.

| Impact | Effort | Priority |
|:------:|:------:|:--------:|
| MEDIUM | MEDIUM | MEDIUM |

---

### Scenario 4: "What's the most important Greek for product X?"

**Atlas readiness: WEAK**

This is the Atlas's biggest interview gap. "Watch: Delta" appears on 17/49 products. An interviewer asking this question for Phoenix, RC, Accumulator, and Forward will receive the same one-word answer four times. Correct answers:

| Product | Current | Better Answer |
|---------|---------|---------------|
| PPN | Delta | **Rho** — interest rates drive the zero-coupon bond's value |
| RC | Delta | **Put delta near strike** — conversion risk is the defining feature |
| Phoenix | Delta | **Autocall probability** — the early termination mechanic defines P&L |
| ACCUM | Delta | **Gearing ratio** — 2x accumulation below strike is the risk |
| DCI | Delta | **FX strike distance** — the conversion trigger |
| FWD | Delta | **Forward points / cost of carry** — what makes forwards unique vs spot |

The 14 products with product-specific watch metrics (DV01, CMS spread delta, Base correlation, Recovery delta, etc.) are interview-ready.

| Impact | Effort | Priority |
|:------:|:------:|:--------:|
| HIGH | MEDIUM | HIGH |

---

### Scenario 5: "Compare product X and product Y"

**Atlas readiness: GOOD**

Family View, Complexity View, and Appendix C (Evolution Chains) provide the structural basis for comparison. A candidate can compare:
- Within-family: PPN vs RC (capital protected vs yield enhanced) via building blocks
- Cross-family: CLN vs CDO (single-name vs portfolio credit) via complexity rationale
- By complexity tier: products at same score in different families

**Gap:** No explicit comparison pairs or "how to distinguish" guidance. The candidate must derive comparisons from individual cards. The Comparison Matrix (not yet generated) will address this fully.

| Impact | Effort | Priority |
|:------:|:------:|:--------:|
| MEDIUM | — | DEFERRED (Matrix) |

---

### Scenario 6: "Why would a client buy product X?"

**Atlas readiness: MIXED**

The one-line summary + Primary Buyer field together answer this — when both are strong. Good examples:

| Product | Buyer + Summary = Clear Client Story |
|---------|--------------------------------------|
| IRS | Corporates + "Transform fixed-rate exposure to floating or vice versa" |
| FWD | Corporates (hedging) + "Lock in future purchase/sale price" |
| SD | Retail + "Replace savings allocation with market-linked upside" |

Weak examples where client motivation is unclear:

| Product | Buyer | Summary | Issue |
|---------|-------|---------|-------|
| VarSwap | Hedge funds, vol traders | "Pure vol exposure" | Why SPECIFICALLY? |
| VLSP | Banks, corporates | "Tailored rate hedge" | Every rate product is a hedge |
| WOAC | Yield-seeking PB/retail | "Enhanced yield from correlation premium" | Client doesn't think in "correlation premium" |
| SNOW | Yield-seeking PB clients | "Enhanced yield with cumulative coupon mechanism" | "Mechanism" is internal language |

| Impact | Effort | Priority |
|:------:|:------:|:--------:|
| HIGH | LOW | HIGH |

---

## Specific Checks

### Check A: Truncated Summaries That Would Embarrass a Candidate

| Section | Product | Summary | Status |
|---------|---------|---------|:------:|
| 5.1.7 | Airbag | "Leveraged upside (e" | **FAIL** |
| 5.1.8 | Bonus | "Guaranteed minimum bonus return (e" | **FAIL** |
| All others | — | Complete sentences | **PASS** |

Root cause: Generation script's `.split('.')[0]` truncates at periods inside "(e.g., ...)".

### Check B: Products With Insufficient Interview Material

No product is entirely unusable. All 49 have building blocks, risk, and hedge. But 7 products have 2+ weak fields that collectively make interview prep harder:

| Section | Product | Weak Fields |
|---------|---------|-------------|
| 5.1.7 | Airbag | Summary (truncated), Watch (generic Delta) |
| 5.1.8 | Bonus | Summary (truncated), Watch (generic Delta) |
| 5.2.4 | VarSwap | Summary (too terse), Hedge (expert-only) |
| 5.2.8 | VLSP | Summary (too generic), Watch (DV01 + Vega — acceptable but dense) |
| 5.6.10 | SNOW | Summary (uses "mechanism"), Watch (generic Delta) |
| 5.6.12 | WOAC | Summary (assumes jargon), Watch (Correlation — correct but unexplained) |
| 5.5.5 | CDO | Summary (5 words for most complex product), Hedge (expert-only) |

### Check C: Watch Metrics Requiring Beginner Explanation

| Metric | Products | Explanation Needed |
|--------|----------|-------------------|
| Digital gamma | 5.1.10, 5.1.11, 5.1.12, 5.3.2 | "Coupon flips from full to zero near strike — gamma explodes at the digital boundary" |
| CMS spread delta | 5.4.1, 5.4.2, 5.4.3, 5.4.4 | "Sensitivity to the slope of the swap curve (difference between long and short rates)" |
| Base correlation | 5.5.5 | "Implied correlation across the credit portfolio — drives tranche pricing" |
| Recovery delta | 5.5.2 | "Sensitivity to assumed recovery rate in credit default event" |
| Dollar Value of One Basis Point | 5.2.6 | Standard DV01 — name is correct but verbose; DV01 is industry standard |

### Check D: Products Where Cheat Sheet Item 3 (Watch) Is Materially Weaker Than Items 1-2

All 17 "Watch: Delta" products. Items 1 (building blocks) and 2 (key risk) are specific and differentiated. Item 3 reverts to generic. This pattern is consistent enough to be a systematic issue rather than product-specific.

---

## Interview Readiness Scores by Family

| Family | Products | Ready | Needs Work | Score |
|--------|:--------:|:-----:|:----------:|:-----:|
| ELN | 15 | 11 | 4 (Airbag, Bonus, Phoenix summary OK but Delta watch, CRA ELN watch OK) | 73% |
| Swaps | 8 | 5 | 3 (VarSwap, EqSwap watch, VLSP) | 63% |
| SRT | 5 | 4 | 1 (Digital CF generic-ish) | 80% |
| STEG | 4 | 4 | 0 (CMS spread delta is correct, just needs gloss) | 100% |
| CLN | 5 | 5 | 0 | 100% |
| Other | 12 | 7 | 5 (ACCUM/DECUM/DCI/SHRK/SNOW watch generic) | 58% |

**Overall: 36/49 cards are interview-ready (73%).** 13 cards need watch metric or summary improvements.

---

## Recommendations Summary

| # | Issue | Impact | Effort | Priority |
|---|-------|:------:|:------:|:--------:|
| 1 | Fix 2 truncated summaries | HIGH | LOW | **HIGH** |
| 2 | Rewrite 5 vague summaries | HIGH | LOW | **HIGH** |
| 3 | Replace 17 generic "Watch: Delta" | HIGH | MEDIUM | **HIGH** |
| 4 | Add parenthetical to 5 expert-only watch metrics | MEDIUM | LOW | **MEDIUM** |
| 5 | Add mechanism labels to 8 expert-only hedges | MEDIUM | MEDIUM | **MEDIUM** |
| 6 | Add "interview framing" note per family in Family View | MEDIUM | LOW | **MEDIUM** |

---

## Verdict

**Interview readiness: 73% (36/49 cards fully usable).** The 27% gap is concentrated in generic watch metrics and vague summaries — fixable with targeted edits. The structural foundation (building blocks, risks, hedges) is solid across all 49 cards. No card is unfixable. Total estimated fix effort: ~2 hours of Atlas regeneration with improved summary extraction + curated watch metric mapping.

---

*Interview readiness review complete.*
