# Product DNA Atlas — Design Review

**Date:** 2026-06-21
**Proposed Section:** Part 6 — Product DNA Atlas
**Framework:** v1.3.1 (FROZEN)
**Purpose:** One-page quick-reference sheet for every product
**Implementation:** After 49/49, after harmonization

---

## 1. Concept

Each product chapter runs 3,000-6,500 words. Readers frequently need a quick-lookup reference — not the full chapter. The Product DNA Atlas provides a standardized one-page "card" for every product: 13 fields, same layout, scannable in 30 seconds.

**Distinction from product chapters:**

| Aspect | Product Chapter (Part 5) | DNA Atlas (Part 6) |
|--------|:------------------------:|:-------------------:|
| Purpose | Teach everything about this product | Quick-reference lookup |
| Length | 3,000-6,500 words | ~250 words (one page) |
| Reading time | 15-30 minutes | 30 seconds |
| Use case | First learning | Desk reference, comparison, interview prep |

---

## 2. Card Layout — 13 Fields Per Product

| # | Field | Content | Source |
|:-:|-------|---------|--------|
| 1 | **Product Name** | Official name + common aliases | §1 |
| 2 | **Family** | ELN / Swaps / SRT / STEG / CLN / Other | Registry |
| 3 | **Complexity Score** | 1-10 with one-line justification | complexity_registry.yaml |
| 4 | **Capital Protection** | Full / Conditional / None + mechanism | §6 |
| 5 | **Coupon Profile** | Fixed / Conditional / Memory / None + typical range | §7-§8 |
| 6 | **Primary Risk** | The single biggest risk to the investor, in one sentence | §10 |
| 7 | **Typical Buyer** | Retail / HNW / Institutional + objective (yield, protection, access) | §3 |
| 8 | **Typical Use Case** | One sentence: when and why this product is used | §3 |
| 9 | **Building Blocks** | Component list: Bond + [derivative(s)] | §5 |
| 10 | **Key Hedge** | Primary hedge instrument(s) the desk uses | §12 |
| 11 | **Similar Products** | 2-3 closest products with one-word differentiator | §4 |
| 12 | **Most Important Greek** | The Greek that dominates this product's risk profile | §11 |
| 13 | **Chapter Reference** | Section number: "See §5.X.Y for full analysis" | Manuscript |

---

## 3. Page Layout Design

```
┌─────────────────────────────────────────────────┐
│  [FAMILY BADGE]          COMPLEXITY: ██████░░░░  │
│                                          [7/10]  │
│  PRODUCT NAME                                    │
│  ─────────────────────────────────────────────── │
│                                                   │
│  Capital Protection: Conditional (70% KI barrier) │
│  Coupon Profile:     7.2% conditional, memory     │
│  Primary Risk:       Barrier breach → capital loss│
│                                                   │
│  ┌──────────────┐  ┌──────────────────────────┐  │
│  │ BUILDING     │  │ TYPICAL BUYER            │  │
│  │ BLOCKS       │  │ HNW seeking enhanced     │  │
│  │ • Bond       │  │ yield in sideways market  │  │
│  │ • Short KI   │  │                          │  │
│  │   Put        │  │ USE CASE                 │  │
│  │ • Autocall   │  │ Replace bond allocation  │  │
│  │ • Memory     │  │ with higher coupon +     │  │
│  │   coupon     │  │ conditional protection   │  │
│  └──────────────┘  └──────────────────────────┘  │
│                                                   │
│  Key Hedge: Delta-hedge (stock/futures)           │
│  Most Important Greek: Vega (vol drives coupon)   │
│                                                   │
│  Similar: RC (no autocall), Athena (no memory),   │
│           Worst-of AC (multi-asset)               │
│                                                   │
│  ► Full analysis: Section 5.1.5                   │
│                                                   │
└─────────────────────────────────────────────────┘
```

---

## 4. Navigation Model

### 4.1 Organization

Cards organized by family, mirroring Part 5 structure:

```
Part 6 — Product DNA Atlas
├── 6.1 ELN Family (15 cards)
├── 6.2 Swaps Family (8 cards)
├── 6.3 SRT Family (5 cards)
├── 6.4 STEG Family (4 cards)
├── 6.5 CLN Family (5 cards)
└── 6.6 Other Family (7 cards — post-Batch 9)
```

### 4.2 Access Methods

| Method | How |
|--------|-----|
| By family | Browse 6.1-6.6 sections |
| By complexity | Index sorted low→high at start of Part 6 |
| By capital protection | Index: Full → Conditional → None |
| By use case | Cross-reference table: "I want X" → product cards |
| Alphabetical | Back-of-Part-6 alphabetical index |

### 4.3 Cross-References

Each card links to:
- Full chapter (Part 5)
- Solutions Manual answers (Part 7)
- Comparison Matrix entry (if implemented)
- Universe Map position (if implemented)

---

## 5. Visual Requirements

| # | Visual | Type | Purpose |
|:-:|--------|------|---------|
| 1 | Card template (master layout) | Template | Reusable Figma component for all 49 cards |
| 2 | Family color badges (6) | Icon set | ELN=Blue, Swaps=Green, SRT=Purple, STEG=Amber, CLN=Red, Other=Gray |
| 3 | Complexity bar (horizontal gauge) | Component | Visual 1-10 scale on each card |
| 4 | Complexity index (sorted visual) | Chart | All 49 products ranked by complexity |
| 5 | Capital protection index | Chart | Products grouped by protection level |

---

## 6. Maintenance Requirements

| Trigger | Action |
|---------|--------|
| New product added | Generate one new DNA card using template |
| Complexity score revised | Update card field + complexity index |
| Chapter content updated | Verify 13 fields still accurate |
| Family reclassified | Move card to correct family section |

**Maintenance effort: LOW.** Cards are derived from chapter content. No independent research needed. Update only when source chapter changes.

---

## 7. Estimates

| Metric | Value |
|--------|:-----:|
| Cards | 49 (44 after Batch 9 + 5 reserved) |
| Words per card | ~250 |
| Total word count | ~12,250 |
| Pages (print) | ~49 (one per page) |
| Visual assets | 5 (template + badges + bars + 2 indexes) |
| Effort | 5 days |
| Publication value | **HIGH** — most-referenced section after product chapters |
| Reader value | **VERY HIGH** — desk reference, interview prep, quick comparison |

---

## 8. Assessment

| Criterion | Score |
|-----------|:-----:|
| Educational impact | HIGH — consolidates learning into scannable format |
| Effort | LOW-MEDIUM — template-driven, data extraction from existing chapters |
| Publication value | VERY HIGH — professional reference standard |
| Reader value | VERY HIGH — daily desk reference tool |
| Risk | LOW — additive, no modifications |

**Recommendation: PROCEED.** High value, low effort. Template-driven generation after 49/49.

---

*Product DNA Atlas Design Review completed 2026-06-21.*
