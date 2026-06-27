# Release Folder Architecture — SP-KE-V1.0

**Version**: 1.0
**Date**: 2026-06-27
**Purpose**: Define canonical folder structure for permanent V1.0 release

---

## Publication Folder Structure

```
Structured Products/
│
├── Desk_Bible_v2.md                          # Primary manuscript (25,764 lines)
│
├── production/                                # All production artifacts
│   │
│   ├── ── CANONICAL CONTENT ──────────────────
│   ├── infrastructure_encyclopedia_v1.md      # Infrastructure handbook
│   ├── product_dna_atlas.md                   # 49 product identity cards
│   ├── interview_system_v2_2.md               # Interview preparation system
│   ├── solutions_manual.md                    # Structuring decisions
│   ├── framework_master_v1.3.1.md             # Governing chapter template
│   ├── product_universe_map.md                # Navigation graphs
│   ├── product_comparison_matrix.md           # 12-dimension comparison
│   ├── learning_dependency_graph.md           # Prerequisite DAG
│   ├── product_evolution_map.md               # Family evolution trees
│   ├── complexity_registry.yaml               # Canonical complexity scores
│   ├── publication_taxonomy.yaml              # Categorical values
│   ├── jargon_watchlist.md                    # Controlled vocabulary
│   │
│   ├── ── GOVERNANCE ─────────────────────────
│   ├── framework_freeze_notice.md             # Framework freeze declaration
│   ├── framework_master_v1.3.1_validation.md  # Template compliance report
│   ├── chapter_acceptance_checklist.md         # Quality gate criteria
│   ├── chapter_generation_standard.md         # Authoring instructions
│   ├── visual_standard.md                     # Visual specifications
│   ├── visual_asset_governance.md             # Visual lifecycle rules
│   ├── visual_asset_master_registry.yaml      # Visual catalogue
│   ├── professor_voice_standard.md            # Voice guidelines
│   ├── publication_architecture.md            # Document structure
│   ├── publication_identifier_standard.md     # Section numbering rules
│   ├── question_identifier_standard.md        # Question ID format
│   ├── review_workflow.md                     # Editorial process
│   │
│   ├── ── PLANNING (ARCHIVE CANDIDATES) ─────
│   ├── generation_dashboard.md
│   ├── product_generation_order.md
│   ├── final_universe_rationale.md
│   ├── execution_readiness_report.md
│   ├── front_matter_plan.md
│   ├── harmonization_master_checklist.md
│   ├── visual_prioritization_matrix.md
│   ├── publication_build_tracker.md
│   ├── digital_supplement_tracker.md
│   ├── volume_1_completion_tracker.md
│   ├── volume_2_completion_tracker.md
│   │
│   ├── ── SUPERSEDED (ARCHIVE) ──────────────
│   ├── framework_master_v1.3.md               # → v1.3.1
│   ├── framework_master_validation.md         # → v1.3.1 validation
│   ├── framework_readiness_report.md          # → freeze notice
│   ├── interview_system.md                    # → v2.2
│   ├── interview_system_v2.md                 # → v2.2
│   ├── interview_system_v2_1.md               # → v2.2
│   │
│   ├── ── ORPHAN (ARCHIVE) ──────────────────
│   ├── part6_sections_1_3.md                  # → integrated into Desk Bible §6
│   ├── part6_sections_4_6.md                  # → integrated into Desk Bible §6
│   ├── part6_sections_7_9.md                  # → integrated into Desk Bible §6
│   ├── part6_sections_10_11.md                # → integrated into Desk Bible §6
│   ├── infrastructure_integration_plan.md     # → integration complete
│   └── figma_production_architecture.md       # → unreferenced
│
├── release/                                   # Release engineering output
│   ├── release_manifest.md
│   ├── release_dependency_manifest.md
│   ├── release_folder_architecture.md         # (this file)
│   ├── metadata_consistency_report.md
│   ├── complexity_registry_synchronization.md
│   ├── cross_reference_validation_report.md
│   ├── superseded_artifact_management.md
│   ├── terminology_freeze_report.md
│   ├── publication_release_notes_v1_0.md
│   ├── publication_freeze_certificate_v1_0.md
│   ├── final_release_engineering_report.md
│   └── ecosystem_v1_0_final_verdict.md
│
├── review/                                    # Prior review deliverables
│   ├── ecosystem_integration_audit.md
│   ├── final_publication_verdict.md
│   ├── educational_quality_review.md
│   ├── practitioner_realism_review.md
│   └── Case_Study.md
│
├── audit/                                     # Audit artifacts
├── design/                                    # Design artifacts
├── outputs/                                   # Generated outputs (DOCX, PDF)
├── reference/                                 # Reference materials
└── reports/                                   # Reports
```

---

## Architecture Rules

1. **Desk Bible** sits at project root — it is the primary deliverable
2. **`production/`** contains all production artifacts — canonical, governance, planning, superseded, and orphan — in a flat structure
3. **`release/`** contains all release engineering documents — generated during this V1.0 release pass
4. **`review/`** contains all review deliverables from prior audit cycles
5. No artifact may be moved between directories after freeze
6. No new files may be added to `production/` after freeze
7. Archive-tagged files remain in place with their tags — no physical deletion

---

## File Counts

| Directory | Files | Purpose |
|-----------|:-----:|---------|
| Root | 1 | Desk Bible |
| `production/` | 48 | All production artifacts |
| `release/` | 12 | Release engineering (this pass) |
| `review/` | 5 | Prior reviews |
| **Total tracked** | **66** | |

---

*Release Folder Architecture — SP-KE-V1.0 — Generated 2026-06-27*
