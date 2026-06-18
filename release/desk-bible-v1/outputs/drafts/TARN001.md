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
