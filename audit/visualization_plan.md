# Desk Bible v2 — Visualization Plan

**Date:** 2026-06-19
**Status:** PLANNING — awaiting approval before any creation work begins.

---

## Design Principles

1. Every diagram should be understandable without reading the surrounding text.
2. Use consistent visual language: same colors for same concepts across all diagrams.
3. Diagrams should answer a specific question, not just decorate.
4. Tables are visualizations too — prefer tables over prose for comparisons.

---

## Priority Key

| Priority | Meaning |
|----------|---------|
| **P1 — Critical** | The section cannot achieve its purpose without this visual. |
| **P2 — Important** | Significantly improves comprehension. |
| **P3 — Useful** | Adds value but section works without it. |

---

## 1. Product Construction and Framework Diagrams

### 1.1 Four-Leg Framework Diagram — P1
**Location:** Part 2.3
**Type:** Flow diagram
**Purpose:** Show how the four legs connect: Client → Note Leg → Issuer Leg → Deposit Leg → Hedge Leg → Market
**Content:**
```
┌─────────┐     Note Leg      ┌──────────┐     Issuer Leg     ┌──────────┐
│  CLIENT  │ ──────────────── │  ISSUER  │ ──────────────── │  BANK    │
│          │  Principal +     │  (SPV)   │  Internal        │  BALANCE │
│          │  Coupon/Redemp   │          │  Liability       │  SHEET   │
└─────────┘                   └──────────┘                   └──────────┘
                                                                  │
                                    Deposit Leg                   │
                              ┌──────────────────────────────────┘
                              │  FTP / Internal Funding
                              ▼
                         ┌──────────┐     Hedge Leg      ┌──────────┐
                         │ TREASURY │ ──────────────── │  MARKET  │
                         │          │  Delta, Vega,     │  (OTC /  │
                         └──────────┘  Options, Swaps   │ Exchange)│
                                                        └──────────┘
```
**Shows:** P&L flows, risk transfer, where each desk sits.

### 1.2 Product Construction Decomposition — P1
**Location:** Part 2.2
**Type:** Stacked diagram
**Purpose:** Show Bond + Option = Structured Product visually
**Content:** For a Reverse Convertible:
- Layer 1: Bond (funding at issuer credit curve)
- Layer 2: Short Put (sold to client, premium funds coupon)
- Layer 3: Desk Margin
- Result: Structured Note (client receives enhanced coupon, bears downside)

### 1.3 Capital Protection Spectrum — P2
**Location:** Part 2.4
**Type:** Horizontal spectrum / gradient bar
**Purpose:** Show the continuum from full protection to zero protection
**Content:**
```
Full Protection ◄──────────────────────────────────────► Zero Protection
     PPN          Airbag      RC/DRC/Phoenix     Warrant
  (100% capital)  (conditional  (conditional      (full
   guaranteed)     leveraged)    at barrier)      exposure)
```
**Shows:** How protection level drives coupon — arrow from high protection/low coupon to low protection/high coupon.

---

## 2. Product Taxonomy Visuals

### 2.1 Product Taxonomy Tree — P1
**Location:** Part 3.1
**Type:** Tree / hierarchy diagram
**Purpose:** Show all ~42 products organized by family
**Content:**
```
Structured Products
├── Equity-Linked Notes (15)
│   ├── Reverse Convertible Variants
│   │   ├── RC
│   │   ├── DRC
│   │   ├── KODRC
│   │   ├── CRC
│   │   └── Airbag
│   ├── Autocallable Variants
│   │   ├── Phoenix
│   │   ├── FCN
│   │   └── Callable Range Accrual
│   └── Other ELNs
│       ├── Bonus / Participation
│       ├── PPN
│       ├── Warrant / Turbo
│       ├── ICN
│       ├── Digital Coupon
│       ├── Booster
│       └── Digital KI Put
├── Credit-Linked Notes (5)
│   ├── Single-Name (Vanilla CLN, Skew CLN)
│   ├── Basket (FTD, NTD)
│   └── Portfolio (Synthetic Tranche)
├── Swaps (7)
│   ├── IRS, TRS, Equity, Currency, Commodity, CDS, VLSP
├── Structured Rate Trades (5)
│   ├── IR Callable, IR Accreting/ZCL, NCRA, CRA, Digital Cap-Floor
├── Steepener Notes (4)
│   ├── Vanilla, Range Accrual, Callable, TARN
└── Other (5)
    ├── Structured Deposits, Accumulators, Option on RC, ELO, Forwards
```

### 2.2 Product Complexity Map — P2
**Location:** Part 3.2 or Part 7.4
**Type:** Scatter plot or tiered diagram
**Purpose:** Map products by complexity (X-axis) and risk profile (Y-axis)
**Content:**
- X-axis: Simple (closed-form) → Complex (path-dependent Monte Carlo)
- Y-axis: Short vol → Long vol → Short correlation
- Plot all ~42 products

---

## 3. Payoff Diagrams — P1

### 3.1 Standard Payoff Diagrams
**Location:** Part 5 (one per product deep dive)
**Type:** P&L vs Underlying Price at maturity
**Count:** ~15 key payoff diagrams (not all 42 — group similar products)

| Diagram | Products Covered |
|---------|-----------------|
| Reverse Convertible payoff | RC, DRC (discount variant shown) |
| Knock-Out Discounted RC payoff | KODRC (showing barrier region) |
| Phoenix Autocallable payoff (multi-period) | Phoenix, FCN |
| Callable RC payoff | CRC, ICN |
| Airbag / Leveraged payoff | Airbag |
| Bonus / Participation payoff | Bonus |
| Principal Protected payoff | PPN |
| Range Accrual coupon diagram | CRAELN, NCRA, CRA, RASTEG |
| Steepener coupon diagram | VSTEG, CSTEG, TARN |
| CLN payoff (credit event) | Vanilla CLN, Skew CLN |
| FTD/NTD loss waterfall | FTD, NTD |
| Tranche attachment/detachment | Synthetic CDO Tranche |
| IRS cashflow diagram | IRS, VLSP |
| CDS cashflow diagram | CDS |
| Accumulator payoff | Accumulator / Decumulator |

---

## 4. Barrier Mechanics Diagrams — P1

### 4.1 Barrier Types Comparison — P1
**Location:** Part 1.3
**Type:** Side-by-side diagrams
**Purpose:** Show KI, KO, European vs American observation
**Content:**
- Panel A: Knock-In barrier — price path crossing barrier activates option
- Panel B: Knock-Out barrier — price path crossing barrier deactivates option
- Panel C: European (final observation only) vs American (continuous) barrier
- Each panel shows a price path with barrier level marked

### 4.2 Barrier Proximity Risk — P2
**Location:** Part 1.3 or Part 5 (RC section)
**Type:** Delta/Gamma sensitivity chart
**Purpose:** Show why barrier proximity is the highest operational risk
**Content:** Delta as a function of spot price, with sharp discontinuity near barrier.

---

## 5. Lifecycle Diagrams

### 5.1 Product Lifecycle Timeline — P1
**Location:** Part 2.5
**Type:** Horizontal timeline
**Purpose:** Show the full life of a structured product
**Content:**
```
Origination → Pricing → Termsheet → Booking → [Coupon Obs.] → [Barrier Obs.] → [Autocall Check] → ... → Maturity/Early Redemption → Settlement
```
Key events marked: trade date, issue date, observation dates, coupon payment dates, maturity date.

### 5.2 Autocall Decision Flowchart — P1
**Location:** Part 5.1.6 (Phoenix) and Part 1.3 (reference)
**Type:** Decision tree / flowchart
**Purpose:** Walk through what happens at each observation date
**Content:**
```
Observation Date N
    │
    ▼
Is Worst-Of ≥ Autocall Barrier?
    ├── YES → Autocall triggered
    │         Pay: Principal + Final Coupon + Memory Coupons
    │         Trade terminates
    │
    └── NO → Is Worst-Of ≥ Coupon Barrier?
              ├── YES → Pay coupon for this period
              │         Store any missed coupons (memory)
              │         Continue to next observation
              │
              └── NO → No coupon this period
                        Missed coupon stored in memory
                        Continue to next observation
```

### 5.3 Trade Lifecycle Swim Lane — P2
**Location:** Part 2.6
**Type:** Swim lane diagram (horizontal lanes by role)
**Purpose:** Show who does what across the trade lifecycle
**Content:**
- Lanes: Front Office, Middle Office, Risk, Operations, Product Control
- Timeline: Pre-trade → Trade → Post-trade → Maturity
- Key handoffs and systems used at each stage

---

## 6. System Architecture Diagrams

### 6.1 System Architecture Map — P1
**Location:** Part 6.1
**Type:** System relationship diagram
**Purpose:** Show how NEMO, Sophis, and Murex relate
**Content:**
```
┌──────────┐        ┌──────────┐        ┌──────────┐
│  NEMO    │◄──────►│  SOPHIS  │        │  MUREX   │
│ (Book of │  feed  │ (Pricing │        │ (Rates/  │
│  Record) │        │  & Risk) │        │  STEG)   │
└────┬─────┘        └────┬─────┘        └────┬─────┘
     │                   │                   │
     │    ┌──────────────┘                   │
     │    │                                  │
     ▼    ▼                                  ▼
┌────────────┐                         ┌──────────┐
│ PRODUCT    │                         │ FOUR-LEG │
│ CONTROL    │                         │ BOOKING  │
│ (Recon,    │                         │ (Note,   │
│  P&L)     │                         │  Issuer, │
└────────────┘                         │  Deposit,│
                                       │  Hedge)  │
                                       └──────────┘
```

### 6.2 System Routing Decision Tree — P2
**Location:** Part 6.1 or Part 7.2
**Type:** Decision tree
**Purpose:** Answer "which system does this product use?"
**Content:**
```
Is it an ELN or CLN?
├── YES → NEMO (book) + Sophis (pricing)
└── NO → Is it an SRT or STEG?
         ├── YES → Murex (four-leg framework)
         └── NO → Is it a Swap?
                  ├── YES → Murex
                  └── NO → [Product-specific]
```

### 6.3 Booking Flow Diagrams — P1
**Location:** Part 6.2
**Type:** Sequential flow (one per product family)
**Count:** 4 booking flows

| Flow | Products | Key Steps |
|------|----------|-----------|
| ELN Booking | All ELNs + CLNs | Termsheet → NEMO entry → Sophis feed → Risk → P&L |
| Murex Four-Leg | SRT + STEG | Termsheet → Note Leg → Issuer Leg → Deposit Leg → Hedge Leg |
| Swap Booking | IRS, TRS, etc. | Confirmation → Murex entry → Collateral |
| CLN Booking | All CLNs | Similar to ELN but with credit reference setup |

---

## 7. Credit Diagrams

### 7.1 Credit Waterfall (CLN Family) — P1
**Location:** Part 5.2
**Type:** Waterfall / flow diagram
**Purpose:** Show what happens when a credit event occurs
**Content:**
```
Reference Entity
    │
    ▼
Credit Event? (Bankruptcy / Failure to Pay / Restructuring)
    │
    ├── NO → Coupon payments continue → Principal repaid at maturity
    │
    └── YES → Determine Recovery Rate
              │
              ▼
         Settlement:
         ├── Cash: Pay (Notional × (1 − Recovery Rate))
         └── Physical: Deliver defaulted bonds
```

### 7.2 Tranche Structure Diagram — P1
**Location:** Part 5.2.5
**Type:** Stacked bar / waterfall
**Purpose:** Show attachment and detachment points, loss absorption
**Content:**
```
100% ┌────────────────────┐
     │   Super Senior     │  (above detachment — no loss until below here)
     │                    │
 D%  ├────────────────────┤ ← Detachment Point
     │   TRANCHE SOLD     │  (investor bears losses in this band)
     │   (Mezzanine)      │
 A%  ├────────────────────┤ ← Attachment Point
     │   Equity / First   │  (first loss — absorbed before tranche)
     │   Loss             │
  0% └────────────────────┘
```

### 7.3 FTD/NTD Correlation Diagram — P2
**Location:** Part 5.2.3 / 5.2.4
**Type:** Conceptual diagram
**Purpose:** Show how correlation affects FTD vs NTD risk
**Content:** Two scenarios — high correlation (defaults cluster → FTD safer, NTD riskier) vs low correlation (defaults independent → FTD riskier, NTD safer).

---

## 8. Rate and Curve Diagrams

### 8.1 Yield Curve Diagram — P1
**Location:** Part 1.7
**Type:** Line chart
**Purpose:** Show normal, flat, and inverted yield curves
**Content:** Three curves plotted on Yield (Y) vs Maturity (X):
- Normal (upward sloping)
- Flat
- Inverted (downward sloping)

### 8.2 CMS Spread Diagram — P1
**Location:** Part 5.5 (STEG products)
**Type:** Annotated yield curve
**Purpose:** Show how CMS 30Y − CMS 2Y spread works
**Content:**
```
Yield
  │        ╱──── 30Y CMS
  │      ╱
  │    ╱───── 2Y CMS
  │  ╱        ↑ CMS Spread = 30Y − 2Y
  │╱
  └────────────────── Maturity
```
Shows: steepening (spread widens) and flattening (spread narrows) scenarios.

### 8.3 Swap Cashflow Diagram — P1
**Location:** Part 5.3.1 (IRS)
**Type:** Two-way arrow diagram
**Purpose:** Show what each party pays in a swap
**Content:**
```
┌──────────┐    Fixed Rate (e.g. 3.5%)    ┌──────────┐
│  FIXED   │ ────────────────────────── │ FLOATING │
│  PAYER   │                              │  PAYER   │
│          │ ◄──────────────────────── │          │
└──────────┘    Floating (SOFR + spread)  └──────────┘
                    │
                    ▼
              Periodic netting
```

### 8.4 Cap/Floor/Swaption Payoff — P2
**Location:** Part 1.7
**Type:** Payoff diagrams
**Purpose:** Visual payoff of rate options

---

## 9. Greek Sensitivity Diagrams

### 9.1 Delta Profile Near Barrier — P2
**Location:** Part 1.4 or Part 5.1.1
**Type:** Line chart
**Purpose:** Show Delta discontinuity near KI barrier
**Content:** Delta (Y) vs Spot Price (X), with sharp jump at barrier level.

### 9.2 Vega Term Structure — P3
**Location:** Part 1.5
**Type:** Line chart
**Purpose:** Show how Vega sensitivity varies with time to maturity
**Content:** Vega (Y) vs Time to Maturity (X), showing ATM vega peak.

### 9.3 Volatility Surface — P3
**Location:** Part 1.5
**Type:** 3D surface or contour plot
**Purpose:** Show implied vol as function of strike and maturity
**Content:** Strike (X) vs Maturity (Y) vs Implied Vol (Z), showing skew.

---

## 10. Comparison Tables (Tabular Visualizations)

These are the 11 tables identified in the gap analysis. They are text-based but function as visual aids.

| Table | Location | Columns | Rows | Priority |
|-------|----------|---------|:----:|:--------:|
| ELN Master Matrix | Part 4.1 | Product, Coupon, Barrier, Autocall, Protection, Put, Underlying, Greeks, System, Client, Complexity | 15 | P1 |
| RC Variant Comparison | Part 4.2 | Product, What Changes, Coupon Impact, Risk Impact | 5 | P1 |
| Autocallable Comparison | Part 4.3 | Product, Coupon Type, Memory, Underlying, Observation | 3 | P1 |
| CLN Family Matrix | Part 4.4 | Product, Reference Type, Correlation, Loss Mechanics, Recovery | 5 | P1 |
| STEG Family Matrix | Part 4.5 | Product, CMS Reference, Coupon Mechanics, Optionality, Path Dependency | 4 | P1 |
| SRT Family Matrix | Part 4.6 | Product, Callable, Accreting, Digital, Rate Reference | 5 | P2 |
| Swaps Matrix | Part 4.7 | Product, What Exchanged, Settlement, Collateral, Typical Use | 7 | P1 |
| System Routing | Part 7.2 | Product, NEMO, Sophis, Murex, Four-Leg | ~42 | P1 |
| Risk Profile Matrix | Part 7.3 | Product, Short Vol, Long Vol, Short Corr, Primary Greeks | ~42 | P2 |
| Capital Protection | Part 7.3 | Product, Protection Type, Barrier, Level | ~42 | P2 |
| Complexity Ranking | Part 7.4 | Product, Tier, Model Type, Components | ~42 | P2 |

---

## Visualization Summary

| Category | Count | P1 | P2 | P3 |
|----------|:-----:|:--:|:--:|:--:|
| Framework diagrams | 3 | 2 | 1 | — |
| Taxonomy visuals | 2 | 1 | 1 | — |
| Payoff diagrams | 15 | 15 | — | — |
| Barrier diagrams | 2 | 1 | 1 | — |
| Lifecycle diagrams | 3 | 2 | 1 | — |
| System diagrams | 3 | 2 | 1 | — |
| Booking flows | 4 | 4 | — | — |
| Credit diagrams | 3 | 2 | 1 | — |
| Rate/curve diagrams | 4 | 3 | 1 | — |
| Greek sensitivity | 3 | — | 1 | 2 |
| Comparison tables | 11 | 7 | 4 | — |
| **Total** | **53** | **39** | **12** | **2** |

---

## Format Recommendations

| Visual Type | Recommended Format | Rationale |
|-------------|-------------------|-----------|
| Flow diagrams | SVG or embedded vector | Scalable, editable, clear at any size |
| Payoff diagrams | Generated charts (matplotlib/plotly → SVG) | Accurate, consistent, reproducible |
| Comparison tables | Native markdown/DOCX tables | Searchable, editable, lightweight |
| Taxonomy trees | SVG or indented text | Tree structure clearest in vector |
| Swim lane diagrams | SVG | Multiple lanes need precise alignment |
| Yield curves | Generated charts → SVG | Accurate curve shapes |
| System architecture | SVG | Box-and-arrow, needs labels |

---

## Implementation Approach

1. **Phase 1 — Tables first:** Build all 11 comparison tables as they require no graphic design, just data extraction from V1 and sources.
2. **Phase 2 — Core diagrams:** Four-Leg Framework, Product Taxonomy Tree, System Architecture Map, Product Lifecycle Timeline. These are referenced most frequently.
3. **Phase 3 — Payoff diagrams:** Generate 15 payoff diagrams. Consider scripting for consistency (same axis scales, same colors, same labels).
4. **Phase 4 — Supporting diagrams:** Barrier mechanics, credit waterfall, tranche structure, swap cashflows, CMS spread, booking flows.
5. **Phase 5 — Nice-to-have:** Greek sensitivity charts, volatility surface, complexity scatter plot.
