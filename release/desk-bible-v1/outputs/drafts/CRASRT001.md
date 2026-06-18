### Callable Range Accrual SRT

#### Definition

A Callable Range Accrual SRT combines a daily range accrual coupon with an issuer call right. The investor receives a headline coupon that accrues for each day the reference rate stays within a specified range — identical to the NCRA mechanism — but at a higher headline rate, because the investor additionally sells the issuer a Bermudan call option on the note.

This is the highest-yielding product in the SRT family. The dual optionality (range accrual risk plus call risk) generates a coupon that exceeds both the NCRA (range only) and the IR Callable Fixed Rate Note (call only). The investor accepts two independent sources of coupon reduction: out-of-range days produce zero accrual, and an issuer call terminates the note early, forcing reinvestment.

The product provides 100% principal protection at maturity or on call. The longer stated tenor (typically 5-10 years) relative to the NCRA reflects the value of the embedded call — longer-dated calls are worth more, generating a larger coupon enhancement.

#### Construction

The Callable Range Accrual SRT decomposes into three components:

**Component 1 — Fixed-rate bond (long).** Provides 100% principal protection. Redeems at par at maturity or on call.

**Component 2 — Daily digital option strip on SOFR (long).** Identical to the NCRA mechanism. Each business day, the coupon accrues if SOFR is within the range [2.5%, 6.0%]. The wider range (compared to NCRA's [3.0%, 5.5%]) partially compensates for the longer tenor and higher probability of rate excursions over 7 years.

**Component 3 — Bermudan call option (short to investor).** The investor sells the issuer a Bermudan call, exercisable quarterly after a 2-year non-call period. The call premium (1.2% annualised) enhances the headline coupon from the NCRA-equivalent level (~5.3%) to 6.5%.

**Decomposition:**

| Component | Value |
|---|---|
| Headline coupon (maximum) | 6.5% p.a. |
| Range | SOFR 2.5% – 6.0% |
| Callable quarterly after year 2 | |
| Funded by: | |
| — Digital strip cost | 1.5% |
| — Call option premium | 1.2% |
| — Funding | 3.0% |
| — FTP | 0.5% |
| — Desk margin | 0.3% |
| Total funding | 6.5% |

**Coupon enhancement from call:** The NCRA-equivalent headline (range only) would be approximately 5.3%. The call adds 1.2%, bringing the headline to 6.5% — a 120 bps enhancement for accepting call risk.

#### Booking & systems

Callable Range Accrual SRTs are booked in the Murex four-leg framework.

**Note leg.** The structured note with both the range accrual coupon formula and the complete call schedule. Critical fields: headline coupon rate, range bounds (2.5% and 6.0%), reference rate (SOFR), observation type (daily), fixing source, call schedule (quarterly from year 2), first call date, call notification period, and maturity. Both the range bounds and the call schedule must be complete.

**Issuer leg.** Standard funding fields. Funding cost applies to the accreting exposure over the longer tenor.

**Deposit leg.** Standard deposit fields.

**Hedge leg.** Contains two instruments: (1) a daily digital caplet/floorlet strip replicating the range condition, and (2) a Bermudan receiver swaption replicating the issuer's call right. The two hedges interact — the call affects the expected life of the digital strip. The combined hedge portfolio must be valued jointly, not independently, to capture the correlation between range accrual and call exercise.

**Termsheet** defines both the range accrual terms and the call terms. A critical term is the treatment of accrued coupon on call: the investor typically receives par plus any accrued (but unpaid) range coupon calculated to the call date. The accrual count must be frozen on the call notice date or the call settlement date — the termsheet specifies which.

#### Pricing intuition

Callable Range Accrual pricing involves two interacting embedded options — making it the most complex pricing challenge in the SRT family.

**Dual optionality interaction.** The range accrual and the call option are not independent. When rates fall, two things happen simultaneously: (1) the rate may still be in-range (maintaining accrual), and (2) the issuer's incentive to call increases. The call effectively caps the benefit of in-range periods — the investor cannot earn the full-life accrual if the issuer calls early.

**Rate volatility — mixed effect.** Higher rate vol simultaneously (1) reduces expected accrual (wider rate distribution, more out-of-range days) and (2) increases call option value (more valuable for the desk). Both effects work against the investor, but they are partially correlated — the net impact requires joint modelling.

**Effective duration.** The effective duration is shorter than the stated maturity due to the call and ranges between the first call date and maturity. The range accrual adds a further complication: the effective duration is path-dependent because the rate path determines both the accrual and the call exercise.

**Greeks:**
- DV01: Complex — rate level affects both range probability and call probability simultaneously
- Vega: Short from both sources (range digital and Bermudan swaption). Double short vol position.
- Call delta: Short — issuer exercises in the investor's unfavourable scenario
- Gamma: Concentrated near range boundaries and near the call exercise boundary
- Convexity: Negative (from both call and range features)

#### Worked example (USD 10M)

**Terms:** USD 10M notional, 7-year maturity, 6.5% headline coupon, SOFR range 2.5%–6.0%, quarterly call after year 2.

**Decomposition:**

| Component | Annualised |
|---|---|
| Headline coupon (maximum) | 6.5% |
| Digital strip cost | 1.5% |
| Call option premium | 1.2% |
| Funding | 3.0% |
| FTP | 0.5% |
| Desk margin | 0.3% |
| Total funding sources | 6.5% |

**Verification:** 1.5% + 1.2% + 3.0% + 0.5% + 0.3% = 6.5%. Matches headline coupon.

**Scenario 1 — rates stable at 4.0%, no call for 7 years:**
- In-range accrual: ~95% (wide range, rate well within)
- Effective coupon: 6.5% × 95% = 6.175% p.a.
- 7-year total coupon: USD 10M × 6.175% × 7 = USD 4,322,500
- Best-case outcome for the investor

**Scenario 2 — rates fall to 2.0% after year 2, issuer calls:**
- Year 1-2 accrual: ~90% (rate in range)
- Year 2 coupon earned: 6.5% × 90% × 2 = 11.7% total
- Issuer calls at year 2: investor receives par + accrued
- Total coupon: USD 10M × 11.7% = USD 1,170,000
- Investor must reinvest at lower rates. Effective yield: 5.85% for 2 years only.

**Scenario 3 — rates volatile, frequent range breaches, no call:**
- Average accrual: ~65%
- Effective coupon: 6.5% × 65% = 4.225% p.a.
- 7-year total coupon: USD 10M × 4.225% × 7 = USD 2,957,500
- Below comparable fixed rate. Investor would have been better off with a bullet bond.

#### Reconciliation specifics

**Range bounds and call schedule (dual critical).** Both the range bounds and the complete call schedule must be verified between the note leg and the hedge leg. Unlike the NCRA (range only) or the IR Callable FRN (call only), the Callable Range Accrual has two independent sets of critical parameters that must each be complete and consistent.

**Accrued coupon on call (unique to callable range accruals).** When the issuer calls, the investor receives par plus accrued range coupon to the call date. The accrual count — how many in-range days occurred in the stub period between the last coupon payment and the call date — must be computed correctly. If the accrual count is frozen on the wrong date (call notice vs call settlement), the coupon differs. This is the single most complex recon item in the SRT family.

**Hedge interaction on call.** When the issuer exercises the call, the digital strip must be terminated along with the note. If the hedge leg does not terminate the digital strip simultaneously, the desk has an unhedged position in daily digitals after the call. Murex must be configured to terminate both hedge instruments on call exercise.

**Daily observation type.** Same as NCRA — must be daily, not period-end. The callable feature does not change the accrual observation convention.

#### Desk view

**Who buys this product.** Sophisticated institutional investors seeking maximum SRT yield. Insurance companies with long-dated liabilities and a view that rates will remain range-bound. Asset managers who can accept both accrual variability and early termination.

**The real risk.** Dual risk concentration: the worst outcome is rates falling out of range (low accrual) followed by an issuer call (early termination). The investor earns a low coupon for a short period, then must reinvest in an unfavourable environment. The double short vol position means both risks intensify simultaneously when volatility increases.

**When appropriate.** Stable rate environments with long investment horizons. Wide ranges with high in-range probability. Investors who can tolerate reinvestment risk and understand the call-accrual interaction.

**When not appropriate.** Volatile rate environments (dual risk amplification). Short investment horizons. Investors requiring income certainty. Investors who do not understand the interaction between range accrual and call exercise.

#### Desk shorthand

*Range coupon, callable; dual optionality, highest SRT yield.*
