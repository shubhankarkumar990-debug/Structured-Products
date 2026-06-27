# Interview System — Design Document

**Date:** 2026-06-22
**Artifact:** `production/interview_system.md`
**Estimated Lines:** 2,000–2,500
**Framework:** v1.3.1 (frozen)

---

## 1. Purpose

Train candidates for Structured Products interviews across 5 desk roles (Structuring, Trading, Sales, Risk, Model Validation), both buy-side and sell-side, from beginner to expert.

---

## 2. Architecture

```
Part 1  INTERVIEW STRATEGY GUIDE
        1.1  How SP Interviews Work (5 roles × buy/sell)
        1.2  The 4-Tier Answer Framework
        1.3  Role-Specific Expectations Matrix

Part 2  PRODUCT ANSWER TEMPLATES
        2.1  49-Product Answer Library (4 tiers × 49 products = 196 blocks)

Part 3  COMPARISON & CONFUSION PAIRS
        3.1  Top 10 Interview Pairs — Full Structured Comparison
        3.2  Quick Differentiation Guide (25 pairs)

Part 4  QUESTION BANK
        4.1  Technical Questions (Greeks, Options, Rates, Credit, Vol, Correlation)
        4.2  Product Knowledge Questions (all 49 products)
        4.3  Structuring Logic Questions (decision framework, governance, anti-patterns)
        4.4  Case Interview Questions (client scenarios, recommendations, trade-offs)
        4.5  Desk-Specific Questions (5 roles)

Part 5  MOCK INTERVIEW TRACKS
        5.1  5 Role-Specific Tracks (Structuring, Trading, Sales, Risk, Model Val)
        5.2  4 Difficulty Progressions
        5.3  Scoring Rubric

Part 6  INTERVIEW TRAPS & ANTI-PATTERNS
        6.1  Technical Traps (20)
        6.2  Behavioral / Framing Traps (10)
```

---

## 3. Deduplication Strategy

### What Solutions Manual Covers (DO NOT REPRODUCE)

| SM Content | Interview System Treatment |
|------------|---------------------------|
| 10-step decision model | REFERENCE §1.1 of SM. Do not reproduce. Interview questions TEST the model. |
| 40 scenarios with candidate selection | REFERENCE by scenario number. Interview cases present SIMILAR but distinct client quotes. |
| 18 anti-patterns | REFERENCE by AP number. Interview traps turn anti-patterns into "spot the mistake" questions. |
| 49-row replacement table | REFERENCE. Interview question: "Client can't get X — what do you propose?" |
| Market regime matrix | REFERENCE §1.3 of SM. Interview questions test regime awareness. |
| Persona filter | REFERENCE §1.2 of SM. Interview questions test suitability judgment. |

### What Interview System Adds (NEW CONTENT)

| New Content | Not in SM |
|-------------|-----------|
| 4-tier answer framework (30s / 2min / desk / senior) | SM has no answer templates |
| 196 per-product answer blocks | SM scenarios cover products indirectly |
| Technical depth (Greeks, pricing, replication) | SM focuses on selection, not mechanics |
| Role-specific expectations | SM is structurer-only |
| Mock interview tracks with scoring | SM has no assessment framework |
| Buy-side vs sell-side framing | SM is sell-side structurer perspective |
| Behavioral/soft interview traps | SM is purely technical |

### Boundary Rule

> The Interview System asks questions and provides answer frameworks.
> The Solutions Manual provides structuring methodology and recommendations.
> If a question's answer IS a Solutions Manual scenario → REFERENCE the scenario, don't recreate it.

---

## 4. Part 1: Interview Strategy Guide

### 1.1 How SP Interviews Work

Role × side matrix:

| Role | Sell-Side Focus | Buy-Side Focus |
|------|----------------|----------------|
| **Structuring** | Product design, client suitability, complexity governance | Term sheet review, hidden risk identification |
| **Trading** | Greeks, hedging, P&L attribution, market making | Position sizing, risk/reward, portfolio construction |
| **Sales** | Product explanation, client matching, objection handling | Due diligence, manager selection, fee analysis |
| **Risk** | Risk metrics, limit frameworks, stress testing, model validation | Portfolio risk, counterparty exposure, regulatory capital |
| **Model Validation** | Pricing models, calibration, numerical methods, model limitations | Model risk assessment, independent valuation, back-testing |

Each role: 3–5 sentences on what interviewers look for, typical round structure, and pass/fail signals.

### 1.2 The 4-Tier Answer Framework

Every product question has 4 levels of answer depth:

| Tier | Name | Time | When Used | What's Expected |
|:----:|------|:----:|-----------|-----------------|
| 1 | Elevator | 30 sec | Phone screen, rapid-fire | What it IS, who buys it, one key risk |
| 2 | Technical | 2 min | First round, written test | Construction, decomposition, payoff diagram, key Greeks |
| 3 | Desk | 5 min | Desk round, experienced interviewer | Hedging, P&L drivers, market regime impact, common mistakes |
| 4 | Senior | 10 min | Final round, MD/partner | Trade-offs vs alternatives, structural edge, regulatory impact, market evolution |

### 1.3 Role-Specific Expectations Matrix

49 products × 5 roles → expected knowledge depth:

| Product Complexity | Structuring | Trading | Sales | Risk | Model Val |
|:------------------:|:-----------:|:-------:|:-----:|:----:|:---------:|
| Beginner (2–3) | Tier 4 | Tier 3 | Tier 3 | Tier 2 | Tier 2 |
| Intermediate (4–5) | Tier 4 | Tier 3 | Tier 2 | Tier 3 | Tier 3 |
| Advanced (6–7) | Tier 3 | Tier 3 | Tier 2 | Tier 3 | Tier 4 |
| Expert (8–10) | Tier 3 | Tier 2 | Tier 1 | Tier 4 | Tier 4 |

This table governs which answer tier to study for each role.

---

## 5. Part 2: Product Answer Templates

### Design

49 products × 4 tiers = 196 answer blocks.

Each block:

```
### [Product Name] (Complexity X) — Section 5.Y.Z

**Tier 1 — Elevator (30 seconds)**
[3–4 sentences: what it is, who buys, key risk]

**Tier 2 — Technical (2 minutes)**
[Construction, components, payoff at maturity, key Greeks, one pricing insight]

**Tier 3 — Desk (5 minutes)**
[Hedging strategy, P&L drivers, market regime, lifecycle events, common desk mistake]

**Tier 4 — Senior (10 minutes)**
[Trade-offs vs alternatives, structural vs market edge, regulatory considerations,
 historical context, when this product fails, what replaces it]
```

### Source Mapping

| Tier | Primary Source | Secondary Source |
|------|---------------|-----------------|
| 1 | §1 (Explain Like I'm New) per chapter | Atlas §1 |
| 2 | §11 (Formal Definition) + §12 (Construction) per chapter | Atlas Appendix E |
| 3 | §14 (Desk Reality) + §15 (Risk Analysis) per chapter | Atlas Appendix G |
| 4 | §3 (What Problem) + §8 (Client Perspective) per chapter | Solutions Manual (REFERENCE) |

### Volume Estimate

- Tier 1: ~3 lines per product × 49 = ~147 lines
- Tier 2: ~8 lines per product × 49 = ~392 lines
- Tier 3: ~10 lines per product × 49 = ~490 lines
- Tier 4: ~8 lines per product × 49 = ~392 lines
- Headers/formatting: ~100 lines
- **Part 2 total: ~1,520 lines**

### Space Management

Part 2 is the largest section. To control line count within target:

- **Top 10 Interview Products** (Matrix View 7: RC, Phoenix, IRS, CDS, PPN, VarSwap, CDO, WOAC, ACCUM, FTD): Full 4-tier treatment
- **Next 15 products** (Complexity 4–6, frequently traded): Full Tier 1–3, abbreviated Tier 4
- **Remaining 24 products**: Full Tier 1–2, abbreviated Tier 3, Tier 4 via cross-reference to similar product

This gives: 10 × 29 lines + 15 × 21 lines + 24 × 14 lines = 290 + 315 + 336 = **~941 lines** (plus headers ~100 = ~1,040)

---

## 6. Part 3: Comparison & Confusion Pairs

### 3.1 Top 10 Interview Pairs — Full Structured Comparison

Selected from Atlas Appendix F (25 pairs) + Matrix Appendix A (25 pairs), filtered for interview frequency:

| # | Pair | Why Top 10 |
|:-:|------|-----------|
| 1 | PPN vs RC | Most fundamental: protection vs yield. Tests option understanding. |
| 2 | Phoenix vs WOAC | Single vs worst-of. Tests correlation understanding. |
| 3 | Phoenix vs FCN | Conditional vs guaranteed coupon. Tests autocall mechanics. |
| 4 | FTD vs NTD | Correlation reversal. Tests deepest credit concept. |
| 5 | CLN vs CDS | Funded vs unfunded. Tests credit transfer mechanics. |
| 6 | IRS vs VLSP | Standard vs enhanced. Tests rate product knowledge. |
| 7 | TRS vs EqSwap | General vs specific swap. Tests synthetic access understanding. |
| 8 | RC vs DCI | Same mechanic, different asset class. Tests cross-asset thinking. |
| 9 | PPN vs SD | Note vs deposit. Tests regulatory/structural knowledge. |
| 10 | CDO vs FTD | Tranched vs binary. Tests portfolio credit depth. |

Each pair: side-by-side table (6 dimensions), "elevator differentiation" (1 sentence), "deep differentiation" (1 paragraph), "trap question" that tests the difference.

### 3.2 Quick Differentiation Guide

All 25 Atlas Appendix F pairs. One line each: key difference + one-sentence elaboration. REFERENCE Atlas F, don't reproduce.

---

## 7. Part 4: Question Bank

### Taxonomy

6 categories, 4 difficulty levels = 24 cells.

| Category | Beginner | Intermediate | Advanced | Expert | Total |
|----------|:--------:|:------------:|:--------:|:------:|:-----:|
| **A. Technical** | 10 | 15 | 15 | 10 | **50** |
| **B. Product Knowledge** | 15 | 20 | 15 | 10 | **60** |
| **C. Structuring Logic** | 5 | 10 | 15 | 10 | **40** |
| **D. Case Interviews** | 5 | 10 | 10 | 5 | **30** |
| **E. Desk-Specific** | 5 | 10 | 10 | 5 | **30** |
| **Total** | **40** | **65** | **65** | **40** | **210** |

### Category Definitions

**A. Technical Questions**
Greeks, options pricing, rates mechanics, credit fundamentals, volatility concepts, correlation.

| Sub-Category | Beginner | Intermediate | Advanced | Expert |
|-------------|----------|-------------|---------|--------|
| Greeks/Options | What is delta? | Explain gamma risk for a barrier | Pin risk near digital strike | Convexity of variance swaps — derive |
| Rates | What is an IRS? | How does CMS convexity affect STEG pricing? | Price a callable note using swaption decomposition | TARN path dependency — Monte Carlo design |
| Credit | What is a CDS? | Why does CLN have dual credit risk? | FTD correlation sensitivity — direction and magnitude | CDO base correlation surface — calibration |
| Volatility | What is implied vol? | Local vol vs implied vol | Vol surface dynamics: skew, term structure, smile | VarSwap replication via log contract |
| Correlation | What is correlation? | Worst-of barrier and correlation | FTD vs NTD correlation reversal | Copula choice impact on CDO pricing |

**B. Product Knowledge Questions**
Per-product understanding. Sourced from Atlas E (49 questions) + curated §19 questions.

Deduplication: Atlas E questions are REFERENCED by number. New questions test DIFFERENT aspects.

Example for RC:
- Atlas E: "If the coupon is above-market, what is the investor giving up in return?" (REFERENCE)
- New Beginner: "Draw the payoff diagram of an RC at maturity."
- New Intermediate: "How does the RC coupon change if implied vol increases?"
- New Advanced: "A client holds an RC with 6 months remaining and the stock is 5% above the barrier. What is the Delta of the embedded put?"
- New Expert: "Design an RC for a client who believes vol is overpriced but rates are rising. What strike, maturity, and barrier do you choose and why?"

**C. Structuring Logic Questions**
Decision framework, product selection, complexity governance, anti-patterns.

Boundary: These questions TEST the Solutions Manual framework. Answers REFERENCE SM sections.

Example:
- Beginner: "A retail client wants yield enhancement. What is the maximum product complexity you can recommend?"
- Intermediate: "Walk through the 10-step framework for a client who wants protected growth in a low-rate environment."
- Advanced: "A private banking client wants CMS spread income but the curve is flat. What do you recommend and why?"
- Expert: "Two competing proposals: Phoenix on single stock (16% coupon) vs WOAC on 3 stocks (24% coupon). The client is private banking. Which do you recommend? Justify using the decision framework."

**D. Case Interview Questions**
Client-facing scenarios with recommendations, trade-offs, rejected alternatives.

Boundary: SM has 40 scenarios. Interview cases present DIFFERENT client quotes testing SIMILAR logic. No scenario duplication.

Format per case:
```
CASE D.X — [Title]
Difficulty: [Beginner/Intermediate/Advanced/Expert]
Role: [Structuring/Trading/Sales/Risk/Model Val]

Client quote: "[2–3 sentence client need]"

Expected answer structure:
1. Identify objective
2. Narrow product set (cite framework steps)
3. Recommend with rationale
4. State rejected alternatives and why
5. Identify key risk

Scoring:
- Excellent: [criteria]
- Adequate: [criteria]
- Poor: [criteria]
```

**E. Desk-Specific Questions**
5 roles × 4 difficulty levels × ~6 questions each = ~30 questions.

| Role | Sample Question Types |
|------|---------------------|
| **Structuring** | "Design a product for...", "Why not X instead of Y?", "Client pushback on..." |
| **Trading** | "How do you hedge...", "P&L attribution on...", "Market moved — what happened to your book?" |
| **Sales** | "Explain X to a client with no derivatives background", "Client asks why coupon dropped", "Objection handling" |
| **Risk** | "What are the top 3 risks of...", "Design a stress test for...", "Limit breach — what do you do?" |
| **Model Val** | "What model do you use for...", "Calibration failed — diagnose", "Model limitation of..." |

### Difficulty Calibration

Mapped to Atlas Appendix G (learning difficulty) and product complexity:

| Difficulty | Product Complexity | Concept Depth | Expected Experience |
|:----------:|:-----------------:|:-------------:|:-------------------:|
| Beginner | 2–3 | Definition, construction | 0–1 years |
| Intermediate | 3–5 | Greeks, hedging, comparison | 1–3 years |
| Advanced | 5–7 | Cross-product, regime, P&L | 3–5 years |
| Expert | 7–10 | Correlation, path dependency, model choice | 5+ years |

---

## 8. Part 5: Mock Interview Tracks

### 5.1 Five Role-Specific Tracks

Each track: 5 rounds, escalating difficulty, 60 minutes total.

```
STRUCTURING TRACK (60 min)
Round 1 (10 min) — Product Knowledge: 5 rapid-fire Tier 1 answers
Round 2 (15 min) — Technical Deep-Dive: 2 products, Tier 2–3 depth
Round 3 (15 min) — Case Study: 1 client scenario, full 10-step walkthrough
Round 4 (10 min) — Comparison: 2 confusion pairs, differentiate
Round 5 (10 min) — Anti-Pattern Spotting: 3 "what's wrong?" scenarios

TRADING TRACK (60 min)
Round 1 (10 min) — Greeks Quiz: Delta, gamma, vega, rho for 5 products
Round 2 (15 min) — Hedging Scenario: "You just sold X to a client. How do you hedge?"
Round 3 (15 min) — P&L Attribution: "Your book moved $2M. Explain."
Round 4 (10 min) — Market Stress: "Vol spikes 5 points overnight. Walk through your book."
Round 5 (10 min) — Risk Limits: Limit breach + escalation procedure

SALES TRACK (60 min)
Round 1 (10 min) — Elevator Pitches: 5 products, 30 seconds each
Round 2 (15 min) — Client Matching: "Client profile X → recommend"
Round 3 (15 min) — Objection Handling: "Client says 'this is too risky/complex/expensive'"
Round 4 (10 min) — Comparison Selling: "Why Product A over Product B?"
Round 5 (10 min) — Suitability: Persona-based governance + know-your-product

RISK TRACK (60 min)
Round 1 (10 min) — Risk Identification: Name top 3 risks for 5 products
Round 2 (15 min) — Stress Test Design: Design scenario for a portfolio of 3 products
Round 3 (15 min) — Model Risk: "What can go wrong with this pricing model?"
Round 4 (10 min) — Limit Framework: "Set risk limits for a new product desk"
Round 5 (10 min) — Regulatory: Capital requirements, suitability, disclosure

MODEL VALIDATION TRACK (60 min)
Round 1 (10 min) — Pricing Model Identification: "What model for X?" × 5
Round 2 (15 min) — Calibration: "Surface doesn't fit. Diagnose."
Round 3 (15 min) — Numerical Methods: Monte Carlo, finite differences, tree methods
Round 4 (10 min) — Model Limitations: "When does Black-Scholes fail for X?"
Round 5 (10 min) — Back-Testing: "Predicted P&L vs actual — explain the gap"
```

### 5.2 Four Difficulty Progressions

Each track has 4 difficulty variants. Products used in each round scale with difficulty:

| Difficulty | Round 1 Products | Round 3 Case Complexity | Round 5 Depth |
|:----------:|:----------------:|:----------------------:|:-------------:|
| Beginner | SD, FWD, PPN, RC, IRS | Single-product, clear objective | 1 trap |
| Intermediate | Digital, CLN, Phoenix, CDS, VO | 2–3 candidates, trade-off required | 2 traps |
| Advanced | VarSwap, FTD, WOAC, NCRA, C.STEG | Cross-family, regime-dependent | 3 traps + regime |
| Expert | CDO, TARN STEG, NTD, DKIP, CRA SRT | Multi-asset, regulatory constraint | 3 traps + model risk |

### 5.3 Scoring Rubric

3-level rubric for each round:

| Score | Definition |
|:-----:|-----------|
| **Excellent** | Correct answer + trade-off awareness + unprompted depth (mentions risk not asked about, cites historical example, identifies edge case) |
| **Adequate** | Correct answer with reasoning. May miss one secondary point. |
| **Poor** | Incorrect, incomplete, or correct answer with wrong reasoning. |

Per-round scoring criteria specified in each mock track.

---

## 9. Part 6: Interview Traps & Anti-Patterns

### 6.1 Technical Traps (20)

Sourced from Matrix Appendix B (8 traps) + §20 Common Mistakes (curated) + new.

Format:
```
TRAP T.X — "[Trap Question]"
Difficulty: [Level]
The Naive Answer: [What most candidates say]
Why It's Wrong: [1–2 sentences]
The Correct Answer: [2–3 sentences]
Products Affected: [List]
```

Categories:
- Greeks traps (5): Delta ≠ probability, gamma at barrier, vega sign confusion, rho on notes vs swaps, theta/carry confusion
- Pricing traps (5): Convexity adjustment, correlation and wrong-way risk, digital pricing near strike, CMS rate ≠ forward rate, recovery assumption impact
- Structure traps (5): Protection ≠ risk-free, guaranteed coupon ≠ guaranteed principal, autocall = good for bank, yield source = risk source, complexity ≠ risk
- Market traps (5): Vol mean reversion assumption, correlation stability, curve shape persistence, spread-rate independence, liquidity in stress

### 6.2 Behavioral / Framing Traps (10)

Not technical — these test how candidates think under pressure.

- "Tell me a trade you would put on today" (tests conviction + reasoning, not the specific trade)
- "This product seems really risky. Convince me otherwise." (tests: don't deny risk — reframe as compensated risk)
- "Walk me through your thought process" (tests: structured framework vs rambling)
- "What would you do if the client insists on a product you think is unsuitable?" (tests: compliance awareness + diplomacy)
- "You have 30 seconds — pitch me this product" (tests: elevator clarity under pressure)
- Plus 5 more role-specific framing traps

---

## 10. Product Family Coverage

### Coverage Matrix

Every product appears in at least 2 sections:

| Product | Part 2 (Answer) | Part 3 (Comparison) | Part 4 (Question Bank) | Part 5 (Mock) | Part 6 (Trap) | Min Touches |
|---------|:---------------:|:-------------------:|:---------------------:|:-------------:|:-------------:|:-----------:|
| Top 10 products | Full 4-tier | 1+ pair | 4+ questions | In all tracks | 2+ traps | 6+ |
| Next 15 products | Full 3-tier | 0–1 pair | 2–3 questions | In 2+ tracks | 1 trap | 4+ |
| Remaining 24 products | Abbreviated | 0–1 pair | 1–2 questions | In 1+ track | 0–1 trap | 2+ |

### Family Balance

| Family | Products | Total Questions (Target) | Mock Track Presence |
|--------|:--------:|:------------------------:|:-------------------:|
| ELN | 15 | 55–65 | All 5 tracks |
| Swaps | 8 | 25–35 | Trading, Risk, MV |
| SRT | 5 | 15–20 | Structuring, Trading, Risk |
| STEG | 4 | 12–16 | Structuring, Sales, Risk |
| CLN | 5 | 18–24 | All 5 tracks |
| Other | 12 | 30–40 | All 5 tracks |

---

## 11. Buy-Side vs Sell-Side Coverage

### Sell-Side Focus (Default)

Structuring, trading, sales perspective. Product design and risk management.

### Buy-Side Additions

| Component | Buy-Side Angle |
|-----------|----------------|
| Part 1 | "What buy-side interviewers look for" — due diligence, hidden fee identification, counterparty risk assessment |
| Part 2 Tier 4 | "Why would you NOT buy this?" — investor perspective on structural disadvantages |
| Part 4 | 15 buy-side-specific questions (e.g., "Your PM wants to add WOAC to the portfolio. What due diligence do you perform?") |
| Part 5 | Buy-side variant for Risk track (portfolio risk, not desk risk) |
| Part 6 | 3 buy-side-specific traps (e.g., "Chasing yield without understanding the short option") |

---

## 12. Scalability

### Extensible Dimensions

| Dimension | Current | Extensible To |
|-----------|:-------:|:-------------:|
| Products | 49 | N (new products get 4-tier template) |
| Roles | 5 | N (new role = new mock track + desk questions) |
| Difficulty levels | 4 | 4 (Beginner–Expert is sufficient) |
| Question categories | 5 | N (new category = new question bank section) |

### Adding a New Product

Template cost: ~30 lines (4-tier answer + 2 questions + 1 comparison). No structural change.

### Adding a New Role

Template cost: ~60 lines (1 mock track + 6 desk questions + 2 traps). No structural change.

---

## 13. Line Budget

| Part | Estimated Lines | % of Total |
|------|:---------------:|:----------:|
| Part 1: Strategy Guide | 120 | 5% |
| Part 2: Answer Templates | 1,040 | 45% |
| Part 3: Comparisons | 200 | 9% |
| Part 4: Question Bank | 500 | 22% |
| Part 5: Mock Tracks | 250 | 11% |
| Part 6: Traps | 150 | 6% |
| Headers/ToC/Traceability | 50 | 2% |
| **Total** | **~2,310** | **100%** |

Within the 1,800–2,500 target range from execution plan.

---

## 14. Source Data Dependencies

| Source | What's Needed | How Used |
|--------|--------------|----------|
| Atlas Appendix E | 49 interview questions | REFERENCE in Part 4 (not reproduced) |
| Atlas Appendix F | 25 confusion pairs | REFERENCE in Part 3.2, expand top 10 in Part 3.1 |
| Atlas Appendix G | 49 learning difficulties | Difficulty calibration in Part 4 |
| Matrix Appendix A | 25 pairs with dimensions | Dimensional evidence for Part 3.1 |
| Matrix Appendix B | 10 priority products + 8 traps | Priority selection for Part 2 + traps for Part 6 |
| Matrix View 7 | Interview priority ranking | Product ordering in Part 2 |
| §1 per chapter | Explain Like I'm New | Tier 1 source |
| §11 per chapter | Formal Definition | Tier 2 source |
| §14 per chapter | Desk Reality | Tier 3 source |
| §15 per chapter | Risk Analysis | Trading/Risk questions |
| §19 per chapter | Knowledge Check (~343 Q) | Curate ~60 into Part 4 (not all 343) |
| §20 per chapter | Common Mistakes (~245) | Synthesize into Part 6 traps |
| Solutions Manual | 40 scenarios, 18 APs | REFERENCE ONLY — never reproduce |

---

## 15. Constraints

1. Atlas is FROZEN — complexity scores, family assignments, section numbers are fixed
2. Framework v1.3.1 is FROZEN — no new sections
3. Solutions Manual is FROZEN — reference only
4. No production artifact modification
5. All product data from Atlas + Registry + Taxonomy only
6. 49-product universe is fixed

---

*Interview System design complete. 2026-06-22.*
