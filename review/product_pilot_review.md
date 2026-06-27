# Product Pilot Review — Desk Bible v2

**Date:** 2026-06-19
**Scope:** 5 Pilot Product Chapters (PPN, RC, Phoenix, IRS, CLN)
**Reviewers:** Master Professor, Jargon Police, Feynman Reviewer, Cognitive Load Reviewer, Analogy Reviewer, Visual Design Reviewer
**Total content reviewed:** ~1,445 lines, ~16,000 words
**Visual design cross-reference:** `review/visual_design_report.md`

---

## 1. Executive Summary

All five pilot chapters meet the educational standard established in the Pilot Charter. The 16-section template plus additional requirements (Professor Note, Desk Perspective, Knowledge Check, Visual Learning Recommendations, Dependency References) prove flexible enough to handle products ranging from simple (PPN — no barriers, no coupons during life) to complex (Phoenix — three barriers, memory, worst-of basket) to non-note derivatives (IRS — pure swap, Murex booking) to credit products (CLN — credit events, ISDA process). The template scales.

The pilot chapters are a meaningful step up from Parts 3-4 in teaching quality — every chapter opens with a real-world scenario, builds intuition through analogy, and progresses to mechanics and operations. The narrative voice established in Parts 0-2 is fully restored. Worked examples are concrete, numerical, and multi-scenario. The 8-quarter Phoenix table is the strongest worked example in the entire document.

**Composite Educational Score: 8.7 / 10**
**Visual Design Score: 6.7 / 10**
**Combined Readiness Score: 8.0 / 10**

**Recommendation: PASS — proceed to full-scale product generation with visual template standardization.**

---

## 2. Strengths

### Teaching Quality

1. **"Teach first, formalize second" pattern.** Every chapter follows the same arc: real-world scenario (§1) → vivid analogy (§2) → client problem (§3) → client motivation (§4) → concrete scenarios with numbers (§5) → technical depth (§6-11) → reinforcement (§12-16). This pattern restores the narrative voice that Parts 3-4 had lost. It is the defining quality of the pilot.

2. **Worked examples with arithmetic.** The PPN construction walk-through (Steps 1-5: $100 → $88.90 bond → $11.10 option budget → 60% participation → margin → 52%) is the best decomposition example in the document. The Phoenix 8-quarter table (Q1-Q8 with memory accumulation, $90,000 memory payout in Q4, eventual autocall in Q8) is the best path-dependent example. Both make abstract concepts traceable through exact numbers.

3. **Analogy discipline.** Every chapter has a distinct, strong primary analogy with natural extensions maintained through the Mental Models table. No domain collisions between chapters or with Parts 0-4. The analogies earn their place — each maps precisely to the product's core mechanic: seat belt (PPN = protection), earthquake insurance (RC = selling risk), employment contract (Phoenix = conditional performance), crop exchange (IRS = symmetric swap), bail bondsman (CLN = posting collateral against default).

4. **Common Mistakes as teaching.** Section 16 in each chapter is not just a list of errors — it corrects specific misconceptions with explanations. "My maximum loss is 30% because the barrier is at 70%" (RC, Mistake #1) directly addresses the most dangerous misunderstanding about barrier products.

5. **Professor Notes that focus.** Each chapter's Professor Note captures the single most important insight — the one thing a reader should remember even if they forget everything else. PPN: "participation rate is determined by arithmetic, not by design." IRS: "a swap does not move money at inception."

### Template Design

6. **100% template compliance.** All 80 section cells (16 sections × 5 chapters) and all 25 additional requirement cells (5 requirements × 5 chapters) are filled. No section is missing, truncated, or formulaic.

7. **System accuracy.** NEMO/Sophis for equity-linked and credit notes; Murex for rates derivatives. Four-Leg Framework applicability explicitly stated for every product (all five pilot products are "No" — four-leg applies to SRT/STEG). These routing distinctions are operationally critical and correctly encoded.

8. **Dependency References as navigation.** Every chapter ends with a table mapping each concept to where it was originally taught. Cross-references are accurate after the Section 1.7/1.8/1.9 renumbering. This enables non-linear reading and self-directed study.

### Structural Coverage

9. **Progressive complexity across the pilot.** PPN (simplest ELN: two components, no barriers) → RC (medium: one barrier, short put) → Phoenix (complex: three barriers, memory, worst-of, path-dependent) → IRS (different family: pure derivative, linear payoff) → CLN (different risk domain: credit events, ISDA). This range proves the template handles structural variation without distortion.

10. **Five-role Desk Perspective consistency.** Trader, Structurer, Product Control, Risk, Operations — every product chapter covers all five roles with specific, non-generic descriptions. The Trader perspective on PPN (long call, long Vega) contrasts meaningfully with RC (long KI put, Gamma spike near barrier), demonstrating that the desk perspective adds real teaching value per product.

---

## 3. Weaknesses

### Educational

1. **CLN credit event process lacks worked example.** Scenario 4 (spread widening, no default) describes mark-to-market value changes without specific numbers. Adding "if the CDS spread widens from 300bp to 800bp, the CLN's market value drops from $500,000 to approximately $420,000" would make the concept concrete. This is the weakest Feynman moment in the pilot.

2. **Phoenix Product Construction is abstract.** Unlike PPN (bond + call, exact arithmetic) and RC (bond + short put, exact decomposition), the Phoenix's multiple embedded options (KI put, digital coupons, autocall barriers, memory) cannot be decomposed into a clean arithmetic walk-through. The chapter handles this by describing rather than decomposing, which is acceptable but less satisfying. The Monte Carlo mention is correctly parenthetical-defined but may intimidate some readers.

3. **IRS family transition is abrupt.** The shift from equity-linked products (PPN, RC, Phoenix) to rates products (IRS) has no bridging text. A one-sentence transition at the start of §5.2 acknowledging the family shift would help: "We now move from equity-linked notes to interest rate derivatives — a different product family, different booking system, and different risk profile."

4. **Formal Definition precedes intuition-building (PPN).** Section 6 (Formal Definition) presents the redemption formula before Section 7 (Product Construction) builds the intuition for why the formula looks the way it does. The ordering is dictated by the template (§6 before §7), which means every chapter will have this slight inversion. In practice, readers who encounter the formula in §6 and don't fully absorb it will have the "aha" in §7. Minor concern.

### Terminology

5. **Six minor jargon violations remain.** "No-call period" (Phoenix), "ACT/360 / 30/360" (IRS), "RED code" (CLN), "ISDA Determinations Committee" (CLN), "high-yield" (CLN Knowledge Check), and "long volatility" (PPN). All have been fixed in the current text, but these violations demonstrate that operational and credit terminology requires extra vigilance during full-scale generation. The Jargon Police agent should flag any term used without definition in the current section or a declared dependency.

### Visual

6. **Zero timeline diagrams.** Timelines are the most important missing visual category. Path-dependent products (Phoenix) and periodic-payment products (RC, IRS, CLN) are best understood temporally, but no chapter includes an inline timeline. The text compensates with tables (the Phoenix Q1-Q8 table, the IRS 3-year cash flow table), but a visual timeline would add significant comprehension value.

7. **Inconsistent payoff diagram axis conventions.** PPN uses "Investor Return (%)" / "Underlying Final Level." IRS uses "P&L for Fixed Payer" / "Market Rate." CLN uses "Investor Return" / "Time." These should be standardized before scaling: "Investor Return (%)" / "Underlying at Maturity (% of Initial)" for equity/credit products.

8. **Missing construction waterfall diagrams.** The PPN Steps 1-5 and the RC coupon decomposition are described in text and tables but not diagrammed. Waterfall diagrams are the most intuitive format for decomposition and would be the highest-impact visual addition.

---

## 4. Template Improvements

### 4.1 Improvements to Apply Before Full-Scale Generation

| # | Improvement | Rationale | Effort |
|:-:|------------|-----------|:------:|
| 1 | **Add family transition text** at the start of each Part 5 subsection (5.1 ELN, 5.2 Swaps, 5.3 SRT, 5.4 STEG, 5.5 CLN, 5.6 Other) | The pilot transition from ELN to Swaps to CLN was abrupt. A 2-3 sentence introduction per family subsection orients the reader | Low |
| 2 | **Standardize ASCII payoff diagram axes** | Axis label inconsistency across pilot chapters will compound at 49 products. Adopt: Y = "Investor Return (%)", X = "Underlying at Maturity (% of Initial)" for equity/credit; Y = "P&L ($)", X = "Market Rate (%)" for rates | Low |
| 3 | **Add a "How This Differs From..." bridge** to the start of chapters within the same family | When writing the DRC after the RC, a 2-sentence opening explaining "this product is like the RC you just learned, except..." provides immediate anchoring. The pilot chapters are standalone (different families), but within-family chapters will benefit from explicit comparison | Low |

### 4.2 Template Observations (No Change Needed)

| Observation | Assessment |
|-------------|-----------|
| Section ordering (§6 Formal Definition before §7 Construction) | Slight intuition-before-formula inversion, but consistent ordering across all chapters is more important than optimal per-chapter ordering. **Keep as-is.** |
| 16 sections per chapter | None of the 16 sections felt redundant or forced across the 5 pilot products. **Keep all 16.** |
| 5 Visual Learning Recommendations per chapter | Appropriate count. 3 would be too few for complex products (Phoenix). 7 would dilute focus. **Keep at 5.** |
| Knowledge Check structure (5+3+1) | The 5 review / 3 scenario / 1 desk question structure works across all product types. **Keep as-is.** |
| Professor Note placement (in §7 Product Construction) | Effective. The construction section is where the key insight typically lives. **Keep as-is.** |

---

## 5. Educational Quality Assessment

### 5.1 Per-Chapter Scores (All 5 Reviewers)

| Chapter | Master Prof | Jargon | Feynman | Cog Load | Analogy | Composite |
|---------|:----------:|:------:|:-------:|:--------:|:-------:|:---------:|
| **5.1.1 PPN** | 9.0 | 95% | 9.0 | 9.0 | 9.0 | **9.0** |
| **5.1.2 RC** | 8.5 | 96% | 8.5 | 8.5 | 9.0 | **8.6** |
| **5.1.3 Phoenix** | 9.0 | 93% | 8.5 | 8.0 | 9.5 | **8.8** |
| **5.2.1 IRS** | 8.5 | 94% | 9.0 | 9.0 | 9.0 | **8.9** |
| **5.5.1 CLN** | 8.5 | 91% | 8.0 | 8.5 | 9.0 | **8.4** |
| **Overall** | **8.7** | **94%** | **8.6** | **8.6** | **9.1** | **8.7** |

### 5.2 Dimension Analysis

**Strongest dimension: Analogy Quality (9.1/10).** All five primary analogies are strong, precisely mapped, memorable, and maintained through Mental Models. No domain collisions. Each chapter uses a distinct domain. Cross-chapter contrast is pedagogically effective (seat belt vs earthquake insurance = buying vs selling protection).

**Second strongest: Master Professor (8.7/10).** Narrative voice is consistent. Progressive complexity is well-calibrated. Reinforcement devices are 100% deployed (every chapter has all 10 device types). The "teach first, formalize second" pattern is the document's signature quality.

**Weakest dimension: Feynman (8.6/10).** Still strong, but the CLN spread-widening scenario (abstract MTM concept) and Phoenix product construction (multiple embedded options resisting decomposition) reveal that the Feynman standard is harder to meet for more abstract concepts. These are not failures — they are inherent difficulty ceilings for certain products.

**Terminology compliance (94%).** High but not perfect. The pattern is clear: core product terminology (barriers, coupons, decomposition) is always well-defined. Operational terminology (day count conventions, no-call periods) and credit market jargon (ISDA committees, RED codes) slip through more often. The Jargon Police agent should receive a supplementary watchlist of operational/credit terms for full-scale generation.

### 5.3 Rule Compliance

| Rule | Compliance | Notes |
|------|:----------:|-------|
| **No Unexplained Terminology** | 94% | 6 minor violations found and fixed. Pattern: operational and credit jargon more prone to violation than core product terms |
| **Why Before How** | 100% | All chapters follow §1-5 (why/what) → §6-11 (how) structure |
| **Feynman Rule** | 100% | All 5 chapters pass. Phoenix and CLN are at the boundary but earn their complexity through reinforcement |
| **Story First** | 100% | All chapters open with a zero-knowledge scenario and analogy before any technical content |
| **Cognitive Load** | 100% | No chapter is critically overloaded. Phoenix (10 concepts) is at the upper limit but is well-scaffolded by the 8-quarter table |
| **Why Do I Care** | 100% | All chapters include §3 (What Problem) and §4 (Why Clients Buy) |

### 5.4 Reinforcement Device Coverage

| Device | PPN | RC | Phoenix | IRS | CLN | Coverage |
|--------|:---:|:--:|:-------:|:---:|:---:|:--------:|
| Professor Note | ✓ | ✓ | ✓ | ✓ | ✓ | 100% |
| Worked Example | ✓ | ✓ | ✓ | ✓ | ✓ | 100% |
| "What Happens If" (4+ scenarios) | ✓ | ✓ | ✓ | ✓ | ✓ | 100% |
| Mental Models Table | ✓ | ✓ | ✓ | ✓ | ✓ | 100% |
| Common Mistakes (5) | ✓ | ✓ | ✓ | ✓ | ✓ | 100% |
| Payoff Diagram / Decision Tree | ✓ | ✓ | ✓ | ✓ | ✓ | 100% |
| Desk Perspective (5 roles) | ✓ | ✓ | ✓ | ✓ | ✓ | 100% |
| Knowledge Check (5+3+1) | ✓ | ✓ | ✓ | ✓ | ✓ | 100% |
| Visual Learning Recs (5) | ✓ | ✓ | ✓ | ✓ | ✓ | 100% |
| Dependency References | ✓ | ✓ | ✓ | ✓ | ✓ | 100% |

**100% reinforcement device coverage** — all 50 cells filled (10 devices × 5 chapters). This is a significant improvement over Parts 1-4, where devices appeared inconsistently.

---

## 6. Visual Quality Assessment

Full analysis in `review/visual_design_report.md`. Summary:

### 6.1 Current State

| Category | Present | Specified | Gap |
|----------|:-------:|:---------:|:---:|
| Payoff charts | 3 ASCII | 5 production | 2 missing inline + 5 need production rendering |
| Structure/flow diagrams | 1 ASCII | 6 production | 5 missing inline + 6 need production rendering |
| Timelines | 0 | 5 production | **5 missing inline** + 5 need production rendering |
| Decision trees | 1 ASCII | 2 production | 1 missing inline + 2 need production rendering |
| Comparison charts | 0 | 7 production | **7 missing inline** + 7 need production rendering |
| Tables (data) | 43 | — | Complete. No gaps |
| **Total** | **48** (6 diagrams + 43 tables) | **25 production** | **20 inline gaps** |

### 6.2 Visual Scores

| Dimension | Score |
|-----------|:-----:|
| Inline ASCII diagrams (existing) | 7.0 / 10 |
| Visual Learning Recommendations (specified) | 8.5 / 10 |
| Template readiness for scaling | 6.5 / 10 |
| Cross-chapter visual consistency | 6.0 / 10 |
| Gap coverage | 5.5 / 10 |
| **Composite Visual Score** | **6.7 / 10** |

### 6.3 Top Visual Priorities

Before full-scale generation, establish these 3 visual templates:

1. **Payoff chart template** — standardized axes, barrier line notation, zone color convention
2. **Timeline template** — horizontal format, event markers, payment arrows
3. **Decision tree template** — box shapes, YES/NO branching, loop indicators

These templates will apply across all 49 product chapters and ensure visual consistency.

---

## 7. Readiness Recommendation

### PASS / FAIL Assessment

| Dimension | Assessment | Verdict |
|-----------|-----------|:-------:|
| **Rule Compliance** | 94% terminology, 100% on all other rules | **PASS** |
| **Template Compliance** | 100% section coverage (80/80), 100% additional requirements (25/25) | **PASS** |
| **Analogy Quality** | All 5 strong. No weak, no conflicts | **PASS** |
| **Worked Example Quality** | All 5 concrete with specific numbers and multi-scenario outcomes | **PASS** |
| **Cross-Product Consistency** | Consistent voice, format, system references, dependency chains | **PASS** |
| **Scalability** | Template tested across 3 families, 3 complexity levels, 2 booking systems, 3 payoff types | **PASS** |
| **Visual Design** | Functional for markdown. Templates need standardization before scaling. 25 production visuals specified | **CONDITIONAL PASS** |

### Final Verdict

## PASS — All 6 Core Dimensions Met. Visual Design Conditionally Passed.

The pilot product chapters demonstrate that the 16-section template, combined with the 6 Permanent Educational Rules and the 10-device reinforcement suite, produces product chapters that teach rather than merely document. The template scales across product types and complexity levels without distortion.

### Pre-Scaling Checklist

| # | Action | Status | Blocking? |
|:-:|--------|:------:|:---------:|
| 1 | Fix 6 minor terminology violations | ✓ Done | — |
| 2 | Add family transition text to Part 5 subsection headers (5.1, 5.2, 5.3, 5.4, 5.5, 5.6) | Pending | No |
| 3 | Standardize ASCII payoff diagram axis conventions | Pending | No |
| 4 | Establish 3 visual templates (payoff, timeline, decision tree) | Pending | No |
| 5 | Add CLN Scenario 4 worked MTM numbers | Pending | No |
| 6 | Add "How This Differs From..." bridge pattern for within-family chapters | Pending | No |

None of items 2-6 blocks scaling. They can be applied iteratively during full-scale generation.

### Patterns to Preserve

1. Analogy-first opening in every chapter
2. "Why" before "How" (§1-5 → §6-11)
3. Four-scenario minimum in "What Happens If"
4. Construction as arithmetic (where the product allows)
5. Professor Note as single most important insight
6. 5-role Desk Perspective for every product
7. Dependency References as navigation aid
8. System routing accuracy (NEMO/Sophis vs Murex)

### Scaling Order

Per the Pilot Charter, remaining 44 products follow Part 5 family ordering:

**ELN (10 remaining):** DRC → KODRC → CRC → Airbag → FCN → Callable Range Accrual → ICN → Digital Coupon Note → Booster → Digital KI Put

**Swaps (6 remaining):** TRS → Equity Swap → Currency Swap → Commodity Swap → CDS → Variance/Volatility Swap

**SRT (5):** IR Callable → IR Accreting/ZCL → NCRA → CRA → Digital Cap-Floor

**STEG (4):** Vanilla Steepener → Range Accrual Steepener → Callable Steepener → TARN Steepener

**CLN (4 remaining):** Skew CLN → FTD → NTD → Synthetic CDO Tranche

**Other (5):** Structured Deposit → Accumulator/Decumulator → Option on RC → ELO → Forward

---

*Pilot review package completed 2026-06-19. Two review files generated:*
- *`review/product_pilot_review.md` — this file (consolidated educational + visual review)*
- *`review/visual_design_report.md` — detailed visual design assessment*

*STOP. No additional product chapters will be generated until approval is received.*
