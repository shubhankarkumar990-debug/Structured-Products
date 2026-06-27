# Chapter Acceptance Checklist

**Version:** 1.2
**Date:** 2026-06-20
**Purpose:** Mandatory checklist that every product chapter must pass before publication. A chapter is not complete until every applicable item is checked. Items marked [CONDITIONAL] only apply when the condition is met.
**Changelog:** v1.1 adds "Why This Product Exists" checks (E13-E18), Visual Specification checks (V8-V10). v1.2 adds Commercial Understanding expansion (E19-E20), Desk Reality checks (P9-P10), Publication Asset checks (V11-V14), and Figure Reference check (C11). Batches 0-3 under v1.0; Batch 4 under v1.1; v1.2 applies from Batch 5 onward.

---

## How to Use This Checklist

1. After generating a chapter, run through every item sequentially
2. Mark each item PASS, FAIL, or N/A (for conditional items)
3. Any FAIL requires correction before the chapter is accepted
4. After correction, re-verify the failed item and all items in the same category
5. Record the final result in `production/generation_dashboard.md`

---

## EDUCATIONAL (12 items)

### Feynman Compliance

| # | Check | Agent |
|:-:|-------|-------|
| E1 | Every section is understandable by a motivated reader who has completed the dependency chain but has no other finance knowledge | Professor Agent |
| E2 | No concept is introduced without first building intuition (why/what before how) | Professor Agent |
| E3 | No formula or equation appears without a preceding plain-English explanation | Cognitive Load Agent |

### Terminology Compliance

| # | Check | Agent |
|:-:|-------|-------|
| E4 | Every technical term is either (a) defined with a parenthetical on first use in the chapter, or (b) listed in the Dependency References table with a valid pointer to Parts 0-4 | Jargon Police Agent |
| E5 | No term from the Jargon Watchlist appears undefined | Jargon Police Agent |
| E6 | Three-barrier disambiguation rule applied (if product has multiple barriers) [CONDITIONAL: multi-barrier products only] | Jargon Police Agent |

### Dependency Compliance

| # | Check | Agent |
|:-:|-------|-------|
| E7 | Dependency References table is present and lists every concept used from Parts 0-4 | Cross-Reference Agent |
| E8 | All section number cross-references are accurate (reflect 1.7/1.8/1.9 renumbering) | Cross-Reference Agent |

### Worked Examples

| # | Check | Agent |
|:-:|-------|-------|
| E9 | §5 (What Happens If) contains at least 4 scenarios with specific numbers | Product Accuracy Agent |
| E10 | §12 (Worked Example) contains a full numerical example with dollar amounts, dates, and calculation steps | Product Accuracy Agent |

### Analogy Quality

| # | Check | Agent |
|:-:|-------|-------|
| E11 | §2 contains exactly one primary analogy that maps precisely to the product's core mechanic and does not collide with any reserved analogy domain | Professor Agent |

### Common Mistakes

| # | Check | Agent |
|:-:|-------|-------|
| E12 | §16 contains exactly 5 common mistakes, each with a bold title and a corrective explanation | Professor Agent |

### Why This Product Exists (v1.1 — Batch 4+)

| # | Check | Agent |
|:-:|-------|-------|
| E13 | "Why This Product Exists" section is present, placed after §4 and before §5 | Final Editor Agent |
| E14 | Contains all 7 subsections: Typical Buyer, Problem Being Solved, How The Client Makes Money, How The Bank Makes Money, Market Conditions Where Demand Increases, When This Product Makes Sense, When This Product Is Usually A Poor Choice | Product Accuracy Agent |
| E15 | "How The Bank Makes Money" is economically accurate and does not imply guaranteed profitability | Practitioner Agent |
| E16 | "When This Product Is Usually A Poor Choice" is educational, not investment advice | Professor Agent |

### Glossary Discipline (v1.1 — Batch 4+)

| # | Check | Agent |
|:-:|-------|-------|
| E17 | All terms checked against glossary.yaml and acronyms.yaml before introduction | Jargon Police Agent |
| E18 | New terms added to glossary only if likely to recur elsewhere in the book | Jargon Police Agent |

### Commercial Understanding (v1.2 — Batch 5+)

| # | Check | Agent |
|:-:|-------|-------|
| E19 | "How The Bank Makes Money" covers all 4 areas: client economics, bank economics, hedging economics, distribution economics | Practitioner Agent |
| E20 | Where applicable: explains why bank prefers structuring vs holding, which desk hedges, what residual risks remain | Practitioner Agent |

---

## VISUAL (14 items — was 10 in v1.1, 7 in v1.0)

### Payoff Diagram

| # | Check | Agent |
|:-:|-------|-------|
| V1 | §8 contains at least one ASCII payoff diagram or decision tree | Visual Design Agent |
| V2 | Payoff diagram axes follow the visual standard (Y = "Investor Return (%)" / X = "Underlying at Maturity (% of Initial)" for equity/credit; Y = "P&L ($)" / X = "Market Rate (%)" for rates) | Visual Design Agent |

### Timeline

| # | Check | Agent |
|:-:|-------|-------|
| V3 | [CONDITIONAL: periodic-payment or path-dependent products] An inline timeline or cash flow diagram is present, or a timeline is specified as a P1 Visual Learning Recommendation | Visual Design Agent |

### Decision Tree

| # | Check | Agent |
|:-:|-------|-------|
| V4 | [CONDITIONAL: products with observation-date conditionality] A decision tree is present inline or specified as a P1 Visual Learning Recommendation | Visual Design Agent |

### Visual Learning Recommendations

| # | Check | Agent |
|:-:|-------|-------|
| V5 | Exactly 5 Visual Learning Recommendations are present | Visual Design Agent |
| V6 | Each recommendation specifies: visual type, content description, and priority (P1/P2/P3) | Visual Design Agent |
| V7 | At least 2 of the 5 recommendations are P1 priority | Visual Design Agent |

### Visual Specifications — Publication Assets (v1.2 — Batch 5+)

| # | Check | Agent |
|:-:|-------|-------|
| V8 | At least 5 visual specifications are present | Visual Design Agent |
| V9 | Each specification includes all required fields: Figure Number, Visual ID, Type, Priority, Purpose, Visual Description, Diagram Elements, Caption, Location, Reuse Potential, Future Asset Filename | Visual Design Agent |
| V10 | Visual IDs follow the naming convention: `TYPE_PRODUCT_##` | Visual Design Agent |
| V11 | Priority distribution: at least 2 P1, 2 P2, 1 P3 | Visual Design Agent |
| V12 | At least one visual is unique to the product (not a reused template) | Visual Design Agent |
| V13 | Axis Definitions present for all chart-type visuals | Visual Design Agent |
| V14 | Future Asset Filenames follow convention: `type_product_##.svg` | Visual Design Agent |

---

## PROFESSIONAL (10 items — was 8 in v1.1)

### Booking Workflow

| # | Check | Agent |
|:-:|-------|-------|
| P1 | §10 specifies the correct booking system (NEMO/Sophis for ELN/CLN, Murex for SRT/STEG/Swaps) | Practitioner Agent |
| P2 | §10 specifies Four-Leg applicability (Yes for SRT/STEG, No for ELN/CLN) | Practitioner Agent |
| P3 | [CONDITIONAL: SRT/STEG products] §10 describes all four legs (Note, Issuer, Deposit, Hedge) | Practitioner Agent |

### Reconciliation Guidance

| # | Check | Agent |
|:-:|-------|-------|
| P4 | §11 contains exactly 5 reconciliation red flags that are operationally actionable | Practitioner Agent |

### Desk Perspective

| # | Check | Agent |
|:-:|-------|-------|
| P5 | Desk Perspective table in §10 contains exactly 5 rows: Trader, Structurer, Product Control, Risk, Operations | Practitioner Agent |
| P6 | Each Desk Perspective row is specific to this product (not generic/reusable across products) | Practitioner Agent |

### Interview Questions and Knowledge Check

| # | Check | Agent |
|:-:|-------|-------|
| P7 | §13 contains exactly 5 interview questions progressing from recall to reasoning | Practitioner Agent |
| P8 | Knowledge Check contains 5 review + 3 scenario + 1 desk question | Practitioner Agent |

### Desk Reality (v1.2 — Batch 5+)

| # | Check | Agent |
|:-:|-------|-------|
| P9 | Desk Reality section present, placed after Desk Perspective and before Knowledge Check | Practitioner Agent |
| P10 | Covers all 5 elements: what keeps traders awake, most important risk, typical junior mistake, hardest operational issue, most misunderstood concept. 150-250 words | Practitioner Agent |

---

## CONSISTENCY (11 items — was 10 in v1.1)

### Professor Voice

| # | Check | Agent |
|:-:|-------|-------|
| C1 | §1 opens with a concrete scenario involving a named person or entity (not "consider an investor") | Professor Agent |
| C2 | Professor Note is present in §7, starts with "If you remember only one thing..." | Final Editor Agent |
| C3 | No forbidden writing patterns from the Professor Voice Standard appear (passive voice in teaching, meta-commentary, hedging language, unnecessary qualifiers, emojis) | Final Editor Agent |

### Chapter Length

| # | Check | Agent |
|:-:|-------|-------|
| C4 | Chapter length is between 1,800 and 3,500 words | Final Editor Agent |

### Section Order

| # | Check | Agent |
|:-:|-------|-------|
| C5 | All 16 sections are present in the correct order (§1-§16) | Final Editor Agent |
| C6 | All 5 additional requirements are present (Professor Note, Desk Perspective, Knowledge Check, Visual Learning Recs, Dependency References) | Final Editor Agent |

### Cross-References

| # | Check | Agent |
|:-:|-------|-------|
| C7 | "How This Differs From..." bridge is present for within-family chapters (2nd+ product in family) [CONDITIONAL] | Cross-Reference Agent |
| C8 | All references to other chapters or sections are accurate | Cross-Reference Agent |

### Formatting

| # | Check | Agent |
|:-:|-------|-------|
| C9 | Chapter title follows format: `### 5.X.Y Product Name` | Final Editor Agent |
| C10 | ASCII diagrams do not exceed 60 characters width; tables do not exceed 8 columns | Final Editor Agent |
| C11 | Every visual specification has a corresponding inline figure reference: `(See Figure 5.X.Y-##)` [v1.2 — Batch 5+] | Final Editor Agent |

---

## Checklist Summary Template

Use this template to record the acceptance result for each chapter:

```
## [Product Name] — Acceptance Result

Date: YYYY-MM-DD
Chapter: 5.X.Y

### Educational (20 items — was 18 in v1.1, 12 in v1.0)
E1: [PASS/FAIL]  E2: [PASS/FAIL]  E3: [PASS/FAIL]
E4: [PASS/FAIL]  E5: [PASS/FAIL]  E6: [PASS/FAIL/N/A]
E7: [PASS/FAIL]  E8: [PASS/FAIL]
E9: [PASS/FAIL]  E10: [PASS/FAIL]
E11: [PASS/FAIL]
E12: [PASS/FAIL]
E13: [PASS/FAIL]  E14: [PASS/FAIL]  E15: [PASS/FAIL]  E16: [PASS/FAIL]
E17: [PASS/FAIL]  E18: [PASS/FAIL]
E19: [PASS/FAIL]  E20: [PASS/FAIL]

### Visual (14 items — was 10 in v1.1, 7 in v1.0)
V1: [PASS/FAIL]  V2: [PASS/FAIL]
V3: [PASS/FAIL/N/A]  V4: [PASS/FAIL/N/A]
V5: [PASS/FAIL/N/A]  V6: [PASS/FAIL/N/A]  V7: [PASS/FAIL/N/A]
V8: [PASS/FAIL]  V9: [PASS/FAIL]  V10: [PASS/FAIL]
V11: [PASS/FAIL]  V12: [PASS/FAIL]  V13: [PASS/FAIL]  V14: [PASS/FAIL]

### Professional (10 items — was 8 in v1.1)
P1: [PASS/FAIL]  P2: [PASS/FAIL]  P3: [PASS/FAIL/N/A]
P4: [PASS/FAIL]
P5: [PASS/FAIL]  P6: [PASS/FAIL]
P7: [PASS/FAIL]  P8: [PASS/FAIL]
P9: [PASS/FAIL]  P10: [PASS/FAIL]

### Consistency (11 items — was 10 in v1.1)
C1: [PASS/FAIL]  C2: [PASS/FAIL]  C3: [PASS/FAIL]
C4: [PASS/FAIL]
C5: [PASS/FAIL]  C6: [PASS/FAIL]
C7: [PASS/FAIL/N/A]  C8: [PASS/FAIL]
C9: [PASS/FAIL]  C10: [PASS/FAIL]
C11: [PASS/FAIL]

### Result
Total: XX/55 PASS (XX applicable)  [v1.2: was 47 in v1.1, 37 in v1.0]
Status: [ACCEPTED / REQUIRES REVISION]
Notes: [any specific issues]
```

---

## Pass/Fail Criteria

| Category | Pass Threshold |
|----------|:-------------:|
| Educational | 20/20 applicable items PASS (was 18 in v1.1, 12 in v1.0) |
| Visual | 14/14 applicable items PASS (was 10 in v1.1, 7 in v1.0) |
| Professional | 10/10 applicable items PASS (was 8 in v1.1) |
| Consistency | 11/11 applicable items PASS (was 10 in v1.1) |
| **Overall** | **All applicable items PASS** |

A single FAIL in any category blocks acceptance. There is no "pass with minor issues" — all issues must be corrected before the chapter is accepted.

---

*Checklist v1.0 effective 2026-06-19. v1.1 effective 2026-06-20. v1.2 effective 2026-06-20. v1.2 items (E19-E20, V11-V14, P9-P10, C11) apply from Batch 5 onward.*
