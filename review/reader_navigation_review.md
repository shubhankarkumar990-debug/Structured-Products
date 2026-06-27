# Reader Navigation Review

**Date:** 2026-06-20
**Scope:** 33 product chapters + Parts 0-4 foundation
**Framework:** v1.3.1 (FROZEN)
**Purpose:** Design role-based and complexity-based reading paths for the final publication

---

## 1. Beginner Path

**For:** New joiners, interns, career switchers with basic financial literacy.

**Goal:** Build understanding from zero to "can read any chapter in the book."

### Phase 1 — Foundations (Parts 0-2)

| Order | Section | Topic | Est. Time |
|:-----:|---------|-------|:---------:|
| 1 | 0.1-0.5 | Markets, bonds, equities, options basics | 45 min |
| 2 | 0.6-0.10 | Derivatives, structured products overview | 30 min |
| 3 | 1.1-1.3 | Barriers, knock-in, knock-out, digital | 30 min |
| 4 | 1.4-1.6 | Correlation, worst-of, tail risk | 20 min |
| 5 | 1.7-1.8 | Yield curves, CMS, swaptions, benchmark rates | 30 min |
| 6 | 2.1-2.8 | FO/MO/BO, booking, four-leg structure, Murex | 30 min |

### Phase 2 — Simplest Products (Complexity 2-3)

| Order | Chapter | Product | Complexity |
|:-----:|---------|---------|:----------:|
| 7 | 5.1.1 | PPN | 2 |
| 8 | 5.2.8 | VLSP | 2 |
| 9 | 5.1.2 | RC | 3 |
| 10 | 5.2.1 | IRS | 3 |
| 11 | 5.1.4 | DRC | 3 |
| 12 | 5.1.11 | ICN | 3 |
| 13 | 5.1.15 | Warrant | 3 |

### Phase 3 — Moderate Products (Complexity 4-5)

| Order | Chapter | Product | Complexity |
|:-----:|---------|---------|:----------:|
| 14 | 5.1.5 | KODRC | 4 |
| 15 | 5.1.7 | Airbag | 4 |
| 16 | 5.1.8 | Bonus Certificate | 4 |
| 17 | 5.1.12 | Digital Note | 4 |
| 18 | 5.1.13 | Booster | 4 |
| 19 | 5.5.1 | CLN | 4 |
| 20 | 5.2.7 | Commodity Swap | 4 |
| 21 | 5.3.2 | ZCL | 4 |
| 22 | 5.1.6 | CRC | 5 |
| 23 | 5.2.2 | TRS | 5 |
| 24 | 5.2.3 | Equity Swap | 5 |
| 25 | 5.2.5 | CDS | 5 |
| 26 | 5.2.6 | Cross-Currency Swap | 5 |
| 27 | 5.3.1 | IR Callable | 5 |
| 28 | 5.3.5 | Digital Cap-Floor | 5 |
| 29 | 5.4.1 | Vanilla STEG | 5 |

### Phase 4 — Complex Products (Complexity 6-8)

| Order | Chapter | Product | Complexity |
|:-----:|---------|---------|:----------:|
| 30 | 5.1.3 | Phoenix | 6 |
| 31 | 5.1.9 | FCN | 6 |
| 32 | 5.1.10 | CRA ELN | 6 |
| 33 | 5.3.3 | NCRA | 6 |
| 34 | 5.4.3 | Callable STEG | 6 |
| 35 | 5.1.14 | Digital KI Put | 7 |
| 36 | 5.2.4 | Variance Swap | 7 |
| 37 | 5.3.4 | CRA SRT | 7 |
| 38 | 5.4.2 | RA STEG | 7 |
| 39 | 5.4.4 | TARN STEG | 8 |

---

## 2. Desk Analyst Path

**For:** Product Control, middle office, valuation analysts.

**Goal:** Understand how each product is valued, booked, and monitored.

**Focus sections per chapter:** §4 Product DNA, §13 Lifecycle, §15 Risks, §16 Booking, §17 Red Flags, §18 Worked Example.

| Phase | Chapters | Focus |
|:-----:|----------|-------|
| 1 | Parts 0-2 (skim) | FO/MO/BO roles, booking systems, four-leg structure |
| 2 | 5.2.1 IRS, 5.2.8 VLSP | Swap valuation fundamentals, DV01, central clearing |
| 3 | 5.1.1 PPN, 5.1.2 RC, 5.1.3 Phoenix | ELN valuation: bond + option decomposition |
| 4 | 5.2.2-5.2.7 (remaining swaps) | TRS, Equity Swap, Variance Swap, CDS, CCY, Commodity |
| 5 | 5.3.1-5.3.5 (SRT) | Four-leg booking, CMS fixings, range accrual counters |
| 6 | 5.4.1-5.4.4 (STEG) | CMS spread valuation, target accumulation, Monte Carlo |
| 7 | 5.5.x (CLN), 5.6.x (Other) | Credit valuation, exotic products |

**Key red-flag sections to master:** Every §17 (Red Flags) — these are the early-warning indicators for booking errors.

---

## 3. Trader Path

**For:** Derivatives traders, desk heads.

**Goal:** Understand hedging, risk management, P&L drivers.

**Focus sections per chapter:** §9 Why Product Exists (bank economics), §10 Scenarios, §15 Risks, Desk Reality, §19 Interview Questions.

| Phase | Chapters | Focus |
|:-----:|----------|-------|
| 1 | 1.4-1.8 | Greeks, correlation, yield curves, CMS rates |
| 2 | 5.1.1-5.1.3 | PPN (long vol), RC (short vol), Phoenix (path-dependent hedging) |
| 3 | 5.1.14 | Digital KI Put — most complex ELN, triple barrier |
| 4 | 5.2.1, 5.2.4, 5.2.5 | IRS (curve risk), Variance Swap (vol trading), CDS (credit hedging) |
| 5 | 5.3.1-5.3.5 | SRT — four-leg hedging, swaption management, range accrual gamma |
| 6 | 5.4.1-5.4.4 | STEG — CMS convexity, curve twist hedging, target clustering |
| 7 | All Desk Reality sections | Practical trading concerns across all products |

**Key Desk Reality sections:**
- Variance Swap (5.2.4) — vega notional vs variance notional confusion
- CRA SRT (5.3.4) — dual-gate P&L decomposition
- TARN STEG (5.4.4) — target clustering causing simultaneous redemptions

---

## 4. Structurer Path

**For:** Product structurers, financial engineers.

**Goal:** Understand construction, pricing, and client customization.

**Focus sections per chapter:** §6 Product Evolution, §9 Bank economics, §11 Formal Definition, §12 Construction, Desk Reality.

| Phase | Chapters | Focus |
|:-----:|----------|-------|
| 1 | Parts 0-2 | Building blocks: options, barriers, swaps |
| 2 | 5.1.1 PPN | Simplest construction: bond + call |
| 3 | 5.1.2 RC → 5.1.6 CRC → 5.1.9 FCN | RC family evolution — how each variant adds value |
| 4 | 5.1.3 Phoenix → 5.1.14 Digital KI Put | Autocallable family — barrier stacking |
| 5 | 5.2.1 IRS → 5.2.8 VLSP | Swap building blocks |
| 6 | 5.3.1-5.3.5 | SRT construction — four-leg decomposition, swaption embedding |
| 7 | 5.4.1-5.4.4 | STEG construction — CMS spread structuring, leverage calibration |
| 8 | All §12 Construction sections | Compare construction approaches across families |

**Key construction insights:**
- PPN (5.1.1) — bond + call option budget arithmetic
- IR Callable (5.3.1) — how swaption premium funds the coupon uplift
- Callable STEG (5.4.3) — dual premium decomposition (CMS + swaption)

---

## 5. Risk Manager Path

**For:** Market risk, credit risk, model validation.

**Goal:** Understand risk factors, worst-case scenarios, model dependencies.

**Focus sections per chapter:** §10 What Happens If, §15 Risks, §17 Red Flags, Knowledge Check (Desk Question).

| Phase | Chapters | Focus |
|:-----:|----------|-------|
| 1 | 1.4-1.8 | Greeks, correlation, yield curves — risk factor taxonomy |
| 2 | 5.1.14 Digital KI Put | Three interacting barriers — maximum ELN risk complexity |
| 3 | 5.2.4 Variance Swap | Nonlinear payoff, convexity, realized vs implied |
| 4 | 5.2.5 CDS | Credit event risk, wrong-way risk, ISDA mechanics |
| 5 | 5.3.3 NCRA, 5.3.4 CRA SRT | Range boundary risk, digital gamma, dual-gate |
| 6 | 5.4.2 RA STEG | Correlation risk between CMS rates, dual-boundary spread |
| 7 | 5.4.4 TARN STEG | Path dependency, Monte Carlo model risk, extension risk |
| 8 | All §15 Risk tables | Cross-product risk comparison |

**Risk severity heatmap (from §15 across 33 chapters):**

| Risk Type | High-Severity Count | Key Chapters |
|-----------|:-------------------:|-------------|
| Market/price risk | 15 | All ELN, Variance Swap |
| Curve/rate risk | 8 | All SRT, all STEG |
| Credit event risk | 3 | CDS, CLN |
| Correlation risk | 5 | Phoenix, RA STEG, CRA SRT |
| Path dependency | 4 | Phoenix, TARN STEG, FCN |
| Operational | 3 | CDS settlement, CMS fixing |

---

## 6. Sales Path

**For:** Sales, relationship managers, client-facing roles.

**Goal:** Understand client value proposition, when to recommend, when NOT to recommend.

**Focus sections per chapter:** §1 ELI5, §3 What Problem, §8 Why Clients Buy, §9 When makes sense / poor choice, §22 Common Mistakes.

| Phase | Chapters | Focus |
|:-----:|----------|-------|
| 1 | Parts 0-1 (skim) | Market context, basic product taxonomy |
| 2 | 4.1-4.3 | Product comparison matrices — which product fits which need |
| 3 | 5.1.1 PPN, 5.1.2 RC | Simplest pitch: capital protection vs yield enhancement |
| 4 | 5.1.3 Phoenix, 5.1.9 FCN | Income products — conditional vs fixed coupon |
| 5 | 5.2.1 IRS, 5.2.5 CDS | Swap-based hedging solutions |
| 6 | 5.3.1 IR Callable | Rate product pitch: above-market coupon for call risk |
| 7 | 5.4.1 Vanilla STEG, 5.4.4 TARN | Curve view expression, defined-return TARN |
| 8 | All §9 "When poor choice" | Critical — know when NOT to recommend |

**Client-matching quick reference:**

| Client Need | Recommended Products | Key Pitch |
|-------------|---------------------|-----------|
| Capital protection + upside | PPN | "Your money back guaranteed, plus participation" |
| High yield, moderate risk | RC, FCN | "6-8% coupon for accepting conditional risk" |
| Income with memory | Phoenix | "Missed coupons come back when market recovers" |
| Rate hedging | IRS, CDS | "Lock in your cost / protect against default" |
| Curve view | Vanilla STEG, TARN | "Profit from curve shape, not rate level" |
| Defined total return | TARN STEG | "15% total return, automatic exit" |

---

## 7. Operations Path

**For:** Operations, settlements, lifecycle management.

**Goal:** Understand booking, settlement, fixings, and operational risks.

**Focus sections per chapter:** §13 Lifecycle, §16 Booking, §17 Red Flags, Who Touches This Product (Operations row).

| Phase | Chapters | Focus |
|:-----:|----------|-------|
| 1 | 2.1-2.8 | FO/MO/BO structure, booking systems, four-leg framework |
| 2 | 5.2.1 IRS, 5.2.8 VLSP | Simplest swap operations: SOFR fixing, central clearing |
| 3 | 5.1.1-5.1.3 | ELN operations: observation dates, barrier monitoring, settlement |
| 4 | 5.2.5 CDS | Credit event operations: ISDA, auction, physical delivery |
| 5 | 5.2.6 CCY Swap | Cross-currency operations: CLS, dual-currency settlement |
| 6 | 5.3.1-5.3.5 | SRT operations: four-leg coordination, CMS fixings, range counters |
| 7 | 5.4.1-5.4.4 | STEG operations: dual CMS fixings, target counters, truncated coupons |
| 8 | All §17 Red Flags | Operational early-warning checklist |

**Hardest operational challenges by family:**

| Family | Hardest Ops Issue | Chapter |
|--------|------------------|---------|
| ELN | Autocall processing with multiple barriers | Phoenix (5.1.3) |
| Swaps | Credit event settlement / CLS coordination | CDS (5.2.5) / CCY (5.2.6) |
| SRT | Daily range observation reconciliation | NCRA (5.3.3) |
| STEG | Truncated final coupon on TARN target | TARN STEG (5.4.4) |

---

## 8. Complexity-Based Reading Paths

### Path A — Complexity 1-3 (Entry Level)

PPN → RC → IRS → DRC → ICN → Warrant → VLSP → CLN

*8 chapters. Building blocks only. No path dependency, no daily observation, no four-leg.*

### Path B — Complexity 4-5 (Intermediate)

Path A + KODRC → Airbag → Bonus → Digital Note → Booster → Commodity Swap → CRC → TRS → Equity Swap → CDS → CCY Swap → ZCL → IR Callable → Digital CF → Vanilla STEG

*23 chapters. Adds barriers, call features, single-observation products.*

### Path C — Complexity 6-7 (Advanced)

Path B + Phoenix → FCN → CRA ELN → NCRA → Callable STEG → Digital KI Put → Variance Swap → CRA SRT → RA STEG

*32 chapters. Adds path dependency, range accrual, multi-barrier, nonlinear payoffs.*

### Path D — Complexity 8+ (Expert)

Path C + TARN STEG → (future: Synthetic CDO Tranche, Accumulator)

*33+ chapters. Path dependency, Monte Carlo, portfolio credit.*

---

## 9. Summary

7 role-based reading paths + 4 complexity-based paths designed. Each path:
- Starts with prerequisites (Parts 0-2)
- Identifies key sections per chapter for that role
- Provides a recommended reading order
- Highlights "must-read" content

**Implementation:** These paths should be included in the publication's "How to Read This Book" section (Part 0 or front matter) during the Template Harmonization Pass.

---

*Reader Navigation Review completed 2026-06-20. No content modifications required.*
