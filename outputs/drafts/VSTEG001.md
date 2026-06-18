### Vanilla Steepener Note

#### Definition

A Vanilla Steepener Note pays a leveraged coupon linked to the spread between two CMS (Constant Maturity Swap) rates of different tenors — typically CMS 30Y − CMS 10Y. When the yield curve is steep (long rates well above short rates), the coupon is high. When the curve flattens or inverts, the coupon drops toward zero, where a floor prevents it from going negative.

The coupon formula is:

**Coupon = N × (CMS 30Y − CMS 10Y), floor 0%, cap C%**

where N is the leverage factor and C is the cap rate. Leverage of 3x–7x is typical; 5x is the standard case. The note is non-callable — there is no issuer call right, making this a pure directional bet on curve steepness for the full tenor.

The investor's trade is exchanging the certainty of a fixed-rate coupon for a leveraged exposure to the yield curve's slope. The convexity adjustment — a correction applied to CMS rates to account for the difference between a swap rate and its expected value under the forward measure — is the single most important pricing concept for this product. It reduces the effective spread and represents a hidden cost to the investor.

#### Construction

The Vanilla Steepener Note decomposes into four components:

**Component 1 — Fixed-rate bond (funding).** The note's principal structure. Provides par redemption at maturity and defines the funding cost of the note. The investor receives 100% of notional at maturity regardless of CMS rate outcomes.

**Component 2 — CMS spread coupon strip (leveraged).** A series of semi-annual coupons, each determined by the CMS 30Y − CMS 10Y spread observed on the fixing date, multiplied by the leverage factor. This is the primary value driver. With 5x leverage, every 10 bps of CMS spread produces 50 bps of coupon.

**Component 3 — CMS floor (embedded, 0%).** A strip of floorlets that activate when the leveraged CMS spread would produce a negative coupon — i.e., when the curve inverts. The investor is long this floor. It ensures the coupon never falls below zero, providing asymmetric protection against curve inversion.

**Component 4 — CMS cap (embedded, 8%).** A strip of caplets that limit the maximum coupon to 8%. The investor is short this cap — they have sold away the upside above 8% to help fund the leveraged spread exposure. The cap strikes represent extreme steepening scenarios (spread above 160 bps with 5x leverage).

**Net position:** The investor is long leveraged CMS spread exposure, long the floor (downside protection), and short the cap (upside given away). The cap and floor together create a collar around the CMS spread coupon.

#### Booking & systems

Vanilla Steepener Notes are booked in the Murex four-leg framework.

**Note leg.** The structured note carrying the CMS spread coupon formula. Critical fields: coupon formula (5 × (CMS 30Y − CMS 10Y)), leverage factor (5x), floor rate (0%), cap rate (8%), CMS fixing dates (semi-annual schedule), CMS tenor pair (30Y/10Y), CMS fixing source (ISDA CMS rate definition), day count convention, and maturity date. The coupon formula must be entered exactly — leverage, floor, cap, and tenor pair are all required for correct valuation.

**Issuer leg.** The issuer's internal funding cost. Standard fields: funding rate, funding curve, and credit spread. Computed on the note's fixed notional.

**Deposit leg.** Client collateral. Standard fields: deposit rate, tenor, and rollover convention.

**Hedge leg.** The market risk hedge consists of CMS cap/floor structures and CMS spread options that replicate the embedded optionality. Critical fields: hedge instrument type (CMS cap, CMS floor, CMS spread option), CMS tenor pair (30Y/10Y), strikes, leverage, expiry schedule, notional, convexity adjustment model, and correlation assumption. The convexity adjustment model and correlation parameters must match between the note leg valuation and the hedge leg pricing — a mismatch creates a systematic P&L leak that compounds over the note's life.

**Termsheet** defines the complete CMS fixing schedule, leverage, floor, cap, CMS tenor pair, and the ISDA CMS rate definition used for fixings. The fixing source is the key operational detail — it determines which CMS rate is used on each observation date.

#### Pricing intuition

Steepener pricing is dominated by three model-dependent inputs: the convexity adjustment, the correlation between CMS tenors, and normal volatility.

**Convexity adjustment.** CMS rates are not equal to forward swap rates. The convexity adjustment corrects for the difference between a swap rate and its expected value under the payment measure. For CMS 30Y, the adjustment is typically 3–8 bps (reducing the effective rate); for CMS 10Y, it is smaller (1–3 bps). The net effect reduces the effective CMS spread by approximately 5 bps. With 5x leverage, this costs the investor roughly 25 bps of coupon — a material hidden cost. The adjustment increases with the level of rates and with volatility.

**Correlation.** The correlation between CMS 30Y and CMS 10Y determines the distribution of the CMS spread. High correlation (e.g., 0.95) means the two rates move closely together, compressing the spread distribution and reducing option values. Lower correlation widens the spread distribution. Correlation is not directly observable — it is an implied or model parameter calibrated to CMS spread option prices or historical data. A 5-point correlation change can move the note's value by 20–40 bps.

**Normal volatility.** The swaption volatility (in Bachelier/normal terms, quoted in bps) affects both the floor value (benefit to investor) and the cap value (cost to investor). At 65 bps normal vol, the floor has meaningful value in environments where the curve is near-flat.

**Greeks:**
- Curve slope (CMS 30Y − CMS 10Y): Primary risk. 10 bps flattening → 50 bps coupon drop (5x leverage)
- Correlation: Higher correlation → lower spread vol → lower option values
- CMS convexity: Rises with rate level → reduces effective coupon in high-rate environments
- Normal vol: Affects floor and cap values in offsetting directions
- DV01: Modest — the note's principal is fixed; rate exposure is through coupon, not notional

#### Worked example (USD 10M)

**Terms:** USD 10M notional, 10-year maturity, semi-annual CMS fixings. Coupon = 5 × (CMS 30Y − CMS 10Y), floor 0%, cap 8%. CMS fixing source: ISDA CMS.

**Current market:** CMS 30Y = 4.20%, CMS 10Y = 3.40%. Spread = 80 bps.

**Decomposition:**

| Component | Value |
|---|---|
| Expected coupon (5 × 80 bps) | 4.0% p.a. |
| Funding cost | 3.0% |
| FTP | 0.4% |
| Desk margin | 0.3% |
| CMS spread optionality (floor + cap + convexity) | 1.3% |

**Verification:** 3.0% + 0.4% + 0.3% + 1.3% = 5.0%. Investor receives 4.0% expected coupon. The 1.0% difference between the total cost (5.0%) and the expected coupon (4.0%) represents the net cost of the leverage and the embedded options — the investor pays for the floor protection and convexity adjustment through the cap premium.

**Semi-annual coupon calculation (first fixing):**

| Step | Calculation | Result |
|---|---|---|
| CMS 30Y fixing | Observed rate | 4.20% |
| CMS 10Y fixing | Observed rate | 3.40% |
| CMS spread | 4.20% − 3.40% | 0.80% |
| Leveraged coupon | 5 × 0.80% | 4.00% |
| Floor test | max(4.00%, 0%) | 4.00% |
| Cap test | min(4.00%, 8%) | 4.00% |
| Semi-annual payment | USD 10M × 4.00% × 0.5 | USD 200,000 |

**Scenario 1 — curve steepens to 120 bps:**
- CMS 30Y = 4.60%, CMS 10Y = 3.40%. Spread = 120 bps
- Coupon = 5 × 1.20% = 6.0%
- Semi-annual payment: USD 10M × 6.0% × 0.5 = USD 300,000
- Investor earns well above funding — the steepening trade is paying

**Scenario 2 — curve flattens to 30 bps:**
- CMS 30Y = 3.70%, CMS 10Y = 3.40%. Spread = 30 bps
- Coupon = 5 × 0.30% = 1.5%
- Semi-annual payment: USD 10M × 1.5% × 0.5 = USD 75,000
- Investor earns below funding — the flattening is eroding the coupon

**Scenario 3 — curve inverts (spread = −20 bps):**
- CMS 30Y = 3.20%, CMS 10Y = 3.40%. Spread = −20 bps
- Leveraged coupon = 5 × (−0.20%) = −1.0%
- Floor activates: max(−1.0%, 0%) = 0%
- Semi-annual payment: USD 0
- Investor earns zero coupon — principal still protected at maturity

#### Reconciliation specifics

**CMS fixing source (most critical operational risk).** The ISDA CMS rate definition used for fixing must be identical in the Murex note leg and the hedge leg. A mismatch — even a different screen page or publication time — creates a fixing basis that produces a small but systematic P&L difference on every fixing date. Over 20 semi-annual fixings, these differences compound.

**Convexity adjustment consistency (most critical model risk).** The convexity adjustment model and its calibration parameters must be the same in the note leg valuation and the hedge leg pricing. If the note leg uses a replication-based convexity adjustment but the hedge leg uses a short-rate model adjustment, the two legs will disagree on the effective CMS rate by 2–5 bps per fixing. With 5x leverage, a 3 bps mismatch becomes a 15 bps coupon disagreement per period — approximately USD 7,500 per semi-annual fixing on USD 10M notional.

**Leverage factor.** The leverage (5x) must appear in both the note leg coupon formula and the hedge leg notional/strike calibration. An error in either leg (e.g., 5x in the note but 4x in the hedge) creates an unhedged CMS spread exposure equal to 1x the spread — approximately 80 bps of coupon risk.

**Floor/cap strikes.** The 0% floor and 8% cap must be present in both the note leg and the hedge leg. A missing floor means the investor could face negative coupons (not contractually possible). A missing cap means the issuer has unlimited coupon exposure.

**Correlation calibration.** The correlation assumption between CMS 30Y and CMS 10Y must be calibrated to market data (CMS spread options if available, or historical correlation with an appropriate lookback window). Using a default flat correlation (e.g., 90%) instead of a calibrated value creates a systematic mispricing — typically undervaluing the spread optionality.

#### Desk view

**Who buys this product.** Macro hedge funds with a structural view that the yield curve will remain steep or steepen further. Insurance companies with long-duration liabilities who believe rates will normalise (long end rising faster than short end). Pension funds seeking above-market coupons in a steep curve environment. Private bank clients who want leveraged yield without principal risk.

**The real risk.** Curve flattening or inversion eliminates the coupon entirely. The 5x leverage that amplifies steepening gains also amplifies flattening losses — every 10 bps of flattening costs 50 bps of coupon. The floor at 0% protects against negative coupons but does not protect against opportunity cost: an investor locked into a 10-year steepener during a prolonged flat-curve period earns zero while the funding rate is 3.0%.

The convexity adjustment is a persistent hidden cost. Unlike the floor (which protects) or the cap (which is visible), the convexity adjustment silently reduces the effective CMS spread on every fixing. In a high-rate, high-vol environment, the convexity adjustment can reduce the expected coupon by 30–50 bps.

**When appropriate.** Strong conviction that the yield curve will remain steep or steepen. 10-year investment horizon. Investor understands leverage and can tolerate zero-coupon periods.

**When not appropriate.** Flat or inverted curve environment. Need for stable income (the coupon is inherently volatile). Investor does not understand convexity adjustment or correlation risk.

#### Desk shorthand

*Leveraged curve bet; CMS spread, floor zero, cap eight.*
