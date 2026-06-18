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
