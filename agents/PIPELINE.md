# Structured Products Desk Bible — Agent Pipeline v2

Token-efficient, resumable, artifact-based pipeline. 12 agents. Three
execution modes. Checkpoint-based resumption. Memory-first reuse.

---

## Architecture diagram

```
                         ┌─────────────────┐
                         │  Product Catalog │
                         │ products/catalog │
                         └────────┬────────┘
                                  │
                         ┌────────▼────────┐
                         │  ORCHESTRATOR   │
                         │  (mode router)  │
                         └────────┬────────┘
                                  │
              ┌───────────────────┼───────────────────┐
              │                   │                   │
       ┌──────▼──────┐    ┌──────▼──────┐    ┌──────▼──────┐
       │    DRAFT     │    │   REVIEW    │    │  PUBLISH    │
       │  (stages 1-4)│    │ (stages 5-7)│    │ (stage 8)   │
       └──────┬──────┘    └──────┬──────┘    └──────┬──────┘
              │                   │                   │
    ┌─────────┼─────────┐        │                   │
    │         │         │        │                   │
    ▼         ▼         ▼        ▼                   ▼
 Memory → Research → Architect → Writing ──┐     Publisher
                                           │        │
                              ┌────────────┤        │
                              │            │        │
                       ┌──────▼──┐  ┌──────▼──┐     │
                       │ Content │  │ Example  │     │
                       │ Writer  │  │Generator │     │
                       └─────────┘  └─────────┘     │
                              │                      │
                       ┌──────▼──────┐               │
                       │   Recon     │               │
                       │ Generator   │               │
                       └─────────────┘               │
                              │                      │
                       ┌──────▼──────┐               │
                       │   Booking   │               │
                       │   Mapping   │               │
                       └──────┬──────┘               │
                              │                      │
                       ┌──────▼──────┐               │
                       │  QA (diff)  │               │
                       └──────┬──────┘               │
                              │                      │
                       ┌──────▼──────┐               │
                       │ Style (diff)│               │
                       └──────┬──────┘               │
                              │                      │
                       ┌──────▼──────┐               │
                       │CrossRef(diff│               │
                       └──────┬──────┘               │
                              │                      │
                              └──────────────────────┘
                                         │
                                  ┌──────▼──────┐
                                  │  Master DOCX│
                                  │ (compiled)  │
                                  └─────────────┘

   All stages read/write ◄──── memory/ ────► (canonical store)
   All stages read/write ◄──── outputs/ ───► (artifact files)
   All stages read/write ◄──── checkpoints/ ► (resumption state)
```

---

## Agent roster

| Agent | Stage | Role | Input | Output |
|---|---|---|---|---|
| sp-orchestrator | — | Mode routing, gate enforcement, checkpoint mgmt | Commands, catalog | Checkpoints, coordination |
| sp-memory-agent | — | Store/retrieve approved artifacts | Agent requests | Memory YAML files |
| sp-research-agent | 1 | Extract product knowledge | Source material, memory | `outputs/research/{id}.yaml` |
| sp-product-architect | 2 | Blueprint from research | Research YAML, memory | `outputs/blueprints/{id}.yaml` |
| sp-content-writer | 3a | Definition, Construction, Pricing, Desk view, Shorthand | Blueprint, memory | `outputs/drafts/{id}_content.md` |
| sp-example-generator | 3b | Worked example (USD 10M) | Blueprint, memory | `outputs/examples/{id}.md` |
| sp-reconciliation-generator | 3c | Booking & systems, Reconciliation specifics | Blueprint, memory | `outputs/reconciliation/{id}.md` |
| sp-murex-mapping | 4 | Booking specification (NEMO+Sophis or Murex 4-leg) | Draft, blueprint, memory | `outputs/booking/{id}.yaml` |
| sp-qa-agent | 5 | Diff review: accuracy and completeness | Artifact refs only | `outputs/reviews/{id}_qa.yaml` |
| sp-style-agent | 6 | Diff review: style violations | Artifact ref + style memory | `outputs/style/{id}_style.yaml` |
| sp-crossref-agent | 7 | Diff review: reference validation | Artifact ref + catalog | `outputs/crossref/{id}_crossref.yaml` |
| sp-publisher | 8 | Pubspec + DOCX merge | Artifact refs + catalog | `outputs/publish/{id}_pubspec.yaml` + DOCX |

---

## Execution modes

| Mode | Stages | Trigger |
|---|---|---|
| DRAFT | 1–4 (Memory, Research, Architecture, Writing, Booking) | Default. `build product PHX001` |
| REVIEW | 5–7 (QA, Style, CrossRef) | `build product PHX001 mode=review` |
| PUBLISH | 8 (Publisher + DOCX merge) | `build product PHX001 mode=publish` |
| FULL | 1–8 | `build product PHX001 mode=full` |

Never run all stages unless explicitly requested.

---

## Folder structure

```
Structured Products/
├── agents/                          # Agent specifications
│   ├── sp-orchestrator.md
│   ├── sp-memory-agent.md
│   ├── sp-research-agent.md
│   ├── sp-product-architect.md
│   ├── sp-content-writer.md         # Replaces sp-technical-writer
│   ├── sp-example-generator.md      # New (split from writer)
│   ├── sp-reconciliation-generator.md # New (split from writer)
│   ├── sp-murex-mapping.md
│   ├── sp-qa-agent.md               # Now a diff reviewer
│   ├── sp-style-agent.md            # Now a diff reviewer
│   ├── sp-crossref-agent.md         # Now a diff reviewer
│   ├── sp-publisher.md              # Only agent that edits DOCX
│   ├── PIPELINE.md                  # This file
│   └── install.sh
│
├── products/
│   └── catalog.yaml                 # Product registry with IDs/status
│
├── outputs/                         # Stage artifacts (file-based)
│   ├── research/                    # {product_id}.yaml
│   ├── blueprints/                  # {product_id}.yaml
│   ├── drafts/                      # {product_id}.md (merged), {id}_content.md
│   ├── examples/                    # {product_id}.md
│   ├── reconciliation/              # {product_id}.md
│   ├── booking/                     # {product_id}.yaml
│   ├── reviews/                     # {product_id}_qa.yaml
│   ├── style/                       # {product_id}_style.yaml
│   ├── crossref/                    # {product_id}_crossref.yaml
│   └── publish/                     # {product_id}_pubspec.yaml
│
├── memory/                          # Canonical knowledge store
│   ├── definitions/                 # Approved product definitions
│   ├── components/                  # Reusable construction components
│   ├── terminology/                 # Approved terms per family
│   ├── examples/                    # Approved worked examples
│   ├── booking-maps/                # System mappings and field specs
│   ├── reconciliation/              # Recon logic and failure modes
│   └── style-patterns/              # Style rules and known false positives
│
├── checkpoints/                     # {product_id}.json — resumption state
│
├── pipeline-logs/                   # Legacy logs (v1 format, retained)
│
├── Structured_Products_Desk_Bible_COMPLETE.docx  # Compiled output
└── structured-products-desk-bible-author.md      # Author guide
```

---

## Artifact schemas

### Research artifact (`outputs/research/{id}.yaml`)

Top-level keys: `research.product_id`, `research.chapter`,
`research.product_family`, `research.extracted_at`, `research.memory_used`,
then sections: `definition`, `construction`, `systems`, `pricing`,
`worked_example`, `reconciliation`, `desk_view`, `desk_shorthand`,
`open_questions`.

### Blueprint artifact (`outputs/blueprints/{id}.yaml`)

Top-level keys: `blueprint.product_id`, `blueprint.product_name`,
`blueprint.product_family`, `blueprint.generated_at`, `blueprint.source`,
`blueprint.memory_used`, then `blueprint.sections` with all 8 sections
as structured YAML, plus `blueprint.validation`.

### Draft artifact (`outputs/drafts/{id}.md`)

Merged Markdown with H3 product name and all 8 H4 subsections in order.
Assembled from three sub-artifacts by the orchestrator.

### Booking artifact (`outputs/booking/{id}.yaml`)

Top-level keys: `booking_spec.product_id`, `booking_spec.spec_type`,
then system-specific fields, `reconciliation_checks`, `failure_modes`,
`validation`.

### Review artifacts (`outputs/reviews/`, `outputs/style/`, `outputs/crossref/`)

YAML with `summary`, `issues`/`violations`/`refs`, `gate` (PASS/FAIL).

### Pubspec artifact (`outputs/publish/{id}_pubspec.yaml`)

YAML with `insertion`, `heading_hierarchy`, `toc_entry`, `numbering`,
`page_structure`, `appendix_updates`, `checklist`, `gate`.

---

## Checkpoint schema (`checkpoints/{id}.json`)

```json
{
  "product_id": "",
  "product_name": "",
  "family": "",
  "updated_at": "",
  "mode": "DRAFT | REVIEW | PUBLISH | FULL",
  "stages": {
    "memory_lookup":   { "status": "", "at": "" },
    "research":        { "status": "", "at": "", "artifact": "" },
    "architecture":    { "status": "", "at": "", "artifact": "" },
    "content":         { "status": "", "at": "", "artifact": "" },
    "example":         { "status": "", "at": "", "artifact": "" },
    "reconciliation":  { "status": "", "at": "", "artifact": "" },
    "draft_merged":    { "status": "", "at": "", "artifact": "" },
    "booking":         { "status": "", "at": "", "artifact": "" },
    "qa":              { "status": "", "at": "", "artifact": "" },
    "style":           { "status": "", "at": "", "artifact": "" },
    "crossref":        { "status": "", "at": "", "artifact": "" },
    "publish":         { "status": "", "at": "", "artifact": "" },
    "docx_merge":      { "status": "", "at": "" }
  },
  "open_issues": []
}
```

Status values: `pending` | `in_progress` | `complete` | `rejected`

---

## Sample commands

```bash
# Draft a single product
build product FCN001

# Review a drafted product
build product FCN001 mode=review

# Publish a reviewed product
build product FCN001 mode=publish

# Full pipeline for one product
build product FCN001 mode=full

# Draft all incomplete products
build desk bible

# Full pipeline for entire desk bible
build desk bible mode=full

# Incremental update
refresh PHX001

# Resume a stalled pipeline
build product FCN001
# (automatically resumes from last checkpoint)
```

---

## Migration plan from v1

### What changed

| v1 | v2 | Change |
|---|---|---|
| sp-technical-writer (monolithic) | sp-content-writer + sp-example-generator + sp-reconciliation-generator | Split into 3 specialists |
| Content passed in prompts | Agents read/write artifact files | File references only |
| No memory layer | sp-memory-agent + memory/ directory | Canonical store, reuse before regenerate |
| No execution modes | DRAFT / REVIEW / PUBLISH | Stage grouping, default = DRAFT only |
| pipeline-logs/*.yaml | checkpoints/*.json | JSON checkpoint with artifact paths |
| Review agents read full doc | Diff reviewers read current product only | Scope reduction |
| DOCX as source | DOCX as compiled output | Only publisher edits Word |
| No product catalog | products/catalog.yaml | Automatic iteration |
| No incremental updates | refresh command | Partial re-run |
| 9 agents | 12 agents | +memory, +content-writer, +example-gen, +recon-gen, −technical-writer |

### Migration steps

1. **Directory structure**: Created — `outputs/`, `memory/`, `checkpoints/`, `products/`.
2. **Product catalog**: Created — `products/catalog.yaml` with all 28 products.
3. **Memory seed**: Created — terminology, system mapping, and style patterns for ELN family.
4. **Agent files**: All 12 agents updated or created.
5. **Checkpoint migration**: PHX001 checkpoint created from legacy pipeline log.
6. **Legacy logs**: Retained in `pipeline-logs/` for reference. Not used by v2.
7. **sp-technical-writer.md**: Retained for reference. Superseded by the three new writer agents.

### To complete migration for existing products

For each product with `status: existing` in the catalog:

1. Extract its content from the master DOCX.
2. Run through the pipeline in DRAFT mode to produce artifacts.
3. Run REVIEW mode to validate.
4. Update catalog status to `complete`.

This can be done incrementally — one product at a time.

---

## System mapping (enforced across all agents)

| Product family | Book of record | Risk/P&L | Legal doc | Murex? |
|---|---|---|---|---|
| ELN | NEMO | Sophis | Termsheet | No |
| CLN | NEMO | Sophis | Termsheet | No |
| Structured Deposit | NEMO | Sophis | Termsheet | No |
| STEG | Murex (4-leg) | Sophis | Termsheet | Yes |
| SRT | Murex (4-leg) | Sophis | Termsheet | Yes |
| Swap | Murex | Sophis | ISDA | Yes |

---

## Gate conditions summary

| Gate | Condition |
|---|---|
| Research → Architecture | YAML complete, no null core fields |
| Architecture → Writing | All 8 sections, system mapping correct |
| Writing → Booking | All 8 subsections in merged draft |
| Booking → QA | Spec type correct, fields named, FTP documented |
| QA → Style | Zero BLOCKER issues |
| Style → CrossRef | Zero MUST_FIX violations |
| CrossRef → Publish | Zero broken references |
| Publish → DOCX merge | Publication checklist passed |
