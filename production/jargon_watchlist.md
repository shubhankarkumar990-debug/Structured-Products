# Jargon Watchlist

**Version:** 1.0
**Date:** 2026-06-19
**Purpose:** Supplementary terminology watchlist for the Jargon Police Agent. These terms are known to slip through without definition during chapter generation. Every term on this list must be either (a) defined with a parenthetical on first use in the chapter, or (b) listed in the Dependency References table with a pointer to where it was taught.

---

## 1. Operational Terms (High Risk)

These terms are used in §10 (Booking and Operations) and §11 (Reconciliation Red Flags) and are frequently left undefined.

| Term | Risk Level | Required Definition or Parenthetical |
|------|:----------:|--------------------------------------|
| ACT/360 | HIGH | "(ACT/360 divides the actual number of days by 360 — a day count convention that determines how interest accrues)" |
| 30/360 | HIGH | "(30/360 treats every month as exactly 30 days — a simplified day count convention)" |
| ACT/365 | HIGH | "(ACT/365 divides the actual number of days by 365)" |
| no-call period | HIGH | "(the initial period during which the issuer cannot exercise its call right)" |
| observation date | MEDIUM | "(a scheduled date on which the system checks whether conditions — coupon, autocall, barrier — are met)" |
| fixing date | MEDIUM | "(the date on which the reference level is officially recorded)" |
| settlement date | MEDIUM | "(the date on which cash or shares are actually transferred — typically T+2 or T+5 after the event)" |
| T+2, T+5 | MEDIUM | "(T+2 means two business days after the trade or event date)" |
| notional | MEDIUM | "(the face value of the contract on which all payments are calculated)" — already defined in 2.3 but should be in Dependency References |
| termsheet | LOW | "(the document listing every detail of the product: coupon, barrier, maturity, underlying, and all other terms)" — already defined in 2.5 |
| ISIN | MEDIUM | "(International Securities Identification Number — the unique code assigned to every financial instrument)" |
| LEI | MEDIUM | "(Legal Entity Identifier — the standardized code that identifies a company in financial transactions)" |
| booking | LOW | The act of entering a trade into the bank's systems. Usually understood from context but verify |

---

## 2. Credit Market Terms (High Risk)

These terms are used in CLN chapters (§6, §10, §11) and are frequently left undefined because they feel like "standard" credit vocabulary.

| Term | Risk Level | Required Definition or Parenthetical |
|------|:----------:|--------------------------------------|
| RED code | HIGH | "(Reference Entity Database code — a standardized identifier that ensures both systems reference the exact same legal entity)" |
| ISDA Determinations Committee | HIGH | "(the industry body that officially rules on whether a credit event has occurred)" |
| credit event | MEDIUM | Should be in Dependency References → Section 1.9 |
| reference entity | MEDIUM | "(the company or sovereign whose creditworthiness is being insured)" |
| protection buyer / seller | MEDIUM | Defined in CDS basics (1.9) but verify in Dependency References |
| high-yield | MEDIUM | "(lower credit rating, higher default risk — typically rated BB+ or below)" |
| investment-grade | MEDIUM | "(higher credit rating, lower default risk — typically rated BBB- or above)" |
| recovery rate | LOW | Should be in Dependency References → Section 1.9 |
| basis point (bp) | LOW | "(1/100th of a percent — so 100bp = 1%)" — already defined in 1.9 but verify |
| CDS spread | MEDIUM | "(the annual fee, in basis points, paid by the protection buyer)" |
| auction settlement | HIGH | "(the ISDA-administered process that determines the recovery price after a credit event — all market participants bid on the defaulted entity's debt)" |
| succession event | HIGH | "(a corporate event — merger, spin-off, or restructuring — that changes the identity of the reference entity and requires ISDA to determine which new entity inherits the CDS contract)" |

---

## 3. Rates Terms (Medium Risk)

These terms are used in SRT and STEG chapters and may slip through for readers who are new to rates.

| Term | Risk Level | Required Definition or Parenthetical |
|------|:----------:|--------------------------------------|
| CMS | MEDIUM | Should be in Dependency References → Section 1.8 |
| CMS spread | MEDIUM | "(the difference between two CMS rates of different maturities — reflects the steepness of the yield curve)" |
| SOFR | MEDIUM | Should be in Dependency References → Section 1.8 |
| EURIBOR | MEDIUM | Should be in Dependency References → Section 1.8 |
| accrual factor | HIGH | "(the fraction of the period during which the condition was met — e.g., if the rate was in-range for 72 of 90 days, the accrual factor is 72/90 = 80%)" |
| callable | MEDIUM | "(the issuer has the right — but not the obligation — to redeem the product early on specified dates)" |
| non-callable | LOW | "(the product runs to maturity — the issuer cannot redeem early)" |
| range accrual | MEDIUM | "(the coupon accumulates day by day, but only on days when a reference rate stays within a defined range)" |
| TARN | HIGH | "(Target Accrual Redemption Note — the product terminates when total coupons paid reach a predefined lifetime cap)" |
| target level | HIGH | "(the maximum total coupon the investor can receive over the product's life — once reached, the product redeems)" |
| digital | LOW | "(an all-or-nothing payoff: you either receive the full amount or nothing)" — already defined in 1.3 |
| cap / floor | MEDIUM | Should be in Dependency References → Section 1.8 |
| swaption | LOW | Should be in Dependency References → Section 1.8 |

---

## 4. ELN Terms (Low-Medium Risk)

These are generally well-handled but occasionally slip through.

| Term | Risk Level | Required Definition or Parenthetical |
|------|:----------:|--------------------------------------|
| worst-of | MEDIUM | "(the payoff is determined by whichever stock in the basket performs the worst)" |
| best-of | LOW | "(the payoff is determined by whichever stock in the basket performs the best)" |
| memory feature | MEDIUM | "(if a coupon is missed on one observation date, it is not lost — it accumulates and is paid on the next date when the condition is met)" |
| participation rate | MEDIUM | "(the percentage of the underlying's gain that the investor receives)" |
| autocall | LOW | Should be in Dependency References → Section 2 framework |
| knock-in / knock-out | LOW | Should be in Dependency References → Section 1.3 |
| European / American barrier | LOW | Should be in Dependency References → Section 1.3 |
| physical delivery | MEDIUM | "(instead of receiving cash, the investor receives the actual shares — typically at a loss)" |
| cash settlement | LOW | "(the investor receives cash equal to the calculated redemption amount)" |
| coupon barrier | MEDIUM | "(the level the underlying must be at or above for the coupon to be paid — distinct from the capital barrier that triggers loss)" |
| autocall barrier | MEDIUM | "(the level the underlying must be at or above for early redemption to trigger)" |
| capital barrier | MEDIUM | "(the knock-in level — if breached, the investor's principal is at risk)" |

---

## 5. Three-Barrier Disambiguation Rule

Any product with more than one barrier must explicitly distinguish between barrier types on first mention:

| Barrier Type | Purpose | Convention |
|-------------|---------|-----------|
| Capital barrier (KI) | Activates principal risk | "capital barrier (70%)" or "knock-in barrier (70%)" |
| Coupon barrier | Determines coupon payment | "coupon barrier (80%)" |
| Autocall barrier | Triggers early redemption | "autocall barrier (100%)" |

**Rule:** Never use the bare word "barrier" when more than one barrier exists. Always specify which barrier.

---

## 6. Usage Protocol

1. **Before generating a chapter:** Scan the watchlist for terms relevant to the product family
2. **During generation:** When writing §6, §10, §11, cross-check against the watchlist
3. **During review:** The Jargon Police Agent checks every term against this watchlist
4. **Escalation:** Any term not on this watchlist that appears undefined in a chapter should be added to the watchlist for future chapters

---

*Watchlist effective 2026-06-19. Updated as new terms are identified during generation.*
