# Bootstrap Guide

How to start a new knowledge-base project using this framework, from empty directory to released document.

---

## 1. How to Start a New Project

### Step 1 — Create the directory structure

```bash
mkdir -p \
  agents/ \
  checkpoints/ \
  memory/terminology/ \
  memory/booking-maps/ \
  memory/style-patterns/ \
  outputs/research/ \
  outputs/blueprints/ \
  outputs/drafts/ \
  outputs/booking/ \
  outputs/reviews/ \
  outputs/style/ \
  outputs/crossref/ \
  outputs/publish/ \
  pipeline-logs/ \
  products/ \
  reports/ \
  release/
```

### Step 2 — Initialise git

```bash
git init
git add .
git commit -m "Initial project structure"
```

### Step 3 — Create the product catalog

Create `products/catalog.yaml` with all products you intend to document:

```yaml
products:
  # Group by family and section
  - id: PROD001
    name: "Product Name"
    family: FAMILY_A
    section: "1.1"
    status: stub
```

Status values: `stub` → `draft` → `review` → `complete`.

### Step 4 — Plan your families

List all families you will need. For each family, identify:

- **System mapping.** Which operational system(s) handle this family's products?
- **Terminology.** What abbreviations and naming conventions does this family use?
- **Style rules.** Are there family-specific formatting rules or conventions?

### Step 5 — Plan your batches

Group products into batches of 3–6 products each. Recommended batch strategy:

1. **Batch 0 (baseline):** One product per family. These are the bootstrap products that create and validate the memory artifacts.
2. **Batch 1–N:** Remaining products, grouped by family. Process one family at a time to maximise memory reuse.

### Step 6 — Adapt the section structure

The default template has 8 sections (Definition through Desk Shorthand). If your domain needs different sections:

1. Edit `framework/templates/draft_artifact.md` with your section headings.
2. Update `framework/templates/style_pattern_memory.yaml` to list your canonical H4 names.
3. Update `framework/templates/blueprint_artifact.yaml` to match.
4. Update `framework/templates/review_artifact.yaml` to check for your sections.

---

## 2. How to Create a New Family

A family is a group of products that share a system mapping, terminology, and style rules. Each family needs exactly 3 memory artifacts before any product can be generated.

### Step 1 — Create terminology memory

Copy `framework/templates/terminology_memory.yaml` to `memory/terminology/{FAMILY}.yaml`.

Fill in:
- All product names and abbreviations for this family.
- All system names with correct casing.
- All domain abbreviations used in this family.

### Step 2 — Create booking-map memory

Copy `framework/templates/booking_map_memory.yaml` to `memory/booking-maps/{FAMILY}_system_mapping.yaml`.

Fill in:
- System type (e.g., `nemo_sophis` or `murex_four_leg`).
- Book of record system and what it carries.
- Risk/P&L system and what it carries.
- Legal document name.

**This is the most important memory artifact.** A wrong system mapping propagates to every product in the family. Double-check with the desk before proceeding.

### Step 3 — Create style-pattern memory

Copy `framework/templates/style_pattern_memory.yaml` to `memory/style-patterns/{FAMILY}.yaml`.

Fill in:
- Canonical H4 section names (use the defaults unless your domain requires different sections).
- Known false positives (start empty — you'll add these during the bootstrap product).
- Approved patterns (start with the defaults: USD prefix, desk shorthand format).
- Leave `accepted_conventions` empty — these are added after validation.

### Step 4 — Commit

```bash
git add memory/
git commit -m "Bootstrap {FAMILY} family: 3 memory artifacts"
```

---

## 3. How to Bootstrap Memory

Memory bootstrapping happens during the first product generated in a new family. The bootstrap product serves two purposes:

1. **Validate the 3 memory artifacts.** Confirm that terminology, system mapping, and style rules are correct by using them in a real product.
2. **Discover family-specific conventions.** Note any patterns that the QA or style review flags as unusual. These are candidates for future `accepted_conventions`.

### Bootstrap Protocol

1. **Generate the bootstrap product** through the full pipeline (all 8 stages).
2. **During QA review (stage 5):** Note any MAJOR advisories that are inherent to the product structure (e.g., a decomposition format that sums differently than other families). Do NOT add these to the style-patterns file yet.
3. **During style review (stage 6):** Note any false positives that the reviewer flags. Add genuine FPs to `known_false_positives` in the style-patterns file.
4. **After the bootstrap product passes all gates:** Review the noted conventions. Mark them as "deferred for validation" in the pipeline log.
5. **After the second product in the family passes all gates:** If the deferred conventions recur and are confirmed as inherent to the family, add them to `accepted_conventions` in the style-patterns file.

### Why Not Add Conventions Immediately?

A convention observed in one product might be an error. A convention observed in two products is a pattern. The validation protocol prevents false conventions from being enshrined in the memory layer.

### Post-Bootstrap Checklist

- [ ] All 3 memory artifacts are correct (no corrections needed during generation).
- [ ] Bootstrap product has all 10 artifacts and status `complete`.
- [ ] Known false positives added to style-patterns.
- [ ] Deferred conventions documented in the pipeline log.

---

## 4. How to Add Products

After the family is bootstrapped, adding products follows a repeatable process.

### Per-Product Process

1. **Verify the product is in the catalog** with status `stub`.

2. **Run DRAFT mode (stages 1–4):**
   - Stage 1: Create `outputs/research/{ID}.yaml` using the family's terminology memory.
   - Stage 2: Create `outputs/blueprints/{ID}.yaml` from the research output.
   - Stage 3: Create `outputs/drafts/{ID}.md` from the blueprint, following the section structure.
   - Stage 4: Create `outputs/booking/{ID}.yaml` from the blueprint, using the family's booking-map memory.
   - Update catalog status to `draft`.

3. **Run REVIEW mode (stages 5–7):**
   - Stage 5: Create `outputs/reviews/{ID}_qa.yaml`. Computationally verify all arithmetic.
   - Stage 6: Create `outputs/style/{ID}_style.yaml`. Apply the family's known FPs and conventions.
   - Stage 7: Create `outputs/crossref/{ID}_crossref.yaml`. Check all product references.
   - If any gate fails, fix the draft and re-run the failed stage.
   - Update catalog status to `review`.

4. **Run PUBLISH mode (stage 8):**
   - Stage 8: Create `outputs/publish/{ID}_pubspec.yaml`. Confirm all gates passed.
   - Update catalog status to `complete`.

5. **Create operational artifacts:**
   - `checkpoints/{ID}.json` — Pipeline state.
   - `pipeline-logs/{slug}.yaml` — Runtime metadata.

6. **Commit.**

### Quality Gates Summary

| Gate | Stage | Pass Criteria | Fail Action |
|------|-------|---------------|-------------|
| QA | 5 | Zero BLOCKERs | Fix arithmetic, re-run stage 5 |
| Style | 6 | Zero MUST_FIX | Fix formatting, re-run stage 6 |
| CrossRef | 7 | Zero broken refs | Fix references, re-run stage 7 |
| Publish | 8 | All above PASS | Fix upstream, re-run stage 8 |

---

## 5. How to Run Batch Processing

Batches group multiple products for efficient processing. The recommended approach:

### Batch Planning

- **Size:** 3–6 products per batch. Larger batches are efficient but harder to debug if something fails.
- **Composition:** Same-family products in a batch to maximise memory reuse.
- **Order:** Process families in this order: (1) families with the most products, (2) families that depend on other families' products (to resolve forward references).

### Batch Execution

1. **Pre-batch tag:**
   ```bash
   git tag desk-bible-before-batch-{N}
   ```

2. **Generate all products in the batch** through the full pipeline. Track progress in a batch report.

3. **Batch validation:**
   - All products have status `complete`.
   - All gates passed.
   - No regressions in previously completed products.

4. **Post-batch commit and tag:**
   ```bash
   git add .
   git commit -m "Batch {N}: {count} products ({IDs}) — {milestone}"
   git tag desk-bible-after-batch-{N}
   ```

5. **Update reports:**
   - `reports/desk_bible_progress.md` — Update counts and percentages.
   - `reports/production_history.log` — Add batch entry with quality metrics.

### Batch Report Template

Create `reports/batch_{N}_completion_report.md` with:

- Products generated (IDs and names).
- Quality metrics (BLOCKERs, MAJORs, MUST_FIX, broken refs).
- Memory artifacts created or reused.
- Issues encountered and resolved.
- Cumulative progress (X/Y complete, Z%).

---

## 6. How to Perform Project Closeout

When all products are complete:

### Step 1 — Final validation

Run the 5-point validation:

1. **Catalog:** Every product has status `complete`. No `stub`, `existing`, `draft`, or `review` entries.
2. **Checkpoints:** Every product has a checkpoint with `all_gates_passed: true`.
3. **Cross-references:** Zero broken references across all crossref files.
4. **Publishing:** Every product has a pubspec with gate `READY`.
5. **Memory:** Every family with products has all 3 memory artifacts.

### Step 2 — Final report

Generate `reports/Desk_Bible_Final_Report.md` covering:

- Completion counts by family.
- Quality metrics (cumulative across all batches).
- Operational metrics (runtime, tokens, commits).
- Memory metrics (created, reused, bootstraps).
- Lessons learned.

### Step 3 — Assemble the final document

Concatenate all drafts in catalog order into a single document. See the `release/` directory for the assembly script used in v1.

### Step 4 — Release package

Create `release/desk-bible-v{N}/` containing:

- Assembled document.
- Catalog.
- Final report.
- Dashboard.
- Production history.
- Maintenance guide.
- All memory artifacts.
- All checkpoints.
- All output artifacts.
- Release notes.

### Step 5 — Final commit and tag

```bash
git add .
git commit -m "Desk Bible complete: {X} of {X} products"
git tag desk-bible-complete-v{N}
```

### Step 6 — Archive

Update the production history log with the final entry. Mark the project as ARCHIVED / RELEASED / COMPLETE.
