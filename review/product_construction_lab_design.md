# Product Construction Lab — Design Review

**Date:** 2026-06-21
**Proposed Section:** Part 1.11 — Product Construction Lab
**Framework:** v1.3.1 (FROZEN)
**Purpose:** Assess design for hands-on product decomposition and construction teaching
**Implementation:** After 49/49, during harmonization

---

## 1. Concept

Section 2.2 (Product Construction Principles) teaches decomposition *theory* — what components are and how they combine. The Product Construction Lab provides *practice* — the reader builds 8 products from scratch, seeing how each component contributes to the final payoff and coupon.

**Distinction from 2.2:**

| Aspect | Section 2.2 (existing) | Section 1.11 (proposed) |
|--------|:----------------------:|:----------------------:|
| Focus | Theory: what decomposition is | Practice: build products step by step |
| Depth | 1 example (RC) | 8 products across 5 families |
| Reader action | Read and understand | Follow along, predict, verify |
| Output | Conceptual understanding | Ability to decompose any product |

---

## 2. Recommended Placement

**Section 1.11** — after Section 1.10 (Payoff Chart Masterclass), closing Part 1.

**Rationale:** Reader has learned all building blocks (1.1-1.9), learned to read payoff charts (1.10), and now assembles the pieces into products (1.11). Part 2 then teaches the desk context (lifecycle, booking, systems). Part 5 applies everything to specific products.

**Learning arc:**
```
Part 1.1-1.9: What are the pieces?
Part 1.10:    How do I read the diagrams?
Part 1.11:    How do the pieces fit together? ← NEW
Part 2:       How does the desk work?
Part 5:       Here are all 49 products
```

---

## 3. Dependencies

| Prerequisite | Section | Why Needed |
|-------------|---------|-----------|
| Options (calls, puts, strikes) | 1.2 | Core building block |
| Barriers (KI, KO) | 1.3 | Discontinuous components |
| Digital payoffs | 1.3 | Step-function components |
| Greeks (sensitivity) | 1.4 | Understanding risk transfer |
| Correlation (baskets) | 1.6 | Multi-asset construction |
| Credit (CDS, defaults) | 1.9 | Credit-linked construction |
| Payoff chart literacy | 1.10 | Reading construction diagrams |

---

## 4. Learning Objectives

| # | Objective |
|:-:|-----------|
| 1 | Decompose any structured product into Bond + Derivative(s) + FTP + Margin |
| 2 | Identify which derivative generates the enhanced coupon |
| 3 | Calculate the approximate coupon from component values |
| 4 | Explain why the coupon is not "free money" — trace it to risk transfer |
| 5 | Recognize common construction patterns across product families |
| 6 | Predict the payoff shape from the component list |
| 7 | Understand how basket construction differs from single-name construction |
| 8 | Understand how credit-linked construction differs from equity-linked |

---

## 5. Section Structure — 8 Product Builds

### 5.1 Build 1: PPN (Complexity 2)

| Step | Component | Value | Purpose |
|:----:|-----------|:-----:|---------|
| 1 | Bond (zero-coupon) | 95% | Capital protection — returns to 100% at maturity |
| 2 | Call option (at-the-money) | 5% | Upside participation funded by bond discount |
| 3 | FTP | -0.3% | Bank's funding cost |
| 4 | Margin | -0.2% | Bank's profit |
| **Result** | PPN with ~90% participation | | Capital protected, capped upside |

**Teaching point:** The participation rate is not a design choice — it is whatever the remaining budget can buy after bond and costs.

### 5.2 Build 2: RC (Complexity 3)

| Step | Component | Value | Purpose |
|:----:|-----------|:-----:|---------|
| 1 | Bond | 2.0% coupon | Baseline interest |
| 2 | Short KI put (70% barrier) | +5.5% premium | Risk transfer — investor sells protection |
| 3 | FTP | -0.5% | |
| 4 | Margin | -0.5% | |
| **Result** | RC paying 6.5% coupon | | Enhanced coupon from put sale |

**Teaching point:** The 6.5% coupon comes from the investor accepting downside risk below the barrier. The bank passes through most of the option premium as coupon.

### 5.3 Build 3: Phoenix Autocallable (Complexity 6)

| Step | Component | Value | Purpose |
|:----:|-----------|:-----:|---------|
| 1 | Bond (conditional) | 1.5% base | Baseline |
| 2 | Short KI put (60% barrier) | +3.0% | Downside risk transfer |
| 3 | Autocall feature (at-the-money) | +2.5% | Early termination risk |
| 4 | Memory coupon feature | +1.0% | Deferred coupon risk |
| 5 | FTP | -0.5% | |
| 6 | Margin | -0.5% | |
| **Result** | Phoenix paying 7.0% conditional | | Multi-feature construction |

**Teaching point:** Each feature adds premium but also adds risk to the investor. The autocall and memory features make this product path-dependent — the coupon depends on what happened *during* the product's life, not just at maturity.

### 5.4 Build 4: IRS (Complexity 3)

| Step | Component | Value | Purpose |
|:----:|-----------|:-----:|---------|
| 1 | Fixed leg | 3.0% | One party pays fixed |
| 2 | Floating leg | SOFR + spread | Other party pays floating |
| 3 | No bond — unfunded | 0 | No principal exchange |
| **Result** | Plain vanilla IRS | | Exchange of cash flows |

**Teaching point:** A swap has no embedded option. It is a pure exchange. The "cost" is opportunity cost — if rates move against you, you pay more than you receive. No premium, no upfront payment (at inception, NPV = 0).

### 5.5 Build 5: CLN (Complexity 4)

| Step | Component | Value | Purpose |
|:----:|-----------|:-----:|---------|
| 1 | Bond | 2.5% coupon | Baseline interest |
| 2 | Short CDS (credit protection sold) | +3.5% | Credit risk transfer |
| 3 | FTP | -0.3% | |
| 4 | Margin | -0.2% | |
| **Result** | CLN paying 5.5% | | Bond + credit derivative |

**Teaching point:** The CLN construction parallels the RC — both involve the investor selling protection (put or CDS) and receiving premium as enhanced coupon. The difference: RC sells equity downside risk, CLN sells credit default risk.

### 5.6 Build 6: FTD (Complexity 7)

| Step | Component | Value | Purpose |
|:----:|-----------|:-----:|---------|
| 1 | Bond | 2.5% | Baseline |
| 2 | Short basket CDS (5 names, first-to-default) | +7.5% | Basket credit risk |
| 3 | FTP | -0.3% | |
| 4 | Margin | -0.7% (higher — complex) | |
| **Result** | FTD paying 9.0% | | Single-name → basket amplification |

**Teaching point:** The jump from CLN (3.5% CDS premium) to FTD (7.5% basket premium) comes from basket mechanics — the probability that *at least one* of 5 names defaults is much higher than a single name. The investor is paid for basket risk, not lower credit quality.

### 5.7 Build 7: NTD (Complexity 8)

| Step | Component | Value | Purpose |
|:----:|-----------|:-----:|---------|
| 1 | Bond | 2.5% | Baseline |
| 2 | Short basket CDS (5 names, 2nd-to-default) | +3.0% | 2nd-default risk (lower than FTD) |
| 3 | FTP | -0.3% | |
| 4 | Margin | -0.5% | |
| **Result** | 2TD paying 4.7% | | Lower coupon = lower trigger probability |

**Teaching point:** Compare FTD (9.0%) vs 2TD (4.7%). The difference is the trigger threshold. The investor is protected against the first default. But correlation reversal means this protection is not as simple as it appears at extreme correlation levels.

### 5.8 Build 8: Synthetic CDO Mezzanine (Complexity 10)

| Step | Component | Value | Purpose |
|:----:|-----------|:-----:|---------|
| 1 | Collateral (cash deposit) | 100% notional | Funds the tranche |
| 2 | Short tranche CDS (3-7% of 100-name portfolio) | +8.0% | Mezzanine credit risk |
| 3 | Subordination (0-3% equity tranche below) | Protection | First 3% of losses absorbed by equity |
| 4 | FTP | -0.3% | |
| 5 | Margin | -0.7% | |
| **Result** | Mezzanine paying 7.0% | | Tranched portfolio construction |

**Teaching point:** The mezzanine tranche earns less than the equity tranche (25%+) because it has subordination protection. It earns more than senior (2.5%) because it has less subordination. The *same portfolio* produces different products by changing attachment/detachment points.

---

## 6. Cross-Product Construction Patterns

| Pattern | Products Using It | Key Insight |
|---------|:-----------------:|------------|
| Bond + short option = enhanced coupon | PPN, RC, Phoenix | Coupon funded by selling optionality |
| Unfunded exchange = swap | IRS | No bond wrapper, pure cash flow exchange |
| Bond + short CDS = credit coupon | CLN, FTD, NTD | Coupon funded by selling credit protection |
| Tranched portfolio = layered risk | Synthetic CDO | Same portfolio, different risk slices |

---

## 7. Estimated Length

| Metric | Value |
|--------|:-----:|
| Word count | ~4,500 |
| Pages (est.) | 10-12 |
| Visual assets | 8-10 (one construction waterfall per product build) |
| Tables | 8 (one per build) + 1 pattern summary |
| Knowledge Check | Yes (3 construction exercises) |

---

## 8. Visual Requirements

| # | Visual | Type | Purpose |
|:-:|--------|------|---------|
| 1 | PPN construction waterfall | Waterfall | Bond discount → call option → costs → participation |
| 2 | RC construction waterfall | Waterfall | Bond + put premium → costs → coupon |
| 3 | Phoenix construction waterfall | Waterfall | Multiple features stacking |
| 4 | IRS construction (symmetric) | Flow | Fixed ↔ floating exchange |
| 5 | CLN construction waterfall | Waterfall | Bond + CDS → costs → coupon |
| 6 | FTD construction (CLN → basket) | Comparison | Single-name vs basket premium |
| 7 | NTD construction (FTD → 2TD) | Comparison | Trigger threshold effect on coupon |
| 8 | CDO construction (portfolio → tranches) | Structure | Portfolio slicing into tranches |
| 9 | Cross-product pattern chart | Summary | All 4 patterns side by side |

---

## 9. Interaction with Existing Content

| Interaction | Detail |
|------------|--------|
| **Extends 2.2** | Section 2.2 teaches theory with 1 example (RC). Section 1.11 provides 8 practice builds. No conflict — complementary |
| **References 1.2-1.9** | Each build references the building block section where the component was taught |
| **Forward to Part 5** | Each build previews the full product chapter: "For the complete analysis, see Section 5.x.y" |
| **Supports front matter** | Construction Lab is a key learning path milestone for Structurer and Desk Analyst paths |

**No existing chapter modifications required.**

---

## 10. Assessment

| Criterion | Score |
|-----------|:-----:|
| Educational impact | **VERY HIGH** — transforms passive reading into active construction |
| Effort | **MEDIUM** — ~4,500 words, 9 visuals, builds on existing content |
| Publication value | **HIGH** — differentiates Desk Bible from other references |
| Reader value | **VERY HIGH** — single most valuable skill for structured products understanding |
| Risk | **LOW** — additive, no modifications to existing content |

**Recommendation: PROCEED.** Highest-priority educational enhancement after Payoff Chart Masterclass.

---

*Product Construction Lab Design Review completed 2026-06-21.*
