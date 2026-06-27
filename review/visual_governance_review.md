# Visual Governance Review

**Date:** 2026-06-20
**Scope:** 69 visual assets across Batches 5-7 (Swaps 15, SRT 30, STEG 24) + 41 visual templates
**Framework:** v1.3.1 (FROZEN)
**Purpose:** Assess visual governance readiness before scaling to 49 products

---

## 1. Visual Template Reuse Assessment

### 1.1 Templates Established (41 total)

| Category | Templates | Source Batch | Reuse Count (actual/potential) |
|----------|:---------:|:------------:|:------------------------------:|
| Barrier payoffs | 4 | 0-3 | High — 10+ ELN chapters use variants |
| Swap flows | 3 | 0, 4-5 | High — all swap chapters adapt |
| Decision trees | 4 | 0, 2, 6-7 | Medium — observation-based products |
| Lifecycle diagrams | 6 | 0, 5-7 | High — every chapter has lifecycle |
| Payoff diagrams | 5 | 0, 1-3, 7 | High — universal |
| Cash flow diagrams | 3 | 5-7 | High — four-leg products |
| Waterfall diagrams | 3 | 0, 6-7 | Medium — construction decomposition |
| Comparison charts | 4 | 4-7 | Low — family-specific |
| Yield curve diagrams | 2 | 7 | Medium — STEG and future rate products |
| Target/accumulation | 2 | 7 | Low — TARN-specific, but reusable for Batch 9 Accumulator/Decumulator |
| Credit event | 2 | 4 | Medium — CLN Batch 8 will reuse |
| Other specialized | 3 | 5-6 | Low — product-specific |

### 1.2 Template Reuse Effectiveness

| Metric | Value |
|--------|:-----:|
| Templates with High reuse status | 17 (41%) |
| Templates with Medium reuse status | 14 (34%) |
| Templates with Low reuse status | 10 (24%) |
| Templates reused across families | 12 |
| Templates family-specific | 29 |

**Assessment:** Template library well-built. Barrier payoffs, lifecycle diagrams, and payoff charts form a reusable core. Batch 8 (CLN) can reuse credit event templates from CDS. Batch 9 (Other) can reuse accumulation templates from TARN.

---

## 2. Figure Numbering Integrity

### 2.1 Numbering Convention

Format: `Figure 5.X.Y-##` where X = family, Y = chapter, ## = sequential within chapter.

| Check | Result |
|-------|:------:|
| All 70 figure numbers follow convention | PASS |
| No duplicate figure numbers | PASS |
| Sequential within each chapter (01-06) | PASS |
| No gaps in numbering within chapters | PASS |
| Family prefix consistent (5.2.x = Swaps, 5.3.x = SRT, 5.4.x = STEG) | PASS |

### 2.2 Numbering Gaps (Expected)

Batches 0-4 visual specs exist in chapter text but NOT in the visual asset master registry (deferred to harmonization). These will be assigned figure numbers during harmonization:

| Family | Missing from Registry | Reason |
|--------|:---------------------:|--------|
| ELN (5.1.1-5.1.15) | ~60-90 visuals | Batches 0-3 use v1.0 Learning Recommendations, not registered |
| Swaps core (5.2.1-5.2.5) | ~20-30 visuals | Batch 4 uses v1.1, not registered |

**Impact:** No impact on current production. Registry entries will be created during harmonization.

---

## 3. Visual Asset Taxonomy

### 3.1 Asset Types in Registry

| Asset Type | Count | % of Total |
|-----------|:-----:|:----------:|
| Cash Flow Diagram | 13 | 19% |
| Lifecycle Diagram | 12 | 17% |
| Payoff Diagram | 11 | 16% |
| Timeline | 10 | 14% |
| Comparison Chart | 8 | 11% |
| Decision Tree | 6 | 9% |
| Waterfall Diagram | 4 | 6% |
| Yield Curve Diagram | 3 | 4% |
| System Flow Diagram | 1 | 1% |
| Balance Sheet Illustration | 1 | 1% |
| Other | 1 | 1% |

**Assessment:** Taxonomy is balanced. Top 4 types (Cash Flow, Lifecycle, Payoff, Timeline) account for 66% — these are the core visual vocabulary. Yield Curve Diagram is new (Batch 7 STEG) and will grow with remaining rate products.

### 3.2 Priority Distribution

| Priority | Count | % |
|----------|:-----:|:-:|
| P1 | 24 | 35% |
| P2 | 24 | 35% |
| P3 | 21 | 30% |

**Assessment:** Near-equal distribution. Each chapter contributes 2P1+2P2+2P3 (Batches 5-7) or 2P1+1P2+2P3 (some Batch 5). Balanced across all chapters.

---

## 4. Publication Asset Readiness

### 4.1 Pipeline Status

| Status | Count | % |
|--------|:-----:|:-:|
| SPEC | 69 | 100% |
| SVG | 0 | 0% |
| PNG | 0 | 0% |
| DOCX | 0 | 0% |
| PDF | 0 | 0% |

All 69 assets at SPEC stage. SVG generation deferred until 49/49 per governance rules.

### 4.2 Readiness for SVG Generation

| Requirement | Status |
|-------------|:------:|
| All 12+ publication fields populated | YES (69/69) |
| Captions written | YES (69/69) |
| Axis definitions specified | YES (where applicable) |
| Diagram elements listed | YES (69/69) |
| Future filenames assigned (unique) | YES (69/69, 0 duplicates) |
| Reuse status tagged | YES (69/69) |

**Assessment:** All 69 registered assets ready for SVG production. Unregistered assets (Batches 0-4) need specification upgrade during harmonization before SVG generation.

### 4.3 Registry Structure

| Check | Result |
|-------|:------:|
| YAML structure valid | PASS |
| Header metadata complete | PASS |
| Governance rules documented | PASS |
| Field definitions documented | PASS |
| Family tagging correct | PASS |
| Section references correct | PASS |

---

## 5. Recommendations

### 5.1 Reusable Figure Families

Recommend grouping assets into figure families for production efficiency:

| Figure Family | Members | Production Approach |
|---------------|:-------:|-------------------|
| **Four-Leg Flow** | 9 diagrams (SRT 5 + STEG 4) | Shared SVG template with product-specific leg labels |
| **Lifecycle Timeline** | 12 diagrams | Shared timeline template with product-specific events |
| **Leveraged Payoff** | 6 diagrams | Shared kinked-line template with variable slope/cap/floor |
| **Worked Example Bar** | 10 diagrams | Shared bar chart template with variable heights/labels |
| **Decision Tree** | 6 diagrams | Shared diamond-branch template with variable conditions |
| **Yield Curve** | 3 diagrams | Shared curve template with variable shape/annotations |
| **Waterfall** | 4 diagrams | Shared waterfall template with variable components |
| **Comparison** | 8 diagrams | Shared grouped-bar template |
| **One-off** | 11 diagrams | Individual production |

**Estimated SVG production savings:** 40-50% by using template families instead of individual production.

### 5.2 Figma Production Hierarchy

Recommended Figma file structure:

```
Desk Bible v2 — Visual Assets
├── 01_Templates
│   ├── Four-Leg Flow Template
│   ├── Lifecycle Timeline Template
│   ├── Leveraged Payoff Template
│   ├── Worked Example Bar Template
│   ├── Decision Tree Template
│   ├── Yield Curve Template
│   └── Waterfall Template
├── 02_ELN (15 chapters × 4-6 visuals)
│   ├── 5.1.01 PPN
│   ├── 5.1.02 RC
│   └── ... (15 sub-pages)
├── 03_Swaps (8 chapters × 6 visuals)
│   ├── 5.2.01 IRS
│   └── ... (8 sub-pages)
├── 04_SRT (5 chapters × 6 visuals)
│   ├── 5.3.01 IR Callable
│   └── ... (5 sub-pages)
├── 05_STEG (4 chapters × 6 visuals)
│   ├── 5.4.01 Vanilla STEG
│   └── ... (4 sub-pages)
├── 06_CLN (5 chapters × 6 visuals)
├── 07_Other (7 chapters × 6 visuals)
└── 08_Exports
    ├── SVG/
    └── PNG/
```

### 5.3 SVG Production Hierarchy

Recommended SVG naming and directory structure:

```
assets/svg/
├── eln/
│   ├── payoff_ppn_01.svg
│   ├── flow_ppn_01.svg
│   └── ...
├── swaps/
│   ├── flow_ccy_swap_01.svg
│   └── ...
├── srt/
│   ├── flow_ir_callable_01.svg
│   └── ...
├── steg/
│   ├── flow_vsteg_01.svg
│   └── ...
├── cln/
│   └── ...
├── other/
│   └── ...
└── templates/
    ├── template_four_leg_flow.svg
    ├── template_lifecycle.svg
    └── ...
```

File naming follows registry: `{type}_{product}_{##}.svg`. All lowercase, underscores. Matches `asset_filename` field in registry.

---

## 6. Summary

| Area | Status |
|------|:------:|
| Visual template reuse | Strong — 41 templates, 41% High reuse |
| Figure numbering integrity | PASS — 0 duplicates, 0 gaps |
| Visual asset taxonomy | Balanced — 11 types, top 4 cover 66% |
| Publication asset readiness | All 69 at SPEC, all fields populated |
| Registry structure | PASS — valid YAML, complete metadata |

**Remaining work (post-49/49):**
1. Register Batch 0-4 visuals (~80-120 additional entries)
2. Generate SVG from all ~190-250 specs
3. Export PNG from SVG
4. Insert into DOCX/PDF

---

*Visual Governance Review completed 2026-06-20. No modifications required.*
