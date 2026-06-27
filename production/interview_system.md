# Interview System

**Desk Bible v2 — Structured Products Interview Preparation**

**Products:** 49
**Roles:** 5 (Structuring, Trading, Sales, Risk, Model Validation)
**Difficulty Levels:** 4 (Beginner, Intermediate, Advanced, Expert)
**Questions:** 210+ (core) + 40 (written assessment) + 22 (regulatory)
**Mock Tracks:** 5 × 4 difficulty variants
**Framework:** v1.3.1 (frozen)
**Generated:** 2026-06-22

---

## Table of Contents

1. [Part 1: Interview Strategy Guide](#part-1-interview-strategy-guide)
2. [Part 2: Product Answer Library](#part-2-product-answer-library)
3. [Part 3: Comparison & Confusion Pairs](#part-3-comparison--confusion-pairs)
4. [Part 4: Question Bank](#part-4-question-bank)
5. [Part 5: Mock Interview Tracks](#part-5-mock-interview-tracks)
6. [Part 6: Interview Traps & Anti-Patterns](#part-6-interview-traps--anti-patterns)

---

# Part 1: Interview Strategy Guide

## 1.1 How Structured Products Interviews Work

### Sell-Side Expectations

| Role | Round Structure | Core Focus | Pass Signal |
|------|----------------|-----------|------------|
| **Structuring** | 3–4 rounds: technical → case → desk → senior | Product design, client suitability, complexity governance | Candidate walks through decision framework unprompted |
| **Trading** | 3–4 rounds: Greeks quiz → scenario → stress → book management | Hedging, P&L attribution, risk limits, market intuition | Candidate identifies second-order risks without prompting |
| **Sales** | 2–3 rounds: pitch → client matching → objection handling | Product explanation, suitability, regulatory awareness | Candidate explains complex product in 30 seconds to non-expert |
| **Risk** | 3–4 rounds: identification → stress test → limit → regulatory | Risk metrics, model limitations, stress scenarios, capital | Candidate names risks the desk doesn't want you to know about |
| **Model Validation** | 3–4 rounds: model choice → calibration → numerical → limitations | Pricing accuracy, model risk, back-testing, numerical stability | Candidate explains when the model fails, not just when it works |

### Buy-Side Expectations

| Role | How It Differs from Sell-Side |
|------|------------------------------|
| **Portfolio Manager / Analyst** | Focus on: hidden fees, counterparty risk, liquidity in stress, total cost of ownership. Question: "Why would you NOT buy this?" |
| **Risk (buy-side)** | Focus on: portfolio-level impact, correlation with existing holdings, tail risk contribution. Less about desk hedging, more about portfolio construction. |
| **Due Diligence** | Focus on: term sheet red flags, issuer selection, secondary market access, regulatory classification. |

### Universal Interview Principle

Every structured product interview tests one thing: **Does the candidate understand where the yield comes from?**

If the coupon is above market, someone is selling an option. If the return is leveraged, someone is paying for it. If the protection is free, it isn't — the cost is elsewhere. Every "enhanced" feature has a corresponding risk that funds it. Candidates who can identify this mechanism for any product will pass.

## 1.2 The 4-Tier Answer Framework

| Tier | Name | Time | When Used | Structure |
|:----:|------|:----:|-----------|-----------|
| 1 | **Elevator** | 30 sec | Phone screen, rapid-fire | What it IS → who buys it → one key risk |
| 2 | **Technical** | 2 min | First round, written test | Construction → components → payoff → key Greeks → one pricing insight |
| 3 | **Desk** | 5 min | Desk round | Hedging → P&L drivers → market regime → lifecycle events → common desk mistake |
| 4 | **Senior** | 10 min | Final round, MD/partner | Trade-offs vs alternatives → structural edge → regulatory → historical context → failure mode |

**Rule:** Start at the tier appropriate to the question, then go deeper if prompted. Never start at Tier 4 for a Tier 1 question — interviewers test whether you can calibrate depth to audience.

## 1.3 Role-Specific Knowledge Depth Matrix

What tier of answer each role should prepare for each complexity band:

| Product Complexity | Structuring | Trading | Sales | Risk | Model Val |
|:------------------:|:-----------:|:-------:|:-----:|:----:|:---------:|
| Beginner (2–3) | Tier 4 | Tier 3 | Tier 3 | Tier 2 | Tier 2 |
| Intermediate (4–5) | Tier 4 | Tier 3 | Tier 2 | Tier 3 | Tier 3 |
| Advanced (6–7) | Tier 3 | Tier 3 | Tier 2 | Tier 3 | Tier 4 |
| Expert (8–10) | Tier 3 | Tier 2 | Tier 1 | Tier 4 | Tier 4 |

**Reading this table:** A structuring candidate must know Beginner products at Tier 4 depth (can discuss trade-offs, regulatory context, historical failures). A sales candidate needs Expert products at Tier 1 only (can explain what a CDO is in 30 seconds, but won't be asked about copula calibration).

---

# Part 2: Product Answer Library

## Top 10 Interview Products — Full 4-Tier Treatment

Products ranked by interview frequency (Matrix View 7).

---

### RC — Reverse Convertible (Complexity 3) — §5.1.2

**Tier 1 — Elevator (30 seconds)**
A Reverse Convertible is a short-term note that pays an above-market coupon in exchange for the investor accepting equity downside risk below a barrier. The investor is effectively selling a put option — the put premium funds the enhanced coupon. If the stock stays above the barrier, full principal is returned. If it breaches, the investor bears full equity losses below the strike.

**Tier 2 — Technical (2 minutes)**
Construction: Bond + short knock-in put. The coupon = bond yield + put premium − FTP − desk margin. For an 8% coupon: ~2% bond yield + ~7.5% put premium − 0.5% FTP − 1% margin. Payoff at maturity: above barrier → 100% principal; below barrier → Principal × (Final/Initial). Key Greeks: short vega (investor loses from rising vol), short gamma near barrier (discontinuous payoff creates hedging difficulty), delta approaches −1 below barrier. Pricing insight: the barrier level sets the put strike — a 70% barrier means the investor sells a 70% strike KI put. Lower barrier = less premium = lower coupon, but more protection.

**Tier 3 — Desk (5 minutes)**
Hedging: Desk is long the KI put → delta-hedges by selling stock as spot falls (buys as spot rises). Near barrier: gamma spikes — the desk must trade larger volumes in a falling market, creating adverse execution. P&L drivers: vol moves (desk is long vega), barrier proximity (gamma P&L), time decay (desk earns theta). Market regime: RCs are most attractive in high-vol environments because put premiums are rich, producing fat coupons. In low-vol regimes, coupons compress to 4–6%, barely above bond rates. Desk mistake: underestimating gap risk — stock drops 15% overnight on earnings, barrier breached with no opportunity to hedge through.

**Tier 4 — Senior (10 minutes)**
RC vs PPN: opposite risk profiles — RC sells vol (short put), PPN buys vol (long call). Client who says "I want protection" should get PPN, not RC. RC vs DRC: DRC replaces coupon with purchase discount — mathematically equivalent in many cases but clients perceive them differently (coupon = income, discount = value). See Solutions Manual §AP-1 for the protection anti-pattern. Regulatory: MiFID II product governance requires RC to be classified as yield-seeking with conditional capital risk. PRIIPs KID must show SRI (Summary Risk Indicator) that captures barrier breach probability. Failure mode: 2008 — Lehman-issued RCs defaulted on the issuer leg, not the equity leg. Investors who thought barrier risk was their main concern lost everything to credit risk.

---

### Phoenix — Phoenix Autocallable (Complexity 6) — §5.1.3

**Tier 1 — Elevator**
A Phoenix is an autocallable note that pays conditional coupons if the underlying stays above a coupon barrier, and redeems early at par if the stock exceeds an autocall trigger. Most traded autocallable globally. Key risk: barrier breach at maturity causes capital loss; autocall means the bank terminates the product when it's performing well for the investor.

**Tier 2 — Technical**
Construction: Bond + short KI put + short series of digital options (coupon) + autocall trigger. Coupon is conditional: paid only if spot ≥ coupon barrier on observation date. Memory feature (common): missed coupons accumulate and are paid when the condition is next met. Autocall: if spot ≥ autocall trigger (usually 100% of initial), note redeems at par + coupon. Greeks: complex vega profile — concentrated near barriers. Delta shifts dramatically across observation dates. Pricing insight: autocall shortens expected life, reducing put premium available for coupon vs a vanilla RC.

**Tier 3 — Desk**
Hedging: Path-dependent — delta-hedging must account for autocall probability at each observation. Near coupon barrier: digital risk creates gamma spike. Between observations: relatively calm. On observation dates: concentrated flow as dealers adjust. P&L drivers: realized vs implied vol spread (desk is short vol), time between observations (theta collection), and barrier proximity. Market regime: High vol = high coupon (premium-rich puts) but also higher barrier breach probability. In a 2020-style crash, Phoenix coupons stop and barriers breach — worst case. Desk mistake: treating memory feature as minor — in recovery scenarios, the accumulated coupon payout can be a significant cash event.

**Tier 4 — Senior**
Phoenix vs FCN: FCN pays guaranteed coupon (lower) vs Phoenix conditional coupon (higher). Client who needs predictable income should use FCN; client who tolerates coupon uncertainty for higher yield should use Phoenix. Phoenix vs WOAC: WOAC adds worst-of basket — dramatically higher coupon (15–25% vs 8–12%) but correlation risk means one stock crashing triggers loss on full notional. See Solutions Manual scenarios 2.4, 3.5 for escalation logic. Regulatory: in Europe, Phoenix is the product regulators scrutinize most. PRIIPs KID must model autocall probability, which varies significantly by methodology. Failure mode: serial autocall in a gently rising market — investor earns 2 coupons and gets money back, then reinvests at lower coupon because vol has dropped. The "good scenario" creates reinvestment risk.

---

### IRS — Interest Rate Swap (Complexity 3) — §5.2.1

**Tier 1 — Elevator**
An IRS exchanges fixed-rate payments for floating-rate payments on a notional amount. No principal changes hands. Used by corporates to lock in borrowing costs and by institutions to manage duration. Key risk: mark-to-market exposure on long-dated swaps can be very large despite no principal at risk.

**Tier 2 — Technical**
Construction: Two legs — fixed payer delivers fixed coupons, floating payer delivers LIBOR/SOFR resets. Both legs have identical present value at inception (swap rate = par rate). Duration of fixed leg ≈ maturity × DV01. Greeks: DV01 (dollar value of 1bp move) is the primary risk metric. Convexity matters for large rate moves. No vega unless the swap has embedded options. Pricing insight: swap rate is determined by the forward curve — it's the fixed rate that makes the PV of the fixed leg equal to the PV of the expected floating payments.

**Tier 3 — Desk**
Hedging: Dealers warehouse swap positions and hedge with government bonds, futures, or offsetting swaps. The desk earns the bid-ask spread. P&L drivers: curve movements (parallel shift, twist, butterfly), funding costs (the desk must fund the cash flows), and counterparty credit (CVA/DVA). Market regime: steepening curve → existing receive-fixed positions gain value (fixed leg worth more as rates rise less than implied). Desk mistake: ignoring convexity on large DV01 positions — a 50bp parallel shift creates more P&L than 50 × DV01 due to second-order effects.

**Tier 4 — Senior**
IRS vs VLSP: VLSP adds features (caps, floors, amortization, step-ups) for clients whose cash flow profile doesn't match vanilla IRS. A corporate with declining notional should use amortizing IRS, not vanilla. See Solutions Manual scenario 4.1 for the VLSP/IRS relationship (note: Atlas complexity ordering places VLSP at 2, below IRS at 3, but IRS is the default in practice). Post-2008 evolution: central clearing mandate moved IRS from bilateral OTC to clearinghouse. This reduced counterparty risk but introduced margin requirements, changing the economics for end-users. SOFR transition: LIBOR discontinuation required repricing of legacy IRS books — the spread adjustment between LIBOR and SOFR created winners and losers on existing positions.

---

### CDS — Credit Default Swap (Complexity 5) — §5.2.5

**Tier 1 — Elevator**
A CDS is insurance on a bond. The protection buyer pays a quarterly premium (the spread) to the protection seller. If the reference entity defaults, the seller pays the buyer the loss. Used for hedging credit exposure and for taking speculative credit views without owning the bond.

**Tier 2 — Technical**
Construction: Protection buyer pays quarterly premium (CDS spread × notional / 4). Protection seller pays loss-given-default (LGD = 1 − recovery rate) × notional if a credit event occurs. Standard recovery assumption: 40% for senior unsecured. Key mechanics: ISDA standard credit events (failure to pay, bankruptcy, restructuring). Settlement: physical (deliver bond, receive par) or cash (receive par − recovery). Greeks: CS01 (dollar value per 1bp spread move), recovery sensitivity, jump-to-default risk. Pricing insight: CDS spread ≈ (1 − recovery) × annual default probability / discount factor, simplified.

**Tier 3 — Desk**
Hedging: Market-making desks hedge CDS positions with bonds (basis trades), other CDS (curve trades), or index CDS (macro hedge). The CDS-bond basis (CDS spread − asset swap spread) should be zero in theory but persists due to funding, delivery option, and liquidity differences. P&L drivers: spread moves (most daily P&L), basis moves, recovery rate assumptions, and jump risk. Market regime: spread widening benefits protection buyers; tightening benefits sellers. In stress, CDS liquidity can evaporate for single-name but index CDS (CDX, iTraxx) remain liquid. Desk mistake: assuming CDS-bond basis is stable — in 2008, the basis blew out to 300+ bps, creating massive losses for basis traders.

**Tier 4 — Senior**
CDS vs CLN: CDS is unfunded (no cash upfront, pure swap), CLN is funded (investor buys note, cash at risk). The funding difference matters: CLN investors face dual credit risk (reference entity + note issuer). CDS provides cleaner credit isolation. See Solutions Manual scenario 5.1 for the funded/unfunded progression. Big Short context: CDS on mortgage-backed securities allowed investors to short the housing market without owning bonds. This created moral hazard — protection buyers profited from defaults they had no economic interest in preventing. Regulatory: CDS is now centrally cleared for standardized contracts (single-name CDS above threshold, index CDS). Non-cleared CDS requires bilateral margin posting under UMR (Uncleared Margin Rules).

---

### PPN — Principal Protected Note (Complexity 2) — §5.1.1

**Tier 1 — Elevator**
A PPN guarantees 100% principal return at maturity plus participation in equity upside. Constructed from a zero-coupon bond (protection) and a call option (growth). Key risk: issuer credit risk — the "guarantee" is only as good as the guarantor. No coupons during life.

**Tier 2 — Technical**
Construction: ZCB (priced on issuer's credit curve) + long call option (funded by the residual). If 3-year ZCB costs $94, desk margin is $1, then $5 buys a call option. If ATM call costs $15, participation = $5/$15 = 33%. Key Greeks: long delta (through the call), long vega (higher vol = more valuable call = better for investor at inception, but at inception the participation is fixed), long rho (higher rates = cheaper ZCB = more option budget). Pricing insight: PPN is long vol — the opposite of RC. This is the most important comparison in structured products.

**Tier 3 — Desk**
Hedging: Desk is short the call option → delta-hedges by buying stock as spot rises. P&L drivers: realized vol vs implied vol (desk sold the call at implied, hedges at realized), interest rate moves (affect ZCB value), time decay (desk earns theta on the option). Market regime: PPNs work best in high-rate environments — cheap ZCB leaves more budget for the call, producing attractive participation (60–80%). In low-rate environments, ZCB costs $97+, leaving $2 for the call — participation drops to 20–30%, barely worth marketing. Desk mistake: pricing the ZCB on the wrong credit curve — using risk-free rates instead of the issuer's funding curve overstates the option budget.

**Tier 4 — Senior**
PPN vs SD: Both are capital-protected with equity participation. SD is a deposit (deposit insurance applies, typically capped at €100K). PPN is a note (issuer credit risk, no deposit insurance, but no cap). For retail clients below the deposit insurance threshold, SD may be strictly better. Above threshold, PPN avoids the cap but adds credit risk. See Solutions Manual scenarios 1.1, 1.5 for protection product escalation. Failure mode: Lehman PPNs in 2008 — investors with "100% protected" notes lost everything because the "protection" was a Lehman credit obligation. This redefined how regulators require product disclosure. Historical evolution: PPNs have declined in popularity since 2010 as low rates made participation unattractive. The CPPI variant (Constant Proportion Portfolio Insurance) offered an alternative but introduced gap risk.

---

### VarSwap — Variance Swap (Complexity 7) — §5.2.4

**Tier 1 — Elevator**
A Variance Swap is a pure bet on realized variance (volatility squared). The buyer pays a fixed variance strike and receives realized variance at expiry. Key risk: convex payoff — a 2× move in vol creates a 4× move in variance. Short sellers face unlimited loss. The instrument that destroyed the short-vol trade in 2018 (Volmageddon).

**Tier 2 — Technical**
Construction: Variance Swap payoff = Notional_var × (σ²_realized − K²_var), where K_var is the variance strike and σ²_realized is annualized realized variance from daily log returns. Can be replicated by a static portfolio of out-of-the-money options across all strikes (the log contract). Greeks: pure vega (linear in vol), convex in variance (key distinction from vol swap). The vega notional is typically quoted rather than variance notional: Notional_var = Vega_notional / (2 × K_var). Pricing insight: the replication portfolio requires options at ALL strikes — in practice, the desk must interpolate/extrapolate beyond traded strikes, introducing model risk.

**Tier 3 — Desk**
Hedging: Replication via strip of OTC options. The desk maintains a portfolio of puts and calls weighted by 1/K². This portfolio must be dynamically adjusted as: (a) new strikes become available, (b) vol surface moves, (c) spot moves change the relevant strike range. P&L drivers: daily realized vol vs implied (the primary source), skew (desk is long wings via the 1/K² weighting), jump risk (jumps increase realized vol disproportionately — benefits long variance). Market regime: VarSwap premium (implied variance − realized variance) is typically positive (variance risk premium). In crisis, realized explodes past implied — long VarSwap holders profit enormously. Desk mistake: quoting vega notional without calculating the maximum loss on a variance swap — there is no natural cap on realized variance.

**Tier 4 — Senior**
VarSwap vs VO: VO provides linear vol exposure with capped loss (premium). VarSwap provides convex variance exposure with unlimited loss for sellers and theoretically unlimited gain for buyers. A client who wants vol exposure should start with VO; only upgrade to VarSwap if they specifically want convexity and understand the non-linear risk. See Solutions Manual scenario 6.1 for the VO → VarSwap escalation. Volmageddon (Feb 2018): XIV (short VIX ETN) lost 96% in one day. The mechanism: short VarSwap positions required increasing amounts of hedging as vol rose, creating a feedback loop. This event permanently changed how dealers size short-vol positions. Model risk: the replication assumes continuous monitoring, no jumps, and complete option markets. All three assumptions fail in practice, creating a persistent gap between theoretical and realized hedging P&L.

---

### CDO — Collateralized Debt Obligation (Complexity 10) — §5.5.5

**Tier 1 — Elevator**
A CDO is a portfolio of 100+ credit exposures divided into tranches ordered by loss priority. Equity tranche absorbs first losses (highest yield, highest risk). Senior tranche absorbs last losses (lowest yield, lowest risk). Correlation between defaults is the dominant pricing input — more important than individual default probabilities. The instrument at the center of the 2008 financial crisis.

**Tier 2 — Technical**
Construction: Reference portfolio (100+ names) → loss waterfall → tranches defined by attachment/detachment points. Equity tranche: 0–3% (absorbs first 3% of portfolio loss). Mezzanine: 3–7%. Senior: 7–15%. Super-senior: 15–100%. Pricing: Gaussian copula (market standard despite known limitations) models joint default probability. Key input: base correlation — the implied correlation that prices each tranche using the same copula model. Greeks: tranche delta (sensitivity to individual spread moves), correlation sensitivity (the dominant risk), and jump-to-default.

**Tier 3 — Desk**
Hedging: Equity tranche hedged with index CDS (delta-neutral). Correlation risk is hedged with other tranches or left as residual. The "correlation desk" manages the book. P&L drivers: spread moves (through tranche delta), correlation moves (the primary unhedgeable risk), and recovery assumption changes. Market regime: in benign credit environments, equity tranche earns carry. In stress, defaults cluster (correlation rises), and the correlation between the hedge and the tranche breaks down. Desk mistake: treating base correlation as stable — it is calibrated to market prices and can jump discontinuously when a default occurs, causing hedge ratios to become wrong instantly.

**Tier 4 — Senior**
CDO is the apex product in the complexity hierarchy. No direct comparison within the universe — CDO vs NTD is the closest: NTD is a simplified basket (5–10 names, Nth-default trigger), CDO is the full portfolio treatment. The 2008 lesson: the Gaussian copula underestimated tail dependence. AAA-rated super-senior tranches that "couldn't lose" lost because defaults were more correlated than the model predicted. This wasn't a black swan — it was a model failure. Regulatory aftermath: Basel III capital charges for correlation trading books (CTP) are now punitive. Most banks have reduced or eliminated CDO trading. Synthetic CDO tranches still trade for capital relief purposes. Model risk: the copula choice (Gaussian, Student-t, Clayton) has enormous impact on mezzanine tranche pricing. No "correct" copula exists. This is the purest example of model risk in finance.

---

### WOAC — Worst-of Autocallable (Complexity 8) — §5.6.12

**Tier 1 — Elevator**
A WOAC is a Phoenix/autocallable linked to a basket of 3–5 stocks where the worst-performing stock drives all outcomes. The additional correlation risk funds coupons of 15–25% — far above single-stock products. Key risk: one stock crashing triggers barrier breach on full notional even if the other 4 stocks are up. Most complex product widely sold to retail.

**Tier 2 — Technical**
Construction: Basket Phoenix + worst-of observation. On each observation: autocall triggered if ALL stocks ≥ trigger. Coupon paid if WORST stock ≥ coupon barrier. Capital protection: if WORST stock ≥ KI barrier at maturity. The worst-of mechanism dramatically increases the option premium because the probability that at least one stock breaches is much higher than any single stock breaching. Greeks: short correlation (investor loses if stocks decorrelate — opposite of equity portfolio diversification), short vega per stock, path-dependent delta for each underlying.

**Tier 3 — Desk**
Hedging: Multi-asset delta hedging (one hedge per underlying) + correlation exposure. Correlation cannot be directly hedged — it's managed by portfolio composition and model reserves. P&L drivers: single-stock moves (which stock is worst changes, shifting the delta profile), realized correlation vs implied, and dispersion (when stocks diverge, worst-of P&L suffers). Market regime: WOACs work when stocks are highly correlated (all up or all down together). Dispersion events (e.g., one stock hit by idiosyncratic news while others rally) are the worst scenario. Desk mistake: pricing correlation using historical data from a calm regime, then holding through a dispersion event — realized correlation drops below implied, and the desk's short-correlation position loses.

**Tier 4 — Senior**
WOAC is the product regulators worry about most. It's sold to retail/private banking clients who are attracted by the 20%+ coupon without understanding that they're selling correlation risk on a basket. The suitability question is acute: does a private banking client understand what correlation risk means? In most cases, no. WOAC vs Phoenix: Phoenix is single-stock — the risk is simpler (one stock, one barrier). WOAC adds N−1 sources of risk. The coupon difference (12% vs 22%) entirely reflects the additional correlation premium. See Solutions Manual scenario 6.3, AP-16. Failure mode: 2020 March crash — WOACs on diversified baskets (e.g., Nestlé, Novartis, Zurich Insurance, ABB, Richemont) — the "safe" Swiss basket. Richemont fell 40% while Nestlé fell 15%. One stock broke the barrier, triggering loss on entire notional. Clients who thought "Swiss blue chips are safe" learned that worst-of converts diversification into concentration risk.

---

### ACCUM — Accumulator (Complexity 6) — §5.6.6

**Tier 1 — Elevator**
An Accumulator commits the investor to buying a fixed number of shares at a discount each day. If the stock rises above a knock-out barrier, the contract terminates (good — bought cheap). If the stock falls, the investor buys 2× the daily quantity at the same strike (bad — forced to buy more of a falling stock). Called "I'll be back" in Asia because clients return to the desk after losses.

**Tier 2 — Technical**
Construction: Daily forward purchase at strike (typically 85–95% of spot) + knock-out barrier (typically 103–105% of spot) + gearing below strike (2× accumulation). Payoff asymmetry: above strike, buy 1× daily shares at discount. Below strike, buy 2× daily shares at the same strike — the "gearing" creates leveraged loss. KO terminates all future obligations. Greeks: short put (gearing below strike creates synthetic short put), short call (KO barrier), path-dependent delta that changes daily. Pricing insight: the gearing ratio (usually 2×) means the investor's downside exposure is roughly double their upside opportunity — an asymmetric bet funded by the initial discount.

**Tier 3 — Desk**
Hedging: Daily delta adjustment as spot moves relative to strike. Near KO: gamma spikes (approaching discontinuity). Below strike: delta doubles due to gearing. The desk must source shares daily for settlement — operational complexity. P&L drivers: daily settlement vs hedge execution timing, gap risk at KO level, dividend timing (shares accumulated before ex-date carry dividend value). Market regime: ACCUMs work in gently rising markets — client accumulates at discount, KO terminates before downside risk materializes. In sharp selloffs, gearing creates accelerating losses. Desk mistake: allowing a client to build multiple overlapping ACCUMs on the same stock — the gearing stacks, and a 20% stock decline creates 4× losses across contracts.

**Tier 4 — Senior**
ACCUM vs DECUM: mirror structures. ACCUM buys shares (bullish corporate accumulating stock). DECUM sells shares (insider disposing of a position with premium). Same gearing mechanics, opposite direction. ACCUM vs FWD: FWD is a single-period forward purchase at agreed price. ACCUM is a daily forward purchase with KO + gearing. FWD has no gearing, no path dependency, and no KO — dramatically simpler. See Solutions Manual scenarios 7.4, 7.5, AP-5. Historical: the "Accumulator crisis" in Hong Kong (2008) — wealthy clients accumulated stock during the rally, then gearing kicked in during the crash. Losses of $1B+ across private banking clients. HKMA subsequently tightened suitability requirements. This product is the reason regulators created "complex product" classification in Asia-Pacific.

---

### FTD — First-to-Default Note (Complexity 7) — §5.5.3

**Tier 1 — Elevator**
An FTD is a credit-linked note on a basket of 5–10 names. The investor earns enhanced coupon but absorbs the loss if ANY one name in the basket defaults first. Key risk: counterintuitive correlation effect — LOW correlation INCREASES FTD risk because independent defaults are more likely. This is the opposite of equity diversification logic.

**Tier 2 — Technical**
Construction: Funded note + embedded credit protection on first-default in basket. Coupon = sum of individual CDS spreads × adjustment factor (less than sum because only first default triggers). Pricing: Gaussian copula applied to default times. Correlation is the key input — not individual default probabilities. As correlation → 0, FTD behaves like the worst credit in the basket (very risky). As correlation → 1, FTD behaves like each individual name (all default together or none do). Greeks: spread sensitivity per name (unequal — the widest spread dominates), correlation sensitivity (long correlation — investor benefits from higher correlation).

**Tier 3 — Desk**
Hedging: Delta-hedge with CDS on each basket name (buy protection proportional to each name's contribution to expected loss). Correlation is the unhedgeable residual. P&L drivers: individual spread moves (asymmetric — widening of the worst name hurts most), correlation moves, and jump-to-default of any name (binary loss event). Market regime: FTD is most dangerous when credit conditions are deteriorating AND correlation is falling (idiosyncratic stress). In a systemic crisis (2008), correlation rises, which paradoxically REDUCES FTD risk. Desk mistake: hedging FTD with index CDS — the index spread and the basket FTD spread have different correlation sensitivity, creating basis risk.

**Tier 4 — Senior**
FTD vs NTD: Opposite correlation sensitivity. FTD: long correlation (benefits from high corr). NTD: short correlation (benefits from low corr). A candidate who can explain WHY the correlation effect reverses demonstrates deep understanding. See Solutions Manual scenarios 5.3, 5.4, AP-13, AP-15. The mechanism: FTD triggers on first default, so independent defaults (low corr) increase the probability of at least one occurring. NTD triggers on Nth default, so clustered defaults (high corr) increase the probability of N or more occurring. CDO connection: FTD is the equity tranche of a mini-CDO (5–10 name basket, 0% attachment). Understanding FTD is the prerequisite for understanding CDO tranching.

---

## Next 15 Products — Tier 1–3 Full, Tier 4 Abbreviated

### DRC — Discount Reverse Convertible (3) — §5.1.4

**Tier 1:** RC variant where yield comes from a purchase discount instead of coupon. Investor buys note below par (e.g., $93). If stock stays above barrier: receives $100 at maturity ($7 gain = yield). Below barrier: receives shares at strike. Key risk: same as RC — barrier breach.

**Tier 2:** Construction identical to RC. The put premium is applied as a discount to the purchase price instead of periodic coupon. Economic equivalence with RC in many cases. Greeks identical. Pricing insight: DRC appeals to clients who prefer "buying cheap" over "receiving coupon" — same economics, different framing.

**Tier 3:** Desk treats identically to RC. Hedging, P&L drivers, and regime effects are the same. The only operational difference is settlement: at maturity, the redemption calculation uses the discounted purchase price as reference. Desk mistake: pricing DRC and RC on the same underlying with inconsistent vol assumptions — they should produce equivalent economics.

**Tier 4:** See RC Tier 4. Key difference: tax treatment may differ by jurisdiction — coupon is income, discount is capital gain. Some clients prefer DRC for tax efficiency. See Solutions Manual scenario 2.2.

---

### KODRC — Knock-Out Discount RC (4) — §5.1.5

**Tier 1:** DRC with an added knock-out barrier above initial level. If stock rises above KO, note redeems early at par (investor loses further upside but locks in the discount gain). Added protection: if stock falls below KI barrier AND then rises above KO, the KI is "healed." Key risk: discontinuity at both barriers.

**Tier 2:** Construction: Bond + short KI put + short KO call. Two barriers create a payoff channel. Greeks: concentrated gamma at both barriers. Between barriers, product behaves like vanilla DRC. Pricing insight: KO barrier caps the investor's upside — the KO call premium partially offsets the KI put premium, narrowing the net coupon.

**Tier 3:** Hedging is more complex than RC — two barrier surfaces to manage. Near either barrier, gamma spikes require aggressive rebalancing. P&L drivers: distance to each barrier (determines which Greek dominates). Market regime: works in range-bound markets (stock stays between barriers). Trending markets are adverse — strong rally triggers KO, strong decline triggers KI. Desk mistake: not adjusting hedge ratios when the stock crosses through the KO barrier — the position changes discontinuously.

**Tier 4:** See RC Tier 4. KODRC adds protection vs RC (barrier protection against temporary dips). See SM scenario 2.3.

---

### CRC — Callable Reverse Convertible (5) — §5.1.6

**Tier 1:** RC where the bank can call (terminate early) the note on any coupon date. Higher coupon than RC because the investor sells both a put (downside risk) and a call option (bank's right to terminate). Key risk: bank calls when the product is performing well for the investor.

**Tier 2:** Construction: Bond + short KI put + short Bermudan call (sold to the bank). Coupon = bond yield + put premium + call premium − FTP − margin. Higher coupon than RC because two options are sold. Greeks: callable products have complex vol sensitivity — the call option creates long-vega exposure for the bank (benefits from rising vol for exercise), while the short put creates short-vega for the investor.

**Tier 3:** Bank calls when the stock has risen (the put is worthless, the investor's position is "good"). This leaves the investor with a below-market return for the period held. The desk decision to call depends on: remaining put value, funding cost of the note, and alternative use of the balance sheet. Desk mistake: not understanding that early call is adverse for the investor — it looks like "getting money back" but it's actually having the profitable position terminated.

**Tier 4:** See Phoenix Tier 4 for autocall comparison. CRC call is discretionary (bank decides); Phoenix autocall is mechanical (trigger-based). SM scenario 2.4.

---

### Airbag (4) — §5.1.7

**Tier 1:** Capital-protected note with leveraged upside above strike and a cushion zone between barrier and strike. Above strike: participation >100% (e.g., 150%). Between barrier and strike: no loss. Below barrier: full equity loss. Key risk: below-barrier loss is unprotected.

**Tier 2:** Construction: ZCB + leveraged call spread + short DI put (below barrier). The leveraged upside is funded by the short put. Participation rate can exceed 100% because the investor trades away downside protection below the barrier. Greeks: long vega above strike (call exposure), short vega below barrier (put exposure). Pricing insight: the "leverage" comes from the investor accepting unlimited loss below barrier — the barrier creates an asymmetric payoff.

**Tier 3:** Hedging: similar to PPN above strike (desk is short the call), similar to RC below barrier (desk is long the put). The cushion zone between barrier and strike creates a delta-flat region. Market regime: Airbag works when the investor believes moderate declines are likely (cushion protects) but severe crashes are unlikely (below barrier is devastating). Desk mistake: mispricing the cushion zone — the probability of the stock ending between barrier and strike is a narrow range that is highly sensitive to vol assumptions.

**Tier 4:** Airbag vs Bonus: both have barrier-contingent payoffs at Complexity 4. Airbag = cushion mechanism. Bonus = minimum return mechanism. SM scenario 1.3.

---

### Bonus (4) — §5.1.8

**Tier 1:** Note that pays a minimum return (the bonus level) at maturity unless the stock breaches a barrier. If barrier untouched: investor receives max(bonus, stock return). If barrier touched: bonus is lost, investor receives actual stock return. Key risk: continuous barrier observation — one bad intraday print eliminates the bonus.

**Tier 2:** Construction: Stock + long down-and-out put (barrier put that disappears if barrier touched). The put guarantees minimum return = bonus level, as long as barrier intact. Greeks: long vega while barrier intact (put provides upside), sharp gamma near barrier (put disappears discontinuously). Pricing insight: the bonus level is funded by the limited upside — if stock rises significantly above the bonus, the investor captures full upside, but the structure is most valuable when the stock ends modestly positive.

**Tier 3:** Hedging: desk is short the DI put — hedges with vanilla puts and monitors barrier continuously. Near barrier: extreme gamma as the put oscillates between existing and extinct. P&L: dominated by barrier proximity and realized vol. Desk mistake: using European barrier for pricing when the term sheet specifies American (continuous) observation — the pricing difference is significant.

**Tier 4:** SM scenario 1.4. Bonus vs Airbag: SM scenario 1.3.

---

### Digital (4) — §5.1.12

**Tier 1:** Note paying a fixed coupon if the underlying is above a digital strike at observation dates. Full capital protection. All-or-nothing coupon: either the full coupon or zero. Key risk: binary outcome near the strike creates extreme hedging costs for the desk.

**Tier 2:** Construction: ZCB (100% protection) + short digital put options. Digital payoff: if spot ≥ strike → coupon; if spot < strike → 0. Greeks: near the strike, digital gamma (and the hedging cost) spikes — known as "pin risk." Pricing: digital options are approximated by tight call spreads (long K, short K+ε). Pricing insight: the width of the call spread used to approximate the digital determines the desk's hedging cost and the client's coupon.

**Tier 3:** The desk dreads observation dates when spot is near the digital strike — small moves create disproportionate P&L swings. Hedging digital risk requires taking large positions in vanilla options that partially replicate the digital payoff. P&L driver: distance from strike (far = easy; near = expensive). Desk mistake: not reserving enough for pin risk — if the stock oscillates near the strike on observation day, the desk's dynamic hedge generates losses from the gamma.

**Tier 4:** Digital vs CRA ELN: CRA accrues proportionally (days in range / total), Digital is all-or-nothing. Digital CF is rate-linked version. SM scenarios 1.2, 2.5.

---

### Vanilla STEG (5) — §5.4.1

**Tier 1:** A note paying coupons linked to the CMS spread (e.g., 30Y swap rate − 2Y swap rate). Coupon = leverage × max(CMS30Y − CMS2Y, 0). Capital protected. The investor bets on curve steepening. Key risk: if the curve flattens or inverts, coupon drops to zero.

**Tier 2:** Construction: ZCB + CMS spread option. The CMS rate does NOT equal the forward rate — a convexity adjustment is required because CMS pays on the CMS rate itself (linear payoff on a non-linear instrument). Greeks: sensitive to the slope of the yield curve, level of rates (through CMS convexity), and vol of rates. Pricing insight: the convexity adjustment is positive — CMS rates are higher than forward rates. This adjustment is often the largest source of model risk in STEG pricing.

**Tier 3:** Hedging: delta-hedged with swaps at different tenors (long 30Y, short 2Y to be long curve steepness). Convexity adjustments hedged with swaptions. P&L drivers: curve shape (primary), rate level (secondary, through convexity), and swaption vol. Market regime: steep curve = high coupon; flat/inverted = zero coupon. Pre-2022 low-rate environment killed STEG demand; post-2022 steepening revived it. Desk mistake: hedging only the 30Y-2Y spread without managing the convexity — rate level moves change the CMS adjustment, creating unexplained P&L.

**Tier 4:** V.STEG → C.STEG → RA STEG → TARN STEG is the complexity escalation. SM scenarios 3.1–3.4. See SM AP-10 through AP-12 for STEG family anti-patterns.

---

### CLN — Credit-Linked Note (4) — §5.5.1

**Tier 1:** A funded note where the investor earns credit spread above risk-free rate. If the reference entity defaults, the investor loses principal proportional to the loss. Combines bond exposure with specific credit risk. Key risk: DUAL credit exposure — both reference entity default AND note issuer default can cause loss.

**Tier 2:** Construction: Bond (funded by investor) + embedded CDS (investor sells protection). Coupon = risk-free rate + CDS spread − desk margin. The "funded" nature means the investor's cash is at risk — unlike CDS where no cash changes hands at inception. Greeks: CS01 (credit spread sensitivity), recovery sensitivity, jump-to-default. Pricing insight: CLN coupon should equal CDS spread minus the funding benefit the desk receives from having investor cash. If CLN coupon > CDS spread, the desk is subsidizing the product.

**Tier 3:** Hedging: desk buys CDS protection on the reference entity to offset the embedded credit risk. Residual: the basis between CLN coupon and CDS spread, plus the issuer credit risk (which cannot be hedged internally). P&L drivers: CDS spread moves, funding cost changes, and issuer-reference correlation (wrong-way risk if the bank that issued the CLN is correlated with the reference entity). Desk mistake: ignoring wrong-way risk — if the bank and the reference entity are in the same sector, defaults are correlated, and the dual-credit protection overlaps.

**Tier 4:** CLN vs CDS: SM scenario 5.1. Funded vs unfunded is the key structural choice. SM AP-13 (FTD without correlation training).

---

### FCN — Fixed Coupon Note (6) — §5.1.9

**Tier 1:** Autocallable note that pays guaranteed fixed coupon every period regardless of stock performance. If stock rises above autocall trigger, note redeems at par. If stock falls below KI barrier at maturity, investor loses capital. Most traded structured product globally (Asia).

**Tier 2:** Construction: Bond + short KI put + autocall trigger. Coupon is FIXED and GUARANTEED — unlike Phoenix where coupon is conditional. The guaranteed coupon is lower than a comparable Phoenix conditional coupon because the bank gives up the optionality on coupon payments. Greeks: similar to Phoenix but without digital coupon risk. Pricing insight: FCN coupon = Phoenix coupon − value of the conditional coupon optionality.

**Tier 3:** Desk hedging nearly identical to Phoenix. Key difference: no digital gamma on coupon observations (coupon is paid regardless). P&L drivers: autocall probability, barrier proximity, realized vol. Market regime: same as Phoenix. Desk mistake: confusing guaranteed coupon with guaranteed principal — the coupon pays no matter what, but the principal is still at risk below the barrier.

**Tier 4:** FCN vs Phoenix: SM scenario 2.1 comparison. SM AP-2.

---

### XCCY — Cross-Currency Swap (5) — §5.2.6

**Tier 1:** Exchange of cash flows in two currencies including principal exchange. Used to convert debt from one currency to another. Key risk: cross-currency basis — the persistent deviation from covered interest rate parity that creates real economic costs.

**Tier 2:** Construction: Two IRS legs in different currencies + initial and final principal exchange. At inception, principals exchanged at spot FX rate. During life: each leg pays its respective floating rate. At maturity: principals re-exchanged at the ORIGINAL FX rate (not the prevailing rate). The cross-currency basis is an additional spread added to one leg. Pricing insight: the basis exists because of supply/demand imbalances for currency funding — USD funding demand creates a persistent USD premium.

**Tier 3:** Hedging: decomposed into IRS in each currency + FX forward. The basis is the residual that cannot be perfectly hedged. P&L drivers: rate differentials between currencies, FX moves (affect the MTM of the principal exchange), and basis moves. Market regime: in USD stress (e.g., 2020 March), the XCCY basis blows out as demand for USD funding surges. Desk mistake: not recognizing that the principal exchange at maturity creates massive FX exposure — the final exchange at original rates can be deeply in- or out-of-the-money.

**Tier 4:** SM scenario 7.3. XCCY vs IRS: SM AP-6 (don't use XCCY for single-currency hedging).

---

### VO — Vanilla Option (3) — §5.6.3

**Tier 1:** A contract giving the buyer the right (not obligation) to buy (call) or sell (put) an asset at a fixed price by a fixed date. The building block of all structured products. Key risk: time decay erodes value; seller faces unlimited risk on calls.

**Tier 2:** Construction: premium paid upfront. Payoff: call = max(S−K, 0), put = max(K−S, 0). Greeks: delta (direction), gamma (acceleration), vega (vol sensitivity), theta (time decay), rho (rate sensitivity). Put-call parity: C − P = S − K×e^(−rT). Pricing: Black-Scholes for European; binomial/Monte Carlo for path-dependent. Pricing insight: implied vol is the "price" of options after accounting for all other inputs — it's what the market charges for uncertainty.

**Tier 3:** Options market-making: desk quotes bid/ask on implied vol, then delta-hedges. Profit comes from the spread and from realized vol being lower than implied (selling options) or higher (buying options). P&L: daily = gamma P&L + theta P&L + vega P&L. Desk mistake: conflating delta with probability — delta approximates the hedge ratio, NOT the probability of finishing in-the-money (though it's close for simple calls).

**Tier 4:** VO → VarSwap escalation: SM scenario 6.1. VO is the foundation product — every structured product contains embedded options.

---

### NCRA — Non-Callable Range Accrual (6) — §5.3.3

**Tier 1:** Capital-protected note paying coupon proportional to the number of days a reference rate stays within a defined range. 100% principal returned at maturity regardless. Key risk: can earn zero coupon for the entire life if rates leave the range — capital is safe but opportunity cost is a decade of zero income.

**Tier 2:** Construction: ZCB + short strip of daily digital options on the reference rate. Coupon per period = Fixed rate × (days in range / total days). Greeks: digital gamma near range boundaries (hedging cost spikes when the rate is near the edge), long vega (more vol = more boundary crossings = less coupon on average). Pricing insight: the range width determines the coupon level — wider range = more days in range = lower coupon rate (less premium from selling narrower digitals).

**Tier 3:** Hedging: daily digital options on rates require swaption strips for hedging. Near boundaries: extreme gamma. P&L: dominated by rate proximity to range edges. Market regime: NCRA works in range-bound rate environments. Trending rates (2022 hiking cycle) destroy NCRA coupons. Desk mistake: not stress-testing the range against central bank policy changes — a 200bp hiking cycle can push rates permanently outside the range.

**Tier 4:** NCRA → CRA SRT escalation: SM scenario 4.4. SM AP-8.

---

### FWD — Forward Contract (2) — §5.6.2

**Tier 1:** Agreement to buy/sell an asset at a fixed price on a future date. Both sides face unlimited gain/loss. The simplest derivative — linear payoff, no optionality. Foundation of all derivatives pricing.

**Tier 2:** Forward price F = S × e^((r−q)T) where S = spot, r = risk-free rate, q = dividend/convenience yield. No optionality → no vega. Delta = 1 (or −1 for seller). Pricing insight: the forward price is NOT a forecast — it's the arbitrage-free price determined by carry costs.

**Tier 3:** Desk hedges by holding the underlying asset (or shorting it). P&L: basis risk between forward price and hedge execution. Market regime: forward basis (forward − spot) is determined by carry costs — positive for low-dividend assets, negative for high-dividend assets. Desk mistake: confusing the forward premium/discount with a market view — it's just carry.

**Tier 4:** FWD is Tier 1 foundation. See SM scenarios 7.1, 7.2, 7.4, 7.5, 8.1.

---

### SD — Structured Deposit (2) — §5.6.1

**Tier 1:** Bank deposit with equity-linked upside. Principal 100% protected by deposit insurance (up to jurisdiction limit). Returns equity participation at maturity. Simplest structured product. Key risk: opportunity cost — zero return in flat/down markets while money is locked up.

**Tier 2:** Construction: Deposit (not note) + call option on equity index. Same economics as PPN but deposit wrapper provides deposit insurance. Greeks: same as PPN — long delta, long vega through the call. Pricing insight: the bank's funding cost on deposits is typically lower than note funding, so participation rates on SD can be slightly higher than PPN for the same maturity.

**Tier 3:** Desk perspective nearly identical to PPN. Key difference: regulatory treatment — deposit insurance creates different capital requirements for the bank. Distribution: bank branches (retail), not private banking. Desk mistake: offering SD above the deposit insurance limit — above €100K (EU) or $250K (US), the deposit insurance advantage disappears.

**Tier 4:** SD vs PPN: SM scenario 1.1. SM scenario 8.2.

---

## Remaining 24 Products — Tier 1–2 Full, Tier 3–4 Abbreviated

### ICN (3) — §5.1.11
**Tier 1:** Note where the BANK has the right to call (terminate) early. Investor earns enhanced coupon for selling call optionality. Key risk: bank calls when product is performing well.
**Tier 2:** Construction: Bond + short call option (sold to bank). Coupon = bond yield + call premium. Greeks: short vega (sold option). Pricing: Bermudan call valuation.
**Tier 3:** Similar to CRC but simpler (no put component). SM scenario 2.6.
**Tier 4:** ICN vs CRC: SM scenario 2.6. CRC = ICN + short put.

### DKIP (7) — §5.1.14
**Tier 1:** Most complex ELN. Three barriers: digital coupon barrier, knock-in put barrier, autocall trigger. Coupon is digital (above barrier = paid, below = zero) and principal is at risk if KI barrier breached. Key risk: dual conditional — coupon depends on one level, capital on another.
**Tier 2:** Construction: Bond + short digital options (coupon) + short KI put (capital) + autocall. Greeks: two sources of digital gamma (coupon strike, KI barrier) + autocall discontinuity. Pricing: Monte Carlo required.
**Tier 3:** Hedging nightmare — multiple barrier surfaces interact. SM scenario 2.5. SM AP-3.
**Tier 4:** DKIP exists for clients who want digital coupon + capital risk transfer. Only for sophisticated institutional clients.

### Booster (4) — §5.1.13
**Tier 1:** Leveraged growth note: 200%+ participation in equity upside, with a cap, and zero capital protection. If stock falls, investor loses proportionally. Key risk: no floor — full equity downside exposure.
**Tier 2:** Construction: Long leveraged call spread (provides upside leverage + cap) + forward at strike (creates equity exposure). Greeks: long delta, long gamma (below cap), zero above cap.
**Tier 3:** SM scenarios 8.3. Desk: simple to hedge — vanilla call spread. SM AP-18 for CLIQ comparison.
**Tier 4:** Booster vs Warrant: SM scenario 8.3.

### Warrant (3) — §5.1.15
**Tier 1:** Exchange-listed option certificate. Pure leveraged directional bet. Retail accessible. Key risk: total loss of premium if out-of-the-money at expiry. Time decay accelerates near expiry.
**Tier 2:** Economically identical to VO. Key differences: exchange-listed, standardized, retail accessible. Warrant premium = option value + distribution/listing cost.
**Tier 3:** Desk hedges with vanilla options. SM scenario 8.3.
**Tier 4:** Warrant vs ELO vs VO: three wrappers for the same economic exposure.

### TRS (5) — §5.2.2
**Tier 1:** Swap exchanging total return (price + dividends) of an asset for a funding rate. Provides synthetic ownership without buying the asset. Key risk: funding spread can change — "synthetic ownership" costs more than direct ownership.
**Tier 2:** Construction: Asset return leg (receiver gets price change + dividends) vs funding leg (receiver pays SOFR + spread). No principal exchange. Greeks: delta = 1 on the asset, funding sensitivity.
**Tier 3:** Desk earns the funding spread. Hedges by holding the asset. SM scenario 7.1.
**Tier 4:** TRS vs EqSwap: TRS is multi-asset (equity, credit, loans). EqSwap is equity-specific TRS. SM scenario 7.1.

### EqSwap (5) — §5.2.3
**Tier 1:** Equity-specific TRS. Exchanges equity index return for floating rate. Used for synthetic equity exposure. Key risk: dividend risk — unexpected dividend changes affect swap value.
**Tier 2:** Same construction as TRS, equity-specific. Key distinction: dividend treatment (expected vs realized) is the primary pricing risk.
**Tier 3:** Desk hedges with futures or ETFs. SM scenario 7.1.
**Tier 4:** See TRS Tier 4.

### CommSwap (4) — §5.2.7
**Tier 1:** Swap exchanging fixed commodity price for floating commodity price. Used by producers/consumers to hedge price risk. Key risk: basis risk — swap references a benchmark price, not the client's actual commodity grade/location.
**Tier 2:** Construction: Fixed payer delivers agreed price per unit. Floating payer delivers benchmark (e.g., Brent, WTI, Henry Hub). Settlement: cash, not physical. Greeks: delta to commodity price, basis sensitivity.
**Tier 3:** SM scenario 7.2. Desk hedges with commodity futures.
**Tier 4:** CommSwap vs FWD: SM scenario 7.2.

### VLSP (2) — §5.2.8
**Tier 1:** Enhanced IRS with added features: caps, floors, amortization schedules, step-up coupons. Used when standard IRS terms don't match the client's cash flow profile. Key risk: same as IRS plus the embedded option risks from the additional features.
**Tier 2:** Construction: IRS + embedded options (caps/floors as interest rate options, amortization as notional schedule). Each added feature has a price — the net is reflected in the swap rate.
**Tier 3:** SM scenario 4.1 (note: Atlas complexity 2 < IRS 3, but IRS is the market default).
**Tier 4:** See IRS Tier 4.

### IR Callable (5) — §5.3.1
**Tier 1:** Fixed-rate note where the issuer can call (redeem early). Enhanced coupon compensates investor for selling the call right. Key risk: issuer calls in a falling-rate environment — investor must reinvest at lower rates.
**Tier 2:** Construction: Bond + short Bermudan swaption (sold to issuer). Extra coupon = amortized swaption premium. Greeks: short vega (sold option), negative convexity (unlike vanilla bond).
**Tier 3:** SM scenario 4.2. Desk: hedges with swaptions.
**Tier 4:** IR Callable vs CRC: same call mechanic, different underlying (rates vs equity). Matrix Appendix A pair #22.

### ZCL (4) — §5.3.2
**Tier 1:** Zero-coupon note linked to interest rates. Capital protected. Returns rate-linked growth at maturity. Used for pension fund liability matching. Key risk: extreme duration sensitivity — 30-year ZCB moves ~30× per basis point vs 1-year bond.
**Tier 2:** Construction: ZCB + rate-linked participation. Duration = maturity (no coupon to reduce duration). Greeks: high DV01 relative to notional.
**Tier 3:** SM scenario 4.3. Desk: hedges with government bond strips.
**Tier 4:** ZCL for pension ALM — liability matching is the only compelling use case.

### CRA SRT (7) — §5.3.4
**Tier 1:** Range accrual note WITH callable feature. Highest coupon in the SRT family because investor sells TWO options (range accrual digital + call right). Key risk: dual optionality — bank calls when most valuable to investor; range exit kills coupon.
**Tier 2:** Construction: Bond + short digital strip (range accrual) + short Bermudan call. Two premiums fund the enhanced coupon.
**Tier 3:** SM scenario 4.4. Hedging: swaption + digital strip. Hardest SRT to hedge.
**Tier 4:** CRA SRT = NCRA + call. SM scenario 4.4.

### Digital CF (5) — §5.3.5
**Tier 1:** Rate-linked note with digital coupon. If reference rate is above/below a strike on observation date, full coupon paid; otherwise zero. Capital protected. Key risk: same pin risk as equity Digital but on rates.
**Tier 2:** Construction: ZCB + short digital options on reference rate. Same digital gamma issue as equity Digital but on rates — near-strike hedging cost spikes.
**Tier 3:** SM scenario 4.5. Desk: hedges with swaption strips.
**Tier 4:** Digital CF is the rate-linked analog of Digital ELN. Matrix Appendix A pair #23.

### RA STEG (7) — §5.4.2
**Tier 1:** Steepener note with range accrual: coupon accrues only when the CMS spread is within a defined range AND positive. Dual condition: curve must steepen AND not steepen too much. Key risk: zero coupon if spread leaves range.
**Tier 2:** Construction: Bond + CMS spread option + range accrual digital strip. Requires two conditions for coupon accrual.
**Tier 3:** SM scenario 3.2. Hedging: CMS spread options + digital boundary hedges.
**Tier 4:** V.STEG → C.STEG → RA STEG → TARN STEG escalation. SM scenarios 3.1–3.4.

### C. STEG — Callable STEG (6) — §5.4.3
**Tier 1:** Vanilla STEG with added bank call right. Higher coupon than V.STEG because investor sells call optionality. Key risk: bank calls when the curve steepens — precisely when the investor wants to hold.
**Tier 2:** Construction: V.STEG + short Bermudan call. Coupon = V.STEG coupon + amortized call premium.
**Tier 3:** SM scenario 3.3. SM AP-12 (don't use C.STEG for long-duration curve exposure).
**Tier 4:** See V.STEG Tier 4.

### TARN STEG (8) — §5.4.4
**Tier 1:** Steepener with target: note redeems automatically when cumulative coupons reach a target level. Highest coupon in STEG family. Key risk: early termination in the BEST scenario — target reached means money returned just as the trade works.
**Tier 2:** Construction: V.STEG + target accumulation + automatic redemption trigger. Path-dependent — requires Monte Carlo pricing.
**Tier 3:** SM scenario 3.4. SM AP-10.
**Tier 4:** TARN STEG is the most complex rate product widely traded. Only for clients with strong rate views.

### Skew CLN (5) — §5.5.2
**Tier 1:** CLN where the payout depends on the ACTUAL recovery rate, not a fixed assumption. If recovery is low, investor loses more; if recovery is high, investor loses less. Key risk: adds recovery rate uncertainty on top of default risk — a new dimension beyond vanilla CLN.
**Tier 2:** Construction: CLN + asymmetric recovery payoff (payout is convex/concave in recovery rate, depending on structure).
**Tier 3:** SM scenario 5.2. Specialist product — rarely offered directly to clients.
**Tier 4:** CLN → Skew CLN escalation. SM scenario 5.2.

### NTD (8) — §5.5.4
**Tier 1:** Basket credit note that triggers on the Nth default (e.g., 2nd, 3rd). Correlation effect REVERSES from FTD: HIGH correlation INCREASES NTD risk. Key risk: the hardest credit concept — correlation reversal between FTD and NTD.
**Tier 2:** Construction: Funded note + Nth-default credit protection. Pricing: copula model with correlation as dominant input. Higher N = more protection = lower coupon.
**Tier 3:** SM scenario 5.4. SM AP-15.
**Tier 4:** FTD vs NTD correlation reversal: SM scenario 5.4. The single most important concept in basket credit.

### ELO (3) — §5.6.4
**Tier 1:** Retail-wrapped option. Same economics as VO but packaged as a note with a term sheet instead of ISDA. Accessible to retail investors. Key risk: identical to VO, but the wrapper may add issuer credit risk.
**Tier 2:** ELO = VO in a different package. Economics identical. Pricing may differ due to: funding, margin, distribution cost.
**Tier 3:** SM scenario 8.3.
**Tier 4:** ELO vs VO vs Warrant: three wrappers, same option.

### DCI (3) — §5.6.8
**Tier 1:** FX yield enhancement. Investor deposits money and sells a put on a currency pair. If FX rate stays above strike, investor earns enhanced yield in base currency. If FX rate falls below strike, principal is converted to the alternate currency at the strike rate. Widely traded in Asia.
**Tier 2:** Construction: Deposit + short FX put. Coupon = deposit rate + FX put premium. Greeks: short FX delta, short FX vega.
**Tier 3:** SM scenario 2.7. Desk: hedges with FX options.
**Tier 4:** DCI vs RC: same mechanic (short put for yield), different asset class (FX vs equity). Matrix pair #21.

### Opt-on-RC (5) — §5.6.5
**Tier 1:** An option giving the right to enter an RC at a future date. Compound option — option on an option. Two decision points during life. Key risk: paying premium for optionality that may expire worthless.
**Tier 2:** Construction: Call option on the RC. Outer option gives right to enter; inner option is the RC's embedded put. Compound Greeks: sensitivity to both outer and inner option parameters.
**Tier 3:** SM scenario 6.2. Rarely traded — most desks recommend buying the RC later instead.
**Tier 4:** See SM scenario 6.2.

### DECUM (6) — §5.6.7
**Tier 1:** Mirror of ACCUM. Investor sells shares at premium each day. KO terminates if stock falls below barrier. Gearing above strike: sells 2× shares when stock rises. Used for insider share disposal.
**Tier 2:** Mirror of ACCUM construction. Gearing creates leveraged loss on upside (forced to sell at strike while stock rises above).
**Tier 3:** SM scenario 7.5. Same gearing risk as ACCUM in reverse.
**Tier 4:** See ACCUM Tier 4.

### SHRK — Shark Fin Note (4) — §5.6.9
**Tier 1:** Capital-protected note with barrier-enhanced participation. If stock rises but stays below KO barrier, investor receives enhanced participation. If stock breaches KO, participation is capped at a rebate level. Key risk: strong rally = capped return.
**Tier 2:** Construction: ZCB + call spread + KO barrier. The KO caps returns but funds higher participation rate below the barrier.
**Tier 3:** SM scenario 1.5.
**Tier 4:** SHRK vs PPN vs CLIQ: three protected growth products. SM scenario 1.5.

### SNOW — Snowball (7) — §5.6.10
**Tier 1:** Autocallable where missed coupons accumulate (snowball effect). If stock recovers and triggers coupon, all previously missed coupons are paid at once. Key risk: extremely illiquid — Monte Carlo valuation, wide bid-ask spreads.
**Tier 2:** Construction: Phoenix-like + cumulative coupon accumulation. Path-dependent — requires Monte Carlo. The snowball effect creates high model risk due to discontinuous payouts.
**Tier 3:** SM scenario 3.5. SM AP-17 (don't recommend for liquidity-sensitive clients).
**Tier 4:** SNOW vs Phoenix: Phoenix loses missed coupons (unless memory). SNOW accumulates them.

### CLIQ — Cliquet Note (7) — §5.6.11
**Tier 1:** Capital-protected note that locks in periodic returns with local caps. Each period, return is measured independently and capped. Final return = sum of capped periodic returns. Key risk: local caps destroy returns in trending markets — strong bull market = underperformance.
**Tier 2:** Construction: ZCB + series of forward-starting call spreads (one per period). Each period resets the strike to the prevailing level. Greeks: forward-starting option sensitivities — vol smile dynamics matter.
**Tier 3:** SM scenario 1.5. SM AP-18.
**Tier 4:** CLIQ outperforms in choppy, mean-reverting markets. Underperforms in trending markets.

---

# Part 3: Comparison & Confusion Pairs

## 3.1 Top 10 Interview Pairs — Full Structured Comparison

---

### Pair 1: PPN vs RC

| Dimension | PPN (2) | RC (3) |
|-----------|---------|--------|
| Capital Protection | Full (100% guaranteed) | Conditional (above barrier only) |
| Vol Exposure | Long vega (buys call) | Short vega (sells put) |
| Yield | Low (participation, no coupon) | High (above-market coupon) |
| Income During Life | None (ZCB pays at maturity) | Fixed coupon paid periodically |
| Investor Bet | "Market goes up" | "Market doesn't crash" |
| Worst Case | Zero return + opportunity cost | Full equity loss below barrier |

**Elevator Differentiation:** PPN buys protection (investor pays for the safety net). RC sells protection (investor is the insurance company). Opposite risk profiles.

**Deep Differentiation:** This is the most fundamental comparison in structured products. PPN contains a long call option — the investor benefits from rising volatility because it makes the embedded call more valuable. RC contains a short put option — the investor is harmed by rising volatility because it increases the probability and cost of barrier breach. When a client says "I want yield AND protection," the answer is always "pick one" — PPN provides protection at the cost of yield, RC provides yield at the cost of protection.

**What The Interviewer Is Testing:** Can the candidate identify the option direction (long vs short) inside each product? Do they understand that "enhanced" features always come from selling optionality?

**Trap Question:** "A client wants to invest €100K with capital protection AND above-market yield. Which product do you recommend?" *Correct answer: Neither — the combination doesn't exist. Explain the trade-off.*

---

### Pair 2: Phoenix vs WOAC

| Dimension | Phoenix (6) | WOAC (8) |
|-----------|------------|----------|
| Underlying | Single stock/index | Basket of 3–5 stocks |
| Coupon | 8–12% typical | 15–25% typical |
| Barrier Observation | Worst of 1 stock | Worst of N stocks |
| Correlation Exposure | None | Short correlation |
| Barrier Breach Probability | Single-stock probability | Higher (any one stock) |
| Typical Buyer | Private Banking | Private Banking (APAC/Europe) |

**Elevator Differentiation:** Phoenix = one stock, one barrier. WOAC = N stocks, worst one controls everything. The coupon difference (12% → 22%) is exactly the price of correlation risk.

**Deep Differentiation:** WOAC converts the "diversification benefit" of a basket into the investor's enemy. In a single-stock Phoenix, the barrier breach probability is P(stock < barrier). In a WOAC, it's approximately 1 − (1−P)^N if stocks are independent — dramatically higher. The coupon compensates for this increased probability. When stocks are highly correlated (all move together), WOAC risk approaches single-stock Phoenix risk, and the coupon is "free money." When stocks decorrelate (one crashes alone), the worst-of mechanism triggers on full notional even though N−1 stocks are fine.

**What The Interviewer Is Testing:** Correlation intuition. Does the candidate understand that diversification HURTS the WOAC investor? Can they quantify why the coupon is higher?

**Trap Question:** "A client says 'I chose 5 blue-chip Swiss stocks for my WOAC because diversification protects me.' What do you say?" *Correct answer: In a WOAC, diversification increases risk, not reduces it. Explain the correlation mechanism.*

---

### Pair 3: Phoenix vs FCN

| Dimension | Phoenix (6) | FCN (6) |
|-----------|------------|---------|
| Coupon | Conditional (paid only if above barrier) | Guaranteed (paid regardless) |
| Coupon Level | Higher (10–15%) | Lower (5–8%) |
| Memory Feature | Common (missed coupons accumulate) | N/A (always paid) |
| Cash Flow Predictability | Low (uncertain income) | High (certain income) |
| Capital Risk | Identical | Identical |

**Elevator Differentiation:** Phoenix and FCN have identical capital risk. The only difference: Phoenix pays higher but uncertain coupons; FCN pays lower but guaranteed coupons.

**Deep Differentiation:** The coupon difference is the value of optionality. In a Phoenix, the bank has the right to "not pay" the coupon if the stock is below the coupon barrier. This right is valuable — the bank can value it as a strip of digital options. The value of this optionality is rebated to the investor as a higher coupon rate. An FCN removes this optionality — the investor always gets paid — so the coupon is lower. For clients who need predictable cash flow (pension funds, trusts), FCN is strictly better. For clients who tolerate uncertainty for higher expected return, Phoenix is better.

**What The Interviewer Is Testing:** Does the candidate understand that guaranteed ≠ safe (capital risk is identical)? Can they explain the option value embedded in the coupon difference?

---

### Pair 4: FTD vs NTD

| Dimension | FTD (7) | NTD (8) |
|-----------|---------|---------|
| Trigger | First default in basket | Nth default in basket |
| Correlation Sensitivity | Long correlation | Short correlation |
| Low Correlation Impact | HIGHER risk | LOWER risk |
| High Correlation Impact | LOWER risk | HIGHER risk |
| Coupon | Higher (absorbs first loss) | Lower (protected by first N−1 defaults) |

**Elevator Differentiation:** FTD and NTD have OPPOSITE correlation sensitivity. Low correlation increases FTD risk (independent defaults more likely). High correlation increases NTD risk (clustered defaults more likely). This reversal is the single hardest concept in credit derivatives.

**Deep Differentiation:** FTD triggers on first default → probability of at least ONE default in a basket = 1 − Π(1−PD_i) when independent. As correlation increases, defaults cluster, and the probability of at least one decreases (either all survive or all default — fewer "one default" outcomes). So FTD benefits from high correlation. NTD triggers on Nth default → requires N or more defaults to occur. When correlation is high, defaults cluster, making N or more defaults more likely. So NTD suffers from high correlation. A candidate who memorizes "FTD long correlation, NTD short correlation" without understanding the mechanism will be caught by follow-up questions.

**What The Interviewer Is Testing:** Can the candidate derive the correlation effect from first principles, or have they just memorized the direction? This is the deepest test of credit intuition.

**Trap Question:** "Correlation between 5 basket names increases from 0.3 to 0.7. What happens to the FTD spread and NTD spread?" *Correct: FTD spread tightens (risk decreases). NTD spread widens (risk increases).*

---

### Pair 5: CLN vs CDS

| Dimension | CLN (4) | CDS (5) |
|-----------|---------|---------|
| Format | Funded (investor buys note) | Unfunded (swap, no cash upfront) |
| Credit Exposure | Dual (reference entity + note issuer) | Single (reference entity only) |
| Capital at Risk | Full principal | Mark-to-market only |
| Counterparty Risk | To note issuer | To swap counterparty (mitigated by margin) |
| Use Case | Funded credit investment | Hedging, speculation, basis trading |

**Elevator Differentiation:** CLN = you buy the credit risk (cash goes to issuer). CDS = you swap the credit risk (no cash changes hands). CLN has dual credit exposure; CDS isolates reference entity credit.

**What The Interviewer Is Testing:** Funded vs unfunded mechanics. Does the candidate understand why CLN has dual credit risk? Can they explain the funding benefit to the desk?

---

### Pair 6: IRS vs VLSP

| Dimension | IRS (3) | VLSP (2) |
|-----------|---------|----------|
| Terms | Standardized | Customized (caps, floors, amortization) |
| Liquidity | Extremely liquid (centrally cleared) | Less liquid (bilateral) |
| Complexity | Simple fixed-for-floating | Additional option features |
| Use Case | Standard rate hedging | Bespoke cash flow matching |

**Elevator Differentiation:** IRS is the vanilla default for rate hedging. VLSP adds features for clients whose cash flow profile doesn't match standard terms.

**What The Interviewer Is Testing:** Does the candidate know that IRS is the starting point (not VLSP) despite VLSP having lower Atlas complexity? This tests practical awareness vs theoretical classification.

---

### Pair 7: TRS vs EqSwap

| Dimension | TRS (5) | EqSwap (5) |
|-----------|---------|------------|
| Underlying | Multi-asset (equity, credit, loans) | Equity only |
| Settlement | Cash or physical | Cash |
| Use Case | Synthetic ownership of illiquid assets | Synthetic equity index exposure |

**Elevator Differentiation:** EqSwap is a TRS restricted to equity. TRS covers any asset class. For equity-only exposure, they're interchangeable.

**What The Interviewer Is Testing:** Asset class breadth. Can the candidate explain when TRS is necessary (credit, loan exposure) vs when EqSwap suffices (pure equity)?

---

### Pair 8: RC vs DCI

| Dimension | RC (3) | DCI (3) |
|-----------|--------|---------|
| Asset Class | Equity | FX |
| Mechanism | Short equity put | Short FX put |
| Yield Source | Equity put premium | FX put premium |
| Worst Case | Receive depreciated shares | Receive principal in weaker currency |
| Distribution | Private banking globally | Private banking (Asia focus) |

**Elevator Differentiation:** Identical mechanism (short put for yield), different asset class (equity vs FX). Same concept, same risk — asset class is the only difference.

**What The Interviewer Is Testing:** Cross-asset thinking. Can the candidate recognize the same embedded option structure across different underlying asset classes?

---

### Pair 9: PPN vs SD

| Dimension | PPN (2) | SD (2) |
|-----------|---------|--------|
| Wrapper | Note (issuer credit risk) | Deposit (deposit insurance) |
| Protection Source | Issuer guarantee | Government deposit insurance |
| Cap | No cap on notional | Deposit insurance limit (€100K EU) |
| Distribution | Private banking | Retail bank branches |

**Elevator Differentiation:** Same economics (ZCB + call), different wrapper. SD has government protection (up to the limit). PPN has issuer protection (no limit, but only as good as the bank).

**What The Interviewer Is Testing:** Regulatory/structural knowledge. Does the candidate know about deposit insurance, and can they advise when SD is strictly better than PPN (below insurance limit)?

---

### Pair 10: CDO vs FTD

| Dimension | CDO (10) | FTD (7) |
|-----------|----------|---------|
| Portfolio Size | 100+ names | 5–10 names |
| Loss Mechanism | Tranched waterfall | Binary first-default trigger |
| Tranching | Multiple tranches (equity → super-senior) | Single "tranche" (0% attachment) |
| Model | Full portfolio (Gaussian copula) | Simplified basket (pairwise copula) |
| Complexity | Highest in universe | High but tractable |

**Elevator Differentiation:** FTD is the baby CDO — same concept (basket credit) but simplified to 5–10 names with binary first-default trigger. CDO is the full treatment: 100+ names, tranched loss waterfall, portfolio-level modeling.

**What The Interviewer Is Testing:** Portfolio credit depth. Can the candidate connect FTD to CDO? Do they understand that FTD ≈ equity tranche of a mini-CDO?

---

## 3.2 Quick Differentiation Guide — 25 Pairs

Reference: Atlas Appendix F. One-line key difference per pair.

| # | Pair | Key Difference |
|:-:|------|---------------|
| 1 | PPN vs RC | PPN buys a call (long vol); RC sells a put (short vol). Opposite risk profiles. |
| 2 | RC vs DRC | RC = coupon income; DRC = discount entry. Same risk, different return mechanism. |
| 3 | RC vs CRC | CRC adds bank call right → higher coupon but bank terminates in the best scenario. |
| 4 | DRC vs KODRC | KODRC adds KO barrier → investor protected unless barrier breached. |
| 5 | Phoenix vs FCN | Phoenix coupon is conditional (higher); FCN coupon is guaranteed (lower). Same capital risk. |
| 6 | Phoenix vs SNOW | SNOW accumulates missed coupons (snowball); Phoenix loses them (unless memory). |
| 7 | Phoenix vs WOAC | WOAC adds worst-of basket → short correlation. Coupon doubles but risk is N stocks, not 1. |
| 8 | CRA ELN vs Digital | CRA accrues proportionally (days in range / total); Digital is all-or-nothing per observation. |
| 9 | VO vs Warrant | Same economics. VO = OTC/exchange. Warrant = exchange-listed, retail-accessible. |
| 10 | VO vs ELO | Same economics. ELO = retail note wrapper. No economic difference, only packaging. |
| 11 | ACCUM vs DECUM | ACCUM buys at discount (bullish). DECUM sells at premium (exit). Mirror structures. |
| 12 | IRS vs VLSP | VLSP = IRS + features (caps, floors, amortization). IRS is the vanilla default. |
| 13 | TRS vs EqSwap | EqSwap = equity-specific TRS. TRS covers any asset class. |
| 14 | NCRA vs CRA SRT | CRA SRT adds callability → higher coupon but bank can terminate early. |
| 15 | V. STEG vs C. STEG | C. STEG adds bank call right → higher coupon, but called when curve steepens (worst timing for investor). |
| 16 | FTD vs NTD | Correlation reversal. Low corr increases FTD risk; high corr increases NTD risk. |
| 17 | CLN vs CDS | CLN = funded (cash at risk, dual credit). CDS = unfunded (swap, single credit). |
| 18 | PPN vs SD | PPN = note (issuer risk). SD = deposit (deposit insurance up to limit). Same economics. |
| 19 | PPN vs SHRK | SHRK adds KO barrier → higher participation but capped if stock rallies strongly. |
| 20 | PPN vs CLIQ | CLIQ locks in periodic returns (ratchet). PPN measures total return at maturity only. |
| 21 | RC vs DCI | Same mechanism (short put for yield). RC = equity. DCI = FX. |
| 22 | IR Callable vs CRC | Both sell call right. IR Callable = rate product (swaption). CRC = equity (Bermudan call + put). |
| 23 | Digital vs Digital CF | Same payoff (binary coupon). Digital = equity-linked. Digital CF = rate-linked. |
| 24 | CDO vs FTD | FTD = 5–10 name basket, binary first-default. CDO = 100+ names, tranched waterfall. |
| 25 | Booster vs Warrant | Both leveraged. Booster = capped leverage in note format. Warrant = uncapped option on exchange. |

---

# Part 4: Question Bank

## 4.1 Technical Questions

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

T.9 [WT] How does time decay (theta) differ for an at-the-money option vs a deep out-of-the-money option? Why?

T.10 What is pin risk? Why do desks dread observation dates when the spot price is near a digital strike?

**Advanced**

T.11 A variance swap has 6 months remaining. Realized vol for the first 6 months was 15%. The strike was 20%. If realized vol for the remaining 6 months is 25%, what is the approximate P&L for the long? *What The Interviewer Is Testing: Can the candidate calculate weighted-average variance, not just volatility? Do they understand convexity?*

T.12 Explain the vol-of-vol concept. Which products have explicit sensitivity to vol-of-vol? *What The Interviewer Is Testing: Understanding of second-order vol risk. Products: VarSwap (convexity), barrier products (gamma of gamma).*

T.13 [WT] Why is a short variance swap position more dangerous than a short straddle, even though both are short volatility? *What The Interviewer Is Testing: Convexity distinction between variance (quadratic) and volatility (linear).*

T.14 An RC has 1 month remaining. The spot is 2% above the barrier. The implied vol is 25%. Should you be worried about gamma? Quantify. *What The Interviewer Is Testing: Near-barrier gamma quantification. Short-dated, near-barrier = extreme gamma.*

T.15 What is the CMS convexity adjustment and why does it matter for STEG pricing? *What The Interviewer Is Testing: Understanding that CMS rate ≠ forward rate. The adjustment is model-dependent — a key source of STEG model risk.*

**Expert**

T.16 Derive the replication argument for a variance swap using a portfolio of options. What assumptions are required? *What The Interviewer Is Testing: Can the candidate walk through the log-contract replication? Key assumptions: continuous monitoring, no jumps, complete options market.*

T.17 How does the choice of copula (Gaussian, Student-t, Clayton) affect CDO tranche pricing? Which tranche is most sensitive? *What The Interviewer Is Testing: Model risk understanding. Mezzanine tranche is most copula-sensitive; equity/senior are more robust.*

T.18 A WOAC has 5 underlyings. Implied correlation is 0.6. One stock's implied vol jumps 10 points while others are unchanged. What happens to the WOAC price? *What The Interviewer Is Testing: Dispersion awareness. Single-stock vol jump with others unchanged → implied correlation drops → WOAC value increases (short correlation position loses).*

T.19 [WT] Explain the "Quanto" adjustment. Why does a Quanto option on a foreign equity trade at a different implied vol than the same option in the foreign currency? *What The Interviewer Is Testing: Cross-asset correlation (equity-FX) and its pricing impact.*

T.20 How would you price a snowball autocallable? Why can't you use a closed-form solution? *What The Interviewer Is Testing: Path dependency requiring Monte Carlo. Cumulative coupon accumulation makes each path unique.*

### Rates

**Beginner**

T.21 [WT] Why does a zero-coupon bond's price increase when interest rates fall?

T.22 What is the difference between a spot rate and a forward rate?

**Intermediate**

T.23 [WT] Explain DV01 and how it differs between a 2-year and a 30-year IRS.

T.24 Why does the swap rate differ from the government bond yield of the same maturity?

**Advanced**

T.25 Explain the CMS-forward rate difference. What drives the convexity adjustment? *What The Interviewer Is Testing: Non-linear payoff on rates creates a Jensen's inequality effect — CMS rates exceed forward rates due to the convex relationship between rate and price.*

**Expert**

T.26 How does the choice of short-rate model (Hull-White, BK, LGM) affect callable note pricing? *What The Interviewer Is Testing: Model selection and its impact on embedded swaption valuation.*

### Credit

**Beginner**

T.27 [WT] What is a credit event under ISDA definitions? Name three types.

T.28 What is recovery rate and why does it matter for CDS pricing?

**Intermediate**

T.29 [WT] Why does a CLN investor face dual credit risk? Name both exposures.

T.30 What is the CDS-bond basis and why does it exist?

**Advanced**

T.31 How does the "Big Bang" protocol (2009) standardize CDS contracts? Why was it introduced? *What The Interviewer Is Testing: Post-crisis market structure. Running spread standardization, upfront payment, auction settlement.*

**Expert**

T.32 Explain base correlation and why it replaced compound correlation for CDO tranche pricing. *What The Interviewer Is Testing: Correlation smile. Compound correlation can produce multiple solutions; base correlation is monotonic.*

### Volatility & Correlation

**Beginner**

T.33 [WT] What does it mean to be "long volatility"? Give an example of a product that is long vol and one that is short vol.

**Intermediate**

T.34 [WT] Explain the volatility smile/skew. Why are out-of-the-money puts typically more expensive than out-of-the-money calls?

T.35 How does realized correlation between stocks affect the price of a worst-of autocallable?

**Advanced**

T.36 What is the variance risk premium and why does it exist? *What The Interviewer Is Testing: Risk premium = implied variance − realized variance. It's positive because investors are willing to pay for downside protection, creating a premium for vol sellers.*

**Expert**

T.37 How would you construct a dispersion trade using VarSwaps? *What The Interviewer Is Testing: Sell index variance, buy single-stock variance. Profits from idiosyncratic vol exceeding index vol (low realized correlation).*

---

## 4.2 Product Knowledge Questions

Organized by family. Each question references Atlas Appendix E where applicable.

### ELN Family

PK.1 [WT] **PPN:** Why is the participation rate always less than 100%? Walk through the arithmetic. (See also Atlas E: 5.1.1)

PK.2 **RC:** Draw the payoff diagram showing both zones (above and below barrier). Mark the break-even point.

PK.3 [WT] **Phoenix:** If the stock drops below the coupon barrier for 3 consecutive quarters then recovers, how does the memory feature work? What is paid?

PK.4 **DRC:** How does the break-even calculation differ between DRC and RC? Which has a lower break-even?

PK.5 [WT] **KODRC:** The stock is exactly at the KI barrier. What is the delta of the embedded put? Why?

PK.6 **CRC:** Why does the bank call the note when it's performing well for the investor? Whose option is being exercised?

PK.7 **Airbag:** A client asks: "Where does the leveraged upside come from?" Answer. (See Atlas E: 5.1.7)

PK.8 **Bonus:** The stock touches the barrier for 5 seconds during an intraday flash crash then recovers. Is the bonus lost?

PK.9 [WT] **FCN:** A client says "my coupon is guaranteed so this product is safe." Is this correct?

PK.10 **CRA ELN:** What is the coupon if the underlying is in the range for 60 out of 90 days? Show the formula.

PK.11 **ICN:** Who benefits from the call option — the investor or the bank? (Atlas E: 5.1.11)

PK.12 **Digital:** What makes hedging cost spike when the underlying is near the digital strike? (Atlas E: 5.1.12)

PK.13 **Booster:** If participation is 200%, why is there a cap? (Atlas E: 5.1.13)

PK.14 **DKIP:** Name the three barriers and explain what each controls.

PK.15 **Warrant:** Why does time decay accelerate as expiry approaches? (Atlas E: 5.1.15)

### Swaps Family

PK.16 [WT] **IRS:** Both legs have the same present value at inception. How does anyone make money? (Atlas E: 5.2.1)

PK.17 **TRS:** Why would an investor pay a funding spread when they could buy the asset directly? (Atlas E: 5.2.2)

PK.18 **EqSwap:** How does an unexpected special dividend affect each leg of the swap?

PK.19 [WT] **VarSwap:** Why is a long variance position more dangerous than a long volatility position? (Atlas E: 5.2.4)

PK.20 **CDS:** CDS spreads widen 100bp but no default occurs. Who profits? (Atlas E: 5.2.5)

PK.21 **XCCY:** Why does the cross-currency basis exist? (Atlas E: 5.2.6)

PK.22 **CommSwap:** What is basis risk in commodity hedging? (Atlas E: 5.2.7)

PK.23 **VLSP:** When would a corporate choose VLSP over IRS? (Atlas E: 5.2.8)

### SRT Family

PK.24 [WT] **IR Callable:** The enhanced coupon is 5% when vanilla bonds pay 3%. Where does the extra 2% come from?

PK.25 **ZCL:** A 30-year ZCL moves roughly how many times more per basis point than a 1-year bond? Why?

PK.26 **NCRA:** If rates leave the accrual range permanently in year 1 of a 10-year note, what does the investor receive?

PK.27 **CRA SRT:** What two risks is the investor selling simultaneously? (Atlas E: 5.3.4)

PK.28 **Digital CF:** What happens to the hedge when rates are exactly at the digital strike? (Atlas E: 5.3.5)

### STEG Family

PK.29 [WT] **V. STEG:** What market scenario causes the coupon to drop to zero? (Atlas E: 5.4.1)

PK.30 **RA STEG:** Why does this product require TWO conditions simultaneously? (Atlas E: 5.4.2)

PK.31 **C. STEG:** In what rate environment would the bank exercise the call? (Atlas E: 5.4.3)

PK.32 **TARN STEG:** Is early termination good or bad for the investor? Explain the reinvestment risk. (Atlas E: 5.4.4)

### CLN Family

PK.33 [WT] **CLN:** Explain dual credit risk. Name both exposures. (Atlas E: 5.5.1)

PK.34 **Skew CLN:** How does the actual recovery rate affect payout? (Atlas E: 5.5.2)

PK.35 [WT] **FTD:** Why does low correlation INCREASE FTD risk? Derive from first principles. (Atlas E: 5.5.3)

PK.36 **NTD:** Why does the correlation effect reverse between FTD and NTD? (Atlas E: 5.5.4)

PK.37 **CDO:** Why is correlation more important than default probability for equity tranche pricing? (Atlas E: 5.5.5)

### Other Family

PK.38 **SD:** Why would a client accept zero return rather than keeping money in cash? (Atlas E: 5.6.1)

PK.39 [WT] **FWD:** If both parties agree on the forward price, why does anyone enter the trade? (Atlas E: 5.6.2)

PK.40 **VO:** Explain put-call parity in one sentence. Why does it matter?

PK.41 **ELO:** How does the retail wrapper change the economics? (Atlas E: 5.6.4)

PK.42 **Opt-on-RC:** Name the two decision points during the product's life. (Atlas E: 5.6.5)

PK.43 [WT] **ACCUM:** Why is the gearing (2×) below strike particularly dangerous?

PK.44 **DECUM:** When would a founder use this instead of selling on the open market? (Atlas E: 5.6.7)

PK.45 **DCI:** What determines whether the investor receives base or alternate currency? (Atlas E: 5.6.8)

PK.46 **SHRK:** Why would an investor accept a return cap? (Atlas E: 5.6.9)

PK.47 **SNOW:** What happens to the coupon after 3 consecutive missed payments if the stock recovers? (Atlas E: 5.6.10)

PK.48 **CLIQ:** Why do local caps make this product underperform in a trending market? (Atlas E: 5.6.11)

PK.49 [WT] **WOAC:** Why does the worst stock drive the entire outcome? (Atlas E: 5.6.12)

---

## 4.3 Structuring Logic Questions

**Beginner**

SL.1 [WT] A retail client wants yield enhancement. What is the maximum product complexity you can recommend under the persona framework?

SL.2 Name the 10 steps of the structurer decision model (reference: Solutions Manual §1.1).

SL.3 A client wants "safe income." Why is CRA SRT the wrong recommendation? (Reference: SM AP-7)

**Intermediate**

SL.4 A private banking client wants protected equity growth but rates are at 1%. Walk through why PPN is problematic in this regime and what alternatives exist.

SL.5 [WT] Explain the concept of the "persona filter" (Step 3.5). Why does it exist? What happens if you skip it?

SL.6 A client wants to sell volatility. Why is a short VarSwap dangerous? What alternative achieves similar economics with bounded risk? (Reference: SM AP-4)

SL.7 What is the difference between a complexity governance violation and a suitability violation?

**Advanced**

SL.8 A pension fund client wants CMS spread income. The yield curve is flat. Walk through the decision framework and explain why you would reject STEG products in this regime. What do you recommend instead? *What The Interviewer Is Testing: Market regime awareness + framework application + ability to redirect the client.*

SL.9 Two proposals for a private banking client: Phoenix on single stock (14% coupon) vs WOAC on 4 stocks (22% coupon). Walk through the comparative selection using the decision framework. *What The Interviewer Is Testing: Correlation risk assessment, persona suitability, and trade-off reasoning — not just picking the higher coupon.*

SL.10 [WT] A client insists on a CDO tranche investment. They are categorized as "Private Banking." What governance steps must you take? *What The Interviewer Is Testing: Complexity governance — CDO (10) exceeds PB cap (8). The structurer must either reclassify the client as Sophisticated or decline.*

**Expert**

SL.11 Design a product for an insurance company that needs 4% income for 10 years with capital protection and tolerance for curve steepening risk. Walk through all 10 steps. *What The Interviewer Is Testing: Full framework execution including institutional persona, rate regime assessment, and complexity governance.*

SL.12 A structurer proposes FTD for a client who has never traded credit products. The client's complexity cap allows it (Institutional). Is this appropriate? Why or why not? *What The Interviewer Is Testing: SM AP-13 — correlation training prerequisite. Complexity cap alone is necessary but not sufficient.*

---

## 4.4 Case Interview Questions

Each case: different client, different quote, different context from all 40 Solutions Manual scenarios.

---

**CASE D.1 — The Conservative Retiree**
Difficulty: Beginner | Role: Sales

Client: "I have €500K in savings. I need this to last 20 years. I can't afford to lose any of it, but savings accounts pay nothing. Is there something that gives me growth without risk?"

Expected answer structure:
1. Identify: capital protection + growth (no income need stated)
2. Narrow: protection → PPN or SD. Under deposit insurance limit in most jurisdictions.
3. Recommend: SD (2) for first €100K (deposit insurance), PPN (2) for remainder
4. Rejected: RC (client said "can't afford to lose"), Phoenix (no protection)
5. Key risk: opportunity cost in flat/down markets; issuer risk on PPN portion

Scoring: Excellent — splits between SD and PPN with deposit insurance reasoning. Adequate — recommends PPN only. Poor — recommends RC or any yield product.

---

**CASE D.2 — The Tech VP's Stock Concentration**
Difficulty: Intermediate | Role: Structuring

Client: "I'm a VP at a tech company. I have 200,000 shares vesting over 2 years. I want to lock in some value without triggering a public sale. My compliance team says I can use structured products."

Expected answer structure:
1. Identify: share disposal, confidentiality, regulatory constraint
2. Narrow: disposal → DECUM (6) or FWD (2) series
3. Recommend: DECUM — sells shares at premium with KO protection if stock drops
4. Rejected: Open market sale (compliance issue), ACCUM (wrong direction — buying not selling)
5. Key risk: gearing above strike forces selling at a discount if stock rallies; insider trading considerations

Scoring: Excellent — identifies regulatory/compliance dimension and gearing risk. Adequate — recommends DECUM correctly. Poor — recommends ACCUM or misidentifies direction.

*What The Interviewer Is Testing: Can the candidate distinguish ACCUM from DECUM? Do they consider the compliance dimension beyond pure product selection?*

---

**CASE D.3 — The Yield-Hungry Trustee**
Difficulty: Intermediate | Role: Structuring

Client: "I manage a trust that distributes 6% annually to beneficiaries. Bond yields are 3%. I need to close the gap but the trust deed prohibits equity investments. Can I use structured products?"

Expected answer structure:
1. Identify: income gap, regulatory constraint (no equity)
2. Narrow: rate/credit products only → IR Callable (5), CLN (4), Digital CF (5), STEG family
3. Recommend: IR Callable (5) — enhanced coupon from selling call right, no equity exposure
4. Rejected: RC/Phoenix (equity — prohibited), CRA SRT (too complex for trust mandate)
5. Key risk: reinvestment risk if called; rate environment determines coupon level

Scoring: Excellent — identifies the trust deed constraint first, then filters accordingly. Adequate — recommends a rate product. Poor — recommends equity-linked product.

*What The Interviewer Is Testing: Constraint identification before product selection. The trust deed prohibition is the binding constraint — it eliminates the entire ELN family upfront.*

---

**CASE D.4 — The Macro Hedge Fund**
Difficulty: Advanced | Role: Trading

Client: "We think realized vol will be significantly higher than implied over the next 6 months. We want convex exposure — not just linear vol. We can handle margin calls and understand the risks."

Expected answer structure:
1. Identify: volatility trading, convexity required, sophisticated client
2. Narrow: long VarSwap (7) — convex exposure to realized variance
3. Recommend: Long VarSwap — variance payoff is quadratic, providing the convexity requested
4. Rejected: Long VO straddle (linear vol exposure, not convex), long VIX futures (basis risk, rolling cost)
5. Key risk: if realized vol stays below strike, they pay the carry; time decay on the variance position

Scoring: Excellent — distinguishes variance (convex) from volatility (linear) and explains the quadratic payoff. Adequate — recommends VarSwap correctly. Poor — recommends straddle (linear, not convex).

*What The Interviewer Is Testing: Variance vs volatility distinction. Can the candidate explain why variance is convex? Do they understand the 2× vol → 4× variance relationship?*

---

**CASE D.5 — The Risk Manager's Nightmare**
Difficulty: Advanced | Role: Risk

Client (internal): "The structuring desk just sold a large WOAC to a private banking client. 5 stocks, 65% barrier, 3-year maturity. The sales team is celebrating the 22% coupon. I need you to identify the top 3 risks and design a stress test."

Expected answer structure:
1. Risks: (a) Single-stock crash — one stock −40% triggers loss on full notional even if others +20%. (b) Correlation breakdown — stocks decorrelate in stress, worst-of probability increases. (c) Liquidity — WOAC has wide bid-ask, client can't exit easily.
2. Stress test: (a) Single-stock −40%, others flat. (b) All stocks −30% (correlated crash). (c) Correlation drop from 0.6 to 0.2 with moderate stock declines.
3. Additional: suitability review — is private banking client appropriate for Complexity 8?

Scoring: Excellent — identifies all 3 risks + designs 3-scenario stress test + raises suitability question. Adequate — identifies 2+ risks. Poor — focuses only on market risk, misses correlation.

*What The Interviewer Is Testing: Risk identification beyond the obvious. Can the candidate think about correlation risk and suitability, not just delta/market risk?*

---

**CASE D.6 — The Model Validator's Challenge**
Difficulty: Expert | Role: Model Validation

Client (internal): "The desk is pricing a TARN STEG using a 2-factor Hull-White model with 500 Monte Carlo paths. The price seems low compared to a simpler 1-factor model. Investigate."

Expected answer structure:
1. Path count: 500 paths is too few for path-dependent TARN. Standard: 10,000+ minimum, ideally 100,000+.
2. Factor model: 2-factor HW captures curve dynamics that 1-factor cannot — spread between tenors is stochastic. This affects TARN trigger probability because the spread determines the coupon, and the cumulative coupon determines the target.
3. Resolution: (a) Increase paths to 50,000+, check convergence. (b) Compare 1F vs 2F with sufficient paths. (c) The 2F price being lower is plausible if the stochastic spread reduces expected coupon accumulation (target is reached later or never).

Scoring: Excellent — identifies path count issue AND explains why 2F vs 1F produces different TARN prices. Adequate — identifies path count issue. Poor — can't diagnose.

*What The Interviewer Is Testing: Numerical methods + model choice impact. Can the candidate connect the abstract model difference (1F vs 2F) to a concrete pricing effect (TARN target probability)?*

---

**CASE D.7 — The Currency Treasurer**
Difficulty: Beginner | Role: Sales

Client: "I'm the treasurer of a European company. We receive USD revenues but report in EUR. I need to budget at a fixed EUR/USD rate for the next 12 months."

Expected answer structure:
1. Identify: FX hedging, budget certainty
2. Narrow: FWD (2) or XCCY (5). Simple need → start simple.
3. Recommend: Series of monthly FX forwards (FWD) to lock in EUR/USD rate
4. Rejected: XCCY (overkill — no debt conversion needed), DCI (not hedging, yield enhancement)
5. Key risk: opportunity cost if EUR/USD moves favorably

Scoring: Excellent — recommends FWD strip, explains why XCCY is unnecessary. Adequate — recommends FWD. Poor — recommends XCCY or DCI.

---

**CASE D.8 — The Credit Analyst's First Trade**
Difficulty: Intermediate | Role: Structuring

Client: "We have strong views on 5 investment-grade credits. We want exposure to all 5 but don't want to buy 5 separate bonds. Can you package this?"

Expected answer structure:
1. Identify: multi-name credit, funded exposure
2. Narrow: CLN basket, FTD (7), or portfolio of individual CLNs
3. Recommend: 5 individual CLNs (4 each) — clean exposure per name, no correlation risk
4. Rejected: FTD (client hasn't expressed correlation view — correlation risk adds complexity without stated benefit)
5. Key risk: dual credit risk on each CLN (reference + issuer)

Scoring: Excellent — recommends individual CLNs and explains why FTD introduces unwanted correlation risk. Adequate — recommends CLN. Poor — recommends FTD without correlation discussion.

*What The Interviewer Is Testing: Restraint. The obvious "packaged" answer is FTD — but the client hasn't asked for correlation exposure. Simpler is better when the need is simple.*

---

## 4.5 Desk-Specific Questions

### Structuring

DS.1 A client pushback: "Your competitor is offering a Phoenix with a 15% coupon. You're offering 12%. Why should I choose yours?" How do you respond?

DS.2 [WT] Design a product for a client who wants: 5% income, capital protection above 70%, 2-year maturity, equity underlying. What product, what parameters?

DS.3 A sales person asks you to lower the barrier on an RC from 70% to 60% to increase the coupon. What are the implications?

DS.4 *Advanced.* A client wants CMS spread income but the curve is flat. Can you design a product that works? What trade-offs are required? *What The Interviewer Is Testing: Creative structuring under adverse regime. Candidate should discuss range accrual with wide range, or alternative rate structure.*

DS.5 *Expert.* Design a capital-protected product with 70%+ participation in a 1% interest rate environment. What compromises must you make? *What The Interviewer Is Testing: Low-rate constraint. ZCB costs ~97%, leaving 2% for the call. Candidate must discuss: extending maturity, adding caps, worst-of basket, or accepting lower participation.*

### Trading

DS.6 You just sold a Phoenix to a client. Walk me through the hedge you would establish on day 1.

DS.7 [WT] Your RC book has $50M notional with barriers at 70%. The market is at 75%. What are your top 3 concerns?

DS.8 *Advanced.* Overnight, one stock in your WOAC basket drops 15% on earnings. The other 4 stocks are unchanged. Walk through the impact on your book and your first three actions. *What The Interviewer Is Testing: Single-stock shock in a worst-of context. Candidate should discuss: delta rebalancing on the dropped stock, correlation impact, barrier proximity for that name, and potential client margin/suitability implications.*

DS.9 *Expert.* Your variance swap book shows +$2M P&L for the day. Vol is unchanged. Spot moved 3%. Explain. *What The Interviewer Is Testing: Gamma P&L vs vega P&L. Variance swaps have gamma exposure — a 3% spot move generates P&L from gamma even with flat vol.*

### Sales

DS.10 Explain a CDO in 30 seconds to a client with no derivatives background.

DS.11 A client asks: "Why is the WOAC coupon so much higher than the Phoenix coupon?" Explain without using the word "correlation."

DS.12 [WT] *Advanced.* A client says: "I saw online that structured products are just ways for banks to rip off investors." How do you respond? *What The Interviewer Is Testing: Objection handling. Candidate should acknowledge the perception, explain the economics (option premium funds the coupon), and discuss transparency.*

DS.13 *Expert.* A client wants to switch from a Phoenix to an ACCUM. Walk them through why this is a fundamental change in risk profile, not just a product swap. *What The Interviewer Is Testing: Can the candidate explain that Phoenix = yield from selling downside optionality, while ACCUM = leveraged directional with gearing? Completely different risk profiles despite both being "equity-linked."*

### Risk

DS.14 [WT] Name the top 3 risks for a CLN. Which one do most investors forget?

DS.15 Design a stress test for a portfolio containing: 1 Phoenix, 1 WOAC, 1 VarSwap long.

DS.16 *Advanced.* A limit breach occurs: the RC desk's barrier proximity metric exceeds the threshold. What do you do? *What The Interviewer Is Testing: Escalation procedure: notify desk head → assess MTM impact → determine if the breach is temporary (one name near barrier) or structural → recommend action (reduce position, buy protection, widen barriers on new trades).*

DS.17 *Expert.* How would you set risk limits for a new CDO correlation trading desk? What metrics, what levels, what stress scenarios? *What The Interviewer Is Testing: Correlation trading risk management. Metrics: CS01 per name, tranche delta, base correlation sensitivity, jump-to-default reserves. Stress: 2008 scenario, correlation spike/drop, clustered defaults.*

### Model Validation

DS.18 [WT] What pricing model would you use for a Phoenix autocallable? Why?

DS.19 The calibration of your local vol surface fails in the wings. What impact does this have on barrier product pricing?

DS.20 *Advanced.* Compare Monte Carlo vs PDE (finite differences) for pricing a TARN STEG. Which is better? Why? *What The Interviewer Is Testing: MC handles path-dependency naturally (TARN target). PDE is faster but struggles with the target constraint (need to add a state variable). MC wins for TARN-type products.*

DS.21 *Expert.* A back-test shows your VarSwap model consistently overprices by 2%. Diagnose. *What The Interviewer Is Testing: Potential causes: (a) discrete vs continuous monitoring adjustment, (b) jump risk not captured in the model, (c) bid-ask spread not reflected, (d) vol surface extrapolation bias in the wings. Systematic 2% overpricing suggests a structural model feature, not random noise.*

---

## 4.6 Written Assessments

### 4.6.1 Multiple Choice Assessment (25 Questions)

**Instructions:** Select the best answer. 45 minutes.

**MC.1** (Beginner) A PPN investor faces which primary risk?
(a) Market risk on the underlying
(b) Issuer credit risk
(c) Interest rate risk
(d) Barrier breach risk

**MC.2** (Beginner) Which product is the investor SHORT volatility?
(a) PPN
(b) Vanilla Option (long call)
(c) Reverse Convertible
(d) Structured Deposit

**MC.3** (Beginner) An IRS at inception has a net present value of:
(a) Positive for the fixed payer
(b) Positive for the floating payer
(c) Zero for both parties
(d) Depends on the swap rate

**MC.4** (Beginner) Which product provides deposit insurance protection?
(a) PPN
(b) CLN
(c) Structured Deposit
(d) RC

**MC.5** (Beginner) The forward price of a non-dividend-paying stock is:
(a) Equal to the spot price
(b) Higher than the spot price
(c) Lower than the spot price
(d) Unpredictable

**MC.6** (Intermediate) A Phoenix note's coupon barrier is at 70%. On observation day, the stock is at 69%. What happens?
(a) Coupon is paid proportionally (69/70)
(b) No coupon is paid
(c) The note is autocalled
(d) The barrier is breached and capital is lost

**MC.7** (Intermediate) Which Greek causes the most hedging difficulty near a digital strike?
(a) Delta
(b) Gamma
(c) Vega
(d) Theta

**MC.8** (Intermediate) A WOAC has 5 stocks. Stock A is down 35%, stocks B-E are up 10%. What drives the WOAC outcome?
(a) The average of all 5 stocks
(b) Stock A (worst performer)
(c) Stocks B-E (best performers)
(d) The weighted average based on notional

**MC.9** (Intermediate) The CDS-bond basis is:
(a) CDS spread minus asset swap spread
(b) Bond yield minus CDS spread
(c) CDS spread minus risk-free rate
(d) Bond price minus CDS upfront

**MC.10** (Intermediate) Why does a CLN pay a higher coupon than the equivalent CDS spread?
(a) CLN has more credit risk
(b) The desk adds the funding benefit from receiving the investor's cash
(c) CLN is more liquid
(d) Regulatory requirements force higher coupons

**MC.11** (Intermediate) An Accumulator's gearing ratio is 2×. The stock is 10% below strike. How many shares does the investor buy daily?
(a) The standard daily amount
(b) Double the standard daily amount
(c) Half the standard daily amount
(d) Zero — the contract is terminated

**MC.12** (Advanced) In a FTD basket of 5 names, correlation increases from 0.3 to 0.7. The FTD spread:
(a) Widens (more risk)
(b) Tightens (less risk)
(c) Is unchanged (correlation doesn't affect FTD)
(d) Effect depends on individual spread levels

**MC.13** (Advanced) The CMS convexity adjustment for a STEG is positive because:
(a) CMS rates are higher than LIBOR rates
(b) The convex relationship between price and yield creates a Jensen's inequality effect
(c) Steepener notes have positive carry
(d) CMS swaps are centrally cleared

**MC.14** (Advanced) A variance swap has a strike of 20 vol (400 variance). Realized variance at expiry is 625 (25 vol). The P&L per unit of vega notional is approximately:
(a) 5 (25 − 20)
(b) 225 (625 − 400) / 40
(c) 225 (625 − 400) / (2 × 20) = 5.625
(d) 12.5

**MC.15** (Advanced) A callable STEG investor faces which unique risk compared to a vanilla STEG?
(a) Credit risk
(b) Reinvestment risk — the bank calls when the curve steepens
(c) Currency risk
(d) Operational risk

**MC.16** (Advanced) Which product has the OPPOSITE correlation sensitivity to an FTD?
(a) CDO equity tranche
(b) NTD
(c) CLN
(d) CDS

**MC.17** (Advanced) A TARN STEG reaches its target coupon in year 2. The investor:
(a) Receives remaining coupons as a lump sum
(b) Receives principal back and must reinvest at prevailing rates
(c) Loses the remaining coupons
(d) Can choose to extend the note

**MC.18** (Expert) In a Gaussian copula CDO model, increasing the correlation from 0.2 to 0.5 has what effect on equity tranche pricing?
(a) Equity tranche spread widens (more expensive to buy protection)
(b) Equity tranche spread tightens (less expensive)
(c) No effect — equity tranche depends on individual spreads only
(d) Effect is ambiguous without knowing attachment points

**MC.19** (Expert) The replication portfolio for a variance swap has option weights proportional to:
(a) 1/K (inverse of strike)
(b) 1/K² (inverse of strike squared)
(c) K (proportional to strike)
(d) Equal weights across all strikes

**MC.20** (Expert) A SNOW (Snowball) autocallable missed coupons in periods 1–4. In period 5, the stock recovers above the coupon barrier. The investor receives:
(a) Period 5 coupon only
(b) Periods 1–5 cumulative coupons
(c) Periods 4–5 coupons (last 2 missed + current)
(d) Depends on the memory feature specification

**MC.21** (Intermediate) A DCI investor deposits USD and sells a EUR/USD put at 1.05. At maturity, EUR/USD is at 1.02. The investor receives:
(a) USD principal back
(b) EUR equivalent at 1.05 strike rate
(c) EUR equivalent at 1.02 market rate
(d) The enhanced coupon only, principal is lost

**MC.22** (Intermediate) Which product family benefits most from a steep yield curve?
(a) ELN
(b) STEG
(c) CLN
(d) SRT

**MC.23** (Advanced) An RC's implied vol is 25%. Realized vol over the product's life is 15%. Who benefits?
(a) The investor (coupon funded by expensive option premium)
(b) The desk (sold overpriced protection, hedged cheaply)
(c) Both benefit equally
(d) Neither — implied vs realized doesn't affect the outcome

**MC.24** (Expert) A 2-factor Hull-White model produces a lower price for a TARN STEG than a 1-factor model because:
(a) The 2-factor model captures stochastic spread, reducing expected coupon accumulation
(b) The 2-factor model has higher computational error
(c) 1-factor models always overprice
(d) The calibration is wrong

**MC.25** (Expert) Why did CDO pricing models fail in 2008?
(a) The Gaussian copula underestimated tail dependence between defaults
(b) Interest rates were too low
(c) CDOs were not hedged
(d) Rating agencies used the wrong models

### 4.6.2 Short Answer Assessment (10 Questions)

**Instructions:** Provide structured answers in 3–5 sentences each. 30 minutes.

**SA.1** [Beginner] Explain why a Reverse Convertible pays an above-market coupon. Where does the extra yield come from?

**SA.2** [Beginner] A client says "this PPN has 100% capital protection, so it's risk-free." Correct this statement.

**SA.3** [Intermediate] Explain the difference between a CLN and a CDS. When would you recommend each?

**SA.4** [Intermediate] A Phoenix has a memory feature. Explain what this means and why it matters for the client.

**SA.5** [Intermediate] Why does the desk prefer to sell structured products in a high-volatility environment?

**SA.6** [Advanced] Explain the FTD correlation paradox: why does diversification (low correlation) INCREASE risk?

**SA.7** [Advanced] A client wants "guaranteed income" from a Phoenix. What is wrong with this expectation? What product should you recommend instead?

**SA.8** [Advanced] What is the CMS convexity adjustment and why does it matter for STEG pricing?

**SA.9** [Expert] Compare and contrast the variance swap and the volatility swap. Why is variance "convex" while volatility is "linear"?

**SA.10** [Expert] A bank's CDO desk uses a Gaussian copula. A risk manager says the model "caused" the 2008 crisis. Is this accurate? Provide a nuanced answer.

### 4.6.3 Mini Case Assessment (5 Cases)

**Instructions:** For each case, provide: (1) recommended product, (2) reasoning, (3) one rejected alternative and why, (4) key risk. 60 minutes total.

**CASE MC.1** [Beginner]
A 65-year-old retiree with €300K in savings wants growth with no risk of losing principal. Current deposit rates are 0.5%. She needs the money in 5 years. What do you recommend?

**CASE MC.2** [Intermediate]
A corporate treasurer needs to hedge €10M of USD receivables over the next 6 months. The company reports in EUR. Budget certainty is the priority. What structure?

**CASE MC.3** [Intermediate]
A wealth manager's client wants quarterly income above 8% with some capital risk tolerance. The client is categorized as Private Banking (complexity cap 8). The client prefers single-stock exposure on a well-known name. What product?

**CASE MC.4** [Advanced]
An insurance company needs to match a 15-year liability with a rate-linked asset that generates 4%+ annual income. The company is comfortable with curve steepening risk but not with call risk (they need duration certainty). What do you recommend?

**CASE MC.5** [Expert]
A hedge fund wants to express a view that credit correlation will decrease over the next 12 months. They have a $50M risk budget and are comfortable with portfolio credit products. Design the trade.

### 4.6.4 Assessment Answer Key

**Multiple Choice Answers:**

| Q | Answer | Reasoning | Common Mistake |
|:-:|:------:|-----------|---------------|
| MC.1 | (b) | PPN principal is guaranteed by the issuer, not the market. If issuer defaults, protection fails. | Choosing (a) — PPN is capital-protected against market risk |
| MC.2 | (c) | RC contains a short put — investor sells vol. PPN (a) is long vol. VO long call (b) is long vol. | Confusing yield source with vol direction |
| MC.3 | (c) | Both legs have equal PV at inception — the swap rate is set to make this true. | Thinking one side "wins" at inception |
| MC.4 | (c) | Only SD has deposit insurance. PPN, CLN, RC are notes. | Confusing PPN with SD |
| MC.5 | (b) | F = S × e^(rT) > S when r > 0. Cost of carry makes forward higher. | Thinking forward = expected future spot |
| MC.6 | (b) | Below coupon barrier → no coupon. Phoenix coupon is all-or-nothing per observation. | Confusing proportional accrual (CRA) with digital (Phoenix) |
| MC.7 | (b) | Digital gamma near strike → discontinuous delta → massive hedging cost. | Choosing delta — delta is the first order; gamma causes the problem |
| MC.8 | (b) | WOAC uses worst-of observation. Stock A drives ALL outcomes. | Choosing (a) — averaging is for different products |
| MC.9 | (a) | Standard definition. Positive basis = CDS wider than ASW. | Inverting the formula |
| MC.10 | (b) | The desk receives cash from the investor (funding benefit). This allows a higher coupon. | Choosing (a) — both have the same reference credit risk |
| MC.11 | (b) | 2× gearing below strike = double accumulation. | Choosing (a) — forgetting the gearing mechanism |
| MC.12 | (b) | Higher correlation → defaults cluster → lower probability of ONE default → FTD spread tightens. | Choosing (a) — applying equity diversification logic |
| MC.13 | (b) | CMS rate is a linear payoff on a convex price function. Jensen's inequality creates the adjustment. | Choosing (a) — conflating CMS level with the adjustment mechanism |
| MC.14 | (c) | P&L = (σ²_realized − K²) × vega / (2K) = (625−400)/(40) = 5.625. | Choosing (a) — using vol instead of variance |
| MC.15 | (b) | Bank calls when steepener works → investor loses exposure at the best time. | Choosing (a) — credit risk exists for all notes |
| MC.16 | (b) | NTD: short correlation. FTD: long correlation. Opposite. | Choosing (a) — CDO equity is similar to FTD, not opposite |
| MC.17 | (b) | Target reached = early redemption at par. Reinvestment at prevailing (possibly lower) rates. | Choosing (a) — TARN target means termination, not acceleration |
| MC.18 | (b) | Higher correlation → expected loss on equity tranche decreases (defaults cluster, but when they don't cluster, losses are smaller). | Choosing (a) — confusion about correlation direction |
| MC.19 | (b) | 1/K² weighting from the log-contract replication argument. | Choosing (a) — common misremembering |
| MC.20 | (b) | Snowball = ALL missed coupons accumulate. Full cumulative payout on recovery. | Choosing (a) — confusing SNOW (cumulative) with Phoenix (memory = carry forward, but individual) |
| MC.21 | (b) | Below strike → put exercised → conversion at strike rate (1.05). Investor receives EUR at the STRIKE rate, not market rate. | Choosing (c) — confusing strike with market rate |
| MC.22 | (b) | STEG coupon = f(CMS30Y − CMS2Y). Steep curve → wide spread → high coupon. | Choosing (d) — SRT benefit from rates but not specifically from steepness |
| MC.23 | (b) | The desk sold vol at 25% (implied) and hedged at 15% (realized). The desk keeps the difference. | Choosing (a) — the investor's coupon is fixed at inception; they don't benefit from low realized vol |
| MC.24 | (a) | Stochastic spread in 2F model allows scenarios where spread narrows, reducing coupon accumulation and delaying or preventing target. | Choosing (b) — computation error is random, not directional |
| MC.25 | (a) | The Gaussian copula assumes a specific (thin) tail dependence structure. Actual defaults were more clustered in the tail than Gaussian predicted. | Choosing (c) — CDOs were hedged; the hedges failed because the model was wrong |

**Short Answer Key:**

| Q | Correct Answer | Common Mistake |
|:-:|---------------|---------------|
| SA.1 | The investor sells a put option to the bank. The put premium funds the enhanced coupon. If the stock crashes through the barrier, the investor bears the loss — this is the "price" of the higher coupon. | Saying "the bank generates the extra coupon from its balance sheet" — no, it comes from the embedded option. |
| SA.2 | The "guarantee" is a promise from the issuing bank. If the bank defaults (as Lehman did in 2008), the protection fails. PPN also has zero return risk in flat/down markets — opportunity cost is real. | Saying "the main risk is market risk" — PPN IS protected against market risk. Issuer credit risk is the primary residual. |
| SA.3 | CLN is funded (investor buys a note, cash at risk). CDS is unfunded (pure swap, no cash upfront). CLN has dual credit risk (reference entity + issuer). CDS isolates reference entity risk. Recommend CLN for funded investment; CDS for hedging or speculation. | Saying they are "the same thing in different formats" — the dual credit risk of CLN is a fundamental difference. |
| SA.4 | If the stock is below the coupon barrier, the coupon is not paid but "remembered." When the stock recovers above the barrier, all accumulated missed coupons are paid at once. This matters because it gives the client a recovery mechanism — even if coupons are missed temporarily, they aren't lost forever. | Confusing memory with snowball — memory carries forward individual missed coupons; snowball accumulates them multiplicatively. |
| SA.5 | Most structured products contain short options (RC, Phoenix, WOAC). In high vol, option premiums are rich, allowing the desk to offer higher coupons to clients while retaining wider margins. High vol = expensive options = attractive products. | Saying "high vol is bad for the desk" — the desk is SELLING vol to clients, so rich premiums benefit the desk. |
| SA.6 | FTD triggers on the FIRST default. With low correlation, each name defaults independently. The probability of at least one default in a 5-name basket is 1−(1−p)^5, which is much higher than p. With high correlation, names either all default or all survive, reducing the "one name defaults alone" scenario. | Applying equity logic: "diversification reduces risk" — true for equity portfolios, false for FTD. |
| SA.7 | Phoenix coupon is CONDITIONAL — paid only if the stock is above the coupon barrier. In a market decline, the coupon stops. For guaranteed income, recommend FCN (fixed coupon regardless of stock performance) or IR Callable (fixed rate income). | Not correcting the client — a structurer must identify the misconception and redirect. |
| SA.8 | CMS rates are paid on the CMS rate itself (a linear function of rate). But bond prices are convex in rates. The difference creates a Jensen's inequality effect: E[CMS] > forward rate. This "convexity adjustment" is positive and model-dependent — different vol models produce different adjustments, making it the largest source of STEG model risk. | Saying "convexity adjustment is small" — it can be 10–20bp for long-dated STEG, which materially affects coupon. |
| SA.9 | Variance swap payoff = σ²_realized − K². Volatility is σ. If σ doubles from 15 to 30, variance goes from 225 to 900 — a 4× increase. This is convexity: variance payoff is quadratic in vol, while a vol swap payoff would be linear. Short sellers of variance face unlimited, convex losses. | Treating variance and volatility as interchangeable — the 2× vol → 4× variance relationship is the critical distinction. |
| SA.10 | The Gaussian copula is a model, not a cause. It underestimated tail dependence — defaults were more correlated in stress than the model predicted. But the model was used despite known limitations because it was computationally tractable and market-standard. The failure was in how the model was applied (as truth rather than approximation) and in the governance around model limitations, not in the mathematics itself. | Saying "the model was fine, it was just bad luck" — the model had known deficiencies that were ignored. Or saying "the model caused the crisis" — over-simplistic. |

**Mini Case Answer Key:**

| Case | Recommended | Reasoning | Rejected | Key Risk |
|:----:|-----------|-----------|----------|----------|
| MC.1 | SD (2) for first €100K + PPN (2) for remainder | Capital protection required. SD under deposit insurance. PPN for excess. 5-year maturity OK for both. | RC (no protection), Phoenix (no protection) | Opportunity cost; issuer credit risk on PPN portion; participation rate may be low in low-rate environment |
| MC.2 | Monthly FX forward strip (FWD) | Simple hedging need → simplest product. Lock in EUR/USD rate for each month's receivables. | XCCY (overkill — no debt conversion), DCI (yield product, not hedge) | Opportunity cost if EUR strengthens; basis risk if receivable timing shifts |
| MC.3 | Phoenix (6) or RC (3) | Phoenix: quarterly observation, conditional coupon 8–12%. RC: simpler, coupon 6–9%. Both within PB cap (8). | WOAC (8) — within cap but correlation risk may be unsuitable. CDO (10) — exceeds cap. | Barrier breach risk; autocall/reinvestment risk for Phoenix |
| MC.4 | Vanilla STEG (5) | Steepener income without call risk. 15-year duration matches liability. Coupon linked to curve slope. | Callable STEG (call risk explicitly prohibited by client), TARN STEG (duration certainty violated by target termination) | Zero coupon if curve flattens/inverts |
| MC.5 | Long FTD protection + short NTD protection on same basket | FTD: long correlation (benefits from high corr, loses from low corr → pays off if corr drops). NTD: short correlation (benefits from low corr → offsets carry cost). Net position profits from decreasing correlation. | Straight CDS (no correlation view), single-name trades (no basket correlation exposure) | Model risk on correlation; basis between FTD and NTD hedging; liquidity in stress |

---

## 4.7 Regulatory & Governance Questions

### Beginner

RG.1 [WT] What is the difference between "suitability" and "appropriateness" under MiFID II?

RG.2 What is a PRIIPs KID and what information must it contain?

RG.3 [WT] What is client categorization under MiFID II? Name the three categories and what each means for product access.

RG.4 Why must a bank classify a structured product before distributing it? What is "product governance"?

RG.5 A retail client wants to buy a Complexity 8 WOAC. What regulatory checks are required?

### Intermediate

RG.6 [WT] Explain the concept of "target market" under MiFID II product governance. Who defines it and when?

RG.7 What is the SRI (Summary Risk Indicator) on a PRIIPs KID? How is it calculated for a barrier product like an RC?

RG.8 A client receives a KID that shows a "stress scenario" return of −40%. The client says "that can't happen to a capital-protected product." Is the client correct? (Trick: depends on the product — PPN stress scenario is near 0%, not −40%.)

RG.9 [WT] What is "best execution" for a structured product? How does it differ from best execution for equities?

RG.10 A sales person recommends a product outside the defined target market. What governance steps are triggered?

### Advanced

RG.11 How does the complexity cap in the persona framework (Retail = 4, PB = 8) relate to MiFID II product governance requirements? Are they the same thing? *What The Interviewer Is Testing: Internal governance (persona caps) vs external regulation (MiFID target market). Internal may be stricter. They overlap but are not identical.*

RG.12 A CLN has dual credit risk (reference + issuer). How should the PRIIPs KID represent this? Should the SRI reflect one or both credit risks? *What The Interviewer Is Testing: Regulatory nuance. The SRI should capture the combined credit risk, but the methodology may not fully reflect the dual exposure.*

RG.13 [WT] Explain the "appropriateness" test for complex products. When can a bank proceed even if the client fails the test? *What The Interviewer Is Testing: Execution-only exception. In execution-only (no advice), the bank can proceed with a warning. In advisory, the bank must refuse.*

RG.14 *Expert.* A bank structures a bespoke CDO tranche for a single institutional client. What MiFID II product governance obligations exist for a product with a target market of one? *What The Interviewer Is Testing: Product governance applies even for bespoke. Target market can be narrow but must exist. Post-sale monitoring still required.*

RG.15 What are the disclosure requirements for structured products under MiFID II? List 5 items that must be disclosed pre-trade.

### Governance Judgment

RG.16 [WT] A retail client wants to invest €50,000 in a Phoenix autocallable. The client's annual income is €40,000 and this represents 80% of their savings. Should you proceed? Why or why not?

RG.17 *Advanced.* A structurer discovers that a product sold last month no longer fits the target market definition due to a regulatory update. What actions are required? *What The Interviewer Is Testing: Post-sale monitoring obligation. Notify compliance → assess existing positions → determine if remediation is needed → update target market for future sales.*

RG.18 A sales person offers a WOAC to a client categorized as "Professional" (institutional). The WOAC is Complexity 8. No suitability check is required for Professional clients. Is the sales person correct? *What The Interviewer Is Testing: MiFID II: appropriateness test may still apply depending on the service provided. Professional categorization reduces but does not eliminate obligations.*

RG.19 [WT] *Expert.* Compare regulatory treatment of structured deposits vs structured notes under PRIIPs. Why does this distinction matter? *What The Interviewer Is Testing: Structured deposits are covered by PRIIPs (KID required) AND deposit guarantee scheme. Notes are covered by PRIIPs only. Different investor protection layers.*

RG.20 *Advanced.* An auto-callable Phoenix is redeemed early (autocalled). The investor complains that the bank "took their money back" and wants to know if this is legal. How do you respond? *What The Interviewer Is Testing: Pre-trade disclosure. The autocall mechanism must be clearly disclosed in the KID and term sheet. If it was disclosed, the bank has met its obligation.*

RG.21 What controls should exist around structured product sales? List 5 specific controls. *What The Interviewer Is Testing: Pre-trade (suitability, appropriateness, KID delivery), at-trade (best execution, conflict management), post-trade (complaints, monitoring, target market review).*

RG.22 [WT] *Expert.* A bank is designing a new structured product category. Under MiFID II product governance, what steps must the manufacturer take BEFORE any product is created? *What The Interviewer Is Testing: Product approval process: identify target market → stress-test scenarios → distribution strategy → appoint responsible person → ongoing review mechanism.*

---

# Part 5: Mock Interview Tracks

## 5.1 Structuring Track

### Beginner Variant (60 min)

**Round 1 — Product Knowledge (10 min)**
Quick-fire: explain in 30 seconds each:
1. PPN 2. RC 3. IRS 4. FWD 5. SD

Scoring: Excellent = all 5 clear, concise, identifies key risk. Adequate = 4/5 correct. Poor = <3 correct.

**Round 2 — Technical Deep-Dive (15 min)**
Product 1: PPN — walk through the construction (ZCB + call). Calculate participation rate given: 3Y ZCB cost = $95, ATM call = $12, desk margin = $1.
Product 2: RC — draw the payoff diagram, mark barrier, break-even, and max loss.

Scoring: Excellent = correct calculations + identifies vol/rate sensitivity. Adequate = correct construction. Poor = cannot decompose.

**Round 3 — Case Study (15 min)**
Case: "A client has €200K in a savings account earning 0.2%. They want growth but 'cannot lose money.' They understand that returns may be modest." Recommend and justify.

Scoring: Excellent = recommends SD (deposit insurance) + PPN, explains trade-off, rejects RC. Adequate = recommends PPN. Poor = recommends RC.

**Round 4 — Comparison (10 min)**
Pair 1: PPN vs RC — what's the fundamental difference?
Pair 2: VO vs Warrant — when would you recommend each?

**Round 5 — Anti-Pattern Spotting (10 min)**
"A colleague recommends a Phoenix to a client who says they need guaranteed quarterly income." What's wrong?

### Advanced Variant (60 min)

**Round 1 — Product Knowledge (10 min)**
Quick-fire: VarSwap, FTD, NCRA, WOAC, CRA SRT

**Round 2 — Technical Deep-Dive (15 min)**
Product 1: WOAC — explain worst-of mechanism, correlation sensitivity, and why the coupon is higher than single-stock Phoenix.
Product 2: FTD — derive the correlation effect from first principles. *What The Interviewer Is Testing: Can the candidate explain WHY low correlation increases FTD risk without memorized formulas?*

**Round 3 — Case Study (15 min)**
Case: "An insurance company wants 10-year rate income. Curve is moderately steep (30Y-2Y = 80bp). They accept curve risk but NOT call risk. Budget: 3.5%+ annual income." Walk through the full decision framework.

*What The Interviewer Is Testing: Framework fluency under realistic constraint. Candidate should eliminate callable products, evaluate V.STEG (3.5% achievable at 80bp spread?), consider NCRA as alternative.*

**Round 4 — Comparison (10 min)**
Pair 1: FTD vs NTD — correlation reversal
Pair 2: CRA ELN vs RA STEG — same mechanism, different asset class

**Round 5 — Anti-Pattern Spotting (10 min)**
Scenario 1: "Client wants to sell vol → recommending short VarSwap"
Scenario 2: "Client wants credit yield → recommending CDO to a private banking client"
Scenario 3: "Client wants simple rate hedge → recommending XCCY for single-currency exposure"

---

## 5.2 Trading Track

### Intermediate Variant (60 min)

**Round 1 — Greeks Quiz (10 min)**
For each product, state: delta direction, vega direction, gamma hotspots.
1. RC 2. Phoenix 3. PPN 4. CLN 5. IRS

**Round 2 — Hedging Scenario (15 min)**
"You just sold a €10M Phoenix on Nestlé. Strike at current level, coupon barrier 70%, autocall 100%, quarterly observations, 2-year maturity. Walk me through your day-1 hedge."

**Round 3 — P&L Attribution (15 min)**
"Your RC book shows +€500K P&L today. Vol was flat. Spot dropped 2%. Rates unchanged. Explain."

**Round 4 — Market Stress (10 min)**
"Overnight, implied vol jumps 5 points across the board. Your book is: long 3 Phoenixes, short 1 VarSwap, long 2 PPNs. What happened to your P&L? Walk through each position."

**Round 5 — Risk Limits (10 min)**
"Your barrier proximity metric for the RC book just hit the amber threshold. 60% of notional has barriers within 5% of current spot. What do you do?"

---

## 5.3 Sales Track

### Beginner Variant (60 min)

**Round 1 — Elevator Pitches (10 min)**
30 seconds each: PPN, RC, IRS, Phoenix, SD. To a client with NO derivatives background.

**Round 2 — Client Matching (15 min)**
Client profile: 55-year-old business owner, €2M liquid assets, moderate risk tolerance, needs income, currently 100% in government bonds. Match to product.

**Round 3 — Objection Handling (15 min)**
Client: "I read that structured products are just hidden gambling. The banks always win."
Client: "Why is the coupon so high? What's the catch?"

**Round 4 — Comparison Selling (10 min)**
"A client asks: why should I buy this RC instead of just buying the stock and a bond?"

**Round 5 — Suitability (10 min)**
A retail client wants a WOAC (Complexity 8). Your persona framework caps retail at Complexity 4. The client insists. What do you do?

---

## 5.4 Risk Track

### Expert Variant (60 min)

**Round 1 — Risk Identification (10 min)**
Name top 3 risks: CDO, TARN STEG, VarSwap (short), WOAC, NTD

*What The Interviewer Is Testing: Can the candidate name risks beyond the obvious "market risk"? Correlation, model, liquidity, path dependency.*

**Round 2 — Stress Test Design (15 min)**
Portfolio: 1 WOAC (5 stocks), 1 TARN STEG (CMS spread), 1 short VarSwap. Design 3 stress scenarios and predict the P&L impact on each position.

**Round 3 — Model Risk (15 min)**
"The desk uses Gaussian copula for CDO pricing. You know it underestimates tail risk. What do you recommend? Reject the model entirely? Add reserves? Use alternative copulas?"

*What The Interviewer Is Testing: Practical model risk management — not "change the model" (impractical) but "understand the limitation and reserve against it."*

**Round 4 — Limit Framework (10 min)**
"Design risk limits for a new structured rates desk that will trade V.STEG, C.STEG, RA STEG, and TARN STEG. What metrics, what levels?"

**Round 5 — Regulatory (10 min)**
"The regulator asks: how much capital does the bank hold against its CDO book? Walk through the relevant Basel framework."

---

## 5.5 Model Validation Track

### Expert Variant (60 min)

**Round 1 — Model Identification (10 min)**
"What model for:..." RC, Phoenix, VarSwap, TARN STEG, CDO.

*What The Interviewer Is Testing: RC = Black-Scholes with barrier adjustment. Phoenix = Local vol Monte Carlo. VarSwap = Replication + log contract. TARN STEG = 2-factor HW Monte Carlo. CDO = Gaussian copula (market standard).*

**Round 2 — Calibration (15 min)**
"Your local vol surface doesn't fit the WOAC's observed prices in the wings. The 10-delta puts are 3 vol points off. What is the impact on barrier pricing? How do you resolve?"

**Round 3 — Numerical Methods (15 min)**
"Compare Monte Carlo, PDE, and tree methods for pricing a callable STEG. Which do you choose? Justify on: accuracy, speed, dimensionality, convergence."

**Round 4 — Model Limitations (10 min)**
"When does Black-Scholes fail for: (a) barrier products, (b) variance swaps, (c) autocallables? Name the specific assumption that breaks."

**Round 5 — Back-Testing (10 min)**
"Your Phoenix pricing model systematically overprices by 1.5% on 3-month products but is accurate on 12-month products. Diagnose."

*What The Interviewer Is Testing: Time-dependent bias suggests: (a) short-dated vol surface calibration issue, (b) autocall probability estimation for short maturities, or (c) digital coupon hedging cost underestimation for frequent observations.*

---

## 5.6 Scoring Summary

| Score | Round 1 | Round 2 | Round 3 | Round 4 | Round 5 |
|:-----:|---------|---------|---------|---------|---------|
| **Excellent** | 5/5 with key risks | Correct + identifies second-order effects | Full framework + rejected alternatives + governance | Clear differentiation + trap awareness | All traps identified + explains WHY |
| **Adequate** | 4/5 correct | Mostly correct, misses one dimension | Correct recommendation with reasoning | Identifies main difference | Spots 2/3 traps |
| **Poor** | <3 correct | Cannot decompose the product | Wrong recommendation or no framework | Cannot differentiate | Misses all traps |

---

# Part 6: Interview Traps & Anti-Patterns

## 6.1 Technical Traps (20)

---

**TRAP T.1 — "Delta is the probability of finishing in-the-money"**
Difficulty: Intermediate
The Naive Answer: "Yes, delta equals the probability of the option expiring ITM."
Why It's Wrong: Delta is the hedge ratio (∂V/∂S), not a probability. It approximates the risk-neutral probability of finishing ITM for simple calls, but this breaks for: barrier options (delta discontinuity at barrier), digital options (delta spikes near strike), and variance swaps (delta depends on realized path). Even for vanilla options, delta = N(d1), while the ITM probability is N(d2). They differ by the d1-d2 gap.
The Correct Answer: "Delta is the rate of change of option value with respect to the underlying. It's used as a hedge ratio. For vanilla European calls, it roughly approximates the ITM probability but they're not equal — the exact probability is N(d2), not delta = N(d1)."
Products Affected: All options-based products.

---

**TRAP T.2 — "This product is capital-protected, so it's risk-free"**
Difficulty: Beginner
The Naive Answer: "Yes, 100% capital protection means no risk."
Why It's Wrong: Capital protection is a PROMISE from the issuer. If the issuer defaults, the protection fails (Lehman 2008). Additionally, opportunity cost is real — zero return for 5 years while markets rally is a significant cost.
The Correct Answer: "Capital-protected means the issuer promises to return principal at maturity. The protection is subject to issuer credit risk. Additionally, the investor faces opportunity cost and inflation risk."
Products Affected: PPN, SD, Digital, ZCL, NCRA, CLIQ, SHRK.

---

**TRAP T.3 — "Higher coupon = better product"**
Difficulty: Beginner
The Naive Answer: "Yes, 22% WOAC coupon is obviously better than 10% Phoenix coupon."
Why It's Wrong: Higher coupon = more risk sold. WOAC's 22% coupon comes from selling correlation risk on a basket. The excess coupon compensates for: multiple barrier breach sources, correlation breakdown risk, and lower liquidity.
The Correct Answer: "The coupon reflects the amount of risk the investor is selling. A higher coupon means the investor is accepting more risk. The question is whether the coupon adequately compensates for the additional risk, not whether it's 'better.'"
Products Affected: All yield-generating products.

---

**TRAP T.4 — "Diversification protects WOAC investors"**
Difficulty: Advanced
The Naive Answer: "Having 5 blue-chip stocks diversifies the risk."
Why It's Wrong: WOAC uses worst-of observation — the WORST stock drives ALL outcomes. Diversification in a portfolio reduces risk because good performers offset bad ones. In WOAC, the worst performer dominates — more stocks = more chances for one to breach the barrier.
The Correct Answer: "In a WOAC, diversification INCREASES risk. Each additional stock is another potential barrier breach. The worst-of mechanism converts portfolio diversification into concentration risk."
Products Affected: WOAC, SNOW (worst-of variant).

*What The Interviewer Is Testing: Can the candidate reverse their equity portfolio intuition for structured products?*

---

**TRAP T.5 — "VarSwap short = selling insurance, limited risk"**
Difficulty: Advanced
The Naive Answer: "Short variance is like selling earthquake insurance — small premium, rare payout."
Why It's Wrong: The payout is CONVEX. A 2× vol move creates 4× variance move. There is no cap. In Feb 2018, XIV (short VIX ETN) lost 96% in one day. The "small premium, rare payout" is true for vol but the convexity makes the tail payout catastrophic.
The Correct Answer: "Short variance has theoretically unlimited, convex loss. A 2× vol spike creates 4× P&L impact. This is fundamentally different from selling a straddle (linear vol exposure). The convexity makes short variance the most dangerous short-vol position."
Products Affected: VarSwap.

*What The Interviewer Is Testing: Convexity understanding. Variance ≠ volatility.*

---

**TRAP T.6 — "Autocall is good for the investor"**
Difficulty: Intermediate
The Naive Answer: "When the stock goes up and the note autocalls, the investor gets their money back plus coupons. That's a good outcome."
Why It's Wrong: The investor's position was profitable and growing. Autocall terminates it. The investor must then reinvest at lower coupons (because vol has dropped). The bank recalls the note precisely when it's cheapest for the bank. Autocall is good for the BANK, not the investor.
The Correct Answer: "Autocall returns principal when the underlying is above the trigger — the investor's position was winning. Termination forces reinvestment, typically at lower coupons because market conditions have improved (lower vol). Autocall is structurally advantageous for the bank."
Products Affected: Phoenix, FCN, DKIP, SNOW, WOAC.

---

**TRAP T.7 — "Guaranteed coupon means the product is safe"**
Difficulty: Intermediate
The Naive Answer: "FCN pays guaranteed coupon, so the product is safe."
Why It's Wrong: Guaranteed coupon ≠ guaranteed principal. FCN pays the coupon NO MATTER WHAT. But if the stock falls below the KI barrier at maturity, the investor loses capital. A product can pay 8% coupon while the investor loses 30% of principal.
The Correct Answer: "Guaranteed coupon and capital protection are independent features. FCN guarantees the coupon but the principal is contingent on the barrier. The investor can receive guaranteed income while losing significant capital."
Products Affected: FCN.

---

**TRAP T.8 — "CMS rate equals the forward rate"**
Difficulty: Advanced
The Naive Answer: "The 10-year CMS rate for a STEG is just the 10-year forward swap rate."
Why It's Wrong: CMS pays on the swap rate itself (a linear function of rate). But the swap rate is a nonlinear function of the discount factor. Jensen's inequality creates a positive "convexity adjustment." CMS rate > forward rate. For long-dated STEGs, this adjustment can be 10–20bp.
The Correct Answer: "CMS rate exceeds the forward rate by the convexity adjustment, which arises from Jensen's inequality applied to the nonlinear relationship between rate and price. This adjustment is model-dependent and is the largest source of STEG pricing risk."
Products Affected: V.STEG, C.STEG, RA STEG, TARN STEG.

*What The Interviewer Is Testing: Technical depth on rate products. This is the #1 rates interview question for structuring roles.*

---

**TRAP T.9 — "No principal at risk means no risk" (IRS)**
Difficulty: Intermediate
The Naive Answer: "IRS has no principal exchange, so there's no risk."
Why It's Wrong: A 30-year IRS has a DV01 of ~25bp per $1M notional. A 100bp rate move creates ~$2.5M MTM exposure. The mark-to-market risk on long-dated swaps can be enormous despite no principal exchange.
The Correct Answer: "IRS has no principal risk at inception but significant mark-to-market risk during life. DV01 × rate move determines exposure. Long-dated swaps can have MTM exposure equivalent to a meaningful fraction of notional."
Products Affected: IRS, VLSP, TRS, EqSwap, CDS, XCCY, CommSwap.

---

**TRAP T.10 — "Low correlation = safer FTD basket"**
Difficulty: Expert
The Naive Answer: "Low correlation between the 5 names means the basket is diversified, so FTD is safer."
Why It's Wrong: FTD triggers on the FIRST default. Low correlation means defaults are independent — the probability of at least ONE default occurring is higher. FTD is LONG correlation — the investor benefits from high correlation.
The Correct Answer: "FTD correlation effect is counterintuitive. Low correlation means independent defaults, increasing the probability that at least one name defaults. High correlation means defaults cluster, reducing the probability of an isolated single default. FTD risk increases as correlation decreases."
Products Affected: FTD, and by extension CDO equity tranche.

*What The Interviewer Is Testing: The single deepest concept in credit derivatives.*

---

**TRAP T.11 — "Recovery rate doesn't matter for CDS"**
Difficulty: Intermediate
The Naive Answer: "CDS spread reflects default probability. Recovery is just an assumption."
Why It's Wrong: CDS spread ≈ PD × (1 − Recovery). If you assume 40% recovery, a 100bp spread implies ~1.67% annual PD. If actual recovery is 20%, the loss-given-default is 80% instead of 60% — a 33% increase in potential loss. Recovery assumptions directly affect CDS pricing and hedging.
The Correct Answer: "Recovery rate is a critical input. Standard assumption is 40% for senior unsecured, but actual recovery varies enormously (Lehman: ~8.6%). CDS pricing, hedging ratios, and expected loss all depend on the recovery assumption."
Products Affected: CDS, CLN, Skew CLN, FTD, NTD, CDO.

---

**TRAP T.12 — "Barrier observation is the same whether European or American"**
Difficulty: Intermediate
The Naive Answer: "The barrier is 70% either way."
Why It's Wrong: European barrier: checked only at maturity. American (continuous): checked every moment. The probability of a continuous barrier being breached during the life is MUCH higher than an end-of-life check. Pricing difference can be 30–50% of the option value.
Products Affected: RC, Phoenix, WOAC, Bonus, KODRC, DKIP.

---

**TRAP T.13 — "The vol smile is a market anomaly that should be arbitraged away"**
Difficulty: Advanced
The Naive Answer: "Black-Scholes assumes flat vol. The smile means the market is wrong."
Why It's Wrong: The smile reflects real risk that Black-Scholes ignores: jump risk (crash risk → expensive OTM puts), stochastic vol (vol is not constant), and supply/demand (systematic demand for downside protection). The smile is a FEATURE, not a bug.
Products Affected: All options-based products.

*What The Interviewer Is Testing: Does the candidate understand model limitations vs market reality?*

---

**TRAP T.14 — "Monte Carlo is always the best pricing method"**
Difficulty: Advanced
The Naive Answer: "Monte Carlo handles everything. Just add more paths."
Why It's Wrong: MC is slow (convergence = 1/√N), has difficulty with: American/Bermudan exercise (need LSM or similar), sensitivities (bumping is noisy), and early-exercise optimization. PDE methods are faster for 1–2 factor models. Trees are better for simple American options. MC wins for high-dimensional, path-dependent products (TARN STEG, SNOW) but is overkill for vanilla options.
Products Affected: Product-dependent — match the method to the product.

*What The Interviewer Is Testing: Numerical methods fluency. The right answer is "it depends on the product."*

---

**TRAP T.15 — "Correlation is constant and can be observed"**
Difficulty: Expert
The Naive Answer: "Historical correlation between stocks X and Y is 0.6."
Why It's Wrong: (a) Correlation is not directly observable — only inferable from market prices (implied correlation from basket options) or estimated from historical data (sample-dependent). (b) Correlation is NOT constant — it increases in stress (correlation breakdown/spike). (c) Implied correlation ≠ realized correlation, just as implied vol ≠ realized vol.
Products Affected: WOAC, FTD, NTD, CDO.

*What The Interviewer Is Testing: Deep understanding of the most dangerous hidden risk in structured products.*

---

**TRAP T.16 — "PPNs are unattractive when rates are low"**
Difficulty: Intermediate
The Naive Answer: "Low rates → expensive ZCB → low participation. PPNs are bad."
Why It's Partially Wrong: The statement is directionally correct but incomplete. Low rates also mean lower forward prices (carry cost is lower), which can make the call option cheaper. The NET effect depends on the relative impact. More importantly, features like caps, averaging, and basket structures can improve participation even in low-rate environments.
Products Affected: PPN, SD, SHRK, CLIQ.

---

**TRAP T.17 — "Forward price = expected future spot price"**
Difficulty: Beginner
The Naive Answer: "The 6-month forward is $105 because the market expects the stock to be at $105."
Why It's Wrong: Forward price = Spot × e^(r−q)T. It reflects CARRY COST, not a forecast. The forward can be above spot (positive carry) or below (negative carry) regardless of where the market "expects" the stock to go. Futures/forwards are priced by arbitrage, not by prediction.
Products Affected: FWD, CommSwap, FX forwards.

---

**TRAP T.18 — "Short-selling CDS is free money in good times"**
Difficulty: Advanced
The Naive Answer: "CDS spreads have been tight for years. Selling protection is easy carry."
Why It's Wrong: CDS spread carry is compensation for jump-to-default risk. The "easy carry" regime ends abruptly when a credit event occurs. The P&L pattern is: many small gains (carry) followed by one catastrophic loss (default). This is the "picking up pennies in front of a steamroller" pattern.
Products Affected: CDS, CLN.

*What The Interviewer Is Testing: Understanding of carry vs risk in credit. The candidate who says "I'd sell CDS protection in a low-spread environment" is demonstrating the exact thinking that led to 2008 losses.*

---

**TRAP T.19 — "Digital options are easy to hedge because the payoff is simple"**
Difficulty: Advanced
The Naive Answer: "Binary outcome, simple payoff."
Why It's Wrong: The payoff is simple but the HEDGE is not. Near the digital strike, the delta is theoretically infinite (step function). In practice, dealers replicate digitals with tight call spreads, but the replication is imperfect. The tighter the spread, the better the replication but the larger the gamma exposure.
Products Affected: Digital, DKIP, CRA ELN, NCRA, Digital CF.

---

**TRAP T.20 — "The Gaussian copula is 'wrong' for CDO pricing"**
Difficulty: Expert
The Naive Answer: "The Gaussian copula caused the 2008 crisis. We should use a different model."
Why It's Wrong: The Gaussian copula is the market standard — prices are QUOTED in terms of implied correlation from this model. Saying it's "wrong" is like saying Black-Scholes is "wrong" for options — true in absolute terms, but the model is used as a quotation convention and risk management tool. The problem in 2008 wasn't the model per se — it was treating the model's outputs as truth rather than approximation, and ignoring known limitations (thin tails, static correlation).
The Correct Answer: "The Gaussian copula is a useful quotation and risk management tool with known limitations. The 2008 failure was in model governance — using a model beyond its valid domain without adequate reserves for its known weaknesses."
Products Affected: CDO, and by extension all correlation products.

*What The Interviewer Is Testing: Maturity. Can the candidate hold nuance — acknowledging model limitations while understanding why the model persists?*

---

## 6.2 Behavioral / Framing Traps (10)

**BT.1 — "Tell me a trade you would put on today."**
What's being tested: Conviction + structured reasoning. There is no "right" trade. The interviewer wants to see: (1) market view articulated clearly, (2) product selection justified, (3) risks acknowledged, (4) sizing discussed. Candidates who hedge excessively ("well it depends...") fail. Candidates who pick a trade without discussing risks also fail.

**BT.2 — "This product seems really risky. Convince me otherwise."**
What's being tested: Risk reframing. DON'T deny the risk. Acknowledge it, then reframe: "The risk is compensated. The coupon reflects the probability and severity of the downside scenario. The question isn't whether there's risk — it's whether the risk is adequately compensated."

**BT.3 — "Walk me through your thought process."**
What's being tested: Structured thinking. Use a framework. The 10-step decision model from the Solutions Manual provides the structure. Candidates who ramble through products randomly fail. Candidates who say "Step 1: identify the objective, Step 2: determine cash flow needs..." pass.

**BT.4 — "The client insists on a product you think is unsuitable. What do you do?"**
What's being tested: Compliance awareness + diplomacy. The answer is NOT "give the client what they want." The answer is: document your concerns, explain the risks clearly, offer alternatives, and escalate to compliance if the client insists. You cannot override suitability requirements regardless of client pressure.

**BT.5 — "You have 30 seconds — pitch me this product."**
What's being tested: Elevator clarity. Use the Tier 1 framework: what it IS, who buys it, one key risk. Candidates who try to cram Tier 4 depth into 30 seconds fail.

**BT.6 — "Your model says one thing, the market says another. Who's right?"**
What's being tested: Humility. The market is right until proven otherwise. If your model disagrees with the market, the model has a problem — not the market. Investigate: calibration issue? Missing risk factor? Liquidity premium?

**BT.7 — "Describe a time you were wrong about a trade."**
What's being tested: Self-awareness + learning. The interviewer wants: (1) honest admission of error, (2) what went wrong (diagnosis, not blame), (3) what changed (process improvement, not just "I lost money"). Candidates who claim they've never been wrong fail.

**BT.8 — "Why structured products and not [other asset class]?"**
What's being tested: Genuine interest. The good answer connects to what makes SP intellectually interesting: the intersection of client needs, mathematical modeling, and risk management. The bad answer is "it pays well."

**BT.9 — "A client calls in a panic — the stock just dropped 15% and their RC barrier is at 70%. Current level is 72%. What do you say?"**
What's being tested: Client management under pressure + risk awareness. Steps: (1) Acknowledge the concern. (2) State the facts: still above barrier, coupon is still being paid. (3) Discuss scenarios: if stock recovers, client is fine; if it drops further, barrier breach. (4) Discuss options: hold to maturity, attempt secondary market sale (at a loss), or hedge with a put. Do NOT say "don't worry."

**BT.10 — "Explain correlation risk to a teenager."**
What's being tested: Communication ability. Good analogy: "Imagine 5 friends. If they always go to the same parties (high correlation), either they ALL get sick or NONE of them get sick. If they go to different parties (low correlation), the chance that AT LEAST ONE gets sick is higher. A WOAC is betting that none of them get sick."

---

## Traceability

| Source Artifact | Role in Interview System |
|----------------|------------------------|
| Product DNA Atlas (frozen) | Product features, complexity scores, Appendix E/F/G |
| Product Comparison Matrix | Dimensional comparisons, decision trees, confusion pairs |
| Desk Bible v2 chapters (49) | §1 (Tier 1), §11 (Tier 2), §14 (Tier 3), §15 (Risk), §19 (curated), §20 (synthesized) |
| Solutions Manual (frozen) | REFERENCED for framework, scenarios, anti-patterns — never reproduced |
| Learning Dependency Graph | Difficulty calibration via complexity bands |
| Product Evolution Map | Family progression for comparison pairs |

---

*Interview System complete. 49 products. 5 roles. 4 difficulty levels. 210+ core questions. 40 written assessment items. 22 regulatory questions. 5 mock tracks. 30 traps. 2026-06-22.*
