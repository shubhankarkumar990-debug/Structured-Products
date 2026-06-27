# Publication Architecture

**Version:** 1.0
**Date:** 2026-06-20
**Purpose:** Define the asset library structure, naming conventions, and cross-reference standards for the Desk Bible v2 publication build (PDF/DOCX)
**Authority:** Governed by Framework Master v1.3 (Section Q)
**Status:** Architecture only. No assets are generated during chapter writing. Asset generation is deferred until all 49 chapters are complete.

---

## 1. Publication Asset Library Structure

```
assets/
├── payoff/
│   ├── payoff_ppn_01.svg
│   ├── payoff_rc_01.svg
│   ├── payoff_phoenix_01.svg
│   └── ...
├── timeline/
│   ├── timeline_phoenix_01.svg
│   ├── timeline_currency_swap_01.svg
│   └── ...
├── decision-tree/
│   ├── decision_tree_phoenix_01.svg
│   ├── decision_tree_cds_01.svg
│   └── ...
├── lifecycle/
│   ├── lifecycle_currency_swap_01.svg
│   ├── lifecycle_commodity_swap_01.svg
│   └── ...
├── cashflow/
│   ├── flow_irs_01.svg
│   ├── flow_currency_swap_01.svg
│   └── ...
├── waterfall/
│   ├── waterfall_ppn_01.svg
│   ├── waterfall_cds_01.svg
│   └── ...
├── system/
│   ├── lifecycle_vlsp_01.svg
│   └── ...
├── comparison/
│   ├── diagram_currency_swap_01.svg
│   ├── diagram_commodity_swap_01.svg
│   └── ...
└── balance-sheet/
    └── (future use)
```

---

## 2. Asset Naming Standards

### 2.1 File Naming Convention

```
type_product_##.svg
```

| Component | Rule | Examples |
|-----------|------|---------|
| **type** | Visual type, lowercase, underscore-separated | `payoff`, `timeline`, `decision_tree`, `lifecycle`, `flow`, `waterfall`, `diagram`, `balance_sheet` |
| **product** | Product name, lowercase, underscore-separated | `ppn`, `rc`, `phoenix`, `irs`, `trs`, `currency_swap`, `commodity_swap`, `vlsp`, `ir_callable` |
| **##** | Two-digit sequential number, starting at 01 | `01`, `02`, `03` |

### 2.2 Type-to-Directory Mapping

| Visual Type (in spec) | Directory | Filename prefix |
|----------------------|-----------|----------------|
| Payoff Diagram | `payoff/` | `payoff_` |
| Timeline | `timeline/` | `timeline_` |
| Decision Tree | `decision-tree/` | `decision_tree_` |
| Lifecycle Diagram | `lifecycle/` | `lifecycle_` |
| Cash Flow Diagram | `cashflow/` | `flow_` |
| Waterfall Diagram | `waterfall/` | `waterfall_` |
| System Flow Diagram | `system/` | `lifecycle_` or `system_` |
| Comparison Chart | `comparison/` | `diagram_` |
| Balance Sheet Illustration | `balance-sheet/` | `balance_sheet_` |

### 2.3 Product Name Abbreviations

| Product | Abbreviation |
|---------|-------------|
| Principal-Protected Note | `ppn` |
| Reverse Convertible | `rc` |
| Phoenix | `phoenix` |
| Interest Rate Swap | `irs` |
| Credit-Linked Note | `cln` |
| Defensive Reverse Convertible | `drc` |
| Knock-Out DRC | `kodrc` |
| Callable Reverse Convertible | `crc` |
| Airbag | `airbag` |
| Bonus Certificate | `bonus` |
| Fixed Coupon Note | `fcn` |
| Conditional Range Accrual ELN | `cra_eln` |
| Issuer Callable Note | `icn` |
| Digital Note | `digital` |
| Booster | `booster` |
| Digital KI Put | `digital_ki_put` |
| Warrant | `warrant` |
| Total Return Swap | `trs` |
| Equity Swap | `equity_swap` |
| Variance Swap | `variance_swap` |
| Credit Default Swap | `cds` |
| Cross-Currency Swap | `currency_swap` |
| Commodity Swap | `commodity_swap` |
| Vanilla Swap (VLSP) | `vlsp` |
| IR Callable | `ir_callable` |
| Zero-Coupon Linked | `zcl` |
| Non-Call Range Accrual | `ncra` |
| CRA (SRT) | `cra_srt` |
| Digital Cap-Floor | `digital_cf` |
| Vanilla STEG | `vanilla_steg` |
| Range Accrual STEG | `ra_steg` |
| Callable STEG | `callable_steg` |
| TARN STEG | `tarn_steg` |
| Skew CLN | `skew_cln` |
| First-to-Default | `ftd` |
| Nth-to-Default | `ntd` |
| Synthetic CDO Tranche | `synth_cdo` |
| Structured Deposit | `struct_deposit` |
| Accumulator | `accumulator` |
| Decumulator | `decumulator` |
| Option on RC | `option_rc` |
| Equity-Linked Option | `elo` |
| Forward | `forward` |
| Vanilla Option | `vanilla_option` |

---

## 3. Figure Numbering Standards

### 3.1 Figure Number Format

```
Figure 5.X.Y-##
```

| Component | Rule |
|-----------|------|
| `5` | Part 5 (Product Chapters) |
| `X` | Family number (1=ELN, 2=Swaps, 3=SRT, 4=STEG, 5=CLN, 6=Other) |
| `Y` | Product number within family |
| `##` | Sequential figure number within chapter, starting at 01 |

### 3.2 Examples

| Product | First Figure | Second Figure |
|---------|-------------|--------------|
| PPN (5.1.1) | Figure 5.1.1-01 | Figure 5.1.1-02 |
| IRS (5.2.1) | Figure 5.2.1-01 | Figure 5.2.1-02 |
| IR Callable (5.3.1) | Figure 5.3.1-01 | Figure 5.3.1-02 |

### 3.3 Figure Number Uniqueness

Figure numbers are globally unique within the book. No two visual specifications share the same figure number.

---

## 4. Visual ID Standards

### 4.1 Visual ID Format

```
TYPE_PRODUCT_##
```

| Component | Rule | Examples |
|-----------|------|---------|
| **TYPE** | Visual type, uppercase | `PAYOFF`, `TIMELINE`, `DECISION_TREE`, `LIFECYCLE`, `FLOW`, `WATERFALL`, `DIAGRAM`, `BALANCE_SHEET` |
| **PRODUCT** | Product abbreviation, uppercase | `PPN`, `RC`, `IRS`, `CCY_SWAP`, `COMM_SWAP`, `VLSP` |
| **##** | Two-digit sequential, starting at 01 | `01`, `02` |

### 4.2 Examples

- `PAYOFF_PPN_01` — first payoff diagram for PPN
- `FLOW_CCY_SWAP_01` — first cash flow diagram for Cross-Currency Swap
- `DECISION_TREE_PHOENIX_01` — first decision tree for Phoenix

---

## 5. Asset Reuse Standards

### 5.1 Template Reuse

Visual templates established in one chapter may be reused in subsequent chapters. When a template is reused:

1. The reused visual gets its own Figure Number and Visual ID (unique to the chapter)
2. The Reuse Potential field in the specification indicates "High" for templates likely to be reused
3. The Visual Template Registry in the generation dashboard tracks all established templates

### 5.2 Reuse Categories

| Category | Rule |
|----------|------|
| **High reuse** | Core structural diagrams (two-party swap flow, barrier payoff, construction waterfall). Reuse across families |
| **Medium reuse** | Family-specific diagrams (observation decision tree, cash flow timeline). Reuse within family |
| **Low reuse** | Product-unique diagrams. Not intended for reuse |

### 5.3 Uniqueness Requirement

Every chapter must have at least one visual with Low reuse potential — a visual that is unique to this product and captures something no other product's visual can.

---

## 6. SVG Generation Standards (Deferred)

**Do not execute until all 49 chapters are complete.**

### 6.1 SVG Technical Requirements

| Parameter | Value |
|-----------|-------|
| Format | SVG 1.1 |
| ViewBox | 700 × 400 (standard), 700 × 300 (compact), 700 × 500 (complex) |
| Fonts | System sans-serif stack: `font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif` |
| Font sizes | Title: 14px, Labels: 12px, Annotations: 10px, Tick marks: 9px |
| Colors | Per visual standard §K.8 |
| Line widths | Axes: 2px, Data lines: 2.5px, Grid lines: 0.5px, Annotations: 1px |
| Accessibility | All text as SVG `<text>`, not paths. `aria-label` on root `<svg>`. `<title>` element with caption |

### 6.2 SVG Template Structure

```xml
<svg viewBox="0 0 700 400" xmlns="http://www.w3.org/2000/svg"
     aria-label="[Caption text]">
  <title>[Caption text]</title>
  <!-- Background -->
  <!-- Grid lines -->
  <!-- Axes -->
  <!-- Data elements -->
  <!-- Labels -->
  <!-- Annotations -->
  <!-- Caption -->
</svg>
```

---

## 7. PNG Generation Standards (Deferred)

**Do not execute until SVG generation is complete.**

| Parameter | Value |
|-----------|-------|
| Resolution | 2x (1400 × 800 pixels for standard 700 × 400 SVG) |
| Format | PNG-24, no interlacing |
| Background | White (#FFFFFF) |
| Compression | Maximum quality, no lossy compression |
| Naming | Same as SVG but with `.png` extension |

---

## 8. DOCX Insertion Standards (Deferred)

**Do not execute until PNG generation is complete.**

### 8.1 Figure Placement

| Rule | Specification |
|------|--------------|
| Position | Inline with text, at the location indicated by the `(See Figure X.Y.Z-##)` reference |
| Width | Full column width (6.5 inches) for standard diagrams, half-width (3.25 inches) for comparison panels |
| Caption | Below the figure, formatted: "**Figure X.Y.Z-##:** [Caption text]" |
| Spacing | 12pt above, 6pt below caption |
| Alt text | Caption text used as alt text for accessibility |

### 8.2 Cross-Reference Format

In the DOCX, figure references become hyperlinked:
```
(See Figure 5.2.6-01)  →  clickable link scrolling to the figure
```

---

## 9. PDF Insertion Standards (Deferred)

**Do not execute until DOCX build is complete.**

| Parameter | Value |
|-----------|-------|
| Source | Generated from DOCX |
| Image format | SVG preferred (vector), PNG fallback (raster) |
| Resolution | 300 DPI minimum for raster elements |
| Bookmarks | Auto-generated from heading structure |
| Table of contents | Auto-generated, 3 levels |
| Page size | A4 (210 × 297 mm) |
| Margins | 25mm all sides |

---

## 10. Cross-Reference Standards

### 10.1 In-Chapter References

```
(See Figure 5.X.Y-##)
```

Every visual specification must have exactly one corresponding inline reference in the chapter body.

### 10.2 Cross-Chapter References

```
Section 5.X.Y (Product Name)
```

Used in bridge text, dependency references, and "Product Evolution" sections.

### 10.3 Part References

```
Section 1.7 (Yield Curves, Spot Rates, and Forward Rates)
Section 1.8 (Benchmark Rates, Swaps, and Rate Options)
Section 1.9 (Credit Risk)
```

Always use the full section title for Parts 0-4 references to avoid ambiguity.

### 10.4 Reference Integrity

Before publication, verify:
1. Every `(See Figure X.Y.Z-##)` reference has a corresponding visual specification
2. Every visual specification has a corresponding `(See Figure X.Y.Z-##)` reference
3. Every dependency reference points to a section that exists in the book
4. Every bridge text references a product that exists in the book

---

## 11. Estimated Asset Counts

Based on 49 chapters × minimum 6 visual specifications per chapter (v1.3):

| Asset Type | Estimated Count |
|-----------|:--------------:|
| Payoff Diagrams | ~50-60 |
| Timelines | ~30-40 |
| Decision Trees | ~15-20 |
| Cash Flow Diagrams | ~25-30 |
| Waterfall Diagrams | ~15-20 |
| Lifecycle Diagrams | ~20-25 |
| System Flow Diagrams | ~10-15 |
| Comparison Charts | ~20-25 |
| Balance Sheet Illustrations | ~5-10 |
| **Total** | **~294+** |

---

*Publication Architecture v1.0 effective 2026-06-20. Architecture only — no assets generated until all 49 chapters are complete.*
