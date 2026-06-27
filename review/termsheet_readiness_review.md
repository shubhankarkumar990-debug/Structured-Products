# Termsheet Readiness Review

## Desk Bible v2 -- Can a Reader Actually Read the Documents?

**Audit scope**: Assess whether a reader who has studied the entire Desk Bible v2 (22,620 lines, 49 products, Parts 0-4, supporting artifacts) could competently read and understand the five core document types encountered in structured products operations.

---

## 1. Indicative Termsheet

An indicative termsheet is issued during the marketing/pre-trade phase. It contains proposed economics, dates, and reference terms. It is NOT binding.

### Terms the reader WOULD understand

| Category | Terms Covered |
|----------|--------------|
| Product type & structure | Product name, underlying, structure type, payoff profile, barrier type, autocall mechanism |
| Core economics | Notional (336), Strike (399), Cap (1055), Floor (169), Participation Rate (85), Trigger (273), Coupon rate, Premium (539) |
| Barrier mechanics | Knock-in, knock-out, barrier level, observation frequency (daily: 39, continuous: 4) |
| Autocall features | Autocall level (5), memory coupon (7), contingent coupon (7) |
| Underlying | Single stock, basket, index, worst-of, reference entity |
| Settlement type | Cash settlement (17), physical delivery (44) |
| Exercise style | European (92), American (62), Bermudan (35) |

### Terms the reader would NOT understand

| Category | Terms Missing |
|----------|--------------|
| Date conventions | Booking Date, Valuation Date, Determination Date, Roll Date; no distinction between Observation Date and Valuation Date |
| Business day rules | Modified Following, Following, Preceding -- how adjusted dates are calculated |
| Day count | ACT/360 and 30/360 appear in formulas but reader cannot explain what they mean or why one is chosen over another |
| Calendar references | "TARGET business days," "London and New York business days," joint calendar logic |
| Price quoting | Clean Price, Dirty Price, accrued interest conventions |
| Issuer terms | Issuer call rights, make-whole provisions, tax call, regulatory call |
| Disclaimer language | "Indicative only," "subject to final terms" -- legal significance not explained |

### Critical gaps

1. **Day count convention**: Reader sees "ACT/360" on a termsheet and has used it in a formula, but cannot explain what it means to a client or verify it is correct for the product/currency.
2. **Business day adjustment**: Reader cannot determine what happens when a payment date falls on a holiday.
3. **Valuation Date vs. Observation Date**: Reader cannot distinguish these two concepts, which determine different cashflows.

### Verdict: PASS WITH GAPS

The reader can understand the economic substance (what the product does and how the payoff works) but cannot verify date/convention mechanics. They would understand ~70% of an indicative termsheet by content weight, but the missing 30% includes fields that operations and middle office rely on.

---

## 2. Final Termsheet

A final termsheet is the binding document issued at pricing. It contains all indicative terms plus: final strike/barrier levels (set at trade date), exact dates with business day conventions, day count conventions, calculation agent, governing law, and settlement mechanics.

### Terms the reader WOULD understand

| Category | Terms Covered |
|----------|--------------|
| All indicative terms above | Same coverage as indicative |
| Final levels | Final strike, final barrier, final coupon rate -- reader understands what these numbers mean |
| Reference price | Closing price, settlement price concept |
| Lifecycle events | Autocall observation, coupon payment, barrier breach |
| Risk factors | Per-product risk analysis from SS15 |

### Terms the reader would NOT understand

| Category | Terms Missing |
|----------|--------------|
| Business day convention field | "Modified Following, New York and London" -- reader cannot parse this |
| Day count convention field | "ACT/360" or "30/360" as a standalone field -- reader has no concept-level understanding |
| Calendar field | "TARGET2," "NYSE," "combined calendar" -- not covered |
| Calculation agent provisions | Role acknowledged (10 mentions) but determination methodology absent |
| Adjustment provisions | Merger events, tender offers, nationalisation -- adjustment mechanics absent |
| Tax provisions | Gross-up, withholding tax, tax call -- not covered |
| Governing law | English law vs. New York law implications -- not covered |
| Selling restrictions | US person, Reg S, QIB -- not covered |
| Minimum denomination | Transfer restrictions -- not covered |
| ISIN / CUSIP | Security identifiers -- not explained |

### Critical gaps

1. **Adjustment provisions**: Final termsheets contain detailed corporate action adjustment clauses. Reader understands stock splits (12 mentions) and mergers (6) as events but not the adjustment methodology.
2. **Tax provisions**: Entirely absent. A practitioner who cannot read tax provisions cannot assess the true economics for different investor jurisdictions.
3. **Governing law implications**: Reader cannot advise on English law vs. New York law enforceability differences.

### Verdict: PASS WITH GAPS

Same economic comprehension as indicative, plus the reader can verify final levels against indicative. But the legal/operational fields (roughly 40% of a final termsheet's content) remain opaque.

---

## 3. ISDA Confirmation

An ISDA confirmation is the binding trade-level document under the ISDA Master Agreement. It contains: transaction type, notional, dates, economic terms, business day conventions, day count, calculation agent, and additional provisions.

### Terms the reader WOULD understand

| Category | Terms Covered |
|----------|--------------|
| Transaction type | Product identification -- strong (49 products covered) |
| Notional Amount | Defined and understood (336 mentions) |
| Trade Date / Effective Date | Trade Date understood (80); Effective Date referenced (16) |
| Underlying / Reference Entity | Well covered (Reference Entity: 69) |
| Fixed/floating rate | Concept covered in swap chapters |
| Credit events | Extensive (145 mentions) for credit products |
| Settlement method | Cash (17) vs. physical (5) |
| Premium / spread | Well covered (Premium: 539) |

### Terms the reader would NOT understand

| Category | Terms Missing |
|----------|--------------|
| "Calculation Agent" section | Determination provisions, fallback hierarchy, dispute resolution -- absent |
| "Business Days" section | "For the purpose of... 'Business Day' means..." -- conventions not covered |
| "Day Count Fraction" section | Formal ISDA day count definitions -- not covered |
| "Modified Following Business Day Convention" | Completely absent (0 mentions) |
| "Payment Dates" section | "Subject to adjustment in accordance with the Modified Following Business Day Convention" -- reader cannot parse this clause |
| "Termination Date" | Distinguished from Maturity Date -- not covered |
| "Additional Provisions" | Fallback rates (ISDA 2020 IBOR Fallbacks), disruption events, force majeure -- not covered |
| "Offices" section | Booking entity, branch -- not covered |
| ISDA Definitions reference | "2006 ISDA Definitions" or "2021 ISDA Interest Rate Derivatives Definitions" -- not distinguished |
| Credit Derivatives: "Reference Obligation" | Distinguished from Reference Entity -- partial coverage |
| "Restructuring" type | Modified Restructuring (Mod R), Modified Modified Restructuring (Mod Mod R), Old R -- not covered |

### Critical gaps

1. **Business day convention clause**: Every ISDA confirmation contains this. The reader cannot parse it.
2. **Calculation Agent determination**: The mechanism by which disputes are resolved and amounts determined is completely absent.
3. **ISDA Definitions version**: The reader cannot assess which definitions booklet governs the trade, which affects every defined term's meaning.
4. **Fallback provisions**: Post-LIBOR, every rate-linked confirmation has fallback language. Not covered.

### Verdict: FAIL

The reader can identify the product type and understand the economic terms but cannot read the operational and legal infrastructure that makes up approximately 60% of an ISDA confirmation. The business day convention, day count, calculation agent, and additional provisions sections would be unreadable. This is a failure because an ISDA confirmation IS the trade -- if you cannot read it, you cannot verify that what was agreed matches what was booked.

---

## 4. PRIIPs KID (Key Information Document)

A PRIIPs KID is a standardised 3-page document required for retail structured products in the EU/UK. It contains: product description, risk indicator (SRI), performance scenarios, costs, and complaint information.

### Terms the reader WOULD understand

| Category | Terms Covered |
|----------|--------------|
| Product description | Reader can understand the product mechanics section |
| "What is this product?" | Product type, objectives, underlying -- strong coverage |
| "What are the risks?" | Risk factors understood from SS15 per chapter |
| Performance scenarios | Payoff mechanics understood; reader can follow the scenarios |
| Underlying description | Well covered |

### Terms the reader would NOT understand

| Category | Terms Missing |
|----------|--------------|
| Summary Risk Indicator (SRI) | Not covered; 1-7 scale, market risk + credit risk |
| "Recommended holding period" | Not covered as regulatory concept |
| Performance scenario methodology | How scenarios are calculated (historical simulation, bootstrapping) -- not covered |
| Cost tables | Entry costs, exit costs, ongoing costs, incidental costs, RIY (Reduction in Yield) -- not covered |
| "How long should I hold it?" | Early exit penalty mechanics -- not covered |
| "How can I complain?" | Complaint procedure -- not covered |
| Comprehension alert | "You are about to purchase a product that is not simple..." -- regulatory significance not covered |
| Target market | MiFID II target market assessment -- not covered |

### Critical gaps

1. **SRI (Summary Risk Indicator)**: The standardised risk measure -- reader cannot interpret or verify.
2. **Cost disclosure**: The cost table is the most scrutinised section by regulators. Reader has no framework to assess it.
3. **Performance scenarios**: Reader understands payoffs but not the regulatory methodology for constructing scenarios (which differs from the structurer's scenario analysis in SS7).

### Verdict: PASS WITH GAPS

The reader can understand the product description and performance scenario narratives (the "what") but cannot assess the regulatory-mandated sections (SRI, costs, methodology) that make a KID compliant. For a sales or structuring role, this is sufficient. For a compliance or product governance role, it is not.

---

## 5. Internal Trade Capture Form

An internal trade capture form (booking ticket) is the system entry point. It contains: product type, notional, dates, economics, counterparty, booking entity, book, trader, sales, systems fields, and approval chain.

### Terms the reader WOULD understand

| Category | Terms Covered |
|----------|--------------|
| Product type | Strong -- 49 products with SS16 (Booking and Systems) per chapter |
| Notional | Covered (336) |
| Core economics | Strike, barrier, coupon, cap, floor -- covered |
| Underlying | Covered |
| Counterparty | Concept understood from SS5 per chapter |
| Booking system | NEMO, Sophis, Murex -- covered in SS16 |
| Key booking fields | Covered per product in SS16 |
| Lifecycle events | Covered per product in SS16 |
| Red flags | Covered per product in SS16 |

### Terms the reader would NOT understand

| Category | Terms Missing |
|----------|--------------|
| Booking entity / legal entity | Which entity books the trade -- not covered |
| Book / portfolio | Trading book assignment -- not covered |
| Trader ID / Sales ID | System attribution -- not covered in depth |
| Day count convention field | System field requiring selection from dropdown -- reader cannot choose correctly |
| Business day convention field | System field requiring selection -- reader cannot choose correctly |
| Calendar field | System field -- reader cannot select correct calendar(s) |
| Settlement instructions | SSI reference -- not covered |
| Netting set | Netting agreement reference -- not covered |
| CSA reference | Which CSA governs -- not covered despite 54 CSA mentions |
| Approval workflow | New product approval, credit approval, limit check -- workflow not covered |
| Static data | Counterparty static, instrument static -- not covered |

### Critical gaps

1. **Convention fields**: When booking a trade, the user must select day count, business day convention, and calendar from system dropdowns. The reader cannot make these selections.
2. **Legal entity / booking entity**: The reader does not know which entity to select or why it matters (regulatory, capital, netting).
3. **CSA linkage**: The reader knows CSA exists but cannot link a specific CSA to a specific trade in the booking system.

### Verdict: PASS WITH GAPS

SS16 per chapter provides good product-specific booking guidance (which system, which fields, which lifecycle events, which red flags). The reader can navigate the product-specific fields. But the cross-product operational fields (conventions, entity, CSA, settlement instructions) that appear on EVERY trade capture form remain gaps. A reader following SS16 could book the product-specific economics correctly but might misconfigure the operational infrastructure fields.

---

## Overall Readiness Matrix

| Document Type | Verdict | Economic Understanding | Convention/Legal Understanding | Operational Understanding |
|---------------|---------|----------------------|-------------------------------|--------------------------|
| Indicative Termsheet | PASS WITH GAPS | Strong (~85%) | Weak (~30%) | N/A |
| Final Termsheet | PASS WITH GAPS | Strong (~85%) | Weak (~25%) | Weak (~30%) |
| ISDA Confirmation | FAIL | Moderate (~60%) | Failed (~15%) | Failed (~20%) |
| PRIIPs KID | PASS WITH GAPS | Strong (~80%) | N/A | Weak (~25%) |
| Internal Trade Capture | PASS WITH GAPS | Strong (~80%) | Failed (~10%) | Moderate (~55%) |

**Overall verdict**: The Desk Bible produces readers who understand WHAT products do and WHY they exist, but who cannot reliably read the HOW of the documents that govern, capture, and confirm those products. The ISDA Confirmation failure is the most consequential: a practitioner who cannot read the confirmation that IS the trade has a critical competence gap.

---

## Root Cause

The manuscript was designed as a product knowledge bible, not an operational reference. Its 22-section per-product architecture covers product mechanics exhaustively but treats the surrounding documentation and convention infrastructure as context rather than content. The gap is architectural, not an oversight -- the manuscript would need a dedicated "Document Reading" part (market conventions, ISDA mechanics, termsheet anatomy, booking conventions) to close it.
