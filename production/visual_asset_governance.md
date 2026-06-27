# Visual Asset Governance

**Version:** 1.0
**Date:** 2026-06-21
**Authority:** Framework Master v1.3.1 (FROZEN)
**Scope:** All visual assets across 49 product chapters + front matter
**Purpose:** Define standards for naming, versioning, accessibility, and export of all publication visuals

---

## 1. Asset Hierarchy

All visual assets belong to one of three tiers. Tier determines production priority, review rigor, and export requirements.

| Tier | Definition | Production Standard | Review Required | Count Target |
|:----:|-----------|--------------------:|:---------------:|:------------:|
| **Tier 1** | Core teaching visuals — payoff diagrams, structure flows, and loss allocation waterfalls that carry the primary educational message. Reader cannot understand the product without this visual. | Publication-grade SVG. Full axis labels, captions, annotations. Color-blind safe. Print-ready. | Structurer sign-off + editorial review | ~98 (2 per chapter × 49) |
| **Tier 2** | Supporting visuals — lifecycle timelines, comparison charts, scenario illustrations. Enhance understanding but product is comprehensible without them. | Publication-grade SVG. Full captions. Color-blind safe. | Editorial review | ~98 (2 per chapter × 49) |
| **Tier 3** | Reference visuals — decision trees, booking flows, system diagrams. Useful for desk operators but not essential for conceptual understanding. | Publication-grade SVG. Simplified annotation acceptable. | Self-review | ~98 (2 per chapter × 49) |

**Tier assignment rule:** Each chapter has 6 visual specs with priority P1/P2/P3. Mapping:
- P1 → Tier 1
- P2 → Tier 2
- P3 → Tier 3

**Total target:** ~294 visual assets (6 per chapter × 49 chapters). Currently 93 registered (Batches 5-8). Remaining ~201 to be registered during harmonization (Batches 0-4 upgrade) and Batch 9 generation.

---

## 2. Naming Conventions

### 2.1 Figure Number Convention

Format: `FIG-5.X.Y-##`

| Component | Description | Example |
|-----------|------------|---------|
| `FIG` | Fixed prefix | FIG |
| `5.X.Y` | Section number (family.chapter) | 5.1.2 (RC), 5.5.5 (Synthetic CDO) |
| `##` | Sequential within chapter (01-06) | 01, 02, ... 06 |

**Examples:**
- `FIG-5.1.1-01` — PPN payoff diagram (first visual in PPN chapter)
- `FIG-5.5.5-06` — Synthetic CDO default timeline (sixth visual in CDO chapter)

**Legacy mapping:** Current registry uses `Figure 5.X.Y-##`. During harmonization, all figure references will be updated to `FIG-5.X.Y-##` format.

### 2.2 SVG Filename Convention

Format: `{type}_{product}_{descriptor}_{##}.svg`

| Component | Description | Examples |
|-----------|------------|---------|
| `{type}` | Visual type prefix | `payoff`, `flow`, `lifecycle`, `timeline`, `comparison`, `decision`, `waterfall`, `correlation`, `portfolio`, `tranche`, `distribution`, `curve` |
| `{product}` | Product short name (snake_case) | `ppn`, `rc`, `ftd`, `scdo`, `vanilla_steg` |
| `{descriptor}` | Content descriptor | `barrier_payoff`, `three_party`, `default_sequence` |
| `{##}` | Sequential number | `01`, `02` |

**Examples:**
- `payoff_rc_barrier_payoff_01.svg`
- `flow_scdo_structure_05.svg`
- `correlation_ntd_reversal_02.svg`

**Constraint:** Filenames globally unique. No duplicates permitted across entire asset library. Checked during registration.

### 2.3 PNG Filename Convention

Format: Same as SVG with `.png` extension and resolution suffix.

- `payoff_rc_barrier_payoff_01_300dpi.png` — Print resolution
- `payoff_rc_barrier_payoff_01_150dpi.png` — Screen resolution
- `payoff_rc_barrier_payoff_01_72dpi.png` — Web resolution

### 2.4 Figma Component Naming Convention

Format: `{Family} / {Product} / {Visual Type} / {Descriptor}`

**Examples:**
- `ELN / RC / Payoff / Barrier Payoff`
- `CLN / Synthetic CDO / Waterfall / Tranche Loss`
- `STEG / TARN STEG / Timeline / Target Accumulation`

**Shared components:** Prefixed with `_Shared /`
- `_Shared / Lifecycle / 4-Stage Template`
- `_Shared / Payoff / Axis Template`
- `_Shared / Colors / Desk Bible Palette`

---

## 3. Version Control

### 3.1 Version Numbering

| Version | Meaning | When Used |
|---------|---------|-----------|
| `v1` | Initial draft — first SVG render from spec | SVG generation pass |
| `v2` | Revised — after editorial or structurer feedback | Review iteration |
| `vFinal` | Approved for publication — no further changes | Publication lock |

**Version in filename:** Append before extension.
- `payoff_rc_barrier_payoff_01_v1.svg`
- `payoff_rc_barrier_payoff_01_v2.svg`
- `payoff_rc_barrier_payoff_01_vFinal.svg`

### 3.2 Version Tracking

| Field | Location | Purpose |
|-------|----------|---------|
| `publication_status` | Visual Asset Master Registry | Tracks pipeline stage: SPEC → SVG → PNG → DOCX → PDF → PUBLISHED |
| `svg_status` | Visual Asset Master Registry | PENDING → DRAFT → REVIEWED → FINAL |
| `version_history` | Figma component metadata | Records v1, v2, vFinal with dates |

### 3.3 Change Control

- **v1 → v2:** Any team member may request revision. Document reason in Figma comment.
- **v2 → vFinal:** Requires editorial sign-off. Tier 1 assets also require structurer confirmation.
- **Post-vFinal changes:** Require formal change request with justification. Version becomes `vFinal.1`, `vFinal.2`.

---

## 4. Accessibility Standards

### 4.1 Color-Blind Safety

| Requirement | Standard | Test |
|-------------|----------|------|
| Never rely on color alone to convey information | Use pattern, shape, label, or position as redundant cue | Remove color → information still readable |
| Use color-blind safe palette | Desk Bible palette (below) avoids red-green reliance | Simulate deuteranopia, protanopia, tritanopia |
| Minimum contrast ratio | 4.5:1 for text on colored background (WCAG AA) | Contrast checker tool |

**Desk Bible Color Palette (color-blind safe):**

| Use | Color | Hex | CB-Safe Pair |
|-----|-------|-----|:------------:|
| Primary (positive/gain) | Blue | #2563EB | Yes |
| Negative (loss/risk) | Orange-Red | #DC2626 | Yes (with blue) |
| Neutral | Medium Gray | #6B7280 | Yes |
| Highlight | Amber | #D97706 | Yes |
| Secondary positive | Teal | #0D9488 | Yes (with orange) |
| Background fill | Light Gray | #F3F4F6 | Yes |
| Axis/border | Dark Gray | #374151 | Yes |

### 4.2 Grayscale Readability

| Requirement | Standard |
|-------------|----------|
| All visuals must be readable in grayscale | Use hatching, line style (solid/dashed/dotted), and labels when color is removed |
| Pattern library | 6 patterns: solid, diagonal hatch, cross-hatch, horizontal lines, dots, empty |
| Grayscale test | Print on B&W laser printer → all elements distinguishable |

### 4.3 Print Readability

| Requirement | Standard |
|-------------|----------|
| Minimum font size | 8pt in printed output (A4/Letter) |
| Line weight | Minimum 0.75pt for all strokes |
| Text contrast | Black text on white/light background only |
| Annotation legibility | All callouts and labels readable at 100% print scale |
| Bleed safety | 5mm margin from any content to page edge |

---

## 5. Export Standards

### 5.1 SVG Master

| Property | Standard |
|----------|----------|
| Format | SVG 1.1 |
| Viewport | Fixed viewBox (no responsive scaling) |
| Dimensions | Width: 700px standard, 1000px for complex diagrams. Height: proportional |
| Fonts | Converted to outlines (no font dependencies) |
| Colors | CSS variables for theming capability |
| File size | Target < 50KB per SVG. Maximum 100KB |
| Naming | Per §2.2 convention |
| Metadata | Include `<title>` and `<desc>` elements for accessibility |

### 5.2 PNG Export

| Property | Standard |
|----------|----------|
| Resolution (print) | 300 DPI |
| Resolution (screen) | 150 DPI |
| Resolution (web) | 72 DPI |
| Color space | sRGB |
| Background | Transparent (diagrams), White (payoff charts with axes) |
| Format | PNG-8 for simple diagrams, PNG-24 for gradients |
| Maximum dimensions | 3000 × 2000px at 300 DPI |

### 5.3 PDF Export

| Property | Standard |
|----------|----------|
| Source | SVG master embedded in PDF |
| Vector preservation | All SVG elements remain vector (no rasterization) |
| Font embedding | All text as outlines |
| Color space | sRGB for screen PDF, CMYK for print PDF |
| PDF version | PDF/A-1b for archival compliance |

### 5.4 Export Pipeline

```
SVG Master (source of truth)
    │
    ├── PNG 300dpi (print)
    ├── PNG 150dpi (screen/DOCX)
    ├── PNG 72dpi (web preview)
    │
    ├── PDF embed (vector, sRGB)
    └── PDF print (vector, CMYK)
```

---

## 6. Quality Gates

| Gate | When | Criteria | Blocker? |
|------|------|----------|:--------:|
| **Spec Review** | After chapter generation | All 12+ fields populated, caption clear, elements listed | YES |
| **SVG Draft** | After v1 render | Matches spec, axes labeled, caption embedded, CB-safe palette | YES |
| **Grayscale Test** | After v1 render | Readable in B&W print | YES (Tier 1 only) |
| **Editorial Review** | Before vFinal | Terminology consistent with chapter, no orphaned labels | YES (Tier 1-2) |
| **Publication Lock** | Before DOCX build | vFinal confirmed, PNG exports complete, registry updated | YES |

---

*Visual Asset Governance v1.0. Effective 2026-06-21. Applies to all visual assets across 49 chapters.*
