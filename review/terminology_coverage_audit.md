# Terminology Coverage Audit

## Desk Bible v2 -- Term-by-Term Classification

**Classification criteria for "Fully Explained"**: (1) defined, (2) explained in plain English, (3) practical usage shown, (4) trade implications discussed, (5) common mistakes noted, (6) cross-referenced to related terms, (7) appears in worked examples. A term meeting all 7 = Fully Explained. Meeting 3-6 = Partially Explained. Appearing with some context but fewer than 3 criteria = Mentioned Only. Zero mentions = Missing.

---

## Phase 1: Termsheet Dates

| Term | Mentions | Classification | Notes |
|------|----------|---------------|-------|
| Trade Date | 80 | Partially Explained | Used consistently across products; defined in context but no dedicated date taxonomy section |
| Booking Date | 0 | Missing | Never appears in manuscript |
| Effective Date | 16 | Mentioned Only | Appears in lifecycle descriptions but not defined or distinguished from Trade Date |
| Settlement Date | 7 | Mentioned Only | Referenced but no settlement date determination rules |
| Issue Date | 17 | Mentioned Only | Used in ELN/note contexts; not explained as distinct from Trade/Effective Date |
| Maturity Date | 2 | Mentioned Only | Surprisingly low frequency; implied by "maturity" references but rarely as exact term |
| Exercise Date | 4 | Mentioned Only | Appears in options context; no detailed exercise notification/mechanics |
| Observation Date | 129 | Partially Explained | Well covered in barrier/autocall contexts; defined in product-specific terms |
| Valuation Date | 0 | Missing | Never appears; critical for settlement amount determination |
| Determination Date | 0 | Missing | Never appears; important for coupon/barrier calculations |
| Fixing Date | 6 | Mentioned Only | Appears in rate-linked products; no fixing source/fallback explanation |
| Reset Date | 5 | Mentioned Only | Used in swap contexts; no reset mechanics detail |
| Roll Date | 0 | Missing | Never appears; important for CDS/index products |
| Payment Date | 33 | Partially Explained | Appears regularly; linked to coupon/settlement but no business day adjustment rules |

**Phase 1 Dates Summary**: 0 Fully Explained, 3 Partially Explained, 7 Mentioned Only, 4 Missing

---

## Phase 1: Economics Terms

| Term | Mentions | Classification | Notes |
|------|----------|---------------|-------|
| Notional | 336 | Fully Explained | Defined, used in examples, cross-referenced, common mistakes noted |
| Issue Price | 17 | Partially Explained | Defined for notes; no clean/dirty distinction |
| Clean Price | 0 | Missing | Never appears; critical for secondary market trading |
| Dirty Price | 0 | Missing | Never appears; critical for accrued interest calculations |
| Premium | 539 | Fully Explained | Extensively covered across options, CDS, structured products |
| Redemption Amount | 10 | Partially Explained | Defined in payoff contexts; no full redemption mechanics |
| Participation Rate | 85 | Fully Explained | Defined, explained with scenarios, practical implications, cross-referenced |
| Memory Coupon | 7 | Partially Explained | Defined in autocall context; limited worked examples |
| Contingent Coupon | 7 | Partially Explained | Defined in autocall context; limited worked examples |
| Guaranteed Coupon | 4 | Mentioned Only | Referenced but minimal explanation |
| Range Accrual | 121 | Fully Explained | Dedicated product chapter with full 22-section treatment |
| Step-Up | 3 | Mentioned Only | Referenced in coupon structures; no detailed mechanics |
| Step-Down | 8 | Mentioned Only | Referenced in coupon/barrier contexts; no detailed mechanics |
| Digital Coupon | 115 | Fully Explained | Extensive coverage in digital product chapters |
| Snowball Coupon | 3 | Mentioned Only | Named but not explained with worked examples |
| Strike | 399 | Fully Explained | Core concept, exhaustively covered across all relevant products |
| Forward Strike | 0 | Missing | Never appears; relevant for forward-starting products |
| Trigger | 273 | Fully Explained | Extensively covered in autocall/barrier products |
| Cap | 1055 | Fully Explained | Highest frequency term; thoroughly covered |
| Floor | 169 | Fully Explained | Well covered across rate and equity products |
| Buffer | 11 | Partially Explained | Defined in buffered note contexts; limited depth |
| Bonus Level | 20 | Partially Explained | Defined in bonus certificate contexts |
| Autocall Level | 5 | Mentioned Only | Surprisingly low as standalone term; concept covered via "autocall" and "trigger" terms |

**Phase 1 Economics Summary**: 8 Fully Explained, 6 Partially Explained, 5 Mentioned Only, 3 Missing

---

## Phase 2: Market Conventions

| Term | Mentions | Classification | Notes |
|------|----------|---------------|-------|
| Modified Following | 0 | Missing | Most common business day convention in derivatives -- completely absent |
| Following | 0 | Missing | Not covered as a business day convention |
| Preceding | 0 | Missing | Not covered |
| ACT/360 | 21 | Mentioned Only | Used in worked examples as a day count fraction (e.g., Notional x Spread x ACT/360) but NEVER explained as a convention. Reader sees the formula but cannot explain what ACT/360 means or when to use it |
| ACT/365 | 0 | Missing | Not covered |
| ACT/ACT | 0 | Missing | Not covered |
| 30/360 | 14 | Mentioned Only | Same pattern as ACT/360 -- appears in calculations, never explained |
| 30E/360 | 0 | Missing | Not covered |
| Trading Calendar | 0 | Missing | Not covered |
| Settlement Calendar | 0 | Missing | Not covered |
| Business Calendar | 0 | Missing | Not covered |
| Joint Calendar | 0 | Missing | Not covered (relevant for cross-currency products) |
| TARGET Calendar | 0 | Missing | Not covered (EUR settlement) |
| Cash Settlement | 17 | Partially Explained | Defined per product; mechanics understood in context |
| Physical Settlement | 5 | Mentioned Only | Referenced; less detail than cash settlement |
| Physical Delivery | 44 | Partially Explained | Better covered than "physical settlement"; delivery mechanics described |
| T+2 | 28 | Partially Explained | Referenced as standard; no explanation of why T+2 or when T+1/T+3 applies |
| T+3 | 5 | Mentioned Only | Referenced for some markets; no comparison framework |
| European Exercise | 92 | Fully Explained | Well covered in options foundations and per-product chapters |
| American Exercise | 62 | Fully Explained | Well covered alongside European |
| Bermudan Exercise | 35 | Partially Explained | Defined and used; less depth than European/American |
| Continuous Observation | 4 | Mentioned Only | Referenced in barrier contexts; not explained as convention |
| Daily Observation | 39 | Partially Explained | Used in barrier/range accrual contexts; convention described |
| Business Day Convention | 30 (combined) | Mentioned Only | The phrase appears but the conventions themselves (Modified Following, etc.) are not defined or explained |

**Phase 2 Summary**: 2 Fully Explained, 5 Partially Explained, 6 Mentioned Only, 11 Missing

---

## Phase 3: Documentation & Legal

| Term | Mentions | Classification | Notes |
|------|----------|---------------|-------|
| ISDA Master Agreement | 173 | Partially Explained | Extensively referenced; function understood; Schedule mechanics not covered |
| ISDA Schedule | 0 | Missing | The negotiated elections document -- not covered |
| ISDA Definitions | 0 | Missing | 2006 ISDA Definitions, 2021 ISDA Definitions -- not distinguished |
| Credit Support Annex (CSA) | 54 | Mentioned Only | Referenced frequently but CSA mechanics (thresholds, MTA, eligible collateral) absent |
| Confirmation | ~30 (est.) | Partially Explained | Referenced in trade lifecycle; no confirmation anatomy |
| Termsheet | ~50 (est.) | Partially Explained | Referenced as document; no "how to read" guide |
| PRIIPs KID | 2 | Mentioned Only | Named; no KID structure or content explanation |
| MiFID Suitability | 5 | Mentioned Only | Named; no practical compliance process |
| Novation | ~5 (est.) | Mentioned Only | Referenced as lifecycle event; no documentation detail |
| Assignment | ~3 (est.) | Mentioned Only | Referenced; no legal mechanics |

**Phase 3 Summary**: 0 Fully Explained, 3 Partially Explained, 5 Mentioned Only, 2 Missing

---

## Phase 4: Collateral & Margin

| Term | Mentions | Classification | Notes |
|------|----------|---------------|-------|
| Initial Margin (IM) | 1 | Mentioned Only | Single mention; no methodology |
| Variation Margin (VM) | 1 | Mentioned Only | Single mention; no methodology |
| Threshold | 0 | Missing | CSA threshold -- not covered |
| Minimum Transfer Amount (MTA) | 0 | Missing | Not covered |
| Independent Amount | 0 | Missing | Not covered |
| Haircut | 0 | Missing | Collateral haircuts -- not covered |
| Eligible Collateral | 0 | Missing | Not covered |
| Margin Call | 0 | Missing | Not covered |
| Credit Support Amount | 0 | Missing | Not covered |
| Exposure | ~20 (est.) | Partially Explained | Used in risk context; not in collateral context |

**Phase 4 Summary**: 0 Fully Explained, 1 Partially Explained, 2 Mentioned Only, 7 Missing

---

## Phase 5: Valuation & Pricing

| Term | Mentions | Classification | Notes |
|------|----------|---------------|-------|
| Yield Curve | 86 | Partially Explained | Concept covered in foundations; no curve construction methodology |
| Discount Curve | ~10 (est.) | Mentioned Only | Referenced; no construction detail |
| Forward Curve | ~15 (est.) | Mentioned Only | Referenced; no derivation |
| Vol Surface | 25 | Partially Explained | Concept covered; no surface construction or parameterisation |
| Credit Spread | 43 | Partially Explained | Used as pricing input; no term structure detail |
| Correlation | ~100 (est.) | Partially Explained | Part 1 correlation chapter; no correlation surface/matrix methodology |
| Monte Carlo | 30 | Partially Explained | Concept described; no implementation detail |
| Black-Scholes | 18 | Partially Explained | Framework referenced; no derivation or limitations depth |
| Risk-Neutral Pricing | ~5 (est.) | Mentioned Only | Concept referenced; not explained |
| Calibration | ~8 (est.) | Mentioned Only | Referenced in model context; no methodology |

**Phase 5 Summary**: 0 Fully Explained, 6 Partially Explained, 4 Mentioned Only, 0 Missing

---

## Phase 6: Product Control & IPV

| Term | Mentions | Classification | Notes |
|------|----------|---------------|-------|
| Product Control | 118 | Partially Explained | Function well referenced; methodology absent |
| P&L Explain | 0 | Missing | Core product control function -- completely absent |
| P&L Attribution | 0 | Missing | Not covered |
| Flash P&L | 0 | Missing | Not covered |
| Official P&L | 0 | Missing | Not covered |
| IPV | 24 | Mentioned Only | Function referenced; no methodology |
| Fair Value Hierarchy | 0 | Missing | ASC 820/IFRS 13 -- not covered |
| Level 1 / Level 2 / Level 3 | 0 | Missing | Fair value levels -- not covered |
| Consensus Pricing | 0 | Missing | Totem/Markit consensus -- not covered |
| Bid-Offer | ~15 (est.) | Mentioned Only | Referenced in trading context; not in control context |

**Phase 6 Summary**: 0 Fully Explained, 1 Partially Explained, 3 Mentioned Only, 6 Missing

---

## Phase 7: Reserves & XVA

| Term | Mentions | Classification | Notes |
|------|----------|---------------|-------|
| Model Reserve | 1 | Mentioned Only | Single passing reference |
| Bid-Offer Reserve | 0 | Missing | Not covered |
| Liquidity Reserve | 0 | Missing | Not covered |
| Credit Reserve | 0 | Missing | Not covered |
| Day-One P&L Reserve | 0 | Missing | Not covered |
| CVA | 2 | Mentioned Only | Word-level matches; no explanation |
| DVA | 1 | Mentioned Only | Single mention |
| FVA | 0 | Missing | Not covered |
| ColVA | 0 | Missing | Not covered |
| MVA | 0 | Missing | Not covered |
| KVA | 0 | Missing | Not covered |

**Phase 7 Summary**: 0 Fully Explained, 0 Partially Explained, 3 Mentioned Only, 8 Missing

---

## Phase 8: Capital & Regulatory

| Term | Mentions | Classification | Notes |
|------|----------|---------------|-------|
| Regulatory Capital | 11 | Mentioned Only | Named; no calculation methodology |
| RWA | 0 | Missing | Risk-Weighted Assets -- not covered |
| SA-CCR | 0 | Missing | Standardised Approach for Counterparty Credit Risk -- not covered |
| EAD | 0 | Missing | Exposure at Default -- not covered |
| PFE | 0 | Missing | Potential Future Exposure -- not covered |
| Basel III/IV | 31 | Mentioned Only | Framework named; no product-level capital impact |
| Leverage Ratio | 0 | Missing | Not covered |
| FRTB | 0 | Missing | Fundamental Review of the Trading Book -- not covered |
| MiFID II | 5 | Mentioned Only | Named; no operational requirements |
| PRIIPs | 2 | Mentioned Only | Named; no KID construction methodology |
| EMIR | 0 | Missing | Not covered |
| Dodd-Frank | 0 | Missing | Not covered |
| UMR | 0 | Missing | Uncleared Margin Rules -- not covered |

**Phase 8 Summary**: 0 Fully Explained, 0 Partially Explained, 4 Mentioned Only, 9 Missing

---

## Phase 9: Operations & Settlement

| Term | Mentions | Classification | Notes |
|------|----------|---------------|-------|
| STP | 0 | Missing | Straight-Through Processing -- not covered |
| Cash Reconciliation | 0 | Missing | Not covered |
| Static Data | 0 | Missing | Not covered |
| Golden Source | 0 | Missing | Not covered |
| SSI | 0 | Missing | Standard Settlement Instructions -- not covered |
| Nostro | 0 | Missing | Not covered |
| CLS | 0 | Missing | Continuous Linked Settlement -- not covered |
| DTCC | 0 | Missing | Not covered |
| Euroclear | 0 | Missing | Not covered |
| Clearstream | 0 | Missing | Not covered |
| Netting | ~5 (est.) | Mentioned Only | Referenced in ISDA context; no close-out netting detail |

**Phase 9 Summary**: 0 Fully Explained, 0 Partially Explained, 1 Mentioned Only, 10 Missing

---

## Phase 10: Corporate Actions & Events

| Term | Mentions | Classification | Notes |
|------|----------|---------------|-------|
| Stock Split | 12 | Partially Explained | Mentioned as adjustment trigger with some context |
| Merger | 6 | Mentioned Only | Referenced as event; no adjustment methodology |
| Reverse Split | 0 | Missing | Not covered |
| Rights Issue | 0 | Missing | Not covered |
| Special Dividend | 0 | Missing | Not covered |
| Delisting | ~3 (est.) | Mentioned Only | Referenced as disruption event |
| Nationalisation | ~2 (est.) | Mentioned Only | Referenced as extraordinary event |
| Calculation Agent | ~10 (est.) | Mentioned Only | Role referenced; no determination methodology |
| Disruption Event | ~8 (est.) | Mentioned Only | Referenced; no ISDA disruption event taxonomy |

**Phase 10 Summary**: 0 Fully Explained, 1 Partially Explained, 4 Mentioned Only, 4 Missing

---

## Phase 11: Model Risk & Quantitative

| Term | Mentions | Classification | Notes |
|------|----------|---------------|-------|
| Model Validation | 24 | Mentioned Only | Function referenced; no validation methodology |
| Model Risk | 33 | Partially Explained | Acknowledged per product; no framework |
| Challenger Model | 0 | Missing | Not covered |
| Benchmark Testing | 0 | Missing | Not covered |
| Backtesting | 0 | Missing | Not covered |
| Model Inventory | 0 | Missing | Not covered |
| Model Tiering | 0 | Missing | Not covered |
| SABR | 0 | Missing | Not covered |
| Heston | 0 | Missing | Not covered |
| Hull-White | 0 | Missing | Not covered |
| Local Volatility | 0 | Missing | Not covered |
| PDE Methods | 0 | Missing | Not covered |
| Finite Difference | 0 | Missing | Not covered |

**Phase 11 Summary**: 0 Fully Explained, 1 Partially Explained, 1 Mentioned Only, 11 Missing

---

## Grand Summary

| Phase | Fully | Partially | Mentioned Only | Missing | Total Terms |
|-------|-------|-----------|----------------|---------|-------------|
| 1 -- Dates | 0 | 3 | 7 | 4 | 14 |
| 1 -- Economics | 8 | 6 | 5 | 3 | 22 |
| 2 -- Conventions | 2 | 5 | 6 | 11 | 24 |
| 3 -- Documentation | 0 | 3 | 5 | 2 | 10 |
| 4 -- Collateral | 0 | 1 | 2 | 7 | 10 |
| 5 -- Valuation | 0 | 6 | 4 | 0 | 10 |
| 6 -- Product Control | 0 | 1 | 3 | 6 | 10 |
| 7 -- Reserves & XVA | 0 | 0 | 3 | 8 | 11 |
| 8 -- Capital & Reg | 0 | 0 | 4 | 9 | 13 |
| 9 -- Operations | 0 | 0 | 1 | 10 | 11 |
| 10 -- Corporate Actions | 0 | 1 | 4 | 4 | 9 |
| 11 -- Model Risk & Quant | 0 | 1 | 1 | 11 | 13 |
| **TOTAL** | **10** | **27** | **45** | **75** | **157** |

**Distribution**: 6.4% Fully Explained, 17.2% Partially Explained, 28.7% Mentioned Only, 47.8% Missing.

**Interpretation**: The manuscript fully explains its core product economics terminology (Strike, Cap, Premium, Notional, Participation Rate, Trigger, Range Accrual, Digital Coupon) but has near-total gaps in operational, regulatory, and infrastructure terminology. The 47.8% Missing rate reflects the manuscript's design as a product knowledge bible rather than an operational desk reference -- it was never scoped to cover these domains, but anyone relying on it as a sole reference would have blind spots in roughly half the terminology a structured products professional encounters daily.
