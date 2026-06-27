# Visual Standard

**Version:** 1.2
**Date:** 2026-06-20
**Scope:** All visual elements in Desk Bible v2 — inline ASCII diagrams and Publication Asset specifications
**Cross-reference:** `audit/visualization_plan.md` (53-visual master plan), `review/visual_design_report.md`
**Changelog:** v1.0 baseline. v1.2 adds Publication Asset specification format, figure reference convention, and asset filename convention. ASCII diagrams remain for inline illustration; Publication Assets are the production visual format.

---

## 1. Payoff Diagram Conventions

### Axis Standards

| Product Domain | Y-Axis Label | X-Axis Label |
|---------------|-------------|-------------|
| Equity-linked (ELN) | Investor Return (%) | Underlying at Maturity (% of Initial) |
| Credit-linked (CLN) | Investor Return (%) | Credit Outcome |
| Rates (SRT, STEG) | P&L ($) | Market Rate (%) |
| Swaps | P&L ($) | Market Rate (%) or Reference Level |

### Barrier Notation

```
Investor
Return (%)
    |
    |  .................... ← Barrier Level (70%)
    |  :                 :
    |  :   LOSS ZONE     :
    |  :                 :
----+--:--+---------+----:--→ Underlying at Maturity
    |  :  70%      100%  :     (% of Initial)
    |  :                 :
```

- Barrier level: horizontal dashed line (`.....` in ASCII)
- Zone labels: LOSS ZONE below barrier, PROTECTION ZONE above barrier
- Strike level: solid horizontal line at 100% (or marked explicitly)
- Coupon line: horizontal line above 0% showing the fixed coupon level

### Template — Standard Payoff Chart

```
Investor
Return (%)
    |
+8% |─────────────────────────────
    |                     ╱
 0% |────────────────────╱────────
    |                   ╱
    |   .............. ╱ ← Barrier (70%)
    |  ╱              :
    | ╱   LOSS ZONE   :
    |╱                :
----+--+----+----+----+----+──→
       60%  70%  80%  100%  120%
       Underlying at Maturity (% of Initial)
```

### Rules

1. Maximum width: 60 characters
2. Always label barrier levels with percentage and the word "Barrier"
3. Always show the 0% return line
4. Always show the 100% underlying level (initial price)
5. Use `╱` and `╲` for diagonal lines, `─` for horizontal lines, `│` for vertical lines
6. Include a caption below the diagram describing what the reader should notice

---

## 2. Timeline Conventions

### Format

Horizontal layout, left-to-right, with events marked above or below the timeline.

### Template — Product Lifecycle Timeline

```
    Trade     Q1 Obs    Q2 Obs    Q3 Obs    Q4 Obs    Maturity
    Date      ↓         ↓         ↓         ↓         ↓
────┬─────────┬─────────┬─────────┬─────────┬─────────┬────
    │         │         │         │         │         │
    Buy       Coupon    Coupon    No        Coupon    Final
    Note      Paid      Paid     Coupon    + Memory  Redemption
              ($2,500)  ($2,500) (missed)  ($7,500)
```

### Rules

1. Time flows left to right
2. Event markers use `↓` above the timeline and `│` below
3. Payment events include dollar amounts in parentheses
4. Missed/skipped events are explicitly labeled
5. Key state changes (barrier breach, autocall trigger) use bold text or `***` markers
6. Maximum width: 70 characters
7. Always label start (Trade Date) and end (Maturity or Autocall)

### Template — Cash Flow Bar Timeline (for Swaps/Rate Products)

```
Year 1        Year 2        Year 3        Year 4        Year 5
  │             │             │             │             │
  │  Fixed      │  Fixed      │  Fixed      │  Fixed      │  Fixed
  │  +$300k     │  +$300k     │  +$300k     │  +$300k     │  +$300k
  │  ▲          │  ▲          │  ▲          │  ▲          │  ▲
──┼──┼──────────┼──┼──────────┼──┼──────────┼──┼──────────┼──┼──
  │  ▼          │  ▼          │  ▼          │  ▼          │  ▼
  │  Floating   │  Floating   │  Floating   │  Floating   │  Floating
  │  -$250k     │  -$350k     │  -$400k     │  -$380k     │  -$420k
  │             │             │             │             │
  Net: -$50k    Net: +$50k    Net: +$100k   Net: +$80k    Net: +$120k
```

---

## 3. Decision Tree Conventions

### Format

Top-down branching with labeled nodes and YES/NO paths.

### Template — Observation Date Decision Tree

```
              ┌─────────────────┐
              │ OBSERVATION DATE │
              └────────┬────────┘
                       │
              ┌────────┴────────┐
              │ Is Underlying   │
              │ ≥ Autocall      │
              │ Level?          │
              └────┬───────┬────┘
                YES│       │NO
                   ▼       ▼
           ┌───────────┐  ┌──────────────────┐
           │ AUTOCALL   │  │ Is Underlying    │
           │ Product    │  │ ≥ Coupon Barrier?│
           │ redeems at │  └───┬──────────┬───┘
           │ par + cpn  │   YES│          │NO
           └───────────┘      ▼          ▼
                      ┌──────────┐  ┌──────────┐
                      │ Coupon   │  │ No coupon │
                      │ PAID     │  │ (memory   │
                      │          │  │ +1)       │
                      └──────────┘  └──────────┘
                              │           │
                              └─────┬─────┘
                                    │
                              ┌─────┴─────┐
                              │ NEXT OBS  │
                              │ DATE      │
                              └───────────┘
```

### Rules

1. Flow direction: top to bottom
2. Decision nodes: rectangles with questions
3. Outcome nodes: rectangles with results
4. Branch labels: YES/NO or specific conditions
5. Loop indicators: arrow back to top with "NEXT OBS DATE" or "REPEAT"
6. Maximum depth: 4 levels (deeper trees should be split into sub-trees)
7. Use box-drawing characters: `┌ ┐ └ ┘ ─ │ ┬ ┴ ├ ┤`

---

## 4. Waterfall Diagram Conventions

### Purpose

Show how a structured product's economics decompose from the investor's $100 into components.

### Template — Construction Waterfall

```
$100.00  ┌──────────────────────────┐  Investor's Principal
         │                          │
         ├──────────────────────────┤
$88.90   │  Zero-Coupon Bond        │  Grows to $100 at maturity
         │  (Funding Component)     │
         ├──────────────────────────┤
$11.10   │  Available for Options   │
         ├────────────┬─────────────┤
$9.60    │  Call       │  $1.50     │
         │  Option     │  Desk      │
         │  Budget     │  Margin    │
         └────────────┴─────────────┘
                │
                ▼
         Participation Rate = $9.60 / (call price per $100 notional)
```

### Rules

1. Flow direction: top to bottom (money flowing from investor's principal into components)
2. Dollar amounts on the left margin
3. Component names and descriptions inside boxes
4. Margin and FTP always shown explicitly
5. Final line shows the resulting product parameter (participation rate, coupon, etc.)
6. Maximum width: 50 characters

---

## 5. Comparison Table Conventions

### Format

Side-by-side comparison of the current product against its closest relative or a benchmark.

### Template — Product Comparison

```
                    │  [Product A]     │  [Product B]
────────────────────┼──────────────────┼──────────────────
Coupon              │  Fixed 8%        │  Conditional
Barrier             │  70% KI          │  70% KI (capital)
                    │                  │  + 80% (coupon)
Autocall            │  No              │  Yes (quarterly)
Memory              │  N/A             │  Yes
Best case           │  8% + principal  │  Autocall at par
Worst case          │  Loss below 70%  │  Loss below 70%
Complexity          │  Simple          │  Complex
System              │  NEMO/Sophis     │  NEMO/Sophis
```

### Rules

1. Always compare to the most closely related product the reader has already learned
2. Highlight the single key difference in the comparison (bold or annotation)
3. Include: Coupon, Barrier, Autocall, Protection, Complexity, System at minimum
4. Maximum 3 products per comparison (2 recommended)
5. Use column alignment with `│` separators

---

## 6. Color Conventions (for Production Rendering)

These conventions apply to production-quality visuals specified in Visual Learning Recommendations. They do not affect inline ASCII diagrams.

| Color | Usage |
|-------|-------|
| Green | Investor profit, coupon received, above barrier, favorable outcome |
| Red | Investor loss, barrier breach, capital risk zone, unfavorable outcome |
| Blue | Autocall / early redemption events |
| Gold | Memory payout, accumulated coupon |
| Gray | Neutral zone, zero-return region, time passing without event |
| Orange | Warning, conditional zone (coupon at risk but not yet lost) |
| Black | Axes, labels, structural elements |

---

## 7. Labeling Conventions

### Diagram Labels

| Element | Label Format | Example |
|---------|-------------|---------|
| Barrier level | "Barrier (XX%)" | "Barrier (70%)" |
| Strike level | "Strike (XX%)" or "Initial Level" | "Initial Level (100%)" |
| Coupon level | "+X%" or "+$X" | "+8%" |
| Autocall level | "Autocall (XX%)" | "Autocall (100%)" |
| Observation dates | "Q1", "Q2", ... or "Year 1", "Year 2", ... | "Q1 Obs" |
| CMS rates | "CMSXY" where X=maturity, Y=unit | "CMS30Y", "CMS2Y" |
| Swap legs | "Fixed Payer" / "Floating Payer" | — |

### Axis Labels

- Always include units: (%), ($), (bp)
- Always include the reference point: "% of Initial", "Market Rate"
- Font size in production: axis labels = 10pt, tick labels = 8pt, title = 12pt

---

## 8. Publication Asset Specification Format (v1.2)

Every chapter must include at least 5 Publication Asset specifications. These specifications are production-ready briefs — detailed enough that a designer can build the graphic without reading the chapter.

**v1.0/v1.1 chapters** used "Visual Learning Recommendations" (informal) or "Visual Specifications" (semi-formal). **v1.2 chapters** use the full Publication Asset format below.

### Required Fields

| Field | Description | Example |
|-------|------------|---------|
| **Figure Number** | `Figure 5.X.Y-##` | `Figure 5.2.6-01` |
| **Visual ID** | `TYPE_PRODUCT_##` | `PAYOFF_CCY_SWAP_01` |
| **Type** | One of the allowed types (see below) | `Cash Flow Diagram` |
| **Priority** | P1 / P2 / P3 | `P1` |
| **Purpose** | One sentence | `Illustrate exchange of principal and interest in two currencies` |
| **Visual Description** | 2-3 sentences for designer | `Two-column layout showing Party A and Party B with arrows...` |
| **Diagram Elements** | Bulleted list of all elements | `Party A, Party B, Currency A flows, Currency B flows` |
| **Axis Definitions** | Y-axis, X-axis, ticks (charts only) | `Y: P&L ($), X: Exchange Rate (USD/EUR)` |
| **Caption** | Publication-ready text | `Currency Swap Cash Flow Structure` |
| **Location** | Section reference | `§7` |
| **Reuse Potential** | High / Medium / Low | `High` |
| **Future Asset Filename** | `type_product_##.svg` | `payoff_currency_swap_01.svg` |

### Allowed Visual Types

Payoff Diagram, Timeline, Decision Tree, Cash Flow Diagram, Waterfall Diagram, Lifecycle Diagram, System Flow Diagram, Comparison Chart, Balance Sheet Illustration.

### Priority Definitions

- **P1:** Essential for comprehension. Would be included in a one-page summary of the product
- **P2:** High value for teaching. Adds significant comprehension but the chapter is functional without it
- **P3:** Enrichment. Useful for deep understanding or specific roles

### Priority Distribution Per Chapter

| Minimum | Count |
|---------|:-----:|
| P1 | 2 |
| P2 | 2 |
| P3 | 1 |
| **Total** | **5** |

At least one visual must be unique to the product (not a reused template from another chapter).

### Figure References

Every visual specification must have a corresponding inline reference in the chapter body:

```
The two-way cash flow structure is shown below. (See Figure 5.2.6-01)
```

This enables future automatic replacement of ASCII diagrams with SVG/PNG publication assets. ASCII diagrams are temporary — no ASCII diagram should be considered final publication output.

### Asset Filename Convention

```
type_product_##.svg
```

Examples:
- `payoff_currency_swap_01.svg`
- `lifecycle_commodity_swap_01.svg`
- `decision_tree_cds_01.svg`

---

*Standard v1.0 effective 2026-06-19. v1.2 update effective 2026-06-20. Publication Asset format applies from Batch 5 onward.*
