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
