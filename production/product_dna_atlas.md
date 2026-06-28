# Product DNA Atlas

**Desk Bible v2 — Canonical Reference Layer**

**Products:** 49  
**Families:** 6  
**Framework:** v1.3.1 (frozen)  
**Generated:** 2026-06-22

---

## Table of Contents

1. [Start Here — First Products To Learn](#start-here-first-products-to-learn)
2. [Family View](#family-view)
3. [Complexity View](#complexity-view)
4. [Alphabetical View](#alphabetical-view)
5. [Product DNA Cards](#product-dna-cards)
6. [Appendix A: Family Summary](#appendix-a-family-summary)
7. [Appendix B: Complexity Distribution](#appendix-b-complexity-distribution)
8. [Appendix C: Product Evolution Summary](#appendix-c-product-evolution-summary)
9. [Appendix D: Top Desk Risk Metrics](#appendix-d-top-desk-risk-metrics)
10. [Appendix E: Common Interview Questions](#appendix-e-common-interview-questions)
11. [Appendix F: Product Confusion Pairs](#appendix-f-product-confusion-pairs)
12. [Appendix G: What Makes This Product Difficult?](#appendix-g-what-makes-this-product-difficult)

---

## Start Here — First Products To Learn

New to the desk? Start with these 7 products. Each is the simplest member of its family and unlocks the more complex products that build on it.

| # | Product | Section | Score | Family It Unlocks | Why Learn First |
|:-:|---------|---------|:-----:|-------------------|-----------------|
| 1 | **Structured Deposit** | 5.6.1 | 2/10 | Other | Simplest product in the universe. Deposit + call option. Full capital protection. If you understand this, you understand how banks embed options into savings products. |
| 2 | **Forward Contract** | 5.6.2 | 2/10 | Other | Foundation of all derivatives. Linear payoff, no optionality. Every swap and structured note builds on forward economics. |
| 3 | **Principal Protected Note** | 5.1.1 | 2/10 | Equity-Linked Notes | Zero-coupon bond + call option = capital protection + upside. The DNA of most capital-protected notes. Learn this, then add features to get RC, Phoenix, etc. |
| 4 | **Interest Rate Swap** | 5.2.1 | 3/10 | Swaps | Most traded OTC derivative globally. Fixed-for-floating exchange. Every structured rate product is an IRS with embedded options. |
| 5 | **Reverse Convertible** | 5.1.2 | 3/10 | Equity-Linked Notes | The yield-enhancement archetype. Bond + short put = above-market coupon. RC mechanics appear in Phoenix, FCN, DRC, Airbag, Bonus, and CRC. |
| 6 | **Vanilla Credit-Linked Note** | 5.5.1 | 4/10 | Credit-Linked Notes | Note + embedded CDS. Gateway to all credit-linked products (Skew CLN, FTD, NTD, CDO). |
| 7 | **Vanilla Steepener Note** | 5.4.1 | 5/10 | Steepener Notes | Leveraged CMS spread coupon. Building block for RA STEG, Callable STEG, and TARN STEG. |

**Learning path:** Products 1-3 in week 1. Products 4-5 in week 2. Products 6-7 in week 3. Then explore each family by ascending complexity score.

---

## Family View

### Equity-Linked Notes (ELN) — 15 products

| Section | Product | Abbrev | Complexity | Capital Protection |
|---------|---------|:------:|:----------:|-------------------|
| 5.1.1 | Principal Protected Note | PPN | 2 / 10 | 100% at maturity |
| 5.1.2 | Reverse Convertible | RC | 3 / 10 | Conditional (protected above put strike) |
| 5.1.3 | Phoenix Autocallable | Phoenix | 6 / 10 | Conditional (protected above barrier) |
| 5.1.4 | Discounted Reverse Convertible | DRC | 3 / 10 | Conditional (protected above adjusted strike) |
| 5.1.5 | Knock-Out Discounted Reverse Convertible | KODRC | 4 / 10 | Enhanced conditional protection (barrier must be breached) |
| 5.1.6 | Callable Reverse Convertible | CRC | 5 / 10 | Conditional (same as RC) |
| 5.1.7 | Airbag Note | Airbag | 4 / 10 | Partial (airbag absorbs losses between strike and barrier) |
| 5.1.8 | Bonus Note | Bonus | 4 / 10 | Conditional (bonus forfeited if barrier breached, but principal returned at maturity) |
| 5.1.9 | Fixed Coupon Note | FCN | 6 / 10 | Conditional (protected above barrier at maturity) |
| 5.1.10 | Callable Range Accrual ELN | CRA ELN | 6 / 10 | 100% at maturity |
| 5.1.11 | Issuer Callable Note | ICN | 3 / 10 | Conditional (depends on variant) |
| 5.1.12 | Digital Coupon Note | Digital | 4 / 10 | 100% at maturity |
| 5.1.13 | Booster Note | Booster | 4 / 10 | None (full equity downside below strike) |
| 5.1.14 | Digital Coupon Knock-In Put | DKIP | 7 / 10 | Conditional (barrier-protected principal) |
| 5.1.15 | Warrant / Turbo Certificate | Warrant | 3 / 10 | None (option can expire worthless — lose entire premium) |

### Swaps (Swaps) — 8 products

| Section | Product | Abbrev | Complexity | Capital Protection |
|---------|---------|:------:|:----------:|-------------------|
| 5.2.1 | Interest Rate Swap | IRS | 3 / 10 | N/A (swap — no principal exchanged) |
| 5.2.2 | Total Return Swap | TRS | 5 / 10 | N/A (swap — unfunded or partially funded) |
| 5.2.3 | Equity Swap | EqSwap | 5 / 10 | N/A (swap) |
| 5.2.4 | Variance Swap | VarSwap | 7 / 10 | N/A (swap — can have large negative MTM) |
| 5.2.5 | Credit Default Swap | CDS | 5 / 10 | N/A (swap — notional at risk for protection seller) |
| 5.2.6 | Cross-Currency Swap | XCCY | 5 / 10 | N/A (swap — principals exchanged) |
| 5.2.7 | Commodity Swap | CommSwap | 4 / 10 | N/A (swap) |
| 5.2.8 | Vanilla Swap Plus | VLSP | 2 / 10 | N/A (swap) |

### Structured Rate Trades (SRT) — 5 products

| Section | Product | Abbrev | Complexity | Capital Protection |
|---------|---------|:------:|:----------:|-------------------|
| 5.3.1 | IR Callable Fixed Rate Swap | IR Callable | 5 / 10 | None (swap — notional not at risk but MTM can be negative) |
| 5.3.2 | Zero-Coupon Linked Note | ZCL | 4 / 10 | 100% at maturity (ZCB structure) |
| 5.3.3 | Non-Callable Range Accrual | NCRA | 6 / 10 | 100% at maturity (principal returned regardless of coupon) |
| 5.3.4 | Callable Range Accrual SRT | CRA SRT | 7 / 10 | 100% at maturity |
| 5.3.5 | Digital Cap-Floor Note | Digital CF | 5 / 10 | 100% at maturity |

### Steepener Notes (STEG) — 4 products

| Section | Product | Abbrev | Complexity | Capital Protection |
|---------|---------|:------:|:----------:|-------------------|
| 5.4.1 | Vanilla Steepener Note | Vanilla STEG | 5 / 10 | 100% at maturity |
| 5.4.2 | Range Accrual Steepener | RA STEG | 7 / 10 | 100% at maturity |
| 5.4.3 | Callable Steepener | Callable STEG | 6 / 10 | 100% at maturity (or on call date) |
| 5.4.4 | TARN Steepener | TARN STEG | 8 / 10 | 100% at maturity or target date |

### Credit-Linked Notes (CLN) — 5 products

| Section | Product | Abbrev | Complexity | Capital Protection |
|---------|---------|:------:|:----------:|-------------------|
| 5.5.1 | Vanilla Credit-Linked Note | CLN | 4 / 10 | Conditional (principal at risk on credit event) |
| 5.5.2 | Skew Credit-Linked Note | Skew CLN | 5 / 10 | Conditional (protected if no credit event) |
| 5.5.3 | First-to-Default Note | FTD | 7 / 10 | Conditional (protected if no credit event in basket) |
| 5.5.4 | Nth-to-Default Note | NTD | 8 / 10 | Conditional (protected if fewer than N defaults) |
| 5.5.5 | Synthetic CDO Tranche | CDO | 10 / 10 | Tranche-dependent (senior protected by subordination, equity tranche = first loss) |

### Other (Other) — 12 products

| Section | Product | Abbrev | Complexity | Capital Protection |
|---------|---------|:------:|:----------:|-------------------|
| 5.6.1 | Structured Deposit | SD | 2 / 10 | Full (100%). Deposit insurance where available + bank guarantee |
| 5.6.2 | Forward Contract | FWD | 2 / 10 | None — linear exposure in both directions |
| 5.6.3 | Vanilla Option (Call / Put) | VO | 3 / 10 | Long option: max loss = premium. Short option: unlimited potential loss |
| 5.6.4 | Equity-Linked Option | ELO | 3 / 10 | None — max loss is premium paid |
| 5.6.5 | Option on Reverse Convertible | Opt-on-RC | 5 / 10 | During option period: max loss = premium. After exercise (in RC): barrier-dependent protection |
| 5.6.6 | Accumulator | ACCUM | 6 / 10 | None — unlimited downside with gearing |
| 5.6.7 | Decumulator | DECUM | 6 / 10 | None — opportunity cost if stock rises significantly with gearing |
| 5.6.8 | Dual Currency Investment | DCI | 3 / 10 | Full in base currency if FX stays above strike. Nominal in alternate currency if converted |
| 5.6.9 | Shark Fin Note (Knock-Out Capital Protected Note) | SHRK | 4 / 10 | 100% at maturity (principal guaranteed) |
| 5.6.10 | Snowball Autocallable Note | SNOW | 7 / 10 | Conditional — protected if no knock-in barrier breach. At risk if barrier breached and underlying below strike at maturity |
| 5.6.11 | Cliquet Note (Ratchet Note) | CLIQ | 7 / 10 | Typically 100% (funded by zero-coupon bond) |
| 5.6.12 | Worst-of Autocallable Note (Worst-of Phoenix) | WOAC | 8 / 10 | Conditional — protected if worst-of stock stays above knock-in barrier |

---

## Complexity View

### Vanilla (1–2) — 4 products

| Score | Section | Product | Family | Asset Class |
|:-----:|---------|---------|--------|-------------|
| 2 / 10 | 5.1.1 | Principal Protected Note (PPN) | ELN | Equity (index-linked) |
| 2 / 10 | 5.2.8 | Vanilla Swap Plus (VLSP) | Swaps | Rates |
| 2 / 10 | 5.6.1 | Structured Deposit (SD) | Other | Equity index, single stock, FX, commodity (most commonly equity index) |
| 2 / 10 | 5.6.2 | Forward Contract (FWD) | Other | Any: equity, FX, commodity, interest rate, credit |

### Standard (3–4) — 17 products

| Score | Section | Product | Family | Asset Class |
|:-----:|---------|---------|--------|-------------|
| 3 / 10 | 5.1.2 | Reverse Convertible (RC) | ELN | Equity (single stock or index) |
| 3 / 10 | 5.1.4 | Discounted Reverse Convertible (DRC) | ELN | Equity (single stock or index) |
| 3 / 10 | 5.1.11 | Issuer Callable Note (ICN) | ELN | Equity (single stock or index) |
| 3 / 10 | 5.1.15 | Warrant / Turbo Certificate (Warrant) | ELN | Equity (stock, index, commodity, FX) |
| 3 / 10 | 5.2.1 | Interest Rate Swap (IRS) | Swaps | Rates |
| 3 / 10 | 5.6.3 | Vanilla Option (Call / Put) (VO) | Other | Any: equity, FX, commodity, interest rate |
| 3 / 10 | 5.6.4 | Equity-Linked Option (ELO) | Other | Single equity (most common), equity index, basket |
| 3 / 10 | 5.6.8 | Dual Currency Investment (DCI) | Other | Foreign Exchange (currency pair) |
| 4 / 10 | 5.1.5 | Knock-Out Discounted Reverse Convertible (KODRC) | ELN | Equity (single stock) |
| 4 / 10 | 5.1.7 | Airbag Note (Airbag) | ELN | Equity (single stock or index) |
| 4 / 10 | 5.1.8 | Bonus Note (Bonus) | ELN | Equity (index or stock) |
| 4 / 10 | 5.1.12 | Digital Coupon Note (Digital) | ELN | Equity (single stock or index) |
| 4 / 10 | 5.1.13 | Booster Note (Booster) | ELN | Equity (index) |
| 4 / 10 | 5.2.7 | Commodity Swap (CommSwap) | Swaps | Commodities |
| 4 / 10 | 5.3.2 | Zero-Coupon Linked Note (ZCL) | SRT | Rates (SOFR / EURIBOR) |
| 4 / 10 | 5.5.1 | Vanilla Credit-Linked Note (CLN) | CLN | Credit |
| 4 / 10 | 5.6.9 | Shark Fin Note (Knock-Out Capital Protected Note) (SHRK) | Other | Equity index (most common), single stock, commodity |

### Moderate (5–6) — 17 products

| Score | Section | Product | Family | Asset Class |
|:-----:|---------|---------|--------|-------------|
| 5 / 10 | 5.1.6 | Callable Reverse Convertible (CRC) | ELN | Equity (single stock or index) |
| 5 / 10 | 5.2.2 | Total Return Swap (TRS) | Swaps | Multi-asset (equity, credit, loans) |
| 5 / 10 | 5.2.3 | Equity Swap (EqSwap) | Swaps | Equity |
| 5 / 10 | 5.2.5 | Credit Default Swap (CDS) | Swaps | Credit |
| 5 / 10 | 5.2.6 | Cross-Currency Swap (XCCY) | Swaps | FX + Rates |
| 5 / 10 | 5.3.1 | IR Callable Fixed Rate Swap (IR Callable) | SRT | Rates (SOFR / EURIBOR) |
| 5 / 10 | 5.3.5 | Digital Cap-Floor Note (Digital CF) | SRT | Rates (3-month SOFR, quarterly observation) |
| 5 / 10 | 5.4.1 | Vanilla Steepener Note (Vanilla STEG) | STEG | Rates (CMS30Y − CMS2Y swap curve slope) |
| 5 / 10 | 5.5.2 | Skew Credit-Linked Note (Skew CLN) | CLN | Credit (single reference entity) |
| 5 / 10 | 5.6.5 | Option on Reverse Convertible (Opt-on-RC) | Other | Single equity or equity index (the RC's underlying) |
| 6 / 10 | 5.1.3 | Phoenix Autocallable (Phoenix) | ELN | Equity (single stock or basket) |
| 6 / 10 | 5.1.9 | Fixed Coupon Note (FCN) | ELN | Equity (single stock or basket) |
| 6 / 10 | 5.1.10 | Callable Range Accrual ELN (CRA ELN) | ELN | Equity (index) |
| 6 / 10 | 5.3.3 | Non-Callable Range Accrual (NCRA) | SRT | Rates (6-month SOFR, daily observation) |
| 6 / 10 | 5.4.3 | Callable Steepener (Callable STEG) | STEG | Rates (CMS30Y − CMS2Y spread) |
| 6 / 10 | 5.6.6 | Accumulator (ACCUM) | Other | Single equity (most common), equity index, FX |
| 6 / 10 | 5.6.7 | Decumulator (DECUM) | Other | Single equity (most common), equity index, FX |

### Complex (7–8) — 10 products

| Score | Section | Product | Family | Asset Class |
|:-----:|---------|---------|--------|-------------|
| 7 / 10 | 5.1.14 | Digital Coupon Knock-In Put (DKIP) | ELN | Equity (single stock) |
| 7 / 10 | 5.2.4 | Variance Swap (VarSwap) | Swaps | Equity (volatility) |
| 7 / 10 | 5.3.4 | Callable Range Accrual SRT (CRA SRT) | SRT | Rates (6-month SOFR, daily observation) |
| 7 / 10 | 5.4.2 | Range Accrual Steepener (RA STEG) | STEG | Rates (CMS30Y − CMS2Y spread, daily observation) |
| 7 / 10 | 5.5.3 | First-to-Default Note (FTD) | CLN | Credit (basket of 5–10 reference entities) |
| 7 / 10 | 5.6.10 | Snowball Autocallable Note (SNOW) | Other | Equity index (CSI 300, KOSPI most common), single stock |
| 7 / 10 | 5.6.11 | Cliquet Note (Ratchet Note) (CLIQ) | Other | Equity index (most common), single stock |
| 8 / 10 | 5.4.4 | TARN Steepener (TARN STEG) | STEG | Rates (CMS30Y − CMS2Y spread) |
| 8 / 10 | 5.5.4 | Nth-to-Default Note (NTD) | CLN | Credit (basket of 5–10 reference entities) |
| 8 / 10 | 5.6.12 | Worst-of Autocallable Note (Worst-of Phoenix) (WOAC) | Other | Basket of 3-5 equities (single stocks, occasionally indices) |

### Highly Complex (9–10) — 1 products

| Score | Section | Product | Family | Asset Class |
|:-----:|---------|---------|--------|-------------|
| 10 / 10 | 5.5.5 | Synthetic CDO Tranche (CDO) | CLN | Credit (portfolio of 100+ reference entities via CDS) |

---

## Alphabetical View

| # | Product | Abbrev | Section | Family | Complexity |
|:-:|---------|:------:|---------|--------|:----------:|
| 1 | Accumulator | ACCUM | 5.6.6 | Other | 6 / 10 |
| 2 | Airbag Note | Airbag | 5.1.7 | ELN | 4 / 10 |
| 3 | Bonus Note | Bonus | 5.1.8 | ELN | 4 / 10 |
| 4 | Booster Note | Booster | 5.1.13 | ELN | 4 / 10 |
| 5 | Callable Range Accrual ELN | CRA ELN | 5.1.10 | ELN | 6 / 10 |
| 6 | Callable Range Accrual SRT | CRA SRT | 5.3.4 | SRT | 7 / 10 |
| 7 | Callable Reverse Convertible | CRC | 5.1.6 | ELN | 5 / 10 |
| 8 | Callable Steepener | Callable STEG | 5.4.3 | STEG | 6 / 10 |
| 9 | Cliquet Note (Ratchet Note) | CLIQ | 5.6.11 | Other | 7 / 10 |
| 10 | Commodity Swap | CommSwap | 5.2.7 | Swaps | 4 / 10 |
| 11 | Credit Default Swap | CDS | 5.2.5 | Swaps | 5 / 10 |
| 12 | Cross-Currency Swap | XCCY | 5.2.6 | Swaps | 5 / 10 |
| 13 | Decumulator | DECUM | 5.6.7 | Other | 6 / 10 |
| 14 | Digital Cap-Floor Note | Digital CF | 5.3.5 | SRT | 5 / 10 |
| 15 | Digital Coupon Knock-In Put | DKIP | 5.1.14 | ELN | 7 / 10 |
| 16 | Digital Coupon Note | Digital | 5.1.12 | ELN | 4 / 10 |
| 17 | Discounted Reverse Convertible | DRC | 5.1.4 | ELN | 3 / 10 |
| 18 | Dual Currency Investment | DCI | 5.6.8 | Other | 3 / 10 |
| 19 | Equity Swap | EqSwap | 5.2.3 | Swaps | 5 / 10 |
| 20 | Equity-Linked Option | ELO | 5.6.4 | Other | 3 / 10 |
| 21 | First-to-Default Note | FTD | 5.5.3 | CLN | 7 / 10 |
| 22 | Fixed Coupon Note | FCN | 5.1.9 | ELN | 6 / 10 |
| 23 | Forward Contract | FWD | 5.6.2 | Other | 2 / 10 |
| 24 | Interest Rate Swap | IRS | 5.2.1 | Swaps | 3 / 10 |
| 25 | IR Callable Fixed Rate Swap | IR Callable | 5.3.1 | SRT | 5 / 10 |
| 26 | Issuer Callable Note | ICN | 5.1.11 | ELN | 3 / 10 |
| 27 | Knock-Out Discounted Reverse Convertible | KODRC | 5.1.5 | ELN | 4 / 10 |
| 28 | Non-Callable Range Accrual | NCRA | 5.3.3 | SRT | 6 / 10 |
| 29 | Nth-to-Default Note | NTD | 5.5.4 | CLN | 8 / 10 |
| 30 | Option on Reverse Convertible | Opt-on-RC | 5.6.5 | Other | 5 / 10 |
| 31 | Phoenix Autocallable | Phoenix | 5.1.3 | ELN | 6 / 10 |
| 32 | Principal Protected Note | PPN | 5.1.1 | ELN | 2 / 10 |
| 33 | Range Accrual Steepener | RA STEG | 5.4.2 | STEG | 7 / 10 |
| 34 | Reverse Convertible | RC | 5.1.2 | ELN | 3 / 10 |
| 35 | Shark Fin Note (Knock-Out Capital Protected Note) | SHRK | 5.6.9 | Other | 4 / 10 |
| 36 | Skew Credit-Linked Note | Skew CLN | 5.5.2 | CLN | 5 / 10 |
| 37 | Snowball Autocallable Note | SNOW | 5.6.10 | Other | 7 / 10 |
| 38 | Structured Deposit | SD | 5.6.1 | Other | 2 / 10 |
| 39 | Synthetic CDO Tranche | CDO | 5.5.5 | CLN | 10 / 10 |
| 40 | TARN Steepener | TARN STEG | 5.4.4 | STEG | 8 / 10 |
| 41 | Total Return Swap | TRS | 5.2.2 | Swaps | 5 / 10 |
| 42 | Vanilla Credit-Linked Note | CLN | 5.5.1 | CLN | 4 / 10 |
| 43 | Vanilla Option (Call / Put) | VO | 5.6.3 | Other | 3 / 10 |
| 44 | Vanilla Steepener Note | Vanilla STEG | 5.4.1 | STEG | 5 / 10 |
| 45 | Vanilla Swap Plus | VLSP | 5.2.8 | Swaps | 2 / 10 |
| 46 | Variance Swap | VarSwap | 5.2.4 | Swaps | 7 / 10 |
| 47 | Warrant / Turbo Certificate | Warrant | 5.1.15 | ELN | 3 / 10 |
| 48 | Worst-of Autocallable Note (Worst-of Phoenix) | WOAC | 5.6.12 | Other | 8 / 10 |
| 49 | Zero-Coupon Linked Note | ZCL | 5.3.2 | SRT | 4 / 10 |

---

## Product DNA Cards

49 standardized cards. One per product. Ordered by section number.

### 5.1.1 — Principal Protected Note (PPN)

| Field | Value |
|-------|-------|
| **Product Name** | Principal Protected Note |
| **Abbreviation** | PPN |
| **Family** | Equity-Linked Notes |
| **Complexity Score** | 2 / 10 |
| **Complexity Rationale** | Two components (ZCB + call option), no barriers, no path dependency, single underlying |
| **Underlying Asset Class** | Equity (index-linked) |
| **Capital Protection** | 100% at maturity |
| **Coupon Type** | None — return via equity participation |
| **Maturity Profile** | 3-5 years |
| **Liquidity Profile** | Secondary market (bid-offer spread widens in stress) |
| **Primary Buyer** | Risk-averse retail and institutional investors: pension funds, retirees, foundations with capital preservation mandates |
| **Primary Risk** | Opportunity cost (capped upside via participation rate). Interest rate risk affects ZCB value. Issuer credit risk |
| **Primary Hedge** | Long ZCB (matched maturity) + long call option (delta-hedged) |
| **Primary System** | Murex |
| **ISDA Required** | No — issued as note |
| **One-Line Summary** | Capital-guaranteed equity exposure |

**Remember These 3 Things:**

1. Zero-coupon bond (principal protection) + European call option (equity upside)
2. Key risk: Opportunity cost (capped upside via participation rate)
3. Watch: Rho (interest rate sensitivity drives ZCB value and participation rate)

---

### 5.1.2 — Reverse Convertible (RC)

| Field | Value |
|-------|-------|
| **Product Name** | Reverse Convertible |
| **Abbreviation** | RC |
| **Family** | Equity-Linked Notes |
| **Complexity Score** | 3 / 10 |
| **Complexity Rationale** | Enhanced yield note with embedded short put. Single barrier, single underlying, conditional principal return |
| **Underlying Asset Class** | Equity (single stock or index) |
| **Capital Protection** | Conditional (protected above put strike) |
| **Coupon Type** | Fixed coupon (above-market) |
| **Maturity Profile** | 6-18 months typically |
| **Liquidity Profile** | Secondary market |
| **Primary Buyer** | Yield-seeking investors with moderate bullish view on underlying. Private banking clients, high-net-worth individuals |
| **Primary Risk** | Underlying falling below put strike — investor receives depreciated shares instead of cash. Full equity downside below strike |
| **Primary Hedge** | Long put option (delta-hedged), fixed-rate bond hedge |
| **Primary System** | Murex |
| **ISDA Required** | No — issued as note |
| **One-Line Summary** | Yield enhancement when investor is willing to buy underlying at a discount (put strike) if market falls |

**Remember These 3 Things:**

1. Fixed-rate note (coupon payments) + short put option (sold by investor to bank)
2. Key risk: Underlying falling below put strike — investor receives depreciated shares instead of cash
3. Watch: Put delta near strike (conversion probability)

---

### 5.1.3 — Phoenix Autocallable (Phoenix)

| Field | Value |
|-------|-------|
| **Product Name** | Phoenix Autocallable |
| **Abbreviation** | Phoenix |
| **Family** | Equity-Linked Notes |
| **Complexity Score** | 6 / 10 |
| **Complexity Rationale** | Autocallable with memory coupon feature, barrier observation, early termination |
| **Underlying Asset Class** | Equity (single stock or basket) |
| **Capital Protection** | Conditional (protected above barrier) |
| **Coupon Type** | Contingent coupon with memory feature |
| **Maturity Profile** | 1-5 years |
| **Liquidity Profile** | Secondary market (autocall shortens expected life) |
| **Primary Buyer** | Yield-seeking investors comfortable with conditional downside. Private banking, wealth management |
| **Primary Risk** | Barrier breach causing principal loss. Autocall in favourable scenario limits upside. Memory coupon complexity |
| **Primary Hedge** | Long DI put, delta-hedge equity, short autocall replication |
| **Primary System** | Murex |
| **ISDA Required** | No — issued as note |
| **One-Line Summary** | Earn conditional coupons with memory feature and automatic early redemption if underlying recovers |

**Remember These 3 Things:**

1. Fixed-rate note (funding) + short down-and-in put (downside risk) + binary coupon options (coupon engine) + autocall triggers (early redemption)
2. Key risk: Barrier breach causing principal loss
3. Watch: Autocall probability (early termination likelihood at each observation date)

---

### 5.1.4 — Discounted Reverse Convertible (DRC)

| Field | Value |
|-------|-------|
| **Product Name** | Discounted Reverse Convertible |
| **Abbreviation** | DRC |
| **Family** | Equity-Linked Notes |
| **Complexity Score** | 3 / 10 |
| **Complexity Rationale** | RC variant issued at discount. Lower entry price reduces break-even. Same put exposure |
| **Underlying Asset Class** | Equity (single stock or index) |
| **Capital Protection** | Conditional (protected above adjusted strike) |
| **Coupon Type** | None or reduced coupon — return via discount |
| **Maturity Profile** | 6-18 months |
| **Liquidity Profile** | Secondary market |
| **Primary Buyer** | Yield-seeking investors wanting lower break-even entry. Private banking clients |
| **Primary Risk** | Underlying falling below adjusted strike. Similar to RC but break-even is lower due to discount |
| **Primary Hedge** | Long put option (delta-hedged), discount bond hedge |
| **Primary System** | Murex |
| **ISDA Required** | No — issued as note |
| **One-Line Summary** | Lower effective entry point than RC |

**Remember These 3 Things:**

1. Discounted note (issued below par) + short put option
2. Key risk: Underlying falling below adjusted strike
3. Watch: Break-even distance (spot vs adjusted strike)

---

### 5.1.5 — Knock-Out Discounted Reverse Convertible (KODRC)

| Field | Value |
|-------|-------|
| **Product Name** | Knock-Out Discounted Reverse Convertible |
| **Abbreviation** | KODRC |
| **Family** | Equity-Linked Notes |
| **Complexity Score** | 4 / 10 |
| **Complexity Rationale** | DRC with knock-out barrier. If underlying stays above barrier, put expires worthless. Barrier adds complexity |
| **Underlying Asset Class** | Equity (single stock) |
| **Capital Protection** | Enhanced conditional protection (barrier must be breached) |
| **Coupon Type** | None or reduced — return via discount |
| **Maturity Profile** | 6-18 months |
| **Liquidity Profile** | Secondary market |
| **Primary Buyer** | Investors wanting buffer protection with barrier. Private banking, sophisticated retail |
| **Primary Risk** | Barrier breach converting protected position to exposed. Sudden jump from full protection to full equity downside at barrier |
| **Primary Hedge** | Long DI put, delta-hedge near barrier, barrier replication |
| **Primary System** | Murex |
| **ISDA Required** | No — issued as note |
| **One-Line Summary** | Higher protection than DRC via barrier |

**Remember These 3 Things:**

1. Discounted note + short down-and-in put option
2. Key risk: Barrier breach converting protected position to exposed
3. Watch: Gamma

---

### 5.1.6 — Callable Reverse Convertible (CRC)

| Field | Value |
|-------|-------|
| **Product Name** | Callable Reverse Convertible |
| **Abbreviation** | CRC |
| **Family** | Equity-Linked Notes |
| **Complexity Score** | 5 / 10 |
| **Complexity Rationale** | RC with bank call right. Bank can terminate early in favourable scenarios. Extra coupon for call optionality |
| **Underlying Asset Class** | Equity (single stock or index) |
| **Capital Protection** | Conditional (same as RC) |
| **Coupon Type** | Enhanced fixed coupon (higher than RC due to call optionality sold) |
| **Maturity Profile** | 1-3 years |
| **Liquidity Profile** | Secondary market |
| **Primary Buyer** | Yield-maximising investors willing to accept call risk. Private banking |
| **Primary Risk** | Same downside as RC plus reinvestment risk if called early. Bank calls when position profitable for investor |
| **Primary Hedge** | Long put + long Bermudan call, delta-hedge |
| **Primary System** | Murex |
| **ISDA Required** | No — issued as note |
| **One-Line Summary** | Higher coupon than standard RC by selling bank call right |

**Remember These 3 Things:**

1. Fixed-rate note + short put + short Bermudan call (both sold by investor)
2. Key risk: Same downside as RC plus reinvestment risk if called early
3. Watch: Vega

---

### 5.1.7 — Airbag Note (Airbag)

| Field | Value |
|-------|-------|
| **Product Name** | Airbag Note |
| **Abbreviation** | Airbag |
| **Family** | Equity-Linked Notes |
| **Complexity Score** | 4 / 10 |
| **Complexity Rationale** | Leveraged RC with airbag protection zone between strike and barrier. Amplified upside participation above strike |
| **Underlying Asset Class** | Equity (single stock or index) |
| **Capital Protection** | Partial (airbag absorbs losses between strike and barrier) |
| **Coupon Type** | None — return via leveraged participation |
| **Maturity Profile** | 2-5 years |
| **Liquidity Profile** | Secondary market |
| **Primary Buyer** | Investors seeking leveraged upside with partial downside buffer. Institutional, private banking |
| **Primary Risk** | Full loss below airbag barrier. In airbag zone, losses are cushioned. Above strike, leveraged participation |
| **Primary Hedge** | Delta-hedge leveraged call, put spread replication |
| **Primary System** | Murex |
| **ISDA Required** | No — issued as note |
| **One-Line Summary** | Amplify equity gains with a cushion zone that absorbs moderate losses below strike |

**Remember These 3 Things:**

1. Leveraged call + short put spread (strike to barrier) + long digital at barrier
2. Key risk: Full loss below airbag barrier
3. Watch: Leverage ratio (gear shift at airbag barrier)

---

### 5.1.8 — Bonus Note (Bonus)

| Field | Value |
|-------|-------|
| **Product Name** | Bonus Note |
| **Abbreviation** | Bonus |
| **Family** | Equity-Linked Notes |
| **Complexity Score** | 4 / 10 |
| **Complexity Rationale** | Capital-protected participation note with bonus minimum return if underlying stays above barrier |
| **Underlying Asset Class** | Equity (index or stock) |
| **Capital Protection** | Conditional (bonus forfeited if barrier breached, but principal returned at maturity) |
| **Coupon Type** | Bonus coupon if barrier not breached |
| **Maturity Profile** | 3-5 years |
| **Liquidity Profile** | Secondary market |
| **Primary Buyer** | Conservative investors wanting equity exposure with minimum return guarantee |
| **Primary Risk** | Barrier breach eliminates bonus. Below barrier, product behaves like direct equity (full loss exposure) |
| **Primary Hedge** | ZCB hedge, delta-hedge call, DI put replication |
| **Primary System** | Murex |
| **ISDA Required** | No — issued as note |
| **One-Line Summary** | Earn a guaranteed minimum return while keeping equity upside, provided underlying stays above barrier |

**Remember These 3 Things:**

1. ZCB + European call + short down-and-in put + bonus coupon mechanism
2. Key risk: Barrier breach eliminates bonus
3. Watch: Gamma

---

### 5.1.9 — Fixed Coupon Note (FCN)

| Field | Value |
|-------|-------|
| **Product Name** | Fixed Coupon Note |
| **Abbreviation** | FCN |
| **Family** | Equity-Linked Notes |
| **Complexity Score** | 6 / 10 |
| **Complexity Rationale** | RC variant paying guaranteed fixed coupons with autocall feature. Combines RC downside with Phoenix-like autocall |
| **Underlying Asset Class** | Equity (single stock or basket) |
| **Capital Protection** | Conditional (protected above barrier at maturity) |
| **Coupon Type** | Fixed guaranteed coupon (paid regardless) |
| **Maturity Profile** | 1-3 years |
| **Liquidity Profile** | Secondary market |
| **Primary Buyer** | Income-focused investors comfortable with conditional downside. Asia-Pacific private banking |
| **Primary Risk** | Barrier breach at maturity with loss. Autocall limits upside. Guaranteed coupons partially offset losses |
| **Primary Hedge** | Long put (delta-hedged), autocall replication |
| **Primary System** | Murex |
| **ISDA Required** | No — issued as note |
| **One-Line Summary** | Guaranteed income stream regardless of performance |

**Remember These 3 Things:**

1. Fixed coupon note (guaranteed income) + short put (downside risk) + autocall binary options (early redemption triggers)
2. Key risk: Barrier breach at maturity with loss
3. Watch: Barrier distance at maturity (final observation determines capital loss)

---

### 5.1.10 — Callable Range Accrual ELN (CRA ELN)

| Field | Value |
|-------|-------|
| **Product Name** | Callable Range Accrual ELN |
| **Abbreviation** | CRA ELN |
| **Family** | Equity-Linked Notes |
| **Complexity Score** | 6 / 10 |
| **Complexity Rationale** | Range accrual coupon on equity underlying with issuer call right. Days in range determine coupon. Most complex ELN coupon |
| **Underlying Asset Class** | Equity (index) |
| **Capital Protection** | 100% at maturity |
| **Coupon Type** | Accrual coupon (proportional to days in range) |
| **Maturity Profile** | 3-7 years |
| **Liquidity Profile** | Secondary market |
| **Primary Buyer** | Yield-seeking institutional investors with range-bound equity view |
| **Primary Risk** | Days outside range reduce coupon to zero. Call risk if accrual is favourable. Dual optionality exposure |
| **Primary Hedge** | Daily digital option strip, call option hedge |
| **Primary System** | Murex |
| **ISDA Required** | No — issued as note |
| **One-Line Summary** | Enhanced yield from selling range and call optionality |

**Remember These 3 Things:**

1. Fixed note (principal) + strip of daily digital options on equity index (coupon engine) + short Bermudan call (issuer termination right)
2. Key risk: Days outside range reduce coupon to zero
3. Watch: Digital gamma

---

### 5.1.11 — Issuer Callable Note (ICN)

| Field | Value |
|-------|-------|
| **Product Name** | Issuer Callable Note |
| **Abbreviation** | ICN |
| **Family** | Equity-Linked Notes |
| **Complexity Score** | 3 / 10 |
| **Complexity Rationale** | Equity-linked note with issuer call right on predetermined dates. Higher coupon for callability. No autocall trigger |
| **Underlying Asset Class** | Equity (single stock or index) |
| **Capital Protection** | Conditional (depends on variant) |
| **Coupon Type** | Enhanced fixed or contingent coupon |
| **Maturity Profile** | 2-5 years |
| **Liquidity Profile** | Secondary market |
| **Primary Buyer** | Yield-seeking investors willing to accept early termination risk |
| **Primary Risk** | Call exercised when profitable for bank. Reinvestment risk for investor. Same directional risk as underlying note type |
| **Primary Hedge** | Long Bermudan call, underlying ELN hedge |
| **Primary System** | Murex |
| **ISDA Required** | No — issued as note |
| **One-Line Summary** | Higher coupon than non-callable equivalent |

**Remember These 3 Things:**

1. Underlying ELN structure + short Bermudan call to issuer
2. Key risk: Call exercised when profitable for bank
3. Watch: Vega

---

### 5.1.12 — Digital Coupon Note (Digital)

| Field | Value |
|-------|-------|
| **Product Name** | Digital Coupon Note |
| **Abbreviation** | Digital |
| **Family** | Equity-Linked Notes |
| **Complexity Score** | 4 / 10 |
| **Complexity Rationale** | Binary coupon structure — pays fixed coupon if underlying above digital strike, zero otherwise. Clean yes/no outcome |
| **Underlying Asset Class** | Equity (single stock or index) |
| **Capital Protection** | 100% at maturity |
| **Coupon Type** | Digital coupon (all-or-nothing based on observation) |
| **Maturity Profile** | 1-3 years |
| **Liquidity Profile** | Secondary market |
| **Primary Buyer** | Income-focused investors with directional equity view. Prefer defined outcomes over variable participation |
| **Primary Risk** | Missing coupon if underlying below strike on observation date. Near-strike, small move causes large P&L swing |
| **Primary Hedge** | Digital option replication via tight call spreads |
| **Primary System** | Murex |
| **ISDA Required** | No — issued as note |
| **One-Line Summary** | Clear binary outcome: coupon paid or not |

**Remember These 3 Things:**

1. Fixed note + strip of digital call options on equity observation dates
2. Key risk: Missing coupon if underlying below strike on observation date
3. Watch: Digital gamma

---

### 5.1.13 — Booster Note (Booster)

| Field | Value |
|-------|-------|
| **Product Name** | Booster Note |
| **Abbreviation** | Booster |
| **Family** | Equity-Linked Notes |
| **Complexity Score** | 4 / 10 |
| **Complexity Rationale** | Leveraged participation note — amplified upside (e.g., 200%) up to a cap, with direct downside exposure below strike |
| **Underlying Asset Class** | Equity (index) |
| **Capital Protection** | None (full equity downside below strike) |
| **Coupon Type** | None — return via leveraged participation |
| **Maturity Profile** | 2-5 years |
| **Liquidity Profile** | Secondary market |
| **Primary Buyer** | Moderately bullish investors wanting amplified returns within a range |
| **Primary Risk** | Full downside below strike. Upside capped despite leverage. No capital protection |
| **Primary Hedge** | Delta-hedge leveraged position, call spread replication |
| **Primary System** | Murex |
| **ISDA Required** | No — issued as note |
| **One-Line Summary** | Double (or more) participation in moderate upside |

**Remember These 3 Things:**

1. Leveraged call spread + equity forward below strike
2. Key risk: Full downside below strike
3. Watch: Participation rate and cap level (defines upside range)

---

### 5.1.14 — Digital Coupon Knock-In Put (DKIP)

| Field | Value |
|-------|-------|
| **Product Name** | Digital Coupon Knock-In Put |
| **Abbreviation** | DKIP |
| **Family** | Equity-Linked Notes |
| **Complexity Score** | 7 / 10 |
| **Complexity Rationale** | Combines digital coupon with knock-in put barrier. Coupon if above digital strike; principal at risk if barrier breached |
| **Underlying Asset Class** | Equity (single stock) |
| **Capital Protection** | Conditional (barrier-protected principal) |
| **Coupon Type** | Digital coupon (binary observation) |
| **Maturity Profile** | 1-3 years |
| **Liquidity Profile** | Secondary market |
| **Primary Buyer** | Yield-seeking investors comfortable with barrier risk and digital coupon uncertainty |
| **Primary Risk** | Barrier breach exposes principal to equity downside. Missing digital coupons if below digital strike. Dual conditional risk |
| **Primary Hedge** | Long DI put, digital replication, delta-hedge |
| **Primary System** | Murex |
| **ISDA Required** | No — issued as note |
| **One-Line Summary** | Higher yield than plain digital or plain RC |

**Remember These 3 Things:**

1. Digital coupon options + short down-and-in put option
2. Key risk: Barrier breach exposes principal to equity downside
3. Watch: Gamma

---

### 5.1.15 — Warrant / Turbo Certificate (Warrant)

| Field | Value |
|-------|-------|
| **Product Name** | Warrant / Turbo Certificate |
| **Abbreviation** | Warrant |
| **Family** | Equity-Linked Notes |
| **Complexity Score** | 3 / 10 |
| **Complexity Rationale** | Leveraged exposure instrument — direct participation in underlying with gearing. Simplest leveraged product |
| **Underlying Asset Class** | Equity (stock, index, commodity, FX) |
| **Capital Protection** | None (option can expire worthless — lose entire premium) |
| **Coupon Type** | None — return via leveraged price movement |
| **Maturity Profile** | Weeks to 2 years |
| **Liquidity Profile** | Exchange-traded (high liquidity) |
| **Primary Buyer** | Directional traders, retail speculators, hedgers seeking cheap protection |
| **Primary Risk** | Total loss of premium if out-of-money at expiry. Leverage amplifies losses. Time decay erodes value |
| **Primary Hedge** | Delta-hedge underlying, manage time decay |
| **Primary System** | Exchange systems |
| **ISDA Required** | No — exchange-traded |
| **One-Line Summary** | Cheap leveraged exposure to underlying |

**Remember These 3 Things:**

1. Standardised call or put option
2. Key risk: Total loss of premium if out-of-money at expiry
3. Watch: Delta + Theta

---

### 5.2.1 — Interest Rate Swap (IRS)

| Field | Value |
|-------|-------|
| **Product Name** | Interest Rate Swap |
| **Abbreviation** | IRS |
| **Family** | Swaps |
| **Complexity Score** | 3 / 10 |
| **Complexity Rationale** | Fixed-for-floating rate exchange. Most liquid OTC derivative. Foundation for all structured rate products |
| **Underlying Asset Class** | Rates |
| **Capital Protection** | N/A (swap — no principal exchanged) |
| **Coupon Type** | Fixed coupon exchanged for floating |
| **Maturity Profile** | 1-30 years |
| **Liquidity Profile** | OTC (very liquid for standard tenors) |
| **Primary Buyer** | Banks (ALM), corporations (hedging), institutional investors (duration management) |
| **Primary Risk** | Interest rate moves against position. MTM exposure grows with maturity. Counterparty credit risk |
| **Primary Hedge** | Offsetting IRS, futures strip, swaption for optionality |
| **Primary System** | Murex |
| **ISDA Required** | Yes — ISDA Master Agreement |
| **One-Line Summary** | Transform fixed-rate exposure to floating or vice versa |

**Remember These 3 Things:**

1. Fixed leg (coupon bond equivalent) vs floating leg (FRN equivalent)
2. Key risk: Interest rate moves against position
3. Watch: DV01 / Duration

---

### 5.2.2 — Total Return Swap (TRS)

| Field | Value |
|-------|-------|
| **Product Name** | Total Return Swap |
| **Abbreviation** | TRS |
| **Family** | Swaps |
| **Complexity Score** | 5 / 10 |
| **Complexity Rationale** | Exchange total return of reference asset for funding rate. Synthetic asset ownership without balance sheet impact |
| **Underlying Asset Class** | Multi-asset (equity, credit, loans) |
| **Capital Protection** | N/A (swap — unfunded or partially funded) |
| **Coupon Type** | Total return (price + income) vs funding rate |
| **Maturity Profile** | 1-5 years |
| **Liquidity Profile** | OTC (bilateral) |
| **Primary Buyer** | Hedge funds (leveraged exposure), banks (regulatory capital management), institutions (synthetic access) |
| **Primary Risk** | Full market risk of reference asset. Counterparty risk. Funding spread can change. Mark-to-market volatility |
| **Primary Hedge** | Hedge reference asset directly or via proxy |
| **Primary System** | Murex |
| **ISDA Required** | Yes — ISDA |
| **One-Line Summary** | Synthetic exposure to assets without owning them |

**Remember These 3 Things:**

1. Total return leg (reference asset P&L) vs funding leg (SOFR + spread)
2. Key risk: Full market risk of reference asset
3. Watch: Funding spread (SOFR + X determines carry cost)

---

### 5.2.3 — Equity Swap (EqSwap)

| Field | Value |
|-------|-------|
| **Product Name** | Equity Swap |
| **Abbreviation** | EqSwap |
| **Family** | Swaps |
| **Complexity Score** | 5 / 10 |
| **Complexity Rationale** | Swap of equity return for fixed or floating rate. Standardised TRS for equity underlyings |
| **Underlying Asset Class** | Equity |
| **Capital Protection** | N/A (swap) |
| **Coupon Type** | Equity return vs funding rate |
| **Maturity Profile** | 6 months - 5 years |
| **Liquidity Profile** | OTC (bilateral) |
| **Primary Buyer** | Institutional investors, hedge funds, asset managers seeking synthetic equity exposure |
| **Primary Risk** | Full equity market risk. Dividend risk. Counterparty credit risk |
| **Primary Hedge** | Delta-hedge equity leg, manage dividend risk |
| **Primary System** | Murex |
| **ISDA Required** | Yes — ISDA Equity Definitions |
| **One-Line Summary** | Synthetic equity exposure without share ownership |

**Remember These 3 Things:**

1. Equity return leg + funding/fixed rate leg
2. Key risk: Full equity market risk
3. Watch: Dividend risk (expected vs realised dividends drive swap value)

---

### 5.2.4 — Variance Swap (VarSwap)

| Field | Value |
|-------|-------|
| **Product Name** | Variance Swap |
| **Abbreviation** | VarSwap |
| **Family** | Swaps |
| **Complexity Score** | 7 / 10 |
| **Complexity Rationale** | Swap paying realised variance vs fixed variance strike. Pure volatility exposure without directional bias. Convex payoff |
| **Underlying Asset Class** | Equity (volatility) |
| **Capital Protection** | N/A (swap — can have large negative MTM) |
| **Coupon Type** | Realised variance vs strike variance |
| **Maturity Profile** | 1 month - 2 years |
| **Liquidity Profile** | OTC (index var swaps reasonably liquid) |
| **Primary Buyer** | Hedge funds (vol trading), dealers (managing vol book), institutional (tail hedging) |
| **Primary Risk** | Variance is convex — large moves cause outsized P&L. Gap risk. Realised vol spikes can cause extreme losses for short position |
| **Primary Hedge** | Replicating portfolio of OTM options, delta-hedged. Vega hedge via swaptions or options |
| **Primary System** | Murex |
| **ISDA Required** | Yes — ISDA |
| **One-Line Summary** | Trade realized volatility directly, without taking a directional view on the market |

**Remember These 3 Things:**

1. Variance swap = portfolio of options across all strikes (log contract replication)
2. Key risk: Variance is convex — large moves cause outsized P&L
3. Watch: Vega

---

### 5.2.5 — Credit Default Swap (CDS)

| Field | Value |
|-------|-------|
| **Product Name** | Credit Default Swap |
| **Abbreviation** | CDS |
| **Family** | Swaps |
| **Complexity Score** | 5 / 10 |
| **Complexity Rationale** | Credit protection contract — buyer pays spread for protection against credit event. Foundation of credit derivatives |
| **Underlying Asset Class** | Credit |
| **Capital Protection** | N/A (swap — notional at risk for protection seller) |
| **Coupon Type** | CDS spread (periodic premium) |
| **Maturity Profile** | 1-10 years (5Y most liquid) |
| **Liquidity Profile** | OTC (index CDS very liquid, single-name varies) |
| **Primary Buyer** | Banks (hedging loan books), hedge funds (credit trading), insurance (selling protection for yield) |
| **Primary Risk** | Credit event of reference entity. Jump-to-default risk. Recovery rate uncertainty. Counterparty risk on protection seller |
| **Primary Hedge** | Offsetting CDS, basis trade (CDS vs bond spread), index hedge |
| **Primary System** | Murex |
| **ISDA Required** | Yes — ISDA Credit Definitions |
| **One-Line Summary** | Hedge credit exposure without selling bonds |

**Remember These 3 Things:**

1. CDS = credit insurance contract
2. Key risk: Credit event of reference entity
3. Watch: Credit spread delta

---

### 5.2.6 — Cross-Currency Swap (XCCY)

| Field | Value |
|-------|-------|
| **Product Name** | Cross-Currency Swap |
| **Abbreviation** | XCCY |
| **Family** | Swaps |
| **Complexity Score** | 5 / 10 |
| **Complexity Rationale** | Exchange of principal and interest in two currencies. Combines IRS with FX forward. Complex due to dual-currency cash flows |
| **Underlying Asset Class** | FX + Rates |
| **Capital Protection** | N/A (swap — principals exchanged) |
| **Coupon Type** | Interest in both currencies |
| **Maturity Profile** | 1-30 years |
| **Liquidity Profile** | OTC (liquid for major pairs) |
| **Primary Buyer** | Multinational corporates (hedging foreign debt), banks (funding in foreign currencies), sovereigns |
| **Primary Risk** | FX risk on principal exchange. Interest rate risk in both currencies. Basis spread risk. Counterparty credit risk |
| **Primary Hedge** | IRS in each currency, FX forwards/options |
| **Primary System** | Murex |
| **ISDA Required** | Yes — ISDA |
| **One-Line Summary** | Convert foreign currency debt to domestic |

**Remember These 3 Things:**

1. Two IRS legs in different currencies + FX forward for principal exchange
2. Key risk: FX risk on principal exchange
3. Watch: FX delta + Dollar Value of One Basis Point

---

### 5.2.7 — Commodity Swap (CommSwap)

| Field | Value |
|-------|-------|
| **Product Name** | Commodity Swap |
| **Abbreviation** | CommSwap |
| **Family** | Swaps |
| **Complexity Score** | 4 / 10 |
| **Complexity Rationale** | Fixed-for-floating exchange on commodity price. Physical or financial settlement. Hedging tool for producers and consumers |
| **Underlying Asset Class** | Commodities |
| **Capital Protection** | N/A (swap) |
| **Coupon Type** | Fixed vs floating commodity price |
| **Maturity Profile** | 1 month - 5 years |
| **Liquidity Profile** | OTC (bilateral, some exchange-cleared) |
| **Primary Buyer** | Commodity producers (lock in selling price), consumers (lock in buying price), traders |
| **Primary Risk** | Commodity price volatility. Basis risk (hedge vs actual commodity). Contango/backwardation. Physical delivery risk |
| **Primary Hedge** | Offsetting commodity swap, futures, options on commodity |
| **Primary System** | Murex / Endur |
| **ISDA Required** | Yes — ISDA |
| **One-Line Summary** | Lock in commodity price for budget certainty |

**Remember These 3 Things:**

1. Fixed-price leg vs floating-price leg (referenced to commodity benchmark)
2. Key risk: Commodity price volatility
3. Watch: Commodity delta

---

### 5.2.8 — Vanilla Swap Plus (VLSP)

| Field | Value |
|-------|-------|
| **Product Name** | Vanilla Swap Plus |
| **Abbreviation** | VLSP |
| **Family** | Swaps |
| **Complexity Score** | 2 / 10 |
| **Complexity Rationale** | Enhanced IRS with additional features — spread compression, amortisation, or cap/floor. Intermediate between IRS and structured rate trades |
| **Underlying Asset Class** | Rates |
| **Capital Protection** | N/A (swap) |
| **Coupon Type** | Fixed vs structured floating |
| **Maturity Profile** | 2-10 years |
| **Liquidity Profile** | OTC (less liquid than vanilla IRS) |
| **Primary Buyer** | Banks, corporates seeking customised rate hedges beyond vanilla IRS |
| **Primary Risk** | Same as IRS plus feature-specific risks — cap/floor gamma, amortisation scheduling, spread basis risk |
| **Primary Hedge** | IRS hedge + feature-specific hedges (cap/floor options, amortisation schedule) |
| **Primary System** | Murex |
| **ISDA Required** | Yes — ISDA |
| **One-Line Summary** | Customize an interest rate swap with caps, floors, amortisation, or step-ups beyond vanilla IRS |

**Remember These 3 Things:**

1. IRS + one or more of: amortising notional, cap/floor, step-up/step-down, spread adjustment
2. Key risk: Same as IRS plus feature-specific risks — cap/floor gamma, amortisation scheduling, spread basis risk
3. Watch: DV01 + Vega

---

### 5.3.1 — IR Callable Fixed Rate Swap (IR Callable)

| Field | Value |
|-------|-------|
| **Product Name** | IR Callable Fixed Rate Swap |
| **Abbreviation** | IR Callable |
| **Family** | Structured Rate Trades |
| **Complexity Score** | 5 / 10 |
| **Complexity Rationale** | Fixed coupon + embedded receiver swaption (call right). Four-leg SRT. Multiple exercise dates |
| **Underlying Asset Class** | Rates (SOFR / EURIBOR) |
| **Capital Protection** | None (swap — notional not at risk but MTM can be negative) |
| **Coupon Type** | Enhanced fixed coupon (above-market rate funded by embedded swaption premium) |
| **Maturity Profile** | 5–30 years (callable after non-call period, typically 1–5 years) |
| **Liquidity Profile** | OTC — unwind at MTM |
| **Primary Buyer** | Insurance companies, pension funds seeking fixed-rate income with yield pickup over vanilla swaps |
| **Primary Risk** | Interest rate risk. Bank exercises call when rates move against investor. Reinvestment risk on early termination |
| **Primary Hedge** | Receiver swaption, IRS delta hedge |
| **Primary System** | Murex (primary, four-leg structure), Sophis (risk) |
| **ISDA Required** | No — issued as note (no derivatives documentation from client) |
| **One-Line Summary** | Yield enhancement on fixed income allocation |

**Remember These 3 Things:**

1. Interest rate swap + embedded receiver swaption sold to bank
2. Key risk: Interest rate risk
3. Watch: Vega

---

### 5.3.2 — Zero-Coupon Linked Note (ZCL)

| Field | Value |
|-------|-------|
| **Product Name** | Zero-Coupon Linked Note |
| **Abbreviation** | ZCL |
| **Family** | Structured Rate Trades |
| **Complexity Score** | 4 / 10 |
| **Complexity Rationale** | Zero-coupon accretion. No periodic cash flows. Four-leg SRT. Single embedded swap |
| **Underlying Asset Class** | Rates (SOFR / EURIBOR) |
| **Capital Protection** | 100% at maturity (ZCB structure) |
| **Coupon Type** | None — return via discount accretion (zero coupon) |
| **Maturity Profile** | 10–30 years (long duration to match liability profiles) |
| **Liquidity Profile** | Secondary market (duration-dependent pricing) |
| **Primary Buyer** | Pension funds, insurance companies, endowments with long-dated liabilities |
| **Primary Risk** | Duration risk (long-dated ZCB sensitivity). Issuer credit risk over multi-year term |
| **Primary Hedge** | Zero-coupon government bonds, IRS |
| **Primary System** | Murex (primary, four-leg structure), Sophis (risk) |
| **ISDA Required** | No — issued as note |
| **One-Line Summary** | Liability matching without reinvestment risk |

**Remember These 3 Things:**

1. Zero-coupon bond + interest rate swap (accreting notional)
2. Key risk: Duration risk (long-dated ZCB sensitivity)
3. Watch: Dollar Value of One Basis Point

---

### 5.3.3 — Non-Callable Range Accrual (NCRA)

| Field | Value |
|-------|-------|
| **Product Name** | Non-Callable Range Accrual |
| **Abbreviation** | NCRA |
| **Family** | Structured Rate Trades |
| **Complexity Score** | 6 / 10 |
| **Complexity Rationale** | Conditional coupon via daily range accrual. Strip of digital options. Multiple observation dates |
| **Underlying Asset Class** | Rates (6-month SOFR, daily observation) |
| **Capital Protection** | 100% at maturity (principal returned regardless of coupon) |
| **Coupon Type** | Accrual coupon (proportional to days SOFR stays in predefined range) |
| **Maturity Profile** | 5–10 years |
| **Liquidity Profile** | Secondary market |
| **Primary Buyer** | Yield-seeking investors with stable rate view |
| **Primary Risk** | Reference rate falling outside range. Days-outside-range reduce coupon. Range set at inception — no adjustment |
| **Primary Hedge** | Strip of digital options on reference rate, IRS |
| **Primary System** | Murex (primary), Sophis (risk) |
| **ISDA Required** | No — issued as note |
| **One-Line Summary** | Enhanced yield when investor believes reference rate will remain range-bound |

**Remember These 3 Things:**

1. Fixed-rate note + strip of digital options (one per accrual day)
2. Key risk: Reference rate falling outside range
3. Watch: Digital gamma

---

### 5.3.4 — Callable Range Accrual SRT (CRA SRT)

| Field | Value |
|-------|-------|
| **Product Name** | Callable Range Accrual SRT |
| **Abbreviation** | CRA SRT |
| **Family** | Structured Rate Trades |
| **Complexity Score** | 7 / 10 |
| **Complexity Rationale** | Combines range accrual + callable. Dual embedded options (digital strip + swaption). Path-dependent |
| **Underlying Asset Class** | Rates (6-month SOFR, daily observation) |
| **Capital Protection** | 100% at maturity |
| **Coupon Type** | Accrual coupon (range-dependent) — enhanced by embedded call premium |
| **Maturity Profile** | 5–15 years (callable after non-call period) |
| **Liquidity Profile** | OTC — model-dependent |
| **Primary Buyer** | Yield-seeking institutional investors willing to sell callability for extra coupon |
| **Primary Risk** | Range accrual risk + callability risk. Bank calls when range accrual is profitable for investor |
| **Primary Hedge** | Digital option strip + receiver swaption |
| **Primary System** | Murex (primary), Sophis (risk) |
| **ISDA Required** | No — issued as note |
| **One-Line Summary** | Maximum yield enhancement — sells both range risk and call optionality |

**Remember These 3 Things:**

1. NCRA + receiver swaption sold to bank
2. Key risk: Range accrual risk + callability risk
3. Watch: Vega

---

### 5.3.5 — Digital Cap-Floor Note (Digital CF)

| Field | Value |
|-------|-------|
| **Product Name** | Digital Cap-Floor Note |
| **Abbreviation** | Digital CF |
| **Family** | Structured Rate Trades |
| **Complexity Score** | 5 / 10 |
| **Complexity Rationale** | Strip of digital caplets. Binary payoff at each observation. Four-leg SRT structure |
| **Underlying Asset Class** | Rates (3-month SOFR, quarterly observation) |
| **Capital Protection** | 100% at maturity |
| **Coupon Type** | Digital coupon (binary — full or zero per observation period) |
| **Maturity Profile** | 3–7 years |
| **Liquidity Profile** | Secondary market |
| **Primary Buyer** | Institutional investors seeking defined-outcome rate exposure |
| **Primary Risk** | Digital payoff — small rate move across strike causes large P&L swing. Discontinuous payoff at cap/floor levels |
| **Primary Hedge** | Digital options, call/put spreads as digital approximation |
| **Primary System** | Murex (primary), Sophis (risk) |
| **ISDA Required** | No — issued as note |
| **One-Line Summary** | Binary view on rates — pay enhanced coupon if rate above/below digital strike |

**Remember These 3 Things:**

1. Fixed-rate note + digital cap/floor options
2. Key risk: Digital payoff — small rate move across strike causes large P&L swing
3. Watch: Digital gamma

---

### 5.4.1 — Vanilla Steepener Note (Vanilla STEG)

| Field | Value |
|-------|-------|
| **Product Name** | Vanilla Steepener Note |
| **Abbreviation** | Vanilla STEG |
| **Family** | Steepener Notes |
| **Complexity Score** | 5 / 10 |
| **Complexity Rationale** | Leveraged CMS spread coupon (CMS30Y - CMS2Y). Floor, cap. CMS convexity adjustment. Building block for STEG family |
| **Underlying Asset Class** | Rates (CMS30Y − CMS2Y swap curve slope) |
| **Capital Protection** | 100% at maturity |
| **Coupon Type** | Leveraged CMS spread coupon with floor and cap |
| **Maturity Profile** | 10–30 years |
| **Liquidity Profile** | Secondary market |
| **Primary Buyer** | Institutional investors with steepening view on yield curve |
| **Primary Risk** | Curve flattening or inversion. Coupon = CMS30 - CMS2 (or similar). If spread narrows, coupon drops. Can reach zero |
| **Primary Hedge** | CMS spread swaps, CMS cap/floor |
| **Primary System** | Murex (primary), Sophis (risk) |
| **ISDA Required** | No — issued as note |
| **One-Line Summary** | Express curve steepening view with leveraged exposure |

**Remember These 3 Things:**

1. Fixed-rate note + CMS spread option (long CMS30, short CMS2)
2. Key risk: Curve flattening or inversion
3. Watch: CMS spread delta

---

### 5.4.2 — Range Accrual Steepener (RA STEG)

| Field | Value |
|-------|-------|
| **Product Name** | Range Accrual Steepener |
| **Abbreviation** | RA STEG |
| **Family** | Steepener Notes |
| **Complexity Score** | 7 / 10 |
| **Complexity Rationale** | Range accrual on CMS spread (not single rate). Daily observation on spread creates strip of digital spread options |
| **Underlying Asset Class** | Rates (CMS30Y − CMS2Y spread, daily observation) |
| **Capital Protection** | 100% at maturity |
| **Coupon Type** | Accrual coupon (proportional to days CMS spread stays in range) |
| **Maturity Profile** | 5–15 years |
| **Liquidity Profile** | OTC — model-dependent |
| **Primary Buyer** | Yield-seeking institutional investors with stable-rate + steepening view |
| **Primary Risk** | Dual risk — curve must steepen AND reference rate must stay in range. Two conditions must be met simultaneously |
| **Primary Hedge** | CMS spread swap + digital option strip |
| **Primary System** | Murex (primary), Sophis (risk) |
| **ISDA Required** | No — issued as note |
| **One-Line Summary** | Maximum yield from combined curve and range view |

**Remember These 3 Things:**

1. Vanilla STEG + range accrual digital strip
2. Key risk: Dual risk — curve must steepen AND reference rate must stay in range
3. Watch: CMS spread delta + digital gamma

---

### 5.4.3 — Callable Steepener (Callable STEG)

| Field | Value |
|-------|-------|
| **Product Name** | Callable Steepener |
| **Abbreviation** | Callable STEG |
| **Family** | Steepener Notes |
| **Complexity Score** | 6 / 10 |
| **Complexity Rationale** | Leveraged CMS spread + Bermudan call right. CMS convexity × swaption interaction. Reinvestment risk |
| **Underlying Asset Class** | Rates (CMS30Y − CMS2Y spread) |
| **Capital Protection** | 100% at maturity (or on call date) |
| **Coupon Type** | Enhanced leveraged CMS spread coupon (call premium funds additional yield) |
| **Maturity Profile** | 10–30 years (callable after non-call period) |
| **Liquidity Profile** | OTC — model-dependent |
| **Primary Buyer** | Institutional investors selling call optionality for enhanced steepener coupon |
| **Primary Risk** | Callability risk + curve risk. Bank calls when steepener coupon is high (good for investor). Reinvestment risk |
| **Primary Hedge** | CMS spread swap + Bermudan swaption |
| **Primary System** | Murex (primary) |
| **ISDA Required** | No — issued as note |
| **One-Line Summary** | Yield pickup over vanilla STEG by selling bank's right to terminate early |

**Remember These 3 Things:**

1. Vanilla STEG + Bermudan swaption sold to bank
2. Key risk: Callability risk + curve risk
3. Watch: Vega

---

### 5.4.4 — TARN Steepener (TARN STEG)

| Field | Value |
|-------|-------|
| **Product Name** | TARN Steepener |
| **Abbreviation** | TARN STEG |
| **Family** | Steepener Notes |
| **Complexity Score** | 8 / 10 |
| **Complexity Rationale** | Leveraged CMS spread with target accumulation and automatic redemption. Path-dependent. Monte Carlo pricing |
| **Underlying Asset Class** | Rates (CMS30Y − CMS2Y spread) |
| **Capital Protection** | 100% at maturity or target date |
| **Coupon Type** | Leveraged CMS spread coupon with cumulative target cap |
| **Maturity Profile** | 10 years maximum (terminates early if target reached) |
| **Liquidity Profile** | OTC — model-dependent |
| **Primary Buyer** | Institutional investors wanting defined total return from curve steepening |
| **Primary Risk** | Target reached = early termination. If curve steepens rapidly, target met quickly and product terminates. Reinvestment risk in favourable environment |
| **Primary Hedge** | CMS spread swap + path-dependent autocall replication |
| **Primary System** | Murex (primary), Sophis (risk) |
| **ISDA Required** | No — issued as note |
| **One-Line Summary** | Target total coupon from steepener — product terminates once total paid reaches target |

**Remember These 3 Things:**

1. Vanilla STEG + target accumulation trigger + early termination mechanism
2. Key risk: Target reached = early termination
3. Watch: CMS spread delta + path-dependent gamma

---

### 5.5.1 — Vanilla Credit-Linked Note (CLN)

| Field | Value |
|-------|-------|
| **Product Name** | Vanilla Credit-Linked Note |
| **Abbreviation** | CLN |
| **Family** | Credit-Linked Notes |
| **Complexity Score** | 4 / 10 |
| **Complexity Rationale** | Funded credit derivative — combines note with embedded CDS. Investor sells credit protection through note purchase |
| **Underlying Asset Class** | Credit |
| **Capital Protection** | Conditional (principal at risk on credit event) |
| **Coupon Type** | Fixed coupon (includes CDS spread) |
| **Maturity Profile** | 3-5 years |
| **Liquidity Profile** | Secondary market (limited) |
| **Primary Buyer** | Yield-seeking investors wanting credit spread exposure in funded format |
| **Primary Risk** | Credit event of reference entity causes principal loss. Dual credit exposure: reference entity AND issuer. Recovery rate uncertainty |
| **Primary Hedge** | CDS on reference entity, credit index hedge |
| **Primary System** | Murex |
| **ISDA Required** | No — issued as note |
| **One-Line Summary** | Access to CDS-like exposure without ISDA agreement |

**Remember These 3 Things:**

1. Fixed-rate note + embedded CDS (investor is protection seller)
2. Key risk: Credit event of reference entity causes principal loss
3. Watch: Credit spread delta

---

### 5.5.2 — Skew Credit-Linked Note (Skew CLN)

| Field | Value |
|-------|-------|
| **Product Name** | Skew Credit-Linked Note |
| **Abbreviation** | Skew CLN |
| **Family** | Credit-Linked Notes |
| **Complexity Score** | 5 / 10 |
| **Complexity Rationale** | Vanilla CLN (4) + modified recovery mechanism adds one structural feature layer |
| **Underlying Asset Class** | Credit (single reference entity) |
| **Capital Protection** | Conditional (protected if no credit event) |
| **Coupon Type** | Fixed (enhanced by modified recovery terms) |
| **Maturity Profile** | 3–5 years |
| **Liquidity Profile** | OTC — model-dependent |
| **Primary Buyer** | Credit investors with specific recovery rate views |
| **Primary Risk** | Credit default of reference entity. Non-linear recovery exposure — loss depends on actual recovery rate vs assumed |
| **Primary Hedge** | CDS + recovery rate swaps |
| **Primary System** | NEMO (primary), Sophis (risk) |
| **ISDA Required** | No — issued as note |
| **One-Line Summary** | Express view on recovery rate distribution, not just default probability |

**Remember These 3 Things:**

1. CLN + digital/barrier recovery payoff
2. Key risk: Credit default of reference entity
3. Watch: Recovery delta

---

### 5.5.3 — First-to-Default Note (FTD)

| Field | Value |
|-------|-------|
| **Product Name** | First-to-Default Note |
| **Abbreviation** | FTD |
| **Family** | Credit-Linked Notes |
| **Complexity Score** | 7 / 10 |
| **Complexity Rationale** | Single-name CLN (4) + basket mechanics + credit correlation + first-default trigger. Correlation-dependent pricing |
| **Underlying Asset Class** | Credit (basket of 5–10 reference entities) |
| **Capital Protection** | Conditional (protected if no credit event in basket) |
| **Coupon Type** | Fixed (enhanced by basket risk premium) |
| **Maturity Profile** | 3–5 years |
| **Liquidity Profile** | OTC — model-dependent |
| **Primary Buyer** | Yield-seeking credit investors willing to take basket default risk |
| **Primary Risk** | First default in basket triggers full loss. Probability driven by correlation — low correlation = higher risk |
| **Primary Hedge** | Individual CDS on each basket constituent + correlation hedge |
| **Primary System** | NEMO (primary), Sophis (risk) |
| **ISDA Required** | No — issued as note |
| **One-Line Summary** | Enhanced yield by selling first-default protection on basket of 3-7 names |

**Remember These 3 Things:**

1. CLN + first-to-default CDS on basket
2. Key risk: First default in basket triggers full loss
3. Watch: Credit spread delta

---

### 5.5.4 — Nth-to-Default Note (NTD)

| Field | Value |
|-------|-------|
| **Product Name** | Nth-to-Default Note |
| **Abbreviation** | NTD |
| **Family** | Credit-Linked Notes |
| **Complexity Score** | 8 / 10 |
| **Complexity Rationale** | FTD (7) + Nth-default threshold + correlation reversal effect. Nonlinear correlation sensitivity |
| **Underlying Asset Class** | Credit (basket of 5–10 reference entities) |
| **Capital Protection** | Conditional (protected if fewer than N defaults) |
| **Coupon Type** | Fixed |
| **Maturity Profile** | 3–5 years |
| **Liquidity Profile** | OTC — model-dependent |
| **Primary Buyer** | Institutional credit investors seeking specific correlation exposure |
| **Primary Risk** | Nth default in basket. Correlation reversal — high correlation INCREASES NTD risk (opposite of FTD). All-or-nothing default threshold |
| **Primary Hedge** | Individual CDS + correlation-dependent basket hedges |
| **Primary System** | NEMO (primary), Sophis (risk) |
| **ISDA Required** | No — issued as note |
| **One-Line Summary** | Tail credit risk exposure — protected against first N-1 defaults, exposed to Nth |

**Remember These 3 Things:**

1. CLN + Nth-to-default CDS on basket
2. Key risk: Nth default in basket
3. Watch: Credit spread delta + correlation

---

### 5.5.5 — Synthetic CDO Tranche (CDO)

| Field | Value |
|-------|-------|
| **Product Name** | Synthetic CDO Tranche |
| **Abbreviation** | CDO |
| **Family** | Credit-Linked Notes |
| **Complexity Score** | 10 / 10 |
| **Complexity Rationale** | NTD (8) + tranching + attachment/detachment points + portfolio-level modeling + copula dependency + 2008 financial crisis context. Most complex product in the universe |
| **Underlying Asset Class** | Credit (portfolio of 100+ reference entities via CDS) |
| **Capital Protection** | Tranche-dependent (senior protected by subordination, equity tranche = first loss) |
| **Coupon Type** | Fixed or floating (varies by tranche seniority) |
| **Maturity Profile** | 5–7 years |
| **Liquidity Profile** | OTC — model-dependent, index tranches more liquid |
| **Primary Buyer** | Banks (regulatory capital relief), hedge funds (leveraged credit), insurance (yield on senior tranches) |
| **Primary Risk** | Portfolio credit losses reaching tranche attachment point. Equity tranche = first loss. Senior tranche = protected but catastrophic loss scenario |
| **Primary Hedge** | Index CDS, single-name CDS, correlation trading (base correlation) |
| **Primary System** | NEMO (primary), Sophis (risk) |
| **ISDA Required** | Yes — ISDA Credit Definitions (unfunded tranches) |
| **One-Line Summary** | Redistribute portfolio credit losses across seniority layers to match different risk appetites |

**Remember These 3 Things:**

1. CDS portfolio + tranching waterfall (attachment/detachment points) + copula dependency model
2. Key risk: Portfolio credit losses reaching tranche attachment point
3. Watch: Base correlation

---

### 5.6.1 — Structured Deposit (SD)

| Field | Value |
|-------|-------|
| **Product Name** | Structured Deposit |
| **Abbreviation** | SD |
| **Family** | Other |
| **Complexity Score** | 2 / 10 |
| **Complexity Rationale** | PPN mechanics (2) in deposit wrapper. No additional structural features |
| **Underlying Asset Class** | Equity index, single stock, FX, commodity (most commonly equity index) |
| **Capital Protection** | Full (100%). Deposit insurance where available + bank guarantee |
| **Coupon Type** | None — return is variable participation at maturity |
| **Maturity Profile** | Typically 1-3 years (shorter than PPN due to deposit format) |
| **Liquidity Profile** | Maturity only. Early withdrawal may forfeit variable return |
| **Primary Buyer** | Retail, mass affluent |
| **Primary Risk** | Opportunity cost (zero return in flat/down markets) |
| **Primary Hedge** | Delta-hedge (futures/options on underlying) |
| **Primary System** | Murex (equity-linked) |
| **ISDA Required** | No — deposit agreement, not derivative documentation |
| **One-Line Summary** | Replace savings allocation with market-linked upside |

**Remember These 3 Things:**

1. Deposit + Call Option
2. Key risk: Opportunity cost (zero return in flat/down markets)
3. Watch: Vega

---

### 5.6.2 — Forward Contract (FWD)

| Field | Value |
|-------|-------|
| **Product Name** | Forward Contract |
| **Abbreviation** | FWD |
| **Family** | Other |
| **Complexity Score** | 2 / 10 |
| **Complexity Rationale** | Linear payoff. No optionality. No barriers. Single settlement. Foundation derivative |
| **Underlying Asset Class** | Any: equity, FX, commodity, interest rate, credit |
| **Capital Protection** | None — linear exposure in both directions |
| **Coupon Type** | None |
| **Maturity Profile** | Typically 1 month to 2 years. Can be longer for specific hedging needs |
| **Liquidity Profile** | OTC — negotiated unwind with counterparty |
| **Primary Buyer** | Corporates (hedging), institutional investors (asset allocation) |
| **Primary Risk** | Adverse price movement (linear, unlimited in both directions) |
| **Primary Hedge** | Offsetting forward, or underlying + funding position |
| **Primary System** | Murex |
| **ISDA Required** | Yes — OTC derivative |
| **One-Line Summary** | Lock in future purchase/sale price |

**Remember These 3 Things:**

1. Forward = agreement to exchange asset for cash at future date
2. Key risk: Adverse price movement (linear, unlimited in both directions)
3. Watch: Forward points (cost of carry drives forward price vs spot)

---

### 5.6.3 — Vanilla Option (Call / Put) (VO)

| Field | Value |
|-------|-------|
| **Product Name** | Vanilla Option (Call / Put) |
| **Abbreviation** | VO |
| **Family** | Other |
| **Complexity Score** | 3 / 10 |
| **Complexity Rationale** | Single strike, single expiry, no exotic features. One step above Forward (adds optionality) |
| **Underlying Asset Class** | Any: equity, FX, commodity, interest rate |
| **Capital Protection** | Long option: max loss = premium. Short option: unlimited potential loss |
| **Coupon Type** | None |
| **Maturity Profile** | 1 week to 5+ years. Most liquid: 1-12 months |
| **Liquidity Profile** | Exchange-traded: high. OTC: negotiated |
| **Primary Buyer** | Hedgers (corporates, funds), speculators, structured product desks (as building block) |
| **Primary Risk** | Premium loss (long), unlimited loss (short) |
| **Primary Hedge** | Delta-hedge (underlying), gamma management (re-hedging frequency) |
| **Primary System** | Murex |
| **ISDA Required** | OTC: Yes. Exchange-traded: No (exchange rules govern) |
| **One-Line Summary** | Hedge directional risk, express view with limited risk, earn premium income |

**Remember These 3 Things:**

1. Option = asymmetric payoff
2. Key risk: Premium loss (long), unlimited loss (short)
3. Watch: Gamma (non-linear exposure requires frequent re-hedging)

---

### 5.6.4 — Equity-Linked Option (ELO)

| Field | Value |
|-------|-------|
| **Product Name** | Equity-Linked Option |
| **Abbreviation** | ELO |
| **Family** | Other |
| **Complexity Score** | 3 / 10 |
| **Complexity Rationale** | Same as vanilla option (3). No additional structural features beyond packaging |
| **Underlying Asset Class** | Single equity (most common), equity index, basket |
| **Capital Protection** | None — max loss is premium paid |
| **Coupon Type** | None |
| **Maturity Profile** | Typically 6 months to 2 years |
| **Liquidity Profile** | Limited — early redemption at bank's discretion, typically at bid price |
| **Primary Buyer** | Retail, mass affluent, private banking clients |
| **Primary Risk** | Total loss of premium if underlying does not move favorably |
| **Primary Hedge** | Delta-hedge (underlying shares or futures) |
| **Primary System** | Murex |
| **ISDA Required** | No — product wrapper with term sheet |
| **One-Line Summary** | Directional bet with defined maximum loss |

**Remember These 3 Things:**

1. Long call option (most common) or long put option
2. Key risk: Total loss of premium if underlying does not move favorably
3. Watch: Theta (time decay erodes option value daily)

---

### 5.6.5 — Option on Reverse Convertible (Opt-on-RC)

| Field | Value |
|-------|-------|
| **Product Name** | Option on Reverse Convertible |
| **Abbreviation** | Opt-on-RC |
| **Family** | Other |
| **Complexity Score** | 5 / 10 |
| **Complexity Rationale** | Two-layer structure: option (3) on RC (3). Combined complexity exceeds individual layers. Requires understanding of both option mechanics and RC mechanics |
| **Underlying Asset Class** | Single equity or equity index (the RC's underlying) |
| **Capital Protection** | During option period: max loss = premium. After exercise (in RC): barrier-dependent protection |
| **Coupon Type** | None during option period. Fixed coupon after exercise (RC coupon) |
| **Maturity Profile** | Option period: 1-6 months. RC period: 6-18 months after exercise |
| **Liquidity Profile** | Very limited. Two-layer structure makes early exit complex |
| **Primary Buyer** | Sophisticated retail, private banking, institutional (yield hunters with timing views) |
| **Primary Risk** | Premium loss (if not exercised) or conversion risk (if exercised into RC) |
| **Primary Hedge** | Compound option Greeks — delta-hedge requires option-on-option modeling |
| **Primary System** | Murex |
| **ISDA Required** | Yes — OTC derivative |
| **One-Line Summary** | Defer RC entry while locking in terms during uncertain markets |

**Remember These 3 Things:**

1. Call option on an RC (which itself = Bond + Short Put)
2. Key risk: Premium loss (if not exercised) or conversion risk (if exercised into RC)
3. Watch: Delta of outer option

---

### 5.6.6 — Accumulator (ACCUM)

| Field | Value |
|-------|-------|
| **Product Name** | Accumulator |
| **Abbreviation** | ACCUM |
| **Family** | Other |
| **Complexity Score** | 6 / 10 |
| **Complexity Rationale** | Periodic accumulation (4), knock-out (1), gearing below strike (1). Path-dependent. Multiple observation dates. Leveraged downside |
| **Underlying Asset Class** | Single equity (most common), equity index, FX |
| **Capital Protection** | None — unlimited downside with gearing |
| **Coupon Type** | None — the "income" is the discount on shares purchased |
| **Maturity Profile** | Typically 6-12 months |
| **Liquidity Profile** | Very limited — OTC, difficult to unwind |
| **Primary Buyer** | High-net-worth private banking clients, institutional (equity desk clients) |
| **Primary Risk** | Leveraged loss in falling market (double accumulation below strike) |
| **Primary Hedge** | Daily forward hedging + barrier hedging (digital risk near KO) |
| **Primary System** | Murex |
| **ISDA Required** | Yes — OTC derivative |
| **One-Line Summary** | Build equity position at guaranteed discount |

**Remember These 3 Things:**

1. Strip of daily/weekly forward purchases + knock-out + gearing
2. Key risk: Leveraged loss in falling market (double accumulation below strike)
3. Watch: Gearing ratio (2x accumulation below strike is the defining risk)

---

### 5.6.7 — Decumulator (DECUM)

| Field | Value |
|-------|-------|
| **Product Name** | Decumulator |
| **Abbreviation** | DECUM |
| **Family** | Other |
| **Complexity Score** | 6 / 10 |
| **Complexity Rationale** | Mirror of Accumulator (6). Same mechanisms reversed: periodic selling, knock-out (down), gearing (up) |
| **Underlying Asset Class** | Single equity (most common), equity index, FX |
| **Capital Protection** | None — opportunity cost if stock rises significantly with gearing |
| **Coupon Type** | None — the "income" is the premium on shares sold |
| **Maturity Profile** | Typically 6-12 months |
| **Liquidity Profile** | Very limited — OTC, difficult to unwind |
| **Primary Buyer** | Founders, insiders, funds reducing positions, corporates divesting |
| **Primary Risk** | Opportunity cost + geared selling in rising market |
| **Primary Hedge** | Daily forward hedging + barrier hedging |
| **Primary System** | Murex |
| **ISDA Required** | Yes — OTC derivative |
| **One-Line Summary** | Orderly share disposal at guaranteed premium |

**Remember These 3 Things:**

1. Strip of daily/weekly forward sales + knock-out + gearing
2. Key risk: Opportunity cost + geared selling in rising market
3. Watch: Gearing ratio (accelerated selling in rising market)

---

### 5.6.8 — Dual Currency Investment (DCI)

| Field | Value |
|-------|-------|
| **Product Name** | Dual Currency Investment |
| **Abbreviation** | DCI |
| **Family** | Other |
| **Complexity Score** | 3 / 10 |
| **Complexity Rationale** | Deposit + single FX option. One strike, one observation. Simple two-currency mechanics |
| **Underlying Asset Class** | Foreign Exchange (currency pair) |
| **Capital Protection** | Full in base currency if FX stays above strike. Nominal in alternate currency if converted |
| **Coupon Type** | Fixed enhanced coupon (above-market deposit rate) |
| **Maturity Profile** | Typically 1 week to 3 months. Rarely beyond 6 months |
| **Liquidity Profile** | Held to maturity. Early termination possible with penalty |
| **Primary Buyer** | Private banking clients, corporate treasurers with multi-currency operations |
| **Primary Risk** | Currency conversion — principal returned in weaker currency |
| **Primary Hedge** | Long FX put option in same currency pair and strike |
| **Primary System** | Murex (FX options desk) |
| **ISDA Required** | No — structured as deposit, not OTC derivative |
| **One-Line Summary** | Yield enhancement on short-term deposits |

**Remember These 3 Things:**

1. Time deposit + short FX put option (on base currency vs alternate currency)
2. Key risk: Currency conversion — principal returned in weaker currency
3. Watch: FX strike distance (conversion trigger proximity)

---

### 5.6.9 — Shark Fin Note (Knock-Out Capital Protected Note) (SHRK)

| Field | Value |
|-------|-------|
| **Product Name** | Shark Fin Note (Knock-Out Capital Protected Note) |
| **Abbreviation** | SHRK |
| **Family** | Other |
| **Complexity Score** | 4 / 10 |
| **Complexity Rationale** | Capital protected + single up-and-out barrier. One barrier, one rebate level. PPN variant with barrier mechanic |
| **Underlying Asset Class** | Equity index (most common), single stock, commodity |
| **Capital Protection** | 100% at maturity (principal guaranteed) |
| **Coupon Type** | None — return delivered as participation in underlying at maturity |
| **Maturity Profile** | Typically 1-3 years |
| **Liquidity Profile** | Secondary market with bid-offer spread. Less liquid than standard PPN |
| **Primary Buyer** | Conservative private banking clients seeking capital-protected equity exposure with enhanced participation |
| **Primary Risk** | Barrier breach caps the return at rebate level. Opportunity cost if underlying surges |
| **Primary Hedge** | Long up-and-out call replication via dynamic barrier hedging |
| **Primary System** | Murex |
| **ISDA Required** | No — issued as note (securities law) |
| **One-Line Summary** | Capital-protected equity participation with higher participation rate than vanilla PPN |

**Remember These 3 Things:**

1. Zero-coupon bond + up-and-in call spread (or: long call + short up-and-out call with rebate)
2. Key risk: Barrier breach caps the return at rebate level
3. Watch: Barrier distance (knock-out proximity caps return)

---

### 5.6.10 — Snowball Autocallable Note (SNOW)

| Field | Value |
|-------|-------|
| **Product Name** | Snowball Autocallable Note |
| **Abbreviation** | SNOW |
| **Family** | Other |
| **Complexity Score** | 7 / 10 |
| **Complexity Rationale** | Autocall + conditional coupon + cumulative accumulation. Path-dependent — coupon amount depends on entire history of missed coupons. Multiple observation dates |
| **Underlying Asset Class** | Equity index (CSI 300, KOSPI most common), single stock |
| **Capital Protection** | Conditional — protected if no knock-in barrier breach. At risk if barrier breached and underlying below strike at maturity |
| **Coupon Type** | Conditional cumulative (snowball accumulation) |
| **Maturity Profile** | Typically 1-2 years |
| **Liquidity Profile** | OTC — limited secondary market |
| **Primary Buyer** | Yield-seeking private banking clients (Asia-Pacific), institutional investors with recovery views |
| **Primary Risk** | Knock-in barrier breach + underlying below strike at maturity = capital loss. Accumulation creates "all-or-nothing" coupon dynamic |
| **Primary Hedge** | Dynamic delta hedging + vol surface management + autocall probability modelling |
| **Primary System** | Murex |
| **ISDA Required** | Yes (OTC derivative) or No (note format, depending on jurisdiction) |
| **One-Line Summary** | Earn accumulated missed coupons when underlying recovers — the snowball pays all at once |

**Remember These 3 Things:**

1. Autocallable note + cumulative coupon counter + knock-in put (capital risk)
2. Key risk: Knock-in barrier breach + underlying below strike at maturity = capital loss
3. Watch: Autocall probability + cumulative coupon counter

---

### 5.6.11 — Cliquet Note (Ratchet Note) (CLIQ)

| Field | Value |
|-------|-------|
| **Product Name** | Cliquet Note (Ratchet Note) |
| **Abbreviation** | CLIQ |
| **Family** | Other |
| **Complexity Score** | 7 / 10 |
| **Complexity Rationale** | Serial forward-starting options. Multiple reset periods. Local + global caps/floors. Path-dependent — total return depends on sequence of periodic returns |
| **Underlying Asset Class** | Equity index (most common), single stock |
| **Capital Protection** | Typically 100% (funded by zero-coupon bond) |
| **Coupon Type** | None — return delivered as sum of periodic locked-in returns |
| **Maturity Profile** | Typically 3-5 years |
| **Liquidity Profile** | Secondary market with spread. Model-dependent pricing |
| **Primary Buyer** | Insurance-linked structured products, conservative private banking, institutional investors with path-sensitive mandates |
| **Primary Risk** | Local caps limit upside in trending markets. Global floor prevents loss but caps total return. Opportunity cost in strong bull markets |
| **Primary Hedge** | Strip of forward-starting options, repriced at each reset. Vol surface risk across the term structure |
| **Primary System** | Murex |
| **ISDA Required** | No — issued as note (securities law) |
| **One-Line Summary** | Capital-protected equity participation with periodic lock-in of gains |

**Remember These 3 Things:**

1. Zero-coupon bond + strip of forward-starting call options (each with local cap) + global floor/cap on total
2. Key risk: Local caps limit upside in trending markets
3. Watch: Vega

---

### 5.6.12 — Worst-of Autocallable Note (Worst-of Phoenix) (WOAC)

| Field | Value |
|-------|-------|
| **Product Name** | Worst-of Autocallable Note (Worst-of Phoenix) |
| **Abbreviation** | WOAC |
| **Family** | Other |
| **Complexity Score** | 8 / 10 |
| **Complexity Rationale** | Phoenix mechanics applied to multi-asset basket. Correlation-dependent pricing. Worst-of observation across 3-5 stocks. Quanto adjustment for cross-listed baskets. All Phoenix complexity plus correlation dimension |
| **Underlying Asset Class** | Basket of 3-5 equities (single stocks, occasionally indices) |
| **Capital Protection** | Conditional — protected if worst-of stock stays above knock-in barrier |
| **Coupon Type** | Conditional periodic (paid if worst-of stock above coupon barrier). May include memory feature |
| **Maturity Profile** | Typically 1-3 years |
| **Liquidity Profile** | OTC — secondary market with model-dependent pricing |
| **Primary Buyer** | Yield-seeking private banking and retail investors globally |
| **Primary Risk** | Worst-performing stock drives all outcomes. Low correlation increases risk of at least one stock breaching barrier. Capital loss if barrier breached and worst-of below strike at maturity |
| **Primary Hedge** | Basket option replication. Delta hedging each stock. Correlation exposure hedged via dispersion trades or basket vs single-stock vol |
| **Primary System** | Murex |
| **ISDA Required** | Yes (OTC derivative) or No (note format, jurisdiction-dependent) |
| **One-Line Summary** | Earn higher yield by taking worst-performer risk across a basket of 3-5 stocks |

**Remember These 3 Things:**

1. Autocallable note (Phoenix mechanics) + worst-of observation on basket + knock-in put on worst performer
2. Key risk: Worst-performing stock drives all outcomes
3. Watch: Correlation

---

## Appendix A: Family Summary

| Family | Code | Count | Anchor Product | Complexity Range | Typical Asset Class |
|--------|:----:|:-----:|---------------|:----------------:|---------------------|
| Equity-Linked Notes | ELN | 15 | Principal Protected Note (5.1.1) | 2–7 | Equity (single stock or index) |
| Swaps | Swaps | 8 | Interest Rate Swap (5.2.1) | 2–7 | Rates |
| Structured Rate Trades | SRT | 5 | IR Callable Fixed Rate Swap (5.3.1) | 4–7 | Rates (SOFR / EURIBOR) |
| Steepener Notes | STEG | 4 | Vanilla Steepener Note (5.4.1) | 5–8 | Rates (CMS30Y − CMS2Y spread) |
| Credit-Linked Notes | CLN | 5 | Vanilla Credit-Linked Note (5.5.1) | 4–10 | Credit (basket of 5–10 reference entities) |
| Other | Other | 12 | Structured Deposit (5.6.1) | 2–8 | Single equity (most common), equity index, FX |

### Family Descriptions

**Equity-Linked Notes:** Note-format products with embedded equity derivatives. Investor typically sells optionality (puts, barriers) in exchange for enhanced yield or protection. Issued as securities — no ISDA needed.

**Swaps:** Bilateral OTC derivatives exchanging cash flow streams. Counterparty risk is primary credit concern. ISDA/CSA required. Used for hedging, basis trading, and synthetic exposure.

**Structured Rate Trades:** Rate-linked structured products combining bonds with interest rate derivatives. Range from simple zero-coupon linked notes to callable range accruals. Bridge between vanilla rates and exotic structures.

**Steepener Notes:** Notes paying coupons linked to the yield curve slope (typically CMS30 – CMS2). Investor expresses a view that the curve stays steep. Complexity increases with range accrual, callability, and target features.

**Credit-Linked Notes:** Funded credit derivatives where the investor sells credit protection via a note wrapper. Range from single-name CLNs to synthetic CDO tranches. Credit correlation is the defining risk for basket products.

**Other:** Diverse product group including deposits, forwards, options, accumulators, and exotic equity structures. Catchall for products that do not fit neatly into the five primary families.

---

## Appendix B: Complexity Distribution

### Score Distribution

| Score | Count | Products |
|:-----:|:-----:|----------|
| 1 | 0 | — |
| 2 | 4 | PPN, VLSP, SD, FWD |
| 3 | 8 | RC, DRC, ICN, Warrant, IRS, VO, ELO, DCI |
| 4 | 9 | KODRC, Airbag, Bonus, Digital, Booster, CommSwap, ZCL, CLN, SHRK |
| 5 | 10 | CRC, TRS, EqSwap, CDS, XCCY, IR Callable, Digital CF, Vanilla STEG, Skew CLN, Opt-on-RC |
| 6 | 7 | Phoenix, FCN, CRA ELN, NCRA, Callable STEG, ACCUM, DECUM |
| 7 | 7 | DKIP, VarSwap, CRA SRT, RA STEG, FTD, SNOW, CLIQ |
| 8 | 3 | TARN STEG, NTD, WOAC |
| 9 | 0 | — |
| 10 | 1 | CDO |

### Tier Distribution

| Tier | Range | Count | % |
|------|:-----:|:-----:|:-:|
| Vanilla (1–2) | 1–2 | 4 | 8% |
| Standard (3–4) | 3–4 | 17 | 35% |
| Moderate (5–6) | 5–6 | 17 | 35% |
| Complex (7–8) | 7–8 | 10 | 20% |
| Highly Complex (9–10) | 9–10 | 1 | 2% |

### Distribution by Family

| Family | 1-2 | 3-4 | 5-6 | 7-8 | 9-10 | Mean |
|--------|:---:|:---:|:---:|:---:|:----:|:----:|
| ELN | 1 | 9 | 4 | 1 | 0 | 4.3 |
| Swaps | 1 | 2 | 4 | 1 | 0 | 4.5 |
| SRT | 0 | 1 | 3 | 1 | 0 | 5.4 |
| STEG | 0 | 0 | 2 | 2 | 0 | 6.5 |
| CLN | 0 | 1 | 1 | 2 | 1 | 6.8 |
| Other | 2 | 4 | 3 | 3 | 0 | 4.7 |

---

## Appendix C: Product Evolution Summary

### Family Evolution Chains

#### Equity-Linked Notes

| From | To | Evolution |
|------|-----|-----------|
| PPN (5.1.1) | RC (5.1.2) | Add short put, remove ZCB protection |
| RC (5.1.2) | Phoenix (5.1.3) | Add autocall + memory coupon |
| RC (5.1.2) | DRC (5.1.4) | Replace coupon with purchase discount |
| RC (5.1.2) | KODRC (5.1.5) | Add knock-out barrier |
| RC (5.1.2) | CRC (5.1.6) | Add issuer call right |
| RC (5.1.2) | Airbag (5.1.7) | Replace linear loss with leveraged loss below barrier |
| RC (5.1.2) | Bonus (5.1.8) | Replace coupon with conditional participation |
| Phoenix (5.1.3) | FCN (5.1.9) | Fix coupon, remove memory feature |
| RC (5.1.2) | CRA ELN (5.1.10) | Replace fixed coupon with range accrual |
| RC (5.1.2) | ICN (5.1.11) | Remove equity link, add issuer call |
| RC (5.1.2) | Digital (5.1.12) | Replace fixed coupon with digital coupon |
| PPN (5.1.1) | Booster (5.1.13) | Add leverage to upside participation |
| Digital (5.1.12) | DKIP (5.1.14) | Add knock-in put to digital |
| PPN (5.1.1) | Warrant (5.1.15) | Remove ZCB, pure leveraged option |

#### Swaps

| From | To | Evolution |
|------|-----|-----------|
| IRS (5.2.1) | TRS (5.2.2) | Swap rate for total asset return |
| TRS (5.2.2) | EqSwap (5.2.3) | Specialize to equity returns |
| IRS (5.2.1) | VarSwap (5.2.4) | Swap rate for realized variance |
| IRS (5.2.1) | CDS (5.2.5) | Swap rate for credit protection |
| IRS (5.2.1) | XCCY (5.2.6) | Add cross-currency principal exchange |
| IRS (5.2.1) | CommSwap (5.2.7) | Swap rate for commodity price |
| IRS (5.2.1) | VLSP (5.2.8) | Simplest rate swap variant |

#### Structured Rate Trades

| From | To | Evolution |
|------|-----|-----------|
| IR Callable (5.3.1) | ZCL (5.3.2) | Strip coupons, link to rate |
| IR Callable (5.3.1) | NCRA (5.3.3) | Add range accrual condition |
| NCRA (5.3.3) | CRA SRT (5.3.4) | Add callability to range accrual |
| IR Callable (5.3.1) | Digital CF (5.3.5) | Digital rate-linked coupon |

#### Steepener Notes

| From | To | Evolution |
|------|-----|-----------|
| Vanilla STEG (5.4.1) | RA STEG (5.4.2) | Add range accrual condition |
| Vanilla STEG (5.4.1) | Callable STEG (5.4.3) | Add issuer call right |
| Vanilla STEG (5.4.1) | TARN STEG (5.4.4) | Add target auto-redemption |

#### Credit-Linked Notes

| From | To | Evolution |
|------|-----|-----------|
| CLN (5.5.1) | Skew CLN (5.5.2) | Modify recovery assumption |
| CLN (5.5.1) | FTD (5.5.3) | Expand to basket, first default |
| FTD (5.5.3) | NTD (5.5.4) | Change trigger from 1st to Nth default |
| FTD (5.5.3) | CDO (5.5.5) | Expand to portfolio, add tranching |

#### Other

| From | To | Evolution |
|------|-----|-----------|
| SD (5.6.1) | ELO (5.6.4) | Add equity-linked option wrapper |
| FWD (5.6.2) | ACCUM (5.6.6) | Repeat forward over multiple dates |
| VO (5.6.3) | ELO (5.6.4) | Wrap option in retail format |
| RC (5.1.2) | Opt-on-RC (5.6.5) | Add option layer on top of RC |
| ACCUM (5.6.6) | DECUM (5.6.7) | Reverse direction (sell, not buy) |
| RC (5.1.2) | DCI (5.6.8) | Apply RC logic to FX, deposit wrapper |
| PPN (5.1.1) | SHRK (5.6.9) | Add knock-out barrier to PPN |
| Phoenix (5.1.3) | SNOW (5.6.10) | Accumulate missed coupons |
| PPN (5.1.1) | CLIQ (5.6.11) | Lock in periodic returns |
| Phoenix (5.1.3) | WOAC (5.6.12) | Replace single stock with worst-of basket |

### Complexity Progression Within Families

**ELN:** PPN(2) → RC(3) → DRC(3) → ICN(3) → Warrant(3) → KODRC(4) → Airbag(4) → Bonus(4) → Digital(4) → Booster(4) → CRC(5) → Phoenix(6) → FCN(6) → CRA ELN(6) → DKIP(7)

**Swaps:** VLSP(2) → IRS(3) → CommSwap(4) → TRS(5) → EqSwap(5) → CDS(5) → XCCY(5) → VarSwap(7)

**SRT:** ZCL(4) → IR Callable(5) → Digital CF(5) → NCRA(6) → CRA SRT(7)

**STEG:** Vanilla STEG(5) → Callable STEG(6) → RA STEG(7) → TARN STEG(8)

**CLN:** CLN(4) → Skew CLN(5) → FTD(7) → NTD(8) → CDO(10)

**Other:** SD(2) → FWD(2) → VO(3) → ELO(3) → DCI(3) → SHRK(4) → Opt-on-RC(5) → ACCUM(6) → DECUM(6) → SNOW(7) → CLIQ(7) → WOAC(8)

---

## Appendix D: Top Desk Risk Metrics

A quick-reference glossary of the risk metrics that appear in "Watch" fields across the 49 DNA cards. Each entry explains what the metric is, why traders watch it, and which products it matters most for.

### Greek Sensitivities

| # | Metric | What It Is | Why Traders Watch It | Key Products |
|:-:|--------|-----------|---------------------|-------------|
| 1 | **Delta** | Change in product value for a 1-unit move in the underlying. Measures directional exposure. | First-order hedge ratio — tells you how many shares/contracts to hold to be market-neutral. | All equity-linked, FX-linked, commodity-linked products |
| 2 | **Gamma** | Rate of change of delta. Measures how quickly your hedge becomes wrong as the underlying moves. | High gamma near barriers means hedge ratio changes rapidly — expensive to re-hedge. Barrier products have gamma spikes. | KODRC, Bonus, DKIP, Vanilla Option (near expiry) |
| 3 | **Vega** | Change in product value for a 1% move in implied volatility. | Vol moves can dwarf delta P&L for long-dated or optionality-rich products. Callables are short vega (bank sold swaption). | CRC, ICN, IR Callable, CRA SRT, Callable STEG, VarSwap, Cliquet, SD |
| 4 | **Theta** | Daily time-decay of option value. Measures how much value an option loses each day. | Long option holders bleed theta daily. Short sellers earn it. Accelerates near expiry. | Warrant, ELO, Vanilla Option |
| 5 | **Rho** | Change in product value for a 1bp move in interest rates. | For products with a zero-coupon bond component, rate changes affect the ZCB value and therefore the available option budget. Higher rates = more option budget = higher participation. | PPN, Shark Fin, Cliquet, ZCL |

### Rate-Specific Metrics

| # | Metric | What It Is | Why Traders Watch It | Key Products |
|:-:|--------|-----------|---------------------|-------------|
| 6 | **DV01 (Dollar Value of a Basis Point)** | Dollar change in value for a 1bp parallel shift in the yield curve. Also called "duration dollar." | Primary rate risk measure for swaps and bonds. Tells you how much money you make or lose per basis point. | IRS, VLSP, ZCL, XCCY |
| 7 | **CMS Spread Delta** | Sensitivity to the slope of the swap curve (CMS30Y minus CMS2Y). A 1bp change in the spread changes the coupon and product value. | Steepener coupons are directly linked to this spread. Flattening kills the coupon. Inversion makes it zero. | Vanilla STEG, RA STEG, Callable STEG, TARN STEG |
| 8 | **Digital Gamma** | Gamma spike at the digital strike where the coupon flips from full to zero (or vice versa). Near the strike, a tiny move causes a huge P&L swing. | The defining hedging challenge for range accruals and digital products. Near the strike, the desk must hedge a discontinuous payoff — like hedging a cliff edge. | CRA ELN, Digital Coupon Note, NCRA, CRA SRT, Digital CF, RA STEG |
| 9 | **Forward Points** | Difference between forward price and spot price, driven by interest rate differential (cost of carry). | For forwards, the forward point IS the product — it tells you the premium or discount for future delivery. Changes as rate differentials shift. | Forward Contract, Accumulator, Decumulator |

### Credit Metrics

| # | Metric | What It Is | Why Traders Watch It | Key Products |
|:-:|--------|-----------|---------------------|-------------|
| 10 | **Credit Spread Delta** | Change in value for a 1bp move in the reference entity's CDS spread. Measures credit sensitivity. | Widening spreads signal deteriorating credit — protection buyers profit, protection sellers lose. Jump-to-default risk for sudden events. | CDS, CLN, Skew CLN, FTD, NTD |
| 11 | **Recovery Delta** | Sensitivity to the assumed recovery rate in a credit event. If actual recovery differs from assumed, the payout changes. | Skew CLNs pay based on recovery rate distribution, not just default/no-default. Recovery assumption directly drives the product's value. | Skew CLN |
| 12 | **Base Correlation** | Implied correlation across a credit portfolio, extracted from tranche prices. Drives the relative value of senior vs equity tranches. | Low correlation = equity tranche risk high, senior tranche safe. High correlation = losses cluster, senior tranche at risk. The single most important input for CDO pricing. | Synthetic CDO Tranche |
| 13 | **Correlation** | Degree to which basket constituents move together. For worst-of products, low correlation increases the chance that at least one stock breaches the barrier. | Correlation is the hidden risk in basket products — it cannot be observed directly, only implied from market prices. Mis-estimating it is the primary model risk. | WOAC, FTD, NTD |

### Product-Specific Metrics

| # | Metric | What It Is | Why Traders Watch It | Key Products |
|:-:|--------|-----------|---------------------|-------------|
| 14 | **Autocall Probability** | Estimated likelihood that the product will terminate early at the next observation date. Derived from underlying's distance to autocall trigger. | Determines expected product life, coupon count, and hedging horizon. High autocall probability = short-dated hedge; low = must hedge to maturity. | Phoenix, FCN, Snowball, WOAC |
| 15 | **Barrier Distance** | Current underlying level expressed as percentage distance from the knock-in or knock-out barrier. | Closer to barrier = higher gamma, more expensive hedging, higher risk of regime change (protected → exposed or capped). | KODRC, FCN, Shark Fin, Snowball, WOAC |
| 16 | **Participation Rate** | Percentage of underlying's return that the investor receives (e.g., 150% participation = 1.5x equity return). | Drives the value proposition for capital-protected products. Set at inception based on available option budget (driven by rates and vol). | PPN, Booster, Shark Fin, Cliquet |
| 17 | **Gearing Ratio** | Multiplier applied to accumulation or selling below/above strike. Typically 2x — investor buys/sells double the normal amount in adverse scenarios. | The defining risk feature of accumulators/decumulators. Turns a moderate decline into a severe obligation. | Accumulator, Decumulator |
| 18 | **Funding Spread** | The spread over the reference rate (SOFR + Xbps) charged on the funded leg of a swap. Determines the carry cost of synthetic exposure. | Changes in funding spread directly affect the economics of synthetic ownership. If spread widens, TRS becomes more expensive for the receiver. | TRS, Equity Swap |
| 19 | **FX Strike Distance** | Current spot rate expressed as percentage distance from the DCI conversion strike. | Closer to strike = higher conversion probability. In DCI, crossing the strike means principal returned in the weaker currency. | DCI |

---

## Appendix E: Common Interview Questions

One question per product. Each question tests deep understanding of the product's core mechanic. Derive your answer from the DNA card — answers are not provided intentionally.

### Equity-Linked Notes

| Section | Product | Most Common Interview Question |
|---------|---------|-------------------------------|
| 5.1.1 | PPN | Why doesn't the investor receive full equity upside if principal is guaranteed? |
| 5.1.2 | RC | If the coupon is above-market, what is the investor giving up in return? |
| 5.1.3 | Phoenix | Why does a Phoenix autocall early when the investor is making money? |
| 5.1.4 | DRC | How does buying at a discount change the risk profile versus a standard RC? |
| 5.1.5 | KODRC | What happens at the exact moment the barrier is breached? |
| 5.1.6 | CRC | Why does the bank call when the product is performing well for the investor? |
| 5.1.7 | Airbag | Where does the money for the leveraged upside come from? |
| 5.1.8 | Bonus | What happens to the bonus if the barrier is breached by 0.01% on one day? |
| 5.1.9 | FCN | Why would an investor accept conditional principal return for a coupon they would receive anyway? |
| 5.1.10 | CRA ELN | What happens to the coupon if the underlying leaves the range for one day out of ninety? |
| 5.1.11 | ICN | Who benefits from the call option — the investor or the bank? |
| 5.1.12 | Digital | What makes the hedging cost spike when the underlying is near the digital strike? |
| 5.1.13 | Booster | If participation is 200%, why does the product have a cap? |
| 5.1.14 | DKIP | How does combining a digital coupon with a knock-in put create dual conditional risk? |
| 5.1.15 | Warrant | Why does time decay accelerate as expiry approaches? |

### Swaps

| Section | Product | Most Common Interview Question |
|---------|---------|-------------------------------|
| 5.2.1 | IRS | If both legs have the same present value at inception, how does anyone make money? |
| 5.2.2 | TRS | Why would an investor pay a funding spread to own returns they could get by buying the asset directly? |
| 5.2.3 | EqSwap | How does dividend risk affect the swap's economics differently for each leg? |
| 5.2.4 | VarSwap | Why is a long variance position more dangerous than a long volatility position? |
| 5.2.5 | CDS | If CDS spreads widen but no default occurs, who makes money? |
| 5.2.6 | XCCY | Why does the cross-currency basis exist if covered interest rate parity should eliminate it? |
| 5.2.7 | CommSwap | What is the difference between hedging with a swap versus hedging with futures? |
| 5.2.8 | VLSP | When would a corporate choose a VLSP over a standard IRS? |

### Structured Rate Trades

| Section | Product | Most Common Interview Question |
|---------|---------|-------------------------------|
| 5.3.1 | IR Callable | Why is the enhanced coupon higher than a vanilla swap rate? |
| 5.3.2 | ZCL | Why would a pension fund prefer a zero-coupon structure over a coupon-paying bond? |
| 5.3.3 | NCRA | If the investor keeps the principal regardless, why is the product risky? |
| 5.3.4 | CRA SRT | What two risks is the investor selling simultaneously? |
| 5.3.5 | Digital CF | What happens to the hedge when rates are exactly at the digital strike? |

### Steepener Notes

| Section | Product | Most Common Interview Question |
|---------|---------|-------------------------------|
| 5.4.1 | Vanilla STEG | What market scenario would cause the coupon to drop to zero? |
| 5.4.2 | RA STEG | Why does this product require TWO conditions to be met simultaneously? |
| 5.4.3 | Callable STEG | In what interest rate environment would the bank exercise the call? |
| 5.4.4 | TARN STEG | Is early termination good or bad for the investor? |

### Credit-Linked Notes

| Section | Product | Most Common Interview Question |
|---------|---------|-------------------------------|
| 5.5.1 | CLN | Why does the investor face dual credit risk (reference entity AND issuer)? |
| 5.5.2 | Skew CLN | How does the actual recovery rate affect the payout differently than in a vanilla CLN? |
| 5.5.3 | FTD | Why does low correlation INCREASE the risk for an FTD investor? |
| 5.5.4 | NTD | Why does high correlation INCREASE the risk for an NTD investor (opposite of FTD)? |
| 5.5.5 | CDO | Why is correlation more important than default probability for equity tranche pricing? |

### Other

| Section | Product | Most Common Interview Question |
|---------|---------|-------------------------------|
| 5.6.1 | SD | Why would a client accept zero return in a down market instead of keeping money in cash? |
| 5.6.2 | FWD | If both parties agree on the forward price, why does anyone enter into the trade? |
| 5.6.3 | VO | Why does an option seller face unlimited risk while the buyer's risk is capped? |
| 5.6.4 | ELO | How does the retail wrapper change the economics compared to a vanilla option? |
| 5.6.5 | Opt-on-RC | What are the TWO decision points the investor faces during the product's life? |
| 5.6.6 | ACCUM | Why is the product sometimes called "I'll be back" in Asia? |
| 5.6.7 | DECUM | When would a corporate founder use this instead of simply selling shares on the market? |
| 5.6.8 | DCI | What determines whether the investor receives their principal in the base or alternate currency? |
| 5.6.9 | SHRK | Why would an investor accept a return cap on a capital-protected product? |
| 5.6.10 | SNOW | What happens to the coupon if the underlying recovers after missing three consecutive payments? |
| 5.6.11 | CLIQ | Why do local caps make this product underperform in a strong bull market? |
| 5.6.12 | WOAC | Why does the worst-performing stock drive the entire outcome even if the other four stocks are up? |

---

## Appendix F: Product Confusion Pairs

Products frequently confused with each other. For each pair: why they are confused, and the single key difference.

### Within-Family Pairs

| # | Product A | Product B | Why People Confuse Them | Key Difference |
|:-:|-----------|-----------|------------------------|----------------|
| 1 | PPN (5.1.1) | RC (5.1.2) | Both are ELNs with equity exposure | PPN buys protection (ZCB guarantees principal). RC sells protection (short put exposes principal). |
| 2 | RC (5.1.2) | DRC (5.1.4) | Both are yield-enhanced with put exposure | RC pays above-market coupon. DRC replaces coupon with purchase discount (lower entry price). |
| 3 | RC (5.1.2) | CRC (5.1.6) | Both are reverse convertibles | CRC adds bank call right — higher coupon but bank terminates when product favours investor. |
| 4 | DRC (5.1.4) | KODRC (5.1.5) | Both are discounted reverse convertibles | KODRC adds knock-out barrier — investor is protected unless barrier is breached. |
| 5 | Phoenix (5.1.3) | FCN (5.1.9) | Both are autocallable with periodic observation | Phoenix coupon is conditional (paid only if above coupon barrier). FCN coupon is guaranteed regardless. |
| 6 | Phoenix (5.1.3) | SNOW (5.6.10) | Both have autocall + conditional coupon | SNOW accumulates missed coupons (snowball effect). Phoenix does not — missed coupons are lost (unless memory). |
| 7 | Phoenix (5.1.3) | WOAC (5.6.12) | Both have autocall + barrier + conditional coupon | WOAC applies worst-of observation across basket of 3-5 stocks. Phoenix is single-asset. |
| 8 | CRA ELN (5.1.10) | Digital (5.1.12) | Both have conditional equity-linked coupons | CRA accrues proportionally (days in range / total days). Digital is all-or-nothing per observation. |
| 9 | VO (5.6.3) | Warrant (5.1.15) | Both are options on equity | VO is OTC or exchange-traded. Warrant is exchange-listed, standardised, retail-accessible. |
| 10 | VO (5.6.3) | ELO (5.6.4) | Same economic exposure | ELO is retail-wrapped VO with term sheet instead of ISDA. Packaging differs, not payoff. |
| 11 | ACCUM (5.6.6) | DECUM (5.6.7) | Mirror structures with identical mechanics | ACCUM buys shares at discount (bullish). DECUM sells shares at premium (exit strategy). |
| 12 | IRS (5.2.1) | VLSP (5.2.8) | Both are interest rate swaps | VLSP adds features (caps, floors, amortisation, step-ups) beyond vanilla IRS. |
| 13 | TRS (5.2.2) | EqSwap (5.2.3) | Both swap asset returns for funding rate | EqSwap is equity-specific TRS. TRS covers multi-asset (equity, credit, loans). |
| 14 | NCRA (5.3.3) | CRA SRT (5.3.4) | Both are range accrual rate products | CRA SRT adds callability — higher coupon but bank can terminate early. |
| 15 | Vanilla STEG (5.4.1) | Callable STEG (5.4.3) | Both are CMS spread steepener notes | Callable adds bank call right — higher coupon, reinvestment risk. |
| 16 | FTD (5.5.3) | NTD (5.5.4) | Both are basket credit default notes | FTD triggers on FIRST default. NTD triggers on Nth. Correlation effect reverses between them. |
| 17 | CLN (5.5.1) | CDS (5.2.5) | Both transfer credit risk of reference entity | CLN is funded (investor buys note, cash at risk). CDS is unfunded (swap, no upfront cash). |

### Cross-Family Pairs

| # | Product A | Product B | Why People Confuse Them | Key Difference |
|:-:|-----------|-----------|------------------------|----------------|
| 18 | PPN (5.1.1) | SD (5.6.1) | Both are capital-protected equity participation | SD is deposit (deposit insurance applies). PPN is note (issuer credit risk, no deposit insurance). |
| 19 | PPN (5.1.1) | SHRK (5.6.9) | Both are capital-protected equity notes | SHRK has knock-out barrier — higher participation rate but return is capped if barrier breached. |
| 20 | PPN (5.1.1) | CLIQ (5.6.11) | Both are capital-protected equity participation | CLIQ locks in periodic returns (ratchet). PPN measures total return at maturity only. |
| 21 | RC (5.1.2) | DCI (5.6.8) | Both sell option for yield enhancement | RC sells equity put. DCI sells FX put. Same mechanic, different asset class. |
| 22 | IR Callable (5.3.1) | CRC (5.1.6) | Both have bank call right for enhanced coupon | IR Callable is rate product (embedded swaption). CRC is equity product (embedded put + Bermudan call). |
| 23 | Digital (5.1.12) | Digital CF (5.3.5) | Both have digital (binary) coupon mechanics | Digital is equity-linked. Digital CF is rate-linked. Same payoff structure, different underlying. |
| 24 | CDO (5.5.5) | FTD (5.5.3) | Both are multi-name credit products | FTD is 5-10 names with binary first-default trigger. CDO is 100+ names with tranched loss waterfall. |
| 25 | Booster (5.1.13) | Warrant (5.1.15) | Both offer leveraged equity exposure | Booster has leverage on upside with a cap. Warrant is pure leveraged option with no cap but total loss risk. |

---

## Appendix G: What Makes This Product Difficult?

One conceptual barrier per product. Focus: where you will get stuck when learning, not operational complexity.

### Vanilla (1–2)

| Section | Product | What Makes This Product Difficult? |
|---------|---------|-----------------------------------|
| 5.1.1 | PPN | Understanding why participation rate is below 100% — the "cost" of capital protection is reduced upside. |
| 5.2.8 | VLSP | Identifying which additional feature (cap, floor, amortisation) changes the risk profile and by how much versus vanilla IRS. |
| 5.6.1 | SD | Understanding why "full capital protection" still carries opportunity cost — zero return in flat/down markets is the price. |
| 5.6.2 | FWD | Understanding that both sides can lose unlimited amounts — there is no asymmetry in a forward, unlike an option. |

### Standard (3–4)

| Section | Product | What Makes This Product Difficult? |
|---------|---------|-----------------------------------|
| 5.1.2 | RC | Understanding that the above-market coupon is payment for taking equity downside risk via a short put. |
| 5.1.4 | DRC | Calculating the adjusted break-even and comparing it to RC break-even — the discount changes the conversion math. |
| 5.1.5 | KODRC | Understanding the discontinuity at the barrier — fully protected one penny above, fully exposed one penny below. |
| 5.1.7 | Airbag | Understanding leverage asymmetry: amplified upside above strike, cushioned zone between strike and barrier, then full loss below barrier. |
| 5.1.8 | Bonus | Understanding that barrier observation is typically continuous — one bad intraday print can eliminate the entire bonus. |
| 5.1.11 | ICN | Distinguishing issuer call right from autocall trigger — different mechanics, similar economic outcome for the investor. |
| 5.1.12 | Digital | Understanding digital gamma near the strike — the hedging cost spike that makes this product expensive to manage. |
| 5.1.13 | Booster | Understanding that leverage works both ways but only the upside is capped — the asymmetry is against the investor. |
| 5.1.15 | Warrant | Understanding leverage erosion: time decay and delta decay compound in adverse moves, accelerating near expiry. |
| 5.2.1 | IRS | Understanding that "no principal at risk" does not mean "no risk" — MTM exposure on long-dated swaps can be very large. |
| 5.2.7 | CommSwap | Understanding basis risk: the swap references a benchmark price, not the client's actual commodity grade or location. |
| 5.3.2 | ZCL | Understanding duration sensitivity: a 30-year ZCB moves roughly 30x more per basis point than a 1-year bond. |
| 5.5.1 | CLN | Understanding dual credit exposure: both the reference entity AND the note issuer can cause principal loss. |
| 5.6.3 | VO | Understanding put-call parity and why selling options has fundamentally different risk from buying options. |
| 5.6.4 | ELO | Recognizing that the retail wrapper does not change the embedded option's economics — same Greeks, different packaging. |
| 5.6.8 | DCI | Understanding that "enhanced deposit rate" is funded by selling an FX put — the currency conversion risk IS the yield source. |
| 5.6.9 | SHRK | Understanding that the knock-out barrier LIMITS returns in the best scenario — strong rallies are capped at the rebate level. |

### Moderate (5–6)

| Section | Product | What Makes This Product Difficult? |
|---------|---------|-----------------------------------|
| 5.1.3 | Phoenix | Understanding how autocall probability and barrier interaction create opposing incentives for bank and investor. |
| 5.1.6 | CRC | Understanding that selling the call right to the bank means giving up optionality in the best scenario. |
| 5.1.9 | FCN | Understanding why guaranteed coupon does NOT mean guaranteed principal — the coupon-barrier disconnect. |
| 5.1.10 | CRA ELN | Understanding daily digital accrual: one day outside the range reduces coupon by 1/N of the period. |
| 5.2.2 | TRS | Understanding funding mechanics: why "synthetic ownership" costs more than direct ownership due to the funding spread. |
| 5.2.3 | EqSwap | Understanding dividend pass-through: which leg bears realised vs expected dividend risk and how it affects swap value. |
| 5.2.5 | CDS | Understanding basis risk between CDS spread and bond spread — they should converge but often don't (negative basis). |
| 5.2.6 | XCCY | Understanding cross-currency basis: why interest rate parity fails in practice and what the basis represents. |
| 5.3.1 | IR Callable | Understanding embedded swaption valuation: the "extra coupon" is exactly the swaption premium amortised over the note's life. |
| 5.3.3 | NCRA | Understanding that 100% capital protection does not protect coupon income — you can earn zero coupon for 10 years and still get principal back. |
| 5.3.5 | Digital CF | Understanding the interaction between rate level (determines coupon) and rate volatility (determines hedging cost). |
| 5.4.1 | Vanilla STEG | Understanding CMS convexity adjustment: why the CMS rate does not equal the forward rate and what drives the difference. |
| 5.4.3 | Callable STEG | Understanding dual optionality: curve must steepen for coupon AND bank must not exercise call — two conditions competing. |
| 5.5.2 | Skew CLN | Understanding how recovery rate distribution (not just default/no-default) drives the payoff — a new dimension beyond vanilla CLN. |
| 5.6.5 | Opt-on-RC | Understanding compound optionality: the option premium reflects BOTH the outer option AND the RC's embedded put risk. |
| 5.6.6 | ACCUM | Understanding gearing asymmetry: buying 1x above strike vs 2x below strike — the risk is not symmetric. |
| 5.6.7 | DECUM | Understanding that the "guaranteed premium" is funded by gearing in adverse moves — the mirror of accumulator risk. |

### Complex (7–8)

| Section | Product | What Makes This Product Difficult? |
|---------|---------|-----------------------------------|
| 5.1.14 | DKIP | Understanding dual conditional risk: digital coupon depends on one level, capital depends on another — two separate barriers. |
| 5.2.4 | VarSwap | Understanding why variance (not volatility) is convex and how small spot moves create disproportionate P&L for long positions. |
| 5.3.4 | CRA SRT | Understanding the interaction between range accrual condition and callability — two embedded options with competing dynamics. |
| 5.4.2 | RA STEG | Understanding that TWO conditions must be simultaneously met: curve steep enough for coupon AND reference rate in range for accrual. |
| 5.4.4 | TARN STEG | Understanding why early termination (which sounds good) is actually reinvestment risk — the product terminates in the best scenario. |
| 5.5.3 | FTD | Understanding basket default correlation: low correlation = diverse portfolio = higher chance of at least one default triggering loss. |
| 5.5.4 | NTD | Understanding correlation reversal: high correlation INCREASES NTD risk — the opposite of FTD. This is the single hardest credit concept. |
| 5.6.10 | SNOW | Understanding snowball accumulation: missed coupons compound, creating an all-or-nothing dynamic when the underlying finally recovers. |
| 5.6.11 | CLIQ | Understanding serial forward-starting options: each reset changes the reference level, and local caps limit returns in trending markets. |
| 5.6.12 | WOAC | Understanding that adding more stocks to the basket INCREASES risk — more chances for one stock to underperform and drive the outcome. |

### Highly Complex (9–10)

| Section | Product | What Makes This Product Difficult? |
|---------|---------|-----------------------------------|
| 5.5.5 | CDO | Understanding how correlation drives tranche loss allocation: equity tranche wants dispersed defaults, senior tranche wants clustered defaults. Base correlation replaced compound correlation after the 2008 crisis because the old model broke. |

---

*Product DNA Atlas — 49 products, 3 views, 7 appendices. Generated 2026-06-22. Frozen 2026-06-22.*