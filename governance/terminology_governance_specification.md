# TERMINOLOGY GOVERNANCE SPECIFICATION

**Ecosystem:** Structured Products Knowledge Ecosystem  
**Version:** V1.0.1-GOV-1.0  
**Effective:** 2026-06-27  
**Authority:** Canonical — all future content must comply  
**Protects against:** Terminology drift, convention drift, semantic contradiction, pedagogical harm

---

## How to Read This Specification

Each governed term has:
- **Canonical meaning** — the default interpretation in this ecosystem
- **Alternate meaning** — valid in practice but requires explicit labeling
- **Forbidden usage** — patterns that must never appear
- **Default interpretation** — what a reader should assume when no qualifier is present
- **Required qualifier** — what must be added when the alternate meaning is intended
- **Correct example** — validated usage
- **Incorrect example** — usage that fails governance
- **Linter rule** — how automated detection works

**Severity levels:**
- **S1 (Critical):** Self-contradictory or factually wrong. Must block publication.
- **S2 (High):** Ambiguous in a way that teaches the wrong answer. Must be resolved before publication.
- **S3 (Medium):** Ambiguous but interpretable from context. Should be resolved.
- **S4 (Low):** Stylistic or pedagogical preference. May be flagged but not blocking.

---

## PART 1 — CORRELATION AND EXPOSURE TERMS

### T-COR-01: Long Correlation

| Field | Value |
|-------|-------|
| **Canonical meaning** | The position benefits when correlation rises (P&L increases or risk decreases as ρ increases) |
| **Alternate meaning** | The position holder bought correlation premium (structural convention) |
| **Forbidden usage** | "Long correlation" combined with "harmed by rising correlation" in the same sentence |
| **Default interpretation** | MTM / economic sensitivity (Convention A) |
| **Required qualifier** | If structural meaning intended: "structurally long correlation" |
| **Correct example** | "FTD investors are long correlation — they benefit when default correlation is high." |
| **Incorrect example** | "FTD investors are long correlation. They lose when correlation rises." |
| **Linter rule** | `LNT-COR-01`: Flag "long correlation" within 2 sentences of "harm/hurt/lose/decrease" + "correlation rise/high/increase" |

### T-COR-02: Short Correlation

| Field | Value |
|-------|-------|
| **Canonical meaning** | The position benefits when correlation falls |
| **Alternate meaning** | The position holder sold correlation premium (structural convention) |
| **Forbidden usage** | "Short correlation" combined with "benefit from high correlation" in the same sentence |
| **Default interpretation** | MTM / economic sensitivity |
| **Required qualifier** | If structural meaning intended: "structurally short correlation" |
| **Correct example** | "NTD investors are short correlation — high ρ increases their risk as defaults cluster." |
| **Incorrect example** | "WOAC investors are short correlation: they benefit from high correlation." |
| **Linter rule** | `LNT-COR-02`: Flag "short correlation" within 2 sentences of "benefit/profit/gain" + "correlation rise/high/increase" |

### T-COR-03: Structural Correlation

| Field | Value |
|-------|-------|
| **Canonical meaning** | Correlation direction described by who bought/sold the correlation premium |
| **Alternate meaning** | None in this ecosystem |
| **Forbidden usage** | Using structural convention without the word "structurally" |
| **Default interpretation** | If "structurally" is absent, assume MTM convention |
| **Required qualifier** | The word "structurally" must appear |
| **Correct example** | "The investor is structurally short correlation — they sold the correlation premium." |
| **Incorrect example** | "The investor is short correlation (sold the premium)." — missing "structurally" |
| **Linter rule** | `LNT-COR-03`: Flag sentences containing "sold.*premium" or "bought.*premium" + "long/short correlation" without "structurally" |

### T-COR-04: Raw / Unhedged Position

| Field | Value |
|-------|-------|
| **Canonical meaning** | Exposure from embedded options in products sold, before any hedge |
| **Alternate meaning** | None |
| **Forbidden usage** | Describing a raw position as if it were a fundamental product property when hedging changes the direction |
| **Default interpretation** | When no qualifier is present and a desk position is described, assume raw |
| **Required qualifier** | "raw" or "unhedged" when the hedged position has a different direction |
| **Correct example** | "The desk's raw position on worst-of is short correlation." |
| **Incorrect example** | "The desk is short correlation on worst-of." — omits raw/hedged |
| **Linter rule** | `LNT-POS-01`: Flag "desk" + "long/short correlation" without "raw/unhedged/net/hedged" within the same sentence or preceding sentence |

### T-COR-05: Net / Hedged Position

| Field | Value |
|-------|-------|
| **Canonical meaning** | Residual exposure after all hedges (delta, gamma, vega, correlation, credit) |
| **Alternate meaning** | None |
| **Forbidden usage** | Describing a hedged position as if it were a structural property of the product |
| **Default interpretation** | Must be explicitly stated — never assumed |
| **Required qualifier** | "net" or "hedged" |
| **Correct example** | "The desk's net position is typically long correlation after dispersion hedges." |
| **Incorrect example** | "Worst-of products are long correlation for the bank." — is this raw or hedged? |
| **Linter rule** | `LNT-POS-02`: Flag "typically" + "long/short correlation" + desk context without "net/hedged" |

### T-COR-06: FTD Correlation Direction

| Field | Value |
|-------|-------|
| **Canonical meaning** | FTD investor is LONG correlation (MTM). Benefits from high ρ. |
| **Alternate meaning** | Structurally short (sold first-default premium) |
| **Forbidden usage** | "FTD is short correlation" without "structurally" qualifier |
| **Default interpretation** | Long correlation |
| **Required qualifier** | "structurally" if referring to premium direction |
| **Correct example** | "FTD investors are long correlation — high ρ means fewer isolated first defaults." |
| **Incorrect example** | "FTD investors are short correlation. They profit when correlation is high." |
| **Linter rule** | `LNT-COR-06`: Flag "FTD" + "short correlation" without "structurally" |

### T-COR-07: NTD Correlation Direction (N≥2)

| Field | Value |
|-------|-------|
| **Canonical meaning** | NTD investor (all N≥2) is SHORT correlation (MTM). Harmed by high ρ. |
| **Alternate meaning** | None commonly used |
| **Forbidden usage** | "NTD is long correlation" or "4TD/5TD is long correlation" without clear justification |
| **Default interpretation** | Short correlation for all N≥2 |
| **Required qualifier** | None — short correlation is unambiguous for NTD |
| **Correct example** | "5TD investors are short correlation — high ρ causes defaults to cluster past the 5th threshold." |
| **Incorrect example** | "5TD is long correlation (unambiguous)." |
| **Linter rule** | `LNT-COR-07`: Flag any NTD product (2TD/3TD/4TD/5TD/NTD) + "long correlation" |

### T-COR-08: Worst-of Investor Correlation Direction

| Field | Value |
|-------|-------|
| **Canonical meaning** | Worst-of investor is LONG correlation (MTM). Benefits from high ρ. |
| **Alternate meaning** | Structurally short (sold correlation premium via basket) |
| **Forbidden usage** | "Worst-of investor is short correlation" without "structurally" |
| **Default interpretation** | Long correlation |
| **Required qualifier** | "structurally" if referring to premium direction |
| **Correct example** | "Worst-of investors are long correlation — stocks moving together reduces barrier breach risk." |
| **Incorrect example** | "Worst-of investors are short correlation — they profit when stocks move together." |
| **Linter rule** | `LNT-COR-08`: Flag "worst-of" + "investor" + "short correlation" without "structurally" |

### T-COR-09: Dispersion Trade Direction

| Field | Value |
|-------|-------|
| **Canonical meaning** | Long single-stock vol + short basket vol = SHORT correlation |
| **Alternate meaning** | None |
| **Forbidden usage** | "dispersion = long correlation" |
| **Default interpretation** | Short correlation |
| **Required qualifier** | None |
| **Correct example** | "Dispersion trade (long single-stock vol, short basket vol) is short correlation." |
| **Incorrect example** | "Long single-stock vol + short basket vol = long correlation." |
| **Linter rule** | `LNT-COR-09`: Flag "long single-stock" + "short basket" + "long correlation" |

### T-COR-10: Correlation Reversal (NTD)

| Field | Value |
|-------|-------|
| **Canonical meaning** | The direction flip between FTD (long) and NTD (short), not a within-product non-monotonicity |
| **Alternate meaning** | None in this ecosystem |
| **Forbidden usage** | Implying that a single NTD product reverses its own correlation direction at some ρ level |
| **Default interpretation** | FTD-vs-NTD direction difference |
| **Required qualifier** | If used, must specify "between FTD and NTD" |
| **Correct example** | "The correlation reversal between FTD and NTD means FTD is long correlation while NTD (N≥2) is short." |
| **Incorrect example** | "2TD has a reversal at high ρ" — implies within-product flip |
| **Linter rule** | `LNT-COR-10`: Flag "reversal" + NTD product without "between FTD and NTD" or equivalent |

---

## PART 2 — CREDIT PROTECTION TERMS

### T-PRO-01: Protection Seller

| Field | Value |
|-------|-------|
| **Canonical meaning** | The party that takes on the credit/equity risk and earns the premium/coupon |
| **Alternate meaning** | None |
| **Forbidden usage** | Labeling the desk as "protection seller" in structured notes (RC/WOAC/CLN/FTD) |
| **Default interpretation** | In structured notes: INVESTOR = protection seller |
| **Required qualifier** | None — must be correct |
| **Correct example** | "The CLN investor sells credit protection and earns an enhanced coupon." |
| **Incorrect example** | "The desk sold protection via the short put." |
| **Linter rule** | `LNT-PRO-01`: Flag "desk" + "sold protection" or "desk" + "sells protection" in structured note context |

### T-PRO-02: Protection Buyer

| Field | Value |
|-------|-------|
| **Canonical meaning** | The party that transfers risk and pays the premium/coupon |
| **Alternate meaning** | None |
| **Forbidden usage** | Labeling the investor as "protection buyer" in structured notes (RC/WOAC/CLN/FTD) |
| **Default interpretation** | In structured notes: DESK = protection buyer |
| **Required qualifier** | None |
| **Correct example** | "The desk buys credit protection via the CLN structure, paying an enhanced coupon." |
| **Incorrect example** | "The investor buys protection through the CLN." |
| **Linter rule** | `LNT-PRO-02`: Flag "investor" + "buys protection" or "investor" + "bought protection" in structured note context |

### T-PRO-03: Embedded Put Ownership

| Field | Value |
|-------|-------|
| **Canonical meaning** | In RC/WOAC/CLN: investor has embedded SHORT put; desk is LONG the put |
| **Alternate meaning** | None |
| **Forbidden usage** | "Desk sold the put" or "desk is short the put" in structured note context |
| **Default interpretation** | Investor sold, desk bought |
| **Required qualifier** | None |
| **Correct example** | "The investor's embedded short put exposes them to downside risk below the barrier." |
| **Incorrect example** | "The desk, which sold the put, benefits from..." |
| **Linter rule** | `LNT-PRO-03`: Flag "desk" + "sold the put" or "desk" + "short put" in RC/WOAC/CLN/structured note context |

---

## PART 3 — VOL / GAMMA / DELTA TERMS

### T-GRK-01: Long Vol / Short Vol

| Field | Value |
|-------|-------|
| **Canonical meaning** | Long vol = P&L increases when implied vol rises. Short vol = P&L increases when implied vol falls. |
| **Alternate meaning** | None |
| **Forbidden usage** | "Long vol" combined with "loses when vol rises" |
| **Default interpretation** | P&L direction with respect to implied volatility |
| **Required qualifier** | None |
| **Correct example** | "The desk is short vol — it profits from volatility compression." |
| **Incorrect example** | "The investor is long vol. Their position loses when vol spikes." |
| **Linter rule** | `LNT-GRK-01`: Flag "long vol" + "lose/harm/hurt" + "vol rise/spike/increase" in same paragraph |

### T-GRK-02: Long Gamma / Short Gamma

| Field | Value |
|-------|-------|
| **Canonical meaning** | Long gamma = benefits from large moves in either direction. Short gamma = harmed by large moves. |
| **Alternate meaning** | None |
| **Forbidden usage** | Conflating short gamma with short delta |
| **Default interpretation** | Convexity/concavity of P&L |
| **Required qualifier** | None |
| **Correct example** | "The desk is short gamma near the barrier — a large move in either direction hurts." |
| **Incorrect example** | "Short gamma means the position loses when the stock drops." — this describes short delta |
| **Linter rule** | `LNT-GRK-02`: Flag "short gamma" + "stock drops/falls" without mentioning "either direction" or "large move" |

### T-GRK-03: Sign Convention for Short Option Greeks

| Field | Value |
|-------|-------|
| **Canonical meaning** | Position Greeks for a short option flip signs from the long option Greeks |
| **Alternate meaning** | The V1.0 Desk Bible uses per-option Greeks scaled by quantity without sign flip (non-standard but internally consistent) |
| **Forbidden usage** | Mixing conventions within the same worked example |
| **Default interpretation** | Standard Black-Scholes (position delta for short put is positive) |
| **Required qualifier** | If using the non-standard convention, add footnote explaining the approach |
| **Correct example** | "100 short puts: position delta = +50 (standard convention)" or "100 short puts: delta shown as −50 (per-option, pre-sign-flip)" with footnote |
| **Incorrect example** | "Delta = −50 for the short put position" without footnote |
| **Linter rule** | `LNT-GRK-03`: Flag "short put" + "delta = −" or "short call" + "delta = +" without footnote or convention note |

### T-GRK-04: Gamma × ΔS Sign

| Field | Value |
|-------|-------|
| **Canonical meaning** | When computing new delta after a stock move, Gamma × ΔS must include the sign of ΔS |
| **Alternate meaning** | None |
| **Forbidden usage** | Writing Gamma × |ΔS| (dropping the sign) and getting an intermediate result that contradicts the final answer |
| **Default interpretation** | ΔS includes its sign |
| **Required qualifier** | None |
| **Correct example** | "New Delta ≈ −50 + (3 × (−2)) = −56" |
| **Incorrect example** | "New Delta ≈ −50 + (3 × 2) = −56" — intermediate step is wrong |
| **Linter rule** | `LNT-GRK-04`: Flag "× 2)" or "× 3)" etc. in gamma calculations where the stock "dropped" or "fell" — the multiplied value should be negative |

---

## PART 4 — PRODUCT STRUCTURE TERMS

### T-STR-01: Strike

| Field | Value |
|-------|-------|
| **Canonical meaning** | The price/level at which the embedded option is exercised. Determines payoff at maturity. |
| **Alternate meaning** | None |
| **Forbidden usage** | Using "strike" to mean "barrier" or vice versa |
| **Default interpretation** | Maturity payoff reference level |
| **Required qualifier** | Must be numerically defined in every worked example terms table |
| **Correct example** | "Strike: 100% of initial. At maturity, if worst-of is below strike, physical delivery applies." |
| **Incorrect example** | "If the stock hits the strike during the life of the product" — this describes a barrier |
| **Linter rule** | `LNT-STR-01`: Flag "hit the strike" or "breach the strike" (likely means barrier) |

### T-STR-02: Barrier

| Field | Value |
|-------|-------|
| **Canonical meaning** | The price/level that activates (knock-in) or deactivates (knock-out) the option during the product's life |
| **Alternate meaning** | None |
| **Forbidden usage** | Using "barrier" and "strike" interchangeably |
| **Default interpretation** | During-life observation level |
| **Required qualifier** | Must specify knock-in vs knock-out; continuous vs discrete; percentage of initial |
| **Correct example** | "Knock-in barrier: 60% of initial, continuous observation." |
| **Incorrect example** | "Barrier: 100%. If at maturity the stock is below the barrier, investor receives shares." — this describes a strike |
| **Linter rule** | `LNT-STR-02`: Flag "barrier" + "at maturity" without explicit knock-in/knock-out context |

### T-STR-03: Autocall Level

| Field | Value |
|-------|-------|
| **Canonical meaning** | The level at which the product is automatically redeemed early |
| **Alternate meaning** | "Trigger level," "redemption level," "call level" |
| **Forbidden usage** | Confusing autocall level with strike or barrier |
| **Default interpretation** | Early redemption threshold |
| **Required qualifier** | Must specify percentage and observation frequency |
| **Correct example** | "Autocall level: 100% of initial, observed quarterly." |
| **Incorrect example** | "If the stock hits the strike, the product autocalls." — conflates strike and autocall level |
| **Linter rule** | `LNT-STR-03`: Flag "autocall" + "strike" without clear separation |

### T-STR-04: Reference Level vs Final Level

| Field | Value |
|-------|-------|
| **Canonical meaning** | Reference level = initial fixing. Final level = closing price at maturity/observation date. |
| **Alternate meaning** | None |
| **Forbidden usage** | Using "reference level" for the final observation |
| **Default interpretation** | Reference = initial; final = maturity |
| **Required qualifier** | None if context is clear |
| **Correct example** | "Final level / reference level = 65%. Below strike (100%), physical delivery applies." |
| **Incorrect example** | "The reference level at maturity was 65%." — "reference level" typically means initial |
| **Linter rule** | `LNT-STR-04`: Flag "reference level" + "at maturity" |

---

## PART 5 — PRICING AND MARKET CONVENTION TERMS

### T-MKT-01: Clean Price / Dirty Price

| Field | Value |
|-------|-------|
| **Canonical meaning** | Clean = excludes accrued interest (quotation). Dirty = includes accrued interest (settlement). |
| **Alternate meaning** | None |
| **Forbidden usage** | Using "price" without specifying clean or dirty when accrued interest matters |
| **Default interpretation** | Quoted prices are clean unless stated otherwise |
| **Required qualifier** | "clean" or "dirty" when the distinction matters for a calculation |
| **Correct example** | "The bond trades at 98 (clean). Settlement price: 98 + 1.25 accrued = 99.25 (dirty)." |
| **Incorrect example** | "The bond is worth 98." — clean or dirty? |
| **Linter rule** | `LNT-MKT-01`: Flag bond price references without "clean" or "dirty" in settlement/pricing context |

### T-MKT-02: Payer / Receiver

| Field | Value |
|-------|-------|
| **Canonical meaning** | Payer = pays fixed, receives floating. Receiver = receives fixed, pays floating. |
| **Alternate meaning** | None |
| **Forbidden usage** | "Payer" meaning "pays floating" |
| **Default interpretation** | Always refers to the fixed leg |
| **Required qualifier** | None |
| **Correct example** | "Enter a payer swap: pay 3.5% fixed, receive SOFR floating." |
| **Incorrect example** | "The payer receives the fixed rate." |
| **Linter rule** | `LNT-MKT-02`: Flag "payer" + "receives fixed" or "receiver" + "pays fixed" |

### T-MKT-03: Day Count Convention

| Field | Value |
|-------|-------|
| **Canonical meaning** | Method for counting days in interest calculations (Act/360, Act/365, 30/360, Act/Act) |
| **Alternate meaning** | None |
| **Forbidden usage** | Inconsistent day count within the same worked example without explanation |
| **Default interpretation** | Must be stated explicitly in every worked example |
| **Required qualifier** | Name the convention (e.g., "Act/360") |
| **Correct example** | "Coupon = Notional × Rate × Days/360 (Act/360 convention)." |
| **Incorrect example** | "Coupon = $60M × 5.4% × 90/365" — mixing Act/365 when the product uses Act/360 |
| **Linter rule** | `LNT-MKT-03`: Flag interest calculations where the denominator (360/365/actual) is not labeled |

---

## PART 6 — INFRASTRUCTURE AND VALUATION TERMS

### T-INF-01: ISDA

| Field | Value |
|-------|-------|
| **Canonical meaning** | International Swaps and Derivatives Association. Refers to the ISDA Master Agreement governing OTC derivatives. |
| **Alternate meaning** | ISDA as an organization vs. ISDA as shorthand for "the Master Agreement" |
| **Forbidden usage** | "ISDA" as a verb or adjective without specifying what it qualifies |
| **Default interpretation** | The ISDA Master Agreement |
| **Required qualifier** | "ISDA Master Agreement" on first use; "ISDA" thereafter |
| **Linter rule** | `LNT-INF-01`: S4 — flag first use of "ISDA" without full expansion |

### T-INF-02: CSA

| Field | Value |
|-------|-------|
| **Canonical meaning** | Credit Support Annex — the collateral agreement under ISDA |
| **Alternate meaning** | None |
| **Forbidden usage** | Confusing CSA with the ISDA Master Agreement itself |
| **Default interpretation** | Collateral terms |
| **Required qualifier** | Specify which CSA terms (VM, IM, threshold, MTA) when relevant |
| **Linter rule** | `LNT-INF-02`: S4 — flag "CSA" without full expansion on first use |

### T-INF-03: XVA Family (CVA, DVA, FVA, ColVA, MVA, KVA)

| Field | Value |
|-------|-------|
| **Canonical meaning** | CVA = Credit Valuation Adjustment (counterparty credit risk). DVA = Debit VA (own credit). FVA = Funding VA. ColVA = Collateral VA. MVA = Margin VA. KVA = Capital VA. |
| **Alternate meaning** | None |
| **Forbidden usage** | Using XVA terms interchangeably or without defining what risk each captures |
| **Default interpretation** | Each is a distinct adjustment to the risk-free price |
| **Required qualifier** | Define on first use in any artifact |
| **Linter rule** | `LNT-INF-03`: S4 — flag XVA acronym without expansion on first use |

### T-INF-04: SA-CCR / EAD / PFE

| Field | Value |
|-------|-------|
| **Canonical meaning** | SA-CCR = Standardised Approach for Counterparty Credit Risk. EAD = Exposure at Default. PFE = Potential Future Exposure. |
| **Alternate meaning** | None |
| **Forbidden usage** | Confusing EAD (regulatory) with PFE (risk management) |
| **Default interpretation** | Regulatory capital context |
| **Required qualifier** | Specify regulatory framework (Basel III/IV) when relevant |
| **Linter rule** | `LNT-INF-04`: S4 — flag EAD/PFE without regulatory context |

### T-INF-05: FTP / IPV / Reserves

| Field | Value |
|-------|-------|
| **Canonical meaning** | FTP = Funds Transfer Pricing (internal cost of funding). IPV = Independent Price Verification. Reserves = adjustments to model prices for uncertainty. |
| **Alternate meaning** | None |
| **Forbidden usage** | Confusing reserves (prudential adjustments) with provisions (accounting) |
| **Default interpretation** | Trading desk / risk management context |
| **Required qualifier** | None |
| **Linter rule** | `LNT-INF-05`: S4 — flag "reserves" + "accounting" without distinguishing from trading reserves |

### T-INF-06: RAROC

| Field | Value |
|-------|-------|
| **Canonical meaning** | Risk-Adjusted Return on Capital = (Revenue − Expected Loss − Costs) / Economic Capital |
| **Alternate meaning** | RORAC (Return on Risk-Adjusted Capital) uses different denominator |
| **Forbidden usage** | Confusing RAROC with RORAC or simple ROE |
| **Default interpretation** | RAROC as defined above |
| **Required qualifier** | Specify formula when used in calculations |
| **Linter rule** | `LNT-INF-06`: S4 — flag RAROC/RORAC used interchangeably |

---

## PART 7 — GOVERNANCE RULE SUMMARY TABLE

| Rule ID | Term | Severity | Protects Against |
|:-------:|------|:--------:|-----------------|
| T-COR-01 | Long correlation | S1 | Self-contradictory direction |
| T-COR-02 | Short correlation | S1 | Self-contradictory direction |
| T-COR-03 | Structural correlation | S2 | Convention ambiguity |
| T-COR-04 | Raw position | S2 | Raw/hedged ambiguity |
| T-COR-05 | Hedged position | S2 | Raw/hedged ambiguity |
| T-COR-06 | FTD direction | S1 | Known defect class (E-01) |
| T-COR-07 | NTD direction | S1 | Known defect class (E-09) |
| T-COR-08 | Worst-of direction | S1 | Known defect class (E-02, E-08) |
| T-COR-09 | Dispersion direction | S1 | Known defect class (E-06) |
| T-COR-10 | Correlation reversal | S2 | Misleading NTD table labels |
| T-PRO-01 | Protection seller | S1 | Known defect class (E-03) |
| T-PRO-02 | Protection buyer | S1 | Ownership misattribution |
| T-PRO-03 | Embedded put | S1 | Known defect class (E-03) |
| T-GRK-01 | Long/short vol | S2 | Direction contradiction |
| T-GRK-02 | Long/short gamma | S2 | Gamma/delta conflation |
| T-GRK-03 | Short option signs | S3 | Sign convention confusion |
| T-GRK-04 | Gamma × ΔS | S1 | Known defect class (E-07) |
| T-STR-01 | Strike | S2 | Strike/barrier confusion |
| T-STR-02 | Barrier | S2 | Strike/barrier confusion |
| T-STR-03 | Autocall level | S3 | Autocall/strike conflation |
| T-STR-04 | Reference level | S3 | Initial/final confusion |
| T-MKT-01 | Clean/dirty price | S3 | Price ambiguity |
| T-MKT-02 | Payer/receiver | S2 | Direction error |
| T-MKT-03 | Day count | S3 | Calculation inconsistency |
| T-INF-01 | ISDA | S4 | Acronym ambiguity |
| T-INF-02 | CSA | S4 | Acronym ambiguity |
| T-INF-03 | XVA family | S4 | Acronym conflation |
| T-INF-04 | SA-CCR/EAD/PFE | S4 | Regulatory term confusion |
| T-INF-05 | FTP/IPV/Reserves | S4 | Term conflation |
| T-INF-06 | RAROC | S4 | Metric confusion |

---

*Terminology Governance Specification | V1.0.1-GOV-1.0 | 2026-06-27*
