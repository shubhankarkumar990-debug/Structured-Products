### Airbag / Leveraged Reverse Convertible

#### Definition

The Airbag (also known as the Leveraged Reverse Convertible) is a structured note, issued as an equity-linked note (ELN) under an ISDA or MTN wrapper, that pays a fixed coupon and provides conditional principal protection through a downside barrier, with leveraged principal loss if the barrier is breached at maturity. If the underlying closes at or above the knock-in barrier at maturity, the investor receives par plus the fixed coupon --- the barrier has protected the principal. If the underlying closes below the knock-in barrier, the investor's principal loss is amplified by a leverage ratio equal to the put strike divided by the barrier level. For a 100% strike and 70% barrier, the leverage ratio is 1.4286x: a 20-percentage-point decline below the barrier produces a 28.6% loss of principal, not 20%. The coupon is paid regardless of the underlying's performance. There is no autocall, no conditional coupon, and no knock-out feature. The product name is misleading: "airbag" suggests a cushion, but below the barrier the structure amplifies losses rather than absorbing them. The barrier provides protection in a range (between the strike and the barrier), but once breached, the leverage accelerates the loss beyond what the investor would experience in a standard Reverse Convertible.

#### Construction

The note decomposes into two primitive instruments. The desk is long a zero-coupon bond funded at the issuer's credit curve, providing the funding leg and par redemption. Against this, the desk is short a leveraged down-and-in put. The put has a strike at 100% of initial fixing and a knock-in barrier at 70% of initial fixing, observed at maturity only (European barrier). If the underlying closes below 70% at maturity, the put activates and the settlement amount reflects the leveraged payoff: the investor receives par multiplied by (Underlying Final / Barrier), which is equivalent to par minus the leverage ratio multiplied by the decline below the barrier. The leveraged down-and-in put is priced between the vanilla European put (used in the base RC) and a standard down-and-in put (used in barrier RCs). The barrier reduces the put premium relative to a vanilla put (the put only activates if the underlying falls 30%), but the leverage increases it relative to a standard barrier put (the loss below the barrier is amplified). The net result is a coupon that sits between the base RC (higher coupon, no barrier) and a standard barrier RC (lower coupon, barrier protection without leverage). Pricing is closed-form for European-observation barriers under Black-Scholes with a barrier adjustment.

#### Booking & systems

The book of record is NEMO, which carries the trade lifecycle, put strike level, knock-in barrier level, leverage ratio, settlement formula, coupon schedule, barrier observation convention, and settlement type. The critical field is the settlement formula below the barrier. NEMO must encode the leveraged payoff: settlement amount equals par multiplied by (Underlying Final / Barrier Level). If NEMO instead applies the standard Reverse Convertible formula (settlement equals par multiplied by Underlying Final / Strike), the settlement will be incorrect --- in the bad scenario, the standard formula would produce USD 5M (50% of par) while the leveraged formula produces USD 7.14M (50/70 × par). Risk and P&L run through Sophis, which prices the leveraged down-and-in put, computes Greeks, and generates daily mark-to-market. Sophis must use the same leverage ratio in its pricing model as NEMO uses in its settlement calculation. The legal document is the Termsheet, which defines the put strike, knock-in barrier, leverage ratio (or equivalently, the settlement formula), barrier observation convention, and fixing rules. Murex is not used. The dominant operational risk is leverage formula inconsistency: if NEMO and Sophis use different settlement formulas, every mark-to-market from inception to maturity will diverge, and the final settlement will not reconcile.

#### Pricing intuition

The dominant Greeks are short Delta, short Vega, and negative Gamma, with discontinuity effects at the barrier level. The structure's coupon is funded by the leveraged down-and-in put premium. The put premium of 4.8% is lower than the base RC's vanilla put premium of 5.5% because the barrier reduces the activation probability, but higher than a standard (non-leveraged) down-and-in put because the leverage amplifies the payoff when the put is in-the-money.

The leverage ratio is the key pricing parameter unique to this product. It is mechanically determined by the strike-to-barrier ratio: a 100% strike with a 70% barrier produces 1.4286x leverage; a 100% strike with a 60% barrier produces 1.667x. Higher leverage means larger losses below the barrier, which increases the put premium and allows a higher coupon. Lower barrier levels reduce the probability of barrier breach but increase the leverage if the barrier is breached --- the investor faces a lower probability of a larger loss.

Near the barrier, Delta is discontinuous and Gamma spikes. If the underlying is trading at 71% approaching maturity, the position is highly sensitive to small moves: a 2-percentage-point decline triggers the barrier and the leveraged loss. The desk must manage this cliff risk through the barrier-proximity Greeks.

#### Worked example (USD 10M)

**Trade parameters.** Notional: USD 10M. Tenor: 1 year. Underlying: single stock, 25% implied volatility at inception. Put strike: 100% of initial fixing. Knock-in barrier: 70% of initial fixing. Leverage ratio: 1.4286x (100/70). Settlement: physical delivery. Fixed coupon: 8.0% per annum (paid at maturity). Barrier observation: maturity only.

**Economic decomposition.** The 8.0% headline coupon reconciles as follows. The leveraged down-and-in put (100% strike, 70% KI barrier, 1.4286x leverage, 25-vol, 1-year) prices at 4.8% of notional (USD 480K). Issuer funding at the credit curve contributes 2.0% per annum (USD 200K). Funds transfer pricing absorbs 0.9% per annum (USD 90K). The residual desk margin is 0.3% per annum (USD 30K). Arithmetic check: leveraged put premium 4.8% plus issuer funding 2.0% plus FTP 0.9% plus desk margin 0.3% equals 8.0% headline coupon.

**Good scenario --- above barrier.** The underlying closes at 80% of initial fixing at maturity. The underlying is above the 70% barrier. The knock-in put is not activated. The investor receives par (USD 10M) plus the fixed coupon (USD 800K). Total return: USD 10.8M, or 8.0% on par. The investor has lost nothing despite a 20% decline in the underlying --- the barrier provided full protection.

**Bad scenario --- below barrier.** The underlying closes at 50% of initial fixing at maturity. The underlying is below the 70% barrier. The knock-in put activates with leverage. Settlement amount: par × (50% / 70%) = USD 10M × 0.7143 = USD 7.143M. The investor receives USD 7.143M plus the fixed coupon (USD 800K). Net proceeds: USD 7.943M. Principal loss: USD 2.057M, or 20.6% of par after accounting for the coupon. Without the leverage (standard barrier RC), the investor would have received USD 5M plus coupon --- the leverage actually benefits the investor in this case because the settlement is calculated relative to the barrier, not the strike.

**Severe scenario --- deep decline.** The underlying closes at 30% of initial fixing. Settlement amount: par × (30% / 70%) = USD 10M × 0.4286 = USD 4.286M. Plus coupon: USD 800K. Net: USD 5.086M. Principal loss: USD 4.914M, or 49.1% of par. At 0% (theoretical), the investor loses the entire principal.

#### Reconciliation specifics

**Leverage formula** --- the Termsheet defines the settlement formula below the barrier, typically as "par × (Final Level / Barrier Level)" --- if NEMO encodes the standard RC formula ("par × Final Level / Strike") instead of the leveraged formula, the settlement in the bad scenario differs by USD 2.143M (the difference between USD 5M standard and USD 7.143M leveraged on a USD 10M note at 50% underlying).

**Barrier level** --- NEMO carries the barrier as a percentage of initial fixing (70%) while Sophis carries an absolute price level --- if the initial fixing is amended post-trade, the Sophis barrier must be recalculated manually, and a stale barrier level will produce incorrect knock-in determination.

**Barrier observation convention** --- the Termsheet specifies European observation (maturity only) --- if NEMO or Sophis monitors the barrier continuously, a mid-life breach at 69% followed by recovery to 80% at maturity would incorrectly trigger the knock-in under continuous monitoring but correctly not trigger it under European observation.

**Settlement type below barrier** --- the leveraged formula calculates a cash amount, but the Termsheet may specify physical delivery --- if physical, the number of shares delivered is par divided by the barrier price (not the final price), which changes the share count calculation and the associated transfer and custody operations.

#### Desk view

The Airbag is a barrier RC with a twist: the leverage ratio amplifies losses below the barrier. The product name suggests cushioning, but the structure does the opposite below the barrier --- it accelerates losses. The barrier provides genuine protection in a range: if the underlying declines up to 30% (from 100% to 70%), the investor receives par. This is the "airbag" zone. Below 70%, the air runs out, and the leveraged loss kicks in.

The product is appropriate when the investor has moderate conviction on the underlying, views the barrier as sufficiently distant, and prefers a higher coupon than a standard barrier RC (which offers 1:1 loss below the barrier). The leverage provides a higher coupon by increasing the put premium relative to a standard barrier put. It is not appropriate when the investor does not understand leverage mechanics, when the investor would be surprised by losses exceeding the underlying's percentage decline, or when the investor focuses solely on the barrier level and ignores what happens below it. Product Control should verify the settlement formula at booking --- the leverage formula is the single most common source of settlement disputes on this product, because Termsheet language varies across issuers and the precise formula determines whether the leverage benefits or hurts the investor relative to a standard RC.

#### Desk shorthand

*Barrier RC; leveraged loss below cushion.*
