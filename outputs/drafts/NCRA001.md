### Non-Callable Range Accrual

#### Definition

A Non-Callable Range Accrual (NCRA) pays an enhanced coupon that accrues on a daily basis, conditional on a reference interest rate staying within a specified range. For each business day the rate is within the range, the investor earns a fraction of the headline coupon. For each day outside, the investor earns nothing for that day. The result is a coupon equal to the headline rate multiplied by the ratio of in-range days to total business days.

The note provides 100% principal protection and is non-callable — the investor holds to maturity with no early redemption risk. The enhanced coupon compensates the investor for accepting the daily accrual risk.

The NCRA is the SRT family's equivalent of the Callable Range Accrual ELN (CRAELN001), but with two key differences: (1) the underlying is an interest rate (SOFR or EURIBOR) rather than an equity index, and (2) there is no embedded call — the product runs to maturity. The absence of a call simplifies the structure but removes the coupon enhancement that a call option would provide.

#### Construction

An NCRA decomposes into two components:

**Component 1 — Fixed-rate bond (long).** Provides 100% principal protection. Redeems at par at maturity.

**Component 2 — Daily digital option strip on SOFR (long).** A strip of daily digital options, one per business day per coupon period. Each digital pays a fraction of the headline coupon (5.5% / number of business days in the period) if SOFR is within the range [3.0%, 5.5%] on that day. The digital strip is replicated as: long a digital floorlet at 3.0% (pays when rate is above the lower bound) and short a digital caplet at 5.5% (cancels the payoff when rate exceeds the upper bound).

**Range mechanics:**

| Rate fixing | In range? | Accrual |
|------------|:---------:|---------|
| SOFR = 4.0% | YES | Headline / N |
| SOFR = 2.8% | NO (below) | 0 |
| SOFR = 5.7% | NO (above) | 0 |

**Decomposition:**

| Component | Value |
|---|---|
| Headline coupon (maximum) | 5.5% p.a. |
| Range | SOFR 3.0% – 5.5% |
| Funded by: | |
| — Digital strip cost | 1.8% (annualised) |
| — Funding | 3.0% |
| — FTP | 0.4% |
| — Desk margin | 0.3% |
| Total funding | 5.5% |

#### Booking & systems

NCRAs are booked in the Murex four-leg framework.

**Note leg.** The structured note with the range accrual coupon formula. Critical fields: headline coupon rate, range lower bound (3.0%), range upper bound (5.5%), reference rate (SOFR), observation type (daily business day), fixing source, accrual formula, coupon payment frequency, and maturity. The range bounds must be entered as exact levels — a 1 bps error shifts the entire accrual probability.

**Issuer leg.** Standard funding fields.

**Deposit leg.** Standard deposit fields.

**Hedge leg.** A strip of daily digital caplets and floorlets replicating the range condition. The hedge must use the same range bounds, the same reference rate, and the same fixing source as the note leg. The digital strip is priced using normal (Bachelier) volatility for SOFR.

**Termsheet** defines the range bounds, the reference rate, the fixing source (e.g., SOFR as published by the Federal Reserve Bank of New York), the observation convention (each New York business day), the boundary treatment (typically "at or above" lower and "strictly below" upper), and the day count for coupon accrual.

#### Pricing intuition

NCRA pricing depends on the probability of the reference rate staying within the range — a function of rate level, rate volatility, and mean reversion.

**Range probability and coupon.** The expected coupon equals the headline rate multiplied by the expected proportion of in-range days. At 85% expected accrual, the effective coupon is 5.5% × 85% = 4.675% — still above the comparable fixed rate of 4.0%. The investor earns a 67.5 bps pickup for accepting accrual risk.

**Rate volatility.** Higher rate volatility increases the probability of the rate moving outside the range, reducing the expected accrual. A 20 bps increase in rate vol might reduce the expected accrual ratio from 85% to 78%, cutting the effective coupon from 4.675% to 4.29%.

**Mean reversion.** Rate mean reversion works in the investor's favour — it pulls the rate back toward the centre of the range after excursions. Strong mean reversion increases the expected accrual ratio. This is why range accruals are more attractive in mean-reverting rate environments.

**Boundary effects.** When the rate is near a range boundary, the daily accrual becomes highly uncertain. A rate at 5.4% (10 bps below the upper bound) has a meaningful probability of fixing above 5.5% on any given day. The desk faces delta and gamma concentrations near boundaries.

**Greeks:**
- DV01: Complex — rate moves affect the accrual probability, not just the discount rate. Net DV01 depends on where the rate is relative to the range.
- Vega (normal): Short. Higher vol reduces expected accrual. The investor is a net seller of rate volatility.
- Gamma: Concentrated near range boundaries. Spikes as the rate approaches either bound.
- Theta: Positive accrual on in-range days; zero on out-of-range days.

#### Worked example (USD 10M)

**Terms:** USD 10M notional, 3-year maturity, 5.5% headline coupon, SOFR range 3.0%–5.5%, quarterly coupon payments, daily observation.

**Decomposition:**

| Component | Annualised |
|---|---|
| Headline coupon (maximum) | 5.5% |
| Digital strip cost | 1.8% |
| Funding | 3.0% |
| FTP | 0.4% |
| Desk margin | 0.3% |
| Total funding sources | 5.5% |

**Verification:** 1.8% + 3.0% + 0.4% + 0.3% = 5.5%. Matches headline coupon.

**Scenario 1 — SOFR stable at 4.0% (mid-range):**
- In-range days: ~252 / 252 = 100%
- Effective coupon: 5.5% × 100% = 5.5%
- Annual coupon: USD 550,000
- 3-year total: USD 1,650,000

**Scenario 2 — SOFR volatile, averaging 4.2% with periodic excursions:**
- In-range days: ~214 / 252 = 85%
- Effective coupon: 5.5% × 85% = 4.675%
- Annual coupon: USD 467,500
- 3-year total: USD 1,402,500

**Scenario 3 — SOFR rises to 6.0% for most of year 2:**
- Year 1 accrual: 90% (rate mostly in range)
- Year 2 accrual: 30% (rate above upper bound for 70% of days)
- Year 3 accrual: 75% (rate drifts back)
- Average accrual: 65%
- Effective coupon: 5.5% × 65% = 3.575%
- Annual coupon: USD 357,500 average
- 3-year total: USD 1,072,500

Principal is returned in full (USD 10M) in all scenarios.

#### Reconciliation specifics

**Range bounds (most critical).** The lower and upper bounds must match exactly between the Murex note leg and the hedge leg (digital strip). A 1 bps shift in a range bound changes the accrual probability on every business day for the life of the note — the cumulative impact on coupon is material. For a 3-year note with ~756 business days, even a small probability shift per day compounds significantly.

**Observation type.** The note leg must be configured for daily (business day) observation, not period-end or monthly. If set to period-end, the system checks the rate once per quarter instead of ~63 times per quarter — a fundamentally different product. This is the most common misconfiguration for range accrual products.

**Reference rate and fixing source.** The SOFR fixing used in the note leg must come from the same source as specified in the termsheet. If the note leg uses a different SOFR publication (e.g., preliminary vs final), the daily in-range determination can differ from the hedge, especially on days when the rate is near a boundary.

**Boundary treatment.** "At or above" the lower bound vs "strictly above" is economically meaningful when the fixing is exactly at the boundary. The termsheet specifies this treatment, and both legs must agree.

#### Desk view

**Who buys this product.** Insurance companies and pension funds seeking enhanced fixed income in stable rate environments. Asset managers with a view that rates will remain range-bound. Yield-hungry investors who understand daily accrual mechanics.

**The real risk.** Coupon variability — the investor cannot predict the exact coupon until each day's fixing is known. In volatile rate environments, the effective coupon can fall well below the headline rate. There is no memory feature — coupons lost on out-of-range days are permanently lost, with no catch-up mechanism.

**When appropriate.** Stable rate environments where the range is centred around the forward rate. Wide ranges with high in-range probability. Low rate volatility.

**When not appropriate.** Rate-trending environments (rate likely to exit range). Narrow ranges (small in-range probability). Investors requiring income certainty. High-volatility periods.

#### Desk shorthand

*Range coupon; daily accrual, rate stays in band.*
