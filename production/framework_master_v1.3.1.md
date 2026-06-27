# Framework Master v1.3.1 — Sole Governing Standard (FROZEN)

**Version:** 1.3.1
**Date:** 2026-06-20
**Authority:** This document is the sole governing standard for all future chapter generation in Desk Bible v2. It supersedes all prior framework versions as the authoritative source of truth. **This version is FROZEN.** No modifications permitted unless a critical defect is discovered (see Section U).
**Scope:** All Part 5 product chapters (49 total, 24 accepted, 25 remaining)
**Lineage:** v1.0 (baseline) → v1.1 (Why This Product Exists, Visual Specs, Glossary Discipline) → v1.2 (Publication Assets, Commercial Understanding, Desk Reality, Visual Quality, Figure References) → v1.3 (Product DNA, Family Position, Product Evolution, Market Invention, Product Lifecycle, Expanded Desk Coverage, Publication Architecture) → v1.3.1 (this document: stabilization, contradiction resolution, registry creation, freeze)
**Grandfathering:** Batches 0-3 under v1.0. Batch 4 under v1.1. Batch 5 under v1.2. v1.3.1 applies from Batch 6 onward.
**Stabilization Audit:** `review/framework_v1_3_1_stabilization_audit.md` — 27 issues identified, 25 resolved, 1 deferred, 1 accepted

---

## SECTION A — BOOK PHILOSOPHY

### A.1 Core Teaching Principles

The Desk Bible is a single coherent educational experience, not 49 independent chapters. Every design decision serves one goal: a motivated reader with no prior finance knowledge should be able to read sequentially from Part 0 through Part 5 and emerge with a working understanding of every structured product the desk trades.

| Principle | Rule |
|-----------|------|
| **Beginner-first** | Every chapter assumes the reader has completed only the dependency chain and nothing else. No assumed knowledge beyond what has been explicitly taught |
| **Professor teaching style** | The author is a patient, experienced practitioner who teaches through stories, analogies, and concrete examples — not a textbook |
| **Feynman standard** | If a concept cannot be explained simply, the explanation is not good enough. Complexity is a failure of teaching, not a property of the material |
| **Progressive disclosure** | Introduce complexity in layers. Each layer must be fully understood before the next is added |
| **Why-before-how** | Sections 1-9 (why/what) precede Sections 10-22 (how). The template enforces this by section order |
| **Story-first** | Every chapter opens with a concrete scenario involving a real person with a real need. No abstraction. No "consider a product that..." |
| **Cognitive load management** | No section may introduce more than 5 new concepts without a reinforcement device (example, diagram, table, or analogy) between them |
| **Mental model construction** | Every key concept gets a one-line mental model. The reader's understanding is built on analogies to things they already know |
| **No unexplained terminology** | Every technical term is either (a) defined with a parenthetical on first use, or (b) listed in the Dependency References table with a valid pointer to Parts 0-4 |

### A.2 Teaching Sequence

The pedagogical order within every chapter follows this invariant sequence:

1. **Teach intuition** — the reader understands WHY the product exists before seeing any mechanics
2. **Teach mechanics** — the reader understands HOW the product works through construction and payoff
3. **Teach jargon** — formal definitions and terminology are introduced AFTER the reader has intuition and mechanics
4. **Teach systems** — booking, operations, and reconciliation come after the reader understands the product itself
5. **Teach products in context** — relationships to other products, family position, and evolution come after standalone understanding
6. **Teach operations** — practical desk reality, mistakes, and operational challenges complete the picture

### A.3 Six Permanent Educational Rules

Every section of every chapter must comply with all six rules. Violation of any rule is a review failure. These rules are operationalized in the acceptance checklist (E1-E6 in Section S.4).

| # | Rule | Requirement | Verification Agent |
|:-:|------|------------|-------------------|
| 1 | **No Unexplained Terminology** | Every term must be defined on first use in the chapter OR listed in the Dependency References table with a pointer to where it was taught. No exceptions | Jargon Police Agent |
| 2 | **Why Before How** | Sections 1-9 (why/what) must precede Sections 10-22 (how). The template enforces this by section order | Structural check |
| 3 | **Feynman Rule** | Every section must be understandable by a motivated person with no finance background, given the dependency chain. If a concept cannot be explained simply, the explanation is not good enough | Professor Agent |
| 4 | **Story First** | §1 must open with a concrete scenario involving a real person or situation. No abstraction | Professor Agent |
| 5 | **Cognitive Load** | No section may introduce more than 5 new concepts without a reinforcement device (example, diagram, table, or analogy) between them | Cognitive Load Agent |
| 6 | **Why Do I Care** | §3 and §8 must answer why this product exists and why clients buy it. Written from the client's perspective, not the bank's | Professor Agent |

---

## SECTION B — MANDATORY CHAPTER COMPONENTS

Every chapter must contain ALL of the following. None may be removed, downgraded, or omitted.

### B.1 Main Sections (22 numbered for v1.3+; 16 for grandfathered)

See Section C for the complete template with purpose, requirements, and review criteria for each.

**Grandfathering rule:** Batches 0-3 (v1.0) have 16 sections. Batch 4 (v1.1) has 16 sections + additional elements. Batch 5 (v1.2) has 16 sections + additional elements. Batch 6+ (v1.3.1) has 22 sections + additional elements. Grandfathered chapters pass review under their applicable version's section count.

### B.2 Additional Mandatory Elements

These elements are required in every chapter but are not numbered sections. They appear in designated positions within or after the numbered sections.

| Element | Position | Version Introduced |
|---------|----------|:------------------:|
| **Professor Note** | Within §12 (Product Construction). Format: "If you remember only one thing from this chapter, remember this: [insight]." | v1.0 |
| **Bridge Text** | Before §1, italicized. "How This Differs From [previous product]." Required for 2nd+ product in a family | v1.0 |
| **Family Transition Text** | At the start of each Part 5 subsection (5.1, 5.2, 5.3, 5.4, 5.5, 5.6). Required for the first product in each family only | v1.0 |
| **Desk Reality** | After Who Touches This Product, before Knowledge Check | v1.2 |
| **Who Touches This Product** | After Common Mistakes, before Desk Reality | v1.3 |
| **Knowledge Check** | After Desk Reality. Structure: 5 review + 3 scenario + 1 desk question | v1.0 |
| **Visual Specifications (Publication Assets)** | After Knowledge Check. Minimum 6 specs for v1.3+ chapters. Supersedes "Visual Learning Recommendations" for Batch 4+ (see B.3) | v1.1 (expanded v1.2, v1.3) |
| **Related Chapters / Dependency References** | Final element. Table: Concept \| Where Taught | v1.0 |
| **Figure References** | Inline throughout chapter body: `(See Figure 5.X.Y-##)` | v1.2 |

### B.3 Visual Specification Versioning (v1.3.1 CLARIFICATION)

| Batch | Visual Block Format | Minimum Count | Priority Distribution |
|:-----:|-------------------|:-------------:|:--------------------:|
| 0-3 | Visual Learning Recommendations (descriptions + priority labels) | 5 | 2 P1 minimum |
| 4-5 | Visual Specifications (Publication Assets) with 12 required fields | 5 | 2P1 + 2P2 + 1P3 |
| 6+ | Visual Specifications (Publication Assets) with 12 required fields | 6 | 2P1 + 2P2 + 2P3 |

Checklist items V5-V7 apply to Batches 0-3 only (grandfathered). V8-V14 apply to Batch 4+. Both are not simultaneously required for the same chapter.

---

## SECTION C — MASTER CHAPTER TEMPLATE

Every v1.3.1 product chapter contains exactly 22 numbered sections in the order below, plus the additional mandatory elements from Section B.2. No section may be omitted, merged, or reordered.

**Grandfathering:** Chapters generated under v1.0-v1.2 have 16 numbered sections per the template that was in effect when they were generated. Checklist item C5 evaluates section presence per the applicable framework version.

### §1. Explain Like I'm New

| Attribute | Specification |
|-----------|--------------|
| **Purpose** | Zero-knowledge opening scenario. A real person with a real need encounters this product for the first time |
| **Required content** | Named protagonist, specific role, specific problem, how this product solves it. No jargon. No prerequisites beyond dependency chain |
| **Target length** | 150-200 words |
| **Common mistakes** | Using "consider an investor" instead of a named person. Introducing jargon before intuition. Making the scenario too abstract |
| **Review criteria** | Professor Agent: Is this understandable by someone who has never heard of the product? Consistency Agent: Is the protagonist unique? |

### §2. Core Analogy

| Attribute | Specification |
|-----------|--------------|
| **Purpose** | One primary analogy that maps precisely to the product's core mechanic. Must be maintained through Mental Models (§20) |
| **Required content** | A single extended analogy from everyday life. Must map to the product's defining characteristic. Must not collide with any analogy used in another chapter or in Parts 0-4 |
| **Target length** | 100-150 words |
| **Common mistakes** | Analogy that maps to a generic financial concept rather than this specific product. Analogy that collides with a reserved domain. Multiple competing analogies |
| **Review criteria** | Professor Agent: Does the analogy map precisely? Consistency Agent: Is the domain unique? |

### §3. What Problem Does It Solve

| Attribute | Specification |
|-----------|--------------|
| **Purpose** | The market problem or client need this product addresses. Written from the client's perspective |
| **Required content** | Table format: Client Need \| How the Product Delivers. Minimum 4 rows |
| **Target length** | 80-120 words |
| **Common mistakes** | Writing from the bank's perspective. Listing features instead of needs |
| **Review criteria** | Professor Agent: Is this written from the client's perspective? |

### §4. Product DNA

| Attribute | Specification |
|-----------|--------------|
| **Purpose** | Allow readers to understand the product's essential identity within 30 seconds |
| **Required content** | Table with exactly these fields: Asset Class, Underlying, Core Building Blocks, Primary Risk, Primary Buyer, Primary Hedge, Complexity Score (1-10). Complexity score must match `production/complexity_registry.yaml` |
| **Target length** | 50-80 words |
| **Common mistakes** | Missing fields. Complexity score not calibrated against family (PPN=2, Synthetic CDO=10) |
| **Review criteria** | Product Accuracy Agent: Are all fields correct? Consistency Agent: Is the complexity score calibrated? Does it match the complexity registry? |
| **Version** | v1.3 NEW |

### §5. Family Position

| Attribute | Specification |
|-----------|--------------|
| **Purpose** | Show where the product sits within the product hierarchy |
| **Required content** | ASCII tree showing the product's position. Maximum 8 lines. Format: `Asset Class → Family → Sub-family → Product` |
| **Target length** | 30-50 words (excluding tree) |
| **Common mistakes** | Tree exceeding 8 lines. Incorrect hierarchy. Missing the current product marker |
| **Review criteria** | Cross-Reference Agent: Is the hierarchy accurate? |
| **Version** | v1.3 NEW |
| **v1.3.1 CLARIFICATION** | Family Position is a **textual navigation aid**, NOT a visual specification or publication asset. It does NOT count toward the 6 visual spec minimum. Checklist V16 checks presence of the tree, not its classification as a visual spec |

**Example:**
```
Rates
└── Swaps
    └── Interest Rate Swaps
        └── Vanilla Swap (VLSP)  ← You are here
```

### §6. Product Evolution

| Attribute | Specification |
|-----------|--------------|
| **Purpose** | Show how complexity accumulated from the simplest ancestor to this product |
| **Required content** | Three stages: (1) Simplest ancestor, (2) Intermediate evolution, (3) Current product. For each: what was added, why it was added, what problem it solved |
| **Target length** | 100-150 words |
| **Common mistakes** | Skipping the intermediate stage. Not explaining WHY each evolution step happened. Describing too many steps |
| **Review criteria** | Professor Agent: Does the evolution explain why complexity was added? Cross-Reference Agent: Are ancestor products correctly identified? |
| **Version** | v1.3 NEW |

### §7. Why The Market Invented This Product

| Attribute | Specification |
|-----------|--------------|
| **Purpose** | Historical context — what market problem or limitation led to this product's creation |
| **Required content** | (1) Historical market problem, (2) Limitation of previous solutions, (3) Innovation introduced by this product, (4) Why adoption occurred |
| **Target length** | 150-200 words |
| **Common mistakes** | Generic history not specific to this product. Inventing history without factual basis. Exceeding 200 words |
| **Review criteria** | Product Accuracy Agent: Is the history accurate? Practitioner Agent: Does this reflect real market development? |
| **Version** | v1.3 NEW |

### §8. Why Clients Buy It

| Attribute | Specification |
|-----------|--------------|
| **Purpose** | 3-5 specific reasons clients choose this product |
| **Required content** | Numbered list. Each reason is one sentence with a concrete example or number |
| **Target length** | 100-150 words |
| **Common mistakes** | Generic reasons that apply to many products. Missing concrete examples. More than 5 reasons |
| **Review criteria** | Professor Agent: Are reasons specific to this product? |
| **Version** | v1.0 |

### §9. Why This Product Exists

| Attribute | Specification |
|-----------|--------------|
| **Purpose** | Comprehensive commercial and market context for the product |
| **Required content** | Exactly 7 subsections (see Section H for detailed requirements): (1) Typical Buyer, (2) Problem Being Solved, (3) How The Client Makes Money, (4) How The Bank Makes Money, (5) Market Conditions Where Demand Increases, (6) When This Product Makes Sense, (7) When This Product Is Usually A Poor Choice |
| **Target length** | 400-600 words |
| **Common mistakes** | Implying guaranteed profitability. Missing any of the 7 subsections. Writing investment advice instead of education |
| **Review criteria** | Practitioner Agent: Is "How The Bank Makes Money" economically accurate? Product Accuracy Agent: Are all 7 subsections present? |
| **Version** | v1.1 (expanded v1.2 with 4 economics areas) |

### §10. What Happens If...

| Attribute | Specification |
|-----------|--------------|
| **Purpose** | Scenario analysis with specific numbers showing product behavior under different conditions |
| **Required content** | Minimum 4 scenarios: (a) best case, (b) moderate case, (c) barrier breach / worst case, (d) one product-specific scenario (e.g., autocall, memory payout, credit event, commodity spike) |
| **Target length** | 200-300 words |
| **Common mistakes** | Scenarios without specific numbers. Missing the worst-case scenario. Scenarios that duplicate the worked example |
| **Review criteria** | Product Accuracy Agent: Are all calculations correct? Arithmetic Agent: Verified programmatically |
| **Version** | v1.0 |

### §11. Formal Definition

| Attribute | Specification |
|-----------|--------------|
| **Purpose** | Precise product definition using correct terminology |
| **Required content** | Formal definition paragraph. All terms must be defined in this section or declared as a dependency from Parts 0-4. Key structural components listed |
| **Target length** | 100-150 words |
| **Common mistakes** | Introducing jargon without definition. Circular definitions. Definition that doesn't distinguish this product from its closest relative |
| **Review criteria** | Jargon Police Agent: Are all terms defined or declared? |
| **Version** | v1.0 |

### §12. Product Construction

| Attribute | Specification |
|-----------|--------------|
| **Purpose** | Decomposition into components. How the product is built from building blocks |
| **Required content** | Component decomposition. Where arithmetic is possible, show exact numbers (e.g., $100 → $88.90 bond + $11.10 option budget). ASCII diagram of the construction. **Must include Professor Note** |
| **Target length** | 200-300 words |
| **Common mistakes** | Missing the Professor Note. Arithmetic errors in construction. Not showing the decomposition step by step |
| **Review criteria** | Product Accuracy Agent: Is the construction correct? Final Editor Agent: Is the Professor Note present and formatted correctly? |
| **Version** | v1.0 |

**Professor Note format:** Placed within §12. One sentence: "If you remember only one thing from this chapter, remember this: [single most important insight]."

### §13. Product Lifecycle

| Attribute | Specification |
|-----------|--------------|
| **Purpose** | Walk through the product's life from trade inception to maturity or early termination |
| **Required content** | Chronological stages: (1) Pre-trade (structuring, pricing, client approval), (2) Trade date (booking, confirmation), (3) During life (observations, payments, corporate actions), (4) Termination/maturity (settlement, final payment). For each stage: what happens, who is involved, what can go wrong |
| **Target length** | 150-250 words |
| **Common mistakes** | Missing stages. Not identifying who is involved at each stage. Generic lifecycle not specific to this product |
| **Review criteria** | Practitioner Agent: Does this reflect how the product actually lives on the desk? |
| **Version** | v1.3 NEW |

### §14. Payoff Logic

| Attribute | Specification |
|-----------|--------------|
| **Purpose** | Visual and mathematical description of the product's payoff |
| **Required content** | At least one ASCII payoff diagram or decision tree. Describe the payoff formula in words and mathematics. Axes must follow the visual standard |
| **Target length** | 150-200 words |
| **Common mistakes** | Payoff diagram axes not following the visual standard. Missing the zero-return line. Formula without preceding plain-English explanation |
| **Review criteria** | Visual Design Agent: Do axes follow the standard? Product Accuracy Agent: Is the payoff formula correct? |
| **Version** | v1.0 |

### §15. Risks

| Attribute | Specification |
|-----------|--------------|
| **Purpose** | Comprehensive risk assessment |
| **Required content** | Table format: Risk \| Description \| Severity (High/Medium/Low). Minimum 5 risks. Must include the primary risk identified in Product DNA |
| **Target length** | 150-200 words |
| **Common mistakes** | Generic risks that apply to any product. Missing the product's defining risk. Severity ratings not calibrated |
| **Review criteria** | Practitioner Agent: Are risks realistic and specific? |
| **Version** | v1.0 |

### §16. Booking And Systems

| Attribute | Specification |
|-----------|--------------|
| **Purpose** | Operational booking details |
| **Required content** | Table format: Field \| Value. Must specify: booking system (NEMO/Sophis or Murex), pricing system, Four-Leg applicability (Yes/No), key booking fields, payment schedule, ISDA documentation |
| **Target length** | 150-200 words |
| **Common mistakes** | Wrong booking system. Forgetting Four-Leg for SRT/STEG. Missing ISDA documentation type |
| **Review criteria** | Practitioner Agent: Is the booking system correct? |
| **Version** | v1.0 |

### §17. Red Flags

| Attribute | Specification |
|-----------|--------------|
| **Purpose** | Reconciliation red flags that Operations or Product Control should watch for |
| **Required content** | Table format: Red Flag \| What It Means \| Action. Exactly 5 red flags. Must be operationally actionable, not theoretical |
| **Target length** | 100-150 words |
| **Common mistakes** | Theoretical risks instead of actionable red flags. Generic flags that apply to any product |
| **Review criteria** | Practitioner Agent: Are these actionable by an operations analyst? |
| **Version** | v1.0 |

### §18. Worked Example

| Attribute | Specification |
|-----------|--------------|
| **Purpose** | Full numerical example with specific dollar amounts, dates, and calculation steps |
| **Required content** | Multi-row table for periodic products. Show every calculation step. Use realistic market parameters. Worked example asset must not collide with any previously used asset |
| **Target length** | 200-300 words |
| **Common mistakes** | Arithmetic errors. Unrealistic parameters. Asset collision with another chapter. Missing calculation steps |
| **Review criteria** | Arithmetic Agent: All calculations verified programmatically. Consistency Agent: Is the worked example asset unique? |
| **Version** | v1.0 |

### §19. Interview Questions

| Attribute | Specification |
|-----------|--------------|
| **Purpose** | 5 questions progressing from factual recall to applied reasoning |
| **Required content** | 5 numbered questions. Q1-Q2: factual recall. Q3-Q4: applied reasoning. Q5: synthesis/desk judgment. All must be answerable from the chapter content |
| **Target length** | 80-120 words |
| **Common mistakes** | All questions at the same difficulty level. Questions not answerable from the chapter. Questions that are too generic |
| **Review criteria** | Professor Agent: Do questions progress in difficulty? |
| **Version** | v1.0 |

### §20. Mental Models

| Attribute | Specification |
|-----------|--------------|
| **Purpose** | One-line mental models for every key concept in the chapter |
| **Required content** | Table format: Concept \| Mental Model. Every key concept gets a one-line mental model. The primary analogy from §2 must appear. Minimum 5 entries |
| **Target length** | 80-120 words |
| **Common mistakes** | Missing the primary analogy. Mental models that are definitions rather than analogies |
| **Review criteria** | Professor Agent: Are mental models intuitive? Consistency Agent: Is the primary analogy present? |
| **Version** | v1.0 |

### §21. Key Takeaways

| Attribute | Specification |
|-----------|--------------|
| **Purpose** | 5 one-sentence takeaways summarizing the chapter |
| **Required content** | Exactly 5 takeaways. Each is one sentence. Must cover: (1) what the product is, (2) who buys it, (3) the core risk, (4) the core mechanic, (5) one operational fact |
| **Target length** | 80-100 words |
| **Common mistakes** | Takeaways that are too generic. Missing one of the 5 required topics. Multi-sentence takeaways |
| **Review criteria** | Final Editor Agent: Are all 5 topics covered? |
| **Version** | v1.0 |

### §22. Common Mistakes

| Attribute | Specification |
|-----------|--------------|
| **Purpose** | 5 common mistakes that practitioners and students make about this product |
| **Required content** | Exactly 5 mistakes. Each has a bold title and a 1-2 sentence explanation of why it is wrong. Must address real misconceptions, not trivial errors |
| **Target length** | 100-150 words |
| **Common mistakes** | Mistakes that are too obvious. Mistakes that apply to any product. Missing the corrective explanation |
| **Review criteria** | Practitioner Agent: Are these real mistakes made in practice? |
| **Version** | v1.0 |

### Complete Section Order Summary

```
[Bridge Text — if 2nd+ product in family]
§1.  Explain Like I'm New
§2.  Core Analogy
§3.  What Problem Does It Solve
§4.  Product DNA                          (v1.3)
§5.  Family Position                      (v1.3)
§6.  Product Evolution                    (v1.3)
§7.  Why The Market Invented This Product (v1.3)
§8.  Why Clients Buy It
§9.  Why This Product Exists              (v1.1, expanded v1.2)
§10. What Happens If...
§11. Formal Definition
§12. Product Construction                 (includes Professor Note)
§13. Product Lifecycle                    (v1.3)
§14. Payoff Logic
§15. Risks
§16. Booking And Systems
§17. Red Flags
§18. Worked Example
§19. Interview Questions
§20. Mental Models
§21. Key Takeaways
§22. Common Mistakes
--- (section break) ---
Who Touches This Product                  (v1.3, expanded from Desk Perspective)
Desk Reality                              (v1.2)
Knowledge Check
Visual Specifications (Publication Assets)
Related Chapters / Dependency References
```

### Length and Format Constraints

| Constraint | v1.0-v1.2 | v1.3.1 | Rationale (v1.3.1 CLARIFICATION) |
|-----------|:---------:|:------:|:--------------------------------|
| Target chapter length | 2,000-3,000 words | 3,500-5,000 words | +600w v1.2 additions (Desk Reality, expanded Commercial Understanding, Publication Assets) + ~800w v1.3 additions (Product DNA, Family Position, Product Evolution, Market Invention, Product Lifecycle, expanded desk roles) = ~1,400w above v1.0 baseline |
| Maximum chapter length | 3,500 words | 5,500 words | Hard ceiling. Exceeding requires mandatory compression before acceptance |
| Minimum chapter length | 1,800 words | 3,000 words | Below this, mandatory content is likely missing |
| Heading format | `### 5.X.Y Product Name` | `### 5.X.Y Product Name` | |
| ASCII diagram width | 60 characters max | 60 characters max | |
| Table column count | 8 columns max | 8 columns max | |
| Sentence length | 15-25 words avg, 40 max | 15-25 words avg, 40 max | |

---

## SECTION D — PRODUCT DNA

**Mandatory from v1.3.** Placed as §4 in the chapter template.

Every chapter must include a Product DNA table with exactly these fields:

| Field | Description | Example (VLSP) |
|-------|------------|----------------|
| **Asset Class** | Rates, Equity, Credit, FX, Commodity | Rates |
| **Underlying** | The specific reference asset or index | SOFR / EURIBOR |
| **Core Building Blocks** | Parts 0-4 concepts the product is built from | Interest rate swap, discount factors, yield curves |
| **Primary Risk** | The single most important risk factor | Interest rate risk (DV01) |
| **Primary Buyer** | The typical client who buys this product | Banks, pension funds, corporate treasurers |
| **Primary Hedge** | How the bank hedges after selling this product | Government bond futures, other VLSPs |
| **Complexity Score** | 1-10 scale calibrated across the full product universe. Must match `production/complexity_registry.yaml` | 2 |

### Complexity Score Calibration

| Score | Meaning | Example Products |
|:-----:|---------|-----------------|
| 1-2 | Vanilla — standard, liquid, well-understood | PPN, VLSP, Vanilla CLN |
| 3-4 | Standard structured — one embedded feature | RC, DRC, IRS |
| 5-6 | Moderate complexity — multiple features or conditions | Phoenix, CRA ELN, TRS, CDS |
| 7-8 | Complex — path-dependent, multi-barrier, or multi-asset | Digital KI Put, Variance Swap, FTD |
| 9-10 | Highly complex — requires specialist knowledge | Synthetic CDO Tranche, Accumulator |

**Registry:** All complexity scores are recorded in `production/complexity_registry.yaml`. The registry is the canonical source. If a chapter's §4 score disagrees with the registry, the registry is authoritative.

---

## SECTION E — FAMILY POSITION

**Mandatory from v1.3.** Placed as §5 in the chapter template.

Show where the product sits within the hierarchy using an ASCII tree.

**Rules:**
- Maximum 8 lines
- Use box-drawing characters: `└── ├── │`
- Mark the current product with `← You are here`
- Start from the asset class level

**v1.3.1 CLARIFICATION:** The Family Position tree is a **textual navigation aid**. It is NOT a visual specification. It is NOT a publication asset. It does NOT count toward the 6 visual spec minimum. Checklist item V16 checks that the tree is present and correctly formatted — it does not classify the tree as a visual asset.

**Template:**
```
[Asset Class]
└── [Family]
    └── [Sub-family]
        └── [Product]  ← You are here
```

---

## SECTION F — PRODUCT EVOLUTION

**Mandatory from v1.3.** Placed as §6 in the chapter template.

Show how the product evolved from its simplest ancestor.

**Required format:**

| Stage | Product | What Was Added | Why |
|:-----:|---------|---------------|-----|
| 1 | [Simplest ancestor] | — (baseline) | — |
| 2 | [Intermediate] | [Feature added] | [Market need that drove the addition] |
| 3 | [Current product] | [Feature added] | [Market need that drove the addition] |

**Rules:**
- Exactly 3 stages (simplest → intermediate → current)
- Maximum 150 words
- Each stage must explain WHAT was added and WHY
- Ancestor products must exist in the Desk Bible (either already taught or in the generation order)

---

## SECTION G — WHY THE MARKET INVENTED THIS PRODUCT

**Mandatory from v1.3.** Placed as §7 in the chapter template.

**Required content (4 elements):**

1. **Historical market problem** — what specific problem existed before this product
2. **Limitation of previous solutions** — why existing products were insufficient
3. **Innovation introduced** — what this product added to the market toolkit
4. **Why adoption occurred** — what drove market participants to adopt this product

**Rules:**
- Maximum 200 words
- Must be historically accurate where possible
- Must be specific to this product, not generic financial history
- For products without clear historical origin (e.g., VLSP evolved naturally), explain the market forces that shaped the standard

---

## SECTION H — WHY THIS PRODUCT EXISTS

**Mandatory from v1.1 (expanded v1.2, v1.3).** Placed as §9 in the chapter template.

Contains exactly 7 subsections:

### H.1 Typical Buyer

| Content | Requirement |
|---------|------------|
| Client type | Institutional, corporate, sovereign, retail (specify which) |
| Investor profile | Sophistication level, typical AUM, market access |
| Client segment | Which business line serves them (e.g., corporate banking, wealth management, institutional sales) |

### H.2 Problem Being Solved

Explain which of these needs the product addresses (may be multiple):
- Yield enhancement
- Capital protection
- Leverage
- Risk transfer
- Market access
- Income generation
- Liability management
- Regulatory optimization

### H.3 How The Client Makes Money

- Best-case outcome with specific numbers
- Typical successful outcome
- Do not duplicate §10 (What Happens If) payoff scenarios

### H.4 How The Bank Makes Money

**v1.2 expanded. Must cover all 4 areas:**

| Area | Content |
|------|---------|
| **Client economics** | How the client's P&L works. What the client pays (explicitly or implicitly) |
| **Bank economics** | Structuring spread, bid-offer spread, embedded option margin, or other revenue sources. Specific numbers where possible (e.g., "5-15bp on notional") |
| **Hedging economics** | Which desk hedges. How (instruments used). What residual risks remain after hedging. Cost of the hedge |
| **Distribution economics** | Sales credit structure. Distribution channel. Client relationship value. Repeat business potential |

**Additionally, where applicable:**
- Why the bank prefers structuring versus holding risk
- Which desk manages the hedge
- What residual risks the bank retains

**Do NOT imply guaranteed profitability.**

### H.5 Market Conditions Where Demand Increases

When demand typically rises and why. Link to observable market conditions (volatility levels, curve shape, spread levels).

### H.6 When This Product Makes Sense

Suitable investor profile and suitable market outlook. Educational.

### H.7 When This Product Is Usually A Poor Choice

Unsuitable investor profile and unsuitable market outlook. **Educational only — not investment advice.**

---

## SECTION I — DESK REALITY

**Mandatory from v1.2.** Placed after Who Touches This Product, before Knowledge Check.

**Target:** 150-250 words

**Required elements (exactly 5):**

| Element | Content |
|---------|---------|
| **What keeps traders awake** | The single biggest overnight worry for someone running this product. Must be specific, not "market risk" |
| **Most important risk** | The risk that causes the largest P&L swings in practice. May differ from the theoretical "highest severity" risk in §15 |
| **Typical junior mistake** | The most common error made by first-year analysts or associates on this product. Must be a real, specific mistake |
| **Hardest operational issue** | The operational challenge that most frequently causes breaks or delays |
| **Most misunderstood concept** | The aspect of this product that even experienced professionals commonly get wrong |

**Goal:** Teach how the product behaves in real trading environments, not textbook theory. Each element must be specific to this product — generic answers are a review failure.

---

## SECTION J — WHO TOUCHES THIS PRODUCT

**Mandatory from v1.3 (expands v1.0 Desk Perspective from 5 to 8 roles).**

Placed after §22 (Common Mistakes), before Desk Reality.

**Required format:** Table with exactly 8 rows for v1.3.1 chapters (Batch 6+). Grandfathered chapters (Batches 0-5) retain 5 rows (Trader, Structurer, Product Control, Risk, Operations).

| Role | Responsibility | Primary Concern | Typical Question |
|------|---------------|----------------|-----------------|
| **Trader** | [Product-specific] | [Product-specific] | [Product-specific] |
| **Structurer** | [Product-specific] | [Product-specific] | [Product-specific] |
| **Sales** | [Product-specific] | [Product-specific] | [Product-specific] |
| **Risk** | [Product-specific] | [Product-specific] | [Product-specific] |
| **Product Control** | [Product-specific] | [Product-specific] | [Product-specific] |
| **Operations** | [Product-specific] | [Product-specific] | [Product-specific] |
| **Legal** | [Product-specific] | [Product-specific] | [Product-specific] |
| **Model Validation** | [Product-specific] | [Product-specific] | [Product-specific] |

**Rules:**
- Every row must be specific to this product. Generic descriptions that could apply to any product are a review failure.
- Each "Typical Question" must be a question that role would actually ask about THIS product.
- **v1.3.1 CLARIFICATION:** Batches 0-5 retain 5 roles (Trader, Structurer, Product Control, Risk, Operations). Batch 6+ requires 8 roles. Template Harmonization Pass may upgrade earlier chapters but upgrade is not mandatory.

---

## SECTION K — VISUAL STANDARDS

### K.1 ASCII Diagrams

ASCII diagrams are inline illustrations for the markdown document. They are educational drafts, NOT final publication assets. They will be replaced by SVG/PNG assets when the Visual Asset Library is built (deferred until all 49 chapters are complete).

**v1.3.1 CLARIFICATION — Visual Hierarchy:**

| Level | Name | Purpose | Status |
|:-----:|------|---------|--------|
| 1 | **Visual Learning Recommendation** | Brief description with priority label. Used in Batches 0-3 | Grandfathered |
| 2 | **Visual Specification (Publication Asset)** | Full 12-field specification. Used in Batch 4+ | Active standard |
| 3 | **Publication Asset** | Rendered SVG/PNG/DOCX/PDF file | Deferred until 49/49 |

ASCII diagrams within the chapter body (e.g., payoff charts in §14, construction diagrams in §12) are Level 1 educational aids. They are NOT Level 2 visual specifications and do NOT count toward the visual spec minimum.

**ASCII rules (unchanged from v1.0):**
- Maximum width: 60 characters
- Always label barrier levels with percentage and the word "Barrier"
- Always show the 0% return line
- Use `╱` and `╲` for diagonal lines, `─` for horizontal lines, `│` for vertical lines
- Include a caption below the diagram

### K.2 Payoff Diagram Axis Standards

| Product Domain | Y-Axis Label | X-Axis Label |
|---------------|-------------|-------------|
| Equity-linked (ELN) | Investor Return (%) | Underlying at Maturity (% of Initial) |
| Credit-linked (CLN) | Investor Return (%) | Credit Outcome |
| Rates (SRT, STEG) | P&L ($) | Market Rate (%) |
| Swaps | P&L ($) | Market Rate (%) or Reference Level |

### K.3 Publication Asset Specifications

Every chapter must include formal visual specifications that serve as publication-ready diagram briefs — detailed enough that a designer can build the graphic without reading the chapter.

**Minimum:** 6 visual specifications per chapter for v1.3.1 (was 5 in v1.2). Grandfathered chapters retain their applicable minimum.

**Priority distribution (v1.3.1):**

| Priority | Minimum Count | Definition |
|:--------:|:------------:|-----------|
| P1 | 2 | Essential for comprehension. Would be included in a one-page summary |
| P2 | 2 | High value for teaching. Adds significant comprehension |
| P3 | 2 | Enrichment. Useful for deep understanding or specific roles |

**Uniqueness:** At least one visual must be unique to the product (not a reused template from another chapter).

### K.4 Required Fields for Every Visual Specification

| Field | Description | Example |
|-------|------------|---------|
| **Figure Number** | `Figure 5.X.Y-##` | `Figure 5.3.1-01` |
| **Visual ID** | `TYPE_PRODUCT_##` | `PAYOFF_IR_CALLABLE_01` |
| **Type** | One of the allowed types (see below) | `Payoff Diagram` |
| **Priority** | P1 / P2 / P3 | `P1` |
| **Purpose** | One sentence | `Show the callable payoff with early termination scenarios` |
| **Visual Description** | 2-3 sentences for a designer | `Two-panel chart showing...` |
| **Diagram Elements** | List of all elements | `X-axis, Y-axis, payoff line, call barrier, ...` |
| **Axis Definitions** | Y-axis, X-axis, ticks (charts only) | `Y: P&L ($), X: Market Rate (%)` |
| **Caption** | Publication-ready text | `IR Callable Swap: payoff with quarterly call dates` |
| **Location** | Which section | `§14` |
| **Reuse Potential** | High / Medium / Low | `Medium` |
| **Future Asset Filename** | `type_product_##.svg` | `payoff_ir_callable_01.svg` |

**Registry:** All visual specifications for accepted chapters must be recorded in `production/visual_asset_master_registry.yaml`. Visual IDs, Figure Numbers, and Future Asset Filenames must be globally unique.

### K.5 Allowed Visual Types

Payoff Diagram, Timeline, Decision Tree, Lifecycle Diagram, Cash Flow Diagram, Waterfall Diagram, Comparison Chart, System Flow Diagram, Balance Sheet Illustration.

### K.6 Figure References

Every visual specification must have a corresponding inline reference in the chapter body:
```
(See Figure 5.X.Y-##)
```

### K.7 Asset Filename Convention

```
type_product_##.svg
```

Examples: `payoff_ir_callable_01.svg`, `lifecycle_zcl_01.svg`, `decision_tree_ncra_01.svg`

### K.8 Color Conventions (Production Rendering)

| Color | Usage |
|-------|-------|
| Green | Profit, above barrier, favorable outcome |
| Red | Loss, barrier breach, capital risk, unfavorable outcome |
| Blue | Autocall / early redemption events |
| Gold | Memory payout, accumulated coupon |
| Gray | Neutral zone, zero-return region |
| Orange | Warning, conditional zone |
| Black | Axes, labels, structural elements |

---

## SECTION L — GLOSSARY DISCIPLINE

**Mandatory from v1.1.**

Before introducing any term in a chapter:

1. Check `reference/glossary/glossary.yaml` — if the term exists, reuse the canonical definition
2. Check `reference/acronyms/acronyms.yaml` — if the acronym exists, use the canonical expansion
3. If the term does not exist and is likely to recur elsewhere in the book, add it to the glossary
4. If the term is chapter-specific and unlikely to recur, define it in context only — do not add to glossary

**Three-barrier disambiguation rule:** If a product has multiple barriers (e.g., capital barrier, coupon barrier, autocall barrier), each must be explicitly labeled on every use. Never use the unqualified word "barrier" alone.

Avoid glossary bloat. The glossary should contain terms a reader might encounter across multiple chapters.

---

## SECTION M — PROFESSOR VOICE STANDARD

### M.1 Required Characteristics

| Characteristic | Requirement |
|---------------|------------|
| **Tone** | Conversational expert — a patient, experienced practitioner explaining to a motivated new colleague |
| **Story-first** | Open with scenarios, not definitions |
| **Concrete examples** | Every abstract concept must have a concrete example within 2 sentences |
| **Intuitive analogies** | Use analogies to build understanding before introducing formal language |
| **Beginner accessible** | Understandable without prior finance knowledge (given the dependency chain) |
| **Progressive disclosure** | Layer complexity — simple first, then nuance |
| **High clarity** | Prefer short sentences. Active voice. Direct statements |

### M.2 Forbidden Patterns

| Pattern | Why It Fails | Example |
|---------|-------------|---------|
| Passive voice in teaching | Obscures agency, reduces clarity | "The product is structured..." → "The structurer builds..." |
| Meta-commentary | Breaks the teaching flow | "In this section we will discuss..." |
| Hedging language | Reduces confidence | "It could perhaps be argued..." |
| Unnecessary qualifiers | Add noise | "It is important to note that..." |
| Jargon dumping | Cognitive overload | Introducing 5 terms in one sentence |
| Academic verbosity | Obscures meaning | "The aforementioned construct..." |
| Unexplained acronyms | Breaks the Feynman rule | Using "CSA" without first saying "Credit Support Annex (CSA)" |
| Circular definitions | Teaches nothing | "A swap is a derivative instrument that swaps..." |
| Emojis | Unprofessional for this context | Any emoji |

---

## SECTION N — CONSISTENCY RULES

### N.1 Uniqueness Requirements

| Element | Rule | Registry |
|---------|------|----------|
| **Protagonist** | Every chapter has a unique named protagonist. No name reuse across the 49-chapter corpus | Analogy Domain Registry (dashboard §5) |
| **Analogy domain** | Every chapter has a unique analogy domain. No collision with reserved domains (Parts 0-4) or prior chapters | Analogy Domain Registry (dashboard §5) |
| **Worked example asset** | Every worked example uses a unique reference asset (stock, index, currency pair, etc.) | Tracked per chapter in dashboard |

### N.2 Structural Consistency

| Check | Requirement |
|-------|------------|
| **Bridge continuity** | Every 2nd+ chapter in a family has a bridge text identifying the single key difference from the predecessor |
| **Dependency integrity** | No chapter references a concept from Parts 0-4 without listing it in the Dependency References table |
| **Cross-reference accuracy** | All section number references reflect the current numbering (1.7/1.8/1.9 renumbering) |
| **Chapter heading format** | `### 5.X.Y Product Name` |
| **Section numbering** | §1 through §22 for v1.3.1 chapters; §1 through §16 for grandfathered chapters. In order, no gaps |
| **Booking system accuracy** | NEMO/Sophis for ELN/CLN. Murex for SRT/STEG/Swaps. Per the system accuracy table |

### N.3 Registries

The following registries are maintained in `production/generation_dashboard.md`:

1. **Analogy Domain Registry** (§5) — all used analogy domains + reserved domains
2. **Protagonist Registry** — tracked per chapter in §3
3. **Visual Template Registry** (§6) — all established visual templates
4. **Jargon Watchlist** (§7) — all new terms discovered during generation
5. **Worked Example Asset Registry** — tracked per chapter in §3

**External registries (v1.3.1):**
6. **Complexity Registry** — `production/complexity_registry.yaml`
7. **Visual Asset Master Registry** — `production/visual_asset_master_registry.yaml`

### N.4 System Accuracy Table

| Product Family | Booking System | Pricing System | Four-Leg? |
|---------------|---------------|---------------|:---------:|
| ELN | NEMO | Sophis | No |
| CLN | NEMO | Sophis | No |
| SRT | Murex | Murex | Yes |
| STEG | Murex | Murex | Yes |
| Swaps | Murex | Murex | Varies |
| Other | Varies | Varies | Varies |

---

## SECTION O — SPECIAL PRODUCT RULES

### O.1 SRT Products (Batch 6)

**Mandatory lifecycle walkthrough in §13 (Product Lifecycle):**

| Stage | What Happens |
|:-----:|-------------|
| 1 | Trade agreed — structurer prices, sales presents to client |
| 2 | Booking — all four legs booked in Murex (Note, Issuer, Deposit, Hedge) |
| 3 | Hedge booking — rates desk books the hedge separately |
| 4 | Daily valuation — Product Control marks all four legs |
| 5 | Coupon events — system processes coupon calculation and payment |
| 6 | Corporate actions — rate fixings, ISDA events |
| 7 | Maturity — note redeems, deposit returns, issuer leg closes, hedge unwinds |

**§16 (Booking And Systems) must describe all four legs:**
- Note leg (client-facing)
- Issuer leg (funding)
- Deposit leg (collateral)
- Hedge leg (risk management)

### O.2 STEG Products (Batch 7)

**Mandatory in every STEG chapter:**
- Yield curve visualization (ASCII or visual spec) showing where the product sits on the curve
- Curve dynamics explanation — how changes in curve shape affect the product
- Rate sensitivity explanation — DV01, convexity, or key rate duration as appropriate

### O.3 CLN Products (Batch 8)

**Mandatory in every CLN chapter:**
- Credit event walkthrough — step-by-step from credit event trigger through settlement
- Default waterfall — how losses are allocated
- Recovery mechanics — how recovery rates affect the investor's return

---

## SECTION P — BOOK-LEVEL INTELLIGENCE

The book must behave as a single coherent educational experience rather than 49 independent chapters. The following tracking systems ensure cross-chapter coherence.

### P.1 Product Evolution Tracking

For every product, maintain a link to its simplest ancestor and intermediate evolution stages (§6). This creates a network of product relationships across the book.

### P.2 Analogy Registry Management

All analogy domains are tracked in the dashboard (§5). Before generating a chapter:
1. Check the registry for collisions
2. Check the reserved domains list (Parts 0-4)
3. After generation, add the new analogy to the registry

### P.3 Protagonist Registry Management

All protagonists are tracked per chapter in the dashboard. Names must be unique across the 49-chapter corpus. Diverse geography and backgrounds are preferred.

### P.4 Cross-Family Dependency Tracking

The Dependency References table in each chapter creates a dependency graph. This graph must be acyclic (no chapter depends on a later chapter).

### P.5 Visual Asset Reuse Tracking

Visual templates established in one chapter may be reused in later chapters. The Visual Template Registry (dashboard §6) tracks which templates exist and when they became available. The Visual Asset Master Registry (`production/visual_asset_master_registry.yaml`) tracks all individual specifications.

### P.6 Glossary Growth Management

The Jargon Watchlist (dashboard §7) tracks all new terms. Terms likely to recur are added to `glossary.yaml`. Chapter-specific terms are defined in context only.

### P.7 Acronym Registry Management

All acronyms are tracked in `acronyms.yaml`. New acronyms are expanded on first use and added to the registry if likely to recur.

### P.8 Reader Journey Management

The chapter generation order (`production/product_generation_order.md`) defines the reading sequence. Each chapter must work for both:
- **Sequential readers** — reading in order, building on prior chapters
- **Reference readers** — jumping directly to a specific product

The bridge text and dependency references serve sequential readers. The Product DNA and Formal Definition serve reference readers.

---

## SECTION Q — PUBLICATION ARCHITECTURE

Defined in: `production/publication_architecture.md`

The publication architecture defines the asset library structure, naming conventions, and cross-reference standards for the future PDF/DOCX build. See that document for full details.

**Key principle:** No assets are generated during chapter writing. Only specifications are created. Asset generation is deferred until all 49 chapters are complete.

### Q.1 Publication Workflow (v1.3.1 ADDITION)

The publication pipeline follows this exact sequence:

| Step | Action | Prerequisite | Deliverable |
|:----:|--------|-------------|------------|
| 1 | All 49 chapters accepted | — | Complete manuscript |
| 2 | Template Harmonization Pass | Step 1 | Harmonized manuscript |
| 3 | Master Editorial Pass | Step 2 | Edited manuscript |
| 4 | SVG generation | Step 3 | SVG files (per publication_architecture.md) |
| 5 | SVG validation | Step 4 | Validated SVGs (viewBox, accessibility, fonts, colors) |
| 6 | PNG fallback generation | Step 5 | PNG files at 2x resolution |
| 7 | DOCX assembly | Step 6 | Word document with all assets |
| 8 | PDF generation | Step 7 | Final PDF (A4, bookmarked, TOC) |
| 9 | Publication QA | Step 8 | Release candidate |

### Q.2 Publication Readiness Score Rubric (v1.3.1 ADDITION)

| Component | Weight | Criteria |
|-----------|:------:|---------|
| Visual spec completeness | 30% | All 12 fields present for every spec |
| Figure reference integrity | 20% | Every spec has exactly one inline reference; every reference has a spec |
| Filename convention compliance | 20% | All filenames follow `type_product_##.svg` convention |
| Asset description quality | 20% | Captions and purpose fields are publication-ready (no placeholders, no abbreviations) |
| Reuse classification accuracy | 10% | High/Medium/Low classifications are consistent with actual reuse across chapters |

### Q.3 Accessibility Standards (v1.3.1 ADDITION)

| Standard | Requirement |
|----------|------------|
| Color contrast | WCAG 2.1 AA minimum (4.5:1 for normal text, 3:1 for large text) |
| Alt text | Alt text = caption text for all visual assets |
| Data accessibility | All data represented in tables or text, not only in graphics |
| SVG text | All text as SVG `<text>` elements, not paths |
| SVG labels | `aria-label` on root `<svg>` element. `<title>` element with caption |

---

## SECTION R — REVIEW REQUIREMENTS

### R.1 Chapter-Level Agents (every chapter)

| # | Agent | Focus |
|:-:|-------|-------|
| 1 | **Professor Agent** | Feynman compliance, teaching quality, analogy quality, voice standard |
| 2 | **Visual Design Agent** | Payoff diagrams, visual specs, axis standards, publication assets |
| 3 | **Jargon Police Agent** | Terminology compliance, glossary discipline, three-barrier rule |
| 4 | **Cognitive Load Agent** | Concept density, reinforcement devices, progressive disclosure |
| 5 | **Practitioner Agent** | Booking accuracy, desk perspective, desk reality, commercial understanding |
| 6 | **Product Accuracy Agent** | Product mechanics, payoff correctness, scenario accuracy |
| 7 | **Cross-Reference Agent** | Dependency references, bridge text, section number accuracy |
| 8 | **Final Editor Agent** | Structural completeness, formatting, section order, voice compliance |
| 9 | **Consistency Agent** | Protagonist uniqueness, analogy uniqueness, asset uniqueness, tone |
| 10 | **Completeness Agent** | All sections present, all requirements met, all counts correct |
| 11 | **Arithmetic Agent** | All calculations verified programmatically (Python3) |

**v1.3.1 FREEZE:** No additional chapter-level review agents may be introduced. The current 11-agent review stack is final.

### R.2 Book-Level Agents (every batch)

| # | Agent | Focus | Output Format |
|:-:|-------|-------|:-------------:|
| 1 | **Master Book Editor** | Cross-chapter consistency, reader journey coherence, repetition risk, style drift | PASS / CONCERNS / FAIL |
| 2 | **Beginner Reader Agent** | Can a complete beginner follow the sequential reading path? Are dependency chains complete? Are bridge texts accurate? | PASS / CONCERNS / FAIL |
| 3 | **Publication Agent** | Are all visual specs publication-ready? Are figure references consistent? Are filenames valid? | PASS / CONCERNS / FAIL |

**v1.3.1 CLARIFICATION:** Book-level agents produce qualitative assessments (PASS / CONCERNS / FAIL), not numerical scores. CONCERNS requires a specific list of issues. FAIL requires mandatory resolution before acceptance.

**v1.3.1 FREEZE:** No additional book-level agents may be introduced. The current 3-agent review stack is final.

### R.3 Family-Level Reviews

Run whenever a product family is completed. **v1.3.1 DEFINITION:** A family is "completed" when all products listed in `production/product_generation_order.md` for that Part 5 subsection have been accepted.

| Check | Description |
|-------|------------|
| Consistency | Protagonist, analogy, and asset uniqueness within the family |
| Progression | Complexity increases logically from simple to complex |
| Repetition risk | No content duplication that would bore a sequential reader |
| Visual reuse | Templates reused appropriately, each chapter has unique visuals |
| Analogy reuse | No analogy domain collision within the family |
| Dependency integrity | Bridge texts accurate, dependency chain acyclic |
| Booking consistency | All products in the family use the correct booking system |

### R.4 Review Output

Every batch review produces:
- `review/batch_N_book_review.md` — 11-agent chapter review + book-level agent review
- `review/[family]_family_review.md` — family-level review (when family is completed)
- Updated `production/generation_dashboard.md`

---

## SECTION S — QUALITY TARGETS

### S.1 Minimum Scores

| Metric | Minimum | Target |
|--------|:-------:|:-----:|
| Educational Score | 8.5 | 9.0 |
| Visual Score | 8.0 | 8.5 |
| Terminology Compliance | 98% | 100% |
| Consistency Score | 8.5 | 9.0 |
| Publication Readiness | 8.0 | 8.5 |
| First-Pass Acceptance Rate | 100% | 100% |

### S.2 Acceptance Criteria

A chapter is accepted only when ALL applicable items pass. There is no "pass with minor issues."

### S.3 Acceptance Checklist Summary

The v1.3.1 acceptance checklist contains the following item counts:

| Category | Items | Pass Threshold |
|----------|:-----:|:--------------:|
| Educational | 22 | 22/22 |
| Visual | 16 | 16/16 |
| Professional | 12 | 12/12 |
| Consistency | 11 | 11/11 |
| **Total** | **61** | **All applicable items PASS** |

**v1.3.1 CHANGE from v1.3:** Consistency reduced from 12 to 11 items. C11 removed (duplicate of V15). Former C12 renumbered to C11.

### S.4 Detailed Acceptance Checklist

#### Educational (22 items)

| # | Check | Agent | Version |
|:-:|-------|-------|:-------:|
| E1 | Every section understandable by a motivated reader who has completed the dependency chain | Professor | v1.0 |
| E2 | No concept introduced without first building intuition | Professor | v1.0 |
| E3 | No formula appears without a preceding plain-English explanation | Cognitive Load | v1.0 |
| E4 | Every technical term defined or declared as dependency | Jargon Police | v1.0 |
| E5 | No Jargon Watchlist term appears undefined | Jargon Police | v1.0 |
| E6 | Three-barrier disambiguation applied [CONDITIONAL: multi-barrier] | Jargon Police | v1.0 |
| E7 | Dependency References table present and complete | Cross-Reference | v1.0 |
| E8 | All section number cross-references accurate | Cross-Reference | v1.0 |
| E9 | §10 contains at least 4 scenarios with specific numbers | Product Accuracy | v1.0 |
| E10 | §18 contains a full numerical worked example | Product Accuracy | v1.0 |
| E11 | §2 contains exactly one primary analogy, no domain collision | Professor | v1.0 |
| E12 | §22 contains exactly 5 common mistakes with bold titles | Professor | v1.0 |
| E13 | "Why This Product Exists" section present after §8 | Final Editor | v1.1 |
| E14 | Contains all 7 subsections of "Why This Product Exists" | Product Accuracy | v1.1 |
| E15 | "How The Bank Makes Money" is economically accurate | Practitioner | v1.1 |
| E16 | "When This Product Is Usually A Poor Choice" is educational, not advice | Professor | v1.1 |
| E17 | All terms checked against glossary.yaml and acronyms.yaml | Jargon Police | v1.1 |
| E18 | New terms added to glossary only if likely to recur | Jargon Police | v1.1 |
| E19 | "How The Bank Makes Money" covers all 4 economics areas | Practitioner | v1.2 |
| E20 | Structuring vs holding, hedging desk, residual risks explained | Practitioner | v1.2 |
| E21 | Product DNA present with all 7 fields, complexity score matches registry | Product Accuracy | v1.3 |
| E22 | Product Evolution present with 3 stages and rationale | Cross-Reference | v1.3 |

#### Visual (16 items)

| # | Check | Agent | Version | Applicability |
|:-:|-------|-------|:-------:|:-------------:|
| V1 | §14 contains at least one ASCII payoff diagram or decision tree | Visual Design | v1.0 | All |
| V2 | Payoff diagram axes follow visual standard | Visual Design | v1.0 | All |
| V3 | Timeline or cash flow diagram present [CONDITIONAL: periodic products] | Visual Design | v1.0 | All |
| V4 | Decision tree present [CONDITIONAL: observation-date products] | Visual Design | v1.0 | All |
| V5 | Visual Learning Recommendations present | Visual Design | v1.0 | Batches 0-3 only |
| V6 | Each recommendation specifies type, description, priority | Visual Design | v1.0 | Batches 0-3 only |
| V7 | At least 2 recommendations are P1 | Visual Design | v1.0 | Batches 0-3 only |
| V8 | At least 5 (v1.2) or 6 (v1.3.1) visual specifications present | Visual Design | v1.3.1 | Batch 4+ |
| V9 | Each specification includes all 12 required fields | Visual Design | v1.2 | Batch 4+ |
| V10 | Visual IDs follow naming convention | Visual Design | v1.2 | Batch 4+ |
| V11 | Priority distribution: 2P1+2P2+1P3 (v1.2) or 2P1+2P2+2P3 (v1.3.1) | Visual Design | v1.3.1 | Batch 4+ |
| V12 | At least one visual unique to the product | Visual Design | v1.2 | Batch 4+ |
| V13 | Axis Definitions present for all chart-type visuals | Visual Design | v1.2 | Batch 4+ |
| V14 | Future Asset Filenames follow convention | Visual Design | v1.2 | Batch 4+ |
| V15 | Every visual spec has a corresponding inline figure reference | Final Editor | v1.2 | Batch 4+ |
| V16 | Family Position tree present (textual aid, not a visual spec) | Visual Design | v1.3 | v1.3.1 chapters |

#### Professional (12 items)

| # | Check | Agent | Version |
|:-:|-------|-------|:-------:|
| P1 | Correct booking system specified | Practitioner | v1.0 |
| P2 | Four-Leg applicability specified | Practitioner | v1.0 |
| P3 | Four legs described [CONDITIONAL: SRT/STEG] | Practitioner | v1.0 |
| P4 | Exactly 5 reconciliation red flags | Practitioner | v1.0 |
| P5 | Who Touches This Product: 8 rows [v1.3.1] or 5 rows [Batches 0-5 grandfathered] | Practitioner | v1.3 |
| P6 | Each role row is product-specific | Practitioner | v1.0 |
| P7 | 5 interview questions progressing recall → reasoning | Practitioner | v1.0 |
| P8 | Knowledge Check: 5 review + 3 scenario + 1 desk | Practitioner | v1.0 |
| P9 | Desk Reality present, 5 elements, 150-250 words | Practitioner | v1.2 |
| P10 | Desk Reality elements are product-specific | Practitioner | v1.2 |
| P11 | Product Lifecycle present with 4 stages | Practitioner | v1.3 |
| P12 | "Why The Market Invented This Product" present, ≤ 200 words | Product Accuracy | v1.3 |

#### Consistency (11 items — v1.3.1: reduced from 12)

| # | Check | Agent | Version |
|:-:|-------|-------|:-------:|
| C1 | §1 opens with a named person, not "consider an investor" | Professor | v1.0 |
| C2 | Professor Note present in §12, correct format | Final Editor | v1.0 |
| C3 | No forbidden writing patterns | Final Editor | v1.0 |
| C4 | Chapter length within range (per applicable framework version) | Final Editor | v1.3.1 |
| C5 | All sections present per applicable framework version (16 for v1.0-v1.2, 22 for v1.3.1) | Final Editor | v1.3.1 |
| C6 | All additional mandatory elements present | Final Editor | v1.0 |
| C7 | Bridge text present [CONDITIONAL: 2nd+ in family] | Cross-Reference | v1.0 |
| C8 | All cross-references accurate | Cross-Reference | v1.0 |
| C9 | Chapter heading: `### 5.X.Y Product Name` | Final Editor | v1.0 |
| C10 | ASCII diagrams ≤ 60 chars, tables ≤ 8 columns | Final Editor | v1.0 |
| C11 | Product DNA complexity score calibrated against family and matches registry | Consistency | v1.3.1 |

---

## SECTION T — FUTURE WORK (DO NOT EXECUTE)

The following work is deferred until ALL 49 chapters are complete. Do not begin any of these tasks during chapter generation.

| Task | Description | Prerequisites |
|------|------------|--------------|
| Template Harmonization Pass | Upgrade all chapters to v1.3.1 template (22 sections, 8 roles, 6 visual specs) | All 49 chapters accepted |
| Visual Asset Library | Build the SVG/PNG asset library from visual specifications | Template Harmonization Pass |
| SVG Generation | Generate SVG files for all publication assets | Visual Asset Library architecture |
| SVG Validation | Validate viewBox, accessibility, fonts, color compliance | SVG generation complete |
| PNG Generation | Generate PNG fallbacks from SVGs | SVG validation complete |
| DOCX Build | Build the Word document with all chapters and visual assets | PNGs complete |
| PDF Build | Build the PDF from DOCX with proper formatting | DOCX complete |
| Master Editorial Pass | Full editorial review for voice, consistency, and quality (see T.1) | All chapters complete |
| Compression Pass | Reduce word count while preserving content | Master Editorial Pass |
| Publication Layout Pass | Final formatting for publication | Compression Pass |
| Reader Experience Review | End-to-end reading test of the full book | All chapters complete |

### T.1 Master Editorial Pass Definition (v1.3.1 ADDITION)

| Attribute | Specification |
|-----------|--------------|
| **Purpose** | Ensure uniform voice, tone, and quality across the complete 49-chapter manuscript |
| **Inputs** | Complete manuscript (49 chapters), Framework Master v1.3.1, all batch/family review files |
| **Scope** | Voice consistency, terminology standardization, cross-reference validation, bridge text accuracy, word count optimization |
| **Agents** | Master Book Editor, Beginner Reader Agent |
| **Outputs** | Edited manuscript, editorial change log, quality delta report (before vs after) |
| **Criteria** | All chapters pass v1.3.1 checklist. No voice drift detected across families. All cross-references valid |

### T.2 Publication Pass Definition (v1.3.1 ADDITION)

| Attribute | Specification |
|-----------|--------------|
| **Purpose** | Transform the manuscript into publication-ready formats (SVG → PNG → DOCX → PDF) |
| **Inputs** | Edited manuscript (post-editorial pass), Visual Asset Master Registry, Publication Architecture |
| **Scope** | Asset generation, asset validation, document assembly, cross-reference linking, accessibility compliance |
| **Agents** | Publication Agent |
| **Workflow** | See Section Q.1 for the 9-step publication pipeline |
| **Outputs** | SVG asset library, PNG fallback library, DOCX document, PDF document, publication QA report |
| **Criteria** | All visual assets rendered. All figure references linked. WCAG 2.1 AA accessibility. A4 format with bookmarks and TOC |

### T.3 Template Harmonization Pass Definition (v1.3.1 ADDITION)

| Attribute | Specification |
|-----------|--------------|
| **Purpose** | Upgrade Batches 0-5 to the v1.3.1 template (add §4-§7, §13, expand desk roles, upgrade visual specs) |
| **Trigger** | ONLY after ALL 49 chapters are accepted. Not during generation |
| **Scope** | Structural additions only. No content rewriting unless a review agent identifies a genuine issue |
| **Outputs** | Harmonized manuscript, harmonization change log |
| **Rules** | Do NOT retrofit during generation. Do NOT rewrite chapters for stylistic reasons. Only add the missing structural elements |

---

## SECTION U — FRAMEWORK FREEZE (v1.3.1 NEW)

### U.1 Freeze Declaration

Framework Master v1.3.1 is **FROZEN** as of 2026-06-20. No modifications are permitted unless a critical defect is discovered.

### U.2 Definition of Critical Defect

A critical defect is one that:
1. Causes chapters to be generated with factually incorrect structure (e.g., wrong section order, missing mandatory element)
2. Creates an unresolvable contradiction between two requirements in this document
3. Makes publication impossible (e.g., naming convention that produces duplicate filenames)

The following are NOT critical defects and do NOT justify framework modification:
- Stylistic preferences
- Performance optimization
- Additional review quality desired
- Requests to add new sections, agents, or governance processes

### U.3 Freeze Scope

The following are frozen and may not be modified:

| Frozen Element | Specification |
|---------------|--------------|
| Chapter template | 22 sections in the order specified in Section C |
| Review agent stack | 11 chapter-level + 3 book-level (Sections R.1, R.2) |
| Acceptance checklist | 61 items (22 Educational + 16 Visual + 12 Professional + 11 Consistency) |
| Registries | complexity_registry.yaml structure, visual_asset_master_registry.yaml structure |
| Publication architecture | publication_architecture.md |
| Quality targets | Section S.1 minimums |
| Grandfathering rules | Batches 0-3 v1.0, Batch 4 v1.1, Batch 5 v1.2, Batch 6+ v1.3.1 |

### U.4 Amendment Process

If a critical defect is discovered:
1. Document the defect with evidence
2. Propose the minimal change required
3. Verify the change does not break any existing requirement
4. Update the framework version to v1.3.2 (or v1.4 if substantial)
5. Update the validation document
6. Update the freeze notice

---

## SECTION V — READER REINFORCEMENT ARCHITECTURE (v1.3.1 NEW)

### V.1 Milestone Assessments

Milestone assessments are placed between major sections of the book to reinforce learning and consolidate knowledge before the reader advances.

| Milestone | Placed After | Purpose |
|-----------|-------------|---------|
| Foundation Assessment | Part 2 (Building Blocks) | Verify the reader has internalized the 10 building block concepts before entering product chapters |
| ELN Family Assessment | Part 5.1 (all 15 ELN chapters) | Consolidate understanding of the full ELN product tree |
| Swaps Family Assessment | Part 5.2 (all 8 Swaps chapters) | Consolidate understanding of the swap family and cross-product relationships |
| SRT Family Assessment | Part 5.3 (all 5 SRT chapters) | Consolidate structured rates products |
| STEG Family Assessment | Part 5.4 (all 4 STEG chapters) | Consolidate structured equity-linked guarantee products |
| CLN Family Assessment | Part 5.5 (all 5 CLN chapters) | Consolidate credit-linked products |
| Final Book Assessment | Part 5.6 (all 7 Other chapters) | Comprehensive assessment spanning all families |

### V.2 Assessment Architecture (Structure Only — Do Not Generate Content)

Each milestone assessment follows this structure:

| Component | Description |
|-----------|------------|
| **Recall block** | 10 factual questions covering key concepts from the preceding section |
| **Scenario block** | 3 scenario-based questions requiring application of concepts |
| **Cross-product block** | 2 questions requiring the reader to compare or connect products across the section |
| **Desk judgment block** | 1 open-ended question requiring synthesis and practical judgment |

### V.3 Generation Rules

- Assessments are generated AFTER the relevant section is complete
- Assessment content must be answerable from the chapters alone (no external knowledge required)
- Assessments are NOT part of the chapter template — they are standalone inter-section elements
- Do NOT generate assessment content until the section is complete

---

## APPENDIX — OPENING PATTERNS

### Bridge Text (2nd+ product in family)

Required for every chapter that is not the first in its family. Placed before §1, italicized.

**Template:**
> *[Previous product] exchanged [X for Y]. The [current product] adds [one key difference]. That single change [creates this consequence].*

### Family Transition Text (first product in family)

Required for the first product in each Part 5 subsection. Placed at the start of the subsection.

**Template:**
> *[Summary of what was covered]. We now turn to [family name] — products whose payoffs depend on [underlying risk factor]. The building blocks for this family were taught in [Part.Section references]: [list key concepts].*

---

## APPENDIX — VERSION HISTORY

| Version | Date | Changes |
|:-------:|------|---------|
| v1.0 | 2026-06-19 | Baseline: 16 sections, 37 checklist items, 7 visual items |
| v1.1 | 2026-06-20 | Added: "Why This Product Exists" (7 subsections), Visual Specs, Glossary Discipline. Checklist: 47 items |
| v1.2 | 2026-06-20 | Added: Publication Assets (12 fields), Commercial Understanding (4 economics), Desk Reality (5 elements), Visual Quality (min 5, 2P1+2P2+1P3), Figure References. Checklist: 55 items |
| v1.3 | 2026-06-20 | Added: Product DNA, Family Position, Product Evolution, Why The Market Invented This Product, Product Lifecycle, Who Touches This Product (8 roles), min 6 visual specs (2P1+2P2+2P3), Book-level agents, Quality targets. Checklist: 62 items. Chapter template: 22 sections + additional mandatory elements |
| v1.3.1 | 2026-06-20 | Stabilization: resolved 25 ambiguities/conflicts/gaps (audit: `review/framework_v1_3_1_stabilization_audit.md`). Removed duplicate checklist item (C11 → 61 items). Added: Family Position clarification, visual hierarchy, grandfathering clarity for C5/V8/V11/P5, publication workflow (Q.1), publication readiness rubric (Q.2), accessibility standards (Q.3), Master Editorial Pass definition (T.1), Publication Pass definition (T.2), Template Harmonization Pass definition (T.3), complexity registry, visual asset master registry, reader reinforcement architecture (V), framework freeze (U). **FROZEN.** |

**Grandfathering:**
- Batches 0-3: v1.0 (16 sections, 37 items)
- Batch 4: v1.1 (16 sections + additional, 47 items)
- Batch 5: v1.2 (16 sections + additional, 55 items)
- Batch 6+: v1.3.1 (22 sections + additional, 61 items)

---

*Framework Master v1.3.1 — sole governing standard effective 2026-06-20. FROZEN. Supersedes framework_master_v1.3.md and all prior framework documents. No modifications permitted unless a critical defect is discovered (Section U).*
