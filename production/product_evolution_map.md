# Product Evolution Map

**Desk Bible v2 — Family Evolution & Visual Specification Layer**

**Families:** 6
**Products:** 49
**Evolution Chains:** 6
**Cross-Family Links:** 10
**Framework:** v1.3.1 (frozen)
**Generated:** 2026-06-22

---

## Table of Contents

1. [Reading Guide](#reading-guide)
2. [ELN Family Evolution](#eln-family-evolution)
3. [Swaps Family Evolution](#swaps-family-evolution)
4. [SRT Family Evolution](#srt-family-evolution)
5. [STEG Family Evolution](#steg-family-evolution)
6. [CLN Family Evolution](#cln-family-evolution)
7. [Other Family Evolution](#other-family-evolution)
8. [Cross-Family Dependency Map](#cross-family-dependency-map)
9. [Complexity Progression Summary](#complexity-progression-summary)
10. [Visual Specification for Universe Map](#visual-specification-for-universe-map)

---

## Reading Guide

### Notation

- `→` = direct evolution (add one feature)
- `┬` = branching point (multiple products evolve from one ancestor)
- `(N)` = complexity score
- `[TN]` = dependency tier (T1–T5)
- `+feature` = what was added in the evolution step
- `★` = cross-family dependency (product uses concepts from another family)

### Evolution Principle

Each arrow adds exactly ONE structural innovation to its parent. If two features are added simultaneously, the product appears at the end of a two-step chain.

---

## ELN Family Evolution

**Family:** Equity-Linked Notes (5.1.x)
**Products:** 15
**Root:** PPN (5.1.1)
**Complexity Range:** 2–7
**Maximum Chain Depth:** 3

### Evolution Tree

```
PPN (2) [T1]
├── +short put ────────── RC (3) [T2]
│   ├── +discount ──────── DRC (3) [T2]
│   ├── +issuer call ───── ICN (3) [T2]
│   ├── +callable ──────── CRC (5) [T3]
│   ├── +KO barrier ───── KODRC (4) [T3]
│   ├── +leverage ──────── Airbag (4) [T3]
│   ├── +DI barrier ───── Bonus (4) [T3]
│   ├── +digital payoff ── Digital (4) [T3]
│   │   └── +KI put ──────── DKIP (7) [T4]
│   ├── +range accrual ── CRA ELN (6) [T4]
│   ├── +autocall ──────── Phoenix (6) [T4]
│   │   └── +fixed coupon ── FCN (6) [T4]
│   └── +FX underlying ── DCI (3) [T2]
│
├── +leverage ─────────── Booster (4) [T3]
└── +warrant wrapper ──── Warrant (3) [T2]
```

### Feature Additions (Chronological)

| Step | From | To | Feature Added | Complexity Change |
|:----:|------|----|--------------|-----------------:|
| 1 | PPN (2) | RC (3) | Short put replaces call | +1 |
| 2 | PPN (2) | Booster (4) | Leveraged call spread | +2 |
| 3 | PPN (2) | Warrant (3) | Exchange-traded wrapper | +1 |
| 4 | RC (3) | DRC (3) | Discount instead of coupon | 0 |
| 5 | RC (3) | ICN (3) | Issuer Bermudan call | 0 |
| 6 | RC (3) | CRC (5) | Bermudan call on coupon | +2 |
| 7 | RC (3) | Airbag (4) | Leverage + put spread | +1 |
| 8 | RC (3) | Bonus (4) | Down-and-in barrier | +1 |
| 9 | RC (3) | Digital (4) | Binary/digital payoff | +1 |
| 10 | RC (3) | Phoenix (6) | Autocall + memory coupon + barrier | +3 |
| 11 | RC (3) | DCI (3) | FX underlying substitution | 0 |
| 12 | RC (3) | KODRC (4) | Knock-out barrier | +1 |
| 13 | RC (3) | CRA ELN (6) | Range accrual + callable | +3 |
| 14 | Digital (4) | DKIP (7) | Knock-in put + dual condition | +3 |
| 15 | Phoenix (6) | FCN (6) | Guaranteed fixed coupon | 0 |

### Key Branching Points

- **PPN** branches 3 ways: RC (yield enhancement path), Booster (leverage path), Warrant (exchange path)
- **RC** branches 11 ways: the most prolific ancestor in the entire universe (DRC, ICN, CRC, KODRC, Airbag, Bonus, Digital, CRA ELN, Phoenix, DCI + cross-family Opt-on-RC)
- **Digital** branches 1 way: dual conditional (DKIP)
- **Phoenix** branches 1 way within ELN (FCN), plus 2 cross-family (SNOW, WOAC)

---

## Swaps Family Evolution

**Family:** Swaps & Derivatives (5.2.x)
**Products:** 8
**Root:** IRS (5.2.1) — but IRS itself evolves from FWD concept
**Complexity Range:** 2–7
**Maximum Chain Depth:** 2

### Evolution Tree

```
FWD (2) [T1] (Other family — conceptual root)
└── +fixed/floating swap ── IRS (3) [T2]
    ├── +total return ──── TRS (5) [T3]
    │   └── +equity-only ── EqSwap (5) [T3]
    ├── +credit events ──── CDS (5) [T3]
    ├── +second currency ── XCCY (5) [T3]
    ├── +commodity ref ──── CommSwap (4) [T3]
    └── +variance strike ── VarSwap (7) [T4]

VLSP (2) [T1] — simplified IRS (parallel entry point, not a derivative)
```

### Feature Additions

| Step | From | To | Feature Added | Complexity Change |
|:----:|------|----|--------------|-----------------:|
| 1 | FWD (2) | IRS (3) | Fixed-for-floating periodic swap | +1 |
| 2 | IRS (3) | TRS (5) | Total return replication | +2 |
| 3 | IRS (3) | CDS (5) | Credit event contingent swap | +2 |
| 4 | IRS (3) | XCCY (5) | Second currency + FX forward | +2 |
| 5 | IRS (3) | CommSwap (4) | Commodity reference price | +1 |
| 6 | IRS (3) | VarSwap (7) | Variance strike + convex payoff | +4 |
| 7 | TRS (5) | EqSwap (5) | Equity-specific (dividends, corporate actions) | 0 |

### Key Branching Points

- **IRS** branches 5 ways: the swap family hub
- **VLSP** is standalone — simpler IRS with caps/floors, not a derivative of IRS

---

## SRT Family Evolution

**Family:** Structured Rate Trades (5.3.x)
**Products:** 5
**Root:** IR Callable (5.3.1)
**Complexity Range:** 4–7
**Maximum Chain Depth:** 2

### Evolution Tree

```
IRS (3) [T2] (Swaps family — conceptual root)
└── +embedded swaption ── IR Callable (5) [T3]
    ├── +zero coupon ────── ZCL (4) [T3] ★ uses PPN accretion concept
    ├── +digital strip ──── Digital CF (5) [T3] ★ uses Digital (ELN) payoff
    └── +range accrual ──── NCRA (6) [T4] ★ uses Digital CF strip
        └── +callable ───── CRA SRT (7) [T4] ★ uses IR Callable swaption
```

### Feature Additions

| Step | From | To | Feature Added | Complexity Change |
|:----:|------|----|--------------|-----------------:|
| 1 | IRS (3) | IR Callable (5) | Embedded swaption (four-leg SRT) | +2 |
| 2 | IR Callable (5) | ZCL (4) | Zero-coupon accretion | -1 |
| 3 | IR Callable (5) | Digital CF (5) | Digital caplet strip | 0 |
| 4 | IR Callable (5) | NCRA (6) | Range accrual on single rate | +1 |
| 5 | NCRA (6) | CRA SRT (7) | Add callable (swaption) to range accrual | +1 |

### Key Branching Points

- **IR Callable** branches 3 ways: zero-coupon, digital, range accrual
- **CRA SRT** recombines two paths: NCRA (range accrual) + IR Callable (callable feature)

### Cross-Family Dependencies

SRT is the most cross-dependent family:
- ZCL uses PPN accretion concept (ELN)
- Digital CF uses Digital payoff structure (ELN)
- NCRA builds on Digital CF digital strip
- CRA SRT recombines NCRA + IR Callable

---

## STEG Family Evolution

**Family:** Steepener Notes (5.4.x)
**Products:** 4
**Root:** Vanilla STEG (5.4.1)
**Complexity Range:** 5–8
**Maximum Chain Depth:** 1 (all branch from root)

### Evolution Tree

```
IRS (3) [T2] (Swaps family — conceptual root)
└── +CMS spread coupon ── Vanilla STEG (5) [T3]
    ├── +bank call right ── Callable STEG (6) [T4]
    ├── +range accrual ──── RA STEG (7) [T4] ★ uses NCRA (SRT) mechanism
    └── +target accum ───── TARN STEG (8) [T5]
```

### Feature Additions

| Step | From | To | Feature Added | Complexity Change |
|:----:|------|----|--------------|-----------------:|
| 1 | IRS (3) | Vanilla STEG (5) | CMS spread coupon + leverage | +2 |
| 2 | Vanilla STEG (5) | Callable STEG (6) | Bermudan call right | +1 |
| 3 | Vanilla STEG (5) | RA STEG (7) | Spread-based range accrual | +2 |
| 4 | Vanilla STEG (5) | TARN STEG (8) | Target accumulation + auto-termination | +3 |

### Key Characteristics

- Flattest family: all 3 variants branch directly from root
- Steepest complexity ramp: +3 from root to TARN in one step
- RA STEG has cross-family dependency on NCRA range accrual mechanism

---

## CLN Family Evolution

**Family:** Credit-Linked Notes (5.5.x)
**Products:** 5
**Root:** CLN (5.5.1)
**Complexity Range:** 4–10
**Maximum Chain Depth:** 2

### Evolution Tree

```
CDS (5) [T3] (Swaps family — conceptual root)
└── +note wrapper ─────── CLN (4) [T3]
    ├── +recovery skew ──── Skew CLN (5) [T3]
    └── +basket (n≥2) ──── FTD (7) [T4]
        ├── +nth trigger ── NTD (8) [T5]
        └── +tranching ──── CDO (10) [T5]
```

### Feature Additions

| Step | From | To | Feature Added | Complexity Change |
|:----:|------|----|--------------|-----------------:|
| 1 | CDS (5) | CLN (4) | Funded note wrapper, dual credit exposure | -1 |
| 2 | CLN (4) | Skew CLN (5) | Non-linear recovery payoff | +1 |
| 3 | CLN (4) | FTD (7) | Basket of names + first-default trigger + correlation | +3 |
| 4 | FTD (7) | NTD (8) | Nth-default threshold + correlation reversal | +1 |
| 5 | FTD (7) | CDO (10) | 100+ names + tranching + copula + loss waterfall | +3 |

### Key Characteristics

- **Longest dependency chain in the universe:** FWD → IRS → CDS → CLN → FTD → NTD/CDO (depth 5)
- **Highest complexity product:** CDO (10/10)
- **Correlation reversal:** FTD and NTD have opposite correlation sensitivity
- CLN is simpler than its parent CDS (note wrapper simplifies settlement)

---

## Other Family Evolution

**Family:** Other / Multi-Class (5.6.x)
**Products:** 12
**Roots:** SD (5.6.1), FWD (5.6.2)
**Complexity Range:** 2–8
**Maximum Chain Depth:** 3

### Evolution Tree

```
SD (2) [T1] ── (standalone entry point)

FWD (2) [T1]
├── +option layer ────── VO (3) [T2]
│   ├── +retail wrapper ── ELO (3) [T2]
│   └── +exchange traded ── (links to Warrant in ELN family)
│
├── +daily obligation ── ACCUM (6) [T4] ★ uses VO barrier concepts
│   └── +mirror (sell) ── DECUM (6) [T4]
│
└── (links to IRS in Swaps family)

PPN (2) [T1] (ELN family — conceptual root for some Other products)
├── +barrier + capped ── SHRK (4) [T3]
└── +forward-starting ── CLIQ (7) [T4] ★ uses VO forward vol concepts

RC (3) [T2] (ELN family — conceptual root)
├── +compound option ──── Opt-on-RC (5) [T3] ★ uses VO compound concept
└── +FX underlying ────── DCI (3) [T2] (listed in ELN tree too)

Phoenix (6) [T4] (ELN family — conceptual root)
├── +cumulative coupon ── SNOW (7) [T4]
└── +worst-of basket ──── WOAC (8) [T5]
```

### Feature Additions

| Step | From | To | Feature Added | Complexity Change |
|:----:|------|----|--------------|-----------------:|
| 1 | FWD (2) | VO (3) | Option payoff (asymmetric) | +1 |
| 2 | VO (3) | ELO (3) | Retail wrapper | 0 |
| 3 | FWD (2) | ACCUM (6) | Daily forward + gearing + KO | +4 |
| 4 | ACCUM (6) | DECUM (6) | Mirror (selling, down KO) | 0 |
| 5 | PPN (2) | SHRK (4) | Up-and-out barrier + rebate | +2 |
| 6 | PPN (2) | CLIQ (7) | Forward-starting options + periodic lock-in | +5 |
| 7 | RC (3) | Opt-on-RC (5) | Compound option layer | +2 |
| 8 | Phoenix (6) | SNOW (7) | Cumulative coupon accumulation | +1 |
| 9 | Phoenix (6) | WOAC (8) | Worst-of basket + correlation | +2 |

### Key Characteristics

- Most diverse family: roots in ELN, Swaps, and standalone
- **SD** has no descendants — pure foundation product
- **CLIQ** has the largest single-step complexity jump: PPN(2) → CLIQ(7) = +5
- SNOW and WOAC are conceptually ELN products but classified as Other due to distinct risk profiles

---

## Cross-Family Dependency Map

Products that require understanding concepts from families other than their own.

### Dependency Table

| Product | Own Family | Depends On | From Family | Dependency Type |
|---------|-----------|------------|-------------|----------------|
| CLN (4) | CLN | CDS (5) | Swaps | CDS mechanics |
| Skew CLN (5) | CLN | CDS (5) | Swaps | via CLN |
| FTD (7) | CLN | CDS (5) | Swaps | via CLN |
| NTD (8) | CLN | CDS (5) | Swaps | via CLN → FTD |
| CDO (10) | CLN | CDS (5) | Swaps | via CLN → FTD |
| ZCL (4) | SRT | PPN (2) | ELN | Accretion concept |
| Digital CF (5) | SRT | Digital (4) | ELN | Digital payoff |
| RA STEG (7) | STEG | NCRA (6) | SRT | Range accrual mechanism |
| DKIP (7) | ELN | KODRC (4) | ELN (same) | Barrier mechanics |
| CRA ELN (6) | ELN | CRC (5) | ELN (same) | Callable mechanics |
| Opt-on-RC (5) | Other | RC (3) | ELN | RC structure |
| Opt-on-RC (5) | Other | VO (3) | Other (same) | Compound option |
| ACCUM (6) | Other | VO (3) | Other (same) | Barrier/option |
| CLIQ (7) | Other | VO (3) | Other (same) | Forward vol |
| SNOW (7) | Other | Phoenix (6) | ELN (via Other) | Autocall + memory |
| WOAC (8) | Other | Phoenix (6) | ELN (via Other) | Autocall + basket |

### Cross-Family Flow

```
ELN ───────── SRT ──────── STEG
 │             │             │
 │ PPN ──────→ ZCL           │
 │ Digital ──→ Digital CF    │
 │             │             │
 │             NCRA ────────→ RA STEG
 │             │
 │             CRA SRT (recombines NCRA + IR Callable)
 │
 ├──────────── Other
 │ RC ──────→ Opt-on-RC, DCI
 │ Phoenix ──→ SNOW, WOAC
 │
Swaps ────────── CLN
 CDS ─────────→ CLN → FTD → NTD → CDO
```

---

## Complexity Progression Summary

Ordered list within each family, from simplest to most complex.

### ELN Family (15 products)

```
PPN (2) → RC (3) → DRC (3) → ICN (3) → Warrant (3) → KODRC (4)
→ Airbag (4) → Bonus (4) → Digital (4) → Booster (4) → CRC (5)
→ Phoenix (6) → FCN (6) → CRA ELN (6) → DKIP (7)
```

### Swaps Family (8 products)

```
VLSP (2) → IRS (3) → CommSwap (4) → TRS (5) → EqSwap (5)
→ CDS (5) → XCCY (5) → VarSwap (7)
```

### SRT Family (5 products)

```
ZCL (4) → IR Callable (5) → Digital CF (5) → NCRA (6) → CRA SRT (7)
```

### STEG Family (4 products)

```
Vanilla STEG (5) → Callable STEG (6) → RA STEG (7) → TARN STEG (8)
```

### CLN Family (5 products)

```
CLN (4) → Skew CLN (5) → FTD (7) → NTD (8) → CDO (10)
```

### Other Family (12 products)

```
SD (2) → FWD (2) → VO (3) → ELO (3) → DCI (3) → SHRK (4)
→ Opt-on-RC (5) → ACCUM (6) → DECUM (6) → SNOW (7) → CLIQ (7) → WOAC (8)
```

---

## Visual Specification for Universe Map

Specifications for the future Universe Map visual. These are rendering instructions — the actual map is NOT generated here.

### Node Specification

Each product is a node with these visual properties:

| Property | Source | Mapping |
|----------|--------|---------|
| **Label** | Atlas DNA card: Abbreviation | Text inside node |
| **Section** | Atlas DNA card: Section | Subtitle below label |
| **Size** | Complexity score | Small (2-3), Medium (4-5), Large (6-7), XL (8-10) |
| **Color** | Family | ELN: Blue, Swaps: Green, SRT: Orange, STEG: Purple, CLN: Red, Other: Grey |
| **Border** | Tier | T1: Solid thin, T2: Solid, T3: Dashed, T4: Double, T5: Bold double |
| **Shape** | Capital Protection | Full: Circle, Partial: Rounded rectangle, None: Rectangle, Conditional: Diamond |

### Edge Specification

| Edge Type | Visual | Meaning |
|-----------|--------|---------|
| Evolution (within family) | Solid arrow, family color | Product A evolves into Product B |
| Cross-family dependency | Dashed arrow, grey | Product requires concept from another family |
| Learning prerequisite | Dotted arrow, light | Suggested learning order (not structural) |

### Layout Rules

1. **Horizontal axis:** Complexity (left=simple, right=complex)
2. **Vertical axis:** Family grouping (6 horizontal bands)
3. **Cross-family links:** Vertical dashed arrows between bands
4. **Tier boundaries:** Vertical dividers at complexity 3/4, 5/6, 7/8

### Recommended Layout Dimensions

| Family | Band Height | Reason |
|--------|:----------:|--------|
| ELN | 3x | 15 products, dense branching |
| Swaps | 2x | 8 products, wide spread |
| SRT | 1x | 5 products, linear chain |
| STEG | 1x | 4 products, flat branching |
| CLN | 1.5x | 5 products, deep chain |
| Other | 2.5x | 12 products, multiple roots |

### Legend Specification

The map legend must include:
- Family color key (6 colors)
- Node size key (4 sizes → complexity ranges)
- Shape key (4 shapes → capital protection)
- Border key (5 borders → tiers)
- Edge key (3 types → evolution / cross-family / learning)

### Statistics Box

| Metric | Value |
|--------|:-----:|
| Total nodes | 49 |
| Within-family evolution edges | 35 |
| Cross-family evolution edges | 10 |
| Total evolution edges | 45 |
| Root nodes (Tier 1, no learning prereqs) | 4 (FWD, SD, PPN, VLSP) |
| Leaf nodes (no outgoing evolution) | 23 |
| Maximum chain length | 6 (FWD→IRS→CDS→CLN→FTD→NTD) |
| Most connected node | RC (9 within ELN + 2 cross-family = 11 outgoing) |

---

*Product Evolution Map — 49 products, 6 families, 35 within-family evolutions, 10 cross-family evolution edges, 45 total edges. Generated 2026-06-22. Revised 2026-06-27 (statistics corrected).*
