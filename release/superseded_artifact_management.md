# Superseded Artifact Management — SP-KE-V1.0

**Version**: 1.0
**Date**: 2026-06-27
**Purpose**: Classify every production artifact as KEEP, ARCHIVE, DELETE, or SUPERSEDE

---

## Classification Rules

| Action | Definition | Physical Effect |
|--------|-----------|-----------------|
| **KEEP** | Canonical V1.0 artifact — part of the release | No change. File remains in `production/` |
| **ARCHIVE** | Non-canonical. Retained for provenance but not part of release | File remains in place. Tagged as archive in manifest |
| **SUPERSEDE** | Replaced by a newer version. Retained for provenance | File remains in place. Successor identified in manifest |
| **DELETE** | Dangerous, incorrect, or misleading. Should be removed | NOT RECOMMENDED — all files retained for audit trail |

---

## Full Classification

### KEEP — Canonical Content (13 artifacts)

| # | Filename | Reason |
|:-:|----------|--------|
| 1 | `Desk_Bible_v2.md` | Primary deliverable |
| 2 | `production/infrastructure_encyclopedia_v1.md` | Canonical infrastructure handbook |
| 3 | `production/product_dna_atlas.md` | Canonical product identity |
| 4 | `production/interview_system_v2_2.md` | Current interview system |
| 5 | `production/solutions_manual.md` | Canonical structuring decisions |
| 6 | `production/framework_master_v1.3.1.md` | Current governing template |
| 7 | `production/product_universe_map.md` | Canonical navigation |
| 8 | `production/product_comparison_matrix.md` | Canonical comparison |
| 9 | `production/learning_dependency_graph.md` | Canonical prerequisites |
| 10 | `production/product_evolution_map.md` | Canonical evolution |
| 11 | `production/complexity_registry.yaml` | Canonical scores |
| 12 | `production/publication_taxonomy.yaml` | Canonical taxonomy |
| 13 | `production/jargon_watchlist.md` | Canonical vocabulary |

### KEEP — Governance (12 artifacts)

| # | Filename | Reason |
|:-:|----------|--------|
| 14 | `production/framework_freeze_notice.md` | Active freeze declaration |
| 15 | `production/framework_master_v1.3.1_validation.md` | Active validation report |
| 16 | `production/chapter_acceptance_checklist.md` | Active quality gate |
| 17 | `production/chapter_generation_standard.md` | Active authoring standard |
| 18 | `production/visual_standard.md` | Active visual spec |
| 19 | `production/visual_asset_governance.md` | Active governance |
| 20 | `production/visual_asset_master_registry.yaml` | Active registry |
| 21 | `production/professor_voice_standard.md` | Active voice standard |
| 22 | `production/publication_architecture.md` | Active architecture |
| 23 | `production/publication_identifier_standard.md` | Active ID standard |
| 24 | `production/question_identifier_standard.md` | Active question ID standard |
| 25 | `production/review_workflow.md` | Active workflow |

### ARCHIVE — Planning & Tracking (11 artifacts)

| # | Filename | Reason | Risk if Removed |
|:-:|----------|--------|-----------------|
| 26 | `production/generation_dashboard.md` | Generation complete. Historical record only | Low — tracking data |
| 27 | `production/product_generation_order.md` | Batch plan executed. Historical | Low |
| 28 | `production/final_universe_rationale.md` | Selection rationale. Useful for provenance | Medium — explains product choices |
| 29 | `production/execution_readiness_report.md` | Pre-gen check. Historical | Low |
| 30 | `production/front_matter_plan.md` | Planning document. Historical | Low |
| 31 | `production/harmonization_master_checklist.md` | Harmonization complete. Historical | Low |
| 32 | `production/visual_prioritization_matrix.md` | Priority ranking. Historical | Low |
| 33 | `production/publication_build_tracker.md` | Build tracking. Historical | Low |
| 34 | `production/digital_supplement_tracker.md` | Supplement tracking. Historical | Low |
| 35 | `production/volume_1_completion_tracker.md` | Vol 1 tracking. Historical | Low |
| 36 | `production/volume_2_completion_tracker.md` | Vol 2 tracking. Historical | Low |

### SUPERSEDE — Replaced by Newer Versions (6 artifacts)

| # | Filename | Superseded By | Version Gap | Reason |
|:-:|----------|---------------|:-----------:|--------|
| 37 | `production/framework_master_v1.3.md` | `framework_master_v1.3.1.md` | 1 minor | Bugfix release |
| 38 | `production/framework_master_validation.md` | `framework_master_v1.3.1_validation.md` | 1 minor | Corresponds to v1.3 |
| 39 | `production/framework_readiness_report.md` | `framework_freeze_notice.md` | N/A | Pre-freeze → post-freeze |
| 40 | `production/interview_system.md` | `interview_system_v2_2.md` | 2 major | V1 → V2.2 |
| 41 | `production/interview_system_v2.md` | `interview_system_v2_2.md` | 2 minor | V2.0 → V2.2 |
| 42 | `production/interview_system_v2_1.md` | `interview_system_v2_2.md` | 1 minor | V2.1 → V2.2 |

### ARCHIVE — Orphan (6 artifacts)

| # | Filename | Reason | Origin |
|:-:|----------|--------|--------|
| 43 | `production/part6_sections_1_3.md` | Content integrated into Desk Bible Part 6 | Draft fragment |
| 44 | `production/part6_sections_4_6.md` | Content integrated into Desk Bible Part 6 | Draft fragment |
| 45 | `production/part6_sections_7_9.md` | Content integrated into Desk Bible Part 6 | Draft fragment |
| 46 | `production/part6_sections_10_11.md` | Content integrated into Desk Bible Part 6 | Draft fragment |
| 47 | `production/infrastructure_integration_plan.md` | Integration complete | Planning |
| 48 | `production/figma_production_architecture.md` | Unreferenced by any canonical artifact | Design tooling |

---

## Summary

| Action | Count | Recommendation |
|--------|:-----:|----------------|
| KEEP (Content) | 13 | No action required |
| KEEP (Governance) | 12 | No action required |
| ARCHIVE (Planning) | 11 | Retain. Tag as archive in manifest |
| SUPERSEDE | 6 | Retain. Tag as superseded with successor |
| ARCHIVE (Orphan) | 6 | Retain. Tag as orphan in manifest |
| DELETE | 0 | No deletions recommended |
| **Total** | **48** | **All files accounted for** |

---

## DELETE Candidates — None

No artifacts recommended for deletion. All files retained for:
- **Provenance**: Superseded versions document the evolution of the ecosystem
- **Audit trail**: Planning documents explain decisions made during development
- **Orphan recovery**: Draft fragments may be useful for future reference

---

*Superseded Artifact Management — SP-KE-V1.0 — Generated 2026-06-27*
