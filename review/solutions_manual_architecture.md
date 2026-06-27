# Solutions Manual Architecture — Design Review

**Date:** 2026-06-21
**Proposed Section:** Part 7 — Solutions Manual
**Framework:** v1.3.1 (FROZEN)
**Purpose:** Design comprehensive answer key for all Knowledge Check questions
**Implementation:** After 49/49, after harmonization

---

## 1. Scope

Every chapter §20 (Knowledge Check) contains three question tiers:

| Tier | Type | Per Chapter | Total (49 chapters) |
|:----:|------|:----------:|:-------------------:|
| 1 | Review Questions | ~5 | ~245 |
| 2 | Scenario Questions | ~3 | ~147 |
| 3 | Desk Questions | ~1 | ~49 |
| | **Total** | **~9** | **~441** |

Part 0-4 foundation sections also have Knowledge Checks. Adding those (~6 sections with questions):

| Source | Questions |
|--------|:---------:|
| 49 product chapters | ~441 |
| Part 0 Knowledge Check | ~9 |
| Part 1 Knowledge Check | ~9 |
| Part 2 Knowledge Check | ~9 |
| Part 3-4 Knowledge Check | ~9 |
| **Grand total** | **~477** |

The Solutions Manual provides a three-tier answer for every question.

---

## 2. Three-Tier Answer Architecture

### Tier 1: Short Answer

| Attribute | Specification |
|-----------|-------------|
| Length | 1-3 sentences |
| Purpose | Quick reference. Confirms the reader's understanding. Gives the "what" |
| Audience | Self-assessment. Reader checking own answer |
| Style | Direct. Factual. No elaboration |
| Example | "A PPN is composed of a zero-coupon bond and a call option. The bond provides capital protection; the option provides upside participation." |

### Tier 2: Detailed Explanation

| Attribute | Specification |
|-----------|-------------|
| Length | 1-2 paragraphs (100-200 words) |
| Purpose | Teaches *why*. Explains the reasoning. Connects to concepts |
| Audience | Learner who got it wrong or wants deeper understanding |
| Style | Educational. References building block concepts. Shows chain of logic |
| Example | "The PPN's two components serve complementary functions. The zero-coupon bond, purchased at a discount (say 95% of notional for a 5-year product), guarantees that the investor receives 100% at maturity regardless of market performance. The remaining budget (5%) purchases an at-the-money call option on the underlying. The participation rate — the percentage of upside the investor captures — is determined entirely by what this remaining budget can afford. If call options are expensive (high implied vol, long tenor), the participation rate is lower. If options are cheap (low vol, short tenor), it is higher. This is why the participation rate is always less than 100% and fluctuates with market conditions — it is not a design choice but a budget constraint." |

### Tier 3: Desk Perspective

| Attribute | Specification |
|-----------|-------------|
| Length | 1 paragraph (75-150 words) |
| Purpose | How this plays out in practice. What the desk actually sees |
| Audience | Reader preparing for desk role or seeking practitioner insight |
| Style | Practical. Role-specific. Uses desk language (but no undefined jargon) |
| Example | "On the desk, the Structurer monitors option implied volatility closely because it directly determines the participation rate offered to clients. When vol is elevated (typically during market stress), the Structurer can offer higher participation — but must balance this against the Trader's hedging concerns, since delta-hedging in high-vol environments is more costly. Product Control independently verifies that the bond component is valued at the correct discount rate (usually the bank's funding curve, not risk-free), because using the wrong curve would misstate the option budget and potentially lead to a mispriced product." |

---

## 3. Answer Specification by Question Type

### 3.1 Review Questions → Three-Tier Answer

Review Questions test factual recall and conceptual understanding.

| Tier | Content Focus | Connects To |
|:----:|--------------|-------------|
| 1 | The fact or definition | Chapter §1-§3 (definition, how it works) |
| 2 | Why it works that way. Chain of reasoning | Chapter §4-§7 (construction, economics) |
| 3 | How the desk uses this knowledge | Chapter §14-§15 (Who Touches, Desk Perspective) |

### 3.2 Scenario Questions → Three-Tier Answer

Scenario Questions test application to specific market conditions.

| Tier | Content Focus | Connects To |
|:----:|--------------|-------------|
| 1 | The numerical answer or directional outcome | Chapter §9 (Three Scenarios) |
| 2 | Step-by-step calculation or reasoning path. What assumptions drive the answer | Chapter §5-§8 (mechanics, cash flows) |
| 3 | What the desk would actually do in this scenario. Risk management response | Chapter §10-§12 (risks, Greeks) |

### 3.3 Desk Questions → Three-Tier Answer

Desk Questions test professional judgment and multi-perspective thinking.

| Tier | Content Focus | Connects To |
|:----:|--------------|-------------|
| 1 | The core tradeoff or answer to the client/stakeholder | Chapter §1 (plain language) |
| 2 | Structured analysis covering all angles requested | Chapter §14-§17 (desk perspective, lifecycle) |
| 3 | What a senior practitioner would add. Nuance, edge cases, war stories framing | Cross-chapter references |

---

## 4. Structure

### 4.1 Organization

```
Part 7 — Solutions Manual
│
├── 7.1 How to Use This Solutions Manual
│
├── 7.2 Foundation Sections (Parts 0-4)
│   ├── Part 0 Solutions
│   ├── Part 1 Solutions
│   ├── Part 2 Solutions
│   └── Parts 3-4 Solutions
│
├── 7.3 ELN Family Solutions (15 products)
│   ├── 5.1.1 PPN Solutions
│   ├── 5.1.2 RC Solutions
│   └── ... (15 total)
│
├── 7.4 Swaps Family Solutions (8 products)
│
├── 7.5 SRT Family Solutions (5 products)
│
├── 7.6 STEG Family Solutions (4 products)
│
├── 7.7 CLN Family Solutions (5 products)
│
├── 7.8 Other Family Solutions (7 products)
│
└── 7.9 Cross-Product Integration Questions
    ├── 5 questions spanning multiple families
    └── Three-tier answers with cross-references
```

### 4.2 Per-Product Answer Block

Each product's solution block follows this format:

```markdown
## 5.X.Y — [Product Name] Solutions

### Review Questions

**Q1:** [Question text repeated for reader convenience]

**Tier 1 — Short Answer:**
[1-3 sentences]

**Tier 2 — Detailed Explanation:**
[1-2 paragraphs]

**Tier 3 — Desk Perspective:**
[1 paragraph]

---

**Q2:** [...]
[...]

### Scenario Questions

**S1:** [...]
[...]

### Desk Question

**D1:** [...]
[...]
```

---

## 5. Cross-Product Integration Questions (Section 7.9)

5 new questions that span multiple product families. Not in individual chapters — only in Solutions Manual.

| # | Question | Products Involved |
|:-:|---------|:-----------------:|
| 1 | A client wants enhanced yield but is concerned about credit risk. Compare the RC, CLN, and FTD approaches. Which offers the best risk-adjusted return in the current environment? | RC, CLN, FTD |
| 2 | Explain how the Accumulator and TARN achieve fundamentally different objectives despite both having barrier-linked termination features | Accumulator, TARN |
| 3 | A Structurer needs to construct a product offering 8%+ yield with capital protection above 80%. Which product types could achieve this, and what market conditions favor each? | PPN, RC, Phoenix, Shark Fin |
| 4 | Walk through how the same underlying equity index can generate products at complexity levels 2, 5, and 8. What structural additions create each jump? | PPN, Phoenix, Worst-of AC |
| 5 | Compare the booking, lifecycle, and risk management workflows for an IRS vs a Phoenix Autocallable. Why does one require far more operational infrastructure? | IRS, Phoenix |

---

## 6. Estimated Length

| Component | Questions | Words per Answer | Total Words |
|-----------|:---------:|:----------------:|:-----------:|
| Review answers (Tier 1+2+3) | ~245 | ~350 | ~85,750 |
| Scenario answers (Tier 1+2+3) | ~147 | ~400 | ~58,800 |
| Desk answers (Tier 1+2+3) | ~49 | ~400 | ~19,600 |
| Foundation section answers | ~36 | ~300 | ~10,800 |
| Cross-product questions | 5 | ~500 | ~2,500 |
| Introduction (7.1) | — | ~500 | ~500 |
| **Grand Total** | **~482** | — | **~177,950** |

| Metric | Value |
|--------|:-----:|
| Estimated word count | ~178,000 |
| Estimated pages | ~350-400 |
| Visual assets | 0 (text-only reference) |
| Implementation time | After harmonization, before final publication |

---

## 7. Generation Strategy

### 7.1 Approach

Generate solutions in family batches, matching manuscript generation order:

| Phase | Family | Products | Questions |
|:-----:|--------|:--------:|:---------:|
| 1 | Foundation sections | 4 sections | ~36 |
| 2 | ELN | 15 | ~135 |
| 3 | Swaps | 8 | ~72 |
| 4 | SRT | 5 | ~45 |
| 5 | STEG | 4 | ~36 |
| 6 | CLN | 5 | ~45 |
| 7 | Other | 7 | ~63 |
| 8 | Cross-product | — | 5 |

### 7.2 Quality Requirements

| Requirement | Detail |
|------------|--------|
| Accuracy | Every numerical answer verified against chapter content |
| Consistency | Tier 1 answer never contradicts Tier 2 or 3 |
| Cross-references | Tier 2 references specific section numbers for further reading |
| Terminology | Matches jargon watchlist — no undefined terms |
| No spoilers | Solutions Manual placed AFTER product chapters. Reader expected to attempt first |

### 7.3 Review Process

| Step | Agent | Purpose |
|:----:|-------|---------|
| 1 | Answer accuracy check | Verify against chapter content |
| 2 | Tier consistency check | Ensure T1/T2/T3 are coherent, not contradictory |
| 3 | Terminology check | All terms in glossary or defined in chapter |
| 4 | Cross-reference check | All section references valid |

---

## 8. Interaction with Existing Content

| Interaction | Detail |
|------------|--------|
| **Sources from §20** | Every answer traces to a specific Knowledge Check in the manuscript |
| **References §1-§19** | Tier 2 and 3 answers reference specific chapter sections |
| **Supports learning paths** | Self-study path uses Solutions Manual as assessment tool |
| **Standalone volume** | Solutions Manual can be published as separate companion or appendix |

**No existing chapter modifications required.**

---

## 9. Assessment

| Criterion | Score |
|-----------|:-----:|
| Educational impact | **VERY HIGH** — transforms questions from rhetorical to assessable |
| Effort | **VERY HIGH** — ~178K words, largest single component |
| Publication value | **VERY HIGH** — differentiates from any competing reference |
| Reader value | **VERY HIGH** — enables self-study without instructor |
| Risk | **LOW** — additive, no modifications to existing content |

**Recommendation: PROCEED.** Highest-volume enhancement. Implement after harmonization, in family batches.

---

*Solutions Manual Architecture Design Review completed 2026-06-21.*
