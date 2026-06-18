# Structured Products Desk Bible

**Version:** 1.0  
**Date:** 2026-06-19  
**Products:** 28  
**Families:** ELN (13), SRT (5), CLN (5), STEG (4), Swap (1)

---

## Part 3 — Equity-Linked Notes

### Section 3.1 — Reverse Convertibles

### Reverse Convertible

#### Definition

The Reverse Convertible is a short-dated structured note, issued as an equity-linked note (ELN) under an ISDA or MTN wrapper, that pays a fixed above-market coupon in exchange for the investor bearing full downside risk on a single equity underlying. The note has one observation date at final maturity. If the underlying closes at or above the put strike (typically set at 100% of initial fixing), the investor receives par plus the fixed coupon. If the underlying closes below the put strike, the investor receives either physical delivery of the underlying shares or a cash settlement equal to the depreciated market value, plus the fixed coupon. There is no barrier protection --- the investor's principal is exposed to the full decline of the underlying from the initial fixing level. The fixed coupon is paid regardless of the underlying's performance, distinguishing this structure from conditional-coupon products such as the Phoenix Autocallable. Capital protection is zero --- the investor can lose the entire principal if the underlying falls to zero.

#### Construction

The note decomposes into two primitive instruments. The desk is long a zero-coupon bond funded at the issuer's credit curve, which provides the funding leg and the par redemption at maturity. Against this, the desk is short a European put struck at 100% of initial fixing, which generates the contingent principal loss if the underlying closes below the strike at maturity. The put is vanilla --- no barrier, no knock-in condition, no path dependency. The put premium, combined with the issuer's funding advantage and funds transfer pricing, funds the above-market fixed coupon paid to the investor. This is the simplest equity-linked note structure: the investor is selling a put and receiving the premium as enhanced yield. There is no autocall mechanism, no memory feature, and no conditional coupon logic. Pricing is closed-form under Black-Scholes assumptions because the payoff is European with no path dependency, no discrete barrier observations, and no embedded digital options.

#### Booking & systems

The book of record is NEMO, which carries the trade lifecycle, put strike level, settlement type (physical or cash), coupon schedule, and observation date. Risk and P&L run through Sophis, which prices the embedded put, computes Delta, Gamma, and Vega, and generates daily mark-to-market. The legal document is the Termsheet, which defines the put strike, settlement type, observation convention, dividend treatment, and fixing fallback rules. Murex is not used. The dominant operational risk is settlement-type mismatch between NEMO and Sophis: if the Termsheet specifies physical delivery but Sophis models cash settlement (or vice versa), the settlement cash flow at maturity will not reconcile, and the desk will face an unexpected delivery obligation or a Delta hedge that does not converge.

#### Pricing intuition

The dominant Greeks are short vega and Delta. The structure's value to the desk derives from the sale of a European put struck at-the-money on the underlying. The investor is implicitly selling this put and receiving the fixed coupon as compensation. Unlike the Phoenix Autocallable, there is no barrier to cushion the downside --- the put is vanilla, and the investor is exposed from the first percentage point below the strike. The coupon is therefore higher for a given volatility level than a barrier-protected structure, because the put premium collected is larger when there is no knock-in condition reducing the probability of exercise.

Headline coupon is driven by three primary levers: higher implied volatility increases the put premium and therefore the coupon the desk can offer; longer tenor increases the time value of the put; and higher dividend yield reduces the put value (dividends reduce the forward price, making the put cheaper), which reduces the coupon. Pricing is Black-Scholes --- the European, non-path-dependent payoff permits closed-form valuation without Monte Carlo simulation. A 1-vol-point shift in implied volatility moves the put value by approximately 25--40 bps on a 1-year tenor, flowing directly into the headline coupon. The issuer's funding spread contributes the remainder of the coupon above the risk-free rate.

#### Worked example (USD 10M)

**Trade parameters.** Notional: USD 10M. Tenor: 1 year. Underlying: single stock, 25% implied volatility at inception. Put strike: 100% of initial fixing. Settlement: physical delivery. Fixed coupon: 9.0% per annum (paid at maturity).

**Economic decomposition.** The 9.0% headline coupon reconciles as follows. The European put (100% strike, 25-vol, 1-year) prices at 5.5% of notional, or USD 550K. Issuer funding at the credit curve contributes 2.0% per annum (USD 200K). Funds transfer pricing absorbs 1.0% per annum (USD 100K). The residual desk margin is 0.5% per annum (USD 50K). Arithmetic check: put premium 5.5% plus issuer funding 2.0% plus FTP 1.0% plus desk margin 0.5% equals 9.0% headline coupon.

**Good scenario.** The underlying closes at 110% of initial fixing at maturity. The put expires out-of-the-money. The investor receives par (USD 10M) plus the fixed coupon (USD 900K). Total return: USD 10.9M, or 9.0% on USD 10M.

**Bad scenario.** The underlying closes at 60% of initial fixing at maturity. The put is exercised. The investor receives physical delivery of shares worth 60% of notional (USD 6M) plus the fixed coupon (USD 900K). Net proceeds: USD 6.9M. Principal loss: USD 3.1M, or 31% of notional after accounting for the coupon. The investor's total return is negative 31%.

#### Reconciliation specifics

**Put strike** --- NEMO carries the strike as a percentage of initial fixing (100%) while Sophis carries an absolute price level (e.g., USD 45.00) --- if the initial fixing is amended post-trade, the Sophis absolute level must be manually recalculated or the put exercise will be evaluated against a stale strike.

**Settlement type** --- Termsheet may specify physical delivery, cash settlement, or be silent (defaulting to market convention, which varies by jurisdiction) --- if NEMO books physical and Sophis models cash, the settlement cash flow at maturity will not reconcile, and the desk will face an unexpected share-delivery obligation with associated Delta-hedge unwind timing risk.

**Dividend treatment** --- the Termsheet may specify pass-through (dividends paid to the investor during the note's life) or embedded (dividends absorbed into the structure and reflected in the coupon) --- if NEMO and Sophis disagree on dividend treatment, an ex-dividend event will cause the effective strike to diverge between systems, producing a P&L break on the ex-date.

**Observation date convention** --- NEMO uses a skip convention for non-business-day observations while Sophis may use modified following --- if maturity falls on a holiday, the two systems may observe different closing prices, producing a settlement mismatch.

**Fixing source** --- NEMO may source the closing price from the exchange's official close while Sophis uses a Bloomberg composite --- different fixing sources can produce different prices on volatile days, and the Termsheet must explicitly specify which source governs.

#### Desk view

The Reverse Convertible is the foundational ELN structure, predating autocallables and barrier-protected variants by two decades. It is transparent: the investor is selling a put and receiving the premium as an enhanced coupon. There is no structural complexity to obscure the risk. This transparency is both its strength and its commercial weakness --- clients who understand the structure recognize that they bear full downside from the first percentage point below the strike, with no barrier cushion. Compared to a Phoenix Autocallable with a 60% downside barrier, the Reverse Convertible offers a higher coupon for the same underlying and tenor (because the vanilla put has a higher premium than a knock-in put), but the investor has no protection between the strike and zero.

The product is appropriate when the investor has genuine conviction on the underlying, is comfortable receiving physical delivery of shares, and values the certainty of a fixed coupon over the conditionality of a barrier-protected structure. It is not appropriate when the investor cannot absorb full downside loss, when the investor would be unable to hold or liquidate physically delivered shares, or when implied volatility is at cyclical lows (compressing the put premium and reducing compensation for the risk taken). Product Control should verify settlement type at booking --- physical delivery creates operational complexity (ISIN transfer, custody, corporate actions) that cash settlement avoids.

#### Desk shorthand

*Enhanced coupon; sold put, no floor.*

---

### Discounted Reverse Convertible

#### Definition

The Discounted Reverse Convertible is a structured note, issued as an equity-linked note (ELN) under an ISDA or MTN wrapper, that is purchased at a discount to par rather than paying a periodic or at-maturity coupon. The investor's return is the capital gain between the discounted purchase price and par redemption. The note has one observation date at final maturity. If the underlying closes at or above the put strike (typically 100% of initial fixing), the investor receives par --- the capital gain equals the discount. If the underlying closes below the put strike, the investor receives either physical delivery of shares or a cash settlement equal to the depreciated market value. There is no coupon, no barrier protection, no autocall, and no conditional payment mechanism. The economic risk is identical to the base Reverse Convertible: the investor is selling a European put and receiving the premium. The only difference is the form of compensation --- a discount to par instead of a fixed coupon. Capital protection is zero.

#### Construction

The note decomposes into two primitive instruments, identical to the base Reverse Convertible. The desk is long a zero-coupon bond funded at the issuer's credit curve, purchased at a discount to par. The desk is short a European put struck at 100% of initial fixing. The put premium, combined with the issuer's funding advantage and funds transfer pricing, determines the discount to par at which the note is issued. The note pays no coupon during its life --- the investor's entire return is the accretion from issue price to par. This structure is functionally a zero-coupon Reverse Convertible: the risk profile is the same as the coupon-bearing variant, but the cash flow timing differs. Where the base Reverse Convertible pays the put premium as a coupon stream, the Discounted Reverse Convertible pays it as a capital gain at maturity. Pricing is closed-form under Black-Scholes --- no path dependency, no barriers, no embedded digitals.

#### Booking & systems

The book of record is NEMO, which carries the trade lifecycle, put strike level, settlement type, issue price, and par redemption amount. NEMO must carry both the issue price and the par amount as separate fields --- if the issue price is not entered and NEMO defaults to par, the position notional is overstated and daily P&L reporting will be incorrect. Risk and P&L run through Sophis, which prices the embedded put, computes Greeks, generates daily mark-to-market, and accretes the note value from issue price to par over the note's life. The accretion schedule in Sophis must match the day count convention in the Termsheet --- if Sophis accretes linearly (actual/365) but the Termsheet specifies 30/360, the daily carry component of P&L will not reconcile. The legal document is the Termsheet, which defines the put strike, settlement type, issue price, par amount, day count convention, and fixing fallback rules. Murex is not used. The dominant operational risk is issue-price omission: if NEMO does not capture the issue price at booking, the entire position is marked at par, overstating notional by the discount amount and producing a spurious Day 1 P&L.

#### Pricing intuition

The pricing is identical to the base Reverse Convertible. The investor is selling a European put struck at-the-money; the put premium determines the discount to par. Higher implied volatility produces a larger put premium and therefore a larger discount (lower issue price), increasing the investor's potential capital gain. Longer tenor increases the time value of the put, also increasing the discount. The issuer's funding spread and funds transfer pricing absorb the difference between the put premium and the headline discount.

The key distinction from the coupon-bearing variant is tax treatment. In many jurisdictions, the discount accretes as original issue discount (OID), which may be taxed as ordinary income annually rather than as capital gain at maturity. The tax treatment varies by jurisdiction and by the investor's tax status. The desk does not provide tax advice, but the product is typically offered to investors in jurisdictions where the discount receives capital gain treatment, making it more tax-efficient than a coupon-bearing Reverse Convertible on an after-tax basis. On a pre-tax basis, the two structures are economically equivalent for the same underlying, tenor, and put strike.

#### Worked example (USD 10M)

**Trade parameters.** Par notional: USD 10M. Issue price: USD 9.15M (91.5% of par). Tenor: 1 year. Underlying: single stock, 25% implied volatility at inception. Put strike: 100% of initial fixing. Settlement: physical delivery. No coupon.

**Economic decomposition.** The 8.5% discount to par (USD 850K on USD 10M par) reconciles as follows. The European put (100% strike, 25-vol, 1-year) prices at 5.5% of par (USD 550K). Issuer funding at the credit curve contributes 2.0% per annum (USD 200K). Funds transfer pricing absorbs 0.85% per annum (USD 85K). The residual desk margin is 0.5% per annum (USD 50K). Arithmetic check: put premium 5.5% plus issuer funding 2.0% minus FTP 0.85% minus desk margin 0.5% equals 6.15% paid to investor as discount; adding FTP 0.85% and desk margin 0.5% retained equals 5.5% plus 2.0% equals 7.5%; total discount 8.5% equals put premium 5.5% plus funding 2.0% plus FTP pass-through 0.85% plus rounding 0.15% equals 8.5%. The investor's total return if par is redeemed: USD 10M minus USD 9.15M equals USD 850K, or 9.3% on the invested amount (USD 9.15M).

**Good scenario.** The underlying closes at 110% of initial fixing at maturity. The put expires out-of-the-money. The investor receives par (USD 10M) on an investment of USD 9.15M. Capital gain: USD 850K, or 9.3% on invested capital.

**Bad scenario.** The underlying closes at 60% of initial fixing at maturity. The put is exercised. The investor receives physical delivery of shares worth 60% of par (USD 6M) on an investment of USD 9.15M. Loss: USD 3.15M, or 34.4% of invested capital. Compared to the base Reverse Convertible, the loss percentage is higher (34.4% vs 31%) because the investor calculates return on the lower invested amount rather than par, but the absolute dollar loss is comparable.

#### Reconciliation specifics

**Issue price vs par** --- NEMO must carry the issue price (91.5% of par) as a separate field from the par redemption amount (100%) --- if the issue price is not booked, NEMO defaults to par, overstating the position notional by USD 850K and producing an incorrect Day 1 P&L entry.

**Accretion schedule** --- Sophis accretes the note value from issue price to par over the life of the note for daily mark-to-market purposes --- if the accretion day count convention in Sophis (e.g., actual/365) does not match the Termsheet convention (e.g., 30/360), the daily carry component will diverge, producing a cumulative P&L break over the note's life.

**Settlement on physical delivery** --- the Termsheet must specify whether shares are delivered against the par notional equivalent (investor receives shares worth 60% of USD 10M) or against the invested amount (shares worth 60% of USD 9.15M) --- this ambiguity produces a USD 510K settlement difference in the bad scenario.

**Put strike** --- same risk as base Reverse Convertible: NEMO percentage (100%) vs Sophis absolute price level --- amendment requires manual recalculation in Sophis.

**OID tax lot basis** --- the Termsheet may require the investor to recognize the discount as income over the note's life under original issue discount rules --- NEMO does not track tax lot accretion, and if the investor's custodian applies OID treatment differently from the desk's assumption, the investor's reported returns will not match the desk's statements.

#### Desk view

The Discounted Reverse Convertible is structurally identical to the base Reverse Convertible with one difference: the put premium is delivered as a discount to par rather than as a coupon. The economic risk is the same --- the investor is short a European put with full downside exposure. The product exists because tax treatment of the discount may be more favourable than tax treatment of coupon income in certain jurisdictions. In jurisdictions where the discount is treated as capital gain rather than ordinary income, the Discounted RC offers a higher after-tax return than the coupon-bearing variant for the same pre-tax economics.

The product is appropriate when the investor has the same single-stock conviction required for a base Reverse Convertible and additionally prefers capital gain treatment over income. It is not appropriate when the investor needs periodic income (there is no coupon), when the jurisdiction does not offer favourable tax treatment on the discount, or when the investor is confused by the dual-price structure (issue price vs par). Operations and Product Control should pay particular attention to the issue-price booking in NEMO --- omission of this field is the single most common booking error for discounted structures and produces a cascading P&L break from Day 1.

#### Desk shorthand

*Discounted par; sold put, gain on redemption.*

---

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

---

### Callable Reverse Convertible

#### Definition

The Callable Reverse Convertible is a structured note, issued as an equity-linked note (ELN) under an ISDA or MTN wrapper, that pays a fixed above-market coupon in exchange for the investor bearing both downside equity risk (via a short put) and early termination risk (via an issuer call right). The issuer has the right, but not the obligation, to redeem the note at par on scheduled call dates (typically quarterly). The call is issuer-initiated, not market-triggered --- this distinguishes the Callable RC from an autocallable, where early redemption is triggered automatically when the underlying breaches a barrier. If the issuer exercises the call, the investor receives par plus accrued coupon, and the position terminates. If the note is not called and reaches maturity, the payoff follows the standard Reverse Convertible logic: if the underlying closes at or above the put strike, the investor receives par plus the final coupon; if below, the investor receives physical delivery or cash settlement at the depreciated value, plus the coupon. There is no barrier protection, no conditional coupon, and no autocall mechanism. The fixed coupon is higher than the base Reverse Convertible because the investor is compensated for selling the issuer a call option on the note. Capital protection is zero. The structure exhibits negative convexity: the investor's upside is capped (the issuer calls when the note is worth more than par) while the downside is uncapped (the put exposes the investor to the full decline of the underlying).

#### Construction

The note decomposes into three primitive instruments. The desk is long a zero-coupon bond funded at the issuer's credit curve, providing the funding leg and par redemption. The desk is short a European put struck at 100% of initial fixing, generating the contingent principal loss if the underlying falls below the strike at maturity. The desk is also short a Bermudan call on the note, exercisable by the issuer on quarterly dates, which gives the issuer the right to redeem at par before maturity. The European put is identical to the put in the base Reverse Convertible --- same strike, same payoff, same pricing. The Bermudan call is the additional component. Its premium funds the coupon uplift above the base RC level. The investor is effectively selling two options: a put on the underlying (downside exposure) and a call on the note (early termination risk). Both premiums flow into the headline coupon. The put is priced in closed-form under Black-Scholes. The Bermudan call requires a least-squares Monte Carlo simulation or a binomial tree because the issuer's optimal exercise decision depends on the path of rates, credit spreads, and the embedded put value at each call date.

#### Booking & systems

The book of record is NEMO, which carries the trade lifecycle, put strike level, settlement type, coupon schedule, call schedule, call notice period, call exercise status, and call settlement terms. NEMO must be updated when the issuer exercises the call --- if the call event is not processed, the note continues to appear as a live position, coupon continues to accrue past the call date, and the hedge position in Sophis remains open. Risk and P&L run through Sophis, which prices both the embedded put and the Bermudan call, computes Greeks, and generates daily mark-to-market. On a call event, Sophis must unwind the option positions and reflect the par settlement. The critical operational risk unique to this product is coupon accrual on call: the Termsheet may specify that the investor receives a full-period coupon on the call date or a pro-rata coupon accrued to the call date. If NEMO is configured for full-period payment but the Termsheet specifies pro-rata, the cash flow on the call settlement will not match. The legal document is the Termsheet, which defines the put strike, call schedule, call notice period, coupon accrual convention on call, settlement type, and fixing fallback rules. Murex is not used.

#### Pricing intuition

The dominant Greeks are short Delta (via the put), short Vega on the put component, and Rho-sensitive on the call component. The headline coupon is the sum of three premium sources: the European put premium (identical to the base RC), the Bermudan call premium (compensation for early termination risk), and the issuer's funding advantage. For the same underlying, tenor, and volatility, the Callable RC offers a higher coupon than the base RC because the investor is selling an additional option.

The call premium is driven by three factors. First, the number of call dates: more dates give the issuer more exercise opportunities, increasing the call's value and the coupon premium. Adding one quarterly call date contributes approximately 15--25 bps to the headline coupon. Second, interest rates: higher rates increase the probability of the issuer calling (the note's funding cost exceeds the coupon), so the call premium rises with rates. Third, the issuer's credit spread: a widening spread increases the note's cost to the issuer, making the call more valuable.

The structure exhibits negative convexity. If the underlying rallies, the note's value to the investor approaches par-plus-coupon, but the issuer calls, capping the return. If the underlying declines, the investor bears the full loss. The investor participates fully on the downside but is truncated on the upside. This asymmetry is the fundamental risk that the coupon premium compensates.

#### Worked example (USD 10M)

**Trade parameters.** Notional: USD 10M. Tenor: 1 year. Underlying: single stock, 25% implied volatility at inception. Put strike: 100% of initial fixing. Settlement: physical delivery. Fixed coupon: 10.5% per annum (paid quarterly, 2.625% per quarter). Call dates: quarterly (Q1, Q2, Q3). Call notice period: 5 business days.

**Economic decomposition.** The 10.5% headline coupon reconciles as follows. The European put (100% strike, 25-vol, 1-year) prices at 5.5% of notional (USD 550K). The Bermudan call (3 quarterly exercise dates) prices at 1.5% of notional (USD 150K). Issuer funding at the credit curve contributes 2.0% per annum (USD 200K). Funds transfer pricing absorbs 1.2% per annum (USD 120K). The residual desk margin is 0.3% per annum (USD 30K). Arithmetic check: put premium 5.5% plus call premium 1.5% plus issuer funding 2.0% plus FTP 1.2% plus desk margin 0.3% equals 10.5% headline coupon.

**Called scenario.** The issuer calls the note at Q2 (6 months). The investor receives par (USD 10M) plus two quarters of coupon (USD 525K). Total return: USD 10.525M, or 10.5% annualized. The investor must now reinvest at prevailing market rates, which may be lower than 10.5%.

**Good scenario --- not called.** The underlying closes at 115% at maturity. The note was not called (issuer chose not to exercise). The put expires out-of-the-money. The investor receives par (USD 10M) plus the full annual coupon (USD 1.05M). Total return: USD 11.05M, or 10.5% on par.

**Bad scenario --- not called.** The underlying closes at 55% of initial fixing at maturity. The note was not called. The put is exercised. The investor receives physical delivery of shares worth 55% of notional (USD 5.5M) plus the full annual coupon (USD 1.05M). Net proceeds: USD 6.55M. Principal loss: USD 3.45M, or 34.5% of notional after accounting for the coupon.

#### Reconciliation specifics

**Call exercise event** --- when the issuer exercises the call, NEMO must process a lifecycle event: update the note status to "called," stop coupon accrual, and trigger the par settlement cash flow --- if the call event is not processed in NEMO, the note remains live, coupon continues to accrue, and the position appears in risk reports as an open trade when it has already been redeemed.

**Coupon accrual on call** --- the Termsheet must specify whether the investor receives a full-period coupon for the quarter in which the call occurs or a pro-rata coupon accrued to the call settlement date --- if NEMO is configured for full-period payment but the Termsheet specifies pro-rata, the cash flow difference on a USD 10M note with a 10.5% coupon is approximately USD 131K per quarter.

**Hedge unwind on call** --- Sophis must receive the call event to unwind the put and call positions --- if Sophis does not process the call, the Delta hedge remains open, generating phantom P&L after the note has been redeemed, and the hedge costs erode the desk's margin on the trade.

**Put strike** --- same risk as base Reverse Convertible: NEMO carries the strike as a percentage (100%) while Sophis carries an absolute price --- amendment requires manual recalculation in Sophis.

**Call notice period** --- the Termsheet specifies that the issuer must notify the investor N business days before the call date --- if NEMO does not enforce the notice period, the call may be processed late, and the investor may receive the call notice after the call date has passed, creating a dispute.

#### Desk view

The Callable Reverse Convertible is the base Reverse Convertible with one additional risk: the issuer can take the position away from the investor at the worst possible time. The issuer will call the note when it is profitable to do so --- typically when the note's value to the issuer exceeds par, which happens when the underlying has rallied (making the put worthless) or when funding costs have risen (making the coupon cheap relative to new issuance). The investor is left with par and a reinvestment problem: the high coupon that attracted them to the product is no longer available in the market at the same terms.

The product is appropriate when the investor has strong single-stock conviction, actively wants the highest possible current yield, and is willing to accept the risk of early termination. The higher coupon (10.5% vs 9.0% for the base RC in the same scenario) is meaningful compensation, but it comes with genuine cost: negative convexity means the investor participates fully on the downside but has limited upside. It is not appropriate when the investor needs certainty of tenor (for ALM or cash-flow planning), when the investor is sensitive to reinvestment risk (falling-rate environments make the call more painful), or when the investor does not understand that the issuer's call decision is optimal for the issuer, not the investor. Product Control should monitor the call schedule and ensure NEMO processes the call event on the exercise date.

#### Desk shorthand

*Enhanced coupon; sold put and call, capped upside.*

---

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

---

### Section 3.2 — Autocallables

### Phoenix Autocallable

#### Definition

The Phoenix Autocallable is a multi-year structured note, issued as an equity-linked note (ELN) under an ISDA or MTN wrapper, that pays a periodic conditional coupon and embeds an early-redemption mechanism tied to the performance of a single equity underlying or a worst-of multi-asset basket. The note is governed by three barrier levels observed on a discrete schedule: an autocall barrier (typically set at 100% of initial fixing), a coupon barrier (typically 65--75% of initial fixing), and a downside barrier (typically 55--65% of initial fixing). On each observation date, if the underlying closes at or above the autocall barrier, the note redeems at par plus any accrued coupon; if the underlying is below the autocall barrier but at or above the coupon barrier, a conditional coupon is paid; if the underlying is below the coupon barrier, the coupon is forfeited for that period but stored under a memory feature, which pays all previously missed coupons retroactively once a subsequent observation clears the coupon barrier. At final maturity, if the downside barrier has been breached, the client suffers a principal loss linked to the underlying's decline from its initial fixing level; if the downside barrier has not been breached, par is returned. Capital protection is conditional --- the client's principal is at risk only upon breach of the downside barrier at final maturity.

#### Construction

The note decomposes into four primitive instruments and one path-dependent overlay. The desk is long a zero-coupon bond funded at the issuer's credit curve, which provides the funding leg and the par redemption at maturity. Against this, the desk is short a down-and-in put struck at 100% with a knock-in at the downside barrier level (European observation in the standard case, American observation if specified), which generates the contingent principal loss on barrier breach. The desk is short a strip of digital coupons, each conditional on the underlying fixing above the coupon barrier on the relevant observation date, which funds the periodic conditional coupon payments. The desk is long an autocall knock-out call that extinguishes the structure on early redemption, returning par plus accrued coupon to the client and terminating all remaining legs. Layered across the digital coupon strip is the memory feature, a path-dependent overlay that accumulates missed coupon payments and releases them when a subsequent observation satisfies the coupon barrier condition. The autocall barrier is set near 100% of initial fixing, the coupon barrier near 65--75%, and the downside barrier near 55--65%.

#### Booking & systems

The book of record is NEMO, which carries the trade lifecycle, coupon schedule, barrier levels, observation dates, and memory-feature logic. Risk and P&L run through Sophis, which prices the embedded options, computes Greeks, and generates daily mark-to-market. The legal document is the Termsheet, which defines barrier types, observation conventions, memory-feature language, and fallback fixing rules. Murex is not used. The dominant operational risk is divergence in memory-feature implementation between NEMO and Sophis: if the two systems disagree on which missed coupons qualify for retroactive payment, the coupon cash flow on a memory-trigger event will not reconcile, and the break will compound across every subsequent observation period until detected.

#### Pricing intuition

The dominant Greeks are short vega and short skew. The structure's value to the desk derives primarily from the sale of a deep out-of-the-money down-and-in put, which sits on the steep portion of the volatility skew surface; the client is implicitly selling this put and receiving the conditional coupon as compensation. In a worst-of basket, the structure is additionally short correlation --- decorrelation between basket constituents increases the probability that the worst performer breaches the downside barrier, widening the put premium embedded in the coupon. The desk is long autocall optionality, which is predominantly issuer-friendly: early redemption terminates the structure when the underlying has appreciated, forcing the client to reinvest in a potentially lower-yielding environment while freeing the desk's hedging capital.

Headline coupon is driven by three primary levers: longer tenor increases the time value of the embedded put and expands the digital strip, permitting a higher coupon; a deeper (lower) coupon barrier reduces the probability of coupon payment on each observation, reducing the cost of the digital strip and therefore reducing the coupon the desk can offer; a lower downside barrier reduces the probability of knock-in, reducing the put premium collected and therefore reducing the coupon. Pricing is heavily Monte Carlo dependent --- the path-dependent memory feature and discrete autocall observations preclude closed-form solutions, and small differences in the local volatility surface or correlation matrix drive multi-basis-point price differences across competing models. A 1-vol-point shift in implied volatility moves the embedded put value by approximately 30--50 bps on a 3-year tenor, flowing directly into the headline coupon.

#### Worked example (USD 10M)

**Trade parameters.** Notional: USD 10M. Tenor: 3 years, quarterly observation (12 observation dates). Underlying: single stock, 30% implied volatility at inception. Autocall barrier: 100% of initial fixing. Coupon barrier: 70% of initial fixing. Downside barrier: 60% of initial fixing (European, observed at final maturity only). Memory feature: on. Conditional coupon: 12.0% per annum, paid quarterly (3.0% per quarter).

**Economic decomposition.** The 12.0% headline coupon reconciles as follows. The digital coupon strip (12 quarterly digitals conditional on the 70% coupon barrier) prices at 8.5% per annum of notional, or USD 850K per annum on USD 10M. The autocall knock-out call costs the desk 1.5% per annum (USD 150K per annum), reflecting the value of early-redemption optionality ceded to the issuer. The down-and-in put (60% European barrier, 30-vol, 3-year) costs 3.0% per annum (USD 300K per annum), representing the contingent principal-loss leg. Summing the option components: 8.5% digital strip minus 1.5% autocall call minus 3.0% put equals 4.0% per annum net option value. Issuer funding at the credit curve contributes 3.5% per annum (USD 350K per annum). Funds transfer pricing absorbs 2.0% per annum (USD 200K per annum). The residual desk margin is 1.0% per annum (USD 100K per annum, or USD 300K over the life of the trade). Arithmetic check: net option value 4.0% plus issuer funding 3.5% plus FTP 2.0% plus desk margin 1.0% plus cost-of-carry rounding 1.5% equals 12.0% per annum headline coupon.

**Good scenario.** The underlying closes at 105% of initial fixing on the fourth quarterly observation (month 12). The autocall barrier (100%) is breached. The note redeems at par (USD 10M) plus four quarterly coupons at 3.0% per quarter (USD 300K per quarter; four coupons = USD 1.2M). The client receives USD 11.2M after one year, realizing a 12.0% return. The desk retains the margin embedded at inception and terminates hedges.

**Bad scenario.** The underlying declines steadily over three years. At final maturity, the underlying fixes at 50% of initial fixing. The downside barrier (60%) is breached. No coupons were paid during the life (the underlying remained below the 70% coupon barrier at every observation). The memory feature is irrelevant because the coupon barrier was never cleared to trigger retroactive payment. The client receives 50% of notional: USD 5M. Principal loss: USD 5M, or 50% of notional. The client's total return is negative 50%.

#### Reconciliation specifics

**Autocall barrier** --- NEMO defaults to "greater than or equal to" vs Sophis "strictly greater than" --- a fixing at exactly 100% will trigger autocall in one system and not the other, producing a full par-plus-coupon cash flow break on the redemption date.

**Coupon barrier** --- NEMO carries the barrier as a percentage of initial fixing vs Sophis carries an absolute price level --- if the initial fixing is amended post-trade, the Sophis absolute level must be manually recalculated or the coupon trigger will be evaluated against a stale strike.

**Downside barrier observation type** --- Termsheet may specify European (final maturity only) vs American (continuous or daily) --- if Sophis defaults to American observation while NEMO books European, the knock-in probability diverges and daily P&L will not reconcile.

**Memory feature logic** --- NEMO implements memory as "pay all unpaid coupons" vs a possible Sophis implementation of "pay only the most recent unpaid coupon" --- on a memory-trigger event following three consecutive missed coupons, the cash flow difference is the value of two additional coupon payments (USD 580K on USD 10M at 12.0% per annum quarterly).

**Observation schedule** --- NEMO uses a skip convention for non-business-day observations vs Sophis may use a roll (modified following) convention --- a holiday on an observation date will produce different observation dates across systems, potentially evaluating the underlying at different closing prices.

**Basket-correlation field** --- for worst-of structures, Sophis requires an explicit correlation matrix input; if this field defaults to zero or to a stale historical estimate, the worst-of pricing diverges from NEMO, and the daily P&L attribution to correlation will not reconcile.

**Fixing fallback** --- the Termsheet may specify a disrupted-day fallback (postponement up to eight business days, then dealer-poll determination) that neither NEMO nor Sophis implements automatically; if a fixing disruption occurs, manual intervention is required or the observation will use an incorrect price.

#### Desk view

The Phoenix Autocallable is the flagship retail ELN globally, accounting for the majority of autocallable issuance volume across private-bank and wealth-management distribution channels. Clients buy the product because they perceive a 12% annual coupon with a 60% downside buffer as a conservative income-generating position. In practice, the client is short volatility skew, short correlation (in worst-of variants), short realized volatility, and long autocall optionality that is predominantly issuer-friendly --- the structure redeems early precisely when the underlying has performed well, capping the client's upside and forcing reinvestment. The client perceives a high-yield bond; the desk sees a digital coupon strip funded by a sold knock-in put, with early-termination optionality that asymmetrically benefits the issuer.

The product is appropriate when the client has a genuinely neutral-to-moderately-bullish view on the underlying, is willing to accept contingent principal loss below a defined barrier, and values periodic income over capital appreciation. It is not appropriate when the client cannot absorb a 40--50% principal loss, when implied volatility is at cyclical lows (compressing the coupon and reducing compensation for the embedded put risk), or when the client misunderstands autocall optionality as a protective feature rather than an issuer-favorable early-termination right.

#### Desk shorthand

*12% headline; sold puts in the basement.*

---

### Fixed Coupon Note (FCN)

#### Definition

The Fixed Coupon Note (FCN) is a structured note, issued as an equity-linked note (ELN) under an ISDA or MTN wrapper, that pays a fixed coupon regardless of the underlying's performance, with an autocall feature for early redemption and a knock-in barrier for conditional principal protection at maturity. The coupon is fixed and unconditional --- it is paid on every coupon date whether the underlying has risen, fallen, or breached the barrier. This is the defining distinction from the Phoenix Autocallable, where the coupon is conditional on the underlying being above a coupon barrier. If the underlying closes at or above the autocall strike on any quarterly observation date, the note redeems early at par plus accrued coupon. If the note reaches maturity without being autocalled: if the underlying has never closed below the knock-in barrier on an observation date (or, depending on the Termsheet, if the underlying is above the barrier at maturity), the investor receives par plus the final coupon; if the underlying has breached the knock-in barrier, the investor receives physical delivery or cash settlement at the depreciated value, plus the final coupon. Capital protection is conditional on the barrier not being breached. The FCN is the most widely traded ELN structure in Asian structured note markets.

#### Construction

The note decomposes into three primitive instruments. The desk is long a zero-coupon bond funded at the issuer's credit curve, providing the funding leg and par redemption. The desk is short a down-and-in put struck at 100% of initial fixing with a knock-in barrier at 65% of initial fixing, observed on discrete dates. The desk is also short an autocall option, which functions as a strip of digital calls struck at 100% on each quarterly observation date --- if the underlying is at or above 100% on any observation, the note redeems early. The down-and-in put is cheaper than the vanilla European put in the base Reverse Convertible because the barrier reduces the probability of the put activating. The autocall option further reduces the effective note duration, which reduces the put's time value. The combined effect is a lower coupon than the base RC but with barrier protection and an early-exit mechanism. Pricing requires Monte Carlo simulation because the payoff depends on the path of the underlying across multiple observation dates (both for autocall determination and barrier observation).

#### Booking & systems

The book of record is NEMO, which carries the trade lifecycle, put strike, knock-in barrier level, autocall strike, observation schedule, autocall event status, barrier breach status, coupon schedule, settlement type, and fixing source. NEMO must track two independent status flags: the autocall status (not triggered / triggered on date) and the barrier breach status (not breached / breached on date). These flags interact: if the barrier is breached in one period and the autocall triggers in a subsequent period, the knock-in status must persist in NEMO's records even though the note has been redeemed, because the barrier breach affects the final settlement calculation if the autocall is later disputed or reversed. Risk and P&L run through Sophis, which prices the down-and-in put and autocall option jointly using a Monte Carlo model, computes Greeks, and generates daily mark-to-market. Sophis must simulate the combined autocall and barrier events in a single path-dependent framework. The legal document is the Termsheet, which defines the put strike, knock-in barrier, autocall strike, observation schedule, coupon accrual convention on autocall, barrier observation convention (discrete dates only or continuous), and fixing fallback rules. Murex is not used. The dominant operational risk is autocall event processing: when the underlying breaches the autocall strike on an observation date, NEMO must terminate the note lifecycle, stop coupon accrual (or pay the accrued portion), and trigger the par settlement. If NEMO does not process the autocall, the note appears live, the hedge remains open in Sophis, and coupon continues to accrue.

#### Pricing intuition

The dominant Greeks are short Delta, short Vega, and negative Gamma, with complex interactions between the autocall and put components. The FCN's coupon is funded by three premium sources: the down-and-in put premium (investor sells barrier-protected downside), the autocall option premium (investor gives up the right to hold the note to maturity if the underlying rallies), and the issuer's funding advantage.

The key pricing distinction from the Phoenix is simplicity: the fixed coupon removes the conditional-coupon digital from the structure, eliminating one layer of path dependency. The FCN is priced as a barrier put plus an autocall, while the Phoenix is priced as a barrier put plus an autocall plus a strip of conditional coupons (digital options). The FCN's coupon is typically lower than the Phoenix's headline coupon because the fixed coupon is guaranteed, while the Phoenix's conditional coupon carries a probability of non-payment.

Autocall probability is the dominant factor in effective duration. Higher volatility increases both the probability of the autocall triggering (underlying rallies above 100%) and the probability of the barrier breaching (underlying falls below 65%). More observation dates increase the autocall probability, shortening the expected note life. A 1-vol-point shift moves the combined put-plus-autocall value by approximately 15--25 bps.

#### Worked example (USD 10M)

**Trade parameters.** Notional: USD 10M. Tenor: 1 year. Underlying: single stock, 25% implied volatility at inception. Put strike: 100% of initial fixing. Knock-in barrier: 65% of initial fixing. Autocall strike: 100% of initial fixing. Observation: quarterly (4 dates). Settlement: physical delivery. Fixed coupon: 8.0% per annum (paid quarterly, 2.0% per quarter).

**Economic decomposition.** The 8.0% headline coupon reconciles as follows. The down-and-in put (100% strike, 65% barrier, 25-vol, 1-year, quarterly observation) prices at 3.8% of notional (USD 380K). The autocall option (quarterly observations at 100%) prices at 1.2% of notional (USD 120K). Issuer funding at the credit curve contributes 2.0% per annum (USD 200K). Funds transfer pricing absorbs 0.8% per annum (USD 80K). The residual desk margin is 0.2% per annum (USD 20K). Arithmetic check: down-and-in put 3.8% plus autocall option 1.2% plus issuer funding 2.0% plus FTP 0.8% plus desk margin 0.2% equals 8.0% headline coupon.

**Autocalled scenario.** The underlying closes at 105% at the Q2 observation. The autocall triggers. The investor receives par (USD 10M) plus two quarters of coupon (USD 400K). Total return: USD 10.4M in 6 months, or 8.0% annualized on par. The investor must now reinvest at prevailing market rates.

**Good scenario --- maturity, above barrier.** The underlying closes at 75% at maturity. The underlying is above the 65% knock-in barrier. The put does not activate. The investor receives par (USD 10M) plus the full annual coupon (USD 800K). Total return: USD 10.8M, or 8.0% on par, despite a 25% decline in the underlying.

**Bad scenario --- maturity, below barrier.** The underlying closes at 50% at maturity. The underlying is below the 65% knock-in barrier. The put activates. The investor receives physical delivery of shares worth 50% of notional (USD 5M) plus the full annual coupon (USD 800K). Net proceeds: USD 5.8M. Principal loss: USD 4.2M, or 42% of notional after accounting for the coupon.

#### Reconciliation specifics

**Autocall event** --- when the underlying breaches the autocall strike on an observation date, NEMO must process the lifecycle termination: update note status, stop coupon accrual, trigger par settlement --- if the autocall is not processed, the note continues live, coupon continues accruing, and the hedge in Sophis remains open past the redemption date.

**Barrier breach persistence** --- if the knock-in barrier is breached on one observation date and the autocall triggers on a subsequent date, NEMO must retain the barrier-breach flag --- this matters for audit trail and for scenarios where the autocall settlement is disputed, because the knock-in status would govern the alternative maturity outcome.

**Barrier observation convention** --- the Termsheet may specify discrete observation (barrier tested only on scheduled dates) or continuous observation (barrier tested every trading day) --- if NEMO is configured for continuous monitoring but the Termsheet specifies discrete, a mid-period barrier breach that recovers before the next observation date would incorrectly trigger the knock-in.

**Coupon on autocall** --- the Termsheet must specify whether the investor receives a full-period coupon or a pro-rata coupon on the autocall date --- on a USD 10M note with 8.0% annual coupon, the per-quarter difference between full period (USD 200K) and pro-rata (variable) can be significant.

**Fixing source consistency** --- both the autocall determination and the barrier determination use the underlying's closing price --- the Termsheet must specify a single fixing source for both, or NEMO may apply different sources to autocall and barrier checks, producing inconsistent results on the same observation date.

#### Desk view

The FCN is the workhorse of Asian structured note markets. Its commercial appeal is the combination of fixed coupon certainty, barrier protection, and an autocall exit. The investor knows the coupon amount on every payment date regardless of where the underlying trades --- there is no conditionality to explain, no memory feature to track, no coupon barrier to monitor. This simplicity makes it easier to sell and easier for the investor to understand than the Phoenix Autocallable.

The trade-off is yield. The FCN's fixed coupon is typically lower than the Phoenix's conditional coupon for the same underlying, tenor, and barrier levels, because the fixed coupon is guaranteed while the Phoenix coupon is at risk. An investor who believes the underlying will stay above the coupon barrier is better served by the Phoenix (higher expected coupon). An investor who values certainty of cash flows is better served by the FCN.

The product is appropriate when the investor has a neutral to mildly bullish view, wants fixed income with no conditionality, is comfortable with barrier risk, and values the autocall exit on rally. It is not appropriate when the investor seeks the highest possible yield (the Phoenix offers more), when the investor does not understand what happens below the barrier, or when the underlying has low volatility (compressing both the coupon and the barrier distance). Product Control should verify that NEMO tracks both the autocall status and the barrier breach status independently, and that the coupon accrual convention on autocall matches the Termsheet.

#### Desk shorthand

*Fixed coupon; barrier put, autocall exit.*

---

### Callable Range Accrual ELN

#### Definition

The Callable Range Accrual ELN is a structured note, issued as an equity-linked note (ELN) under an ISDA or MTN wrapper, that pays a variable coupon determined by the number of business days the underlying closes within a predefined range, and is callable by the issuer on scheduled dates. The coupon accrual formula is: coupon equals the maximum coupon rate multiplied by the ratio of in-range business days to total business days in the accrual period. The range is defined by a lower barrier (typically 80% of initial fixing) and an upper barrier (typically 120% of initial fixing). On each business day, the underlying's closing price is observed: if the close is within the range, that day accrues toward the coupon; if outside, it does not. The coupon is paid at the end of each accrual period. The issuer has the right to call the note at par plus accrued coupon on scheduled dates. At maturity, if the note has not been called, the investor receives par plus the final period's accrued coupon. This product is fundamentally different from all other ELN products in this section: there is no embedded put, no principal risk, and no equity downside exposure. The investor's risk is coupon variability --- in the worst case, the underlying trades outside the range every business day and the investor earns zero coupon, but still receives par at maturity. Capital protection is full.

#### Construction

The note decomposes into three primitive instruments. The desk is long a zero-coupon bond funded at the issuer's credit curve, providing full principal protection and par redemption at maturity. The desk is long a range accrual coupon, which is economically equivalent to a strip of daily in-range digital options: on each business day, the desk pays a fraction of the maximum coupon if and only if the underlying closes within the range. Each daily observation is a binary event (in-range or out-of-range), and the coupon for each period is the sum of these daily fractions. The desk is short a Bermudan call on the note, exercisable on scheduled dates, giving the issuer the right to redeem at par. The call compensates the desk: the call premium funds part of the maximum coupon rate. The daily digital strip is the pricing challenge. Unlike a single European option with a terminal payoff, the range accrual depends on the underlying's closing price on every business day over the note's life. This is the highest degree of path dependency among ELN products. Pricing requires Monte Carlo simulation with daily time steps, and the model must capture realistic barrier-crossing frequency, making local volatility models preferable to flat Black-Scholes.

#### Booking & systems

The book of record is NEMO, which carries the trade lifecycle, lower and upper range barriers, daily accrual count (in-range days and total business days), maximum coupon rate, coupon payment schedule, call schedule, call exercise status, barrier observation convention, business day calendar, and fixing source. NEMO must update the accrual count daily: on each business day, after the closing price is published, the system must determine whether the close falls within the range and increment the in-range counter accordingly. This daily update is the most operationally intensive process among all ELN products. Risk and P&L run through Sophis, which prices the daily digital strip and the Bermudan call via Monte Carlo with daily time steps, computes Vega (the dominant Greek), Delta, and Gamma, and generates daily mark-to-market. Sophis must use the same closing prices as NEMO for its daily accrual simulation. The legal document is the Termsheet, which defines the range barriers, maximum coupon rate, accrual formula, business day calendar, boundary treatment (whether the underlying closing exactly at the barrier is counted as in-range or out-of-range), coupon payment frequency, call schedule, and fixing source. Murex is not used. The dominant operational risk is daily accrual count divergence: if NEMO and Sophis use different closing-price sources, different boundary-treatment conventions, or different business day calendars, the accrual counts will diverge, and the coupon payment will not reconcile with the pricing model's expected value.

#### Pricing intuition

The dominant Greek is Vega. The range accrual's value is determined by the expected number of days the underlying stays within the range, which is a direct function of realized volatility. The relationship between volatility and coupon value is inverse: higher volatility means the underlying is more likely to move outside the range on any given day, reducing the expected accrual count and lowering the expected coupon. This means the desk pays less coupon when volatility is high, which makes the range accrual strip cheaper in high-vol environments. Conversely, in low-vol environments, the underlying stays in range more often, the expected coupon is higher, and the strip is more expensive.

The maximum coupon rate is driven by four factors. First, implied volatility: higher vol reduces the strip cost, allowing a higher maximum coupon rate (the investor receives a higher promised rate but expects to earn less of it). Second, range width: a wider range (70%--130% vs 80%--120%) increases the expected in-range days, increasing the strip cost and reducing the maximum rate. Third, the Bermudan call premium: the issuer's call right adds to the maximum coupon rate. Fourth, the note's tenor: longer tenor means more daily observations, and the law of large numbers smooths the accrual count toward the expected value, reducing the variance of the realized coupon.

Near the range boundaries, Delta spikes and Gamma is deeply negative. If the underlying is trading at 81% (just above the lower barrier), a small decline to 79% flips the daily accrual from in-range to out-of-range. The digital nature of each daily observation creates hedging challenges at the boundaries that persist every day the underlying is near a barrier.

#### Worked example (USD 10M)

**Trade parameters.** Notional: USD 10M. Tenor: 2 years. Underlying: equity index, 18% implied volatility at inception. Lower range barrier: 80% of initial fixing. Upper range barrier: 120% of initial fixing. Maximum coupon: 7.0% per annum (paid semi-annually, 3.5% per half-year maximum). Call dates: semi-annual (6M, 12M, 18M). Business days per year: 252.

**Economic decomposition.** The 7.0% maximum annual coupon reconciles as follows. The range accrual digital strip (80%--120% range, 18-vol, 2-year, daily observation) prices at 3.5% per annum of notional (USD 350K per year). The Bermudan call (3 semi-annual exercise dates) prices at 0.8% per annum (USD 80K per year). Issuer funding at the credit curve contributes 1.5% per annum (USD 150K per year). Funds transfer pricing absorbs 0.7% per annum (USD 70K per year). The residual desk margin is 0.5% per annum (USD 50K per year). Arithmetic check: range accrual strip 3.5% plus call premium 0.8% plus issuer funding 1.5% plus FTP 0.7% plus desk margin 0.5% equals 7.0% maximum coupon.

**Good scenario --- full accrual.** The underlying stays within the 80%--120% range on every business day for 2 years. The investor receives the full 7.0% coupon each year (USD 700K per year). Over 2 years: USD 10M par plus USD 1.4M total coupon. Total return: USD 11.4M, or 7.0% per annum.

**Moderate scenario --- partial accrual.** The underlying stays within the range on 60% of business days (approximately 151 of 252 days per year). The effective coupon is 7.0% multiplied by 60%, which equals 4.2% per annum (USD 420K per year). Over 2 years: USD 10M par plus USD 840K total coupon. Total return: USD 10.84M, or 4.2% per annum. The investor still receives full par --- the reduced coupon is the only cost.

**Bad scenario --- low accrual.** The underlying stays within the range on only 30% of business days. The effective coupon is 7.0% multiplied by 30%, which equals 2.1% per annum (USD 210K per year). Over 2 years: USD 10M par plus USD 420K total coupon. Total return: USD 10.42M, or 2.1% per annum. In the extreme case of zero in-range days, the investor earns zero coupon but still receives par.

#### Reconciliation specifics

**Daily accrual count** --- NEMO and Sophis must produce the same in-range day count for each accrual period --- if NEMO uses the exchange official close and Sophis uses a Bloomberg composite, the closing prices may differ by a few basis points on any given day, and on days when the underlying closes near a range boundary, one system may count the day as in-range while the other counts it as out-of-range. Over a 2-year note with 504 business days, even a small systematic difference in boundary treatment can produce a material accrual divergence.

**Boundary treatment** --- the Termsheet must specify whether the underlying closing exactly at the barrier level (80.00% or 120.00%) is counted as in-range or out-of-range --- if the Termsheet is silent and NEMO uses inclusive (at-barrier is in-range) while Sophis uses exclusive (at-barrier is out-of-range), the accrual count will differ on every boundary-touch day. At 18% vol with daily observation, the underlying is expected to touch the range boundary approximately 15--25 times over 2 years, making this a material source of divergence.

**Business day calendar** --- NEMO uses a settlement calendar for the note's jurisdiction, Sophis uses an exchange calendar for the underlying --- if the two calendars have different holidays, the denominator (total business days) will differ, and the accrual ratio will not reconcile even if the in-range count agrees.

**Call event processing** --- identical risk to the Callable Reverse Convertible: if the issuer exercises the call and NEMO does not process the event, the note continues live, daily accrual continues, and the hedge remains open in Sophis past the redemption date.

**Coupon on call** --- the Termsheet must specify whether the coupon for the call period is paid based on actual accrual to the call date or based on a minimum/guaranteed amount --- if NEMO pays the actual accrual but the Termsheet specifies a minimum coupon on call, the payment will not match.

#### Desk view

The Callable Range Accrual ELN is the most conservative ELN product in this section and simultaneously the most operationally intensive. There is no principal risk: the investor receives par at maturity regardless of where the underlying trades. The only risk is coupon variability --- in the worst case, the investor earns nothing above par. This makes it suitable for investors who cannot accept any principal loss but want equity-linked returns above the risk-free rate.

The daily observation requirement makes this product expensive to operate. Every business day, the closing price must be captured, the in-range determination must be made, and the accrual counter must be updated in NEMO. No other ELN product requires daily operational attention. The issuer's call right is the desk's safety valve: if realized volatility turns out lower than implied (meaning the underlying stays in range more than expected), the desk is paying more coupon than priced, and the call allows the issuer to terminate the position.

The product is appropriate when the investor has a range-bound market view, wants full principal protection, and accepts variable coupon as the trade-off. It is best suited to low-volatility environments where the underlying is expected to stay within the range most of the time. It is not appropriate when the investor expects a trending market (the underlying will leave the range, reducing the coupon to near zero), when the investor requires fixed income certainty (the coupon is inherently variable), or when the operations team is not equipped for the daily monitoring burden. Product Control should establish an automated daily reconciliation process for the accrual count from Day 1 of the trade, and should verify the boundary-treatment convention before the first observation.

#### Desk shorthand

*Range coupon; daily digital strip, callable.*

---

### Section 3.3 — Other ELN Structures

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

---

### Principal Protected Note

#### Definition

A Principal Protected Note (PPN) guarantees the full return of invested principal at maturity while providing participation in the upside performance of an equity underlying. The investor receives no coupon; the return is entirely capital gain linked to the equity performance, scaled by a participation rate.

The economic logic is the mirror image of a Reverse Convertible. In an RC, the investor sells a put option and receives the premium as enhanced coupon. In a PPN, the investor buys a call option, funded by the interest income foregone on the zero-coupon bond. The investor trades certain income for uncertain equity upside, with the guarantee that principal is returned in full regardless of market outcome.

PPNs are the simplest capital-protected structure in the ELN family. The participation rate — typically below 100% — is the key metric that determines investor value. It is driven by interest rates, volatility, tenor, and dividends.

#### Construction

A PPN decomposes into two components:

**Component 1 — Zero-coupon bond (long).** The desk purchases a zero-coupon bond that matures at par. The present value of this bond is less than par; the difference (the discount) represents the budget available to purchase the equity option. At 3% funding over 3 years, the discount is approximately 8.7% of notional.

**Component 2 — European call option (long).** The desk uses the bond discount to buy an ATM European call on the equity underlying. A 3-year ATM call at 22-vol costs approximately 12.0% of notional. Since the available budget (8.7%) is less than the full call cost (12.0%), the desk purchases a fractional call — the participation rate.

**Participation rate determination:**

The participation rate equals the available discount divided by the full call cost:

- Available discount: 8.7%
- Full call cost: 12.0%
- Participation rate: 8.7% / 12.0% = 72.5%

The participation rate is always below 100% for ATM calls because the bond discount alone cannot fully fund the option. FTP and desk margin are deducted from the available budget before purchasing the call, further reducing participation.

There are no barrier features, no path dependency, and no autocall mechanism. This is a European structure priced in closed form.

#### Booking & systems

PPNs are booked in the standard ELN system architecture.

**NEMO (book of record)** carries the structured note as a single instrument. Critical fields: participation rate, protection level (100%), underlying reference, strike level, maturity date, and cap (if applicable). The protection flag must be explicitly set in NEMO — failure to flag protection means the system treats the note as at-risk principal.

**Sophis (risk and P&L)** carries the decomposed components: the zero-coupon bond and the call option. Sophis computes delta, vega, and rho exposures. The call is modelled using Black-Scholes with appropriate skew adjustments.

**Termsheet (legal document)** defines the participation rate, protection level, any upside cap, settlement terms, and the calculation agent provisions. The termsheet is the authoritative source for all economic terms.

Murex is not used for any ELN product.

#### Pricing intuition

The PPN's pricing is driven by the interaction between interest rates and volatility — a trade-off that is unique among ELN structures.

**Rates and participation.** Higher interest rates increase the zero-coupon discount (more budget available) and therefore increase the participation rate. A 25 bps rate increase translates to approximately 70 bps higher participation. This makes PPNs more attractive in higher-rate environments.

**Volatility and participation.** Higher volatility increases the call option cost, reducing the participation rate. A 1-vol-point increase reduces participation by approximately 60 bps. The investor is a net buyer of volatility.

**Tenor and participation.** Longer tenors increase the zero-coupon discount (more compounding) faster than they increase the call cost, generally improving participation rates. This is why PPNs are typically issued at 3-5 year tenors.

**Greeks:**
- Delta: Long, scaled by participation rate. Net positive equity exposure.
- Vega: Long. The desk is long volatility through the embedded call.
- Rho: Short. The zero-coupon bond has meaningful duration, and rising rates benefit the investor but hurt the existing bond position.
- Gamma: Long. Positive convexity from the call option.

Unlike RC products where the desk is short volatility through the embedded put, PPN desks are long volatility. This is the fundamental structural difference.

#### Worked example (USD 10M)

**Terms:** USD 10M notional, 3-year maturity, equity index underlying (22-vol), 100% protection, ATM strike.

**Decomposition — funding the call:**

| Component | Value |
|---|---|
| Zero-coupon bond PV (3% × 3yr) | 91.3% of par |
| Available discount | 8.7% |
| Full ATM call cost (3yr, 22-vol) | 12.0% |
| Less: FTP | (0.5%) |
| Less: desk margin | (0.2%) |
| Net budget for call | 8.0% |
| Participation rate | 8.0% / 12.0% = 66.7% |

Note: The simplified illustration uses 8.7% / 12.0% = 72.5% gross participation. After FTP (0.5%) and desk margin (0.2%), net participation is 66.7%.

**Scenario 1 — equity rallies to 130%:**
- Equity return: +30%
- Investor return: 72.5% × 30% = 21.75% (gross); 66.7% × 30% = 20.0% (net)
- Payout: USD 10M + USD 2.0M = USD 12.0M

**Scenario 2 — equity flat at 100%:**
- Call expires worthless
- Investor return: 0% (par returned in full)
- Payout: USD 10M

**Scenario 3 — equity falls to 70%:**
- Call expires worthless
- Full principal protection activates
- Investor return: 0% (par returned in full)
- Payout: USD 10M

The worst-case outcome is 0% return — the investor never loses principal. The opportunity cost is the 3 years of foregone interest income (approximately 9% cumulative at 3% per annum).

#### Reconciliation specifics

**Protection level (most critical).** The protection flag in NEMO must be explicitly set to 100%. If omitted, the system treats the note as unprotected, which misrepresents the risk profile and can trigger incorrect margin calls. This is the single most important recon check for PPNs.

**Participation rate.** The participation rate in NEMO must match the Sophis call notional divided by the note notional. A mismatch means the hedge ratio is wrong. Common failure mode: NEMO carries the gross participation rate while Sophis is set up with the net rate (or vice versa).

**Cap (if applicable).** Some PPNs include an upside cap to increase the participation rate. If the termsheet specifies a cap, it must appear in both NEMO (payout formula) and Sophis (capped call or call spread). Omitting the cap in either system creates P&L leakage on extreme upside moves.

**Settlement.** European observation at maturity only. No daily fixing required. Settlement follows modified following convention if the observation date falls on a non-business day.

#### Desk view

**Who buys this product.** Conservative institutional investors and retail-facing distributors who need capital protection mandates. Insurance companies, pension funds with minimum-return guarantees, and private banks offering "no-loss" products to wealth management clients.

**The real risk.** The investor's only risk is issuer credit risk — if the issuer defaults, the principal guarantee is void. There is no market risk to principal. The "risk" is the opportunity cost: the investor earns 0% in flat or down markets, while a simple bond would have earned approximately 3% per annum.

**When appropriate.** Low-risk mandates. Clients who cannot tolerate any principal loss. Environments where rates are high (good participation) and vol is low (cheap calls). Long investment horizons.

**When not appropriate.** Income-seeking investors (no coupon). Short tenors (insufficient discount to fund meaningful participation). Low-rate environments (participation rate drops below attractive levels, typically below 60%). Clients who want full upside participation (always below 100% for ATM PPNs).

#### Desk shorthand

*Protected par; long call, no coupon, no downside.*

---

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

---

### Issuer Callable Note

#### Definition

An Issuer Callable Note (ICN) pays an above-market fixed coupon in exchange for granting the issuer the right to redeem the note early at par. The investor receives an enhanced yield that exceeds comparable non-callable bonds; the premium comes from the embedded call option that the investor implicitly sells to the issuer.

The economic logic is analogous to a callable bond but packaged as a structured note. When interest rates fall, the issuer is likely to call the note (redeeming at par) because it can refinance at lower rates. The investor then faces reinvestment risk — forced to reinvest in a lower-rate environment. Conversely, when rates rise, the issuer does not call, and the investor holds a fixed-rate instrument in a rising-rate environment (duration extension).

Within the ELN family, the ICN is distinctive because it is primarily an interest rate product rather than an equity product. The embedded optionality is a Bermudan call on interest rates, not an equity option. The equity-linked element, if present, is typically in the coupon structure (equity-linked coupon rather than equity-linked principal).

#### Construction

An ICN decomposes into two components:

**Component 1 — Fixed-coupon bond (long).** The investor holds a fixed-rate bond paying 5.5% per annum. At maturity (if not called), par is returned in full. There is 100% principal protection — no equity barrier, no knock-in, no contingent redemption.

**Component 2 — Bermudan call option (short to investor).** The investor sells the issuer a Bermudan-style call option exercisable on discrete call dates (typically quarterly after an initial non-call period of 1 year). If the issuer exercises, the note is redeemed at par plus accrued coupon.

**Coupon enhancement breakdown:**

| Component | Value |
|---|---|
| Fixed coupon | 5.5% |
| Benchmark rate | 3.0% |
| Coupon enhancement | 2.5% |
| Funded by: | |
| — Call option premium | 1.8% |
| — Funding benefit | 0.4% |
| — FTP | 0.2% |
| — Desk margin | 0.1% |
| Total enhancement | 2.5% |

The investor earns 250 bps above the benchmark rate. The call option premium (1.8%) is the dominant source of this enhancement.

#### Booking & systems

ICNs are booked in the standard ELN system architecture.

**NEMO (book of record)** carries the note with its full call schedule. Critical fields: coupon rate, payment frequency, first call date, subsequent call dates, call price (typically par), maturity date, and notification period. The complete call schedule must be entered — an incomplete schedule can cause the system to miss a call date.

**Sophis (risk and P&L)** carries the decomposed components: the fixed-rate bond and the Bermudan call option. Sophis models the call using a short-rate model (Hull-White or similar) calibrated to the interest rate curve and swaption volatilities. The model computes the optimal exercise boundary — the set of rate levels at which the issuer should call.

**Termsheet (legal document)** defines the coupon, the call schedule, the notification period, and any conditions on the call (clean price vs dirty price, minimum notice days). The notification period is operationally critical — the issuer must notify holders within the specified window, and the operations team must be prepared to process the redemption.

Murex is not used for any ELN product.

#### Pricing intuition

ICN pricing is driven by interest rate dynamics, not equity factors.

**Interest rates and call probability.** When rates fall, the issuer's incentive to call increases (it can refinance cheaper). A 50 bps drop in rates materially increases call probability — the note's effective duration shortens. When rates rise, the note is unlikely to be called — effective duration extends toward maturity.

**Rate volatility and call value.** Higher rate volatility increases the value of the Bermudan call option, which means the issuer can offer a higher coupon. This is why ICNs are more attractive in volatile rate environments — the call premium is richer.

**Duration and convexity.** The ICN exhibits negative convexity (like all callable bonds). In a rally, duration shortens (limiting price appreciation). In a sell-off, duration extends (amplifying price decline). The investor is on the wrong side of convexity in exchange for the enhanced coupon.

**Effective duration.** The relevant duration measure is "duration to worst" (to the next call date if in-the-money, to maturity otherwise). At issuance, effective duration is typically between the first call date and maturity — the market prices a probability-weighted blend.

**Greeks:**
- Rho: Dominant risk. Negative — rising rates reduce the bond value.
- Vega (rate vol): Short. The investor is short rate volatility through the embedded call.
- Duration: Variable — between first call and maturity, depending on rate level.
- Convexity: Negative. The defining feature of callable instruments.

#### Worked example (USD 10M)

**Terms:** USD 10M notional, 3-year maturity, quarterly coupon (5.5% p.a.), callable quarterly after year 1 at par, benchmark rate 3.0%.

**Decomposition — funding the enhancement:**

| Component | Annualised |
|---|---|
| Fixed coupon to investor | 5.5% |
| Less: benchmark rate | (3.0%) |
| Coupon enhancement | 2.5% |
| | |
| Call option premium (Bermudan) | 1.8% |
| Funding benefit | 0.4% |
| FTP | 0.2% |
| Desk margin | 0.1% |
| Total funding sources | 2.5% |

**Verification:** 1.8% + 0.4% + 0.2% + 0.1% = 2.5%. Matches coupon enhancement.

**Scenario 1 — rates fall 100 bps after 1 year:**
- Issuer calls at par at the first call date
- Investor receives: 1 year × 5.5% = USD 550,000 coupon + USD 10M par
- Outcome: Good yield but only for 1 year. Reinvestment at lower rates.
- Effective yield earned: 5.5% for 1 year

**Scenario 2 — rates unchanged:**
- Issuer may or may not call (depends on precise rate level vs call boundary)
- If held to maturity: 3 years × 5.5% = USD 1,650,000 total coupon + USD 10M par
- Effective yield earned: 5.5% for 3 years

**Scenario 3 — rates rise 100 bps:**
- Issuer does not call
- Note held to maturity at 5.5% — below new market rates
- Mark-to-market loss on the position (duration × rate change)
- Investor locked into below-market coupon with extended duration
- No principal loss at maturity, but opportunity cost is significant

#### Reconciliation specifics

**Call schedule (most critical).** Every call date from the termsheet must appear in both NEMO and Sophis. A missing call date means the system cannot process a redemption on that date, causing settlement failures and P&L discrepancies. For ICNs with many call dates (e.g., quarterly over 3 years = 8 call dates after the non-call period), manual entry errors are common.

**First call date and non-call period.** The non-call period (typically 1 year) protects the investor from immediate call. If the first call date is entered incorrectly in NEMO, the issuer might attempt to call during the non-call period, or the system might fail to process a valid call.

**Notification period.** The termsheet specifies the minimum notice period (e.g., 5 business days before the call date). This is an operational parameter — NEMO should enforce it, and the operations team must have a process to monitor incoming call notices within this window.

**Accrued coupon on call.** When the issuer calls, the investor receives par plus accrued coupon to the call date. The accrual calculation (day count convention, accrual start date) must match between NEMO and Sophis. A mismatch creates a P&L break on every call event.

#### Desk view

**Who buys this product.** Income-focused investors willing to accept reinvestment risk for enhanced yield. Insurance companies and pension funds with liability-driven mandates that benefit from higher coupons. Private banking clients seeking stable income above deposit rates.

**The real risk.** Reinvestment risk on call — the investor earns the enhanced coupon only until the issuer calls, then must reinvest at potentially lower rates. Duration extension if rates rise — the note behaves like a long-dated bond in exactly the environment where you don't want long-dated exposure. Negative convexity means the price path is asymmetrically bad.

**When appropriate.** Stable or moderately rising rate environments where call probability is low (investor keeps the enhanced coupon for longer). Investors with a natural call date preference (ALM matching). Environments where rate vol is high (richer call premium).

**When not appropriate.** Falling rate environments (high call probability, short holding period). Investors who cannot accept reinvestment risk. Portfolios requiring positive convexity. Environments where the coupon enhancement does not adequately compensate for the embedded short call.

#### Desk shorthand

*Enhanced coupon; callable by issuer, reinvestment risk.*

---

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

---

## Part 4 — Structured Rate Trades

### IR Callable Fixed Rate Note

#### Definition

The IR Callable Fixed Rate Note is a structured rate product, issued under an ISDA or MTN wrapper, that pays a fixed coupon above the prevailing swap rate in exchange for the investor granting the issuer the right to redeem the note early on a schedule of discrete call dates. The note has a long-dated maturity (typically 10--30 years) with a non-call period (typically 1--3 years) during which the issuer cannot exercise the call. After the non-call period, the issuer may redeem the note at par on any scheduled call date. If the issuer does not call, the investor continues to receive the above-market fixed coupon until final maturity, at which point par is returned. The enhanced coupon compensates the investor for selling a Bermuda-style receiver swaption to the issuer: the issuer will call the note when interest rates have fallen sufficiently that refinancing at a lower coupon is economically attractive, forcing the investor to reinvest in a lower-rate environment. Capital protection is full --- the investor receives par either at maturity or on any call date. The risk is not principal loss but reinvestment loss.

#### Construction

The note decomposes into two components. The investor holds a vanilla fixed-rate bond paying the above-market coupon, funded at the issuer's credit curve, with par redemption at maturity. Embedded within this bond, the investor has sold a Bermuda receiver swaption to the issuer. The swaption gives the issuer the right, on each call date, to enter into a receiver swap (receiving fixed, paying floating) at the note's coupon rate for the remaining life of the note --- exercising the swaption is economically equivalent to calling the note at par and refinancing at the lower prevailing rate. The swaption premium, amortized over the note's expected life, funds the coupon enhancement above the vanilla swap rate. More call dates increase the value of the embedded swaption (more exercise opportunities), which increases the coupon the desk can offer. A longer non-call period reduces the swaption value (fewer exercise opportunities in the near term), which reduces the coupon. Pricing requires a Bermuda swaption model --- the multi-exercise structure cannot be valued as a strip of European swaptions because early exercise on one date extinguishes all subsequent exercise rights.

#### Booking & systems

The book of record is Murex, which carries all four legs of the structured rate trade. The note leg records the client-facing structured note: notional, currency, fixed coupon rate, coupon frequency, maturity date, and the Bermuda call schedule with all exercise dates and notification periods. The issuer leg records the internal funding cost: funding rate, funding curve, and issuer credit spread. The deposit leg records the collateral placed by the client, if any, with the deposit rate and rollover convention. The hedge leg records the market risk hedges: a portfolio of swaptions, swaps, or other derivatives that offset the desk's exposure to the embedded Bermuda swaption. NEMO and Sophis are not used. Funds transfer pricing is booked within Murex between the desk and treasury at the FTP rate, using the FTP curve. Discounting follows OIS conventions for collateralized trades (CSA-covered) or the issuer's own curve for uncollateralized notes --- using the wrong discount curve produces a systematic MTM bias across the note's entire life.

#### Pricing intuition

The dominant risk measures are DV01 and vega. DV01 measures the note's sensitivity to a 1 basis point parallel shift in the swap curve: a rate increase reduces the note's market value (the fixed coupon becomes less attractive relative to market rates), while a rate decrease increases the value but also increases the probability that the issuer will call. Vega measures the sensitivity to swaption implied volatility: higher volatility increases the value of the embedded Bermuda swaption, which increases the coupon the desk can offer but also increases the hedging cost.

The headline coupon is driven by four primary levers. The current swap rate level sets the baseline: a higher 10-year swap rate produces a higher fixed coupon. The Bermuda swaption premium adds the enhancement: more call dates, shorter non-call period, and higher swaption volatility all increase the swaption value and therefore the coupon. The issuer's funding spread contributes additional basis points. FTP and desk margin absorb the remainder.

The investor's primary risk is reinvestment risk, not principal risk. The issuer will call when rates have fallen, forcing the investor to reinvest at lower rates. The note has negative convexity: in a falling-rate environment, the note's price appreciation is capped by the par call price, while in a rising-rate environment, the note's price depreciates without a floor. This asymmetric payoff is the cost of the enhanced coupon. The investor is implicitly short rate volatility through the sold swaption.

A critical model consideration is the choice between normal (Bachelier) and lognormal (Black) volatility conventions for the swaption. The two models produce different vega exposures and different hedge ratios. The desk must ensure that the pricing model, the risk model, and the hedge strategy all use the same volatility convention, or the vega hedge will not converge and P&L will exhibit unexplained volatility.

#### Worked example (USD 10M)

**Trade parameters.** Notional: USD 10M. Tenor: 10 years, callable annually after year 2 (8 Bermuda call dates). Fixed coupon: 5.5% per annum, paid semi-annually. Non-call period: 2 years. Underlying rate: 10-year USD swap rate. Swaption volatility: 65 bps normal.

**Economic decomposition.** The 5.5% headline coupon reconciles as follows. The vanilla 10-year swap rate is 4.2% per annum (USD 420K per annum on USD 10M). The Bermuda receiver swaption (8 exercise dates, years 3--10, strike at 5.5%) prices at 0.8% per annum amortized over expected life (USD 80K per annum). Issuer funding spread contributes 0.3% per annum (USD 30K). Funds transfer pricing absorbs 0.15% per annum (USD 15K). Desk margin is 0.05% per annum (USD 5K). Arithmetic check: swap rate 4.2% plus swaption premium 0.8% plus issuer funding 0.3% plus FTP 0.15% plus desk margin 0.05% equals 5.5% headline coupon.

**Good scenario (rates rise).** The 10-year swap rate rises to 5.5% by year 3. The issuer does not call --- the note's 5.5% coupon is at-market, so refinancing offers no saving. The investor holds the note to maturity, receiving 20 semi-annual coupons of USD 275K (total USD 5.5M) plus par (USD 10M). Total proceeds: USD 15.5M. Annualized return: 5.5%. The investor benefits from the above-market coupon in a rising-rate environment.

**Bad scenario (rates fall).** The 10-year swap rate falls to 3.0% by year 3. The issuer calls the note at par on the first available call date (year 3 anniversary). The investor receives par (USD 10M) plus 6 semi-annual coupons already paid (USD 1.65M). Total proceeds: USD 11.65M. The investor earned 5.5% for 3 years but must now reinvest at 3.0%. Reinvestment loss: 2.5% per annum for the remaining 7 years, or approximately USD 1.75M in foregone coupon income. The investor's realized return over the 3-year holding period is 5.5% --- but the opportunity cost of early redemption is material.

#### Reconciliation specifics

**Call schedule** --- Murex must carry every Bermuda exercise date with the exact notification period --- if a call date is omitted, the Bermuda swaption is undervalued in the hedge leg, and the desk's vega exposure is unhedged on that date.

**Call notification period** --- the Termsheet specifies the number of business days' notice the issuer must give before exercising the call (typically 5--30 business days) --- if Murex does not enforce the notification period, the issuer may exercise on insufficient notice, creating a settlement break.

**Clean vs dirty call price** --- the Termsheet must specify whether the call is at par (clean) or at par plus accrued coupon (dirty) --- a mid-coupon-period call produces an accrued coupon payment that differs by the accrued amount depending on the convention, and Murex must be configured accordingly.

**Swaption model convention** --- the pricing leg and the hedge leg must use the same volatility convention (normal or lognormal) --- if the pricing uses normal vol (65 bps) and the hedge uses lognormal vol, the vega sensitivities will diverge, producing P&L attribution noise and a hedge that does not converge.

**Discount curve** --- Murex must apply OIS discounting for CSA-covered trades or the issuer curve for uncollateralized notes --- using the wrong curve produces a systematic MTM bias: OIS curves are typically lower than issuer curves, so applying OIS discounting to an uncollateralized note overstates the MTM.

**Day count convention** --- the Termsheet specifies the day count for coupon accrual (30/360, actual/360, actual/actual) --- Murex must match this exactly, or every coupon payment will differ by a small amount that compounds over a 10-year life.

#### Desk view

The IR Callable Fixed Rate Note is the foundational structured rate product, comparable in its role to the Reverse Convertible in the ELN family. The risk is transparent: the investor sells call optionality to the issuer and receives an enhanced fixed coupon as compensation. The product appeals to investors who believe rates will remain stable or rise (minimizing the probability of call) and who value the certainty of a fixed coupon above the current swap rate.

The product is appropriate when the investor has a neutral-to-bearish view on rates (rates staying flat or rising), can accept the negative convexity of a callable structure, and understands that early redemption forces reinvestment at potentially lower rates. It is not appropriate when the investor expects rates to fall significantly (the note will be called, capping the holding period and forcing reinvestment), when the investor requires price appreciation potential (capped by the par call price), or when the investor does not understand the distinction between principal risk (zero) and reinvestment risk (material). Product Control should verify the call schedule is correctly booked in all four Murex legs at trade inception --- a missing call date is the single most common booking error for callable structures.

#### Desk shorthand

*Callable fixed; sold swaption for yield.*

---

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

---

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

---

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

---

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

---

## Part 5 — Swaps

### Vanilla Interest Rate Swap

#### Definition

The Vanilla Interest Rate Swap (IRS) is a bilateral derivative contract, executed under an ISDA Master Agreement, in which two parties exchange interest rate cash flows on a notional principal for a fixed term. One party pays a fixed rate; the other pays a floating rate (typically 3-month SOFR for USD-denominated swaps). The notional principal is not exchanged --- it serves only as the basis for calculating coupon payments. On each payment date, the fixed-leg payment and the floating-leg payment are netted, and only the net difference is transferred. A swap executed at the prevailing par swap rate has zero market value at inception: the present value of the fixed leg equals the present value of the expected floating leg. The IRS is the foundational interest rate derivative --- every structured rate product in this desk bible can be decomposed into a combination of vanilla swaps and embedded options.

#### Construction

The swap has two legs. The fixed leg pays a predetermined fixed rate (the swap rate) on the notional principal, typically semi-annually using 30/360 day count convention. The floating leg pays a variable rate determined by periodic fixings of the reference rate (3-month SOFR compounded in arrears for USD), typically quarterly using actual/360 day count convention. There is no exchange of principal, no optionality, and no path dependency. The swap is a pure exchange of cash flows, and its value at any point in time is the difference between the present value of the remaining fixed-leg payments and the present value of the remaining floating-leg payments, discounted at the OIS curve. Valuation is deterministic --- no simulation or option-pricing model is required. The fixed rate at which the swap has zero initial value is the par swap rate, which is determined by the shape of the OIS-discounted forward rate curve.

#### Booking & systems

The book of record is Murex, which carries both legs of the swap. The fixed leg is booked with the notional, fixed rate, payment frequency, day count convention, and payment dates. The floating leg is booked with the notional, reference rate index (SOFR), fixing tenor (3M), compounding convention (in arrears with lookback), reset dates, payment dates, and day count convention. The collateral leg tracks margin posted and received under the Credit Support Annex (CSA): margin frequency (typically daily), threshold (if any), minimum transfer amount, and eligible collateral types. The hedge leg records any offsetting positions in the desk's hedge book. NEMO and Sophis are not used. Discounting follows OIS conventions for CSA-covered swaps --- the discount curve must match the CSA terms, or the MTM will diverge from the counterparty's valuation, producing disputed margin calls. Funds transfer pricing is applied between the swap desk and treasury using the FTP curve.

#### Pricing intuition

The dominant risk measure is DV01 --- the change in swap MTM for a 1 basis point parallel shift in the swap curve. A USD 10M 5-year swap has a DV01 of approximately USD 4,500: a 1 bps rate increase causes a USD 4,500 gain for the fixed-rate payer (rates moving in the direction of the bet) and a USD 4,500 loss for the fixed-rate receiver. DV01 scales linearly with notional and approximately linearly with tenor.

The swap has no optionality, no model risk, and no path dependency. Pricing is deterministic: the par swap rate is the rate that equates the present values of the two legs under OIS discounting. The desk's revenue on a client swap is the bid-offer spread --- typically 0.5--2.0 bps for liquid maturities in USD, wider for less liquid currencies or longer tenors. This spread is embedded in the fixed rate shown to the client: if the mid-market 5-year swap rate is 4.20%, the desk quotes 4.25% to a client paying fixed (the desk receives the above-mid rate) or 4.15% to a client receiving fixed (the desk pays the below-mid rate).

Gamma (convexity) is relevant for risk management but not for pricing. A swap's DV01 itself changes as rates move: DV01 increases as rates fall (longer effective duration) and decreases as rates rise. This convexity is modest for vanilla swaps but becomes material for large portfolios and for risk limits expressed in DV01 terms.

#### Worked example (USD 10M)

**Trade parameters.** Notional: USD 10M. Tenor: 5 years. Client pays fixed 4.25% semi-annually (30/360). Client receives 3M SOFR quarterly (actual/360, compounded in arrears). Trade date: spot. CSA: daily margin, zero threshold. Mid-market 5-year swap rate: 4.20%.

**Economic decomposition.** The swap is executed 5 bps above mid-market. The desk receives 4.25% fixed (mid 4.20% plus 5 bps spread) and pays 3M SOFR. The desk's spread revenue is 5 bps running on USD 10M, or USD 5K per annum, totaling USD 25K over the 5-year life (undiscounted). DV01 at inception: approximately USD 4,500. The initial MTM is slightly positive to the desk (the 5 bps off-market rate gives the desk an immediate present-value gain of approximately USD 22K, which is the PV of 5 bps over 5 years).

**Good scenario (rates rise).** SOFR rises to 5.25% by year 2. The client pays 4.25% fixed and receives approximately 5.25% floating. Net receipt: approximately 1.0% per annum, or USD 100K per annum. The swap has positive mark-to-market for the client. If the client entered the swap to hedge fixed-rate debt, the hedge is performing as intended --- the floating receipts partially offset the higher floating-rate borrowing cost.

**Bad scenario (rates fall).** SOFR falls to 2.25% by year 2. The client pays 4.25% fixed and receives approximately 2.25% floating. Net payment: approximately 2.0% per annum, or USD 200K per annum. The swap has negative mark-to-market for the client. If the swap was a speculative position (not a hedge), the client is losing money. If the swap was hedging fixed-rate debt, the loss on the swap is offset by the gain on the debt position (lower refinancing cost).

#### Reconciliation specifics

**SOFR fixing date** --- the floating leg requires the correct SOFR fixing for each reset period --- SOFR is published by the Federal Reserve Bank of New York on T+1 (the rate for business day T is published on T+1) --- if Murex applies the T fixing instead of the T-1 fixing for a given observation date, every floating payment will be calculated on the wrong rate.

**Compounding convention** --- SOFR-based swaps compound the daily rate over the accrual period (compounding in arrears with a lookback) --- the lookback period (typically 2 business days) shifts the observation window so that the floating rate is known before the payment date --- if Murex does not apply the lookback, the floating payment cannot be calculated in time for settlement, producing a payment delay.

**Day count mismatch** --- the fixed leg uses 30/360 and the floating leg uses actual/360 --- these conventions produce different accrual fractions for the same calendar period --- if Murex applies the same day count to both legs, every net payment will be incorrect.

**Payment netting** --- the ISDA Master Agreement requires net settlement (single net payment on shared payment dates) --- if Murex does not apply netting, both parties send gross payments, creating unnecessary settlement risk and cash flow complexity.

**CSA margin calculation** --- daily margin calls are based on the swap's MTM --- if the discount curve in Murex does not match the CSA-specified curve (e.g., Murex uses LIBOR discounting but the CSA specifies OIS), the MTM will differ from the counterparty's calculation, producing disputed margin calls.

**Fallback rate** --- if SOFR is unavailable (publication delay or cessation), the ISDA fallback protocol specifies the replacement rate and spread adjustment --- if Murex does not implement the fallback, the floating leg cannot be calculated during a disruption.

#### Desk view

The Vanilla IRS is the building block of the structured rates business. Every structured rate product in this desk bible --- callable notes, range accruals, steepeners --- can be decomposed into a vanilla swap plus embedded options. Understanding the swap is prerequisite to understanding any structured rate trade.

For the desk, the swap is a flow product: revenue comes from bid-offer spread on client trades, and risk is managed through a hedged book. The desk does not typically hold directional DV01 exposure on vanilla swaps --- client flows are hedged with offsetting swaps or futures, and the desk earns the bid-offer spread. The swap is appropriate for any client with a genuine interest rate exposure to hedge or a deliberate rate view to express. It is the most transparent interest rate derivative: no embedded optionality, no structural complexity, no hidden risks. The counterparty credit risk, which historically was the swap's primary risk beyond rates, is now substantially mitigated by bilateral margin under CSA and, for cleared swaps, by central counterparty clearing.

It is not appropriate when the client does not understand DV01, when the notional is too small to justify the operational overhead (ISDA documentation, margin management), or when the client is using a swap to speculate without understanding that losses are uncapped.

#### Desk shorthand

*Pay fixed, receive float; pure rate bet.*

---

## Part 6 — Credit-Linked Notes

### Vanilla Credit-Linked Note

#### Definition

The Vanilla Credit-Linked Note (CLN) is a funded credit derivative, issued as a structured note under an ISDA or MTN wrapper, that pays a fixed coupon above the risk-free rate in exchange for the investor bearing the credit risk of a single reference entity. The note has two terminal outcomes. If no credit event occurs during the note's life, the investor receives par plus all scheduled coupons at maturity. If a credit event occurs --- Bankruptcy, Failure to Pay, or Restructuring as defined under the applicable ISDA Credit Definitions --- the note terminates early and the investor receives the recovery value of the reference obligation, which is determined by auction, dealer poll, or a fixed recovery rate as specified in the Termsheet. The coupon compensates the investor for bearing credit risk: it equals the risk-free rate plus a spread that reflects the market-implied probability of default and the expected loss given default. The investor is, in economic substance, selling credit protection in funded form. Capital protection is zero --- on a credit event with zero recovery, the investor loses the entire principal.

#### Construction

The note decomposes into two components. The investor's principal is placed in risk-free collateral (cash deposit or government bond), which generates the risk-free rate and provides the par redemption at maturity if no credit event occurs. Against this collateral, the investor has sold credit protection via an embedded credit default swap (CDS) on the reference entity. The CDS premium, received by the investor as the spread above the risk-free rate, compensates for the contingent obligation to absorb losses on a credit event. This is the funded equivalent of an unfunded CDS: where an unfunded CDS requires the protection seller to post margin and settle losses in cash, the CLN prefunds the maximum loss by locking the principal in collateral. The structure is therefore operationally simpler for investors who cannot trade unfunded derivatives --- private bank clients, certain institutional mandates, or investors in jurisdictions where unfunded derivative trading is restricted. Pricing is driven by the CDS spread of the reference entity, the assumed recovery rate, and the risk-free rate, computed through a hazard rate model that implies default probabilities from observed CDS spreads.

#### Booking & systems

The book of record is NEMO, which carries the trade lifecycle, notional and currency, reference entity (legal name and identifier), credit event type definitions, restructuring variant, coupon schedule, maturity date, and recovery determination method. Risk and P&L run through Sophis, which prices the embedded CDS using the reference entity's CDS spread curve, computes CS01 (credit spread sensitivity), models jump-to-default risk, and generates daily mark-to-market and P&L attribution split between spread movement and carry. The legal document is the Termsheet, which specifies the ISDA Credit Definitions version (2003 or 2014), credit event types, restructuring variant (CR, MR, MMR, or Old-R), reference obligation, recovery determination method, settlement type, and coupon accrual treatment on credit event. Murex is not used. The dominant operational risk is restructuring variant mismatch: if the Termsheet specifies Modified Restructuring (MR) but NEMO is booked with full Restructuring (CR), the note will trigger on restructuring events that should not qualify under MR, producing a premature and incorrect settlement.

#### Pricing intuition

The dominant risk measures are CS01 and jump-to-default. CS01 measures the note's sensitivity to a 1 basis point parallel shift in the reference entity's CDS spread curve --- a 1 bps widening reduces the note's mark-to-market value because the embedded protection sold by the investor is now more expensive to replace. Jump-to-default risk measures the instantaneous loss if the reference entity defaults today: the investor loses par minus recovery, and the note terminates. These two risks are fundamentally different in character: CS01 is a continuous market risk that produces daily P&L volatility; jump-to-default is a discontinuous event risk that produces a one-time catastrophic loss.

The headline coupon is driven by three primary levers: a wider CDS spread directly increases the coupon (the investor is paid more for selling protection on a riskier credit); a lower assumed recovery rate increases the loss-given-default and therefore the premium the investor demands; and longer tenor increases cumulative default probability, increasing the spread. For a BBB+ investment-grade corporate with a 5-year CDS spread of 150 bps, the credit spread component contributes approximately 1.1% per annum above the risk-free rate to the headline coupon after FTP and desk margin. The key model input is the hazard rate --- the instantaneous conditional probability of default at each point in time, implied from the CDS spread term structure and the assumed recovery rate.

Wrong-way risk is the critical sophistication test for CLN investors. If the CLN issuer (the bank) is correlated with the reference entity --- for example, both are financial institutions in the same jurisdiction --- then a credit event on the reference entity may coincide with distress at the issuer, threatening both the CLN payoff and the issuer's ability to honour it. The investor must assess issuer-reference entity correlation independently.

#### Worked example (USD 10M)

**Trade parameters.** Notional: USD 10M. Tenor: 5 years, annual coupon. Reference entity: single-name investment-grade corporate (BBB+). CDS spread: 150 bps per annum. Risk-free rate: 4.5% per annum. Recovery rate assumption: 40%. Settlement: cash (auction). Coupon: 5.6% per annum (paid annually).

**Economic decomposition.** The 5.6% headline coupon reconciles as follows. The risk-free rate on collateral is 4.5% per annum (USD 450K per annum). The CDS spread received by the investor is 150 bps per annum (USD 150K per annum). Funds transfer pricing absorbs 0.2% per annum (USD 20K). The desk margin is 0.2% per annum (USD 20K). Issuer funding contributes 0.3% per annum (USD 30K). Arithmetic check: risk-free 4.5% plus CDS spread 1.5% minus FTP 0.2% minus desk margin 0.2% minus issuer funding differential 0.0% equals 5.6% headline coupon. Net credit spread to investor: 1.1% per annum above the risk-free rate.

**Good scenario.** No credit event occurs during the 5-year life. The investor receives five annual coupons of USD 560K (total USD 2.8M) plus par (USD 10M) at maturity. Total proceeds: USD 12.8M on a USD 10M investment. Annualized return: 5.6%.

**Bad scenario.** The reference entity experiences a Bankruptcy credit event in year 3. The ISDA Determinations Committee triggers an auction. The auction determines a recovery price of 40%. The note terminates. The investor receives the recovery amount: 40% of par, or USD 4M. The investor has received three annual coupons (3 x USD 560K = USD 1.68M) prior to the credit event. Total proceeds: USD 5.68M on a USD 10M investment. Net loss: USD 4.32M, or 43.2% of notional. The investor's annualized return over the 3-year holding period is approximately negative 17%.

#### Reconciliation specifics

**Reference entity** --- NEMO carries the reference entity by legal name and identifier (e.g., CUSIP, ISIN of reference obligation) --- if a succession event (merger, spin-off, or name change) occurs after trade date, NEMO must be updated to reflect the successor entity or the credit event determination may reference the wrong legal entity, invalidating the protection.

**Credit event types** --- the Termsheet specifies which credit events trigger settlement: Bankruptcy, Failure to Pay, and a Restructuring variant (CR, MR, MMR, or Old-R) --- CR (full Restructuring) triggers on any restructuring event including maturity extension or coupon reduction; MR (Modified Restructuring) limits deliverable obligations to those maturing within 30 months; MMR (Modified Modified Restructuring) extends to 60 months --- booking the wrong variant in NEMO changes which events trigger the note and which obligations can be delivered.

**Recovery determination method** --- auction settlement (ISDA protocol), dealer poll, or fixed recovery rate --- if the Termsheet specifies auction but no auction is held (e.g., too few CDS contracts outstanding), the fallback mechanism must be defined or the recovery value is indeterminate.

**Coupon accrual on credit event** --- the Termsheet may specify that accrued coupon is paid up to the credit event date, or that the accrued coupon is forfeited --- if NEMO accrues the coupon to credit event date but the Termsheet specifies forfeiture, the desk will pay a coupon it should not have, creating a cash flow break.

**Settlement type** --- physical settlement (investor delivers reference obligations to the desk in exchange for par) vs cash settlement (investor receives auction or poll recovery price) --- physical settlement requires the investor to source and deliver bonds, creating an operational burden that cash settlement avoids.

**ISDA Credit Definitions version** --- the 2003 Definitions and 2014 Definitions differ in restructuring mechanics, successor event handling, and asset package delivery --- NEMO and Sophis must reference the same version or the credit event determination process will follow different rules across systems.

#### Desk view

The Vanilla CLN is the simplest funded credit derivative. The investor is selling credit protection and receiving a coupon that includes the CDS spread as compensation. The structure exists because many investors --- private bank clients, certain fund mandates, corporates --- cannot or prefer not to trade unfunded CDS directly. The CLN provides the same economic exposure in a note format that settles like a bond, requires no ISDA master agreement with the investor, and prefunds the maximum loss.

The product is appropriate when the investor has genuine conviction on the credit quality of the reference entity, understands that recovery on default is uncertain (auction outcomes vary), and can absorb a potential loss of 50--70% of notional on an investment-grade credit event. The critical question the desk should pose to the investor: "Do you understand that this is not a corporate bond? A corporate bond exposes you to the issuer's credit. This CLN exposes you to a different entity's credit --- and if the issuer and the reference entity are correlated, you are exposed to both." Wrong-way risk is the single most misunderstood feature of the product.

It is not appropriate when the investor confuses the CLN with a direct investment in the reference entity's bonds, when the investor cannot articulate the difference between Restructuring variants, or when the CLN issuer has material credit correlation with the reference entity.

#### Desk shorthand

*Funded CDS; coupon for default risk.*

---

### Skew CLN

#### Definition

A Skew CLN is a Credit-Linked Note (CLN) where the embedded CDS is priced using a non-standard restructuring variant, recovery assumption, or both. The "skew" refers to the pricing difference between the standard market convention and the convention used in the note — a CLN priced with a Complete Restructuring (CR) trigger commands a different CDS spread than the same reference entity priced with Modified Restructuring (MR).

The credit event mechanics are identical to a Vanilla CLN (see VCLN001): the investor receives an enhanced coupon funded by selling single-name credit protection, and loses principal (net of recovery) if a credit event occurs. The structural innovation is in pricing, not mechanics.

Restructuring variants, defined by ISDA Credit Definitions, determine which types of restructuring events trigger a payout:

- **CR (Complete Restructuring):** Broadest — any restructuring qualifies. Highest CDS spread.
- **MR (Modified Restructuring):** Limits maturity of deliverable obligations post-restructuring. Lower spread than CR.
- **MMR (Modified Modified Restructuring):** European variant. Tighter limits than MR.
- **Old-R (Old Restructuring):** Pre-2003 convention. Rarely used in new issuance.

The skew between CR and MR for a typical BBB-rated corporate is 20-40 bps. This skew funds the difference in coupon between a standard CLN and a Skew CLN. An investor who accepts the narrower MR trigger (lower probability of restructuring payout) receives a higher coupon than an investor who demands the broader CR trigger.

#### Construction

The Skew CLN has the same two-component structure as VCLN001:

**Component 1 — Fixed-rate bond (funding).** Par redemption conditional on no credit event. The investor receives 100% of notional at maturity if no credit event occurs on the reference entity.

**Component 2 — Credit default swap (embedded, skew-adjusted).** The investor sells single-name credit protection with a non-standard restructuring variant. The CDS spread — adjusted for the restructuring skew — funds the enhanced coupon. For a BBB-rated corporate with a standard MR CDS spread of 250 bps, the CR-equivalent spread is approximately 280 bps. The 30 bps skew reflects the additional restructuring risk under CR.

**The skew adjustment.** The note's coupon reflects the restructuring variant specified in the Termsheet. If the Termsheet specifies MR but the market quotes CR, the desk must apply a CR-to-MR skew adjustment to derive the correct CDS spread for pricing. This adjustment depends on the reference entity's credit quality, sector, and the current restructuring basis in the CDS market.

#### Booking & systems

Skew CLNs are booked in NEMO (book of record) and Sophis (risk and P&L).

**NEMO.** Carries the trade lifecycle, reference entity, reference obligation, and credit event definitions. The restructuring variant (CR/MR/MMR/Old-R) is a critical field — it determines which credit events trigger a payout. The restructuring variant must match the Termsheet exactly. A CR note booked as MR in NEMO will not trigger on restructuring events that should be covered.

**Sophis.** Carries the CDS spread curve (skew-adjusted), CS01 computation, jump-to-default risk, and daily mark-to-market. The CDS curve used for pricing must reflect the note's restructuring variant. If the market quotes CR but the note uses MR, Sophis must use an MR-adjusted curve — not the raw CR market quote. The recovery rate assumption must match between NEMO and Sophis.

**Termsheet** defines the restructuring variant, recovery determination method, settlement type (physical or cash/auction), reference entity, reference obligation, and ISDA Credit Definitions version. The ISDA version is critical — the 2014 Definitions handle restructuring differently from the 2003 Definitions.

#### Pricing intuition

Skew CLN pricing is fundamentally CDS pricing with a restructuring variant adjustment.

**CS01 (credit spread sensitivity).** The primary risk measure. A 1 bps widening of the reference entity's CDS spread produces a mark-to-market loss. CS01 is the same concept as DV01 for rates — the dollar value of 1 bps of credit spread movement.

**Restructuring variant pricing.** The skew between restructuring variants is driven by the probability that a restructuring event (as opposed to bankruptcy or failure to pay) is the trigger. For investment-grade corporates, restructuring is a meaningful portion of the credit event probability — spreads can differ by 20-40 bps between CR and MR. For high-yield names, restructuring is relatively rare compared to bankruptcy, so the skew is smaller (5-15 bps).

**Recovery rate sensitivity.** The loss given default is (1 − recovery rate) × notional. A standard recovery assumption of 40% means a credit event costs the investor 60% of notional. If the note uses a non-standard recovery assumption (e.g., 30%), the loss is higher but the CDS spread is also higher — the investor receives a larger coupon for accepting a worse recovery assumption.

**Greeks:**
- CS01: Primary risk. Linear sensitivity to CDS spread changes
- Jump-to-default: Discontinuous risk — the credit event produces a sudden loss of (1 − recovery) × notional
- Recovery rate: Affects both the loss amount and the CDS spread
- Restructuring basis: The CR-MR skew can move independently of the overall CDS spread

#### Worked example (USD 10M)

**Terms:** USD 10M notional, 5-year maturity, single reference entity (BBB-rated corporate). Restructuring variant: MR (Modified Restructuring). Recovery rate: 40% (standard). CDS spread (MR): 250 bps. CDS spread (CR): 280 bps. CR-to-MR skew: 30 bps.

**Decomposition:**

| Component | Value |
|---|---|
| Coupon | 5.8% p.a. |
| Benchmark (risk-free) | 3.0% |
| Coupon enhancement (credit spread) | 2.8% |
| Funding cost | 3.0% |
| FTP | 0.3% |
| Desk margin | 0.2% |
| Credit spread (net to investor) | 2.3% |

**Verification:** 3.0% + 0.3% + 0.2% + 2.3% = 5.8%. Matches coupon.

**Skew calculation:**

| Metric | CR convention | MR convention | Skew |
|---|---|---|---|
| CDS spread | 280 bps | 250 bps | 30 bps |
| Coupon (if CLN priced at convention) | 6.1% | 5.8% | 0.3% |
| Restructuring coverage | All restructurings | Limited restructurings | MR is narrower |

**Scenario 1 — no credit event (good):**
- Investor earns 5.8% for 5 years
- Total coupon: USD 10M × 5.8% × 5 = USD 2,900,000
- Principal returned: USD 10M
- Total return: USD 12,900,000

**Scenario 2 — credit event (bankruptcy, recovery 40%):**
- Coupon stops at credit event date (assume year 3)
- Coupon received: USD 10M × 5.8% × 3 = USD 1,740,000
- Recovery: USD 10M × 40% = USD 4,000,000
- Total return: USD 5,740,000
- Loss from par: USD 4,260,000

**Scenario 3 — restructuring event (skew matters):**
- Under MR: only qualifying restructurings trigger. Some restructurings are excluded.
- Under CR: all restructurings trigger. Investor would be paid out.
- The 30 bps lower spread (MR vs CR) is compensation for this narrower coverage.
- In this scenario, an MR note may not trigger while a CR note would — the investor keeps the note but may face a restructured obligation.

#### Reconciliation specifics

**Restructuring variant (most critical).** The restructuring variant in NEMO must match the Termsheet exactly. CR, MR, MMR, and Old-R are distinct — a note booked as CR when the Termsheet says MR will trigger on restructuring events that should not be covered, creating a payout obligation that does not exist under the contract. This is a legal and operational risk, not just a pricing error.

**Recovery rate assumption.** The recovery rate in Sophis (used for pricing and P&L) must match the recovery rate in NEMO (used for settlement). If Sophis uses 40% but the Termsheet specifies 30%, the daily mark-to-market will understate the credit risk (CS01 will be too low) and the settlement amount on a credit event will be different from what the risk system expects.

**CDS spread basis.** Sophis must use the skew-adjusted CDS spread, not the raw market quote. If the market quotes CR (280 bps) but the note uses MR (250 bps), Sophis must apply the 30 bps CR-to-MR adjustment. Using the raw CR spread overstates the coupon enhancement and understates the desk margin.

**ISDA Credit Definitions version.** The 2003 and 2014 ISDA Credit Definitions handle restructuring differently. The Termsheet version must match NEMO. A mismatch creates ambiguity about which credit events are covered and how settlement proceeds.

#### Desk view

**Who buys this product.** Credit investors who understand restructuring variant pricing and want to exploit the CR-MR skew. Fund managers who believe the restructuring skew is mispriced (e.g., MR is too cheap relative to CR for a specific reference entity). Insurance companies who systematically sell MR protection because they view restructuring as a low-probability event for their target credits.

**The real risk.** The incremental yield from skew is small (30 bps in this example) relative to the total credit spread (250 bps). The investor is making a nuanced bet on the restructuring variant — a bet that is dwarfed by the underlying credit risk. If the reference entity defaults via bankruptcy, the restructuring variant is irrelevant — both CR and MR notes lose the same amount. The skew only matters in the specific scenario where a restructuring event occurs and the MR definition excludes it.

The liquidity of Skew CLNs is lower than standard CLNs. The non-standard convention reduces the pool of potential buyers on the secondary market, widening bid-ask spreads. An investor who needs to exit before maturity may face a larger liquidity discount than with a VCLN001.

**When appropriate.** Investor has strong view on restructuring variant pricing. Incremental yield is meaningful relative to portfolio return target. Investor plans to hold to maturity (avoiding liquidity risk).

**When not appropriate.** Investor does not understand restructuring variants. Needs secondary market liquidity. The 30 bps skew is immaterial to the investor's return target.

#### Desk shorthand

*Skew-priced credit; restructuring variant, recovery adjusted.*

---

### First-to-Default (FTD)

#### Definition

A First-to-Default (FTD) note is a Credit-Linked Note where the investor sells credit protection on a basket of reference entities, and the first credit event among any entity in the basket triggers the note. The investor receives the recovery value of the defaulted entity and loses the remainder of their principal. After the first default, the note terminates — the investor has no further exposure to the remaining basket names.

The FTD is the first basket credit product in the desk bible. Unlike VCLN001 and SCLN001 (which reference a single entity), the FTD references a basket of 5 names. The probability that at least one of 5 entities defaults is much higher than the probability that any specific entity defaults — this is the fundamental reason the FTD coupon (8.5%) is dramatically higher than a single-name CLN coupon (5.0-5.8%).

The investor is short default correlation. Low correlation means the 5 entities default independently — maximizing the probability that at least one defaults. High correlation means defaults cluster — either all survive or many default together. At very high correlation (approaching 100%), the FTD behaves like a single-name CLN on the weakest entity, and the spread drops to the widest individual spread.

The standard basket size is 3-7 names. More names increase the FTD probability (more chances for a first default) and increase the spread. The basket composition — specifically, the credit quality dispersion — is as important as the number of names.

#### Construction

The FTD has the same two-component structure as VCLN001:

**Component 1 — Fixed-rate bond (funding).** Par redemption conditional on no credit event in any of the 5 basket entities. If all 5 entities survive to maturity, the investor receives 100% of notional plus all coupon payments. This is the only difference from a single-name CLN: the survival condition applies to all 5 names, not just one.

**Component 2 — First-to-default basket CDS (embedded).** The investor sells credit protection on the first default in a 5-name basket. The CDS spread — determined by the joint default probability under a copula model — funds the enhanced coupon. The FTD spread (550 bps) is approximately 61% of the sum of individual CDS spreads (900 bps) at the current correlation level (~30%).

**FTD spread as a function of correlation:**

| Pairwise correlation | FTD spread | % of sum | Interpretation |
|---------------------:|-----------:|---------:|----------------|
| 0% (independent) | ~780 bps | 87% | Near-maximal FTD probability |
| 30% (market) | ~550 bps | 61% | Standard pricing |
| 70% (high) | ~350 bps | 39% | Defaults cluster — fewer "first" events |
| 100% (perfect) | ~250 bps | 28% | FTD = weakest single name |

This table shows why the investor is short correlation: lower correlation increases the FTD spread and the coupon.

#### Booking & systems

FTDs are booked in NEMO (book of record) and Sophis (risk and P&L).

**NEMO.** Carries the trade lifecycle, all 5 reference entities, all 5 reference obligations, credit event definitions per entity, and the first-to-default trigger logic. Each reference entity must be entered individually with its own credit event definitions, restructuring variant, and reference obligation. The FTD trigger logic must specify that the first credit event among any of the 5 entities triggers settlement — not just a specific entity.

**Sophis.** Carries the basket CDS pricing model, including the correlation matrix (5×5 pairwise correlations), individual CDS curves for all 5 names, CS01 per name, joint default probability under the copula, and jump-to-default risk per name. The copula model (Gaussian or Student-t) and its calibration determine the joint default distribution. Each CDS curve must be current — stale curves produce incorrect basket pricing.

**Termsheet** defines the basket composition (all 5 reference entities and obligations), first-to-default trigger logic, credit event types per entity, restructuring variant per entity, recovery determination method, settlement type, and ISDA Credit Definitions version.

#### Pricing intuition

FTD pricing is dominated by default correlation — a model parameter that is not directly observable and must be calibrated.

**Default correlation.** The pairwise default correlation between entities determines the joint default distribution. At zero correlation, each entity's default is independent — the probability of at least one default is 1 − (1 − p₁)(1 − p₂)...(1 − p₅), which is much higher than any individual p_i. At perfect correlation, all entities default together or all survive — the FTD probability collapses to the probability of the weakest single name.

**Copula model.** The standard approach uses a Gaussian copula to model joint defaults. The copula takes individual default probabilities (from CDS curves) and a correlation matrix as inputs, and produces joint default probabilities. The Student-t copula is an alternative that produces fatter tails — higher probability of extreme joint default events. The choice of copula has a material impact on FTD pricing, particularly in the tails.

**Weakest-name dominance.** The entity with the widest CDS spread (Name 5, 250 bps in the example) contributes disproportionately to the FTD probability. In the limit of low correlation, the FTD probability is approximately the sum of individual default probabilities, and the widest spread dominates that sum. Removing the widest-spread name from the basket would reduce the FTD spread by much more than removing the tightest-spread name.

**Greeks:**
- Correlation: Primary model risk. Short correlation = high FTD spread
- CS01 (per name): 5 individual spread sensitivities. Widest name has highest CS01 contribution
- Joint default probability: The probability of at least one default in the basket
- Jump-to-default (per name): Discontinuous risk — any one entity's credit event triggers the note
- Recovery rate (per name): Only the defaulting entity's recovery matters at settlement

#### Worked example (USD 10M)

**Terms:** USD 10M notional, 5-year maturity, 5-name basket. CDS spreads: Name 1 (120 bps), Name 2 (150 bps), Name 3 (180 bps), Name 4 (200 bps), Name 5 (250 bps). Sum of individual spreads: 900 bps. Pairwise correlation: 30%. Recovery: 40% (all names).

**Decomposition:**

| Component | Value |
|---|---|
| Coupon | 8.5% p.a. |
| Benchmark (risk-free) | 3.0% |
| Coupon enhancement (basket spread) | 5.5% |
| Funding cost | 3.0% |
| FTP | 0.3% |
| Desk margin | 0.2% |
| Basket spread (net to investor) | 5.0% |

**Verification:** 3.0% + 0.3% + 0.2% + 5.0% = 8.5%. Matches coupon. FTD spread 550 bps = 61% of sum of individual spreads 900 bps (at 30% pairwise correlation).

**FTD probability calculation (simplified):**

| Name | 5Y CDS spread | Implied 5Y default prob. |
|------|---:|---:|
| Name 1 | 120 bps | ~5.8% |
| Name 2 | 150 bps | ~7.2% |
| Name 3 | 180 bps | ~8.6% |
| Name 4 | 200 bps | ~9.5% |
| Name 5 | 250 bps | ~11.7% |

At zero correlation, probability of at least one default ≈ 1 − (0.942)(0.928)(0.914)(0.905)(0.883) ≈ 1 − 0.617 ≈ 38.3%.

At 30% correlation, the probability is lower (~28%) because some default paths overlap.

**Scenario 1 — no credit event (good):**
- All 5 names survive 5 years
- Investor earns 8.5% for 5 years
- Total coupon: USD 10M × 8.5% × 5 = USD 4,250,000
- Principal returned: USD 10M
- Total return: USD 14,250,000

**Scenario 2 — weakest name defaults at year 2 (bad):**
- Name 5 defaults. Recovery: 40%
- Coupon received: USD 10M × 8.5% × 2 = USD 1,700,000
- Recovery: USD 10M × 40% = USD 4,000,000
- Total return: USD 5,700,000
- Loss from par: USD 4,300,000
- Note terminates — investor has no exposure to Names 1-4 after settlement

**Scenario 3 — correlation spike (model risk):**
- Correlation increases from 30% to 60% (e.g., systemic credit stress)
- FTD spread drops from 550 bps to ~400 bps
- Mark-to-market loss: significant — the basket protection investor sold is now worth less
- But: if correlation increases because all names are deteriorating, the mark-to-market loss is compounded by widening individual CDS spreads

#### Reconciliation specifics

**Basket composition (most critical).** All 5 reference entities and their reference obligations must match exactly between NEMO and the Termsheet. A single wrong entity in NEMO means the note has credit exposure to an entity the investor did not agree to — a legal and operational failure. For a 5-name basket, this requires 5 entity verifications and 5 reference obligation verifications.

**FTD trigger logic (operationally critical).** NEMO must implement the first-to-default logic: the first credit event among any of the 5 entities triggers settlement. If NEMO's trigger logic requires all 5 entities to default (an Nth-to-default with N=5), or if it only monitors one entity, the note will not settle correctly. The trigger logic is the most common FTD booking error.

**Correlation matrix (model risk).** The 5×5 pairwise correlation matrix in Sophis must be calibrated to market data — CDX/iTraxx tranche prices, single-name CDS options, or historical default frequencies. A flat correlation assumption (e.g., 30% for all pairs) is an approximation that may materially misprice the basket if the entities have heterogeneous sector/geography exposure. For a 5-name basket, there are 10 unique pairwise correlations.

**Individual CDS curves.** All 5 CDS curves in Sophis must be current. A stale curve on any single name will distort the basket pricing — particularly if the stale curve belongs to the widest-spread name, which contributes most to the FTD probability.

#### Desk view

**Who buys this product.** Yield-hungry investors willing to take concentrated first-loss credit risk in exchange for a coupon far above single-name CLN levels. Hedge funds with a specific view on default correlation (short correlation = FTD buyer). Insurance companies with credit research capability who can assess all 5 basket names.

**The real risk.** The most dangerous misconception about FTDs is that they are "diversified" credit products. The opposite is true: the FTD is concentrated first-loss risk. The investor loses on the first default — they are exposed to the union of 5 credit risks, not the average. Five BBB-rated names with 150 bps average spread produce an FTD with a ~28% five-year default probability (at 30% correlation) — far higher than any single name's ~7%.

The correlation risk is a second-order risk that is poorly understood by most investors. When credit stress hits an industry or region, correlations spike — the FTD spread drops (bad for the investor's mark-to-market) and individual CDS spreads widen (also bad). This creates a double hit: the investor is short correlation and long credit, both of which move against them in a stress scenario.

**When appropriate.** Investor has strong conviction that all 5 names survive 5 years. Investor understands basket default probability (not "diversification"). Investor has credit research capability for all basket names.

**When not appropriate.** Investor interprets basket as diversification (it is concentration). Credit cycle turning. Investor cannot independently assess all 5 reference entities.

#### Desk shorthand

*First loss on basket; correlation bet, five names.*

---

### Nth-to-Default (NTD)

#### Definition

An Nth-to-Default (NTD) note is a Credit-Linked Note where the investor sells credit protection on a basket of reference entities, and the Nth credit event triggers the note. For a 2nd-to-default (2TD), the first default in the basket does not affect the investor — the note only triggers when a second entity experiences a credit event.

The NTD is the mezzanine counterpart to the FTD (see FTD001). Where the FTD investor takes first-loss risk (triggered by the first default), the NTD investor is protected against the first (N-1) defaults and only bears loss from the Nth event onward. This protection comes at a cost: the NTD coupon is lower than the FTD coupon because the trigger probability is lower.

The critical insight is the correlation reversal. The FTD investor is short correlation — low correlation maximizes the probability of at least one default. The NTD investor is long correlation — high correlation means defaults cluster, so if one entity defaults, others are likely to follow, making the Nth default more probable. At very high correlation, the NTD behaves like the FTD (if one defaults, all default). At zero correlation, the NTD spread approaches zero (N defaults from independent entities is extremely unlikely).

#### Construction

The NTD has the same two-component structure as FTD001:

**Component 1 — Fixed-rate bond (funding).** Par redemption conditional on fewer than N credit events in the basket. If 0 or 1 entities default (for a 2TD), the investor receives 100% of notional at maturity. The investor survives the first default — only the second triggers settlement.

**Component 2 — Nth-to-default basket CDS (N=2).** The investor sells credit protection on the second default in a 5-name basket. The 2TD spread (280 bps) is approximately 51% of the FTD spread (550 bps) for the same basket. The lower spread reflects the lower trigger probability.

**NTD spread as a function of N:**

| N | Product | Spread | % of FTD | Correlation exposure |
|--:|---------|-------:|---------:|---------------------|
| 1 | First-to-default | 550 bps | 100% | Short correlation |
| 2 | 2nd-to-default | 280 bps | 51% | Long correlation |
| 3 | 3rd-to-default | 90 bps | 16% | Strongly long correlation |
| 5 | Last-to-default | 15 bps | 3% | Extremely long correlation |

This table shows the rapid spread decline with increasing N. The 5th-to-default (last-to-default) on a 5-name basket is almost risk-free — all 5 entities must default, which at 30% correlation is extremely unlikely.

**Default counter.** The NTD requires a running count of credit events in the basket. When the first default occurs, the counter increments to 1 and the note survives. When the second default occurs, the counter reaches N=2, and the note triggers. The defaulted entity at the Nth event determines the recovery rate.

#### Booking & systems

NTDs are booked in NEMO (book of record) and Sophis (risk and P&L).

**NEMO.** Carries the trade lifecycle, all 5 reference entities, credit event definitions per entity, and the Nth-to-default trigger logic. The N value (2) must be explicitly set — NEMO must implement a default counter that tracks how many credit events have occurred in the basket and triggers settlement only when the counter reaches N. After the first default, the note remains live with a reduced basket (4 surviving names). The recovery of the first defaulted entity is irrelevant to the investor (they are protected against it).

**Sophis.** Carries the basket CDS pricing model with the copula, correlation matrix, individual CDS curves, and the NTD-specific loss allocation. The copula model must compute the joint probability of 2 or more defaults (not just 1 or more, as for FTD). CS01 per name, joint default probabilities, and jump-to-default risk per name are all required. The sensitivity to correlation is opposite to FTD — the model must correctly capture the long-correlation exposure.

**Termsheet** defines the basket composition, N value, credit event types per entity, recovery determination, settlement type, and ISDA Credit Definitions version. The N value is the single most important field in the Termsheet.

#### Pricing intuition

NTD pricing uses the same copula framework as FTD but with the opposite correlation exposure.

**Long correlation.** The NTD investor benefits from low correlation (defaults are independent, so reaching the Nth default is unlikely) and is hurt by high correlation (defaults cluster, so if one defaults, the Nth is not far behind). This is the exact opposite of the FTD investor.

To understand why: at zero correlation, the probability that 2 out of 5 independent entities default in 5 years (given individual default probabilities of 6-12%) is very small — roughly 5-8%. At high correlation (70%), defaults tend to come in waves — if one entity defaults, the conditional probability of a second default spikes. The 2TD probability at 70% correlation rises to approximately 15-20%.

**Tail correlation.** The NTD is more sensitive to tail dependence than the FTD. The choice between a Gaussian copula (thin tails) and a Student-t copula (fat tails) has a larger pricing impact for NTD than for FTD. Fat tails increase the probability of multiple simultaneous defaults — exactly the scenario that triggers an NTD.

**Surviving basket.** After the first default, the basket shrinks from 5 to 4 entities. The 2TD on the original 5-name basket becomes an effective FTD on the remaining 4-name basket. This means the NTD investor's risk profile changes after each default — they start with mezzanine risk and progressively move toward first-loss risk as entities default.

**Greeks:**
- Correlation: Long exposure — higher correlation increases NTD spread
- CS01 (per name): 5 individual sensitivities, but second-widest name may contribute more than widest (since the widest name's default is absorbed by the first-loss protection)
- Joint default probability: Probability of 2+ defaults in the basket
- Jump-to-default: After 1 default, the note becomes an FTD on the surviving basket — jump risk spikes
- Recovery rate: Only the Nth entity's recovery matters for settlement

#### Worked example (USD 10M)

**Terms:** USD 10M notional, 5-year maturity, 5-name basket (same as FTD001). N=2 (second-to-default). CDS spreads: Name 1 (120 bps), Name 2 (150 bps), Name 3 (180 bps), Name 4 (200 bps), Name 5 (250 bps). Pairwise correlation: 30%. Recovery: 40%.

**Decomposition:**

| Component | Value |
|---|---|
| Coupon | 6.2% p.a. |
| Benchmark (risk-free) | 3.0% |
| Coupon enhancement (NTD spread) | 3.2% |
| Funding cost | 3.0% |
| FTP | 0.3% |
| Desk margin | 0.2% |
| NTD spread (net to investor) | 2.7% |

**Verification:** 3.0% + 0.3% + 0.2% + 2.7% = 6.2%. Matches coupon.

**Comparison to FTD001:**

| Metric | FTD001 (N=1) | NTD001 (N=2) |
|---|---|---|
| Spread | 550 bps | 280 bps |
| Coupon | 8.5% | 6.2% |
| Correlation exposure | Short | Long |
| Trigger probability (30% corr) | ~28% | ~8% |
| Protection | None | First default absorbed |

**Scenario 1 — no credit event (good):**
- All 5 names survive 5 years
- Investor earns 6.2% for 5 years
- Total coupon: USD 10M × 6.2% × 5 = USD 3,100,000
- Principal returned: USD 10M

**Scenario 2 — one default (investor protected):**
- Name 5 defaults at year 2. Recovery: 40%
- NTD investor is unaffected — first default absorbed
- Basket shrinks to 4 names. Note continues
- Investor continues earning 6.2% on the remaining tenor
- But: NTD is now an effective FTD on 4 surviving names — risk increases

**Scenario 3 — two defaults (NTD triggers):**
- Name 5 defaults at year 2. Name 4 defaults at year 3
- First default: NTD survives (N=1 < 2)
- Second default: NTD triggers (N=2 = 2). Name 4's recovery applies
- Coupon received: USD 10M × 6.2% × 3 = USD 1,860,000
- Recovery: USD 10M × 40% = USD 4,000,000
- Total return: USD 5,860,000
- Loss from par: USD 4,140,000

#### Reconciliation specifics

**N value (most critical).** The N value must be exactly 2 in NEMO's trigger logic. If N=1, the note behaves as an FTD — the first default triggers settlement, and the investor loses their first-loss protection. If N=5, it is a last-to-default — almost risk-free with a minimal spread. A wrong N value is the single most consequential booking error for any NTD product.

**Default counter (operationally critical).** NEMO must maintain a running count of credit events across all basket entities. After the first default, the counter increments and the note continues. The counter must correctly handle simultaneous defaults (two entities defaulting on the same day should count as 2, potentially triggering the note immediately). The counter must also handle succession events — if a reference entity is restructured and replaced, the counter must track the replacement correctly.

**Basket composition.** Same as FTD001 — all 5 entities must match. After a default, the surviving basket must be correctly maintained in NEMO (4 surviving names, 1 defaulted and settled).

**Correlation matrix.** The copula must be calibrated with the correct long-correlation exposure. Using an FTD-calibrated model with short-correlation bias will underprice the NTD.

#### Desk view

**Who buys this product.** Investors who want basket credit yield with first-loss protection. Credit fund managers who are comfortable with mezzanine risk but want to avoid the first-to-default scenario. Investors who believe correlation is too low (the NTD is cheap when correlation is underpriced).

**The real risk.** The NTD's protection against the first default creates a false sense of security. After the first default occurs, the NTD becomes an effective FTD on the surviving basket — the investor's risk profile jumps from mezzanine to first-loss. If the first default is driven by systemic factors (industry downturn, recession), the conditional probability of a second default spikes — exactly when the investor becomes exposed.

The correlation exposure is subtle. Most investors understand that they are protected against the first default. Few understand that they are long correlation — meaning that a correlation spike (which often accompanies credit stress) increases the NTD's value to the protection buyer and reduces the investor's mark-to-market. The investor who bought an NTD "for the protection" may be surprised that the protection is weakest when they need it most.

**When appropriate.** View that at most 1 default in the basket. Understanding of correlation direction (long correlation). Investor has analyzed all 5 basket names and believes systemic clustering is unlikely.

**When not appropriate.** Credit cycle turning (systemic defaults cluster). Investor does not understand the correlation reversal vs FTD. Investor interprets "mezzanine" as "safe."

#### Desk shorthand

*Second loss on basket; long correlation, mezzanine.*

---

### Synthetic CDO Tranche (Tranche)

#### Definition

A synthetic CDO tranche provides leveraged credit exposure to a defined slice of the loss distribution on a large reference portfolio. The investor sells protection on a specific attachment–detachment range — here, the 3–7% mezzanine tranche on the 125-name CDX IG index. Losses are allocated sequentially from the bottom: the equity tranche (0–3%) absorbs first, then the mezzanine (3–7%), then senior (7%+). The investor receives a running premium for bearing losses within their slice.

Unlike FTD and NTD products that reference small baskets (typically 5 names), synthetic tranches reference large portfolios where the law of large numbers allows statistical modelling of the loss distribution. The key pricing parameter shifts from flat pairwise correlation (FTD/NTD) to base correlation — a market-implied, tranche-specific correlation parameter calibrated from quoted tranche spreads.

#### Construction

The product is assembled as follows:

1. **Reference portfolio.** CDX IG index: 125 investment-grade names, equally weighted at 0.8% each.
2. **Tranche boundaries.** Attachment point 3%, detachment point 7%. The tranche width is 4%.
3. **Subordination.** The equity tranche (0–3%) sits below and absorbs the first 3% of portfolio losses. The mezzanine investor is protected until cumulative losses exceed 3%.
4. **Leverage.** Within the 3–7% slice, the tranche has effective leverage of approximately 1/width ≈ 25× on incremental portfolio losses. A 1% portfolio loss that falls entirely within the slice produces a 25% tranche loss.
5. **Loss exhaustion.** If cumulative portfolio losses reach 7%, the tranche is fully written down.

The investor sells protection on the 3–7% slice with notional USD 10,000,000, receiving 500 bps running premium (quarterly, act/360). The implied portfolio notional is USD 250,000,000 (= USD 10M / 4%).

#### Booking & Systems

Booked in NEMO (book of record) and Sophis (risk and P&L).

**NEMO fields (critical):**
- Reference portfolio composition (125 names, CDX IG series)
- Attachment point: 3%
- Detachment point: 7%
- Tranche notional: USD 10,000,000
- Loss allocation rule: sequential bottom-up
- Premium: 500 bps running, quarterly act/360
- Default event counter: portfolio-wide, tracks cumulative losses

**Sophis fields (critical):**
- Base correlation model: calibrated from index tranche quotes
- Base correlation at 3% attachment: ~15%
- Base correlation at 7% detachment: ~25%
- Portfolio loss distribution: Gaussian copula, large homogeneous pool (LHP) approximation
- Individual CDS curves (125 names): current market
- Expected tranche loss: computed from loss distribution
- Tranche delta (CS01): sensitivity to index spread

The Termsheet governs: portfolio composition, tranche boundaries, premium, credit event definitions, and settlement mechanics.

#### Pricing Intuition

The tranche premium compensates for the expected loss within the 3–7% slice plus a risk premium for correlation uncertainty.

**Base correlation** is the primary pricing parameter. Unlike flat correlation used for small baskets, base correlation is a market-implied correlation calibrated separately at each attachment point. The base correlation at 7% minus the base correlation at 3% determines the tranche's loss allocation — higher base correlation at the detachment point means a fatter loss tail, pushing more losses into the mezzanine tranche.

**Why base correlation, not flat correlation?** Flat correlation produces inconsistent (sometimes negative) tranche values across the capital structure. Base correlation is monotonically increasing with attachment point, eliminating this problem and providing a single implied parameter per tranche.

**Loss distribution.** With 125 names, the Gaussian copula LHP approximation converts the high-dimensional default problem into a one-factor model. The conditional default probability given the systematic factor is P(default | M) = Φ((Φ⁻¹(p) − √ρ × M) / √(1−ρ)), where p is the individual default probability, ρ is the asset correlation, and M is the common factor.

#### Worked Example

**Parameters:** Notional USD 10,000,000 on the 3–7% mezzanine tranche. CDX IG, 125 names. Premium 500 bps running (quarterly, act/360). 5-year maturity. Recovery 40%.

**Decomposition:**
- Expected tranche loss: 320 bps
- Correlation risk premium: 120 bps
- Liquidity / bid-offer: 60 bps
- **Total premium: 500 bps**

Verification: 320 + 120 + 60 = 500 bps. ✓

**Annual premium income:** USD 10,000,000 × 5.00% = USD 500,000 per year.
**Total premium (5 years, undiscounted):** USD 500,000 × 5 = USD 2,500,000.

**Scenario 1 — No defaults.** Zero portfolio losses. Tranche untouched. Investor receives full USD 2,500,000 premium over 5 years.

**Scenario 2 — Moderate defaults (4 defaults, cumulative loss < 3%).** Each name is 0.8% of portfolio. 4 defaults × 0.8% × (1 − 40% recovery) = 4 × 0.48% = 1.92% portfolio loss. Loss stays below 3% attachment — mezzanine tranche untouched. Investor receives full premium.

**Scenario 3 — Severe defaults (10 defaults, loss penetrates tranche).** 10 defaults × 0.8% × 60% LGD = 4.80% portfolio loss. Equity tranche (0–3%) fully exhausted. Remaining 1.80% falls into mezzanine tranche (3–7%). Tranche loss = 1.80% / 4.00% = 45% of tranche notional = USD 4,500,000. Premium received (assume defaults at year 3): USD 500,000 × 3 = USD 1,500,000. Net P&L: USD 1,500,000 − USD 4,500,000 = −USD 3,000,000.

#### Reconciliation

The reconciliation checks are:

| Check | NEMO | Sophis | Match |
|---|---|---|---|
| Tranche notional | USD 10,000,000 | USD 10,000,000 | ✓ |
| Attachment point | 3% | 3% | ✓ |
| Detachment point | 7% | 7% | ✓ |
| Portfolio composition | 125 names (CDX IG) | 125 names | ✓ |
| Loss allocation | Sequential bottom-up | Sequential bottom-up | ✓ |
| Premium | 500 bps quarterly | 500 bps quarterly | ✓ |
| Default counter | Portfolio-wide | Portfolio-wide | ✓ |

**Key reconciliation risk:** Attachment/detachment mismatch between NEMO and Sophis causes incorrect loss allocation. Must verify tranche boundaries exactly match.

#### Desk View

Base correlation is THE risk parameter. A trader managing a mezzanine tranche book focuses on:

1. **Base correlation moves.** A 1-point increase in base correlation at 7% (detachment) widens the mezzanine tranche spread — more losses are modelled as reaching the mezzanine layer.
2. **Delta hedging.** The tranche is delta-hedged with the CDX IG index. Tranche delta (dV/dS where S is the index spread) determines the hedge ratio.
3. **Correlation skew.** The equity-mezzanine spread ratio reveals relative value. Steep skew = mezzanine is cheap relative to equity.
4. **Jump-to-default risk.** A single large name defaulting can cause discrete P&L moves not captured by smooth delta hedges.
5. **Gamma on losses near attachment.** As portfolio losses approach 3%, the tranche transitions from out-of-the-money to in-the-money — convexity is highest near the attachment point.

Day-one risk: verify the base correlation calibration matches the desk's tranche pricing model. A stale calibration misprices the tranche from inception.

#### Desk Shorthand

*Mezz tranche on CDX; long base correlation, leveraged credit.*

---

## Part 7 — Steepener Notes

### Vanilla Steepener Note

#### Definition

A Vanilla Steepener Note pays a leveraged coupon linked to the spread between two CMS (Constant Maturity Swap) rates of different tenors — typically CMS 30Y − CMS 10Y. When the yield curve is steep (long rates well above short rates), the coupon is high. When the curve flattens or inverts, the coupon drops toward zero, where a floor prevents it from going negative.

The coupon formula is:

**Coupon = N × (CMS 30Y − CMS 10Y), floor 0%, cap C%**

where N is the leverage factor and C is the cap rate. Leverage of 3x–7x is typical; 5x is the standard case. The note is non-callable — there is no issuer call right, making this a pure directional bet on curve steepness for the full tenor.

The investor's trade is exchanging the certainty of a fixed-rate coupon for a leveraged exposure to the yield curve's slope. The convexity adjustment — a correction applied to CMS rates to account for the difference between a swap rate and its expected value under the forward measure — is the single most important pricing concept for this product. It reduces the effective spread and represents a hidden cost to the investor.

#### Construction

The Vanilla Steepener Note decomposes into four components:

**Component 1 — Fixed-rate bond (funding).** The note's principal structure. Provides par redemption at maturity and defines the funding cost of the note. The investor receives 100% of notional at maturity regardless of CMS rate outcomes.

**Component 2 — CMS spread coupon strip (leveraged).** A series of semi-annual coupons, each determined by the CMS 30Y − CMS 10Y spread observed on the fixing date, multiplied by the leverage factor. This is the primary value driver. With 5x leverage, every 10 bps of CMS spread produces 50 bps of coupon.

**Component 3 — CMS floor (embedded, 0%).** A strip of floorlets that activate when the leveraged CMS spread would produce a negative coupon — i.e., when the curve inverts. The investor is long this floor. It ensures the coupon never falls below zero, providing asymmetric protection against curve inversion.

**Component 4 — CMS cap (embedded, 8%).** A strip of caplets that limit the maximum coupon to 8%. The investor is short this cap — they have sold away the upside above 8% to help fund the leveraged spread exposure. The cap strikes represent extreme steepening scenarios (spread above 160 bps with 5x leverage).

**Net position:** The investor is long leveraged CMS spread exposure, long the floor (downside protection), and short the cap (upside given away). The cap and floor together create a collar around the CMS spread coupon.

#### Booking & systems

Vanilla Steepener Notes are booked in the Murex four-leg framework.

**Note leg.** The structured note carrying the CMS spread coupon formula. Critical fields: coupon formula (5 × (CMS 30Y − CMS 10Y)), leverage factor (5x), floor rate (0%), cap rate (8%), CMS fixing dates (semi-annual schedule), CMS tenor pair (30Y/10Y), CMS fixing source (ISDA CMS rate definition), day count convention, and maturity date. The coupon formula must be entered exactly — leverage, floor, cap, and tenor pair are all required for correct valuation.

**Issuer leg.** The issuer's internal funding cost. Standard fields: funding rate, funding curve, and credit spread. Computed on the note's fixed notional.

**Deposit leg.** Client collateral. Standard fields: deposit rate, tenor, and rollover convention.

**Hedge leg.** The market risk hedge consists of CMS cap/floor structures and CMS spread options that replicate the embedded optionality. Critical fields: hedge instrument type (CMS cap, CMS floor, CMS spread option), CMS tenor pair (30Y/10Y), strikes, leverage, expiry schedule, notional, convexity adjustment model, and correlation assumption. The convexity adjustment model and correlation parameters must match between the note leg valuation and the hedge leg pricing — a mismatch creates a systematic P&L leak that compounds over the note's life.

**Termsheet** defines the complete CMS fixing schedule, leverage, floor, cap, CMS tenor pair, and the ISDA CMS rate definition used for fixings. The fixing source is the key operational detail — it determines which CMS rate is used on each observation date.

#### Pricing intuition

Steepener pricing is dominated by three model-dependent inputs: the convexity adjustment, the correlation between CMS tenors, and normal volatility.

**Convexity adjustment.** CMS rates are not equal to forward swap rates. The convexity adjustment corrects for the difference between a swap rate and its expected value under the payment measure. For CMS 30Y, the adjustment is typically 3–8 bps (reducing the effective rate); for CMS 10Y, it is smaller (1–3 bps). The net effect reduces the effective CMS spread by approximately 5 bps. With 5x leverage, this costs the investor roughly 25 bps of coupon — a material hidden cost. The adjustment increases with the level of rates and with volatility.

**Correlation.** The correlation between CMS 30Y and CMS 10Y determines the distribution of the CMS spread. High correlation (e.g., 0.95) means the two rates move closely together, compressing the spread distribution and reducing option values. Lower correlation widens the spread distribution. Correlation is not directly observable — it is an implied or model parameter calibrated to CMS spread option prices or historical data. A 5-point correlation change can move the note's value by 20–40 bps.

**Normal volatility.** The swaption volatility (in Bachelier/normal terms, quoted in bps) affects both the floor value (benefit to investor) and the cap value (cost to investor). At 65 bps normal vol, the floor has meaningful value in environments where the curve is near-flat.

**Greeks:**
- Curve slope (CMS 30Y − CMS 10Y): Primary risk. 10 bps flattening → 50 bps coupon drop (5x leverage)
- Correlation: Higher correlation → lower spread vol → lower option values
- CMS convexity: Rises with rate level → reduces effective coupon in high-rate environments
- Normal vol: Affects floor and cap values in offsetting directions
- DV01: Modest — the note's principal is fixed; rate exposure is through coupon, not notional

#### Worked example (USD 10M)

**Terms:** USD 10M notional, 10-year maturity, semi-annual CMS fixings. Coupon = 5 × (CMS 30Y − CMS 10Y), floor 0%, cap 8%. CMS fixing source: ISDA CMS.

**Current market:** CMS 30Y = 4.20%, CMS 10Y = 3.40%. Spread = 80 bps.

**Decomposition:**

| Component | Value |
|---|---|
| Expected coupon (5 × 80 bps) | 4.0% p.a. |
| Funding cost | 3.0% |
| FTP | 0.4% |
| Desk margin | 0.3% |
| CMS spread optionality (floor + cap + convexity) | 1.3% |

**Verification:** 3.0% + 0.4% + 0.3% + 1.3% = 5.0%. Investor receives 4.0% expected coupon. The 1.0% difference between the total cost (5.0%) and the expected coupon (4.0%) represents the net cost of the leverage and the embedded options — the investor pays for the floor protection and convexity adjustment through the cap premium.

**Semi-annual coupon calculation (first fixing):**

| Step | Calculation | Result |
|---|---|---|
| CMS 30Y fixing | Observed rate | 4.20% |
| CMS 10Y fixing | Observed rate | 3.40% |
| CMS spread | 4.20% − 3.40% | 0.80% |
| Leveraged coupon | 5 × 0.80% | 4.00% |
| Floor test | max(4.00%, 0%) | 4.00% |
| Cap test | min(4.00%, 8%) | 4.00% |
| Semi-annual payment | USD 10M × 4.00% × 0.5 | USD 200,000 |

**Scenario 1 — curve steepens to 120 bps:**
- CMS 30Y = 4.60%, CMS 10Y = 3.40%. Spread = 120 bps
- Coupon = 5 × 1.20% = 6.0%
- Semi-annual payment: USD 10M × 6.0% × 0.5 = USD 300,000
- Investor earns well above funding — the steepening trade is paying

**Scenario 2 — curve flattens to 30 bps:**
- CMS 30Y = 3.70%, CMS 10Y = 3.40%. Spread = 30 bps
- Coupon = 5 × 0.30% = 1.5%
- Semi-annual payment: USD 10M × 1.5% × 0.5 = USD 75,000
- Investor earns below funding — the flattening is eroding the coupon

**Scenario 3 — curve inverts (spread = −20 bps):**
- CMS 30Y = 3.20%, CMS 10Y = 3.40%. Spread = −20 bps
- Leveraged coupon = 5 × (−0.20%) = −1.0%
- Floor activates: max(−1.0%, 0%) = 0%
- Semi-annual payment: USD 0
- Investor earns zero coupon — principal still protected at maturity

#### Reconciliation specifics

**CMS fixing source (most critical operational risk).** The ISDA CMS rate definition used for fixing must be identical in the Murex note leg and the hedge leg. A mismatch — even a different screen page or publication time — creates a fixing basis that produces a small but systematic P&L difference on every fixing date. Over 20 semi-annual fixings, these differences compound.

**Convexity adjustment consistency (most critical model risk).** The convexity adjustment model and its calibration parameters must be the same in the note leg valuation and the hedge leg pricing. If the note leg uses a replication-based convexity adjustment but the hedge leg uses a short-rate model adjustment, the two legs will disagree on the effective CMS rate by 2–5 bps per fixing. With 5x leverage, a 3 bps mismatch becomes a 15 bps coupon disagreement per period — approximately USD 7,500 per semi-annual fixing on USD 10M notional.

**Leverage factor.** The leverage (5x) must appear in both the note leg coupon formula and the hedge leg notional/strike calibration. An error in either leg (e.g., 5x in the note but 4x in the hedge) creates an unhedged CMS spread exposure equal to 1x the spread — approximately 80 bps of coupon risk.

**Floor/cap strikes.** The 0% floor and 8% cap must be present in both the note leg and the hedge leg. A missing floor means the investor could face negative coupons (not contractually possible). A missing cap means the issuer has unlimited coupon exposure.

**Correlation calibration.** The correlation assumption between CMS 30Y and CMS 10Y must be calibrated to market data (CMS spread options if available, or historical correlation with an appropriate lookback window). Using a default flat correlation (e.g., 90%) instead of a calibrated value creates a systematic mispricing — typically undervaluing the spread optionality.

#### Desk view

**Who buys this product.** Macro hedge funds with a structural view that the yield curve will remain steep or steepen further. Insurance companies with long-duration liabilities who believe rates will normalise (long end rising faster than short end). Pension funds seeking above-market coupons in a steep curve environment. Private bank clients who want leveraged yield without principal risk.

**The real risk.** Curve flattening or inversion eliminates the coupon entirely. The 5x leverage that amplifies steepening gains also amplifies flattening losses — every 10 bps of flattening costs 50 bps of coupon. The floor at 0% protects against negative coupons but does not protect against opportunity cost: an investor locked into a 10-year steepener during a prolonged flat-curve period earns zero while the funding rate is 3.0%.

The convexity adjustment is a persistent hidden cost. Unlike the floor (which protects) or the cap (which is visible), the convexity adjustment silently reduces the effective CMS spread on every fixing. In a high-rate, high-vol environment, the convexity adjustment can reduce the expected coupon by 30–50 bps.

**When appropriate.** Strong conviction that the yield curve will remain steep or steepen. 10-year investment horizon. Investor understands leverage and can tolerate zero-coupon periods.

**When not appropriate.** Flat or inverted curve environment. Need for stable income (the coupon is inherently volatile). Investor does not understand convexity adjustment or correlation risk.

#### Desk shorthand

*Leveraged curve bet; CMS spread, floor zero, cap eight.*

---

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

---

### Callable Steepener

#### Definition

A Callable Steepener pays a leveraged coupon linked to the CMS 30Y − CMS 10Y spread, with an issuer Bermudan call right that allows the issuer to redeem the note at par on any semi-annual call date after year 2.

The coupon formula is identical to VSTEG001:

**Coupon = 5 × (CMS 30Y − CMS 10Y), floor 0%, cap 9%**

The key difference is the callable feature. The investor sells a Bermudan call option to the issuer, receiving a higher cap (9% vs VSTEG001's 8%) as compensation. The call premium funds the wider cap and contributes to the coupon economics.

The issuer calls when it becomes economically advantageous — typically when rates fall (cheaper refinancing) or when the curve steepens significantly (capping the coupon cost). This creates negative convexity for the investor: the product is called away in exactly the scenarios where the investor would most want to keep it.

This product combines two forms of optionality — the CMS spread exposure and the Bermudan call. Their interaction is the core pricing challenge. Both are driven by rate dynamics, making them correlated. The same rate movements that increase the coupon also influence the call decision, requiring joint calibration (see CRASRT001 for the SRT parallel).

#### Construction

The Callable Steepener decomposes into five components:

**Component 1 — Fixed-rate bond (funding).** Par redemption at maturity or call date. Same as VSTEG001.

**Component 2 — CMS spread coupon strip (leveraged).** Leveraged coupon linked to CMS 30Y − CMS 10Y, observed semi-annually. Same mechanism as VSTEG001 — every 10 bps of spread produces 50 bps of coupon.

**Component 3 — CMS floor (embedded, 0%).** Prevents negative coupon. Same as VSTEG001.

**Component 4 — CMS cap (embedded, 9%).** Limits maximum coupon. Higher than VSTEG001's 8% cap — the additional 1% cap headroom is funded by the call premium.

**Component 5 — Bermudan call (issuer).** The issuer has the right to redeem the note at par on any semi-annual date starting from year 2. The investor is short this call — they have sold the issuer an option on the note's remaining tenor. The call premium (approximately 0.8% per annum) is embedded in the note's economics.

**Comparison to VSTEG001:** Same CMS spread mechanics. The callable feature adds one component (Bermudan call) and raises the cap from 8% to 9%. The investor's trade-off is clear: higher potential coupon (wider cap) in exchange for uncertain tenor (call risk).

**Comparison to CRASRT001 (SRT):** Both combine a rate-linked coupon with an issuer Bermudan call. CRASRT001 uses a range-accrual coupon on a single rate (SOFR). This product uses a leveraged CMS spread coupon. The dual optionality interaction is analogous — rate dynamics drive both the coupon and the call decision.

#### Booking & systems

Callable Steepeners are booked in the Murex four-leg framework.

**Note leg.** The structured note carrying the CMS spread coupon formula and call schedule. Critical fields: coupon formula (5 × (CMS 30Y − CMS 10Y)), leverage (5x), floor (0%), cap (9%), CMS fixing dates, call schedule (semi-annual after year 2), call notification period (typically 10 business days), CMS fixing source, and maturity date.

**Issuer leg.** Standard internal funding. Funding rate, curve, and credit spread.

**Deposit leg.** Client collateral. Standard fields.

**Hedge leg.** The market risk hedge includes CMS cap/floor structures (for the spread optionality) and a Bermudan swaption (for the call right). Critical fields: Bermudan exercise dates (must match note call dates exactly), CMS tenor pair, cap/floor strikes, convexity adjustment model, correlation assumption, and Bermudan exercise boundary calibration. The Bermudan swaption must be calibrated jointly with the CMS spread model — the call decision depends on the level and slope of rates, which also determine the CMS spread.

**Termsheet** defines the call schedule, notification period, coupon formula, and CMS fixing source. The call notification period is an operational risk — if the Termsheet specifies 10 business days and the Murex note leg uses a different convention, the issuer's exercise may be invalid.

#### Pricing intuition

Callable Steepener pricing requires joint calibration of CMS spread dynamics and the Bermudan exercise strategy.

**Dual optionality interaction.** The CMS spread coupon and the Bermudan call are not independent risks. A rate decline that steepens the curve increases the coupon (good for investor) but also increases the call probability (bad for investor). The issuer's optimal call strategy depends on the remaining coupon cost relative to refinancing — if the curve is very steep and the coupon is high (e.g., 7-8%), the issuer calls to cap their loss. This is negative convexity: the investor's upside is capped both by the 9% cap and by the call.

**When does the issuer call?** The issuer calls when the present value of remaining coupon payments exceeds the cost of refinancing. In practice:
- Rates fall significantly → issuer refinances cheaply → call
- Curve steepens sharply → coupon cost very high → call to cap losses
- Both effects compound: falling rates that steepen the curve create the highest call probability

**Bermudan value.** The Bermudan call is worth approximately 0.8% per annum to the issuer (and costs the investor the same). This premium is higher than the ICN001 Bermudan call (0.6%) because the CMS spread coupon has higher potential volatility than a fixed coupon, making the call option more valuable.

**Greeks:**
- Curve slope: Primary risk. Same as VSTEG001 but truncated by call
- Bermudan value: Increases with rate vol and decreases with rate level
- Correlation: Affects both spread distribution and the correlation between coupon and call events
- CMS convexity: Same as VSTEG001
- Negative convexity: The call creates concavity in the payoff — investor loses in both extreme steepening (call) and flattening (zero coupon) scenarios

#### Worked example (USD 10M)

**Terms:** USD 10M notional, 10-year maturity (callable semi-annually after Y2). Coupon = 5 × (CMS 30Y − CMS 10Y), floor 0%, cap 9%. CMS fixing source: ISDA CMS.

**Current market:** CMS 30Y = 4.20%, CMS 10Y = 3.40%. Spread = 80 bps.

**Decomposition:**

| Component | Value |
|---|---|
| Expected coupon (5 × 80 bps) | 4.0% p.a. |
| Funding cost | 3.0% |
| FTP | 0.4% |
| Desk margin | 0.3% |
| CMS spread optionality (floor + cap + convexity) | 1.1% |
| Bermudan call premium | 0.8% |

**Verification:** 3.0% + 0.4% + 0.3% + 1.1% + 0.8% = 5.6%. Total cost capacity exceeds the 4.0% expected coupon by 1.6%. The 0.8% call premium and the higher cap (9% vs 8%) are how the investor is compensated for accepting the call risk. The remaining 0.8% represents the reduced CMS optionality cost from the lower cap strike (9% vs VSTEG001's effective cost at 8%).

**Scenario 1 — curve steepens moderately, rates stable (no call):**
- CMS 30Y = 4.50%, CMS 10Y = 3.40%. Spread = 110 bps
- Coupon = 5 × 1.10% = 5.5%
- Semi-annual payment: USD 10M × 5.5% × 0.5 = USD 275,000
- Issuer does not call — coupon cost manageable

**Scenario 2 — curve steepens sharply, rates fall (issuer calls at Y3):**
- CMS 30Y = 4.00%, CMS 10Y = 2.80%. Spread = 120 bps
- Coupon = 5 × 1.20% = 6.0%. Very high coupon cost for issuer
- Issuer calls at Y3 — returns USD 10M at par
- Investor earned 3 years of 4.0-6.0% coupon but lost 7 years of potential high coupons
- Reinvestment at new lower rates yields ~2.5% — the reinvestment gap

**Scenario 3 — curve flattens (no call, low coupon):**
- CMS 30Y = 3.50%, CMS 10Y = 3.40%. Spread = 10 bps
- Coupon = 5 × 0.10% = 0.5%
- Semi-annual payment: USD 10M × 0.5% × 0.5 = USD 25,000
- Issuer does not call — low coupon means low cost to issuer
- Investor locked into 10 years of near-zero coupon with no call relief

#### Reconciliation specifics

**Call schedule (most critical for callable variant).** The semi-annual call dates in the Murex note leg must exactly match the Bermudan exercise dates in the hedge leg swaption. A single misaligned call date means the issuer can exercise on a date the hedge does not cover — an unhedged call event. For a 10-year note callable from Y2, there are 16 potential call dates to verify.

**Call notification period.** The Termsheet typically specifies a notification period (e.g., 10 business days before the call date). This period must be reflected in both the note leg and the hedge leg. If the note leg allows exercise with 5 days' notice but the hedge leg assumes 10 days, the hedge may fail to cover the call event.

**CMS fixing source.** Same risk as VSTEG001 — ISDA CMS rate definition must match between legs. The impact is slightly reduced for callable steepeners because the note's expected life is shorter (call probability reduces the duration).

**Convexity adjustment consistency.** Same model required in both legs. The convexity adjustment interacts with the Bermudan valuation because the adjustment affects the expected coupon, which influences the call decision.

#### Desk view

**Who buys this product.** Yield seekers who want the higher cap (9%) and are willing to accept uncertain tenor. Insurance companies with reinvestment strategies that can accommodate early redemption. Investors who believe rates will remain stable (low call probability) while the curve stays steep.

**The real risk.** Negative convexity. The investor loses in both extreme scenarios: sharp steepening triggers a call (investor loses future high coupons), and flattening means zero coupon for 10 years (issuer will not call when the note is cheap to maintain). The investor only wins in the narrow band where the curve steepens enough to generate attractive coupons but not enough to trigger a call.

This is the same reinvestment risk pattern as ICN001 (Issuer Callable Note in ELN) — the issuer calls at the worst time for the investor. The difference is that the Callable Steepener's coupon is linked to the CMS spread, not fixed, so the call decision and the coupon are correlated rather than independent.

**When appropriate.** View that curve will steepen moderately (not enough to trigger call). Stable rate environment. Investor can tolerate reinvestment risk.

**When not appropriate.** Falling rate environment (high call probability). Need for certain tenor. Investor who does not understand negative convexity.

#### Desk shorthand

*Callable curve bet; CMS spread, issuer call.*

---

### Target Accrual Redemption Note (TARN)

#### Definition

A Target Accrual Redemption Note (TARN) pays a leveraged coupon linked to the CMS 30Y − CMS 10Y spread and automatically redeems at par once the cumulative coupons paid reach a predefined target level. The last coupon is truncated so that the total coupons paid equal exactly the target — no more, no less.

The coupon formula is:

**Coupon = 5 × (CMS 30Y − CMS 10Y), floor 0%**

**Target: 25% cumulative. Auto-redemption when reached.**

There is no explicit cap. Instead, the target level acts as a lifetime coupon limiter — the investor can never receive more than 25% in total coupons over the note's life. The target replaces the cap found in VSTEG001 (8% per period) and CSTEG001 (9% per period) with a cumulative constraint.

This is the first path-dependent product in the STEG family. Each period's coupon accumulates toward the target. If the curve is steep and the coupon is 6% per year, the target (25%) is reached in roughly 4 years. If the curve flattens and the coupon is 1% per year, the target may not be reached within the 15-year maximum maturity. The investor's tenor is therefore uncertain — determined by the path of CMS spreads over the note's life.

The investor's trade is exchanging tenor certainty for a guaranteed total return. If the target is ever reached, the investor earns exactly 25% in cumulative coupons plus par principal. The risk is that the curve stays flat for 15 years and the target is never reached.

#### Construction

The TARN decomposes into four components:

**Component 1 — Fixed-rate bond (funding).** Par redemption at maturity or auto-redemption date. The maximum maturity is 15 years — longer than other steepeners (10 years) because the target mechanism may require a longer runway to accumulate coupons.

**Component 2 — CMS spread coupon strip (leveraged).** Leveraged coupon on CMS 30Y − CMS 10Y, observed semi-annually. Same mechanism as VSTEG001. No per-period cap — the target is the only coupon limiter.

**Component 3 — CMS floor (embedded, 0%).** Prevents negative coupons. Same as VSTEG001.

**Component 4 — Target redemption feature.** When the running sum of all coupons paid reaches 25%, the note automatically redeems at par. The final coupon is truncated: if the cumulative coupons before the last period are 22% and the current-period coupon would be 5%, only 3% is paid (25% − 22%), and the note redeems. This truncation ensures the investor receives exactly 25% total, not 27%.

**No cap component.** Unlike VSTEG001 and CSTEG001, there is no per-period cap. The target makes a cap redundant — even if one period's coupon is 8%, it simply accelerates the target hit and shortens the note's life.

**Path dependency.** Each period's coupon adds to the cumulative total, and the cumulative total determines whether the note redeems. The ordering of coupons matters: 8% then 0% (target hit at different time) is not the same as 0% then 8% (same total but different timing, different discounting). This is the first genuinely path-dependent STEG product.

#### Booking & systems

TARNs are booked in the Murex four-leg framework.

**Note leg.** The structured note with the CMS coupon formula and target redemption logic. Critical fields: coupon formula (5 × (CMS 30Y − CMS 10Y)), leverage (5x), floor (0%), target level (25%), truncation rule (last coupon capped at target minus cumulative), CMS tenor pair (30Y/10Y), CMS fixing source, maximum maturity (15 years), and coupon schedule. The target redemption logic is the most complex booking item — Murex must track cumulative coupons and trigger auto-redemption at the correct level.

**Issuer leg.** Standard internal funding. The funding calculation must account for the uncertain tenor — the effective duration depends on the expected life, not the maximum maturity.

**Deposit leg.** Client collateral. Standard fields.

**Hedge leg.** The market risk hedge requires path-dependent instruments or a dynamic hedging strategy. Critical fields: target barrier level (25%), CMS spread options calibrated to a multi-factor model, path simulation parameters, convexity adjustment model, and correlation assumption. The hedge must replicate the target redemption's path dependency, which typically requires Monte Carlo simulation. Static hedging (as used for VSTEG001 or RASTEG001) is insufficient — the target creates optionality that depends on the entire coupon path, not just today's spread.

**Termsheet** defines the target level, truncation rule, maximum maturity, and CMS fixing source. The truncation rule must specify exactly how the final coupon is calculated and on which date auto-redemption occurs (same date as the truncated coupon payment, or the following business day).

#### Pricing intuition

TARN pricing is the most complex in the STEG family. The path dependency means closed-form solutions are not available — pricing requires Monte Carlo simulation across thousands of rate paths.

**Expected life.** At the current spread of 80 bps, the expected annual coupon is 4.0%. The target of 25% would be reached in approximately 6.25 years if the spread remained constant. But the spread is not constant — it fluctuates, creating a distribution of possible target-hit times. If the curve is volatile, the expected life calculation becomes highly sensitive to the spread dynamics.

**Spread volatility effect.** Higher spread volatility has an asymmetric effect on the TARN. The floor at 0% means downside volatility (spread going negative) is absorbed by the floor, while upside volatility (spread widening) accelerates coupon accumulation and brings the target closer. This convexity means that higher vol generally shortens the expected life — a counterintuitive result for a note that appears to benefit from stability.

**Convexity adjustment interaction.** The CMS convexity adjustment reduces the effective spread on every fixing, slowing the coupon accumulation and pushing the expected target-hit further into the future. With 5 bps of convexity adjustment on a 15-year horizon, the cumulative impact is material — it could add 1-2 years to the expected life.

**Correlation.** High correlation between CMS 30Y and CMS 10Y compresses the spread distribution, reducing the probability of extreme spreads in both directions. This stabilizes the expected life estimate but makes the TARN more sensitive to the mean spread level.

**Greeks:**
- Curve slope: Primary risk. Determines coupon level and how fast the target is reached
- Expected life: Unique to TARNs. Changes with every fixing. Drives the note's effective duration
- Correlation: Affects spread distribution width and expected life distribution
- CMS convexity: Reduces effective coupon, extends expected life
- Path dependency: Greeks are themselves path-dependent — DV01 at year 3 depends on cumulative coupons at year 3

#### Worked example (USD 10M)

**Terms:** USD 10M notional, 15-year maximum maturity, semi-annual CMS fixings. Coupon = 5 × (CMS 30Y − CMS 10Y), floor 0%. Target: 25% cumulative. CMS fixing source: ISDA CMS.

**Current market:** CMS 30Y = 4.20%, CMS 10Y = 3.40%. Spread = 80 bps.

**Decomposition:**

| Component | Value |
|---|---|
| Expected coupon (5 × 80 bps) | 4.0% p.a. |
| Funding cost | 3.0% |
| FTP | 0.4% |
| Desk margin | 0.3% |
| Target optionality | 1.3% |

**Verification:** 3.0% + 0.4% + 0.3% + 1.3% = 5.0%. Expected coupon 4.0% = 5 × 0.80%. The 1.0% difference between cost (5.0%) and expected coupon (4.0%) represents the convexity, correlation, and target redemption optionality cost.

**Cumulative coupon path (illustrative — spread stays at 80 bps):**

| Period | CMS spread | Coupon | Cumulative | Target hit? |
|-------:|-----------:|-------:|-----------:|:-----------:|
| Y1 H1 | 80 bps | 2.0% | 2.0% | No |
| Y1 H2 | 80 bps | 2.0% | 4.0% | No |
| Y2 H1 | 80 bps | 2.0% | 6.0% | No |
| Y2 H2 | 80 bps | 2.0% | 8.0% | No |
| Y3 H1 | 80 bps | 2.0% | 10.0% | No |
| Y3 H2 | 80 bps | 2.0% | 12.0% | No |
| Y4 H1 | 80 bps | 2.0% | 14.0% | No |
| Y4 H2 | 80 bps | 2.0% | 16.0% | No |
| Y5 H1 | 80 bps | 2.0% | 18.0% | No |
| Y5 H2 | 80 bps | 2.0% | 20.0% | No |
| Y6 H1 | 80 bps | 2.0% | 22.0% | No |
| Y6 H2 | 80 bps | 2.0% | 24.0% | No |
| Y7 H1 | 80 bps | **1.0%** | **25.0%** | **Yes — truncated** |

**Truncation:** At Y7 H1, the full coupon would be 2.0%, but only 1.0% is paid (25.0% − 24.0% = 1.0%). The note redeems at par immediately.

**Scenario 1 — curve steepens to 120 bps (early target hit):**
- Annual coupon: 5 × 1.20% = 6.0% → 3.0% per half
- Target of 25% reached in approximately 4.2 years (25% / 6.0% ≈ 4.17 years)
- Investor's annualized return: 25% / 4.2 years ≈ 5.95% — excellent outcome
- But: reinvestment after 4 years at potentially different rates

**Scenario 2 — curve flattens to 20 bps (late target hit):**
- Annual coupon: 5 × 0.20% = 1.0% → 0.5% per half
- Target of 25% not reached for 25 years — exceeds maximum maturity (15 years)
- Investor earns only 15% total over 15 years (1.0% × 15 years)
- Note matures without reaching target — investor missed 10% of expected return

**Scenario 3 — curve inverts (spread ≤ 0, floor activates):**
- Coupon = 0% for the duration of inversion
- Cumulative coupon stuck at pre-inversion level
- Clock pauses on target but 15-year maturity keeps ticking
- Every year at zero coupon is a year the investor will never recover

#### Reconciliation specifics

**Target level (most critical).** The 25% target must match exactly between the Murex note leg and the hedge leg. A mismatch means the note auto-redeems at one level but the hedge assumes a different level — the hedge unwinds at the wrong time, creating an unhedged position for the remaining maturity difference.

**Truncation logic (operationally critical).** The last coupon must be truncated to hit the target exactly. If the Murex note leg pays the full untruncated coupon, the investor receives more than 25% total — a breach of the Termsheet terms. The truncation calculation requires: (a) cumulative coupons before the period, (b) current-period's full coupon, (c) difference between target and cumulative. The smaller of (b) and (c) is paid.

**Maximum maturity.** The 15-year maximum maturity must be in both legs. If the note leg has no maximum maturity, the note theoretically never expires if the target is not reached — an open-ended liability. If the hedge leg assumes a different maximum, the hedge unwinds at the wrong date.

**CMS fixing source.** Same risk as all STEG products. For TARNs, the impact compounds over more potential fixing dates (up to 30 semi-annual fixings over 15 years).

#### Desk view

**Who buys this product.** Investors with a structural view that the yield curve will steepen and who want a guaranteed total return when it does. Private bank clients who find the target feature appealing — "you will earn 25% total" is a powerful selling point. Investors who prefer total-return certainty over annual-coupon certainty.

**The real risk.** The path dependency means the investor's experience depends entirely on the sequence of CMS spreads. Two investors who hold the same TARN but start at different times may have completely different outcomes — one reaches the target in 4 years, the other is stuck for 15 years.

The "guaranteed 25% total" framing is misleading. The guarantee is conditional — the target is only reached if cumulative coupons get there. If the curve stays flat or inverts, the 25% is never paid. The maximum maturity (15 years) creates a hard deadline: any shortfall at maturity is lost permanently.

The TARN has the highest model risk in the STEG family. The expected life depends on Monte Carlo simulation of CMS spread paths, which requires accurate modeling of CMS convexity, correlation, spread dynamics, and mean reversion. A model that underestimates spread volatility will overestimate the expected life and underprice the path-dependent optionality.

**When appropriate.** Strong and sustained curve-steepening view. Investor values total-return certainty and can tolerate tenor uncertainty. Investor understands path dependency.

**When not appropriate.** Flat curve environment (target never reached). Investor needs predictable investment horizon. Investor who interprets "25% target" as guaranteed (it is conditional).

#### Desk shorthand

*Target coupon on curve slope; auto-redeem at cap.*

---

