### Warrant / Turbo Certificate

#### Definition

A Warrant (or Turbo Certificate) provides leveraged exposure to an equity underlying through a barrier option structure. The investor purchases the right to equity gains above a strike price, paying only a fraction of the underlying value as premium. In exchange for this leverage, the product is subject to a knock-out barrier: if the underlying falls to the barrier level, the warrant is terminated and the investor loses most or all of the invested premium.

Warrants are the most aggressive product in the ELN family. Unlike Reverse Convertibles or Bonus Notes that embed options within a note structure, a warrant is a naked option instrument — typically listed on an exchange — with no bond component and no principal protection.

The key distinction from a vanilla call option is the knock-out barrier. This barrier (continuous, intraday monitoring) suppresses optionality and reduces the premium, which is precisely what creates the leverage. A standard Turbo sets the KO barrier at or very near the strike level, meaning the product has almost no time value and moves nearly 1:1 with the underlying in absolute terms.

#### Construction

A bull warrant (long) decomposes into a single primary component:

**Component — Down-and-out call option (long).** The investor is long a call option with a strike (financing level) below spot, and a knock-out barrier at or near the strike. The issuer funds the difference between spot and strike; the investor pays a premium equal to the intrinsic value plus a small time value and funding cost.

**Premium breakdown:**

- Intrinsic value: Spot minus Strike (e.g., 100% - 85% = 15%)
- Time value: Small (0.8% for a deep ITM turbo — barrier suppresses extrinsic value)
- Funding cost: Issuer charges for financing the strike level (1.2%)
- Total premium: 17.0% of underlying

**Leverage:**

The leverage ratio is the underlying value divided by the premium: 100% / 17.0% = 5.9x. A 1% move in the underlying translates to approximately 5.9% change in the warrant value.

There is no bond component, no coupon, and no principal protection. The structure is a single barrier option.

For put warrants (bear turbos), the construction is symmetric: a down-and-in put or up-and-out put, providing leveraged short exposure with a knock-out on the upside.

#### Booking & systems

Warrants are booked in the standard ELN system architecture, though the listed nature adds exchange-specific fields.

**NEMO (book of record)** carries the warrant as a listed instrument. Critical fields: warrant type (call/put), strike/financing level, KO barrier level, ratio (how many warrants per unit of underlying), multiplier, listing exchange, and ISIN. For open-ended products, the strike and barrier are adjusted periodically (typically daily) to reflect funding costs.

**Sophis (risk and P&L)** carries the barrier option model with continuous monitoring. Sophis must be set to continuous barrier observation — not discrete. The model handles delta hedging, gamma exposure near the barrier, and the funding adjustment for open-ended structures.

**Termsheet / Exchange listing (legal document)** defines the knock-out terms, settlement method (cash or physical), and the precise barrier observation rules (including any grace periods or end-of-day settlement triggers used by some exchanges).

Murex is not used for any ELN product.

#### Pricing intuition

Warrant pricing is dominated by three factors: leverage, barrier proximity, and funding cost.

**Leverage and delta.** A turbo warrant's delta is close to 1 in absolute terms (it moves almost dollar-for-dollar with the underlying), but the percentage delta is amplified by the leverage ratio. At 5.9x leverage, a 1% underlying move creates a 5.9% warrant move. This makes the product extremely sensitive to directional moves.

**Barrier proximity and gamma.** As the underlying approaches the KO barrier, two effects intensify: (1) gamma spikes as the probability of knock-out increases rapidly, and (2) delta collapses — the warrant transitions from a leveraged equity instrument to a rapidly decaying option. The "barrier gamma" is the dominant risk near knock-out.

**Vega suppression.** Unlike vanilla options, the KO barrier suppresses vega. The barrier caps the option's potential to benefit from increased volatility (higher vol means higher probability of KO, which offsets the higher expected payoff). This is why turbos have lower premiums than vanilla calls of the same strike.

**Funding cost.** The issuer finances the strike level (the portion of the underlying not paid by the investor). This funding cost is embedded in the premium for fixed-tenor warrants and reflected in daily strike adjustments for open-ended products. Higher rates increase the funding cost and slightly reduce leverage.

**Greeks:**
- Delta: High (close to 1 in absolute terms, leveraged in percentage terms).
- Gamma: High near barrier; manageable away from barrier.
- Vega: Lower than vanilla equivalent — barrier suppresses optionality.
- Theta: Minimal for deep ITM turbos; increases near barrier as time decay accelerates knock-out probability.

#### Worked example (USD 10M)

**Terms:** USD 10M notional exposure, single stock at 100, warrant strike at 85, KO barrier at 85 (standard turbo, barrier = strike), ratio 1:1.

**Premium calculation:**

| Component | Value |
|---|---|
| Intrinsic value (100 - 85) | 15.0% |
| Time value | 0.8% |
| Funding cost (1Y) | 1.2% |
| Total premium | 17.0% |
| Investment required | USD 1,700,000 |
| Leverage | 5.9x |

**Scenario 1 — underlying rallies to 115 (+15%):**
- Warrant value: 115 - 85 = 30 (plus minor time/funding adjustments)
- Approximate return: (30 - 17) / 17 = +76.5%
- Equivalent unleveraged return: +15%
- Leverage confirmed: 76.5% / 15% ≈ 5.1x (slightly below static leverage due to non-linearity)

**Scenario 2 — underlying flat at 100:**
- Warrant value: 100 - 85 = 15 (intrinsic) + minor time value
- Return: approximately (15.3 - 17) / 17 = -10%
- Loss due to time decay and funding cost erosion

**Scenario 3 — underlying falls to 85 (barrier hit):**
- Knock-out triggered
- Warrant terminated
- Residual value: zero (standard turbo) or small rebate (some structures)
- Loss: 100% of invested premium (USD 1,700,000)

**Gap risk:** If the underlying gaps below the barrier overnight (e.g., opens at 80 after closing at 87), the issuer absorbs the gap loss below the barrier. This gap risk is the issuer's primary residual risk after hedging and is reflected in the bid-offer spread.

#### Reconciliation specifics

**KO barrier observation (most critical).** Sophis must be configured for continuous (intraday) barrier monitoring. If set to discrete (daily close), the model will underestimate knock-out probability and misprice the warrant. This is the single most dangerous misconfiguration — it creates a systematic pricing error that compounds over the product's life.

**Strike / financing level.** For open-ended products, the strike is adjusted daily to reflect funding costs. NEMO must carry the current strike, and Sophis must apply the same adjustment schedule. A drift between the two systems accumulates over time and distorts the hedge ratio.

**Ratio / multiplier.** Warrants are often issued with a ratio (e.g., 10 warrants per unit of underlying). This ratio must be consistent across NEMO, Sophis, and the exchange listing. A ratio error directly scales the entire position by the wrong factor — a silent but large error.

**Settlement method.** Some warrants settle physically (deliver underlying) while others settle in cash. The settlement method must match across systems and the exchange specification.

#### Desk view

**Who buys this product.** Sophisticated retail investors, day traders, and tactical institutional allocators seeking leveraged directional exposure. Warrants are exchange-listed, liquid, and accessible — making them the primary leveraged equity instrument for retail markets in Europe and Asia.

**The real risk.** Total loss of premium at knock-out. Unlike a vanilla call that expires worthless only at maturity, a warrant can be knocked out at any point during its life. The continuous barrier means intraday volatility can trigger knock-out even if the underlying recovers by close. Gap risk on overnight moves can knock out the warrant at a level far below the barrier.

**When appropriate.** Short-term directional views with high conviction. Tactical hedging where leverage is desired. Markets with adequate liquidity in the listed warrant market.

**When not appropriate.** Long-term investment horizons (funding cost erodes value). Investors who cannot monitor positions intraday (continuous KO risk). Volatile markets where gap risk is elevated. Any investor who cannot afford total loss of the invested premium.

#### Desk shorthand

*Leveraged call; KO barrier, total loss risk.*
