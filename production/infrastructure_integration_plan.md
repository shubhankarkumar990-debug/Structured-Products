# Infrastructure Integration Plan

**Date**: 2026-06-25
**Scope**: Desk Bible v2 — Knowledge Domain Remediation
**Trigger**: Comprehensive audit verdict: PASS WITH GAPS (product knowledge 8.3/10, infrastructure 1.6/10)
**Objective**: Transform the Desk Bible from a product knowledge reference into a complete practitioner reference

---

## 1. Architectural Decision

### Decision: Integrate as Part 6 — The Operational Ecosystem

The manuscript's "How to Use" section (line 25) already routes readers to "the operational guide in Part 6." Reading paths (line 33) direct Product Control and Operations through "Part 2 → 6 → 4 → 7." Part 6 was planned from inception but never written.

**Why NOT a separate handbook:**
- Part 6 is already referenced in the table of contents and reading paths
- The educational style, voice, and progression are established — separate documents fragment the learning experience
- Cross-references to Part 1 foundations and Part 5 product chapters are natural within one volume
- The "How to Use" section already tells readers where to find this content

**Why NOT embedded in existing chapters:**
- Infrastructure knowledge is inherently cross-product (P&L Explain applies to all 49 products, not one)
- Framework v1.3.1 freezes the 22-section chapter structure — no new sections can be added to product chapters
- Existing chapters are production-complete and should not be modified for infrastructure content

**Architecture:**
```
Part 0 — How Finance Works          (existing, unchanged)
Part 1 — Foundations                (existing, unchanged)
Part 2 — The SP Framework           (existing, unchanged)
Part 3 — Product Taxonomy            (existing, unchanged)
Part 4 — Product Comparison          (existing, unchanged)
Part 5 — Product Deep Dives          (existing, unchanged)
Part 6 — THE OPERATIONAL ECOSYSTEM   ← NEW (this remediation)
```

---

## 2. Gap Triage — Bucket Classification

### Bucket A — Standalone Educational Topics (New Part 6 Sections)

These gaps require full educational treatment: explanation, context, examples, common mistakes, cross-references. They are cross-product concepts that cannot live inside individual product chapters.

| # | Concept | Audit Finding | Part 6 Section |
|---|---------|--------------|----------------|
| 1 | Business Day Conventions | 0 mentions of "Modified Following" | 6.1 |
| 2 | Day Count Conventions | ACT/360 used but never explained | 6.1 |
| 3 | Settlement Calendars | 0 mentions of settlement/trading calendar | 6.1 |
| 4 | Observation & Exercise Conventions | Continuous/daily mentioned, not systematized | 6.1 |
| 5 | Floating Rate Conventions | Stub periods, broken dates, end-of-month = 0 | 6.1 |
| 6 | Termsheet Field Anatomy | Trade dates used but many never explained | 6.2 |
| 7 | Clean vs Dirty Price | 0 mentions each | 6.2 |
| 8 | ISDA Master Agreement mechanics | 173 mentions, no Schedule/default/netting detail | 6.3 |
| 9 | CSA mechanics | 54 mentions, no threshold/MTA/eligible collateral | 6.3 |
| 10 | Market Disruption Events | 0 mentions | 6.3 |
| 11 | Capital Structure hierarchy | Only basic debt vs equity in Part 0 | 6.4 |
| 12 | CDS Restructuring Clauses (FR/MR/MMR/NR) | All 0 mentions | 6.4 |
| 13 | AT1, CoCos, Bail-in | All 0 mentions | 6.4 |
| 14 | Recovery waterfall | Not taught | 6.4 |
| 15 | Fair Value Hierarchy (Level 1/2/3) | 0/2/1/0 mentions | 6.5 |
| 16 | IPV process | 24 mentions, never explained | 6.5 |
| 17 | Valuation governance | 0 mentions | 6.5 |
| 18 | P&L Explain | 0 mentions — most critical daily PC activity | 6.6 |
| 19 | Reserve framework (all types) | All 0-1 mentions | 6.6 |
| 20 | Day One P&L | Barely mentioned | 6.6 |
| 21 | FTP methodology | 44 mentions, no methodology | 6.7 |
| 22 | XVA framework (CVA/DVA/FVA/ColVA/MVA/KVA) | CVA:2, DVA:1, rest:0 | 6.7 |
| 23 | Capital metrics (RWA/SA-CCR/EAD/PFE) | All 0 word-match | 6.7 |
| 24 | Model validation process | Mentioned but not explained | 6.8 |
| 25 | Model lifecycle & governance | 0 for approval/inventory/backtesting | 6.8 |
| 26 | Booking workflow (cross-product) | Per-product strong, cross-product absent | 6.9 |
| 27 | Static data & golden source | 0 mentions each | 6.9 |
| 28 | Cash reconciliation | 0 mentions | 6.9 |
| 29 | Corporate action adjustment methodology | Stock Split:12, no methodology | 6.9 |
| 30 | Desk vocabulary (flow/exotic book, risk warehouse) | All 0-1 mentions | 6.10 |
| 31 | Greeks positioning language | Used but rarely defined as concepts | 6.10 |
| 32 | Regulatory framework (MiFID II, EMIR, UMR) | MiFID:5, EMIR:0, UMR:0 | 6.11 |

### Bucket B — Integrate Into Existing Sections (Cross-References Only)

These concepts are best taught in Part 6 but need cross-reference pointers noted in Part 6 that connect back to existing Part 1/2/5 content. No modifications to existing chapters (frozen content).

| Concept | Natural Home | Cross-Reference From |
|---------|-------------|---------------------|
| Restructuring clauses impact on CLN settlement | Part 6 §6.4 | References CLN chapters (§5.5.x) |
| Capital structure impact on credit-linked products | Part 6 §6.4 | References Part 1 §1.9 (Credit Risk) |
| Reserve impact on product pricing | Part 6 §6.6 | References Part 2 §2.2 (Product Construction) |
| XVA impact on trade economics | Part 6 §6.7 | References Part 2 §2.2 (coupon formula) |
| Model risk per product family | Part 6 §6.8 | References §15 (Risk Analysis) per chapter |

### Bucket C — Worked Examples (Embedded in Part 6 Sections)

| Example | Section |
|---------|---------|
| Day count calculation: ACT/360 vs 30/360 on same trade | 6.1 |
| Modified Following adjustment on a coupon date | 6.1 |
| Reading a real indicative termsheet field-by-field | 6.2 |
| ISDA confirmation vs termsheet comparison | 6.3 |
| Capital structure waterfall: who gets paid in default | 6.4 |
| Level 1 vs Level 2 vs Level 3 classification of products | 6.5 |
| P&L Explain walkthrough for an autocallable | 6.6 |
| Reserve calculation: bid-offer reserve on a barrier product | 6.6 |
| CVA calculation concept for a CLN | 6.7 |
| SA-CCR exposure calculation concept | 6.7 |
| Model validation report structure | 6.8 |
| Corporate action: stock split adjustment to strike/barrier | 6.9 |
| Trade break escalation workflow | 6.9 |

### Bucket D — Taught Concisely Within Broader Topics

These are specialist terms that need definition and context but not full standalone treatment. They are taught within their parent section, not as separate topics.

| Term | Taught Within |
|------|-------------|
| TLAC, MREL | 6.4 (Capital Structure — bail-in context) |
| LCR, NSFR, HQLA | 6.7 (Treasury — liquidity regulation context) |
| ALM | 6.7 (Treasury function context) |
| RAROC | 6.7 (Capital consumption — return metric context) |
| SRI (Summary Risk Indicator) | 6.11 (PRIIPs/KID context) |
| Best Execution | 6.11 (MiFID II context) |
| Target Market | 6.11 (Product Governance context) |

---

## 3. Part 6 Architecture

### Title: PART 6 — THE OPERATIONAL ECOSYSTEM

*Subtitle: How the infrastructure around structured products works — from market conventions to regulatory compliance*

### Section Sequence (Educational Flow)

The sequence follows the lifecycle of a trade, from how markets express terms → how trades are documented → how they are valued → how they are controlled → how the system governs them.

```
6.1  Market Conventions               "How the market speaks"
6.2  Reading a Termsheet              "What the document says"
6.3  Documentation & Legal Framework  "What the contract means"
6.4  Credit & Capital Structure       "Who gets paid when things go wrong"
6.5  Valuation & Fair Value           "How we know what things are worth"
6.6  Product Control                  "How we verify the numbers"
6.7  Treasury, Capital & XVA          "How the bank prices its own costs"
6.8  Model Risk Management            "How we govern the models"
6.9  Operations                       "How trades flow through the system"
6.10 The Practitioner's Desk          "How the desk actually talks and works"
6.11 Regulatory Framework             "What the regulators require"
```

### Section Detail

#### 6.1 Market Conventions (~400 lines)
- Business day conventions: Following, Modified Following, Preceding, Modified Preceding
- Day count conventions: ACT/360, ACT/365, ACT/ACT, 30/360, 30E/360 — with worked calculations
- Calendar conventions: Trading, Settlement, Business, Joint calendars, TARGET
- Settlement conventions: T+0 through T+3, DvP, FoP
- Observation conventions: Continuous vs daily, European vs American barrier monitoring
- Exercise conventions: European, American, Bermudan (deepened from Part 1)
- Floating rate mechanics: fixing lag, reset dates, stub periods, broken dates, end-of-month rules
- Coupon mechanics: accrual, compounding, day count application

#### 6.2 Reading a Termsheet (~350 lines)
- Anatomy of an indicative termsheet (field-by-field walkthrough)
- Trade dates: Trade Date, Booking Date, Effective Date, Issue Date, Settlement Date
- Observation dates: Valuation Date, Determination Date, Fixing Date, Observation Date, Reset Date, Roll Date
- Payment mechanics: Payment Date, Record Date, Ex-Date
- Economics: Strike, Barrier, Participation, Cap, Floor, Trigger, Buffer, Bonus Level
- Price conventions: Clean Price, Dirty Price, Accrued Interest
- Settlement: Cash vs Physical, Settlement Calendar, Settlement Currency
- Legal: Calculation Agent, Governing Law, Jurisdiction
- Common termsheet misreading mistakes

#### 6.3 Documentation & Legal Framework (~350 lines)
- ISDA Master Agreement: purpose, structure, Schedule, key provisions
- CSA: threshold, MTA, eligible collateral, haircuts, independent amount, dispute resolution
- Confirmations: structure, matching process, economic terms vs legal terms
- Novation & assignment: when, why, process
- Market Disruption Events: what they are, how they affect observation dates
- Additional Disruption Events & Extraordinary Events
- Force Majeure provisions
- Close-out netting
- Compression & tear-up (brief)

#### 6.4 Credit & Capital Structure (~350 lines)
- Capital hierarchy: equity → preferred → senior secured → senior unsecured → senior non-preferred → subordinated → Tier 2 → AT1
- Recovery waterfall: who gets paid first in default
- AT1 & CoCos: conversion triggers, write-down mechanics
- Bail-in: TLAC, MREL, resolution framework
- CDS restructuring clauses: Full Restructuring (FR), Modified Restructuring (MR), Modified Modified Restructuring (MMR), No Restructuring (NR)
  - Regional conventions: Europe (MMR→CR), North America (MR→NR), Asia (varies)
  - Settlement implications for each clause type
  - Impact on CLN products
- Reference obligations & deliverable obligations (deepened)
- Credit event auction mechanics

#### 6.5 Valuation & Fair Value (~350 lines)
- Fair Value: definition, IFRS 13/ASC 820 context
- Mark-to-Market vs Mark-to-Model
- Fair Value Hierarchy: Level 1, Level 2, Level 3 — criteria, examples per product family
- IPV: purpose, process, data sources, tolerance thresholds, escalation
- Consensus pricing services (Markit, Bloomberg BVAL)
- Broker quotes: when used, reliability assessment
- Valuation Committees: composition, mandate, frequency
- Price testing: stale price detection, price challenge process
- Day One P&L: what it is, regulatory requirements, deferral rules

#### 6.6 Product Control (~400 lines)
- Product Control function: mandate, daily workflow
- P&L Explain: decomposition by risk factor (Delta, Gamma, Vega, Theta, Rho, credit, funding)
- Flash P&L vs Official P&L: timing, differences, reconciliation
- Unexplained P&L: what triggers investigation, escalation thresholds
- Reserve framework:
  - Bid-offer reserve: why it exists, how it's calculated
  - Model reserve: model uncertainty quantification
  - Liquidity reserve: illiquid position adjustment
  - Day One reserve (inception profit deferral)
  - Parameter uncertainty reserve
  - Funding reserve
  - Credit reserve
  - Concentration reserve
- Reserve governance: who sets reserves, review frequency, release criteria
- Month-end process: formal P&L sign-off, reserve adequacy review
- Product Control for each product family (brief per-family notes)

#### 6.7 Treasury, Capital & XVA (~400 lines)
- Treasury function: what Treasury does, relationship to trading desks
- FTP methodology: how internal funding rates are set, FTP curve, term structure
- Liquidity cost: LCR, NSFR, HQLA — what they mean for product pricing
- XVA framework:
  - CVA (Credit Valuation Adjustment): counterparty credit risk pricing
  - DVA (Debit Valuation Adjustment): own credit risk
  - FVA (Funding Valuation Adjustment): cost of funding uncollateralized exposure
  - ColVA (Collateral Valuation Adjustment): cost of collateral terms
  - MVA (Margin Valuation Adjustment): cost of initial margin
  - KVA (Capital Valuation Adjustment): cost of capital consumption
- How XVA affects structured product pricing (worked example)
- Capital framework:
  - SA-CCR (Standardised Approach for Counterparty Credit Risk)
  - RWA (Risk-Weighted Assets): what they are, why they matter
  - PFE (Potential Future Exposure)
  - EAD (Exposure at Default)
  - RAROC: how capital consumption affects product profitability
- Capital optimization: netting, collateral, central clearing impact

#### 6.8 Model Risk Management (~350 lines)
- What is model risk: SR 11-7 / SS1/23 framework
- Model lifecycle: development → validation → approval → monitoring → retirement
- Model validation: independent review, challenger models, benchmarking
- Backtesting: P&L attribution, hypothesis testing, traffic light approach
- Sensitivity testing: bump-and-reprice, scenario analysis
- Model inventory: registration, classification, materiality assessment
- Model limitations: known limitations documentation, usage restrictions
- Expert judgment & model override: when allowed, governance, documentation
- Model risk for structured products: which products are model-heavy, which are model-light
- Common model risk issues per product family

#### 6.9 Operations (~350 lines)
- Trade lifecycle (operational view): capture → confirm → settle → maintain → mature
- Booking workflow: trade capture, enrichment, validation, four-eyes check
- Static data: counterparty data, instrument data, SSI (Standard Settlement Instructions)
- Golden source: which system is authoritative for which data
- Cash reconciliation: daily cash breaks, nostro reconciliation, investigation
- Trade reconciliation: front-to-back, position reconciliation
- Settlement: settlement workflow, fails management, fails charges
- Corporate actions (systematic):
  - Stock splits: ratio adjustment to strike, barrier, notional
  - Mergers & acquisitions: successor entity, adjustment methodology
  - Rights issues, spin-offs: dilution adjustment
  - ISDA fallback provisions for corporate events
- Trade amendments: when needed, approval workflow
- Trade breaks: detection, investigation, resolution, escalation
- Lifecycle events: fixings, coupon payments, barrier observations, autocall checks

#### 6.10 The Practitioner's Desk (~300 lines)
- Desk organization: flow book vs exotic book, vanilla vs structured
- Risk warehousing: what it means, why desks do it, inventory management
- Hedge vocabulary: internal hedge, external hedge, back-to-back, novation
- Greeks positioning language: long/short gamma, vega, correlation — what each means for the trader
- Role-specific vocabulary:
  - Structurer language: reverse inquiry, bespoke, vanilla wrapper
  - Trader language: axed, lifted, working, inventory, warehouse
  - Sales language: suitability, target market, indication, firm price
  - Risk language: limit breach, VaR, stress test, scenario
  - Product Control language: flash, official, unexplained, reserve
  - Operations language: break, fail, SSI, static data, golden source
- How a trade flows through the desk (end-to-end narrative)
- Day in the life: Structurer, Trader, Sales, Risk, PC, Ops

#### 6.11 Regulatory Framework (~300 lines)
- MiFID II: product governance, target market, appropriateness, suitability (deepened)
- PRIIPs: KID requirements, SRI methodology, performance scenarios
- EMIR: reporting, clearing obligation, risk mitigation for non-cleared
- UMR (Uncleared Margin Rules): IM/VM requirements, ISDA SIMM
- Basel framework (practical): how Basel III/IV affects structured products
- Best execution: obligation, evidence, monitoring
- MAR (Market Abuse Regulation): insider dealing, market manipulation relevance
- Dodd-Frank: Title VII, swap dealer registration, cross-border implications
- Central clearing: which products clear, CCP mechanics, default fund

### Estimated Scale

| Section | Est. Lines | Pages (equiv.) |
|---------|:---------:|:--------------:|
| 6.1 Market Conventions | ~400 | ~16 |
| 6.2 Reading a Termsheet | ~350 | ~14 |
| 6.3 Documentation & Legal | ~350 | ~14 |
| 6.4 Credit & Capital Structure | ~350 | ~14 |
| 6.5 Valuation & Fair Value | ~350 | ~14 |
| 6.6 Product Control | ~400 | ~16 |
| 6.7 Treasury, Capital & XVA | ~400 | ~16 |
| 6.8 Model Risk Management | ~350 | ~14 |
| 6.9 Operations | ~350 | ~14 |
| 6.10 Practitioner's Desk | ~300 | ~12 |
| 6.11 Regulatory Framework | ~300 | ~12 |
| Part 6 Knowledge Check & Mental Models | ~150 | ~6 |
| **TOTAL** | **~3,850** | **~152** |

### Educational Principles for Part 6

1. **Same voice**: Experienced structurer teaching a new analyst
2. **Same pattern**: Analogy → Explanation → Table → Example → Common Mistakes → Professor Note
3. **Build on foundations**: Reference Part 1 concepts (options, Greeks, credit) rather than re-explain
4. **Product-specific hooks**: Each section connects back to specific products from Part 5
5. **No duplication**: If Part 2 §2.7 teaches hedging, Part 6 teaches the infrastructure AROUND hedging (P&L explain, reserve impact)
6. **Interview-ready**: Each section implicitly prepares for infrastructure interview questions

---

## 4. Cross-Artifact Impact Assessment

| Artifact | Modification Needed | Scope |
|----------|:------------------:|-------|
| Desk_Bible_v2.md | YES | Append Part 6 (~3,850 lines) |
| Product DNA Atlas | NO | Product-level data unchanged |
| Product Comparison Matrix | NO | Product comparisons unchanged |
| Solutions Manual | NO | Frozen 2026-06-22 |
| Interview System | NO | Explicitly excluded from this task |
| Universe Map | MINOR | May note Part 6 exists (deferred) |
| Learning Dependency Graph | MINOR | May add Part 6 as prerequisite for some paths (deferred) |

---

## 5. Execution Plan

| Step | Action | Deliverable |
|------|--------|-------------|
| 1 | Write §6.1–6.3 (Conventions, Termsheet, Legal) | Content in Desk_Bible_v2.md |
| 2 | Write §6.4–6.6 (Credit, Valuation, Product Control) | Content in Desk_Bible_v2.md |
| 3 | Write §6.7–6.9 (Treasury/XVA, MRM, Operations) | Content in Desk_Bible_v2.md |
| 4 | Write §6.10–6.11 + Knowledge Check + Mental Models | Content in Desk_Bible_v2.md |
| 5 | Write execution log | review/knowledge_domain_remediation_execution.md |
| 6 | Write change log | review/cross_artifact_change_log.md |
| 7 | Write publication review | review/post_remediation_publication_review.md |

---

**End of integration plan.**
