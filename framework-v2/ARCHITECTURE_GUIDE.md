# Architecture Guide

## Pipeline Architecture

```
┌─────────────┐
│   Catalog    │  Source of truth: IDs, families, status
└──────┬──────┘
       │
       ▼
┌─────────────┐     ┌────────────┐
│  1. Research │────▶│  Memory    │  Per-family: terminology,
└──────┬──────┘     │  Layer     │  operational maps, style
       │            └────────────┘
       ▼                  ▲
┌─────────────┐           │
│  2. Write   │───────────┘  Reads memory to generate content
└──────┬──────┘
       │
       ▼
┌─────────────┐
│  3. Review  │  Three sub-gates: Accuracy, Style, CrossRef
└──────┬──────┘
       │
       ▼
┌─────────────┐
│  4. Publish │  Final gate: all reviews passed?
└──────┬──────┘
       │
       ▼
┌─────────────┐
│ Checkpoint  │  Record completion state
└─────────────┘
```

### Design Decisions

**4 stages, not 8.** The original Desk Bible used 8 stages (splitting write into content/example/reconciliation and review into QA/style/crossref). In practice, the sub-stages always ran together and the separation added overhead without adding value. The v2 framework consolidates: the Write stage produces a single draft, and the Review stage runs all three checks.

**Artifact-based, not prompt-based.** Every stage reads files and writes files. No stage passes content through prompts. This means:
- The pipeline can be interrupted at any point and resumed.
- Every intermediate result is inspectable and auditable.
- No in-memory state is ever lost.

**Memory-first, not generate-first.** Before writing, the pipeline checks the family's memory artifacts. This prevents re-deriving decisions that were already made for earlier entries in the same family.

---

## Directory Structure

```
project/
├── catalog.yaml              # Master entry list
├── memory/                    # Per-family reusable knowledge
│   ├── terminology/           # {FAMILY}.yaml — names, abbreviations, casing
│   ├── operational-maps/      # {FAMILY}.yaml — system/process mappings
│   └── style-conventions/     # {FAMILY}.yaml — formatting, FPs, conventions
├── outputs/                   # Pipeline artifacts
│   ├── research/              # {ID}.yaml — Stage 1
│   ├── drafts/                # {ID}.md — Stage 2 (the actual document page)
│   ├── reviews/               # {ID}_accuracy.yaml, {ID}_style.yaml, {ID}_crossref.yaml — Stage 3
│   └── publish/               # {ID}_pubspec.yaml — Stage 4
├── checkpoints/               # {ID}.json — pipeline state per entry
├── pipeline-logs/             # {slug}.yaml — runtime metadata per entry
└── reports/                   # Batch reports, dashboard, retrospectives
```

### Artifact Lifecycle

```
catalog entry (stub)
    │
    ▼ Stage 1
research/{ID}.yaml ──────────── domain knowledge extracted
    │
    ▼ Stage 2
drafts/{ID}.md ──────────────── structured content generated
    │
    ▼ Stage 3
reviews/{ID}_accuracy.yaml ──── factual/arithmetic verification
reviews/{ID}_style.yaml ─────── formatting/notation check
reviews/{ID}_crossref.yaml ──── internal reference validation
    │
    ▼ Stage 4
publish/{ID}_pubspec.yaml ───── final gate: READY or NOT_READY
    │
    ▼
checkpoints/{ID}.json ──────── all_gates_passed: true
catalog entry → status: complete
```

---

## Stage Details

### Stage 1 — Research

**Input:** Catalog entry + domain expertise + family terminology memory.  
**Output:** `outputs/research/{ID}.yaml`  
**Purpose:** Extract and structure domain knowledge about the entry.

The research artifact captures:
- Definition (plain language)
- Key parameters
- Primary and secondary drivers
- Risk factors or failure modes
- Relationships to other entries in the family
- Complexity assessment

### Stage 2 — Write

**Input:** Research YAML + family memory (all 3 types).  
**Output:** `outputs/drafts/{ID}.md`  
**Purpose:** Generate the structured document page.

The draft follows a standardised section structure defined per-project (see the domain onboarding guide). Every entry in the project uses the same sections in the same order. The family's terminology memory ensures consistent naming. The operational map memory ensures correct system/process references.

### Stage 3 — Review

**Input:** Draft MD + family style-conventions memory + catalog.  
**Output:** Three review files:
- `outputs/reviews/{ID}_accuracy.yaml` — factual and arithmetic verification
- `outputs/reviews/{ID}_style.yaml` — formatting and notation check
- `outputs/reviews/{ID}_crossref.yaml` — internal reference validation

**Purpose:** Validate quality through three independent gates.

Each gate produces a binary PASS/FAIL result. If any gate fails, the draft is fixed and the failed gate is re-run. See the Quality Control Guide for gate protocols.

### Stage 4 — Publish

**Input:** All three review YAMLs.  
**Output:** `outputs/publish/{ID}_pubspec.yaml`  
**Purpose:** Final confirmation that all gates passed and the entry is ready for inclusion in the assembled document.

The pubspec records:
- Draft exists: yes/no
- Accuracy gate: PASS/FAIL
- Style gate: PASS/FAIL
- CrossRef gate: PASS/FAIL
- All sections present: yes/no
- Blocking issues: count (must be 0)
- Gate result: READY / NOT_READY

---

## Data Flow

```
                    ┌─────────────────────────────────────┐
                    │           memory/                    │
                    │  ┌──────────┐ ┌──────┐ ┌─────────┐ │
                    │  │Terminology│ │OpMaps│ │StyleConv│ │
                    │  └─────┬────┘ └──┬───┘ └────┬────┘ │
                    └────────┼─────────┼──────────┼──────┘
                             │         │          │
  catalog ──▶ Research ──────┼────▶ Write ────────┼────▶ Review ──▶ Publish
                 │           │      │    │        │       │  │  │      │
                 ▼           ▼      ▼    ▼        ▼       ▼  ▼  ▼      ▼
              research/   (reads) drafts/ (reads)      reviews/    publish/
              {ID}.yaml           {ID}.md              {ID}_*.yaml {ID}_pubspec
```

---

## Execution Modes

| Mode | Stages | When to Use |
|------|--------|-------------|
| **DRAFT** | 1–2 | Initial content generation |
| **REVIEW** | 3 | After fixing issues from a prior review |
| **PUBLISH** | 4 | After all reviews pass |
| **FULL** | 1–4 | Default for production runs |

In practice, FULL mode is used for every entry once the pipeline is stable. The separate modes exist for debugging and re-runs.

---

## Scaling Patterns

### Batch Processing

Group 3–6 entries per batch, ideally from the same family. This maximises memory reuse and minimises context-switching.

**Batch lifecycle:**
1. Pre-batch tag → safety snapshot.
2. Generate all entries in the batch.
3. Post-batch validation → verify all gates pass.
4. Post-batch commit and tag.
5. Update dashboard and production history.

### Family-Sequential Processing

Process families in order: largest family first (maximises memory reuse ROI), then families that reference other families (resolves forward references).

### Context Continuation

For projects that span multiple sessions: the artifact-based architecture means no state is lost. Each session reads existing files, checks which entries are complete via checkpoints, and resumes from the next incomplete entry.
