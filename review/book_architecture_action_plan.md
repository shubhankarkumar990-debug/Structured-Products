# Book Architecture Action Plan — Desk Bible v2

**Date:** 2026-06-19
**Source:** `review/book_architecture_review.md` (7-dimension assessment)
**Purpose:** Prioritized list of architectural improvements to apply during full-scale product generation

---

## 1. Must-Do Changes Before Scaling

These items address architectural issues that will compound if not resolved before generating the remaining 44 product chapters. None are blockers — the Part 5 template is production-ready — but applying them now prevents inconsistency at scale.

| # | Change | Dimension | Files Affected | Effort |
|:-:|--------|:---------:|----------------|:------:|
| 1.1 | **Standardize payoff chart axis conventions.** Adopt: Y = "Investor Return (%)", X = "Underlying at Maturity (% of Initial)" for equity/credit products. Y = "P&L ($)", X = "Market Rate (%)" for rates/swap products. Apply retroactively to 5 pilot chapters | E (Visual) | 5 pilot chapters in Desk_Bible_v2.md | Small |
| 1.2 | **Establish 3 ASCII visual templates.** (a) Payoff chart: standardized axes, barrier line as dashed horizontal, zone labels above/below. (b) Timeline: horizontal with event markers, payment arrows, date labels. (c) Decision tree: bracketed nodes, YES/NO branches, loop indicators. Document templates in a reference section or internal note for reuse | E (Visual) | New reference (internal) | Small |
| 1.3 | **Add family transition text** at the start of each Part 5 subsection (5.1 ELN, 5.2 Swaps, 5.3 SRT, 5.4 STEG, 5.5 CLN, 5.6 Other). 2-3 sentences per transition: what the reader just learned, what this family is, why it matters, which building blocks from Parts 1-2 it uses | A (Curriculum) | Desk_Bible_v2.md (6 insertions) | Small |
| 1.4 | **Add "How This Differs From..." bridge** to the opening of within-family product chapters. When writing the DRC after the RC, open with: "This product is identical to the Reverse Convertible you just learned, except the coupon is replaced by a discount to the purchase price." One sentence per chapter | A (Curriculum) | Each new chapter during generation | Trivial |
| 1.5 | **Create a Jargon Police supplementary watchlist** for operational and credit terminology. The pilot review found that core product terms (barrier, coupon, decomposition) are consistently defined, but operational terms (day count conventions, no-call periods, RED codes, ISDA committees) slip through. Add a watchlist of ~20 operational/credit terms to check during generation | D (Dependency) | Internal reference | Small |

**Total estimated effort for Section 1:** 3-4 hours. Most changes are small insertions applied iteratively during chapter generation.

### Estimated Impact

| Change | Without It | With It |
|--------|-----------|---------|
| 1.1 Axis standardization | 49 chapters with inconsistent axes; visual system degrades at scale | Consistent visual language across all payoff charts |
| 1.2 Visual templates | Ad hoc diagram creation per chapter; inconsistent format | Reusable templates reduce per-chapter visual effort and ensure consistency |
| 1.3 Family transitions | Abrupt family shifts (the ELN→Swaps transition in the pilot was flagged as jarring) | Smooth reader orientation at each family boundary |
| 1.4 Within-family bridges | Reader must mentally compare to previous chapter; higher cognitive load | Immediate anchoring to prior knowledge; progressive complexity is explicit |
| 1.5 Jargon watchlist | 6 terminology violations per 5 chapters = ~55 violations at 49 chapters | Proactive screening catches violations during generation, not during review |

---

## 2. High-Value Improvements

These items address the "teaching valley" in Parts 3-4 and the reinforcement gaps in Part 1. They improve the book's architecture significantly but are not strictly required for Part 5 generation. Best applied as a targeted revision pass between generation batches.

| # | Change | Dimension | Files Affected | Effort |
|:-:|--------|:---------:|----------------|:------:|
| 2.1 | **Add one worked scenario per Part 4 matrix.** Each major matrix (4.1 ELN, 4.4 Swaps, 4.5 SRT, 4.6 STEG, 4.7 CLN) gets a "client need → matrix lookup → product recommendation" walkthrough. Example already exists for 4.1 (added during educational review) — replicate pattern for 4.4-4.7 | B, C (Load, Voice) | Desk_Bible_v2.md (4 insertions, ~400 words) | Medium |
| 2.2 | **Add one-sentence product descriptions to all Part 3 family trees.** Each product in the tree gets a brief description of its distinctive feature. The ELN tree (3.3) already has these (e.g., "DRC — Instead of a coupon, investor buys at a discount"). Ensure all 6 trees follow this pattern consistently | B, C (Load, Voice) | Desk_Bible_v2.md (verify 6 trees) | Small |
| 2.3 | **Add integrated worked example to Section 1.4 (Greeks).** A single scenario showing: "You sold a put with Delta -0.50, Gamma 0.03, Theta -$5/day, Vega $2 per vol point. The stock drops $2. Calculate your new Delta, one-day P&L from each Greek, and net P&L." This makes all Greeks concrete simultaneously | B (Load) | Desk_Bible_v2.md (1 insertion, ~200 words) | Small |
| 2.4 | **Standardize reinforcement devices across Parts 1-4.** Add Common Mistakes sections to: 1.1, 1.2, 1.4, 1.5, 1.6, 1.7, 1.8, 1.9 (where missing). Add Desk Perspective tables to: 1.2, 1.4, 1.5. These are the sections most directly relevant to desk roles | C, F (Voice, Retention) | Desk_Bible_v2.md (~8 additions, ~400 words) | Medium |
| 2.5 | **Add Professor Notes to key Part 1 and Part 3 sections.** Target: 1.2 (Options), 1.4 (Greeks), 1.5 (Volatility), 1.6 (Correlation), 3.1 (Family Overview). One sentence each, following the Part 2 and Part 5 pattern: "If you remember only one thing..." | C, F (Voice, Retention) | Desk_Bible_v2.md (5 insertions, ~100 words) | Small |
| 2.6 | **Add inter-Part bridge paragraphs.** Between Part 1 → Part 2, Part 2 → Part 3, Part 3 → Part 4, Part 4 → Part 5. 2-3 sentences each: "You now know X. Next, Y. This matters because Z." The bridge between 1.6 → 1.7 already demonstrates this pattern effectively | A (Curriculum) | Desk_Bible_v2.md (4 insertions, ~200 words) | Small |

**Total estimated effort for Section 2:** 4-6 hours. Can be applied as a single revision pass or distributed across generation batches.

### Estimated Impact

| Change | Impact Level | Rationale |
|--------|:-----------:|-----------|
| 2.1 Part 4 scenarios | HIGH | Converts 5 dense reference tables into teaching moments. The single existing scenario (4.1) demonstrates the pattern works |
| 2.2 Part 3 descriptions | MEDIUM | Reduces cumulative cognitive load from 44 unanchored product names |
| 2.3 Greeks worked example | HIGH | The single highest-impact addition to Part 1. Four reviewers flagged this gap |
| 2.4 Reinforcement standardization | MEDIUM | Eliminates device inconsistency; establishes Common Mistakes and Desk Perspective as universal |
| 2.5 Professor Notes | MEDIUM | Extends the strongest single-sentence teaching device to the sections that need it most |
| 2.6 Inter-Part bridges | MEDIUM | Reduces the "teaching valley" perception; creates narrative continuity across the full document |

---

## 3. Nice-to-Have Improvements

These items polish the architecture without changing the learning experience materially. Apply during a final review pass after all Part 5 chapters are written.

| # | Change | Dimension | Effort |
|:-:|--------|:---------:|:------:|
| 3.1 | **Add mid-Part 1 knowledge check** after Section 1.6 (the equity/rates boundary). 3 review questions + 1 scenario. Provides a reinforcement break before the rates material begins | F (Retention) | Small |
| 3.2 | **Add cumulative milestone assessments** at the Part 2 → Part 3 boundary ("you can now deconstruct any structured product") and the Part 4 → Part 5 boundary ("you can now classify and compare any product — next you'll master them individually"). 2-3 cumulative questions each | F (Retention) | Small |
| 3.3 | **Add one procedural exercise per Part.** Beyond conceptual Knowledge Check questions, add one exercise requiring the reader to: calculate a P&L (Part 1), decompose a coupon (Part 2), classify a product by all 6 dimensions (Part 3), recommend a product from a matrix (Part 4) | G (Readiness) | Small |
| 3.4 | **Add diagrams to Part 0 key sections.** 0.7 (banking ecosystem map), 0.11 (investment banking organizational diagram), 0.12 (FO/MO/BO flow). These are specified in the curriculum but not present in the text | E (Visual) | Medium |
| 3.5 | **Extend Desk Perspective tables to Part 1 key sections** (1.2 Options, 1.4 Greeks, 1.5 Volatility). Show how each desk role uses these foundational concepts daily | G (Readiness) | Small |
| 3.6 | **Add unifying theme callouts to STEG (3.6) and Other (3.8) family trees.** Currently present in ELN (3.3), Swaps (3.4), SRT (3.5), and CLN (3.7) but missing from STEG and Other | C (Voice) | Trivial |
| 3.7 | **Consider moving model risk from Section 1.9 (Credit Risk) to a standalone subsection or end-of-Part-1 position.** Model risk applies to all derivatives (equity, rates, credit), not just credit. Its placement within the credit section is technically accurate (it was introduced there in context) but architecturally suboptimal | D (Dependency) | Small |

**Total estimated effort for Section 3:** 3-4 hours. Best applied as a polish pass after Part 5 generation is complete.

---

## 4. Estimated Impact Summary

### By Dimension

| Dimension | Current Score | After Must-Do (§1) | After High-Value (§2) | After Nice-to-Have (§3) |
|-----------|:------------:|:-------------------:|:---------------------:|:-----------------------:|
| A. Curriculum Progression | 8.0 | 8.5 | 9.0 | 9.0 |
| B. Cognitive Load | 7.5 | 7.5 | 8.5 | 8.5 |
| C. Professor Voice | 7.0 | 7.0 | 8.0 | 8.5 |
| D. Knowledge Dependency | 8.5 | 9.0 | 9.0 | 9.0 |
| E. Visual System | 5.5 | 7.0 | 7.0 | 7.5 |
| F. Retention Design | 7.0 | 7.0 | 7.5 | 8.5 |
| G. Practitioner Readiness | 7.5 | 7.5 | 7.5 | 8.0 |
| **Composite** | **7.3** | **7.6** | **8.1** | **8.4** |

### By Priority

| Priority | Item Count | Total Effort | Composite Impact |
|----------|:---------:|:------------:|:----------------:|
| Must-Do (§1) | 5 items | 3-4 hours | +0.3 (7.3 → 7.6) |
| High-Value (§2) | 6 items | 4-6 hours | +0.5 (7.6 → 8.1) |
| Nice-to-Have (§3) | 7 items | 3-4 hours | +0.3 (8.1 → 8.4) |
| **Total** | **18 items** | **10-14 hours** | **+1.1 (7.3 → 8.4)** |

---

## 5. Estimated Effort

### By Change Type

| Type | Items | Effort per Item | Total |
|------|:-----:|:---------------:|:-----:|
| Template/convention creation (1.1, 1.2, 1.5) | 3 | 30-60 min | 1.5-3 hr |
| One-time text insertions (1.3, 2.3, 2.5, 2.6, 3.1, 3.2) | 6 | 15-30 min | 1.5-3 hr |
| Standardization passes (2.2, 2.4, 3.6) | 3 | 30-60 min | 1.5-3 hr |
| Per-chapter application (1.4, 1.5, 2.1) | 3 | 5-10 min per chapter | Distributed |
| Structural additions (3.3, 3.4, 3.5, 3.7) | 4 | 15-45 min | 1-3 hr |
| **Total** | **18** | — | **10-14 hr** |

### Recommended Application Schedule

| Phase | When | Items | Rationale |
|-------|------|-------|-----------|
| **Pre-scaling** | Before generating Chapter 6 (DRC) | §1 items (1.1-1.5) | Establishes conventions that all remaining chapters follow |
| **During scaling — Batch 1** | After first 10 chapters generated | §2 items (2.1-2.6) | Revision pass on Parts 1-4 while generation is in progress |
| **Post-scaling** | After all 49 product chapters complete | §3 items (3.1-3.7) | Final polish pass across the full document |

---

## Dependencies and Sequencing

```
§1.1 (axis convention) ──→ §1.2 (visual templates) ──→ applied to all new chapters
§1.3 (family transitions) ──→ applied at each family boundary during generation
§1.4 (within-family bridges) ──→ applied to each new chapter during generation
§1.5 (jargon watchlist) ──→ used during generation and review

§2.1 (Part 4 scenarios) ──→ independent, can apply any time
§2.2 (Part 3 descriptions) ──→ independent, can apply any time
§2.3 (Greeks worked example) ──→ independent, can apply any time
§2.4 (reinforcement devices) ──→ independent, can apply any time
§2.5 (Professor Notes) ──→ independent, can apply any time
§2.6 (inter-Part bridges) ──→ independent, can apply any time

§3 items ──→ all independent, all post-scaling
```

No item in Section 2 or 3 blocks Section 1. No item in Section 3 blocks Section 2. The only sequencing constraint is §1.1 → §1.2 (axis convention must be set before templates are built).

---

*Action plan generated 2026-06-19. Based on book architecture review (7 dimensions, 8 review agents). Both reports complete.*

*STOP. No additional product chapters will be generated until approval is received.*
