## 6.7 Treasury, Capital & XVA

### How the Bank Prices Its Own Costs — Funding, Capital Consumption, and Valuation Adjustments

Imagine you run a restaurant. Your menu prices must cover more than just ingredients (the hedge). They must also cover rent (funding cost), insurance (capital), the health inspector's requirements (regulatory capital), and the cost of extending credit to regular customers who run tabs (CVA). Treasury, Capital, and XVA are the structured products desk's equivalent of these overhead costs. They are invisible to the customer but critical to profitability.

Part 2 taught you the product construction formula: **Coupon = Bond Yield + Option Premium - FTP - Margin.** That formula told you *that* FTP exists and *that* it reduces the coupon. This section teaches you *how* FTP works, *why* Treasury charges it, and what other invisible costs — XVA and capital consumption — sit between the desk's gross revenue and its actual profit.

---

### Treasury Function

Treasury is the department that manages the bank's money at the enterprise level. It raises funding in the capital markets, allocates funding costs to business lines, manages the bank's liquidity buffers, and controls the interest rate risk of the banking book.

Treasury is NOT the trading desk. Think of Treasury as the landlord of a building, and the structured products desk as a tenant. The desk does not negotiate the bank's borrowing costs any more than a restaurant tenant negotiates the building's mortgage. The desk pays an internal rent — the Funds Transfer Price — and Treasury manages the building.

**Key Treasury responsibilities:**

| Responsibility | What It Means |
|---------------|---------------|
| **Raise funding** | Treasury issues bonds, commercial paper, and certificates of deposit in the capital markets to raise the money the bank lends and invests |
| **Allocate funding costs** | Treasury charges each desk an internal rate (FTP) that reflects the true cost of funding that desk's activities |
| **Manage liquidity buffers** | Treasury holds high-quality liquid assets (HQLA) to meet regulatory requirements and survive stress scenarios |
| **Manage interest rate risk of the banking book** | Treasury ensures that the bank's overall interest rate exposure (from all its assets and liabilities) stays within risk appetite |

The structured products desk interacts with Treasury primarily through FTP. Every time the desk issues a structured note, it is borrowing from the bank's balance sheet — and Treasury charges for that borrowing.

---

### FTP Methodology

In Part 2 Section 2.2, you learned that FTP is a cost component in the product formula. In the Four-Leg Framework (Section 2.3), you saw the Deposit Leg — the leg where Treasury charges the desk for funding. This section explains how that charge is calculated.

**What FTP is:** FTP (Funds Transfer Price) is the internal cost charged to the trading desk for the funding embedded in a structured product. When the bank issues a 5-year structured note, it needs to fund that note for 5 years. FTP is the price Treasury charges the desk for that 5-year funding.

**The FTP curve:** Treasury does not charge a single rate. It constructs an internal funding curve — a set of rates for different tenors — based on three components:

1. **The bank's external borrowing costs.** Treasury monitors the bank's bond spreads, commercial paper rates, and other market funding costs. If the bank borrows at 5-year swap rate + 80 basis points, that spread feeds into the 5-year FTP.

2. **A term premium.** Longer-dated funding costs more than short-dated funding. A 1-year structured note costs less to fund than a 5-year note because the bank is committing its balance sheet for a shorter period.

3. **A liquidity premium.** Some positions are harder to fund than others. Illiquid collateral, hard-to-repo securities, or products with uncertain maturity profiles attract an additional liquidity charge.

**Illustrative FTP curve:**

| Tenor | FTP Rate (illustrative) | Components |
|-------|:-----------------------:|-----------|
| 1 year | 1.20% | External cost 0.60% + term premium 0.30% + liquidity 0.30% |
| 3 years | 1.80% | External cost 0.70% + term premium 0.60% + liquidity 0.50% |
| 5 years | 2.40% | External cost 0.80% + term premium 0.90% + liquidity 0.70% |
| 10 years | 3.10% | External cost 0.90% + term premium 1.20% + liquidity 1.00% |

**FTP for structured products:** The FTP charge depends on the product's maturity and its funding profile.

- A **1-year note** gets 1-year FTP. Simple.
- A **5-year note** gets 5-year FTP. Also simple.
- An **autocallable with expected life of 1.5 years** is more complex. The note has a 5-year legal maturity but is expected to autocall after 1.5 years. Treasury typically charges based on the expected life, with an adjustment for early termination optionality. If the autocall does not trigger, the desk may face a higher FTP charge as the remaining life extends.

This expected-life adjustment is one of the most debated aspects of FTP methodology. If Treasury charges 5-year FTP on a product that usually autocalls in 18 months, the product becomes uncompetitively expensive. If Treasury charges 18-month FTP and the product does not autocall, the desk has underfunded its position.

**FTP and profitability — the "hidden killer":**

Consider a 3-year ELN with a 6% coupon. The desk prices it as follows:

| Component | Amount |
|-----------|:------:|
| Bond yield (what the bank earns from investing the principal) | 3.50% |
| Option premium (from selling the embedded put) | 3.80% |
| Total revenue | 7.30% |
| Coupon paid to investor | -6.00% |
| FTP charge from Treasury | -1.80% |
| **Desk margin** | **-0.50%** |

The product looks profitable before FTP: 7.30% revenue minus 6.00% coupon = 1.30% margin. But after the 1.80% FTP charge, the desk is *losing* 50 basis points per year. The product destroys value.

This is why FTP is called the "hidden killer" of structured product margins. A structurer who ignores FTP will design products that appear profitable but actually cost the bank money.

---

### Liquidity Regulation

Treasury does not operate in a vacuum. Regulators require the bank to hold enough liquid assets to survive a crisis. These requirements directly affect the cost of structured products.

**LCR (Liquidity Coverage Ratio)**

The LCR requires the bank to hold enough high-quality liquid assets (HQLA) to cover 30 days of net cash outflows under a stress scenario. The formula is simple in concept:

LCR = HQLA / Net Cash Outflows over 30 days >= 100%

Structured products that create potential outflow obligations consume LCR. For example, if the bank has sold a structured note that could require a large cash payout upon autocall within the next 30 days, that potential outflow reduces the LCR ratio. Treasury must hold additional HQLA to compensate — and it charges the desk for this.

**NSFR (Net Stable Funding Ratio)**

The NSFR takes a longer view. The bank's available stable funding (equity, long-term debt, stable deposits) must exceed its required stable funding over a 1-year horizon.

NSFR = Available Stable Funding / Required Stable Funding >= 100%

Long-dated structured products require stable funding. A 10-year CLN requires the bank to commit funding for a decade — this requires stable funding sources, which are more expensive than short-term borrowing.

**HQLA (High-Quality Liquid Assets)**

HQLA is the buffer Treasury holds to meet the LCR. It consists of:

| Category | Examples | Haircut |
|----------|----------|:-------:|
| Level 1 | Cash, central bank reserves, government bonds | 0% |
| Level 2A | Certain corporate bonds (AA- or better), covered bonds | 15% |
| Level 2B | Certain corporate bonds (A+ to BBB-), equities in major indices | 25-50% |

The bank must hold HQLA that earns a low return. The opportunity cost of holding low-yielding government bonds instead of higher-yielding assets is a real cost that flows through to desks via FTP.

**Why it matters for structured products:** Every structured product creates a funding obligation. The desk must factor in the liquidity cost — a product that creates large potential outflows (e.g., a callable note with short call dates) costs more in LCR terms than a product with predictable, scheduled cash flows.

---

### ALM (Asset-Liability Management)

ALM is the discipline of matching the maturity and interest rate profile of the bank's assets (what the bank owns or is owed) with its liabilities (what the bank owes).

When the bank issues a 5-year structured note, it creates a 5-year liability — it owes the investor their coupon payments and principal at maturity. If the bank hedges that note with a 3-month rolling derivative position, there is a **maturity mismatch**: the liability is long-dated but the asset (the hedge) is short-dated. If interest rates change significantly, the cost of rolling the hedge may exceed what was assumed in the original pricing.

Treasury manages ALM at the enterprise level — aggregating all the bank's assets and liabilities to identify mismatches. The structured products desk manages its own hedge tenor: matching the hedge maturity to the product maturity where possible, or accepting and pricing the mismatch where it is not.

In practice, ALM risk for the structured products desk is most acute for products with uncertain maturities — autocallables, callable notes, and products with optional early termination. The desk books a hedge for the expected life, but if the product does not terminate as expected, the hedge must be extended at whatever market rates prevail at that time.

---

### XVA Framework

XVA stands for a family of Valuation Adjustments — corrections to the model price of a derivative that reflect real-world costs the model does not capture. If you think of the model price as the "theoretical" value of a trade in a frictionless world, XVAs are the adjustments that bring the price back to reality.

Each XVA addresses a different cost:

---

**CVA (Credit Valuation Adjustment)**

CVA is the cost of counterparty credit risk — the expected loss from the counterparty defaulting on their derivative obligations.

When the bank enters a derivative trade with a counterparty, there is a risk that the counterparty will default before the trade matures. If the trade has positive value to the bank at the time of default (the counterparty owes the bank money), the bank suffers a loss.

The concept is straightforward:

**CVA approximately equals Probability of Default x Loss Given Default x Expected Positive Exposure**

- **Probability of Default (PD):** How likely is the counterparty to default? This is inferred from CDS spreads or internal credit ratings.
- **Loss Given Default (LGD):** If the counterparty defaults, how much does the bank lose? Typically 60-70% (recovery rates of 30-40%).
- **Expected Positive Exposure (EPE):** Over the life of the trade, how much is the counterparty expected to owe the bank on average?

CVA is charged to the trade. A trade with a BBB-rated counterparty has a higher CVA charge than the same trade with a AA-rated counterparty. The desk must earn enough margin to cover this charge.

Many banks have a dedicated **CVA desk** that manages counterparty credit risk centrally. The CVA desk aggregates all the bank's derivative exposures, hedges the credit risk using CDS, and charges each trading desk a CVA for each new trade.

---

**DVA (Debit Valuation Adjustment)**

DVA is the symmetric counterpart to CVA. It represents the bank's own credit risk from the counterparty's perspective.

Here is the counterintuitive part: DVA means the bank *benefits* when its own creditworthiness deteriorates. Why? Because if the bank is more likely to default, its obligations to counterparties become less valuable — from an accounting perspective, the bank's liabilities decrease.

This creates an uncomfortable situation: a bank that is approaching distress would report a DVA gain in its earnings. The bank's credit spreads widen, its obligations become less certain, and accounting rules require it to recognize a profit.

**Accounting treatment:** IFRS 13 requires banks to recognize DVA in fair value measurements. However, Basel III partially excludes DVA gains from regulatory capital, acknowledging that a bank cannot practically monetize a gain that only arises from its own deterioration.

DVA is conceptually important but operationally less central than CVA. Most desk-level discussions focus on CVA, not DVA.

---

**FVA (Funding Valuation Adjustment)**

FVA captures the cost or benefit of funding uncollateralized derivative exposures.

When a derivative trade is fully collateralized — covered by a Credit Support Annex (CSA) with zero threshold and daily margin calls — the bank does not need to fund its exposure from its own balance sheet. The collateral covers the mark-to-market. In this case, FVA is approximately zero.

But when a trade is uncollateralized (no CSA, or a CSA with a high threshold), the bank must fund any positive mark-to-market from its own balance sheet. This funding has a cost — the bank must borrow to finance the exposure.

**When FVA matters:**
- Trades with corporate clients who do not post collateral: **high FVA**
- Trades with institutional counterparties under full CSA: **low FVA**
- Trades with sovereigns or supranationals (typically uncollateralized): **high FVA**

**The FVA debate:** Academics have argued that FVA is double-counting — that the funding cost is already reflected in the discount rate used to value the derivative. Practitioners counter that FVA is a real cost that the desk incurs: if the desk must borrow money from Treasury (at FTP rates) to fund an uncollateralized exposure, that cost is real regardless of what the discount rate says. In practice, most banks charge FVA and consider it a real cost of doing business.

---

**ColVA (Collateral Valuation Adjustment)**

ColVA captures the cost or benefit of posting specific types of collateral under a CSA.

If the CSA specifies that collateral must be posted in EUR cash, but the bank's natural funding currency is USD, the bank incurs a cost to convert or source EUR cash. Similarly, if the CSA allows government bonds as collateral but the bank holds mostly corporate bonds, there is an opportunity cost in purchasing or sourcing the required collateral.

ColVA is typically small relative to CVA and FVA, but it can be material for trades with restrictive CSA terms — particularly cross-currency CSAs where the bank must hold collateral in a currency it does not naturally fund in.

---

**MVA (Margin Valuation Adjustment)**

MVA captures the cost of posting initial margin over the life of a trade.

Initial margin (IM) is a buffer that protects against losses during the close-out period if a counterparty defaults. It must be posted as cash or high-quality securities. Unlike variation margin (which reflects mark-to-market and is exchanged daily), initial margin is held in segregated accounts and cannot be reused. The bank must fund this margin for the life of the trade.

MVA is the present value of the expected funding cost of initial margin over the trade's life.

**When MVA matters:**
- **Cleared trades:** The CCP determines IM using its own models (e.g., SPAN, PRISMA). IM can be substantial for complex or long-dated trades.
- **Bilateral trades subject to UMR (Uncleared Margin Rules):** Counterparties above the threshold must exchange IM on uncleared derivatives. The IM is calculated using ISDA SIMM or a regulatory schedule.

For long-dated structured products with large notionals, MVA can be a meaningful cost — particularly when the bank's cost of funding significantly exceeds the return earned on the posted collateral.

---

**KVA (Capital Valuation Adjustment)**

KVA captures the cost of holding regulatory capital against a trade over its lifetime.

Regulatory capital is expensive. The bank's equity capital has a high required return — typically 10-15% (the bank's cost of equity). When a trade consumes regulatory capital, the bank must hold equity against that trade for its entire life. KVA is the present value of the expected cost of that capital over the trade's life.

**How KVA affects pricing:** A trade that consumes significant capital must earn enough to justify that capital consumption. If the KVA charge exceeds the desk's margin on the trade, the trade destroys shareholder value — even if it is profitable before capital costs.

KVA is increasingly factored into trade pricing, especially for capital-intensive products like CLNs, CDOs, and long-dated cross-currency swaps. Banks that ignore KVA in pricing will accumulate trades that appear profitable but do not earn their cost of capital.

---

### XVA Impact on Structured Products — Worked Example

To make these concepts concrete, consider a simplified pricing for a **5-year CLN on a BBB-rated reference entity**, sold to an uncollateralized corporate counterparty.

| Component | Amount | Explanation |
|-----------|:------:|-------------|
| Model price (mid) | $100.00 | Fair value assuming frictionless markets |
| CVA charge | -$0.80 | Counterparty default risk over 5 years |
| FVA charge | -$0.30 | Funding cost of uncollateralized exposure |
| KVA charge | -$0.50 | Capital consumption over 5 years (CLNs are capital-intensive) |
| MVA charge | -$0.10 | Initial margin funding cost |
| **Total XVA** | **-$1.70** | |
| **Fair value (post-XVA)** | **$98.30** | |

Without XVA adjustments, the desk would sell this CLN at $100 — giving the investor $1.70 of value that the bank is not being compensated for. The desk would appear profitable in the model but would be losing money in reality, because the model ignores funding costs, capital costs, and counterparty credit risk.

> **Professor Note:** XVA is the bridge between the theoretical world of models and the real world of bank economics. A desk that prices without XVA is like a restaurant that sets menu prices based on ingredient costs alone — ignoring rent, insurance, and staff. They will be busy (because prices are too low) but unprofitable.

---

### Capital Framework

Regulatory capital is the equity buffer that banks must hold to absorb losses. The more risk a bank takes, the more capital it must hold. Since capital is expensive, products that consume more capital must earn higher returns to justify their existence.

---

**RWA (Risk-Weighted Assets)**

RWA is the bank's total assets adjusted for risk. Riskier assets receive higher weights, requiring more capital.

| Asset Type | Risk Weight | Capital Required (at 10%) |
|-----------|:----------:|:-------------------------:|
| Cash and government bonds | 0% | $0 per $100 |
| AAA-rated corporate bonds | 20% | $2 per $100 |
| A-rated corporate loans | 50% | $5 per $100 |
| Unrated corporate exposures | 100% | $10 per $100 |
| Sub-investment grade loans | 150% | $15 per $100 |
| Derivatives | Calculated via SA-CCR | Varies — often material |

The bank must hold capital equal to a percentage of total RWA — typically 8% minimum under Basel III, with additional buffers pushing the effective requirement to 10-13%. Products that generate high RWA consume expensive capital and must earn proportionally higher returns.

---

**SA-CCR (Standardised Approach for Counterparty Credit Risk)**

SA-CCR is the Basel III method for calculating the exposure amount of derivative trades. It replaced the older Current Exposure Method (CEM) and Standardised Method (SM).

SA-CCR calculates exposure as:

**EAD = alpha x (Replacement Cost + PFE)**

Where:
- **alpha** = 1.4 (a regulatory scaling factor)
- **Replacement Cost (RC)** = the current exposure — what the bank would lose if the counterparty defaulted today
- **Potential Future Exposure (PFE)** = the estimated maximum increase in exposure over the margin period of risk

PFE depends on the derivative type, notional, remaining maturity, and netting and collateral arrangements. Complex derivatives with long maturities and large notionals generate high PFE, which generates high EAD, which generates high RWA, which generates high capital consumption.

**Why SA-CCR matters for structured products:** A 10-year interest rate swap on $100M notional generates far more SA-CCR exposure than a 1-year equity option on $10M notional. The capital cost of the swap is correspondingly higher, and the desk must price this capital cost into the product.

---

**EAD (Exposure at Default)**

EAD is the estimated exposure to a counterparty at the time of default. Under SA-CCR, it is calculated as:

**EAD = 1.4 x (Replacement Cost + PFE)**

EAD is used in two key processes:
1. **Capital calculation:** EAD feeds into the RWA calculation, which determines how much capital the bank must hold.
2. **Credit limit management:** The bank sets limits on how much exposure it will take to any single counterparty. EAD is the measure used to track exposure against those limits.

---

**PFE (Potential Future Exposure)**

PFE is the maximum expected exposure over a future time horizon at a given confidence level — typically 97.5%. It answers the question: "If markets move against us, how bad could our exposure get?"

PFE is used for:
- **Credit limit monitoring:** Ensuring that the bank's total exposure to a counterparty (including potential future increases) stays within approved limits.
- **Capital calculation:** PFE is a component of SA-CCR exposure.

For structured products, PFE can be particularly high for long-dated derivatives with path-dependent features — autocallable notes, for example, have uncertain lives and payoff profiles that make PFE estimation complex.

---

**RAROC (Risk-Adjusted Return on Capital)**

RAROC is the metric that answers the question every bank manager asks: "Is this trade worth the capital it consumes?"

**RAROC = (Revenue - Costs - Expected Loss) / Capital Consumed**

Consider two trades:

| | Trade A | Trade B |
|-|:-------:|:-------:|
| Annual revenue | $1,000,000 | $500,000 |
| Annual costs | $200,000 | $100,000 |
| Expected loss | $100,000 | $50,000 |
| Net income | $700,000 | $350,000 |
| Capital consumed | $50,000,000 | $5,000,000 |
| **RAROC** | **1.4%** | **7.0%** |

Trade A earns twice as much revenue, but it consumes ten times as much capital. Its RAROC of 1.4% is below the bank's typical hurdle rate of 10-12%. Trade B earns less revenue but is far more capital-efficient.

**How RAROC affects structuring:** Desks increasingly optimize products for RAROC, not just margin. A structurer might redesign a product to reduce its capital consumption — for example, by adding collateral provisions, shortening the maturity, or reducing the notional — even if these changes slightly reduce the margin, because the RAROC improvement makes the trade more valuable to shareholders.

---

### Capital Optimization

Smart desks do not accept high capital consumption as a given. They actively manage it.

**Netting:** Trades under the same ISDA netting agreement offset each other. If the bank has a $10M positive exposure and a $7M negative exposure to the same counterparty under the same netting agreement, the net exposure is $3M — not $10M. This dramatically reduces capital requirements. Desks actively seek to build balanced portfolios with counterparties to benefit from netting.

**Collateral:** CSA collateral reduces exposure. If a counterparty posts $5M of collateral against a $5M exposure, the bank's net exposure — and capital consumption — is zero. Negotiating strong CSA terms (low thresholds, frequent margin calls, broad eligible collateral) is a capital optimization strategy.

**Central clearing:** Cleared trades attract lower capital charges than bilateral trades because the CCP interposes itself as the counterparty to both sides, reducing counterparty credit risk. Desks consider clearing eligibility when designing products.

**Trade compression:** Over time, a desk accumulates many trades with the same counterparty that partially offset each other. Trade compression eliminates redundant trades, reducing gross notional and capital consumption without changing the net risk. Compression cycles are typically run quarterly with the help of services like TriOptima or Quantile.

---

### Common Mistakes

1. **Ignoring FTP when designing products.** A product that looks attractive before FTP may destroy value after FTP. Always price with the full FTP curve. A structurer who quotes a 7% coupon to sales without checking the FTP charge is guessing, not pricing.

2. **Treating XVA as a rounding error.** On a single trade, XVA may be small relative to the notional. But across a portfolio of thousands of trades, XVA charges are a major cost. A desk that systematically undercharges XVA will accumulate hidden losses.

3. **Confusing CVA with credit risk on the reference entity.** CVA is the cost of *counterparty* default risk — the risk that the party you are trading with defaults. This is different from the credit risk of the reference entity in a CLN (which is the risk you are deliberately taking). A CLN on a BBB corporate sold to a BBB counterparty has credit risk in both directions.

4. **Assuming capital is free.** Capital has a cost — the bank's cost of equity. A trade that earns $500K but consumes $10M of capital earns a 5% return on capital. If the bank's cost of equity is 12%, the trade is destroying shareholder value despite being nominally profitable.

5. **Optimizing for revenue instead of RAROC.** The largest trades are not necessarily the best trades. A $200M trade that earns $2M margin but consumes $100M of capital (RAROC = 2%) is worse for the bank than a $20M trade that earns $500K margin but consumes $3M of capital (RAROC = 17%).

6. **Not understanding the FTP expected-life problem for autocallables.** An autocallable with a 5-year legal maturity but 1.5-year expected life creates a tension: should FTP be based on 5 years or 1.5 years? The answer affects the coupon by potentially 100+ basis points. Structurers must understand how Treasury resolves this for their bank.

> **Professor Note:** If you remember only one thing from this section, remember this: the model gives you the theoretical price. FTP tells you what it costs to fund. XVA tells you what it costs to bear real-world frictions. Capital tells you what it costs to hold the risk. A trade is only profitable if revenue exceeds all four costs — not just the hedge.

---

## 6.8 Model Risk Management

### How We Govern the Models — Validation, Limitations, and the Discipline of Knowing What We Do Not Know

Models are like maps. A good map helps you navigate confidently. But every map has limitations: it may be outdated, it may not show elevation, it may distort distances at the edges. Model Risk Management is the discipline of knowing where the map is accurate, where it is approximate, and where it is dangerously wrong.

Part 1 Section 1.9 introduced model risk as "the risk that your math is wrong." This section expands on that introduction. Model risk has two sources. The first is that the model is *inherently* wrong — it makes assumptions that do not reflect reality. The second is that the model is *used* incorrectly — correct model, wrong inputs, wrong application. Both sources can produce large losses.

---

### The Regulatory Foundation

Model risk is not just an internal concern. Regulators have formalized expectations for how banks govern their models.

**SR 11-7** (United States, Federal Reserve/OCC): "Guidance on Model Risk Management." This document establishes that banks must have a formal framework for identifying, measuring, and controlling model risk. It requires independent validation, ongoing monitoring, and clear documentation of model limitations.

**SS1/23** (United Kingdom, PRA): The PRA's supervisory statement on model risk management. It requires banks to maintain a model inventory, assign risk ratings, and ensure that model risk is integrated into the bank's overall risk management framework.

Both standards share a common philosophy: *a model is useful, but a model you do not understand is dangerous.*

---

### The Model Lifecycle

Models are not built once and forgotten. They follow a lifecycle — and every stage has governance requirements.

**1. Development**

The Quant team builds the model. They choose the mathematical methodology (Black-Scholes? Local Vol? Stochastic Vol?), define the calibration approach (which market data does the model fit to?), and test the model against known benchmarks.

Development is where the critical design decisions are made: which simplifications are acceptable? Which market features does the model capture, and which does it ignore? A model that captures every feature of reality would be too slow to use in practice. A model that ignores too many features will produce prices that diverge from market reality. The art of quant development is finding the right balance.

**2. Documentation**

Every model must be documented before it can be validated. The model documentation typically includes:

| Section | Contents |
|---------|----------|
| **Purpose** | What the model prices and why it was built |
| **Methodology** | The mathematical framework — equations, derivations, assumptions |
| **Assumptions** | Every simplification the model makes (constant rates? continuous hedging? no jumps?) |
| **Calibration** | How the model is fitted to market data — which data, which method, how often |
| **Testing** | Results of accuracy tests, convergence tests, and boundary condition tests |
| **Limitations** | Explicit statements about what the model cannot do or where it may be unreliable |
| **Usage guidelines** | Which products the model can price, and any restrictions on parameter ranges |

The documentation is not an afterthought. It is the contract between the model developers and the model users. If a limitation is not documented, users cannot be expected to know about it.

**3. Validation**

Independent review by the Model Validation team — a team that did NOT build the model. Validation is covered in detail below.

**4. Approval**

The Model Risk Management (MRM) committee reviews the validation report and decides:
- **Approve:** The model is fit for purpose. It may be used in production.
- **Conditional approval:** The model may be used, but with restrictions (e.g., "not for barriers below 50%" or "with a model reserve of X").
- **Reject:** The model is not fit for purpose. It must be reworked before resubmission.

**5. Implementation**

The approved model is coded into the bank's pricing systems — Sophis for ELN/CLN products, Murex for SRT/STEG products (as described in Part 2 Section 2.8). Implementation is itself a source of model risk: the code may not perfectly match the mathematics. This is why implementation testing is a validation requirement.

**6. Monitoring**

Once live, the model is monitored for ongoing performance. Does it still calibrate well to current market data? Are the P&L predictions consistent with realized P&L? Has the market changed in ways that violate the model's assumptions?

Monitoring is continuous. The model does not stop being risky just because it was validated once.

**7. Material Change**

If the model is significantly changed — a new calibration method, a new payoff type, a different numerical scheme — it must be re-validated. Not every change triggers re-validation: minor parameter updates (recalibrating to today's vol surface) are routine. But structural changes (switching from Local Vol to Stochastic Vol) require a full validation cycle.

**8. Retirement**

When a model is replaced by a newer version or is no longer needed (because the products it priced have all matured), it is decommissioned. Retirement must be documented: which model replaced it, why, and what legacy positions (if any) remain on the old model.

---

### Model Validation

Model validation is the independent assessment of whether a model is fit for purpose. It is performed by the **Model Validation team** — a team that is organizationally separate from both the Quant team (who built the model) and the Trading desk (who use the model). Independence is critical: if the builders validate their own work, they have a natural incentive to overlook weaknesses.

**What validators check:**

| Check | What It Means |
|-------|---------------|
| **Mathematical correctness** | Are the equations right? Is the derivation free of errors? Does the model solve the correct problem? |
| **Conceptual soundness** | Are the assumptions appropriate for the product being priced? Is a Gaussian copula suitable for a CDO? Is Black-Scholes suitable for a barrier option? |
| **Implementation testing** | Does the code match the math? Validators run independent implementations and compare results |
| **Calibration quality** | Does the model fit market data well? Are there systematic biases? Does the calibration produce stable parameters? |
| **Stability** | Do small input changes cause large output changes? An unstable model produces unreliable prices |
| **Boundary behavior** | Does the model behave correctly at extreme values? What happens when vol is very high, or when the spot is near the barrier, or when the maturity is very short? |
| **Benchmarking** | How does the model compare to alternative approaches? If the primary model says $100 and the benchmark says $97, what explains the difference? |

Validation is not a pass/fail test. The validator's goal is to *quantify* the model's strengths and weaknesses, not to declare it perfect. Every model has limitations. The question is whether those limitations are understood, documented, and appropriately managed.

---

### Challenger Models

A challenger model is an alternative model used to benchmark the primary (production) model. It serves as a reality check.

For example, if the desk prices worst-of autocallables using a **Local Volatility + Monte Carlo** model, the challenger might use a **Stochastic Volatility + Monte Carlo** model. Both models should produce similar prices for vanilla products (where the choice of model matters less) but may diverge for complex products (where model assumptions become more important).

The difference between the primary model price and the challenger model price is a measure of **model uncertainty**. This difference often drives the **Model Reserve** — a reserve that Product Control holds against positions where model risk is material (as discussed in Section 6.6).

| Primary Model | Challenger Model | Typical Products |
|--------------|-----------------|-----------------|
| Local Vol + Monte Carlo | Stochastic Vol + Monte Carlo | Worst-of autocallables, barrier products |
| Black-Scholes (analytic) | Local Vol + Monte Carlo | Vanilla ELNs, single-stock options |
| Hull-White 1-factor | Hull-White 2-factor or SABR | CMS swaps, SRT products |
| Gaussian Copula | Student-t Copula or Stochastic Correlation | CDOs, FTDs |

The challenger model does not need to be "better" than the primary model. It needs to be *different enough* to reveal where the primary model's assumptions matter most.

---

### Backtesting

Backtesting compares model predictions against realized outcomes. It is the most direct test of whether a model works.

**P&L backtesting:** Each day, the model predicts how the P&L should change based on the Greeks and observed market moves. The predicted P&L (from Greeks) is compared to the actual P&L (from re-marking the portfolio). Persistent differences — actual P&L consistently higher or lower than predicted — indicate a model problem.

**Pricing backtesting:** At trade inception, the model produces a price. Over time, the trade can be compared to subsequent market prices (if observable) or to the prices the product trades at in the secondary market. Systematic pricing bias (the model consistently overprices or underprices) indicates a calibration issue.

**Traffic light approach:**

| Zone | Meaning | Action |
|------|---------|--------|
| **Green** | Model performs within statistical expectations. Exceptions are within the expected frequency (e.g., fewer than 5 exceptions in 250 trading days at 99% confidence) | Normal monitoring continues |
| **Yellow** | Borderline performance. Exceptions are higher than expected but not dramatically so | Enhanced monitoring. Root cause investigation. Model may need recalibration |
| **Red** | Model performance is unacceptable. Exceptions significantly exceed expectations | Immediate remediation. Model may be suspended. Positions may be marked with an additional reserve |

---

### Sensitivity Testing

Sensitivity testing answers the question: "Which inputs matter most, and where is the model fragile?"

**Bump-and-reprice:** Shift one input at a time (spot price up 1%, vol up 1 point, rate up 25 basis points) and observe how the output changes. This is the standard method for computing Greeks, but it is also a model diagnostic tool. If the model produces Greeks that are extremely sensitive to the bump size, the model may be numerically unstable.

**Stress testing:** Apply extreme scenarios — a market crash (spot down 30%, vol up 20 points), a correlation breakdown (correlation drops from 0.7 to 0.2), a credit event (recovery rate at 10% instead of 40%). Stress tests reveal where the model behaves differently from market reality under extreme conditions.

What you learn from sensitivity testing is where the model is robust and where it is fragile. A model that produces stable, well-behaved prices across a wide range of inputs is more trustworthy than a model that produces erratic results near barriers, at extreme vols, or for very long maturities.

---

### Model Inventory

The model inventory is a central register of every model used in the bank. Regulators expect the bank to know exactly which models it uses, who owns them, and whether they are validated.

**Required information per model:**

| Field | Example |
|-------|---------|
| Model name | "EQ-LV-MC-01: Equity Local Vol Monte Carlo" |
| Purpose | Pricing and risk for single-stock and worst-of autocallable ELNs |
| Owner | Equity Quant desk |
| Validator | Model Validation team, Lead: J. Smith |
| Approval date | 2024-03-15 |
| Next review date | 2025-03-15 (annual cycle) |
| Risk rating | High (material notional, complex payoffs, significant model assumptions) |
| Known limitations | "Does not capture stochastic vol dynamics. Not suitable for products with barriers below 50%." |

**Model risk rating** is typically High / Medium / Low, based on:
- **Materiality:** How much notional is priced by this model? A $10B portfolio model is High; a $50M portfolio model may be Low.
- **Complexity:** How many simplifying assumptions does the model make? A Black-Scholes model has fewer model risk concerns than a multi-factor stochastic model with correlation.
- **Data quality:** How reliable are the inputs? Models calibrated to liquid, exchange-traded options have lower data risk than models calibrated to illiquid OTC quotes.

---

### Model Limitations

Every model has limitations. The question is whether the desk *knows* and *documents* them.

**Common limitations for structured product models:**

| Model | Limitation | Practical Impact |
|-------|-----------|-----------------|
| Black-Scholes | Assumes constant volatility | Misprices products with barrier features, which are sensitive to the vol surface |
| Gaussian copula | Assumes normal (Gaussian) dependence between defaults | Underestimates tail dependence — correlation in extreme scenarios. This was a contributing factor to CDO losses in 2008 |
| Local Volatility | Assumes a deterministic volatility surface | The vol surface moves stochastically in reality. This creates hedging error, especially for products with forward-starting features |
| All continuous-time models | Assume continuous hedging | Hedging is discrete in reality — the desk rebalances once or twice a day, not continuously. Transaction costs and market gaps create hedging slippage |

Limitations must be documented and communicated to users — traders, risk managers, and Product Control. A limitation that exists only in the quant's head is not a managed risk.

**Usage restrictions** are the operational consequence of limitations. If validation determines that the Local Vol model is unreliable for barriers below 50%, the model approval may include a restriction: "This model may not be used for products with barriers below 50% of spot." Trades that violate usage restrictions must use an alternative model or receive a model reserve.

---

### Expert Judgment and Model Override

Sometimes the model gives a price that the desk believes is wrong. Perhaps the model does not capture a known market effect, or the market is dislocated and model assumptions are temporarily invalid.

In these situations, the desk may apply an **expert judgment override** — adjusting the model price based on market knowledge.

**When overrides are used:**
- The model does not capture a specific market feature (e.g., a dividend cut that the model does not yet reflect)
- The model is being applied outside its validated range (e.g., pricing a 15-year product with a model validated only to 10 years)
- The market is dislocated (e.g., during a crisis, when model calibration breaks down)

**Governance requirements:** Any override must be:
1. **Documented** — what was the model price, what is the adjusted price, and what is the rationale?
2. **Justified** — the explanation must be specific and substantive, not "the trader thinks the model is wrong"
3. **Approved** — a senior person (Head of Trading or Head of Quants) must sign off
4. **Reviewed by MRM** — the Model Risk Management team reviews overrides periodically to ensure they are not being abused
5. **Time-limited** — overrides should not persist indefinitely. If the model needs a permanent adjustment, the model should be changed

**The danger of ungoverned overrides:** Without governance, overrides become a mechanism for traders to manipulate marks. A trader who disagrees with the model price could simply "override" it to a more favorable level, masking losses. This is why override governance is taken seriously by regulators and auditors.

---

### Model Risk for Structured Products

Different product families have different model risk profiles. The table below summarizes the key model risks for each family covered in Part 5.

| Product Family | Key Model Risks | Most Sensitive Parameter |
|---------------|----------------|------------------------|
| **ELN (vanilla)** | Vol surface calibration, barrier proximity effects, dividend assumptions | Implied volatility near the barrier |
| **ELN (worst-of)** | Correlation modeling, copula choice, joint distribution assumptions | Correlation between underlyings |
| **Swaps** | Curve extrapolation beyond liquid points, convexity adjustments, basis risk between indices | Long-end rate assumptions |
| **SRT** | Rate model choice (Hull-White vs SABR), CMS convexity adjustment, rate distribution | CMS convexity correction |
| **STEG** | Correlation between rate tenors (2-year vs 10-year), curve dynamics under stress | Rate-rate correlation |
| **CLN** | Credit spread dynamics, jump-to-default modeling, recovery rate assumptions | Recovery rate at default |
| **CDO / FTD** | Correlation modeling (Gaussian copula limitations), base correlation methodology, tail dependence | Default correlation |

The pattern is clear: the more complex the product, the more assumptions the model makes, and the higher the model risk. A vanilla ELN on a single stock has relatively low model risk — the vol surface is liquid, the payoff is simple, and Black-Scholes (with adjustments) is well understood. A CDO tranche has high model risk — correlation is not directly observable, the copula choice is debatable, and small changes in assumptions can produce large price differences.

---

### Common Mistakes

1. **Trusting the model output without understanding the assumptions.** A model price is only as good as the assumptions behind it. A trader who quotes a price without knowing which model produced it, and what that model assumes, is quoting a number they do not understand.

2. **Assuming validation means the model is correct.** Validation means the model has been independently reviewed and found fit for purpose *within its limitations*. It does not mean the model is perfect. The validation report documents what the model cannot do — read it.

3. **Not updating challenger model comparisons.** Challenger model benchmarks are most useful when run regularly. A challenger comparison from two years ago may not reflect current market conditions or the current portfolio composition.

4. **Applying a model outside its validated range without an override.** If the model is validated for maturities up to 10 years but the desk uses it for a 15-year product, the prices may be unreliable. This requires a formal override with appropriate reserves.

5. **Treating model risk as a quant problem.** Model risk belongs to everyone who uses the model. Traders are responsible for understanding the limitations of the models they rely on. Product Control is responsible for ensuring that model reserves reflect actual model uncertainty. Risk managers are responsible for stress-testing model assumptions. Model risk is not delegated to the quant team and forgotten.

> **Professor Note:** If you remember only one thing from this section, remember this: the map is not the territory. Every model simplifies reality to make it tractable. The discipline of model risk management is not to eliminate simplification — that would make models unusable — but to *know* where the simplifications matter and to *reserve* against the uncertainty they create.

---

## 6.9 Operations

### How Trades Flow Through the System — Booking, Settlement, Reconciliation, and the Discipline of Getting It Right

Operations is the logistics network of a structured products desk. If the front office is the factory that designs and builds products, Operations is the shipping, warehousing, and delivery system that ensures every product reaches its destination correctly and on time. A brilliant product that is booked incorrectly, settled late, or reconciled wrong is a failed delivery — regardless of how elegant the design.

Part 2 Section 2.6 introduced the trade lifecycle from the perspective of front, middle, and back office. Each product chapter in Part 5 includes Section 16 (Booking and Systems), which describes how that specific product is booked. This section goes deeper into the operational machinery that applies across all products: the detailed workflow from trade capture to maturity, the systems of checks and reconciliation that prevent errors, and the lifecycle events that require operational attention.

---

### Trade Lifecycle — The Operational View

The operational trade lifecycle has eight stages. Each stage has its own procedures, checks, and failure modes.

**1. Trade Capture**

The structurer finalizes the product terms with the client. Once terms are agreed, the trade is entered into the booking system — NEMO for ELN and CLN products, Murex for SRT, STEG, and Swaps (as established in Part 2 Section 2.8).

The person entering the trade fills in a trade capture form with the key economic terms: notional, underlying, strike, barrier levels, maturity date, coupon schedule, counterparty, settlement currency, and observation conventions. The system validates these fields against business rules before accepting the trade.

**2. Trade Enrichment**

Once the core economic terms are entered, the system automatically populates secondary fields that derive from the primary inputs:

| Enriched Field | How It Is Determined |
|---------------|---------------------|
| Settlement dates | Calculated from trade date + settlement lag, adjusted for business day conventions and the applicable settlement calendar |
| Counterparty SSI | Pulled from the static data repository based on the counterparty ID and settlement currency |
| Day count convention | Populated based on the product template (e.g., ACT/360 for money market products, 30/360 for bond-like products) |
| Holiday calendar | Determined by the settlement location, exchange location, and currency of the trade |
| Coupon observation dates | Generated from the coupon schedule template, adjusted for holidays and business day conventions |

Enrichment errors are subtle and dangerous. If the system populates the wrong holiday calendar, every coupon date in the product's life may be shifted by a day — causing discrepancies with the counterparty and potentially triggering settlement fails.

**3. Trade Validation (Four-Eyes Check)**

No trade is booked without independent verification. A second person — typically an operations analyst or a senior operations officer — reviews the booking against the termsheet or trade confirmation.

The validator checks:
- Do the key economic terms (notional, strike, barrier, maturity, coupon) match the termsheet?
- Are the observation dates correct?
- Is the counterparty correctly identified?
- Are the settlement instructions correct?
- Does the booking use the correct product template?

If discrepancies are found, the trade is rejected back to the originator for correction before it enters the book of record.

**4. Confirmation**

After the trade is booked and validated, a confirmation is generated and sent to the counterparty. The confirmation is the legal record of the trade — it specifies all economic terms, observation conventions, calculation agent provisions, and fallback procedures.

The counterparty reviews the confirmation and either confirms (agrees to the terms as stated) or disputes (identifies discrepancies). Disputed confirmations must be resolved before settlement.

Unconfirmed trades are a risk: if the parties disagree on terms and the disagreement is not discovered until a payment is due, the resolution can be costly and contentious.

**5. Settlement**

On the settlement date, cash and/or securities are exchanged according to the standing settlement instructions (SSI).

For a new structured note issue: the investor sends the principal to the bank. For coupon payments: the bank sends the coupon amount to the investor. For maturity: the final payoff is calculated and settled — either as a cash amount or as physical delivery of securities.

Settlement follows the **DvP (Delivery versus Payment)** principle where applicable: securities and cash are exchanged simultaneously to eliminate the risk that one party delivers without receiving payment.

**6. Daily Maintenance**

Once a trade is live, it requires daily operational attention:

- **Fixings:** On observation dates, the underlying price is recorded. For equity-linked products, this is typically the official closing price from the relevant exchange.
- **Coupon observation:** For conditional coupons, the underlying level is compared against the coupon barrier. If the condition is met, a coupon payment is scheduled.
- **Barrier monitoring:** For products with American (continuous) barriers, the underlying price is monitored against the barrier level throughout each trading day. For European (discrete) barriers, monitoring occurs only on specified observation dates.

**7. Lifecycle Events**

Lifecycle events are the milestones that change the trade's status or trigger cash flows:

| Event | What Happens | Operational Action |
|-------|-------------|-------------------|
| Autocall trigger | Underlying is above autocall level on observation date | Calculate early redemption amount. Schedule settlement. Notify counterparty. Close the trade. |
| Barrier breach | Underlying crosses the knock-in barrier | Update barrier status in the system. Adjust hedge booking if needed. No cash flow — but the trade's payoff profile changes. |
| Coupon payment | Coupon condition met on observation date | Calculate coupon amount. Generate payment instruction. Send payment. |
| Credit event (CLN) | Reference entity experiences a credit event | Determine event type. Calculate recovery. Process credit event settlement per ISDA terms. |
| Corporate action | Stock split, merger, dividend, etc. | Apply adjustment to strike, barrier, notional per the product's terms. Update the system. Notify counterparty. |

**8. Maturity / Termination**

At maturity, the final payoff is calculated based on the product's terms and the final fixing. The final settlement is processed, the trade is marked as matured in the booking system, and it is archived.

For products that terminate early (autocall, credit event, issuer call), the same process applies at the termination date rather than the legal maturity date.

---

### Booking Workflow — Deeper

The booking workflow is the most error-prone stage of the trade lifecycle, because it is where human judgment meets system constraints.

**Trade capture form:** The form varies by product family, but typically includes:

| Field Category | Specific Fields |
|---------------|----------------|
| **Economic terms** | Notional, underlying(s), strike level, barrier level(s), maturity date, coupon rate, coupon frequency |
| **Product structure** | Product type (RC, Autocallable, CLN, etc.), observation convention (European/American), settlement type (cash/physical) |
| **Counterparty** | Counterparty name, counterparty ID, ISDA agreement reference, CSA reference |
| **System fields** | Booking system (NEMO/Murex), trading book, trader ID, structurer ID |
| **Settlement** | Settlement currency, settlement lag, SSI reference |

**Validation rules** in the booking system catch common errors:

- Does the maturity date fall on a business day? If not, apply the business day convention.
- Is the notional within the counterparty's credit limit?
- Is the counterparty approved for this product type?
- Are the observation dates consistent with the coupon schedule?
- Is the product template correct for the product type?

**Amendment process:** After a trade is booked, terms may need to change — a notional reduction, a maturity extension, or a restructuring of the coupon. Every amendment follows a formal workflow:

1. Trader or structurer submits an amendment request with the proposed changes and the reason
2. Operations reviews the amendment for completeness and system feasibility
3. A second person (four-eyes check) verifies the amendment
4. The amendment is booked in the system with a full audit trail (who changed what, when, and why)
5. A new confirmation is sent to the counterparty reflecting the amended terms

Amendments without proper governance are a major operational risk — and a common focus of audit findings.

---

### Static Data

Static data is the reference data that does not change frequently — counterparty details, instrument definitions, settlement instructions, calendar definitions, and market data source mappings. It is the foundation on which the entire operational infrastructure rests.

**Why static data matters:** If the counterparty's SSI is wrong, the settlement will fail — money will be sent to the wrong account. If the holiday calendar is wrong, coupon dates will be wrong — the trade will pay on the wrong day. If the underlying instrument definition is wrong, fixings will reference the wrong price.

Static data errors are insidious because they are silent. The system does not know the data is wrong — it processes trades normally, using the incorrect data. The error is only discovered when a settlement fails, a coupon is missed, or a reconciliation break appears.

**Static data governance:**

| Aspect | Standard |
|--------|----------|
| **Who maintains it** | A dedicated static data team, separate from trading and operations |
| **How changes are approved** | Four-eyes principle: one person proposes a change, another approves it |
| **Reconciliation** | Periodic reconciliation against external sources (exchanges, clearing houses, counterparties) |
| **Quality checks** | Automated checks for completeness, consistency, and validity |

**Golden Source:** Every data element has a single authoritative system — the "golden source." When two systems disagree, the golden source is the tiebreaker.

| Data Type | Golden Source |
|-----------|-------------|
| Counterparty data | CRM or counterparty master database |
| Instrument data | Booking system (NEMO for ELN/CLN, Murex for SRT/STEG) |
| Market data | Pricing system (Sophis for ELN/CLN, Murex for SRT/STEG) |
| Settlement instructions | SSI database or settlement system |
| Holiday calendars | Market data vendor or internal calendar management system |

When a reconciliation break occurs, the first question is always: "Which system is the golden source for this data?" The golden source wins.

---

### Cash Reconciliation

Cash reconciliation is the daily comparison of expected cash flows against actual cash movements. It is the operational equivalent of checking your bank statement against your receipts.

**Nostro reconciliation:** The bank's internal records say it should have received $1M in coupon payments and paid $500K in settlements today. The bank's actual bank account (the nostro account) shows $995K received and $500K paid. The $5K difference is a "break" — and it must be investigated.

**What breaks look like:**

| Break Type | Example | Likely Cause |
|-----------|---------|-------------|
| Amount mismatch | Expected $1,000,000; received $999,722.22 | Day count calculation difference (ACT/360 vs ACT/365) |
| Missing payment | Expected a coupon payment; nothing received | Counterparty paid late, or payment is stuck in the clearing system |
| Unexpected payment | Received cash with no matching expected flow | A trade was amended but the expected flow was not updated |
| Rounding difference | Expected $100,000.00; received $100,000.01 | Rounding convention difference between systems |

**Investigation process:**
1. **Identify:** The reconciliation system flags the break
2. **Research:** Trace the expected flow back to the trade booking. Compare the calculation with the counterparty's calculation. Check for calendar differences, day count differences, or amendment history.
3. **Resolve:** Correct the error (in the system or by contacting the counterparty) and process any resulting cash flows
4. **Document:** Record the cause, the resolution, and any systemic fix to prevent recurrence

**Escalation:** Unresolved breaks exceeding a threshold (typically defined by dollar amount and age) are escalated to management. The escalation framework ensures that no break is forgotten.

| Break Age | Escalation Level |
|-----------|-----------------|
| 1 business day | Operations analyst investigates |
| 3 business days | Team lead reviews and assigns priority |
| 5 business days | Operations manager is informed |
| 10 business days | Department head and senior management are notified |

---

### Trade Reconciliation

Trade reconciliation is the front-to-back comparison of positions — ensuring that the front office systems (NEMO, Murex) agree with the back office systems (settlement system, accounting system) on what trades exist and what their terms are.

**What it catches:**

| Discrepancy | Meaning | Common Cause |
|------------|---------|-------------|
| Missing trade | Front office shows a trade that back office does not | Trade was entered in NEMO/Murex but not propagated to the settlement system |
| Duplicate booking | Two records for the same trade | Trade was entered twice (perhaps after a system error and retry) |
| Terms mismatch | Notional in NEMO is $10M; notional in settlement system is $1M | Decimal error during booking, or amendment not reflected in both systems |
| Status mismatch | NEMO shows the trade as live; settlement system shows it as matured | Lifecycle event (autocall, maturity) processed in one system but not the other |

Trade reconciliation is performed daily for active products. Breaks are investigated and resolved using the same identify-research-resolve-document process as cash reconciliation.

---

### Settlement

Settlement is where the abstract world of bookings becomes the concrete world of money and securities changing hands.

**Settlement workflow:**

```
Trade Date  →  +Settlement Lag  →  Settlement Date  →  DvP Instruction  →  Cash/Securities Exchange
   (T)            (typically T+2)        (T+2)           (sent to CSD)        (executed via CSD)
```

**Fails management:** A settlement fail occurs when one party does not deliver on the settlement date. This can happen because:
- The seller does not have the securities to deliver
- The buyer does not have the cash to pay
- Settlement instructions are wrong (wrong account, wrong currency)
- A system or communication failure prevents the instruction from reaching the CSD (Central Securities Depository)

**Consequences of fails:**

| Consequence | Description |
|------------|-------------|
| **Fails charges** | Many CSDs and settlement systems impose monetary penalties for late settlement (e.g., CSDR in Europe). These charges accrue daily until the fail is resolved. |
| **Buy-in** | If the seller fails to deliver securities after a specified period, the buyer can execute a buy-in — purchasing the securities in the open market and charging the price difference to the failing seller. |
| **Reputational damage** | Persistent settlement fails damage the bank's reputation with counterparties and custodians. |

**Settlement types per product family:**

| Product Family | Typical Settlement |
|---------------|-------------------|
| **ELN** | Cash settlement (final redemption paid in cash) or physical delivery of shares if barrier is breached and product terms require physical settlement |
| **Swaps** | Net cash settlement of periodic payments — only the net difference between the two legs is exchanged |
| **SRT** | Cash settlement of coupon payments. At maturity, the notional principal is returned (unless the rate conditions trigger a different outcome) |
| **CLN** | Cash settlement if no credit event occurs. If a credit event occurs, physical delivery of the reference obligation (bonds of the defaulted entity) or cash settlement at recovery value |

---

### Corporate Actions — Systematic Treatment

Corporate actions are changes to a company's share structure or capital — stock splits, mergers, dividends, spin-offs. For structured products linked to equities, these events require precise adjustments to the product's terms. A missed or miscalculated corporate action adjustment can result in material financial loss.

**Stock Split**

When a company splits its shares, the strike, barrier, and unit quantity are adjusted by the split ratio to maintain economic equivalence.

*Example:* A 2-for-1 stock split on a Reverse Convertible.
- Before split: Strike = $100, Barrier = $70, Notional shares = 10,000
- After split: Strike = $50, Barrier = $35, Notional shares = 20,000
- The economic exposure is unchanged — the investor's position is worth the same.

**Reverse Stock Split**

The opposite adjustment. A 1-for-5 reverse split:
- Before: Strike = $10, Barrier = $7, Notional shares = 50,000
- After: Strike = $50, Barrier = $35, Notional shares = 10,000

**Merger**

When the underlying company is acquired or merges with another entity, the successor entity replaces the original underlying. The ISDA Equity Definitions define the adjustment methodology — typically, the calculation agent determines a fair adjustment ratio based on the merger terms.

If Company A (the underlying) is acquired by Company B at a ratio of 0.8 shares of B per share of A, the product's underlying becomes Company B, and the strike and barrier are adjusted by the 0.8 ratio.

**Tender Offer**

A tender offer may trigger an **Extraordinary Event** under the ISDA Equity Definitions. If the tender results in a change of control, the product may be terminated early at its fair market value (Cancellation and Payment), or the terms may be adjusted to reflect the new corporate structure.

**Rights Issue**

When a company issues new shares at a discount to existing shareholders, this dilutes the value of existing shares. The strike and barrier must be adjusted to reflect the dilution effect.

The adjustment factor is typically calculated as: R = (Market Price) / (Market Price + Rights Value per Share)

Strike and barrier are multiplied by R to maintain economic equivalence.

**Spin-Off**

When a company separates a business unit into a new independent company, existing shareholders receive shares in the new entity. For structured products, the basket may need to include the new entity, or the terms may be adjusted to reflect the value allocated to the spin-off.

**Special Dividend**

Ordinary dividends are anticipated in the product's pricing and do not trigger adjustments. But dividends that exceed a threshold (defined in the product's terms or in the ISDA Equity Definitions) are classified as **extraordinary dividends** and trigger an adjustment — typically, the strike is reduced by the extraordinary dividend amount per share.

**ISDA Fallback Provisions**

The ISDA 2002 Equity Definitions provide a cascade of adjustment methods:

| Priority | Method | Description |
|:--------:|--------|-------------|
| 1 | Calculation Agent Adjustment | The calculation agent (typically the bank) determines an appropriate adjustment to maintain economic equivalence |
| 2 | Modified Calculation Agent Adjustment | The calculation agent adjusts, but the method is constrained by reference to the relevant exchange's adjustment to listed options |
| 3 | Cancellation and Payment | The trade is terminated at its fair market value — used when no reasonable adjustment is possible |

**Why corporate actions are operationally dangerous:** They require immediate identification (often within hours of announcement), correct mathematical calculation, system update across all relevant platforms (NEMO, Sophis, Murex), and client notification — all within tight deadlines. A stock split announced on Friday afternoon must be reflected in the systems by Monday morning. A missed adjustment means every subsequent fixing, coupon observation, and barrier check will be calculated against the wrong levels.

---

### Trade Amendments

After a trade is booked, its terms may need to change. Common reasons include:

- The client requests a partial unwind (reducing the notional)
- The client and bank agree to extend the maturity
- A restructuring changes the coupon or barrier terms
- A booking error is discovered and must be corrected

**Approval workflow:**

1. Trader or structurer submits the amendment request, specifying the proposed changes and the commercial rationale
2. Operations reviews the request for completeness and checks that the system can accommodate the change
3. Four-eyes verification: a second operations analyst confirms the amendment details against the original booking
4. The amendment is executed in the booking system
5. An amended confirmation is generated and sent to the counterparty
6. Product Control reviews the P&L impact of the amendment

**Audit trail:** Every amendment is recorded with:
- What was changed (old value and new value)
- Who requested the change
- Who approved the change
- When the change was made
- Why the change was made

The audit trail is non-negotiable. Amendments without documentation are a control failure — and a regulatory red flag.

---

### Trade Breaks

A trade break is a discrepancy between two systems or two parties that should agree but do not. Trade breaks are the symptoms of operational errors, system failures, or process gaps.

**Types of trade breaks:**

| Break Type | Description | Example |
|-----------|-------------|---------|
| **Position break** | Two internal systems disagree on the position | NEMO shows 10,000 shares underlying; Sophis shows 10,500 shares |
| **Cash break** | Expected cash flow does not match actual cash flow | Expected $500K coupon; received $495K |
| **Confirmation break** | The bank and counterparty disagree on trade terms | Bank's confirmation says strike = 95%; counterparty says strike = 90% |
| **Valuation break** | Front office and Product Control disagree on the trade's value | Trader marks the trade at $102; independent valuation says $99 |

**Investigation — systematic approach:**

1. Check the original booking: is the trade correctly entered?
2. Check the amendment history: was the trade changed after booking, and was the change reflected in all systems?
3. Check the enrichment: did the system populate the secondary fields correctly?
4. Check the counterparty records: does the counterparty's version match ours?
5. Check the market data: are both systems using the same market data?

**Resolution:** Once the cause is identified, the error is corrected in the relevant system. The correction is documented, and the root cause is analyzed to determine whether a systemic fix is needed to prevent recurrence.

**Escalation schedule:**

| Break Age | Action |
|-----------|--------|
| 0-1 day | Operations analyst owns the investigation |
| 1-3 days | Escalated to team lead for prioritization |
| 3-5 days | Escalated to desk head / operations manager |
| 5+ days | Escalated to department head and senior management. Reported in operational risk metrics. |

Unresolved breaks that persist beyond the escalation thresholds are reported in the bank's operational risk reporting and may be flagged by internal audit.

---

### Lifecycle Events — Detailed

Lifecycle events are the moments during a trade's life where something happens that requires operational action. Each product family has its own set of lifecycle events, but the operational principles are consistent.

**Fixings**

On observation dates, the underlying price must be captured from the correct source. For equity-linked products, the fixing source is typically the official closing price from the relevant exchange (e.g., the NYSE official closing price for US-listed stocks, the Xetra closing price for German-listed stocks).

Operations must ensure:
- The correct fixing source is used (per the product's terms)
- The fixing is captured at the correct time (closing auction, not intraday)
- The fixing is applied to the correct observation date (accounting for holidays and business day adjustments)
- If the fixing source is unavailable (market disruption), the fallback procedure is followed per the product's terms

**Coupon Payments**

For products with conditional coupons (e.g., Phoenix Autocallables, Reverse Convertibles with coupon barriers), the coupon payment depends on whether the underlying meets the coupon condition on the observation date.

The operational workflow:
1. Capture the fixing on the observation date
2. Compare the fixing to the coupon barrier
3. If the condition is met, calculate the coupon amount
4. Generate the payment instruction
5. Send the payment on the payment date (typically 2-5 business days after the observation date)

For memory coupons (as taught in Section 5.1.3, Phoenix Autocallable), Operations must also check whether previously missed coupons are recoverable — adding complexity to the calculation.

**Barrier Observations**

Barrier monitoring requires knowing the observation convention specified in the product's terms:

| Convention | Monitoring Approach |
|-----------|-------------------|
| **Continuous (American)** | The underlying is monitored throughout every trading day. If the price touches the barrier at any point — even intraday — the barrier is breached. |
| **Daily close (discrete)** | The barrier is checked only against the official closing price on each trading day. Intraday breaches do not count. |
| **Periodic (European-style)** | The barrier is checked only on specified observation dates (e.g., quarterly, or only at maturity). |

Getting the observation convention wrong is one of the most consequential operational errors. If the system is set to daily close observation but the product's terms specify continuous monitoring, a barrier breach could be missed — or vice versa, a barrier breach could be incorrectly recorded.

**Autocall Checks**

On autocall observation dates (typically quarterly or semi-annually), Operations checks whether the underlying is above the autocall level:

1. Capture the fixing on the autocall observation date
2. Compare the fixing to the autocall barrier (e.g., 100% of initial level)
3. If the underlying is at or above the autocall level, the product terminates early
4. Calculate the early redemption amount (typically 100% of notional plus any accrued or memory coupons)
5. Schedule the redemption payment
6. Notify the counterparty of the early termination
7. Close the trade in the booking system

If the autocall does not trigger, the trade continues to the next observation date.

---

### Common Mistakes

1. **Treating booking as a clerical task.** Booking is the foundation of every subsequent operational process — P&L, risk, settlement, lifecycle events. A booking error propagates through every downstream system. A strike entered as 95 instead of 95% (or vice versa) will cause a reconciliation break in every system that references the trade.

2. **Not verifying the fixing source.** The product's terms specify which price source to use for fixings. Using the wrong source (e.g., Bloomberg closing price instead of the exchange official closing price) can result in a different fixing value — and a different coupon or payoff.

3. **Assuming the system handles corporate actions automatically.** Some systems have automated corporate action processing; many do not. Even automated systems require human verification. A stock split that is correctly identified but incorrectly applied (e.g., the ratio is entered as 2.0 instead of 0.5 for a reverse split) will corrupt every subsequent calculation.

4. **Ignoring unconfirmed trades.** An unconfirmed trade is a ticking time bomb. The bank and the counterparty may disagree on terms without knowing it. When a payment comes due and the amounts do not match, resolving the dispute can be costly. Best practice: escalate any trade that remains unconfirmed beyond 5 business days.

5. **Not documenting trade break resolutions.** Fixing a break without documenting the cause and the fix is like patching a leak without finding the source. The same error will recur. Every break resolution must include a root cause analysis and, where appropriate, a systemic fix.

6. **Confusing barrier observation conventions.** Continuous observation and daily-close observation produce different outcomes for the same product and market path. A product that should monitor continuously but is set to daily close may miss a barrier breach — resulting in an incorrect payoff and a potential dispute with the counterparty.

> **Professor Note:** If you remember only one thing from this section, remember this: the front office designs the product and the hedge. Operations makes it real. Every coupon payment, every fixing, every barrier check, every settlement — these are the moments where the product's promises are either kept or broken. Operations does not create the P&L, but Operations can destroy it.
