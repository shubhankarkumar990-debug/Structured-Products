# PART 6 — THE OPERATIONAL ECOSYSTEM

*How the infrastructure around structured products works — from market conventions to regulatory compliance. Part 5 told you what each product is and how it works. Part 6 tells you how those products are documented, valued, controlled, and governed in practice.*

---

## 6.1 Market Conventions

*How the market speaks — the conventions that govern when, how, and on what basis payments are calculated*

### Why Conventions Exist

Imagine two neighbors agree to share the cost of a fence. One neighbor calculates the total in meters, the other in feet. One measures from the front of the property, the other from the back. One expects payment on the first of the month, the other on the last.

Without shared conventions, even a simple agreement becomes an argument.

Financial markets are the same, except the sums are measured in millions. When a bank in London sells a structured note to a pension fund in New York, with an underlying stock listed in Tokyo, every party must agree on precisely how dates are counted, which calendars determine business days, when payments settle, and how interest accrues. Market conventions are the shared language that makes this possible.

Every field you will encounter in a termsheet (Section 6.2), every booking parameter in Part 5's §16 sections, and every clause in the ISDA Master Agreement (Section 6.3) rests on these conventions. Get them wrong by one day, one calendar, or one day count method, and the numbers stop matching between counterparties.

---

### Business Day Conventions

A "business day" sounds simple — Monday through Friday, excluding weekends. But in practice, business days depend on where you are.

New Year's Day is a holiday in most countries, but January 2 is only a holiday in some. Chinese New Year shuts down Hong Kong but not London. Eid al-Fitr closes markets in Dubai but not in New York. Thanksgiving is a US holiday that does not exist in Europe. When a structured product references "the next business day," the answer depends entirely on which country's calendar you are using.

A **business day** is a day on which commercial banks and financial markets are open for business in the relevant jurisdiction(s). The termsheet and confirmation will specify which jurisdiction(s) apply — and multiple can apply simultaneously.

Now, the question: what happens when a scheduled payment date falls on a non-business day?

**Following Business Day Convention.** Move the date forward to the next business day. If a coupon is due on Saturday, it is paid on Monday (assuming Monday is not also a holiday).

**Modified Following Business Day Convention.** Move the date forward to the next business day — *unless* that would push the date into the next calendar month. If it would, move backward to the preceding business day instead.

This is the market standard for most structured products. The reason is straightforward: if a coupon is due on Friday, January 31 but the 31st is a holiday, the Following convention would move the payment to Monday, February 3. That pushes the payment into February, which changes the accrual period, the month-end accounting, and potentially the day count calculation. Modified Following avoids this by moving the date backward to Thursday, January 30 instead.

**Preceding Business Day Convention.** Move the date backward to the most recent business day. If a coupon is due on Saturday, it is paid on Friday. This convention is less common for coupon payments but appears in some contexts (for example, period-end dates in certain swap structures).

**No Adjustment.** Use the calendar date regardless of whether it is a business day. The date is the date; payments may be delayed but the economic date is unchanged. This is rare for payment dates but can apply to observation and fixing dates in specific structures.

**Worked Example: Saturday, December 31**

A structured note has a semi-annual coupon due on December 31. December 31 falls on a Saturday. January 1 and January 2 are public holidays. The next business day is Monday, January 3.

| Convention | Adjusted Date | Reasoning |
|-----------|--------------|-----------|
| Following | January 3 (Monday) | Next business day after December 31 |
| Modified Following | December 30 (Friday) | January 3 is in the next month (January), so move backward instead |
| Preceding | December 30 (Friday) | Previous business day before December 31 |
| No Adjustment | December 31 (Saturday) | Date stands; payment settles on next available day but economic date is unchanged |

In practice, this product would almost certainly use Modified Following. The payment would occur on Friday, December 30, keeping everything within the December accrual period and the same calendar year.

---

### Day Count Conventions

A day count convention answers a deceptively simple question: *what fraction of a year does this period represent?*

If you lend someone $1,000,000 at 5% per year, but the coupon period is only 90 days, how much do you owe? The answer is $1,000,000 × 5% × (day count fraction). The day count fraction depends entirely on which convention you use.

A **day count fraction** (also called a day count basis or accrual basis) is the formula used to calculate the proportion of a year that a given period represents. Different markets use different formulas, and the dollar differences are material.

**ACT/360 (Actual/360)**

Count the actual number of calendar days in the period. Divide by 360.

This convention treats the year as having 360 days, even though actual years have 365 (or 366). This means every coupon payment is slightly larger than it would be under ACT/365, because you are dividing by a smaller number. ACT/360 is the standard convention for money market instruments, SOFR-based floating rates, EUR and USD interest rate swaps, and most floating-rate notes.

Day count fraction = Actual days / 360

**ACT/365 (Actual/365 Fixed)**

Count the actual number of calendar days in the period. Divide by 365.

This convention is the standard for GBP-denominated instruments. It does not adjust for leap years — it always uses 365, even in a leap year. This is why it is sometimes called "ACT/365 Fixed."

Day count fraction = Actual days / 365

**ACT/ACT (Actual/Actual)**

Count the actual number of calendar days in the period. Divide by the actual number of days in the relevant year (or coupon period, depending on the variant). In a leap year, the denominator is 366; otherwise, 365.

ACT/ACT is the standard for most government bonds (US Treasuries, Gilts, Bunds). It is the most precise convention because it accounts for leap years. There are several variants (ACT/ACT ISDA, ACT/ACT ICMA), which differ in how they handle periods that span a leap year boundary. For our purposes, the key point is that ACT/ACT adjusts for reality.

Day count fraction = Actual days / Actual days in year (or period)

**30/360 (Bond Basis)**

Assume every month has exactly 30 days and every year has exactly 360 days. If a period runs from March 15 to June 15, the convention counts 90 days (3 months × 30 days), even though the actual number of calendar days is 92.

This convention is used for many US corporate bonds, some structured notes, and some fixed-rate legs of swaps. Its simplicity makes calculations easy — every semi-annual period is exactly 180 days — but it does not reflect the actual passage of time.

Day count fraction = (360 × (Y₂ − Y₁) + 30 × (M₂ − M₁) + (D₂ − D₁)) / 360

**30E/360 (Eurobond Basis)**

Similar to 30/360, but with different rules for end-of-month dates. If the start date is the 31st, it becomes the 30th. If the end date is the 31st, it also becomes the 30th. The "E" stands for European.

This convention is used for Eurobonds and many EUR-denominated fixed-rate instruments.

**Worked Example: The Dollar Difference**

A structured note pays a 5% annual coupon on $100,000,000 notional. The coupon period runs from March 15 to September 15 — 184 actual calendar days.

| Convention | Day Count Fraction | Coupon Payment |
|-----------|-------------------|----------------|
| ACT/360 | 184 / 360 = 0.51111 | $100M × 5% × 0.51111 = **$2,555,556** |
| ACT/365 | 184 / 365 = 0.50411 | $100M × 5% × 0.50411 = **$2,520,548** |
| 30/360 | 180 / 360 = 0.50000 | $100M × 5% × 0.50000 = **$2,500,000** |

The difference between ACT/360 and 30/360 on this single coupon payment is **$55,556**. Over the life of a multi-year product with multiple coupon periods, these differences compound. On a desk that manages billions in notional, getting the day count convention wrong is not a rounding error — it is a material booking mistake.

---

### Calendar Conventions

Markets in different countries operate on different schedules. When a structured product involves parties, underlyings, or currencies in multiple jurisdictions, the question of "which calendar?" becomes critical.

**Trading Calendar.** Determines when a particular exchange or market is open for trading. This matters for observation dates — if the termsheet says "the closing price on June 15," but the exchange is closed on June 15, you need a fallback.

**Settlement Calendar.** Determines when settlement can occur in a particular jurisdiction. This may differ from the trading calendar. A trade can execute on a day when the exchange is open, but settlement may be delayed if the payment system in the settlement currency's jurisdiction is closed.

**Business Calendar (Union Calendar).** When a trade involves multiple jurisdictions, the business calendar is typically the *union* of all relevant holiday calendars. A day is a non-business day if it is a holiday in *any* of the specified jurisdictions. This is the most conservative approach — it has the most holidays.

Example: A USD/EUR cross-currency swap references both New York and London calendars. Independence Day (July 4) is a holiday in New York but not London. Under a union calendar, July 4 is a non-business day for this trade because it is a holiday in at least one jurisdiction.

**Joint Calendar (Intersection Calendar).** Less common, but used in some contexts. A day is a non-business day only if it is a holiday in *all* specified jurisdictions. This produces fewer holidays than the union approach.

**TARGET Calendar.** The TARGET (Trans-European Automated Real-time Gross settlement Express Transfer) calendar is used for all EUR-denominated settlements processed through the TARGET2 payment system. TARGET holidays are standardized across the Eurozone: New Year's Day, Good Friday, Easter Monday, May 1 (Labour Day), December 25, and December 26. This calendar is specified in virtually every EUR swap and structured note confirmation.

**Why calendars matter for structured products:**

- **Barrier observations.** If a barrier is monitored continuously but the exchange is closed for a local holiday, the barrier cannot be breached on that day. The calendar determines which days count.
- **Coupon accrual.** Day count fractions depend on the number of days in a period, and business day adjustments depend on the calendar.
- **Fixing dates.** Floating-rate coupons fix against reference rates on specific dates. If the fixing date falls on a holiday in the rate's publication calendar, the fallback provisions apply.
- **Settlement.** A trade cannot settle if the payment system in the settlement currency is closed.

---

### Settlement Conventions

When a trade is executed, the securities and cash do not change hands immediately. Settlement occurs after a specified number of business days.

**T+0 (Same-day settlement).** Cash and securities are exchanged on the trade date. This is unusual for structured products but occurs in some money market transactions.

**T+1 (Next-day settlement).** Settlement occurs one business day after the trade date. Some equity markets have moved to T+1 (the US moved to T+1 in May 2024).

**T+2 (Standard settlement).** Settlement occurs two business days after the trade date. This has been the global standard for most securities since the mid-2010s, when markets moved from T+3 to reduce settlement risk. Most structured products settle on a T+2 basis.

**T+3 (Three-day settlement).** Historically the standard before the T+2 transition. Still applies in some emerging markets.

The "T" is the trade date, and the "+" refers to *business* days, not calendar days. If you execute a trade on Friday (T), T+2 is Tuesday, not Sunday.

**Delivery versus Payment (DvP).** The standard settlement mechanism for most securities transactions. The securities and the cash move simultaneously — neither party releases their side until both sides are ready. This eliminates settlement risk: the risk that one party delivers but the other fails to pay.

**Free of Payment (FoP).** Delivery of securities without a corresponding cash payment. Used in specific contexts such as collateral transfers under a CSA (Section 6.3), internal transfers between accounts, or corporate actions like stock splits.

**Cash Settlement vs Physical Delivery.** This distinction matters enormously for structured products and connects directly to Part 5.

In **cash settlement**, the redemption amount is calculated as a cash value and paid to the investor. The investor never receives the underlying securities. Most structured notes are cash-settled.

In **physical delivery**, the investor receives actual shares of the underlying instead of cash. This occurs in some Reverse Convertibles when the barrier is breached — instead of receiving a cash amount reflecting the stock's depreciated value, the investor receives the actual shares. The economic outcome is similar, but the tax, accounting, and operational implications differ significantly.

---

### Observation Conventions

Observation conventions determine *when* and *how often* the underlying is checked against barriers, triggers, and fixing levels. This is where structured products come alive — the observation convention can mean the difference between full principal repayment and a significant loss.

**Continuous Observation (American-style).** The barrier is monitored at every traded price during market hours on every trading day. If the underlying touches the barrier at any point — even for a single transaction at 2:47 PM on a quiet Tuesday — the barrier event is triggered.

This is the most aggressive form of observation for the investor. More observation points mean more chances for the barrier to be hit.

**Daily Observation (Closing Price).** The barrier is checked only once per day, using the official closing price. The underlying could trade below the barrier during the day, recover by the close, and the barrier would not be breached.

**Periodic Observation (Discrete).** The barrier is checked only on specific dates listed in the termsheet — typically matching coupon observation dates (quarterly, semi-annually). The underlying could spend months below the barrier, but if it is above the barrier on every observation date, no barrier event occurs.

**The practical difference is enormous:**

Consider a stock at $100 with a knock-in barrier at $70. During a market selloff, the stock drops to $68 on a Wednesday afternoon but recovers to $73 by the close.

| Observation Convention | Barrier Breached? | Investor Outcome |
|----------------------|-------------------|------------------|
| Continuous | Yes — the stock traded at $68 | Knock-in put activated; investor faces downside risk at maturity |
| Daily (closing) | No — closing price was $73 | No barrier event; principal protected (subject to maturity observation) |
| Periodic (quarterly) | No — unless the observation date was that Wednesday | No barrier event unless checked that day |

This connects directly to Part 1, Section 1.3, where we introduced European vs American barrier observation. American barriers use continuous or daily observation. European barriers use periodic (often single-date) observation at maturity. The coupon premium reflects this difference — American barriers pay higher coupons because they are riskier for the investor.

---

### Floating Rate Mechanics

Many structured products reference floating interest rates — either as the coupon on a floating-rate note, as the reference rate in a swap, or as a component in a rate-linked structured product. Since the transition away from LIBOR, the floating rate landscape has changed fundamentally.

**SOFR (Secured Overnight Financing Rate).** The replacement for USD LIBOR. SOFR is based on overnight repurchase agreement (repo) transactions secured by US Treasury securities. It is published daily by the Federal Reserve Bank of New York. Unlike LIBOR, which was based on bank estimates, SOFR is based on actual transactions — roughly $1 trillion in daily volume.

SOFR is an overnight rate, meaning it applies for a single day. To create a term rate equivalent to the old 3-month LIBOR, SOFR must be compounded over the relevant period. This compounding — SOFR compounded in arrears — means the rate for a coupon period is not known until the end of the period, which is a significant operational change from the old LIBOR world where the rate was fixed at the start.

**EURIBOR (Euro Interbank Offered Rate).** The benchmark rate for EUR-denominated instruments. Unlike SOFR, EURIBOR survived the benchmark reform and continues as a forward-looking term rate (1-week, 1-month, 3-month, 6-month, 12-month). It is based on contributions from a panel of Eurozone banks.

**SONIA (Sterling Overnight Index Average).** The replacement for GBP LIBOR. Like SOFR, SONIA is an overnight rate based on actual transactions. It is published by the Bank of England and used for GBP-denominated derivatives and floating-rate instruments.

**Fixing Lag.** In the LIBOR era, the rate was typically fixed two business days before the start of the accrual period. This "2-day fixing lag" gave counterparties time to calculate and settle payments. In the post-LIBOR world, overnight rates like SOFR are fixed daily, and the compounded rate is typically calculated with a lookback period (e.g., the rate used for each day is the rate published two business days prior) to give operational breathing room.

**Reset Dates.** The dates on which the floating rate resets for the next accrual period. For a quarterly-pay floating-rate note, the reset dates typically coincide with the coupon dates. Between resets, the rate is fixed — payments are predictable.

**Stub Periods.** When a trade's start date does not align with the standard rate reset schedule, the first (or last) accrual period will be shorter or longer than the standard period. This non-standard period is called a stub.

- **Short first stub:** The trade starts partway through a period, so the first period is shorter than normal.
- **Long first stub:** The trade starts before the standard period start, so the first period is longer than normal.
- **Short last stub** and **long last stub:** Same concept at the end of the trade.

Stubs affect the day count fraction calculation and must be handled correctly in system booking.

**Broken Dates.** Non-standard period lengths that do not align with the regular payment schedule. Similar to stubs, but can occur at any point in the trade's life due to amendments, novations, or non-standard terms.

**End-of-Month Rule.** If a payment or reset date falls on the last business day of a month, all subsequent payment or reset dates also fall on the last business day of their respective months. This prevents "date drift" where a date that starts at month-end gradually shifts earlier in the month due to business day adjustments.

Example: A swap with quarterly payments starting on February 28 (last business day of February in a non-leap year). Under the end-of-month rule, the next payment date is March 31 (last business day of March), then June 30, then September 30 — always the last business day of the month.

**Compounding vs Simple Interest for Overnight Rates.** When SOFR or SONIA is used as the reference rate, the market standard is compounding in arrears. This means the daily rates are compounded (interest on interest) over the accrual period to produce the period rate. Simple interest would just average the daily rates. The difference is small for short periods but becomes material for longer accrual periods.

SOFR compounded in arrears for a quarterly period:

Rate = [∏(1 + SOFRᵢ × dᵢ/360) − 1] × 360/D

Where SOFRᵢ is the rate for each day, dᵢ is the number of days that rate applies (usually 1, but 3 over weekends), and D is the total actual days in the period.

---

### Coupon Mechanics

Coupons are the regular payments that structured products make to investors. The mechanics of how coupons accrue, who receives them, and how they compound are governed by specific conventions.

**Accrual.** Interest on a coupon accrues day by day from the previous coupon date (or issue date, for the first period) to the current coupon date. The accrued interest at any point in time equals:

Accrued Interest = Notional × Coupon Rate × Day Count Fraction (from last coupon date to today)

This matters for secondary market trading — if an investor sells a note between coupon dates, the buyer must compensate the seller for interest that has accrued but not yet been paid. This is the difference between clean price and dirty price (covered in Section 6.2).

**Record Date.** The date on which the registrar determines who owns the note and is therefore entitled to receive the next coupon. Typically 1-2 business days before the payment date. If you own the note on the record date, you receive the coupon — even if you sell the note the next day.

**Ex-Date.** The first date on which a buyer of the note does NOT receive the upcoming coupon. The ex-date is typically one business day before the record date. If you buy the note on or after the ex-date, you will not receive the next coupon.

The relationship is: Ex-Date → Record Date → Payment Date

**Compounding.** In some structures, if a coupon is not paid in a given period (for example, a memory coupon in a Phoenix Autocallable where the observation condition was not met), the unpaid coupon may compound — earning interest on itself — until it is eventually paid. The compounding convention (simple or compound, and the compounding rate) is specified in the termsheet.

**Day Count Application to Coupons.** Putting it all together, a coupon payment is calculated as:

Coupon Payment = Notional × Coupon Rate × Day Count Fraction × [Coupon Condition]

Where the Day Count Fraction is determined by the day count convention (ACT/360, 30/360, etc.), and the Coupon Condition is 1 for unconditional coupons, or a binary (0 or 1) outcome for conditional coupons like digitals and Phoenix structures.

---

### Common Mistakes

1. **Using the wrong day count convention.** This is the most common convention error on the desk. A trade booked with ACT/365 instead of ACT/360 will produce incorrect coupon amounts on every single payment date. On a $100M notional at 5%, the difference per semi-annual coupon can exceed $30,000. Always confirm the day count convention against the termsheet before booking.

2. **Confusing Modified Following with Following.** A coupon date of January 31 (Saturday) under Following moves to February 2 (Monday). Under Modified Following, it moves backward to January 30 (Friday). If you apply the wrong convention, the accrual period is wrong, the day count fraction is wrong, and the coupon amount is wrong. Modified Following is the market default — but always verify from the confirmation.

3. **Forgetting the calendar.** A trade referencing a US underlying, settled in EUR, with a Japanese counterparty may need to respect three separate holiday calendars. US holidays affect observation dates, TARGET holidays affect EUR settlement, and Tokyo holidays affect counterparty availability. Booking the trade with only one calendar will produce incorrect observation and settlement dates.

4. **Ignoring the end-of-month rule.** A swap starting on January 31 should, under the end-of-month rule, have subsequent dates on February 28/29, March 31, April 30, and so on. If you ignore this rule and simply add months, you get February 28, March 28, April 28 — a permanently shifted schedule that compounds errors across the life of the trade.

5. **Assuming SOFR behaves like LIBOR.** LIBOR was fixed at the start of the period. SOFR compounded in arrears is not known until the end of the period. This means coupon amounts cannot be calculated until the period is nearly complete. Systems that assume the rate is known at period start will produce incorrect interim valuations.

6. **Miscounting days across weekends and holidays.** T+2 means two *business* days, not two calendar days. A trade executed on Thursday settles on Monday (skipping Saturday and Sunday). A trade executed on Wednesday before a Thursday public holiday settles on Monday (skipping Thursday, Saturday, and Sunday). Getting this wrong delays settlement and triggers fails.

> **Professor Note:** If you remember only one thing from this section, remember this: conventions are not preferences — they are contractual obligations. The termsheet specifies ACT/360 or 30/360, Modified Following or Following, T+2 or T+3, continuous or daily observation. Each choice has precise economic consequences. A $100M trade with the wrong day count convention will pay the wrong coupon on every single payment date, and neither counterparty's system will flag it as an error — it will simply calculate a different number. The convention is the contract. Read it. Book it. Verify it.

Every §16 (Booking and Systems) section in Part 5 specifies the system and key booking fields for each product. This section teaches the conventions that those fields rely on. When you see "Day Count: ACT/360" or "Business Day Convention: Modified Following" in a booking screen, you now know exactly what those fields mean, why they matter, and what goes wrong when they are incorrect.

---

## 6.2 Reading a Termsheet

*What the document says — a field-by-field guide to structured product documentation*

### The Blueprint

A termsheet is like an architectural blueprint. Every line specifies a precise measurement, material, or specification. An architect who misreads a blueprint builds the wrong building. A desk professional who misreads a termsheet books the wrong trade.

Unlike a blueprint, however, a termsheet does not come with illustrations. It is a dense, text-heavy document, typically 3-10 pages long, packed with dates, percentages, conventions, and legal references. It looks intimidating. But like any document, once you know what each field means and where to find it, reading a termsheet becomes systematic.

This section teaches you to read a termsheet the way a pilot reads a checklist — every item, in order, with full understanding of what each one means and what happens if it is wrong.

---

### What a Termsheet Is

A **termsheet** (also called a term sheet, pricing supplement, or product supplement) is a summary document that lists all economic and legal terms of a structured product trade. It is the single reference point that both parties — the issuer and the investor — use to confirm what was agreed.

**Indicative Termsheet.** A proposal. Issued during the pre-trade phase, it shows approximate terms based on current market conditions. Key terms like coupons, barriers, and participation rates may change before the trade is finalized. The header will typically say "INDICATIVE TERMS — SUBJECT TO CHANGE." An indicative termsheet is not binding.

**Final Termsheet.** Binding. Issued after the trade is priced and executed. The terms are fixed and reflect the actual economics of the trade. The final termsheet is the basis for the confirmation (Section 6.3) and the booking in systems.

**Who produces it:** The structurer drafts the termsheet based on the product design and pricing. Legal reviews it for accuracy and compliance. Sales sends it to the client. After execution, Operations uses it as the primary reference for booking.

**Standard layout:** While formats vary by bank, most termsheets follow a consistent structure:

| Section | What It Contains |
|---------|-----------------|
| **Header** | Product name, ISIN/CUSIP, indicative or final status, date |
| **Parties** | Issuer, calculation agent, paying agent, investor (for bilateral trades) |
| **Underlying** | Reference asset(s), exchange, Bloomberg/Reuters ticker |
| **Economics** | Notional, coupon, strike, barrier, participation, cap/floor |
| **Dates** | Trade date, issue date, observation dates, maturity, payment dates |
| **Conventions** | Day count, business day convention, settlement calendar, settlement type |
| **Legal** | Governing law, ISDA definitions, market disruption provisions, corporate action adjustments |
| **Settlement** | Settlement currency, settlement type (cash/physical), settlement date |

---

### Date Fields

Dates are the skeleton of a structured product. Every cash flow, every observation, every economic event is anchored to a date. A single incorrect date can cause a missed coupon observation, a delayed settlement, or a booking error that persists for the life of the trade.

**Trade Date.** The date on which the trade is agreed between the two parties. This is when the economic terms are locked in. The trade date establishes the legal existence of the transaction.

**Booking Date.** The date on which the trade is entered into the bank's systems (NEMO, Sophis, or Murex, as described in Part 5's §16 sections). The booking date may differ from the trade date — a trade agreed on a Friday afternoon might not be booked until Monday. The booking date matters for system reconciliation and audit trails, but the economic terms are governed by the trade date.

**Effective Date.** The date on which the trade's economics begin. For swaps, this is when cash flows start accruing. For notes, the effective date may coincide with the issue date. The effective date is not always the same as the trade date — a swap agreed on March 15 might have an effective date of March 17 (T+2).

**Issue Date.** The date on which a note is formally issued to investors. This is when the investor's cash is exchanged for the note and the security legally exists. For structured notes, the issue date is the starting point for the first accrual period.

**Settlement Date.** The date on which cash and securities are actually exchanged. For an initial purchase, this is when the investor pays and receives the note. For a maturity payment, this is when the issuer pays the redemption amount. Settlement follows trade date by the applicable settlement convention (typically T+2).

**Maturity Date.** The final date of the product's life. On this date (or the next business day per the business day convention), the product terminates and the final redemption is paid. This is not negotiable after issuance.

**Observation Date(s).** The dates on which the underlying is checked against barriers, autocall triggers, or coupon conditions. A Phoenix Autocallable with quarterly observations will have observation dates every three months. These are among the most important dates in the termsheet — they determine whether coupons are paid, whether barriers are breached, and whether the product autocalls.

**Valuation Date.** The date on which the final value of the underlying is determined for the purpose of calculating the redemption amount. This is typically the last observation date (for autocallables) or the maturity observation date (for non-autocallable products). The closing price on the valuation date determines the final payoff.

**Determination Date.** The date on which the calculation agent formally determines an outcome — for example, whether a barrier has been breached, whether an autocall condition has been met, or what the final redemption amount is. This may be the same as the observation date or a specified number of business days after.

**Fixing Date.** The date on which a floating rate or reference price is observed and fixed for the purpose of calculating a payment. For SOFR-based coupons, the fixing date is each business day during the accrual period. For equity-linked products, the fixing date is when the initial reference level is set (often the trade date or issue date).

**Reset Date.** The date on which a floating rate resets for the next accrual period. For a quarterly-pay floating-rate note, the reset date is typically 2 business days before the start of each new accrual period (the "fixing lag" from Section 6.1).

**Roll Date.** The date on which a position moves from one contract period to the next. This is most relevant for products linked to futures contracts or for rolling swap positions. The roll date determines which contract month the product references.

**Payment Date(s).** The dates on which coupon payments or principal payments are made to the investor. Payment dates are subject to business day conventions — if a payment date falls on a holiday, the convention determines which day the payment actually occurs.

**Record Date.** The cutoff date for determining who is entitled to receive a payment. If you own the note on the record date, you receive the upcoming coupon. Typically set 1-2 business days before the payment date.

**Ex-Date.** The first date on which a purchaser of the note will NOT receive the upcoming payment. If you buy the note on the ex-date or later, you do not get the next coupon. The ex-date is typically one business day before the record date. This matters for secondary market trading — the note's price drops by approximately the coupon amount on the ex-date.

---

### Economics Fields

These are the numbers that define the payoff. Every economics field maps directly to a component in the product decomposition framework taught in Part 2.

**Notional / Face Value.** The reference amount on which all calculations are based. A $10,000,000 notional structured note means all coupons, barriers, and redemption amounts are calculated as percentages of $10,000,000. The investor's initial investment equals the notional multiplied by the issue price.

**Issue Price.** The price at which the note is issued, expressed as a percentage of notional. An issue price of 100% (par) means the investor pays the full notional. An issue price of 99% means the investor pays $9,900,000 on a $10,000,000 notional — the 1% discount may reflect structuring fees or market conditions. Discount Reverse Convertibles (Part 5) are issued below par by design.

**Clean Price.** The quoted price of the note excluding accrued interest. This is what you see on trading screens and what dealers quote to each other. Clean price facilitates comparison because it strips out the coupon accrual effect that would otherwise make prices change daily.

**Dirty Price.** The actual amount the buyer pays, including accrued interest. Dirty Price = Clean Price + Accrued Interest. When you buy a note between coupon dates, you pay the dirty price — compensating the seller for interest that has accrued since the last coupon.

**Accrued Interest.** The interest that has accumulated since the last coupon payment (or issue date). Calculated using the day count convention specified in the termsheet. Accrued interest resets to zero immediately after each coupon payment.

**Strike.** The reference level for option payoffs. In a Reverse Convertible, the strike is typically set at the underlying's closing price on the trade date (100% of initial level). In a Principal Protected Note, the strike determines the level above which the investor participates in upside. The strike may be expressed as a percentage of the initial level or as an absolute price.

**Barrier.** The level that triggers a change in payoff. A knock-in barrier at 70% means the put option activates if the underlying falls to 70% of its initial level. A knock-out barrier at 130% means the option is extinguished if the underlying rises to 130%. The barrier level, observation convention (Section 6.1), and barrier type (knock-in vs knock-out) together define the conditional protection structure.

**Participation Rate.** The percentage of the underlying's performance that the investor receives. A participation rate of 60% on upside means if the underlying rises 20%, the investor earns 12% (60% × 20%). This appears primarily in Principal Protected Notes and Booster Notes.

**Cap.** The maximum return the investor can receive, regardless of how well the underlying performs. A cap of 15% means even if the underlying rises 50%, the investor receives only 15%. Caps appear in products like capped PPNs and some FCNs.

**Floor.** The minimum return the investor is guaranteed. A floor of 0% means the investor cannot lose money (full principal protection). A floor of -10% means the maximum loss is 10% of the notional. Floors appear in Principal Protected Notes and Airbag structures.

**Trigger / Autocall Level.** The level at which early redemption is triggered. Typically expressed as a percentage of the initial level. If the underlying is at or above the autocall level on an observation date, the product terminates early and the investor receives their notional plus any accrued or conditional coupon. Autocall levels can be fixed (e.g., 100% on every date) or declining (e.g., 100% in year 1, 95% in year 2, 90% in year 3).

**Buffer.** The range of downside protection expressed as a percentage. A 30% buffer means the investor is protected against the first 30% of decline. If the underlying falls 25%, the investor loses nothing. If the underlying falls 35%, the investor loses only 5% (the decline beyond the buffer). Buffers differ from barriers — a barrier is all-or-nothing (protection until breached, then full exposure), while a buffer absorbs losses up to the buffer level.

**Coupon Rate.** The periodic return paid to the investor, expressed as an annualized percentage. A 7% semi-annual coupon on $10,000,000 pays $10,000,000 × 7% × Day Count Fraction per period. The coupon may be fixed (unconditional), conditional (paid only if an observation condition is met), or memory (conditional with ability to recover missed payments).

**Funding Spread.** The spread over the reference rate that reflects the issuer's cost of borrowing. This appears in the pricing breakdown rather than the client-facing termsheet. It represents FTP (Funds Transfer Pricing) discussed in Part 2 — the internal cost that reduces the coupon budget.

**Discount Spread.** The spread used to discount future cash flows when calculating the present value of the product. This includes the issuer's credit spread and is used in mark-to-market valuation, not in coupon calculations.

---

### Convention Fields

These fields specify *how* the economics are calculated. They reference the conventions taught in Section 6.1.

**Business Day Convention.** Specifies which business day convention applies to payment and observation dates (Modified Following, Following, Preceding, or No Adjustment). As discussed in Section 6.1, this determines what happens when a scheduled date falls on a holiday.

**Day Count Convention.** Specifies the day count basis for interest calculations (ACT/360, ACT/365, 30/360, ACT/ACT, or 30E/360). This determines the fraction of a year used in every coupon and accrual calculation.

**Settlement Calendar.** Specifies which jurisdiction's calendar governs settlement dates. A note settling in USD will reference the New York calendar. A note settling in EUR will reference the TARGET calendar. A cross-currency product may reference multiple calendars.

**Settlement Type.** Cash or Physical. Cash settlement means the investor receives a cash payment. Physical settlement means the investor receives shares of the underlying. Most structured notes are cash-settled, but some Reverse Convertibles and DRCs may deliver shares if the barrier is breached.

**Settlement Currency.** The currency in which all payments are made. A note linked to a Japanese stock but denominated in USD will have all coupon and redemption payments in USD. Any currency conversion is handled by the issuer (and the FX risk may or may not be hedged — this is a separate consideration).

**Exercise Style.** European, American, or Bermudan. This describes when the embedded option can be exercised, and connects directly to Part 1, Section 1.2. Most structured products use European exercise (option exercisable only at maturity), but autocallable features effectively create early exercise opportunities on discrete observation dates (Bermudan-like behavior).

---

### Legal Fields

These fields define the legal framework that governs the trade. They connect to Section 6.3 and are often the most overlooked — and most dangerous — section of the termsheet.

**Calculation Agent.** The entity responsible for determining outcomes under the termsheet — including whether barriers have been breached, what coupon amounts are due, and what the final redemption amount is. The calculation agent is almost always the issuing bank. This means the bank acts as both counterparty and referee, which creates a conflict of interest that is managed through standard market practice and regulatory oversight.

**Governing Law.** The jurisdiction whose law governs the contract. English law and New York law are the most common for international structured products. The governing law determines how disputes are resolved and how contractual terms are interpreted.

**ISDA Definitions.** The version of the ISDA definitions that applies. Common references include the 2006 ISDA Definitions (for interest rate terms), the 2002 ISDA Equity Derivatives Definitions (for equity-linked terms), and the 2014 ISDA Credit Derivatives Definitions (for credit-linked terms). These definitions are incorporated by reference — meaning the termsheet does not reproduce every definition, but instead says "as defined in the 2006 ISDA Definitions." If you have not read the relevant ISDA definitions, you may not fully understand the termsheet.

**Market Disruption Event.** The provisions that define what happens if normal market conditions are disrupted. A market disruption event might include exchange closure, trading suspension, material change in the calculation methodology, or failure of the underlying to be available. The consequences typically include postponement of the observation or fixing date, with fallback procedures if the disruption persists. These clauses are critical — during COVID-19, market disruption provisions were triggered across many structured products when exchanges imposed short-selling bans and trading halts.

**Corporate Action Adjustment.** How the trade's terms adjust in response to corporate events affecting the underlying — stock splits, mergers, tender offers, special dividends, and spin-offs. If the underlying stock has a 2-for-1 split, the strike and barrier levels must be adjusted to reflect the new price. The adjustment methodology is specified in the ISDA definitions referenced by the termsheet.

---

### Common Termsheet Misreading Mistakes

1. **Confusing clean price and dirty price.** An investor sees a note quoted at 99.50 and assumes this is what they will pay per 100 of notional. But 99.50 may be the clean price. If the note has been accruing interest for three months at 6%, the accrued interest is approximately 1.50, making the dirty price 101.00. The investor actually pays $10,100,000 on a $10,000,000 notional, not $9,950,000. Always clarify whether a quoted price is clean or dirty.

2. **Ignoring the settlement date gap.** The trade is agreed on Monday, but settlement is T+2 — Wednesday. If the investor is expecting to fund on Monday, they will miss the settlement. Worse, if the investor needs the redemption proceeds on the maturity date itself, they will not receive funds until T+2 business days after maturity. The settlement lag affects cash management and must be planned.

3. **Not reading the business day convention.** A quarterly coupon schedule with dates on March 31, June 30, September 30, and December 31 looks straightforward. But under Modified Following, if any of these dates falls on a weekend or holiday, the adjusted date changes — and with it, the accrual period and the coupon amount. Ignoring this leads to booking errors that compound across the trade's life.

4. **Skipping the corporate action clause.** An investor buys a Reverse Convertible linked to a stock. Six months later, the company announces a merger. The investor assumes the product will simply continue with the merged company's stock. But the termsheet's corporate action clause may specify that a merger triggers an early termination event, with the calculation agent determining a fair value payment. The investor receives a cash settlement amount that may differ significantly from what they expected. Always read how the product handles mergers, delistings, and tender offers.

5. **Assuming observation = European when it is American.** The termsheet specifies "Barrier Observation: Continuous." The investor reads "barrier at 70%" and mentally calculates that the stock needs to fall 30% by maturity to trigger the knock-in. In reality, continuous observation means the barrier can be triggered at any point during the product's life — including an intraday flash crash that recovers within minutes. The observation convention dramatically changes the probability of the barrier being hit.

6. **Misreading the autocall level as fixed when it is declining.** The termsheet shows an initial autocall level of 100%, but a careful read of the schedule reveals that the level steps down by 5% each year: 100% in year 1, 95% in year 2, 90% in year 3. An investor who only reads the first line assumes the stock must recover to its initial level for autocall. In reality, by year 3, the stock only needs to be at 90% of the initial level. This changes the expected life of the product and, consequently, the expected return.

> **Professor Note:** The most dangerous termsheet misread is not getting a number wrong — it is skipping a section entirely. Specifically, the Market Disruption Event and Corporate Action Adjustment clauses. These clauses sit at the end of the termsheet, buried in legal language, and most people never read them. Until the day a stock gets delisted, a company gets acquired, or an exchange shuts down unexpectedly. Then those clauses become the *only* thing that matters, and the person who did not read them discovers that the trade settles at a price they did not expect, on a date they did not expect, using a methodology they do not understand. Read every clause. Especially the ones you think will never apply.

---

## 6.3 Documentation & Legal Framework

*What the contract means — the legal architecture that governs structured product trades*

### Building Codes and Blueprints

If the termsheet is a blueprint, the ISDA Master Agreement is the building code. The termsheet says *what* you are building. The Master Agreement says what happens if things go wrong.

A city does not require building codes because buildings always collapse. It requires them because when a building *does* have a problem — a fire, a flood, an earthquake — there must be pre-established rules for how to respond. Who is responsible? What are the minimum safety standards? How is damage assessed?

The legal framework for structured products works the same way. The ISDA Master Agreement, the CSA, and the confirmations exist not for the 99% of trades that settle normally, but for the 1% where something goes wrong — a counterparty defaults, a market disruption occurs, a force majeure event strikes. The legal documentation is the contingency plan.

Every structured product lives inside this legal architecture. Understanding it is essential not because you will negotiate ISDA agreements (that is the job of the legal team), but because the documentation affects how the desk books, values, and risk-manages every trade.

---

### ISDA Master Agreement

The **ISDA Master Agreement** (published by the International Swaps and Derivatives Association) is the foundation of the global derivatives market. It is a standardized contract that governs all over-the-counter derivative trades between two parties.

**Why it exists.** Without the ISDA Master Agreement, every single derivative trade would require its own standalone contract. Two banks that trade 500 derivatives between them would need 500 separate legal agreements, each negotiated from scratch. This would be impractical, expensive, and slow.

The ISDA Master Agreement solves this by creating a single umbrella contract. Once two parties sign a Master Agreement, every subsequent derivative trade between them is governed by that agreement. Individual trades are documented as "Confirmations" — short documents that specify the economic terms of each trade by reference to the Master Agreement's standard terms.

**Structure.** The ISDA documentation architecture has three layers:

| Layer | What It Is | How It Works |
|-------|-----------|-------------|
| **Master Agreement** | The standard contract (published by ISDA, rarely modified) | Sets the baseline rules: events of default, termination, netting, representations |
| **Schedule** | The negotiated modifications to the Master Agreement | Customizes the standard terms: threshold amounts, cross-default provisions, additional termination events, elections |
| **Confirmations** | The trade-specific documents | Records the economic terms of each individual trade: notional, coupon, dates, underlying |

Think of it as a franchise agreement. The Master Agreement is the franchise manual (standard rules). The Schedule is the local customization (we agreed to modify rules 7 and 12 for our specific relationship). Each Confirmation is an individual transaction within the franchise (today we did this specific trade).

**Events of Default.** These are the triggers that allow one party to terminate all outstanding trades with the other. The standard events include:

- **Failure to Pay.** A party fails to make a payment when due and does not remedy the failure within the grace period (typically 1-3 business days).
- **Breach of Agreement.** A party violates a term of the Master Agreement or Schedule and does not cure the breach within 30 days of notice.
- **Credit Support Default.** A party fails to meet its collateral obligations under the CSA (see below).
- **Misrepresentation.** A representation made by a party proves to have been materially false.
- **Default Under Specified Transaction.** A party defaults on another specified financial transaction (cross-default).
- **Cross Default.** A party defaults on other indebtedness above a specified threshold amount.
- **Bankruptcy.** A party files for bankruptcy, becomes insolvent, or has a receiver appointed.
- **Merger Without Assumption.** A party merges with another entity that does not assume the obligations under the Master Agreement.

When an Event of Default occurs, the non-defaulting party has the right (but not the obligation) to designate an Early Termination Date — the date on which all outstanding trades are terminated and netted.

**Termination Events.** Unlike Events of Default (which involve fault), Termination Events are no-fault triggers. Neither party did anything wrong, but circumstances make it impossible or impractical to continue the trades.

- **Illegality.** A change in law makes it illegal for one party to perform its obligations.
- **Force Majeure.** An event beyond the parties' control (natural disaster, war, pandemic, exchange closure) prevents performance for a sustained period.
- **Tax Event.** A change in tax law results in one party being required to gross up payments (pay additional amounts to compensate for withholding taxes).
- **Tax Event Upon Merger.** A merger triggers a tax event that would not have occurred absent the merger.

**Close-Out Netting.** When trades are terminated early (whether due to default or a termination event), all outstanding transactions under the Master Agreement are valued and netted to a single amount. One party owes the other a net payment.

Why does this matter? Without netting, the defaulting party could selectively honor profitable trades and walk away from losing ones. Netting prevents this cherry-picking by aggregating all trades to a single net exposure.

Example: Bank A and Bank B have 50 outstanding derivatives. Bank A is in-the-money on 30 trades (aggregate value: +$200M) and out-of-the-money on 20 trades (aggregate value: -$180M). Under close-out netting, the net exposure is $20M — Bank B owes Bank A $20M. Without netting, Bank B could default on the 30 losing trades (-$200M to Bank B) while demanding payment on the 20 profitable trades (+$180M to Bank B), creating a gross exposure of $380M instead of a net exposure of $20M.

**Payment Netting.** Distinct from close-out netting, payment netting aggregates payments in the same currency due on the same date. If Bank A owes Bank B $5M in USD on March 15, and Bank B owes Bank A $3M in USD on March 15, payment netting reduces this to a single payment: Bank A pays Bank B $2M. This reduces settlement risk and operational complexity.

**The Schedule.** The Schedule is where the two parties customize the Master Agreement for their specific relationship. Key negotiated terms include:

- **Threshold Amount.** The exposure level below which collateral is not required (see CSA section below).
- **Cross-Default Threshold.** The amount of other indebtedness default that triggers cross-default.
- **Specified Entities.** Affiliates whose default can trigger cross-default.
- **Additional Termination Events.** Custom triggers beyond the standard list (for example, a credit rating downgrade below a specified level).
- **Transfer provisions.** Whether and how trades can be transferred to affiliates.

**2002 vs 1992 Master Agreement.** The 1992 ISDA Master Agreement used two alternative methods for determining the close-out amount: "Market Quotation" (obtaining dealer quotes) and "Loss" (calculating a party's actual loss). The 2002 version replaced both with a single "Close-out Amount" methodology, which gives more flexibility and is generally considered more robust. Most new relationships now use the 2002 version, but many legacy agreements from the 1992 era remain in effect.

---

### CSA (Credit Support Annex)

The **Credit Support Annex** is the collateral agreement that sits alongside the ISDA Master Agreement. If the Master Agreement is the building code, the CSA is the insurance policy — it reduces the risk of loss if the building catches fire.

**Why it exists.** When two parties have outstanding derivatives, they are exposed to each other's credit risk. If Bank A owes $50M to Bank B, and Bank A defaults, Bank B may lose the full $50M. The CSA reduces this exposure by requiring the party that is "out of the money" (the party that owes more) to post collateral — assets that the other party can seize in the event of default.

**Key terms:**

**Threshold.** The exposure level below which no collateral is required. If the threshold is $10M, the out-of-the-money party does not need to post collateral until the exposure exceeds $10M. A threshold of zero means collateral is required from the first dollar of exposure. Lower thresholds provide better credit protection but impose greater operational and funding costs.

**Independent Amount (IA).** Additional collateral that must be posted regardless of the current exposure. Similar to initial margin in exchange-traded futures. The IA provides a buffer against sudden adverse moves. For example, a CSA might require a $5M Independent Amount plus collateral on any exposure above the threshold.

**Minimum Transfer Amount (MTA).** The minimum amount of collateral that must be transferred in any single call. If the MTA is $250,000, a collateral call for $200,000 would not be made — the exposure would need to exceed the threshold by at least $250,000 before a transfer is triggered. The MTA avoids the operational burden of transferring trivially small amounts of collateral every day.

**Eligible Collateral.** Not all assets can be posted as collateral. The CSA specifies which types are acceptable:

| Collateral Type | Typical Haircut | Why the Haircut |
|----------------|----------------|-----------------|
| Cash (USD, EUR, GBP) | 0% | Cash is cash — no price risk |
| US Treasuries (< 1 year) | 0.5% - 1% | Minimal price risk, highly liquid |
| US Treasuries (1-10 years) | 1% - 3% | Some interest rate risk |
| US Treasuries (> 10 years) | 3% - 6% | Significant interest rate risk |
| Government bonds (G7) | 1% - 5% | Similar to Treasuries, with some liquidity variance |
| Corporate bonds (investment grade) | 5% - 15% | Credit risk and liquidity risk |
| Equities (major indices) | 10% - 25% | Price volatility |

**Haircuts.** The percentage reduction applied to the market value of non-cash collateral. If an entity posts $10M in 10-year US Treasuries and the haircut is 3%, the collateral is valued at $9.7M for the purpose of meeting the collateral requirement. Haircuts protect against the risk that the collateral itself loses value — if the posting party defaults and the collateral must be liquidated, the haircut provides a buffer against adverse price moves during the liquidation period.

**Valuation Agent.** The party responsible for calculating the exposure and making collateral calls. Typically one of the two counterparties (often alternating, or the party with the larger portfolio). The Valuation Agent runs the mark-to-market, compares it against the threshold and MTA, and issues a collateral call (or return) as appropriate.

**Dispute Resolution.** If the two parties disagree on the exposure calculation (which happens regularly, as each party uses its own pricing models), the CSA specifies a dispute resolution process. Typically, the disputing party must still post the undisputed amount (the lower of the two calculated amounts) while the dispute is resolved. The resolution may involve obtaining third-party valuations or averaging the two parties' calculations.

**Bilateral vs Cleared CSA.** In bilateral trades (between two specific counterparties), the CSA is negotiated as part of the ISDA documentation. In cleared trades (executed through a central counterparty or CCP), the collateral terms are standardized by the clearinghouse — initial margin and variation margin are calculated centrally, and there is no bilateral negotiation.

**How CSA terms affect XVA.** The CSA terms directly influence the valuation adjustments (XVA) discussed in Section 6.7. A CSA with a zero threshold and daily margin calls significantly reduces Credit Valuation Adjustment (CVA) because the counterparty exposure is continuously collateralized. A CSA with a high threshold or infrequent margin calls leaves more uncollateralized exposure, increasing CVA. The Funding Valuation Adjustment (FVA) is affected by the cost of funding the collateral posted. The collateral currency (a CSA might specify USD cash as eligible collateral) affects the discount rate used for valuation.

---

### Confirmations

A **confirmation** is the trade-specific document that records the economic terms of an individual derivative transaction under the ISDA Master Agreement. If the Master Agreement is the franchise manual and the Schedule is the local customization, the confirmation is the receipt for each individual order.

**What a confirmation contains:** All the economic terms from the termsheet (Section 6.2) are replicated in the confirmation, plus references to the applicable ISDA definitions. The confirmation ties the trade to the legal framework — it says "this trade is governed by the ISDA Master Agreement dated [date] between [Party A] and [Party B], as modified by the Schedule, and the terms of this trade are as set forth below."

**Confirmation matching.** Both parties must agree on every term in the confirmation. After a trade is executed, each side produces its version of the confirmation. The operations teams compare the two versions (a process called "matching") and resolve any discrepancies. A matched confirmation means both parties agree on all terms.

**Long-form vs short-form confirmations:**

- **Long-form confirmation:** Contains all terms explicitly, including definitions that would otherwise be incorporated by reference. Used for complex or non-standard trades where precision is critical.
- **Short-form confirmation:** References the ISDA definitions and Master Confirmation Agreement (if one exists) for standard terms, and only specifies the trade-specific variables (notional, dates, levels). Used for standard, repeat trade types.

**Master Confirmation Agreements (MCAs).** When two parties regularly trade the same type of product (for example, they trade Phoenix Autocallables every week), they may negotiate an MCA that pre-agrees the standard terms for that product type. Each individual trade then requires only a brief "transaction supplement" specifying the variable terms (notional, coupon, underlying, dates). MCAs dramatically reduce documentation time and confirmation backlog.

**Confirmation backlog risk.** Unconfirmed trades create operational and legal risk. If a trade is executed but not confirmed, and a dispute arises, the parties may disagree on the terms. Regulators (including the SEC, FCA, and ESMA) require firms to confirm trades within specified timeframes. A large confirmation backlog is a red flag in regulatory examinations and internal audits.

---

### Novation & Assignment

Derivatives contracts are bilateral — they exist between two specific parties. But circumstances change, and sometimes one party needs to transfer its position to a third party.

**Novation.** Replacing one party to a trade with a new party. The original trade between Party A and Party B is terminated, and a new trade is established between Party A and Party C, on the same economic terms. All three parties must consent.

*Analogy:* You have a gym membership contract with Gym X. You want to transfer it to your friend. The gym, you, and your friend all must agree. The gym cancels your membership and creates a new one for your friend on the same terms.

**When novation is used:**
- A client wants to exit a trade before maturity (they novate their position to another counterparty).
- A bank is restructuring its portfolio and transfers trades from one entity to another.
- A counterparty is acquired, and the acquiring entity assumes the positions.
- Portfolio rebalancing — a hedge fund wants to consolidate its derivatives positions with fewer counterparties.

**Process:** Novation follows the ISDA Novation Protocol. The transferor (outgoing party) proposes the novation. The remaining party (the party that is not changing) must consent. The transferee (incoming party) must agree to assume the obligations. The trade is then "stepped" — the original trade is terminated and a new trade is created, with the transferee stepping into the transferor's shoes.

**Assignment.** Transferring rights under a contract to a third party. Unlike novation, assignment transfers *rights* (the right to receive payments) but may not transfer *obligations* (the obligation to make payments) without consent. Assignment is more limited than novation and is less common in derivatives markets, where obligations are as important as rights.

The key distinction: novation replaces a party entirely (rights AND obligations). Assignment transfers specific rights and may leave the original party with continuing obligations.

---

### Legal Events

Structured products exist in the real world, and the real world does not always cooperate with financial models. The legal framework must address what happens when the assumptions underlying the trade break down.

**Market Disruption Event.** A condition that prevents the calculation agent from determining a price or rate in the normal way. Examples include:

- **Exchange closure:** The relevant stock exchange is closed on a scheduled observation date (beyond the normal holiday calendar).
- **Trading suspension:** The underlying security is suspended from trading by the exchange.
- **Material change in formula:** The index calculation methodology is materially changed.
- **Failure of the underlying to trade:** The underlying is listed but no trades occur at or near the relevant time.

**Consequences of a Market Disruption Event:**

The termsheet's market disruption provisions typically specify a cascading set of responses:

1. **Postponement.** The observation or fixing date is moved to the next scheduled trading day that is not a disrupted day.
2. **Maximum postponement period.** If the disruption persists for a specified number of trading days (typically 5-8), the postponement ends and the calculation agent uses its best estimate of the price that would have prevailed.
3. **Fallback determination.** If the maximum postponement period expires, the calculation agent determines the price in good faith using whatever information is available.

**Additional Disruption Events.** These are events that affect the parties' ability to trade or hedge, rather than the underlying itself:

- **Change in Law.** A change in law or regulation makes it illegal, impractical, or materially more expensive for a party to maintain its hedge position.
- **Insolvency Filing.** The issuer of the underlying security files for bankruptcy.
- **Hedging Disruption.** A party is unable to hedge or maintain its hedge for the trade due to market conditions.
- **Increased Cost of Hedging.** A material increase in the cost of maintaining the hedge (for example, due to new taxes or regulatory requirements).

**Extraordinary Events.** These are corporate events affecting the underlying that go beyond normal corporate actions:

- **Merger Event.** The underlying company merges with or is acquired by another entity. The trade terms may need to be adjusted to reference the surviving entity, or the trade may be terminated.
- **Tender Offer.** A party offers to buy a significant percentage of the outstanding shares. This may trigger a delisting or liquidity event.
- **Delisting.** The underlying is removed from trading on its primary exchange. The calculation agent must determine how to continue observing the underlying, or may terminate the trade.
- **Nationalization.** A government takes ownership of the underlying entity.

**Force Majeure.** An event beyond the control of either party that prevents performance. The ISDA Master Agreement (2002 version) includes a force majeure provision that applies when an event "beyond the control of the parties" and "that could not, after all reasonable efforts, be overcome" prevents a party from making or receiving payments.

The standard process: a waiting period of up to 8 local business days, after which either party may designate an early termination date. The terminated trades are valued at fair value (Close-out Amount), and the net payment is made.

The COVID-19 pandemic tested force majeure provisions extensively. In most cases, derivatives trades continued because electronic markets remained open, but the experience reinforced the importance of understanding exactly what the documentation says — and what it does not say.

---

### Close-Out Netting (Deeper)

Close-out netting is so important to the functioning of the derivatives market that it deserves deeper treatment.

**What it means in practice.** Upon an Event of Default, the non-defaulting party:

1. Designates an Early Termination Date.
2. Calculates the Close-out Amount for each terminated transaction.
3. Nets all Close-out Amounts, together with any unpaid amounts, to a single net figure.
4. One party pays the other the net amount.

**Why it matters for capital and credit.** Without netting, a bank's credit exposure to a counterparty equals the sum of all positive mark-to-market values across all trades. With netting, the exposure equals the *net* mark-to-market across all trades. This difference is enormous.

Example: A bank has 200 trades with a counterparty. 100 trades have positive MTM (the counterparty owes the bank) totaling $500M. 100 trades have negative MTM (the bank owes the counterparty) totaling $480M.

| Measure | Without Netting | With Netting |
|---------|----------------|--------------|
| Credit exposure | $500M (sum of all positive) | $20M (net of all trades) |
| Capital required (simplified) | Based on $500M | Based on $20M |

The capital savings from netting are substantial. This is why banks insist on signing ISDA Master Agreements before trading — without the legal framework for netting, the capital cost of each trade would be dramatically higher.

**Netting enforceability.** Close-out netting only works if it is legally enforceable in the defaulting party's jurisdiction. If a court in the defaulting party's country does not recognize netting — for example, if local bankruptcy law requires all creditors to be treated equally and does not permit netting of bilateral obligations — then the netting agreement has no effect.

Banks obtain legal opinions (typically from ISDA or from local counsel) confirming the enforceability of netting in each jurisdiction where they have counterparties. These netting opinions are maintained and updated regularly. Trading with counterparties in jurisdictions where netting is not enforceable requires significantly more credit risk capital and is approached with caution.

---

### Compression & Tear-Up

Over time, a derivatives portfolio between two counterparties accumulates trades — many of which partially or fully offset each other. Compression and tear-up are mechanisms for cleaning up this accumulated complexity.

**Portfolio Compression.** The process of terminating offsetting positions and replacing them with a smaller number of trades that produce the same net economic exposure. Two parties with 500 outstanding swaps might find that 300 of them can be replaced by 50 trades, with identical net cash flows.

Compression is typically facilitated by a third-party service provider (such as TriOptima or Capitalab) that analyzes the portfolios of multiple dealers simultaneously to identify the maximum number of trades that can be eliminated.

**Tear-Up.** The voluntary termination of a trade before maturity. The two parties agree to cancel the trade, with one party making a payment to the other equal to the current mark-to-market value.

**Why desks do compression and tear-up:**

- **Reduce operational burden.** Fewer trades means fewer confirmations to match, fewer payments to process, fewer mark-to-market calculations, and fewer potential booking errors.
- **Reduce counterparty exposure.** Fewer gross trades reduces the gross notional outstanding, which can reduce capital requirements even when netting is in place (because regulatory capital calculations sometimes use gross notional as an input).
- **Reduce capital requirements.** Regulatory frameworks (Basel III and beyond) impose capital charges based on measures that include gross notional, trade count, and complexity. Compression directly reduces these inputs.
- **Portfolio hygiene.** A cleaner portfolio is easier to risk-manage, easier to explain to regulators, and less prone to operational errors.

---

### Common Mistakes

1. **Confusing novation with assignment.** Novation replaces a party entirely — both rights and obligations transfer. Assignment transfers rights only and may not relieve the assigning party of its obligations. If a desk professional processes an assignment as a novation (or vice versa), the legal status of the trade is incorrect. The original party may still be on the hook for obligations they believe were transferred.

2. **Not checking netting enforceability.** A desk assumes that close-out netting will work because the ISDA Master Agreement is in place. But if the counterparty is domiciled in a jurisdiction where netting is not legally enforceable, the agreement is worthless in a default scenario. The bank's credit exposure is the gross amount, not the net. Always verify that a valid netting opinion exists for the counterparty's jurisdiction.

3. **Ignoring the Minimum Transfer Amount in collateral disputes.** During a dispute, one party calculates the exposure at $12M, the other at $9M. The CSA threshold is $10M and the MTA is $500,000. Party A believes it is owed $2M in collateral ($12M - $10M threshold). Party B believes no collateral is due ($9M is below the $10M threshold). Under dispute resolution, the undisputed amount must be posted — but if the undisputed excess is below the MTA, no transfer occurs. Desk professionals who ignore the MTA during disputes create unnecessary friction with counterparties and may escalate situations that should resolve naturally.

4. **Assuming all collateral is eligible.** A counterparty attempts to post corporate bonds as collateral. The CSA may only permit cash and government bonds. Accepting ineligible collateral — even temporarily — can create legal ambiguity about whether the collateral is enforceable. Always verify eligibility against the CSA before accepting any non-cash collateral.

5. **Failing to update the confirmation backlog.** A desk executes trades faster than Operations can confirm them. After a month, there are 50 unconfirmed trades. If a dispute arises on any of those trades, there is no bilateral agreement on the terms. Regulators view confirmation backlogs as evidence of weak controls. A backlog above regulatory thresholds triggers supervisory action and can restrict the desk's ability to trade.

> **Professor Note:** If you remember only one thing from this section, remember this: the ISDA Master Agreement is not a document you sign and forget. It is the document that determines what happens on the worst day — the day a counterparty defaults, a market shuts down, or a force majeure event strikes. On that day, the Master Agreement, the Schedule, and the CSA are the only things that matter. The termsheet tells you what the trade should have been. The legal documentation tells you what actually happens. Every clause that seemed academic on the day you signed it becomes the governing reality on the day something goes wrong. Respect the documentation. Read the Schedule. Know the CSA terms. Understand what triggers default and what happens when it is triggered. This is not legal trivia — it is operational survival.
