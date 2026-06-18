# Release Notes — Desk Bible v1.0

**Release date:** 2026-06-19  
**Tag:** `desk-bible-complete-v1`  
**Commit:** `5faaff0`

---

## Project Overview

The Structured Products Desk Bible is a comprehensive reference document covering 28 structured products across 5 families. Each product has a standardised 8-section page covering definition, construction, booking and systems, pricing intuition, a worked example with full arithmetic, reconciliation, desk view, and desk shorthand.

The bible was generated using an 8-stage automated pipeline (Research → Architecture → Writing → Booking → QA → Style → CrossRef → Publish) backed by a per-family memory layer (terminology, booking maps, style patterns).

---

## Product Counts by Family

| Family | Count | Products |
|--------|------:|----------|
| ELN (Equity-Linked Notes) | 13 | RC001, DRC001, KODRC001, CRC001, AIRBAG001, PHX001, FCN001, CRAELN001, BONUS001, PPN001, WARRANT001, ICN001, DIGITAL001 |
| SRT (Structured Rate Trades) | 5 | IRCFRN001, AFRN001, NCRA001, CRASRT001, DCFN001 |
| CLN (Credit-Linked Notes) | 5 | VCLN001, SCLN001, FTD001, NTD001, TRANCHE001 |
| STEG (Steepener Notes) | 4 | VSTEG001, RASTEG001, CSTEG001, TARN001 |
| Swap | 1 | SWAP001 |
| **Total** | **28** | |

---

## Final Quality Metrics

| Metric | Value |
|--------|-------|
| QA BLOCKERs (total) | 0 |
| QA MAJOR advisories (total) | 31 |
| Style MUST_FIX violations (total) | 0 |
| Broken cross-references (total) | 0 |
| Publishing failures (total) | 0 |
| QA gate pass rate | 28/28 (100%) |
| Style gate pass rate | 28/28 (100%) |
| CrossRef gate pass rate | 28/28 (100%) |
| Publish gate pass rate | 28/28 (100%) |

All 31 QA MAJOR findings were advisory (decomposition format conventions inherent to the product structure). None required content changes.

---

## Final Memory Metrics

| Metric | Value |
|--------|-------|
| Memory artifacts created | 15 (3 per family × 5 families) |
| Memory artifacts reused | 69 cumulative reuse events |
| Families with complete memory | 5 of 5 |
| Accepted conventions added | 5+ (per-family) |
| Known false positives suppressed | 3 per product (84 total) |

### Memory Artifacts

| Family | Terminology | Booking Map | Style Patterns |
|--------|:-----------:|:-----------:|:--------------:|
| ELN | `memory/terminology/ELN.yaml` | `memory/booking-maps/ELN_system_mapping.yaml` | `memory/style-patterns/ELN.yaml` |
| SRT | `memory/terminology/SRT.yaml` | `memory/booking-maps/SRT_system_mapping.yaml` | `memory/style-patterns/SRT.yaml` |
| CLN | `memory/terminology/CLN.yaml` | `memory/booking-maps/CLN_system_mapping.yaml` | `memory/style-patterns/CLN.yaml` |
| STEG | `memory/terminology/STEG.yaml` | `memory/booking-maps/STEG_system_mapping.yaml` | `memory/style-patterns/STEG.yaml` |
| Swap | `memory/terminology/Swap.yaml` | `memory/booking-maps/Swap_system_mapping.yaml` | `memory/style-patterns/Swap.yaml` |

---

## Git Tags Created

| Tag | Milestone |
|-----|-----------|
| `desk-bible-v2-production-ready` | Pipeline v2.1 baseline (6 products) |
| `desk-bible-after-batch-1` | ELN batch 1 complete (11 products) |
| `desk-bible-after-batch-2` | ELN family complete (16 products) |
| `desk-bible-before-batch-3` | Pre-SRT/STEG generation |
| `desk-bible-after-batch-3a` | SRT family complete (20 products) |
| `desk-bible-after-steg-bootstrap` | STEG bootstrapped (21 products) |
| `desk-bible-75-percent-complete` | 75% milestone |
| `desk-bible-after-batch-4` | STEG complete, CLN 3/5 (26 products) |
| `desk-bible-before-final-batch` | Pre-final safety snapshot |
| `desk-bible-complete-v1` | All 28 products complete |

---

## Major Milestones

| Date | Milestone |
|------|-----------|
| 2026-06-18 | Pipeline v2.1 production-ready (QA arithmetic protocol, style conventions) |
| 2026-06-18 | Batch 0: 6 baseline products across 4 families |
| 2026-06-18 | Batch 1: ELN sections 3.1 and 3.2 complete |
| 2026-06-18 | Batch 2: ELN family complete (13/13) |
| 2026-06-18 | Batch 3A: SRT family complete (5/5) |
| 2026-06-19 | Batch 3B: STEG family bootstrapped (cleanest bootstrap) |
| 2026-06-19 | 75% milestone (21 products) |
| 2026-06-19 | Batch 4: STEG complete (4/4), CLN at 3/5 |
| 2026-06-19 | Final batch: CLN complete (5/5), project complete |

---

## Known Limitations

1. **No Deposit family products.** The Deposit family exists in the architecture but no products were scoped. Deposits are vanilla instruments that do not typically require desk bible coverage.

2. **Batch 0 artifact variance.** The first 6 products (PHX001, RC001, DRC001, VCLN001, IRCFRN001, SWAP001) were generated before the pipeline was fully standardised. Some have slightly different artifact structures (e.g., missing blueprint files for PHX001/IRCFRN001/SWAP001, legacy pipeline-log formats for PHX001).

3. **Static content.** Product pages reflect market conventions as of June 2026. Benchmark rates, index compositions, and recovery assumptions may change over time. See the Maintenance and Governance Guide for annual review procedures.

4. **No live system validation.** System mappings (NEMO/Sophis vs Murex) were documented based on desk knowledge, not validated against live booking systems.

5. **QA is arithmetic-only.** The QA gate verifies computational correctness of worked examples. It does not validate pricing models, market data, or business logic beyond arithmetic.

---

## Future Enhancement Opportunities

1. **Deposit family.** If deposits require desk bible coverage in the future, the family can be bootstrapped using the procedure in the Maintenance and Governance Guide (Section 4).

2. **Cross-product comparison tables.** A summary table comparing key features (system, complexity, optionality) across all 28 products would aid navigation.

3. **Interactive worked examples.** The static Markdown worked examples could be converted to interactive calculators that let users modify inputs and see updated outputs.

4. **Automated annual review.** The manual annual review checklist could be automated as a pipeline stage that validates market conventions against current data.

5. **DOCX/PDF generation pipeline.** Currently, document assembly is a manual concatenation step. A Pandoc-based build script would automate this with consistent formatting.

6. **Batch 0 artifact normalisation.** The 6 Batch 0 products could be re-run through the standardised pipeline to align their artifact structures with later products.

---

## Release Package Contents

```
release/desk-bible-v1/
├── Desk_Bible_v1.md                    # Assembled 28-product document
├── release_notes_v1.md                 # This file
├── catalog.yaml                        # Product catalog (source of truth)
├── Desk_Bible_Final_Report.md          # 5-section final report
├── desk_bible_progress.md              # Dashboard (100%)
├── production_history.log              # Full batch-by-batch history
├── Maintenance_and_Governance_Guide.md # Operational runbook
├── memory/                             # 15 family memory artifacts
│   ├── booking-maps/                   # 5 system mapping files
│   ├── style-patterns/                 # 5 style rule files
│   └── terminology/                    # 5 terminology files
├── checkpoints/                        # 28 product checkpoint files
└── outputs/                            # 280+ pipeline artifacts
    ├── research/                       # 28 research YAMLs
    ├── blueprints/                     # 25+ blueprint YAMLs
    ├── drafts/                         # 28 product page Markdowns
    ├── booking/                        # 28 booking YAMLs
    ├── reviews/                        # 28+ QA review YAMLs
    ├── style/                          # 28+ style review YAMLs
    ├── crossref/                       # 28+ cross-reference YAMLs
    └── publish/                        # 28+ publishing gate YAMLs
```
