# AMBIGUOUS TERMS POLICY

**Ecosystem:** Structured Products Knowledge Ecosystem  
**Version:** V1.0.1-GOV-1.0  
**Effective:** 2026-06-27  
**Purpose:** Policy for handling terms that are inherently ambiguous in structured products practice.

---

## Policy Structure

For each ambiguous term class:
- **Default interpretation** — what readers assume when no qualifier appears
- **Required qualifier** — what must be added for alternate meaning
- **Alternate allowed in** — where the non-default meaning is permitted
- **Same-chapter rule** — what happens when both meanings appear in one chapter
- **Footnote requirement** — whether the alternate must be footnoted
- **Table usage** — whether the alternate can appear in tables
- **Interview answer usage** — whether the alternate can appear in interview prep

---

## AMB-01: Correlation (Long / Short)

| Field | Value |
|-------|-------|
| **Default** | MTM sensitivity: long = benefits from ρ rising |
| **Required qualifier** | "structurally" for premium-direction meaning |
| **Alternate allowed in** | Any artifact, but only with qualifier |
| **Same-chapter rule** | Both may appear in the same chapter. Each sentence must be internally consistent. The chapter should explain the two conventions if both are used. |
| **Footnote** | Not required if "structurally" is used. Recommended on first use of dual-convention discussion. |
| **Tables** | Tables must use canonical (MTM) unless the column header specifies "structural." |
| **Interview answers** | Must use MTM unless the question explicitly asks about structural convention. The answer should mention both conventions for completeness. |

---

## AMB-02: Protection (Buyer / Seller)

| Field | Value |
|-------|-------|
| **Default** | In structured notes: investor = seller, desk = buyer. In standalone CDS: either party can be buyer or seller. |
| **Required qualifier** | Specify "in the structured note" or "via CDS" when context is ambiguous |
| **Alternate allowed in** | CDS-specific discussions only |
| **Same-chapter rule** | If the chapter discusses both structured notes and CDS, explicitly state which context applies before each protection reference. |
| **Footnote** | Not required if context is unambiguous. |
| **Tables** | Must specify the structure (RC/CLN/CDS) in the row/column header. |
| **Interview answers** | Must specify the product context. "In an RC, the investor sells protection." |

---

## AMB-03: Spread

| Field | Value |
|-------|-------|
| **Default** | Context-dependent: credit spread (CDS/bond), bid-ask spread (market-making), option spread (strategy). No single default. |
| **Required qualifier** | Always specify: "credit spread," "bid-ask spread," "option spread," or "swap spread" |
| **Alternate allowed in** | N/A — all meanings are valid; disambiguation is always required |
| **Same-chapter rule** | If multiple spread types appear, define each on first use. |
| **Footnote** | Not required if qualified. |
| **Tables** | Column header must specify type. |
| **Interview answers** | Always qualify. "The credit spread widened to 200bp." |

---

## AMB-04: Risk

| Field | Value |
|-------|-------|
| **Default** | Context-dependent: market risk, credit risk, operational risk, counterparty risk, model risk, liquidity risk. |
| **Required qualifier** | Specify the risk type when used in a context where multiple types could apply |
| **Alternate allowed in** | "Risk" without qualifier is acceptable in general statements ("higher risk") where the type is evident from context |
| **Same-chapter rule** | If multiple risk types are discussed, qualify each reference. |
| **Footnote** | Not required. |
| **Tables** | Column header should specify risk type. |
| **Interview answers** | Must qualify on first mention. |

---

## AMB-05: Premium

| Field | Value |
|-------|-------|
| **Default** | Context-dependent: option premium (price paid), credit premium (CDS spread), correlation premium (embedded), risk premium (compensation for bearing risk). |
| **Required qualifier** | Specify the premium type when ambiguity exists |
| **Alternate allowed in** | All artifacts with qualifier |
| **Same-chapter rule** | Define on first use if multiple premium types appear. |
| **Footnote** | Not required. |
| **Tables** | Specify in header. |
| **Interview answers** | Qualify: "The correlation premium embedded in the worst-of coupon." |

---

## AMB-06: Yield

| Field | Value |
|-------|-------|
| **Default** | Return metric. Context determines type: YTM, current yield, option-adjusted yield, spread yield. |
| **Required qualifier** | Specify the yield metric in any calculation |
| **Alternate allowed in** | General discussion can use "yield" unqualified if only one metric is relevant |
| **Same-chapter rule** | If multiple yield metrics are discussed, qualify each. |
| **Footnote** | Not required. |
| **Tables** | Specify metric in header: "YTM," "Current Yield." |
| **Interview answers** | Qualify the metric. |

---

## AMB-07: Strike / Barrier

| Field | Value |
|-------|-------|
| **Default** | Strike = maturity payoff reference. Barrier = during-life observation trigger. |
| **Required qualifier** | Both must be defined separately in every worked example. Never use interchangeably. |
| **Alternate allowed in** | No alternate — these are distinct concepts |
| **Same-chapter rule** | Both must be numerically defined in the terms table. |
| **Footnote** | Not required. |
| **Tables** | Separate rows for strike and barrier in every terms table. |
| **Interview answers** | Must distinguish: "The barrier is 60%, the strike is 100%." |

---

## AMB-08: Fix / Reset

| Field | Value |
|-------|-------|
| **Default** | Fix/reset = the observation event that determines the rate or level for a period. |
| **Required qualifier** | Specify: "fixing date," "reset date," or "observation date" |
| **Alternate allowed in** | "Fix" as a verb ("fix the rate") is acceptable |
| **Same-chapter rule** | Use consistently throughout the chapter. |
| **Footnote** | Not required. |
| **Tables** | Use "fixing date" or "reset date" — not just "fix." |
| **Interview answers** | Use full term: "The SOFR fixing on the reset date." |

---

## AMB-09: Exercise / Settlement / Maturity

| Field | Value |
|-------|-------|
| **Default** | Exercise = when option is activated. Settlement = when cash/securities change hands. Maturity = when the product reaches its end date. |
| **Required qualifier** | Specify when these differ (exercise date ≠ settlement date ≠ maturity date in many products) |
| **Alternate allowed in** | N/A — distinct concepts |
| **Same-chapter rule** | If exercise triggers settlement before maturity, explain the sequence. |
| **Footnote** | Not required unless non-standard settlement applies. |
| **Tables** | List each date separately. |
| **Interview answers** | Distinguish: "The autocall is exercised quarterly, settles T+2, but maturity is 3 years." |

---

## AMB-10: Coupon

| Field | Value |
|-------|-------|
| **Default** | Periodic payment to the investor. In structured notes: enhanced coupon = compensation for embedded risk. |
| **Required qualifier** | Specify: fixed coupon, memory coupon, conditional coupon, accrued coupon |
| **Alternate allowed in** | "Coupon" without qualifier is acceptable when only one type exists in the product |
| **Same-chapter rule** | If memory and conditional coupons coexist, qualify each reference. |
| **Footnote** | Not required. |
| **Tables** | Specify type in column header. |
| **Interview answers** | Qualify the coupon type for complex products. |

---

## AMB-11: Reserve / Hedge

| Field | Value |
|-------|-------|
| **Default** | Reserve = prudential adjustment to model price (trading context). Hedge = offsetting position to manage risk. |
| **Required qualifier** | "Reserve" must specify: model reserve, bid-ask reserve, close-out reserve. "Hedge" must specify: delta hedge, vega hedge, correlation hedge. |
| **Alternate allowed in** | Accounting "provisions" are distinct from trading "reserves" — never conflate. |
| **Same-chapter rule** | If multiple reserve types or hedge types appear, qualify each. |
| **Footnote** | Not required. |
| **Tables** | Specify type. |
| **Interview answers** | Qualify: "The desk's delta hedge" or "the model uncertainty reserve." |

---

## AMB-12: Long / Short (Generic)

| Field | Value |
|-------|-------|
| **Default** | Long = benefits from rising. Short = benefits from falling. |
| **Required qualifier** | Always specify WHAT is long or short: long correlation, long credit, long vol, long gamma, long the put. Never say "long" or "short" in isolation without a noun. |
| **Alternate allowed in** | "Long the stock" (position direction) is universally understood — no qualifier needed |
| **Same-chapter rule** | Every instance of "long" or "short" must specify the risk factor or instrument. |
| **Footnote** | Not required. |
| **Tables** | Column header must specify: "Correlation Direction," not just "Direction." |
| **Interview answers** | Always qualify: "The investor is long correlation, short credit, short vol." |

---

## AMB-13: Investor / Dealer / Desk

| Field | Value |
|-------|-------|
| **Default** | Investor = the end buyer of the structured note. Desk = the structuring/trading desk that creates and hedges the product. Dealer = the legal entity of the desk (interchangeable with desk for governance purposes). |
| **Required qualifier** | Specify when describing positions: "the investor's position" or "the desk's position" |
| **Alternate allowed in** | "Dealer" may be used in place of "desk" in legal/ISDA context |
| **Same-chapter rule** | Pick one term (desk or dealer) per chapter and use it consistently. |
| **Footnote** | Not required. |
| **Tables** | Specify perspective in column header: "Investor Direction" or "Desk Position." |
| **Interview answers** | Always specify: "From the investor's perspective..." |

---

## AMB-14: Raw / Hedged

| Field | Value |
|-------|-------|
| **Default** | If unqualified, assume raw (pre-hedge exposure). |
| **Required qualifier** | "raw/unhedged" or "net/hedged" — mandatory for any desk position where hedging changes direction |
| **Alternate allowed in** | Both meanings appear in every desk-position discussion. Neither is "alternate" — both must be stated. |
| **Same-chapter rule** | If a chapter describes desk positions, both raw and hedged must be discussed and explicitly labeled. |
| **Footnote** | Not required if inline qualifiers are present. |
| **Tables** | Separate rows for raw and hedged positions, or column specifying which. |
| **Interview answers** | Must distinguish: "The desk's raw position is short correlation; after dispersion hedges, the net position is typically long." |

---

## AMB-15: Structural / MTM

| Field | Value |
|-------|-------|
| **Default** | MTM / economic sensitivity is the default convention. |
| **Required qualifier** | "structurally" when using premium-direction convention |
| **Alternate allowed in** | Any artifact with qualifier |
| **Same-chapter rule** | If both conventions are discussed, explain the distinction on first use. Each sentence must be labeled. |
| **Footnote** | Recommended on first dual-convention usage in a chapter. |
| **Tables** | Column header must specify convention: "Direction (MTM)" or "Direction (Structural)." |
| **Interview answers** | Default to MTM. Mention structural for completeness: "Long correlation under MTM convention; structurally short, having sold the premium." |

---

## ENFORCEMENT SUMMARY

| AMB ID | Term | Must Qualify | Footnote | Tables | Interview |
|:------:|------|:----------:|:--------:|:------:|:---------:|
| AMB-01 | Correlation | Yes ("structurally") | Recommended | MTM default | MTM default |
| AMB-02 | Protection | Yes (product context) | No | Specify product | Specify product |
| AMB-03 | Spread | Always | No | Specify type | Always qualify |
| AMB-04 | Risk | When multiple types | No | Specify type | Qualify first mention |
| AMB-05 | Premium | When ambiguous | No | Specify type | Qualify |
| AMB-06 | Yield | In calculations | No | Specify metric | Qualify |
| AMB-07 | Strike/Barrier | Always separate | No | Separate rows | Always distinguish |
| AMB-08 | Fix/Reset | Use full term | No | Full term | Full term |
| AMB-09 | Exercise/Settlement | When they differ | No | List each | Distinguish |
| AMB-10 | Coupon | For complex products | No | Specify type | Qualify for complex |
| AMB-11 | Reserve/Hedge | Always specify type | No | Specify type | Qualify |
| AMB-12 | Long/Short | Always specify noun | No | Specify factor | Always qualify |
| AMB-13 | Investor/Desk | Always specify | No | Specify perspective | Always specify |
| AMB-14 | Raw/Hedged | Mandatory for desk | No | Separate rows | Must distinguish |
| AMB-15 | Structural/MTM | "structurally" | Recommended | Specify convention | MTM default |

---

*Ambiguous Terms Policy | V1.0.1-GOV-1.0 | 2026-06-27*
