# Master Educational Roadmap — Final Enhancement Sequence

**Date:** 2026-06-21
**Framework:** v1.3.1 (FROZEN)
**Purpose:** Rank and sequence all remaining educational enhancements after 49/49
**Status:** All design reviews complete. No enhancements implemented yet.

---

## 1. Enhancement Inventory

| # | Enhancement | Type | Est. Words | Est. Visuals | Design Doc |
|:-:|------------|------|:----------:|:------------:|:----------:|
| E1 | Payoff Chart Masterclass (§1.10) | New section | 3,500 | 12 | `review/payoff_chart_masterclass_design.md` |
| E2 | Product Construction Lab (§1.11) | New section | 4,500 | 9 | `review/product_construction_lab_design.md` |
| E3 | Trade Lifecycle Masterclass (§2.9) | New section | 7,000 | 7 | `review/trade_lifecycle_masterclass_design.md` |
| E4 | Solutions Manual (Part 7) | New part | 178,000 | 0 | `review/solutions_manual_architecture.md` |
| E5 | Front Matter (Reader Guide, Learning Paths, etc.) | New section | 6,000 | 4 | `production/front_matter_plan.md` |
| E6 | Template Harmonization Pass | Retrofit | Variable | 0 | Deferred until 49/49 |
| E7 | Glossary & Acronym Refresh | Update | 2,000 | 0 | Dashboard tracked |
| E8 | Visual Asset Production | Production | 0 | ~294 | `production/visual_asset_governance.md` |
| E9 | DOCX Build | Production | 0 | 0 | Deferred |
| E10 | PDF Build | Production | 0 | 0 | Deferred |

---

## 2. Ranking Matrix

### 2.1 Scoring Criteria

| Criterion | Weight | Description |
|-----------|:------:|------------|
| Impact | 30% | How much does this improve the reader's learning outcome? |
| Effort | 20% | Inverse — lower effort scores higher |
| Publication value | 25% | How much does this improve the published book? |
| Reader value | 25% | How much does the reader directly benefit? |

### 2.2 Scores

| # | Enhancement | Impact | Effort (inv.) | Pub Value | Reader Value | **Weighted** |
|:-:|------------|:------:|:-------------:|:---------:|:------------:|:------------:|
| E1 | Payoff Chart Masterclass | 9 | 8 | 9 | 10 | **9.05** |
| E2 | Product Construction Lab | 10 | 7 | 9 | 10 | **9.15** |
| E5 | Front Matter | 8 | 7 | 10 | 9 | **8.65** |
| E3 | Trade Lifecycle Masterclass | 8 | 6 | 8 | 8 | **7.70** |
| E4 | Solutions Manual | 10 | 2 | 10 | 10 | **8.20** |
| E6 | Template Harmonization | 7 | 5 | 9 | 6 | **6.95** |
| E7 | Glossary Refresh | 5 | 9 | 7 | 6 | **6.55** |
| E8 | Visual Asset Production | 8 | 2 | 10 | 9 | **7.55** |
| E9 | DOCX Build | 3 | 6 | 10 | 8 | **6.85** |
| E10 | PDF Build | 3 | 6 | 10 | 8 | **6.85** |

### 2.3 Final Ranking

| Rank | Enhancement | Weighted Score | Category |
|:----:|------------|:--------------:|:--------:|
| **1** | E2 — Product Construction Lab | 9.15 | Content |
| **2** | E1 — Payoff Chart Masterclass | 9.05 | Content |
| **3** | E5 — Front Matter | 8.65 | Navigation |
| **4** | E4 — Solutions Manual | 8.20 | Content |
| **5** | E3 — Trade Lifecycle Masterclass | 7.70 | Content |
| **6** | E8 — Visual Asset Production | 7.55 | Production |
| **7** | E6 — Template Harmonization | 6.95 | Quality |
| **8** | E9 — DOCX Build | 6.85 | Production |
| **9** | E10 — PDF Build | 6.85 | Production |
| **10** | E7 — Glossary Refresh | 6.55 | Quality |

---

## 3. Implementation Sequence

### Phase 0: Batch 9 Completion (PREREQUISITE)

| Step | Task | Output |
|:----:|------|--------|
| 0.1 | Generate 7 remaining products (#38-#44) | 49/49 complete |
| 0.2 | Update all registries | Complexity, visual assets, dashboard |
| 0.3 | Batch 9 review | All chapters pass |

**Gate: 49/49 products complete. No further work until this gate passes.**

---

### Phase 1: Template Harmonization (MUST DO FIRST)

| Step | Task | Est. Effort | Output |
|:----:|------|:----------:|--------|
| 1.1 | Audit Batches 0-3 chapters (v1.0 template, 16 sections) | 2 days | Gap analysis |
| 1.2 | Retrofit missing sections (§17-§22) to 16 grandfathered chapters | 8 days | 16 chapters updated |
| 1.3 | Align Batch 4 chapters (v1.1) to v1.3.1 | 2 days | 5 chapters updated |
| 1.4 | Align Batch 5 chapters (v1.2) to v1.3.1 | 1 day | 4 chapters updated |
| 1.5 | Verify all 49 chapters pass v1.3.1 checklist | 2 days | Full compliance |

**Total: ~15 days. All subsequent phases assume harmonized manuscript.**

**Why first:** Every other enhancement references specific section numbers. Harmonization stabilizes the section numbering across all chapters.

---

### Phase 2: Content Enhancements (HIGHEST READER VALUE)

| Step | Task | Est. Effort | Dependencies |
|:----:|------|:----------:|:------------|
| 2.1 | Generate §1.10 — Payoff Chart Masterclass | 2 days | Phase 1 complete |
| 2.2 | Generate §1.11 — Product Construction Lab | 3 days | Phase 1 + 2.1 complete |
| 2.3 | Generate §2.9 — Trade Lifecycle Masterclass | 3 days | Phase 1 complete |
| 2.4 | Glossary & Acronym Refresh | 1 day | Phase 1 complete |

**Total: ~9 days. 2.1 and 2.3 can run in parallel. 2.2 depends on 2.1.**

```
Phase 1 complete
    │
    ├── 2.1 Payoff Chart Masterclass (2d)
    │       │
    │       └── 2.2 Product Construction Lab (3d)
    │
    ├── 2.3 Trade Lifecycle Masterclass (3d) ← parallel with 2.1
    │
    └── 2.4 Glossary Refresh (1d) ← parallel with 2.1
```

---

### Phase 3: Navigation Layer (PUBLICATION READINESS)

| Step | Task | Est. Effort | Dependencies |
|:----:|------|:----------:|:------------|
| 3.1 | Generate Front Matter (Reader Guide, Learning Paths) | 3 days | Phase 2 complete (need final section numbers) |
| 3.2 | Generate Complexity Scale visual | 1 day | Phase 2 complete |
| 3.3 | Generate Product Dependency Map | 1 day | Phase 2 complete |
| 3.4 | Insert cross-references across all chapters | 2 days | Phase 3.1 complete |

**Total: ~7 days.**

---

### Phase 4: Solutions Manual (LARGEST COMPONENT)

| Step | Task | Est. Effort | Dependencies |
|:----:|------|:----------:|:------------|
| 4.1 | Foundation section solutions (Parts 0-4) | 2 days | Phase 2 complete |
| 4.2 | ELN family solutions (15 products) | 5 days | Phase 2 complete |
| 4.3 | Swaps family solutions (8 products) | 3 days | Phase 2 complete |
| 4.4 | SRT family solutions (5 products) | 2 days | Phase 2 complete |
| 4.5 | STEG family solutions (4 products) | 2 days | Phase 2 complete |
| 4.6 | CLN family solutions (5 products) | 2 days | Phase 2 complete |
| 4.7 | Other family solutions (7 products) | 3 days | Phase 2 complete |
| 4.8 | Cross-product integration questions | 1 day | 4.1-4.7 complete |
| 4.9 | Solutions Manual review | 2 days | 4.8 complete |

**Total: ~22 days. 4.1-4.7 sequential by family (each references prior family patterns).**

---

### Phase 5: Visual Asset Production (PARALLEL TRACK)

| Step | Task | Est. Effort | Dependencies |
|:----:|------|:----------:|:------------|
| 5.1 | Python chart template setup | 2 days | Phase 1 complete |
| 5.2 | Figma component library build | 3 days | Phase 1 complete |
| 5.3 | Top 25 priority visuals (Tier 1 critical) | 10 days | 5.1 + 5.2 complete |
| 5.4 | Remaining Tier 1 visuals | 8 days | 5.3 complete |
| 5.5 | Tier 2 visuals | 10 days | 5.4 complete |
| 5.6 | Tier 3 visuals | 6 days | 5.5 complete |
| 5.7 | New section visuals (1.10, 1.11, 2.9) | 4 days | Phase 2 + 5.2 complete |
| 5.8 | Front matter visuals | 2 days | Phase 3 + 5.2 complete |

**Total: ~45 days. Can run partially in parallel with Phase 4.**

---

### Phase 6: Publication Build (FINAL)

| Step | Task | Est. Effort | Dependencies |
|:----:|------|:----------:|:------------|
| 6.1 | Master editorial pass | 5 days | Phases 2-4 complete |
| 6.2 | Full compression pass | 3 days | 6.1 complete |
| 6.3 | DOCX build | 2 days | 6.2 + Phase 5 complete |
| 6.4 | PDF build | 1 day | 6.3 complete |
| 6.5 | Final proofread | 3 days | 6.4 complete |

**Total: ~14 days.**

---

## 4. Critical Path

```
Batch 9 (7 products)
    │
    ▼
Phase 1: Harmonization (15d)
    │
    ├──────────────────────────────────┐
    │                                  │
    ▼                                  ▼
Phase 2: Content (9d)        Phase 5.1-5.2: Tool Setup (5d)
    │                                  │
    ▼                                  ▼
Phase 3: Navigation (7d)     Phase 5.3-5.6: Visual Prod (34d)
    │                                  │
    ▼                                  │
Phase 4: Solutions Manual (22d)        │
    │                                  │
    ├──────────────────────────────────┘
    │
    ▼
Phase 6: Publication Build (14d)
```

**Critical path: Phase 1 → Phase 2 → Phase 4 → Phase 6 = 60 days**
**With visual production parallel: ~67 days total** (visual production is longest parallel track)

---

## 5. Summary Table

| Phase | Duration | Deliverable | Cumulative |
|:-----:|:--------:|------------|:----------:|
| 0 | Variable | 49/49 products | Manuscript complete |
| 1 | 15 days | All chapters v1.3.1 compliant | Harmonized |
| 2 | 9 days | 3 new sections + glossary | Content enhanced |
| 3 | 7 days | Front matter + cross-refs | Navigable |
| 4 | 22 days | 482 three-tier answers | Self-study enabled |
| 5 | 45 days | ~294 publication visuals | Visually complete |
| 6 | 14 days | DOCX + PDF | Published |
| **Total** | **~67 days** | **Complete publication** | **Done** |

---

## 6. Risk Register

| Risk | Probability | Impact | Mitigation |
|------|:----------:|:------:|-----------|
| Harmonization reveals structural issues in early chapters | Medium | High | Budget 2 extra days for unexpected rework |
| Solutions Manual volume causes quality drift | Medium | Medium | Generate by family with review gates between families |
| Visual production bottleneck (45 days) delays publication | High | High | Start tool setup during Phase 1. Prioritize Top 25 |
| New sections (1.10, 1.11, 2.9) create dependencies not anticipated | Low | Medium | All new sections are additive. No existing content modified |
| Cross-reference insertions break during harmonization | Low | Low | Automated cross-ref validation after each phase |

---

## 7. Decision Points

| Gate | Decision | Criteria |
|:----:|----------|---------|
| G0 | Proceed from Batch 9 to harmonization? | 49/49 accepted, all reviews passed |
| G1 | Proceed from harmonization to content? | All 49 chapters pass v1.3.1 checklist |
| G2 | Proceed to Solutions Manual? | New sections complete and reviewed |
| G3 | Proceed to publication build? | Solutions Manual reviewed, visuals 80%+ complete |
| G4 | Release? | DOCX + PDF pass final proofread |

---

*Master Educational Roadmap completed 2026-06-21. 10 enhancements ranked. 6-phase implementation sequence defined. Critical path: ~67 days post-49/49.*
