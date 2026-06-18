### Range-Accrual Steepener

#### Definition

A Range-Accrual Steepener pays a coupon that accrues only on days when the CMS spread (CMS 30Y − CMS 10Y) falls within a specified range. The headline coupon rate is applied pro-rata: if the spread is inside the range for 220 out of 260 business days in a year, the investor receives 220/260 of the headline coupon.

The coupon formula is:

**Coupon = 6.0% × (N_in / N_total)**

where N_in is the number of days the CMS 30Y − CMS 10Y spread is within [0 bps, 150 bps] and N_total is the total observation days in the period.

This product merges two concepts: the leveraged curve slope exposure of a steepener (see VSTEG001) with the daily digital observation of a range accrual (see NCRA001 in SRT). The headline coupon (6.0%) is higher than the vanilla steepener's expected coupon (~4.0%) because the investor accepts accrual risk — the possibility of earning less than the full headline when the spread moves outside the range.

The note is non-callable. The investor's principal is returned in full at maturity regardless of coupon outcomes.

#### Construction

The Range-Accrual Steepener decomposes into three components:

**Component 1 — Fixed-rate bond (funding).** The note's principal structure. Provides par redemption at maturity. Identical to the funding component in VSTEG001.

**Component 2 — CMS spread range-accrual coupon strip.** A series of semi-annual coupons, each determined by how many days during the period the CMS 30Y − CMS 10Y spread was inside the [0 bps, 150 bps] range. Each day's observation is independent — the spread is either in range (accrues 1/N_total of coupon) or out of range (accrues nothing for that day).

**Component 3 — Digital CMS spread strip (embedded).** The range accrual mechanism is economically a strip of daily digital options on the CMS spread. Each day, the investor receives a binary payoff: full daily accrual if the spread is in range, zero if not. The desk hedges this with a digital CMS spread strip that replicates the daily in/out observation.

**Comparison to VSTEG001:** The vanilla steepener pays a leveraged linear function of the CMS spread. This product pays a fixed rate conditional on the spread being in a specified range. The linear leverage of VSTEG001 is replaced by a binary (digital) mechanism — higher headline, but all-or-nothing on each observation day.

**Comparison to NCRA001:** NCRA001 applies range accrual to a single rate (SOFR). This product applies range accrual to a CMS spread — a two-rate quantity. The additional complexity comes from modeling the joint distribution of CMS 30Y and CMS 10Y, including their correlation and individual convexity adjustments.

#### Booking & systems

Range-Accrual Steepeners are booked in the Murex four-leg framework.

**Note leg.** The structured note carrying the CMS spread range-accrual formula. Critical fields: headline coupon rate (6.0%), range lower bound (0 bps), range upper bound (150 bps), CMS tenor pair (30Y/10Y), daily observation schedule, CMS fixing source (ISDA CMS rate definition), day count convention, and maturity date.

**Issuer leg.** The issuer's internal funding cost. Standard fields: funding rate, funding curve, and credit spread.

**Deposit leg.** Client collateral. Standard fields: deposit rate, tenor, and rollover convention.

**Hedge leg.** The market risk hedge consists of a digital CMS spread strip replicating the daily range-accrual observations, plus CMS cap/floor structures for the range bounds. Critical fields: digital strike levels (0 bps and 150 bps), CMS tenor pair (30Y/10Y), daily expiry schedule, convexity adjustment model, and correlation assumption. The range bounds must match exactly between the note leg and the hedge leg — a 1 bps discrepancy in either bound creates a systematic accrual mismatch.

**Termsheet** defines the complete observation schedule, range bounds, headline coupon, CMS tenor pair, and fixing source. The observation schedule specifies whether observation days are calendar days or business days — this distinction affects the accrual fraction denominator.

#### Pricing intuition

Range-Accrual Steepener pricing combines the CMS-specific challenges of steepener products with the digital-strip challenges of range-accrual products.

**Spread distribution.** The probability of the CMS spread being inside [0 bps, 150 bps] on any given day depends on the joint distribution of CMS 30Y and CMS 10Y. This distribution is driven by the individual rate dynamics, their correlation, and the convexity adjustments applied to each CMS rate. With the current spread at 80 bps (well inside the range), the historical probability of being in range is approximately 85%.

**Digital risk near boundaries.** When the CMS spread is near 0 bps or 150 bps, small moves determine whether the day accrues or not. This creates high digital gamma — the sensitivity of the expected coupon to small spread movements is maximal near the range boundaries. A spread sitting at 148 bps has a roughly 50% chance of being in or out of range on any given day, making the coupon highly uncertain.

**Convexity adjustment effect.** The convexity adjustment reduces the effective CMS spread by approximately 5 bps. For a range of [0, 150] bps, this shifts the spread distribution leftward, slightly increasing the probability of breaching the lower bound (0 bps) and decreasing the probability of breaching the upper bound (150 bps). The net effect depends on where the current spread sits relative to the range center.

**Greeks:**
- Curve slope (CMS 30Y − CMS 10Y): Primary risk. Determines whether the spread is in range
- Spread volatility: Higher vol → more boundary crossings → lower expected accrual
- Correlation: Affects the width of the spread distribution
- CMS convexity: Shifts the effective spread distribution relative to range bounds
- Digital gamma: Spikes near range boundaries — highest risk when spread is near 0 or 150 bps

#### Worked example (USD 10M)

**Terms:** USD 10M notional, 10-year maturity, semi-annual coupon. Coupon = 6.0% × (days in range / total days). Range: CMS 30Y − CMS 10Y ∈ [0 bps, 150 bps]. CMS fixing source: ISDA CMS.

**Current market:** CMS 30Y = 4.20%, CMS 10Y = 3.40%. Spread = 80 bps (inside range).

**Decomposition:**

| Component | Value |
|---|---|
| Headline coupon | 6.0% p.a. |
| Expected accrual (~85%) | ~5.1% p.a. |
| Digital strip cost | 1.5% |
| Funding cost | 3.0% |
| FTP | 0.4% |
| Desk margin | 0.3% |
| Investor yield pickup | 0.8% |

**Verification:** 1.5% + 3.0% + 0.4% + 0.3% + 0.8% = 6.0%. Matches headline coupon.

**Semi-annual coupon calculation (illustrative period — 130 business days):**

| Step | Calculation | Result |
|---|---|---|
| Days observed | Total business days in period | 130 |
| Days CMS spread ∈ [0, 150] bps | Count of in-range days | 112 |
| Accrual fraction | 112 / 130 | 86.2% |
| Period coupon | 6.0% × 86.2% × 0.5 | 2.586% |
| Semi-annual payment | USD 10M × 2.586% | USD 258,600 |

**Scenario 1 — spread stays at 80 bps (well inside range):**
- Near-100% of days in range
- Expected accrual: ~98%
- Annual coupon: 6.0% × 98% = ~5.88%
- Semi-annual payment: ~USD 294,000

**Scenario 2 — spread widens to 140 bps (near upper boundary):**
- Many days near the 150 bps boundary — high digital risk
- Expected accrual: ~60%
- Annual coupon: 6.0% × 60% = ~3.6%
- Semi-annual payment: ~USD 180,000
- Below funding — investor earning less than cost of carry

**Scenario 3 — curve inverts (spread = −20 bps, below lower boundary):**
- Zero days in range
- Annual coupon: 6.0% × 0% = 0%
- Semi-annual payment: USD 0
- Same outcome as VSTEG001 in inversion — but investor gave up the linear upside of leverage

#### Reconciliation specifics

**Range bounds (most critical).** The lower bound (0 bps) and upper bound (150 bps) must match exactly between the Murex note leg and the hedge leg. A 1 bps error in either bound shifts the accrual probability and creates a systematic mismatch. For example, a 149 bps upper bound in the hedge vs 150 bps in the note means every day the spread is between 149-150 bps produces conflicting accrual/hedge outcomes.

**Observation schedule.** The note leg and hedge leg must agree on whether observation days are business days or calendar days. A business-day schedule produces approximately 260 observations per year; a calendar-day schedule produces 365. The accrual fraction denominator changes accordingly, and a mismatch means the pro-rata coupon calculation diverges between legs.

**CMS fixing source.** Same risk as VSTEG001 — the ISDA CMS rate definition must match between legs. For range-accrual products, the impact is amplified: a fixing source that produces a spread 2 bps wider than the other source will cause accrual disagreements on boundary days across the entire 10-year life.

**Convexity adjustment consistency.** The same model and parameters must be used in both legs. A convexity mismatch shifts the effective spread distribution differently in each leg, causing them to disagree on the probability of being in range.

#### Desk view

**Who buys this product.** Yield seekers who believe the CMS spread will remain in a moderate range (0-150 bps) for the foreseeable future. Insurance companies with a mean-reversion view on curve slope. Investors who want a higher headline coupon than VSTEG001 and are willing to accept the digital (all-or-nothing) accrual mechanism.

**The real risk.** The digital nature of the accrual means the transition from "earning 6%" to "earning 0%" is abrupt. Unlike VSTEG001 where the coupon degrades linearly as the spread narrows, this product maintains the full 6.0% coupon until the spread crosses a boundary — then drops to zero for that day. Near the boundaries, small spread moves create large coupon uncertainty. An investor who chose this over VSTEG001 for the higher headline may find the volatility of realized coupons far exceeds the linear product.

**When appropriate.** Strong conviction that CMS spread stays in [0, 150] bps. Investor understands range-accrual mechanics (from NCRA001 experience or equivalent). Long investment horizon to average out boundary-crossing periods.

**When not appropriate.** Volatile curve slope environment. Investor who cannot tolerate zero-coupon periods. Investor who does not understand digital risk near boundaries.

#### Desk shorthand

*Range coupon on curve slope; daily accrual, CMS spread.*
