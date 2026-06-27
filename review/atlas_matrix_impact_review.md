# Atlas-to-Matrix Impact Review

**Date:** 2026-06-22
**Scope:** Workstream 7 — Assess whether accepted enhancements conflict with Comparison Matrix generation
**Framework:** v1.3.1 (frozen)

---

## Context

Three enhancements were accepted in the Final Enhancement Review:

1. **Common Interview Questions** — 49 product-specific questions (Appendix E)
2. **Product Confusion Pairs** — ~25 pairs with key differentiators (Appendix F)
3. **Learning Difficulty** — 49 conceptual-barrier descriptions (Appendix G)

The Comparison Matrix will consume:
- Manuscript §4 CM fields (10 dimensions × 49 products)
- Publication taxonomy (6 dimensions, 31 canonical categories)
- Complexity registry (49 scores)
- DNA Atlas (product identity, naming, section numbers)

---

## Impact Assessment

### Enhancement 1: Common Interview Questions

| Criterion | Assessment |
|-----------|-----------|
| Does it help Matrix generation? | **NO** — Matrix consumes CM fields, not interview questions. Questions are educational, not structural. |
| Does it duplicate Matrix functionality? | **NO** — Matrix compares quantitative dimensions (complexity, yield potential, liquidity). Questions test conceptual understanding. Zero overlap. |
| Does it create taxonomy conflicts? | **NO** — Questions are free-text, not categorical. No taxonomy interaction. |
| Does it create maintenance burden? | **MINIMAL** — Questions are structurally stable. Adding a new product requires one new question. |
| Does Matrix depend on this? | **NO** — Matrix generators would not read or consume Appendix E. |

**Classification: SAFE**

No interaction with Matrix generation pipeline. Fully independent content layer.

---

### Enhancement 2: Product Confusion Pairs

| Criterion | Assessment |
|-----------|-----------|
| Does it help Matrix generation? | **INDIRECT** — Confusion pairs highlight which products need strong differentiation in the Matrix. But the Matrix generates from CM fields, not from pairs. |
| Does it duplicate Matrix functionality? | **PARTIAL** — The Matrix provides side-by-side comparison across 10 dimensions. Confusion pairs provide a 1-sentence differentiator. Different granularity, same intent. |
| Does it create taxonomy conflicts? | **NO** — Pairs are descriptive, not categorical. No new taxonomy dimensions. |
| Does it create maintenance burden? | **MINIMAL** — Pairs are structurally stable (PPN vs RC will always be a confusion pair). |
| Does Matrix depend on this? | **NO** — But Matrix output could be cross-validated against confusion pairs to ensure the differentiating dimension is visible in the Matrix columns. |

**Classification: CAUTION**

The Comparison Matrix will provide richer, multi-dimensional comparison between any two products. The confusion pairs provide a quick, memorable differentiator. These are complementary, not conflicting, but there is a risk of inconsistency:

**Risk scenario:** Confusion pair says "PPN buys protection, RC sells protection." Matrix shows both have "Conditional" capital protection in different categories. A reader could perceive contradiction if the Matrix categories don't cleanly map to the pair's language.

**Mitigation:** When generating the Matrix, verify that the confusion pair's key difference is reflected in at least one Matrix dimension for each pair.

---

### Enhancement 3: Learning Difficulty

| Criterion | Assessment |
|-----------|-----------|
| Does it help Matrix generation? | **NO** — Matrix compares product characteristics, not learning barriers. |
| Does it duplicate Matrix functionality? | **NO** — "What makes this product difficult to understand" is not a Matrix dimension. |
| Does it create taxonomy conflicts? | **NO** — Free-text descriptions, not categorical. |
| Does it create maintenance burden? | **MINIMAL** — Learning barriers are structural (VarSwap convexity will always be the hard part). |
| Does Matrix depend on this? | **NO** — Fully independent. |

**Classification: SAFE**

No interaction with Matrix generation pipeline. Purely educational layer.

---

## Impact Summary

| Enhancement | Classification | Matrix Dependency | Taxonomy Risk | Duplication Risk |
|------------|:--------------:|:-----------------:|:-------------:|:----------------:|
| Interview Questions | **SAFE** | None | None | None |
| Confusion Pairs | **CAUTION** | None (indirect validation value) | None | Partial (different granularity) |
| Learning Difficulty | **SAFE** | None | None | None |

---

## Pre-Matrix Generation Checklist

If enhancements are implemented before Matrix generation:

| # | Check | Purpose |
|:-:|-------|---------|
| 1 | Verify confusion pair key differences don't contradict Matrix CM categories | Consistency |
| 2 | Verify no new taxonomy dimensions were introduced | Taxonomy integrity |
| 3 | Verify Atlas section numbers unchanged | Matrix cross-reference stability |
| 4 | Verify no complexity scores were modified | Registry consistency |
| 5 | Verify no family assignments were changed | Classification consistency |

All checks are expected to pass — none of the accepted enhancements modify structural data.

---

## Recommendation

**All three enhancements are safe to implement before Matrix generation.** The one CAUTION item (Confusion Pairs) requires a post-implementation cross-check against Matrix output but does not block generation.

Recommended implementation order:
1. Learning Difficulty (Appendix G) — SAFE, highest educational value
2. Interview Questions (Appendix E) — SAFE, highest interview value
3. Confusion Pairs (Appendix F) — CAUTION, implement last, cross-check against Matrix

---

*Matrix impact review complete.*
