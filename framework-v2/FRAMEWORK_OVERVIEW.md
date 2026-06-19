# Knowledge Bible Framework — Overview

**Version:** 2.0  
**Origin:** Extracted from the Structured Products Desk Bible (28 products, 5 families, 280+ artifacts, zero defects)  
**Purpose:** A reusable system for generating high-quality, structured documentation in any knowledge domain.

---

## What This Framework Does

The Knowledge Bible Framework converts domain knowledge into a structured, validated, internally-consistent reference document. It does this through:

1. **A 4-stage pipeline** (Research → Write → Review → Publish) that transforms a catalog entry into a complete, quality-controlled document page.
2. **A per-family memory layer** that stores reusable knowledge (terminology, operational mappings, style conventions) so that each document page in a family benefits from decisions made during the first page.
3. **Binary quality gates** (Accuracy, Style, Cross-Reference) that enforce consistency without subjective judgment.
4. **Artifact-based state management** where every intermediate result is a file on disk, enabling interruption, resumption, auditing, and debugging.

## What This Framework Is NOT

- **Not a content management system.** It generates documentation; it does not serve or version it.
- **Not a template engine.** Templates provide structure, but content is generated from domain knowledge, not filled in from forms.
- **Not domain-specific.** The framework was proven on structured finance but is designed for any domain where standardised documentation must be produced at scale.

---

## Core Concepts

### Entries and Families

An **entry** is a single item to be documented (a product, a process, a regulation, a model). A **family** is a group of entries that share operational context — same systems, same terminology, same style conventions.

### The Catalog

The **catalog** (`catalog.yaml`) is the master list of all entries. It is the single source of truth for what exists, its family, its status, and its position in the final document.

### The Pipeline

The **pipeline** has 4 stages, grouped into 3 modes:

| Mode | Stage | Purpose | Output |
|------|-------|---------|--------|
| DRAFT | 1. Research | Gather domain knowledge | `outputs/research/{ID}.yaml` |
| DRAFT | 2. Write | Generate structured content | `outputs/drafts/{ID}.md` |
| REVIEW | 3. Review | Validate accuracy, style, references | `outputs/reviews/{ID}_*.yaml` |
| PUBLISH | 4. Publish | Final gate check | `outputs/publish/{ID}_pubspec.yaml` |

### Memory

**Memory** is a set of per-family YAML files that store reusable knowledge. Three types, proven necessary and sufficient:

| Type | What It Stores | Why It Matters |
|------|---------------|----------------|
| **Terminology** | Names, abbreviations, casing rules | Consistency across entries |
| **Operational Map** | System/process/tool mappings | Prevents the most dangerous error class |
| **Style Conventions** | Formatting rules, known false positives, accepted conventions | Eliminates false violations |

### Quality Gates

Three gates, each with a binary PASS/FAIL result:

| Gate | Checks | Pass Criteria |
|------|--------|---------------|
| **Accuracy** | Factual correctness, arithmetic, completeness | Zero BLOCKERs |
| **Style** | Formatting, notation, terminology | Zero MUST_FIX |
| **Cross-Reference** | Internal links, catalog consistency | Zero broken references |

All three must pass before an entry can be published.

### Checkpoints

A **checkpoint** is a JSON file per entry that records which stages are complete, which gates passed, and whether retries were needed. Checkpoints enable resumption and auditing.

---

## Why This Framework Works

The framework's effectiveness was validated across 28 products in the Structured Products Desk Bible:

| Metric | Result |
|--------|--------|
| Entries completed | 28/28 (100%) |
| QA BLOCKERs | 0 |
| Style MUST_FIX | 0 |
| Broken cross-references | 0 |
| Publishing failures | 0 |
| Retries (Batch 1+) | 0 |
| Memory reuse ratio | 4.6:1 |
| Per-entry cost | ~14,866 tokens (stable ±0%) |

The three factors that drove this result:

1. **Memory reuse** eliminated repetitive decisions and prevented the most dangerous error class (wrong system mapping).
2. **Arithmetic verification protocol** eliminated false-positive BLOCKERs in the accuracy gate.
3. **Convention validation protocol** (observe once, validate twice, then enshrine) prevented false conventions from polluting the memory layer.

---

## Framework Components

| Guide | Purpose | Read When... |
|-------|---------|-------------|
| [ARCHITECTURE_GUIDE.md](ARCHITECTURE_GUIDE.md) | Pipeline, artifacts, data flow | You want to understand the system |
| [MEMORY_DESIGN_GUIDE.md](MEMORY_DESIGN_GUIDE.md) | Memory types, lifecycle, bootstrap | You're creating a new family |
| [GOVERNANCE_GUIDE.md](GOVERNANCE_GUIDE.md) | Git, commits, tags, branches | You're managing the project |
| [QUALITY_CONTROL_GUIDE.md](QUALITY_CONTROL_GUIDE.md) | Gates, protocols, checklists | You're reviewing entries |
| [RELEASE_MANAGEMENT_GUIDE.md](RELEASE_MANAGEMENT_GUIDE.md) | Versioning, packaging, distribution | You're preparing a release |
| [PROJECT_BOOTSTRAP_GUIDE.md](PROJECT_BOOTSTRAP_GUIDE.md) | Setup, first family, first entry | You're starting a new project |
| [NEW_DOMAIN_ONBOARDING_GUIDE.md](NEW_DOMAIN_ONBOARDING_GUIDE.md) | Adaptation examples for 7 domains | You're applying the framework to a new domain |
