### Callable Steepener

#### Definition

A Callable Steepener pays a leveraged coupon linked to the CMS 30Y − CMS 10Y spread, with an issuer Bermudan call right that allows the issuer to redeem the note at par on any semi-annual call date after year 2.

The coupon formula is identical to VSTEG001:

**Coupon = 5 × (CMS 30Y − CMS 10Y), floor 0%, cap 9%**

The key difference is the callable feature. The investor sells a Bermudan call option to the issuer, receiving a higher cap (9% vs VSTEG001's 8%) as compensation. The call premium funds the wider cap and contributes to the coupon economics.

The issuer calls when it becomes economically advantageous — typically when rates fall (cheaper refinancing) or when the curve steepens significantly (capping the coupon cost). This creates negative convexity for the investor: the product is called away in exactly the scenarios where the investor would most want to keep it.

This product combines two forms of optionality — the CMS spread exposure and the Bermudan call. Their interaction is the core pricing challenge. Both are driven by rate dynamics, making them correlated. The same rate movements that increase the coupon also influence the call decision, requiring joint calibration (see CRASRT001 for the SRT parallel).

#### Construction

The Callable Steepener decomposes into five components:

**Component 1 — Fixed-rate bond (funding).** Par redemption at maturity or call date. Same as VSTEG001.

**Component 2 — CMS spread coupon strip (leveraged).** Leveraged coupon linked to CMS 30Y − CMS 10Y, observed semi-annually. Same mechanism as VSTEG001 — every 10 bps of spread produces 50 bps of coupon.

**Component 3 — CMS floor (embedded, 0%).** Prevents negative coupon. Same as VSTEG001.

**Component 4 — CMS cap (embedded, 9%).** Limits maximum coupon. Higher than VSTEG001's 8% cap — the additional 1% cap headroom is funded by the call premium.

**Component 5 — Bermudan call (issuer).** The issuer has the right to redeem the note at par on any semi-annual date starting from year 2. The investor is short this call — they have sold the issuer an option on the note's remaining tenor. The call premium (approximately 0.8% per annum) is embedded in the note's economics.

**Comparison to VSTEG001:** Same CMS spread mechanics. The callable feature adds one component (Bermudan call) and raises the cap from 8% to 9%. The investor's trade-off is clear: higher potential coupon (wider cap) in exchange for uncertain tenor (call risk).

**Comparison to CRASRT001 (SRT):** Both combine a rate-linked coupon with an issuer Bermudan call. CRASRT001 uses a range-accrual coupon on a single rate (SOFR). This product uses a leveraged CMS spread coupon. The dual optionality interaction is analogous — rate dynamics drive both the coupon and the call decision.

#### Booking & systems

Callable Steepeners are booked in the Murex four-leg framework.

**Note leg.** The structured note carrying the CMS spread coupon formula and call schedule. Critical fields: coupon formula (5 × (CMS 30Y − CMS 10Y)), leverage (5x), floor (0%), cap (9%), CMS fixing dates, call schedule (semi-annual after year 2), call notification period (typically 10 business days), CMS fixing source, and maturity date.

**Issuer leg.** Standard internal funding. Funding rate, curve, and credit spread.

**Deposit leg.** Client collateral. Standard fields.

**Hedge leg.** The market risk hedge includes CMS cap/floor structures (for the spread optionality) and a Bermudan swaption (for the call right). Critical fields: Bermudan exercise dates (must match note call dates exactly), CMS tenor pair, cap/floor strikes, convexity adjustment model, correlation assumption, and Bermudan exercise boundary calibration. The Bermudan swaption must be calibrated jointly with the CMS spread model — the call decision depends on the level and slope of rates, which also determine the CMS spread.

**Termsheet** defines the call schedule, notification period, coupon formula, and CMS fixing source. The call notification period is an operational risk — if the Termsheet specifies 10 business days and the Murex note leg uses a different convention, the issuer's exercise may be invalid.

#### Pricing intuition

Callable Steepener pricing requires joint calibration of CMS spread dynamics and the Bermudan exercise strategy.

**Dual optionality interaction.** The CMS spread coupon and the Bermudan call are not independent risks. A rate decline that steepens the curve increases the coupon (good for investor) but also increases the call probability (bad for investor). The issuer's optimal call strategy depends on the remaining coupon cost relative to refinancing — if the curve is very steep and the coupon is high (e.g., 7-8%), the issuer calls to cap their loss. This is negative convexity: the investor's upside is capped both by the 9% cap and by the call.

**When does the issuer call?** The issuer calls when the present value of remaining coupon payments exceeds the cost of refinancing. In practice:
- Rates fall significantly → issuer refinances cheaply → call
- Curve steepens sharply → coupon cost very high → call to cap losses
- Both effects compound: falling rates that steepen the curve create the highest call probability

**Bermudan value.** The Bermudan call is worth approximately 0.8% per annum to the issuer (and costs the investor the same). This premium is higher than the ICN001 Bermudan call (0.6%) because the CMS spread coupon has higher potential volatility than a fixed coupon, making the call option more valuable.

**Greeks:**
- Curve slope: Primary risk. Same as VSTEG001 but truncated by call
- Bermudan value: Increases with rate vol and decreases with rate level
- Correlation: Affects both spread distribution and the correlation between coupon and call events
- CMS convexity: Same as VSTEG001
- Negative convexity: The call creates concavity in the payoff — investor loses in both extreme steepening (call) and flattening (zero coupon) scenarios

#### Worked example (USD 10M)

**Terms:** USD 10M notional, 10-year maturity (callable semi-annually after Y2). Coupon = 5 × (CMS 30Y − CMS 10Y), floor 0%, cap 9%. CMS fixing source: ISDA CMS.

**Current market:** CMS 30Y = 4.20%, CMS 10Y = 3.40%. Spread = 80 bps.

**Decomposition:**

| Component | Value |
|---|---|
| Expected coupon (5 × 80 bps) | 4.0% p.a. |
| Funding cost | 3.0% |
| FTP | 0.4% |
| Desk margin | 0.3% |
| CMS spread optionality (floor + cap + convexity) | 1.1% |
| Bermudan call premium | 0.8% |

**Verification:** 3.0% + 0.4% + 0.3% + 1.1% + 0.8% = 5.6%. Total cost capacity exceeds the 4.0% expected coupon by 1.6%. The 0.8% call premium and the higher cap (9% vs 8%) are how the investor is compensated for accepting the call risk. The remaining 0.8% represents the reduced CMS optionality cost from the lower cap strike (9% vs VSTEG001's effective cost at 8%).

**Scenario 1 — curve steepens moderately, rates stable (no call):**
- CMS 30Y = 4.50%, CMS 10Y = 3.40%. Spread = 110 bps
- Coupon = 5 × 1.10% = 5.5%
- Semi-annual payment: USD 10M × 5.5% × 0.5 = USD 275,000
- Issuer does not call — coupon cost manageable

**Scenario 2 — curve steepens sharply, rates fall (issuer calls at Y3):**
- CMS 30Y = 4.00%, CMS 10Y = 2.80%. Spread = 120 bps
- Coupon = 5 × 1.20% = 6.0%. Very high coupon cost for issuer
- Issuer calls at Y3 — returns USD 10M at par
- Investor earned 3 years of 4.0-6.0% coupon but lost 7 years of potential high coupons
- Reinvestment at new lower rates yields ~2.5% — the reinvestment gap

**Scenario 3 — curve flattens (no call, low coupon):**
- CMS 30Y = 3.50%, CMS 10Y = 3.40%. Spread = 10 bps
- Coupon = 5 × 0.10% = 0.5%
- Semi-annual payment: USD 10M × 0.5% × 0.5 = USD 25,000
- Issuer does not call — low coupon means low cost to issuer
- Investor locked into 10 years of near-zero coupon with no call relief

#### Reconciliation specifics

**Call schedule (most critical for callable variant).** The semi-annual call dates in the Murex note leg must exactly match the Bermudan exercise dates in the hedge leg swaption. A single misaligned call date means the issuer can exercise on a date the hedge does not cover — an unhedged call event. For a 10-year note callable from Y2, there are 16 potential call dates to verify.

**Call notification period.** The Termsheet typically specifies a notification period (e.g., 10 business days before the call date). This period must be reflected in both the note leg and the hedge leg. If the note leg allows exercise with 5 days' notice but the hedge leg assumes 10 days, the hedge may fail to cover the call event.

**CMS fixing source.** Same risk as VSTEG001 — ISDA CMS rate definition must match between legs. The impact is slightly reduced for callable steepeners because the note's expected life is shorter (call probability reduces the duration).

**Convexity adjustment consistency.** Same model required in both legs. The convexity adjustment interacts with the Bermudan valuation because the adjustment affects the expected coupon, which influences the call decision.

#### Desk view

**Who buys this product.** Yield seekers who want the higher cap (9%) and are willing to accept uncertain tenor. Insurance companies with reinvestment strategies that can accommodate early redemption. Investors who believe rates will remain stable (low call probability) while the curve stays steep.

**The real risk.** Negative convexity. The investor loses in both extreme scenarios: sharp steepening triggers a call (investor loses future high coupons), and flattening means zero coupon for 10 years (issuer will not call when the note is cheap to maintain). The investor only wins in the narrow band where the curve steepens enough to generate attractive coupons but not enough to trigger a call.

This is the same reinvestment risk pattern as ICN001 (Issuer Callable Note in ELN) — the issuer calls at the worst time for the investor. The difference is that the Callable Steepener's coupon is linked to the CMS spread, not fixed, so the call decision and the coupon are correlated rather than independent.

**When appropriate.** View that curve will steepen moderately (not enough to trigger call). Stable rate environment. Investor can tolerate reinvestment risk.

**When not appropriate.** Falling rate environment (high call probability). Need for certain tenor. Investor who does not understand negative convexity.

#### Desk shorthand

*Callable curve bet; CMS spread, issuer call.*
