# Market Conventions Gap Analysis

## Desk Bible v2 -- Detailed Convention Coverage Assessment

**Context**: Market conventions are the mechanical rules that convert economic intent into precise cashflows. A product with a 5% coupon paid quarterly on a $10M notional does not produce $125,000 per quarter -- the actual amount depends on the day count convention, the business day convention, and the calendar. These conventions are not optional knowledge for a structured products professional; they are the plumbing that makes every cashflow calculable.

---

## 1. Business Day Conventions

Business day conventions determine what happens when a scheduled date (payment, fixing, observation) falls on a non-business day.

### What IS covered

| Evidence | Detail |
|----------|--------|
| Modified Following mentions | 0 |
| Following mentions | 0 |
| Preceding mentions | 0 |
| "business day convention" or "day count" combined | ~30 mentions |
| Practical usage | None -- conventions are never applied to adjust a date in the manuscript |

The manuscript occasionally references "business days" in general terms but never defines or applies any specific business day convention.

### What is NOT covered

| Convention | Definition | Usage | Status |
|-----------|-----------|-------|--------|
| **Following** | Move to the next business day | Simple instruments | NOT COVERED |
| **Modified Following** | Move to the next business day unless it falls in the next month, then move to the preceding business day | Standard for most derivatives and notes | NOT COVERED |
| **Preceding** | Move to the preceding business day | Some fixed income instruments | NOT COVERED |
| **Modified Preceding** | Move to the preceding business day unless it falls in the previous month, then move to the following business day | Rare but exists | NOT COVERED |
| **No Adjustment** | Date is unadjusted (payment occurs on next business day but accrual uses the unadjusted date) | Some bond conventions | NOT COVERED |
| **End of Month rule** | If the start date is the last business day of the month, then subsequent dates are also the last business day of the month | Swap conventions | NOT COVERED |

### Severity: CRITICAL

**Impact**: A structured products professional encounters "Modified Following Business Day Convention" on every confirmation, every termsheet, and in every booking system. A reader of the Desk Bible has never seen this convention defined or applied. They cannot:
- Verify that a payment date on a confirmation is correctly adjusted
- Explain to a client why a payment date differs from the scheduled date
- Correctly populate the business day convention field in a booking system
- Identify a business day convention error on a confirmation

This is arguably the single largest gap relative to its importance. Modified Following is to derivatives documentation what punctuation is to English -- invisible when correct, catastrophic when wrong.

---

## 2. Day Count Conventions

Day count conventions determine how the "year fraction" is calculated for accrual-based cashflows (coupons, premiums, interest).

### What IS covered

| Convention | Mentions | How Used | Explanation Provided |
|-----------|----------|----------|---------------------|
| ACT/360 | 21 | Used in worked examples: `quarterly premium = Notional x Spread x (actual days / 360)` | NO -- the formula is shown but the convention is never defined. Reader sees "ACT/360" as a formula label, not as a concept they could explain or choose between alternatives |
| 30/360 | 14 | Used in worked examples for some coupon calculations | NO -- same issue. Appears in formulas, never explained |
| ACT/365 | 0 | Not present | N/A |
| ACT/ACT | 0 | Not present | N/A |
| 30E/360 | 0 | Not present | N/A |
| ACT/365F | 0 | Not present | N/A |

### What is NOT covered

| Gap | Detail |
|-----|--------|
| **What each convention means** | ACT/360 = actual days in the period divided by 360. 30/360 = assumes each month has 30 days, year has 360 days. ACT/ACT = actual days divided by actual days in the year. These definitions are never stated. |
| **When to use which** | ACT/360: money market, LIBOR/SOFR-based products. 30/360: many corporate bonds, some fixed legs. ACT/365: GBP markets. ACT/ACT: government bonds. This mapping is absent. |
| **Currency conventions** | USD typically ACT/360 for floating, 30/360 for fixed. EUR ACT/360 for floating, 30/360 for fixed. GBP ACT/365. JPY ACT/360. This table is absent. |
| **Impact on cashflows** | The difference between ACT/360 and ACT/365 on a $10M notional at 5% over a 90-day period is: ACT/360 = $125,000 vs. ACT/365 = $123,288. This $1,712 difference is never demonstrated. |
| **End-of-month conventions** | How day counts handle months with 28/29/30/31 days -- not covered. |
| **ISDA definitions** | The ISDA 2006 Definitions provide exact specifications for each day count fraction. Not referenced. |

### Severity: HIGH

**Impact**: The reader has seen ACT/360 and 30/360 used mechanically and could reproduce the formula if prompted. But they cannot:
- Choose the correct day count convention for a new product
- Identify a day count error on a confirmation
- Explain to a client or auditor why a specific convention was selected
- Calculate the P&L impact of using the wrong day count

The gap is between mechanical use (seeing it in a formula) and conceptual understanding (knowing what it means, why it exists, and when it applies). The manuscript teaches the former but not the latter.

---

## 3. Calendar Conventions

Calendar conventions determine which days are business days for a given instrument or obligation.

### What IS covered

| Calendar Type | Mentions | Coverage |
|--------------|----------|----------|
| Trading Calendar | 0 | NOT COVERED |
| Settlement Calendar | 0 | NOT COVERED |
| Business Calendar | 0 | NOT COVERED |
| Joint Calendar | 0 | NOT COVERED |
| TARGET / TARGET2 | 0 | NOT COVERED |
| SIFMA | 0 | NOT COVERED |
| NYSE | 0 | NOT COVERED |
| London | 0 (as calendar) | NOT COVERED |

### What is NOT covered

| Gap | Detail |
|-----|--------|
| **Single-centre calendars** | Products traded and settled in one jurisdiction use one calendar (e.g., NYSE calendar for US equity options). Not explained. |
| **Multi-centre calendars** | Cross-currency swaps or structured products may reference "London AND New York business days" -- meaning both must be open. Joint calendar logic is absent. |
| **TARGET2 calendar** | The standard EUR settlement calendar. Critical for EUR-denominated structured products. Not mentioned. |
| **Calendar selection logic** | How to determine which calendar(s) apply to a specific product based on currency, underlying, and settlement jurisdiction. Absent. |
| **Holiday impact** | What happens when a holiday in one centre affects a payment date, fixing date, or observation date. Not covered. |
| **Calendar data sources** | Where calendars are maintained (e.g., ISDA calendar service, internal calendar maintenance). Not covered. |

### Severity: HIGH

**Impact**: Calendar selection affects every date on every trade. A reader of the Desk Bible has no framework for understanding why "London and TARGET business days" appears on a EUR-denominated note with a London issuer, or what happens on a TARGET holiday that is not a London holiday.

---

## 4. Settlement Conventions

### What IS covered

| Convention | Mentions | Coverage Quality |
|-----------|----------|-----------------|
| Cash Settlement | 17 | PARTIALLY COVERED -- defined as settlement type per product; mechanics described |
| Physical Settlement | 5 | MENTIONED ONLY -- referenced but less detail than cash |
| Physical Delivery | 44 | PARTIALLY COVERED -- delivery mechanics described for equity-linked products |
| T+2 | 28 | PARTIALLY COVERED -- referenced as standard settlement cycle; no explanation of why T+2 or regulatory basis |
| T+3 | 5 | MENTIONED ONLY -- referenced for some markets |
| T+0 | 0 | NOT COVERED |
| T+1 | 0 | NOT COVERED |

### What is NOT covered

| Gap | Detail |
|-----|--------|
| **T+1 migration** | US and other markets have moved or are moving to T+1. Not addressed. |
| **Settlement cycle by market** | Which markets are T+1, T+2, T+3. Absent. |
| **Cash settlement mechanics** | Calculation agent determines settlement amount. Settlement amount = f(valuation, day count, convention). The formula chain is incomplete because the convention inputs are missing. |
| **Physical settlement logistics** | Delivery notice periods, delivery baskets, cheapest-to-deliver for credit products. Partial coverage only. |
| **Failed settlement** | What happens when settlement fails. Buy-in procedures. Fails charges. Not covered. |
| **Settlement currency** | When settlement currency differs from the product's currency (quanto, composite). Referenced in product context but settlement mechanics absent. |
| **FX settlement risk (Herstatt risk)** | Cross-currency settlement timing mismatch. Not covered. |
| **CLS settlement** | Continuous Linked Settlement for FX-related settlement. Not covered. |

### Severity: MEDIUM

**Impact**: The reader understands the economic distinction between cash and physical settlement (what the investor receives) but not the operational mechanics (how, when, and through what infrastructure settlement actually occurs). This gap is less critical for front-office roles but significant for middle/back office.

---

## 5. Exercise Styles

### What IS covered

| Style | Mentions | Coverage Quality |
|-------|----------|-----------------|
| European | 92 | WELL COVERED -- defined, explained, contrasted with American, used extensively across equity and rate products |
| American | 62 | WELL COVERED -- defined, early exercise premium discussed, optimal exercise considerations |
| Bermudan | 35 | PARTIALLY COVERED -- defined and used in callable/puttable contexts; less depth on exercise strategy optimisation |

### What is NOT covered

| Gap | Detail |
|-----|--------|
| **Exercise notification mechanics** | How to exercise: notice periods, irrevocability, written notice requirements. Not covered. |
| **Automatic exercise provisions** | When options auto-exercise at expiry (ISDA standard: in-the-money by > threshold). Not covered. |
| **Exercise cut-off times** | Time zone and cut-off time for exercise notices. Not covered. |
| **Partial exercise** | Whether partial exercise is permitted and mechanics thereof. Not covered. |
| **Exercise documentation** | Exercise notice format, delivery requirements. Not covered. |
| **Bermudan exercise strategy** | Optimal exercise boundaries, callable structured product exercise analysis. Partial coverage only. |

### Severity: LOW

**Impact**: Exercise styles are one of the manuscript's relative strengths. The conceptual coverage (what each style means for the option holder/writer) is strong. The gaps are in the operational mechanics of exercise (how to actually exercise), which are important for operations but less so for structuring, sales, and trading roles. This is the least severe gap in the conventions domain.

---

## 6. Observation Conventions

### What IS covered

| Convention | Mentions | Coverage Quality |
|-----------|----------|-----------------|
| Observation Date | 129 | WELL COVERED -- extensively used in autocall, barrier, and range accrual contexts |
| Daily Observation | 39 | PARTIALLY COVERED -- used in barrier and range accrual products |
| Continuous Observation | 4 | MENTIONED ONLY -- referenced but not fully distinguished from daily |

### What is NOT covered

| Gap | Detail |
|-----|--------|
| **Observation Date vs. Valuation Date** | The distinction between when a barrier/trigger is observed vs. when a settlement amount is determined. Not explicitly drawn. |
| **Observation time** | Closing price vs. intraday observation. Partially covered in barrier products but not as a convention. |
| **Scheduled Observation Dates** | The concept of a predetermined schedule of observation dates (common in autocalls). Implicitly covered but not formalised. |
| **Observation frequency conventions** | How "daily," "weekly," "monthly," "quarterly" observation maps to actual dates. Not formalised. |
| **Disrupted day provisions** | What happens when an observation date falls on a disrupted trading day. Partially covered in some products but not as a convention. |
| **Averaging conventions** | Asian observation (arithmetic vs. geometric averaging). Covered in Asian option products but not as a general convention. |

### Severity: LOW

**Impact**: Observation conventions are reasonably well covered relative to other convention types, primarily because autocall and barrier products (which make up a large portion of the manuscript) inherently require discussion of observation mechanics. The gaps are in the formalisation of conventions rather than the substance.

---

## Severity Summary

| Convention Category | Coverage Level | Severity of Gap | Terms Covered / Total |
|--------------------|---------------|-----------------|----------------------|
| Business Day Conventions | NOT COVERED | CRITICAL | 0 / 6 |
| Day Count Conventions | MECHANICALLY USED, NOT EXPLAINED | HIGH | 2 mentioned / 6 |
| Calendar Conventions | NOT COVERED | HIGH | 0 / 7 |
| Settlement Conventions | PARTIALLY COVERED | MEDIUM | 3 / 8 |
| Exercise Styles | WELL COVERED | LOW | 3 / 3 + operational gaps |
| Observation Conventions | PARTIALLY COVERED | LOW | 3 / 6 |

---

## Impact on Practitioner Competence

| Role | Impact of Convention Gaps |
|------|--------------------------|
| **Structurer** | MEDIUM -- can design product economics but cannot specify convention fields on a termsheet without external reference |
| **Trader** | MEDIUM -- understands risk but may not catch convention errors in confirmations that affect P&L |
| **Sales** | LOW-MEDIUM -- can explain product to clients but cannot answer convention questions from sophisticated buyers |
| **Middle Office / Product Control** | HIGH -- cannot verify confirmations, cannot populate booking system convention fields, cannot perform P&L Explain with correct day counts |
| **Operations** | CRITICAL -- conventions are the core of operational processing. Every payment, every fixing, every settlement requires correct convention application |
| **Risk** | MEDIUM -- risk calculations require correct day counts for time-weighted metrics; convention errors propagate into risk numbers |
| **Compliance** | LOW -- conventions are not directly a compliance concern, but incorrect convention selection can cause regulatory reporting errors |

---

## Recommendation Hierarchy

If the manuscript were to address convention gaps, priority order should be:

| Priority | Convention | Reason | Estimated Addition |
|----------|-----------|--------|-------------------|
| 1 | Business Day Conventions | Zero coverage of a universal concept | ~800 lines (1 chapter) |
| 2 | Day Count Conventions | Used but not explained; conceptual gap | ~600 lines (1 chapter) |
| 3 | Calendar Conventions | Zero coverage; enables day count and business day application | ~400 lines (1 section) |
| 4 | Settlement Mechanics | Operational depth needed | ~400 lines (1 section) |
| 5 | Observation Formalisation | Already partially covered; needs formalisation | ~200 lines (additions to existing sections) |
| 6 | Exercise Mechanics | Operational exercise detail | ~200 lines (additions to existing sections) |

**Total estimated addition**: ~2,600 lines, representing ~11.5% growth on the current 22,620-line manuscript. This could form a single new Part or be integrated into Part 2 (Framework) as a dedicated "Market Conventions" chapter.
