# Framework v1.3.1 Stabilization Audit

**Date:** 2026-06-20
**Scope:** Complete audit of framework_master_v1.3.md, framework_master_validation.md, publication_architecture.md, and all batch/family/architecture review findings
**Purpose:** Identify ambiguities, gaps, conflicts, and risks before framework freeze

---

## 1. Ambiguous Requirements

| # | Issue | Location | Impact | Recommendation | Resolution |
|:-:|-------|----------|--------|----------------|------------|
| A1 | Family Position §5 is listed as a numbered section AND references a "V16" visual checklist item, implying it counts as a visual asset | v1.3 §5, checklist V16 | Generators may count the Family Position tree toward the 6 visual spec minimum | Clarify: Family Position is a textual navigation aid, NOT a visual specification or publication asset. V16 checks presence of the tree, not its status as a visual spec | **RESOLVED in v1.3.1** — Family Position exclusion documented |
| A2 | §20 Mental Models references "§25" in the Core Analogy specification | v1.3 Section C, §2 | Typo — there is no §25; Mental Models is §20 | Correct cross-reference from §25 to §20 | **RESOLVED in v1.3.1** — Fixed |
| A3 | "Who Touches This Product" says 8 roles for Batch 6+, but checklist item P5 says "8 rows [v1.3] or 5 rows [grandfathered]" without specifying which batches are grandfathered | v1.3 Section J, checklist P5 | Ambiguity about whether Batch 5 chapters need 5 or 8 roles during harmonization | Clarify: Batches 0-5 retain 5 roles. Batch 6+ requires 8 roles. Harmonization pass may upgrade earlier chapters but is not mandatory | **RESOLVED in v1.3.1** |
| A4 | Word count range changed to 3,000-5,500 for v1.3 but no rationale links the increase to the specific new sections added | v1.3 Section C length table | Generators may produce unnecessarily long chapters | Add rationale: +600 words from v1.2 additions (Desk Reality, expanded Commercial Understanding, Publication Assets) + ~800 words from v1.3 additions (Product DNA, Family Position, Product Evolution, Market Invention, Product Lifecycle, expanded desk roles) = ~1,400 words above v1.0 baseline | **RESOLVED in v1.3.1** |
| A5 | "Visual Learning Recommendations" appears in Section B.2 and checklist V5-V7 alongside "Visual Specifications (Publication Assets)" in V8-V14 — unclear if both are required or if one supersedes | v1.3 Section B.2, checklist | Generators may produce two separate visual blocks (Recommendations AND Specifications) | Clarify: "Visual Specifications (Publication Assets)" supersedes "Visual Learning Recommendations" for v1.3 chapters. V5-V7 are grandfathered checks for Batches 0-3. Batch 4+ uses the Publication Asset format | **RESOLVED in v1.3.1** |

## 2. Duplicate Requirements

| # | Issue | Location | Impact | Recommendation | Resolution |
|:-:|-------|----------|--------|----------------|------------|
| D1 | Checklist C11 ("Every visual spec has inline figure reference") duplicates V15 (same check, moved from Consistency to Visual) | v1.3 checklist C11, V15 | Double-counting the same check inflates the checklist | Remove C11. V15 covers the requirement. Renumber C12 → C11 | **RESOLVED in v1.3.1** |
| D2 | Six Permanent Educational Rules appear in both Section A.3 and are implicitly repeated in checklist items E1-E6 | v1.3 Section A.3, checklist | Not harmful — the checklist operationalizes the rules — but the duplication creates two places to update | No action needed. This is intentional: Section A states the rules; the checklist operationalizes them. Document this relationship explicitly | **RESOLVED — documented** |

## 3. Conflicting Requirements

| # | Issue | Location | Impact | Recommendation | Resolution |
|:-:|-------|----------|--------|----------------|------------|
| F1 | v1.3 says "22 numbered sections" but checklist C5 says "All 22 sections present in correct order" — for grandfathered chapters (Batches 0-5) the section count is 16, not 22 | v1.3 Section C, checklist C5 | Grandfathered chapters would fail C5 under v1.3 rules | Clarify C5: "All sections present per the applicable framework version (16 for v1.0-v1.2, 22 for v1.3)" | **RESOLVED in v1.3.1** |
| F2 | Visual spec minimum: v1.2 says 5 with 2P1+2P2+1P3. v1.3 says 6 with 2P1+2P2+2P3. Checklist V8 says "at least 6" and V11 says "2P1+2P2+2P3" — but Batch 5 chapters have 5 specs with 2P1+2P2+1P3 | v1.3 Section K.3, checklist V8, V11 | Batch 5 chapters pass under v1.2 but would fail under v1.3 | Grandfathering already handles this. Document explicitly: V8 and V11 apply only to Batch 6+ chapters | **RESOLVED in v1.3.1** |

## 4. Publication Risks

| # | Issue | Location | Impact | Recommendation | Resolution |
|:-:|-------|----------|--------|----------------|------------|
| P1 | No formal definition of "publication readiness" score despite it appearing in quality targets (Section S) | v1.3 Section S | Publication Readiness ≥ 8.0 target exists but no scoring rubric | Define rubric: visual spec completeness (30%), figure reference integrity (20%), filename convention compliance (20%), asset description quality (20%), reuse classification accuracy (10%) | **RESOLVED in v1.3.1** |
| P2 | publication_architecture.md defines SVG/PNG/DOCX/PDF standards but does not define the generation workflow sequence | publication_architecture.md | Risk of out-of-order asset generation | Add workflow: (1) all chapters complete → (2) harmonization pass → (3) SVG generation → (4) PNG fallback → (5) DOCX assembly → (6) PDF generation → (7) publication QA | **RESOLVED in v1.3.1** |
| P3 | No validation step defined between SVG generation and DOCX assembly | publication_architecture.md | Bad SVGs could propagate into final documents | Add SVG validation step: check viewBox, accessibility attributes, font declarations, color compliance | **RESOLVED in v1.3.1** |

## 5. Governance Gaps

| # | Issue | Location | Impact | Recommendation | Resolution |
|:-:|-------|----------|--------|----------------|------------|
| G1 | No formal policy on when framework modifications are permitted post-freeze | v1.3 (absent) | Risk of ad-hoc framework changes during generation | Add Framework Freeze Notice: modifications only for critical defects, require explicit documentation | **RESOLVED — freeze notice created** |
| G2 | No formal definition of "critical defect" that would justify framework modification | v1.3 (absent) | Subjective threshold for reopening the framework | Define: a critical defect is one that (a) causes chapters to be generated with factually incorrect structure, (b) creates an unresolvable contradiction between requirements, or (c) makes publication impossible | **RESOLVED in v1.3.1** |
| G3 | Review agent list says "11 chapter + 3 book-level" but no governance rule prevents adding more agents | v1.3 Section R | Risk of agent proliferation | Add: "No additional review agents may be introduced. The current review stack is final." | **RESOLVED in v1.3.1** |
| G4 | No complexity registry exists — complexity scores are defined conceptually but not tracked per product | v1.3 Section D | Scores may be inconsistent across batches without a central registry | Create complexity_registry.yaml | **RESOLVED — registry created** |
| G5 | No visual asset master registry exists — visual specs are scattered across 49 chapters with no central tracking | v1.3 (absent) | Risk of duplicate Visual IDs, filename conflicts, and missed assets during publication | Create visual_asset_master_registry.yaml | **RESOLVED — registry created** |

## 6. Review-Process Gaps

| # | Issue | Location | Impact | Recommendation | Resolution |
|:-:|-------|----------|--------|----------------|------------|
| R1 | Book-level agents (Master Book Editor, Beginner Reader Agent, Publication Agent) are listed but have no scoring rubric | v1.3 Section R.2 | Book-level agents produce qualitative reviews but no scores, making quality tracking inconsistent | Define: book-level agents produce qualitative assessments (PASS/CONCERNS/FAIL), not numerical scores. Chapter-level agents produce numerical scores | **RESOLVED in v1.3.1** |
| R2 | No formal trigger for family-level reviews — framework says "whenever a family is completed" but does not define completion | v1.3 Section R.3 | Ambiguity about when to run family reviews | Define: a family is "completed" when all products in the product_generation_order.md for that Part 5 subsection have been accepted | **RESOLVED in v1.3.1** |

## 7. Reader-Experience Gaps

| # | Issue | Location | Impact | Recommendation | Resolution |
|:-:|-------|----------|--------|----------------|------------|
| X1 | No milestone assessments between families — readers have no reinforcement checkpoints | v1.3 (absent) | Reader retention decreases over 49 sequential chapters without knowledge consolidation | Define milestone assessment architecture (architecture only, not content) | **RESOLVED — architecture defined in v1.3.1** |
| X2 | No formal reader journey validation — no check that a beginner can follow the entire sequential path | v1.3 (absent) | The Beginner Reader Agent is defined but has no formal process | Define: Beginner Reader Agent runs at batch level, validates that dependency chains are complete and bridge texts are accurate | **RESOLVED in v1.3.1** |

## 8. Scalability Risks

| # | Issue | Location | Impact | Recommendation | Resolution |
|:-:|-------|----------|--------|----------------|------------|
| S1 | Analogy registry in dashboard §5 will reach 49+ entries — registry may become unwieldy | Dashboard §5 | Difficult to check for collisions at scale | No action needed — the registry is a flat list and 49 entries is manageable. Linear search is sufficient | **Accepted — no action** |
| S2 | Visual specs at 6 per chapter × 49 chapters = 294+ specs — no batch-level tracking | v1.3 (absent) | Risk of duplicate Visual IDs or filename conflicts across chapters | Mitigated by visual_asset_master_registry.yaml | **RESOLVED** |

## 9. Registry-Management Risks

| # | Issue | Location | Impact | Recommendation | Resolution |
|:-:|-------|----------|--------|----------------|------------|
| M1 | Jargon Watchlist (dashboard §7) tracks "Added to Watchlist: YES" but does not track whether the term was added to glossary.yaml | Dashboard §7 | Terms may be watchlisted but never formalized in the glossary | Add column: "Added to Glossary" (YES/NO/CHAPTER-SPECIFIC). Deferred to harmonization pass | **Deferred** |
| M2 | No governance for complexity_registry.yaml — who updates it, when, and how conflicts are resolved | v1.3 (absent) | Complexity scores may drift without governance | Define governance in registry file header | **RESOLVED — governance in registry** |

## 10. Future Publication Risks

| # | Issue | Location | Impact | Recommendation | Resolution |
|:-:|-------|----------|--------|----------------|------------|
| FP1 | No accessibility standard beyond SVG aria-label — no guidance for alt text, color contrast, or screen reader support | publication_architecture.md §6 | Publication may not meet accessibility requirements | Add: WCAG 2.1 AA color contrast (4.5:1 minimum), alt text = caption text, all data in tables not just graphics | **RESOLVED in v1.3.1** |
| FP2 | No versioning strategy for publication assets — if an SVG is regenerated, the old version is overwritten | publication_architecture.md (absent) | No rollback capability for asset changes | Add: SVG files are versioned by git. No separate asset versioning needed — git provides the history | **RESOLVED — git versioning** |

---

## Audit Summary

| Category | Issues Found | Resolved | Deferred | Accepted |
|----------|:-----------:|:--------:|:--------:|:--------:|
| Ambiguous requirements | 5 | 5 | 0 | 0 |
| Duplicate requirements | 2 | 2 | 0 | 0 |
| Conflicting requirements | 2 | 2 | 0 | 0 |
| Publication risks | 3 | 3 | 0 | 0 |
| Governance gaps | 5 | 5 | 0 | 0 |
| Review-process gaps | 2 | 2 | 0 | 0 |
| Reader-experience gaps | 2 | 2 | 0 | 0 |
| Scalability risks | 2 | 1 | 0 | 1 |
| Registry-management risks | 2 | 1 | 1 | 0 |
| Future publication risks | 2 | 2 | 0 | 0 |
| **Total** | **27** | **25** | **1** | **1** |

**Audit Result:** 25 of 27 issues resolved in v1.3.1. 1 deferred to harmonization pass (M1). 1 accepted as-is (S1).

---

*Audit completed 2026-06-20. All critical issues resolved. Framework ready for freeze.*
