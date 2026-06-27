# Solutions Manual Design Review

**Date:** 2026-06-22
**Purpose:** Validate design teaches structuring DECISIONS, not product matching.
**Framework:** v1.3.1 (frozen)

---

## 1. Input Analysis — What Determines Product Selection?

### 1.1 Complete Input Inventory

| # | Input | Type | Source |
|:-:|-------|:----:|--------|
| 1 | Client objective | Mandatory | Client brief |
| 2 | Capital protection requirement | Mandatory | Investment mandate / risk tolerance |
| 3 | Risk budget | Mandatory | Max acceptable loss scenario |
| 4 | Time horizon | Mandatory | Maturity preference |
| 5 | Complexity tolerance | Mandatory | Suitability / sophistication |
| 6 | Market view — equity | Conditional | Required for equity-linked products |
| 7 | Market view — rates | Conditional | Required for rate-linked products |
| 8 | Market view — credit | Conditional | Required for credit-linked products |
| 9 | Market view — volatility | Conditional | Required for vol products |
| 10 | Liquidity needs | Optional | Hold-to-maturity vs exit capability |
| 11 | Income requirement | Optional | Regular coupon vs growth |
| 12 | Regulatory constraints | Optional | Retail eligibility, MiFID suitability, PRIIPS |
| 13 | Underlying preference | Optional | Single stock, index, basket, rates, credit |
| 14 | Currency | Optional | Domestic vs cross-currency |

### 1.2 Mandatory vs Optional Classification

**5 MANDATORY inputs** — without these, no recommendation is possible:

| Input | Why Mandatory | What Happens Without It |
|-------|---------------|------------------------|
| Client objective | Determines which product FAMILY to consider | Cannot narrow from 49 products |
| Capital protection | Determines full/conditional/none spectrum | Cannot assess suitability |
| Risk budget | Determines barrier levels, worst-case tolerance | Cannot size the trade |
| Time horizon | Determines maturity, path dependency tolerance | Cannot select product lifecycle |
| Complexity tolerance | Determines maximum product complexity | Cannot assess client comprehension |

**4 CONDITIONAL inputs** — required only for specific product families:

| Input | When Required | Products Affected |
|-------|--------------|-------------------|
| Equity view | When objective is yield/growth/protection on equity | ELN family, Equity Swaps, Options |
| Rates view | When objective is income/rate exposure | STEG, SRT, IRS, VLSP |
| Credit view | When objective is credit spread exposure | CLN, CDS, FTD, NTD, CDO |
| Volatility view | When objective is vol trading/hedging | VarSwap, VO, Opt-on-RC |

**5 OPTIONAL inputs** — refine but don't determine:

| Input | Impact | Default If Missing |
|-------|--------|--------------------|
| Liquidity needs | Eliminates illiquid products if client needs exit | Assume hold-to-maturity |
| Income requirement | Splits growth vs income paths | Consider both |
| Regulatory | Eliminates non-eligible products | Assume professional investor |
| Underlying preference | Narrows within family | Consider all underlyings |
| Currency | Adds FX dimension | Assume domestic |

### 1.3 Key Combinations That Change Recommendations

| Combination | Result |
|-------------|--------|
| Conservative + Income + Equity | RC, Digital, Phoenix → NOT PPN (no income) |
| Conservative + Growth + Equity | PPN, Booster, SD → NOT RC (income not growth) |
| Conservative + Income + Rates | STEG family → NOT ELN family |
| Moderate + Yield + Equity + Bullish | RC, Bonus → NOT Phoenix (pays less if bullish) |
| Moderate + Yield + Equity + Range-bound | Digital, CRA ELN → NOT RC (needs direction) |
| Aggressive + Max Yield + Multi-stock | WOAC → but ONLY if correlation understood |
| Hedging + Rate risk | IRS, VLSP → NOT CLN (credit, not rate) |
| Hedging + Credit risk | CDS (unfunded), CLN (funded) → distinct paths |
| Any + Low complexity tolerance | Cap at Complexity 3–4 regardless of objective |
| Any + Need liquidity | Eliminates OTC-only, long-dated, exotic structures |

**Critical finding:** The same objective (e.g., "yield enhancement") produces 10+ different recommendations depending on the combination of market view, risk budget, and complexity tolerance. This confirms the Solutions Manual CANNOT be a simple lookup table.

---

## 2. Input Overlap with Existing Content

### 2.1 What Chapters Already Provide

| Input | Where It's Covered | What's Missing |
|-------|--------------------|----------------|
| Client objective | §3 per product (49 sections) | Per-product only. No CROSS-PRODUCT comparison |
| Client perspective | §8 per product (49 sections) | Per-product only. No "given need X, choose between A/B/C" |
| Risk dimensions | Matrix Part 2 (49 × 4 dimensions) | Classification only. No decision logic |
| Product selection | Matrix Decision Trees (3 trees) | Classification by risk/objective/experience. No reasoning framework |

### 2.2 What's Genuinely Missing

1. **Reasoning methodology** — HOW to think through a structuring decision (the "structurer's mental model")
2. **Comparative analysis** — given the SAME client need, why choose product A over product B
3. **Anti-patterns** — when a product SEEMS right but is wrong
4. **Market regime sensitivity** — how the same objective requires different products in different market environments
5. **Complexity escalation** — systematic approach to start simple and escalate only when needed

---

## 3. Structurer Decision Model Assessment

### 3.1 Proposed Flow

```
CLIENT NEED
    ↓
MARKET VIEW
    ↓
RISK BUDGET
    ↓
LIQUIDITY CONSTRAINT
    ↓
COMPLEXITY TOLERANCE
    ↓
PRODUCT RECOMMENDATION
```

### 3.2 Assessment

**Verdict: GOOD but requires two modifications.**

**Modification 1: Add INCOME vs GROWTH split before Market View.**

Many clients' primary distinction is "I need regular payments" vs "I want capital appreciation." This split eliminates entire product families before market view matters.

Revised flow:

```
CLIENT NEED (objective classification)
    ↓
INCOME vs GROWTH (cash flow requirement)
    ↓
ASSET CLASS VIEW (equity / rates / credit / vol / FX)
    ↓
MARKET REGIME (directional view within asset class)
    ↓
RISK BUDGET (max loss, barrier tolerance)
    ↓
CONSTRAINTS (liquidity, time horizon, regulatory)
    ↓
COMPLEXITY FILTER (cap product universe by tolerance)
    ↓
CANDIDATE SET (3–8 products)
    ↓
FINAL SELECTION (comparative analysis)
```

**Modification 2: Add "CANDIDATE SET → FINAL SELECTION" as distinct step.**

The flow should NOT jump from constraints to a single product. It should narrow to 3–8 candidates and then teach comparative selection. This is where structurer judgment lives.

### 3.3 Should This Be Part 1 of the Solutions Manual?

**YES.** This framework is inseparable from the scenarios that follow. It provides the METHODOLOGY that makes each scenario teachable rather than just a lookup.

Structure:
- **Part 1:** Structurer Decision Framework (the model above, ~300 lines)
- **Part 2:** Scenario Library (problem → recommendation, ~800 lines)
- **Part 3:** Anti-Patterns (~200 lines)
- **Part 4:** Quick Reference (~100 lines)

---

## 4. Scenario Architecture Assessment

### 4.1 Current Proposal Review

| Proposed Category | Products Covered | Assessment |
|-------------------|:----------------:|------------|
| Capital Protection | ~7 | KEEP — distinct client need |
| Yield Enhancement | ~11 | KEEP — but split income/growth |
| Rates Exposure | ~7 | KEEP — rename "Rates & Inflation" |
| Credit Exposure | ~6 | KEEP |
| Portfolio Hedging | ~7 | KEEP — rename "Portfolio Management" |
| Complex Structures | ~3 | KEEP — but reframe as "Multi-Asset & Specialist" |

### 4.2 Missing Categories

| Category | Assessment | Products | Recommendation |
|----------|-----------|:--------:|:--------------:|
| Income Generation | CRITICAL gap. Income ≠ Yield. RC coupon, STEG coupon, CLN coupon serve different income needs | ~12 | **ADD** |
| Volatility Trading | Missing as standalone. VarSwap/VO/Opt-on-RC need own category | ~3 | **ADD** — split from Portfolio Hedging |
| Tactical Trading | NOT needed. Warrants, FWDs subsumable into other categories | ~3 | **SKIP** |
| FX Exposure | NOT needed. DCI and XCCY covered in Yield Enhancement and Portfolio Management respectively | ~2 | **SKIP** |
| Correlation Exposure | NOT needed. Too specialist. Covered under Multi-Asset | ~4 | **SKIP** |
| Liability Matching | NOT needed. ZCL/PPN covered in Capital Protection + Rates | ~2 | **SKIP** |

### 4.3 Recommended Final Scenario Architecture

| # | Category | Client Need Statement | Est. Scenarios | Products Covered |
|:-:|----------|----------------------|:--------------:|:----------------:|
| 1 | Capital Protection | "I cannot afford to lose principal" | 5 | PPN, Booster, Airbag, Bonus, SHRK, CLIQ, SD, ELO |
| 2 | Yield Enhancement | "I want higher returns than deposits/bonds" | 7 | RC, DRC, KODRC, CRC, Phoenix, FCN, Digital, DKIP, ICN, DCI |
| 3 | Income Generation | "I need regular coupon payments" | 5 | CRA ELN, Vanilla STEG, RA STEG, Callable STEG, TARN STEG, SNOW |
| 4 | Rates & Inflation | "I have a view on rates or the curve" | 5 | IRS, VLSP, IR Callable, ZCL, NCRA, CRA SRT, Digital CF |
| 5 | Credit Exposure | "I want credit spread exposure" | 5 | CDS, CLN, Skew CLN, FTD, NTD, CDO |
| 6 | Volatility Strategies | "I want to trade or hedge volatility" | 4 | VarSwap, VO, Opt-on-RC, WOAC |
| 7 | Portfolio Management | "I need to manage portfolio-level exposures" | 5 | FWD, TRS, EqSwap, XCCY, CommSwap, ACCUM, DECUM |
| 8 | Multi-Asset & Specialist | "Standard products don't fit" | 4 | WOAC, SNOW, CDO, Warrant, CLIQ |
| | | **Total** | **40** | **49 (all covered)** |

### 4.4 Coverage Verification

All 49 products appear in at least one scenario:

| Family | Count | All Covered |
|--------|:-----:|:-----------:|
| ELN (15) | 15 | YES |
| Swaps (8) | 8 | YES |
| SRT (5) | 5 | YES |
| STEG (4) | 4 | YES |
| CLN (5) | 5 | YES |
| Other (12) | 12 | YES |

**Some products appear in multiple categories.** This is intentional — WOAC appears in both Volatility (as vol trade) and Multi-Asset (as specialist structure). Context determines which framing is appropriate.

---

## 5. Anti-Pattern Framework

### 5.1 Framework Design

Each anti-pattern follows:

```
ANTI-PATTERN #N: [Title]

Client Says: "[Quote expressing need]"
Instinct:     [Product that seems right]
Why Wrong:    [Specific reason this product fails the need]
Instead:      [Correct product with reasoning]
Complexity:   [Wrong product] (X) vs [Right product] (Y)
```

### 5.2 Sample Anti-Patterns (framework only, not exhaustive)

| # | Client Says | Wrong Product | Why Wrong | Right Product |
|:-:|-------------|--------------|-----------|---------------|
| 1 | "I want protection" | RC (3) | RC has CONDITIONAL protection only — barrier breach = full loss | PPN (2) or Airbag (4) |
| 2 | "I want simplicity" | CDO (10) | Impossible to explain. Correlation + tranching + copula | CLN (4) if credit need |
| 3 | "I need liquidity" | SNOW (7) | Illiquid, complex secondary. Path-dependent valuation | RC (3) or Digital (4) |
| 4 | "I want yield" | PPN (2) | PPN pays ZERO coupon. Growth only, not yield | RC (3) or STEG (5) |
| 5 | "Low risk please" | WOAC (8) | Worst-of = risk of WORST stock. Multiplied downside | PPN (2) or SD (2) |
| 6 | "Guaranteed income" | Phoenix (6) | Coupon is CONTINGENT on barrier. Not guaranteed | FCN (6) or bond |
| 7 | "Credit exposure" | FTD (7) | First-to-default amplifies risk without understanding correlation | CLN (4) single name |
| 8 | "Hedge my portfolio" | ACCUM (6) | Accumulator is a LEVERAGED directional bet, not a hedge | EqSwap (5) or TRS (5) |
| 9 | "I want to sell vol" | VarSwap (7) | Unlimited loss. Convex payoff crushes short sellers | RC (3) — vol selling embedded |
| 10 | "Rates will steepen" | TARN STEG (8) | Target feature may terminate before steepening materializes | Vanilla STEG (5) |

### 5.3 Anti-Pattern Coverage Target

Minimum 15 anti-patterns in final Solutions Manual covering:
- All 6 families
- All common client needs
- All complexity bands (2–10)

---

## 6. Complexity Governance

### 6.1 Escalation Rule

**ALWAYS consider products in ascending complexity order. Only escalate when lower-complexity alternatives fail to meet requirements.**

This is the "Complexity Ladder" — never skip rungs without documented justification.

### 6.2 Example Ladder: "Client Wants Protection + Equity Upside"

| Rung | Product | Complexity | What You Get | What You Give Up |
|:----:|---------|:----------:|-------------|------------------|
| 1 | SD | 2 | Full protection, simplest | Low participation, short maturity |
| 2 | PPN | 2 | Full protection, longer maturity | Low participation (50-60%) |
| 3 | Booster | 4 | Leveraged upside, no barriers | NO protection — full downside |
| 4 | Airbag | 4 | Conditional protection, better terms | Barrier risk below airbag level |
| 5 | Bonus | 4 | Minimum return guarantee + full upside | Barrier risk eliminates bonus |
| 6 | SHRK | 4 | Barrier-enhanced PPN, higher participation | Capped upside above knock-out |
| 7 | CLIQ | 7 | Periodic lock-in, protection resets | Complex valuation, wide bid-ask |

**Decision documentation:** For each recommendation, the Solutions Manual should show which lower rungs were considered and WHY they were rejected.

### 6.3 Tier Respect Rules

| Rule | Implementation |
|------|---------------|
| Tier 1 products (Complexity 2) ALWAYS considered first | SD, FWD, PPN, VLSP |
| Tier 2 products (Complexity 3) tried before Tier 3 | RC, DRC, ICN, Warrant, IRS, VO, ELO, DCI |
| Complexity 7+ ONLY when 4–6 exhausted | Require explicit justification |
| Complexity 10 (CDO) ONLY for institutional/specialist | Never for retail/PB |

### 6.4 Atlas/Dependency Integration

Each scenario in Part 2 must:
1. Start with lowest-complexity product that meets the objective
2. Show the escalation path with trade-offs at each step
3. Reference Atlas complexity scores
4. Reference Dependency Graph learning prerequisites
5. Never recommend a product whose prerequisites the reader hasn't been introduced to in the scenario

---

## 7. Risk Assessment

| Risk | Severity | Mitigation |
|------|:--------:|------------|
| Scenarios become product catalogs instead of decision guides | High | Each scenario MUST include "why NOT the alternatives" |
| Anti-patterns too obvious | Medium | Include 5+ non-obvious traps (Phoenix ≠ guaranteed income, ACCUM ≠ hedge) |
| Framework too abstract to be actionable | Medium | Every step in Part 1 must have a worked example |
| Missing products in scenario coverage | High | Verify 49/49 after generation. Checklist built into review |
| Complexity governance feels pedantic | Low | Keep to 1 ladder per scenario. Don't belabor the obvious |

---

*Solutions Manual design review complete. 2026-06-22.*
