# Practitioner Knowledge Gap Analysis

**Audit Phase**: 10-11 — Practitioner Knowledge, Quantitative Methods, Regulatory
**Scope**: Desk Bible v2 (22,620 lines, 49 products, 1,078 sections)
**Date**: 2026-06-25
**Verdict**: PARTIAL — concepts well covered, desk vocabulary and advanced methods absent

---

## 1. Executive Summary

The Desk Bible teaches WHAT a practitioner thinks about — Greeks, hedging, risks, payoffs — but not the operational LANGUAGE of the desk. Terms like "flow book," "exotic book," "risk warehouse," "internal hedge," and "external hedge" are either absent or mentioned once. A reader joining a structured products desk would understand the concepts but struggle with the daily vocabulary. Similarly, quantitative methods beyond Black-Scholes and Monte Carlo are absent. The Bible knows that models exist; it does not explain the practitioner's choice between them. Regulatory coverage is thin outside Basel and suitability.

---

## 2. Greeks and Positioning Language

### 2.1 Term Frequency

| Term | Count | Assessment |
|------|------:|------------|
| Long Gamma | 1 | Used but not defined as a concept |
| Short Gamma | 1 | Used but not defined as a concept |
| Long Vega | 10 | Used in context — readers can infer meaning |
| Short Vega | 23 | More frequently used (sellers of optionality are short vega) |
| Long Correlation | 7 | Used in multi-asset context |
| Short Correlation | 12 | Used appropriately (worst-of structures are short correlation) |
| Delta Neutral | 1 | Concept used extensively, term itself appears once |
| Delta Hedging | 7 | Covered in §2.7 and product chapters |

### 2.2 Analysis

The Bible USES Greeks positioning language correctly. "Short vega" appears 23 times — almost exclusively in §14 Desk Reality sections. This is good: it means the practical trading perspective naturally invokes these terms. But the terms are never DEFINED.

**The gap**: A reader encountering "the desk is short gamma on this product" for the first time would need external reference to understand what this means operationally. The Bible assumes familiarity with:

| Concept | Used In Bible? | Defined In Bible? | Gap |
|---------|:--------------:|:------------------:|-----|
| "Long/short gamma" as a position description | Yes (2 times) | No | Reader must know this already |
| "Long/short vega" as a position description | Yes (33 times) | No | High-frequency use without definition |
| "Long/short correlation" | Yes (19 times) | No | Complex concept used without explanation |
| "Delta neutral" as a hedging state | Yes (1 time) | No | Foundational concept barely named |

**Recommendation**: Part 2 §2.7 (Hedging) should include a section defining Greeks positioning language. This is ~2 pages of content and would eliminate the assumption gap.

---

## 3. Desk Vocabulary and Organization

### 3.1 Term Frequency

| Term | Count | Assessment |
|------|------:|------------|
| Internal Hedge | 0 | **ABSENT** — hedging within the bank's own books |
| External Hedge | 0 | **ABSENT** — hedging in the market |
| Risk Warehouse | 0 | **ABSENT** — the concept of warehousing risk before hedging |
| Flow Book | 1 | Single mention — should be a defined concept |
| Exotic Book | 0 | **ABSENT** — the book where complex products sit |
| Prop Book | 0 | Absent |
| Hedge Book | 0 | Absent |
| Back Book | 0 | Absent — the existing portfolio vs new flow |
| Run (as in "the desk runs") | 0 | Absent — "running a book" as desk vocabulary |

### 3.2 Analysis

This is the most revealing gap in practitioner coverage. The Bible teaches 49 products in detail. It never explains how a desk ORGANIZES those products.

**Operational reality**:
- A structured products desk maintains multiple books: flow (vanilla hedges), exotic (complex products), and potentially segregated books by product family
- Trades are internally hedged (risk transferred between books within the bank) before being externally hedged (in the market)
- The desk "warehouses" risk — accumulating positions before hedging in aggregate
- The distinction between flow and exotic is fundamental to how traders, risk managers, and Product Control interact with the portfolio

**Bible's silence**: None of this organizational framework appears. The Bible treats each product as an independent entity. It never explains that a worst-of autocallable sits in the exotic book, that its delta and vega are internally hedged against the flow book, and that residual correlation risk is warehoused.

**Impact**: A reader understands each product. They do not understand how the desk OPERATES as a business. This is the gap between product knowledge and desk knowledge.

---

## 4. Risk Concepts

### 4.1 Term Frequency

| Term | Count | Assessment |
|------|------:|------------|
| Residual Risk | 11 | Adequately covered |
| Basis Risk | 37 | Well covered — central to hedging discussions |
| Pin Risk | 11 | Well covered — particularly for barrier products |
| Gap Risk | 8 | Adequately covered |
| Jump Risk | 1 | Mentioned but not fully developed |
| Gamma Risk | 3 | Underrepresented given its importance |
| Tail Risk | — | Present conceptually, not measured |
| Wrong-Way Risk | — | Present in credit context |

### 4.2 Analysis

Risk concepts are generally well covered. Basis risk (37 mentions) reflects the Bible's strength in explaining WHY hedging is imperfect. Pin risk (11 mentions) appears in barrier product contexts where it matters most.

**Gaps within the coverage**:

| Risk Concept | Conceptual Coverage | Quantification | Mitigation Strategy |
|--------------|:-------------------:|:--------------:|:-------------------:|
| Basis risk | 8/10 | 3/10 | 5/10 |
| Pin risk | 7/10 | 2/10 | 4/10 |
| Gap risk | 6/10 | 1/10 | 3/10 |
| Jump risk | 2/10 | 0/10 | 1/10 |
| Gamma risk | 3/10 | 1/10 | 2/10 |

The pattern: risks are NAMED and their CAUSE is explained. How to MEASURE and MANAGE them is not covered systematically.

---

## 5. Quantitative Methods

### 5.1 Term Frequency — Pricing Models

| Term | Count | Assessment |
|------|------:|------------|
| Monte Carlo | 30 | Well covered conceptually — mentioned as primary simulation method |
| Black-Scholes | 18 | Well covered — limitations discussed |
| Local Vol | 4 | Mentioned, not explained as a model choice |
| Stochastic Vol | 2 | Mentioned in passing |
| PDE | 0 | **ABSENT** — Partial Differential Equation methods |
| Finite Difference | 0 | **ABSENT** — numerical PDE solution method |
| Binomial Tree | 0 | **ABSENT** — foundational lattice method |
| Hull-White | 0 | **ABSENT** — standard interest rate model |
| SABR | 0 | **ABSENT** — standard vol smile model |
| Heston | 0 | **ABSENT** — standard stochastic vol model |

### 5.2 Term Frequency — Quantitative Concepts

| Term | Count | Assessment |
|------|------:|------------|
| Calibration | 13 | Concept covered — model calibration to market |
| Convexity Adjustment | 14 | Well covered — important for rate products |
| Replication | 16 | Well covered — static replication arguments |
| Log Contract | 1 | Single mention — variance swap replication |
| Quanto | 8 | Concept covered — FX adjustment for non-domestic payoffs |
| Correlation Smile | 3 | Mentioned — correlation surface dynamics |

### 5.3 Analysis — The Model Choice Gap

The Bible presents Monte Carlo and Black-Scholes as if they are the only methods. In practice, a quant or sophisticated trader must choose between:

| Method | When Used | Bible Coverage |
|--------|-----------|:--------------:|
| Black-Scholes analytic | Vanillas, simple Europeans | Covered (18 mentions) |
| Monte Carlo simulation | Path-dependent, multi-asset | Covered (30 mentions) |
| PDE / Finite Difference | American options, early exercise | ABSENT |
| Binomial/Trinomial Trees | American options, convertibles | ABSENT |
| Local Volatility (Dupire) | Barrier options, smile-consistent | Named (4 mentions), not explained |
| Stochastic Volatility (Heston, SABR) | Smile dynamics, forward smile | Named (2 mentions), not explained |
| Hull-White | Interest rate products | ABSENT |
| SABR | Swaption/caplet vol smile | ABSENT |

**Impact**: The Bible's quant coverage is appropriate for a Structurer or Trader who needs to understand what models do, not how they work internally. It is NOT appropriate for a Quant, a Model Validator, or anyone who needs to choose between models.

### 5.4 The Calibration Gap

Calibration is mentioned 13 times — the concept that model parameters must be fit to market data. But the Bible never explains:

| Gap | Operational Reality | Bible Coverage |
|-----|---------------------|----------------|
| What is calibrated | Vol surface, correlation matrix, rate curves, recovery rates | Implied but not systematic |
| Calibration instruments | Vanillas used to calibrate exotic models | ABSENT |
| Calibration frequency | Daily, weekly, or event-driven recalibration | ABSENT |
| Calibration stability | The tension between fitting today's market and stability over time | ABSENT |
| Calibration failure | What happens when the model cannot fit the market | ABSENT |

---

## 6. Regulatory Coverage

### 6.1 Term Frequency

| Term | Count | Assessment |
|------|------:|------------|
| Suitability | 105 | Extensively covered — central to product governance |
| Basel | 31 | Well covered — capital framework |
| Central Clearing | 16 | Adequately covered |
| MiFID | 5 | Mentioned — not detailed |
| PRIIPs | 2 | Mentioned — not detailed |
| KID | 2 | Mentioned — Key Information Document |
| Product Governance | 3 | Minimal |
| SRI (Summary Risk Indicator) | 0 | Absent — required for PRIIPs KID |
| Appropriateness | 0 | **ABSENT** — distinct from suitability |
| Target Market | 0 | **ABSENT** — MiFID II product governance requirement |
| EMIR | 0 | **ABSENT** — derivatives regulation |
| Dodd-Frank | 0 | **ABSENT** — US derivatives regulation |
| UMR (Uncleared Margin Rules) | 0 | **ABSENT** — bilateral margin requirements |
| Best Execution | 0 | **ABSENT** — MiFID II obligation |

### 6.2 Analysis

The Bible's regulatory coverage has a clear shape:

**Strong**: Suitability (105 mentions) — the Bible treats suitability as a per-product attribute, consistently covered in every chapter. This is excellent for Structurers and Sales who need to assess product appropriateness for clients.

**Adequate**: Basel (31 mentions), Central Clearing (16 mentions) — capital and clearing are discussed where they affect product design and economics.

**Weak**: Everything else. The major European and US regulatory frameworks for derivatives (MiFID II, EMIR, Dodd-Frank) are barely mentioned or absent. For a desk operating in a regulated environment, this is a gap.

| Regulatory Domain | Coverage Level | Risk |
|-------------------|:--------------:|------|
| Product suitability | 9/10 | Low |
| Capital requirements | 5/10 | Medium |
| Clearing obligations | 4/10 | Medium |
| Product governance (MiFID II) | 1/10 | High |
| Derivatives regulation (EMIR/DF) | 0/10 | High |
| Margin requirements (UMR) | 0/10 | High |
| Best execution | 0/10 | Medium |
| Investor documentation (PRIIPs) | 1/10 | Medium |

### 6.3 The Appropriateness vs Suitability Gap

The Bible uses "suitability" 105 times. "Appropriateness" appears 0 times. Under MiFID II, these are distinct concepts:

- **Suitability**: Applies to advised sales — the product must be suitable for the specific client's objectives, risk tolerance, and knowledge
- **Appropriateness**: Applies to non-advised (execution-only) sales — the client must have sufficient knowledge and experience

The Bible conflates these or ignores the distinction. For Sales and Compliance professionals, this is a regulatory gap.

---

## 7. Practitioner Vocabulary Gap Summary

The following terms represent the daily operating language of a structured products desk. None are adequately covered:

| Term | Count | What It Means | Why It Matters |
|------|------:|---------------|----------------|
| Internal Hedge | 0 | Risk transfer between books within the bank | Fundamental to how desks manage risk |
| External Hedge | 0 | Risk transfer to the market | Distinguishes internal from market-facing activity |
| Risk Warehouse | 0 | Accumulating risk before hedging in aggregate | Core desk strategy for managing flow |
| Flow Book | 1 | Book for liquid, vanilla hedging instruments | Organizational structure of every desk |
| Exotic Book | 0 | Book for complex structured products | Where the products in this Bible sit |
| Back Book | 0 | Existing portfolio (vs new flow) | Critical for P&L attribution and risk management |
| Axe | 0 | Desired trade direction (what the desk wants to do) | Daily trading vocabulary |
| Skew | — | Vol skew as a trading concept | Discussed in vol context, not as desk language |
| Sticky Strike / Sticky Delta | 0 | Vol dynamics models used for hedging decisions | ABSENT — daily quant/trader vocabulary |

---

## 8. Coverage Scorecard

| Domain | Score | Evidence |
|--------|:-----:|----------|
| Greeks concepts | 8/10 | Extensively used in §14 Desk Reality sections |
| Greeks positioning language | 3/10 | Used but never defined ("long gamma", "short vega") |
| Hedging approach | 7/10 | Part 2 §2.7 + per-product §14 coverage |
| Desk vocabulary | 1/10 | Flow/exotic/warehouse/axe — almost entirely absent |
| Risk concepts | 7/10 | Basis risk, pin risk, gap risk well covered |
| Risk quantification | 2/10 | Risks named, rarely measured |
| Quantitative methods (basic) | 6/10 | Black-Scholes, Monte Carlo adequately covered |
| Quantitative methods (advanced) | 0/10 | PDE, trees, SABR, Heston, Hull-White all absent |
| Model selection guidance | 1/10 | Models mentioned, choice framework absent |
| Regulatory framework | 3/10 | Suitability strong, everything else weak to absent |
| Suitability | 9/10 | 105 mentions, consistently per-product |
| Post-trade regulatory (EMIR, UMR) | 0/10 | Absent |

---

## 9. Audience Impact Assessment

| Role | Can learn practitioner vocabulary from the Bible? | Assessment |
|------|---------------------------------------------------|------------|
| Structurer | Mostly — understands products, partially understands desk dynamics | 7/10 |
| Trader | Partially — understands products and hedging, missing desk organization vocabulary | 5/10 |
| Quant | No — model choice framework absent, advanced methods absent | 3/10 |
| Sales | Partially — suitability well covered, regulatory framework weak | 5/10 |
| Risk Manager | Partially — risk concepts present, risk infrastructure vocabulary absent | 4/10 |
| Compliance | No — regulatory framework outside suitability is absent | 2/10 |

---

## 10. Recommendation

The practitioner knowledge gap has three distinct components requiring different solutions:

### 10.1 Quick Fix — Greeks and Desk Vocabulary Glossary
Add a 5-10 page section to Part 2 defining: long/short gamma/vega/correlation, flow book/exotic book, internal/external hedge, risk warehouse, delta neutral hedging, sticky strike/delta. This is low effort, high impact.

### 10.2 Medium Fix — Quantitative Methods Overview
Add a 15-20 page chapter covering: model choice framework (when to use MC vs PDE vs trees), vol model comparison (LV vs SV vs SABR), rate model basics (Hull-White, short rate models), calibration process. Target audience: Traders and Structurers who need to understand model choices without being Quants.

### 10.3 Full Fix — Regulatory Framework
Add a 20-30 page chapter covering: MiFID II product governance, EMIR clearing and margin, PRIIPs/KID requirements, Best Execution, UMR for bilateral derivatives. This is substantial content but essential for operational completeness.

**Total estimated additional content**: 40-60 pages across all three components.

See infrastructure_handbook_recommendation.md for how these fit into the overall recommendation.
