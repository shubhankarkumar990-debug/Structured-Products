# Desk Bible v2 — Table of Contents

**Design Date:** 2026-06-19
**Design Principle:** Teach from first principles, progress toward desk-level understanding.
**Mix:** 40% Training Manual / 30% Desk Handbook / 20% Operational Guide / 10% Product Encyclopedia

---

## PART 1 — FOUNDATIONS (Training Manual)

*Prerequisite reading. No structured products knowledge assumed.*

### 1.1 Core Trading Concepts
- Long vs Short
- Bid, Offer, Spread
- Price vs Value vs Mark-to-Market
- P&L basics
- Carry and Funding
- Leverage
- Liquidity

### 1.2 Options From Zero
- What is an option
- Calls and Puts
- In-the-Money / At-the-Money / Out-of-the-Money
- European vs American vs Bermudan exercise
- Intrinsic value vs Time value
- Payoff diagrams (visual)

### 1.3 Barriers and Digitals
- Knock-In barriers
- Knock-Out barriers
- European vs American barrier observation
- Digital / Binary payoffs
- Why barriers matter for structured products

### 1.4 Greeks — How Risk Is Measured
- Delta (directional exposure)
- Gamma (how Delta changes)
- Vega (volatility sensitivity)
- Theta (time decay)
- Rho (rate sensitivity)
- Convexity
- Linear vs Non-Linear payoffs

### 1.5 Volatility
- Implied vs Realized
- Volatility term structure
- Volatility skew and smile
- Why clients consistently misprice volatility

### 1.6 Correlation and Baskets
- What correlation means
- Worst-of / Best-of payoffs
- Why correlation drives structured product pricing
- Tail risk

### 1.7 Rates and Yield Curves
- What a yield curve is
- Spot vs Forward rates
- SOFR, EURIBOR, and benchmark rates
- CMS (Constant Maturity Swap) rates
- Caps, Floors, and Swaptions

### 1.8 Credit Risk
- Credit spread
- Recovery rate
- Credit Default Swaps — the fundamentals
- Credit events (ISDA taxonomy)
- Model risk

**Estimated length:** 30–40 pages
**Estimated reading time:** 1.5–2 hours

---

## PART 2 — STRUCTURED PRODUCTS FRAMEWORK (Training Manual + Desk Handbook)

*How structured products are built, traded, and managed.*

### 2.1 What Is a Structured Product
- Definition
- Why structured products exist
- The risk transfer concept: what clients think they buy vs what the desk sells
- Asymmetry: the unifying theme

### 2.2 Product Construction Principles
- Bond + Option = Structured Product
- Decomposition: how to break any structure into primitives
- Issuer credit curve and funding
- Funds Transfer Pricing (FTP)
- Desk margin

### 2.3 The Four-Leg Framework
- Note Leg — what the client sees
- Issuer Leg — the bank's liability
- Deposit Leg — internal funding
- Hedge Leg — what the trader actually does
- How P&L flows across legs
- Worked example: what flows where

### 2.4 Capital Protection Spectrum
- Full protection (principal guaranteed)
- Conditional protection (barrier-dependent)
- Zero protection (full downside exposure)
- How protection level drives coupon

### 2.5 Product Lifecycle
- Origination and structuring
- Pricing and termsheet
- Trade booking
- Observations (coupons, barriers, autocalls)
- Maturity or early redemption
- Post-trade events (corporate actions, fixing disruptions)

### 2.6 Trade Lifecycle
- Front office: pricing, execution
- Middle office: booking, confirmation
- Risk: daily mark-to-market, Greeks
- Operations: fixing, payments, settlements
- Product Control: reconciliation, P&L

### 2.7 How Desks Hedge
- ELN hedging (Delta, Gamma, Vega)
- Rates hedging (duration, convexity)
- Credit hedging (CDS, index)
- Why hedging is continuous, not static
- What happens in stress

**Estimated length:** 20–25 pages
**Estimated reading time:** 1–1.5 hours

---

## PART 3 — PRODUCT TAXONOMY (Desk Handbook)

*Classification framework. Read before deep dives.*

### 3.1 Product Family Overview
- Equity-Linked Notes (ELN)
- Credit-Linked Notes (CLN)
- Swaps
- Structured Rate Trades (SRT)
- Steepener Notes (STEG)
- Structured Deposits
- Other Products (Accumulators, Forwards, Options)

### 3.2 Product Classification Dimensions
- By underlying (equity, credit, rates, FX, commodity)
- By coupon type (fixed, conditional, accrual, none)
- By capital protection (full, conditional, zero)
- By optionality (autocall, callable, knockout)
- By complexity (simple → complex)
- By booking system (NEMO/Sophis vs Murex)

### 3.3 ELN Family Tree
- Reverse Convertible variants (RC, DRC, KODRC, CRC, Airbag)
- Autocallable variants (Phoenix, FCN, Range Accrual)
- Other ELNs (Bonus, PPN, Warrant, ICN, Digital, Booster)

### 3.4 CLN Family Tree
- Single-name (Vanilla CLN, Skew CLN)
- Basket (FTD, NTD)
- Portfolio (Synthetic Tranche)

### 3.5 Swaps Family Tree
- Interest Rate Swap
- Total Return Swap
- Equity Swap
- Cross-Currency Swap
- Commodity Swap
- Credit Default Swap

### 3.6 SRT Family Tree
- Callable (IR Callable, Callable Range Accrual)
- Non-Callable (Non-Callable Range Accrual)
- Accreting (Zero Coupon Linear)
- Digital (Cap-Floor)

### 3.7 STEG Family Tree
- Vanilla Steepener
- Range-Accrual Steepener
- Callable Steepener
- TARN Steepener

**Estimated length:** 10–15 pages
**Estimated reading time:** 30–45 minutes

---

## PART 4 — PRODUCT COMPARISON MATRICES (Desk Handbook + Quick Reference)

*Side-by-side comparison tables. The fastest way to understand differences.*

### 4.1 ELN Master Comparison Matrix
Columns: Product, Coupon Type, Barrier, Autocall, Capital Protection, Put Type, Underlying, Primary Greeks, Booking System, Typical Client, Complexity

### 4.2 Reverse Convertible Variant Comparison
What changes between RC → DRC → KODRC → CRC → Airbag

### 4.3 Autocallable Variant Comparison
Phoenix vs FCN vs Callable Range Accrual ELN

### 4.4 CLN Family Comparison
Vanilla → Skew → FTD → NTD → Tranche: correlation exposure, reference type, loss mechanics

### 4.5 STEG Family Comparison
Vanilla → Range Accrual → Callable → TARN: coupon mechanics, optionality, path dependency

### 4.6 SRT Family Comparison
Callable vs non-callable, accreting vs fixed, digital vs vanilla

### 4.7 Swaps Comparison Matrix
IRS vs TRS vs Equity vs Currency vs Commodity vs CDS: what is exchanged, settlement, collateral

### 4.8 Cross-Family Comparisons
- ELN vs SRT: risk profile, system mapping, coupon source
- SRT vs STEG: rate reference, booking framework
- All products by risk profile (short vol, long vol, short correlation)
- All products by capital protection level
- All products by booking system

**Estimated length:** 15–20 pages (primarily tables)
**Estimated reading time:** 30–45 minutes (reference, not linear reading)

---

## PART 5 — PRODUCT DEEP DIVES (Product Encyclopedia, condensed)

*3–5 pages per product maximum. Structured for desk use, not academic reference.*

### Section Structure Per Product (standardized):
1. **What It Is** (2–3 sentences, plain English)
2. **Why Clients Buy It** (bullet list)
3. **Payoff Logic** (what happens at maturity — good/bad scenario, one paragraph)
4. **Construction** (component list, not prose)
5. **Key Risks** (3–5 bullets, ranked by severity)
6. **Booking** (system, key fields — one paragraph, referencing Part 6)
7. **Reconciliation Red Flags** (product-specific risks only — referencing Part 6 for common risks)
8. **Worked Example** (tabular format where possible)
9. **Desk Shorthand** (one line, italic)

### 5.1 Equity-Linked Notes
- 5.1.1 Reverse Convertible
- 5.1.2 Discounted Reverse Convertible
- 5.1.3 Knock-Out Discounted RC
- 5.1.4 Callable Reverse Convertible
- 5.1.5 Airbag / Leveraged RC
- 5.1.6 Phoenix Autocallable
- 5.1.7 Fixed Coupon Note (FCN)
- 5.1.8 Callable Range Accrual ELN
- 5.1.9 Bonus / Participation Note
- 5.1.10 Principal Protected Note
- 5.1.11 Warrant / Turbo Certificate
- 5.1.12 Issuer Callable Note
- 5.1.13 Digital Coupon Notes
- 5.1.14 Booster Note (NEW)
- 5.1.15 Digital Coupon Knock-In Put (NEW)

### 5.2 Credit-Linked Notes
- 5.2.1 Vanilla CLN
- 5.2.2 Skew CLN
- 5.2.3 First-to-Default
- 5.2.4 Nth-to-Default
- 5.2.5 Synthetic CDO Tranche

### 5.3 Swaps
- 5.3.1 Interest Rate Swap
- 5.3.2 Total Return Swap (NEW)
- 5.3.3 Equity Swap (NEW)
- 5.3.4 Cross-Currency Swap (NEW)
- 5.3.5 Commodity Swap (NEW)
- 5.3.6 Credit Default Swap (NEW)
- 5.3.7 Vanilla Swap — VLSP (NEW)

### 5.4 Structured Rate Trades
- 5.4.1 IR Callable Fixed Rate Note
- 5.4.2 IR Accreting Callable Swap / Zero Coupon Linear (EXPANDED)
- 5.4.3 Non-Callable Range Accrual
- 5.4.4 Callable Range Accrual
- 5.4.5 Digital Cap-Floor

### 5.5 Steepener Notes
- 5.5.1 Vanilla Steepener
- 5.5.2 Range-Accrual Steepener
- 5.5.3 Callable Steepener
- 5.5.4 TARN Steepener

### 5.6 Other Products
- 5.6.1 Structured Deposits (NEW)
- 5.6.2 Accumulators / Decumulators (NEW)
- 5.6.3 Option on Risk Control (NEW)
- 5.6.4 Equity Linked Option (NEW)
- 5.6.5 Forwards (NEW)

**Estimated length:** 120–160 pages (3–4 pages × ~42 products)
**Estimated reading time:** Product-by-product reference, not sequential reading

---

## PART 6 — OPERATIONS (Operational Guide)

*Centralized. Read once, referenced from every product.*

### 6.1 Systems Overview
- NEMO: what it does, what it carries, key fields
- Sophis: what it does, how it prices, key outputs
- Murex: what it does, the four-leg framework, key instruments
- When each system is used (routing rules by product family)

### 6.2 Booking Flows
- ELN booking flow (NEMO + Sophis)
- SRT/STEG booking flow (Murex four-leg)
- CLN booking flow (NEMO + Sophis)
- Swap booking flow
- End-to-end: from termsheet to live position

### 6.3 Lifecycle Events
- Coupon payments
- Barrier observations
- Autocall events
- Call events (issuer-initiated)
- Maturity settlement
- Corporate actions

### 6.4 Product Control and Reconciliation
- Common reconciliation risks (centralized — not repeated per product):
  - Strike: percentage vs absolute price
  - Fixing source: exchange close vs Bloomberg composite
  - Settlement type: physical vs cash
  - Observation convention: European vs American, discrete vs continuous
  - Day count: 30/360 vs actual/365
  - Boundary treatment: at-barrier in-range or out-of-range
  - Coupon on early redemption: full period vs pro-rata
- Product-specific reconciliation risks (reference table)
- Daily reconciliation checklist

### 6.5 Fixing and Observation Conventions
- Fixing sources
- Disrupted day fallbacks
- Business day calendars
- Non-business-day adjustment conventions

### 6.6 Settlement
- Physical delivery mechanics
- Cash settlement mechanics
- Settlement timing (T+N conventions)

**Estimated length:** 20–25 pages
**Estimated reading time:** 1 hour

---

## PART 7 — QUICK REFERENCE GUIDE (Desk Handbook)

*One-page-per-question format. Lookup, not reading.*

### 7.1 Product Attribute Lookups
- Which products are short volatility?
- Which products are long volatility?
- Which products are short correlation?
- Which products are autocallable?
- Which products have barriers?
- Which products are capital protected?
- Which products pay fixed coupons?
- Which products pay conditional coupons?
- Which products have memory features?

### 7.2 System Routing
- Which products use NEMO?
- Which products use Sophis?
- Which products use Murex?
- Which products use four-leg booking?

### 7.3 Risk Lookups
- Dominant Greeks by product
- Barrier proximity risks
- Highest operational risk products
- Highest model risk products

### 7.4 Complexity Ranking
- Simple (closed-form, 1–2 components)
- Medium (Monte Carlo, 3–4 components)
- Complex (path-dependent, multi-observation, correlation)

### 7.5 Desk Shorthand Index
- All products with their one-line desk shorthand

**Estimated length:** 10–15 pages
**Estimated reading time:** Reference only

---

## PART 8 — APPENDICES

### Appendix A — Glossary
- All abbreviations (ISDA, MTN, FTP, CMS, CDS, CDX, LHP, etc.)
- All technical terms used in the document
- Arranged alphabetically

### Appendix B — System Maps
- NEMO field reference
- Sophis model reference
- Murex leg structure reference

### Appendix C — Product Maps
- Product taxonomy tree (visual)
- Product-to-family mapping
- Product-to-section cross-reference

### Appendix D — Booking Maps
- Per-family booking field checklists
- Critical field reference (fields that cause breaks if wrong)

### Appendix E — Reference Tables
- Worked termsheet: Phoenix Autocallable (from COMPLETE.docx Appendix A)
- Booking field reference (from COMPLETE.docx Appendix B)
- Common decomposition formulas

### Appendix F — Reading Paths
- New Joiner: Parts 1 → 2 → 3 → 4 → selected deep dives
- Product Control: Parts 6 → 4 → 7 → selected deep dives
- Risk: Parts 1.4–1.6 → 2.7 → 4 → selected deep dives
- Trader: Parts 4 → 5 → 7

**Estimated length:** 15–20 pages
**Estimated reading time:** Reference only

---

## Document Totals

| Part | Pages | Type |
|------|:-----:|------|
| Part 1 — Foundations | 30–40 | Training Manual |
| Part 2 — Framework | 20–25 | Training Manual + Handbook |
| Part 3 — Taxonomy | 10–15 | Desk Handbook |
| Part 4 — Comparisons | 15–20 | Desk Handbook |
| Part 5 — Deep Dives | 120–160 | Product Encyclopedia |
| Part 6 — Operations | 20–25 | Operational Guide |
| Part 7 — Quick Reference | 10–15 | Desk Handbook |
| Part 8 — Appendices | 15–20 | Reference |
| **Total** | **240–320** | |

**Estimated total reading time (cover-to-cover):** 8–12 hours
**Estimated time to desk proficiency (targeted path):** 3–4 hours
