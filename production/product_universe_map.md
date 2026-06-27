# Structured Products Universe Map

**Desk Bible v2 — Canonical Navigation & Visualization Specification**

**Products:** 49
**Families:** 6
**Tiers:** 5
**Graph Systems:** 3 (Evolution, Dependency, Learning)
**Framework:** v1.3.1 (frozen)
**Generated:** 2026-06-22

---

## Table of Contents

1. [Executive Overview](#1-executive-overview)
2. [Universe Statistics](#2-universe-statistics)
3. [Family Cluster Map](#3-family-cluster-map)
4. [Evolution Layer](#4-evolution-layer)
5. [Dependency Layer](#5-dependency-layer)
6. [Learning Layer](#6-learning-layer)
7. [Cross-Family Interaction Layer](#7-cross-family-interaction-layer)
8. [Root Node Analysis](#8-root-node-analysis)
9. [Most Connected Products](#9-most-connected-products)
10. [Complexity Heat Map](#10-complexity-heat-map)
11. [Interview Hotspots](#11-interview-hotspots)
12. [Risk Concentration Zones](#12-risk-concentration-zones)
13. [Navigation Instructions](#13-navigation-instructions)
14. [Atlas → Matrix → Dependency → Universe Traceability](#14-traceability)

---

## 1. Executive Overview

The Structured Products Universe Map is a textual specification of the complete 49-product universe. It encodes three separate relationship graphs:

- **Evolution Graph** — structural lineage. "Product A evolves into Product B by adding one feature." 42 directed edges, 8 roots, 34 leaf nodes. Source: Atlas Appendix C.

- **Dependency Graph** — prerequisite knowledge. "You must understand Product A before learning Product B." 53 directed edges, 4 roots, 31 leaf nodes. Source: Learning Dependency Graph.

- **Learning Graph** — recommended study order. "Study Product A, then B, then C." 5 sequenced paths covering all 49 products. Source: Learning Dependency Graph paths.

These three graphs share the same 49 nodes but have different edge sets and different root/leaf structures. They must NOT be merged.

---

## 2. Universe Statistics

### Node Statistics

| Metric | Value |
|--------|:-----:|
| Total products | 49 |
| Families | 6 |
| Dependency tiers | 5 |
| Complexity range | 2–10 |
| Complexity median | 5 |

### Edge Statistics

| Graph | Edges | Roots | Leaves | Max Depth |
|-------|:-----:|:-----:|:------:|:---------:|
| Evolution | 42 | 8 | 34 | 5 |
| Dependency | 53 | 4 | 31 | 5 |
| Learning | 5 paths | 4 | 49 (all endpoints) | 16 weeks |

### Family Distribution

| Family | Products | Section Range | Complexity Range |
|--------|:--------:|:------------:|:----------------:|
| ELN | 15 | 5.1.1–5.1.15 | 2–7 |
| Swaps | 8 | 5.2.1–5.2.8 | 2–7 |
| SRT | 5 | 5.3.1–5.3.5 | 4–7 |
| STEG | 4 | 5.4.1–5.4.4 | 5–8 |
| CLN | 5 | 5.5.1–5.5.5 | 4–10 |
| Other | 12 | 5.6.1–5.6.12 | 2–8 |

### Tier Distribution

| Tier | Name | Complexity | Products |
|:----:|------|:----------:|:--------:|
| 1 | Foundation | 2 | 4 |
| 2 | Core Structures | 3 | 8 |
| 3 | Structured Products | 4–5 | 19 |
| 4 | Advanced Structures | 6–7 | 14 |
| 5 | Specialist Structures | 8–10 | 4 |

---

## 3. Family Cluster Map

Position of each product in the universe, organized by family (vertical) and complexity (horizontal).

```
COMPLEXITY →    2        3           4              5               6              7            8         10
            ┌────────┬───────────┬──────────────┬───────────────┬──────────────┬────────────┬─────────┬──────┐
   ELN      │ PPN    │ RC        │ KODRC        │ CRC           │ Phoenix      │ DKIP       │         │      │
   (15)     │        │ DRC       │ Airbag       │               │ FCN          │            │         │      │
            │        │ ICN       │ Bonus        │               │ CRA ELN      │            │         │      │
            │        │           │ Digital      │               │              │            │         │      │
            │        │           │ Booster      │               │              │            │         │      │
            │        │ Warrant   │              │               │              │            │         │      │
            ├────────┼───────────┼──────────────┼───────────────┼──────────────┼────────────┼─────────┼──────┤
   Swaps    │ VLSP   │ IRS       │ CommSwap     │ TRS           │              │ VarSwap    │         │      │
   (8)      │        │           │              │ EqSwap        │              │            │         │      │
            │        │           │              │ CDS           │              │            │         │      │
            │        │           │              │ XCCY          │              │            │         │      │
            ├────────┼───────────┼──────────────┼───────────────┼──────────────┼────────────┼─────────┼──────┤
   SRT      │        │           │ ZCL          │ IR Callable   │ NCRA         │ CRA SRT    │         │      │
   (5)      │        │           │              │ Digital CF    │              │            │         │      │
            ├────────┼───────────┼──────────────┼───────────────┼──────────────┼────────────┼─────────┼──────┤
   STEG     │        │           │              │ Vanilla STEG  │ Callable STEG│ RA STEG    │TARN STEG│      │
   (4)      │        │           │              │               │              │            │         │      │
            ├────────┼───────────┼──────────────┼───────────────┼──────────────┼────────────┼─────────┼──────┤
   CLN      │        │           │ CLN          │ Skew CLN      │              │ FTD        │ NTD     │ CDO  │
   (5)      │        │           │              │               │              │            │         │      │
            ├────────┼───────────┼──────────────┼───────────────┼──────────────┼────────────┼─────────┼──────┤
   Other    │ SD     │ VO        │ SHRK         │ Opt-on-RC     │ ACCUM        │ SNOW       │ WOAC    │      │
   (12)     │ FWD    │ ELO       │              │               │ DECUM        │ CLIQ       │         │      │
            │        │ DCI       │              │               │              │            │         │      │
            └────────┴───────────┴──────────────┴───────────────┴──────────────┴────────────┴─────────┴──────┘
```

**49 products placed. All cells verified against Complexity Registry.**

---

## 4. Evolution Layer

**Graph type:** Directed acyclic graph (DAG)
**Edge meaning:** "Product A evolves into Product B by adding one structural feature"
**Source:** Atlas Appendix C (frozen)
**Edges:** 42
**Roots:** 8 (PPN, IRS, IR Callable, Vanilla STEG, CLN, SD, FWD, VO)
**Leaves:** 34

### 4.1 Complete Edge List

Each edge represents one structural innovation added to the parent product.

#### ELN Family — 14 edges

| # | From | To | Feature Added |
|:-:|------|----|--------------:|
| 1 | PPN (2) | RC (3) | Short put replaces call |
| 2 | PPN (2) | Booster (4) | Leveraged call spread |
| 3 | PPN (2) | Warrant (3) | Exchange-traded wrapper |
| 4 | RC (3) | DRC (3) | Discount replaces coupon |
| 5 | RC (3) | ICN (3) | Issuer call right |
| 6 | RC (3) | CRC (5) | Bermudan call |
| 7 | RC (3) | KODRC (4) | Knock-out barrier |
| 8 | RC (3) | Airbag (4) | Leverage + put spread |
| 9 | RC (3) | Bonus (4) | Down-and-in barrier |
| 10 | RC (3) | Digital (4) | Binary/digital payoff |
| 11 | RC (3) | CRA ELN (6) | Range accrual + callable |
| 12 | RC (3) | Phoenix (6) | Autocall + memory coupon |
| 13 | Digital (4) | DKIP (7) | Knock-in put |
| 14 | Phoenix (6) | FCN (6) | Fixed coupon replaces conditional |

#### Swaps Family — 7 edges

| # | From | To | Feature Added |
|:-:|------|----|--------------:|
| 15 | IRS (3) | TRS (5) | Total return replication |
| 16 | IRS (3) | CDS (5) | Credit event contingency |
| 17 | IRS (3) | XCCY (5) | Second currency + FX forward |
| 18 | IRS (3) | CommSwap (4) | Commodity reference price |
| 19 | IRS (3) | VarSwap (7) | Variance strike + convex payoff |
| 20 | IRS (3) | VLSP (2) | Simplified variant |
| 21 | TRS (5) | EqSwap (5) | Equity-specific specialization |

#### SRT Family — 4 edges

| # | From | To | Feature Added |
|:-:|------|----|--------------:|
| 22 | IR Callable (5) | ZCL (4) | Zero-coupon accretion |
| 23 | IR Callable (5) | NCRA (6) | Range accrual condition |
| 24 | IR Callable (5) | Digital CF (5) | Digital rate-linked coupon |
| 25 | NCRA (6) | CRA SRT (7) | Add callability |

#### STEG Family — 3 edges

| # | From | To | Feature Added |
|:-:|------|----|--------------:|
| 26 | Vanilla STEG (5) | Callable STEG (6) | Bermudan call right |
| 27 | Vanilla STEG (5) | RA STEG (7) | Range accrual on spread |
| 28 | Vanilla STEG (5) | TARN STEG (8) | Target accumulation |

#### CLN Family — 4 edges

| # | From | To | Feature Added |
|:-:|------|----|--------------:|
| 29 | CLN (4) | Skew CLN (5) | Non-linear recovery |
| 30 | CLN (4) | FTD (7) | Basket + first-default trigger |
| 31 | FTD (7) | NTD (8) | Nth-default threshold |
| 32 | FTD (7) | CDO (10) | Portfolio + tranching |

#### Cross-Family — 10 edges

| # | From | From Family | To | To Family | Feature Added |
|:-:|------|-------------|----|-----------|--------------:|
| 33 | RC (3) | ELN | Opt-on-RC (5) | Other | Compound option layer |
| 34 | RC (3) | ELN | DCI (3) | Other | FX underlying |
| 35 | PPN (2) | ELN | SHRK (4) | Other | KO barrier + rebate |
| 36 | PPN (2) | ELN | CLIQ (7) | Other | Forward-starting options |
| 37 | Phoenix (6) | ELN | SNOW (7) | Other | Cumulative coupon |
| 38 | Phoenix (6) | ELN | WOAC (8) | Other | Worst-of basket |
| 39 | SD (2) | Other | ELO (3) | Other | Equity-linked option wrapper |
| 40 | FWD (2) | Other | ACCUM (6) | Other | Daily forwards + gearing |
| 41 | VO (3) | Other | ELO (3) | Other | Retail wrapper |
| 42 | ACCUM (6) | Other | DECUM (6) | Other | Mirror (sell direction) |

### 4.2 Evolution Roots (8 products)

Products with no incoming evolution edge. Each is the ancestor of its family subtree.

| Root | Family | Descendants | Largest Branch |
|------|--------|:-----------:|----------------|
| PPN (2) | ELN | 14 (within ELN) + 6 (cross-family) | RC → Phoenix → FCN |
| IRS (3) | Swaps | 6 | TRS → EqSwap |
| IR Callable (5) | SRT | 4 | NCRA → CRA SRT |
| Vanilla STEG (5) | STEG | 3 | (all direct children) |
| CLN (4) | CLN | 4 | FTD → NTD / CDO |
| SD (2) | Other | 1 | ELO (shared with VO) |
| FWD (2) | Other | 2 | ACCUM → DECUM |
| VO (3) | Other | 1 | ELO (shared with SD) |

### 4.3 Evolution Leaves (34 products)

Products with no outgoing evolution edge. Terminal nodes in the evolution graph.

| Family | Leaves |
|--------|--------|
| ELN (11) | DRC, ICN, CRC, KODRC, Airbag, Bonus, Booster, Warrant, FCN, CRA ELN, DKIP |
| Swaps (6) | VLSP, CommSwap, CDS, XCCY, EqSwap, VarSwap |
| SRT (3) | ZCL, Digital CF, CRA SRT |
| STEG (3) | Callable STEG, RA STEG, TARN STEG |
| CLN (3) | Skew CLN, NTD, CDO |
| Other (8) | ELO, DCI, SHRK, Opt-on-RC, DECUM, SNOW, CLIQ, WOAC |

---

## 5. Dependency Layer

**Graph type:** Directed acyclic graph (DAG)
**Edge meaning:** "You must understand Product A before learning Product B"
**Source:** Learning Dependency Graph
**Edges:** 53
**Roots:** 4 (FWD, SD, PPN, VLSP)
**Leaves:** 31
**Maximum chain depth:** 5

### 5.1 Complete Prerequisite Map

For each product: direct prerequisites and dependency depth (longest chain to a Tier 1 root).

#### Tier 1 — Foundation (4 products, Depth 0)

| Product | Prerequisites | Depth |
|---------|:------------:|:-----:|
| FWD (2) | — | 0 |
| SD (2) | — | 0 |
| PPN (2) | — | 0 |
| VLSP (2) | — | 0 |

#### Tier 2 — Core Structures (8 products, Depth 1–2)

| Product | Prerequisites | Depth |
|---------|:------------:|:-----:|
| VO (3) | FWD | 1 |
| IRS (3) | FWD | 1 |
| RC (3) | PPN | 1 |
| DRC (3) | RC | 2 |
| ICN (3) | RC | 2 |
| Warrant (3) | VO | 2 |
| ELO (3) | VO | 2 |
| DCI (3) | RC | 2 |

#### Tier 3 — Structured Products (19 products, Depth 1–4)

| Product | Prerequisites | Depth |
|---------|:------------:|:-----:|
| KODRC (4) | RC | 2 |
| Airbag (4) | RC | 2 |
| Bonus (4) | RC | 2 |
| Digital (4) | RC | 2 |
| Booster (4) | PPN | 1 |
| CommSwap (4) | IRS | 2 |
| ZCL (4) | PPN, IRS | 2 |
| CLN (4) | CDS | 3 |
| SHRK (4) | PPN | 1 |
| CRC (5) | RC | 2 |
| TRS (5) | IRS | 2 |
| EqSwap (5) | TRS | 3 |
| CDS (5) | IRS | 2 |
| XCCY (5) | IRS | 2 |
| IR Callable (5) | IRS | 2 |
| Digital CF (5) | IRS, Digital | 3 |
| Vanilla STEG (5) | IRS | 2 |
| Skew CLN (5) | CLN | 4 |
| Opt-on-RC (5) | RC, VO | 2 |

#### Tier 4 — Advanced Structures (14 products, Depth 2–4)

| Product | Prerequisites | Depth |
|---------|:------------:|:-----:|
| Phoenix (6) | RC | 2 |
| FCN (6) | Phoenix | 3 |
| CRA ELN (6) | Digital, CRC | 3 |
| NCRA (6) | IR Callable, Digital CF | 3 |
| Callable STEG (6) | Vanilla STEG | 3 |
| ACCUM (6) | FWD, VO | 2 |
| DECUM (6) | ACCUM | 3 |
| DKIP (7) | Digital, KODRC | 3 |
| VarSwap (7) | VO | 2 |
| CRA SRT (7) | NCRA, IR Callable | 4 |
| RA STEG (7) | Vanilla STEG, NCRA | 3 |
| FTD (7) | CLN | 4 |
| SNOW (7) | Phoenix | 3 |
| CLIQ (7) | PPN, VO | 2 |

#### Tier 5 — Specialist Structures (4 products, Depth 3–5)

| Product | Prerequisites | Depth |
|---------|:------------:|:-----:|
| TARN STEG (8) | Vanilla STEG | 3 |
| NTD (8) | FTD | 5 |
| WOAC (8) | Phoenix | 3 |
| CDO (10) | FTD | 5 |

### 5.2 Dependency Roots (4 products)

Products requiring no prior product knowledge. Entry points to the universe.

| Root | Role | Unlocks |
|------|------|---------|
| FWD (2) | Foundation of all derivatives | VO, IRS → entire Swaps/SRT/STEG/CLN branches |
| PPN (2) | Foundation of capital protection | RC → entire ELN branch |
| SD (2) | Simplest structured product | Standalone. Conceptual foundation only |
| VLSP (2) | Parallel rates entry | Standalone. Simplified IRS for orientation |

### 5.3 Dependency Leaves (31 products)

Products that no other product requires as a prerequisite.

| Tier | Leaves |
|:----:|--------|
| T1 | SD, VLSP |
| T2 | DRC, ICN, Warrant, ELO, DCI |
| T3 | Airbag, Bonus, Booster, CommSwap, EqSwap, XCCY, ZCL, SHRK, Skew CLN, Opt-on-RC |
| T4 | FCN, CRA ELN, Callable STEG, DECUM, DKIP, VarSwap, CRA SRT, RA STEG, SNOW, CLIQ |
| T5 | TARN STEG, NTD, WOAC, CDO |

### 5.4 Longest Dependency Chains

| Chain | Length | Path |
|:-----:|:------:|------|
| 1 | 5 | FWD → IRS → CDS → CLN → FTD → NTD |
| 2 | 5 | FWD → IRS → CDS → CLN → FTD → CDO |
| 3 | 4 | FWD → IRS → CDS → CLN → Skew CLN |
| 4 | 4 | FWD → IRS → IR Callable → NCRA → CRA SRT |
| 5 | 4 | FWD → IRS → CDS → CLN → FTD |

---

## 6. Learning Layer

**Graph type:** Sequenced paths (total orderings within each path)
**Edge meaning:** "Study Product A, then Product B next"
**Source:** Learning Dependency Graph
**Paths:** 5
**Combined coverage:** 49 / 49

### 6.1 Equity Path (25 products)

```
Phase 1 Foundation:  PPN(2) → VO(3) → RC(3)
Phase 2 RC Variants: DRC(3) → ICN(3) → DCI(3)
Phase 3 Barriers:    KODRC(4) → Airbag(4) → Bonus(4) → SHRK(4)
Phase 4 Coupons:     Digital(4) → Booster(4) → CRC(5) → Warrant(3) → ELO(3)
Phase 5 Autocall:    Phoenix(6) → FCN(6) → SNOW(7) → WOAC(8)
Phase 6 Complex:     CRA ELN(6) → DKIP(7) → CLIQ(7) → Opt-on-RC(5)
Phase 7 Non-ELN Eq:  ACCUM(6) → DECUM(6)
```

### 6.2 Rates Path (14 products)

```
Phase 1 Foundation:  FWD(2) → VLSP(2) → IRS(3)
Phase 2 SRT:         IR Callable(5) → ZCL(4) → Digital CF(5) → NCRA(6) → CRA SRT(7)
Phase 3 STEG:        Vanilla STEG(5) → Callable STEG(6) → RA STEG(7) → TARN STEG(8)
Phase 4 FX:          XCCY(5)
Phase 5 Commodity:   CommSwap(4)
```

### 6.3 Credit Path (8 products)

```
Phase 1 Foundation:  FWD(2) → IRS(3) → CDS(5)
Phase 2 Funded:      CLN(4) → Skew CLN(5)
Phase 3 Basket:      FTD(7) → NTD(8)
Phase 4 Portfolio:   CDO(10)
```

### 6.4 Volatility Path (20 products)

```
Phase 1 Foundation:  FWD(2) → VO(3) → Warrant(3)
Phase 2 Long Vega:   PPN(2) → SD(2) → Booster(4) → SHRK(4) → ELO(3) → CLIQ(7)
Phase 3 Short Vega:  RC(3) → DRC(3) → CRC(5) → FCN(6) → DCI(3) → WOAC(8)
Phase 4 Complex:     Phoenix(6) → KODRC(4) → Digital(4) → ACCUM(6)
Phase 5 Pure Vol:    VarSwap(7)
```

### 6.5 Beginner → Expert Roadmap

| Weeks | Tier | Products | Cumulative |
|:-----:|:----:|:--------:|:----------:|
| 1–2 | T1 Foundation | SD, FWD, PPN, VLSP | 4 |
| 2–4 | T2 Core | VO, IRS, RC, DRC, ICN, Warrant, ELO, DCI | 12 |
| 5–8 | T3 Structured | KODRC, Airbag, Bonus, Digital, Booster, SHRK, CommSwap, ZCL, CLN, CRC, TRS, CDS, EqSwap, XCCY, IR Callable, Digital CF, Vanilla STEG, Skew CLN, Opt-on-RC | 31 |
| 9–12 | T4 Advanced | Phoenix, FCN, CRA ELN, NCRA, Callable STEG, ACCUM, DECUM, DKIP, VarSwap, CRA SRT, RA STEG, FTD, SNOW, CLIQ | 45 |
| 13–16 | T5 Specialist | TARN STEG, NTD, WOAC, CDO | 49 |

---

## 7. Cross-Family Interaction Layer

Products whose understanding requires concepts from a different family.

### 7.1 Cross-Family Evolution Edges (10 of 42 total)

| From | From Family | To | To Family | Innovation |
|------|:-----------:|----|-----------:|:----------:|
| RC (3) | ELN | Opt-on-RC (5) | Other | Compound option |
| RC (3) | ELN | DCI (3) | Other | FX underlying |
| PPN (2) | ELN | SHRK (4) | Other | KO barrier |
| PPN (2) | ELN | CLIQ (7) | Other | Forward-starting |
| Phoenix (6) | ELN | SNOW (7) | Other | Cumulative coupon |
| Phoenix (6) | ELN | WOAC (8) | Other | Worst-of basket |
| SD (2) | Other | ELO (3) | Other | Option wrapper |
| FWD (2) | Other | ACCUM (6) | Other | Daily forwards |
| VO (3) | Other | ELO (3) | Other | Retail wrapper |
| ACCUM (6) | Other | DECUM (6) | Other | Mirror direction |

### 7.2 Cross-Family Dependency Edges (12 of 53 total)

Products whose learning prerequisites span families.

| Product | Own Family | Prerequisite | Prereq Family |
|---------|:----------:|:------------:|:-------------:|
| CLN (4) | CLN | CDS (5) | Swaps |
| ZCL (4) | SRT | PPN (2) | ELN |
| ZCL (4) | SRT | IRS (3) | Swaps |
| Digital CF (5) | SRT | Digital (4) | ELN |
| Digital CF (5) | SRT | IRS (3) | Swaps |
| Opt-on-RC (5) | Other | RC (3) | ELN |
| RA STEG (7) | STEG | NCRA (6) | SRT |
| ACCUM (6) | Other | FWD (2) | Other |
| ACCUM (6) | Other | VO (3) | Other |
| CLIQ (7) | Other | PPN (2) | ELN |
| CLIQ (7) | Other | VO (3) | Other |
| SNOW (7) | Other | Phoenix (6) | ELN |
| WOAC (8) | Other | Phoenix (6) | ELN |

### 7.3 Family Interaction Summary

```
         ELN ──────────→ Other
          │                 ↑
          │    PPN ────────→ SHRK, CLIQ
          │    RC ─────────→ DCI, Opt-on-RC
          │    Phoenix ────→ SNOW, WOAC
          │    Digital ───→ Digital CF (SRT)
          │    PPN ───────→ ZCL (SRT)
          │
          ↓
        Swaps ──────────→ SRT ──────────→ STEG
          │                 │
          │    IRS ────────→ IR Callable    NCRA ────→ RA STEG
          │    CDS ────────→ CLN (credit)
          │
          ↓
         CLN
```

**Most dependent family:** SRT (requires concepts from ELN + Swaps)
**Most exported family:** ELN (provides concepts to SRT + Other + Swaps via CDS→CLN)
**Self-contained families:** Swaps (except CDS→CLN), STEG (except RA STEG←NCRA)

---

## 8. Root Node Analysis

### 8.1 Evolution Roots (8)

| Root | Complexity | Family | Out-Degree | Universe Reach |
|------|:----------:|:------:|:----------:|:--------------:|
| PPN (2) | 2 | ELN | 3 direct, 20 transitive | 40.8% of universe |
| IRS (3) | 3 | Swaps | 6 direct | 12.2% of universe |
| IR Callable (5) | 5 | SRT | 3 direct, 4 transitive | 8.2% of universe |
| Vanilla STEG (5) | 5 | STEG | 3 direct | 6.1% of universe |
| CLN (4) | 4 | CLN | 2 direct, 4 transitive | 8.2% of universe |
| FWD (2) | 2 | Other | 1 direct, 2 transitive | 4.1% of universe |
| SD (2) | 2 | Other | 1 direct (shared) | 2.0% of universe |
| VO (3) | 3 | Other | 1 direct (shared) | 2.0% of universe |

**PPN is the most prolific evolution root** — its descendants (via RC) account for 20 of 49 products.

### 8.2 Dependency Roots (4)

| Root | Universe Coverage via Prerequisites | Key Unlock |
|------|:-----------------------------------:|------------|
| FWD (2) | 26 products reachable | VO, IRS → all Swaps, SRT, STEG, CLN |
| PPN (2) | 20 products reachable | RC → all ELN, many Other |
| SD (2) | 0 products (standalone) | Conceptual foundation only |
| VLSP (2) | 0 products (standalone) | Parallel rates entry |

**FWD and PPN together unlock 46 of 49 products** (94%). The remaining 3 (SD, VLSP, and overlapping ELO which is reachable from both) are Tier 1/2 standalone entry points.

---

## 9. Most Connected Products

### 9.1 By Evolution Out-Degree

Products with the most outgoing evolution edges.

| Rank | Product | Out-Degree | Children |
|:----:|---------|:----------:|----------|
| 1 | **RC (3)** | 11 | DRC, ICN, CRC, KODRC, Airbag, Bonus, Digital, CRA ELN, Phoenix, DCI, Opt-on-RC |
| 2 | IRS (3) | 6 | TRS, CDS, XCCY, CommSwap, VarSwap, VLSP |
| 3 | PPN (2) | 5 | RC, Booster, Warrant, SHRK, CLIQ |
| 4 | Phoenix (6) | 3 | FCN, SNOW, WOAC |
| 5 | IR Callable (5) | 3 | ZCL, NCRA, Digital CF |
| 5 | Vanilla STEG (5) | 3 | Callable STEG, RA STEG, TARN STEG |

**RC is the single most connected product in the universe** with 11 direct evolution children (9 within ELN + 2 cross-family).

### 9.2 By Dependency Out-Degree (products most needed as prerequisites)

| Rank | Product | Products That Require It | Count |
|:----:|---------|-------------------------|:-----:|
| 1 | **RC (3)** | DRC, ICN, DCI, KODRC, Airbag, Bonus, Digital, CRC, Phoenix, CRA ELN, Opt-on-RC | 11 |
| 2 | IRS (3) | CommSwap, TRS, CDS, XCCY, IR Callable, Vanilla STEG, ZCL, Digital CF | 8 |
| 3 | VO (3) | Warrant, ELO, VarSwap, Opt-on-RC, ACCUM, CLIQ | 6 |
| 4 | PPN (2) | RC, Booster, SHRK, ZCL, CLIQ | 5 |
| 5 | Phoenix (6) | FCN, SNOW, WOAC | 3 |

### 9.3 By Combined Connectivity (In + Out, both graphs)

| Product | Evo In | Evo Out | Dep In | Dep Out | Total |
|---------|:------:|:-------:|:------:|:-------:|:-----:|
| RC (3) | 1 | 11 | 1 | 11 | 24 |
| IRS (3) | 0 | 6 | 1 | 8 | 15 |
| PPN (2) | 0 | 5 | 0 | 5 | 10 |
| Phoenix (6) | 1 | 3 | 1 | 3 | 8 |
| VO (3) | 0 | 1 | 1 | 6 | 8 |

---

## 10. Complexity Heat Map

Distribution of products across complexity scores.

```
Score 2:  ████                           4 products  (8.2%)
Score 3:  ████████                       8 products  (16.3%)
Score 4:  █████████                      9 products  (18.4%)
Score 5:  ██████████                    10 products  (20.4%)
Score 6:  ███████                        7 products  (14.3%)
Score 7:  ███████                        7 products  (14.3%)
Score 8:  ███                            3 products  (6.1%)
Score 9:                                 0 products  (0%)
Score 10: █                              1 product   (2.0%)
```

### Distribution by Family

| Family | Min | Median | Max | Spread |
|--------|:---:|:------:|:---:|:------:|
| ELN | 2 | 4 | 7 | 5 |
| Swaps | 2 | 5 | 7 | 5 |
| SRT | 4 | 5 | 7 | 3 |
| STEG | 5 | 6.5 | 8 | 3 |
| CLN | 4 | 5 | 10 | 6 |
| Other | 2 | 4.5 | 8 | 6 |

**CLN has the widest complexity spread** (4–10), containing both moderate (CLN at 4) and the universe maximum (CDO at 10).

### Tier Density

| Tier | Products | % of Universe | Density Label |
|:----:|:--------:|:-------------:|:------------:|
| T1 | 4 | 8% | Sparse — entry points |
| T2 | 8 | 16% | Moderate — core toolkit |
| T3 | 19 | 39% | Dense — main body |
| T4 | 14 | 29% | Dense — specialist zone |
| T5 | 4 | 8% | Sparse — expert only |

**68% of all products are in Tiers 3–4** (complexity 4–7). This is the working universe for most structured products desks.

---

## 11. Interview Hotspots

Products most likely to appear in structured products interviews, mapped onto the universe.

### 11.1 Top 10 Interview Products

| Priority | Product | Tier | Family | Why It's Asked |
|:--------:|---------|:----:|:------:|----------------|
| 1 | RC (3) | T2 | ELN | Yield enhancement archetype. "Where does the coupon come from?" |
| 2 | Phoenix (6) | T4 | ELN | Most traded autocallable. Barrier + memory + autocall |
| 3 | IRS (3) | T2 | Swaps | Most liquid OTC derivative. DV01, swap valuation |
| 4 | CDS (5) | T3 | Swaps | Credit risk transfer. Credit events, recovery |
| 5 | PPN (2) | T1 | ELN | Capital protection. "Why isn't participation 100%?" |
| 6 | VarSwap (7) | T4 | Swaps | Pure vol. Convexity. Separates intermediate from advanced |
| 7 | CDO (10) | T5 | CLN | Tranching, correlation, 2008 crisis |
| 8 | WOAC (8) | T5 | Other | Basket correlation. "Why does adding stocks increase risk?" |
| 9 | ACCUM (6) | T4 | Other | Gearing asymmetry. Leveraged obligation |
| 10 | FTD (7) | T4 | CLN | Basket default. "Why does low correlation increase risk?" |

### 11.2 Interview Hotspot Locations in Universe

```
TIER →     T1         T2           T3          T4            T5
         ┌──────┬──────────┬──────────┬────────────┬────────────┐
   ELN   │★PPN  │★RC       │          │★Phoenix    │            │
         ├──────┼──────────┼──────────┼────────────┼────────────┤
   Swaps │      │★IRS      │★CDS      │★VarSwap    │            │
         ├──────┼──────────┼──────────┼────────────┼────────────┤
   CLN   │      │          │          │★FTD        │★CDO        │
         ├──────┼──────────┼──────────┼────────────┼────────────┤
   Other │      │          │          │★ACCUM      │★WOAC       │
         └──────┴──────────┴──────────┴────────────┴────────────┘
```

**Interview hotspot pattern:** 2 products per tier (except T3 which has 1). Hotspots cluster at family roots (RC, IRS, PPN) and correlation products (CDO, WOAC, FTD).

### 11.3 Top 8 Confusion Pairs

Pairs interviewers use to test differentiation:

| Pair | Products | The Question |
|:----:|----------|:------------:|
| 1 | PPN vs RC | Protection buyer vs protection seller |
| 2 | Phoenix vs FCN | Conditional vs guaranteed coupon |
| 3 | FTD vs NTD | Correlation reversal |
| 4 | CLN vs CDS | Funded vs unfunded credit |
| 5 | ACCUM vs DECUM | Buy vs sell obligation |
| 6 | IRS vs VLSP | Standard vs customised swap |
| 7 | Phoenix vs WOAC | Single vs worst-of basket |
| 8 | PPN vs SHRK | Plain vs barrier protection |

---

## 12. Risk Concentration Zones

Regions of the universe where specific risk types cluster.

### 12.1 Volatility Exposure Map

| Zone | Products | Count | Family Concentration |
|------|----------|:-----:|---------------------|
| **No Vol** | IRS, ZCL, FWD | 3 | Linear products only |
| **Low Vol** | TRS, CDS, VLSP, CLN, Skew CLN, FTD, NTD, CDO | 8 | Credit family + simple swaps |
| **Long Vega** | PPN, Booster, Warrant, SD, VO, ELO, EqSwap, CommSwap, Vanilla STEG, CLIQ | 10 | Buyer-friendly: retail + capital-protected |
| **Short Vega** | RC, DRC, CRC, ICN, FCN, CRA ELN, DKIP, Bonus, IR Callable, NCRA, CRA SRT, Callable STEG, DCI, SNOW, WOAC | 15 | ELN yield-enhanced + SRT callable |
| **Complex** | Phoenix, KODRC, Airbag, Digital, VarSwap, XCCY, Digital CF, RA STEG, TARN STEG, Opt-on-RC, ACCUM, DECUM, SHRK | 13 | Barrier products + multi-factor |

**Short Vega is the largest risk zone** (15 products). Desks running ELN and callable SRT books are structurally short volatility.

### 12.2 Correlation Exposure Map

| Zone | Products | Count |
|------|----------|:-----:|
| **None** | 40 products | 40 |
| **Moderate** | XCCY, Vanilla STEG, Callable STEG, RA STEG, TARN STEG | 5 |
| **High** | FTD, NTD, WOAC | 3 |
| **Extreme** | CDO | 1 |

**Correlation risk concentrates in two families:** STEG (curve correlation, 4 of 5 moderate) and CLN (credit correlation, FTD/NTD/CDO). WOAC is the only non-CLN, non-STEG product with high correlation.

### 12.3 Path Dependency Map

| Zone | Products | Count |
|------|----------|:-----:|
| **None** | 24 products (all T1/T2 + simple T3) | 24 |
| **Low** | CRC, FCN, ICN, Warrant, Digital, Digital CF, Vanilla STEG, Callable STEG | 8 |
| **Moderate** | Phoenix, KODRC, Bonus, CRA ELN, DKIP, VarSwap, NCRA, CRA SRT, RA STEG, CDO, SHRK, WOAC | 12 |
| **High** | TARN STEG, ACCUM, DECUM, SNOW, CLIQ | 5 |

**High path dependency concentrates in 5 products** with daily observation or target accumulation mechanics.

### 12.4 Capital Protection Map

| Zone | Products | Count |
|------|----------|:-----:|
| **Full** | PPN, Digital, CRA ELN, ZCL, NCRA, CRA SRT, Digital CF, Vanilla STEG, RA STEG, Callable STEG, TARN STEG, SD, SHRK, CLIQ | 14 |
| **Conditional** | RC, Phoenix, DRC, KODRC, Bonus, FCN, ICN, DKIP, CLN, Skew CLN, FTD, NTD, SNOW, WOAC | 14 |
| **None / N/A** | Booster, IR Callable, FWD, ACCUM, DECUM + all 8 Swaps (N/A) | 13 |
| **Other** | Airbag (Partial), VO/ELO (Premium-limited), Warrant (None), Opt-on-RC (Compound), CDO (Tranche-dep.) | 8 |

**Full and Conditional protection split evenly at 14 each.** Capital-protected products cluster in SRT and STEG families. Conditional products cluster in ELN and CLN.

### 12.5 Credit Exposure Map

| Zone | Products | Count | Risk Profile |
|------|----------|:-----:|:-------------|
| **Issuer** | 27 products (all ELN notes + SRT/STEG notes) | 27 | Single-name issuer default |
| **Counterparty** | 11 products (all Swaps + FWD + ACCUM + DECUM) | 11 | Bilateral swap exposure |
| **Ref + Issuer** | CLN, Skew CLN, FTD, NTD | 4 | Dual credit — reference AND issuer |
| **Issuer/Cpty** | CRA SRT, SNOW, WOAC | 3 | Hybrid wrap |
| **Cpty + Ref** | CDS | 1 | Unfunded credit transfer |
| **Portfolio** | CDO | 1 | 100+ reference names |
| **Exchange** | VO, Warrant | 2 | Clearing house guarantee |

**55% of products carry issuer credit risk.** The CLN family uniquely carries dual credit exposure (reference entity AND note issuer).

---

## 13. Navigation Instructions

### How to Use This Map

**Finding a product:** Use the Family Cluster Map (Section 3) to locate a product by family and complexity. Every product appears exactly once.

**Understanding where a product came from:** Use the Evolution Layer (Section 4). Find the product and trace backwards to its evolution root.

**Understanding what to learn first:** Use the Dependency Layer (Section 5). Find the product and trace its prerequisites. All chains resolve to one of 4 Tier 1 roots.

**Planning a study path:** Use the Learning Layer (Section 6). Choose the path matching your focus (Equity, Rates, Credit, Volatility) or follow the Beginner → Expert Roadmap for full coverage.

**Finding related products:** Use the Cross-Family Interaction Layer (Section 7) to identify concepts that bridge families.

**Preparing for interviews:** Use the Interview Hotspots (Section 11) for the 10 highest-priority products and 8 comparison pairs.

### Graph Navigation Rules

| Question | Layer | Start Point | Direction |
|----------|:-----:|:------------|:---------:|
| "What evolved into X?" | Evolution | X | Trace backward |
| "What did X evolve into?" | Evolution | X | Trace forward |
| "What must I know before X?" | Dependency | X | Trace backward |
| "What can I learn after X?" | Dependency | X | Trace forward |
| "What should I study next?" | Learning | Current position | Follow path |
| "How does X relate to Y?" | All three | X and Y | Compare positions |

### Quick Reference: Product Lookup

| Product | Section | Family | Tier | Complexity | Evo Parent | Dep Parents |
|---------|:-------:|:------:|:----:|:----------:|:----------:|:------------|
| PPN | 5.1.1 | ELN | T1 | 2 | (root) | — |
| RC | 5.1.2 | ELN | T2 | 3 | PPN | PPN |
| Phoenix | 5.1.3 | ELN | T4 | 6 | RC | RC |
| DRC | 5.1.4 | ELN | T2 | 3 | RC | RC |
| KODRC | 5.1.5 | ELN | T3 | 4 | RC | RC |
| CRC | 5.1.6 | ELN | T3 | 5 | RC | RC |
| Airbag | 5.1.7 | ELN | T3 | 4 | RC | RC |
| Bonus | 5.1.8 | ELN | T3 | 4 | RC | RC |
| FCN | 5.1.9 | ELN | T4 | 6 | Phoenix | Phoenix |
| CRA ELN | 5.1.10 | ELN | T4 | 6 | RC | Digital, CRC |
| ICN | 5.1.11 | ELN | T2 | 3 | RC | RC |
| Digital | 5.1.12 | ELN | T3 | 4 | RC | RC |
| Booster | 5.1.13 | ELN | T3 | 4 | PPN | PPN |
| DKIP | 5.1.14 | ELN | T4 | 7 | Digital | Digital, KODRC |
| Warrant | 5.1.15 | ELN | T2 | 3 | PPN | VO |
| IRS | 5.2.1 | Swaps | T2 | 3 | (root) | FWD |
| TRS | 5.2.2 | Swaps | T3 | 5 | IRS | IRS |
| EqSwap | 5.2.3 | Swaps | T3 | 5 | TRS | TRS |
| VarSwap | 5.2.4 | Swaps | T4 | 7 | IRS | VO |
| CDS | 5.2.5 | Swaps | T3 | 5 | IRS | IRS |
| XCCY | 5.2.6 | Swaps | T3 | 5 | IRS | IRS |
| CommSwap | 5.2.7 | Swaps | T3 | 4 | IRS | IRS |
| VLSP | 5.2.8 | Swaps | T1 | 2 | IRS | — |
| IR Callable | 5.3.1 | SRT | T3 | 5 | (root) | IRS |
| ZCL | 5.3.2 | SRT | T3 | 4 | IR Callable | PPN, IRS |
| NCRA | 5.3.3 | SRT | T4 | 6 | IR Callable | IR Callable, Digital CF |
| CRA SRT | 5.3.4 | SRT | T4 | 7 | NCRA | NCRA, IR Callable |
| Digital CF | 5.3.5 | SRT | T3 | 5 | IR Callable | IRS, Digital |
| Vanilla STEG | 5.4.1 | STEG | T3 | 5 | (root) | IRS |
| RA STEG | 5.4.2 | STEG | T4 | 7 | Vanilla STEG | Vanilla STEG, NCRA |
| Callable STEG | 5.4.3 | STEG | T4 | 6 | Vanilla STEG | Vanilla STEG |
| TARN STEG | 5.4.4 | STEG | T5 | 8 | Vanilla STEG | Vanilla STEG |
| CLN | 5.5.1 | CLN | T3 | 4 | (root) | CDS |
| Skew CLN | 5.5.2 | CLN | T3 | 5 | CLN | CLN |
| FTD | 5.5.3 | CLN | T4 | 7 | CLN | CLN |
| NTD | 5.5.4 | CLN | T5 | 8 | FTD | FTD |
| CDO | 5.5.5 | CLN | T5 | 10 | FTD | FTD |
| SD | 5.6.1 | Other | T1 | 2 | (root) | — |
| FWD | 5.6.2 | Other | T1 | 2 | (root) | — |
| VO | 5.6.3 | Other | T2 | 3 | (root) | FWD |
| ELO | 5.6.4 | Other | T2 | 3 | SD, VO | VO |
| Opt-on-RC | 5.6.5 | Other | T3 | 5 | RC | RC, VO |
| ACCUM | 5.6.6 | Other | T4 | 6 | FWD | FWD, VO |
| DECUM | 5.6.7 | Other | T4 | 6 | ACCUM | ACCUM |
| DCI | 5.6.8 | Other | T2 | 3 | RC | RC |
| SHRK | 5.6.9 | Other | T3 | 4 | PPN | PPN |
| SNOW | 5.6.10 | Other | T4 | 7 | Phoenix | Phoenix |
| CLIQ | 5.6.11 | Other | T4 | 7 | PPN | PPN, VO |
| WOAC | 5.6.12 | Other | T5 | 8 | Phoenix | Phoenix |

---

## 14. Traceability

### Atlas → Matrix → Dependency → Universe

Each product flows through all 4 artifacts with consistent identity.

| Source | What It Provides | Key Fields |
|--------|-----------------|------------|
| **Atlas** (frozen) | Product identity, DNA cards, evolution chains | Section, Name, Abbreviation, Family, Complexity, 16 DNA fields |
| **Matrix** | 12 comparison dimensions per product | Capital Protection, Yield, Liquidity, Credit, Vol, Correlation, Path, Buyer, Use Case, Risk, Hedge |
| **Dependency Graph** | Prerequisites, tiers, learning paths | Prereq products, prereq concepts, depth, tier, 5 paths |
| **Evolution Map** | Family trees, cross-family links | 42 evolution edges, visual spec |
| **Universe Map** | All of the above in navigable form | All 3 graph systems unified |

### Verification Chain

| Check | Method | Result |
|-------|--------|:------:|
| 49 products in all artifacts | Count per artifact | **PASS** |
| Section numbers consistent | Cross-reference all 4 sources | **PASS** |
| Complexity scores consistent | Cross-reference Registry, Atlas, Matrix, Dep Graph, Evo Map | **PASS** |
| Family assignments consistent | Cross-reference all 4 sources | **PASS** |
| 42 evolution edges preserved | Compare Evo Map edges vs Atlas Appendix C | **PASS** |
| 53 dependency edges preserved | Compare Dep Graph prerequisites vs Universe Layer 5 | **PASS** |
| 5 tiers preserved | Compare Dep Graph tiers vs Universe Layer 5/6 | **PASS** |
| 5 learning paths preserved | Compare Dep Graph paths vs Universe Layer 6 | **PASS** |

### Traceability Matrix (49 × 4 artifacts)

Every product has a verified entry in:

| Artifact | Entry Type | Count |
|----------|-----------|:-----:|
| Atlas | DNA Card (16 fields + cheat sheet) | 49 / 49 |
| Matrix | Row in 3-part table (12 dimensions) | 49 / 49 |
| Dependency Graph | Entry in Master Dependency Table | 49 / 49 |
| Universe Map | Entry in Quick Reference Lookup | 49 / 49 |

**Full traceability confirmed. No orphans in any artifact.**

---

## Universe Map Statistics

| Metric | Value |
|--------|:-----:|
| Total products | 49 |
| Total families | 6 |
| Total tiers | 5 |
| Evolution edges | 42 |
| Dependency edges | 53 |
| Learning paths | 5 |
| Evolution roots | 8 |
| Evolution leaves | 34 |
| Dependency roots | 4 |
| Dependency leaves | 31 |
| Cross-family evolution edges | 10 |
| Cross-family dependency edges | 12 |
| Maximum evolution depth | 5 |
| Maximum dependency depth | 5 |
| Most connected product | RC (24 total connections) |
| Most complex product | CDO (10) |
| Interview hotspot products | 10 |
| Risk zones mapped | 5 |

---

*Structured Products Universe Map — 49 products, 6 families, 3 graph systems, 42 evolution edges, 53 dependency edges, 5 learning paths. Generated 2026-06-22.*
