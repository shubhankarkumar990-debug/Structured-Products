# Payoff Chart Masterclass — Design Review

**Date:** 2026-06-21
**Proposed Section:** Part 1.10 — How to Read and Create Payoff Charts
**Framework:** v1.3.1 (FROZEN)
**Purpose:** Assess design for a standalone payoff chart literacy section
**Implementation:** After 49/49, during harmonization

---

## 1. Recommended Placement

**Section 1.10** — immediately after Section 1.9 (Credit Risk), completing Part 1 (Building Blocks).

**Rationale:** Part 1 teaches concepts. Sections 1.1-1.9 introduce all the building blocks (options, barriers, Greeks, volatility, correlation, rates, credit). Section 1.10 closes Part 1 by teaching the reader how to *read the diagrams* that appear in every product chapter.

**Alternative considered:** Part 2.x (after Product Construction). Rejected — readers encounter payoff charts in Part 1 itself (options, barriers). The skill is needed *before* Part 2.

**Dependency chain:**
```
1.1 (Core Trading) → 1.2 (Options) → 1.3 (Barriers) → ... → 1.10 (Payoff Charts)
                                                                      │
                                                                      ▼
                                                              Part 2 (Product Construction)
                                                                      │
                                                                      ▼
                                                              Part 5 (All product chapters §21)
```

---

## 2. Dependencies

| Prerequisite | Section | Why Needed |
|-------------|---------|-----------|
| Long/short concept | 1.1 | Reader must understand position direction |
| Option payoff (call/put) | 1.2 | Payoff charts built on option payoffs |
| Barrier mechanics (KI/KO) | 1.3 | Discontinuous payoff charts |
| Digital payoff | 1.3 | Step-function charts |
| Greeks (delta as slope) | 1.4 | Slope interpretation |
| Correlation (worst-of) | 1.6 | Multi-asset payoff interpretation |

**All prerequisites already taught in 1.1-1.9.** No new dependencies.

---

## 3. Learning Objectives

By the end of Section 1.10, the reader will be able to:

| # | Objective | Assessment Method |
|:-:|-----------|:-----------------:|
| 1 | Read any payoff diagram in the book and identify: the investor's gain/loss at each price level | Knowledge Check |
| 2 | Identify the breakeven point on a payoff chart | Knowledge Check |
| 3 | Distinguish between linear, kinked, capped, floored, and digital payoff shapes | Visual matching exercise |
| 4 | Decompose a complex payoff into its component shapes (bond + option + barrier) | Construction exercise |
| 5 | Interpret axis conventions: X = underlying at maturity (% of initial), Y = investor return (% of notional) | Convention check |
| 6 | Recognize how barriers create discontinuities in payoff diagrams | Scenario question |
| 7 | Read a multi-scenario comparison chart (Vanilla vs Structured) | Comparison exercise |
| 8 | Sketch a rough payoff diagram from a term sheet description | Desk question |

---

## 4. Section Structure

| Subsection | Content | Est. Words |
|-----------|---------|:----------:|
| **1.10.1 — Why Payoff Charts Matter** | Every product chapter has payoff diagrams. This section teaches you to read them. The payoff chart is the universal language of structured products | 200 |
| **1.10.2 — The Axes** | X-axis: underlying price at maturity (% of initial level). Y-axis: investor return (% of notional). Origin: initial level. Convention: 100% = par | 300 |
| **1.10.3 — The Five Basic Shapes** | Linear (forward), kinked (option), capped (cap), floored (floor), step (digital). Each with diagram and one-sentence description | 500 |
| **1.10.4 — Reading a Bond Payoff** | Flat line at coupon level. No market exposure. This is the baseline | 200 |
| **1.10.5 — Reading an Option Payoff** | Hockey stick. Long call slopes up from strike. Long put slopes down from strike. Short positions mirror. Delta = slope | 400 |
| **1.10.6 — Reading a Barrier Payoff** | KI: payoff appears only below/above barrier. KO: payoff disappears at barrier. Discontinuity point. Before vs after barrier | 400 |
| **1.10.7 — Combining Shapes** | Bond + Short Put = Reverse Convertible. Bond + Call Spread = PPN. Show construction by layering. Decomposition in reverse | 500 |
| **1.10.8 — The Comparison Chart** | Side-by-side: structured product vs direct investment vs bond. How to read grouped bars and overlaid lines | 300 |
| **1.10.9 — Common Traps** | (1) Confusing percentage return with dollar return. (2) Forgetting that the X-axis is at maturity, not during life. (3) Reading a payoff chart as a price chart. (4) Ignoring the coupon component | 300 |
| **1.10.10 — Exercises** | 5 payoff charts to interpret. 3 term sheets to sketch. 1 decomposition exercise | 400 |
| **Total** | | **~3,500** |

---

## 5. Estimated Length

| Metric | Value |
|--------|:-----:|
| Word count | ~3,500 |
| Pages (est.) | 8-10 |
| Visual assets | 10-12 (more than standard chapter — teaching visual literacy requires many examples) |
| Knowledge Check | Yes (Review + Scenario + Desk) |

---

## 6. Visual Requirements

| # | Visual | Type | Purpose |
|:-:|--------|------|---------|
| 1 | Axis convention diagram | Reference | Define X/Y axes, origin, scale |
| 2 | Five basic shapes (one panel each) | Payoff set | Linear, kinked, capped, floored, step |
| 3 | Bond payoff (flat line) | Payoff | Baseline reference |
| 4 | Long call payoff | Payoff | Hockey stick up |
| 5 | Long put payoff | Payoff | Hockey stick down |
| 6 | Short put payoff | Payoff | Inverted hockey stick |
| 7 | KI barrier payoff (before/after) | Payoff | Discontinuity |
| 8 | KO barrier payoff (before/after) | Payoff | Disappearing section |
| 9 | RC construction (bond + short put = RC) | Construction | Layered build-up |
| 10 | PPN construction (bond + call spread = PPN) | Construction | Layered build-up |
| 11 | Comparison chart example | Comparison | Structured vs direct vs bond |
| 12 | "What's wrong?" exercise diagram | Exercise | Intentionally mislabeled for reader to identify errors |

---

## 7. Interaction with Existing Product Chapters

| Interaction | Detail |
|------------|--------|
| **Forward reference from 1.10 → Part 5** | "When you reach the product chapters, every §21 (Visual Specifications) references payoff diagrams. You now have the tools to read them." |
| **Back reference from product §9 → 1.10** | Product chapters' Three Scenarios (§9) can reference 1.10 for payoff interpretation. Optional — does not require chapter modification |
| **Foundation for §21 visual specs** | All product visual specs assume the reader understands payoff chart conventions. Section 1.10 makes this explicit |
| **Supports front matter Learning Paths** | Beginner path includes 1.10 as mandatory. Trader/Structurer paths reference it as prerequisite |

**No existing chapter modifications required.** Section 1.10 is additive.

---

## 8. Assessment

| Criterion | Score |
|-----------|:-----:|
| Educational impact | **HIGH** — fills a gap; currently readers must infer chart conventions |
| Effort | **MEDIUM** — ~3,500 words, 12 visuals, standalone section |
| Publication value | **HIGH** — makes the book self-contained for chart literacy |
| Reader value | **VERY HIGH** — unlocks every visual in the book |
| Risk | **LOW** — no framework modification, no chapter changes |

**Recommendation: PROCEED.** Implement after 49/49, before harmonization pass.

---

*Payoff Chart Masterclass Design Review completed 2026-06-21.*
