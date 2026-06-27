# Product Generation Order

**Version:** 1.0
**Date:** 2026-06-19
**Scope:** 44 remaining products (49 total minus 5 pilot chapters)
**Optimization criteria:** Educational progression, concept dependencies, family continuity, visual template reuse

---

## 1. Design Principles

The generation order is optimized for four objectives, ranked by priority:

1. **Educational progression:** Each chapter builds on concepts the reader has already encountered. Simpler products precede complex variants. No chapter requires knowledge from a later chapter.

2. **Concept dependencies:** Products that introduce new building blocks (e.g., IRS introduces swap mechanics) are placed before products that require those blocks (e.g., SRT products require swap mechanics).

3. **Family continuity:** Products within the same family are generated consecutively. The "How This Differs From..." bridge pattern requires the reader to have just finished the previous product in the family.

4. **Visual template reuse:** Products that establish visual templates (payoff chart, decision tree, timeline) are generated before products that reuse those templates.

---

## 2. Complete Generation Order (49 Products)

### Batch 0 — Pilot (COMPLETE)

| # | Product | Family | Status | Notes |
|:-:|---------|--------|:------:|-------|
| 1 | Principal Protected Note (PPN) | ELN | DONE | Establishes: construction waterfall, payoff chart template |
| 2 | Reverse Convertible (RC) | ELN | DONE | Establishes: barrier payoff template, coupon decomposition |
| 3 | Phoenix Autocallable | ELN | DONE | Establishes: decision tree template, memory mechanism |
| 4 | Interest Rate Swap (IRS) | Swaps | DONE | Establishes: two-party flow, swap cash flow template |
| 5 | Vanilla CLN | CLN | DONE | Establishes: 3-party structure, credit event framework |

---

### Batch 1 — ELN RC Family (5 products)

These 5 products are direct variants of the RC. Each adds exactly one feature to the base product. They should be generated in this order because each variant's "How This Differs" bridge references the one before it.

| # | Product | Concept Added | Depends On | Visual Reuse |
|:-:|---------|--------------|-----------|-------------|
| 6 | Discounted RC (DRC) | Discount replaces coupon | RC (pilot) | Barrier payoff (RC template) |
| 7 | Knock-Out Discounted RC (KODRC) | + KO barrier above | DRC (#6) | Barrier payoff + KO line |
| 8 | Callable RC (CRC) | + Issuer call right | RC (pilot) | Barrier payoff + call timeline |
| 9 | Airbag / Leveraged RC | + Leverage below barrier | RC (pilot) | Barrier payoff + leverage zone |
| 10 | Bonus / Participation Note | Upside participation + floor | PPN + RC concepts | Payoff chart (PPN-style participation) |

**New concepts introduced:** Discount mechanism (DRC), knock-out barrier (KODRC), issuer call right (CRC), leverage below barrier (Airbag), participation with floor (Bonus).

---

### Batch 2 — ELN Autocallable + Other ELN (5 products)

These products build on the autocall mechanism introduced by Phoenix and the RC foundation.

| # | Product | Concept Added | Depends On | Visual Reuse |
|:-:|---------|--------------|-----------|-------------|
| 11 | Fixed Coupon Note (FCN) | Simpler autocall (fixed coupon, no memory) | RC + Phoenix concepts | Decision tree (Phoenix template, simplified) |
| 12 | Callable Range Accrual ELN | Accrual + equity + call | RC + SRT concepts (range accrual) | Timeline (new: accrual counter) |
| 13 | Issuer Callable Note (ICN) | Pure callable, no barrier, no put | CRC concepts | Simple payoff (bond-like) |
| 14 | Digital Coupon Notes | Digital (all-or-nothing) coupon | Digital concept (1.3) + RC | Payoff chart (step function) |
| 15 | Booster Note | Leveraged upside, no protection | PPN concepts (participation) | Payoff chart (steeper slope) |

**New concepts introduced:** Range accrual on equity (CRA ELN), digital coupon structure, leveraged participation without protection.

---

### Batch 3 — ELN Complex + Warrant (2 products)

The most complex ELN products. Placed last in ELN because they combine multiple mechanics.

| # | Product | Concept Added | Depends On | Visual Reuse |
|:-:|---------|--------------|-----------|-------------|
| 16 | Digital Coupon Knock-In Put | Digital + barrier — most complex ELN | Digital (#14) + RC barrier | Decision tree + barrier payoff |
| 17 | Warrant / Turbo Certificate | Pure option exposure, no bond wrapper | Options (1.2), Greeks (1.4) | Payoff chart (simple option payoff) |

**ELN family complete: 15/15 products.**

---

### Batch 4 — Swaps Core (4 products)

These swaps must be generated before SRT and STEG families because SRT/STEG products use swap mechanics. CDS must be generated before the remaining CLN products.

| # | Product | Concept Added | Depends On | Visual Reuse |
|:-:|---------|--------------|-----------|-------------|
| 18 | Total Return Swap (TRS) | Synthetic asset exposure | IRS (pilot) | Two-party flow (IRS template) |
| 19 | Equity Swap | Equity return vs financing rate | TRS (#18) | Two-party flow |
| 20 | Variance Swap | Realized vs implied variance | Volatility (1.5), IRS (pilot) | Payoff chart (linear in variance) |
| 21 | Credit Default Swap (CDS) | Full CDS mechanics | CLN (pilot), Credit (1.9) | Two-party flow + credit event flowchart |

**New concepts introduced:** Synthetic exposure (TRS), variance as tradeable (Variance Swap), full CDS settlement mechanics.

**Dependency note:** CDS (#21) must precede CLN Batch 8 products. Variance Swap (#20) introduces variance trading which is referenced in risk discussions for multiple product families.

---

### Batch 5 — Swaps Remaining (3 products)

| # | Product | Concept Added | Depends On | Visual Reuse |
|:-:|---------|--------------|-----------|-------------|
| 22 | Cross-Currency Swap | Principal exchange in two currencies | IRS (pilot) | Two-party flow + FX |
| 23 | Commodity Swap | Fixed vs floating commodity price | IRS (pilot) | Two-party flow |
| 24 | Vanilla Swap (VLSP) | Standard IRS with simplified terms | IRS (pilot) | Two-party flow |

**Swaps family complete: 8/8 products.**

---

### Batch 6 — Structured Rate Trades (5 products)

SRT products require swap mechanics (from Batch 4-5) and rate concepts (from 1.7-1.8). All are booked in Murex with four legs.

| # | Product | Concept Added | Depends On | Visual Reuse |
|:-:|---------|--------------|-----------|-------------|
| 25 | IR Callable Fixed Rate Swap | Fixed coupon + issuer call in Murex | IRS + CRC call concept | Cash flow timeline (IRS template) + four-leg diagram |
| 26 | IR Accreting Callable / ZCL | Accreting notional, no periodic coupons | IR Callable (#25) | Timeline (growing notional) |
| 27 | IR Non-Callable Range Accrual | Day-by-day accrual based on rate range | Range accrual concept, rates (1.7-1.8) | Timeline + accrual counter |
| 28 | IR Callable Range Accrual | + Issuer call right on range accrual | NCRA (#27) | Timeline + call overlay |
| 29 | Digital Cap-Floor | Digital payout on rate level | Digital (1.3), caps/floors (1.8) | Payoff chart (step function on rate axis) |

**New concepts introduced:** Four-leg booking in detail, accreting notional, rate range accrual mechanics, digital rate products.

**SRT family complete: 5/5 products.**

---

### Batch 7 — Steepener Notes (4 products)

STEG products require CMS rates (from 1.8) and swap mechanics. They share the yield curve slope as their driving risk factor.

| # | Product | Concept Added | Depends On | Visual Reuse |
|:-:|---------|--------------|-----------|-------------|
| 30 | Vanilla Steepener | Coupon = CMS30Y - CMS2Y | CMS (1.8), IRS (pilot) | Yield curve diagram + cash flow timeline |
| 31 | Range-Accrual Steepener | Accrual when spread in range | Vanilla STEG (#30) + range accrual (SRT) | Timeline + accrual counter |
| 32 | Callable Steepener | + Issuer call right | Vanilla STEG (#30) + call concept | Timeline + call overlay |
| 33 | TARN Steepener | Lifetime coupon cap (target) | Vanilla STEG (#30) | Timeline + target accumulation |

**New concepts introduced:** CMS spread as coupon driver, target accrual redemption mechanism (TARN).

**STEG family complete: 4/4 products.**

---

### Batch 8 — Credit-Linked Notes Remaining (4 products)

These require CDS mechanics (from Batch 4, #21) and the CLN framework (from pilot). Placed after CDS to ensure the full credit protection mechanics are established.

| # | Product | Concept Added | Depends On | Visual Reuse |
|:-:|---------|--------------|-----------|-------------|
| 34 | Skew CLN | Modified recovery terms | Vanilla CLN (pilot) | 3-party structure (CLN template) |
| 35 | First-to-Default (FTD) | Basket of 5-10 names, first default triggers | CLN + correlation (1.6) | 3-party structure + basket diagram |
| 36 | Nth-to-Default (NTD) | Nth default triggers (less risky than FTD) | FTD (#35) | Same as FTD with threshold shift |
| 37 | Synthetic CDO Tranche | Portfolio of 100+ names, tranched risk | NTD (#36) + advanced correlation | Tranche waterfall (new template) |

**New concepts introduced:** Recovery modification (Skew), basket credit default mechanics, Nth-to-default, tranching, attachment/detachment points.

**CLN family complete: 5/5 products.**

**Note:** Synthetic CDO Tranche (#37) is the most complex product in the universe. It may exceed the 3,500-word limit. If so, the Final Editor Agent should approve the exception rather than cutting content.

---

### Batch 9 — Other Products (7 products)

Miscellaneous products that do not fit neatly into the main families. These are placed last because they draw on concepts from all prior families.

| # | Product | Concept Added | Depends On | Visual Reuse |
|:-:|---------|--------------|-----------|-------------|
| 38 | Structured Deposits | Deposit insurance + derivative | PPN concepts | Payoff chart (PPN-like) |
| 39 | Accumulator | Daily share accumulation at discount + KO | Forward concept (0.8), barrier (1.3) | Timeline (daily accumulation) |
| 40 | Decumulator | Daily share sale at premium + KO | Accumulator (#39) | Timeline (daily sale) |
| 41 | Option on Risk Control | Option on managed fund | Options (1.2), fund concepts | Payoff chart (option on index) |
| 42 | Equity Linked Option | Standalone option, no bond wrapper | Options (1.2), Warrant (#17) | Payoff chart (standard option) |
| 43 | Forwards | Obligatory future purchase/sale | Forwards (0.8) | Linear payoff chart |
| 44 | Vanilla Options | Standard calls/puts without structure | Options (1.2) | Payoff chart (standard option) |

**Other family complete: 7/7 products.**
**Total universe complete: 49/49 products.**

---

## 3. Generation Batches Summary

| Batch | Products | Family | Count | Dependencies |
|:-----:|----------|--------|:-----:|-------------|
| 0 | PPN, RC, Phoenix, IRS, CLN | Mixed (pilot) | 5 | Parts 0-4 |
| 1 | DRC, KODRC, CRC, Airbag, Bonus | ELN (RC variants) | 5 | Batch 0 |
| 2 | FCN, CRA ELN, ICN, Digital, Booster | ELN (autocall + other) | 5 | Batch 0-1 |
| 3 | Digital KI Put, Warrant | ELN (complex + standalone) | 2 | Batch 0-2 |
| 4 | TRS, Equity Swap, Variance Swap, CDS | Swaps (core) | 4 | Batch 0 (IRS) |
| 5 | Currency Swap, Commodity Swap, VLSP | Swaps (remaining) | 3 | Batch 0, 4 |
| 6 | IR Callable, ZCL, NCRA, CRA, Digital CF | SRT | 5 | Batch 4-5 (swap mechanics) |
| 7 | Vanilla STEG, RA STEG, Callable STEG, TARN STEG | STEG | 4 | Batch 6 (CMS in SRT context) |
| 8 | Skew CLN, FTD, NTD, Synthetic CDO Tranche | CLN (remaining) | 4 | Batch 4 (CDS) |
| 9 | Structured Deposit, Accumulator, Decumulator, Option on RC, ELO, Forward, Vanilla Options | Other | 7 | All prior batches |
| **Total** | | | **44** | |

---

## 4. Visual Template Establishment Order

| Template | Established By | Reused In |
|----------|---------------|----------|
| Payoff chart (equity barrier) | RC (pilot, Batch 0) | DRC, KODRC, CRC, Airbag, FCN, Digital, Digital KI Put |
| Payoff chart (participation) | PPN (pilot, Batch 0) | Bonus, Booster, Structured Deposit |
| Payoff chart (linear) | IRS (pilot, Batch 0) | TRS, Equity Swap, Variance Swap, CDS, Forwards, Vanilla Options |
| Payoff chart (digital/step) | Digital (Batch 2) | Digital KI Put, Digital Cap-Floor |
| Decision tree (observation) | Phoenix (pilot, Batch 0) | FCN, CRA ELN, all autocallable variants |
| Two-party flow (swap) | IRS (pilot, Batch 0) | TRS, Equity Swap, Variance Swap, Currency Swap, Commodity Swap, VLSP |
| Three-party structure (credit) | CLN (pilot, Batch 0) | Skew CLN, FTD, NTD, Synthetic CDO |
| Construction waterfall | PPN (pilot, Batch 0) | All ELN products, CLN products |
| Cash flow timeline (periodic) | IRS (pilot, Batch 0) | All SRT, all STEG, RC, CLN |
| Four-leg diagram | IR Callable (Batch 6) | All SRT, all STEG |
| Accrual counter timeline | NCRA (Batch 6) | CRA SRT, RA STEG, CRA ELN |
| Target accumulation | TARN STEG (Batch 7) | — (unique to TARN) |
| Tranche waterfall | Synthetic CDO (Batch 8) | — (unique to tranched products) |
| Daily accumulation timeline | Accumulator (Batch 9) | Decumulator |

All pilot-established templates (Batch 0) are available from the first generation batch. New templates introduced in Batches 6-9 serve their specific families.

---

## 5. Concept Dependency Graph (Simplified)

```
Parts 0-4 (foundation)
    │
    ├── PPN (pilot) ──→ Bonus, Booster, Structured Deposit
    │
    ├── RC (pilot) ──→ DRC → KODRC
    │               ──→ CRC → ICN
    │               ──→ Airbag
    │               ──→ FCN → CRA ELN
    │               ──→ Digital → Digital KI Put
    │
    ├── Phoenix (pilot) ──→ FCN (simpler autocall), all autocallable variants
    │
    ├── IRS (pilot) ──→ TRS → Equity Swap
    │               ──→ Variance Swap
    │               ──→ Currency Swap, Commodity Swap, VLSP
    │               ──→ IR Callable → ZCL
    │               ──→ NCRA → CRA (SRT)
    │               ──→ Digital Cap-Floor
    │               ──→ Vanilla STEG → RA STEG, Callable STEG, TARN STEG
    │
    ├── CLN (pilot) ──→ Skew CLN
    │               ──→ CDS (full) → FTD → NTD → Synthetic CDO Tranche
    │
    └── Other: Accumulator, Decumulator, Option on RC, ELO, Forward, Vanilla Options
              (draw from multiple families)
```

---

*Generation order effective 2026-06-19. All remaining chapters follow this sequence.*
