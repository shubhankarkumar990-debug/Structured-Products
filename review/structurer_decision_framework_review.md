# Structurer Decision Framework Review

**Date:** 2026-06-22
**Purpose:** Validate decision framework teaches reasoning, not classification.
**Framework:** v1.3.1 (frozen)

---

## 1. Distinction: Classification vs Decision

### 1.1 What Already Exists (Classification)

Matrix Decision Trees 1–3 classify products by:
- Risk Appetite → Conservative / Moderate / Aggressive / Hedging
- Investment Objective → Income / Growth / Hedging / Synthetic Access / Volatility
- Experience Level → Beginner / Intermediate / Advanced / Specialist

These are TAXONOMIES. They answer: "Given trait X, which products have that trait?"

### 1.2 What's Missing (Decision)

A decision framework answers: "Given this COMBINATION of inputs, why is Product A better than Product B, and under what conditions does that ranking reverse?"

| Classification (exists) | Decision (missing) |
|------------------------|-------------------|
| "RC is a yield product" | "RC beats Digital when client is bullish, not range-bound" |
| "PPN is conservative" | "PPN is wrong when rates are low because participation drops below 40%" |
| "Phoenix is complexity 6" | "Phoenix beats RC when client accepts autocall risk for contingent income" |
| "CDO is specialist" | "CDO is the only product that provides leveraged exposure to a specific attachment point" |

### 1.3 The Gap

**Classification tells you WHAT a product is. Decision teaches you WHEN to use it and WHEN NOT to.**

The entire Solutions Manual exists to close this gap.

---

## 2. Framework Validation

### 2.1 Revised 9-Step Decision Flow

```
Step 1: OBJECTIVE CLASSIFICATION
        What does the client fundamentally want?
        → Protection / Yield / Income / Directional / Hedging / Vol

Step 2: CASH FLOW REQUIREMENT
        Does the client need periodic payments?
        → Growth (no) / Income (yes, fixed) / Contingent Income (yes, conditional)

Step 3: ASSET CLASS SELECTION
        Which market does the client have a view on?
        → Equity / Rates / Credit / Volatility / FX / Commodity / Multi-Asset

Step 4: MARKET REGIME ASSESSMENT
        What is the client's directional conviction?
        → Bullish / Bearish / Range-bound / No view / Steepening / Flattening

Step 5: RISK BUDGET DETERMINATION
        What is the maximum acceptable loss?
        → Zero (full protection) / Conditional (barrier) / Defined (premium) / Unlimited

Step 6: CONSTRAINT APPLICATION
        Apply hard constraints that eliminate products:
        → Liquidity / Maturity / Regulatory / Currency

Step 7: COMPLEXITY FILTER
        Cap product universe by client sophistication:
        → Simple (2-3) / Standard (4-5) / Complex (6-7) / Specialist (8-10)

Step 8: CANDIDATE SET IDENTIFICATION
        Products surviving Steps 1-7 (typically 3-8)

Step 9: COMPARATIVE SELECTION
        Why Product A over Product B from the candidate set
```

### 2.2 Step-by-Step Validation

| Step | Purpose | Can Be Skipped? | What It Eliminates |
|------|---------|:---------------:|-------------------|
| 1 | Primary filter | NO | Entire families (e.g., "Hedging" eliminates all ELN) |
| 2 | Income/Growth split | NO | Growth path eliminates coupon products; Income path eliminates PPN/Booster |
| 3 | Asset class | NO | Equity view eliminates STEG/SRT; Credit view eliminates ELN |
| 4 | Direction | NO | Bullish eliminates range products; Range eliminates directional |
| 5 | Risk budget | NO | Zero loss eliminates all conditional products |
| 6 | Constraints | YES if none | Liquidity eliminates exotic/illiquid |
| 7 | Complexity | NO | Complexity 3 cap eliminates 37 of 49 products |
| 8 | Narrowing | Automatic | Output of Steps 1-7 |
| 9 | Selection | NO | This is where structurer judgment lives |

**Mandatory steps: 1, 2, 3, 4, 5, 7, 9 (7 of 9)**
**Optional step: 6 (constraints may not apply)**
**Automatic step: 8 (computed from above)**

### 2.3 Framework Walk-Through: Two Paths, Same Starting Point

**Client says: "I want yield enhancement on equities."**

**Path A: Bullish, moderate risk, simple**
1. Objective: Yield → Yield Enhancement category
2. Cash Flow: Income (wants coupon) → Coupon products
3. Asset Class: Equity → ELN family
4. Market Regime: Bullish → Directional products preferred
5. Risk Budget: Conditional (accepts barrier risk) → RC/DRC/Bonus eligible
6. Constraints: None
7. Complexity: Simple (max 4) → RC(3), DRC(3), Bonus(4)
8. Candidates: RC, DRC, Bonus
9. Selection: **RC** — simplest, client is bullish so barrier unlikely to breach, fixed coupon meets income need

**Path B: Range-bound, moderate risk, intermediate complexity**
1. Objective: Yield → Yield Enhancement category
2. Cash Flow: Income (wants coupon) → Coupon products
3. Asset Class: Equity → ELN family
4. Market Regime: Range-bound → Digital/Range products preferred
5. Risk Budget: Conditional (accepts limited downside) → Digital/CRA eligible
6. Constraints: None
7. Complexity: Standard (max 6) → Digital(4), CRA ELN(6), DKIP(7 — exceeds cap)
8. Candidates: Digital, CRA ELN
9. Selection: **Digital** if simple range view; **CRA ELN** if client has range accrual tolerance and wants higher coupon

**Same starting point, different products.** The framework forces the divergence at Step 4 (Market Regime).

---

## 3. Market Regime Sensitivity

### 3.1 How Regime Changes Recommendations

The same client objective produces different products under different market conditions. This is the HARDEST part of structuring and must be explicitly taught.

| Objective | High Vol, Low Rates | Low Vol, High Rates | Rising Rates | Falling Rates |
|-----------|--------------------|--------------------|-------------|---------------|
| Protection + Growth | PPN (poor — low participation) → consider Airbag | PPN (good — high participation) | PPN worse (ZCB more expensive) | PPN better (cheaper ZCB) |
| Yield Enhancement | RC (good — high premium) | RC (poor — low premium). Consider STEG | Short-duration RC | Long-duration RC |
| Income | Phoenix (good — high contingent coupon) | Phoenix (poor — low coupon). Consider STEG | STEG attractive (curve steep) | STEG unattractive (curve flat) |
| Credit | CLN spreads wide (high premium) | CLN spreads tight (low compensation) | — | — |

### 3.2 Regime-Product Sensitivity Matrix

Must be included in Part 1 of Solutions Manual. Shows which products benefit/suffer in each regime.

| Regime | Benefits | Suffers |
|--------|----------|---------|
| High equity vol | RC/Phoenix (rich premiums), VarSwap long | PPN (option expensive), WOAC (barrier risk) |
| Low equity vol | PPN (cheap option = good participation) | RC/Phoenix (thin premiums) |
| Steep yield curve | STEG (wide CMS spread), IR Callable | Flat-rate products |
| Flat yield curve | Fixed-rate products | STEG (zero spread coupon) |
| Wide credit spreads | CLN (high premium), CDS protection seller | CDS protection buyer (expensive) |
| Tight credit spreads | CDS protection buyer (cheap) | CLN (low premium) |

---

## 4. Comparative Selection Logic (Step 9)

### 4.1 What Step 9 Must Teach

Step 9 is where classification ENDS and decision BEGINS. Given 3–8 candidates, the structurer must evaluate:

| Comparison Dimension | Question Answered |
|---------------------|-------------------|
| **Payoff shape** | Which payoff best matches client's market view? |
| **Cost of protection** | How much upside/yield does each product sacrifice for its protection level? |
| **Path dependency** | Does the client understand and accept monitoring risk? |
| **Complexity premium** | Does the more complex product offer enough extra value to justify the step up? |
| **Hedge cost to desk** | Which product is cheaper for the desk to hedge → better client terms? |
| **Secondary market** | Can the client exit if needed? At what cost? |

### 4.2 Example: RC (3) vs Phoenix (6) vs Digital (4)

All three serve "yield enhancement on equity." How to choose:

| Dimension | RC (3) | Phoenix (6) | Digital (4) |
|-----------|--------|-------------|-------------|
| Coupon | Fixed, above-market | Contingent, higher if paid | Digital: all-or-nothing |
| Protection | Strike barrier | Observation barrier + autocall | Full principal (100%) |
| Path dependency | No (European) | Yes (periodic observations) | No (European digital) |
| Best market | Mildly bullish | Range-bound to mildly bullish | Range-bound |
| Worst scenario | Stock falls through barrier | Stock falls through barrier + no coupons | Stock below digital → zero coupon |
| Complexity | Simplest | Moderate | Low |

**Decision rule:** Use RC when bullish with moderate risk tolerance. Use Digital when range-bound and client needs principal safety. Use Phoenix when client accepts path risk for higher potential coupon + autocall chance.

---

## 5. Integration with Atlas/Matrix

### 5.1 Source Data Flow

```
Atlas DNA Cards → Product features (inputs to Step 3, 5, 7)
Matrix Part 1-3 → Comparison dimensions (inputs to Step 9)
Matrix Decision Trees → Classification skeleton (Steps 1-3)
Atlas Complexity Scores → Complexity Filter (Step 7)
Dependency Graph Tiers → Learning prerequisites
§3 per chapter → Per-product client need (ground truth for scenarios)
§8 per chapter → Client perspective (scenario context)
```

### 5.2 What the Solutions Manual ADDS Beyond These Sources

| Source | What It Provides | What Solutions Manual Adds |
|--------|-----------------|---------------------------|
| §3 per chapter | "This product solves X" (per-product) | "Given problem X, choose between A, B, C" (cross-product) |
| §8 per chapter | "Client sees this product as Y" (per-product) | "Client with need Y should consider Z instead of W" (comparative) |
| Matrix Decision Trees | "Products classified by trait" (taxonomy) | "Why Product A beats Product B for this client" (reasoning) |
| Matrix Views | "Products with trait X" (filtered lists) | "Trade-offs between products in this list" (selection logic) |

---

## 6. Structural Decision

### 6.1 Recommended Part 1 Structure

```
Part 1: Structurer Decision Framework

  1.1 The 9-Step Decision Model
      - Visual: flow diagram specification
      - Each step: definition, inputs, outputs, decision logic
      
  1.2 Market Regime Awareness
      - 6 regimes × product impact matrix
      - When to deviate from default recommendations
      
  1.3 Complexity Escalation Protocol
      - The Complexity Ladder principle
      - 3 worked escalation examples (Protection, Yield, Rates)
      
  1.4 The Structurer's Anti-Instincts
      - 5 cases where the "obvious" choice is wrong
      - Why experience matters more than classification
```

**Estimated size: 250–350 lines.** Concise. Every sentence teaches a decision, not describes a product.

### 6.2 Relationship to Part 2 (Scenarios)

Each scenario in Part 2 is a WORKED EXAMPLE of the 9-step model:
- Steps 1–7 shown as the narrowing process
- Step 8 shows the candidate set
- Step 9 shows the comparative selection with reasoning

The reader should be able to apply the Part 1 framework to ANY client situation, not just the 40 scenarios in Part 2.

---

## 7. Verdict

### Does the framework teach decisions, not matching?

| Criterion | Assessment |
|-----------|-----------|
| Multiple inputs considered simultaneously | YES — 9 steps, 5 mandatory |
| Same objective → different products under different conditions | YES — market regime sensitivity |
| "Why NOT" reasoning included | YES — anti-patterns + comparative selection |
| Complexity governance enforced | YES — escalation protocol |
| Cross-product comparison taught | YES — Step 9 comparative selection |
| Not reducible to lookup table | YES — combination explosion prevents simple mapping |

**PASS.** Framework teaches structuring decisions. Ready for integration into Solutions Manual Part 1.

---

*Structurer Decision Framework review complete. 2026-06-22.*
