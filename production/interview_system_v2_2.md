# Interview System V2.2 — The Complete Structured Products Interview Handbook

**Version**: 2.2
**Date**: 2026-06-26
**Audit**: V2.1 adversarial audit findings + V2.2 ecosystem audit corrections (3 fixes)
**Framework**: v1.3.1 (frozen)
**Coverage**: 49 products × 13 roles × 15 banks × 11 infrastructure domains
**Source Artifacts**: Desk Bible v2 (Parts 0–6), Product DNA Atlas, Solutions Manual, Product Comparison Matrix, Learning Dependency Graph, Product Evolution Map

---

# Part 1: Interview Strategy Guide

## 1.1 How Structured Products Interviews Work

Structured products interviews differ from standard finance interviews. They test the intersection of product knowledge, mathematical intuition, client awareness, operational understanding, and regulatory literacy. No single question has a "right" answer — interviewers assess the depth, structure, and confidence of your reasoning.

**The interview arc across rounds:**

| Round | Format | Duration | What Is Tested | Typical Interviewer |
|:-----:|--------|:--------:|----------------|-------------------|
| Phone Screen | Rapid-fire | 30 min | Elevator definitions, motivation, basic Greeks | HR or junior desk member |
| Technical Round 1 | Product deep-dive | 45–60 min | Product construction, payoff mechanics, risk factors | Associate / VP |
| Technical Round 2 | Infrastructure + desk | 60 min | Conventions, P&L Explain, trade lifecycle, systems | VP / Director |
| Case Study | Scenario analysis | 30–45 min | Client suitability, structuring logic, framework application | VP / Director |
| Desk Round | Real-desk simulation | 60–90 min | Hedging, stress scenarios, market awareness, desk vocabulary | Director / MD |
| Written Assessment | MC + short answer | 60–90 min | Breadth of knowledge, calculation accuracy | Standardized |
| Senior Round | Strategic + behavioural | 45–60 min | Market views, cross-functional awareness, leadership | MD / Head of Desk |

**What distinguishes excellent candidates:**

1. **Tiered depth.** They adjust explanation depth to the interviewer's seniority and the question's scope.
2. **Infrastructure awareness.** They connect products to the operational ecosystem — booking systems, P&L attribution, settlement mechanics, reserve governance.
3. **Framework fluency.** They use structured decision models, not ad hoc reasoning.
4. **Trap recognition.** They identify common misconceptions and explain why the naive answer fails.
5. **Cross-functional vision.** They understand how their role connects to other desk functions.

---

## 1.2 The 4-Tier Answer Framework

Every product question should be answered at the tier appropriate to the context. Using Tier 4 depth for a phone screen wastes time. Using Tier 1 depth for a desk round signals superficiality.

| Tier | Name | Duration | When To Use | What To Include |
|:----:|------|:--------:|-------------|-----------------|
| 1 | Elevator | 30 sec | Phone screen, quick-fire rounds | What it IS, who buys it, one key risk |
| 2 | Technical | 2 min | First-round technical | Construction, Greeks, risk decomposition |
| 3 | Desk | 5 min | Desk round, trading interview | Hedging, systems (NEMO/Sophis/Murex), lifecycle, P&L attribution |
| 4 | Senior | 10 min | Senior round, MD interview | Failure modes, regulatory implications, cross-functional impact, historical precedent |

**Parallel infrastructure tiers:**

| Tier | Product Example | Infrastructure Example |
|:----:|----------------|----------------------|
| 1 | "What is an RC?" | "What is P&L Explain?" |
| 2 | "How is an RC constructed?" | "Walk through the P&L attribution components" |
| 3 | "How do you hedge an RC?" | "You have $500K unexplained — investigation steps?" |
| 4 | "Lehman 2008 — RC impact?" | "IPV shows $2M difference on a CDO tranche — reserve governance?" |

---

## 1.3 Role-Specific Knowledge Depth Matrix

The matrix below shows the expected knowledge depth for each role across product and infrastructure domains. Use it to prioritize your preparation.

**Scale:** ◆◆◆ = Must master | ◆◆ = Must know well | ◆ = Should understand | · = Awareness only

| Domain | Structuring | Trading | Sales | Risk | Model Val | Product Control | Operations | Treasury | Finance | Legal | Compliance | Market Risk | Credit Risk |
|--------|:----------:|:-------:|:-----:|:----:|:---------:|:--------------:|:----------:|:--------:|:-------:|:-----:|:----------:|:-----------:|:-----------:|
| Product construction | ◆◆◆ | ◆◆◆ | ◆◆ | ◆◆ | ◆◆◆ | ◆◆ | ◆ | ◆ | ◆ | · | · | ◆◆ | ◆◆ |
| Greeks & hedging | ◆◆◆ | ◆◆◆ | ◆ | ◆◆◆ | ◆◆◆ | ◆◆ | · | · | · | · | · | ◆◆◆ | ◆◆ |
| Client suitability | ◆◆◆ | ◆ | ◆◆◆ | ◆ | · | · | · | · | · | ◆ | ◆◆◆ | · | · |
| Market conventions (§6.1) | ◆◆ | ◆◆◆ | ◆ | ◆◆ | ◆ | ◆◆◆ | ◆◆◆ | ◆◆ | ◆◆ | ◆ | · | ◆◆ | ◆◆ |
| Termsheet literacy (§6.2) | ◆◆◆ | ◆◆ | ◆◆ | ◆◆ | ◆ | ◆◆ | ◆◆◆ | ◆ | ◆ | ◆◆◆ | ◆◆ | ◆ | ◆ |
| Documentation & legal (§6.3) | ◆◆ | ◆ | ◆ | ◆◆ | · | ◆ | ◆◆ | ◆ | ◆ | ◆◆◆ | ◆◆◆ | ◆ | ◆◆ |
| Credit & capital structure (§6.4) | ◆◆ | ◆◆ | ◆ | ◆◆◆ | ◆ | ◆◆ | ◆ | ◆◆ | ◆◆ | ◆◆ | ◆ | ◆◆ | ◆◆◆ |
| Valuation & fair value (§6.5) | ◆◆ | ◆◆ | · | ◆◆ | ◆◆◆ | ◆◆◆ | · | ◆ | ◆◆◆ | · | · | ◆◆ | ◆ |
| Product control (§6.6) | ◆ | ◆◆ | · | ◆◆ | ◆◆ | ◆◆◆ | ◆ | ◆ | ◆◆◆ | · | · | ◆◆ | ◆ |
| Treasury/XVA (§6.7) | ◆◆ | ◆◆ | ◆ | ◆◆ | ◆ | ◆◆ | · | ◆◆◆ | ◆◆ | · | · | ◆◆ | ◆◆ |
| Model risk (§6.8) | ◆◆ | ◆◆ | · | ◆◆◆ | ◆◆◆ | ◆◆ | · | · | ◆ | · | · | ◆◆◆ | ◆ |
| Operations (§6.9) | ◆ | ◆ | · | ◆ | · | ◆◆ | ◆◆◆ | ◆ | ◆ | ◆ | ◆ | ◆ | ◆ |
| Regulatory (§6.11) | ◆◆ | ◆ | ◆◆ | ◆◆ | ◆ | ◆ | ◆ | ◆◆ | ◆◆ | ◆◆◆ | ◆◆◆ | ◆◆ | ◆◆ |

---

## 1.4 Career-Level Preparation Guide

| Level | Product Focus | Infrastructure Focus | Interview Emphasis |
|-------|-------------|---------------------|-------------------|
| **Graduate / Analyst Y1** | Tier 1-2 for Complexity 2-4 (PPN, RC, IRS, FWD, SD) | Basic conventions (Modified Following, ACT/360), what is a termsheet, trade lifecycle overview | Elevator pitches, payoff diagrams, motivation |
| **Analyst Y2-3** | Tier 1-3 for Complexity 3-6 (Phoenix, CLN, TRS, CDS) | Day count calculations, settlement mechanics, booking basics, ISDA awareness | Product decomposition, comparison pairs, basic hedging |
| **Associate** | Tier 1-3 for Complexity 5-7 (WOAC, VarSwap, FTD, STEG) | P&L Explain basics, CSA mechanics, reserve awareness, FTP concept | Case studies, structuring logic, framework application |
| **VP** | Tier 1-4 for Complexity 6-8 + infrastructure mastery | Full P&L attribution, IPV process, reserve governance, XVA pricing, model validation basics | Desk round depth, cross-functional scenarios, infrastructure calculations |
| **Director** | Tier 4 for Complexity 7-10 + cross-functional | XVA optimization, capital metrics (SA-CCR, RAROC), regulatory strategy, model governance (SR 11-7) | Strategic vision, business economics, regulatory awareness |
| **MD** | All tiers + business strategy | Full business economics: FTP curves, capital optimization, FRTB impact, LCR/NSFR | Market views, P&L management, regulatory engagement, client franchise |

---

## 1.5 Bank-Specific Interview Emphasis

| Bank | Product Strength | Infrastructure Focus | Distinctive Question Types |
|------|-----------------|---------------------|--------------------------|
| **Goldman Sachs** | Equity derivatives, VarSwap, CDO | Mental math, market intuition, strats crossover | "What happened in markets yesterday?", brainteasers, conviction trades |
| **JP Morgan** | Full spectrum, strong credit | P&L Explain always tested, operational rigor | "Walk me through your P&L attribution", trader language |
| **Morgan Stanley** | Structuring, wealth management | Client suitability depth, solutions focus | Bespoke structuring cases, client scenario depth |
| **Barclays** | Credit products, CDS, CLN, CDO | Risk framework depth, stress testing | Credit correlation, risk identification beyond obvious |
| **UBS** | Private banking focus, autocallables | Conservative suitability, Swiss regulatory (FINMA) | Wealth management lens, PPN prominence |
| **BNP Paribas** | European rates, STEG, CMS products | Convention testing (every interview), ACPR/AMF | Modified Following, day count quiz, CMS convexity |
| **Société Générale** | Exotic equity, barrier products | Day count, settlement in every interview | Convention calculation, exotic pricing depth |
| **Deutsche Bank** | Cross-asset, rates | Trade lifecycle (heavily tested), front-to-back | Operations scenarios, booking workflow, reconciliation |
| **Citi** | Markets breadth, credit | Global coverage, EM products | Cross-border regulatory, emerging market cases |
| **HSBC** | FX/treasury, DCI, Asian focus | Settlement, booking, reconciliation | Asia-specific conventions, DCI depth, treasury cases |
| **Nomura** | Autocallables (APAC), ACCUM/DECUM | Asian calendar conventions, T+2 settlement | Phoenix/FCN depth, accumulator mechanics |
| **Credit Agricole** | French rates, covered bonds | European regulatory depth | STEG structuring, rate regime cases |
| **Standard Chartered** | EM credit, FX structured | Cross-border settlement, EM conventions | Emerging market credit cases |
| **MUFG** | Japanese rates, cross-currency | JGB conventions, BOJ policy awareness | XCCY depth, Japanese market specifics |
| **Mizuho** | Japanese structured products | Asian settlement, Samurai bond conventions | Japan-specific regulatory, autocallable variants |

---

# Part 2: Product Answer Library

## How To Use This Section

Each product entry provides tiered answers calibrated to interview depth. The **Top 10** most-interviewed products receive full 4-tier treatment. The **Next 16** receive Tier 1-3. The **Remaining 23** receive Tier 1-2. Every entry includes infrastructure cross-references to Part 6 sections and follow-up question awareness.

Product interview frequency ranking (source: Atlas Appendix G, Matrix View 7):

| Rank | Product | Complexity | Family | Interview Frequency |
|:----:|---------|:----------:|--------|:-------------------:|
| 1 | Reverse Convertible (RC) | 3 | ELN | Very High |
| 2 | Phoenix Autocallable | 6 | ELN | Very High |
| 3 | Interest Rate Swap (IRS) | 3 | Swaps | Very High |
| 4 | Credit Default Swap (CDS) | 5 | Swaps | Very High |
| 5 | Principal Protected Note (PPN) | 2 | ELN | High |
| 6 | Variance Swap (VarSwap) | 7 | Swaps | High |
| 7 | Synthetic CDO Tranche (CDO) | 10 | CLN | High |
| 8 | Worst-of Autocallable (WOAC) | 8 | Other | High |
| 9 | Accumulator (ACCUM) | 6 | Other | Moderate |
| 10 | First-to-Default (FTD) | 7 | CLN | Moderate |

---

## 2.1 Top 10 — Full 4-Tier Treatment

### Product 1: Reverse Convertible (RC)

**Tier 1 — Elevator (30 seconds)**
A Reverse Convertible is a short-term note that pays an above-market coupon. The investor earns the coupon by selling downside protection on a stock — if the stock falls through a barrier, the investor receives depreciated shares instead of their cash back. It is the most common yield-enhancement product in private banking. The key risk is capital loss if the barrier is breached.

**Tier 2 — Technical (2 minutes)**
Construction: Bond (par, short-dated) + Short Put Option (strike at initial level, knock-in barrier typically 60-80%). The put premium funds the enhanced coupon. The investor is economically short a down-and-in put.

Greeks profile: Short delta (below barrier), short vega (rising vol hurts because the embedded put becomes more valuable — the investor sold it), short gamma near the barrier (delta changes rapidly as spot approaches the barrier, creating hedging cost for the desk).

Pricing inputs: underlying spot, implied volatility (most important), barrier level, maturity, risk-free rate, dividend yield, issuer credit spread.

Coupon formula: Coupon ≈ Bond Yield + Put Premium − FTP − Desk Margin. (See §2.2 for construction, §6.7 for FTP methodology.)

**Tier 3 — Desk (5 minutes)**
Hedging: The desk is long the embedded put (bought from the investor). Day-1 hedge: sell delta in the underlying stock, buy gamma/vega protection via listed options if available. Near the barrier, gamma spikes — the desk must rebalance delta frequently, incurring transaction costs. This barrier-proximity hedging cost is the desk's primary risk management challenge.

Systems: Booked in NEMO (book of record for ELN products). Priced and risk-managed in Sophis. Settlement typically T+2, cash or physical delivery. Observation convention (continuous vs discrete barrier) must be specified at booking — see §6.1 for observation conventions, §6.9 for booking workflow.

P&L attribution (§6.6): Delta P&L dominates when spot moves. Vega P&L when vol surface shifts. Theta is positive for the desk (time decay benefits the short-option holder). Near barriers, gamma P&L can dominate. PC runs daily P&L Explain; unexplained >5-10% triggers investigation.

**Tier 4 — Senior (10 minutes)**
Failure mode — Lehman 2008: Lehman Brothers issued RCs. When Lehman defaulted, the capital protection (issuer guarantee) failed. Investors who thought they owned a "safe income product" lost both the stock value AND the issuer's promise. This demonstrated that RC has dual risk: market risk (barrier breach) AND issuer credit risk.

Regulatory dimension: Under MiFID II, RC is classified as a complex product requiring appropriateness assessment. PRIIPs KID must show SRI (typically 5-6 for RC), performance scenarios including stress scenario showing potential loss. The negative target market includes retail clients with no derivatives understanding and low loss tolerance. (See §6.11 for MiFID II product governance.)

Cross-functional impact: Product Control monitors barrier proximity across the RC book — a stock approaching barrier creates concentrated gamma risk. Risk Management sets notional limits per underlying. Operations processes physical delivery if barrier is breached (share settlement via DvP — see §6.9). Treasury charges FTP based on note maturity (see §6.7). Model Validation reviews the barrier adjustment methodology periodically (see §6.8).

Capital consumption: RC generates SA-CCR exposure via the embedded derivative component. The capital charge depends on the maturity, notional, and netting benefits under the ISDA Master Agreement with the hedging counterparty. (See §6.7 for SA-CCR, §6.3 for ISDA netting.)

**Infrastructure cross-references:** §6.1 (barrier observation conventions), §6.2 (termsheet fields), §6.3 (ISDA documentation), §6.5 (IPV for single-stock vol surface), §6.6 (P&L Explain worked example), §6.7 (FTP, XVA charges), §6.8 (Local Vol model validation), §6.9 (booking in NEMO, settlement, corporate action adjustments), §6.11 (MiFID II, PRIIPs KID)

**Follow-up awareness:** "Draw the payoff diagram" (mark barrier, break-even, max loss). "What happens to the desk's hedge when spot is 2% above the barrier?" (extreme gamma). "How does a stock split affect the RC?" (strike and barrier adjusted by split ratio — §6.9 corporate actions).

---

### Product 2: Phoenix Autocallable

**Tier 1 — Elevator (30 seconds)**
A Phoenix pays a conditional coupon — you receive income only if the stock stays above a coupon barrier. If the stock rises above the autocall level, the note redeems early and you get your money back. If the stock crashes through the knock-in barrier, you lose capital. It is the most popular structured product in European and Asian private banking.

**Tier 2 — Technical (2 minutes)**
Construction: Bond + Short Down-and-In Put + Strip of Digital Coupons + Autocall Feature. The digital coupons are conditional on spot > coupon barrier on each observation date. The autocall feature terminates the note when spot ≥ autocall level.

Greeks: Short delta (below knock-in barrier), short vega, short gamma near both barriers (coupon barrier creates digital gamma, knock-in barrier creates put gamma). The autocall feature creates path dependency — the product may terminate early, changing the expected duration.

Memory feature: If the stock drops below the coupon barrier and the coupon is "missed," the memory feature stores the missed coupon. When the stock recovers above the coupon barrier, all accumulated missed coupons are paid at once.

**Tier 3 — Desk (5 minutes)**
Hedging: More complex than RC because of autocall path dependency. Day-1 hedge: delta via underlying, vega via listed options or OTC vol swaps, digital coupon hedged via tight call spreads. The autocall feature changes the product's effective maturity — if the desk hedges for 3 years but the note autocalls in 6 months, the remaining hedge must be unwound.

Pricing model: Local Volatility + Monte Carlo simulation (path-dependent payoff requires simulation). Cannot use closed-form solutions due to autocall feature. Typical: 50,000+ paths for pricing convergence. (See §6.8 for model governance, validation requirements.)

P&L attribution: On autocall observation dates, the autocall probability creates discontinuous P&L. If the stock is 99% of autocall level and rises to 101%, the note autocalls — the desk's entire position terminates, all hedges must be unwound simultaneously. This "autocall event day" creates concentrated P&L and operational activity.

**Tier 4 — Senior (10 minutes)**
The autocall paradox: Autocall benefits the bank, not the investor. The note is recalled precisely when the investor's position is performing well. The investor must then reinvest at lower coupons (because vol has declined in a rising market). This is a critical suitability point — clients who need long-term income should not buy autocallables.

Cross-desk workflow on autocall day: Trading unwinds hedges. Operations processes early redemption and schedules settlement (§6.9). Product Control verifies the final P&L and closes the position (§6.6). Sales notifies the client and discusses reinvestment. Treasury releases the FTP charge on the remaining unfunded period (§6.7).

FTP challenge: An autocallable with 5-year legal maturity but 1.5-year expected life creates an FTP dilemma. Treasury must charge based on expected life, with adjustment for early termination optionality. If the autocall does not trigger, the desk faces higher FTP as the remaining life extends. (See §6.7 FTP methodology.)

**Infrastructure cross-references:** §6.1 (observation conventions, fixing sources), §6.2 (termsheet date fields — 14 date types), §6.5 (Level 2 valuation for index-linked, Level 3 for single-stock bespoke), §6.6 (P&L attribution on autocall dates), §6.7 (FTP expected-life problem), §6.8 (Local Vol Monte Carlo validation), §6.9 (autocall lifecycle event processing, coupon payment workflow), §6.11 (PRIIPs performance scenarios)

---

### Product 3: Interest Rate Swap (IRS)

**Tier 1 — Elevator (30 seconds)**
An IRS exchanges fixed interest payments for floating interest payments on the same notional. No principal changes hands. It is the most liquid derivative in the world — used by every bank, corporation, and government for interest rate hedging. One party pays fixed, the other pays floating (SOFR). Both legs have equal present value at inception.

**Tier 2 — Technical (2 minutes)**
Construction: Fixed leg (pays a fixed rate, typically semi-annual, 30/360 day count) vs floating leg (pays SOFR resets, typically quarterly, ACT/360 day count). The swap rate is set so that NPV = 0 at inception.

The day count convention difference matters: 30/360 on the fixed leg vs ACT/360 on the floating leg means the accrual calculations differ even for the same period. (See §6.1 for day count conventions — the $55,556 difference on $100M illustrative example.)

DV01: The sensitivity to a 1bp rate move. A 30-year IRS has DV01 ≈ $2,500 per bp per $1M notional. On a $10M position, a 100bp rate move creates ~$2.5M MTM exposure despite no principal exchange. (Trap: "No principal at risk means no risk" — FALSE, see Trap TT.9.)

**Tier 3 — Desk (5 minutes)**
Systems: Booked in Murex (book of record for rates products). Cleared through CCP (LCH, CME) for standardized tenors — clearing reduces counterparty credit risk and capital consumption (see §6.11 EMIR clearing obligation). Bilateral for non-standard terms.

Floating rate mechanics: SOFR resets follow specific conventions — fixing lag (typically T-2), compounding methodology (compounded in arrears for SOFR), reset dates, stub periods for non-standard start dates. (See §6.1 floating rate mechanics for the complete treatment including the compounding formula.)

Settlement: Net cash settlement — only the difference between fixed and floating payments is exchanged on each payment date. No DvP required (no securities). Settlement follows the business day convention of the payment currency.

**Tier 4 — Senior (10 minutes)**
LIBOR transition: The transition from LIBOR to SOFR fundamentally changed the IRS market. SOFR is a secured overnight rate (based on Treasury repo), unlike LIBOR (unsecured interbank lending). The credit risk component present in LIBOR is absent from SOFR, creating basis risk for legacy portfolios. Fallback provisions under ISDA's IBOR Fallback Protocol specify how legacy LIBOR trades transition to SOFR + spread adjustment.

Capital impact: Cleared IRS attracts significantly lower capital charges than bilateral IRS under SA-CCR (§6.7). The CCP's default waterfall provides additional protection. FRTB (§6.11) requires desk-level model approval — the rates desk must qualify independently for internal models.

**Infrastructure cross-references:** §6.1 (day count: 30/360 vs ACT/360, SOFR compounding, business day conventions, fixing lag), §6.3 (ISDA Master Agreement, clearing documentation), §6.7 (SA-CCR for capital, netting benefits), §6.9 (booking in Murex, settlement workflow), §6.11 (EMIR clearing obligation, FRTB)

---

### Product 4: Credit Default Swap (CDS)

**Tier 1 — Elevator (30 seconds)**
A CDS is credit insurance. The protection buyer pays a periodic premium (the CDS spread) to the protection seller. If the reference entity defaults, the seller compensates the buyer for the loss. It is the fundamental building block of credit derivatives — used for hedging credit exposure, speculating on credit quality, and constructing complex credit products (CLN, FTD, CDO).

**Tier 2 — Technical (2 minutes)**
Construction: Protection buyer pays fixed premium quarterly (ACT/360, Modified Following). Protection seller pays contingent amount upon credit event: (1 − Recovery Rate) × Notional.

Credit events under ISDA 2014 Definitions: Bankruptcy, Failure to Pay, Restructuring (if applicable — see restructuring clause types below), Governmental Intervention (added for bail-in scenarios). (See §6.4 for detailed restructuring clause treatment.)

CDS spread ≈ PD × (1 − Recovery). Standard recovery assumption: 40% for investment-grade, 25% for high-yield. A 100bp CDS spread with 40% recovery implies ~1.67% annual default probability.

Restructuring clauses (§6.4): Full Restructuring (FR), Modified Restructuring (MR), Modified Modified Restructuring (MMR), No Restructuring (NR). Regional conventions: North America = NR, Europe = MMR (pre-Big Bang), Asia = varies. Getting the clause wrong means the difference between full protection and no protection.

**Tier 3 — Desk (5 minutes)**
Post-2009 Big Bang standardization: Running spread standardized to 100bp (IG) or 500bp (HY) with upfront payment. Auction settlement replaced physical delivery for most CDS. This standardization enabled central clearing of CDS index products.

CDS-bond basis: CDS spread minus asset swap spread. Positive basis = CDS wider than bonds (common pre-crisis). Negative basis = bonds wider than CDS (common during stress). Basis trades exploit this relationship.

Systems: CDS booked in Murex. Index CDS (iTraxx, CDX) cleared through CCP. Single-name CDS typically bilateral with CSA. Trade reporting to repository under EMIR (§6.11).

**Tier 4 — Senior (10 minutes)**
Bail-in risk (§6.4): The 2023 Credit Suisse AT1 write-down showed that regulatory bail-in can impose losses without triggering a traditional CDS credit event. Under NR documentation, a debt restructuring does NOT trigger CDS — an investor hedging via CDS could suffer real losses with no payout. The 2014 ISDA Definitions added "Governmental Intervention" as a credit event specifically for bail-in, but older documentation may not include it.

CVA on CDS positions (§6.7): The bank selling CDS protection faces wrong-way risk — if the reference entity defaults, the bank's exposure increases at precisely the moment when credit markets are stressed. CVA for CDS positions must account for this correlation between counterparty credit and reference entity credit.

**Infrastructure cross-references:** §6.1 (ACT/360, Modified Following for premium payments), §6.3 (ISDA Master Agreement, close-out netting, Big Bang Protocol), §6.4 (restructuring clauses FR/MR/MMR/NR, capital hierarchy, recovery waterfall, AT1/CoCos, bail-in framework, TLAC/MREL), §6.7 (CVA, wrong-way risk), §6.9 (credit event settlement, auction mechanics), §6.11 (EMIR clearing for index CDS, Dodd-Frank)

---

### Product 5: Principal Protected Note (PPN)

**Tier 1 — Elevator (30 seconds)**
A PPN guarantees the return of your principal at maturity while giving you upside participation in a stock or index. Construction: a zero-coupon bond (provides the guarantee) plus a call option (provides the upside). The key risk is issuer credit — if the bank fails, the guarantee fails. The main trade-off is limited participation rate, especially in low-rate environments.

**Tier 2 — Technical (2 minutes)**
Construction: ZCB (cost = e^(-rT)) + Call Option (ATM or OTM). The residual after buying the ZCB funds the call option.

Participation rate calculation: If 3Y ZCB costs $95, desk margin is $1, the remaining $4 buys a call option. If the ATM call costs $12, participation = $4 / $12 = 33%. The investor gets 33% of any upside. In low-rate environments, the ZCB costs more (e.g., $98), leaving only $1 for the call — participation drops to ~8%.

Greeks: Long delta (from the call), long vega (rising vol makes the call more valuable — but the investor already owns it, so rising vol after purchase benefits the investor's mark-to-market), long gamma. Opposite risk profile to RC.

**Tier 3 — Desk (5 minutes)**
Rate sensitivity: PPN economics are dominated by the rate environment. Each 100bp of yield adds approximately 3-5% of participation for a 5-year note. In a 5% rate environment, participation can exceed 100%. In a 0.5% environment, it may be uneconomically low.

Enhancements to improve participation: Add a cap (sell upside above cap → buy more participation below it), use a basket or worst-of underlying (cheaper options → higher participation), extend maturity (cheaper ZCB → more residual), use Asian averaging (cheaper option).

**Tier 4 — Senior (10 minutes)**
PPN vs SD (§6.11): A Structured Deposit wraps the same economics in a deposit format, providing government deposit insurance (up to €100K in EU). For amounts below the insurance limit, SD is strictly superior — the protection comes from the government, not the bank. Above the limit, PPN applies. This distinction is a regulatory knowledge test.

Fair value classification (§6.5): A PPN on a major index is typically Level 2 (observable inputs — liquid index options). A PPN on a bespoke basket of illiquid stocks could be Level 3 (significant unobservable inputs).

**Infrastructure cross-references:** §6.1 (settlement conventions for notes), §6.2 (termsheet fields — issue price, participation rate, cap level), §6.5 (fair value hierarchy classification), §6.7 (FTP impact on participation rate, bond yield component), §6.9 (booking, maturity settlement), §6.11 (PRIIPs KID — SRI typically 2-3 for PPN, deposit insurance for SD variant)

---

### Product 6: Variance Swap (VarSwap)

**Tier 1 — Elevator (30 seconds)**
A variance swap pays the difference between realized variance and a pre-agreed strike variance. It provides pure exposure to volatility — specifically, to the square of volatility. Long variance positions are convex: they benefit disproportionately from large market moves. Short variance positions are the most dangerous short-vol position in the market.

**Tier 2 — Technical (2 minutes)**
Payoff: (σ²_realized − K²) × Vega Notional / (2K). The payoff is in variance (σ²), not volatility (σ). This creates convexity: if vol doubles from 15 to 30, variance quadruples from 225 to 900.

Replication: A variance swap can be replicated by a portfolio of options with weights proportional to 1/K² (inverse strike squared). This replication argument requires: continuous monitoring, no jumps, a complete options market across all strikes. (See §6.8 for model assumptions and limitations.)

Vega notional vs variance notional: Vega notional = the P&L per vol point. Variance notional = Vega notional / (2K). Industry convention quotes in vega notional.

**Tier 3 — Desk (5 minutes)**
Hedging: The desk replicates the VarSwap using a strip of OTC or listed options across strikes, weighted by 1/K². The replication is imperfect because: (a) options exist at discrete strikes, not continuously, (b) deep OTM options may not be available, (c) the market can gap (jumps violate the continuous monitoring assumption).

P&L attribution: Daily VarSwap P&L = (Daily Return²) × Variance Notional. The desk accrues realized variance daily and compares to the strike. Vega P&L captures changes in implied variance. Gamma P&L is significant — VarSwap has positive gamma for long positions (large moves generate positive P&L regardless of direction).

**Tier 4 — Senior (10 minutes)**
Volmageddon — February 2018: XIV (short VIX ETN) lost 96% in a single day when VIX spiked from 14 to 37. The convexity of variance (2× vol → 4× variance) created catastrophic losses for short variance positions. This event demonstrated that short variance has theoretically unlimited, convex loss potential.

Variance risk premium: Implied variance consistently exceeds realized variance — the variance risk premium is positive. This premium compensates sellers of variance for bearing the convexity risk. The premium exists because institutional investors are willing to pay for downside protection, creating systematic demand for long-vol positions.

**Infrastructure cross-references:** §6.1 (observation conventions — continuous monitoring vs discrete), §6.5 (Level 2 for index VarSwap, Level 3 for single-stock long-dated), §6.6 (P&L attribution — gamma P&L dominant on large move days), §6.8 (replication model validation — 1/K² weighting, jump risk, discrete strike limitations)

---

### Product 7: Collateralized Debt Obligation (CDO)

**Tier 1 — Elevator (30 seconds)**
A CDO tranches the credit risk of a portfolio of 100+ names into layers with different risk and return profiles. The equity tranche absorbs first losses, the mezzanine takes middle losses, and the super-senior is protected by all layers below. It is the most complex product in the universe (Complexity 10) and the product most associated with the 2008 financial crisis.

**Tier 2 — Technical (2 minutes)**
Tranching: Equity (0-3% attachment), Mezzanine (3-7%, 7-10%, 10-15%), Senior (15-30%), Super-Senior (30-100%). Each tranche absorbs losses in order. The equity tranche investor loses first dollar — their coupon is highest to compensate.

Correlation sensitivity: The most critical concept. High correlation → defaults cluster → either everyone defaults (bad for senior) or nobody defaults (good for equity). Low correlation → defaults are independent → first-loss probability is higher (bad for equity) but catastrophic loss is lower (good for senior). Mezzanine tranche is MOST sensitive to correlation assumptions.

Pricing model: Gaussian copula with base correlation. Base correlation replaced compound correlation because compound correlation could produce multiple solutions (non-monotonic) while base correlation is monotonic. Known limitation: Gaussian copula underestimates tail dependence. (See §6.8.)

**Tier 3 — Desk (5 minutes)**
Product Control challenge (§6.6): CDO tranches are almost always Level 3 in the fair value hierarchy. IPV requires: broker quotes (limited availability), model comparison (Gaussian vs Student-t copula), parameter uncertainty assessment (correlation reserve). The model reserve for CDO positions can be very material — a 5% correlation shift can change tranche values by millions.

Reserve framework: CDO positions attract multiple simultaneous reserves — bid-offer reserve (wide spreads), model reserve (copula uncertainty), correlation parameter reserve, liquidity reserve (large positions relative to market depth), and potentially Day One P&L deferral for bespoke tranches. (See §6.6 reserve framework.)

**Tier 4 — Senior (10 minutes)**
2008 failure analysis: The Gaussian copula underestimated tail dependence — defaults were more correlated in stress than the model predicted. But the model was used despite known limitations because: (a) computationally tractable, (b) market standard (prices quoted in implied correlation), (c) regulatory accepted. The failure was in model governance — using the model as truth rather than approximation — not in the mathematics itself. (See §6.8 for the nuanced treatment of model limitations vs model governance.)

Regulatory capital: CDO positions consume significant capital under both SA-CCR and FRTB. The correlation trading book has specific capital requirements. Banks that cannot qualify for internal models under FRTB must use the standardised approach, which penalizes correlation products heavily. (See §6.7 for capital framework, §6.11 for FRTB.)

**Infrastructure cross-references:** §6.4 (capital hierarchy — CDO tranching mirrors corporate capital structure), §6.5 (Level 3 classification, Day One P&L deferral), §6.6 (multiple simultaneous reserves, model reserve calculation, correlation parameter reserve), §6.7 (capital consumption, KVA for CDO positions), §6.8 (Gaussian copula limitations, challenger models — Student-t copula, model inventory rating: HIGH), §6.11 (Basel capital for correlation book, FRTB desk-level qualification)

---

### Product 8: Worst-of Autocallable (WOAC)

**Tier 1 — Elevator (30 seconds)**
A WOAC is a Phoenix autocallable on a basket of stocks where the WORST-performing stock drives all outcomes — coupons, autocall, and barrier breach. The coupon is much higher than single-stock Phoenix (typically 18-25% vs 10-15%) because the investor is selling correlation risk. Diversification HURTS the WOAC investor — more stocks means more chances for one to crash.

**Tier 2 — Technical (2 minutes)**
The correlation mechanism: In a single-stock Phoenix, barrier breach probability = P(stock < barrier). In a WOAC with N independent stocks, barrier breach probability ≈ 1 − (1−P)^N — dramatically higher. When correlation is high (stocks move together), the basket behaves like a single stock and the extra coupon is "free." When correlation breaks down (one stock crashes alone), the worst-of mechanism triggers on full notional.

The investor is **long** correlation (MTM convention): they benefit from high correlation (stocks move together, reducing worst-of risk) and lose from low correlation (independent moves increase the chance of one stock hitting the barrier). The investor is *structurally* short — they sold the correlation premium embedded in the worst-of basket coupon.

Greeks (the desk's raw risk profile, the mirror of the investor): same as Phoenix (short delta, short vega, short gamma near barriers) PLUS short correlation on a **raw** basis — the desk's raw worst-of position is short correlation, while the investor is **long** correlation under the MTM convention (see the line above). After dispersion hedging the desk's net correlation is smaller. Correlation is not directly observable and is the primary model risk. (See §6.8 for correlation modeling limitations.)

**Tier 3 — Desk (5 minutes)**
Hedging: Single-stock hedges for each underlying PLUS correlation hedging. Correlation cannot be perfectly hedged — the desk manages it through portfolio construction, dispersion trades, and model reserves. If one stock drops sharply while others are unchanged, implied correlation drops and the WOAC position loses (the correlation risk materializes).

Product Control (§6.6): WOAC positions require: vol surface IPV per underlying (multiple surfaces to verify), correlation verification (implied from basket option prices, limited observability), model reserve for correlation uncertainty (+/- 5% correlation shift can move P&L by millions). PC monitors barrier proximity on the WORST-performing stock — one stock near barrier means the entire position is at risk.

**Tier 4 — Senior (10 minutes)**
The diversification trap: A client says "I chose 5 blue-chip Swiss stocks for my WOAC because diversification protects me." Correct response: In a WOAC, diversification INCREASES risk. Each additional stock is another potential barrier breach. The worst-of mechanism converts portfolio diversification into concentration risk on the weakest name. The coupon compensates for this — but clients rarely understand the mechanism.

Suitability challenge: WOAC (Complexity 8) is at the boundary of Private Banking suitability (cap = 8 under the persona framework). A structurer must verify the client's correlation understanding before proceeding. SM AP-7 documents this anti-pattern. (See Solutions Manual scenarios for full guidance.)

**Infrastructure cross-references:** §6.1 (observation conventions — worst-of checked on each underlying separately), §6.5 (Level 2 if on liquid indices, Level 3 for single-stock bespoke basket), §6.6 (correlation parameter reserve, barrier proximity monitoring per underlying, PC by product family table), §6.7 (CVA considerations — WOAC counterparty exposure), §6.8 (correlation modeling: Gaussian copula, Local Vol + MC, challenger: Stochastic Vol + MC), §6.9 (corporate action on one basket constituent — strike/barrier adjustment per §6.9 methodology)

---

### Product 9: Accumulator (ACCUM)

**Tier 1 — Elevator (30 seconds)**
An Accumulator obliges the investor to buy a fixed quantity of shares daily at a discount to the market — as long as the stock stays above the strike. If the stock rises above a knock-out barrier, the contract terminates (the investor stops accumulating). If the stock falls below the strike, the investor must buy at 2× the daily quantity at the strike price — accumulating shares at a price above the market. The 2× gearing below strike is what makes accumulators dangerous.

**Tier 2 — Technical (2 minutes)**
Construction: Strip of daily forward purchases at a discount + Knock-Out barrier (upside cap) + 2× Gearing below strike. The investor is economically long a strip of forward contracts with an embedded short put (below strike, at 2× notional) and a short call (the KO feature).

The name in Hong Kong: "I kill you later" — because the gearing below strike forces the investor to buy declining shares at an above-market price, with double the quantity. In the 2008 Hong Kong market crash, ACCUM losses for high-net-worth clients were catastrophic.

**Tier 3 — Desk (5 minutes)**
Daily settlement complexity: Each business day, the fixing is checked. Above strike but below KO: investor buys the standard daily quantity. Below strike: investor buys 2× the daily quantity. Above KO: contract terminates. This creates daily operational workflow — fixings, settlement instructions, quantity calculations. (See §6.9 for daily lifecycle event processing.)

**Tier 4 — Senior (10 minutes)**
Regulatory scrutiny: Post-2008, regulators in Hong Kong (SFC) and Singapore (MAS) imposed enhanced suitability requirements for accumulators. The gearing feature and daily settlement obligation make this product unsuitable for clients without significant liquid wealth and risk tolerance. The 2008 losses led to multiple lawsuits and regulatory sanctions.

**Infrastructure cross-references:** §6.1 (daily fixing conventions, business day calendar for daily accumulation), §6.2 (termsheet fields — daily quantity, gearing ratio, KO level), §6.9 (daily operational processing — fixing, quantity calculation, settlement), §6.11 (SFC/MAS enhanced suitability requirements)

---

### Product 10: First-to-Default (FTD)

**Tier 1 — Elevator (30 seconds)**
An FTD basket provides credit exposure to 5-10 names where the FIRST default in the basket triggers the payout. The investor sells protection on the first default — if any name defaults, the investor takes the loss on that name's notional. The coupon is high because the probability of at least one default in a basket is much higher than the probability of any single default.

**Tier 2 — Technical (2 minutes)**
Correlation sensitivity — the deepest concept in credit: FTD is LONG correlation. Low correlation → defaults are independent → probability of at least one default = 1 − Π(1−PD_i) → HIGH. High correlation → defaults cluster → either all default or none → probability of exactly ONE default DECREASES. The FTD investor benefits from high correlation.

This is counterintuitive: in equity portfolios, low correlation = diversification = good. In FTD, low correlation = independent defaults = higher probability of at least one default = BAD for the protection seller.

**Tier 3 — Desk (5 minutes)**
Pricing model: Basket copula (Gaussian or Student-t) with pairwise correlations. CDS spreads for each reference entity provide the marginal default probabilities. The copula combines them into joint default probabilities. The base correlation methodology (§6.6, §6.8) determines the implied correlation from market prices.

The FTD ≈ CDO equity tranche analogy: An FTD on 5 names is economically similar to the equity tranche of a mini-CDO with 0% attachment. Both absorb first losses. Both are long correlation.

**Tier 4 — Senior (10 minutes)**
NTD comparison: NTD (Nth-to-Default) has OPPOSITE correlation sensitivity — it is SHORT correlation. High correlation → defaults cluster → if N defaults occur, they are more likely to occur together → NTD risk increases. This reversal is the hardest concept in credit derivatives and the most tested in interviews.

Recovery rate sensitivity (§6.4): FTD payout = (1 − Recovery) × Notional. Standard assumption of 40% recovery may be far from actual. Lehman recovery: ~8.6%. The difference between 40% assumed and 8.6% actual on a $10M FTD is $3.14M of unexpected loss.

**Infrastructure cross-references:** §6.3 (ISDA credit event definitions, Big Bang Protocol auction settlement), §6.4 (restructuring clauses — FR/MR/MMR/NR directly affect whether a debt restructuring triggers FTD payout, recovery waterfall, capital hierarchy), §6.5 (Level 3 — correlation is unobservable), §6.6 (correlation parameter reserve, model reserve for copula choice), §6.7 (CVA — wrong-way risk if counterparty and basket names are correlated), §6.8 (Gaussian copula limitations, challenger: Student-t copula, model inventory: HIGH risk rating)

---

## 2.2 Next 16 — Tier 1-3 Treatment

### DRC (Discount Reverse Convertible) — Complexity 3
**Tier 1:** Same risk as RC, different return mechanism. Instead of receiving a coupon, the investor buys the note at a discount (e.g., $92 for a note redeemable at $100). The discount IS the option premium.
**Tier 2:** Construction: Discounted bond + short put. Break-even is lower than RC because the entry price is below par. Economic equivalence to RC with different cash flow timing.
**Tier 3:** Hedging identical to RC. Booking difference: issue price ≠ 100%. Operations must track the discount amortization schedule. (§6.6: P&L attribution includes the discount accretion as Theta-equivalent.)

### KODRC (Knock-Out Discount RC) — Complexity 4
**Tier 1:** A DRC with added downside protection via a knock-out barrier. If the stock drops through the KO barrier, the put option is extinguished and the investor is protected. Higher protection = lower discount.
**Tier 2:** Construction: Discount bond + short down-and-out put. The KO feature modifies the embedded put — it is extinguished if the stock drops through the barrier. Above the KO level: investor is exposed to downside (put is live). Below the KO level: put is extinguished, investor is protected.
**Tier 3:** Barrier observation convention critical (§6.1) — continuous vs discrete monitoring produces materially different pricing.

### CRC (Callable Reverse Convertible) — Complexity 5
**Tier 1:** An RC where the bank has the right to call (redeem early). The bank calls when the product is performing well for the investor — higher coupon compensates for this adverse optionality.
**Tier 2:** Contains a Bermudan call option sold by the investor to the bank. Coupon is higher than standard RC because the investor has sold two options (the put AND the call right).
**Tier 3:** Autocall-like operational complexity — the bank must decide on each call date whether to exercise. P&L attribution includes the call option value decay. (§6.9: lifecycle event processing for issuer call.)

### Airbag Certificate — Complexity 4
**Tier 1:** Leveraged upside participation with capital protection down to a barrier. Above barrier: full upside. Below barrier: loss. The leverage comes from selling the downside below the barrier to fund leveraged upside.
**Tier 2:** Construction: ZCB + leveraged call spread. The leverage ratio typically 1.5-2×. Capital protection only applies above the barrier.
**Tier 3:** Hedging requires managing leveraged delta above barrier. Digital risk at barrier level.

### FCN (Fixed Coupon Note) — Complexity 6
**Tier 1:** Like a Phoenix but with GUARANTEED coupon — paid regardless of where the stock trades. Same capital risk as Phoenix (barrier breach = capital loss). The guaranteed coupon means lower rate (5-8% vs Phoenix 10-15%).
**Tier 2:** The coupon difference = option value. Phoenix desk has the right to not pay the coupon (digital option). FCN removes that optionality — the investor always gets paid — so the coupon is lower. For clients needing predictable cash flow: FCN strictly better. For clients tolerating uncertainty for higher expected return: Phoenix better.
**Tier 3:** Simpler P&L attribution than Phoenix — no conditional coupon digital. Operations: guaranteed coupon payments scheduled at booking (§6.9).

### CRA ELN (Conditional Range Accrual ELN) — Complexity 6
**Tier 1:** Coupon accrues proportionally based on how many days the underlying stays within a defined range. 60 days in range out of 90 total = coupon × (60/90) = 66.7% of maximum coupon. Differs from Phoenix (all-or-nothing) by providing proportional payout.
**Tier 2:** Construction: Bond + strip of daily digital options. Each day is a binary observation — in range or out. The coupon accumulates proportionally. Greeks: short vega (each daily digital is short vol), concentrated gamma at range boundaries.
**Tier 3:** Operational complexity: daily fixing required (§6.9). Each business day, Operations records whether the underlying is within the range. At coupon date, the ratio of in-range days to total observation days determines the coupon. Systems must track the running count. Day count convention (§6.1) applies to the accrual calculation.
**Infrastructure cross-references:** §6.1 (daily observation, business day calendar determines total observation days), §6.2 (termsheet: range boundaries, observation convention), §6.9 (daily fixing workflow)

### Digital Coupon Note — Complexity 4
**Tier 1:** Pays a fixed digital coupon if the underlying is above/below a strike on the observation date. All-or-nothing — no proportionality.
**Tier 2:** The hedging nightmare: near the digital strike, delta is theoretically infinite (step function). Dealers replicate with tight call spreads, but replication is imperfect. The tighter the spread, better replication but larger gamma.
**Tier 3:** P&L attribution on observation dates is discontinuous — similar to autocall event days. (§6.6: large unexplained risk on digital observation dates.)

### Booster Note — Complexity 4
**Tier 1:** Leveraged participation below a cap. 200% participation up to cap, then 1× (unleveraged) above cap — the extra call and short call offset, leaving only the underlying position. Leverage comes from selling upside above cap.
**Tier 2:** Construction: Underlying + extra call (for leverage) − call at cap (sold to fund leverage). Net: 2× exposure up to cap, 1× above.
**Tier 3:** Cap creates a discontinuity in delta at the cap level.

### DKIP (Down-and-Knock-In Put) — Complexity 7
**Tier 1:** Three barriers: autocall barrier (upside), coupon barrier (conditional income), knock-in barrier (capital risk). Most feature-rich ELN variant.
**Tier 2:** Combines autocall + conditional coupon + KI put in a single note. Each barrier creates its own delta/gamma profile.
**Tier 3:** Most operationally complex ELN — three separate barrier monitoring requirements (§6.9, §6.1 observation conventions).

### TRS (Total Return Swap) — Complexity 5
**Tier 1:** Synthetic ownership — one party receives the total return (price change + dividends) of an asset and pays a funding rate (SOFR + spread). No physical ownership changes. Used for: leveraged exposure, short selling, regulatory capital optimization.
**Tier 2:** Multi-asset: can reference equity, credit, loans, or any asset class. Unlike EqSwap (equity only), TRS covers any underlying.
**Tier 3:** Settlement: periodic cash settlement of total return vs funding. Dividend handling critical for equity TRS (§6.9 corporate actions).

### EqSwap (Equity Swap) — Complexity 5
**Tier 1:** A TRS restricted to equity underlyings. Cash-settled, typically on indices. Used for synthetic index exposure without physical ownership.
**Tier 2:** Economically equivalent to borrowing money, buying the index, and paying SOFR + spread. The desk provides the leverage.
**Tier 3:** Special dividend impact (§6.9): unexpected dividends affect each leg differently — the total return leg receives the dividend, but the pricing assumed a lower dividend forecast.

### XCCY (Cross-Currency Swap) — Complexity 5
**Tier 1:** Exchanges cash flows in two different currencies. Unlike IRS, XCCY exchanges principal at inception and maturity. Used by corporates to convert debt from one currency to another.
**Tier 2:** The cross-currency basis exists because the cost of borrowing USD via FX swaps differs from the direct USD borrowing rate. This basis reflects supply/demand imbalances in the FX swap market.
**Tier 3:** Operations: settlement in two currencies on each payment date, principal exchange at maturity (§6.9). FTP charge applies to both currency legs (§6.7).

### IR Callable Note — Complexity 5
**Tier 1:** A rate-linked note with an enhanced coupon funded by selling a call right (swaption) to the bank. Bank calls when rates move favorably for the bank — leaving the investor with reinvestment risk. Enhanced coupon = vanilla yield + swaption premium − FTP − margin.
**Tier 2:** Embedded Bermudan swaption. The extra coupon (e.g., 5% vs 3% vanilla) = the value of the swaption the investor has sold. The bank exercises when rate conditions make the note expensive for the bank to maintain.
**Tier 3:** Model: Hull-White (1- or 2-factor) for swaption valuation. Mean reversion parameter is unobservable — a key source of model risk. (§6.8: parameter uncertainty reserve for mean reversion.)

### V. STEG (Vanilla Steepener) — Complexity 5
**Tier 1:** Coupon = leverage × (CMS Long Rate − CMS Short Rate), floored at zero. Pays when the yield curve is steep. Zero coupon when the curve is flat or inverted.
**Tier 2:** CMS convexity adjustment: CMS rate > forward rate due to Jensen's inequality (§6.1 for CMS convexity). This adjustment is model-dependent and is the largest source of STEG pricing risk. A 10-20bp adjustment on long-dated STEG is common.
**Tier 3:** Product Control (§6.6): Curve steepness sensitivity — small changes in 2s10s or 2s30s spread create large P&L impact. Rate-rate correlation between tenors is not independently observable. Model reserve for lambda (mean reversion) parameter uncertainty.

### NTD (Nth-to-Default) — Complexity 8
**Tier 1:** Like FTD but triggers on the Nth default, not the first. Protected by the first N-1 defaults — the investor only loses when N or more names default. Lower coupon than FTD but different correlation exposure.
**Tier 2:** Correlation reversal: NTD is SHORT correlation (opposite of FTD). High correlation → defaults cluster → if one defaults, others likely follow → probability of N defaults INCREASES → NTD risk rises. Low correlation → defaults are independent → probability of N defaults is low → NTD risk decreases.
**Tier 3:** The FTD-NTD pair is the most tested correlation concept in credit interviews. A candidate who memorizes "FTD long corr, NTD short corr" without understanding the mechanism will fail follow-ups. (See §6.4 for full treatment, Pair 4 in Part 4.)

### TARN STEG (Target Redemption Steepener) — Complexity 8
**Tier 1:** A steepener note that terminates when cumulative coupons reach a target amount. If the curve steepens early, coupons accumulate quickly and the note redeems — the investor gets their target but must reinvest at prevailing rates (reinvestment risk). If the curve flattens, zero coupons accrue and the note persists for its full term.
**Tier 2:** Path-dependent: the cumulative coupon at each observation depends on the entire history of CMS spread observations. Requires Monte Carlo simulation. Pricing model: 2-factor Hull-White to capture stochastic spread dynamics (§6.8).
**Tier 3:** PC challenge (§6.6): The uncertain maturity creates FTP difficulty (§6.7). TARN expected life is model-dependent. Model Validation (§6.8) must verify that the target probability is correctly estimated — 500 Monte Carlo paths is insufficient (minimum 10,000+, ideally 50,000+).

---

## 2.3 Remaining 23 — Tier 1-2 Treatment

Each entry provides Tier 1 elevator pitch and Tier 2 technical construction with infrastructure cross-references.

**VLSP (Vanilla Leveraged Swap Product) — Complexity 2:** IRS with features (caps, floors, amortization). Used for bespoke cash flow matching. Atlas complexity 2 but less liquid than IRS (3) in practice. §6.1: non-standard day count and payment schedules.

**FWD (Forward) — Complexity 2:** Agreement to buy/sell at a fixed price on a future date. Forward price = Spot × e^(r-q)T. Reflects carry cost, NOT a forecast. §6.1: settlement conventions, §6.9: settlement workflow.

**SD (Structured Deposit) — Complexity 2:** Same economics as PPN (ZCB + call) wrapped in a deposit. Deposit insurance applies (up to €100K in EU). Strictly superior to PPN below the insurance limit. §6.11: PRIIPs KID required for SD.

**VO (Vanilla Option) — Complexity 3:** Standard call/put. OTC or exchange-traded. Foundation of all options-based products. Five pricing inputs (spot, strike, vol, rate, time). §6.8: Black-Scholes model limitations for exotic products.

**Warrant — Complexity 3:** Exchange-listed option for retail investors. Same economics as VO but with retail wrapper, smaller denominations, and exchange liquidity. Time decay accelerates near expiry.

**ELO (Equity-Linked Option) — Complexity 3:** VO wrapped in a retail note format. No economic difference from VO — only packaging. Retail-accessible, small denominations.

**CommSwap (Commodity Swap) — Complexity 4:** Exchanges fixed commodity price for floating market price. Basis risk (hedge vs actual commodity grade/location) is the key risk. §6.1: commodity day count conventions.

**CLN (Credit-Linked Note) — Complexity 4:** Funded credit exposure. Investor buys a note whose principal is at risk if the reference entity defaults. Dual credit risk: reference entity + note issuer. Coupon > CDS spread because the desk receives the funding benefit. §6.3: ISDA confirmation matching, §6.4: recovery waterfall determines loss severity, §6.7: FTP + XVA on the funded position.

**Skew CLN — Complexity 5:** CLN where the payout depends on actual recovery rate rather than a fixed digital payout. If recovery = 30%, investor loses 70%. If recovery = 60%, investor loses 40%. More precise credit exposure. §6.4: recovery rate variability by seniority.

**Bonus Note — Complexity 4:** Guaranteed minimum return (bonus level) unless a barrier is breached during the observation period. If barrier is never breached: investor receives at least the bonus return. If breached: bonus is lost, investor receives underlying performance. Flash crash risk: a 5-second intraday barrier touch destroys the bonus.

**ICN (Issuer Callable Note) — Complexity 3:** A note where the bank can call at par on predetermined dates. The investor receives a higher coupon in exchange for the call risk. The call benefits the BANK, not the investor. §6.9: lifecycle event processing for issuer call.

**Opt-on-RC (Option on Reverse Convertible) — Complexity 5:** An option that gives the holder the right to enter into an RC at a future date. Two decision points: (1) exercise the option (2) the RC's own barrier observation. Useful for tactical positioning.

**DECUM (Decumulator) — Complexity 6:** Mirror of ACCUM. The investor SELLS shares at a premium daily. Below strike: sells standard quantity. Above strike: sells 2× quantity at below-market price. Used by corporate insiders for structured share disposal. §6.11: insider trading considerations, compliance constraints.

**DCI (Dual Currency Investment) — Complexity 3:** FX-linked yield enhancement. Investor deposits in one currency, sells a put on a currency pair. If the exchange rate moves against the investor, principal is converted at the strike rate. Same mechanism as RC but in FX. §6.1: FX settlement conventions (T+2 standard).

**SHRK (Shark Fin Note) — Complexity 4:** PPN with a knock-out barrier on the upside. Participation in underlying gains up to the KO barrier. If the underlying rallies through the barrier, the participation is capped or reduced. Higher participation than plain PPN (the KO finances additional leverage) but return is capped.

**SNOW (Snowball Autocallable) — Complexity 7:** Phoenix variant where missed coupons ACCUMULATE multiplicatively. If the stock recovers, ALL accumulated coupons are paid at once. Recovery payout is much larger than Phoenix (where missed coupons are simply lost unless memory feature applies). Snowball = full cumulative payout.

**CLIQ (Cliquet Note) — Complexity 7:** Periodic returns are individually capped and floored, then summed. Local caps make the product underperform in trending markets but protect in volatile markets. The ratchet "locks in" periodic gains. §6.2: termsheet field — local cap, local floor, global floor.

**ZCL (Zero-Coupon Linker) — Complexity 4:** A zero-coupon bond with payout linked to an index at maturity. Duration is very high (no coupons to reduce duration). A 30-year ZCL moves roughly 25-30× more per basis point than a 1-year bond. §6.1: day count for accrual calculation.

**NCRA (Non-Callable Range Accrual) — Complexity 6:** Rate-linked range accrual — coupon accrues only when a reference rate stays within a range. If rates leave the range permanently in year 1 of a 10-year note, the investor receives zero coupon for the remaining 9 years. §6.1: rate fixing conventions, §6.6: P&L attribution for range accrual books.

**CRA SRT (Callable Range Accrual SRT) — Complexity 7:** NCRA plus bank call right. Two risks sold simultaneously: range risk (coupon depends on rates staying in range) + call risk (bank terminates when conditions favor the investor). §6.8: model risk — requires rate model calibration for both range and call.

**Digital CF (Digital Coupon Flow) — Complexity 5:** Binary coupon paid if a rate condition is met. Same hedging nightmare as equity digital (delta theoretically infinite at strike) but in rate space. §6.1: rate fixing source, §6.6: P&L attribution discontinuity on observation dates.

**RA STEG (Range Accrual Steepener) — Complexity 7:** STEG with range accrual — coupon accrues only when CMS spread AND a rate condition are simultaneously met. Two conditions: (1) curve steepness, (2) rate level. Requires BOTH to earn coupon.

**C. STEG (Callable Steepener) — Complexity 6:** V. STEG plus bank call right. Bank calls when curve steepens — precisely when the investor's coupon is highest. Worst timing for investor. Higher coupon compensates.

---

# Part 3: Infrastructure Answer Library

This section covers the 11 infrastructure domains from Part 6 of the Desk Bible, reformatted as interview-ready answers using the 4-tier framework.

## 3.1 Market Conventions (§6.1)

### Business Day Conventions

**Tier 1:** Business day conventions determine what happens when a payment or observation date falls on a weekend or holiday. The four main conventions are Following, Modified Following, Preceding, and No Adjustment.

**Tier 2:** Modified Following is the most important: move to the next business day, UNLESS doing so crosses a month boundary — in which case, move BACKWARD to the previous business day. This "do not cross the month" rule prevents a January payment from shifting into February, which would affect accrual calculations.

Example: Payment due Saturday, January 31. Following → Monday, February 2 (crossed month boundary). Modified Following → Friday, January 30 (moved backward to stay in January). The difference affects accrual period length, which affects the payment amount on large notionals.

**Tier 3:** Calendar conventions compound the complexity. A "London + New York" calendar means the date must be a business day in BOTH cities. A "London OR New York" calendar means the date is valid if EITHER city is open. The wrong calendar selection at booking (§6.9) can shift every payment date in a 30-year swap. Fixing lag conventions (T-2 for SOFR) interact with business day conventions — the fixing date and the payment date may reference different calendars.

**Tier 4:** Calendar disputes between counterparties are resolved by reference to the ISDA Master Agreement Schedule (§6.3), which specifies the governing calendar. If the Schedule is ambiguous, the calculation agent (typically the bank) determines the appropriate calendar. This determination power is a significant privilege — and a significant responsibility.

### Day Count Conventions

**Tier 1:** Day count conventions determine how interest accrues between two dates. Different conventions give different numbers for the same period, creating real dollar differences on large notionals.

**Tier 2:** The four main conventions:
- **ACT/360:** Actual days / 360. Common for money markets, SOFR floating legs. Produces higher accrual than ACT/365 for the same rate because the denominator is smaller.
- **ACT/365 (Fixed):** Actual days / 365. Common for GBP.
- **30/360:** Assumes 30 days per month, 360 per year. Common for fixed legs of USD swaps, Eurobonds. Simplifies calculations but diverges from actual calendar.
- **ACT/ACT:** Actual days / actual days in the coupon period (or year). Most accurate. Used for government bonds.

**Tier 3:** Worked example — the $16,667 difference: $100M notional, 6% annual rate, semi-annual coupon, accrual period January 15 to July 15 (181 actual days).
- ACT/360: $100M × 6% × (181/360) = **$3,016,667**
- 30/360: $100M × 6% × (180/360) = **$3,000,000**
- Difference: **$16,667** per coupon period. Over 10 years (20 coupons): **$333,340**. On a $1B notional: **$3.3M** total difference from the choice of day count convention alone.

This is not a rounding error. Misapplying the convention at booking (§6.9) creates a cash reconciliation break (§6.9) that will persist for the life of the trade.

**Tier 4:** Day count convention selection is specified in the termsheet (§6.2) and confirmed in the ISDA confirmation (§6.3). If the booking system (NEMO/Murex) applies a different convention than what the confirmation specifies, every coupon payment will be wrong. This is one of the most common sources of trade breaks and reconciliation failures.

### Settlement Conventions

**Tier 1:** Settlement lag is the time between trade date and settlement date. Standard: T+2 for most products. DvP (Delivery versus Payment) ensures securities and cash exchange simultaneously.

**Tier 2:** Settlement types by product family: ELN = cash or physical delivery. Swaps = net cash settlement. CLN = cash (no credit event) or physical delivery of reference obligation (credit event). Physical settlement after barrier breach means the investor receives depreciated shares — Operations must arrange DvP through the CSD (§6.9).

### Floating Rate Mechanics

**Tier 1:** SOFR (Secured Overnight Financing Rate) is the standard USD floating rate, replacing LIBOR. It is a secured overnight rate based on Treasury repo transactions.

**Tier 2:** SOFR compounding: For swap floating legs, SOFR is compounded in arrears over the interest period. The compounding formula accumulates daily SOFR fixings over the period, applying compound interest. The fixing lag (typically T-2) means the rate for day T is fixed 2 business days prior. Stub periods occur when the trade start date does not align with the standard roll date. (See §6.1 for the complete compounding formula and end-of-month rule.)

---

## 3.2 Termsheet Literacy (§6.2)

**Tier 1:** A termsheet is the architectural blueprint of a structured product. Every field specifies a precise measurement. Misreading a single field can change the product's economics entirely.

**Tier 2:** Key field categories:
- **Date fields (14 types):** Trade date, booking date, effective date, issue date, settlement date, maturity date, observation dates, valuation date, determination date, fixing dates, reset dates, roll dates, payment dates, record date, ex-date. Each serves a distinct purpose — confusing trade date (when terms are agreed) with effective date (when economics begin) is a common error.
- **Economics fields:** Notional, issue price (clean vs dirty — see §6.1), strike, barrier(s), participation rate, cap, floor, coupon rate, funding spread.
- **Convention fields:** Day count, business day convention, settlement lag, observation convention (continuous/discrete/periodic), fixing source.
- **Legal fields:** Calculation agent, governing law, ISDA definitions reference, market disruption provisions, corporate action adjustment method.

**Tier 3:** Six common termsheet misreading mistakes (§6.2):
1. Confusing issue price (what the investor pays) with redemption price (what the investor receives)
2. Missing the difference between observation date (when fixing occurs) and payment date (when cash settles)
3. Ignoring the business day convention on payment dates — a Saturday payment shifted to Monday changes the accrual
4. Assuming continuous barrier observation when the termsheet specifies discrete (or vice versa)
5. Not checking whether the barrier is on closing price or intraday (continuous monitoring requires different systems setup — §6.9)
6. Confusing accrued interest with clean/dirty price conventions

**Tier 4:** The calculation agent clause is critically important and often overlooked. The calculation agent (typically the bank) has discretion in certain determinations — market disruption fallback, corporate action adjustment methodology, "good faith" price estimates when observable prices are unavailable. This discretion is governed by a reasonableness standard but gives the bank significant power. Investors should understand who the calculation agent is and what decisions they can make unilaterally.

---

## 3.3 Documentation & Legal (§6.3)

**Tier 1:** The ISDA Master Agreement is the standard contract governing OTC derivatives. It establishes the legal framework for what happens when things go wrong — default, market disruption, force majeure.

**Tier 2:** Key components:
- **Master Agreement:** Standard terms (events of default, termination events, close-out netting, payment netting). Rarely modified.
- **Schedule:** Customizes the Master Agreement for each counterparty relationship. Specifies governing law, netting provisions, additional termination events.
- **CSA (Credit Support Annex):** Governs collateral. Key terms: Threshold (unsecured exposure allowed before collateral is posted), Independent Amount (additional collateral buffer), MTA (Minimum Transfer Amount — transfers below this are not required), eligible collateral (cash, government bonds with haircuts), valuation agent, dispute resolution.

**Tier 3:** CSA worked example: Threshold = €10M, MTA = €500K. Current exposure = €12M. Required collateral = €12M − €10M = €2M. If exposure were €10.3M: required = €10.3M − €10M = €300K, but €300K < MTA (€500K), so NO collateral is posted. The MTA creates a gap — exposures between Threshold and Threshold + MTA are uncollateralized.

Close-out netting (§6.3): Upon default, all trades are netted to a single amount. Without netting: credit exposure = sum of all positive MTMs ($500M). With netting: exposure = net of all MTMs ($20M). Capital savings from netting are enormous — this is why banks insist on ISDA Master Agreements before trading. Netting enforceability must be confirmed by legal opinion in each jurisdiction.

**Tier 4:** Credit events that trigger CDS payouts (§6.3, §6.4): Bankruptcy, Failure to Pay, Restructuring (depending on clause type), Governmental Intervention (for bail-in). The 2023 Credit Suisse AT1 write-down tested these definitions — FINMA's emergency ordinance allowed AT1 write-down while equity received $3.2B, inverting the normal creditor hierarchy. Under NR documentation, this would not trigger CDS. Under FR, it would. The restructuring clause choice is not academic — it determines whether your hedge works.

---

## 3.4 Credit & Capital Structure (§6.4)

**Tier 1:** The capital hierarchy determines who gets paid first when a company defaults. Eight layers from Senior Secured (safest) to Common Equity (first to absorb losses).

**Tier 2:** Recovery rates by seniority: Senior Secured ~65-70%, Senior Unsecured ~40-50%, Subordinated ~20-30%, Preferred Equity ~10-15%, Common Equity ~0-5%. A CLN referencing senior unsecured has fundamentally different recovery expectations than one referencing AT1. Same bank, same credit risk on the surface — completely different loss outcomes.

**Tier 3:** AT1/CoCos: Most junior bank debt, designed for going-concern loss absorption. Trigger: CET1 ratio falls below 5.125% (standard) or 7% (high trigger). Two types: conversion to equity (bondholder becomes shareholder) or principal write-down (permanent or temporary). PONV (Point of Non-Viability): regulator can force conversion/write-down at discretion, regardless of contractual trigger.

Bail-in framework: Losses applied in reverse seniority order — equity first, then AT1, Tier 2, Senior Non-Preferred, Senior Preferred. Stops when bank is recapitalized. TLAC requirement: G-SIBs must hold ≥18% of RWA in loss-absorbing capacity.

**Tier 4:** CDS restructuring clauses (§6.4): FR (broadest — any restructuring triggers, deliver any bond up to 30 years), MR (restructuring triggers but deliverable limited to 30 months), MMR (60 months for restructured debt, 30 for non-restructured), NR (restructuring NOT a credit event). Regional conventions: North America = NR, Europe = MMR, Asia = varies. Getting the clause wrong means the difference between full protection and zero payout on your hedge.

---

## 3.5 Valuation & Fair Value (§6.5)

**Tier 1:** The Fair Value Hierarchy classifies how assets are valued. Level 1: quoted market prices. Level 2: observable inputs (models calibrated to liquid market data). Level 3: significant unobservable inputs (models with assumptions that cannot be verified against market data).

**Tier 2:** Classification by product: 6-month RC on Apple = Level 2 (liquid single-stock options). 1-year autocallable on Euro Stoxx 50 = Level 2 (liquid index options). 5-year CDO bespoke tranche = Level 3 (correlation unobservable). 10-year worst-of on EM stocks = Level 3 (no liquid options market for these underlyings).

IPV (Independent Price Verification) (§6.5): Product Control independently verifies trader marks using: broker quotes, consensus pricing services, model comparison. When IPV price differs from trader mark beyond tolerance, the mark is challenged. Persistent overmarking by traders is a red flag triggering investigation.

**Tier 3:** Day One P&L: When a Level 3 trade is booked and the model shows profit at inception, that profit must be DEFERRED — not recognized immediately. The deferred P&L is amortized over the trade's life or released when observable evidence supports the valuation. IFRS 13 and ASC 820 mandate this deferral. (See §6.6 Day One Reserve for operational implementation.)

**Tier 4:** Valuation governance: The Valuation Committee reviews Level 3 valuations, approves methodology changes, and oversees reserve adequacy. Quarter-end and year-end add external auditor review. Level 3 disclosures in financial statements are closely scrutinized by analysts and regulators.

---

## 3.6 Product Control (§6.6)

**Tier 1:** Product Control independently verifies trading P&L, position valuations, and risk sensitivities every day. PC answers one question: "Is the P&L number correct, and do we understand why it changed?"

**Tier 2:** P&L Explain — the core of PC:

| Component | What It Captures | Typical Driver |
|-----------|-----------------|---------------|
| Delta P&L | Change from underlying price move | Stock/index moved |
| Gamma P&L | Change from convexity (delta changing) | Large underlying move |
| Vega P&L | Change from implied vol shift | Vol surface moved |
| Theta P&L | Time decay (one day passing) | Always negative for long options |
| Rho P&L | Change from interest rate move | Rate curve shifted |
| Credit P&L | Change from credit spread move | CDS spreads moved |
| Dividend P&L | Change from dividend forecast revision | Dividend estimate changed |
| New Deals | Manufacturing margin on new trades | New trade booked |
| Unexplained | Residual — should be small | Large = problem |

Tolerance: Unexplained <5-10% of gross P&L. Large unexplained triggers investigation: stale marks? booking errors? model calibration? corporate actions?

**Tier 3:** Flash P&L vs Official P&L: Flash is preliminary (7-8 AM, pre-IPV). Official is verified (midday-afternoon, post-IPV, post-reserves). Management decisions use Official only. A pattern of Official consistently lower than Flash signals systematic overmarking — a red flag.

Reserve framework (§6.6): Multiple reserves may apply simultaneously to a single position:
- **Bid-offer reserve:** Half the bid-offer spread × position size. Illiquid single-stock products have wider spreads.
- **Model reserve:** Difference between primary and challenger model prices.
- **Correlation reserve:** P&L impact of shifting correlation ±5%. Material for WOAC, FTD.
- **Liquidity reserve:** Market impact of unwinding a large position over 10-30 business days.
- **Parameter uncertainty reserve:** Impact of shifting vol, dividend, or mean reversion parameters.
- **Day One reserve:** Deferred inception profit on Level 3 trades.
- **Funding reserve:** Cost of funding uncollateralized MTM receivables.

Reserve governance: PC proposes, Valuation Committee approves. Monthly routine review, quarterly deep-dive with external auditors. Release only when uncertainty resolves — NOT for P&L management.

**Tier 4:** Month-end process: Position reconciliation → final IPV → P&L Explain sign-off → reserve adequacy review → formal sign-off (desk head, PC lead, Risk lead, CFO representative). Quarter-end and year-end add: external auditor review, Day One P&L amortization review, impairment testing, Level 3 disclosure preparation.

---

## 3.7 Treasury, Capital & XVA (§6.7)

**Tier 1:** Treasury manages the bank's funding. FTP (Funds Transfer Price) is the internal cost charged to the desk for using the bank's balance sheet. XVA adjustments correct the theoretical model price for real-world costs the model ignores.

**Tier 2:** FTP methodology: Treasury constructs an internal funding curve based on: the bank's external borrowing costs, a term premium (longer = more expensive), and a liquidity premium. Illustrative: 1Y FTP ~1.20%, 5Y ~2.40%, 10Y ~3.10%.

FTP as the "hidden killer": A 3Y ELN with 6% coupon. Revenue (bond yield + option premium) = 7.30%. After coupon (−6.00%) and FTP (−1.80%): desk margin = **−0.50%**. The product DESTROYS value after FTP despite appearing profitable before it.

XVA framework:
- **CVA:** Cost of counterparty default risk ≈ PD × LGD × EPE. Higher for uncollateralized, low-rated counterparties.
- **DVA:** Bank's own credit risk (counterintuitive — bank "benefits" from its own deterioration). IFRS 13 requires recognition; Basel III partially excludes from regulatory capital.
- **FVA:** Funding cost of uncollateralized derivative exposures. High for corporates/sovereigns with no CSA. Low for fully collateralized institutional trades.
- **MVA:** Cost of posting initial margin (cash/securities in segregated accounts). Material for long-dated cleared trades.
- **KVA:** Cost of holding regulatory capital over the trade's life. Capital costs 10-15% (bank's cost of equity). Trades that consume significant capital must earn proportionally higher returns.
- **ColVA:** Cost of posting specific collateral types (cross-currency CSA, non-standard eligible collateral).

**Tier 3:** Capital framework:
- **RWA:** Risk-weighted assets. Riskier assets get higher weights → require more capital. Government bonds = 0% weight. Unrated corporates = 100%.
- **SA-CCR:** EAD = 1.4 × (Replacement Cost + PFE). Determines derivative exposure for capital calculation. Long-dated, large-notional derivatives generate high EAD → high RWA → high capital cost.
- **RAROC:** (Revenue − Costs − Expected Loss) / Capital Consumed. The true profitability metric. A trade earning $1M but consuming $50M capital (RAROC 2%) is worse than a trade earning $350K consuming $5M capital (RAROC 7%).

**Tier 4:** Capital optimization strategies: Netting (balanced portfolios under same ISDA), collateral (strong CSA terms), central clearing (lower capital charges), compression (reduce gross notional). Smart desks optimize for RAROC, not just revenue. The FTP expected-life problem for autocallables remains one of the most debated aspects of structured products economics.

Liquidity regulation: LCR (30-day stress outflows covered by HQLA), NSFR (1-year stable funding). Structured products with uncertain cash flows (autocallables) consume LCR. Long-dated products require NSFR-compliant stable funding.

---

## 3.8 Model Risk Management (§6.8)

**Tier 1:** Model risk is the risk that the mathematical model used to price and hedge a product is wrong — either inherently (bad assumptions) or operationally (correct model, wrong inputs). Regulatory frameworks (SR 11-7 in the US, SS1/23 in the UK) require formal model governance.

**Tier 2:** The model lifecycle: Development → Documentation → Validation → Approval → Implementation → Monitoring → Material Change → Retirement. Each stage has governance requirements. Approval outcomes: Approve, Conditional Approval (with restrictions or reserves), Reject.

Validation checks: Mathematical correctness, conceptual soundness, implementation testing (code matches math), calibration quality, stability, boundary behavior, benchmarking against challenger models.

**Tier 3:** Challenger models: Alternative models that benchmark the primary model. The difference in valuation = measure of model uncertainty → drives model reserve (§6.6).

| Primary | Challenger | Products |
|---------|-----------|----------|
| Local Vol + MC | Stochastic Vol + MC | WOAC, barrier products |
| Black-Scholes | Local Vol + MC | Vanilla ELN |
| Hull-White 1-factor | Hull-White 2-factor / SABR | CMS, SRT |
| Gaussian Copula | Student-t Copula | CDO, FTD |

Model inventory: Every model registered with purpose, owner, validator, approval date, next review date, risk rating (High/Medium/Low), and known limitations.

**Tier 4:** Expert judgment overrides: When the model gives a price the desk believes is wrong (e.g., unobserved market feature, model applied outside validated range, market dislocation). Governance: documented, justified, approved by senior person, reviewed by MRM, time-limited. Without governance, overrides become a mark-manipulation mechanism.

Backtesting: Compare model predictions to realized outcomes. Traffic light system — Green (within expectations), Yellow (borderline — enhanced monitoring), Red (unacceptable — immediate remediation, potential model suspension, additional reserves).

---

## 3.9 Operations (§6.9)

**Tier 1:** Operations processes every trade from booking to maturity. Eight stages: Trade Capture → Enrichment → Validation (Four-Eyes) → Confirmation → Settlement → Daily Maintenance → Lifecycle Events → Maturity/Termination.

**Tier 2:** Booking workflow: Trade capture form (economic terms, product structure, counterparty, system fields, settlement). System validation rules: maturity on business day? notional within credit limit? counterparty approved? observation dates consistent? Four-eyes check: second person verifies booking against termsheet.

Static data: Reference data that rarely changes (counterparty details, instrument definitions, SSI, calendars). Golden source: single authoritative system per data type (counterparty = CRM, instrument = NEMO/Murex, market data = Sophis/Murex, SSI = settlement system, calendars = vendor/internal).

**Tier 3:** Reconciliation: Cash reconciliation (expected vs actual cash flows — nostro account comparison). Trade reconciliation (front office vs back office positions). Break types: amount mismatch, missing payment, unexpected payment, rounding difference, position break, terms mismatch, status mismatch.

Break investigation: Check original booking → amendment history → enrichment → counterparty records → market data. Escalation: 1 day = analyst, 3 days = team lead, 5 days = manager, 10 days = department head + operational risk reporting.

Corporate actions: Stock split (adjust strike, barrier, quantity by ratio), merger (successor entity replaces underlying), rights issue (dilution adjustment), special dividend (strike reduction if extraordinary), spin-off (basket adjustment). ISDA Equity Definitions cascade: Calculation Agent Adjustment → Modified Calculation Agent Adjustment → Cancellation and Payment.

**Tier 4:** Settlement fails: consequences include CSDR fails charges (daily penalties), buy-in risk (buyer purchases in open market and charges seller), reputational damage. Settlement types by family: ELN (cash or physical), Swaps (net cash), SRT (cash), CLN (cash or physical delivery of reference obligation upon credit event).

Confirmation backlog risk: Unconfirmed trades = no bilateral agreement on terms. Regulators view backlogs >5 business days as evidence of weak controls. A backlog above regulatory thresholds triggers supervisory action.

---

## 3.10 Desk Practice & Vocabulary (§6.10)

**Tier 1:** The structured products desk is short gamma and short vega by construction. Clients buy products that embed options — selling those options makes the desk short gamma and short vega. Everything else follows from this fundamental positioning.

**Tier 2:** Key desk vocabulary:
- **Flow book vs Exotic book:** Flow = high-volume standard products (vanilla RC, FCN), low margin, automated pricing. Exotic = bespoke structures (WOAC, CDO), low volume, high margin, model-intensive.
- **Axed:** Actively looking to trade a specific product. "We're axed in 1Y Euro Stoxx autocalls" = marketing aggressively.
- **Risk warehousing:** Accumulating risk from multiple trades and hedging the net position, rather than hedging each trade individually. Efficient but creates warehouse risk if positions move before hedging.
- **Flash vs Official P&L:** Flash = preliminary (7 AM, pre-IPV). Official = verified (afternoon, post-IPV, post-reserves).

**Tier 3:** Greeks positioning language:
- **Short gamma:** Loses from large moves in either direction. Near barriers, short gamma is extremely painful — delta changes rapidly, forcing "buy high, sell low" rebalancing. This is the default SP desk position.
- **Short vega:** Loses from rising implied vol. A vol spike across the board creates significant MTM losses across the portfolio.
- **Long correlation (WOAC):** Benefits when assets move together (reduces worst-of risk). Correlation breakdown → losses.

Role-specific vocabulary: Structurer (reverse inquiry, bespoke, indication, firm price), Trader (lifted, hit the bid, working, stuffed, scratched), Sales (suitability, target market, IOI, execution-only, advisory), Risk (limit breach, VaR, stress test, concentration risk), PC (flash, official, unexplained, reserve, IPV break), Ops (break, fail, SSI, static data, golden source, four-eyes).

---

## 3.11 Regulatory Framework (§6.11)

**Tier 1:** Four major frameworks: MiFID II (EU investor protection), PRIIPs (standardized disclosure), EMIR (OTC derivatives clearing/reporting), Basel III/IV (bank capital and liquidity).

**Tier 2:** MiFID II: Product governance (target market + negative target market), suitability/appropriateness assessment, cost transparency, best execution. PRIIPs: KID required for retail — SRI (1-7 scale), performance scenarios (favorable/moderate/unfavorable/stress), costs.

EMIR three pillars: Reporting (all trades to repository within T+1), Clearing (standardized OTC through CCP — IRS, CDS indices), Risk mitigation for non-cleared (timely confirmation, portfolio reconciliation, compression, dispute resolution).

UMR: Bilateral margin for non-cleared derivatives. Variation margin (daily MTM exchange). Initial margin (additional buffer calculated via ISDA SIMM — 10-day 99% confidence). IM must be segregated at independent custodian.

**Tier 3:** Basel/FRTB: FRTB overhauls market risk capital. Standardised approach (SA) vs Internal Models Approach (IMA). Desk-level model approval — each desk qualifies independently. Desks that fail use SA (typically higher capital). CVA capital: dedicated charge for CVA risk from credit spread movements.

Dodd-Frank (US): Title VII governs swap dealers — registration, clearing (through DCO), reporting (to SDR), margin. Cross-border implications: trades between US and non-US entities may face both Dodd-Frank and EMIR.

MAR: Prohibits insider dealing, market manipulation, unlawful disclosure. SP desk holds significant MNPI: barrier levels, client order flow, autocall observation dates. Chinese walls required.

**Tier 4:** Product intervention power: ESMA can ban or restrict products (banned binary options for retail 2018, restricted CFD leverage). Structured deposits vs structured notes under PRIIPs: both require KID, but SD additionally has deposit guarantee protection. Non-cleared ≠ unregulated — EMIR risk mitigation requirements and UMR margin rules apply.

---

# Part 4: Comparison & Confusion Pairs

## 4.1 Full Product Comparison Pairs (10)

### Pair 1: PPN vs RC

| Dimension | PPN (2) | RC (3) |
|-----------|---------|--------|
| Embedded Option | Long call (bought) | Short put (sold) |
| Vol Direction | Long vega | Short vega |
| Capital Risk | Protected (issuer guarantee) | Full downside below barrier |
| Yield Source | None (growth from call) | Put premium funds coupon |
| Upside | Participation × underlying gain | Capped at coupon |
| Worst Case | Zero return + issuer default | Barrier breach → receive depreciated shares |

**Elevator Differentiation:** PPN buys growth (long call, long vol). RC sells protection (short put, short vol). Opposite risk profiles from the same underlying.

**Deep Differentiation:** Both are issued by the same bank, on the same underlying, with the same maturity. The ONLY difference is which option is embedded. PPN buyer is long vol — they benefit from rising markets and rising vol. RC buyer is short vol — they earn carry (coupon) in exchange for selling downside protection. A client who says "I want something safe with upside" should get PPN. A client who says "I want income and can tolerate some downside" should get RC. Recommending the wrong one is a suitability failure.

**What The Interviewer Is Testing:** Does the candidate understand that the embedded option direction determines the ENTIRE risk profile? Can they match product to client based on this?

---

### Pair 2: Phoenix vs WOAC

| Dimension | Phoenix (6) | WOAC (8) |
|-----------|------------|----------|
| Underlying | Single stock | Basket (3-5 stocks) |
| Coupon | 10-15% | 18-25% |
| Barrier Driver | One stock's performance | Worst stock in basket |
| Correlation Exposure | None | Short correlation |
| Barrier Breach Probability | P(stock < barrier) | ≈ 1−(1−P)^N if independent |

**Elevator Differentiation:** Phoenix = one stock, one barrier. WOAC = N stocks, worst one controls everything. Coupon difference (12% → 22%) is the price of correlation risk.

**Deep Differentiation:** WOAC converts "diversification benefit" into the investor's enemy. When stocks decorrelate (one crashes alone), the worst-of mechanism triggers on FULL notional even though N-1 stocks are fine. The coupon compensates. When stocks are highly correlated, WOAC risk approaches single-stock risk and the extra coupon is uncompensated — the best scenario for the investor.

**Trap Question:** "A client chose 5 blue-chip Swiss stocks for their WOAC because diversification protects them." *In WOAC, diversification increases risk, not reduces it.*

---

### Pair 3: Phoenix vs FCN

| Dimension | Phoenix (6) | FCN (6) |
|-----------|------------|---------|
| Coupon | Conditional (above barrier only) | Guaranteed (always paid) |
| Coupon Level | Higher (10-15%) | Lower (5-8%) |
| Memory Feature | Common | N/A |
| Cash Flow Predictability | Low | High |
| Capital Risk | Identical | Identical |

**Elevator Differentiation:** Same capital risk. Phoenix pays higher uncertain coupons; FCN pays lower guaranteed coupons. Coupon difference = value of optionality (the bank's right to not pay).

**What The Interviewer Is Testing:** Does the candidate understand that guaranteed ≠ safe? Capital risk is identical — FCN guarantees the coupon but NOT the principal.

---

### Pair 4: FTD vs NTD

| Dimension | FTD (7) | NTD (8) |
|-----------|---------|---------|
| Trigger | First default | Nth default |
| Correlation Sensitivity | Long correlation | Short correlation |
| Low Correlation → | HIGHER risk | LOWER risk |
| High Correlation → | LOWER risk | HIGHER risk |

**Elevator Differentiation:** OPPOSITE correlation sensitivity. The single hardest concept in credit derivatives.

**Deep Differentiation:** FTD: probability of at least ONE default = 1 − Π(1−PD_i) when independent. High correlation → defaults cluster → fewer "one default" outcomes → FTD benefits. NTD: requires N+ defaults → high correlation → defaults cluster → more likely to reach N → NTD suffers.

**Trap Question:** "Correlation rises from 0.3 to 0.7 — what happens to FTD spread and NTD spread?" *FTD tightens (risk decreases). NTD widens (risk increases).*

---

### Pair 5: CLN vs CDS

| Dimension | CLN (4) | CDS (5) |
|-----------|---------|---------|
| Format | Funded (cash at risk) | Unfunded (swap) |
| Credit Exposure | Dual (reference + issuer) | Single (reference only) |
| Capital at Risk | Full principal | MTM only |
| Use Case | Funded credit investment | Hedging, speculation |

**Elevator Differentiation:** CLN = buy the credit risk (cash goes to issuer). CDS = swap the credit risk (no cash). CLN has dual credit exposure.

---

### Pair 6: IRS vs VLSP

| Dimension | IRS (3) | VLSP (2) |
|-----------|---------|----------|
| Terms | Standardized | Customized (caps, floors, amortization) |
| Liquidity | Extremely liquid, centrally cleared | Less liquid, bilateral |
| Use Case | Standard rate hedging | Bespoke cash flow matching |

**What The Interviewer Is Testing:** IRS is the starting point despite VLSP having lower Atlas complexity.

---

### Pair 7: TRS vs EqSwap

| Dimension | TRS (5) | EqSwap (5) |
|-----------|---------|------------|
| Underlying | Multi-asset (equity, credit, loans) | Equity only |
| Use Case | Synthetic ownership of illiquid assets | Synthetic equity index exposure |

**What The Interviewer Is Testing:** Asset class breadth. TRS necessary for credit/loan exposure; EqSwap sufficient for pure equity.

---

### Pair 8: RC vs DCI

| Dimension | RC (3) | DCI (3) |
|-----------|--------|---------|
| Asset Class | Equity | FX |
| Mechanism | Short equity put | Short FX put |
| Worst Case | Receive depreciated shares | Receive principal in weaker currency |

**What The Interviewer Is Testing:** Same embedded option structure across different asset classes.

---

### Pair 9: PPN vs SD

| Dimension | PPN (2) | SD (2) |
|-----------|---------|--------|
| Wrapper | Note (issuer credit risk) | Deposit (deposit insurance) |
| Protection Source | Issuer guarantee | Government up to limit (€100K EU) |

**What The Interviewer Is Testing:** Below deposit insurance limit, SD is strictly superior.

---

### Pair 10: CDO vs FTD

| Dimension | CDO (10) | FTD (7) |
|-----------|----------|---------|
| Portfolio Size | 100+ names | 5-10 names |
| Loss Mechanism | Tranched waterfall | Binary first-default |
| Model | Full portfolio Gaussian copula | Simplified basket copula |

**Elevator Differentiation:** FTD is the baby CDO — same concept but simplified to a small basket with binary trigger.

---

## 4.2 Quick Differentiation Guide — 25 Pairs

| # | Pair | Key Difference |
|:-:|------|---------------|
| 1 | PPN vs RC | PPN buys a call (long vol); RC sells a put (short vol). Opposite risk profiles. |
| 2 | RC vs DRC | RC = coupon income; DRC = discount entry. Same risk, different return mechanism. |
| 3 | RC vs CRC | CRC adds bank call right → higher coupon but bank terminates in best scenario. |
| 4 | DRC vs KODRC | KODRC adds KO barrier → investor protected unless barrier breached. |
| 5 | Phoenix vs FCN | Phoenix coupon conditional (higher); FCN guaranteed (lower). Same capital risk. |
| 6 | Phoenix vs SNOW | SNOW accumulates missed coupons (snowball); Phoenix loses them (unless memory). |
| 7 | Phoenix vs WOAC | WOAC adds worst-of basket → investor long correlation (MTM; structurally sold corr premium). Coupon doubles but risk is N stocks. |
| 8 | CRA ELN vs Digital | CRA accrues proportionally (days in range / total); Digital is all-or-nothing. |
| 9 | VO vs Warrant | Same economics. VO = OTC/exchange. Warrant = exchange-listed retail. |
| 10 | VO vs ELO | Same economics. ELO = retail note wrapper. |
| 11 | ACCUM vs DECUM | ACCUM buys at discount (bullish). DECUM sells at premium (exit). Mirror. |
| 12 | IRS vs VLSP | VLSP = IRS + features. IRS is the vanilla default. |
| 13 | TRS vs EqSwap | EqSwap = equity-specific TRS. TRS covers any asset class. |
| 14 | NCRA vs CRA SRT | CRA SRT adds callability → higher coupon but bank can terminate. |
| 15 | V. STEG vs C. STEG | C. STEG adds bank call → higher coupon, called when curve steepens (worst timing). |
| 16 | FTD vs NTD | Correlation reversal. Low corr increases FTD risk; high corr increases NTD risk. |
| 17 | CLN vs CDS | CLN = funded (dual credit). CDS = unfunded (single credit). |
| 18 | PPN vs SD | PPN = note (issuer risk). SD = deposit (deposit insurance up to limit). |
| 19 | PPN vs SHRK | SHRK adds KO barrier → higher participation but capped if stock rallies strongly. |
| 20 | PPN vs CLIQ | CLIQ locks in periodic returns (ratchet). PPN measures total at maturity only. |
| 21 | RC vs DCI | Same mechanism (short put for yield). RC = equity. DCI = FX. |
| 22 | IR Callable vs CRC | Both sell call right. IR Callable = rate (swaption). CRC = equity (Bermudan call + put). |
| 23 | Digital vs Digital CF | Same payoff (binary coupon). Digital = equity-linked. Digital CF = rate-linked. |
| 24 | CDO vs FTD | FTD = 5-10 names, binary first-default. CDO = 100+ names, tranched waterfall. |
| 25 | Booster vs Warrant | Both leveraged. Booster = capped leverage in note. Warrant = uncapped on exchange. |

---

## 4.3 Infrastructure Confusion Pairs (10)

| # | Confusion | Wrong | Right | §6 Reference |
|:-:|-----------|-------|-------|:------------:|
| 1 | Modified Following = Following | Both move to next business day | Modified Following moves BACKWARD if crossing month-end | §6.1 |
| 2 | ACT/360 = ACT/365 | Same convention, different notation | Different denominator: $100M × 6% × 1 day = $16,667 (ACT/360) vs $16,438 (ACT/365). $229/day difference | §6.1 |
| 3 | Flash P&L = Official P&L | Same number, flash is just earlier | Different: Flash is pre-IPV, pre-reserves. Official is verified. Gap signals overmarking | §6.6 |
| 4 | CSA Threshold = No collateral | If exposure < threshold, no collateral posted | Threshold is the UNSECURED amount. Exposure above threshold requires collateral. MTA creates additional gap | §6.3 |
| 5 | CVA = Credit risk on reference entity | Both are "credit risk" | CVA = counterparty default risk. Reference entity risk = the risk you deliberately took. Different directions | §6.7 |
| 6 | IPV = Checking Bloomberg | IPV uses Bloomberg and is done | IPV is a full process: broker quotes, model comparison, consensus services, challenge process | §6.5 |
| 7 | Golden source = One system for everything | One master database | Different data types have different golden sources: counterparty in CRM, instrument in NEMO, market data in Sophis | §6.9 |
| 8 | Model validation = Model is correct | Validated = perfect | Validated = reviewed and fit for purpose WITHIN its limitations. Limitations documented | §6.8 |
| 9 | Non-cleared = Unregulated | No CCP = no rules | EMIR risk mitigation (confirmation, reconciliation, dispute resolution) + UMR margin requirements apply | §6.11 |
| 10 | Capital is free | Revenue > costs = profitable | Capital has a cost (10-15% cost of equity). RAROC must exceed hurdle rate | §6.7 |

---

# Part 5: Termsheet Exercises

## Exercise 1: Reverse Convertible — Beginner

**Termsheet Extract:**
```
Product Type:         Reverse Convertible
Underlying:           NESN VX Equity (Nestlé SA)
Notional:             CHF 1,000,000
Issue Price:          100%
Trade Date:           15 January 2026
Settlement Date:      17 January 2026
Maturity Date:        17 July 2026
Coupon:               8.00% p.a.
Day Count:            30/360
Business Day Conv:    Modified Following (Zurich)
Barrier Type:         European (observed at maturity only)
Barrier Level:        70% of Initial Level
Initial Level:        CHF 95.50
Settlement:           Physical delivery if barrier breached; Cash otherwise
Calculation Agent:    The Issuer
```

**Questions:**
1. What is the settlement lag? (Answer: T+2 — trade date Jan 15, settlement Jan 17)
2. Calculate the coupon payment amount. (Answer: CHF 1,000,000 × 8% × (180/360) = CHF 40,000. Note: 30/360 assumes 180 days for exactly 6 months.)
3. The maturity date July 17 falls on a Friday. What if it fell on Saturday? (Answer: Modified Following → Monday July 19, unless July 19 is in August — but July 19 is still in July, so Monday July 19.)
4. What is the barrier level in CHF? (Answer: 70% × CHF 95.50 = CHF 66.85)
5. The stock closes at CHF 66.00 on maturity. What does the investor receive? (Answer: Physical delivery. Number of shares = CHF 1,000,000 / CHF 95.50 ≈ 10,471 shares. Investor receives ~10,471 depreciated shares worth CHF 66.00 each ≈ CHF 691,099 plus the CHF 40,000 coupon.)
6. Identify one risk NOT visible in this termsheet. (Answer: Issuer credit risk — the issuer could default before maturity.)

---

## Exercise 2: Phoenix Autocallable — Intermediate

**Termsheet Extract:**
```
Product Type:         Phoenix Autocallable Note
Underlyings:          SIE GY Equity (Siemens AG)
Notional:             EUR 500,000
Issue Price:          100%
Maturity:             3 Years (18 July 2029)
Coupon:               11.00% p.a. (conditional)
Coupon Barrier:       75% of Initial Level
Coupon Frequency:     Quarterly
Memory Feature:       Yes
Autocall Barrier:     100% of Initial Level
Autocall Observation: Quarterly (starting Month 6)
Knock-In Barrier:     65% of Initial Level
Barrier Observation:  Continuous
Day Count:            ACT/360
Settlement:           Cash
```

**Questions:**
1. The note has quarterly observations. How many total coupon observation dates exist over 3 years? (Answer: 12)
2. How many autocall observation dates? (Answer: Starting month 6, quarterly → 10 autocall dates)
3. The stock drops to 72% at Q1 observation. What happens to the coupon? (Answer: 72% < 75% coupon barrier → no coupon paid. But memory feature stores the missed coupon.)
4. At Q2, stock recovers to 80%. What coupon is paid? (Answer: 80% > 75% → coupon paid. PLUS the Q1 missed coupon due to memory. Total: 2 × (EUR 500,000 × 11% × 90/360) = 2 × EUR 13,750 = EUR 27,500)
5. The barrier observation is "Continuous" — what does this mean operationally? (Answer: The knock-in barrier is monitored every moment during trading hours, not just at closing. An intraday breach counts. Operations must have real-time monitoring systems in place — see §6.9.)
6. Why is the day count ACT/360 and not 30/360? (Answer: This affects the coupon calculation. A 92-day quarter under ACT/360 yields EUR 500K × 11% × 92/360 = EUR 14,056. Under 30/360 it would be EUR 500K × 11% × 90/360 = EUR 13,750. Difference: EUR 306 per quarter.)

---

## Exercise 3: CLN with CDS Restructuring — Advanced

**Termsheet Extract:**
```
Product Type:         Credit Linked Note
Reference Entity:     Deutsche Bank AG
Reference Obligation: Senior Unsecured Bonds
Notional:             EUR 5,000,000
Maturity:             5 Years
Coupon:               CDS Spread + 50bp (fixed at inception)
Credit Events:        Bankruptcy, Failure to Pay, Modified Modified Restructuring (MMR)
Recovery:             Auction-determined (ISDA Credit Event Auction)
Restructuring Deliverable: Bonds maturing within 60 months of CDS maturity (restructured) / 30 months (non-restructured)
```

**Questions:**
1. Why does the CLN pay CDS spread + 50bp, not just CDS spread? (Answer: The desk receives the investor's cash — this funding benefit allows a higher coupon. See §6.7 FTP.)
2. The CLN uses MMR. If the restructuring clause were NR instead, and Deutsche Bank restructures its debt (extends maturity by 3 years, cuts coupon by 100bp) — would the investor receive a payout? (Answer: Under NR — NO. Restructuring is not a credit event. The investor suffers real economic loss with no CDS payout. Under MMR — YES, but deliverable bonds are limited to those maturing within 60 months of CLN maturity.)
3. Name the dual credit risk. (Answer: (1) Reference entity credit risk — Deutsche Bank defaults. (2) Issuer credit risk — the bank that issued the CLN defaults.)
4. What is the fair value hierarchy classification? (Answer: Likely Level 2 — Deutsche Bank senior CDS is liquid, providing observable credit spreads. If the CLN had bespoke features or illiquid reference entity, it could be Level 3.)

---

## Exercise 4: IRS Day Count Calculation — Intermediate

**Scenario:** A 5-year USD IRS, notional $50M. Fixed leg: 3.50% semi-annual, 30/360. Floating leg: SOFR, quarterly, ACT/360. Calculate the first fixed coupon and first floating coupon.

**Fixed leg (6-month period, 30/360):**
Accrual period: Jan 15 to Jul 15. Under 30/360: 180 days.
Coupon = $50M × 3.50% × (180/360) = **$875,000**

**Floating leg (3-month period, ACT/360):**
Accrual period: Jan 15 to Apr 15. Actual days: 90 (non-leap year).
Assume compounded SOFR = 3.25% for the period.
Coupon = $50M × 3.25% × (90/360) = **$406,250**

**Net settlement (fixed payer pays):** $875,000 − $406,250 = $468,750 (but note: fixed is semi-annual, floating is quarterly — the first floating payment occurs at 3 months while the first fixed payment occurs at 6 months. The net settlement at 6 months would combine the fixed payment with the second floating payment.)

---

## Exercise 5: P&L Explain Challenge — Advanced

**Scenario:** You are a Product Control analyst. The equity derivatives desk reports +€800K P&L yesterday. Your P&L Explain shows:

| Component | Amount |
|-----------|-------:|
| Delta P&L | +€500K |
| Vega P&L | −€150K |
| Theta P&L | +€200K |
| New Deals | +€50K |
| **Explained** | **+€600K** |
| **Actual** | **+€800K** |
| **Unexplained** | **+€200K** |

The unexplained tolerance is 10% of gross P&L.

**Questions:**
1. Should you escalate? (Answer: YES. Unexplained = €200K / €800K = 25%. Far exceeds the 10% threshold.)
2. The trader says "it's just noise, it'll wash out tomorrow." What is your response? (Answer: You do NOT accept this. PC's job is to explain today's P&L today. "Washing out tomorrow" is not an explanation — it is a deferral. You investigate.)
3. List your investigation steps. (Answer: (1) Challenge trader marks — are end-of-day prices correct? Stale market data? (2) Check for booking errors — trade booked twice? wrong notional? wrong book? (3) Check model calibration — new model version? vol surface shift in a way Greeks don't capture? (4) Check corporate actions — ex-dividend? stock split? (5) If unresolved within morning window, escalate to desk head and risk management.)
4. If unexplained were +€10K every day for 20 days, would each day pass? (Answer: Each day individually: €10K/€800K = 1.25% — passes the threshold. But the cumulative pattern (+€200K over 20 days) signals a systematic issue. PC must monitor trends, not just daily levels.)

---

# Part 6: Question Bank

## 6.1 Technical Questions (T.1–T.37)

### Greeks & Options

**Beginner**

T.1 [WT] What is delta and how does it change as the underlying price moves? Which products are long delta and which are short delta?

T.2 [WT] Explain the difference between a European option and an American option. Why does early exercise matter?

T.3 What determines the price of a vanilla call option? Name 5 inputs.

T.4 A client holds a put option. The stock drops 5%. Approximately how much does the option value change if delta is −0.4?

T.5 [WT] What is implied volatility? Why is it different from realized volatility?

**Intermediate**

T.6 [WT] What is gamma risk at a barrier level? Why does the desk's hedging cost spike when the underlying is near a knock-in barrier?

T.7 A Phoenix note has a coupon barrier at 70% and autocall at 100%. Draw the delta profile as spot moves from 50% to 120% of initial level.

T.8 Explain why an RC investor is short vega while a PPN investor is long vega.

T.9 [WT] How does time decay (theta) differ for an ATM option vs a deep OTM option? Why?

T.10 What is pin risk? Why do desks dread observation dates when spot is near a digital strike?

**Advanced**

T.11 A variance swap has 6 months remaining. Realized vol for the first 6 months was 15%. The strike was 20%. If realized vol for the remaining 6 months is 25%, what is the approximate P&L for the long?

T.12 Explain vol-of-vol. Which products have explicit sensitivity to it?

T.13 [WT] Why is a short variance swap position more dangerous than a short straddle?

T.14 An RC has 1 month remaining. Spot is 2% above the barrier. Implied vol is 25%. Should you be worried about gamma? Quantify.

T.15 What is the CMS convexity adjustment and why does it matter for STEG pricing?

**Expert**

T.16 Derive the replication argument for a variance swap using a portfolio of options. What assumptions are required?

T.17 How does the choice of copula (Gaussian, Student-t, Clayton) affect CDO tranche pricing? Which tranche is most sensitive?

T.18 A WOAC has 5 underlyings. Implied correlation is 0.6. One stock's implied vol jumps 10 points while others are unchanged. What happens to the WOAC price?

T.19 [WT] Explain the "Quanto" adjustment. Why does a Quanto option trade at a different implied vol?

T.20 How would you price a snowball autocallable? Why can't you use a closed-form solution?

### Rates

T.21 [WT] Why does a zero-coupon bond's price increase when interest rates fall?

T.22 What is the difference between a spot rate and a forward rate?

T.23 [WT] Explain DV01 and how it differs between a 2-year and a 30-year IRS.

T.24 Why does the swap rate differ from the government bond yield of the same maturity?

T.25 Explain the CMS-forward rate difference. What drives the convexity adjustment?

T.26 How does the choice of short-rate model (Hull-White, BK, LGM) affect callable note pricing?

### Credit

T.27 [WT] What is a credit event under ISDA definitions? Name three types.

T.28 What is recovery rate and why does it matter for CDS pricing?

T.29 [WT] Why does a CLN investor face dual credit risk? Name both exposures.

T.30 What is the CDS-bond basis and why does it exist?

T.31 How does the Big Bang protocol (2009) standardize CDS contracts?

T.32 Explain base correlation and why it replaced compound correlation for CDO tranche pricing.

### Volatility & Correlation

T.33 [WT] What does it mean to be "long volatility"? Give a long vol and short vol product example.

T.34 [WT] Explain the volatility smile/skew. Why are OTM puts typically more expensive than OTM calls?

T.35 How does realized correlation between stocks affect WOAC pricing?

T.36 What is the variance risk premium and why does it exist?

T.37 How would you construct a dispersion trade using VarSwaps?

---

## 6.2 Product Knowledge Questions (PK.1–PK.49)

One question per product, organized by family. Each references Atlas Appendix E.

### ELN Family

PK.1 [WT] **PPN:** Why is the participation rate always less than 100%? Walk through the arithmetic.
PK.2 **RC:** Draw the payoff diagram showing both zones (above and below barrier). Mark break-even and max loss.
PK.3 [WT] **Phoenix:** Stock drops below coupon barrier for 3 consecutive quarters then recovers. How does the memory feature work?
PK.4 **DRC:** How does the break-even calculation differ between DRC and RC?
PK.5 [WT] **KODRC:** Stock is exactly at the KI barrier. What is the delta of the embedded put? Why?
PK.6 **CRC:** Why does the bank call the note when it's performing well for the investor?
PK.7 **Airbag:** Where does the leveraged upside come from?
PK.8 **Bonus:** Stock touches the barrier for 5 seconds during an intraday flash crash then recovers. Is the bonus lost?
PK.9 [WT] **FCN:** A client says "my coupon is guaranteed so this product is safe." Correct?
PK.10 **CRA ELN:** What is the coupon if the underlying is in the range for 60 out of 90 days? Show the formula.
PK.11 **ICN:** Who benefits from the call option — the investor or the bank?
PK.12 **Digital:** What makes hedging cost spike when the underlying is near the digital strike?
PK.13 **Booster:** If participation is 200%, why is there a cap?
PK.14 **DKIP:** Name the three barriers and explain what each controls.
PK.15 **Warrant:** Why does time decay accelerate as expiry approaches?

### Swaps Family

PK.16 [WT] **IRS:** Both legs have the same PV at inception. How does anyone make money?
PK.17 **TRS:** Why would an investor pay a funding spread when they could buy the asset directly?
PK.18 **EqSwap:** How does an unexpected special dividend affect each leg?
PK.19 [WT] **VarSwap:** Why is a long variance position more dangerous than a long volatility position?
PK.20 **CDS:** CDS spreads widen 100bp but no default occurs. Who profits?
PK.21 **XCCY:** Why does the cross-currency basis exist?
PK.22 **CommSwap:** What is basis risk in commodity hedging?
PK.23 **VLSP:** When would a corporate choose VLSP over IRS?

### SRT Family

PK.24 [WT] **IR Callable:** The enhanced coupon is 5% when vanilla bonds pay 3%. Where does the extra 2% come from?
PK.25 **ZCL:** A 30-year ZCL moves roughly how many times more per basis point than a 1-year bond?
PK.26 **NCRA:** If rates leave the accrual range permanently in year 1 of a 10-year note, what does the investor receive?
PK.27 **CRA SRT:** What two risks is the investor selling simultaneously?
PK.28 **Digital CF:** What happens to the hedge when rates are exactly at the digital strike?

### STEG Family

PK.29 [WT] **V. STEG:** What market scenario causes the coupon to drop to zero?
PK.30 **RA STEG:** Why does this product require TWO conditions simultaneously?
PK.31 **C. STEG:** In what rate environment would the bank exercise the call?
PK.32 **TARN STEG:** Is early termination good or bad for the investor? Explain the reinvestment risk.

### CLN Family

PK.33 [WT] **CLN:** Explain dual credit risk. Name both exposures.
PK.34 **Skew CLN:** How does the actual recovery rate affect payout?
PK.35 [WT] **FTD:** Why does low correlation INCREASE FTD risk? Derive from first principles.
PK.36 **NTD:** Why does the correlation effect reverse between FTD and NTD?
PK.37 **CDO:** Why is correlation more important than default probability for equity tranche pricing?

### Other Family

PK.38 **SD:** Why would a client accept zero return rather than keeping money in cash?
PK.39 [WT] **FWD:** If both parties agree on the forward price, why does anyone enter the trade?
PK.40 **VO:** Explain put-call parity in one sentence.
PK.41 **ELO:** How does the retail wrapper change the economics?
PK.42 **Opt-on-RC:** Name the two decision points during the product's life.
PK.43 [WT] **ACCUM:** Why is the gearing (2×) below strike particularly dangerous?
PK.44 **DECUM:** When would a founder use this instead of selling on the open market?
PK.45 **DCI:** What determines whether the investor receives base or alternate currency?
PK.46 **SHRK:** Why would an investor accept a return cap?
PK.47 **SNOW:** What happens to the coupon after 3 consecutive missed payments if the stock recovers?
PK.48 **CLIQ:** Why do local caps make this product underperform in a trending market?
PK.49 [WT] **WOAC:** Why does the worst stock drive the entire outcome?

---

## 6.3 Infrastructure Questions (IC.1–IC.50)

### Market Conventions (§6.1)

IC.1 [WT] What is Modified Following? Give an example where it produces a different date than Following.

IC.2 Calculate the accrued interest on a $100M notional at 5% for 92 actual days under ACT/360 and ACT/365. What is the dollar difference?

IC.3 [WT] What is the difference between a Trading calendar and a Settlement calendar? When would you use each?

IC.4 A swap pays quarterly, Modified Following, using a London + New York joint calendar. The payment date falls on July 4 (US holiday, UK business day). When is the payment made?

IC.5 Explain SOFR compounding in arrears. Why is the fixing lag important?

IC.6 What is the end-of-month rule and when does it apply?

### Termsheet Literacy (§6.2)

IC.7 [WT] Name 5 date fields on a structured product termsheet and explain the purpose of each.

IC.8 A termsheet shows "Issue Price: 100%" and "Settlement: Dirty Price." What does the investor actually pay on settlement day?

IC.9 What is the role of the Calculation Agent? Why does this matter during market disruption?

IC.10 List 3 common termsheet misreading mistakes and explain why each is dangerous.

### Documentation & Legal (§6.3)

IC.11 [WT] What is the purpose of the ISDA Master Agreement? Name two events of default.

IC.12 Explain the difference between payment netting and close-out netting.

IC.13 A counterparty's CSA has a Threshold of €15M, MTA of €1M, and current exposure is €17M. How much collateral should be posted? What if exposure were €15.5M?

IC.14 What is novation? How does it differ from assignment?

IC.15 [WT] Why is close-out netting critical for capital calculation? Give a numerical example.

IC.16 What is a confirmation backlog? Why do regulators care?

### Credit & Capital Structure (§6.4)

IC.17 [WT] Draw the capital hierarchy from Senior Secured to Common Equity. Where does AT1 sit?

IC.18 A company defaults with €6B in recoveries. Capital structure: €5B senior secured, €3B senior unsecured, €2B subordinated, €1B AT1, €4B common equity. How is recovery distributed?

IC.19 Explain the difference between Full Restructuring and No Restructuring in CDS. When does the choice matter?

IC.20 What is a CoCo trigger? Explain the difference between 5.125% and 7% CET1 triggers.

IC.21 What is PONV (Point of Non-Viability)? Why does it make AT1 different from ordinary subordinated debt?

IC.22 Explain the TLAC requirement. What is its purpose?

### Valuation (§6.5)

IC.23 [WT] Classify these into Fair Value Hierarchy levels: (a) 6-month RC on Apple, (b) 5-year CDO tranche, (c) 1-year autocallable on Euro Stoxx 50, (d) 10-year worst-of on illiquid EM stocks.

IC.24 What is Day One P&L? Why is it deferred for Level 3 trades?

IC.25 What is IPV? Walk through the process.

### Product Control (§6.6)

IC.26 [WT] What is P&L Explain? Name the standard attribution components.

IC.27 Worked calculation: The desk's RC book shows +$145K P&L. Explain: Delta +$120K, Gamma −$8K, Vega −$30K, Theta +$45K, Rho +$5K, Dividend +$3K, New Deals +$15K. Calculate Unexplained. Does it pass?

IC.28 What is the difference between Flash P&L and Official P&L? Why does it matter?

IC.29 [WT] Name 5 reserve types and explain what uncertainty each covers.

IC.30 The Unexplained is +$10K every day for 20 consecutive days. Each day passes the individual threshold. Is there a problem?

IC.31 Describe the month-end PC close process in 5 steps.

### Treasury, Capital & XVA (§6.7)

IC.32 [WT] What is FTP? Why is it called the "hidden killer" of structured product margins?

IC.33 A 3Y ELN has 6% coupon, bond yield 3.50%, option premium 3.80%. FTP is 1.80%. What is the desk margin? Is the product profitable?

IC.34 Name 5 XVA adjustments and explain what real-world cost each captures.

IC.35 [WT] What is RAROC? Why is it more informative than revenue alone?

IC.36 Trade A earns $1M margin, consumes $50M capital. Trade B earns $350K margin, consumes $5M capital. Which is better for the bank? Why?

IC.37 What is the FTP expected-life problem for autocallables? Why is it controversial?

IC.38 What is the LCR? How do autocallable products affect it?

### Model Risk (§6.8)

IC.39 [WT] Name the stages of the model lifecycle.

IC.40 What is a challenger model? Why is the difference between primary and challenger useful?

IC.41 The desk uses a 2-factor Hull-White model with 500 Monte Carlo paths for a TARN STEG. The price seems low compared to 1-factor. Diagnose.

IC.42 What is SR 11-7? What does it require?

IC.43 When can a trader override the model price? What governance is required?

### Operations (§6.9)

IC.44 [WT] Describe the 8-stage trade lifecycle from booking to maturity.

IC.45 What is the four-eyes principle? Why is it required for trade booking?

IC.46 A stock split is announced for the underlying of a Phoenix. What terms need adjustment? What systems need updating?

IC.47 What is a trade break? Name 4 types and give an example of each.

IC.48 Explain the settlement fail escalation process.

IC.49 What is static data? Why is it "insidious" when wrong?

IC.50 Describe the corporate action adjustment cascade under ISDA Equity Definitions.

---

## 6.4 Infrastructure Calculations (IF.1–IF.15)

IF.1 **Day Count:** $50M notional, 4.5% rate, 91-day period. Calculate accrued interest under (a) ACT/360, (b) ACT/365, (c) 30/360. (Answer: (a) $568,750, (b) $560,959, (c) $562,500. Spread between highest and lowest: $7,791.)

IF.2 **Modified Following:** Payment due Saturday, March 31. London calendar. What date? (Answer: March 31 is Saturday → Following would be Monday April 2 → crosses month boundary → Modified Following moves BACKWARD to Friday March 30.)

IF.3 **CSA Collateral:** Threshold €10M, MTA €500K, current exposure €11.2M. How much collateral? (Answer: €11.2M − €10M = €1.2M. €1.2M > MTA → post €1.2M.)

IF.4 **CSA Collateral (Edge Case):** Same CSA, exposure €10.4M. (Answer: €10.4M − €10M = €400K. €400K < MTA (€500K) → NO collateral posted.)

IF.5 **Recovery Waterfall:** Company defaults with €8B recovery. Capital: €5B sr secured, €4B sr unsecured, €3B sub, €1B AT1, €5B equity. Distribute. (Answer: Sr Secured receives €5B (full). Sr Unsecured receives remaining €3B out of €4B owed = 75% recovery. Sub receives €0. AT1 receives €0. Equity receives €0.)

IF.6 **CDS Pricing:** CDS spread = 200bp, assumed recovery = 40%. Implied annual PD? (Answer: PD = Spread / (1 − Recovery) = 200bp / 0.60 = 333bp ≈ 3.33%.)

IF.7 **P&L Explain Tolerance:** Actual P&L = +€500K. Explained = +€460K. Unexplained = +€40K. Threshold = 10%. Pass or fail? (Answer: €40K / €500K = 8% < 10% → PASS.)

IF.8 **Bid-Offer Reserve:** Book of 50 RCs on illiquid mid-cap stocks, EUR 1M notional each, average bid-offer spread 3% of notional. Calculate total bid-offer reserve. (Answer: 50 × EUR 1M × 1.5% (half-spread) = **EUR 750,000**.)

IF.9 **FTP Margin:** 5Y ELN, coupon 7%, bond yield 4%, option premium 4.5%, FTP 2.40%. Desk margin? (Answer: Revenue = 4% + 4.5% = 8.5%. After coupon (−7%) and FTP (−2.40%) = **−0.90%.** Product destroys value.)

IF.10 **RAROC:** Revenue $800K, costs $200K, expected loss $100K, capital consumed $10M. RAROC? (Answer: ($800K − $200K − $100K) / $10M = $500K / $10M = **5.0%.** Below typical 10-12% hurdle rate → trade destroys shareholder value.)

IF.11 **SA-CCR Exposure:** Replacement Cost = $5M, PFE = $3M. Calculate EAD. (Answer: EAD = 1.4 × ($5M + $3M) = 1.4 × $8M = **$11.2M**.)

IF.12 **Netting Benefit:** Without netting: 100 trades with positive MTM = $500M. 100 trades with negative MTM = $480M. Credit exposure without netting? With netting? (Answer: Without: $500M. With: $500M − $480M = **$20M.** Capital savings: 96%.)

IF.13 **VarSwap P&L:** Strike = 20 vol (400 variance). Realized = 25 vol (625 variance). Vega notional = $100K. P&L? (Answer: (625 − 400) × $100K / (2 × 20) = 225 × $100K / 40 = **$562,500**.)

IF.14 **Autocall FTP Problem:** Product has 5Y legal maturity, 1.5Y expected life. 5Y FTP = 2.40%, 1.5Y FTP = 1.30%. Impact on coupon of using one vs the other? (Answer: Difference = 1.10% p.a. On a $10M note, that's $110K/year in coupon difference. Using 5Y FTP makes the product 1.10% less competitive.)

IF.15 **PPN Participation:** 5Y ZCB costs $78 (5% rate environment). Desk margin $1. ATM call costs $15. Participation rate? (Answer: Residual = $100 − $78 − $1 = $21. Participation = $21 / $15 = **140%** (capped in practice). In a 1% rate environment: ZCB costs ~$95, residual = $100 − $95 − $1 = $4, participation = $4/$15 = **26.7%.** Rate environment dominates PPN economics.)

---

## 6.5 Structuring Logic Questions (SL.1–SL.12)

SL.1 [WT] A retail client wants yield enhancement. Maximum product complexity you can recommend under the persona framework?

SL.2 Name the 10 steps of the structurer decision model (Solutions Manual §1.1).

SL.3 A client wants "safe income." Why is CRA SRT wrong? (SM AP-7)

SL.4 A PB client wants protected equity growth but rates are at 1%. Walk through why PPN is problematic.

SL.5 [WT] Explain the "persona filter" (Step 3.5). Why does it exist?

SL.6 A client wants to sell vol. Why is short VarSwap dangerous? What alternative achieves similar economics with bounded risk? (SM AP-4)

SL.7 What is the difference between a complexity governance violation and a suitability violation?

SL.8 A pension fund wants CMS spread income. Curve is flat. Walk through the decision framework and explain why you would reject STEG. What do you recommend instead?

SL.9 Two proposals for a PB client: Phoenix on single stock (14% coupon) vs WOAC on 4 stocks (22% coupon). Walk through comparative selection.

SL.10 [WT] A client insists on a CDO tranche. They are "Private Banking." What governance steps must you take?

SL.11 Design a product for an insurance company needing 4% income for 10 years with capital protection and curve steepening tolerance. Walk through all 10 steps.

SL.12 A structurer proposes FTD for a client who has never traded credit. The client's complexity cap allows it. Is this appropriate?

---

## 6.6 Case Interview Questions (D.1–D.14)

### Product Cases (D.1–D.8 — preserved from V1)

**CASE D.1 — The Conservative Retiree** (Beginner | Sales)
Client: "€500K in savings. Need this to last 20 years. Can't afford to lose any of it, but savings accounts pay nothing."
*Expected: SD for first €100K (deposit insurance) + PPN for remainder. Rejected: RC (can't lose).*

**CASE D.2 — The Tech VP's Stock Concentration** (Intermediate | Structuring)
Client: "200,000 shares vesting over 2 years. Want to lock in value without triggering a public sale."
*Expected: DECUM — sells shares at premium with KO protection. Rejected: ACCUM (wrong direction).*

**CASE D.3 — The Yield-Hungry Trustee** (Intermediate | Structuring)
Client: "Trust distributes 6% annually. Bond yields are 3%. Trust deed prohibits equity."
*Expected: IR Callable. Rejected: RC/Phoenix (equity prohibited).*

**CASE D.4 — The Macro Hedge Fund** (Advanced | Trading)
Client: "Realized vol will be significantly higher than implied. Want convex exposure."
*Expected: Long VarSwap — variance payoff is quadratic. Rejected: Straddle (linear, not convex).*

**CASE D.5 — The Risk Manager's Nightmare** (Advanced | Risk)
Internal: "Desk sold large WOAC to PB client. 5 stocks, 65% barrier. Identify top 3 risks and design a stress test."
*Expected: (a) Single-stock crash, (b) Correlation breakdown, (c) Liquidity. Plus suitability question.*

**CASE D.6 — The Model Validator's Challenge** (Expert | Model Validation)
Internal: "TARN STEG priced with 2F Hull-White, 500 MC paths. Price seems low vs 1-factor."
*Expected: 500 paths insufficient (need 50K+). 2F captures stochastic spread dynamics → plausible explanation.*

**CASE D.7 — The Currency Treasurer** (Beginner | Sales)
Client: "European company receiving USD. Need to budget fixed EUR/USD for 12 months."
*Expected: Monthly FX forward strip. Rejected: XCCY (overkill), DCI (not hedging).*

**CASE D.8 — The Credit Analyst's First Trade** (Intermediate | Structuring)
Client: "Strong views on 5 IG credits. Want exposure to all 5 without buying 5 bonds."
*Expected: 5 individual CLNs. Rejected: FTD (unwanted correlation risk). Tests restraint.*

### Infrastructure Cases (D.9–D.14 — NEW)

**CASE D.9 — The P&L Explain Challenge** (Intermediate | Product Control)
Scenario: "You're a new PC analyst. Flash P&L shows the desk made €2M. By 2pm, P&L Explain shows €1.6M explained, €400K unexplained (25%). Trader says 'just noise.'"
*Expected: Do NOT accept. Investigate: challenge marks, check bookings, check model calibration, check corporate actions, check data feeds. Escalate if unresolved. The trader's dismissal is itself a red flag.*

**CASE D.10 — The CLN Restructuring Crisis** (Advanced | Credit Risk / Legal)
Scenario: "CLN references a European bank that announces voluntary debt restructuring — extending maturity 3 years, cutting coupon 100bp. CDS documented under NR. Sales fielding calls from nervous investors."
*Expected: Under NR, restructuring is NOT a credit event → no CDS payout → investors suffer real loss with no hedge payout. Under FR, restructuring IS a credit event → protection pays. The restructuring clause choice determined the outcome at inception.*

**CASE D.11 — The Autocall Operations Day** (Intermediate | Operations)
Scenario: "A Phoenix autocallable on Siemens triggers autocall. Euro Stoxx closes at 101% of initial. Walk through the operational steps."
*Expected: (1) Capture fixing from correct source (Xetra closing). (2) Compare to autocall barrier (100%). (3) 101% ≥ 100% → autocall triggered. (4) Calculate redemption: 100% notional + accrued coupon + any memory coupons. (5) Schedule settlement (T+2 from observation). (6) Notify counterparty. (7) Close trade in NEMO. (8) PC verifies final P&L. (9) Trader unwinds hedges.*

**CASE D.12 — The XVA Pricing Decision** (Advanced | Treasury / Structuring)
Scenario: "A structurer proposes a 5-year CLN to an uncollateralized corporate counterparty. Walk through the XVA charges and determine whether the trade is profitable."
*Expected: CVA (counterparty default risk), FVA (funding uncollateralized exposure), KVA (5Y capital consumption), MVA (if UMR applies). Total XVA = $1.70 per $100 notional (illustrative). If desk margin < XVA, trade destroys value.*

**CASE D.13 — The Corporate Action Emergency** (Intermediate | Operations)
Scenario: "Friday 4pm: a 2-for-1 stock split is announced for the underlying of 15 outstanding Phoenix autocallables. Systems must be updated by Monday morning."
*Expected: Adjust strike, barriers, and unit quantities by split ratio. Update NEMO, Sophis, and Murex. Verify all observation dates. Notify counterparties. Four-eyes check on each adjustment. Monday morning: verify fixings reference post-split prices. Failure to adjust = every subsequent calculation is wrong.*

**CASE D.14 — The Reserve Governance Test** (Expert | Product Control)
Scenario: "The desk requests release of €500K model reserve on a CDO tranche position, arguing that a recent secondary trade confirms the model price. The quarterly target is under pressure."
*Expected: Reserve release requires Valuation Committee approval. One secondary trade is not sufficient — is the trade comparable (same tranche, same portfolio)? Is the trade at arm's length? Is the desk under P&L pressure (conflict of interest)? Release criteria: genuine reduction in uncertainty, not P&L management. PC must push back if justification is insufficient.*

---

## 6.7 Desk-Specific Questions (DS.1–DS.40)

### Structuring (DS.1–DS.5)

DS.1 A client pushback: "Your competitor offers 15% Phoenix coupon. You offer 12%. Why choose yours?"
DS.2 [WT] Design a product: 5% income, capital protection above 70%, 2-year maturity, equity underlying.
DS.3 Sales asks to lower RC barrier from 70% to 60% to increase coupon. Implications?
DS.4 Client wants CMS spread income but curve is flat. Design a product. What trade-offs?
DS.5 Design a capital-protected product with 70%+ participation in a 1% rate environment.

### Trading (DS.6–DS.10)

DS.6 You just sold a Phoenix. Walk through the day-1 hedge.
DS.7 [WT] Your RC book has $50M notional with barriers at 70%. Market is at 75%. Top 3 concerns?
DS.8 Overnight, one stock in your WOAC basket drops 15%. Others unchanged. Impact and first 3 actions?
DS.9 Your VarSwap book shows +$2M P&L. Vol unchanged. Spot moved 3%. Explain.
DS.10 [WT] Your barrier proximity metric hits amber — 60% of notional within 5% of barrier. What do you do?

### Sales (DS.11–DS.14)

DS.11 Explain a CDO in 30 seconds to a non-derivatives client.
DS.12 Client asks why WOAC coupon is so much higher than Phoenix. Explain without using "correlation."
DS.13 [WT] Client: "Structured products are just ways for banks to rip off investors." Respond.
DS.14 Client wants to switch from Phoenix to ACCUM. Walk through why this is a fundamental risk profile change.

### Risk (DS.15–DS.18)

DS.15 [WT] Name top 3 risks for a CLN. Which one do most investors forget?
DS.16 Design a stress test for: 1 Phoenix, 1 WOAC, 1 VarSwap long.
DS.17 A limit breach occurs: RC barrier proximity exceeds threshold. What do you do?
DS.18 Design risk limits for a new CDO correlation trading desk.

### Model Validation (DS.19–DS.22)

DS.19 [WT] What pricing model for a Phoenix autocallable? Why?
DS.20 Local vol surface fails in the wings. Impact on barrier pricing?
DS.21 MC vs PDE for a TARN STEG. Which is better? Why?
DS.22 Back-test shows VarSwap model overprices by 2%. Diagnose.

### Product Control (DS.23–DS.28) — NEW

DS.23 [WT] Walk through the daily P&L Explain process for an equity derivatives desk.
DS.24 The desk's flash P&L is consistently €100K higher than official. What does this pattern suggest? What investigation do you launch?
DS.25 You discover a €2M IPV break on a CDO tranche position. The trader says the broker quote is stale. What steps do you take?
DS.26 A new RC trade is booked. The manufacturing margin is $500K (Day One P&L). How should this be treated for a Level 2 product? For a Level 3 product?
DS.27 [WT] Describe the reserve adequacy review process. Who proposes? Who approves? How often?
DS.28 The desk requests reserve release of €300K citing improved liquidity. What evidence do you require?

### Operations (DS.29–DS.34) — NEW

DS.29 [WT] A new Phoenix is booked. What fields do you verify in the four-eyes check?
DS.30 A coupon payment for a CLN failed to settle. Describe your investigation steps.
DS.31 You discover a trade break: NEMO shows 10,000 shares, settlement system shows 10,500. How do you investigate?
DS.32 An autocall observation date falls on a national holiday. What happens? (Answer depends on the product's business day convention and calendar — see §6.1.)
DS.33 [WT] What is the golden source for: (a) counterparty data, (b) instrument data, (c) market data, (d) settlement instructions?
DS.34 A confirmation has been outstanding for 8 business days. What is the risk and what action do you take?

### Treasury (DS.35–DS.37) — NEW

DS.35 [WT] Explain how the FTP curve is constructed. Name the three components.
DS.36 An autocallable has 5Y legal maturity but 18-month expected life. How do you set the FTP charge?
DS.37 A product consumes significant LCR due to potential short-term outflows. How does this affect pricing?

### Cross-Functional (DS.38–DS.40) — NEW

DS.38 A junior structurer says "XVA charges are just accounting adjustments, not real costs." Explain why this is wrong.
DS.39 [WT] Walk through a single trade from origination to maturity, naming every function that touches it.
DS.40 The regulator asks: "How much capital does your bank hold against its structured products book?" Walk through the relevant framework.

---

## 6.8 Regulatory & Governance Questions (RG.1–RG.30)

### Beginner (RG.1–RG.5)

RG.1 [WT] What is the difference between "suitability" and "appropriateness" under MiFID II?
RG.2 What is a PRIIPs KID and what must it contain?
RG.3 [WT] Name the three MiFID II client categories and what each means for product access.
RG.4 Why must a bank classify a structured product before distributing it?
RG.5 A retail client wants a Complexity 8 WOAC. What regulatory checks are required?

### Intermediate (RG.6–RG.15)

RG.6 [WT] Explain the "target market" under MiFID II product governance.
RG.7 What is the SRI on a PRIIPs KID? How is it calculated for an RC?
RG.8 Client receives a KID showing stress scenario return of −40%. Client says "that can't happen to a capital-protected product." Correct?
RG.9 [WT] What is "best execution" for a structured product?
RG.10 A sales person recommends a product outside the target market. What governance steps are triggered?
RG.11 How does the persona complexity cap relate to MiFID II product governance?
RG.12 A CLN has dual credit risk. How should the PRIIPs KID SRI reflect this?
RG.13 [WT] Explain the appropriateness test. When can the bank proceed despite a failed test?
RG.14 A bank structures a bespoke CDO tranche for a single institutional client. What product governance obligations exist?
RG.15 List 5 pre-trade disclosure requirements under MiFID II.

### Advanced (RG.16–RG.25)

RG.16 [WT] A retail client wants to invest €50K in a Phoenix. Annual income €40K. This is 80% of savings. Should you proceed?
RG.17 A product sold last month no longer fits the target market due to a regulatory update. What actions?
RG.18 A WOAC is offered to a "Professional" client. No suitability check required for Professionals. Is the sales person correct?
RG.19 [WT] Compare regulatory treatment of structured deposits vs structured notes under PRIIPs.
RG.20 An autocallable is redeemed early. Investor complains the bank "took their money back." How do you respond?
RG.21 List 5 controls around structured product sales.
RG.22 [WT] A bank designs a new structured product category. What steps must the manufacturer take before any product is created?

### Infrastructure Regulatory (RG.23–RG.30) — NEW

RG.23 [WT] What are the three pillars of EMIR? Explain each in one sentence.
RG.24 Which structured products must be cleared through a CCP? Which are exempt?
RG.25 What is ISDA SIMM? What does it calculate?
RG.26 Explain FRTB's desk-level model approval requirement. Why does it matter for structured products?
RG.27 [WT] What is the difference between LCR and NSFR? How do structured products affect each?
RG.28 What is MAR? Name 3 types of MNPI that a structured products desk holds.
RG.29 How do UMR margin requirements affect the pricing of non-cleared structured products?
RG.30 [WT] A trade between a London desk and a New York client. Which regulatory frameworks potentially apply simultaneously?

---

# Part 7: Whiteboard Exercises

Exercises marked [WT]. These test the candidate's ability to organize and communicate concepts visually.

## 7.1 Product Whiteboard (15)

WT.1 Draw the payoff diagram for: (a) RC, (b) PPN, (c) Phoenix at maturity.
WT.2 Draw the delta profile of a Phoenix as spot moves from 50% to 120%.
WT.3 Construct a PPN: show ZCB + call option, calculate participation rate.
WT.4 Draw the correlation sensitivity chart for FTD vs NTD.
WT.5 Decompose a CDO waterfall: show equity, mezzanine, senior, super-senior.
WT.6 Draw the VarSwap payoff vs vol (show convexity vs linear straddle).
WT.7 Show the replication portfolio for a variance swap (1/K² weighting).
WT.8 Map the STEG coupon as a function of curve steepness.
WT.9 Draw the ACCUM payoff: show above-strike (buy 1×), below-strike (buy 2×), above-KO (terminate).
WT.10 Draw the vol surface (smile/skew) and explain each region.
WT.11 Show the Greeks profile for an RC near barrier (delta, gamma spike).
WT.12 Construct the 10-step structurer decision model.
WT.13 Map the product family tree (VO → RC → Phoenix → WOAC progression).
WT.14 Draw the autocall event cascade (fixing → comparison → trigger → settlement → close).
WT.15 Show memory coupon accumulation over 4 quarters (2 missed, 1 recovered, 1 paid).

## 7.2 Infrastructure Whiteboard (13) — NEW

WT.16 [WT] Draw the P&L attribution waterfall (Delta → Gamma → Vega → Theta → Rho → Credit → Dividend → New Deals → Unexplained).
WT.17 [WT] Draw the capital hierarchy (8 layers from Senior Secured to Common Equity with recovery expectations).
WT.18 [WT] Map the CSA collateral flow: exposure calculation → threshold check → MTA check → collateral call → eligible collateral verification → settlement.
WT.19 [WT] Draw the trade lifecycle (8 stages: Capture → Enrichment → Validation → Confirmation → Settlement → Daily Maintenance → Lifecycle Events → Maturity).
WT.20 [WT] Draw the XVA bridge from model price to fair value (Model Price − CVA − FVA − KVA − MVA = Fair Value).
WT.21 [WT] Map the Fair Value Hierarchy decision tree (quoted prices? → L1. Observable inputs? → L2. Significant unobservable? → L3).
WT.22 [WT] Draw the FTP curve (tenor vs rate, show three components: external cost, term premium, liquidity premium).
WT.23 [WT] Map the settlement workflow (Trade Date → +Settlement Lag → Settlement Date → DvP Instruction → Cash/Securities Exchange).
WT.24 [WT] Draw the corporate action adjustment cascade (Calc Agent Adjustment → Modified Calc Agent → Cancellation and Payment).
WT.25 [WT] Draw the model lifecycle (Development → Documentation → Validation → Approval → Implementation → Monitoring → Material Change → Retirement).
WT.26 [WT] Show the day count comparison: $100M at 6% for 181 days under ACT/360, ACT/365, 30/360.
WT.27 [WT] Draw the Modified Following decision tree (is next business day in same month? → YES: use it. NO: go backward).
WT.28 [WT] Map the reserve governance framework (PC proposes → Valuation Committee reviews → monthly routine / quarterly deep-dive / ad hoc event → release only when uncertainty resolves).

---

# Part 8: Mock Interview Tracks

## 8.1 Structuring Track — Beginner Variant (60 min)

**Round 1 — Product Knowledge (10 min)**
Quick-fire 30-second pitches: PPN, RC, IRS, FWD, SD.

**Round 2 — Technical Deep-Dive (15 min)**
Product 1: PPN — walk through construction. Calculate participation: 3Y ZCB = $95, ATM call = $12, margin = $1.
Product 2: RC — draw payoff diagram, mark barrier, break-even, max loss.

**Round 3 — Case Study (15 min)**
"A client has €200K earning 0.2%. Wants growth but 'cannot lose money.' Returns may be modest."

**Round 4 — Comparison (10 min)**
Pair 1: PPN vs RC. Pair 2: VO vs Warrant.

**Round 5 — Anti-Pattern Spotting (10 min)**
"A colleague recommends Phoenix to a client who needs guaranteed quarterly income."

## 8.2 Structuring Track — Advanced Variant (60 min)

**Round 1:** Quick-fire: VarSwap, FTD, NCRA, WOAC, CRA SRT.
**Round 2:** Product 1: WOAC — worst-of mechanism, correlation, coupon justification. Product 2: FTD — derive correlation effect from first principles.
**Round 3:** "Insurance company wants 10Y rate income. Curve moderately steep. No call risk. Budget 3.5%+."
**Round 4:** Pair 1: FTD vs NTD. Pair 2: CRA ELN vs RA STEG.
**Round 5:** Spot 3 anti-patterns: (a) Client wants to sell vol → short VarSwap, (b) Client wants credit yield → CDO for PB client, (c) Client wants simple rate hedge → XCCY for single-currency.

## 8.3 Trading Track — Intermediate Variant (60 min)

**Round 1 — Greeks Quiz (10 min):** Delta direction, vega direction, gamma hotspots for: RC, Phoenix, PPN, CLN, IRS.
**Round 2 — Hedging Scenario (15 min):** "Sold €10M Phoenix on Nestlé. Walk through day-1 hedge."
**Round 3 — P&L Attribution (15 min):** "RC book shows +€500K. Vol flat. Spot dropped 2%. Rates unchanged. Explain."
**Round 4 — Market Stress (10 min):** "Overnight, implied vol jumps 5 points. Book: long 3 Phoenixes, short 1 VarSwap, long 2 PPNs. P&L impact?"
**Round 5 — Risk Limits (10 min):** "Barrier proximity metric hit amber. 60% of notional within 5% of barrier. What do you do?"

## 8.4 Sales Track — Beginner Variant (60 min)

**Round 1 — Elevator Pitches (10 min):** 30 seconds each to a non-derivatives client: PPN, RC, IRS, Phoenix, SD.
**Round 2 — Client Matching (15 min):** 55-year-old business owner, €2M liquid, moderate risk, needs income, 100% in government bonds.
**Round 3 — Objection Handling (15 min):** "Structured products are hidden gambling." "Why is the coupon so high?"
**Round 4 — Comparison Selling (10 min):** "Why buy this RC instead of just buying the stock and a bond?"
**Round 5 — Suitability (10 min):** Retail client wants WOAC (Complexity 8). Persona cap = 4. Client insists.

## 8.5 Risk Track — Expert Variant (60 min)

**Round 1 — Risk Identification (10 min):** Top 3 risks: CDO, TARN STEG, VarSwap (short), WOAC, NTD.
**Round 2 — Stress Test Design (15 min):** Portfolio: 1 WOAC, 1 TARN STEG, 1 short VarSwap. Design 3 scenarios and predict P&L impact.
**Round 3 — Model Risk (15 min):** "Desk uses Gaussian copula for CDO. You know it underestimates tail risk. What do you recommend?"
**Round 4 — Limit Framework (10 min):** "Design risk limits for a new structured rates desk (V.STEG, C.STEG, RA STEG, TARN)."
**Round 5 — Regulatory (10 min):** "How much capital does the bank hold against its CDO book?"

## 8.6 Model Validation Track — Expert Variant (60 min)

**Round 1 — Model Identification (10 min):** "What model for:" RC, Phoenix, VarSwap, TARN STEG, CDO.
**Round 2 — Calibration (15 min):** "Local vol surface doesn't fit WOAC's observed prices in the wings. Impact on barrier pricing?"
**Round 3 — Numerical Methods (15 min):** "Compare MC, PDE, and tree for a callable STEG."
**Round 4 — Model Limitations (10 min):** "When does BS fail for: barriers, VarSwap, autocallables?"
**Round 5 — Back-Testing (10 min):** "Phoenix model overprices by 1.5% on 3-month products but accurate on 12-month. Diagnose."

## 8.7 Product Control Track — Intermediate Variant (60 min) — NEW

**Round 1 — P&L Explain Fundamentals (10 min)**
Quick-fire: Name the 10 standard P&L attribution components. What does each capture?

**Round 2 — P&L Investigation (15 min)**
"The desk reports +$800K. Your P&L Explain shows +$600K explained, $200K unexplained. Walk through your investigation."

**Round 3 — IPV & Reserves (15 min)**
"A CDO tranche position shows a $3M difference between trader mark and the challenger model. How do you determine the appropriate reserve?"

**Round 4 — Flash vs Official (10 min)**
"For the past 3 months, Flash P&L has been consistently $150K higher than Official. What does this pattern suggest? What investigation do you launch?"

**Round 5 — Month-End Close (10 min)**
"Walk through the month-end PC close process. What does each sign-off mean?"

## 8.8 Operations Track — Intermediate Variant (60 min) — NEW

**Round 1 — Trade Lifecycle (10 min)**
"Describe the 8-stage trade lifecycle. What is the operational risk at each stage?"

**Round 2 — Booking & Reconciliation (15 min)**
"A new WOAC is booked on 5 underlyings. Walk through: what fields must be verified? What can go wrong with enrichment?"

**Round 3 — Corporate Action Scenario (15 min)**
"A 2-for-1 stock split is announced Friday afternoon for an underlying with 20 outstanding structured products. Walk through your weekend action plan."

**Round 4 — Trade Break Investigation (10 min)**
"NEMO shows a $10M notional; settlement system shows $1M. You discover this on T+3. Investigate and resolve."

**Round 5 — Settlement Fail (10 min)**
"A coupon payment failed to settle. The counterparty claims they never received instructions. What happened and how do you fix it?"

## 8.9 Treasury Track — Senior Variant (45 min) — NEW

**Round 1 — FTP (15 min):** "Explain how the FTP curve is constructed. Walk through the autocallable expected-life problem."
**Round 2 — XVA Pricing (15 min):** "A structurer proposes a 5Y CLN to an uncollateralized corporate. List every cost component between gross margin and net profit."
**Round 3 — Capital & Liquidity (15 min):** "How do LCR and NSFR requirements affect the structured products desk?"

## 8.10–8.13 Cross-Functional Tracks (Abbreviated)

### Finance (45 min)
Focus: Fair value hierarchy classification, Level 3 disclosures, Day One P&L treatment, quarter-end audit coordination. Key question: "Walk through the Level 3 disclosure in the annual report for a CDO tranche position."

### Legal / Compliance (45 min)
Focus: ISDA Schedule negotiation, CSA terms, MiFID II product governance, target market definition, suitability documentation. Key question: "The CDS on a reference entity is documented under NR. A bail-in occurs. Is the CLN investor protected?"

### Market Risk / Credit Risk (60 min)
Focus: VaR methodology, stress testing, limit framework design, correlation risk measurement, wrong-way risk. Key question: "Design a stress test for a portfolio containing WOAC, CDO equity, and short VarSwap positions."

## 8.14 Scoring Summary

| Score | Round 1 | Round 2 | Round 3 | Round 4 | Round 5 |
|:-----:|---------|---------|---------|---------|---------|
| **Excellent** | 5/5 with key risks | Correct + second-order effects | Full framework + rejected alts + governance | Clear differentiation + trap awareness | All issues identified + explains WHY |
| **Adequate** | 4/5 correct | Mostly correct, misses one dimension | Correct recommendation with reasoning | Main difference identified | Spots 2/3 issues |
| **Poor** | <3 correct | Cannot decompose | Wrong recommendation or no framework | Cannot differentiate | Misses all issues |

---

# Part 9: Interview Traps & Anti-Patterns

## 9.1 Technical Traps (TT.1–TT.20)

**TT.1 — "Delta is the probability of finishing ITM"**
*Naive:* Yes. *Wrong because:* Delta = ∂V/∂S (hedge ratio), not probability. Delta = N(d1); ITM probability = N(d2). Breaks completely for barriers, digitals, VarSwaps.

**TT.2 — "Capital-protected means risk-free"**
*Naive:* Yes. *Wrong because:* Protection is an ISSUER promise. Lehman 2008 proved issuer default destroys protection. Plus: opportunity cost, inflation risk.

**TT.3 — "Higher coupon = better product"**
*Naive:* 22% WOAC > 10% Phoenix. *Wrong because:* Coupon reflects risk sold. Higher coupon = more risk. Question is risk-adjusted value, not absolute yield.

**TT.4 — "Diversification protects WOAC investors"**
*Naive:* 5 blue-chips = diversified. *Wrong because:* WOAC worst-of mechanism makes diversification INCREASE risk. Each stock is another potential breach source.

**TT.5 — "VarSwap short = limited risk like selling insurance"**
*Naive:* Small premium, rare payout. *Wrong because:* CONVEX payout. 2× vol = 4× variance. XIV lost 96% in one day (Feb 2018). No cap on loss.

**TT.6 — "Autocall is good for the investor"**
*Naive:* Money back plus coupons. *Wrong because:* Note recalled when performing well. Investor must reinvest at lower coupons. Autocall benefits the BANK.

**TT.7 — "Guaranteed coupon means safe product"**
*Naive:* FCN coupon guaranteed = safe. *Wrong because:* Guaranteed coupon ≠ guaranteed principal. Investor can receive 8% coupon while losing 30% of capital.

**TT.8 — "CMS rate = forward rate"**
*Naive:* Same thing. *Wrong because:* CMS convexity adjustment (Jensen's inequality). CMS > forward. 10-20bp for long-dated STEG. Model-dependent.

**TT.9 — "No principal at risk = no risk (IRS)"**
*Naive:* No principal exchange = safe. *Wrong because:* 30Y IRS DV01 ≈ $2,500/bp/$1M. On $10M, 100bp rate move = ~$2.5M MTM exposure. Enormous risk despite no principal.

**TT.10 — "Low correlation = safer FTD"**
*Naive:* Diversified basket = safer. *Wrong because:* FTD is LONG correlation. Low corr = independent defaults = higher P(at least one defaults). The deepest credit concept.

**TT.11 — "Recovery rate doesn't matter for CDS"**
*Naive:* CDS spread = PD only. *Wrong because:* CDS spread ≈ PD × (1−R). Assumed 40% recovery → Lehman actual 8.6% = 33% increase in loss severity.

**TT.12 — "European and American barrier are the same"**
*Naive:* 70% barrier either way. *Wrong because:* Continuous monitoring → much higher breach probability. Pricing difference: 30-50% of option value.

**TT.13 — "Vol smile is a market anomaly"**
*Naive:* BS assumes flat vol, smile = market error. *Wrong because:* Smile reflects real risk: jump risk, stochastic vol, supply/demand for downside protection. Feature, not bug.

**TT.14 — "Monte Carlo is always the best pricing method"**
*Naive:* MC handles everything. *Wrong because:* MC is slow (convergence = 1/√N), struggles with American exercise. PDE better for 1-2 factor. Trees for simple American. Right method = product-dependent.

**TT.15 — "Correlation is constant and observable"**
*Naive:* Historical corr = 0.6. *Wrong because:* (a) Not directly observable — only implied. (b) Not constant — spikes in stress. (c) Implied ≠ realized. The most dangerous hidden risk.

**TT.16 — "PPNs are unattractive when rates are low"**
*Naive:* Low rates → low participation. *Wrong because:* Partially correct but incomplete. Low rates also reduce forward prices (cheaper calls). Net effect depends on relative impact. Features (caps, baskets) can improve participation.

**TT.17 — "Forward price = expected future spot"**
*Naive:* Market predicts stock will be at $105. *Wrong because:* Forward = Spot × e^(r-q)T. Reflects CARRY COST, not forecast. Priced by arbitrage, not prediction.

**TT.18 — "Short-selling CDS is free money in good times"**
*Naive:* Tight spreads = easy carry. *Wrong because:* Carry compensates for jump-to-default. Many small gains followed by one catastrophic loss. "Pennies in front of a steamroller."

**TT.19 — "Digital options are easy to hedge because payoff is simple"**
*Naive:* Binary = simple. *Wrong because:* Hedging is the problem. Near digital strike, delta → ∞. Dealers replicate with tight call spreads — the tighter, the larger the gamma exposure.

**TT.20 — "Gaussian copula is 'wrong' for CDO pricing"**
*Naive:* Caused 2008, should abandon. *Wrong because:* It's the market standard quotation convention. Like saying BS is "wrong" for options. Problem was governance — treating approximation as truth. Model limitations were known but not reserved against.

---

## 9.2 Infrastructure Traps (IT.1–IT.15) — NEW

**IT.1 — "Modified Following and Following are the same"**
*Wrong because:* Modified Following moves BACKWARD if crossing month boundary. Following always moves forward. Different dates → different accrual → different cash flows.

**IT.2 — "Day count doesn't matter — the differences are small"**
*Wrong because:* On $100M at 6%, ACT/360 vs 30/360 difference = $16,667 per semi-annual coupon. Over 10 years = $333K. Not small.

**IT.3 — "P&L Explain residual is noise"**
*Wrong because:* Small daily unexplained may be noise. But: (a) Large unexplained = problem requiring investigation. (b) Consistently positive unexplained = systematic issue, possibly overmarking. PC must monitor trends.

**IT.4 — "CSA threshold means no collateral required"**
*Wrong because:* Threshold is the UNSECURED amount. Exposure above threshold requires collateral. Also: MTA creates an additional gap — exposure between Threshold and Threshold + MTA is uncollateralized.

**IT.5 — "IPV is just checking Bloomberg"**
*Wrong because:* IPV is a full process: multiple sources (broker quotes, consensus services, model comparison), challenge procedures, escalation, tolerance thresholds, Valuation Committee oversight.

**IT.6 — "FTP is the risk-free rate"**
*Wrong because:* FTP = external borrowing cost + term premium + liquidity premium. Significantly above risk-free. FTP can make the difference between profitable and value-destroying products.

**IT.7 — "Reserves are just a cushion against losses"**
*Wrong because:* Each reserve covers a specific, quantified source of uncertainty: bid-offer (exit cost), model (methodology uncertainty), liquidity (market impact), parameter (input uncertainty), Day One (unverifiable inception profit). Not a generic buffer.

**IT.8 — "XVA is a back-office adjustment"**
*Wrong because:* XVA represents real economic costs the desk incurs: funding (FVA), counterparty default (CVA), capital consumption (KVA). A desk pricing without XVA is systematically selling products below cost.

**IT.9 — "Golden source means one system for everything"**
*Wrong because:* Different data types have different golden sources. Counterparty data: CRM. Instrument data: NEMO/Murex. Market data: Sophis/Murex. SSI: settlement system. Calendars: vendor/internal.

**IT.10 — "Corporate actions don't affect derivatives"**
*Wrong because:* Stock splits require strike/barrier/quantity adjustment. Mergers may trigger extraordinary events. Special dividends may adjust strike. ISDA Equity Definitions specify the adjustment cascade. A missed adjustment corrupts every subsequent calculation.

**IT.11 — "Non-cleared means unregulated"**
*Wrong because:* EMIR risk mitigation applies: timely confirmation, portfolio reconciliation, compression, dispute resolution. UMR requires bilateral margin. "Non-cleared" ≠ "unregulated."

**IT.12 — "Capital is free"**
*Wrong because:* Capital has a cost = bank's cost of equity (10-15%). A trade earning 5% RAROC when hurdle is 12% destroys shareholder value despite being nominally profitable.

**IT.13 — "Flash P&L is fine for trading decisions"**
*Wrong because:* Flash is pre-IPV, pre-reserve, preliminary. Official is verified. Trading and management decisions should reference Official. Using Flash alone is a control failure.

**IT.14 — "Model validation means the model is correct"**
*Wrong because:* Validation means the model was independently reviewed and found fit for purpose WITHIN its limitations. Every model has limitations. The validation report documents what the model CANNOT do.

**IT.15 — "The booking system handles corporate actions automatically"**
*Wrong because:* Some systems have automation, but human verification is always required. An automatically applied ratio entered incorrectly (2.0 instead of 0.5 for a reverse split) corrupts every subsequent calculation.

---

## 9.3 Behavioural Traps (BT.1–BT.17)

**BT.1 — "Tell me a trade you would put on today."**
Tests: Conviction + structured reasoning. No "right" trade. Articulate market view, product selection, risks, sizing. Excessive hedging = fail. No risk acknowledgment = fail.

**BT.2 — "This product seems risky. Convince me otherwise."**
Tests: Risk reframing. DON'T deny risk. Acknowledge, then: "The risk is compensated. The coupon reflects the probability and severity."

**BT.3 — "Walk me through your thought process."**
Tests: Structured thinking. Use the 10-step decision model. Rambling through products = fail.

**BT.4 — "The client insists on an unsuitable product."**
Tests: Compliance + diplomacy. Document concerns, explain risks, offer alternatives, escalate if insistence continues.

**BT.5 — "30 seconds — pitch me this product."**
Tests: Tier 1 clarity. What it IS, who buys it, one key risk. Cramming Tier 4 depth into 30 seconds = fail.

**BT.6 — "Your model says one thing, market says another."**
Tests: Humility. The market is right until proven otherwise. Investigate calibration, missing risk factors, liquidity premium.

**BT.7 — "Describe a time you were wrong."**
Tests: Self-awareness. Honest admission, diagnosis (not blame), process improvement.

**BT.8 — "Why structured products?"**
Tests: Genuine interest. Good: intersection of client needs, mathematical modeling, risk management. Bad: "it pays well."

**BT.9 — "Client calls in panic — stock dropped 15%, RC barrier at 70%, current level 72%."**
Tests: Client management under pressure. Acknowledge concern. State facts (still above barrier). Discuss scenarios. Discuss options (hold, sell at loss, hedge). Do NOT say "don't worry."

**BT.10 — "Explain correlation risk to a teenager."**
Tests: Communication ability. Good analogy: "If 5 friends go to different parties (low correlation), each faces independent risk — higher chance at least one gets sick. If they all go to the same party (high correlation), either all get sick or none do — the chance of exactly one getting sick is lower."

**BT.11 — "What happened in markets yesterday?"** — NEW
Tests: Market awareness. Candidates should follow major indices, vol levels, credit spreads, and rate curves daily. Not knowing yesterday's market moves signals lack of genuine interest.

**BT.12 — "The trader says the Unexplained is noise."** — NEW
Tests: Independence (for PC roles). Do NOT accept dismissal. Investigate. The trader's incentive is to minimize scrutiny; your job is to maximize transparency.

**BT.13 — "Walk me through your day."** — NEW
Tests: Role understanding. Use §6.10 Day in the Life as reference. Show you understand the rhythm: morning prep → market open → midday management → afternoon close → sign-off.

**BT.14 — "A settlement failed. The counterparty blames us."** — NEW
Tests: Operational composure. Check SSI, check payment instructions, check system timestamps. Don't assign blame before investigating. Escalate per the break resolution process.

**BT.15 — "Our competitor prices this 50bp cheaper."** — NEW
Tests: Pricing discipline. Possible explanations: different FTP, different XVA assumptions, different model, deliberately underpricing to win flow. Do NOT match blindly — explain your pricing components.

**BT.16 — "The reserve release would help us hit our quarterly target."** — NEW
Tests: Governance integrity (for PC roles). Reserves are released when uncertainty resolves, not when P&L targets are under pressure. This is a compliance test.

**BT.17 — "Why do we need model validation? The desk knows their models best."** — NEW
Tests: Independence principle. The builders cannot validate their own work — inherent incentive to overlook weaknesses. SR 11-7 requires organizational separation.

---

# Part 10: Written Assessments

## 10.1 Multiple Choice (40 Questions)

**Instructions:** Select the best answer. 60 minutes.

### Product Questions (MC.1–MC.25 — preserved from V1)

**MC.1** (Beginner) A PPN investor faces which primary risk? (a) Market risk (b) **Issuer credit risk** (c) Interest rate risk (d) Barrier breach risk

**MC.2** (Beginner) Which product is the investor SHORT volatility? (a) PPN (b) VO long call **(c) Reverse Convertible** (d) Structured Deposit

**MC.3** (Beginner) An IRS at inception has NPV of: (a) Positive for fixed payer (b) Positive for floating payer **(c) Zero for both** (d) Depends on swap rate

**MC.4** (Beginner) Which product provides deposit insurance? (a) PPN (b) CLN **(c) Structured Deposit** (d) RC

**MC.5** (Beginner) Forward price of non-dividend stock is: (a) Equal to spot **(b) Higher than spot** (c) Lower than spot (d) Unpredictable

**MC.6** (Intermediate) Phoenix coupon barrier 70%. Observation day stock at 69%. What happens? (a) Proportional coupon **(b) No coupon** (c) Autocalled (d) Barrier breached

**MC.7** (Intermediate) Which Greek causes most hedging difficulty near digital strike? (a) Delta **(b) Gamma** (c) Vega (d) Theta

**MC.8** (Intermediate) WOAC 5 stocks. Stock A −35%, B-E +10%. What drives outcome? (a) Average **(b) Stock A** (c) Stocks B-E (d) Weighted average

**MC.9** (Intermediate) CDS-bond basis is: **(a) CDS spread − ASW spread** (b) Bond yield − CDS spread (c) CDS − risk-free (d) Bond price − CDS upfront

**MC.10** (Intermediate) CLN pays higher than CDS spread because: (a) More credit risk **(b) Funding benefit from receiving cash** (c) More liquid (d) Regulatory requirement

**MC.11** (Intermediate) ACCUM gearing 2×, stock 10% below strike. Daily purchase: (a) Standard **(b) Double** (c) Half (d) Zero

**MC.12** (Advanced) FTD basket, correlation 0.3→0.7. FTD spread: (a) Widens **(b) Tightens** (c) Unchanged (d) Depends

**MC.13** (Advanced) CMS convexity adjustment is positive because: (a) CMS > LIBOR **(b) Jensen's inequality from convex price-yield relationship** (c) Positive carry (d) Central clearing

**MC.14** (Advanced) VarSwap strike 20 vol (400 var). Realized 625 (25 vol). P&L per vega notional ≈: (a) 5 (b) 225/50 **(c) 5.625** (d) 12.5

**MC.15** (Advanced) Callable STEG unique risk vs vanilla STEG: (a) Credit **(b) Reinvestment risk — bank calls when curve steepens** (c) Currency (d) Operational

**MC.16** (Advanced) OPPOSITE correlation sensitivity to FTD: (a) CDO equity **(b) NTD** (c) CLN (d) CDS

**MC.17** (Advanced) TARN reaches target in year 2. Investor: (a) Lump sum **(b) Principal back, reinvest at prevailing rates** (c) Loses remaining (d) Can extend

**MC.18** (Expert) Gaussian copula, correlation 0.2→0.5, equity tranche spread: (a) Widens **(b) Tightens** (c) No effect (d) Ambiguous

**MC.19** (Expert) VarSwap replication option weights proportional to: (a) 1/K **(b) 1/K²** (c) K (d) Equal

**MC.20** (Expert) SNOW missed coupons 1-4. Stock recovers in period 5: (a) Period 5 only **(b) Periods 1-5 cumulative** (c) Last 2 + current (d) Depends on memory

**MC.21** (Intermediate) DCI: USD deposited, EUR/USD put strike 1.05, maturity rate 1.02. Investor receives: (a) USD back **(b) EUR at 1.05 strike** (c) EUR at 1.02 market (d) Coupon only

**MC.22** (Intermediate) Which family benefits most from steep curve? (a) ELN **(b) STEG** (c) CLN (d) SRT

**MC.23** (Advanced) RC implied vol 25%, realized 15%. Who benefits? (a) Investor **(b) Desk** (c) Both (d) Neither

**MC.24** (Expert) 2F Hull-White lower TARN price than 1F because: **(a) Stochastic spread reduces expected coupon accumulation** (b) Computational error (c) 1F always overprices (d) Calibration wrong

**MC.25** (Expert) CDO models failed in 2008 because: **(a) Gaussian copula underestimated tail dependence** (b) Low rates (c) No hedging (d) Wrong rating models

### Infrastructure Questions (MC.26–MC.40) — NEW

**MC.26** (Beginner) Modified Following: payment due Saturday, January 31. London calendar. Payment is on: (a) Monday Feb 2 (b) **Friday January 30** (c) Thursday January 29 (d) Saturday January 31

**MC.27** (Beginner) The golden source for instrument data is: (a) Bloomberg (b) Reuters **(c) Booking system (NEMO/Murex)** (d) Settlement system

**MC.28** (Intermediate) P&L Explain Unexplained of $50K on $500K total P&L. Threshold is 10%. Action? **(a) Investigate — 10% = borderline, requires review** (b) Pass — exactly at threshold (c) Ignore (d) Release reserves

**MC.29** (Intermediate) CSA: Threshold €10M, MTA €500K, exposure €10.3M. Collateral posted: (a) €300K **(b) Zero (below MTA)** (c) €10.3M (d) €10M

**MC.30** (Intermediate) Which XVA is the cost of funding uncollateralized derivatives? (a) CVA (b) DVA **(c) FVA** (d) KVA

**MC.31** (Advanced) RAROC = 5%. Bank's cost of equity = 12%. The trade: (a) Is profitable **(b) Destroys shareholder value** (c) Is break-even (d) Cannot determine

**MC.32** (Advanced) SR 11-7 requires: (a) All models use Black-Scholes **(b) Independent model validation and formal governance** (c) Quarterly model replacement (d) Models validated by traders

**MC.33** (Advanced) A Day One P&L of $500K on a Level 3 trade should be: (a) Recognized immediately (b) Recognized over first year **(c) Deferred and amortized over trade life** (d) Written off

**MC.34** (Advanced) SA-CCR formula: EAD = **(a) 1.4 × (RC + PFE)** (b) RC × PFE (c) 1.4 × RC (d) RC + 1.4 × PFE

**MC.35** (Intermediate) The most common cause of a $278 cash reconciliation break on a coupon payment: **(a) Day count convention mismatch (ACT/360 vs ACT/365)** (b) Wrong counterparty (c) Missed trade (d) Rounding

**MC.36** (Advanced) Close-out netting reduces credit exposure from $500M to $20M. What made this possible? **(a) ISDA Master Agreement with enforceable netting in counterparty's jurisdiction** (b) CDS protection (c) Collateral (d) Central clearing

**MC.37** (Expert) CDS documented under NR. Reference entity restructures debt. Investor: (a) Receives full payout **(b) Receives nothing — restructuring not a credit event under NR** (c) Receives partial payout (d) Can choose to trigger

**MC.38** (Expert) FRTB desk-level model approval means: **(a) Each trading desk individually qualifies for internal models** (b) All desks use same model (c) No models allowed (d) Models approved globally

**MC.39** (Intermediate) A stock split requires adjustment to: **(a) Strike, barrier levels, and unit quantity** (b) Only strike (c) Only barrier (d) No adjustment needed

**MC.40** (Expert) FTP for an autocallable with 5Y legal maturity and 18-month expected life: (a) Always 5Y rate **(b) Based on expected life with adjustment for early termination optionality** (c) Always 18-month rate (d) Average of 5Y and 18M

**Answer Key:** MC.1(b), MC.2(c), MC.3(c), MC.4(c), MC.5(b), MC.6(b), MC.7(b), MC.8(b), MC.9(a), MC.10(b), MC.11(b), MC.12(b), MC.13(b), MC.14(c), MC.15(b), MC.16(b), MC.17(b), MC.18(b), MC.19(b), MC.20(b), MC.21(b), MC.22(b), MC.23(b), MC.24(a), MC.25(a), MC.26(b), MC.27(c), MC.28(a), MC.29(b), MC.30(c), MC.31(b), MC.32(b), MC.33(c), MC.34(a), MC.35(a), MC.36(a), MC.37(b), MC.38(a), MC.39(a), MC.40(b)

---

## 10.2 Short Answer Assessment (15 Questions)

**Instructions:** 3-5 sentences each. 45 minutes.

**SA.1** [Beginner] Explain why an RC pays an above-market coupon.
**SA.2** [Beginner] A client says "this PPN has 100% capital protection, so it's risk-free." Correct this.
**SA.3** [Intermediate] Difference between CLN and CDS. When recommend each?
**SA.4** [Intermediate] Explain the Phoenix memory feature and why it matters.
**SA.5** [Intermediate] Why does the desk prefer to sell structured products in high-vol environments?
**SA.6** [Advanced] Explain the FTD correlation paradox.
**SA.7** [Advanced] Client wants "guaranteed income" from a Phoenix. What is wrong?
**SA.8** [Advanced] What is the CMS convexity adjustment?
**SA.9** [Expert] Variance swap vs volatility swap — why is variance "convex"?
**SA.10** [Expert] "Gaussian copula caused the 2008 crisis." Accurate? Nuanced answer.
**SA.11** [Intermediate] What is P&L Explain and why does Product Control do it daily? (NEW)
**SA.12** [Intermediate] What is FTP and why is it called the "hidden killer"? (NEW)
**SA.13** [Advanced] Explain why close-out netting reduces capital requirements. Give a numerical example. (NEW)
**SA.14** [Advanced] Name three XVA adjustments and explain the real-world cost each captures. (NEW)
**SA.15** [Expert] A model validation report lists a known limitation: "not suitable for barriers below 50%." A trade is booked with a 45% barrier. What governance failure occurred? (NEW)

---

## 10.3 Mini Case Assessment (8 Cases — MCS Series)

**Instructions:** For each: (1) recommended product or action, (2) reasoning, (3) one rejected alternative, (4) key risk. 90 minutes.

**MCS.1** 65-year-old retiree, €300K, wants growth with no principal risk. Deposit rates 0.5%. Needs money in 5 years.
**MCS.2** Corporate treasurer, €10M USD receivables over 6 months. Reports in EUR. Budget certainty priority.
**MCS.3** Wealth manager client wants quarterly income >8%, some capital risk tolerance. PB cap 8. Single-stock preference.
**MCS.4** Insurance company, 15-year liability, rate-linked asset generating 4%+. Comfortable with steepening risk, NOT call risk.
**MCS.5** Hedge fund wants to express view that credit correlation will decrease. $50M risk budget. Comfortable with portfolio credit.
**MCS.6** (NEW) You are a PC analyst. The desk's CDO book shows $200K of consistently positive unexplained P&L over 15 days. Each day passes the threshold individually. What is your recommended action?
**MCS.7** (NEW) A CLN referencing a European bank is documented with MMR restructuring clause. The bank announces a voluntary subordinated debt extension. Does this trigger a credit event? What if the clause were NR?
**MCS.8** (NEW) A 2-for-1 stock split is announced for the underlying of an RC with initial spot $100, strike $100, barrier $70. What are the post-split terms? What systems need updating?

---

# Part 11: Bank-Specific Preparation

## 11.1 Preparation Matrix

| Bank | Must-Know Products | Must-Know Infrastructure | Distinctive Style | Key Preparation |
|------|-------------------|-------------------------|-------------------|-----------------|
| **Goldman Sachs** | VarSwap, CDO, options | Mental math, market views | Analytical, quantitative | Practice mental math, prepare conviction trade, know yesterday's markets |
| **JP Morgan** | Full spectrum | P&L Explain (always asked) | Operational rigor, precision | Master P&L attribution, practice desk scenarios |
| **Morgan Stanley** | Structuring depth | Solutions framework | Wealth management lens | Practice client suitability cases |
| **Barclays** | CDS, CLN, CDO, FTD | Credit risk framework | Deep credit focus | Master correlation, recovery waterfall, stress testing |
| **UBS** | Autocallables, PPN | Swiss regulatory (FINMA) | Conservative, PB-focused | Emphasize suitability, capital protection, PPN depth |
| **BNP Paribas** | STEG, CMS products | Conventions (every interview) | European rates expertise | Practice Modified Following, day count calculations |
| **SocGen** | Exotic equity, barriers | Day count, settlement | Quantitative depth | Barrier pricing, exotic Greeks, convention math |
| **Deutsche Bank** | Cross-asset | Trade lifecycle (heavily tested) | Front-to-back understanding | Master booking → settlement → reconciliation flow |
| **Citi** | Broad markets, credit | Global regulatory | Cross-border awareness | Understand EMIR + Dodd-Frank interaction |
| **HSBC** | FX/DCI, treasury | Settlement, booking, reconciliation | Asia-Pacific focus | DCI mechanics, Asian conventions, treasury products |
| **Nomura** | Phoenix/FCN, ACCUM | Asian calendars, T+2 | APAC structured products | Autocallable depth, accumulator mechanics |
| **Credit Agricole** | Rates, covered bonds | European regulatory | French rates focus | STEG structuring, ACPR awareness |
| **Standard Chartered** | EM credit, FX | Cross-border settlement | Emerging markets | EM credit analysis, FX conventions |
| **MUFG** | Japanese rates, XCCY | JGB conventions | Japanese markets | XCCY depth, BOJ policy |
| **Mizuho** | Japanese SP | Asian settlement | Japan-specific | Regulatory awareness, autocallable variants |

---

# Part 12: Career Path Guide

## 12.1 Preparation Roadmap by Career Level

### Graduate / Analyst Year 1
**Product preparation:** Master Tier 1-2 for: PPN, RC, IRS, FWD, SD, VO. Be able to draw payoff diagrams, explain construction, name key risks.
**Infrastructure preparation:** Know what Modified Following means, what a termsheet is, what P&L Explain is (conceptual level), what an ISDA Master Agreement does.
**Practice format:** Phone screen (30-second pitches), basic MC quiz, simple case study.
**Target pass rate:** 80%+ on Beginner MC questions.

### Analyst Year 2-3
**Product preparation:** Master Tier 1-3 for: Phoenix, CLN, CDS, TRS, CRC, EqSwap. Comparison pairs for all Beginner + Intermediate products.
**Infrastructure preparation:** Day count calculations (ACT/360 vs 30/360), settlement conventions (T+2, DvP), booking basics (four-eyes), CSA awareness (what is threshold, MTA).
**Practice format:** 45-minute technical interview, product decomposition, basic structuring case.
**Target pass rate:** 80%+ on Intermediate MC questions.

### Associate
**Product preparation:** Master Tier 1-3 for: WOAC, VarSwap, FTD, STEG, CRA ELN. Full comparison pair fluency. Structuring logic (10-step model).
**Infrastructure preparation:** P&L Explain (walk through components), reserve awareness (name 5 types), CSA mechanics (collateral calculation), FTP concept (why it matters).
**Practice format:** 60-minute desk round, structuring case, comparison pairs, anti-pattern spotting.
**Target pass rate:** 70%+ on Advanced MC questions.

### VP
**Product preparation:** All Tier 1-4 for Top 10 products. Expert on your product family. Cross-family awareness.
**Infrastructure preparation:** Full P&L attribution (worked examples), IPV process, reserve governance, XVA pricing, model validation basics, capital metrics (SA-CCR, RAROC).
**Practice format:** 60-90 minute desk simulation, infrastructure cases, cross-functional scenarios, senior behavioural questions.
**Target pass rate:** 60%+ on Expert MC questions.

### Director / MD
**Product preparation:** Strategic view across all products. Business economics (margin, capital, FTP). Regulatory strategy.
**Infrastructure preparation:** Full business economics (FTP curves, capital optimization, FRTB impact, LCR/NSFR). Model governance (SR 11-7). Regulatory engagement.
**Practice format:** Senior round with market views, business strategy discussion, regulatory scenario, franchise management.
**Differentiator:** Cross-functional fluency — can discuss any desk function's perspective on any product.

---

# Appendix: Role-Based Question Index

| Role | Core Questions | Infrastructure Questions | Cases | Mock Track |
|------|---------------|------------------------|-------|------------|
| **Structuring** | PK.1-49, SL.1-12, DS.1-5 | IC.7-10, IC.32-33, IC.37 | D.2-3, D.8 | §8.1-8.2 |
| **Trading** | T.1-20, DS.6-10 | IC.26-28, IC.39 | D.4 | §8.3 |
| **Sales** | PK.1-49, DS.11-14, BT.1-10 | IC.7-10 | D.1, D.7 | §8.4 |
| **Risk** | T.1-20, DS.15-18 | IC.17-22, IC.39-43 | D.5 | §8.5 |
| **Model Validation** | T.11-20, DS.19-22 | IC.39-43 | D.6 | §8.6 |
| **Product Control** | DS.23-28, IF.7-10 | IC.23-31 | D.9, D.14 | §8.7 |
| **Operations** | DS.29-34 | IC.1-6, IC.44-50 | D.11, D.13 | §8.8 |
| **Treasury** | DS.35-37, IF.9-14 | IC.32-38 | D.12 | §8.9 |
| **Finance** | DS.23-25 | IC.23-31 | D.14 | §8.10 |
| **Legal / Compliance** | RG.1-30 | IC.11-22 | D.10 | §8.10 |
| **Market Risk** | T.1-20, DS.15-18, RG.23-30 | IC.17-22, IC.39-43 | D.5 | §8.5 variant |
| **Credit Risk** | T.27-32, DS.15-18 | IC.17-22 | D.10 | §8.5 variant |

---

# Traceability

| Source Artifact | Role in Interview System V2 |
|----------------|---------------------------|
| Product DNA Atlas (frozen 2026-06-22) | Product features, complexity scores, Appendix E/F/G |
| Product Comparison Matrix (frozen) | Dimensional comparisons, decision trees, confusion pairs |
| Desk Bible v2 Parts 0–5 (frozen) | §1 (Tier 1), §11 (Tier 2), §14 (Tier 3), §15 (Risk), §19-20 (curated/synthesized) |
| Desk Bible v2 Part 6 (frozen 2026-06-25) | §6.1-§6.11 infrastructure content — source for Part 3, infrastructure questions, infrastructure traps, infrastructure calculations, PC/Ops/Treasury mock tracks |
| Solutions Manual (frozen 2026-06-22) | REFERENCED for framework, scenarios, anti-patterns — never reproduced |
| Learning Dependency Graph (frozen) | Difficulty calibration via complexity bands |
| Product Evolution Map (frozen) | Family progression for comparison pairs |
| Framework Master v1.3.1 (frozen) | Governing framework — no modifications |
| Searchability Alias Map (2026-06-25) | 198 searchable terms for navigation |
| Cross-Reference Map (2026-06-25) | Forward/reverse references between sections |

---

**Interview System V2.0 complete. 49 products × 13 roles × 15 banks × 11 infrastructure domains. 400+ questions. 40 written assessment items. 30 regulatory questions. 28 whiteboard exercises. 13 mock tracks. 35 traps (20 technical + 15 infrastructure). 15 infrastructure calculations. 5 termsheet exercises. 14 case studies. 15 infrastructure calculations. Bank-specific preparation for 15 institutions. Career-level guide from Graduate to MD. 2026-06-25.**
