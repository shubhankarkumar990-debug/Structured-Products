# Solutions Manual

**Desk Bible v2 — Structuring Decisions for 49 Products**

**Products:** 49
**Scenarios:** 40
**Anti-Patterns:** 18
**Personas:** 4
**Framework:** v1.3.1 (frozen)
**Generated:** 2026-06-22

---

## Table of Contents

1. [Part 1: Structurer Decision Framework](#part-1-structurer-decision-framework)
2. [Part 2: Scenario Library](#part-2-scenario-library)
3. [Part 3: Anti-Patterns](#part-3-anti-patterns)
4. [Part 4: Quick Reference & Replacement Table](#part-4-quick-reference--replacement-table)

---

# Part 1: Structurer Decision Framework

## 1.1 The 10-Step Decision Model

Every structuring recommendation follows this sequence. Steps 1–7 narrow the 49-product universe. Steps 8–9 compare survivors. Step 10 validates.

```
Step 1   CLIENT OBJECTIVE
         Protection / Yield / Income / Growth / Hedging / Vol Trading
              ↓
Step 2   CASH FLOW REQUIREMENT
         Growth (no payments) / Fixed Income / Contingent Income
              ↓
Step 3   ASSET CLASS
         Equity / Rates / Credit / Volatility / FX / Commodity
              ↓
Step 3.5 PERSONA FILTER
         Retail (cap 4) / PB (cap 8) / Institutional (full) / Sophisticated (full)
              ↓
Step 4   MARKET REGIME
         Bullish / Bearish / Range-bound / Steepening / Flattening / No view
              ↓
Step 5   RISK BUDGET
         Zero loss / Conditional (barrier) / Defined (premium) / Unlimited
              ↓
Step 6   CONSTRAINTS
         Liquidity / Maturity / Regulatory / Currency
              ↓
Step 7   COMPLEXITY FILTER
         Apply persona cap from Step 3.5 + client-specific tolerance
              ↓
Step 8   CANDIDATE SET
         3–8 products surviving Steps 1–7
              ↓
Step 9   COMPARATIVE SELECTION
         Evaluate candidates on payoff, cost, path dependency, hedge cost
              ↓
Step 10  VALIDATION
         Confirm recommendation respects all constraints
```

**Step 1** eliminates entire families. A hedging objective eliminates all ELN products. A protection objective eliminates all swaps.

**Step 2** splits paths early. "Growth" eliminates coupon products (RC, STEG). "Fixed income" eliminates growth products (PPN, Booster).

**Step 3** narrows to an asset class. Equity clients see ELN + Equity Swaps. Rates clients see SRT + STEG + IRS.

**Step 3.5** applies persona-based product eligibility (see §1.2).

**Step 4** is where structurer judgment begins. The same objective under different market views produces different products. Bullish equity → RC. Range-bound equity → Digital.

**Step 5** determines protection level. Zero-loss clients get PPN/SD. Conditional-loss clients get RC/Phoenix. Premium-loss clients get Warrants/Options.

**Step 6** applies hard constraints. Need liquidity? Eliminate long-dated exotics. Need short maturity? Eliminate 5-year SRT.

**Step 7** caps complexity. A Retail persona cannot access Phoenix (6). A PB client capped at 5 cannot access WOAC (8).

**Step 8** outputs the candidate set — typically 3–8 products.

**Step 9** is the decision. Use the Comparative Selection table to evaluate candidates on payoff shape, protection cost, path dependency, complexity premium, and desk hedge cost.

**Step 10** validates: does the recommendation respect all constraints from Steps 1–7? If not, return to Step 8.

---

## 1.2 The 4 Personas

| Persona | Complexity Cap | Product Universe | Key Constraint |
|---------|:--------------:|:----------------:|----------------|
| **Retail** | ≤4 | Notes only. No swaps, no ISDA | PRIIPS/KID required. Suitability rules |
| **Private Banking** | ≤8 | All notes + select swaps (IRS, CDS) | Sophistication assessed. Advisory mandate |
| **Institutional** | No cap | Full universe including all swaps, SRT, STEG | ALM/hedging focus. Regulatory capital aware |
| **Sophisticated** | No cap | Full universe + leverage products | ACCUM/DECUM/VarSwap accessible. No suitability cap |

**Persona determines eligibility, not preference.** A Retail client cannot access Phoenix (6) regardless of their market view. An Institutional client can access PPN (2) if it fits their mandate.

Product counts by persona eligibility:

| Persona | Eligible Products | Excluded |
|---------|:-----------------:|:--------:|
| Retail | 12 | 37 |
| Private Banking | 41 | 8 (VarSwap, CRA SRT, TARN STEG, NTD, CDO, RA STEG, ACCUM, DECUM) |
| Institutional | 49 | 0 |
| Sophisticated | 49 | 0 |

---

## 1.3 Market Regime Awareness

The same client objective requires different products in different regimes.

| Regime | Benefits | Suffers | Structurer Action |
|--------|----------|---------|-------------------|
| **High equity vol** | RC, Phoenix (rich premium) | PPN (option expensive, low participation) | Favour yield products over protection |
| **Low equity vol** | PPN (cheap option, high participation) | RC, Phoenix (thin premiums, unattractive coupons) | Favour protection products over yield |
| **Steep yield curve** | STEG family (wide CMS spread) | Flat-rate products | STEG coupons attractive |
| **Flat/inverted curve** | Fixed-rate products, IRS | STEG family (zero spread coupon) | Avoid STEG — recommend fixed income |
| **Wide credit spreads** | CLN (high credit premium) | CDS buyer (expensive protection) | Sell credit protection via CLN/CDS |
| **Tight credit spreads** | CDS buyer (cheap protection) | CLN (low premium, poor compensation) | Buy credit protection, avoid selling |
| **Rising rates** | PPN worse (expensive ZCB) | Floating-rate products benefit | Favour floating over fixed |
| **Falling rates** | PPN better (cheap ZCB, high participation) | Floating-rate products suffer | Favour PPN, lock fixed rates |

**Regime awareness is the single biggest differentiator between a junior and senior structurer.** A junior recommends RC because it's the "yield product." A senior knows RC premiums are thin in low-vol environments and switches to Digital or STEG.

---

## 1.4 Complexity Escalation Protocol

**The Complexity Ladder:** always start at the lowest complexity that meets the objective. Only escalate when the simpler product fails to meet a specific requirement.

Rules:
1. Tier 1 products (Complexity 2) considered first: SD, FWD, PPN, VLSP
2. Tier 2 (Complexity 3) tried before Tier 3: RC, DRC, ICN, Warrant, IRS, VO, ELO, DCI
3. Complexity 7+ only when 4–6 are exhausted — require explicit justification
4. Complexity 10 (CDO) only for Institutional/Sophisticated with documented credit expertise

Each ladder rung has an **escalation trigger** — the specific condition that justifies moving up:

```
PPN (2) — full protection, 55% participation
   ↑ Trigger: Participation below 40% in current rate environment
Airbag (4) — conditional protection, ~80% participation
   ↑ Trigger: Client accepts barrier risk for higher participation
Bonus (4) — minimum return guarantee + full upside
   ↑ Trigger: Client wants guaranteed minimum above zero
SHRK (4) — barrier-enhanced, higher participation
   ↑ Trigger: Client accepts capped upside via knock-out barrier
CLIQ (7) — periodic lock-in, protection resets
```

**Never skip rungs without documenting why the intermediate product was inadequate.**

---

## 1.5 The Desk Economics Lens

When two products meet client needs equally, the desk prefers the product that is:

| Preference | Why | Example |
|-----------|-----|---------|
| **Higher margin** | Structuring fee + bid-offer | RC margin 2–3× PPN margin |
| **Easier to hedge** | Liquid underliers, standard Greeks | Index-linked over single-stock |
| **Lower operational burden** | Fewer observations, simpler lifecycle | RC (European) over Phoenix (periodic observations) |
| **Lower capital consumption** | Simpler RWA calculation | Notes over swaps (funded vs unfunded) |

Desk economics should never override client suitability. But when choosing between equally suitable products, the desk preference matters — it produces better pricing for the client (the desk passes through lower hedge cost).

---

## 1.6 The Structurer's Anti-Instincts

Five cases where the "obvious" choice is wrong:

1. **"Client wants yield" → PPN is wrong.** PPN pays zero coupon. It's a growth product. Yield means RC/STEG/CLN.

2. **"Client wants protection" → RC is wrong.** RC has conditional protection. Below the barrier, the client takes full equity loss. Protection means PPN/SD.

3. **"Client wants maximum coupon" → WOAC is tempting but dangerous.** WOAC coupon is high because the client sells correlation risk on a basket. The worst stock drives all outcomes. This is not "high yield" — it's concentrated tail risk.

4. **"Client wants volatility exposure" → VarSwap short is tempting but catastrophic.** VarSwap has convex payoff. Short sellers face unlimited loss. A 2× vol move produces 4× loss. Use VO for directional vol instead.

5. **"Client is bullish" → Phoenix is wrong.** Phoenix is designed for range-bound markets. Autocall terminates quickly if stock rallies, capping total return. Bullish clients should use RC, Booster, or Warrant.

---

# Part 2: Scenario Library

## Category 1 — Capital Protection

*"I cannot afford to lose my principal."*

---

### Scenario 1.1: Full Protection With Equity Upside

**Client says:** "I need 100% principal protection but want equity market participation."

**Persona:** Retail / PB. Cap varies by persona.

**Narrowing:** Objective → Protection | Cash Flow → Growth | Asset → Equity | Regime → Neutral | Risk → Zero loss | Complexity → ≤4 (Retail) or ≤8 (PB)

**Candidates:** PPN (2), SD (2), SHRK (4)

**Rejected:**

| Product | Step | Reason |
|---------|:----:|--------|
| RC (3) | Risk Budget | Conditional protection — client demands zero loss |
| Booster (4) | Risk Budget | No capital protection at all |
| CLIQ (7) | Persona | Exceeds Retail cap of 4 |

**Selection:**

| Dimension | PPN (2) | SD (2) | SHRK (4) |
|-----------|---------|--------|----------|
| Protection | 100% at maturity | 100% (deposit insurance) | 100% at maturity |
| Participation | 50–65% | 30–50% | 60–80% |
| Complexity | Simplest note | Simplest product | Barrier caps upside |
| Maturity | 3–5 years | 1–3 years | 1–3 years |

**Recommendation:** PPN (2) — full protection, highest participation among fully protected products, no barrier complications.

**Why This Wins:**
- Full 100% principal guarantee with no conditions or barriers
- Participation rate 50–65% captures meaningful equity upside
- Complexity 2 — accessible to all personas including Retail

**Ladder:**
1. SD (2) — deposit insurance, ~40% participation
   ↑ If participation too low and client accepts note format (no deposit insurance): escalate
2. PPN (2) — note format, ~55% participation
   ↑ If participation still insufficient and client accepts barrier cap: escalate
3. SHRK (4) — barrier-enhanced, ~70% participation but KO caps strong rallies

**Common Mistake:** Recommending RC because "it also has protection." RC protection is conditional — barrier breach means full equity loss. The client said "cannot lose principal."

**Regime Note:** In low-rate environments (rates < 2%), PPN participation drops below 40%. Consider SD for shorter duration or wait for better rate conditions.

---

### Scenario 1.2: Capital Protection With Regular Income

**Client says:** "I want my principal safe AND regular coupon payments."

**Persona:** PB / Institutional.

**Narrowing:** Objective → Protection | Cash Flow → Income | Asset → Equity or Rates | Risk → Zero loss | Complexity → ≤6

**Candidates:** Digital (4), CRA ELN (6), Vanilla STEG (5), Digital CF (5)

**Rejected:**

| Product | Step | Reason |
|---------|:----:|--------|
| PPN (2) | Cash Flow | No coupon — growth only |
| RC (3) | Risk Budget | Conditional protection |
| TARN STEG (8) | Complexity | Exceeds cap and path-dependent |

**Selection:**

| Dimension | Digital (4) | Vanilla STEG (5) | CRA ELN (6) |
|-----------|-------------|-------------------|-------------|
| Coupon type | Binary (all-or-nothing) | CMS spread | Range accrual |
| Protection | 100% | 100% | 100% |
| Income risk | Near-strike: zero coupon | Flat curve: zero coupon | Outside range: zero coupon |
| Asset class | Equity | Rates | Equity |

**Recommendation:** Digital (4) for equity view. Vanilla STEG (5) for rates view. Decision depends on Step 3 (Asset Class).

**Why This Wins:**
- Both offer 100% capital protection WITH coupon payments
- Digital is simpler (Complexity 4) and appropriate for equity-focused clients
- Vanilla STEG suits clients with a yield curve steepening view

**Ladder:**
1. Digital (4) — binary coupon, principal safe
   ↑ If need higher coupon and accept range condition: escalate
2. Vanilla STEG (5) — CMS spread coupon if rates view exists
   ↑ If accept call risk for better coupon: escalate
3. CRA ELN (6) — range accrual, highest coupon among protected products

**Common Mistake:** Assuming "capital protection + income" is contradictory. 14 products offer 100% protection — the income risk shifts from principal to coupon.

**Regime Note:** In flat yield curve environments, avoid STEG (zero coupon). Default to equity-linked Digital.

---

### Scenario 1.3: Better Terms With Conditional Protection

**Client says:** "I'd accept some downside risk if it means significantly better participation or yield."

**Persona:** PB. Complexity ≤6.

**Narrowing:** Objective → Protection (conditional) | Cash Flow → Growth | Asset → Equity | Regime → Mildly bullish | Risk → Conditional (barrier) | Complexity → ≤6

**Candidates:** Airbag (4), Bonus (4), KODRC (4)

**Rejected:**

| Product | Step | Reason |
|---------|:----:|--------|
| PPN (2) | Objective | Client explicitly accepts conditional risk for better terms |
| Phoenix (6) | Cash Flow | Income product — client wants growth |
| WOAC (8) | Complexity | Exceeds cap and multi-stock risk inappropriate |

**Selection:**

| Dimension | Airbag (4) | Bonus (4) | KODRC (4) |
|-----------|------------|-----------|-----------|
| Mechanism | Cushion absorbs losses between strike and barrier | Minimum return if barrier intact | KO barrier + discount entry |
| Upside | Leveraged above strike | Full participation above bonus | Capped at KO level |
| Downside | Full loss below airbag level | Full loss below barrier | Full loss below KI barrier |

**Recommendation:** Airbag (4) — best balance of leveraged upside and defined cushion. Client who accepts conditional risk gets 1.5× participation.

**Why This Wins:**
- Leveraged upside (typically 150% participation) vs PPN's 55%
- Airbag cushion absorbs first 20–30% of decline
- Same complexity as alternatives but clearest payoff diagram

**Ladder:**
1. PPN (2) — zero downside, ~55% participation
   ↑ If participation insufficient: escalate
2. Airbag (4) — cushion protection, ~150% participation
   ↑ If client wants guaranteed minimum return: switch to
3. Bonus (4) — min 10%+ return if barrier unbreached, full upside above

**Common Mistake:** Treating Airbag and Bonus as interchangeable. Airbag provides a leverage mechanism. Bonus provides a minimum return. Different payoff shapes for different views.

**Regime Note:** High vol makes barriers risky. In high-vol regimes, widen the barrier (lower cushion) or retreat to PPN.

---

### Scenario 1.4: Guaranteed Minimum Return Plus Full Upside

**Client says:** "I want at least 10% return even if markets are flat, plus full upside if markets rally."

**Persona:** Retail / PB.

**Narrowing:** Objective → Protection + Growth | Cash Flow → Growth | Asset → Equity | Regime → Uncertain (flat or up) | Risk → Conditional | Complexity → ≤4

**Candidates:** Bonus (4)

**Rejected:**

| Product | Step | Reason |
|---------|:----:|--------|
| PPN (2) | Objective | No minimum return — just principal back if flat |
| Airbag (4) | Objective | No guaranteed minimum — only cushion |
| RC (3) | Cash Flow | Income product, not growth |

**Recommendation:** Bonus (4) — unique payoff: guaranteed bonus above zero if barrier intact, plus full participation in rally.

**Why This Wins:**
- Only product guaranteeing positive return in flat markets (barrier intact)
- Full 100% participation above the bonus level
- Attractive in uncertain markets where direction is unclear

**Ladder:**
1. PPN (2) — zero return if flat, ~55% participation if up
   ↑ If client demands positive return even in flat market: escalate
2. Bonus (4) — 10%+ minimum return + full upside

**Common Mistake:** Ignoring barrier risk. If the barrier is breached at any point (even temporarily), the bonus evaporates and the product becomes a direct equity position. The "guarantee" is conditional.

**Regime Note:** Bonus works best in low-vol environments where barrier breach is unlikely. In high-vol, the barrier becomes a real threat.

**Desk Note:** Bonus is harder to hedge than RC (down-and-in put + call combination). Desk passes through higher hedge cost as wider bid-ask.

---

### Scenario 1.5: Periodic Gain Lock-In

**Client says:** "I want protection but also want to lock in gains periodically so I don't lose them."

**Persona:** PB. Complexity ≤7.

**Narrowing:** Objective → Protection + Growth | Cash Flow → Growth | Asset → Equity | Regime → Trending | Risk → Zero loss on principal | Complexity → ≤7

**Candidates:** SHRK (4), CLIQ (7)

**Rejected:**

| Product | Step | Reason |
|---------|:----:|--------|
| PPN (2) | Objective | No lock-in — all return at maturity |
| Bonus (4) | Objective | Minimum return, but no periodic lock-in |
| WOAC (8) | Complexity | Exceeds cap |

**Selection:**

| Dimension | SHRK (4) | CLIQ (7) |
|-----------|----------|----------|
| Mechanism | Barrier-enhanced participation with KO cap | Serial forward-starting options, periodic resets |
| Lock-in | Single barrier event | Periodic (quarterly/annual) |
| Protection | 100% principal | 100% principal |
| Upside cap | KO barrier caps strong rally (rebate paid) | Local caps per period |

**Recommendation:** SHRK (4) for simpler lock-in. CLIQ (7) for true periodic reset with PB sophistication.

**Why This Wins:**
- SHRK: principal safe + enhanced participation up to KO barrier
- CLIQ: genuine periodic lock-in — gains from each period are banked regardless of future performance
- Both address the specific "don't lose my gains" anxiety

**Ladder:**
1. PPN (2) — no lock-in, all at maturity
   ↑ If client explicitly wants gain capture during life: escalate
2. SHRK (4) — barrier-enhanced, rebate on KO
   ↑ If need true periodic lock-in (not just barrier): escalate
3. CLIQ (7) — serial forward-starting options, periodic gain banking

**Common Mistake:** Recommending CLIQ for bullish clients. CLIQ has local caps per period — in a strongly trending market, the caps reduce total return below what PPN would deliver.

**Regime Note:** CLIQ outperforms in choppy, mean-reverting markets. In trending markets, PPN wins.

---

## Category 2 — Yield Enhancement

*"I want higher returns than bonds or deposits."*

---

### Scenario 2.1: Bullish Equity — Above-Market Yield

**Client says:** "I'm bullish on this stock and want a higher yield than bonds."

**Persona:** PB. Complexity ≤5.

**Narrowing:** Objective → Yield | Cash Flow → Fixed Income | Asset → Equity | Regime → Bullish | Risk → Conditional | Complexity → ≤5

**Candidates:** RC (3), DRC (3), Bonus (4), KODRC (4)

**Rejected:**

| Product | Step | Reason |
|---------|:----:|--------|
| Phoenix (6) | Complexity | Exceeds cap of 5 |
| PPN (2) | Cash Flow | No coupon |
| VarSwap (7) | Asset/Risk | Not yield — pure vol |

**Selection:**

| Dimension | RC (3) | DRC (3) | KODRC (4) |
|-----------|--------|---------|-----------|
| Coupon | Fixed 8–12% | None (discount entry) | Fixed 6–10% |
| Entry | Par | Below par (~95%) | Par |
| Protection | Barrier at 60–70% | Barrier at 60–70% | KO barrier + KI barrier |
| Bullish fit | Best — barrier unlikely to breach | Good — discount provides extra buffer | Good — KO adds protection layer |

**Recommendation:** RC (3) — highest fixed coupon, simplest structure, barrier protection adequate for bullish view.

**Why This Wins:**
- Highest fixed coupon among Complexity ≤5 products
- Simplest yield enhancement structure — universally understood
- Bullish view means barrier breach probability is low

**Ladder:**
1. RC (3) — 8–12% coupon, barrier 60–70%
   ↑ If coupon insufficient and client accepts callable risk: escalate
2. CRC (5) — higher coupon via embedded call option sold to issuer

**Common Mistake:** Recommending Phoenix for a bullish client. If the stock rallies, Phoenix autocalls early — total return is just one coupon period. RC pays the full coupon for the entire term.

**Regime Note:** In low-vol environments, RC premiums shrink to 4–6%. Switch to Digital (4) for principal-protected binary coupon.

**Desk Note:** RC margin is 2–3× PPN margin. Desk actively prefers RC flow.

---

### Scenario 2.2: Yield With Discount Entry Margin

**Client says:** "I want yield but with more downside buffer than a standard RC."

**Persona:** PB.

**Narrowing:** Objective → Yield | Cash Flow → Growth (return at maturity) | Asset → Equity | Regime → Mildly bullish | Risk → Conditional with extra buffer | Complexity → ≤4

**Candidates:** DRC (3), KODRC (4)

**Rejected:**

| Product | Step | Reason |
|---------|:----:|--------|
| RC (3) | Objective | Client explicitly wants MORE buffer |
| Airbag (4) | Cash Flow | Growth/protection — not yield-enhancement framing |
| DKIP (7) | Complexity | Far exceeds cap |

**Selection:**

| Dimension | DRC (3) | KODRC (4) |
|-----------|---------|-----------|
| Buffer mechanism | Discount entry (~95%) | KO barrier adds protection layer |
| Coupon | None (return via discount) | Fixed coupon |
| Effective buffer | ~35% (barrier 65% + 5% discount) | Dual barrier (KO + KI) |

**Recommendation:** DRC (3) — extra 5% buffer via discount, simplest enhanced-buffer product.

**Why This Wins:**
- Discount entry provides automatic 5% additional buffer vs standard RC
- Same complexity as RC — no additional features to understand
- Effective protection level is 35% decline vs RC's 30% decline

**Ladder:**
1. RC (3) — standard barrier at 65%
   ↑ If client needs more buffer: escalate
2. DRC (3) — same barrier + 5% discount entry
   ↑ If client wants both coupon AND buffer: escalate
3. KODRC (4) — KO barrier adds protection, fixed coupon maintained

**Common Mistake:** Confusing DRC's discount entry with "buying at a discount." The discount is embedded in the put strike — the client buys at par but the effective strike is lower.

**Regime Note:** DRC works in any vol regime since the buffer is structural, not premium-dependent.

---

### Scenario 2.3: Yield With Knock-Out Protection Layer

**Client says:** "I want yield like an RC but with an extra protection feature."

**Persona:** PB. Complexity ≤5.

**Narrowing:** Objective → Yield | Cash Flow → Fixed Income | Asset → Equity | Regime → Moderate | Risk → Conditional (enhanced) | Complexity → ≤5

**Candidates:** KODRC (4), CRC (5)

**Rejected:**

| Product | Step | Reason |
|---------|:----:|--------|
| RC (3) | Objective | Client explicitly wants enhanced protection |
| Phoenix (6) | Complexity | Exceeds cap |
| CLIQ (7) | Objective | Not yield enhancement — protection/growth |

**Recommendation:** KODRC (4) — standard RC yield plus KO barrier that cancels downside risk if stock recovers above KO level.

**Why This Wins:**
- Same coupon as RC but with additional knock-out protection
- If stock dips then recovers above KO level, principal is safe regardless of prior KI breach
- Moderate complexity step up (3→4) for meaningful protection improvement

**Ladder:**
1. RC (3) — single barrier
   ↑ If client wants protection against temporary dips: escalate
2. KODRC (4) — KO barrier cancels KI on recovery

**Common Mistake:** Thinking KO protection is "free." KODRC coupon is lower than RC because the KO barrier costs the desk money. The client pays for protection via reduced yield.

**Regime Note:** KODRC outperforms RC in volatile-but-recovering markets. In sustained declines, both suffer equally.

---

### Scenario 2.4: Maximum Conditional Coupon With Autocall

**Client says:** "I want the highest possible coupon. I understand it's contingent on performance."

**Persona:** PB. Complexity ≤6.

**Narrowing:** Objective → Yield | Cash Flow → Contingent Income | Asset → Equity | Regime → Range-bound to mildly bullish | Risk → Conditional | Complexity → ≤6

**Candidates:** Phoenix (6), FCN (6)

**Rejected:**

| Product | Step | Reason |
|---------|:----:|--------|
| RC (3) | Objective | Coupon lower than Phoenix/FCN |
| DKIP (7) | Complexity | Exceeds cap |
| WOAC (8) | Complexity | Far exceeds cap |

**Selection:**

| Dimension | Phoenix (6) | FCN (6) |
|-----------|-------------|---------|
| Coupon | Contingent (paid if above barrier) | Fixed (paid regardless) |
| Autocall | Yes — early exit if above trigger | Yes — early exit if above trigger |
| Best scenario | All coupons + autocall at par | All coupons + autocall at par |
| Worst scenario | Zero coupons + below barrier at maturity | All coupons but below barrier at maturity |

**Recommendation:** Phoenix (6) for maximum coupon. FCN (6) for coupon certainty.

**Why This Wins:**
- Phoenix: highest coupon in the ELN family (contingent = higher premium)
- FCN: coupon is guaranteed regardless of performance — pure income certainty
- Both offer autocall for early exit if market cooperates

**Ladder:**
1. RC (3) — fixed coupon, no autocall
   ↑ If coupon insufficient: escalate
2. CRC (5) — higher coupon via callable
   ↑ If client wants autocall + maximum coupon: escalate
3. Phoenix (6) — contingent coupon, autocall, memory feature

**Common Mistake:** Choosing Phoenix for income certainty. Phoenix coupon is CONTINGENT — if the stock is below the coupon barrier on any observation date, that period's coupon is zero. For guaranteed income, use FCN.

**Regime Note:** Phoenix thrives in range-bound markets where stock hovers above barrier. In trending markets (up or down), autocall terminates quickly or coupons are lost.

**Desk Note:** Phoenix is the desk's most traded autocallable. Hedge liquidity is excellent on major indices.

---

### Scenario 2.5: Digital All-or-Nothing Coupon

**Client says:** "I want a high coupon if the market stays above a level. I don't need the coupon to scale with performance."

**Persona:** PB. Complexity ≤7.

**Narrowing:** Objective → Yield | Cash Flow → Contingent Income | Asset → Equity | Regime → Mildly bullish | Risk → Zero capital loss (Digital) or Conditional (DKIP) | Complexity → ≤7

**Candidates:** Digital (4), DKIP (7)

**Rejected:**

| Product | Step | Reason |
|---------|:----:|--------|
| RC (3) | Objective | Coupon not digital — scales linearly |
| Phoenix (6) | Objective | Memory + autocall add complexity beyond need |
| CRA ELN (6) | Objective | Range accrual — client wants binary, not daily |

**Selection:**

| Dimension | Digital (4) | DKIP (7) |
|-----------|-------------|----------|
| Capital | 100% protected | Conditional (KI barrier) |
| Coupon | Binary: above strike = full coupon, below = zero | Digital coupon + separate KI capital risk |
| Yield | Moderate (6–8%) | High (10–15%) |

**Recommendation:** Digital (4) for principal safety. DKIP (7) only for PB clients who accept capital risk for significantly higher yield.

**Why This Wins:**
- Digital: 100% principal protection + binary coupon — cleanest digital structure
- Risk is purely on coupon, never on capital
- DKIP trades capital safety for 2× the yield — clear risk/return upgrade

**Ladder:**
1. Digital (4) — 100% protected, 6–8% binary coupon
   ↑ If coupon insufficient and client accepts capital risk: escalate
2. DKIP (7) — 10–15% coupon but KI barrier on principal

**Common Mistake:** Assuming digital coupon = guaranteed coupon. Digital is all-or-nothing: one tick below the strike = zero coupon. The P&L discontinuity at the digital strike is severe.

**Regime Note:** Digital works in any directional regime where the strike is set appropriately. In high-vol, set strike lower for higher coupon probability.

---

### Scenario 2.6: Callable Yield Enhancement

**Client says:** "I want yield and understand the issuer may call the note early."

**Persona:** PB. Complexity ≤5.

**Narrowing:** Objective → Yield | Cash Flow → Fixed Income | Asset → Equity | Risk → Conditional + call risk | Complexity → ≤5

**Candidates:** CRC (5), ICN (3)

**Rejected:**

| Product | Step | Reason |
|---------|:----:|--------|
| RC (3) | Objective | No call feature — client accepts call for higher coupon |
| Phoenix (6) | Complexity | Exceeds stated cap |
| IR Callable (5) | Asset | Rate-linked, not equity |

**Selection:**

| Dimension | CRC (5) | ICN (3) |
|-----------|---------|---------|
| Coupon | Highest RC variant | Moderate |
| Call | Issuer calls when stock rallies | Issuer calls when funding cheaper |
| Risk | Downside + call reinvestment | Downside + call reinvestment |

**Recommendation:** ICN (3) for simplicity. CRC (5) for maximum coupon.

**Why This Wins:**
- ICN: Complexity 3, simple callable — extra coupon for call risk
- CRC: highest coupon in the RC family — issuer sold both put and call
- Both compensate client for reinvestment risk with higher yield

**Ladder:**
1. RC (3) — no call, 8–12% coupon
   ↑ If willing to accept call risk for higher coupon: escalate
2. ICN (3) — callable, moderate coupon uplift
   ↑ If want maximum coupon: escalate
3. CRC (5) — callable + highest coupon (short put + short call)

**Common Mistake:** Ignoring call timing. Issuers call when it benefits THEM (rates fall, stock rallies). The call always comes at the worst time for the investor's reinvestment.

**Regime Note:** Callable products benefit from stable markets. In volatile markets, call probability fluctuates — pricing becomes challenging.

---

### Scenario 2.7: FX-Linked Deposit Yield

**Client says:** "I want to earn more than my deposit rate and have a view on FX."

**Persona:** PB. Complexity ≤3.

**Narrowing:** Objective → Yield | Cash Flow → Fixed Income | Asset → FX | Regime → FX view (mild) | Risk → Conditional (FX conversion) | Complexity → ≤3

**Candidates:** DCI (3)

**Rejected:**

| Product | Step | Reason |
|---------|:----:|--------|
| RC (3) | Asset | Equity-linked, not FX |
| SD (2) | Objective | Lower yield — no risk premium |
| XCCY (5) | Persona/Complexity | Institutional swap, not deposit product |

**Recommendation:** DCI (3) — enhanced deposit rate funded by selling FX put option. If FX moves against client, principal converts to alternate currency.

**Why This Wins:**
- Simple: deposit + embedded FX option = enhanced yield
- Complexity 3 — accessible to most PB clients
- Client already has FX view — product monetizes that view

**Ladder:**
1. Standard deposit — base rate
   ↑ If client has directional FX view: escalate
2. DCI (3) — deposit + FX option premium = enhanced yield

**Common Mistake:** Clients don't understand the conversion risk. If their base currency weakens past the strike, they receive principal in the alternate (weaker) currency. The enhanced yield does not compensate for large FX moves.

**Regime Note:** DCI works when FX volatility is moderate. In high FX vol, conversion risk outweighs yield premium.

---

## Category 3 — Income Generation

*"I need regular coupon payments."*

---

### Scenario 3.1: Rate-Linked Regular Income

**Client says:** "I want regular coupon payments linked to the yield curve. I believe the curve will steepen."

**Persona:** Institutional.

**Narrowing:** Objective → Income | Cash Flow → Periodic coupon | Asset → Rates (CMS spread) | Regime → Steepening | Risk → Zero capital loss | Complexity → ≤6

**Candidates:** Vanilla STEG (5), Callable STEG (6)

**Rejected:**

| Product | Step | Reason |
|---------|:----:|--------|
| RC (3) | Asset | Equity-linked, not rates |
| IRS (3) | Cash Flow | Fixed/floating exchange — not CMS spread coupon |
| RA STEG (7) | Complexity | Exceeds cap |

**Selection:**

| Dimension | Vanilla STEG (5) | Callable STEG (6) |
|-----------|-------------------|-------------------|
| Coupon | Leverage × (CMS30Y – CMS2Y) | Same formula, higher leverage |
| Call risk | None | Issuer calls when curve steepens (worst timing) |
| Yield | Moderate | Higher (compensates for call) |
| Protection | 100% | 100% |

**Recommendation:** Vanilla STEG (5) — pure steepener exposure without call risk.

**Why This Wins:**
- Clean expression of steepening view — no additional features to distort payoff
- 100% capital protection at maturity
- No call risk — client holds to maturity and captures full steepening

**Ladder:**
1. Vanilla STEG (5) — pure CMS spread coupon
   ↑ If coupon insufficient and accept call risk: escalate
2. Callable STEG (6) — higher leverage, issuer callable
   ↑ If accept range condition for maximum coupon: escalate
3. RA STEG (7) — range accrual on CMS spread (dual condition)

**Common Mistake:** Buying STEG without checking the current curve shape. If CMS30Y – CMS2Y is already negative (inverted), the coupon is zero from day one. STEG requires a STEEPENING view, not just positive slope.

**Regime Note:** In flat/inverted curve environments, avoid STEG entirely. Switch to Digital CF (5) for binary rate income.

**Desk Note:** Desk prefers Callable STEG — the call optionality generates extra margin.

---

### Scenario 3.2: Range-Bound Rate Income

**Client says:** "I believe rates will stay in a range. I want income that accrues daily when they do."

**Persona:** Institutional / Sophisticated.

**Narrowing:** Objective → Income | Cash Flow → Accrual coupon | Asset → Rates or Equity | Regime → Range-bound | Risk → Zero capital loss | Complexity → ≤7

**Candidates:** CRA ELN (6), NCRA (6), RA STEG (7)

**Rejected:**

| Product | Step | Reason |
|---------|:----:|--------|
| Vanilla STEG (5) | Regime | Directional (steepening), not range-bound |
| Digital (4) | Cash Flow | Periodic binary, not daily accrual |
| CRA SRT (7) | Complexity | At cap — CRA SRT adds callable to range accrual |

**Selection:**

| Dimension | CRA ELN (6) | NCRA (6) | RA STEG (7) |
|-----------|-------------|----------|-------------|
| Underlying | Equity index | Interest rate | CMS spread |
| Accrual | Days equity in range | Days rate in range | Days spread in range |
| Protection | 100% | 100% | 100% |
| Callable | Yes | No | No |

**Recommendation:** NCRA (6) for pure rate range view. CRA ELN (6) for equity range view.

**Why This Wins:**
- Daily accrual means coupon scales linearly with time in range
- 100% capital protection — risk is purely on coupon amount
- Range accrual generates higher yields than fixed coupons because client sells vol

**Ladder:**
1. Digital (4) / Digital CF (5) — periodic binary coupon
   ↑ If client wants daily accrual (not periodic): escalate
2. NCRA (6) / CRA ELN (6) — daily range accrual
   ↑ If accept dual condition (curve + range): escalate
3. RA STEG (7) — range accrual on CMS spread

**Common Mistake:** Setting the range too narrow for higher coupon. A narrow range = more accrual days missed = volatile income. Range width should match rate volatility.

**Regime Note:** Range accrual products suffer when rates break out of the range. In trending rate environments, switch to directional products (STEG for steepening, IRS for hedging).

---

### Scenario 3.3: Enhanced Income With Call Risk

**Client says:** "I want higher income than a vanilla steepener. I understand the issuer may call."

**Persona:** Institutional.

**Narrowing:** Objective → Income | Cash Flow → Periodic coupon | Asset → Rates | Regime → Steepening | Risk → Zero capital + call risk | Complexity → ≤6

**Candidates:** Callable STEG (6)

**Rejected:**

| Product | Step | Reason |
|---------|:----:|--------|
| Vanilla STEG (5) | Objective | Client wants MORE income — willing to accept call |
| RA STEG (7) | Complexity | Exceeds cap |
| IR Callable (5) | Asset | Single rate, not CMS spread |

**Recommendation:** Callable STEG (6) — higher leverage ratio than Vanilla STEG, compensated by issuer call right.

**Why This Wins:**
- Higher leverage on CMS spread = higher coupon when curve is steep
- Call feature compensates client with better terms (leverage, floor, cap)
- 100% capital protection maintained

**Ladder:**
1. Vanilla STEG (5) — no call risk, lower leverage
   ↑ If coupon insufficient: accept call risk
2. Callable STEG (6) — higher leverage, issuer callable

**Common Mistake:** Ignoring the "call when it's best for the issuer" dynamic. The issuer calls when the curve steepens significantly — exactly when the client wants to hold. The high coupon periods are the ones you lose.

**Regime Note:** In persistently steep curve environments, Callable STEG gets called quickly. If client needs long-duration income, Vanilla STEG is more reliable.

---

### Scenario 3.4: Income With Target Exit

**Client says:** "I want income but with a total return target. Once I've earned enough, I'm happy to exit."

**Persona:** Sophisticated. No complexity cap.

**Narrowing:** Objective → Income | Cash Flow → Periodic + target | Asset → Rates | Regime → Steepening | Risk → Zero capital + path risk | Complexity → ≤8

**Candidates:** TARN STEG (8)

**Rejected:**

| Product | Step | Reason |
|---------|:----:|--------|
| Vanilla STEG (5) | Objective | No target — holds to maturity regardless |
| Callable STEG (6) | Objective | Call is issuer's decision, not target-based |
| RA STEG (7) | Objective | No target feature |

**Recommendation:** TARN STEG (8) — cumulative coupon triggers early redemption once target reached.

**Why This Wins:**
- Only product with a target redemption feature in the STEG family
- Locks in total return once target met — no risk of giving back gains
- 100% principal protection if target not reached by maturity

**Ladder:**
1. Vanilla STEG (5) — no target, no cap
   ↑ If client wants defined total return: escalate
2. Callable STEG (6) — issuer may call (uncertain timing)
   ↑ If client wants CLIENT-driven exit: escalate
3. TARN STEG (8) — target triggers automatic redemption

**Common Mistake:** Assuming the target will be reached. In flat curve environments, the TARN STEG may reach maturity without ever hitting the target — the client holds a complex product for 10 years earning minimal coupon.

**Regime Note:** TARN STEG is a steepening bet with a profit-taking mechanism. In flat curve environments, it becomes an expensive way to earn near-zero income.

---

### Scenario 3.5: Accumulated Coupon Recovery

**Client says:** "I want income, and if I miss coupons in bad periods, I want them back when markets recover."

**Persona:** PB. Complexity ≤7.

**Narrowing:** Objective → Income | Cash Flow → Contingent + cumulative | Asset → Equity | Regime → Volatile with recovery expectation | Risk → Conditional | Complexity → ≤7

**Candidates:** SNOW (7)

**Rejected:**

| Product | Step | Reason |
|---------|:----:|--------|
| Phoenix (6) | Objective | Memory feature recovers ONE missed coupon — SNOW recovers ALL |
| RC (3) | Objective | No coupon recovery mechanism |
| Digital (4) | Objective | Binary — no accumulation |

**Recommendation:** SNOW (7) — snowball coupon accumulates missed payments. On recovery, all missed coupons paid in a single large payment.

**Why This Wins:**
- Unique cumulative coupon mechanism — missed coupons are not lost but deferred
- Recovery payment can be very large (6+ missed coupons paid at once)
- Autocall feature provides early exit once market recovers

**Ladder:**
1. Phoenix (6) — memory feature recovers 1 missed coupon per observation
   ↑ If client wants FULL cumulative recovery: escalate
2. SNOW (7) — all missed coupons accumulate and pay on recovery

**Common Mistake:** Assuming the snowball will always pay out. If the market stays below the barrier until maturity, the snowball accumulates to a large number that is never paid — plus the client faces principal loss.

**Regime Note:** SNOW requires a recovery view. In sustained bear markets, the accumulated coupon is meaningless. Use SNOW only when the client believes volatility is temporary.

---

## Category 4 — Rates & Inflation

*"I have a view on interest rates or the yield curve."*

---

### Scenario 4.1: Hedge Floating Rate Exposure

**Client says:** "I have floating rate debt and want to fix my interest costs."

**Persona:** Institutional.

**Narrowing:** Objective → Hedging | Cash Flow → Fixed/floating exchange | Asset → Rates | Regime → Any | Risk → Mark-to-market | Complexity → ≤3

**Candidates:** IRS (3), VLSP (2)

**Rejected:**

| Product | Step | Reason |
|---------|:----:|--------|
| STEG (5) | Objective | CMS spread product, not a hedge |
| XCCY (5) | Asset | Cross-currency — client's exposure is single-currency |
| IR Callable (5) | Objective | Structured note, not a hedge |

**Selection:**

| Dimension | IRS (3) | VLSP (2) |
|-----------|---------|----------|
| Mechanism | Fixed-for-floating exchange | Enhanced IRS with additional features |
| Complexity | Standard derivative | Simplest customized swap |
| Liquidity | Most liquid OTC derivative globally | Less liquid |
| Customization | Standard terms | Bespoke features available |

**Recommendation:** IRS (3) — the global standard for rate hedging.

**Why This Wins:**
- Most liquid OTC derivative — tight spreads, deep market
- Exact hedge for floating-rate exposure
- Universally understood by all counterparties

**Ladder:**
1. VLSP (2) — enhanced IRS for specific customization
   ↑ If standard terms sufficient: prefer more liquid option
2. IRS (3) — global standard

**Common Mistake:** Using a STEG note as a "rate hedge." STEG is a leveraged CMS spread bet — it is a directional view, not a hedge. Rate hedging requires IRS.

**Regime Note:** Always appropriate when the objective is hedging. IRS pricing reflects market-implied forward rates.

---

### Scenario 4.2: Structured Rate Exposure With Call

**Client says:** "I want above-market fixed income from a rate-linked note. I accept the issuer may call."

**Persona:** Institutional (Insurance/Pension).

**Narrowing:** Objective → Income | Cash Flow → Fixed coupon (enhanced) | Asset → Rates | Risk → Zero capital + call risk | Complexity → ≤5

**Candidates:** IR Callable (5)

**Rejected:**

| Product | Step | Reason |
|---------|:----:|--------|
| IRS (3) | Cash Flow | Swap — no enhanced fixed coupon |
| Vanilla STEG (5) | Asset | CMS spread, not fixed rate |
| NCRA (6) | Complexity | Range accrual adds complexity beyond need |

**Recommendation:** IR Callable (5) — enhanced fixed coupon in exchange for issuer call right.

**Why This Wins:**
- Higher fixed coupon than comparable bonds — funded by selling swaption to issuer
- 100% capital protection at maturity
- Standard institutional product for insurance/pension ALM

**Ladder:**
1. Plain bond — base rate
   ↑ If yield insufficient: accept call risk
2. IR Callable (5) — enhanced yield, issuer callable

**Common Mistake:** Not stress-testing the call scenario. If rates fall, the issuer calls and the client must reinvest at lower rates. The "enhanced yield" disappears on reinvestment.

**Regime Note:** In rising rate environments, IR Callable is unlikely to be called — client gets enhanced yield for full term. In falling rate environments, expect early call.

---

### Scenario 4.3: Zero-Coupon Rate Growth for Liability Matching

**Client says:** "I need a rate-linked product that matches my future liability at a specific date."

**Persona:** Institutional (Pension).

**Narrowing:** Objective → Growth (liability matching) | Cash Flow → Zero coupon | Asset → Rates | Regime → Any | Risk → Duration risk | Complexity → ≤4

**Candidates:** ZCL (4)

**Rejected:**

| Product | Step | Reason |
|---------|:----:|--------|
| PPN (2) | Asset | Equity-linked, not rate-linked |
| IR Callable (5) | Cash Flow | Pays coupons — client needs zero-coupon for matching |
| IRS (3) | Objective | Swap — no principal matching |

**Recommendation:** ZCL (4) — zero-coupon rate-linked note. Grows to par at maturity, matching future liability.

**Why This Wins:**
- Zero-coupon structure exactly matches a future liability payment
- Rate-linked return provides inflation/rate protection
- 100% principal at maturity

**Ladder:**
1. ZCB (plain zero-coupon bond) — fixed growth to par
   ↑ If need rate-linked return: escalate
2. ZCL (4) — rate-linked zero-coupon

**Common Mistake:** Ignoring duration risk. ZCL has very long duration sensitivity. A 1% rate move can cause 10%+ MTM swing on a 10-year ZCL. The product matches liability at maturity but fluctuates before.

**Regime Note:** ZCL is always appropriate for liability matching regardless of rate view. The matching benefit is at maturity, not during the life.

---

### Scenario 4.4: Range Accrual Rate Income

**Client says:** "I believe rates will stay in a band. I want income that accrues each day they stay in range."

**Persona:** Institutional / Sophisticated.

**Narrowing:** Objective → Income | Cash Flow → Accrual | Asset → Rates | Regime → Range-bound | Risk → Zero capital, coupon at risk | Complexity → ≤7

**Candidates:** NCRA (6), CRA SRT (7)

**Rejected:**

| Product | Step | Reason |
|---------|:----:|--------|
| Digital CF (5) | Cash Flow | Periodic binary, not daily accrual |
| Vanilla STEG (5) | Regime | Directional steepener, not range-bound |
| CRA ELN (6) | Asset | Equity-linked range accrual |

**Selection:**

| Dimension | NCRA (6) | CRA SRT (7) |
|-----------|----------|-------------|
| Accrual | Daily, based on rate in range | Daily + callable |
| Coupon | High (range accrual premium) | Highest (range + call premium) |
| Call risk | None | Issuer callable |
| Protection | 100% | 100% |

**Recommendation:** NCRA (6) — pure range accrual without call risk.

**Why This Wins:**
- Highest daily accrual coupon among non-callable rate products
- 100% principal protection — risk is purely on coupon amount
- No call risk means full term exposure to range accrual

**Ladder:**
1. Digital CF (5) — periodic binary rate coupon
   ↑ If client wants daily accrual: escalate
2. NCRA (6) — daily range accrual, no call
   ↑ If accept call risk for higher coupon: escalate
3. CRA SRT (7) — range accrual + callable = maximum coupon

**Common Mistake:** Setting the range to maximize coupon rate without considering breakout probability. The highest-quoted coupon has the narrowest range — and the highest chance of earning zero.

**Regime Note:** Range accrual products work in low-vol rate environments. In trending rate environments (hiking or cutting cycles), rates leave the range and coupon drops to zero.

---

### Scenario 4.5: Digital Rate Coupon

**Client says:** "I want a rate-linked coupon that pays if rates are above a certain level."

**Persona:** Institutional.

**Narrowing:** Objective → Income | Cash Flow → Binary periodic | Asset → Rates | Regime → Mildly bullish on rates | Risk → Zero capital | Complexity → ≤5

**Candidates:** Digital CF (5)

**Rejected:**

| Product | Step | Reason |
|---------|:----:|--------|
| NCRA (6) | Complexity | Daily accrual adds complexity |
| Vanilla STEG (5) | Asset | CMS spread, not single rate |
| Digital (4) | Asset | Equity-linked digital |

**Recommendation:** Digital CF (5) — binary cap/floor rate coupon. Above strike = full coupon. Below = zero.

**Why This Wins:**
- Clean digital payoff on a single rate reference
- 100% capital protection
- Simpler than range accrual (single condition vs range)

**Ladder:**
1. Plain FRN — floating rate coupon
   ↑ If client wants above-market binary coupon: escalate
2. Digital CF (5) — digital rate coupon

**Common Mistake:** Confusing digital cap-floor with range accrual. Digital CF checks one condition once per period. Range accrual checks every day. Different risk profiles — digital has jump risk at the strike.

**Regime Note:** Digital CF works when the rate is comfortably above the strike. When rates are near the strike, the P&L becomes extremely sensitive to small moves.

---

## Category 5 — Credit Exposure

*"I want credit spread exposure."*

---

### Scenario 5.1: Single-Name Funded Credit Exposure

**Client says:** "I want to earn credit spread on a specific corporate. I prefer a funded note."

**Persona:** Institutional.

**Narrowing:** Objective → Credit income | Cash Flow → Coupon (credit spread) | Asset → Credit (single name) | Risk → Credit event = principal loss | Complexity → ≤5

**Candidates:** CLN (4), CDS (5)

**Rejected:**

| Product | Step | Reason |
|---------|:----:|--------|
| FTD (7) | Complexity/Risk | Basket — client wants single-name |
| Skew CLN (5) | Objective | Non-linear recovery — client wants standard |
| CDO (10) | Complexity | Portfolio product, not single-name |

**Selection:**

| Dimension | CLN (4) | CDS (5) |
|-----------|---------|---------|
| Format | Funded (note) | Unfunded (swap) |
| ISDA needed | No | Yes |
| Capital treatment | Note on balance sheet | Off-balance-sheet |
| Counterparty risk | Issuer + reference name | Reference name only |

**Recommendation:** CLN (4) — funded note format, no ISDA required, simpler for institutional credit investors.

**Why This Wins:**
- Funded format = cash investment, no ISDA documentation needed
- Simpler legal structure than CDS
- Standard note booking — fits existing infrastructure

**Ladder:**
1. Corporate bond — direct credit exposure
   ↑ If specific credit exposure not available in bond market: escalate
2. CLN (4) — synthetic credit via note
   ↑ If unfunded format preferred: escalate
3. CDS (5) — unfunded credit swap

**Common Mistake:** Ignoring double credit risk in CLN. The investor is exposed to BOTH the reference name AND the issuing bank. If either defaults, principal is at risk.

**Regime Note:** Wide credit spreads = high CLN premium. Tight spreads = low compensation for credit risk. Timing matters.

**Desk Note:** CLN provides funding advantage to the desk — client's cash funds the note, reducing desk funding costs.

---

### Scenario 5.2: Asymmetric Credit Payoff

**Client says:** "I have a view on recovery rates for a specific credit. I want exposure to that view."

**Persona:** Institutional / Sophisticated.

**Narrowing:** Objective → Credit (recovery view) | Asset → Credit | Risk → Credit event + recovery uncertainty | Complexity → ≤5

**Candidates:** Skew CLN (5), CDS (5)

**Rejected:**

| Product | Step | Reason |
|---------|:----:|--------|
| CLN (4) | Objective | Linear recovery — client wants non-linear payoff |
| FTD (7) | Objective | Basket — client has single-name view |
| NTD (8) | Complexity/Objective | Multi-name basket |

**Selection:**

| Dimension | Skew CLN (5) | CDS (5) |
|-----------|-------------|---------|
| Recovery exposure | Non-linear — payoff depends on actual recovery rate | Linear — fixed recovery assumption |
| View expression | Pays more/less based on recovery outcome | Binary credit event trigger |

**Recommendation:** Skew CLN (5) — unique product for recovery rate views.

**Why This Wins:**
- Only product that provides direct exposure to recovery rate uncertainty
- Allows expression of view that market-implied recovery is wrong
- Same funded format as CLN but with skewed payoff

**Ladder:**
1. CLN (4) — standard linear credit exposure
   ↑ If client has specific recovery view: escalate
2. Skew CLN (5) — non-linear recovery-dependent payoff

**Common Mistake:** Confusing Skew CLN with leveraged CLN. Skew CLN doesn't multiply credit exposure — it changes the SHAPE of the payoff based on recovery rate.

**Regime Note:** Skew CLN is most valuable when market-implied recovery rates diverge from client's fundamental analysis.

---

### Scenario 5.3: Basket First-to-Default Exposure

**Client says:** "I want to earn premium on a basket of credits. I accept the first-to-default risk."

**Persona:** Sophisticated.

**Narrowing:** Objective → Credit income (basket) | Asset → Credit (multi-name) | Risk → First default triggers full loss | Complexity → ≤7

**Candidates:** FTD (7)

**Rejected:**

| Product | Step | Reason |
|---------|:----:|--------|
| CLN (4) | Objective | Single-name, not basket |
| NTD (8) | Complexity | Higher complexity for Nth-default |
| CDO (10) | Complexity | Portfolio tranching is different product |

**Recommendation:** FTD (7) — premium from selling first-to-default protection on a credit basket.

**Why This Wins:**
- Highest single-payment credit premium (compensates for first-default risk)
- Basket diversification provides some protection — all 5 names must be separately analysed
- Standard basket credit product for sophisticated credit investors

**Ladder:**
1. CLN (4) — single-name credit
   ↑ If client wants higher premium via basket: escalate
2. FTD (7) — first-to-default basket
   ↑ If client wants protection against early defaults: escalate
3. NTD (8) — Nth-to-default (2nd, 3rd default trigger)

**Common Mistake:** Assuming basket diversification reduces FTD risk. In FTD, LOW correlation INCREASES risk — independent defaults mean higher probability of at least one default. This is the opposite of equity diversification.

**Regime Note:** In high correlation environments, FTD risk drops (all names default together or none do). In low correlation, FTD risk rises sharply.

---

### Scenario 5.4: Basket Nth-to-Default Exposure

**Client says:** "I want the higher premium of basket credit but with protection against the first default."

**Persona:** Sophisticated.

**Narrowing:** Objective → Credit income (protected basket) | Asset → Credit (multi-name) | Risk → Nth default | Complexity → ≤8

**Candidates:** NTD (8)

**Rejected:**

| Product | Step | Reason |
|---------|:----:|--------|
| FTD (7) | Objective | First default triggers loss — client wants protection against first |
| CDO (10) | Complexity | Portfolio tranching |
| CLN (4) | Objective | Single-name |

**Recommendation:** NTD (8) — Nth-to-default note. Client survives first N-1 defaults; only the Nth triggers loss.

**Why This Wins:**
- Protection against first (or first few) defaults — junior tranche absorbs initial losses
- Higher premium than single-name CLN due to basket + correlation risk
- Explicit attachment point: client knows exactly when loss starts

**Ladder:**
1. FTD (7) — first default triggers loss (highest premium)
   ↑ If client wants first-default protection: escalate to higher attachment
2. NTD (8) — Nth default trigger (lower premium but safer)

**Common Mistake:** Ignoring correlation reversal. In NTD, HIGH correlation INCREASES risk (opposite of FTD). When correlation rises, all names tend to default together — the "protection" of the first N-1 defaults evaporates.

**Regime Note:** NTD is the mirror image of FTD on correlation. Understanding this is mandatory before trading.

---

### Scenario 5.5: Tranched Portfolio Credit

**Client says:** "I need exposure to a specific attachment point in a credit portfolio."

**Persona:** Institutional / Sophisticated. No complexity cap.

**Narrowing:** Objective → Credit (tranched) | Asset → Credit (portfolio) | Risk → Losses reach attachment | Complexity → 10

**Candidates:** CDO (10)

**Rejected:**

| Product | Step | Reason |
|---------|:----:|--------|
| FTD (7) | Objective | Single tranche — CDO provides specific attachment point |
| NTD (8) | Objective | Basket, not portfolio |
| CLN (4) | Objective | Single name, not portfolio |

**Recommendation:** CDO (10) — synthetic CDO tranche note. Client selects attachment and detachment points on a portfolio.

**Why This Wins:**
- Only product providing exposure to a specific loss tranche of a credit portfolio
- Equity tranche (0–3%) for maximum leverage; senior tranche (12–22%) for investment-grade-like exposure
- Essential product for bank capital relief trades

**Ladder:** N/A — CDO is the only product at this level. No simpler substitute provides tranched portfolio credit.

**Common Mistake:** Using equity tranche correlation assumptions for senior tranches. Equity and senior tranches have OPPOSITE correlation sensitivity. This is the "correlation smile" — the single most tested concept in structured credit interviews.

**Regime Note:** CDO pricing is driven by base correlation, not just spread levels. In spread widening events, correlation typically increases — equity tranches benefit, senior tranches suffer.

**Desk Note:** CDO margin is the highest in the credit universe but requires sophisticated correlation modelling. Model risk is material.

---

## Category 6 — Volatility Strategies

*"I want to trade or hedge volatility."*

---

### Scenario 6.1: Pure Volatility Exposure

**Client says:** "I want direct exposure to realized volatility. I have a vol view."

**Persona:** Sophisticated (long vol) / Institutional (hedge).

**Narrowing:** Objective → Vol trading | Asset → Volatility | Risk → Defined (VO) or convex (VarSwap) | Complexity → depends on persona

**Candidates:** VO (3), VarSwap (7)

**Rejected:**

| Product | Step | Reason |
|---------|:----:|--------|
| RC (3) | Objective | Embedded vol selling — not pure vol exposure |
| WOAC (8) | Objective | Correlation product, not pure vol |
| Phoenix (6) | Objective | Autocall — vol is secondary |

**Selection:**

| Dimension | VO (3) | VarSwap (7) |
|-----------|--------|-------------|
| Vol exposure | Asymmetric (limited loss long) | Pure variance (convex, unlimited short risk) |
| Premium | Paid upfront | No premium (MTM swap) |
| Payoff | Non-linear | Convex in variance (squared vol) |
| Complexity | Simple | High — convexity traps |

**Recommendation:** VO (3) for directional vol view with limited loss. VarSwap (7) ONLY for sophisticated clients who understand convexity.

**Why This Wins:**
- VO: defined maximum loss (premium), unlimited upside — cleanest vol bet
- VarSwap: direct variance exposure but CONVEX — short sellers face unlimited loss
- Choice between these two separates retail from institutional vol trading

**Ladder:**
1. VO (3) — limited loss, asymmetric payoff
   ↑ If client needs variance (not vol) and understands convexity: escalate
2. VarSwap (7) — pure variance swap (squared exposure)

**Common Mistake:** Shorting VarSwap as "selling vol." VarSwap convexity means a 2× vol move produces 4× loss. Short VarSwap is the product that destroyed XIV and similar vehicles in the 2018 Volmageddon event.

**Regime Note:** Long vol works when implied vol is cheap relative to expected realized. Short vol works when implied is rich. The difficulty is knowing which regime you're in.

**Desk Note:** Desk earns convexity premium from VarSwap clients who misunderstand the squared payoff.

---

### Scenario 6.2: Option on a Structured Product

**Client says:** "I want the right — but not the obligation — to enter an RC at a future date."

**Persona:** Sophisticated.

**Narrowing:** Objective → Deferred entry | Asset → Equity (via RC) | Risk → Premium loss | Complexity → ≤5

**Candidates:** Opt-on-RC (5)

**Rejected:**

| Product | Step | Reason |
|---------|:----:|--------|
| RC (3) | Objective | Immediate entry — client wants optionality on entry |
| VO (3) | Objective | Option on underlying, not on RC structure |
| Phoenix (6) | Complexity | No deferred entry mechanism |

**Recommendation:** Opt-on-RC (5) — compound option giving right to enter RC at a future date on predetermined terms.

**Why This Wins:**
- Only product providing optionality on entry into a structured product
- Premium is the maximum loss — no obligation to enter the RC
- Useful when client expects better entry conditions in the future

**Ladder:**
1. VO (3) — option on underlying asset directly
   ↑ If client wants optionality on entering a STRUCTURED product: escalate
2. Opt-on-RC (5) — compound option on RC

**Common Mistake:** Treating Opt-on-RC as a leveraged RC. The compound option has two layers of Greeks — the outer option and the inner RC each have their own sensitivities. Hedging is significantly more complex.

**Regime Note:** Opt-on-RC is most valuable when implied vol is high (option is expensive to buy outright) but expected to fall (making future RC entry cheaper).

---

### Scenario 6.3: Multi-Stock Correlation via Autocall

**Client says:** "I want to earn premium from selling correlation risk on a basket of stocks."

**Persona:** PB / Sophisticated.

**Narrowing:** Objective → Yield (correlation premium) | Asset → Equity basket | Regime → Range-bound, moderate correlation | Risk → Worst stock drives outcome | Complexity → ≤8

**Candidates:** WOAC (8)

**Rejected:**

| Product | Step | Reason |
|---------|:----:|--------|
| Phoenix (6) | Objective | Single-stock autocall — no correlation premium |
| FTD (7) | Asset | Credit basket, not equity |
| SNOW (7) | Objective | Snowball — no explicit correlation exposure |

**Recommendation:** WOAC (8) — worst-of autocallable. Coupon funded by selling correlation risk across basket of 3–5 stocks.

**Why This Wins:**
- Highest coupon in the ELN universe (15–25%) due to correlation premium
- Autocall provides early exit if all stocks perform
- Most traded complex retail product in APAC and Europe

**Ladder:**
1. Phoenix (6) — single-stock autocall, lower coupon
   ↑ If coupon insufficient and client accepts worst-of risk: escalate
2. WOAC (8) — multi-stock worst-of, maximum coupon

**Common Mistake:** Thinking basket = diversification. In WOAC, the WORST stock drives all outcomes. A basket of 5 stocks doesn't reduce risk — it multiplies the chance that at least one stock breaches the barrier.

**Regime Note:** WOAC suffers when correlations drop (stocks diverge). In dispersion events, the worst stock decouples from the others and breaches barriers independently.

**Desk Note:** WOAC is the most profitable retail structured product for the desk. Correlation premium is large and difficult for clients to price independently.

---

### Scenario 6.4: Embedded Volatility Selling

**Client says:** "I want to earn from selling volatility but through a simple, familiar structure."

**Persona:** PB. Complexity ≤3.

**Narrowing:** Objective → Vol selling (implicit) | Cash Flow → Fixed Income | Asset → Equity | Risk → Conditional | Complexity → ≤3

**Candidates:** RC (3)

**Rejected:**

| Product | Step | Reason |
|---------|:----:|--------|
| VarSwap (7) short | Risk/Complexity | Unlimited loss, convex |
| Phoenix (6) | Complexity | Exceeds cap |
| WOAC (8) | Complexity | Far exceeds cap |

**Recommendation:** RC (3) — embedded short put = implicit vol selling. Client earns premium (coupon) for selling downside risk.

**Why This Wins:**
- Simplest vol-selling structure — bond + short put
- Loss is defined by barrier level (not unlimited like VarSwap short)
- Coupon IS the vol premium — client earns richly when vol is high

**Ladder:** RC is already the simplest vol-selling product. No further simplification possible.

**Common Mistake:** Not recognizing RC as vol selling. When a client buys RC, they are selling a put option. The coupon comes from vol premium. If the client doesn't have a vol view, they shouldn't be trading RC.

**Regime Note:** RC coupon is highest when vol is high (rich put premium). In low-vol, RC coupon is thin — switch to Digital for protected income.

---

## Category 7 — Portfolio Management

*"I need to manage portfolio-level exposures."*

---

### Scenario 7.1: Synthetic Equity Ownership

**Client says:** "I want equity exposure without owning the stock. I need synthetic access."

**Persona:** Institutional (hedge fund / asset manager).

**Narrowing:** Objective → Synthetic access | Cash Flow → Total return exchange | Asset → Equity | Complexity → ≤5

**Candidates:** TRS (5), EqSwap (5)

**Rejected:**

| Product | Step | Reason |
|---------|:----:|--------|
| FWD (2) | Objective | Single-period — client wants ongoing exposure |
| CLN (4) | Asset | Credit-linked, not equity |
| RC (3) | Objective | Yield product, not synthetic ownership |

**Selection:**

| Dimension | TRS (5) | EqSwap (5) |
|-----------|---------|------------|
| Mechanism | Total return of asset vs financing rate | Equity return vs fixed/floating |
| Asset class | Any (equity, credit, bond) | Equity only |
| Flexibility | Broadest — any reference asset | Equity-specific optimizations |
| Typical user | Hedge funds (leverage, short selling) | Asset managers (tracking) |

**Recommendation:** TRS (5) for maximum flexibility. EqSwap (5) for equity-specific.

**Why This Wins:**
- TRS: can reference any asset — equity, bond, index, loan — most versatile
- EqSwap: optimized for equity-specific exposure (dividend, withholding tax)
- Both achieve synthetic ownership without balance sheet impact

**Ladder:**
1. FWD (2) — single-period forward exposure
   ↑ If need ongoing synthetic ownership: escalate
2. EqSwap (5) — equity-specific swap
   ↑ If need multi-asset flexibility: escalate
3. TRS (5) — total return on any reference asset

**Common Mistake:** Using TRS for "no-risk" equity exposure. TRS gives full equity risk — the synthetic owner bears all market, dividend, and corporate action risk. It's just off-balance-sheet.

**Regime Note:** TRS/EqSwap financing rates widen in stressed markets. The "cost of carry" for synthetic exposure can spike during crises.

**Desk Note:** TRS is the primary product for prime brokerage. High revenue, recurring fees.

---

### Scenario 7.2: Commodity Price Hedging

**Client says:** "I'm a producer/consumer and need to lock my commodity price."

**Persona:** Institutional (corporate).

**Narrowing:** Objective → Hedging | Asset → Commodity | Risk → Basis risk | Complexity → ≤4

**Candidates:** CommSwap (4)

**Rejected:**

| Product | Step | Reason |
|---------|:----:|--------|
| FWD (2) | Cash Flow | Single settlement — client needs ongoing hedge |
| IRS (3) | Asset | Rate swap, not commodity |
| TRS (5) | Complexity | More complex than needed |

**Recommendation:** CommSwap (4) — fixed-for-floating commodity swap. Producer locks selling price; consumer locks buying price.

**Why This Wins:**
- Exact hedge for commodity price risk over multiple periods
- No premium — swap exchanges fixed for floating
- Standard product for corporate hedging programs

**Ladder:**
1. FWD (2) — single-period commodity forward
   ↑ If need multi-period hedge: escalate
2. CommSwap (4) — ongoing commodity swap

**Common Mistake:** Ignoring basis risk. The swap references a commodity index (e.g., Brent crude). The client's actual exposure may differ (e.g., WTI or a specific grade). The basis between the two can move independently.

**Regime Note:** Commodity curves shift between contango and backwardation. The forward curve shape affects swap pricing — hedging is cheaper in contango for producers.

---

### Scenario 7.3: Cross-Currency Debt Management

**Client says:** "I issued debt in EUR but my revenue is in USD. I need to manage the FX mismatch."

**Persona:** Institutional (corporate / sovereign).

**Narrowing:** Objective → Hedging (FX + rate) | Asset → Cross-currency | Risk → FX + rate + basis | Complexity → ≤5

**Candidates:** XCCY (5)

**Rejected:**

| Product | Step | Reason |
|---------|:----:|--------|
| IRS (3) | Asset | Single currency — doesn't address FX |
| FWD (2) | Cash Flow | Single-period FX — doesn't match debt coupons |
| DCI (3) | Objective | Yield product, not hedge |

**Recommendation:** XCCY (5) — cross-currency swap. Converts EUR debt to synthetic USD debt by exchanging principals and coupons.

**Why This Wins:**
- Complete hedge: converts both principal and interest rate exposure between currencies
- Matches debt maturity and coupon schedule exactly
- Standard corporate treasury product for foreign-currency debt management

**Ladder:**
1. FX forward strip — individual forwards for each coupon date
   ↑ If need principal exchange and full restructuring: escalate
2. XCCY (5) — single swap converting entire debt structure

**Common Mistake:** Ignoring cross-currency basis. XCCY pricing includes a basis spread that can move 50+ bps. This basis is a separate risk factor beyond FX and rates.

**Regime Note:** Cross-currency basis widens in USD funding stress events. Hedging costs spike when dollar demand is highest.

---

### Scenario 7.4: Discounted Share Accumulation

**Client says:** "I want to buy shares at below-market prices on a schedule. I accept the risk of buying more if the stock falls."

**Persona:** Sophisticated.

**Narrowing:** Objective → Accumulation | Asset → Equity | Risk → Geared downside (2× below strike) | Complexity → ≤6

**Candidates:** ACCUM (6)

**Rejected:**

| Product | Step | Reason |
|---------|:----:|--------|
| FWD (2) | Objective | No discount, no gearing |
| EqSwap (5) | Objective | Synthetic — client wants physical shares |
| TRS (5) | Objective | Total return swap, not share accumulation |

**Recommendation:** ACCUM (6) — daily accumulator. Buys shares at discount when above strike. Buys 2× shares at discount when below strike.

**Why This Wins:**
- Guaranteed discount to market price on every accumulation day
- KO barrier terminates if stock rallies too far (limits bank's exposure)
- Systematic accumulation replaces ad hoc buying

**Ladder:**
1. FWD (2) — buy at today's price, settled later
   ↑ If client wants ongoing discounted accumulation: escalate
2. ACCUM (6) — daily discounted accumulation with gearing

**Common Mistake:** Using ACCUM as a hedge. The 2× gearing below strike means the client buys DOUBLE the shares when the stock is falling — this is a leveraged directional bet, not a hedge. The client must want to own more shares at lower prices.

**Regime Note:** ACCUM works when the stock is range-bound above strike. In sharp declines, 2× gearing creates forced buying at the worst time.

**Desk Note:** ACCUM is highly profitable for the desk due to daily barrier monitoring and gearing premium.

---

### Scenario 7.5: Systematic Share Disposal

**Client says:** "I have a large stock position and want to sell at above-market prices on a schedule."

**Persona:** Sophisticated.

**Narrowing:** Objective → Disposal | Asset → Equity | Risk → Geared opportunity cost (2× above strike) | Complexity → ≤6

**Candidates:** DECUM (6)

**Rejected:**

| Product | Step | Reason |
|---------|:----:|--------|
| FWD (2) | Objective | Single sale, no premium |
| EqSwap (5) | Objective | Synthetic — client wants physical disposal |
| ACCUM (6) | Objective | Accumulation, not disposal |

**Recommendation:** DECUM (6) — daily decumulator. Sells shares at premium when below strike. Sells 2× shares at premium when above strike.

**Why This Wins:**
- Guaranteed premium to market price on every disposal day
- Systematic liquidation of large positions without market impact
- Mirror image of ACCUM — same mechanics, opposite direction

**Ladder:**
1. FWD (2) — sell at today's price
   ↑ If client wants ongoing premium disposal: escalate
2. DECUM (6) — daily premium disposal with gearing

**Common Mistake:** Not understanding the gearing reversal. If the stock rallies, the client sells 2× shares at a premium — but misses the upside on those extra shares. The "premium" becomes an opportunity cost in rallying markets.

**Regime Note:** DECUM works when stock is range-bound. In strong rallies, the 2× gearing forces selling at the worst time (relative to holding).

---

## Category 8 — Building Blocks & Specialist

*"I need a fundamental building block or specialist product."*

---

### Scenario 8.1: Forward Price Lock

**Client says:** "I need to lock today's price for a future transaction."

**Persona:** Institutional / Corporate.

**Narrowing:** Objective → Price lock | Risk → Unlimited (symmetric) | Complexity → ≤2

**Candidates:** FWD (2)

**Rejected:**

| Product | Step | Reason |
|---------|:----:|--------|
| IRS (3) | Asset | Rate swap, not price lock |
| VO (3) | Risk | Asymmetric — premium + limited loss, client wants exact lock |
| ACCUM (6) | Risk | Geared — not a pure hedge |

**Recommendation:** FWD (2) — linear payoff, no optionality, purest price-locking derivative.

**Why This Wins:**
- Zero basis risk — exact price lock at the forward price
- No premium — symmetric payoff
- Foundation of all derivative pricing

**Ladder:** N/A — FWD is Tier 1. No simpler derivative exists.

**Common Mistake:** Using ACCUM/DECUM as "discounted forwards." Both have 2× gearing — they are leveraged directional bets, not hedges. A hedge should not amplify exposure on one side.

**Regime Note:** Forward pricing reflects carry (dividends, funding, storage). No directional view required — it's a mathematical relationship.

---

### Scenario 8.2: Deposit-Based Structured Return

**Client says:** "I want something safer than a note. I want deposit insurance."

**Persona:** Retail.

**Narrowing:** Objective → Protection | Cash Flow → Growth | Risk → Zero (deposit insurance) | Complexity → ≤2

**Candidates:** SD (2)

**Rejected:**

| Product | Step | Reason |
|---------|:----:|--------|
| PPN (2) | Risk | Note format — no deposit insurance |
| RC (3) | Risk | Conditional protection |
| Digital (4) | Complexity | Exceeds Retail preference for simplest product |

**Recommendation:** SD (2) — structured deposit. Bank deposit with embedded call option. Protected by deposit insurance (up to national limit).

**Why This Wins:**
- Deposit insurance — protection beyond issuer credit
- Simplest structured product in the universe (Complexity 2)
- Available through bank branches — widest distribution

**Ladder:** SD is the simplest product. No further simplification possible.

**Common Mistake:** Confusing SD with PPN. Both offer 100% protection + equity participation. The difference: SD has deposit insurance. PPN is a note — if the bank defaults, the "guarantee" fails.

**Regime Note:** SD participation rates are lower than PPN (deposit insurance has a cost). In high-rate environments, PPN may be more attractive if the client accepts note format.

---

### Scenario 8.3: Retail Leveraged Directional Exposure

**Client says:** "I want to make a leveraged directional bet on equities. I accept I can lose my entire investment."

**Persona:** Retail / PB.

**Narrowing:** Objective → Directional leverage | Cash Flow → Growth | Asset → Equity | Risk → Total premium loss | Complexity → ≤4

**Candidates:** Warrant (3), ELO (3), Booster (4)

**Rejected:**

| Product | Step | Reason |
|---------|:----:|--------|
| ACCUM (6) | Complexity/Risk | Geared accumulation — different product |
| VarSwap (7) | Complexity | Volatility, not directional |
| Phoenix (6) | Complexity | Income product with autocall |

**Selection:**

| Dimension | Warrant (3) | ELO (3) | Booster (4) |
|-----------|-------------|---------|-------------|
| Format | Exchange-listed | OTC note (retail wrapper) | OTC note |
| Leverage | High (premium < notional) | Moderate | Leveraged up, full down |
| Max loss | Premium | Premium | Full notional below strike |
| Upside | Unlimited (call) or geared | Asymmetric | Leveraged but capped |

**Recommendation:** Warrant (3) for exchange-traded. ELO (3) for OTC retail wrapper. Booster (4) for leveraged participation with cap.

**Why This Wins:**
- Warrant: exchange-listed, regulated, transparent pricing — best for retail
- ELO: same option exposure but in a note wrapper for bank distribution
- Booster: leveraged upside (150%+) but capped — defined risk/return profile

**Ladder:**
1. VO (3) — institutional vanilla option (if accessible)
   ↑ If need retail format: escalate
2. Warrant (3) / ELO (3) — retail option wrappers
   ↑ If want leveraged note format: escalate
3. Booster (4) — leveraged participation note (no protection)

**Common Mistake:** Treating Booster as a "protected" product. Booster has ZERO capital protection — below the strike, the client takes full equity loss. The "booster" refers to upside leverage, not downside protection.

**Regime Note:** Leveraged directional products work when the view is correct. They amplify both gains AND losses. Only appropriate when the client has genuine directional conviction.

---

### Scenario 8.4: Maximum Multi-Stock Yield for Private Banking

**Client says:** "I want the absolute highest coupon available on an equity-linked note. I understand the risks."

**Persona:** PB / Sophisticated.

**Narrowing:** Objective → Maximum yield | Cash Flow → Contingent Income | Asset → Equity basket | Risk → Worst stock = total loss | Complexity → ≤8

**Candidates:** WOAC (8)

**Rejected:**

| Product | Step | Reason |
|---------|:----:|--------|
| Phoenix (6) | Objective | Single stock — lower coupon than worst-of |
| DKIP (7) | Objective | Single stock digital — lower correlation premium |
| SNOW (7) | Objective | Snowball — cumulative, not maximum current coupon |

**Recommendation:** WOAC (8) — worst-of autocallable on 3–5 stock basket. Highest coupon in the structured products universe (15–25%).

**Why This Wins:**
- Coupon of 15–25% is funded by selling correlation + vol on a basket
- Autocall provides early exit if all stocks perform above trigger
- The most traded complex retail/PB product globally

**Ladder:**
1. RC (3) — single stock, 8–12% coupon
   ↑ If coupon insufficient: escalate
2. Phoenix (6) — single stock autocall, 10–15% contingent coupon
   ↑ If still insufficient and client accepts worst-of risk: escalate
3. WOAC (8) — worst-of basket, 15–25% coupon

**Common Mistake:** Underestimating worst-of risk. A basket of 5 blue-chip stocks feels diversified. It's not. The WORST stock drives all outcomes. If even one stock drops 35%+, the barrier breaches and the client faces principal loss on the full notional.

**Regime Note:** WOAC suffers most in dispersion events — when stocks decorrelate and the worst stock drops independently. In high-correlation environments (all stocks move together), WOAC is safer.

---

# Part 3: Anti-Patterns

**18 "When NOT To" Rules — 3 Per Family**

---

## ELN Anti-Patterns

### AP-1: "Client Wants Protection" → NOT RC

RC has conditional protection. Below the barrier, the investor takes full equity loss. If the client cannot tolerate any principal loss, use PPN (2) or SD (2). RC is a yield product, not a protection product.

### AP-2: "Client Wants Guaranteed Income" → NOT Phoenix

Phoenix coupon is contingent on the stock staying above the coupon barrier. If the stock drops below, coupon is zero. For guaranteed income, use FCN (6) — fixed coupon paid regardless of performance.

### AP-3: "Client Wants Simplicity" → NOT DKIP

DKIP has three barrier conditions: digital coupon barrier, knock-in put barrier, and autocall trigger. Explaining this to a client requires understanding three simultaneous conditions. For simple digital income, use Digital (4).

---

## Swaps Anti-Patterns

### AP-4: "Client Wants to Sell Vol" → NOT VarSwap Short

VarSwap has convex payoff. Short sellers face unlimited loss — a 2× vol move produces 4× loss. The 2018 Volmageddon event destroyed short vol products overnight. For vol selling with defined risk, use RC (3) — the embedded short put IS vol selling with a barrier floor.

### AP-5: "Client Wants to Hedge Equity" → NOT ACCUM

ACCUM buys 2× shares when the stock falls — this INCREASES equity exposure on the downside. ACCUM is a leveraged accumulation strategy, not a hedge. For equity hedging, use VO (3) long put, EqSwap (5), or FWD (2).

### AP-6: "Client Wants Simple Rate Hedge" → NOT XCCY

XCCY adds FX risk on top of rate risk. If the client's exposure is single-currency, XCCY introduces unnecessary complexity. Use IRS (3) or VLSP (2) for single-currency rate hedging.

---

## SRT Anti-Patterns

### AP-7: "Client Wants Safe Income" → NOT CRA SRT

CRA SRT can earn zero coupon for 10 years. If rates leave the accrual range, every period pays nothing — while principal is returned at maturity, the opportunity cost is a decade of zero income. For safer rate income, use IR Callable (5) with fixed coupon.

### AP-8: "Client Wants Simple Rate Product" → NOT NCRA

NCRA (Non-Callable Range Accrual) involves digital options on rates with daily observation. The "range" concept is simple but the risk is not — near-boundary rates create extreme P&L sensitivity. For simple rate exposure, use IRS (3).

### AP-9: "Client Wants Bond Substitute" → NOT ZCL for Income Seekers

ZCL pays zero coupon. It's a zero-coupon growth product for liability matching, not an income product. Clients seeking bond-like income should use IR Callable (5) or Digital CF (5).

---

## STEG Anti-Patterns

### AP-10: "Curve Will Steepen" → NOT TARN STEG

TARN STEG has a target feature that triggers early redemption once cumulative coupons reach the cap. If the curve steepens slowly, the target may be reached in year 2 — the client gets their money back just as the steepening accelerates. For pure steepening exposure without target termination, use Vanilla STEG (5).

### AP-11: "Client Wants Stable Income" → NOT RA STEG

RA STEG requires a dual condition: the CMS spread must be positive AND within a range. If either condition fails, the coupon is zero. For more stable CMS spread income, use Vanilla STEG (5) — only one condition (spread > 0).

### AP-12: "Client Wants Long-Duration Steepener" → NOT Callable STEG if Duration Matters

Callable STEG will be called by the issuer when the curve steepens significantly — precisely when the client wants to hold. If the client values long-duration exposure, Vanilla STEG (5) is the only non-callable option.

---

## CLN Anti-Patterns

### AP-13: "Client Wants Credit Exposure" → NOT FTD Without Correlation Training

FTD risk depends on correlation between basket names. LOW correlation INCREASES FTD risk (opposite of equity diversification). A client who thinks "5 names = diversified" will be shocked when an independent default triggers full loss. Start with CLN (4) for single-name credit.

### AP-14: "Client Wants High Credit Yield" → NOT CDO for Non-Specialists

CDO requires understanding of: portfolio loss distributions, attachment/detachment points, base correlation, copula models, and tranche sensitivity. Complexity 10. For high credit yield without portfolio modelling, use FTD (7) with correlation education.

### AP-15: "Client Wants Simple Funded Credit" → NOT NTD

NTD (Nth-to-Default) has opposite correlation sensitivity to FTD. Rising correlation INCREASES NTD risk. A client who learned FTD correlation dynamics will apply the wrong intuition to NTD. Start with CLN (4), then FTD (7) with explicit correlation reversal education.

---

## Other Family Anti-Patterns

### AP-16: "Client Wants Low Risk" → NOT WOAC

WOAC coupon is 15–25% because the client is selling correlation risk on a basket. The worst stock out of 3–5 names drives all outcomes. A single stock declining 35% triggers barrier breach on the entire notional. For low-risk yield, use Digital (4) with 100% protection.

### AP-17: "Client Needs Liquidity" → NOT SNOW

SNOW (Snowball) has cumulative path-dependent payoff. Valuing it on the secondary market requires Monte Carlo simulation with hundreds of paths. Bid-ask spreads are wide. For liquid autocallable income, use Phoenix (6) — standardized, actively traded.

### AP-18: "Client Wants Protection With Maximum Upside" → NOT CLIQ for Trending Markets

CLIQ has local caps per period. In a strong trending market, the caps limit return from each period — cumulative return underperforms PPN or direct equity investment. CLIQ outperforms in choppy, mean-reverting markets. For trending bullish view, use PPN (2) or Booster (4).

---

# Part 4: Quick Reference & Replacement Table

## Objective → Top 3 Products

| Client Objective | First Choice | Second Choice | Third Choice |
|-----------------|:------------:|:-------------:|:------------:|
| Full capital protection + equity growth | PPN (2) | SD (2) | SHRK (4) |
| Yield enhancement (equity, bullish) | RC (3) | DRC (3) | KODRC (4) |
| Maximum conditional coupon | Phoenix (6) | WOAC (8) | CRC (5) |
| Guaranteed coupon + autocall | FCN (6) | ICN (3) | Callable STEG (6) |
| Digital coupon (equity) | Digital (4) | DKIP (7) | CRA ELN (6) |
| CMS spread income | Vanilla STEG (5) | Callable STEG (6) | RA STEG (7) |
| Range-bound rate income | NCRA (6) | CRA SRT (7) | Digital CF (5) |
| Rate hedging | IRS (3) | VLSP (2) | XCCY (5) |
| Single-name credit | CLN (4) | CDS (5) | Skew CLN (5) |
| Basket credit | FTD (7) | NTD (8) | CDO (10) |
| Pure volatility exposure | VO (3) | VarSwap (7) | Opt-on-RC (5) |
| Synthetic equity access | TRS (5) | EqSwap (5) | FWD (2) |
| Commodity hedging | CommSwap (4) | FWD (2) | — |
| Cross-currency management | XCCY (5) | IRS (3) | FWD (2) |
| Share accumulation | ACCUM (6) | FWD (2) | — |
| Share disposal | DECUM (6) | FWD (2) | — |
| Leveraged directional (retail) | Warrant (3) | ELO (3) | Booster (4) |
| FX yield enhancement | DCI (3) | SD (2) | — |
| Liability matching | ZCL (4) | PPN (2) | — |
| Snowball recovery income | SNOW (7) | Phoenix (6) | — |
| Periodic gain lock-in | CLIQ (7) | SHRK (4) | PPN (2) |

---

## 49-Product Replacement Table

When the recommended product is unavailable, use the nearest substitute.

**Rule:** At least one substitute is lower or equal complexity.

| Product | Cmplx | Objective | Sub 1 | Sub 2 | Trade-Off |
|---------|:-----:|-----------|:-----:|:-----:|-----------|
| PPN | 2 | Protected growth | SD (2) | Airbag (4) | SD: deposit insurance, lower participation. Airbag: conditional |
| RC | 3 | Yield enhancement | DRC (3) | Digital (4) | DRC: discount not coupon. Digital: protected, binary |
| Phoenix | 6 | Conditional income | FCN (6) | CRC (5) | FCN: guaranteed coupon. CRC: callable, no autocall |
| DRC | 3 | Discount yield | RC (3) | KODRC (4) | RC: coupon not discount. KODRC: KO protection added |
| KODRC | 4 | Protected yield | RC (3) | Airbag (4) | RC: no KO layer. Airbag: cushion not KO |
| CRC | 5 | Callable yield | ICN (3) | Phoenix (6) | ICN: simpler callable. Phoenix: autocall not call |
| Airbag | 4 | Conditional protection | Bonus (4) | PPN (2) | Bonus: min return not cushion. PPN: full protection |
| Bonus | 4 | Min return + upside | Airbag (4) | PPN (2) | Airbag: cushion not guarantee. PPN: zero not min return |
| FCN | 6 | Guaranteed coupon | RC (3) | Phoenix (6) | RC: lower coupon. Phoenix: contingent not guaranteed |
| CRA ELN | 6 | Equity range accrual | Digital (4) | RA STEG (7) | Digital: periodic not daily. RA STEG: rate not equity |
| ICN | 3 | Callable note | CRC (5) | RC (3) | CRC: higher coupon. RC: no call |
| Digital | 4 | Binary equity coupon | RC (3) | CRA ELN (6) | RC: continuous not binary. CRA ELN: range not digital |
| DKIP | 7 | Complex digital | Digital (4) | Phoenix (6) | Digital: no KI capital risk. Phoenix: autocall mechanism |
| Booster | 4 | Leveraged growth | Warrant (3) | PPN (2) | Warrant: option format. PPN: protected, lower leverage |
| Warrant | 3 | Directional leverage | ELO (3) | Booster (4) | ELO: OTC wrapper. Booster: note format, capped |
| IRS | 3 | Rate hedging | VLSP (2) | FWD (2) | VLSP: enhanced features. FWD: single period |
| TRS | 5 | Synthetic ownership | EqSwap (5) | FWD (2) | EqSwap: equity-specific. FWD: single period |
| EqSwap | 5 | Equity swap | TRS (5) | FWD (2) | TRS: multi-asset. FWD: single period |
| VarSwap | 7 | Pure vol | VO (3) | Opt-on-RC (5) | VO: linear vol, limited loss. Opt-on-RC: indirect |
| CDS | 5 | Credit transfer | CLN (4) | FTD (7) | CLN: funded note. FTD: basket, not single-name |
| XCCY | 5 | Cross-currency | IRS (3) | FWD (2) | IRS: single currency. FWD: single period FX |
| CommSwap | 4 | Commodity hedge | FWD (2) | TRS (5) | FWD: single period. TRS: broader but complex |
| VLSP | 2 | Enhanced rate swap | IRS (3) | FWD (2) | IRS: standard terms. FWD: single period |
| IR Callable | 5 | Callable rate note | ZCL (4) | C. STEG (6) | ZCL: no coupon. C.STEG: CMS spread not fixed |
| ZCL | 4 | Zero-coupon rate | PPN (2) | IR Call. (5) | PPN: equity-linked. IR Callable: has coupon |
| NCRA | 6 | Rate range accrual | CRA SRT (7) | Dig. CF (5) | CRA SRT: callable. Digital CF: periodic binary |
| CRA SRT | 7 | Callable range accrual | NCRA (6) | C. STEG (6) | NCRA: no call. C.STEG: spread not range |
| Digital CF | 5 | Digital rate coupon | Digital (4) | NCRA (6) | Digital: equity not rate. NCRA: daily accrual |
| V. STEG | 5 | Curve steepener | C. STEG (6) | IRS (3) | C.STEG: higher yield + call. IRS: hedge not income |
| RA STEG | 7 | Range accrual steepener | V. STEG (5) | CRA ELN (6) | V.STEG: no range. CRA ELN: equity not rates |
| C. STEG | 6 | Callable steepener | V. STEG (5) | IR Call. (5) | V.STEG: no call. IR Callable: fixed not spread |
| TARN STEG | 8 | Target steepener | C. STEG (6) | RA STEG (7) | C.STEG: no target. RA STEG: range not target |
| CLN | 4 | Funded credit | CDS (5) | Skew CLN (5) | CDS: unfunded. Skew: non-linear recovery |
| Skew CLN | 5 | Asymmetric credit | CLN (4) | CDS (5) | CLN: linear recovery. CDS: unfunded |
| FTD | 7 | First-to-default | CLN (4) | NTD (8) | CLN: single-name. NTD: Nth default |
| NTD | 8 | Nth-to-default | FTD (7) | CDO (10) | FTD: first default. CDO: portfolio tranche |
| CDO | 10 | Tranched credit | NTD (8) | FTD (7) | NTD: simpler basket. FTD: single tranche |
| SD | 2 | Deposit protection | PPN (2) | ELO (3) | PPN: note (no deposit ins.). ELO: option wrapper |
| FWD | 2 | Price lock | IRS (3) | CommSwap (4) | IRS: multi-period rate. CommSwap: commodity swap |
| ELO | 3 | Retail option | VO (3) | Warrant (3) | VO: institutional. Warrant: exchange-listed |
| VO | 3 | Vanilla option | ELO (3) | VarSwap (7) | ELO: retail wrapper. VarSwap: variance not vol |
| DCI | 3 | FX deposit yield | RC (3) | SD (2) | RC: equity not FX. SD: no FX view |
| Opt-on-RC | 5 | Deferred RC entry | RC (3) | VO (3) | RC: immediate entry. VO: option on underlying |
| ACCUM | 6 | Share accumulation | FWD (2) | EqSwap (5) | FWD: no gearing. EqSwap: synthetic, no physical |
| DECUM | 6 | Share disposal | FWD (2) | EqSwap (5) | FWD: no gearing. EqSwap: synthetic |
| SHRK | 4 | Barrier-enhanced PPN | PPN (2) | Booster (4) | PPN: no KO cap. Booster: no protection |
| SNOW | 7 | Snowball coupon | Phoenix (6) | WOAC (8) | Phoenix: memory not snowball. WOAC: worst-of basket |
| CLIQ | 7 | Periodic lock-in | PPN (2) | SHRK (4) | PPN: no lock-in. SHRK: KO not periodic |
| WOAC | 8 | Multi-stock yield | Phoenix (6) | SNOW (7) | Phoenix: single stock. SNOW: snowball not worst-of |

---

## Traceability

| Source Artifact | Role in Solutions Manual |
|----------------|------------------------|
| Product DNA Atlas (frozen) | Product features, complexity scores, family assignments |
| Product Comparison Matrix | 12 dimensions, decision trees, fast views, interview priority |
| Learning Dependency Graph | Tier assignments, prerequisite chains |
| Product Evolution Map | Family trees, evolution paths |
| Product Universe Map | 3 graph systems, cross-product navigation |
| Desk Bible v2 §3 per chapter | Client need per product (ground truth) |
| Desk Bible v2 §7 per chapter | Desk economics per product |
| Desk Bible v2 §8 per chapter | Client perspective per product |

---

*Solutions Manual complete. 49 products. 40 scenarios. 18 anti-patterns. 49 replacement mappings. 2026-06-22.*
