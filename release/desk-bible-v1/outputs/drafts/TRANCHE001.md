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
