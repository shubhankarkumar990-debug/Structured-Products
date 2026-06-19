# Project Bootstrap Guide

How to start a new Knowledge Bible project from scratch using this framework.

---

## Step 1 — Define Your Domain

Before creating any files, answer these questions:

| Question | Your Answer |
|----------|-------------|
| What are you documenting? | (entries: products, processes, regulations, models, etc.) |
| How many entries total? | (determines batch count and timeline) |
| How are entries grouped? | (families: by system, by regulation, by department) |
| What sections does each entry need? | (definition, procedure, risk, controls, etc.) |
| Who is the audience? | (traders, auditors, regulators, new hires) |
| What operational systems are involved? | (determines operational map memory) |

---

## Step 2 — Create the Directory Structure

```bash
mkdir -p \
  memory/terminology/ \
  memory/operational-maps/ \
  memory/style-conventions/ \
  outputs/research/ \
  outputs/drafts/ \
  outputs/reviews/ \
  outputs/publish/ \
  checkpoints/ \
  pipeline-logs/ \
  reports/ \
  release/
```

---

## Step 3 — Create the Catalog

Create `catalog.yaml` with all entries:

```yaml
entries:
  # Family: {FAMILY_A}
  - id: "{ID}"
    name: "{Entry Name}"
    family: "{FAMILY_A}"
    section: "{section number}"
    status: stub

  # Family: {FAMILY_B}
  - id: "{ID}"
    name: "{Entry Name}"
    family: "{FAMILY_B}"
    section: "{section number}"
    status: stub
```

**ID convention:** `{ABBREVIATION}{NNN}` (e.g., `RC001`, `CRED001`, `SOP001`).  
**Status values:** `stub` → `draft` → `review` → `complete`.

---

## Step 4 — Define Your Section Structure

The Desk Bible used 8 sections. Your domain may need more, fewer, or different sections. Examples:

| Domain | Recommended Sections |
|--------|---------------------|
| Structured Products | Definition, Construction, Booking & Systems, Pricing Intuition, Worked Example, Reconciliation, Desk View, Desk Shorthand |
| Model Risk | Model Description, Mathematical Specification, Implementation, Validation Approach, Limitations, Monitoring, Model Risk Rating |
| Credit Risk | Facility Description, Risk Assessment, Exposure Calculation, Mitigation, Monitoring, Regulatory Treatment, Risk Summary |
| SOPs | Purpose, Scope, Responsibilities, Procedure Steps, Exceptions, Escalation, Review History |

Record your chosen sections in the style-conventions memory template.

---

## Step 5 — Plan Your Families

For each family, identify:

1. **Operational mapping.** Which systems/tools handle this family's entries?
2. **Terminology.** What abbreviations and naming conventions does this family use?
3. **Style rules.** Any family-specific formatting rules?

---

## Step 6 — Plan Your Batches

| Batch | Purpose | Size |
|-------|---------|------|
| Batch 0 | Bootstrap — one entry per family | 1 per family (max 6 total) |
| Batch 1–N | Production — same-family batches | 3–6 per batch |
| Final | Last entries to complete the project | Remaining entries |

**Process families in this order:**
1. Largest family first (maximises memory reuse ROI).
2. Families that other families reference (resolves forward references).
3. Smallest families last.

---

## Step 7 — Bootstrap the First Family

### 7a. Create Memory Artifacts

For the first family, create 3 files using the templates in `framework-v2/templates/`:

1. `memory/terminology/{FAMILY}.yaml`
2. `memory/operational-maps/{FAMILY}.yaml`
3. `memory/style-conventions/{FAMILY}.yaml`

### 7b. Generate the Bootstrap Entry

Select the simplest, most representative entry in the family. Run the full pipeline:

1. **Research:** Create `outputs/research/{ID}.yaml`.
2. **Write:** Create `outputs/drafts/{ID}.md` using all 3 memory artifacts.
3. **Review:** Create the 3 review files. Note any corrections or new conventions.
4. **Publish:** Create `outputs/publish/{ID}_pubspec.yaml`. Gate should be READY.
5. **Checkpoint:** Create `checkpoints/{ID}.json`.
6. **Pipeline log:** Create `pipeline-logs/{slug}.yaml`.

### 7c. Post-Bootstrap

- Fix any memory corrections discovered during the bootstrap.
- Note any deferred conventions (add to memory only after validation in a second entry).
- Update catalog status to `complete`.
- Commit: `"Bootstrap {FAMILY}: {ID} complete, 3 memory artifacts validated"`

---

## Step 8 — Generate Remaining Entries

For each subsequent batch:

1. **Pre-batch tag:** `git tag {project}-before-batch-{N}`
2. **Generate entries:** Full pipeline for each entry.
3. **Validate:** All gates pass, no regressions.
4. **Commit and tag:** Descriptive message + `{project}-after-batch-{N}`.
5. **Update reports:** Dashboard + production history.

Repeat for each family until all entries are complete.

---

## Step 9 — Final Validation

Run the 5-point validation (see Release Management Guide):

1. Catalog: all entries `complete`.
2. Checkpoints: all `all_gates_passed: true`.
3. Cross-references: zero broken.
4. Publishing: all READY.
5. Memory: all families have 3 artifacts.

---

## Step 10 — Release and Archive

1. Generate final report.
2. Assemble the document.
3. Create release package.
4. Final commit and tag.
5. Update production history: ARCHIVED / RELEASED / COMPLETE.

---

## Timeline Estimates

Based on the Desk Bible experience (~14,866 tokens per entry, stable across complexity levels):

| Project Size | Entries | Estimated Batches | Estimated Tokens |
|-------------|---------|-------------------|------------------|
| Small | 10–15 | 3–4 | ~150K–225K |
| Medium | 25–40 | 6–9 | ~375K–600K |
| Large | 50–100 | 12–20 | ~750K–1.5M |

Memory reuse improves efficiency by 20–30% from the second batch onward.
