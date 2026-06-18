### Bonus / Participation Note

#### Definition

The Bonus / Participation Note is a structured note, issued as an equity-linked note (ELN) under an ISDA or MTN wrapper, that provides the investor with participation in the upside of an equity underlying, combined with conditional principal protection through a downside knock-in barrier. There is no coupon --- the investor's entire return is the capital gain from upside participation. At maturity, if the underlying has not breached the knock-in barrier, the investor receives par plus a participation percentage of any positive return above the call strike. If the underlying has breached the knock-in barrier at maturity, the investor bears 1:1 downside exposure from the initial fixing level, receiving par multiplied by the underlying's final level divided by the initial fixing level. The participation rate (typically 60--100% for single-stock underlyings) determines the fraction of the upside the investor captures. Capital protection is conditional on the barrier: above the barrier, the investor is protected and participates in gains; below the barrier, the investor bears the full decline.

#### Construction

The note decomposes into three primitive instruments. The desk is long a zero-coupon bond funded at the issuer's credit curve, providing the principal-protection leg. The desk is long a European call option struck at 100% of initial fixing with a participation rate of 80%, providing the investor's upside exposure. The desk is short a down-and-in put struck at 100% with a knock-in barrier at 70% of initial fixing, observed at maturity only, which generates the contingent principal loss if the barrier is breached. The put premium received from the investor (via coupon foregone) partially funds the call premium, and the issuer's funding advantage covers the difference. The participation rate is the residual variable: after pricing the call and the put, the desk determines what fraction of the call it can afford to pass through to the investor. Higher volatility increases both the call premium (more expensive to buy) and the put premium (more received from sale), with the net effect on participation depending on the volatility skew. Pricing is closed-form for European barrier and European call under Black-Scholes with skew adjustment.

#### Booking & systems

The book of record is NEMO, which carries the trade lifecycle, call strike, put strike, knock-in barrier level, participation rate, barrier observation convention, and settlement type. NEMO must carry the participation rate as a distinct field --- if the participation rate is not booked or defaults to 100%, the upside settlement amount will be overstated. Risk and P&L run through Sophis, which prices the long call and the short down-and-in put, computes net Delta, Vega, and Gamma, and generates daily mark-to-market. Sophis must net the long call delta against the short put delta for the hedge position. The legal document is the Termsheet, which defines the call strike, put strike, knock-in barrier, participation rate, any upside cap, barrier observation convention, and fixing rules. Murex is not used. The dominant operational risk is participation rate consistency: NEMO's settlement calculation must apply the exact same participation percentage as Sophis uses in its pricing model. A 1-percentage-point difference in participation rate on a USD 10M note with a 20% underlying return produces a USD 20K settlement discrepancy.

#### Pricing intuition

The dominant Greeks are Delta (net long from the call, partially offset by the short put), Vega (net long --- the long call typically has higher vega exposure than the short put at inception), and Gamma (positive near the call strike, negative near the barrier). Unlike the Reverse Convertible family where the investor is a net seller of volatility, the Bonus Note investor is approximately volatility-neutral to slightly long volatility at inception, because the long call and short put partially offset.

The participation rate is the key commercial parameter. It is determined by the residual after pricing the call, the put, the funding, and the desk margin. Three levers increase the participation rate: lower barrier (cheaper put, more premium available for the call), higher dividend yield (cheaper call, lower cost to the desk), and wider issuer funding spread (more funding advantage available). Conversely, higher implied volatility typically reduces the participation rate because the call premium increases faster than the put premium for at-the-money strikes with out-of-the-money barriers, due to the put's lower delta at inception.

#### Worked example (USD 10M)

**Trade parameters.** Notional: USD 10M. Tenor: 1 year. Underlying: single stock, 25% implied volatility at inception. Call strike: 100% of initial fixing. Put strike: 100% of initial fixing. Knock-in barrier: 70% of initial fixing. Participation rate: 80%. Barrier observation: maturity only. No coupon. No upside cap.

**Economic decomposition.** The structure's economics balance as follows. The desk buys the European call (100% strike, 25-vol, 1-year) at 8.0% of notional, but passes through only 80% participation, costing 6.4% of notional (USD 640K) in effective call premium. The desk sells the down-and-in put (100% strike, 70% barrier, 25-vol, 1-year) at 3.0% of notional (USD 300K). Issuer funding at the credit curve contributes 2.0% (USD 200K). Funds transfer pricing contributes 1.0% (USD 100K). Net desk position: call cost 6.4% minus put income 3.0% minus funding 2.0% minus FTP 1.0% equals 0.4% desk margin (USD 40K). Arithmetic check: call cost 6.4% equals put income 3.0% plus funding 2.0% plus FTP 1.0% plus desk margin 0.4%.

**Good scenario --- upside.** The underlying closes at 130% of initial fixing at maturity. Above the 70% barrier. The call is in-the-money. The investor receives par (USD 10M) plus 80% participation in the 30% upside: 80% × 30% × USD 10M = USD 2.4M. Total return: USD 12.4M, or 24% on par.

**Good scenario --- flat.** The underlying closes at 100% at maturity. The call is at-the-money (zero upside). The barrier was not breached. The investor receives par (USD 10M). Zero capital gain, zero loss.

**Bad scenario --- below barrier.** The underlying closes at 50% at maturity. Below the 70% barrier. The put activates with 1:1 downside. The investor receives par × (50%/100%) = USD 5M. Loss: USD 5M, or 50% of notional. No coupon to offset.

#### Reconciliation specifics

**Participation rate** --- NEMO carries the participation rate as a percentage (80%) that is applied to the underlying's positive return at maturity to calculate the upside settlement amount --- if NEMO's participation rate differs from Sophis's by even 1 percentage point, the settlement discrepancy on a 20% underlying return is USD 20K per USD 10M notional.

**Upside cap** --- the Termsheet may impose a maximum return cap (e.g., 30% upside cap) that truncates the participation payout --- if NEMO does not enforce the cap but Sophis prices with a cap, the settlement will exceed the priced value, producing a loss for the desk.

**Barrier observation** --- same risk as other barrier products: if NEMO monitors continuously but the Termsheet specifies European observation, a mid-life barrier breach followed by recovery produces an incorrect knock-in determination.

**Net Delta hedging** --- the desk's hedge position must reflect the net Delta of the long call and short put --- if Sophis computes the hedge for each component separately without netting, the aggregate hedge position will overshoot, creating unnecessary transaction costs.

#### Desk view

The Bonus / Participation Note is the natural product for equity-bullish clients who prefer capital gain over coupon income. Unlike the Reverse Convertible family, where the investor sells volatility and receives a fixed coupon, the Bonus Note investor buys upside exposure (via the call) while selling downside exposure (via the barrier put). The net result is a product that behaves like a conditional equity investment with a barrier cushion: above the barrier, the investor participates in gains; below the barrier, the investor participates in losses.

The product is appropriate when the investor has a directional bullish view on the underlying, prefers capital appreciation over income, and is comfortable with barrier risk. It is best suited to moderate-to-high-volatility environments where the participation rate is attractive (higher vol funds a better participation rate through the put premium). It is not appropriate when the investor wants certainty of return (the product may return zero if the underlying is flat at maturity), when the investor cannot absorb full downside loss below the barrier, or when dividends are high (reducing the call value and compressing the participation rate). Product Control should verify the participation rate and any upside cap at booking.

#### Desk shorthand

*Upside participation; barrier put, no coupon.*
