# Knowledge Base Pipeline Framework

A reusable framework for generating structured, artifact-based knowledge bases using an 8-stage automated pipeline with per-family memory, checkpoint-based resumption, and multi-gate quality control.

Originally developed for the Structured Products Desk Bible (28 products, 5 families). Designed to be adapted to any domain where standardised documentation must be produced at scale with consistent quality.

---

## Architecture

```
                        ┌──────────────────┐
                        │  Product Catalog  │
                        │  (source of truth)│
                        └────────┬─────────┘
                                 │
                        ┌────────▼─────────┐
                        │   ORCHESTRATOR    │
                        │  (mode router)    │
                        └────────┬─────────┘
                                 │
             ┌───────────────────┼───────────────────┐
             │                   │                   │
      ┌──────▼──────┐    ┌──────▼──────┐    ┌──────▼──────┐
      │    DRAFT     │    │   REVIEW    │    │  PUBLISH    │
      │ (stages 1-4) │    │ (stages 5-7)│    │ (stage 8)   │
      └──────┬──────┘    └──────┬──────┘    └─────────────┘
             │                   │
   ┌─────────┼─────────┐   ┌────┼────┐
   │         │         │   │    │    │
Research  Architect  Writer QA  Style CrossRef
   │         │         │   │    │    │
   ▼         ▼         ▼   ▼    ▼    ▼
 .yaml     .yaml      .md .yaml .yaml .yaml
```

### Core Principles

1. **Artifact-based.** Every stage produces a file on disk. The pipeline can be interrupted and resumed from any checkpoint.
2. **Memory-first.** Per-family memory artifacts (terminology, system mappings, style patterns) are created once and reused across all products in the family.
3. **Gate-based quality.** Three review gates (QA, Style, CrossRef) must pass before publication. Gates are binary — PASS or FAIL.
4. **Deterministic order.** Stages run sequentially within a mode. Dependencies are explicit: each stage consumes the output of the previous stage.

---

## Pipeline Stages

### DRAFT Mode (Stages 1–4)

| Stage | Name | Input | Output | Purpose |
|-------|------|-------|--------|---------|
| 1 | **Research** | Catalog entry + domain knowledge | `outputs/research/{ID}.yaml` | Gather parameters, pricing drivers, risk factors, market context |
| 2 | **Architecture** | Research YAML | `outputs/blueprints/{ID}.yaml` | Plan each section's content, key points, and structure |
| 3 | **Writing** | Blueprint YAML + memory artifacts | `outputs/drafts/{ID}.md` | Generate the full document with all sections |
| 4 | **Booking / Mapping** | Blueprint YAML + system mapping memory | `outputs/booking/{ID}.yaml` | Map the product to operational systems, document failure modes |

### REVIEW Mode (Stages 5–7)

| Stage | Name | Input | Output | Gate |
|-------|------|-------|--------|------|
| 5 | **QA Review** | Draft MD | `outputs/reviews/{ID}_qa.yaml` | PASS if zero BLOCKERs |
| 6 | **Style Review** | Draft MD + style-pattern memory | `outputs/style/{ID}_style.yaml` | PASS if zero MUST_FIX |
| 7 | **Cross-Reference** | Draft MD + catalog | `outputs/crossref/{ID}_crossref.yaml` | PASS if zero broken refs |

### PUBLISH Mode (Stage 8)

| Stage | Name | Input | Output | Gate |
|-------|------|-------|--------|------|
| 8 | **Publisher** | All review YAMLs | `outputs/publish/{ID}_pubspec.yaml` | READY if all prior gates passed |

### Execution Modes

- **DRAFT** — Run stages 1–4 only. Use for initial content generation.
- **REVIEW** — Run stages 5–7 only. Use after fixing issues found in a prior review.
- **PUBLISH** — Run stage 8 only. Use after all reviews pass.
- **FULL** — Run all 8 stages end-to-end. Use for new products when confident in quality.

---

## Memory Layer

Memory artifacts are per-family YAML files that store reusable knowledge. They prevent the pipeline from re-deriving the same decisions for every product in a family.

### Three Memory Types

| Type | Path | Purpose | Example Content |
|------|------|---------|-----------------|
| **Terminology** | `memory/terminology/{FAMILY}.yaml` | Product names, abbreviations, casing rules | "SOFR" not "Sofr"; "CLN" first mentioned as "Credit-Linked Note (CLN)" |
| **System Mapping** | `memory/booking-maps/{FAMILY}_system_mapping.yaml` | Which operational system books this family | NEMO + Sophis for credit/equity; Murex for rates |
| **Style Patterns** | `memory/style-patterns/{FAMILY}.yaml` | Heading format, known false positives, accepted conventions | H4 names are canonical; suppress Sophis casing FP |

### Memory Lifecycle

1. **Created** during family bootstrap (first product in a new family).
2. **Reused** by all subsequent products in the family.
3. **Updated** when new conventions are validated across multiple products.
4. **Never deleted** unless the entire family is removed.

### Convention Validation Protocol

A new convention (e.g., a decomposition format specific to a family) should not be added to the style-patterns file immediately. Instead:

1. Observe it in the bootstrap product. Note it but defer.
2. Validate it in the next 1–2 products of the same family.
3. If it recurs and is inherent to the product structure (not an error), add it as an `accepted_convention`.

---

## Checkpoints

Each product has a checkpoint file (`checkpoints/{ID}.json`) that tracks:

- Which stages are complete.
- Gate results for each review stage.
- Retry count.
- Whether checkpoint recovery was used.
- Overall `all_gates_passed` status.

Checkpoints enable:

- **Resumption.** If the pipeline is interrupted, it can resume from the last completed stage.
- **Validation.** A bulk check can verify all products have complete checkpoints with passing gates.
- **Auditing.** The checkpoint record shows whether any product required retries.

---

## Review Gates

### QA Gate (Stage 5)

- **Protocol:** v2.1 — arithmetic verification with ±0.2% rounding tolerance.
- **Rule:** Computationally verify all arithmetic in the worked example before raising a BLOCKER.
- **PASS criteria:** Zero BLOCKERs.
- **Advisory findings (MAJOR):** Decomposition format conventions that are inherent to the product structure. These are noted but do not block publication.

### Style Gate (Stage 6)

- **Checks:** Heading structure, currency notation, system casing, desk shorthand format, forbidden phrases.
- **PASS criteria:** Zero MUST_FIX violations.
- **Known false positives:** Suppressed per-family using the style-patterns memory file. Common FPs: H4 heading names, system name casing, legal document naming.

### CrossRef Gate (Stage 7)

- **Checks:** Every product ID mentioned in the draft exists in the catalog and has a corresponding draft file.
- **PASS criteria:** Zero broken references.
- **Forward references:** References to products that exist in the catalog but haven't been generated yet. These are flagged as warnings, not broken references.

---

## Publishing Workflow

The publishing gate (stage 8) is the final checkpoint before a product is marked `complete`. It verifies:

1. Draft file exists and has all required sections.
2. QA gate: PASS.
3. Style gate: PASS.
4. CrossRef gate: PASS.
5. Zero blocking issues remain.

If all checks pass, the gate result is `READY` and the product status in the catalog can be set to `complete`.

---

## Directory Structure

```
project/
├── agents/                # Agent specifications (pipeline stage definitions)
├── checkpoints/           # Per-product pipeline state (JSON)
├── memory/                # Per-family reusable knowledge (YAML)
│   ├── booking-maps/      # System mapping files
│   ├── style-patterns/    # Style rules and conventions
│   └── terminology/       # Abbreviation and naming rules
├── outputs/               # Pipeline artifacts
│   ├── research/          # Stage 1 output
│   ├── blueprints/        # Stage 2 output
│   ├── drafts/            # Stage 3 output (the actual document)
│   ├── booking/           # Stage 4 output
│   ├── reviews/           # Stage 5 output (QA)
│   ├── style/             # Stage 6 output
│   ├── crossref/          # Stage 7 output
│   └── publish/           # Stage 8 output
├── pipeline-logs/         # Per-product runtime metadata (YAML)
├── products/
│   └── catalog.yaml       # Master product list
├── reports/               # Batch reports, dashboards, retrospectives
└── framework/             # This directory — reusable templates
```

---

## Adapting to a New Domain

To use this framework for a different knowledge base:

1. **Define your catalog.** List all items to be documented in `products/catalog.yaml`.
2. **Define your families.** Group items by shared characteristics (same system, same review criteria, same terminology).
3. **Define your sections.** Replace the 8-section structure with whatever sections are appropriate for your domain.
4. **Bootstrap each family.** Create the 3 memory artifacts, then generate the first product to validate them.
5. **Batch generate.** Process remaining products family by family.
6. **Review and publish.** Run the 3 review gates and the publishing gate for each product.

The pipeline stages, memory layer, checkpoints, and gate system are domain-agnostic. Only the content of the templates and the section structure need to change.
