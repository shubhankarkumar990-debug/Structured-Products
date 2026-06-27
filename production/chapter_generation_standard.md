# Chapter Generation Standard

**Version:** 1.2
**Date:** 2026-06-20
**Scope:** All Part 5 product chapters (49 total, 21 accepted, 28 remaining)
**Authority:** This standard governs every product chapter generated for the Desk Bible v2. No chapter may deviate from these requirements without explicit approval.
**Changelog:** v1.0 baseline. v1.1 adds "Why This Product Exists" section, Visual Specification Standard, and Glossary Discipline rule. v1.2 adds Publication Asset fields, Commercial Understanding expansion, Desk Reality section, Visual Quality rules, and Figure Reference format. Batches 0-3 grandfathered under v1.0; Batch 4 under v1.1; v1.2 applies from Batch 5 onward.

---

## 1. Chapter Template — 16 Mandatory Sections

Every product chapter must contain exactly 16 sections in this order. No section may be omitted, merged, or reordered.

| § | Section | Purpose | Min Length |
|:-:|---------|---------|:----------:|
| 1 | Explain Like I'm New | Zero-knowledge opening scenario. A real person with a real need encounters this product for the first time. No jargon. No prerequisites. | 150 words |
| 2 | Real World Analogy | One primary analogy that maps precisely to the product's core mechanic. Must be maintained through the Mental Models table (§14). Must not collide with any analogy used in another chapter or in Parts 0-4 | 100 words |
| 3 | What Problem Does This Solve? | The market problem or client need this product addresses. Written from the client's perspective | 80 words |
| 4 | Why Clients Buy It | 3-5 specific reasons. Each reason is one sentence with a concrete example or number | 100 words |
| 5 | What Happens If... | Minimum 4 scenarios with specific numbers. Must include: (a) best case, (b) moderate case, (c) barrier breach / worst case, (d) one product-specific scenario (e.g., autocall, memory payout, credit event) | 200 words |
| 6 | Formal Definition | Precise product definition using correct terminology. All terms must be defined in this section or declared as a dependency from Parts 0-4 | 100 words |
| 7 | Product Construction | Decomposition into components. Where arithmetic is possible, show exact numbers (e.g., $100 → $88.90 bond + $11.10 option budget). Include a Professor Note | 200 words |
| 8 | Payoff Logic | At least one ASCII payoff diagram or decision tree. Describe the payoff formula in words and mathematics | 150 words |
| 9 | Key Risks | Table format: Risk | Description | Severity (High/Medium/Low) | Who Bears It. Minimum 5 risks | 150 words |
| 10 | Booking and Operations | Table format: Field | Value/Convention. Must specify: booking system (NEMO/Sophis or Murex), Four-Leg applicability (Yes/No), key booking fields, observation conventions | 150 words |
| 11 | Reconciliation Red Flags | 5 specific red flags that Operations or Product Control should watch for. Must be operationally actionable, not theoretical | 100 words |
| 12 | Worked Example | Full numerical example with specific dollar amounts, dates, and outcomes. Multi-row table for periodic products. Show the calculation steps | 200 words |
| 13 | Interview Questions | 5 questions progressing from factual recall to applied reasoning. Must be answerable from the chapter content | 80 words |
| 14 | Mental Models | Table format: Concept | Mental Model. Every key concept from the chapter gets a one-line mental model. The primary analogy from §2 must appear | 80 words |
| 15 | Key Takeaways | 5 takeaways. Each is one sentence. Must cover: what the product is, who buys it, the core risk, the core mechanic, and one operational fact | 80 words |
| 16 | Common Mistakes | 5 common mistakes. Each has a bold title and a 1-2 sentence explanation of why it's wrong. Must address real misconceptions, not trivial errors | 100 words |

**Total minimum chapter length: ~1,800 words. Target range: 2,000-3,000 words.**

---

## 2. Additional Mandatory Requirements

Beyond the 16 sections, every chapter must include:

| Requirement | Specification |
|-------------|--------------|
| **Professor Note** | Placed in §7 (Product Construction). One sentence: "If you remember only one thing from this chapter, remember this: [single most important insight]." |
| **Why This Product Exists** | Placed after §4 (Why Clients Buy It), before §5 (What Happens If). Contains 7 subsections (see §2a below). **v1.1 addition — applies from Batch 4 onward.** |
| **Desk Perspective** | Standalone section after §16. Table with exactly 5 rows: Trader, Structurer, Product Control, Risk, Operations. Each row describes what this product means specifically for that role. Non-generic — must differ meaningfully between products |
| **Desk Reality** | After Desk Perspective, before Knowledge Check. 150-250 words covering what actually keeps traders awake at night (see §2c below). **v1.2 addition — applies from Batch 5 onward.** |
| **Knowledge Check** | After Desk Reality. Structure: 5 review questions + 3 scenario questions + 1 desk question. Review questions test recall. Scenario questions test application. Desk question tests synthesis |
| **Visual Specifications (Publication Assets)** | Minimum 5 per chapter. Each specification is a publication-ready brief (see §2b below). Must include at least 2 P1, 2 P2, 1 P3. At least one visual must be unique to the product. **v1.2 expands from v1.1 format.** |
| **Figure References** | Inline references to visual specifications using format: `(See Figure 5.X.Y-##)`. Every visual specification must have a corresponding figure reference in the chapter body. **v1.2 addition.** |
| **Dependency References** | Table at chapter end: Concept | Where Taught (Part.Section). Every concept used in the chapter that was taught in Parts 0-4 must be listed. Cross-references must be accurate after the 1.7/1.8/1.9 renumbering |

### §2a. "Why This Product Exists" Section (v1.1)

Placed after §4, before §5. Contains exactly 7 subsections:

| # | Subsection | Content |
|:-:|-----------|---------|
| 1 | **Typical Buyer** | Who buys it: investor profile, client segment, sophistication level |
| 2 | **Problem Being Solved** | What need is being addressed; why the investor considers the product |
| 3 | **How The Client Makes Money** | Best-case outcome, typical successful outcome. Do not duplicate §5 payoff scenarios |
| 4 | **How The Bank Makes Money** | **v1.2 expanded.** Must cover: (a) Client economics — how the client's P&L works. (b) Bank economics — structuring spread, bid-offer, embedded option margin. (c) Hedging economics — which desk hedges, how, what residual risks remain. (d) Distribution economics — sales credit, distribution channel, client relationship value. Where applicable: why the bank prefers structuring versus holding risk. Be economically accurate. Do not imply guaranteed profitability |
| 5 | **Market Conditions Where Demand Increases** | When demand typically rises and why |
| 6 | **When This Product Makes Sense** | Suitable investor profile, suitable market view |
| 7 | **When This Product Is Usually A Poor Choice** | Unsuitable investor profile, unsuitable market environment. Educational only — not investment advice |

### §2b. Visual Specification Standard — Publication Assets (v1.2)

The final output is PDF and DOCX. ASCII diagrams are retained for inline illustration but are NOT the publication visual format. Every chapter must include formal visual specifications that serve as publication-ready diagram briefs — detailed enough that a designer can build the graphic without reading the chapter.

**Minimum:** 5 visual specifications per chapter.
**Priority distribution:** At least 2 P1, 2 P2, 1 P3.
**Uniqueness:** At least one visual must be unique to the product (not a reused template).

Each specification must include:

| Field | Description |
|-------|------------|
| **Figure Number** | Sequential figure number: `Figure 5.X.Y-##` (e.g., `Figure 5.2.6-01`) |
| **Visual ID** | Unique identifier: `TYPE_PRODUCT_##` (e.g., `PAYOFF_CCY_SWAP_01`) |
| **Type** | One of: Payoff Diagram, Timeline, Decision Tree, Cash Flow Diagram, Waterfall Diagram, Lifecycle Diagram, System Flow Diagram, Comparison Chart, Balance Sheet Illustration |
| **Priority** | P1 (essential), P2 (recommended), P3 (nice-to-have) |
| **Purpose** | One sentence: what the visual communicates |
| **Visual Description** | 2-3 sentences describing the visual in enough detail for a designer to build it |
| **Diagram Elements** | Bulleted list of all elements the diagram must contain |
| **Axis Definitions** | Y-axis label, X-axis label, tick marks (if applicable — omit for non-chart visuals) |
| **Caption** | Publication-ready caption text |
| **Location** | Which section the visual accompanies |
| **Reuse Potential** | High / Medium / Low — whether the visual template can be reused in other chapters |
| **Future Asset Filename** | Target filename: `type_product_##.svg` (e.g., `payoff_currency_swap_01.svg`) |

**Figure references:** Every visual specification must have a corresponding inline reference in the chapter body using the format `(See Figure 5.X.Y-##)`. This enables future automatic replacement of ASCII diagrams with SVG/PNG publication assets.

### §2c. Desk Reality Section (v1.2)

Placed after Desk Perspective, before Knowledge Check. 150-250 words. Covers:

| Element | Content |
|---------|---------|
| **What keeps traders awake** | The single biggest overnight worry for someone running this product |
| **Most important risk** | The risk that causes the largest P&L swings in practice (may differ from theoretical "highest severity" in §9) |
| **Typical junior mistake** | The most common error made by first-year analysts or associates on this product |
| **Hardest operational issue** | The operational challenge that most frequently causes breaks or delays |
| **Most misunderstood concept** | The aspect of this product that even experienced professionals commonly get wrong |

Goal: teach how the product behaves in real trading environments, not textbook theory.

---

## 3. Opening Pattern — "How This Differs From..."

For within-family chapters (the 2nd+ product in a family), the chapter must open with a 1-2 sentence bridge before §1:

> *This product is [identical to / a variant of] the [previous product] you just learned, except [one key difference]. That single change [creates this consequence].*

This bridge appears before §1 and is italicized. It provides immediate anchoring for sequential readers.

**Exception:** The first product in each family (PPN for ELN, IRS for Swaps, first SRT, first STEG, Vanilla CLN) does not need this bridge — they have family transition text instead.

---

## 4. Family Transition Text

At the start of each Part 5 subsection (5.1 ELN, 5.2 Swaps, 5.3 SRT, 5.4 STEG, 5.5 CLN, 5.6 Other), include a 2-3 sentence transition paragraph:

1. What the reader has learned so far
2. What this family is and what drives its payoff
3. Which Parts 1-2 building blocks this family uses

**Template:**
> *[Summary of what was covered]. We now turn to [family name] — products whose payoffs depend on [underlying risk factor]. The building blocks for this family were taught in [Part.Section references]: [list key concepts].*

---

## 5. Six Permanent Educational Rules

Every section of every chapter must comply with all six rules. Violation of any rule is a review failure.

| Rule | Requirement | Verification |
|------|------------|-------------|
| **No Unexplained Terminology** | Every term must be defined on first use in the chapter OR listed in the Dependency References table with a pointer to where it was taught. No exceptions | Jargon Police Agent |
| **Why Before How** | §§1-5 (why/what) must precede §§6-11 (how). The template enforces this by section order | Structural check |
| **Feynman Rule** | Every section must be understandable by a motivated person with no finance background, given the dependency chain. If a concept cannot be explained simply, the explanation is not good enough | Professor Agent |
| **Story First** | §1 must open with a concrete scenario involving a real person or situation. No abstraction. No "consider a product that..." | Professor Agent |
| **Cognitive Load** | No section may introduce more than 5 new concepts without a reinforcement device (example, diagram, table, or analogy) between them | Cognitive Load Agent |
| **Why Do I Care** | §3 and §4 must answer why this product exists and why clients buy it. These sections must be written from the client's perspective, not the bank's | Professor Agent |

---

## 6. System Accuracy Requirements

| Product Family | Booking System | Pricing System | Four-Leg? |
|---------------|---------------|---------------|:---------:|
| ELN | NEMO | Sophis | No |
| CLN | NEMO | Sophis | No |
| SRT | Murex | Murex | Yes |
| STEG | Murex | Murex | Yes |
| Swaps | Murex | Murex | Varies |
| Other | Varies | Varies | Varies |

Every chapter §10 must correctly specify the booking system. SRT and STEG chapters must describe all four legs (Note, Issuer, Deposit, Hedge).

---

## 7. Glossary Discipline (v1.1)

Before introducing any term in a chapter:

1. Check `reference/glossary/glossary.yaml` — if the term exists, reuse the canonical definition
2. Check `reference/acronyms/acronyms.yaml` — if the acronym exists, use the canonical expansion
3. If the term does not exist and is likely to recur elsewhere in the book, add it to the glossary
4. If the term is chapter-specific and unlikely to recur, define it in context only — do not add to glossary

Avoid glossary bloat. The glossary should contain terms a reader might encounter across multiple chapters.

---

## 8. Cross-Reference Accuracy

All cross-references must reflect the current section numbering:
- Section 1.7: Yield Curves, Spot Rates, and Forward Rates
- Section 1.8: Benchmark Rates, Swaps, and Rate Options
- Section 1.9: Credit Risk

The Dependency References table in each chapter must be verified against the actual section numbers in Desk_Bible_v2.md.

---

## 9. Length and Format Constraints

| Constraint | Specification |
|-----------|--------------|
| Target chapter length | 2,000-3,000 words |
| Maximum chapter length | 3,500 words (complex products like Phoenix, Synthetic CDO Tranche) |
| Minimum chapter length | 1,800 words |
| Heading format | `### 5.X.Y Product Name` for the chapter title. Bold numbered labels for each section |
| ASCII diagram width | Maximum 60 characters |
| Table column count | Maximum 8 columns |
| Sentence length | Target: 15-25 words average. Maximum single sentence: 40 words |

---

*Standard v1.0 effective 2026-06-19. v1.1 update effective 2026-06-20. Applies to all chapters generated after this date.*
