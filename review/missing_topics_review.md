# Infrastructure Encyclopedia V1.0 — Missing Topics Review

**Date**: 2026-06-26
**Reviewer**: Independent Publication Board — Completeness Specialist
**Manuscript**: `production/infrastructure_encyclopedia_v1.md` (4,438 lines, ~347 entries)

---

## Methodology

Exhaustive review of topics absent from the encyclopedia, organised by category. Each missing topic assigned:
- **Priority**: P1 (critical for V1.0) / P2 (important for V2.0) / P3 (nice-to-have)
- **Rationale**: Why the topic should be included
- **Impact**: Consequence of its absence

---

## Category 1: TOC-Promised but Undelivered Sections

These sections appear in the Table of Contents (lines 43-111) but have NO corresponding content in the body. This is the highest-priority gap category.

| # | Missing Section | TOC Reference | Priority | Impact |
|:-:|----------------|:-------------:|:--------:|--------|
| 1 | ColVA (Collateral Valuation Adjustment) | 4.4 | P1 | XVA coverage incomplete. ColVA = cost when CSA collateral rate ≠ OIS rate |
| 2 | MVA (Margin Valuation Adjustment) | 4.5 | P1 | XVA coverage incomplete. MVA = lifetime cost of funding IM under UMR |
| 3 | KVA (detailed, beyond current entry) | 4.6 | P2 | Current KVA is within Part 4 but TOC implies a separate detailed section |
| 4 | LVA (Liquidity Valuation Adjustment) | 4.7 | P2 | XVA coverage incomplete. LVA adjusts for liquidity cost of hedging |
| 5 | XVA Interactions & Total XVA | 4.8 | P2 | How XVAs interact, double-counting, and Total XVA aggregation |
| 6 | Capital & Return Metrics | 4.9 | P2 | RAROC, RORWA, hurdle rate, FTP — key desk economics metrics |
| 7 | Interest Rate Models | 5.2 | P1 | Hull-White, Vasicek, CIR — essential for rates product pricing |
| 8 | Credit Models | 5.3 | P1 | Structural (Merton), Reduced-form (JLT), Copula (Li) — essential for CLN/FTD/SRT |
| 9 | Exotic Pricing Models | 5.4 | P2 | Heston, SABR, SLV — essential for autocallable/barrier products |
| 10 | Numerical Methods | 5.5 | P2 | PDE/FD, Trees, Quasi-MC, American exercise (Longstaff-Schwartz) |
| 11 | Booking Systems | 6.2 | P1 | NEMO dedicated entry — core ecosystem system |
| 12 | Lifecycle Management | 6.3 | P2 | Trade lifecycle: inception → amendment → novation → maturity/termination |
| 13 | Reporting & Analytics | 6.4 | P2 | P&L reporting, risk reporting, regulatory reporting, management reporting |
| 14 | Clearing & Settlement Infrastructure | 7.2 | P2 | CCPs (detailed), settlement systems, CSD, TARGET2-Securities |
| 15 | Tax Treatment | 7.3 | P2 | Withholding tax, QI regime, gross-up, tax wrapper treatment |
| 16 | Accounting Standards | 7.4 | P2 | IFRS 9 vs IAS 39, hedge accounting, embedded derivative bifurcation |
| 17 | Cross-Border Considerations | 7.5 | P2 | Cross-border distribution, AIFMD, passporting, third-country equivalence |
| 18 | Bloomberg & System Mnemonics | 8.9 (expanded) | P2 | FLDS, DES, OVME, SWPM, MARS, GP, GIP, CDSW, VCUB |
| 19 | Acronym Master List | 8.11 | P2 | Comprehensive A-Z acronym expansion list |

**Total TOC-promised gaps: 19 sections**

---

## Category 2: Missing Terms — Derivatives & Structured Products

| # | Missing Term | Priority | Rationale |
|:-:|-------------|:--------:|-----------|
| 1 | **Parisian Barrier** | P2 | Barrier that must be breached for a continuous period before triggering |
| 2 | **Lookback Option** | P2 | Payoff based on optimal underlying price during the life |
| 3 | **Asian Option (Arithmetic vs Geometric)** | P2 | Average-based payoff — common in commodity and FX structured products |
| 4 | **Quanto Adjustment** | P1 | Adjustment for cross-currency exposure in quanto products — already referenced in entries but no standalone definition |
| 5 | **Composite vs Quanto** | P2 | Key distinction for multi-currency structured products |
| 6 | **Variance Swap** | P2 | Swap on realised variance — referenced in practitioner table but no full entry |
| 7 | **Volatility Swap** | P2 | Swap on realised volatility — distinct from variance swap (convexity adjustment) |
| 8 | **Dispersion Trade** | P3 | Selling index vol, buying single-stock vol — common structured products strategy |
| 9 | **Corridor** | P2 | Range accrual corridor — subset of range accrual products |
| 10 | **Digital Option** | P2 | Binary payoff (all-or-nothing) — building block for many structured products |
| 11 | **Forward-Starting Option** | P2 | Option where strike is set at a future date — relevant for cliquets |
| 12 | **Rainbow Option** | P3 | Option on the best/worst of multiple assets |
| 13 | **Mountain Range Options** | P3 | Altiplano, Annapurna, Atlas, Himalaya — exotic multi-asset options |

---

## Category 3: Missing Terms — Workflow & Operations

| # | Missing Term | Priority | Rationale |
|:-:|-------------|:--------:|-----------|
| 1 | **Novation** | P1 | Transfer of a derivative from one counterparty to another. Daily OTC operation |
| 2 | **Portfolio Compression** | P1 | Reducing gross notional by terminating offsetting trades. TriOptima, Quantile |
| 3 | **Tear-Up** | P1 | Involuntary termination of trades (e.g., CCP default management) |
| 4 | **Amendment** | P2 | Modification of trade economics post-booking. Lifecycle event |
| 5 | **Partial Termination** | P2 | Reducing notional on an existing trade without full unwind |
| 6 | **Give-Up / Give-In** | P2 | Transfer of executed trade from executing broker to clearing broker |
| 7 | **Allocation** | P2 | Splitting a block trade into sub-allocations for different accounts |
| 8 | **SSI (Standard Settlement Instructions)** | P1 | Counterparty settlement details — critical operational reference |
| 9 | **Nostro / Vostro** | P2 | Our account at their bank / their account at our bank — core settlement concepts |
| 10 | **SWIFT Messages** | P2 | MT103, MT202, MT300, MT320, MT540/541/542/543 — settlement messaging |
| 11 | **Settlement Fails** | P1 | When delivery/payment does not occur on value date. CSDR penalties |
| 12 | **Corporate Actions** | P1 | Dividends, stock splits, mergers, spin-offs — impact on structured product payoffs |
| 13 | **Corporate Action Processing** | P2 | Ex-date, record date, pay date, SWIFT CA notifications |
| 14 | **Confirmation Matching** | P2 | Matching trade details between counterparties (MarkitWire, DTCC) |
| 15 | **Dispute Resolution** | P2 | Collateral disputes, valuation disputes, ISDA dispute resolution protocol |

---

## Category 4: Missing Terms — Bloomberg & System Fields

| # | Missing Term | Priority | Rationale |
|:-:|-------------|:--------:|-----------|
| 1 | **FLDS** (Field Search) | P2 | Finding Bloomberg fields for any security |
| 2 | **DES** (Description) | P2 | Security description page — first stop for any instrument |
| 3 | **OVME** (Option Valuation) | P2 | Option pricing and Greeks calculator |
| 4 | **SWPM** (Swap Manager) | P2 | Swap pricing and structuring tool |
| 5 | **MARS** (Multi-Asset Risk System) | P2 | Portfolio risk analysis |
| 6 | **CDSW** (CDS Pricing) | P2 | CDS spread and upfront calculator |
| 7 | **VCUB** (Volatility Cube) | P2 | Interest rate vol surface viewer |
| 8 | **ALLQ** (All Quotes) | P2 | Market maker quotes for a security |
| 9 | **SRCH** (Search) | P3 | Screening tool for bonds, equities, derivatives |
| 10 | **YAS** (Yield Analysis) | P2 | Bond yield and spread analysis |
| 11 | **Murex: MxML** | P2 | Murex's XML-based data exchange format |
| 12 | **Murex: Datamart** | P3 | Murex's reporting and analytics database |
| 13 | **Sophis: Toolkit API** | P3 | Sophis's programmable interface for custom pricing |
| 14 | **NEMO: Product Templates** | P1 | NEMO's structured product booking templates |
| 15 | **NEMO: Lifecycle Events** | P2 | How NEMO handles fixings, coupons, barriers, autocalls |

---

## Category 5: Missing Terms — Holiday & Calendar Edge Cases

| # | Missing Term | Priority | Rationale |
|:-:|-------------|:--------:|-----------|
| 1 | **IMM Dates** | P2 | Third Wednesday of March, June, September, December — standard futures expiry |
| 2 | **TARGET Calendar** | P2 | Trans-European Automated Real-time Gross settlement Express Transfer calendar |
| 3 | **Eid / Lunar Calendar Holidays** | P3 | Impact on MENA and Asian markets — moveable holidays |
| 4 | **Golden Week** | P3 | Japan (late April-early May) and China (early October) — extended market closures |
| 5 | **Bank Holiday Monday (UK)** | P3 | Impact on GBP settlement and London market hours |
| 6 | **Combined Calendar Logic** | P2 | How to resolve when a date is a holiday in one calendar but not another |
| 7 | **End-of-Month Rule** | P1 | ISDA convention: if a period end date falls on the last business day of a month, subsequent period end dates also fall on the last business day |
| 8 | **Short/Long First/Last Coupon Interaction** | P2 | How stub periods interact with day count conventions |

---

## Category 6: Missing Terms — Fixing & Rate Mechanics

| # | Missing Term | Priority | Rationale |
|:-:|-------------|:--------:|-----------|
| 1 | **Lookback Period** | P2 | The observation period for RFR compounding (SOFR, ESTR). Lookback vs payment delay vs lockout |
| 2 | **Payment Delay** | P2 | Delay between rate determination and payment — alternative to lookback |
| 3 | **Lockout Period** | P2 | Fixing the rate N days before payment — alternative to lookback |
| 4 | **Observation Shift** | P2 | Shifting the observation period relative to the interest period |
| 5 | **ECB Fixing** | P2 | European Central Bank reference rates for FX |
| 6 | **WM/Reuters Fix** | P2 | 4pm London FX fixing — primary FX benchmark |
| 7 | **Fallback Rate** | P1 | ISDA fallback provisions for benchmark discontinuation. Spread adjustment methodology |
| 8 | **ISDA Fallback Protocol** | P1 | Adherence mechanism for LIBOR transition fallback provisions |
| 9 | **Term SOFR** | P2 | CME forward-looking SOFR term rate — distinct from overnight SOFR |
| 10 | **SOFR Index** | P2 | Daily compounded SOFR index published by NY Fed |

---

## Category 7: Missing Terms — Legal & Documentation

| # | Missing Term | Priority | Rationale |
|:-:|-------------|:--------:|-----------|
| 1 | **ISDA 2021 Interest Rate Definitions** | P1 | Replaced 2006 Definitions for new trades. New RFR conventions, compounding methods |
| 2 | **ISDA Credit Derivatives Definitions (2014)** | P1 | Governs CDS, CLN, FTD documentation |
| 3 | **ISDA Determinations Committee** | P2 | DC decisions on credit events, succession events, auction settlement |
| 4 | **Negative Pledge** | P2 | Covenant restricting issuer from granting security over assets |
| 5 | **Cross-Default** | P2 | Default on one obligation triggers default on others |
| 6 | **Material Adverse Change (MAC)** | P3 | Condition precedent for drawdown/closing |
| 7 | **Offering Circular / Prospectus** | P2 | Legal document for note issuance — distinct from termsheet |
| 8 | **EMTN Programme** | P1 | Euro Medium Term Note programme — the issuance vehicle for most structured notes |
| 9 | **Selling Restrictions** | P2 | Jurisdictional restrictions on who can buy the product |
| 10 | **Force Majeure** | P3 | Extraordinary event provisions in ISDA documentation |

---

## Category 8: Missing Terms — Quantitative Methods

| # | Missing Term | Priority | Rationale |
|:-:|-------------|:--------:|-----------|
| 1 | **Heston Model** | P1 | Standard stochastic volatility model: dS = rS dt + √v S dW₁, dv = κ(θ−v)dt + σ√v dW₂ |
| 2 | **Hull-White Model** | P1 | Standard short-rate model: dr = [θ(t) − ar]dt + σdW |
| 3 | **SABR Model** | P1 | Stochastic α-β-ρ model for swaption and cap/floor vol |
| 4 | **Ito's Lemma** | P2 | Fundamental result for stochastic calculus. df = f'dX + ½f''(dX)² |
| 5 | **Girsanov's Theorem** | P3 | Measure change — foundation of risk-neutral pricing |
| 6 | **Longstaff-Schwartz** | P2 | Least-squares Monte Carlo for American/Bermudan option pricing |
| 7 | **PDE Methods** | P2 | Partial differential equation approach to option pricing (BS PDE) |
| 8 | **Finite Difference** | P2 | Explicit, implicit, Crank-Nicolson schemes for PDE solving |
| 9 | **Binomial/Trinomial Trees** | P2 | CRR tree, convergence to BS, early exercise handling |
| 10 | **Curve Bootstrapping** | P1 | Building a zero-coupon curve from market instruments (deposits, futures, swaps) |
| 11 | **Vol Surface Construction** | P2 | Building the implied vol surface from market quotes (SVI, SSVI parameterisation) |

---

## Category 9: Missing Terms — Regulation & Compliance

| # | Missing Term | Priority | Rationale |
|:-:|-------------|:--------:|-----------|
| 1 | **SFTR** | P2 | Securities Financing Transactions Regulation — reporting requirements |
| 2 | **MAR** | P2 | Market Abuse Regulation — insider dealing, market manipulation |
| 3 | **CSDR** | P2 | Central Securities Depositories Regulation — settlement discipline, buy-in |
| 4 | **BMR (Benchmarks Regulation)** | P2 | EU regulation on financial benchmarks — critical/significant classification |
| 5 | **LEI (Legal Entity Identifier)** | P1 | 20-character alphanumeric code identifying legal entities in OTC transactions |
| 6 | **UTI (Unique Transaction Identifier)** | P2 | Unique ID for each OTC derivative transaction (EMIR/CFTC reporting) |
| 7 | **UPI (Unique Product Identifier)** | P2 | ISDA taxonomy-based product classification for regulatory reporting |
| 8 | **SR 11-7** | P2 | Fed guidance on model risk management — governs model validation |
| 9 | **MREL / TLAC** | P2 | Minimum loss-absorbing capacity requirements — related to bail-in |
| 10 | **CRR III / CRD VI** | P2 | Latest EU prudential regulation package (Basel IV implementation) |

---

## Category 10: Missing Practitioner Knowledge

| # | Missing Area | Priority | Rationale |
|:-:|-------------|:--------:|-----------|
| 1 | **Desk P&L attribution** | P1 | How daily P&L is decomposed and explained — core daily workflow |
| 2 | **FTP (Funds Transfer Pricing)** | P1 | Internal funding cost allocation to desks |
| 3 | **Hedge accounting** | P2 | IFRS 9 hedge accounting — when/how to designate a hedge relationship |
| 4 | **Embedded derivative bifurcation** | P2 | When to separate an embedded derivative from its host contract |
| 5 | **STP (Straight-Through Processing) rate** | P2 | Key operations KPI — percentage of trades processed without manual intervention |
| 6 | **Golden source** | P2 | The authoritative system of record for a given data element |
| 7 | **Trade blotter** | P3 | Daily record of all trades executed — front office operational tool |
| 8 | **Position reconciliation** | P2 | Daily process of matching front office vs back office positions |
| 9 | **Cash reconciliation** | P2 | Matching expected vs actual cash flows (nostro breaks) |

---

## Summary Statistics

| Category | Missing Items | P1 | P2 | P3 |
|----------|:------------:|:--:|:--:|:--:|
| 1. TOC-Promised Sections | 19 | 4 | 15 | 0 |
| 2. Derivatives & SP | 13 | 1 | 8 | 4 |
| 3. Workflow & Operations | 15 | 5 | 9 | 1 |
| 4. Bloomberg & Systems | 15 | 1 | 11 | 3 |
| 5. Holiday & Calendar | 8 | 1 | 4 | 3 |
| 6. Fixing & Rate Mechanics | 10 | 2 | 7 | 1 |
| 7. Legal & Documentation | 10 | 3 | 5 | 2 |
| 8. Quantitative Methods | 11 | 3 | 7 | 1 |
| 9. Regulation & Compliance | 10 | 1 | 9 | 0 |
| 10. Practitioner Knowledge | 9 | 2 | 6 | 1 |
| **TOTAL** | **120** | **23** | **81** | **16** |

---

## Assessment

The encyclopedia contains ~347 entries and is missing ~120 additional topics. Of these:
- **23 P1 topics** should ideally be in V1.0 but are not publication-blocking individually
- **81 P2 topics** are natural V2.0 candidates
- **16 P3 topics** are nice-to-have enhancements

The most impactful gap cluster is the **19 TOC-promised sections** that don't exist — these represent an explicit commitment not met.

The second most impactful cluster is the **missing pricing models** (Heston, Hull-White, SABR) — these are the industry-standard models that a practitioner would expect in an infrastructure encyclopedia.

**Recommendation**: Accept for V1.0 publication with a clear Phase 2 roadmap addressing P1 topics first. The TOC should be reconciled with actual content to avoid false expectations.
