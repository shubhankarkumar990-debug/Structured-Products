# Educational Quality Report — Desk Bible v2 (Parts 0-4)

**Date:** 2026-06-19
**Scope:** Parts 0 through 4 (~2,183 lines, ~22,700 words)
**Reviewers:** Master Professor, Jargon Police, Feynman Reviewer, Cognitive Load Reviewer, Analogy Reviewer

---

## 1. Combined Findings

### Overall Educational Score

| Dimension | Score | Reviewer |
|-----------|:-----:|---------|
| Educational Quality | 8.0 | Master Professor |
| Clarity | 9.0 | Master Professor |
| Progression | 8.0 | Master Professor |
| Narrative | 7.0 | Master Professor |
| Consistency | 8.0 | Master Professor |
| Feynman Test | 7.5 | Feynman Reviewer |
| Cognitive Load | 7.5 | Cognitive Load Reviewer |
| Analogy Quality | 8.0 | Analogy Reviewer |
| Terminology Compliance | 92% | Jargon Police |
| **Composite** | **7.8 / 10** | |

### Verdict

Parts 0-4 are a strong educational foundation. Part 0 is excellent — it achieves the rare feat of making finance accessible without dumbing it down. Sections 2.1-2.3 (product construction, decomposition, Four-Leg Framework) are the intellectual core and are well-executed. The primary weaknesses are structural: Parts 3-4 abandon the teaching voice established in Parts 0-2, and two sections in Part 1 (1.4 Greeks, 1.7 Rates) are overloaded.

The material is publishable in its current form but would benefit substantially from a targeted revision pass.

---

## 2. Common Weaknesses

### 2.1 Narrative Abandonment in Parts 3-4

All five reviewers flagged the same issue: Parts 3 and 4 abandon the narrative, story-driven teaching approach that makes Parts 0-2 effective. Part 3 presents family trees as lists. Part 4 presents comparison matrices as reference tables. Neither has worked scenarios, guiding narrative, or teaching context.

**Impact:** The document serves two audiences (beginners and professionals) through Parts 0-2 but loses beginners entirely in Parts 3-4.

### 2.2 Section 1.7 Overload

Four of five reviewers identified Section 1.7 (Rates and Yield Curves) as the most problematic section. It introduces nine distinct concepts (yield curves, spot rates, forward rates, SOFR, EURIBOR, LIBOR transition, CMS rates, CMS spread, swaps, caps, floors, swaptions) with insufficient depth for the latter half. Caps, floors, and swaptions each receive approximately two sentences.

**Impact:** A reader encountering rates concepts for the first time will not retain the material from CMS onward.

### 2.3 Missing Worked Examples

Sections 1.4 (Greeks) and 1.7 (Rates) lack the worked numerical examples that make Sections 2.2-2.3 so effective. The contrast is stark: Section 2.2 breaks a 7% coupon into $20k + $45k - $5k - $5k with exact arithmetic. Section 1.4 defines Delta conceptually ("if the stock rises by $1, the option price rises by $0.50") but never walks through a hedging calculation.

### 2.4 Inconsistent Reinforcement Devices

Common Mistakes sections, Desk Perspective tables, and Professor Notes appear in Part 2 but not consistently in Parts 1, 3, or 4. These are high-value teaching devices that should be standardized.

---

## 3. Terminology Violations

**Compliance Rate:** 92% (8 violations found, 5 moderate, 3 minor)

| Term | Location | Severity | Fix |
|------|----------|:--------:|-----|
| CDO | 1.8 | Moderate | Not defined until Part 3.7. Add parenthetical or replace with "complex portfolio credit products" |
| closed-form pricing | 3.2 | Moderate | Add: "a direct formula gives you the price, rather than requiring a simulation" |
| path-dependent | 3.2 | Moderate | Add: "the payoff depends not just on where the price ends up, but on the entire path it took" |
| notional | 2.3 | Minor | Listed as Part 0 term in curriculum but never formally defined. Define on first use |
| termsheet | 2.5 | Minor | Add parenthetical defining it |
| IPO | 0.7 | Minor | Expand to "Initial Public Offering" |
| simulation | 3.2 | Minor | Add: "running thousands of random price paths through a computer" |
| MTN | Curriculum only | Info | Listed in curriculum as Part 2 term but absent from text. Define if needed for Part 5 |

**Strengths:** Part 0 terminology discipline is exemplary. Every term is bolded, immediately defined, and followed by an analogy. The pattern is consistent and replicable.

---

## 4. Clarity Issues

### Strong Clarity Sections
- Part 0 (all sections) — consistent register, short declarative sentences, Term → Definition → Analogy → Example → Why It Matters pattern
- Section 1.2 (Options From Zero) — methodical progression from concept to payoff diagram to terminology
- Section 2.2 (Decomposition) — exact arithmetic that makes abstract economics concrete
- Section 2.3 (Four-Leg Framework) — worked example with dollar amounts

### Clarity Problems

1. **Four-Leg Framework diagram (2.3):** The ASCII flow diagram uses plain-text arrows and floating labels ("FTP Cost," "Hedge Costs") that are difficult to parse. Compare to the cleaner swap diagram in 1.7.

2. **Barrier terminology ambiguity:** "Barrier" is used with three distinct meanings without explicit disambiguation:
   - Capital barrier (knock-in level for principal risk)
   - Coupon barrier (level that determines coupon payment in Phoenix)
   - Autocall barrier (level that triggers early redemption)
   The Phoenix entry in Section 4.1 lists "KI (coupon + autocall)" in one cell, conflating multiple thresholds.

3. **Part 4 abbreviation density:** Tables use KI, KO, RC, DRC, KODRC, CRC, CRA, ICN, FTD, NTD without re-expansion. While all are introduced in earlier sections, the abbreviation density in Part 4 is high. A legend at the top of Section 4.1 would help.

---

## 5. High Cognitive Load Sections

Ranked by severity:

| Rank | Section | Concepts | Load | Fix |
|:----:|---------|:--------:|:----:|-----|
| 1 | 1.7 Rates/Yield Curves | 9 | VERY HIGH | Split into two sections with worked examples |
| 2 | Part 4 (all matrices) | 50+ data points | HIGH | Add narrative introductions and worked scenarios |
| 3 | 1.4 Greeks | 8 | HIGH | Add integrated worked example |
| 4 | Part 3 (cumulative) | 44 product names | HIGH | Add one-sentence descriptions per product |
| 5 | 1.5 Volatility | 6 | MODERATE-HIGH | Add historical evidence for mispricing claim |

**Reinforcement Device Gaps:**
- "Why This Matters for Structured Products" closings present in Part 0, absent in Parts 1-4
- Common Mistakes sections present in some Part 2/3 sections, absent elsewhere
- Desk Perspective tables present only in Part 2
- No mid-Part reinforcement exercises (only end-of-Part Knowledge Checks)

---

## 6. Missing Analogies

| Concept | Location | Impact | Suggested Analogy |
|---------|----------|--------|-------------------|
| CMS rates | 1.7 | High (central to STEG) | Real-time price quotes for fixed-rate mortgages of different lengths |
| Swaptions | 1.7 | High (compound concept) | Gym membership reservation — pay a fee for the right to join at today's rate |
| Notional | 2.3 | Medium | Face value of a gift card — all calculations based on it |
| Path-dependence | 3.2 | Medium | Step-counter (path matters) vs scale (only final number matters) |
| Product family evolution | Part 3 | Medium | Smartphone product line — base model plus one feature per variant |
| How to read matrices | Part 4 | Medium | Restaurant menu — scan the columns that matter to you |

**Weak Analogies Needing Replacement:**
- Lottery ticket → Vega (1.4): Imprecise. Replace with umbrella price sensitivity to rain forecast changes
- Weather forecast → model risk (1.8): Conflicts with implied volatility weather analogy in 1.5. Replace with outdated road map analogy

**Conflicting Analogies:**
- Restaurant (FO/MO/BO in 0.12) vs Casino (hedging in 2.7): The front office is framed as "the kitchen" in 0.12, but 2.7 frames the hedging desk as a "casino" — a complete business, not a kitchen. Resolve by nesting: "the kitchen runs like a casino — follow tested recipes to earn a consistent margin."

---

## 7. Recommended Revisions

### Priority 1 — Critical (apply before Part 5)

| # | Revision | Sections | Rationale |
|:-:|----------|----------|-----------|
| 1 | Split Section 1.7 into 1.7a (Yield Curves, Spot/Forward Rates) and 1.7b (Benchmarks, CMS, Caps/Floors/Swaptions) | 1.7 | Highest cognitive load section. Flagged by 4 of 5 reviewers |
| 2 | Add integrated worked example to Section 1.4 showing Delta, Gamma, Theta changing together | 1.4 | Greeks are abstract without numbers. Flagged by 3 of 5 reviewers |
| 3 | Add narrative introductions to Part 3 family trees (one sentence per product explaining its distinctive feature) | 3.3-3.8 | Converts taxonomy from list to teaching. Flagged by 3 of 5 reviewers |
| 4 | Add worked scenario to Part 4 ELN master matrix (client need → matrix lookup → product recommendation) | 4.1 | Converts reference table to teaching moment. Flagged by 4 of 5 reviewers |
| 5 | Fix all moderate-severity terminology violations (CDO, closed-form, path-dependent, notional, termsheet) | Various | No Unexplained Terminology rule violations |

### Priority 2 — High (apply during review pass)

| # | Revision | Sections | Rationale |
|:-:|----------|----------|-----------|
| 6 | Disambiguate barrier terminology (capital barrier, coupon barrier, autocall barrier) | 1.3, 4.1 | Barrier ambiguity flagged by 2 reviewers |
| 7 | Add transition bridges between Parts 2→3 and 3→4 | End of 2.8, end of 3.8 | Narrative breaks flagged by Master Professor |
| 8 | Standardize Common Mistakes sections across all Parts 1-4 | All | Inconsistency flagged by Master Professor and Cognitive Load reviewer |
| 9 | Replace Vega lottery ticket analogy with umbrella/forecast sensitivity | 1.4 | Weak analogy flagged by Analogy Reviewer |
| 10 | Add historical evidence for volatility mispricing claim in 1.5 | 1.5 | Unsupported claim flagged by Master Professor and Feynman Reviewer |

### Priority 3 — Medium (apply during final polish)

| # | Revision | Sections | Rationale |
|:-:|----------|----------|-----------|
| 11 | Resolve casino/restaurant analogy conflict | 2.7 | Minor analogy inconsistency |
| 12 | Resolve weather forecast analogy reuse (implied vol vs model risk) | 1.8 | Domain collision flagged by Analogy Reviewer |
| 13 | Add framing paragraph to Greeks connecting Delta→Gamma→Vega→Theta as a system | 1.4 | No hierarchy narrative — flagged by Master Professor |
| 14 | Extend Desk Perspective tables to key Part 1 sections (1.2, 1.4, 1.5) | Part 1 | Reinforcement device gap |
| 15 | Add abbreviation legend to top of Part 4 | 4.1 | High abbreviation density in reference tables |
| 16 | Move model risk from 1.8 to standalone section or end of Part 1 | 1.8 | Model risk applies to all derivatives, not just credit |
| 17 | Add CMS rates and swaptions analogies | 1.7 | Missing analogies for key STEG/SRT concepts |
| 18 | Fix minor terminology violations (IPO, simulation) | 0.7, 3.2 | Minor rule violations |

---

## 8. Overall Educational Score

| Dimension | Score | Assessment |
|-----------|:-----:|-----------|
| Part 0 | 9.5 / 10 | Exemplary. Zero-to-derivatives in 12 sections, narrative-driven, Feynman-compliant |
| Part 1 | 7.0 / 10 | Strong in 1.1-1.3, weakens in 1.4 (no examples), fails in 1.7 (overload) |
| Part 2 | 8.5 / 10 | Strong throughout. Decomposition and Four-Leg Framework are intellectual core |
| Part 3 | 5.5 / 10 | Taxonomically correct, pedagogically thin. Needs narrative and product descriptions |
| Part 4 | 5.0 / 10 | Useful reference, poor teaching. Needs worked scenarios and introductions |
| **Composite** | **7.8 / 10** | **Strong foundation, targeted revision needed in 4 areas** |

### Strongest Chapters
1. **0.10 — Why Structured Products Exist** (pension fund narrative, five reasons, bank perspective)
2. **2.2 — Product Construction / Decomposition** (coupon arithmetic, Common Mistakes)
3. **1.2 — Options From Zero** (restaurant/insurance analogies, payoff diagrams, seller twist)

### Weakest Chapters
1. **1.7 — Rates and Yield Curves** (nine concepts, insufficient depth for final six)
2. **Part 4 — Comparison Matrices** (reference without teaching)
3. **Part 3 — Product Taxonomy** (taxonomy without narrative)

---

*Report compiled from five independent reviews. All findings cross-referenced for consistency. Priority 1 revisions should be applied before beginning Part 5 writing. Estimated revision effort: 2-3 hours for Priority 1, 1-2 hours for Priority 2.*
