### Accreting Fixed Rate Note

#### Definition

An Accreting Fixed Rate Note pays a fixed coupon on a notional amount that increases over time according to a predetermined schedule. Unlike a bullet bond where the notional remains constant, the AFRN's notional steps up at specified dates, increasing the absolute coupon payment and the interest rate exposure in later periods.

The accretion schedule is deterministic — there are no triggers, barriers, or conditions. The notional increases are locked in at issuance. This makes the AFRN the simplest non-bullet structure in the SRT family: a pure fixed-rate instrument with a time-varying notional.

The investor's primary trade is accepting back-loaded cash flows and increasing duration in exchange for a yield pickup over a comparable bullet bond. The weighted-average life (WAL) is longer than that of a bullet with the same maturity, and the DV01 grows as the notional accretes — meaning rate sensitivity increases over the life of the note.

#### Construction

The AFRN is a single-component structure:

**Component — Fixed-rate bond with accreting notional.** The note pays a fixed coupon (4.2% p.a.) on a notional that starts at USD 10M and increases to USD 15M according to a step-up schedule. The accretion typically begins after an initial flat period and follows a linear or step-function pattern.

**Notional schedule (illustrative):**

| Year | Notional | Coupon Payment |
|-----:|--------:|--------------:|
| 1 | USD 10M | USD 420,000 |
| 2 | USD 10M | USD 420,000 |
| 3 | USD 11.25M | USD 472,500 |
| 4 | USD 12.50M | USD 525,000 |
| 5 | USD 15M | USD 630,000 |

**Total coupon over 5 years:** USD 2,467,500
**Weighted-average life:** 4.1 years (vs 5.0 years for a bullet of same maturity)
**Comparable bullet yield (4.1Y):** 3.8%
**AFRN yield pickup:** 40 bps

There is no embedded optionality — no call, no floor, no cap, no barrier. The cash flows are fully deterministic at issuance.

#### Booking & systems

AFRNs are booked in the Murex four-leg framework.

**Note leg.** The structured note with the full accreting notional schedule. Critical fields: initial notional, each accretion step (date and new notional level), fixed coupon rate, coupon frequency, day count convention, and maturity date. The notional schedule must be entered as a complete table — partial entry causes incorrect coupon calculations on accretion dates.

**Issuer leg.** The issuer's internal funding cost. Standard fields: funding rate, funding curve, and credit spread. The funding cost is computed on the accreting notional, not the initial notional.

**Deposit leg.** Client collateral. Standard fields. Deposit rate, tenor, and rollover convention.

**Hedge leg.** An accreting interest rate swap (pay fixed, receive floating) with a notional schedule that exactly matches the note leg. The hedge swap must accrete on the same dates and to the same levels as the note. A mismatch between the note and hedge notional schedules creates unhedged rate exposure that grows over time.

**Termsheet** defines the complete accretion schedule, coupon rate, and whether the coupon is computed on the current (accreted) notional or the initial notional. This distinction is critical — some structures compute the coupon on the initial notional and accrete only for redemption, while others accrete the coupon base.

#### Pricing intuition

AFRN pricing is straightforward — deterministic cash flows discounted at the appropriate rate.

**No model risk.** All cash flows are known at issuance. The pricing is pure discounted cash flow (DCF) analysis. There are no embedded options, no stochastic elements, and no model calibration. This is the simplest pricing in the SRT family.

**Back-loaded DV01.** The key risk characteristic is that DV01 (dollar value of a 1 bps rate move) increases over the note's life as the notional accretes. In year 1, the DV01 reflects USD 10M notional. By year 5, it reflects USD 15M. This means rate moves in later years have 50% more P&L impact than identical moves in year 1.

**WAL vs maturity.** The weighted-average life (4.1 years) is the relevant duration measure, not the stated maturity (5 years). WAL accounts for the time-weighting of all cash flows including the accreting notional. Comparable bonds should be matched on WAL, not maturity.

**Greeks:**
- DV01: Increasing over time (proportional to accreted notional)
- Duration: WAL-based, positive, no optionality adjustment needed
- Convexity: Positive (standard fixed-rate instrument)
- Vega: Zero (no embedded options)

#### Worked example (USD 10M)

**Terms:** USD 10M initial notional, 5-year maturity, 4.2% fixed coupon, accreting to USD 15M over years 3-5.

**Decomposition:**

| Component | Value |
|---|---|
| Fixed coupon | 4.2% p.a. |
| Funding cost | 3.0% |
| FTP | 0.3% |
| Desk margin | 0.1% |
| Investor yield pickup (vs 4.1Y bullet) | 0.8% |

**Verification:** 3.0% + 0.3% + 0.1% + 0.8% = 4.2%. Matches coupon.

**Scenario 1 — rates fall 50 bps after year 2 (notional now accreting):**
- Year 3 notional: USD 11.25M
- DV01 at year 3: ~USD 4,613 per bps (vs ~USD 4,100 at year 1)
- Mark-to-market gain amplified by higher notional
- Gain approximately USD 4,613 × 50 = USD 230,650

**Scenario 2 — rates unchanged:**
- Investor earns 4.2% on accreting notional for 5 years
- Total coupon: USD 2,467,500
- Principal returned: USD 15M (final accreted notional)
- Effective yield: 4.2% on WAL of 4.1 years

**Scenario 3 — rates rise 50 bps after year 2:**
- Mark-to-market loss amplified by accreting notional
- Loss increases year-over-year as DV01 grows
- No credit loss at maturity — full final notional returned
- Opportunity cost: locked into 4.2% when market now pays 4.7%

#### Reconciliation specifics

**Notional schedule (most critical).** The complete accretion schedule — every step date and new notional level — must match exactly between the Murex note leg and the hedge leg (accreting swap). A single mismatched accretion step creates an unhedged notional gap that grows until the next correct step. For a 5-year note with 3 accretion steps, all 3 must be verified.

**Coupon base.** The termsheet specifies whether the coupon is computed on the current (accreted) notional or the initial notional. If the note leg computes coupon on accreted notional but the hedge leg uses initial notional, the coupon payments diverge on every accretion date — a systematic error.

**Accretion dates vs coupon dates.** Accretion steps should align with coupon payment dates. If they do not (e.g., notional accretes mid-period), the stub coupon calculation requires careful handling. Verify that Murex handles the stub correctly and that the hedge swap uses the same convention.

**Redemption amount.** At maturity, the investor receives the final accreted notional (USD 15M in the example), not the initial notional. The redemption leg must reflect the final notional.

#### Desk view

**Who buys this product.** Insurance companies and pension funds with liability schedules that naturally increase over time (growing liabilities). Asset managers seeking back-loaded duration to match long-dated obligations. Investors with a bullish rates view who want increasing exposure as their conviction builds.

**The real risk.** Back-loaded rate exposure means the worst P&L scenario occurs when rates rise in the later years — exactly when the notional (and therefore the loss) is largest. The investor cannot reduce exposure without selling the note, and the accreting structure makes it harder to find a buyer at fair value in a rising-rate environment (back-loaded duration is less liquid).

**When appropriate.** Falling or stable rate environments. Liability matching with growing obligations. Investors who understand and want increasing rate exposure.

**When not appropriate.** Rising rate environments (amplified losses). Need for stable or decreasing rate exposure. Liquidity-constrained investors (harder to exit than bullet bonds).

#### Desk shorthand

*Step-up notional; fixed coupon, back-loaded duration.*
