# Desk Bible v2 — Final Curriculum Design

**Date:** 2026-06-19
**Status:** APPROVED — incorporates all findings from curriculum review and final amendment.

---

## Governing Rules

1. **No Unexplained Terminology Rule** — A reader must never encounter a term not already explained.
2. **Why Before How Rule** — Explain why something exists before how it works.
3. **Cognitive Load Rule** — Build mental models, not information dumps. Reinforce before advancing.
4. **Progressive Disclosure Rule** — Teach in layers: intuition → analogy → example → explanation → terminology → advanced.
5. **Feynman Test** — Every section must be understandable by a motivated teenager.
6. **Story First Rule** — Introduce concepts through stories whenever possible.
7. **Why Do I Care Rule** — Every chapter answers why this matters to clients, traders, risk, operations, P&L.
8. **Visual Learning Rule** — Prefer diagrams, flowcharts, tables, timelines over prose whenever possible.

---

## Final Structure

### PART 0 — HOW FINANCE WORKS (20-25 pages)

| Section | Title | Key Concepts | Teaching Method |
|---------|-------|-------------|-----------------|
| 0.1 | What Is a Financial Market? | Buyers, sellers, price discovery, exchanges, OTC | Story: village marketplace → stock exchange |
| 0.2 | Why Companies Need Capital | Growth, expansion, operations funding | Story: bakery opening a second location |
| 0.3 | Debt vs Equity | Lending vs ownership, bonds vs stocks, risk/return tradeoff | Analogy: lending to a friend vs investing in their business |
| 0.4 | Risk and Return | Uncertainty, compensation for risk, spectrum | Analogy: savings account vs startup investment |
| 0.5 | What Is Interest? | Price of borrowing, simple/compound, rates | Story: lending money to a friend for a year |
| 0.6 | Time Value of Money | Present value, discounting, compounding, why a dollar today > dollar tomorrow | Example: would you rather have $100 today or $100 next year? |
| 0.7 | What Banks Actually Do | Commercial vs investment banking, advisory, underwriting, trading | Map: the bank as an ecosystem |
| 0.8 | What Is a Derivative? | Contract whose value depends on something else, three types (futures, options, swaps) | Analogy: derivative = side bet on a football game |
| 0.9 | Why Derivatives Were Invented | Hedging uncertainty | Stories: farmer/baker, airline/fuel, exporter/FX |
| 0.10 | Why Structured Products Exist | Income, protection, leverage, yield enhancement | Story: pension fund seeking income with protection |
| 0.11 | The Investment Banking Ecosystem | Sales, Trading, Structuring, Research, Risk, Compliance | Diagram: who talks to whom |
| 0.12 | Front Office vs Middle Office vs Back Office | Revenue generation vs risk control vs processing | Analogy: restaurant (kitchen/manager/dishwasher) |

**Knowledge Check:** 5 review + 3 scenario + 1 practical question

**Terminology introduced in Part 0:** market, security, stock, bond, share, equity, debt, principal, interest, coupon, yield, maturity, risk, return, present value, discount, compound, bank, investment bank, derivative, futures, option, swap, hedge, structured product, notional, front office, middle office, back office, sales, trading, structuring, risk management, product control, operations.

---

### PART 1 — FOUNDATIONS (40-50 pages)

| Section | Title | Key Concepts | Prerequisites (all from Part 0) |
|---------|-------|-------------|-------------------------------|
| 1.1 | Core Trading Concepts | Long/short, bid/offer/spread, P&L, mark-to-market, leverage, liquidity, carry | Market, security, risk, return |
| 1.2 | Options From Zero | Calls, puts, premium, strike, exercise, expiry, moneyness (ITM/ATM/OTM), exercise styles, intrinsic/time value, how to read a payoff diagram | Derivative, long/short, stock, bond |
| 1.3 | Barriers and Digitals | Knock-in, knock-out, European/American observation, digital/binary payoffs, why barriers matter for SP | Options, payoff diagrams |
| 1.4 | Greeks — How Risk Is Measured | Delta, gamma, vega, theta, rho, convexity, linear vs non-linear | Options, P&L, risk |
| 1.5 | Volatility | Implied vs realized, term structure, skew/smile, variance, why clients misprice vol | Options, Greeks (vega), risk |
| 1.6 | Correlation and Baskets | What correlation means, worst-of/best-of, why correlation drives SP pricing, tail risk | Volatility, options, risk |
| — | *[Bridge: From Equity to Rates]* | Transition paragraph | — |
| 1.7 | Rates and Yield Curves | What a yield curve is, spot/forward rates, SOFR/EURIBOR, CMS rates, caps/floors/swaptions, swap concept revisited | Interest, time value of money, derivative |
| 1.8 | Credit Risk | Credit spread, recovery rate, CDS basics, credit events (ISDA), model risk | Bond, interest, risk, derivative |

**Knowledge Check:** 5 review + 3 scenario + 1 practical question (per major section group)

**Terminology introduced in Part 1:** long, short, bid, offer, spread, P&L, mark-to-market, leverage, liquidity, carry, funding, call, put, option, premium, strike price, exercise, expiry, in-the-money, at-the-money, out-of-the-money, European, American, Bermudan, intrinsic value, time value, payoff diagram, breakeven, barrier, knock-in, knock-out, digital, binary, delta, gamma, vega, theta, rho, convexity, linear, non-linear, implied volatility, realized volatility, volatility term structure, skew, smile, variance, correlation, worst-of, best-of, basket, tail risk, yield curve, spot rate, forward rate, SOFR, EURIBOR, LIBOR, CMS, cap, floor, swaption, credit spread, recovery rate, CDS, credit event, ISDA, bankruptcy, failure to pay, restructuring, model risk.

---

### PART 2 — STRUCTURED PRODUCTS FRAMEWORK (25-30 pages)

| Section | Title |
|---------|-------|
| 2.1 | What Is a Structured Product |
| 2.2 | Product Construction Principles (Bond + Option decomposition, FTP, desk margin) |
| 2.3 | The Four-Leg Framework (Note/Issuer/Deposit/Hedge) |
| 2.4 | Capital Protection Spectrum |
| 2.5 | Product Lifecycle |
| 2.6 | Trade Lifecycle |
| 2.7 | How Desks Hedge |
| 2.8 | The Systems: A First Look (NEMO, Sophis, Murex primer) |

**Knowledge Check:** 5 review + 3 scenario + 1 practical question

**New terminology introduced:** structured product, note, issuer, SPV, MTN, FTP, desk margin, four-leg framework, note leg, issuer leg, deposit leg, hedge leg, termsheet, autocall, memory feature, NEMO, Sophis, Murex, book of record, pricing engine.

---

### PART 3 — PRODUCT TAXONOMY (10-15 pages)

| Section | Title |
|---------|-------|
| 3.1 | Product Family Overview |
| 3.2 | Classification Dimensions (underlying, coupon, protection, optionality, complexity, system) |
| 3.3 | ELN Family Tree |
| 3.4 | Swaps Family Tree |
| 3.5 | SRT Family Tree |
| 3.6 | STEG Family Tree |
| 3.7 | CLN Family Tree |
| 3.8 | Other Products |

---

### PART 4 — PRODUCT COMPARISON MATRICES (15-20 pages)

| Section | Title |
|---------|-------|
| 4.1 | ELN Master Comparison Matrix |
| 4.2 | Reverse Convertible Variant Comparison |
| 4.3 | Autocallable Variant Comparison |
| 4.4 | Swaps Comparison Matrix |
| 4.5 | SRT Family Comparison |
| 4.6 | STEG Family Comparison |
| 4.7 | CLN Family Comparison |
| 4.8 | Cross-Family Comparisons |

---

### PART 5 — PRODUCT DEEP DIVES (250-280 pages)

**Family ordering (revised per curriculum review):**

| Order | Family | Product Count | Rationale |
|:-----:|--------|:------------:|-----------|
| 5.1 | Equity-Linked Notes | 15 | Most intuitive. Familiar underlying. |
| 5.2 | Swaps | 8 | Required before SRT, STEG, and CLN. |
| 5.3 | Structured Rate Trades | 5 | Built on IRS from 5.2. |
| 5.4 | Steepener Notes | 4 | Built on CMS from 5.3. |
| 5.5 | Credit-Linked Notes | 5 | Built on CDS from 5.2. |
| 5.6 | Other Products | 7 | Miscellaneous. |

**ELN ordering (revised — progressive complexity):**

1. Principal Protected Note (simplest — no downside)
2. Reverse Convertible (core — introduces barrier risk)
3. Discounted Reverse Convertible (+discount)
4. Knock-Out Discounted RC (+KO barrier)
5. Callable Reverse Convertible (+issuer call)
6. Airbag / Leveraged RC (+leverage below barrier)
7. Bonus / Participation Note (different structure — upside participation)
8. Fixed Coupon Note / FCN (introduces autocall — simpler version)
9. Phoenix Autocallable (adds conditionality and memory to autocall)
10. Callable Range Accrual ELN (cross-family — accrual + equity)
11. Issuer Callable Note (pure callable)
12. Digital Coupon Notes (digital payoff)
13. Booster Note (leveraged upside)
14. Digital Coupon Knock-In Put (digital + barrier — most complex)
15. Warrant / Turbo Certificate (standalone option exposure)

**Swaps (8 products):**
1. Interest Rate Swap
2. Total Return Swap
3. Equity Swap
4. Variance Swap (NEW — added per directive)
5. Currency Swap
6. Commodity Swap
7. Credit Default Swap
8. Vanilla Swap (VLSP)

**SRT (5 products):** IR Callable Fixed Rate Swap, IR Accreting Callable / ZCL, Non-Callable Range Accrual, Callable Range Accrual, Digital Cap-Floor

**STEG (4 products):** Vanilla Steepener, Range-Accrual Steepener, Callable Steepener, TARN Steepener

**CLN (5 products):** Vanilla CLN, Skew CLN, First-to-Default, Nth-to-Default, Synthetic CDO Tranche

**Other (7 products):** Structured Deposits, Accumulators, Decumulators, Option on Risk Control, Equity Linked Option, Forwards, Vanilla Options

**Total: 49 products**

**16-section product chapter template:**
1. Explain Like I'm New
2. Real World Analogy
3. What Problem Does This Solve?
4. Why Clients Buy It
5. What Happens If... (4 scenarios)
6. Formal Definition
7. Product Construction
8. Payoff Logic
9. Key Risks
10. Booking and Operations
11. Reconciliation Red Flags
12. Worked Example
13. Interview Questions
14. Mental Models
15. Key Takeaways
16. Common Mistakes

---

### PART 6 — OPERATIONS (25-30 pages)

| Section | Title |
|---------|-------|
| 6.1 | Systems Overview (NEMO, Sophis, Murex — full detail) |
| 6.2 | Booking Flows (ELN, SRT/STEG, CLN, Swap) |
| 6.3 | Lifecycle Events |
| 6.4 | Product Control and Reconciliation |
| 6.5 | Fixing and Observation Conventions |
| 6.6 | Settlement |

---

### PART 7 — QUICK REFERENCE (15-20 pages)

| Section | Title |
|---------|-------|
| 7.1 | Glossary |
| 7.2 | Acronym Dictionary |
| 7.3 | Product Cheat Sheets |
| 7.4 | Decision Trees |
| 7.5 | Common Interview Questions |
| 7.6 | System Routing Guides |
| 7.7 | Desk Shorthand Index |
| 7.8 | Reading Paths by Role |

---

## Totals

| Part | Pages |
|------|:-----:|
| Part 0 — How Finance Works | 20–25 |
| Part 1 — Foundations | 40–50 |
| Part 2 — Framework | 25–30 |
| Part 3 — Taxonomy | 10–15 |
| Part 4 — Comparisons | 15–20 |
| Part 5 — Deep Dives (49 products) | 250–280 |
| Part 6 — Operations | 25–30 |
| Part 7 — Quick Reference | 15–20 |
| **Total** | **400–470** |
