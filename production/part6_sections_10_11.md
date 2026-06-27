## 6.10 The Practitioner's Desk

*How the desk actually talks and works — vocabulary, organization, and the daily rhythm of structured products*

### The Language of the Desk

Every profession has its own language. A surgeon does not say "cut the skin open" — they say "make an incision." A lawyer does not say "the contract is broken" — they say "the party is in material breach." The structured products desk has its own vocabulary too, and understanding this vocabulary is the difference between understanding the concepts and being able to work on the desk.

This section bridges that gap. Parts 1 through 5 taught you what structured products are, how they work, and how to analyze them. This section teaches you how the people who trade them every day actually communicate.

---

### Desk Organization

**Flow Book vs Exotic Book**

Most structured products desks divide their trading activity into two books:

The **flow book** handles standardized, high-volume products: vanilla Reverse Convertibles, standard FCNs, plain autocallables on major indices. These products follow established templates, price quickly, and trade frequently. The flow book is the assembly line — efficient, predictable, high throughput.

The **exotic book** handles complex, bespoke structures: worst-of autocallables with custom barriers, path-dependent payoffs, multi-asset structures, CDO tranches. These products require significant structuring effort, careful model selection, and individual risk assessment. The exotic book is the custom workshop — slower, more skilled, higher margin per trade.

| Dimension | Flow Book | Exotic Book |
|-----------|-----------|-------------|
| Products | Standard RCs, FCNs, vanilla swaps | Worst-of, path-dependent, CDOs, bespoke |
| Volume | High (dozens per day) | Low (a few per week) |
| Margin per trade | Low ($5K–$50K) | High ($50K–$500K+) |
| Pricing | Automated or semi-automated | Manual, model-intensive |
| Hedging | Delta + Vega, relatively straightforward | Multi-Greek, correlation, gap risk |
| Model risk | Low (well-understood models) | High (model choice matters significantly) |
| Trader skill | Efficient execution, position management | Deep mathematical understanding, judgment |

**Inventory**

The desk's **inventory** is its outstanding portfolio of risk positions. "The desk has $500M of short vega inventory" means the desk has sold $500M notional of products that are short volatility — it will lose money if implied vol rises. Inventory management is one of the trader's core responsibilities: too much inventory in one direction creates concentration risk; too little means the desk is not earning its margin.

**Axed**

When a desk is **axed** in a product, it is actively trying to trade it. "We're axed in 1-year Euro Stoxx autocalls" means the desk is marketing that product aggressively — typically because it helps the desk's inventory position (e.g., buying back some of its short vega by selling autocallables that create offsetting risk).

---

### Risk Warehousing

Instead of hedging every single product perfectly and immediately, a structured products desk typically accumulates risk from multiple trades and hedges the **net position**. This is called **risk warehousing**.

*Analogy:* Think of a shipping company. It would be inefficient to send a separate truck for every single package. Instead, the company warehouses packages at a distribution center, groups them by destination, and sends full trucks. The structured products desk does the same with risk — it warehouses individual trade risks, nets them against each other, and hedges the residual.

**Why desks do it:**

1. **Offsetting risks cancel out.** If the desk sells a product that is short vega on the S&P 500 and another product that is long vega on the S&P 500, the net vega may be close to zero — no hedge needed.
2. **Lower transaction costs.** One large hedge trade is cheaper than ten small ones (lower bid-offer spread relative to size).
3. **Better execution.** The desk can time its hedges to coincide with favorable market conditions rather than hedging reactively after every client trade.

**The risk:**

Warehouse risk is the risk that accumulated inventory moves against the desk before it can be hedged or offloaded. If the desk has $200M of short gamma inventory and the market gaps through a barrier level overnight, the losses can be severe. Risk limits exist precisely to prevent excessive warehousing.

---

### Hedge Vocabulary

| Term | Meaning | Example |
|------|---------|---------|
| **Internal hedge** | Hedge executed with another desk within the same bank | SP desk buys vol from the flow options desk |
| **External hedge** | Hedge executed in the external market | Buying listed options on an exchange |
| **Back-to-back** | An offsetting trade with an external party that exactly mirrors the client risk | Zero residual risk, but lower margin |
| **Delta neutral** | Net delta exposure is zero — no directional risk | Does NOT mean zero risk (gamma, vega remain) |
| **Flat** | No position in a particular risk factor | "The desk is flat gamma" = zero net gamma |
| **Covered** | The risk has been hedged | "The vega is covered" |
| **Residual** | Risk that remains after hedging | Model error, basis risk, gap risk |
| **Unwind** | Close out a position or trade | "We unwound the hedge" |

---

### Greeks Positioning Language

Part 1 taught what the Greeks **are**. This section teaches how the desk **talks** about them.

**Long Gamma**

The desk benefits from large market moves in either direction. When the market moves, long gamma positions generate positive P&L because the delta hedge creates a "buy low, sell high" dynamic. The desk buys as the market falls (becoming more negative delta, requiring more long stock) and sells as the market rises.

Typical of desks that have **bought** options. Rare for structured product desks, which usually sell options to clients.

**Short Gamma**

The desk loses from large market moves. Near barrier levels, short gamma becomes extremely painful because delta changes rapidly — the desk must buy high and sell low to maintain delta neutrality. This is the dominant position for most structured product desks, because clients buy products that embed short put options.

*Why it matters:* A trader who says "I'm short 50 million gamma in AAPL" is telling you that a 1% move in Apple creates approximately $500K of P&L impact that must be hedged immediately. Near barriers, this can spike dramatically.

**Long Vega**

The desk benefits from rising implied volatility. Less common for structured product desks. When present, it is usually because the desk bought back some of its short vega exposure through listed options or variance swaps.

**Short Vega**

The desk loses from rising implied volatility. This is the natural position for a structured product desk — because the products sold to clients embed options, and selling options creates short vega. A vol spike can create significant mark-to-market losses across the entire portfolio.

**Long Correlation**

The desk's **net (hedged)** position benefits when asset correlations increase. Worst-of products create long correlation exposure for the hedged desk: when correlations are high, the basket moves together, reducing the probability that the worst performer hits the barrier. This benefits the desk's hedged book. (Note: the **investor** sold the embedded put and is structurally short correlation; the desk is long the put and hedges its raw short-correlation exposure via dispersion trades to achieve a net long-correlation position.)

**Short Correlation**

The desk loses when correlations increase. Less common for structured products; more typical of correlation trading desks or certain CDO structures.

| Family | Typical Desk Greek Position |
|--------|---------------------------|
| ELN (RC, FCN, Phoenix) | Short gamma, short vega, long correlation (worst-of, **net/hedged** position) |
| Swaps | Varies — rate swaps are directional; equity swaps depend on structure |
| SRT | Long convexity (CMS products), moderate vega |
| STEG | Sensitive to curve steepness, moderate rate-tenor correlation |
| CLN | Short credit spread, short jump-to-default risk |

---

### Role-Specific Vocabulary

**Structurer Language**

| Term | Meaning |
|------|---------|
| Reverse inquiry | Client asks for a bespoke product rather than choosing from a menu |
| Bespoke | Custom-designed for a specific client |
| Vanilla wrapper | Simple product structure wrapping complex economics |
| Pricing request / RFQ | Client asks for a price on a specific product specification |
| Indication | Preliminary price (not binding) |
| Firm price | Binding price the desk commits to trade at |
| Payoff diagram | Visual representation of the product's return profile |
| Barrier shift | Adjusting the barrier level to change the risk/return trade-off |

**Trader Language**

| Term | Meaning |
|------|---------|
| Axed | Actively looking to trade a specific product or risk |
| Lifted | Sold. "We got lifted on the 3-year autocall" = client bought it |
| Working | Actively trying to execute a hedge in the market |
| Hit the bid | Sold at the bid price (accepting lower price for speed) |
| Paying the offer | Bought at the offer price |
| Size | Large notional. "There's size in the name" = large trades happening |
| Bid-offer | Spread between buy and sell price — the desk's compensation |
| Scratched | Executed at no profit or loss |
| Stuffed | Holding unwanted inventory that is hard to offload |

**Sales Language**

| Term | Meaning |
|------|---------|
| Suitability | Whether the product fits the client's risk profile and objectives |
| Target market | Intended client segment for a product (MiFID II requirement) |
| IOI (Indication of Interest) | Early-stage expression of interest from a client |
| Pre-trade disclosure | Risk, cost, and conflict information provided before execution |
| Execution-only | Client makes their own investment decision; bank provides no advice |
| Advisory | Bank recommends the product; higher suitability obligation |

**Risk Language**

| Term | Meaning |
|------|---------|
| Limit breach | A risk limit has been exceeded — must be reported and remediated |
| VaR | Maximum expected loss at a given confidence level over a given horizon |
| Stress test | Hypothetical extreme scenario applied to the portfolio |
| Scenario analysis | "What if" analysis for specific market conditions |
| Concentration risk | Too much exposure to one name, sector, or risk factor |
| Notional limit | Maximum notional per counterparty, product, or underlying |

**Product Control Language**

| Term | Meaning |
|------|---------|
| Flash | Preliminary P&L estimate (pre-IPV, pre-reserves) |
| Official | Verified, reconciled P&L — the number that matters |
| Unexplained | P&L not attributable to any risk factor — a red flag |
| Reserve | Valuation adjustment for uncertainty |
| IPV break | Independent price differs from trader mark beyond tolerance |
| New deal P&L | Manufacturing margin captured on trade date |

**Operations Language**

| Term | Meaning |
|------|---------|
| Break | Discrepancy between two records that should match |
| Fail | Settlement that did not occur on the expected date |
| SSI | Standard Settlement Instructions — pre-agreed bank accounts |
| Static data | Reference data that rarely changes (counterparty, calendar) |
| Golden source | The single authoritative system for a given data type |
| Four-eyes | Two-person review requirement for trade booking |

---

### How a Trade Flows Through the Desk

Here is the end-to-end journey of a 1-year Phoenix Autocallable on the Euro Stoxx 50:

**Day 0 — Origination**
1. A private bank client tells their relationship manager they want enhanced yield on European equities with some downside protection.
2. **Sales** calls the structuring desk with the client profile: risk tolerance = moderate, investment horizon = 1 year, target coupon = 8%+.
3. **Structurer** designs a Phoenix Autocallable: 1-year, quarterly observation, 10% conditional coupon, 70% knock-in barrier, 100% autocall barrier on Euro Stoxx 50. Runs the pricing model.
4. Structurer sends an indicative termsheet to Sales with an 11% coupon (manufacturing margin embedded).

**Day 1 — Execution**
5. Sales presents the termsheet to the client. Client accepts.
6. Sales confirms the trade internally. **Trader** receives the risk.
7. Trader executes the hedge: sells the embedded put option in the interbank market (or warehouses the risk if the desk already needs that exposure), buys delta in Euro Stoxx 50 futures.
8. **Operations** books the trade in NEMO. Four-eyes check against the termsheet.
9. Confirmation sent to counterparty.

**Day 2 — Settlement**
10. Client pays the notional amount. Cash settles via DvP.

**Days 3–365 — Daily Life**
11. Every day: **Trader** manages the hedge (rebalances delta, monitors gamma near barrier). **Product Control** runs P&L explain and IPV. **Risk** monitors exposure against limits.
12. Every quarter: **Operations** checks the Euro Stoxx 50 closing price against the autocall barrier (100%) and coupon barrier.
13. If autocall triggers: Operations processes early redemption, returns notional + coupon to client. Trade ends.
14. If coupon barrier is met but no autocall: Operations processes coupon payment.
15. If coupon barrier is missed: coupon is stored in memory for potential future payment.

**Maturity**
16. Final observation: check Euro Stoxx 50 level vs knock-in barrier and coupon barrier.
17. **Operations** calculates final payoff, initiates settlement.
18. **Product Control** verifies final P&L. Trade is archived.

---

### Day in the Life

| Time | Structurer | Trader | Sales | Risk | Product Control | Operations |
|------|-----------|--------|-------|------|----------------|------------|
| 7:00 | Review overnight pricing requests | Check flash P&L, review positions | Morning prep, review IOIs | Review overnight limit usage | Produce flash P&L | Process overnight fixings |
| 9:00 | Client call — bespoke product discussion | Market opens — execute hedges | Client calls — present indications | Challenge pricing assumptions | Begin IPV checks | Reconcile settlements |
| 12:00 | Run pricing for afternoon inquiries | Manage gamma near barriers | Follow up on outstanding IOIs | Review stress test results | Complete P&L explain | Investigate breaks |
| 15:00 | Finalize termsheets for next-day | Rebalance delta before close | Confirm executed trades with clients | Investigate limit breaches | Challenge trader marks | Confirm new trades |
| 17:00 | Calibration review, next-day prep | Sign off daily P&L | Prepare next-day materials | Prepare risk report | Sign off official P&L | Process lifecycle events |

---

### Common Mistakes

1. **Confusing "short gamma" with "short delta."** Short gamma means you lose from large moves in either direction. Short delta means you lose if the market rises. A desk can be delta-neutral and still have massive short gamma — this is the normal state for a structured products desk near barrier levels.

2. **Thinking "internal hedge" means "no risk."** An internal hedge transfers risk to another desk within the bank — it does not eliminate risk from the bank's perspective. The consolidated risk remains the same. Internal hedges are useful for desk-level risk management but do not reduce the bank's aggregate exposure.

3. **Assuming flow products are simple.** Flow products have simple structures but complex risk management at scale. A desk that has sold 500 autocallables on the same index has massive concentrated gamma and vega exposure that requires sophisticated portfolio-level hedging.

4. **Using desk vocabulary without understanding the underlying concept.** Saying "I'm long correlation" without understanding that this means the desk benefits from assets moving together — and that a correlation breakdown would cause losses — is dangerous. Vocabulary must be backed by understanding.

5. **Ignoring the difference between flash and official P&L.** Flash P&L is an estimate. Official P&L is the verified number. Trading decisions should not be based on flash P&L alone, and management should not react to flash numbers without waiting for the official reconciliation.

> **Professor Note:** If you remember only one thing from this section, remember this: the structured products desk is short gamma and short vega by construction. Clients buy products that embed options — and when the bank sells those options, it becomes short gamma and short vega. Every other aspect of desk management — hedging, risk limits, P&L explain, reserves — follows from this fundamental positioning.

---

## 6.11 Regulatory Framework

*What the regulators require — the rules that govern structured product design, distribution, and risk management*

### The Building Codes of Finance

Regulations are the building codes of finance. Just as a building must meet fire safety, structural integrity, and accessibility requirements regardless of how beautiful the architecture is, a structured product must meet suitability, transparency, and capital requirements regardless of how elegant the financial engineering is.

This section covers the major regulatory frameworks that affect structured products. The goal is not to make you a compliance expert — it is to ensure you understand which rules apply, why they exist, and how they affect the products you will work with.

---

### MiFID II — Markets in Financial Instruments Directive

MiFID II is the European Union's comprehensive framework governing financial markets, investor protection, and transparency. It took effect in January 2018 and fundamentally changed how structured products are designed, distributed, and monitored.

**Product Governance**

Under MiFID II, every financial product must have a clearly defined **target market** — the type of client for whom the product is designed.

The manufacturer (the bank that creates the product) must specify:

| Target Market Dimension | What Must Be Defined |
|------------------------|---------------------|
| Client type | Retail, Professional, Eligible Counterparty |
| Knowledge and experience | What the client needs to understand |
| Financial situation | Minimum wealth, income, loss-bearing capacity |
| Risk tolerance | Willingness to accept losses |
| Investment objective | Growth, income, preservation, hedging |
| Needs and objectives | What problem the product solves |

The manufacturer must also define a **negative target market** — clients who should NOT buy the product under any circumstances. For example, a worst-of autocallable with a 60% barrier should never be sold to a retail client with no derivatives experience and low loss tolerance.

The **distributor** (the sales team or external bank that sells the product) must independently assess whether each client falls within the target market. Selling outside the target market is a regulatory breach.

**Suitability and Appropriateness**

Part 5 of the Bible already covers suitability extensively (105 mentions). MiFID II adds specific procedural requirements:

- **Advisory sales**: the bank must conduct a full suitability assessment — checking knowledge, experience, financial situation, investment objectives, and risk tolerance. The assessment must be documented and provided to the client.
- **Execution-only sales**: the bank must conduct an appropriateness assessment — checking only whether the client has sufficient knowledge and experience to understand the product's risks. If the client fails, the bank must warn them (but the client may still proceed).
- **Portfolio management**: the strictest standard — the bank must ensure the product is suitable within the context of the client's entire portfolio.

**Cost Transparency**

All costs must be disclosed to the client, both in monetary terms and as a percentage:
- Manufacturing costs (structuring, hedging, model costs)
- Distribution costs (sales commission, trailer fees)
- Ongoing costs (management fees, custody fees)
- Exit costs (early redemption penalties)
- Performance-related costs (if applicable)

The disclosure must show the cumulative effect of costs on the client's return — in plain language, before the trade is executed.

**Best Execution**

When executing client orders, the bank must take all sufficient steps to achieve the best possible result for the client, considering:
- Price
- Costs
- Speed
- Likelihood of execution
- Settlement
- Size
- Nature of the order

For structured products, best execution is complex because most products are bespoke OTC instruments with no secondary market. The bank must demonstrate that the pricing was fair relative to the underlying risks.

**Product Intervention**

Regulators can ban or restrict products they consider harmful. ESMA (the European Securities and Markets Authority) has used this power to:
- Ban binary options for retail clients (2018)
- Restrict CFD leverage for retail clients
- Require enhanced warnings for complex products

---

### PRIIPs — Key Information Documents

The PRIIPs regulation (Packaged Retail and Insurance-based Investment Products) requires that every packaged retail investment product comes with a **Key Information Document (KID)** — a standardized, three-page summary that retail investors must receive before investing.

**KID Contents**

| Section | What It Contains |
|---------|-----------------|
| What is this product? | Product description, objectives, intended investor, maturity |
| What are the risks? | Summary Risk Indicator (SRI: 1-7 scale) |
| What could I get in return? | Performance scenarios (favorable, moderate, unfavorable, stress) |
| What happens if the company cannot pay? | Issuer default consequences |
| What are the costs? | Entry, exit, ongoing, performance costs |
| How long should I hold it? | Recommended holding period |
| How can I complain? | Complaints procedure |

**Summary Risk Indicator (SRI)**

The SRI combines market risk and credit risk into a single score from 1 (lowest risk) to 7 (highest risk):

| SRI | Risk Level | Typical Structured Products |
|:---:|-----------|---------------------------|
| 1 | Lowest risk | Capital-guaranteed deposits |
| 2 | Low risk | Principal Protected Notes on major indices |
| 3 | Medium-low | Callable notes with full coupon protection |
| 4 | Medium | Standard autocallables with conditional protection |
| 5 | Medium-high | Reverse Convertibles, Phoenix notes |
| 6 | High | Worst-of autocallables, leveraged products |
| 7 | Highest risk | Warrants, turbos, CDO equity tranches |

Market risk is measured by VaR-equivalent volatility (how much the product's value could fluctuate). Credit risk is based on the issuer's credit rating.

**Performance Scenarios**

The KID must show projected returns under four scenarios, calculated using historical data and forward-looking simulation:
- **Favorable** (approximately 90th percentile outcome)
- **Moderate** (approximately 50th percentile outcome)
- **Unfavorable** (approximately 10th percentile outcome)
- **Stress** (extreme adverse scenario)

These scenarios are controversial because they are based on historical data that may not predict future performance, and the methodology can make some products appear more attractive than their actual risk warrants.

---

### EMIR — European Market Infrastructure Regulation

EMIR is the EU framework governing OTC derivatives. It was introduced after the 2008 financial crisis to reduce systemic risk in the derivatives market.

**Three Pillars of EMIR**

**1. Reporting**

All derivative trades must be reported to a registered Trade Repository within one business day of execution. The report must include:
- Trade identifiers (UTI — Unique Trade Identifier)
- Counterparty details (LEI — Legal Entity Identifier)
- Trade economics (notional, maturity, underlying, price)
- Valuation updates (daily mark-to-market)

Failure to report is a regulatory breach. Most banks automate reporting through middleware that extracts trade details from booking systems (NEMO, Murex) and transmits to the repository.

**2. Clearing Obligation**

Standardized OTC derivatives must be cleared through a **Central Counterparty (CCP)**:
- **Cleared products**: interest rate swaps (IRS) in major currencies, CDS index products (iTraxx, CDX)
- **Not cleared**: most structured products (too bespoke for CCP standardization), single-name CDS, exotic options

How a CCP works:
- When two parties execute a trade, the CCP interposes itself between them via novation
- Party A faces the CCP, and the CCP faces Party B — the CCP becomes the counterparty to both
- The CCP requires initial margin (collateral against potential losses) and daily variation margin (mark-to-market settlement)
- If one party defaults, the CCP uses its default waterfall: defaulter's margin → default fund contribution → CCP's own capital → surviving members' default fund

**3. Risk Mitigation for Non-Cleared Trades**

Derivatives that are not cleared must comply with risk mitigation requirements:
- **Timely confirmation**: within T+1 for electronic, T+2 for non-electronic
- **Portfolio reconciliation**: periodic comparison of positions with counterparties (daily for large portfolios, weekly or quarterly for smaller ones)
- **Portfolio compression**: regular exercises to reduce gross outstanding notional
- **Dispute resolution**: formal process for valuation disputes, with escalation to senior management

---

### UMR — Uncleared Margin Rules

The Uncleared Margin Rules are a global regulation (implemented via national law in each jurisdiction) requiring bilateral exchange of margin for non-cleared derivatives.

**Variation Margin (VM)**

Daily exchange of collateral to reflect changes in the mark-to-market value of the portfolio. If the portfolio value moves in your favor, the counterparty posts collateral to you; if it moves against you, you post to them.

VM has been required for most counterparties since 2017.

**Initial Margin (IM)**

Additional collateral to cover potential future exposure — the risk that the portfolio value could change between the last VM exchange and the close-out of the position after a counterparty default.

IM is required for counterparties whose aggregate average notional amount (AANA) of non-cleared derivatives exceeds regulatory thresholds. Implementation was phased in from 2016 to 2022.

**ISDA SIMM (Standard Initial Margin Model)**

The industry-standard model for calculating bilateral IM:
- Sensitivity-based: calculates IM using risk sensitivities (delta, vega, curvature) rather than full revaluation
- Calibrated to a 10-day, 99% confidence level — meaning the IM should cover losses in 99% of 10-day periods
- Updated annually to reflect current market conditions
- Approved by regulators in most jurisdictions

**Impact on Structured Products**

UMR increases the cost of bilateral (non-cleared) trades by requiring funded collateral. This cost flows into product pricing via MVA (see §6.7). Products that would have been economically viable before UMR may become too expensive after the margin funding cost is included.

**Segregation**

Bilateral IM must be held by an independent third-party custodian — neither party may use or rehypothecate it. This ensures the collateral is available if either party defaults.

---

### Basel Framework — Practical Impact

The Basel framework (Basel III, with Basel IV changes being implemented) sets global minimum standards for bank capital and liquidity. For structured products professionals, the key question is: how does Basel affect the products we trade?

**Credit Risk Capital (SA-CCR)**

The Standardised Approach for Counterparty Credit Risk (covered in §6.7) determines the exposure amount for derivative trades. Higher exposure → higher RWA → higher capital → higher cost.

**Market Risk Capital (FRTB)**

The Fundamental Review of the Trading Book (FRTB) overhauls how banks calculate market risk capital:

| Approach | How It Works | Capital Impact |
|----------|-------------|---------------|
| Standardised (SA) | Formula-based, prescribed risk weights | Higher capital, simpler to implement |
| Internal Models (IMA) | Bank's own VaR/ES models, regulator-approved | Lower capital, but each desk must qualify independently |

FRTB introduces desk-level model approval — each trading desk must individually qualify to use internal models. Desks that fail qualification must use the standardised approach, which typically results in higher capital charges.

**CVA Capital**

A dedicated capital charge for CVA risk — the risk that the bank's CVA changes due to credit spread movements. Banks must hold capital against this risk, which flows into KVA and product pricing.

**Impact on Product Design**

Products that generate high RWA or high market risk capital are less profitable after capital charges. This creates a direct incentive for capital-efficient structuring:
- Products cleared through CCPs have lower capital charges than bilateral products
- Collateralized trades have lower exposure than uncollateralized trades
- Shorter-dated products consume less capital than longer-dated products
- Well-hedged books generate less residual risk capital than directional books

---

### Dodd-Frank — US Regulatory Framework

The Dodd-Frank Wall Street Reform and Consumer Protection Act (2010) is the US equivalent of EMIR for OTC derivatives regulation.

**Title VII** governs swap dealers:
- **Registration**: entities that deal in swaps above de minimis thresholds must register with the CFTC (commodity/rates) or SEC (security-based)
- **Clearing**: standardized swaps must be cleared through a DCO (Derivatives Clearing Organization)
- **Reporting**: all swaps must be reported to a Swap Data Repository (SDR)
- **Margin**: similar to UMR — bilateral margin requirements for non-cleared swaps

**Cross-Border Implications**

Trades between US and non-US entities may be subject to both Dodd-Frank and EMIR (or other local regulations). Substituted compliance provisions exist to reduce duplicative requirements, but the interaction remains complex.

---

### MAR — Market Abuse Regulation

MAR prohibits three categories of market abuse:

1. **Insider dealing**: trading on material non-public information (MNPI)
2. **Market manipulation**: artificially affecting the price or supply of a financial instrument
3. **Unlawful disclosure**: sharing MNPI with others without a legitimate reason

**Relevance to Structured Products**

The desk holds significant MNPI:
- Barrier levels of outstanding products (a stock approaching a barrier could trigger large hedging activity)
- Client order flow (knowing that large client orders are coming)
- Autocall observation dates and levels

Using this information to benefit the desk or personal accounts is illegal. Banks maintain **Chinese walls** — information barriers between departments — and monitor trading activity for potential abuse.

---

### Common Mistakes

1. **Assuming suitability is just a checkbox exercise.** Suitability under MiFID II is substantive — the bank must genuinely assess whether the product is right for the client. Rubber-stamping suitability assessments exposes the bank to regulatory sanctions and client lawsuits.

2. **Ignoring the negative target market.** Defining who should NOT buy the product is as important as defining who should. Regulators specifically check whether products were sold to clients in the negative target market.

3. **Treating the PRIIPs KID as a marketing document.** The KID is a regulatory disclosure document, not a sales tool. Presenting it selectively or emphasizing favorable scenarios while downplaying stress scenarios is a regulatory breach.

4. **Assuming non-cleared means unregulated.** Non-cleared derivatives are subject to EMIR risk mitigation requirements (timely confirmation, portfolio reconciliation, dispute resolution) and UMR margin requirements. "Non-cleared" does not mean "unregulated."

5. **Forgetting cross-border regulatory interaction.** A trade between a London desk and a New York client may be subject to MiFID II, EMIR, Dodd-Frank, and local margin rules simultaneously. Compliance must consider all applicable regimes.

> **Professor Note:** If you remember only one thing about regulation, remember this: regulation exists because the 2008 crisis demonstrated that unregulated derivatives could threaten the entire financial system. Every rule — clearing, margin, reporting, capital, suitability — is a response to a specific failure. Understanding *why* a regulation exists makes compliance intuitive rather than burdensome.

---

## Part 6 — Knowledge Check

### Review Questions

1. A coupon payment date falls on Saturday, December 31. The business day convention is Modified Following, and the relevant calendar is London. When is the coupon paid? What if the convention were Following instead?

2. You are reading a termsheet for a 1-year Reverse Convertible. The Issue Price is 100%, but the settlement amount at maturity says "Clean Price." The trade has been outstanding for 6 months. A colleague says the investor will receive exactly 100% of their notional back (plus coupon) if no barrier is breached. Is this correct? Explain the difference between clean price and dirty price.

3. A bank enters into a derivative with a counterparty. The CSA specifies a Threshold of €10M, an MTA of €500K, and eligible collateral of cash only. The current exposure is €12M. How much collateral should the counterparty post? What if the exposure were €10.3M?

4. A company has the following capital structure: €5B senior secured bonds, €3B senior unsecured bonds, €2B subordinated debt, €1B AT1, €4B common equity. The company defaults and the total recovery is €6B. How is the recovery distributed across creditors?

5. Classify the following structured products into Fair Value Hierarchy levels (1, 2, or 3): (a) a 6-month Reverse Convertible on Apple, (b) a 5-year CDO tranche on a bespoke portfolio, (c) a 1-year autocallable on the Euro Stoxx 50, (d) a 10-year worst-of on three emerging market stocks with no liquid options market.

6. The desk made €800K yesterday. P&L Explain shows: Delta P&L +€500K, Vega P&L −€150K, Theta P&L +€200K, New deals +€50K, Unexplained +€200K. The unexplained threshold is 10% of gross P&L. Should Product Control escalate? What would you investigate?

7. A Reverse Convertible has a notional of €10M, a 6-month tenor, and the underlying stock has a bid-offer spread of 2%. What is the approximate bid-offer reserve? Why does this reserve exist?

8. A bank trades a 5-year interest rate swap with a BBB-rated corporate counterparty. No CSA is in place. Which XVA charges apply? Which would be eliminated if the counterparty posted daily variation margin under a CSA?

9. A quant team has built a new pricing model for worst-of autocallables using stochastic local volatility. The model has been tested internally and shows good calibration to market data. Before the desk can use it for live trading, what governance steps must it go through?

10. A 2-for-1 stock split is announced for the underlying of a Phoenix Autocallable. The original terms are: initial spot = $200, knock-in barrier = 70% ($140), autocall barrier = 100% ($200), coupon barrier = 80% ($160). What are the adjusted terms after the split? Which system fields need to be updated?

### Scenario Questions

1. You are a new Product Control analyst. Your flash P&L shows the desk made €2M yesterday. By 2pm, the P&L Explain is complete: Delta €1.2M, Theta €0.3M, New deals €0.1M — total explained €1.6M. Unexplained is €400K (25% of total). The trader says "that's just noise, it'll wash out tomorrow." What do you do?

2. A CLN references a European bank that has just announced a voluntary restructuring of its subordinated debt — extending the maturity by 3 years and reducing the coupon by 100bps. The CDS on this reference entity is documented under No Restructuring (NR). Sales is fielding calls from nervous CLN investors. What should investors be told? What if the CDS were documented under Full Restructuring (FR)?

3. Your bank has sold a 1-year Phoenix Autocallable on a single stock. The stock has been trading at 72% of its initial level — just above the 70% knock-in barrier. A major competitor announces a tender offer for the stock, and the share price jumps to 120% of the initial level overnight. Describe the impact on: (a) the desk's hedge, (b) Operations, (c) Product Control, (d) the client.

### Desk Question

A junior structurer says: "We do not need to worry about XVA charges — they are just accounting adjustments, not real costs." Explain why this statement is wrong. In your answer, describe at least three XVA charges and explain how each represents a real economic cost to the bank.

---

## Part 6 — Mental Models Summary

| Concept | Mental Model |
|---------|-------------|
| Modified Following | The "do not cross the month" rule — move forward to the next business day, unless it pushes you into the next month, then move backward |
| Day Count Convention | The ruler that measures time — but different rulers give different answers for the same period |
| ACT/360 vs 30/360 | On a $100M notional, the wrong ruler costs you $10,000+ per coupon |
| Clean vs Dirty Price | Clean = the sticker price on the car. Dirty = the sticker price plus the fuel already in the tank |
| Termsheet | The architectural blueprint — every field specifies a precise measurement |
| ISDA Master Agreement | The building code — the termsheet says what you are building; the Master Agreement says what happens when things go wrong |
| CSA Threshold | The deductible on your insurance — you absorb the first $X of exposure before collateral kicks in |
| Close-out Netting | The "no cherry-picking" rule — upon default, all trades are settled together, not individually |
| Capital Hierarchy | The apartment building — ground floor gets out first in a fire, penthouse last |
| Recovery Waterfall | The queue at the ATM — senior creditors get paid first, equity holders get what is left |
| AT1 / CoCos | The ejection seat — designed to absorb losses before the plane crashes |
| Restructuring Clause | The insurance policy fine print — FR covers everything including fender-benders; NR only covers total write-offs |
| Fair Value Hierarchy | The house appraisal — market comps (L1), adjusted comps (L2), expert opinion (L3) |
| IPV | The second opinion — an independent doctor checking the surgeon's diagnosis |
| P&L Explain | The financial autopsy — dissecting yesterday's result into its causes |
| Unexplained P&L | The smoke detector — small amounts of smoke are normal; large amounts mean something is burning |
| Reserves | The rainy-day fund — set aside for the things the model might be wrong about |
| Bid-Offer Reserve | The exit toll — you cannot sell at mid; you sell at the bid |
| Model Reserve | The margin of error — different reasonable models give different prices |
| Day One P&L | The "too good to be true" check — did you really make money, or did your model assume you did? |
| CVA | The tab insurance — the cost of the customer potentially not paying their bill |
| FVA | The rent — the cost of funding the money you have lent out |
| KVA | The opportunity cost — the capital tied up in this trade could be earning returns elsewhere |
| FTP | The internal rent — Treasury charges the desk for using the bank's balance sheet |
| SA-CCR | The exposure meter — measures how much the bank could lose if the counterparty defaults |
| RWA | The risk-adjusted size — not all assets are equally risky; risk weights reflect this |
| RAROC | The true profitability — revenue means nothing if the capital consumed to earn it is excessive |
| Model Lifecycle | The car inspection — build it, test it, certify it, monitor it, eventually retire it |
| Backtesting | The reality check — did the model's predictions match what actually happened? |
| Challenger Model | The second opinion — a different approach to the same problem, to see if the answer changes |
| Model Inventory | The fleet register — every model in the bank is registered, rated, and tracked |
| Golden Source | The single source of truth — one authoritative system per data type, no arguments |
| Trade Break | The mismatched puzzle piece — two records that should agree but do not |
| Corporate Action | The rule change mid-game — the underlying changes, so the contract must adjust |
| Flow vs Exotic | Assembly line vs custom workshop — high volume and low margin vs low volume and high margin |
| Risk Warehouse | The shipping depot — accumulate risks, group them, and hedge in bulk rather than one at a time |
| Short Gamma | Losing in earthquakes — the desk hurts from large sudden moves in any direction |
| Short Vega | Losing in storms — the desk hurts when volatility rises across the market |
| Long Correlation | Benefiting from herding — the desk profits when assets move together |
| Suitability | The prescription — the right medicine for the right patient, not every medicine for every patient |
| SRI | The nutritional label — a standardized score so consumers can compare risks across products |
| Central Clearing | The trusted middleman — the CCP stands between buyer and seller, guaranteeing both sides |
| UMR | The bilateral safety net — collateral required even when no CCP is involved |

---
