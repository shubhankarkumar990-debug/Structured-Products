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
