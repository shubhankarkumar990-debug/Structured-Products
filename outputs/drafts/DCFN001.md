### Digital Cap-Floor Note

#### Definition

A Digital Cap-Floor Note pays a binary coupon that switches between a high rate and a low rate depending on whether the reference interest rate is above or below a cap strike on each observation date. If the rate is below the cap strike, the investor receives the high coupon (6.0%). If the rate is above the cap strike, the investor receives the low coupon (1.0%). There is no partial payout — the outcome on each observation date is strictly one of two states.

The note provides 100% principal protection at maturity.

The DCFN is the SRT family's equivalent of the Digital / Exotic Coupon Note (DIGITAL001) in the ELN family. The economic logic is identical — a binary payoff conditional on a market observable — but the underlying is an interest rate (SOFR) rather than an equity index. The key pricing concept is the same: pin risk near the digital strike, where a small fixing difference flips the coupon between 6.0% and 1.0%.

The DCFN differs from the Non-Callable Range Accrual (NCRA001) in a fundamental way: the NCRA has daily observation with proportional accrual (smooth outcome), while the DCFN has discrete observation with binary outcome (discontinuous). The NCRA is a "how many days in range" product; the DCFN is a "which side of the strike" product.

#### Construction

A DCFN decomposes into two or three components:

**Component 1 — Fixed-rate bond (long).** Provides 100% principal protection and a guaranteed minimum coupon (the low coupon of 1.0%).

**Component 2 — Digital caplet strip (long).** A series of digital options on SOFR, one per coupon period. Each digital pays the coupon differential (6.0% - 1.0% = 5.0%) if SOFR is below the cap strike (4.5%) on the observation date. The strip has one digital per quarter (or per semi-annual period).

The total coupon is: Low coupon (guaranteed) + Digital payoff (conditional) = 1.0% + 5.0% (if below strike) = 6.0% (high) or 1.0% (low).

**Component 3 — Digital floor strip (implicit).** The guaranteed low coupon is effectively a digital floor — the investor always receives at least 1.0%. This is embedded in the bond component.

**Decomposition:**

| Component | Value |
|---|---|
| High coupon (rate below cap) | 6.0% p.a. |
| Low coupon (rate above cap) | 1.0% p.a. |
| Cap strike | 4.5% (SOFR) |
| Funded by: | |
| — Digital caplet strip cost | 1.8% (annualised) |
| — Funding | 3.0% |
| — FTP | 0.4% |
| — Desk margin | 0.3% |
| — Floor coupon cost | 0.5% |
| Total funding | 6.0% |

**Digital replication.** Each digital caplet is replicated as a tight caplet spread: short a caplet at 4.5% and long a caplet at 4.5% + epsilon, scaled to produce the 5.0% differential. The replication uses normal (Bachelier) volatility for SOFR.

#### Booking & systems

DCFNs are booked in the Murex four-leg framework.

**Note leg.** The structured note with the two-state coupon formula. Critical fields: high coupon rate (6.0%), low coupon rate (1.0%), cap strike (4.5%), reference rate (SOFR), observation dates, fixing source, and coupon condition (below cap = high coupon, above cap = low coupon). The coupon condition direction is critical — inverting it makes the note pay 1.0% when the investor expects 6.0%.

**Issuer leg.** Standard funding fields.

**Deposit leg.** Standard deposit fields.

**Hedge leg.** A strip of digital caplets replicating the binary coupon condition. Each digital caplet is implemented as a tight caplet spread at the 4.5% strike. The hedge must use the same observation dates, the same reference rate, and the same fixing source as the note leg. Normal (Bachelier) volatility is used for the caplet pricing.

**Termsheet** defines the cap strike, the high and low coupon rates, the observation dates, the coupon condition (explicitly stating whether "below" means strictly below or at-or-below), the fixing source, and the fixing time.

#### Pricing intuition

DCFN pricing shares the key characteristics of all digital products: discontinuous payoff, extreme gamma near the strike, and pin risk.

**The binary cliff.** On each observation date, the coupon difference is 500 bps (6.0% vs 1.0%). A 1 bps change in the SOFR fixing near the 4.5% strike can flip the coupon from the high state to the low state — a USD 50,000 difference per quarter on a USD 10M note. This creates extreme P&L sensitivity near observation dates when the rate is close to the strike.

**Normal volatility and digital pricing.** For interest rate digitals, normal (Bachelier) volatility is the standard model, unlike equity digitals which use lognormal (Black-Scholes) vol. Normal vol produces a symmetric distribution around the forward rate, which affects the digital probability calculation. The digital's value equals the probability (under the risk-neutral measure) that the rate will be below the cap strike.

**Pin risk.** Identical to the equity digital (DIGITAL001): when the rate is near the cap strike on an observation date, the hedge ratio oscillates and the P&L is highly uncertain until the fixing is published. Pin risk management is operational — it requires pre-hedging and active monitoring on observation dates.

**Rate directionality.** Unlike the NCRA (which benefits from rate stability), the DCFN benefits from rates staying below the cap strike. The investor has a directional view — bullish on rates staying low. This makes the DCFN more directional than the NCRA.

**Greeks:**
- DV01: Dominated by the digital probability. Rate below strike → high coupon regime, DV01 reflects 6.0% coupon. Rate above → 1.0% regime.
- Vega (normal): Complex. Near the strike, vega changes sign. Away from the strike, vega impact is muted.
- Gamma: Extreme near the cap strike. The defining risk.
- Theta: Accelerates into each observation date.

#### Worked example (USD 10M)

**Terms:** USD 10M notional, 3-year maturity, quarterly observation, SOFR cap strike 4.5%, high coupon 6.0%, low coupon 1.0%.

**Decomposition:**

| Component | Annualised |
|---|---|
| High coupon | 6.0% |
| Digital caplet strip cost | 1.8% |
| Funding | 3.0% |
| FTP | 0.4% |
| Desk margin | 0.3% |
| Floor coupon cost | 0.5% |
| Total funding sources | 6.0% |

**Verification:** 1.8% + 3.0% + 0.4% + 0.3% + 0.5% = 6.0%. Matches high coupon.

**Scenario 1 — SOFR below 4.5% on all 12 observation dates:**
- All high coupons: 12 × (6.0% / 4) = 12 × 1.5% = 18.0%
- Total coupon: USD 10M × 18.0% = USD 1,800,000
- Principal: USD 10M returned

**Scenario 2 — SOFR below 4.5% on 8 dates, above on 4 dates:**
- High coupons: 8 × 1.5% = 12.0%
- Low coupons: 4 × 0.25% = 1.0%
- Total: 13.0%
- Total coupon: USD 10M × 13.0% = USD 1,300,000
- Average effective rate: 13.0% / 3 = 4.33% p.a.

**Scenario 3 — SOFR above 4.5% on all 12 observation dates:**
- All low coupons: 12 × 0.25% = 3.0%
- Total coupon: USD 10M × 3.0% = USD 300,000
- Average effective rate: 1.0% p.a.
- Significantly below comparable fixed rate

Principal is returned in full (USD 10M) in all scenarios.

#### Reconciliation specifics

**Cap strike level (most critical).** The cap strike must be entered exactly in both the Murex note leg and the hedge leg. A 1 bps error shifts the digital probability and can flip coupon outcomes on observation dates when the fixing is near the strike. For rate digitals, the impact is the same as for equity digitals — economically material and operationally dangerous.

**Coupon condition direction.** The note leg must correctly map "rate below cap strike" to the high coupon and "rate above cap strike" to the low coupon. An inversion — assigning the coupons in the wrong direction — means the note pays 1.0% when it should pay 6.0% and vice versa. This is a booking error, not a market risk, but it is catastrophic if undetected. Verify the condition on first booking and after any amendment.

**Observation dates.** Every coupon observation date must be present in both the note leg and the hedge leg. A missing date means the coupon for that period is either not determined or incorrectly defaulted. For a 3-year quarterly product, all 12 dates must be individually verified.

**Fixing source and time.** The SOFR fixing used for the digital condition must come from the same source and be captured at the same time as specified in the termsheet. If the note leg uses a different SOFR publication than the hedge leg, the digital outcomes can diverge.

#### Desk view

**Who buys this product.** Investors with a directional view that rates will stay below the cap strike. Yield-seeking investors who understand binary payoffs and accept the all-or-nothing coupon risk. Insurance companies with a rate outlook and a tolerance for coupon variability.

**The real risk.** Binary coupon risk — the difference between the high and low coupons is 500 bps, and this difference is determined by a single fixing on each observation date. Near the cap strike, the outcome is essentially a coin flip. Over multiple periods, a string of unfavourable fixings can result in a cumulative coupon well below comparable fixed rates.

**When appropriate.** Strong conviction that rates will remain below the cap strike. Cap strike set well above the forward rate (high probability of high coupon). Low rate volatility environment.

**When not appropriate.** Rate uncertainty or upward trend. Cap strike near the forward rate (coin-flip probability). Income-dependent investors who cannot tolerate 1.0% coupons. High rate volatility.

#### Desk shorthand

*Binary rate coupon; cap strike, high or low.*
