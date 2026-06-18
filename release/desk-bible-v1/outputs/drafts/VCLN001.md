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
