# Learning Dependency Graph

**Desk Bible v2 — Educational Navigation Layer**

**Products:** 49
**Tiers:** 5
**Learning Paths:** 5
**Maximum Dependency Depth:** 5
**Framework:** v1.3.1 (frozen)
**Generated:** 2026-06-22

---

## Table of Contents

1. [Tier Definitions](#tier-definitions)
2. [Master Dependency Table](#master-dependency-table)
3. [Master Dependency Graph](#master-dependency-graph)
4. [Equity Path](#equity-path)
5. [Rates Path](#rates-path)
6. [Credit Path](#credit-path)
7. [Volatility Path](#volatility-path)
8. [Beginner → Expert Roadmap](#beginner--expert-roadmap)

---

## Tier Definitions

| Tier | Name | Complexity Range | Products | Description |
|:----:|------|:----------------:|:--------:|-------------|
| 1 | Foundation | 2 | 4 | Building blocks. No product prerequisites. Learn these first |
| 2 | Core Structures | 3 | 8 | Single-feature products. Require one foundation product |
| 3 | Structured Products | 4–5 | 19 | Multi-feature products. Combine core structures |
| 4 | Advanced Structures | 6–7 | 14 | Complex multi-factor. Path dependency, dual conditions |
| 5 | Specialist Structures | 8–10 | 4 | Highest complexity. Correlation, portfolio, Monte Carlo |

---

## Master Dependency Table

For each product: tier, prerequisite products (direct only), prerequisite concepts, and dependency depth (longest chain to a Tier 1 root).

### Tier 1 — Foundation (4 products)

| Section | Product | Complexity | Prereq Products | Prereq Concepts | Depth |
|---------|---------|:----------:|----------------|-----------------|:-----:|
| 5.6.2 | Forward Contract (FWD) | 2 | — | Forward pricing, cost of carry, settlement | 0 |
| 5.6.1 | Structured Deposit (SD) | 2 | — | Deposit mechanics, call option basics | 0 |
| 5.1.1 | Principal Protected Note (PPN) | 2 | — | Zero-coupon bond, European call option, participation rate | 0 |
| 5.2.8 | Vanilla Swap Plus (VLSP) | 2 | — | Fixed vs floating rates, swap mechanics, cap/floor basics | 0 |

**No product prerequisites.** These 4 products are entry points for all learning paths.

---

### Tier 2 — Core Structures (8 products)

| Section | Product | Complexity | Prereq Products | Prereq Concepts | Depth |
|---------|---------|:----------:|----------------|-----------------|:-----:|
| 5.6.3 | Vanilla Option (VO) | 3 | FWD | Put-call parity, Greeks, time decay, intrinsic vs extrinsic value | 1 |
| 5.2.1 | Interest Rate Swap (IRS) | 3 | FWD | Swap valuation, DV01, fixed vs floating, yield curve | 1 |
| 5.1.2 | Reverse Convertible (RC) | 3 | PPN | Short put, yield enhancement, conditional capital return | 1 |
| 5.1.4 | Discounted RC (DRC) | 3 | RC | Discount pricing, break-even calculation, adjusted strike | 2 |
| 5.1.11 | Issuer Callable Note (ICN) | 3 | RC | Bermudan call right, reinvestment risk | 2 |
| 5.1.15 | Warrant / Turbo (Warrant) | 3 | VO | Exchange-traded leverage, time decay acceleration | 2 |
| 5.6.4 | Equity-Linked Option (ELO) | 3 | VO | Retail wrapper, term sheet vs ISDA | 2 |
| 5.6.8 | Dual Currency Investment (DCI) | 3 | RC | FX option, currency conversion risk | 2 |

---

### Tier 3 — Structured Products (19 products)

| Section | Product | Complexity | Prereq Products | Prereq Concepts | Depth |
|---------|---------|:----------:|----------------|-----------------|:-----:|
| 5.1.5 | KODRC | 4 | RC | Knock-out barrier, continuous monitoring, barrier gap risk | 2 |
| 5.1.7 | Airbag Note | 4 | RC | Leverage ratio, put spread, cushion zone | 2 |
| 5.1.8 | Bonus Note | 4 | RC | Down-and-in barrier, conditional bonus, continuous observation | 2 |
| 5.1.12 | Digital Coupon Note | 4 | RC | Binary/digital payoff, digital gamma, call spread replication | 2 |
| 5.1.13 | Booster Note | 4 | PPN | Leveraged call spread, participation cap | 1 |
| 5.2.7 | Commodity Swap | 4 | IRS | Commodity benchmarks, Asian averaging, basis risk | 2 |
| 5.3.2 | Zero-Coupon Linked Note | 4 | PPN, IRS | Zero-coupon accretion, duration, liability matching | 2 |
| 5.5.1 | Vanilla CLN | 4 | CDS | Funded credit, note wrapper, dual credit exposure | 3 |
| 5.6.9 | Shark Fin Note | 4 | PPN | Up-and-out barrier, rebate, barrier knock-out | 1 |
| 5.1.6 | Callable RC (CRC) | 5 | RC | Bermudan exercise, embedded swaption, reinvestment risk | 2 |
| 5.2.2 | Total Return Swap | 5 | IRS | Total return, synthetic ownership, funding spread | 2 |
| 5.2.3 | Equity Swap | 5 | TRS | Dividend risk (gross vs net), quanto, equity delta | 3 |
| 5.2.5 | Credit Default Swap | 5 | IRS | Credit events, recovery rate, ISDA determinations | 2 |
| 5.2.6 | Cross-Currency Swap | 5 | IRS | Cross-currency basis, Herstatt risk, dual-currency PV | 2 |
| 5.3.1 | IR Callable Fixed Rate Swap | 5 | IRS | Embedded swaption, four-leg SRT, non-call period | 2 |
| 5.3.5 | Digital Cap-Floor Note | 5 | IRS, Digital | Digital caplet strip, binary rate payoff | 3 |
| 5.4.1 | Vanilla Steepener Note | 5 | IRS | CMS spread, convexity adjustment, curve slope | 2 |
| 5.5.2 | Skew CLN | 5 | CLN | Recovery rate distribution, non-linear recovery payoff | 4 |
| 5.6.5 | Option on RC | 5 | RC, VO | Compound option, vol-of-vol, two-layer structure | 2 |

---

### Tier 4 — Advanced Structures (14 products)

| Section | Product | Complexity | Prereq Products | Prereq Concepts | Depth |
|---------|---------|:----------:|----------------|-----------------|:-----:|
| 5.1.3 | Phoenix Autocallable | 6 | RC | Autocall trigger, memory coupon, barrier observation, early termination | 2 |
| 5.1.9 | Fixed Coupon Note | 6 | Phoenix | Guaranteed vs conditional coupon, step-down autocall | 3 |
| 5.1.10 | Callable Range Accrual ELN | 6 | Digital, CRC | Range accrual mechanism, daily observation, digital strip + call | 3 |
| 5.3.3 | Non-Callable Range Accrual | 6 | IR Callable, Digital CF | Range accrual on rates, digital option strip, days-in-range | 3 |
| 5.4.3 | Callable Steepener | 6 | Vanilla STEG | CMS spread + Bermudan call, dual optionality | 3 |
| 5.6.6 | Accumulator | 6 | FWD, VO | Daily forwards, gearing, knock-out, obligation asymmetry | 2 |
| 5.6.7 | Decumulator | 6 | ACCUM | Mirror mechanics, selling vs buying, down knock-out | 3 |
| 5.1.14 | Digital Coupon KI Put | 7 | Digital, KODRC | Dual barrier (digital + KI), three-barrier interaction | 3 |
| 5.2.4 | Variance Swap | 7 | VO | Variance vs volatility, convexity, log contract replication | 2 |
| 5.3.4 | Callable Range Accrual SRT | 7 | NCRA, IR Callable | Dual embedded options (digital strip + swaption), correlation | 4 |
| 5.4.2 | Range Accrual Steepener | 7 | Vanilla STEG, NCRA | Spread-based range accrual, dual-condition coupon | 3 |
| 5.5.3 | First-to-Default Note | 7 | CLN | Basket credit, first-default trigger, credit correlation | 4 |
| 5.6.10 | Snowball Autocallable | 7 | Phoenix | Cumulative coupon accumulation, all-or-nothing dynamic | 3 |
| 5.6.11 | Cliquet Note | 7 | PPN, VO | Forward-starting options, periodic reset, local/global caps | 2 |

---

### Tier 5 — Specialist Structures (4 products)

| Section | Product | Complexity | Prereq Products | Prereq Concepts | Depth |
|---------|---------|:----------:|----------------|-----------------|:-----:|
| 5.4.4 | TARN Steepener | 8 | Vanilla STEG | Target accumulation, path-dependent termination, Monte Carlo | 3 |
| 5.5.4 | Nth-to-Default Note | 8 | FTD | Nth-default threshold, correlation reversal, non-monotonic sensitivity | 5 |
| 5.6.12 | Worst-of Autocallable | 8 | Phoenix | Worst-of observation, basket correlation, dispersion | 3 |
| 5.5.5 | Synthetic CDO Tranche | 10 | FTD | Tranching, attachment/detachment, copula dependency, base correlation, loss waterfall | 5 |

---

## Master Dependency Graph

Text-based specification showing all prerequisite chains. Read left-to-right: each product requires all products to its left on its chain.

### Tier 1 Roots

```
FWD ─────┬── VO ───┬── Warrant
         │         ├── ELO
         │         ├── VarSwap
         │         └── CLIQ (+ PPN)
         │
         ├── IRS ──┬── CommSwap
         │         ├── TRS ──── EqSwap
         │         ├── CDS ──── CLN ──┬── Skew CLN
         │         │                  ├── FTD ──┬── NTD
         │         │                  │         └── CDO
         │         ├── XCCY
         │         ├── IR Callable ──┬── ZCL (+ PPN)
         │         │                 ├── NCRA ─── CRA SRT
         │         │                 └── Digital CF (+ Digital)
         │         └── Vanilla STEG ┬── Callable STEG
         │                          ├── RA STEG (+ NCRA)
         │                          └── TARN STEG
         └── ACCUM (+ VO) ── DECUM

SD ──────── (standalone entry point, unlocks conceptual understanding)

PPN ─────┬── RC ───┬── DRC
         │         ├── ICN
         │         ├── DCI
         │         ├── KODRC
         │         ├── Airbag
         │         ├── Bonus
         │         ├── Digital ──┬── DKIP (+ KODRC)
         │         │             └── Digital CF (+ IRS)
         │         ├── CRC
         │         ├── CRA ELN (+ Digital, CRC)
         │         ├── Phoenix ─┬── FCN
         │         │            ├── SNOW
         │         │            └── WOAC
         │         └── Opt-on-RC (+ VO)
         │
         ├── Booster
         ├── SHRK
         └── CLIQ (+ VO)

VLSP ────── (standalone, simplified IRS — parallel entry to rates)
```

### Cross-Family Dependencies

Products that require prerequisites from multiple families:

| Product | Family | Prereqs from Other Families |
|---------|--------|----------------------------|
| CLN (5.5.1) | CLN | CDS (Swaps) |
| Digital CF (5.3.5) | SRT | Digital (ELN) + IRS (Swaps) |
| CRA ELN (5.1.10) | ELN | Digital (ELN) + CRC (ELN) |
| ZCL (5.3.2) | SRT | PPN (ELN) + IRS (Swaps) |
| NCRA (5.3.3) | SRT | IR Callable (SRT) + Digital CF (SRT) |
| RA STEG (5.4.2) | STEG | Vanilla STEG (STEG) + NCRA (SRT) |
| CRA SRT (5.3.4) | SRT | NCRA (SRT) + IR Callable (SRT) |
| DKIP (5.1.14) | ELN | Digital (ELN) + KODRC (ELN) |
| Opt-on-RC (5.6.5) | Other | RC (ELN) + VO (Other) |
| ACCUM (5.6.6) | Other | FWD (Other) + VO (Other) |
| CLIQ (5.6.11) | Other | PPN (ELN) + VO (Other) |

---

## Equity Path

Learning sequence for equity-focused structured products.

### Phase 1 — Equity Foundations

```
Step 1: PPN (2)        → Capital protection = ZCB + call option
Step 2: VO (3)         → Option mechanics: Greeks, time decay, asymmetric payoff
Step 3: RC (3)         → Yield enhancement = bond + short put
```

### Phase 2 — RC Variants

```
Step 4: DRC (3)        → Discount instead of coupon. Lower break-even
Step 5: ICN (3)        → Add call right. Reinvestment risk
Step 6: DCI (3)        → RC in FX wrapper. Same mechanics, different asset
```

### Phase 3 — Barrier Products

```
Step 7: KODRC (4)      → Add knock-out barrier to DRC
Step 8: Airbag (4)     → Leverage + cushion zone
Step 9: Bonus (4)      → Conditional minimum return + DI barrier
Step 10: SHRK (4)      → Capital-protected + KO barrier (PPN variant)
```

### Phase 4 — Coupon Variants

```
Step 11: Digital (4)   → Binary coupon: yes/no per observation
Step 12: Booster (4)   → Leveraged participation (PPN variant)
Step 13: CRC (5)       → RC + Bermudan call. Maximum RC yield
Step 14: Warrant (3)   → Exchange-traded leveraged option
Step 15: ELO (3)       → Retail-wrapped VO
```

### Phase 5 — Autocallable Family

```
Step 16: Phoenix (6)   → RC + autocall + memory coupon + barrier
Step 17: FCN (6)       → Phoenix with guaranteed coupon
Step 18: SNOW (7)      → Phoenix + cumulative missed coupons
Step 19: WOAC (8)      → Phoenix + worst-of basket + correlation
```

### Phase 6 — Complex ELN

```
Step 20: CRA ELN (6)   → Range accrual on equity + call (requires Digital + CRC)
Step 21: DKIP (7)      → Digital + knock-in put = dual conditional (requires Digital + KODRC)
Step 22: CLIQ (7)      → PPN + forward-starting options + periodic lock-in
Step 23: Opt-on-RC (5) → Compound option: option layer on top of RC
```

### Phase 7 — Non-ELN Equity

```
Step 24: ACCUM (6)     → Daily forwards + gearing + KO barrier
Step 25: DECUM (6)     → Mirror of ACCUM (selling instead of buying)
```

**Total equity path:** 25 products. Covers all 15 ELN + 10 equity-related Other products.

---

## Rates Path

Learning sequence for interest rate structured products.

### Phase 1 — Rate Foundations

```
Step 1: FWD (2)          → Forward pricing, cost of carry
Step 2: VLSP (2)         → Simplest rate swap. Cap, floor, amortisation
Step 3: IRS (3)          → Fixed-for-floating. DV01, yield curve
```

### Phase 2 — Structured Rate Trades

```
Step 4: IR Callable (5)  → IRS + embedded swaption. Four-leg SRT
Step 5: ZCL (4)          → Zero-coupon accretion (requires PPN concepts)
Step 6: Digital CF (5)   → Digital caplet strip (requires Digital concepts)
Step 7: NCRA (6)         → Range accrual on single rate. Daily observation
Step 8: CRA SRT (7)      → NCRA + callable = maximum rate yield
```

### Phase 3 — Steepener Notes

```
Step 9: Vanilla STEG (5)   → Leveraged CMS spread coupon
Step 10: Callable STEG (6) → Add bank call right
Step 11: RA STEG (7)       → Add range accrual on spread (requires NCRA)
Step 12: TARN STEG (8)     → Add target accumulation + auto-redemption
```

### Phase 4 — Cross-Currency

```
Step 13: XCCY (5)        → IRS in two currencies + FX forward
```

### Phase 5 — Commodity

```
Step 14: CommSwap (4)    → IRS mechanics applied to commodity prices
```

**Total rates path:** 14 products. Covers all 5 SRT + 4 STEG + IRS, VLSP, XCCY, CommSwap, FWD.

---

## Credit Path

Learning sequence for credit-linked structured products.

### Phase 1 — Credit Foundations

```
Step 1: FWD (2)        → Forward pricing foundation
Step 2: IRS (3)        → Swap mechanics
Step 3: CDS (5)        → Credit protection. Credit events, recovery, settlement
```

### Phase 2 — Funded Credit

```
Step 4: CLN (4)        → CDS in note wrapper. Dual credit exposure
Step 5: Skew CLN (5)   → Modified recovery mechanism
```

### Phase 3 — Basket Credit

```
Step 6: FTD (7)        → Basket of names. First-default trigger. Correlation: low = higher risk
Step 7: NTD (8)        → Nth-default threshold. Correlation reversal: high = higher risk
```

### Phase 4 — Portfolio Credit

```
Step 8: CDO (10)       → 100+ names. Tranching. Loss waterfall. Base correlation
```

**Total credit path:** 8 products. Covers all 5 CLN + CDS, IRS, FWD.

**Longest dependency chain in the universe:** FWD → IRS → CDS → CLN → FTD → NTD/CDO (depth 5).

---

## Volatility Path

Learning sequence for volatility-focused products.

### Phase 1 — Vol Foundations

```
Step 1: FWD (2)        → Linear payoff baseline (no vol sensitivity)
Step 2: VO (3)         → Option basics. Greeks: delta, gamma, vega, theta
Step 3: Warrant (3)    → Exchange-traded leverage. Time decay acceleration
```

### Phase 2 — Long Vega Products

Products where investor benefits from rising volatility.

```
Step 4: PPN (2)        → Long call (vega positive). Rho sensitivity
Step 5: SD (2)         → Same as PPN in deposit wrapper
Step 6: Booster (4)    → Leveraged call spread (long vega)
Step 7: SHRK (4)       → Long up-and-out call. Complex vega near barrier
Step 8: ELO (3)        → Long option in retail format
Step 9: CLIQ (7)       → Long forward-starting options. Forward vol curve
```

### Phase 3 — Short Vega Products

Products where investor loses from rising volatility.

```
Step 10: RC (3)        → Short put = short vega
Step 11: DRC (3)       → Short put variant
Step 12: CRC (5)       → Short put + short call = double short vega
Step 13: FCN (6)       → Short options via autocall + barrier
Step 14: DCI (3)       → Short FX put
Step 15: WOAC (8)      → Short basket options
```

### Phase 4 — Complex Vega Products

Products with state-dependent or mixed vega.

```
Step 16: Phoenix (6)   → Vega concentrated near barrier
Step 17: KODRC (4)     → Short below barrier, long above
Step 18: Digital (4)   → Concentrated near digital strike
Step 19: ACCUM (6)     → KO barrier + gearing sensitivity
```

### Phase 5 — Pure Volatility

```
Step 20: VarSwap (7)   → Linear in variance, CONVEX in vol. Pure vol instrument
```

**Key insight:** VarSwap is the ONLY product where volatility IS the underlying. All other products have vol as a secondary exposure.

---

## Beginner → Expert Roadmap

Week-by-week learning plan covering all 49 products across all 5 tiers.

### Weeks 1–2: Tier 1 — Foundation (4 products)

| Week | Day | Product | Key Lesson |
|:----:|:---:|---------|-----------|
| 1 | 1 | SD (2) | Simplest structured product. Deposit + call option |
| 1 | 2 | FWD (2) | Linear payoff. Foundation of all derivatives |
| 1 | 3 | PPN (2) | ZCB + call = capital protection. Participation rate |
| 2 | 1 | VLSP (2) | Simplest swap. Cap, floor, amortisation |

**Milestone:** Can explain capital protection, forward pricing, and swap mechanics.

### Weeks 2–4: Tier 2 — Core Structures (8 products)

| Week | Day | Product | Key Lesson |
|:----:|:---:|---------|-----------|
| 2 | 2 | VO (3) | Asymmetric payoff. Greeks. Put-call parity |
| 2 | 3 | IRS (3) | Fixed-for-floating. DV01. Most liquid OTC derivative |
| 3 | 1 | RC (3) | Yield enhancement archetype. Bond + short put |
| 3 | 2 | DRC (3) | Discount variant. Lower break-even |
| 3 | 3 | ICN (3) | Callable note. Reinvestment risk |
| 4 | 1 | Warrant (3) | Exchange-traded leverage |
| 4 | 2 | ELO (3) | Retail option wrapper |
| 4 | 3 | DCI (3) | FX yield enhancement |

**Milestone:** Can explain yield enhancement, option Greeks, and swap valuation.

### Weeks 5–8: Tier 3 — Structured Products (19 products)

| Week | Day | Product | Key Lesson |
|:----:|:---:|---------|-----------|
| 5 | 1 | KODRC (4) | Knock-out barrier. Discontinuity |
| 5 | 2 | Airbag (4) | Leverage + cushion zone |
| 5 | 3 | Bonus (4) | DI barrier. Continuous observation |
| 6 | 1 | Digital (4) | Binary coupon. Digital gamma |
| 6 | 2 | Booster (4) | Leveraged participation. Cap |
| 6 | 3 | SHRK (4) | Capital-protected + KO barrier |
| 7 | 1 | CommSwap (4) | Commodity swap. Basis risk |
| 7 | 2 | ZCL (4) | Zero-coupon rate. Duration |
| 7 | 3 | CLN (4) | Funded credit. Dual exposure |
| 8 | 1 | CRC (5) | RC + call right. Maximum RC yield |
| 8 | 2 | TRS (5) | Synthetic ownership. Funding spread |
| 8 | 3 | CDS (5) | Credit protection. Credit events |
| 8+ | — | EqSwap (5) | Equity-specific TRS. Dividends |
| 8+ | — | XCCY (5) | Cross-currency. Basis spread |
| 8+ | — | IR Callable (5) | Embedded swaption. Four-leg SRT |
| 8+ | — | Digital CF (5) | Binary rate coupon |
| 8+ | — | Vanilla STEG (5) | CMS spread. Curve view |
| 8+ | — | Skew CLN (5) | Modified recovery |
| 8+ | — | Opt-on-RC (5) | Compound option |

**Milestone:** Can explain barrier mechanics, range accrual, funded credit, and CMS spreads.

### Weeks 9–12: Tier 4 — Advanced Structures (14 products)

| Week | Product | Key Lesson |
|:----:|---------|-----------|
| 9 | Phoenix (6) | Autocall + memory + barrier. Most traded autocallable |
| 9 | FCN (6) | Guaranteed vs conditional coupon |
| 9 | CRA ELN (6) | Range accrual on equity |
| 10 | NCRA (6) | Range accrual on rates |
| 10 | Callable STEG (6) | CMS spread + call |
| 10 | ACCUM (6) | Daily forwards + gearing. Obligation asymmetry |
| 10 | DECUM (6) | Mirror of ACCUM |
| 11 | DKIP (7) | Three barriers. Most complex ELN |
| 11 | VarSwap (7) | Convex variance. Pure vol instrument |
| 11 | CRA SRT (7) | Range + call = dual embedded options |
| 12 | RA STEG (7) | Spread-based range accrual |
| 12 | FTD (7) | Basket credit. Correlation |
| 12 | SNOW (7) | Cumulative coupon. Snowball accumulation |
| 12 | CLIQ (7) | Forward-starting options. Periodic lock-in |

**Milestone:** Can explain autocall mechanics, range accrual, gearing, credit correlation, and path dependency.

### Weeks 13–16: Tier 5 — Specialist Structures (4 products)

| Week | Product | Key Lesson |
|:----:|---------|-----------|
| 13 | TARN STEG (8) | Target accumulation. Monte Carlo pricing |
| 14 | NTD (8) | Nth-default. Correlation reversal |
| 14 | WOAC (8) | Worst-of basket. Dispersion |
| 16 | CDO (10) | Tranching. Loss waterfall. Copula. Base correlation |

**Milestone:** Can explain correlation-dependent pricing, path-dependent termination, and tranched loss allocation.

### Roadmap Summary

| Phase | Weeks | Tier | Products | Cumulative |
|-------|:-----:|:----:|:--------:|:----------:|
| Foundation | 1–2 | 1 | 4 | 4 |
| Core | 2–4 | 2 | 8 | 12 |
| Structured | 5–8 | 3 | 19 | 31 |
| Advanced | 9–12 | 4 | 14 | 45 |
| Specialist | 13–16 | 5 | 4 | 49 |

**Total:** 16 weeks from zero to full universe coverage.

---

## Dependency Statistics

| Metric | Value |
|--------|:-----:|
| Total products | 49 |
| Root products (depth 0) | 4 |
| Maximum dependency depth | 5 |
| Longest chain | FWD → IRS → CDS → CLN → FTD → NTD/CDO |
| Products with cross-family dependencies | 11 |
| Products with single prerequisite | 29 |
| Products with two prerequisites | 10 |
| Products with no prerequisites | 4 |
| Average prerequisites per product | 1.3 |

---

*Learning Dependency Graph — 49 products, 5 tiers, 5 learning paths. Generated 2026-06-22.*
