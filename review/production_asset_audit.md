# Production Asset Audit

**Date:** 2026-06-19
**Purpose:** Determine what exists, what is partial, and what is missing before scaling to Batch 2+
**Scope:** 9 production assets requested for audit

---

## Asset Status Summary

| # | Asset | Status | Location |
|:-:|-------|:------:|----------|
| 1 | Knowledge Base | PARTIAL | Distributed across `memory/`, `production/`, `framework-v2/` |
| 2 | Canonical Glossary | MISSING | No standalone glossary exists |
| 3 | Acronym Registry | MISSING | No standalone registry exists |
| 4 | Concept Dependency Graph | EXISTS | `production/product_generation_order.md` §5 (lines 226-253) |
| 5 | Visual Asset Library | PARTIAL | `audit/visualization_plan.md` (plan only) + `production/visual_standard.md` (conventions) + dashboard §6 (template registry) |
| 6 | Memory-V2 | PARTIAL | `framework-v2/MEMORY_DESIGN_GUIDE.md` (design doc only). Actual V2 memory files do not exist — `memory/` contains V1 artifacts |
| 7 | Master Book Editor Agent | EXISTS | `production/review_workflow.md` §3, Agent 9 (lines 318-370) |
| 8 | Beginner Reader Agent | EXISTS | `production/review_workflow.md` §3, Agent 10 (lines 372-399) |
| 9 | Publication Agent | EXISTS | `production/review_workflow.md` §3, Agent 11 (lines 404-431) |

---

## Detailed Findings

### 1. Knowledge Base — PARTIAL

**What exists:**
- `memory/terminology/` — 5 family YAML files (ELN, CLN, SRT, STEG, Swap). V1 artifacts. Contain product names, abbreviations, system name casing, forbidden phrases.
- `memory/booking-maps/` — 5 family YAML files. V1 artifacts. Contain system assignments per family (NEMO, Sophis, Murex roles).
- `memory/style-patterns/` — 5 family YAML files. V1 artifacts. Contain formatting conventions per family.
- `memory/components/`, `memory/definitions/`, `memory/examples/`, `memory/reconciliation/` — 4 empty directories. Created in V1 architecture but never populated (confirmed as unused in `framework-v2/MEMORY_DESIGN_GUIDE.md`).
- `production/jargon_watchlist.md` — 100+ terms across 5 categories with required definitions. Active, used by Jargon Police Agent.
- `production/generation_dashboard.md` §5 — Analogy domain registry (10 used + 25 reserved).
- `production/generation_dashboard.md` §6 — Visual template registry (9 established, 5 planned).
- `production/generation_dashboard.md` §7 — Jargon watchlist additions tracker (4 entries).

**What is missing:**
- No unified, queryable knowledge base that consolidates terminology, analogies, templates, booking maps, and cross-references into a single source of truth.
- The V1 `memory/` YAML files are frozen V1 artifacts — they are not actively updated during V2 production. V2 generation uses inline knowledge (the production framework docs + the main document itself), not these files.
- The 4 empty `memory/` subdirectories were planned but never used.

**Gap assessment:** The knowledge is distributed across ~8 files in 3 directories. It works because V2 generation references `production/*.md` documents directly. A consolidated knowledge base would be useful at scale (Batches 4-9 when 5+ families are in play) but is not blocking for Batches 2-3 (still ELN family).

---

### 2. Canonical Glossary — MISSING

**What exists:**
- Terms are defined inline throughout `Desk_Bible_v2.md` with parenthetical definitions on first use.
- `production/jargon_watchlist.md` contains ~100+ terms with required definitions — but this is a **watchlist** (terms to police during generation), not a **glossary** (reader-facing term definitions with locations).
- `memory/terminology/*.yaml` files contain product names and system name casing — but no definitions of financial concepts.
- The Final Publication Agent (review_workflow.md Agent 11) is designed to extract glossary items during batch review — but no extraction has been performed yet.
- No "glossary" appears anywhere in `Desk_Bible_v2.md`. The word "glossary" appears only in `review_workflow.md` Agent 11's definition.

**What is missing:**
- A canonical glossary file mapping every defined term to: (a) its definition, (b) the section where it is first defined, (c) which product chapters use it.
- The planned Part 7 (Quick Reference) would include this, but Part 7 has not been written.

**Gap assessment:** A glossary is a publication-phase asset, not a generation-phase asset. Its absence does not block chapter generation. However, building it incrementally during generation (extracting terms as chapters are produced) is more efficient than building it retroactively after all 49 chapters are complete.

---

### 3. Acronym Registry — MISSING

**What exists:**
- Part 4 includes an abbreviation legend before the comparison matrices (e.g., PPN, RC, FCN, DRC, etc.).
- `memory/terminology/*.yaml` files contain abbreviations per product family.
- `production/jargon_watchlist.md` includes some acronyms (ISIN, LEI, RED code).
- The Final Publication Agent is designed to index acronyms — but no indexing output exists.

**What is missing:**
- A standalone registry listing every acronym used in the book with: (a) full expansion, (b) first-use location, (c) all chapters where it appears.
- No acronym-specific tracking file exists anywhere in the project.

**Gap assessment:** Same as glossary — publication-phase asset. However, acronym consistency has been an implicit success (no acronym errors detected in the quality gate review). An acronym registry would prevent drift as the remaining 39 chapters introduce new terms.

---

### 4. Concept Dependency Graph — EXISTS

**Location:** `production/product_generation_order.md`, Section 5 (lines 226-253)

**What exists:**
- ASCII-art dependency graph showing all 49 products and their concept prerequisites.
- Parts 0-4 as foundation → 5 pilot products → all downstream dependencies.
- Every product linked to its parent concept and prerequisite chapters.
- Also: Section 4 (lines 203-221) contains a Visual Template Establishment Order showing which templates are established by which products and reused where.
- Also: Section 2 (lines 24-181) contains per-batch dependency tables with "Depends On" and "Visual Reuse" columns.

**Completeness:** Full. All 49 products are mapped. The graph is accurate — spot-checked against actual chapter dependency references in Batches 0-1.

**No action required.**

---

### 5. Visual Asset Library — PARTIAL

**What exists:**
- `audit/visualization_plan.md` (461 lines, 40 prioritized entries) — Master plan for all visuals across the entire book. Contains descriptions, ASCII mockups, priorities (P1/P2/P3), and locations. This is a **plan**, not a library of produced assets.
- `production/visual_standard.md` (full document) — Axis conventions, barrier notation templates, payoff chart templates, timeline conventions, color conventions. This is the **standard**, not the assets.
- `production/generation_dashboard.md` §6 — Visual Template Registry tracking 14 templates (9 established in Batches 0-1, 5 planned for Batches 2-9). This is a **registry**, not the assets.
- Inline ASCII diagrams in `Desk_Bible_v2.md` — ~20 payoff diagrams, flow charts, decision trees, and tables embedded in the 10 product chapters and Parts 0-4. These are the **actual visual assets**, but they live inline in the document, not in a separate library.

**What is missing:**
- No separate visual asset library file that catalogs all produced visual assets with: (a) visual type, (b) location in the document, (c) compliance status vs the Visual Standard, (d) reuse information.
- The visualization plan describes what *should* exist; the template registry tracks what *templates* are established; but neither catalogs the actual inline diagrams that have been produced.

**Gap assessment:** The inline approach works and is the intended design — visuals are part of the chapter, not external files. A catalog would help the Visual Design Agent track drift across batches, but the template registry already serves this purpose partially.

---

### 6. Memory-V2 — PARTIAL

**What exists:**
- `framework-v2/MEMORY_DESIGN_GUIDE.md` (full design document, ~180 lines) — Describes the V2 memory architecture: 3 memory types (Terminology, Operational Map, Style Convention), empirical validation that only 3 of 7 planned types were used, path conventions, and usage patterns.
- This is a **design document** extracted as reusable IP from the V1 experience.

**What does NOT exist:**
- No V2-specific memory files. The `memory/` directory contains V1 artifacts only (created 2026-06-18, predating V2 production).
- V2 production does not use the V1 `memory/` files. Instead, V2 relies on:
  - `production/jargon_watchlist.md` (terminology function)
  - `production/generation_dashboard.md` §5-7 (analogy registry, visual template registry, jargon additions — style/convention function)
  - `memory/booking-maps/*.yaml` (operational map function — these V1 files are still accurate and implicitly used)
  - Inline content in `Desk_Bible_v2.md` itself (definitions, conventions, patterns)

**Gap assessment:** V2 generation has effectively replaced the explicit memory file architecture with inline tracking in the production dashboard and framework documents. The V1 booking maps are still accurate and usable. The empty `memory/` subdirectories (components, definitions, examples, reconciliation) confirm the MEMORY_DESIGN_GUIDE's finding that only 3 of 7 memory types were needed. The question is whether V2 needs its own dedicated memory files or whether the current distributed approach (dashboard + framework docs + inline) is sufficient.

---

### 7. Master Book Editor Agent — EXISTS

**Location:** `production/review_workflow.md`, Section 3, Agent 9 (lines 318-370)

**What exists:**
- Full agent definition with objective, review criteria, pass/fail rules, escalation rules, and output format.
- Criteria: cross-chapter duplication detection, bridge sentence verification, analogy domain collision check, structural consistency, section numbering integrity, tone drift detection.
- Successfully deployed during Batch 1 book review and the 10-chapter quality gate.

**Completeness:** Full. No action required.

---

### 8. Beginner Reader Agent — EXISTS

**Location:** `production/review_workflow.md`, Section 3, Agent 10 (lines 372-399)

**What exists:**
- Full agent definition with objective, review criteria, pass/fail rules, and output format.
- Criteria: zero-knowledge accessibility of Parts 0-2, unexplained terms, concept leaps, dependency chain coverage, engagement quality.
- Successfully deployed during Batch 1 book review and the 10-chapter quality gate.

**Completeness:** Full. No action required.

---

### 9. Publication Agent — EXISTS

**Location:** `production/review_workflow.md`, Section 3, Agent 11 (lines 404-431)

**What exists:**
- Full agent definition with objective, review criteria, and output format.
- Criteria: glossary extractability, acronym expansion on first use, figure numbering readiness, chapter sequencing, cross-reference integrity, interview question deduplication, reconciliation red flag deduplication.
- Output format includes `glossary_items` and `index_items` fields — designed to produce glossary/acronym data, but no extraction has been run yet.
- Successfully deployed during the 10-chapter quality gate.

**Completeness:** Full as an agent definition. The agent's *output artifacts* (extracted glossary, acronym index) do not exist yet — they would be produced as a side effect of future batch reviews.

---

## Gap Summary

| # | Asset | Status | Blocks Scaling? | Effort to Create |
|:-:|-------|:------:|:---------------:|:----------------:|
| 1 | Knowledge Base | PARTIAL | No (Batch 2-3) / Maybe (Batch 4+) | 45-60 min |
| 2 | Canonical Glossary | MISSING | No (generation phase) / Yes (publication phase) | 30-40 min (retroactive for 10 chapters) |
| 3 | Acronym Registry | MISSING | No | 20-30 min (retroactive for 10 chapters) |
| 4 | Concept Dependency Graph | EXISTS | — | 0 min |
| 5 | Visual Asset Library | PARTIAL | No | 20-30 min (catalog existing assets) |
| 6 | Memory-V2 | PARTIAL | No (current approach works) | 30-45 min (if explicit files desired) |
| 7 | Master Book Editor Agent | EXISTS | — | 0 min |
| 8 | Beginner Reader Agent | EXISTS | — | 0 min |
| 9 | Publication Agent | EXISTS | — | 0 min |

---

## Recommendations

### Do Not Create Before Scaling

1. **Knowledge Base consolidation** — The distributed approach (dashboard + framework docs + booking maps) works for Batches 2-3 (still ELN family). Consolidation becomes valuable at Batch 4 (Swaps core) when multiple families are actively in play. Create at the Batch 3/4 boundary.

2. **Memory-V2 dedicated files** — V2 generation has organically evolved beyond the V1 file-per-family model. The current approach (production framework docs as living memory) is working. Creating new memory files would duplicate information that already lives in the dashboard and standards documents.

### Create Before Scaling (Incremental, Low Effort)

3. **Canonical Glossary** — Start a `production/canonical_glossary.md` file now and populate incrementally. Extract terms from the 10 existing chapters (retroactive: ~30 min). Then extend it as each new batch is generated (incremental: ~5 min per chapter). This is more efficient than building it retroactively after 49 chapters. The Publication Agent's output format already includes `glossary_items` — route that output to the glossary file.

4. **Acronym Registry** — Start a `production/acronym_registry.md` file now. Extract acronyms from the 10 existing chapters (retroactive: ~20 min). Then extend incrementally. This prevents the drift risk identified in the gap assessment.

### Create When Needed (Not Now)

5. **Visual Asset Library catalog** — The template registry in the dashboard and the visualization plan together cover the need. A formal catalog adds marginal value. Create only if visual drift becomes a pattern in Batches 2-3.

### No Action Required

6. **Concept Dependency Graph** — Exists and is complete.
7. **Master Book Editor Agent** — Exists and has been deployed.
8. **Beginner Reader Agent** — Exists and has been deployed.
9. **Publication Agent** — Exists and has been deployed.

---

## Recommended Execution Order

| Priority | Action | Effort | When |
|:--------:|--------|:------:|------|
| 1 | Create `production/canonical_glossary.md` (retroactive extraction from 10 chapters) | 30 min | Before Batch 2 |
| 2 | Create `production/acronym_registry.md` (retroactive extraction from 10 chapters) | 20 min | Before Batch 2 |
| 3 | Extend glossary and acronym registry after each future batch | 5 min/ch | During Batch 2+ |
| 4 | Consolidate Knowledge Base | 45 min | Before Batch 4 |
| 5 | Visual Asset Library catalog | 20 min | Only if drift detected |
| 6 | Memory-V2 dedicated files | 30 min | Only if distributed approach fails |

**Total effort before Batch 2:** ~50 minutes (glossary + acronym registry)

---

*Audit complete 2026-06-19. No files modified. No assets generated. Awaiting instructions.*
