# Batch 4 Book Review

**Date:** 2026-06-20
**Reviewer:** 11-Agent Review Pipeline (Framework v1.1)
**Scope:** 4 chapters — TRS (5.2.2), Equity Swap (5.2.3), Variance Swap (5.2.4), CDS (5.2.5)
**Framework:** Production Framework v1.1 (first batch under v1.1 requirements)

---

## 1. Executive Summary

**Verdict: PASS — Framework v1.1 Compliant**

Batch 4 delivers the Swaps Core family (4 products following the IRS pilot). All 4 chapters meet v1.1 requirements: 16 mandatory sections, bridge text, Professor Note, Desk Perspective (5-row standalone), Knowledge Check (5+3+1), Visual Specifications (5 per chapter, replacing Visual Learning Recommendations), Dependency References, and the new "Why This Product Exists" section (7/7 subsections in all 4 chapters).

All arithmetic verified programmatically. Zero errors found across 4 chapters (16 scenarios + 4 worked examples).

The Swaps dependency-chain review confirms Parts 1.7, 1.8, 1.9, and IRS (5.2.1) provide sufficient prerequisites. One minor gap identified and addressed: variance as a tradeable quantity (Variance Swap bridges from volatility foundation in Part 1.5).

**0 mandatory fixes. 3 recommended improvements. 0 cosmetic issues.**

---

## 2. Chapter-Level Agent Results

### Agent 1: Educational Clarity (Professor Agent)

| Chapter | Score | Notes |
|---------|:-----:|-------|
| TRS (5.2.2) | 8.7 | Strong bridge from IRS. "Synthetic ownership" concept well-developed. Car rental analogy is intuitive. §1 Dmitri scenario clearly motivates the product |
| Equity Swap (5.2.3) | 8.5 | Clean distinction from TRS — equity-specific considerations (dividend treatment, corporate actions) well-explained. Corporate treasurer scenario is practical |
| Variance Swap (5.2.4) | 8.8 | Excellent treatment of an abstract concept. Weather insurance analogy makes variance intuitive. Convexity explained through the "vol² = variance" relationship. Strongest educational chapter in the batch |
| CDS (5.2.5) | 8.6 | Home warranty analogy captures credit protection clearly. ISDA credit event mechanics well-structured. Clean bridge from Part 1.9 foundations |

**Batch average: 8.65** (target ≥ 8.5 ✓)

### Agent 2: Visual Completeness (Visual Design Agent)

| Chapter | Score | Notes |
|---------|:-----:|-------|
| TRS (5.2.2) | 8.0 | 5 visual specs. Two-party flow diagram and linear payoff chart effectively communicate the product. Lifecycle diagram adds operational depth |
| Equity Swap (5.2.3) | 7.5 | 5 visual specs. Product is structurally similar to TRS, limiting visual differentiation. Comparison chart (equity swap vs direct ownership) is the strongest visual |
| Variance Swap (5.2.4) | 8.5 | 5 visual specs. Two payoff diagrams (variance space + volatility space) effectively show convexity. Strongest visual portfolio in the batch |
| CDS (5.2.5) | 8.0 | 5 visual specs. Decision tree for credit event determination is novel. Waterfall diagram for settlement calculation adds clarity |

**Batch average: 8.0** (target ≥ 8.0 ✓)

### Agent 3: Terminology Compliance (Jargon Police Agent)

| Chapter | Score | Notes |
|---------|:-----:|-------|
| TRS (5.2.2) | 100% | "Total return," "financing rate," "notional," "reference asset" all defined or referenced correctly |
| Equity Swap (5.2.3) | 100% | "Gross vs net dividend," "quanto" defined with parenthetical. "ISDA Equity Definitions" referenced appropriately |
| Variance Swap (5.2.4) | 100% | "Realized variance," "variance strike," "vega notional," "variance notional," "convexity" all defined. Bridge from Part 1.5 volatility concepts is explicit |
| CDS (5.2.5) | 100% | "Credit event," "protection buyer/seller," "recovery rate," "ISDA Determinations Committee," "wrong-way risk" all defined or referenced |

**Batch compliance: 100%** (target ≥ 98% ✓)

### Agent 4: Beginner Accessibility (Cognitive Load Agent)

| Chapter | Score | Notes |
|---------|:-----:|-------|
| TRS (5.2.2) | 8.5 | Car rental analogy is universally accessible. Linear payoff simplifies understanding |
| Equity Swap (5.2.3) | 8.5 | Film royalty deal analogy is clear. Builds naturally on TRS concepts |
| Variance Swap (5.2.4) | 8.5 | Weather insurance analogy effectively demystifies variance. The concept that "direction doesn't matter, only magnitude" is clearly stated |
| CDS (5.2.5) | 8.5 | Home warranty analogy maps precisely to CDS mechanics. Three credit events clearly enumerated |

**Batch average: 8.5**

### Agent 5: Section Consistency (Final Editor Agent)

| Chapter | 16 Sections | Bridge | Prof Note | Desk Persp | Knowledge Check | Visual Specs | Dep Refs | Why Exists |
|---------|:-----------:|:------:|:---------:|:----------:|:---------------:|:-----------:|:--------:|:----------:|
| TRS | ✓ | ✓ | ✓ | ✓ (5 rows) | ✓ (5+3+1) | ✓ (5 specs) | ✓ (6 refs) | ✓ (7/7) |
| Equity Swap | ✓ | ✓ | ✓ | ✓ (5 rows) | ✓ (5+3+1) | ✓ (5 specs) | ✓ (6 refs) | ✓ (7/7) |
| Variance Swap | ✓ | ✓ | ✓ | ✓ (5 rows) | ✓ (5+3+1) | ✓ (5 specs) | ✓ (6 refs) | ✓ (7/7) |
| CDS | ✓ | ✓ | ✓ | ✓ (5 rows) | ✓ (5+3+1) | ✓ (5 specs) | ✓ (6 refs) | ✓ (7/7) |

**v1.1 compliance: All 4 chapters include "Why This Product Exists" (7/7 subsections) and Visual Specifications (5 each, all with Visual ID, Type, Priority, Purpose, Caption, Location, Reuse Potential). First batch fully compliant with v1.1.**

### Agent 6: Arithmetic Verification (Product Accuracy Agent)

| Chapter | Scenarios | Worked Example | Result |
|---------|:---------:|:--------------:|:------:|
| TRS | 4 scenarios verified | S&P 500 quarterly table + annual total verified | ✓ All correct |
| Equity Swap | 4 scenarios verified | Nestlé quarterly table + annual total verified | ✓ All correct |
| Variance Swap | 4 scenarios verified | EURO STOXX 50 variance calculation + vega approximation verified | ✓ All correct |
| CDS | 4 scenarios verified | Petrobras 5-year premium table + default payoff verified | ✓ All correct |

**Verification method:** Programmatic (Python3). All return calculations, financing costs, variance payoffs, and CDS settlements verified. Zero errors.

### Agent 7: Dependency Chain (Cross-Reference Agent)

| Chapter | Bridge Source | Dependencies Valid | Notes |
|---------|-------------|:-----------------:|-------|
| TRS | IRS (5.2.1) | ✓ 6/6 valid | Correctly extends IRS swap structure to total return concept |
| Equity Swap | TRS (5.2.2) | ✓ 6/6 valid | Correctly positions as TRS specialization for equity |
| Variance Swap | IRS (5.2.1), Volatility (1.5) | ✓ 6/6 valid | Bridges from volatility (1.5) to variance as tradeable — minor gap addressed |
| CDS | CLN (5.5.1), Credit Risk (1.9) | ✓ 6/6 valid | Builds on CDS basics from 1.9, extends to full product mechanics |

### Agent 8: Professional Accuracy (Practitioner Agent)

| Chapter | Result | Notes |
|---------|:------:|-------|
| TRS | PASS | Two-leg structure correct. Financing rate convention accurate. Corporate action pass-through correctly described. Murex booking confirmed |
| Equity Swap | PASS | Gross vs net dividend treatment correctly distinguished. ISDA Equity Definitions reference accurate. Quanto risk correctly flagged |
| Variance Swap | PASS | Variance vs volatility distinction correctly maintained. Convexity explanation accurate. Vega notional vs variance notional convention clearly stated. Cap mechanism described |
| CDS | PASS | Credit event definitions match 2014 ISDA Credit Definitions. Physical vs cash vs auction settlement correctly described. IMM date convention accurate. Upfront payment convention noted |

---

## 3. Book-Level Agent Results

### Agent 9: Cross-Chapter Consistency

| Check | Result | Notes |
|-------|:------:|-------|
| Protagonist uniqueness | ✓ | Dmitri, Natasha, Kwame, Isabella — 21 unique protagonists across 21 chapters |
| Analogy uniqueness | ✓ | Car rental, film royalty deal, weather insurance, home warranty — 21 unique domains |
| Booking system consistency | ✓ | All 4 use Murex, consistent with IRS pilot and Swaps family convention |
| Section structure | ✓ | 16 sections + v1.1 additional requirements in all 4 chapters |
| Professor Voice | ✓ | All 4 Professor Notes follow "If you remember only one thing" pattern |
| Bridge continuity | ✓ | TRS→IRS, Equity Swap→TRS, Variance Swap→IRS+Vol, CDS→CLN+Credit |
| v1.1 elements | ✓ | "Why This Product Exists" and Visual Specifications present in all 4 |
| Visual Spec naming | ✓ | All 20 Visual IDs follow TYPE_PRODUCT_## convention |

**Consistency score: 9.0**

### Agent 10: Progressive Complexity

| Check | Result | Notes |
|-------|:------:|-------|
| TRS position | ✓ | Natural first step after IRS — extends swap from interest to total return |
| Equity Swap position | ✓ | Specializes TRS to equity — builds logically |
| Variance Swap position | ✓ | Most abstract product in the batch — correctly placed after directional swaps |
| CDS position | ✓ | Credit swap mechanics fully developed — prerequisite for CLN batch |
| Swap family progression | ✓ | IRS → TRS → Equity Swap → Variance Swap → CDS follows rate → return → vol → credit |
| No forward references | ✓ | No chapter requires knowledge from later sections |

### Agent 11: Publication Readiness

| Metric | Score |
|--------|:-----:|
| Formatting consistency | 9.0 |
| Table alignment | 9.0 |
| ASCII diagram clarity | 9.0 |
| Spelling/grammar | 9.0 |
| Overall readiness | 9.0 |

---

## 4. Swaps Dependency-Chain Review

**Scope:** Verify that Parts 0-4 and the IRS pilot (5.2.1) provide sufficient prerequisites for all 4 Batch 4 products.

### Prerequisites Matrix

| Concept | Source | TRS | Eq Swap | Var Swap | CDS |
|---------|--------|:---:|:-------:|:--------:|:---:|
| Swap mechanics (two-party, netting) | 1.8, 5.2.1 | ✓ | ✓ | ✓ | ✓ |
| SOFR, EURIBOR, benchmark rates | 1.8 | ✓ | ✓ | ✓ | — |
| Yield curves, forward rates | 1.7 | ✓ | ✓ | — | — |
| ISDA Master Agreement, CSA | 5.2.1, 1.9 | ✓ | ✓ | ✓ | ✓ |
| Murex booking | 2.8 | ✓ | ✓ | ✓ | ✓ |
| Volatility (historical, implied) | 1.5 | — | — | ✓ | — |
| Options, Greeks (Vega) | 1.2, 1.4 | — | — | ✓ | — |
| Credit risk, credit spread | 1.9 | — | — | — | ✓ |
| CDS basics, credit events | 1.9 | — | — | — | ✓ |
| Recovery rate, ISDA definitions | 1.9 | — | — | — | ✓ |
| Equity, dividends | 0.3 | — | ✓ | — | — |
| Derivatives concept | 0.8 | ✓ | — | ✓ | — |
| Delta hedging | 2.7 | ✓ | — | — | — |
| CLN mechanics | 5.5.1 | — | — | — | ✓ |

### Assessment

**Overall: SUFFICIENT.** All 4 products have adequate prerequisite coverage in Parts 0-4 and the IRS pilot.

**One minor gap addressed:**
- **Variance as a tradeable quantity:** Part 1.5 teaches volatility but does not explicitly frame variance (vol²) as a tradeable asset class. The Variance Swap chapter (5.2.4) bridges this by defining variance from the volatility foundation and explaining why variance (not volatility) is the natural unit for swaps. This is handled within the chapter — no external gap remains.

**No gaps for TRS, Equity Swap, or CDS.** All prerequisites are fully covered.

---

## 5. v1.1 Compliance Assessment

This is the first batch under Framework v1.1. All new requirements are assessed:

### "Why This Product Exists" Section

| Check | TRS | Eq Swap | Var Swap | CDS |
|-------|:---:|:-------:|:--------:|:---:|
| Present after §4, before §5 | ✓ | ✓ | ✓ | ✓ |
| Typical Buyer | ✓ | ✓ | ✓ | ✓ |
| Problem Being Solved | ✓ | ✓ | ✓ | ✓ |
| How Client Makes Money | ✓ | ✓ | ✓ | ✓ |
| How Bank Makes Money | ✓ | ✓ | ✓ | ✓ |
| Market Conditions | ✓ | ✓ | ✓ | ✓ |
| When Makes Sense | ✓ | ✓ | ✓ | ✓ |
| When Poor Choice | ✓ | ✓ | ✓ | ✓ |
| Bank economics accurate (no guaranteed profitability implied) | ✓ | ✓ | ✓ | ✓ |
| Poor Choice is educational, not investment advice | ✓ | ✓ | ✓ | ✓ |

**All 4 chapters: 10/10 v1.1 educational checks PASS.**

### Visual Specifications

| Check | TRS | Eq Swap | Var Swap | CDS |
|-------|:---:|:-------:|:--------:|:---:|
| ≥ 3 specs (5+ recommended) | 5 ✓ | 5 ✓ | 5 ✓ | 5 ✓ |
| Visual ID, Type, Priority, Purpose, Caption, Location, Reuse | ✓ | ✓ | ✓ | ✓ |
| IDs follow TYPE_PRODUCT_## | ✓ | ✓ | ✓ | ✓ |
| ≥ 2 P1 specs | 3 ✓ | 2 ✓ | 3 ✓ | 3 ✓ |

**All 4 chapters: Visual Specifications fully compliant.**

### Glossary Discipline

All 4 chapters define terms consistently with established conventions. Key terms verified:
- "Total return" — defined in context (TRS, Equity Swap)
- "Variance" / "realized variance" — defined from volatility foundation (Variance Swap)
- "Credit event" — consistent with Part 1.9 (CDS)
- No glossary bloat introduced

---

## 6. Aggregate Quality Scores

| Metric | TRS | Eq Swap | Var Swap | CDS | Batch 4 Avg | Target | Status |
|--------|:---:|:-------:|:--------:|:---:|:-----------:|:------:|:------:|
| Educational | 8.7 | 8.5 | 8.8 | 8.6 | 8.65 | ≥ 8.5 | ✓ |
| Visual | 8.0 | 7.5 | 8.5 | 8.0 | 8.0 | ≥ 8.0 | ✓ |
| Terminology | 100% | 100% | 100% | 100% | 100% | ≥ 98% | ✓ |
| Beginner | 8.5 | 8.5 | 8.5 | 8.5 | 8.5 | — | ✓ |
| Consistency | 9.0 | 9.0 | 9.0 | 9.0 | 9.0 | — | ✓ |
| Pub Ready | 9.0 | 9.0 | 9.0 | 9.0 | 9.0 | — | ✓ |

---

## 7. Cumulative Quality (Batches 0-4)

| Metric | Pilot | Batch 1 | Batch 2 | Batch 3 | Batch 4 | Overall (21 chapters) |
|--------|:-----:|:-------:|:-------:|:-------:|:-------:|:---------------------:|
| Avg Educational | 8.7 | 8.62 | 8.62 | 8.55 | 8.65 | 8.64 |
| Avg Visual | 7.0 | 8.0 | 8.0 | 7.75 | 8.0 | 7.76 |
| Terminology | 94% | 100% | 100% | 100% | 100% | 98.5% |
| First-Pass Acceptance | 5/5 | 5/5 | 5/5 | 2/2 | 4/4 | 21/21 (100%) |

---

## 8. Findings

### Mandatory Fixes

None.

### Recommended Improvements

**R1 — Equity Swap Visual Score (7.5):**
The Equity Swap's lower visual score reflects its structural similarity to TRS — the product is essentially a TRS specialized to equity, limiting visual differentiation. The Comparison Chart (equity swap vs direct ownership) provides the strongest visual distinction. If visual parity is desired, consider adding a dividend flow visualization showing gross vs net treatment through the swap structure. This is cosmetic — all visual structural requirements are met.

**R2 — Variance Swap: Variance as Tradeable Quantity:**
Part 1.5 (Volatility) introduces volatility but does not explicitly teach variance as a tradeable asset class. The Variance Swap chapter bridges this gap effectively within §6 and §7. For future editions, consider adding a brief subsection to Part 1.5 that previews "variance" as a concept, reducing the cognitive load when the reader reaches §5.2.4. Not actionable now — deferred to Master Editorial Pass.

**R3 — Glossary Candidates from Batch 4:**
The following terms may warrant glossary entries if they recur in future batches:
- "Total return" (likely to appear in CLN and portfolio product chapters)
- "Realized variance" / "implied variance" (may appear in STEG volatility products)
- "Wrong-way risk" (relevant to CLN and CDO chapters)
- "ISDA Determinations Committee" (relevant to CLN and CDO chapters)

### Cosmetic Issues

None.

---

## 9. Acceptance Checklist

### v1.1 Checklist (47 items per chapter)

| # | Requirement | TRS | Eq Swap | Var Swap | CDS |
|:-:|------------|:---:|:-------:|:--------:|:---:|
| E1 | Feynman: understandable with dependencies | ✓ | ✓ | ✓ | ✓ |
| E2 | Why before how | ✓ | ✓ | ✓ | ✓ |
| E3 | No formula without plain-English first | ✓ | ✓ | ✓ | ✓ |
| E4 | Terms defined or in dependency table | ✓ | ✓ | ✓ | ✓ |
| E5 | No jargon watchlist violations | ✓ | ✓ | ✓ | ✓ |
| E6 | Three-barrier disambiguation | N/A | N/A | N/A | N/A |
| E7 | Dependency References table present | ✓ | ✓ | ✓ | ✓ |
| E8 | Cross-references accurate | ✓ | ✓ | ✓ | ✓ |
| E9 | §5 ≥ 4 scenarios with numbers | ✓ (4) | ✓ (4) | ✓ (4) | ✓ (4) |
| E10 | §12 full worked example | ✓ | ✓ | ✓ | ✓ |
| E11 | §2 unique analogy | ✓ | ✓ | ✓ | ✓ |
| E12 | §16 exactly 5 common mistakes | ✓ | ✓ | ✓ | ✓ |
| E13 | Why This Product Exists present | ✓ | ✓ | ✓ | ✓ |
| E14 | 7 subsections complete | ✓ | ✓ | ✓ | ✓ |
| E15 | Bank economics accurate | ✓ | ✓ | ✓ | ✓ |
| E16 | Poor Choice is educational | ✓ | ✓ | ✓ | ✓ |
| E17 | Glossary terms checked | ✓ | ✓ | ✓ | ✓ |
| E18 | No glossary bloat | ✓ | ✓ | ✓ | ✓ |
| V1 | §8 ASCII payoff/decision tree | ✓ | ✓ | ✓ | ✓ |
| V2 | Payoff axes follow standard | ✓ | ✓ | ✓ | ✓ |
| V3 | Timeline for periodic products | ✓ | ✓ | N/A | ✓ |
| V4 | Decision tree for conditional products | N/A | N/A | N/A | ✓ |
| V5 | Visual Learning Recs (5) | N/A (v1.1) | N/A (v1.1) | N/A (v1.1) | N/A (v1.1) |
| V6 | Rec fields specified | N/A (v1.1) | N/A (v1.1) | N/A (v1.1) | N/A (v1.1) |
| V7 | ≥ 2 P1 recs | N/A (v1.1) | N/A (v1.1) | N/A (v1.1) | N/A (v1.1) |
| V8 | ≥ 3 visual specs | ✓ (5) | ✓ (5) | ✓ (5) | ✓ (5) |
| V9 | Spec fields complete | ✓ | ✓ | ✓ | ✓ |
| V10 | ID naming convention | ✓ | ✓ | ✓ | ✓ |
| P1 | Correct booking system (Murex) | ✓ | ✓ | ✓ | ✓ |
| P2 | Four-Leg applicability (No) | ✓ | ✓ | ✓ | ✓ |
| P3 | Four-leg description | N/A | N/A | N/A | N/A |
| P4 | §11 exactly 5 red flags | ✓ | ✓ | ✓ | ✓ |
| P5 | Desk Perspective 5 rows | ✓ | ✓ | ✓ | ✓ |
| P6 | Desk Perspective product-specific | ✓ | ✓ | ✓ | ✓ |
| P7 | §13 exactly 5 interview questions | ✓ | ✓ | ✓ | ✓ |
| P8 | Knowledge Check 5+3+1 | ✓ | ✓ | ✓ | ✓ |
| C1 | §1 opens with named person | ✓ (Dmitri) | ✓ (Natasha) | ✓ (Kwame) | ✓ (Isabella) |
| C2 | Professor Note in §7 | ✓ | ✓ | ✓ | ✓ |
| C3 | No forbidden writing patterns | ✓ | ✓ | ✓ | ✓ |
| C4 | Length 1,800-3,500 words | ✓ (3,183) | ✓ (2,798) | ✓ (3,136) | ✓ (3,379) |
| C5 | 16 sections in correct order | ✓ | ✓ | ✓ | ✓ |
| C6 | Additional requirements present | ✓ | ✓ | ✓ | ✓ |
| C7 | Bridge text present | ✓ | ✓ | ✓ | ✓ |
| C8 | Cross-references accurate | ✓ | ✓ | ✓ | ✓ |
| C9 | Title format correct | ✓ | ✓ | ✓ | ✓ |
| C10 | ASCII ≤ 60 chars, tables ≤ 8 cols | ✓ | ✓ | ✓ | ✓ |

**All 4 chapters accepted. Swaps Core family: 5/8 products complete (IRS pilot + 4 Batch 4).**

---

## 10. Swaps Family Progress

| # | Product | Section | Protagonist | Analogy | Educational | Visual | Status |
|:-:|---------|---------|-------------|---------|:-----------:|:------:|:------:|
| 1 | IRS | 5.2.1 | Marcus | Crop exchange | 8.9 | 7.5 | Pilot ✓ |
| 2 | TRS | 5.2.2 | Dmitri | Car rental | 8.7 | 8.0 | Batch 4 ✓ |
| 3 | Equity Swap | 5.2.3 | Natasha | Film royalty deal | 8.5 | 7.5 | Batch 4 ✓ |
| 4 | Variance Swap | 5.2.4 | Kwame | Weather insurance | 8.8 | 8.5 | Batch 4 ✓ |
| 5 | CDS | 5.2.5 | Isabella | Home warranty | 8.6 | 8.0 | Batch 4 ✓ |
| 6 | Currency Swap | 5.2.6 | — | — | — | — | Batch 5 |
| 7 | Commodity Swap | 5.2.7 | — | — | — | — | Batch 5 |
| 8 | VLSP | 5.2.8 | — | — | — | — | Batch 5 |

**Swaps Family Avg Educational: 8.70 | Avg Visual: 7.90 | Terminology: 99.2% | Acceptance: 5/5**

---

*Review completed 2026-06-20. Batch 4 PASSED. Swaps Core complete: 5/8 products (IRS pilot + 4 Batch 4). First batch under Framework v1.1 — all new requirements met.*
