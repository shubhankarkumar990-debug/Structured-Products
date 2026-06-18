### Knock-Out Discounted Reverse Convertible

#### Definition

The Knock-Out Discounted Reverse Convertible is a structured note, issued as an equity-linked note (ELN) under an ISDA or MTN wrapper, that combines the discount-to-par issuance of the base Discounted Reverse Convertible with an upside knock-out barrier that triggers early redemption at par. The investor purchases the note below par, and the return is the capital gain between the discounted purchase price and par. The note has a discrete knock-out barrier observed at scheduled dates (typically quarterly). If the underlying closes at or above the knock-out level on any observation date, the note terminates early and the investor receives par --- realizing the full discount as an accelerated capital gain. If the knock-out is never triggered and the underlying closes at or above the put strike at maturity, the investor receives par. If the underlying closes below the put strike at maturity, the investor receives physical delivery of shares or cash settlement at the depreciated market value. There is no coupon. Capital protection is zero --- the knock-out barrier is an upside feature that accelerates the return on rally; it does not protect the investor's principal on the downside.

#### Construction

The note decomposes into two primitive instruments. The desk is long a zero-coupon bond funded at the issuer's credit curve, purchased at a discount to par. Against this, the desk is short an up-and-out European put struck at 100% of initial fixing with a knock-out barrier at 120% of initial fixing, observed discretely at quarterly intervals. The up-and-out put is cheaper than the vanilla European put used in the base Discounted RC because the knock-out reduces the probability of the put surviving to expiry --- if the underlying rallies to 120% at any observation, the put ceases to exist. This lower put premium translates directly into a smaller discount to par: the Knock-Out DRC offers a lower headline yield than the base DRC in exchange for the early-exit feature. The knock-out introduces path dependency. The vanilla DRC is priced in closed-form under Black-Scholes because the payoff depends only on the terminal value. The Knock-Out DRC requires Monte Carlo simulation or a discrete barrier adjustment (Broadie-Glasserman correction) because the payoff depends on the entire path of the underlying across observation dates.

#### Booking & systems

The book of record is NEMO, which carries the trade lifecycle, put strike level, knock-out barrier level, observation schedule, knock-out status flag, issue price, par redemption amount, settlement type, and fixing source. NEMO must carry the issue price as a separate field from par --- omission causes the same cascading P&L error as the base DRC. In addition, NEMO must carry the knock-out barrier level and the observation schedule, and must be updated to reflect the knock-out event if the barrier is breached. Risk and P&L run through Sophis, which prices the up-and-out put using a discrete barrier model, computes Delta, Gamma, and Vega, generates daily mark-to-market, and accretes the note value from issue price to par. The critical operational risk unique to this product is knock-out event synchronization: when the underlying breaches the knock-out barrier on an observation date, both NEMO and Sophis must record the event on the same date using the same closing price. If NEMO sources the closing price from the exchange official close and Sophis uses a Bloomberg composite, the two systems may disagree on whether the barrier was breached on a day when the close is near the 120% level. The legal document is the Termsheet, which defines the put strike, knock-out barrier, observation schedule, observation convention (close-of-business vs intraday), settlement on knock-out (par on T+2 vs next scheduled date), and fixing fallback rules. Murex is not used.

#### Pricing intuition

The dominant Greeks are short Delta and short Vega, with pronounced Gamma effects near the knock-out barrier. The structure's value derives from the sale of an up-and-out put. Because the put dies when the underlying reaches the knock-out level, the put premium is lower than for a vanilla put --- the investor is giving up some discount in exchange for the early-exit feature. The discount to par is therefore smaller than the base DRC for the same underlying, tenor, and volatility.

Three additional pricing levers distinguish this product from the base DRC. First, the knock-out barrier level: raising the barrier from 120% to 130% makes the knock-out less likely, increasing the put premium and the discount. Second, observation frequency: quarterly observations give the underlying four chances to breach the barrier over one year; switching to monthly observations gives twelve chances, making the knock-out more likely and reducing the put premium. Third, discrete vs continuous barrier pricing: the Termsheet specifies discrete observation, which means the underlying can trade above 120% intraday without triggering the knock-out. The discrete barrier put is worth more than a continuous barrier put because the barrier is tested less frequently. The Broadie-Glasserman correction estimates this premium at approximately 10--20 bps for quarterly observations on a 25-vol underlying.

Near the knock-out barrier, Delta becomes discontinuous and Gamma spikes. The desk faces pin risk on observation dates --- if the underlying closes at 119.5%, the put survives; at 120.5%, the put dies. Hedging near the barrier requires careful management of the Delta discontinuity.

#### Worked example (USD 10M)

**Trade parameters.** Par notional: USD 10M. Issue price: USD 9.28M (92.8% of par). Tenor: 1 year. Underlying: single stock, 25% implied volatility at inception. Put strike: 100% of initial fixing. Knock-out barrier: 120% of initial fixing. Observation: quarterly (4 dates). Settlement: physical delivery. No coupon.

**Economic decomposition.** The 7.2% discount to par (USD 720K on USD 10M par) reconciles as follows. The up-and-out put (100% strike, 120% KO barrier, 25-vol, 1-year, quarterly observation) prices at 4.2% of par (USD 420K). This compares to 5.5% for the vanilla put in the base DRC --- the knock-out reduces the put premium by 1.3 percentage points. Issuer funding at the credit curve contributes 2.0% per annum (USD 200K). Funds transfer pricing absorbs 0.6% per annum (USD 60K). The residual desk margin is 0.4% per annum (USD 40K). Arithmetic check: up-and-out put premium 4.2% plus issuer funding 2.0% plus FTP 0.6% plus desk margin 0.4% equals 7.2% discount to par.

**Good scenario --- knock-out triggered.** The underlying closes at 125% of initial fixing at the Q2 observation date (6 months). The knock-out is triggered. The note redeems at par (USD 10M). The investor realizes the full discount of USD 720K on an investment of USD 9.28M in 6 months. Annualized return: approximately 15.5% on invested capital.

**Good scenario --- maturity.** The underlying closes at 110% at maturity. No knock-out was triggered (the underlying never reached 120% on an observation date). The put expires out-of-the-money. The investor receives par (USD 10M). Capital gain: USD 720K, or 7.8% on invested capital over 1 year.

**Bad scenario.** The underlying closes at 60% of initial fixing at maturity. No knock-out was triggered. The put is exercised. The investor receives physical delivery of shares worth 60% of par (USD 6M) on an investment of USD 9.28M. Loss: USD 3.28M, or 35.3% of invested capital. The loss percentage is higher than the base DRC's 34.4% because the discount is smaller (7.2% vs 8.5%), so the invested amount is higher relative to the loss.

#### Reconciliation specifics

**Knock-out event** --- the Termsheet specifies which closing price governs the knock-out determination (exchange official close, Bloomberg composite, or other source) and whether the observation is close-of-business only or includes intraday levels --- if NEMO records a knock-out triggered on a date where Sophis does not (because they use different closing-price sources), the two systems will diverge on the note's status: NEMO will show the note as redeemed while Sophis continues to price a live option, producing an irreconcilable P&L break.

**Issue price vs par** --- identical risk to the base DRC: NEMO must carry the issue price (92.8%) as a separate field from par, or the position notional is overstated and Day 1 P&L is incorrect.

**Observation schedule** --- NEMO's observation dates must exactly match the Termsheet schedule --- if NEMO has a different non-business-day adjustment convention than the Termsheet, an observation may shift to a different date, and the closing price on the shifted date may be above or below the barrier when the original date's close was the opposite.

**Settlement timing on knock-out** --- the Termsheet may specify par redemption on T+2 from the knock-out observation date, or on the next scheduled payment date --- NEMO must carry the correct settlement date for the early redemption, or cash flow timing will not match the investor's expectation and the desk's funding position.

**Accretion schedule** --- Sophis accretes the note from issue price to par over the original tenor --- if the knock-out triggers mid-life, the accretion must accelerate to par on the knock-out settlement date, and the unaccreted portion hits P&L as a one-time mark.

#### Desk view

The Knock-Out Discounted Reverse Convertible is the base DRC with an upside accelerator. The investor accepts a smaller discount (7.2% vs 8.5%) in exchange for the possibility of realizing that discount early if the underlying rallies through the knock-out barrier. The economic intuition is straightforward: the investor is paying for an escape hatch on the upside by giving up yield. The downside risk is unchanged --- below the put strike, the investor bears the full depreciation of the underlying.

The product is appropriate when the investor has a bullish bias on the underlying and prefers capital gain treatment, but wants an early-exit mechanism if the rally materializes quickly. It is more attractive when the underlying has higher volatility (increasing the probability of the knock-out triggering). It is not appropriate when the investor's primary concern is maximizing discount (the base DRC offers a larger discount), when the underlying has low volatility (the knock-out is unlikely to trigger, making the feature worthless while still compressing the discount), or when the investor does not understand that the knock-out provides no downside protection. Product Control should verify the knock-out observation schedule at booking and confirm that the barrier trigger mechanism (closing price source, observation convention) is consistent between NEMO, Sophis, and the Termsheet.

#### Desk shorthand

*Discounted par; sold KO put, early exit on rally.*
