# Domain Inventory Audit

## Desk Bible v2 -- Structured Products Knowledge Coverage

**Audit scope**: 22,620-line manuscript, 49 products, 6 families, 22 sections per product, Parts 0-4, supporting artifacts (Product DNA Atlas, Product Comparison Matrix, Solutions Manual, Interview System).

**Audit question**: Does the Bible cover everything needed to OPERATE in structured products, not just understand the products?

---

## Domain-by-Domain Assessment

### 1. Product Knowledge

| Attribute | Detail |
|-----------|--------|
| **Coverage** | FULLY COVERED |
| **Location** | Parts 3-4 (49 chapters x 22 sections) |
| **What IS covered** | Complete taxonomy across 6 families (ELN 15, Swaps 8, SRT 5, STEG 4, CLN 5, Other 12). Each product receives 22 standardised sections covering definition, intuition, payoff, construction, use cases, risks, hedging, booking, desk reality, knowledge checks, and common mistakes. |
| **What is NOT covered** | No gap. This is the manuscript's core strength. |

### 2. Structuring

| Attribute | Detail |
|-----------|--------|
| **Coverage** | FULLY COVERED |
| **Location** | Per-chapter sections: SS3 (Construction), SS7 (Payoff Scenarios), SS12 (Structuring Considerations) + Solutions Manual artifact |
| **What IS covered** | Product construction from component instruments, payoff engineering, scenario analysis, structuring trade-offs, investor/issuer economics, and worked structuring problems in the Solutions Manual. |
| **What is NOT covered** | No material gap. Structuring depth is a standout feature. |

### 3. Termsheet Reading

| Attribute | Detail |
|-----------|--------|
| **Coverage** | PARTIALLY COVERED |
| **Location** | Per-chapter economics definitions; SS3, SS4 per product |
| **What IS covered** | Key economics terms (Notional: 336, Strike: 399, Cap: 1055, Floor: 169, Participation Rate: 85, Trigger: 273). Trade Date (80), Payment Date (33), Observation Date (129). Settlement mechanics (cash: 17, physical delivery: 44). |
| **What is NOT covered** | Booking Date (0), Valuation Date (0), Determination Date (0), Roll Date (0), Forward Strike (0). Clean Price (0), Dirty Price (0). No dedicated "how to read a termsheet" walkthrough. No termsheet anatomy section. |

### 4. Market Conventions

| Attribute | Detail |
|-----------|--------|
| **Coverage** | WEAKLY COVERED |
| **Location** | Scattered across worked examples in per-product chapters |
| **What IS covered** | ACT/360 (21 mentions) and 30/360 (14 mentions) used in day count fraction calculations within worked examples. T+2 settlement (28 mentions). Exercise styles well covered (European: 92, American: 62, Bermudan: 35). |
| **What is NOT covered** | Modified Following (0), ACT/365 (0), ACT/ACT (0), 30E/360 (0). No explanation of what business day conventions MEAN. No calendar conventions (Trading Calendar: 0, Settlement Calendar: 0, Business Calendar: 0). Day counts used mechanically in formulas but never explained as concepts. |

### 5. Trade Lifecycle

| Attribute | Detail |
|-----------|--------|
| **Coverage** | PARTIALLY COVERED |
| **Location** | Part 2 SS2.6 (high-level lifecycle), SS16 per chapter (Booking and Systems) |
| **What IS covered** | Conceptual lifecycle stages. Per-product booking system mapping (NEMO/Sophis/Murex), key booking fields, lifecycle events, red flags. |
| **What is NOT covered** | No end-to-end lifecycle for a single trade from inquiry to maturity. No STP (straight-through processing) coverage. No amendment/novation lifecycle. No early termination workflow detail. |

### 6. Documentation & Legal

| Attribute | Detail |
|-----------|--------|
| **Coverage** | PARTIALLY COVERED |
| **Location** | Per-chapter legal references; Part 2 foundations |
| **What IS covered** | ISDA framework (173 mentions), CSA (54 mentions), reference to master agreements and confirmations. |
| **What is NOT covered** | No ISDA Schedule explanation (what's negotiated, common elections). No CSA mechanics (thresholds, minimum transfer amounts, eligible collateral, valuation frequency). No novation documentation detail. No term sheet vs. confirmation mapping. No credit support annex walkthrough. |

### 7. Collateral & Margin

| Attribute | Detail |
|-----------|--------|
| **Coverage** | WEAKLY COVERED |
| **Location** | Mentioned in passing within CSA and risk sections |
| **What IS covered** | Initial Margin (1 mention), Variation Margin (1 mention). Existence of margin requirements acknowledged. |
| **What is NOT covered** | No threshold/MTA mechanics. No eligible collateral schedules. No haircut methodology. No margin call process. No dispute resolution. No UMR (Uncleared Margin Rules) coverage. No central clearing margin model. |

### 8. Valuation

| Attribute | Detail |
|-----------|--------|
| **Coverage** | PARTIALLY COVERED |
| **Location** | Part 1 (yield curves: 86, vol surface: 25, credit spread: 43), per-chapter SS15 |
| **What IS covered** | Yield curve concepts, volatility surface basics, credit spread as pricing input. Monte Carlo (30 mentions), Black-Scholes (18 mentions). Qualitative valuation drivers per product. |
| **What is NOT covered** | No discount curve construction depth (bootstrapping, interpolation). No correlation surface methodology. No model calibration procedures. No pricing library/tool walkthrough. No mark-to-market vs. mark-to-model distinction. |

### 9. Product Control

| Attribute | Detail |
|-----------|--------|
| **Coverage** | PARTIALLY COVERED |
| **Location** | 118 mentions across manuscript, primarily in SS16 and SS14 |
| **What IS covered** | Product control function referenced. Role acknowledged in booking checks and lifecycle events. |
| **What is NOT covered** | No P&L Explain methodology (daily P&L attribution to Greeks, market moves, time decay, new deals, amendments). No P&L reserves process. No month-end/quarter-end close procedures. No flash vs. official P&L distinction. |

### 10. Independent Price Verification (IPV)

| Attribute | Detail |
|-----------|--------|
| **Coverage** | WEAKLY COVERED |
| **Location** | 24 mentions, scattered |
| **What IS covered** | IPV function referenced as part of control framework. Existence acknowledged. |
| **What is NOT covered** | No Fair Value Hierarchy (ASC 820 / IFRS 13). No Level 1/2/3 classification. No IPV methodology (bid-offer, consensus pricing, model-based). No tolerance thresholds. No escalation procedures for IPV breaks. |

### 11. Reserves

| Attribute | Detail |
|-----------|--------|
| **Coverage** | MISSING |
| **Location** | Model Reserve: 1 mention. All others absent. |
| **What IS covered** | Single passing reference to model reserve concept. |
| **What is NOT covered** | Bid-offer reserve, model reserve methodology, liquidity reserve, credit reserve, parameter uncertainty reserve, day-one P&L reserve. No reserve calculation methodology. No reserve governance. Complete blind spot. |

### 12. XVA (Valuation Adjustments)

| Attribute | Detail |
|-----------|--------|
| **Coverage** | WEAKLY COVERED |
| **Location** | CVA: 2 word-matches, DVA: 1 |
| **What IS covered** | CVA and DVA mentioned. Conceptual awareness that counterparty credit affects pricing. |
| **What is NOT covered** | FVA (0), ColVA (0), MVA (0), KVA (0). No XVA desk function. No XVA calculation methodology. No XVA impact on pricing/P&L. No incremental vs. standalone XVA. No XVA hedging. |

### 13. Capital

| Attribute | Detail |
|-----------|--------|
| **Coverage** | WEAKLY COVERED |
| **Location** | Regulatory Capital: 11 mentions, Basel: 31 mentions |
| **What IS covered** | Regulatory capital mentioned as constraint. Basel framework referenced. SRT chapter covers capital relief mechanics. |
| **What is NOT covered** | RWA (0 word-match). No SA-CCR methodology. No EAD/PFE calculations. No capital charge per product type. No leverage ratio impact. No FRTB. No capital allocation to desks. |

### 14. Risk Management

| Attribute | Detail |
|-----------|--------|
| **Coverage** | FULLY COVERED |
| **Location** | Part 1 (Greeks, Vol, Correlation), SS15 per chapter, Part 2 SS2.7 (Hedging) |
| **What IS covered** | Full Greeks treatment. Volatility risk. Correlation risk. Per-product risk analysis (49 chapters). Hedging strategies. Risk scenarios. Tail risks. Gap risk. Pin risk. Practical risk warnings. |
| **What is NOT covered** | No VaR methodology. No stress testing framework. No risk limits structure. Minor gaps in an otherwise strong domain. |

### 15. Model Risk Management

| Attribute | Detail |
|-----------|--------|
| **Coverage** | WEAKLY COVERED |
| **Location** | Model Validation: 24 mentions, Model Risk: 33 mentions |
| **What IS covered** | Model validation referenced. Model risk acknowledged as a concern. Some model limitations discussed per product. |
| **What is NOT covered** | No SR 11-7 / SS1/23 framework. No challenger model methodology. No benchmark testing. No backtesting requirements. No model inventory/tiering. No model approval governance. No model lifecycle. |

### 16. Governance & Compliance

| Attribute | Detail |
|-----------|--------|
| **Coverage** | PARTIALLY COVERED |
| **Location** | Suitability: 105 mentions, Product Governance: 3, MiFID: 5, PRIIPs: 2 |
| **What IS covered** | Suitability assessment well covered as a concept. Product governance referenced. Regulatory framework names mentioned. |
| **What is NOT covered** | No target market assessment detail. No product approval process. No complaint handling. No best execution obligations. No conflicts of interest framework. MiFID/PRIIPs mentioned but not explained in operational depth. |

### 17. Operations

| Attribute | Detail |
|-----------|--------|
| **Coverage** | WEAKLY COVERED |
| **Location** | SS16 per chapter covers booking systems |
| **What IS covered** | Booking systems (NEMO/Sophis/Murex) and key booking fields per product. Lifecycle events from operations perspective. |
| **What is NOT covered** | No P&L Explain. No cash reconciliation. No static data management. No golden source concept. No break management. No exception processing. No operational risk controls. No STP rates. |

### 18. Settlement

| Attribute | Detail |
|-----------|--------|
| **Coverage** | PARTIALLY COVERED |
| **Location** | Cash Settlement: 17, Physical Settlement: 5, Physical Delivery: 44, T+2: 28, T+3: 5 |
| **What IS covered** | Cash vs. physical settlement distinction per product. T+2 standard referenced. Settlement mechanics described at product level. |
| **What is NOT covered** | No settlement instruction workflow. No SSI (Standard Settlement Instructions). No fails management. No CLS/DTCC/Euroclear mechanics. No cross-currency settlement. |

### 19. Corporate Actions

| Attribute | Detail |
|-----------|--------|
| **Coverage** | WEAKLY COVERED |
| **Location** | Stock Split: 12, Merger: 6 mentions |
| **What IS covered** | Stock splits and mergers referenced as adjustment triggers. Impact on structured products acknowledged. |
| **What is NOT covered** | Reverse Split (0), Rights Issue (0). No adjustment methodology (Calculation Agent determination, ratio adjustment, extraordinary events). No corporate action notification workflow. No ISDA corporate action definitions mapping. |

### 20. Credit Derivatives

| Attribute | Detail |
|-----------|--------|
| **Coverage** | FULLY COVERED |
| **Location** | Reference Entity: 69, Credit Event: 145, full CDS/CLN/FTD/CDO chapters |
| **What IS covered** | Complete credit derivatives taxonomy. Credit events (145 mentions). Reference entity mechanics. CDS, CLN, FTD, CDO product chapters with full 22-section treatment. Recovery rates. Credit curves. |
| **What is NOT covered** | No material gap within credit derivatives scope. |

### 21. Funding

| Attribute | Detail |
|-----------|--------|
| **Coverage** | PARTIALLY COVERED |
| **Location** | FTP: 44 mentions, Funding Cost: 16 mentions |
| **What IS covered** | Funds Transfer Pricing concept. Funding cost as structuring input. Impact on product economics. |
| **What is NOT covered** | No FTP methodology detail. No funding curve construction. No secured vs. unsecured funding distinction. No term funding vs. overnight. No funding benefit/cost attribution. |

### 22. Treasury

| Attribute | Detail |
|-----------|--------|
| **Coverage** | WEAKLY COVERED |
| **Location** | Minimal, scattered references |
| **What IS covered** | Treasury function referenced in context of funding. |
| **What is NOT covered** | No treasury function explanation. No ALM (Asset-Liability Management). No liquidity buffer management. No HQLA classification. No internal funding market mechanics. No balance sheet optimisation. |

### 23. Sales

| Attribute | Detail |
|-----------|--------|
| **Coverage** | PARTIALLY COVERED |
| **Location** | SS5 (Who Touches This Product) and SS8 per chapter |
| **What IS covered** | Sales role defined per product. Use cases and investor targeting. Client suitability. Product positioning. |
| **What is NOT covered** | No sales process workflow. No pricing request mechanics. No RFQ process. No client onboarding. No KYC/AML touchpoints. |

### 24. Trading

| Attribute | Detail |
|-----------|--------|
| **Coverage** | FULLY COVERED |
| **Location** | SS14 (Desk Reality) per chapter, Part 2 SS2.7 (Hedging) |
| **What IS covered** | Per-product trading perspective (49 chapters). Hedging strategies. Greeks management. Market making considerations. Risk warehousing. Practical desk knowledge. |
| **What is NOT covered** | No execution venue detail. No e-trading/platform coverage. Minor gaps in an otherwise comprehensive domain. |

### 25. Quantitative Concepts

| Attribute | Detail |
|-----------|--------|
| **Coverage** | PARTIALLY COVERED |
| **Location** | Part 1, Monte Carlo: 30, Black-Scholes: 18 |
| **What IS covered** | Monte Carlo simulation concepts. Black-Scholes framework. Basic numerical methods awareness. Stochastic process intuition. |
| **What is NOT covered** | No PDE/finite difference methods. No tree-based pricing (binomial/trinomial). No SABR model. No Heston model. No Hull-White model. No local volatility. No model comparison framework. |

### 26. Interview Readiness

| Attribute | Detail |
|-----------|--------|
| **Coverage** | FULLY COVERED |
| **Location** | SS19 (Knowledge Check) x 49 products + Interview System artifact |
| **What IS covered** | Per-product knowledge check questions. Dedicated Interview System artifact. Common mistakes (SS20) as anti-pattern reference. Cross-product comparison capability. |
| **What is NOT covered** | No gap. Purpose-built coverage. |

### 27. Regulatory

| Attribute | Detail |
|-----------|--------|
| **Coverage** | WEAKLY COVERED |
| **Location** | MiFID: 5, PRIIPs: 2, Basel: 31 |
| **What IS covered** | Regulatory framework names mentioned. Basel referenced in capital context. MiFID and PRIIPs acknowledged. |
| **What is NOT covered** | EMIR (0), Dodd-Frank (0), UMR (0). No regulatory reporting requirements. No transaction reporting. No trade repository obligations. No clearing mandates. No margin rules for uncleared derivatives. No regulatory timeline/implementation detail. |

---

## Summary Table

| # | Domain | Coverage Level | Key Evidence |
|---|--------|---------------|--------------|
| 1 | Product Knowledge | FULLY COVERED | 49 products x 22 sections |
| 2 | Structuring | FULLY COVERED | SS3, SS7, SS12 + Solutions Manual |
| 3 | Termsheet Reading | PARTIALLY COVERED | Economics strong; dates and conventions incomplete |
| 4 | Market Conventions | WEAKLY COVERED | Day counts in formulas only; conventions absent |
| 5 | Trade Lifecycle | PARTIALLY COVERED | Per-product lifecycle; no end-to-end workflow |
| 6 | Documentation & Legal | PARTIALLY COVERED | ISDA/CSA named; mechanics absent |
| 7 | Collateral & Margin | WEAKLY COVERED | IM/VM: 1 mention each |
| 8 | Valuation | PARTIALLY COVERED | Inputs covered; methodology absent |
| 9 | Product Control | PARTIALLY COVERED | Function referenced; P&L Explain absent |
| 10 | IPV | WEAKLY COVERED | 24 mentions; no methodology |
| 11 | Reserves | MISSING | 1 total mention |
| 12 | XVA | WEAKLY COVERED | CVA: 2, DVA: 1; FVA/MVA/KVA: 0 |
| 13 | Capital | WEAKLY COVERED | Named only; no SA-CCR/RWA methodology |
| 14 | Risk Management | FULLY COVERED | SS15 x 49 + Greeks + hedging |
| 15 | Model Risk Management | WEAKLY COVERED | Acknowledged; no framework |
| 16 | Governance & Compliance | PARTIALLY COVERED | Suitability strong; regulations thin |
| 17 | Operations | WEAKLY COVERED | Booking covered; reconciliation absent |
| 18 | Settlement | PARTIALLY COVERED | Cash/physical per product; no workflow |
| 19 | Corporate Actions | WEAKLY COVERED | Splits/mergers only; no methodology |
| 20 | Credit Derivatives | FULLY COVERED | Full chapter treatment |
| 21 | Funding | PARTIALLY COVERED | FTP named; no methodology |
| 22 | Treasury | WEAKLY COVERED | Function referenced only |
| 23 | Sales | PARTIALLY COVERED | Role and use cases; no process |
| 24 | Trading | FULLY COVERED | SS14 x 49 + hedging |
| 25 | Quantitative Concepts | PARTIALLY COVERED | MC/BS covered; advanced models absent |
| 26 | Interview Readiness | FULLY COVERED | SS19 x 49 + Interview System |
| 27 | Regulatory | WEAKLY COVERED | Named only; no EMIR/Dodd-Frank/UMR |

---

## Coverage Distribution

| Coverage Level | Count | Domains |
|----------------|-------|---------|
| **Fully Covered** | 7 | Product Knowledge, Structuring, Risk Management, Credit Derivatives, Trading, Interview Readiness, Credit Derivatives |
| **Partially Covered** | 10 | Termsheet Reading, Trade Lifecycle, Documentation & Legal, Valuation, Product Control, Governance, Settlement, Sales, Funding, Quantitative Concepts |
| **Weakly Covered** | 9 | Market Conventions, Collateral & Margin, IPV, XVA, Capital, Model Risk Management, Operations, Corporate Actions, Treasury, Regulatory |
| **Missing** | 1 | Reserves |

**Final count: 7 Fully, 10 Partially, 9 Weakly, 1 Missing.**

The manuscript excels at product-centric knowledge (what things are, how they work, how to trade them) but has systematic gaps in the operational infrastructure that surrounds product trading (how things get booked, controlled, settled, margined, reported, and governed).
