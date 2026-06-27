# Infrastructure Encyclopedia V1.0 — Domain Coverage Matrix

**Date**: 2026-06-26
**Reviewer**: Independent Publication Board — Domain Coverage Specialist
**Manuscript**: `production/infrastructure_encyclopedia_v1.md` (4,438 lines, ~347 entries)

---

## Methodology

Each knowledge domain assessed on four dimensions:
- **Coverage %**: Proportion of essential concepts addressed (0-100%)
- **Depth**: Quality of treatment (Shallow / Adequate / Deep / Comprehensive)
- **Quality**: Accuracy and clarity (Low / Medium / High / Exceptional)
- **Missing Concepts**: Specific terms/topics absent from the encyclopedia

---

## Domain 1: Termsheet Fields & Product Parameters

| Sub-Domain | Coverage % | Depth | Quality | Missing Concepts |
|------------|:----------:|:-----:|:-------:|-----------------|
| Product Identifiers (ISIN, ticker, product type) | 85% | Deep | High | LEI for issuer, CFI code |
| Dates & Schedules (trade, settle, maturity, observation, fixing) | 95% | Comprehensive | Exceptional | IMM dates, futures roll dates |
| Day Count Conventions | 95% | Comprehensive | Exceptional | Bus/252 (Brazil), ISMA-Year |
| Business Day Conventions | 95% | Comprehensive | Exceptional | End-of-Month rule (in BDC context) |
| Frequency & Period Conventions | 90% | Deep | High | Long/short stub interaction with roll conventions |
| Notional Conventions | 90% | Deep | High | Step-up notional schedules (beyond amortising) |
| Coupon Structures | 95% | Comprehensive | Exceptional | Range accrual with digital features |
| Barrier Mechanics | 95% | Comprehensive | Exceptional | Barrier shift (quanto barriers), Parisian barriers |
| Strike Conventions | 90% | Deep | High | Forward-starting strike, variance strike |
| Autocall Mechanics | 95% | Comprehensive | Exceptional | Memory autocall with step-down schedule |
| Settlement | 90% | Deep | High | Partial settlement, settlement fails process |
| Calendar Conventions | 85% | Deep | High | Combined calendar resolution rules, TARGET2-Securities |
| Early Termination | 90% | Deep | High | Mandatory early termination (regulatory trigger) |
| Market Disruption | 90% | Deep | High | Emerging market disruption, inconvertibility |
| Participation | 90% | Deep | High | Leveraged participation with cap |
| Underlying Definitions | 85% | Adequate | High | Custom basket rebalancing rules, fund-linked underlyings |

**Domain Average**: 91% | Deep | High

---

## Domain 2: Credit Structure & Capital Stack

| Sub-Domain | Coverage % | Depth | Quality | Missing Concepts |
|------------|:----------:|:-----:|:-------:|-----------------|
| Seniority Hierarchy | 90% | Comprehensive | Exceptional | Pari passu, structural vs contractual subordination |
| AT1 / CoCo Mechanics | 95% | Comprehensive | Exceptional | Point of non-viability (PONV) trigger mechanics |
| Bail-in Framework | 90% | Deep | High | MREL, TLAC calculation methodology |
| Credit Events (CDS) | 85% | Deep | High | Succession events, Standard Reference Obligations |
| Recovery & LGD | 85% | Deep | High | Distressed debt exchange, recovery swaps |
| Tranche Mechanics | 85% | Deep | High | Correlation trading, base correlation interpolation |
| Credit Indices | 70% | Adequate | High | iTraxx/CDX roll mechanics, on-the-run vs off-the-run indices |
| CDS Mechanics | 75% | Adequate | High | CDS Big Bang Protocol, ISDA Determinations Committee process |

**Domain Average**: 84% | Deep | High

---

## Domain 3: Valuation Framework

| Sub-Domain | Coverage % | Depth | Quality | Missing Concepts |
|------------|:----------:|:-----:|:-------:|-----------------|
| Fair Value (IFRS 13 / ASC 820) | 90% | Deep | High | Observable vs unobservable inputs decision tree |
| Level 1/2/3 Hierarchy | 95% | Comprehensive | Exceptional | Level transfers disclosure requirements |
| IPV (Independent Price Verification) | 90% | Deep | High | IPV tolerance calibration, stale price detection |
| Mark-to-Market | 85% | Deep | High | Mark-to-model governance, model uncertainty reserves |
| Reserves & Adjustments | 60% | Adequate | Medium | Bid-offer reserves, model reserves, close-out cost reserves, liquidity reserves |
| Day One P&L | 55% | Adequate | Medium | Day One P&L reserve policy, release schedule, IFRS 9 Day One gain deferral |
| P&L Explain / Attribution | 30% | Shallow | Medium | Full P&L decomposition (delta, gamma, vega, theta, rho, carry, new deals, unexplained) |

**Domain Average**: 72% | Adequate | High

---

## Domain 4: XVA Framework

| Sub-Domain | Coverage % | Depth | Quality | Missing Concepts |
|------------|:----------:|:-----:|:-------:|-----------------|
| CVA (Credit Valuation Adjustment) | 95% | Comprehensive | Exceptional | WWR (wrong-way risk) modelling approaches, CVA VaR |
| DVA (Debit Valuation Adjustment) | 90% | Deep | High | Symmetric CVA/DVA accounting debate |
| FVA (Funding Valuation Adjustment) | 90% | Deep | High | FVA-DVA double counting resolution, desk-level FVA allocation |
| KVA (Capital Valuation Adjustment) | 85% | Deep | High | KVA under Basel IV changes, lifetime capital projection |
| ColVA (Collateral Valuation Adjustment) | 0% | None | N/A | Entire topic missing despite TOC listing. ColVA = cost of posting collateral at a rate different from the discount rate |
| MVA (Margin Valuation Adjustment) | 0% | None | N/A | Entire topic missing despite TOC listing. MVA = cost of funding initial margin requirements |
| LVA (Liquidity Valuation Adjustment) | 0% | None | N/A | Entire topic missing despite TOC listing. LVA = adjustment for liquidity costs |
| XVA Desk Operations | 40% | Shallow | Medium | XVA desk mandate, XVA hedging, centralised vs decentralised XVA |

**Domain Average**: 50% | Adequate (for covered topics) | High (for covered topics)

---

## Domain 5: Pricing Models

| Sub-Domain | Coverage % | Depth | Quality | Missing Concepts |
|------------|:----------:|:-----:|:-------:|-----------------|
| Black-Scholes-Merton | 95% | Comprehensive | Exceptional | Greeks derivation from BSM, BSM for dividend-paying stocks |
| Local Volatility (Dupire) | 90% | Deep | High | SLV (Stochastic Local Volatility) hybrid models |
| Monte Carlo Methods | 90% | Deep | High | Longstaff-Schwartz for American/Bermudan options, Quasi-MC |
| Stochastic Volatility (Heston) | 0% | None | N/A | Entire model missing despite TOC listing. Heston dynamics, calibration, characteristic function |
| Interest Rate Models (Hull-White) | 0% | None | N/A | Entire model missing despite TOC listing. HW tree construction, mean reversion, swaption calibration |
| SABR Model | 0% | None | N/A | Entire model missing despite TOC listing. SABR parameters (α, β, ρ, ν), Hagan formula |
| Finite Difference Methods | 0% | None | N/A | Entire model missing despite TOC listing. Explicit/implicit/Crank-Nicolson schemes |
| Tree Methods (Binomial/Trinomial) | 0% | None | N/A | Entire model missing despite TOC listing. CRR tree, convergence properties |
| Copula Models | 0% | None | N/A | Gaussian copula, Li (2000), base correlation framework |
| Model Governance | 30% | Shallow | Medium | Model validation, model risk management (SR 11-7), model inventory |

**Domain Average**: 31% | Adequate (for covered topics) | High (for covered topics)

---

## Domain 6: Systems & Operations

| Sub-Domain | Coverage % | Depth | Quality | Missing Concepts |
|------------|:----------:|:-----:|:-------:|-----------------|
| Murex | 85% | Deep | High | MxML, datamart configuration, deal capture workflow |
| Sophis | 85% | Deep | High | Sophis Value toolkit, portfolio simulation module |
| NEMO | 30% | Shallow | Medium | No dedicated entry. Referenced but not documented. NEMO booking fields, lifecycle management, product templates |
| SA-CCR | 90% | Deep | High | Add-on factor tables by asset class, margin set definitions |
| Bloomberg Terminal | 40% | Adequate | Medium | FLDS, ALLQ, OVME, SWPM, MARS, DES fields specific to structured products |
| Market Data Systems | 60% | Adequate | High | MDH (Market Data Hub), contributed vs composite pricing |
| Risk Systems | 50% | Adequate | Medium | Risk engine architecture, scenario generation, VaR back-testing |
| Middleware & Integration | 70% | Adequate | High | FpML, CDM (Common Domain Model) |
| Trade Lifecycle | 65% | Adequate | High | Novation, amendment, compression, partial termination, post-trade processing |

**Domain Average**: 64% | Adequate | High

---

## Domain 7: Regulation

| Sub-Domain | Coverage % | Depth | Quality | Missing Concepts |
|------------|:----------:|:-----:|:-------:|-----------------|
| Basel III/IV | 90% | Deep | High | Output floor, CRR III implementation timeline |
| FRTB | 90% | Deep | High | P&L attribution test (PLAT), risk factor eligibility test (RFET) |
| PRIIPs | 90% | Deep | High | Performance scenario methodology updates (2022 RTS) |
| EMIR | 85% | Deep | High | EMIR Refit (EMIR 3.0), active account requirement |
| MiFID II / MiFIR | 85% | Deep | High | Product intervention powers (ESMA Article 40) |
| Dodd-Frank | 80% | Deep | High | SEF requirements for structured products, Title II resolution |
| Volcker Rule | 80% | Adequate | High | Market-making exemption tests, compliance program |
| UMR / SIMM | 85% | Deep | High | AANA calculation, phase-in timeline completion |
| SFTR | 0% | None | N/A | Entire regulation missing |
| MAR | 0% | None | N/A | Entire regulation missing (only referenced in passing) |
| CSDR | 0% | None | N/A | Central Securities Depositories Regulation — settlement discipline |
| Benchmark Regulation (BMR) | 30% | Shallow | Medium | Critical/significant/non-significant benchmark classification, fallback provisions |

**Domain Average**: 60% | Adequate | High

---

## Domain 8: Practitioner Vocabulary

| Sub-Domain | Coverage % | Depth | Quality | Missing Concepts |
|------------|:----------:|:-----:|:-------:|-----------------|
| 8.1 Trading & Market-Making | 85% | Adequate | High | "Hung," "stuffed," "offside," "crossing," "lifting" |
| 8.2 Risk Management | 85% | Adequate | High | Tail risk, stress testing methodology, risk budget |
| 8.3 Documentation & Legal | 80% | Adequate | High | Negative pledge, cross-default, pari passu, material adverse change |
| 8.4 Operations | 80% | Adequate | High | SSI (Standard Settlement Instructions), nostro/vostro, SWIFT |
| 8.5 Accounting & Finance | 75% | Adequate | Medium | Hedge accounting (IFRS 9), hedge effectiveness testing |
| 8.6 Product & Structuring | 80% | Adequate | High | Wrapper, EMTN programme, offer document |
| 8.7 Credit & Fixed Income | 85% | Adequate | High | Fallen angel, rising star, crossover credit |
| 8.8 Quantitative Terms | 85% | Adequate | High | Martingale, Ito's lemma, measure change |
| 8.9 Systems & Technology | 75% | Adequate | High | STP rate, exception management, golden source |
| 8.10 Regulatory Terms | 80% | Adequate | High | LEI, UTI, UPI |
| 8.11 Miscellaneous | 80% | Adequate | High | "Color" (market intelligence), "follow" (derivative position from flow) |

**Domain Average**: 81% | Adequate | High

---

## Coverage Heat Map Summary

| Domain | Coverage % | Depth | Quality | Critical Gaps |
|--------|:----------:|:-----:|:-------:|:-------------:|
| 1. Termsheet Fields | 91% | Deep | High | 0 |
| 2. Credit Structure | 84% | Deep | High | 0 |
| 3. Valuation Framework | 72% | Adequate | High | 2 (Reserves, P&L Explain) |
| 4. XVA Framework | 50% | Mixed | High | 3 (ColVA, MVA, LVA) |
| 5. Pricing Models | 31% | Mixed | High | 6 (Heston, HW, SABR, FD, Trees, Copula) |
| 6. Systems & Operations | 64% | Adequate | High | 2 (NEMO, Bloomberg) |
| 7. Regulation | 60% | Adequate | High | 3 (SFTR, MAR, CSDR) |
| 8. Practitioner Vocab | 81% | Adequate | High | 0 |

**Overall Weighted Coverage: 67%**

---

## Assessment

The encyclopedia achieves excellent coverage (90%+) in its core domain — termsheet fields and product parameters (Domain 1). Credit structure and practitioner vocabulary are also well-covered (80%+). The quality of what IS written is consistently high to exceptional.

The primary gaps are:
1. **Pricing Models (31%)**: Only 3 of ~10 expected models covered. The TOC promises 6 additional models that don't exist.
2. **XVA Framework (50%)**: 3 of 7 XVA types entirely missing despite TOC listing.
3. **Regulation (60%)**: 3 regulations entirely absent; others have depth gaps.
4. **Systems (64%)**: NEMO — one of the three core ecosystem systems — lacks a dedicated entry.

These gaps are notable but not publication-blocking for a V1.0. The TOC-body mismatch is the most actionable finding — it creates false expectations.

---

**Recommendation**: Publish V1.0 as-is with TOC revised to mark undelivered sections as "Phase 2." Alternatively, retain the aspirational TOC with a clear "Sections marked [P2] are planned for V2.0" notation.
