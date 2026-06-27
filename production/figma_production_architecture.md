# Figma Production Architecture

**Version:** 1.0
**Date:** 2026-06-21
**Authority:** Framework Master v1.3.1 (FROZEN) + Visual Asset Governance v1.0
**Scope:** Complete visual production pipeline for 49 chapters (~294 assets)
**Purpose:** Define Figma file structure, component library, template inheritance, and production workflow

---

## 1. Figma File Structure

### 1.1 File Organization

One master Figma file: **Desk Bible v2 — Visual Assets**

### 1.2 Page Structure

| Page | Contents | Asset Count (est.) |
|------|----------|:------------------:|
| **00 — Foundations** | Color palette, typography, axis templates, shared components, icon library | ~30 components |
| **01 — ELN** | 5.1.1-5.1.15 (15 chapters × 6 visuals) | ~90 assets |
| **02 — Swaps** | 5.2.1-5.2.8 (8 chapters × 6 visuals) | ~48 assets |
| **03 — SRT** | 5.3.1-5.3.5 (5 chapters × 6 visuals) | 30 assets |
| **04 — STEG** | 5.4.1-5.4.4 (4 chapters × 6 visuals) | 24 assets |
| **05 — CLN** | 5.5.1-5.5.5 (5 chapters × 6 visuals) | ~30 assets |
| **06 — Other** | 5.6.1-5.6.7 (7 chapters × 6 visuals) | ~42 assets |
| **07 — Front Matter** | Reader guide visuals, complexity scale, dependency map, visual legend | ~10 assets |
| **08 — Publication Assets** | Final export frames (DOCX-ready, PDF-ready), master index | Mirrors all |

**Total:** ~304 assets (294 chapter visuals + ~10 front matter)

### 1.3 Within-Page Layout

Each family page organized by chapter, left-to-right:

```
┌─────────────┬─────────────┬─────────────┐
│  5.1.1 PPN  │  5.1.2 RC   │  5.1.3 Phx  │  ...
├─────────────┼─────────────┼─────────────┤
│ FIG-01 (P1) │ FIG-01 (P1) │ FIG-01 (P1) │
│ FIG-02 (P1) │ FIG-02 (P1) │ FIG-02 (P1) │
│ FIG-03 (P2) │ FIG-03 (P2) │ FIG-03 (P2) │
│ FIG-04 (P2) │ FIG-04 (P2) │ FIG-04 (P2) │
│ FIG-05 (P3) │ FIG-05 (P3) │ FIG-05 (P3) │
│ FIG-06 (P3) │ FIG-06 (P3) │ FIG-06 (P3) │
└─────────────┴─────────────┴─────────────┘
```

Frame spacing: 100px between chapters, 40px between visuals within chapter.

---

## 2. Component Library (Page 00 — Foundations)

### 2.1 Color Styles

| Style Name | Hex | Usage |
|-----------|-----|-------|
| `DB/Primary/Blue` | #2563EB | Positive values, gains, investor flows |
| `DB/Primary/Red` | #DC2626 | Negative values, losses, risk indicators |
| `DB/Neutral/Gray-600` | #6B7280 | Neutral elements, axes, borders |
| `DB/Accent/Amber` | #D97706 | Highlights, callouts, warning indicators |
| `DB/Accent/Teal` | #0D9488 | Secondary positive, alternative flow paths |
| `DB/Background/Light` | #F3F4F6 | Fill backgrounds, inactive areas |
| `DB/Background/White` | #FFFFFF | Canvas, chart backgrounds |
| `DB/Text/Dark` | #111827 | Primary text, labels |
| `DB/Text/Medium` | #374151 | Secondary text, axis labels |
| `DB/Text/Light` | #9CA3AF | Tertiary text, annotations |

### 2.2 Typography

| Style Name | Font | Size | Weight | Usage |
|-----------|------|:----:|:------:|-------|
| `DB/Title` | Inter | 16px | Bold | Figure captions |
| `DB/Label` | Inter | 12px | Medium | Axis labels, legend items |
| `DB/Annotation` | Inter | 10px | Regular | Callouts, annotations |
| `DB/Value` | Inter Mono | 11px | Medium | Numeric values on diagrams |
| `DB/Axis` | Inter | 10px | Regular | Axis tick labels |

### 2.3 Shared Components

| Component | Name | Usage | Variants |
|-----------|------|-------|----------|
| **Axis frame** | `_Shared / Axis / Standard` | X-Y payoff charts | Horizontal-only, Vertical-only, Both |
| **Arrow** | `_Shared / Arrow / Flow` | Cash flow diagrams | Single, Double, Dashed |
| **Entity box** | `_Shared / Entity / Standard` | Party boxes (Investor, Bank, etc.) | Blue (investor), Gray (bank), Red (counterparty) |
| **Timeline bar** | `_Shared / Timeline / Horizontal` | Lifecycle and sequence diagrams | 3-stage, 4-stage, 5-stage |
| **Decision diamond** | `_Shared / Decision / Standard` | Decision trees | Yes/No, Threshold |
| **Legend** | `_Shared / Legend / Standard` | All charts with multiple series | 2-item, 3-item, 4-item |
| **Caption block** | `_Shared / Caption / Standard` | Below every visual | Single-line, Multi-line |
| **Barrier line** | `_Shared / Barrier / Standard` | Payoff diagrams with barriers | KI (red dashed), KO (blue dashed) |
| **Coupon indicator** | `_Shared / Coupon / Standard` | Periodic payment indicators | Green tick, Red cross, Amber conditional |
| **Credit event marker** | `_Shared / Credit / Event` | CLN and CDS diagrams | Default (red), Near-miss (amber), No event (green) |
| **Tranche band** | `_Shared / Tranche / Band` | CDO diagrams | Equity (red), Mezz (orange), Senior (yellow), Super-senior (green) |
| **Correlation panel** | `_Shared / Correlation / Panel` | Correlation impact visuals | Low, Medium, High |

---

## 3. Reusable Component Standards

### 3.1 Component Architecture

Every visual is built from a **frame** containing shared components + custom elements:

```
Frame (700 × 400px standard)
├── _Shared / Caption / Standard
├── _Shared / Axis / Standard (if payoff chart)
├── Custom diagram elements
└── _Shared / Legend / Standard (if multi-series)
```

### 3.2 Component Detach Rules

| Rule | Rationale |
|------|-----------|
| Never detach shared components | Ensures global updates propagate |
| Override only via component properties (variants) | Preserves inheritance chain |
| Custom elements live outside shared components | Clear separation of reusable vs custom |
| If a custom element appears 3+ times, promote to shared | DRY principle |

### 3.3 Instance Override Protocol

| Property | Override Allowed? | Example |
|----------|:-----------------:|---------|
| Text content | YES | Change axis label from "Stock Price" to "CDS Spread" |
| Color style | YES (within palette) | Change entity box from Blue to Red |
| Visibility | YES | Hide legend item for single-series chart |
| Size/position | NO | Must match template grid |
| Font style | NO | All text uses DB typography styles |

---

## 4. Template Inheritance Standards

### 4.1 Template Hierarchy

```
_Shared / Axis / Standard
    ├── ELN / Payoff / Barrier (adds barrier lines)
    │   ├── ELN / RC / Barrier Payoff (instance)
    │   ├── ELN / KODRC / Dual Barrier (instance)
    │   └── ELN / Airbag / Wide Barrier (instance)
    │
    ├── Swaps / Payoff / Linear (symmetric payoff)
    │   ├── Swaps / IRS / Linear Payoff (instance)
    │   └── Swaps / TRS / Total Return (instance)
    │
    └── CLN / Payoff / Recovery (adds recovery line)
        ├── CLN / Skew CLN / Recovery Comparison (instance)
        └── CLN / FTD / Basket Default (instance)
```

### 4.2 Template Registry (52 templates)

| Template Family | Count | Source Batch | Inheritance Base |
|----------------|:-----:|:-----------:|-----------------|
| Barrier payoff | 4 | 0-3 | `_Shared / Axis` |
| Swap flow | 3 | 0, 4-5 | `_Shared / Entity` + `_Shared / Arrow` |
| Decision tree | 4 | 0, 2, 6-7 | `_Shared / Decision` |
| Lifecycle | 6 | 0, 5-7 | `_Shared / Timeline` |
| Payoff (general) | 5 | 0, 1-3, 7 | `_Shared / Axis` |
| Cash flow | 3 | 5-7 | `_Shared / Entity` + `_Shared / Arrow` |
| Waterfall | 3 | 0, 6-7 | Custom stacked bars |
| Comparison | 4 | 4-7 | `_Shared / Axis` + grouped bars |
| Yield curve | 2 | 7 | `_Shared / Axis` |
| Target/accumulation | 2 | 7 | `_Shared / Timeline` |
| Credit event | 2 | 4 | `_Shared / Credit` |
| Recovery comparison | 2 | 8 | `_Shared / Axis` + recovery lines |
| Basket default | 1 | 8 | `_Shared / Entity` grid |
| Credit correlation | 2 | 8 | `_Shared / Correlation` |
| Default sequence | 1 | 8 | `_Shared / Timeline` + markers |
| Tranche waterfall | 1 | 8 | `_Shared / Tranche` |
| Tranche bands | 1 | 8 | `_Shared / Tranche` + axis |
| Portfolio loss distribution | 1 | 8 | `_Shared / Axis` + curve |
| CDO structure flow | 1 | 8 | `_Shared / Entity` + `_Shared / Arrow` |
| Correlation reversal | 1 | 8 | `_Shared / Axis` + dual curves |
| Premium scaling | 1 | 8 | `_Shared / Axis` + descending curve |
| **Total** | **52** | | |

### 4.3 Adding New Templates (Batch 9)

Batch 9 (Other, 7 products) will need:
- Daily accumulation timeline (Accumulator/Decumulator) — extend `_Shared / Timeline`
- Option payoff on managed fund (Option on RC) — extend `_Shared / Axis`
- Forward payoff (symmetric linear) — reuse Swaps / Payoff / Linear
- Standard option payoff (vanilla) — reuse ELN / Payoff / Barrier (simplified)

**Estimated new templates for Batch 9:** 1-2 (daily accumulation timeline is the only genuinely new pattern)

---

## 5. Production Workflow

### 5.1 Per-Chapter Visual Production

| Step | Action | Output | Time Est. |
|:----:|--------|--------|:---------:|
| 1 | Read chapter visual specs (§21) | Spec understanding | 5 min |
| 2 | Identify template from registry | Template selection | 2 min |
| 3 | Duplicate template frame in Figma | v1 frame created | 1 min |
| 4 | Customize: data, labels, captions, annotations | v1 SVG draft | 20-40 min |
| 5 | Color-blind check (simulate deuteranopia) | Accessibility verified | 5 min |
| 6 | Grayscale check (desaturate) | Print verified | 2 min |
| 7 | Export SVG + PNG (3 resolutions) | Export files | 2 min |
| 8 | Update Visual Asset Master Registry status | Registry current | 1 min |

**Total per visual:** ~40-60 min. Per chapter (6 visuals): ~4-6 hours.

### 5.2 Batch Production Schedule

| Batch | Chapters | Visuals | Est. Hours | Priority |
|:-----:|:--------:|:-------:|:----------:|:--------:|
| Harmonization (0-4) | 27 | ~162 | 108-162 | After 49/49 |
| Batch 5 (already registered) | 3 | 15 | 10-15 | After 49/49 |
| Batch 6 (already registered) | 5 | 30 | 20-30 | After 49/49 |
| Batch 7 (already registered) | 4 | 24 | 16-24 | After 49/49 |
| Batch 8 (already registered) | 4 | 24 | 16-24 | After 49/49 |
| Batch 9 (to be generated) | 7 | ~42 | 28-42 | After 49/49 |
| Front matter | — | ~10 | 7-10 | After 49/49 |
| **Total** | **49+** | **~307** | **205-307** | — |

---

## 6. Quality Assurance

| QA Check | Applies To | Method |
|----------|-----------|--------|
| Template compliance | All assets | Visual diff against template |
| Color palette compliance | All assets | Automated check against DB styles |
| Typography compliance | All assets | Font audit (no non-DB fonts) |
| Naming convention | All files | Script check against convention |
| Accessibility (CB) | Tier 1-2 | Deuteranopia + protanopia simulation |
| Accessibility (grayscale) | Tier 1 | B&W print test |
| Caption match | All assets | Cross-reference chapter §21 |
| Registry sync | All assets | Compare Figma export list vs registry |

---

*Figma Production Architecture v1.0. Effective 2026-06-21. Production begins after 49/49 chapter completion.*
