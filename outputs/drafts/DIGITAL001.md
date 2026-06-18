### Digital / Exotic Coupon Notes

#### Definition

A Digital Coupon Note pays a fixed coupon that is conditional on the underlying being above (or below) a specified digital strike level on the observation date. The coupon is all-or-nothing: if the condition is met, the investor receives the full coupon; if not, zero. There is no partial payout.

The binary nature of the payoff distinguishes digital notes from range accrual notes (CRAELN001), where the coupon accrues proportionally based on how many days the underlying satisfies a condition. In a digital note, the outcome on each observation date is strictly binary — 8% or 0%, with nothing in between.

Principal protection varies. In the simplest form, the note provides 100% principal protection (the digital option is embedded in the coupon only). More complex variants add a down-and-in put on the principal, creating a dual-risk product: binary coupon risk above and barrier principal risk below.

The digital coupon note is the ELN family's purest expression of a directional binary view. It suits investors who have a strong directional conviction and want maximum coupon for a given probability of payout.

#### Construction

A digital coupon note decomposes into two or three components:

**Component 1 — Fixed-rate bond (long).** The principal component. Redeems at par at maturity (unless a DI barrier is present and breached).

**Component 2 — Digital option strip (long).** A series of digital call options, one per coupon period. Each digital pays a fixed coupon (8.0% annualised) if the underlying is above the digital strike (100% of initial) on the observation date. The strip has one digital per quarter (or per semi-annual period).

**Component 3 — Down-and-in put (short, optional).** If present, makes the principal conditional on a barrier. This is a separate risk layer — the coupon is conditional on the digital strike, while the principal is conditional on the DI barrier. Not all digital notes include this component.

**Decomposition:**

| Component | Value |
|---|---|
| Digital coupon (conditional) | 8.0% p.a. |
| Digital strike | 100% of initial |
| | |
| Funded by: | |
| — Digital option strip cost | 3.2% (annualised) |
| — Funding | 2.0% |
| — FTP | 0.6% |
| — DI put income (if barrier) | 2.0% |
| — Desk margin | 0.2% |
| Total funding | 8.0% |

**Digital replication.** In practice, digital options are not traded as pure binary instruments. The desk replicates each digital as a tight call spread: long a call at K and short a call at K + epsilon, scaled so the payoff at the digital strike equals the coupon. The width of the call spread (epsilon) determines the replication precision and the exposure to skew.

#### Booking & systems

Digital coupon notes are booked in the standard ELN system architecture.

**NEMO (book of record)** carries the structured note with its coupon schedule. Critical fields: digital strike level, coupon rate (conditional), observation dates per period, coupon condition (above, at-or-above), underlying reference, and DI barrier level (if applicable). The distinction between "above" and "at-or-above" the digital strike is economically meaningful — it determines the boundary treatment.

**Sophis (risk and P&L)** carries the decomposed components: the bond, the digital option strip (replicated as call spreads), and the DI put (if present). Sophis must apply skew-adjusted pricing to the call spread replication. The width of the replicating spread must be narrow enough to accurately represent the binary payoff but wide enough to be hedgeable.

**Termsheet (legal document)** defines the digital strike, the coupon rate, the exact observation dates, the boundary condition (strictly above or at-or-above), the fixing source, and any DI barrier terms. Boundary treatment is critical — a 1 basis point difference in the fixing can flip an 8% coupon to zero.

Murex is not used for any ELN product.

#### Pricing intuition

Digital option pricing has unique characteristics that differ from vanilla options.

**The binary cliff.** The payoff function has a discontinuity at the digital strike. Immediately above the strike, the coupon is 8%; immediately below, it is zero. This creates extreme gamma near the strike and makes the P&L highly sensitive to small spot movements around observation dates.

**Skew dominance.** For digital options, the volatility skew matters more than the at-the-money volatility. The digital's value depends on the probability of finishing above the strike, which is determined by the risk-neutral probability distribution — and that distribution is shaped by skew. A flat-vol model can misprice a digital by 10-20% compared to a skew-adjusted model.

**Pin risk.** On observation dates, if the underlying is near the digital strike, the desk faces "pin risk" — the outcome is uncertain until the fixing, and the hedge ratio oscillates wildly. Pin risk is the most operationally challenging aspect of digital products. It requires active management on observation dates and sometimes pre-hedging.

**Call spread replication width.** The tighter the call spread, the more accurate the digital replication but the higher the skew sensitivity. A 50 bps spread is typical for liquid underlyings; wider spreads may be used for illiquid names where hedging at tight strikes is impractical.

**Greeks:**
- Delta: Discontinuous at the digital strike. Spikes to extreme values near the strike, then drops to near-zero away from it.
- Gamma: Extreme near the strike (the derivative of the discontinuous delta). This is the defining risk of digital products.
- Vega: Complex — depends on skew, not just ATM vol. Can change sign near the strike.
- Theta: Accelerates into each observation date as the digital's resolution approaches.

#### Worked example (USD 10M)

**Terms:** USD 10M notional, 2-year maturity, quarterly digital coupon (8.0% p.a. conditional), digital strike at 100% of initial, equity index underlying (20-vol), optional DI barrier at 65%.

**Decomposition — funding the coupon:**

| Component | Annualised |
|---|---|
| Digital coupon (conditional) | 8.0% |
| Digital option strip cost | 3.2% |
| Funding | 2.0% |
| FTP | 0.6% |
| DI put income (65% barrier) | 2.0% |
| Desk margin | 0.2% |
| Total funding sources | 8.0% |

**Verification:** 3.2% + 2.0% + 0.6% + 2.0% + 0.2% = 8.0%. Matches digital coupon.

**Scenario 1 — underlying above digital strike on all 8 observation dates:**
- Coupon received: 8 quarters × 2.0% = 16.0% total
- Principal: 100% (barrier not breached)
- Total return: 16.0%

**Scenario 2 — underlying above strike on 5 of 8 dates, no barrier breach:**
- Coupon received: 5 quarters × 2.0% = 10.0% total
- Missed coupons: 3 quarters × 2.0% = 6.0% (lost — no memory, no catch-up)
- Principal: 100%
- Total return: 10.0%

**Scenario 3 — underlying falls to 60%, barrier breached, above strike on 3 dates:**
- Coupon received: 3 quarters × 2.0% = 6.0%
- Principal: USD 10M × (60% / 100%) = USD 6M (barrier breached, DI put triggered)
- Total return: 6.0% coupon - 40.0% principal loss = -34.0%

The all-or-nothing coupon means there is no smoothing between good and bad outcomes. Each period is an independent binary bet.

#### Reconciliation specifics

**Digital strike level (most critical).** The digital strike must be entered exactly in both NEMO and Sophis. A 1 basis point error can flip the coupon outcome on the observation date. Unlike barrier levels where small errors are unlikely to trigger (barrier is far from spot), the digital strike is often near the money — even tiny errors have material consequences.

**Observation dates.** Every coupon observation date must be present in both systems. A missing observation date means a coupon is either missed or incorrectly paid. For a 2-year quarterly product, there are 8 observation dates — each must be entered individually.

**Boundary condition.** The termsheet specifies whether the condition is "strictly above" or "at or above" the digital strike. This is not a theoretical distinction — if the fixing comes in exactly at the strike, the boundary condition determines whether 8% or 0% is paid. NEMO and Sophis must agree on the boundary treatment.

**Fixing source.** The observation fix must come from the source specified in the termsheet (e.g., Bloomberg, Reuters, exchange closing price). If different systems use different fixing sources, the coupon determination can differ between them.

#### Desk view

**Who buys this product.** Investors with strong directional conviction who want maximum coupon for a given probability threshold. Yield-hungry investors willing to accept binary outcomes. Private banking clients attracted by the headline coupon rate (8.0%) without fully appreciating the all-or-nothing nature.

**The real risk.** Binary coupon means no partial compensation for near-miss scenarios. The underlying could close 1 basis point below the digital strike, and the investor receives zero coupon for that period. Pin risk on observation dates creates operational pressure. If a DI barrier is present, the principal risk is layered on top of the coupon risk.

**When appropriate.** Strong directional conviction. Investors who understand binary payoffs. Products where the digital strike is sufficiently out-of-the-money that coupon probability is high. Markets with low volatility (higher probability of staying above strike).

**When not appropriate.** Investors who cannot tolerate missed coupons (income-dependent mandates). High-volatility environments (more frequent coupon misses). Situations where the underlying is likely to hover near the digital strike (pin risk). Retail investors who equate the headline coupon with an expected return.

#### Desk shorthand

*Binary coupon; digital strike, all or nothing.*
