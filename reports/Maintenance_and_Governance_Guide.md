# Desk Bible — Maintenance and Governance Guide

**Version:** 1.0  
**Created:** 2026-06-19  
**Baseline tag:** `desk-bible-complete-v1`  
**Audience:** Any analyst inheriting this project with no prior context.

---

## Table of Contents

1. [Project Overview](#1-project-overview)
2. [How to Add a New Product](#2-how-to-add-a-new-product)
3. [How to Update an Existing Product](#3-how-to-update-an-existing-product)
4. [How to Create a New Product Family](#4-how-to-create-a-new-product-family)
5. [How to Update Memory Artifacts](#5-how-to-update-memory-artifacts)
6. [How to Perform Annual Reviews](#6-how-to-perform-annual-reviews)
7. [How to Validate Cross-References](#7-how-to-validate-cross-references)
8. [How to Regenerate the Final Desk Bible](#8-how-to-regenerate-the-final-desk-bible)
9. [Git Workflow for Future Changes](#9-git-workflow-for-future-changes)
10. [Release Management Process](#10-release-management-process)
11. [Quality-Control Checklist](#11-quality-control-checklist)

---

## 1. Project Overview

### What This Project Is

The Structured Products Desk Bible is a reference document covering 28 structured products across 5 families. Each product has a standardised page with 8 sections (Definition, Construction, Booking & Systems, Pricing Intuition, Worked Example, Reconciliation, Desk View, Desk Shorthand). The bible was generated using an 8-stage automated pipeline backed by per-family memory artifacts.

### Directory Structure

```
Structured Products/
├── agents/                    # Pipeline agent specifications (read-only reference)
│   ├── PIPELINE.md            # Architecture overview and stage definitions
│   ├── sp-orchestrator.md     # Orchestrator agent spec
│   ├── sp-research-agent.md   # Stage 1: Research
│   ├── sp-product-architect.md # Stage 2: Architecture / Blueprint
│   ├── sp-content-writer.md   # Stage 3: Writing (content)
│   ├── sp-example-generator.md # Stage 3: Writing (worked example)
│   ├── sp-reconciliation-generator.md # Stage 3: Writing (recon)
│   ├── sp-murex-mapping.md    # Stage 4: Booking / system mapping
│   ├── sp-qa-agent.md         # Stage 5: QA review
│   ├── sp-style-agent.md      # Stage 6: Style review
│   ├── sp-crossref-agent.md   # Stage 7: Cross-reference validation
│   ├── sp-publisher.md        # Stage 8: Publishing gate
│   └── stage-briefings/       # Per-stage briefing documents
├── checkpoints/               # One JSON per product — tracks pipeline completion
├── memory/                    # Per-family reusable knowledge
│   ├── booking-maps/          # System mapping (NEMO/Sophis vs Murex)
│   ├── style-patterns/        # Style rules, known false positives, accepted conventions
│   └── terminology/           # Abbreviations, casing rules, product names
├── outputs/                   # Pipeline artifacts (10 per product)
│   ├── research/              # Stage 1 output (YAML)
│   ├── blueprints/            # Stage 2 output (YAML)
│   ├── drafts/                # Stage 3 output (Markdown — the actual product page)
│   ├── booking/               # Stage 4 output (YAML)
│   ├── reviews/               # Stage 5 output (QA review YAML)
│   ├── style/                 # Stage 6 output (Style review YAML)
│   ├── crossref/              # Stage 7 output (Cross-reference YAML)
│   └── publish/               # Stage 8 output (Publishing gate YAML)
├── pipeline-logs/             # One YAML per product — runtime metadata
├── products/
│   └── catalog.yaml           # Master product list — source of truth for IDs and status
├── reports/                   # Batch reports, dashboard, final report, this guide
└── schemas/                   # YAML schemas (reference)
```

### Product Families and System Mappings

| Family | System Framework | Book of Record | Risk / P&L | Products |
|--------|-----------------|----------------|------------|----------|
| **ELN** (Equity-Linked Notes) | `nemo_sophis` | NEMO | Sophis | 13 |
| **SRT** (Structured Rate Trades) | `murex_four_leg` | Murex | Murex | 5 |
| **CLN** (Credit-Linked Notes) | `nemo_sophis` | NEMO | Sophis | 5 |
| **STEG** (Steepener Notes) | `murex_four_leg` | Murex | Murex | 4 |
| **Swap** | `murex_four_leg` | Murex | Murex | 1 |

This mapping is the single most critical fact in the bible. Getting the system wrong is the highest-severity error possible.

### The 8 Pipeline Stages

| Stage | Mode | Agent | Input | Output |
|-------|------|-------|-------|--------|
| 1. Research | DRAFT | `sp-research-agent` | Catalog entry | `outputs/research/{ID}.yaml` |
| 2. Architecture | DRAFT | `sp-product-architect` | Research YAML | `outputs/blueprints/{ID}.yaml` |
| 3. Writing | DRAFT | `sp-content-writer` + `sp-example-generator` + `sp-reconciliation-generator` | Blueprint YAML + memory | `outputs/drafts/{ID}.md` |
| 4. Booking | DRAFT | `sp-murex-mapping` | Blueprint YAML + booking-map memory | `outputs/booking/{ID}.yaml` |
| 5. QA | REVIEW | `sp-qa-agent` | Draft MD | `outputs/reviews/{ID}_qa.yaml` |
| 6. Style | REVIEW | `sp-style-agent` | Draft MD + style-pattern memory | `outputs/style/{ID}_style.yaml` |
| 7. CrossRef | REVIEW | `sp-crossref-agent` | Draft MD + catalog | `outputs/crossref/{ID}_crossref.yaml` |
| 8. Publish | PUBLISH | `sp-publisher` | All review YAMLs | `outputs/publish/{ID}_pubspec.yaml` |

Execution modes group stages: **DRAFT** runs stages 1–4, **REVIEW** runs stages 5–7, **PUBLISH** runs stage 8, **FULL** runs all 8.

### The 10 Artifacts Per Product

Every completed product must have exactly these files:

1. `outputs/research/{ID}.yaml`
2. `outputs/blueprints/{ID}.yaml`
3. `outputs/drafts/{ID}.md`
4. `outputs/booking/{ID}.yaml`
5. `outputs/reviews/{ID}_qa.yaml`
6. `outputs/style/{ID}_style.yaml`
7. `outputs/crossref/{ID}_crossref.yaml`
8. `outputs/publish/{ID}_pubspec.yaml`
9. `checkpoints/{ID}.json`
10. `pipeline-logs/{product-name-slug}.yaml`

### The 8 Draft Sections

Every product page (`outputs/drafts/{ID}.md`) follows this structure:

1. **Definition** — What the product is, in plain language.
2. **Construction** — How the product is assembled, step by step.
3. **Booking & Systems** — Which system books it (NEMO/Sophis or Murex), critical fields, failure modes.
4. **Pricing Intuition** — What drives the price, without formulas where possible.
5. **Worked Example** — Concrete USD 10M example with full arithmetic decomposition and scenarios.
6. **Reconciliation** — What to check between systems, what breaks if they disagree.
7. **Desk View** — How the trader thinks about the product day-to-day.
8. **Desk Shorthand** — One italicised phrase, 8 words or fewer.

---

## 2. How to Add a New Product

### Prerequisites

- The product belongs to an existing family (ELN, SRT, CLN, STEG, Swap) or you have already created the new family (see Section 4).
- You know the product's system mapping (NEMO/Sophis or Murex).
- You have the family's 3 memory artifacts in place.

### Step-by-Step

**Step 1 — Assign a product ID.**

Use the pattern `{ABBREVIATION}001` (or increment the number if the abbreviation already exists). Examples: `BARR001` for a Barrier product, `SNOW002` for a second Snowball variant.

**Step 2 — Add the product to the catalog.**

Edit `products/catalog.yaml`. Add an entry under the correct family section:

```yaml
- id: BARR001
  name: "Barrier Reverse Convertible"
  family: ELN
  section: "3.1"
  status: stub
```

Set status to `stub` initially.

**Step 3 — Run the DRAFT pipeline (stages 1–4).**

Generate the following artifacts in order, using the corresponding agent specs in `agents/` as reference for format and content expectations:

1. `outputs/research/BARR001.yaml` — Product research. Consult `memory/terminology/{FAMILY}.yaml` for abbreviation conventions.
2. `outputs/blueprints/BARR001.yaml` — Section-by-section blueprint. Plan all 8 sections.
3. `outputs/drafts/BARR001.md` — Full 8-section draft. Must follow the heading structure in the family's style-pattern file.
4. `outputs/booking/BARR001.yaml` — System mapping. Consult `memory/booking-maps/{FAMILY}_system_mapping.yaml` for the correct system framework.

Update catalog status to `draft`.

**Step 4 — Run the REVIEW pipeline (stages 5–7).**

5. `outputs/reviews/BARR001_qa.yaml` — QA review using protocol v2.1. Computationally verify all arithmetic. Apply ±0.2% rounding tolerance. Flag BLOCKERs only for verified arithmetic errors.
6. `outputs/style/BARR001_style.yaml` — Style review. Apply the family's known false positives and accepted conventions from `memory/style-patterns/{FAMILY}.yaml`.
7. `outputs/crossref/BARR001_crossref.yaml` — Cross-reference validation. Check all product mentions against the catalog. Flag broken references.

If QA or Style raises BLOCKERs or MUST_FIX items, fix the draft and re-run the review. Update catalog status to `review`.

**Step 5 — Run the PUBLISH pipeline (stage 8).**

8. `outputs/publish/BARR001_pubspec.yaml` — Publishing gate. Verify all prior gates passed, all 8 sections present, zero blocking issues. Gate result should be `READY`.

Update catalog status to `complete`.

**Step 6 — Create checkpoint and pipeline log.**

9. `checkpoints/BARR001.json` — Record all 8 stage statuses, gate results, and retry count.
10. `pipeline-logs/barrier-reverse-convertible.yaml` — Record batch, timing, memory usage, and gate results.

**Step 7 — Commit and tag.**

```bash
git add outputs/ checkpoints/ pipeline-logs/ products/catalog.yaml
git commit -m "Add BARR001 (Barrier Reverse Convertible) — ELN family"
git tag desk-bible-v1.1  # increment the version
```

### Validation

After adding the product, verify:

- [ ] All 10 artifacts exist on disk.
- [ ] Catalog status is `complete`.
- [ ] Checkpoint shows `all_gates_passed: true`.
- [ ] QA gate: PASS (zero BLOCKERs).
- [ ] Style gate: PASS (zero MUST_FIX).
- [ ] CrossRef gate: PASS (zero broken references).
- [ ] Publish gate: READY.
- [ ] No other product's crossref is now broken (if the new product was a forward-ref target).

---

## 3. How to Update an Existing Product

### When to Update

- A system migration changes the booking platform (e.g., NEMO → Murex).
- A pricing convention changes (e.g., new benchmark rate replaces SOFR).
- An arithmetic error is found in the worked example.
- A style convention changes across the desk.
- A new cross-reference needs to be added.

### Step-by-Step

**Step 1 — Edit the draft.**

Modify `outputs/drafts/{ID}.md` directly. Make the change.

**Step 2 — Re-run affected review stages.**

- If arithmetic changed → re-run QA (stage 5). Write the new review to `outputs/reviews/{ID}_qa.yaml` (or `_qa_v2.yaml` if you want to preserve the original).
- If text/formatting changed → re-run Style (stage 6).
- If product references changed → re-run CrossRef (stage 7).
- Always re-run Publish (stage 8) to confirm gates still pass.

**Step 3 — Update the checkpoint.**

Edit `checkpoints/{ID}.json` to reflect the updated stage statuses and timestamp.

**Step 4 — If the system mapping changed**, also update:

- `outputs/booking/{ID}.yaml`
- The family's `memory/booking-maps/{FAMILY}_system_mapping.yaml` if the change applies to the whole family.

**Step 5 — Commit.**

```bash
git add outputs/ checkpoints/
git commit -m "Update {ID}: {brief description of change}"
```

### What NOT to Change

- Do not change a product's ID once it exists in the catalog. Other products may reference it.
- Do not change the 8-section heading structure. All downstream tools and reviews depend on it.

---

## 4. How to Create a New Product Family

Creating a new family is a two-phase process: first create the 3 memory artifacts (the "bootstrap"), then generate the first product in the family.

### Phase 1 — Create Memory Artifacts

You must create exactly 3 files:

**4.1 Terminology file** — `memory/terminology/{FAMILY}.yaml`

```yaml
meta:
  product_id: {FAMILY}
  product_name: "{Family Long Name} (family)"
  family: {FAMILY}
  category: terminology
  stored_at: "{ISO timestamp}"
  source_stage: style
  version: 1

content:
  product_names:
    - full: "{First Product Full Name}"
      abbreviation: "{ABBR}"
      first_mention_format: "{Full Name} ({ABBR})"

  system_names:
    - name: {SYSTEM}
      casing: "{Correct Casing}"
    # ... list all systems used by this family

  abbreviations:
    - term: "{TERM}"
      expansion: "{Full expansion}"
    # ... list all domain abbreviations
```

**4.2 Booking map** — `memory/booking-maps/{FAMILY}_system_mapping.yaml`

```yaml
meta:
  product_id: {FAMILY}
  product_name: "{Family Long Name} (family)"
  family: {FAMILY}
  category: booking-maps
  stored_at: "{ISO timestamp}"
  source_stage: booking
  version: 1

content:
  system_type: nemo_sophis | murex_four_leg
  book_of_record: NEMO | Murex
  risk_pnl: Sophis | Murex
  legal_document: Termsheet | Murex Confirm
  murex_used: true | false

  # List what each system carries (fields, lifecycle events, etc.)
```

Choosing the system framework is the most consequential decision. The two frameworks are:

- **`nemo_sophis`** — NEMO is book of record, Sophis handles risk/P&L. Used by ELN and CLN (credit and equity products where the risk engine is separate from the booking system).
- **`murex_four_leg`** — Murex handles everything via a four-leg structure (note leg, issuer leg, deposit leg, hedge leg). Used by SRT, STEG, and Swap (rate products where booking and risk live in one system).

**4.3 Style patterns** — `memory/style-patterns/{FAMILY}.yaml`

```yaml
meta:
  product_id: {FAMILY}
  product_name: "{Family Long Name} (family)"
  family: {FAMILY}
  category: style-patterns
  stored_at: "{ISO timestamp}"
  source_stage: style
  version: 1

content:
  heading_format: "Sentence case for H4 subsections"
  currency_notation: "USD with international notation: 10M, 250k, 1.5bn"

  canonical_h4_names:
    - "Definition"
    - "Construction"
    - "Booking & systems"
    - "Pricing intuition"
    - "Worked example (USD 10M)"
    - "Reconciliation specifics"
    - "Desk view"
    - "Desk shorthand"

  known_false_positives:
    - rule: "H4 heading names flagged as non-canonical"
      reason: "The canonical names ARE sentence case per author/writer specs."
      applies_to: "All products"
    # ... add system-specific FPs

  approved_patterns:
    - pattern: "USD prefix on all monetary figures"
      note: "Bare '10M' without 'USD' prefix is a genuine style violation."
    - pattern: "Desk shorthand in italic, 8 words or fewer"
      note: "Count words literally."

  accepted_conventions: []
  # Add family-specific conventions here as they are validated
```

### Phase 2 — Generate the Bootstrap Product

The first product in a new family is the "bootstrap." Follow the full procedure in Section 2 (How to Add a New Product). During this process:

- The QA review may surface new conventions specific to this family (e.g., CMS decomposition format for STEG). Note these but do not immediately add them to the style-patterns file.
- After the bootstrap product passes all gates, review any deferred conventions. If they are expected to recur in future products of this family, add them to `memory/style-patterns/{FAMILY}.yaml` under `accepted_conventions`.

### Validation

After creating the family:

- [ ] All 3 memory files exist and follow the schema above.
- [ ] The bootstrap product has all 10 artifacts and status `complete`.
- [ ] The system mapping is correct (verify against how the desk actually books the product).

---

## 5. How to Update Memory Artifacts

### When to Update

- A new abbreviation or product name is added to the family.
- The system mapping changes (e.g., migration from NEMO to a new platform).
- A new accepted convention is validated across multiple products.
- A known false positive is identified during review.

### Rules

1. **Never delete information from memory artifacts without verifying that no product depends on it.** Grep for the term across all drafts and review files first.
2. **Increment the `version` field** in the `meta` block each time you edit a memory file.
3. **Update the `stored_at` timestamp** to the current date.
4. **Accepted conventions require validation.** A convention should only be added to `accepted_conventions` after it has been observed in at least 2 products in the family and confirmed to be inherent to the product structure (not an error).

### Step-by-Step

```bash
# 1. Edit the memory file
#    e.g., memory/terminology/CLN.yaml — add a new product name

# 2. Verify no downstream breakage
grep -r "OLD_TERM" outputs/drafts/ outputs/reviews/ outputs/style/

# 3. Commit
git add memory/
git commit -m "Update {FAMILY} {category}: {brief description}"
```

### Memory File Locations

| Category | Path Pattern | Purpose |
|----------|-------------|---------|
| Terminology | `memory/terminology/{FAMILY}.yaml` | Product names, abbreviations, system casing |
| Booking maps | `memory/booking-maps/{FAMILY}_system_mapping.yaml` | System framework, field ownership |
| Style patterns | `memory/style-patterns/{FAMILY}.yaml` | Heading format, FP suppressions, conventions |

---

## 6. How to Perform Annual Reviews

The Desk Bible should be reviewed annually to catch stale content. The review covers 4 areas.

### 6.1 Market Convention Review

Check each product draft for:

- **Benchmark rates.** Are the reference rates still current? (e.g., LIBOR → SOFR transition would require updating all rate-linked products.)
- **Index compositions.** Is CDX IG still 125 names? Has the on-the-run series changed?
- **Recovery rate assumptions.** Are the standard recovery rates (40% for IG credit) still market convention?
- **Typical deal sizes and maturities.** Do the "typical" ranges in the research files still reflect actual desk flow?

### 6.2 System Mapping Review

For each family:

1. Open `memory/booking-maps/{FAMILY}_system_mapping.yaml`.
2. Confirm with the desk that the book-of-record and risk systems are still correct.
3. If a system migration has occurred, update the booking map and re-run booking (stage 4) for all affected products.

### 6.3 Arithmetic Spot-Check

Select 3–5 products at random. For each:

1. Open `outputs/drafts/{ID}.md`, find the Worked Example section.
2. Verify the decomposition sums to the stated coupon/premium.
3. Verify at least one scenario's arithmetic end-to-end.
4. Cross-check against the QA review file (`outputs/reviews/{ID}_qa.yaml`) — the `arithmetic_verification` block should confirm all checks pass.

### 6.4 Cross-Reference Integrity

Run the validation procedure in Section 7 below.

### Documenting the Review

Create a file `reports/annual_review_{YEAR}.md` documenting:

- Date of review.
- Reviewer name.
- Products spot-checked.
- Issues found and actions taken.
- Overall verdict (PASS / PASS WITH ACTIONS / FAIL).

Commit and tag:

```bash
git add reports/
git commit -m "Annual review {YEAR}: {verdict}"
git tag annual-review-{YEAR}
```

---

## 7. How to Validate Cross-References

Cross-references are product-to-product mentions in the draft text. A "broken reference" means a draft mentions a product ID that does not exist in the catalog or whose draft file is missing.

### Manual Validation

```bash
# 1. Extract all product IDs mentioned across all drafts
grep -rohE '[A-Z]{2,10}[0-9]{3}' outputs/drafts/*.md | sort -u > /tmp/mentioned_ids.txt

# 2. Extract all product IDs from the catalog
grep -oE 'id: [A-Z]+[0-9]+' products/catalog.yaml | sed 's/id: //' | sort -u > /tmp/catalog_ids.txt

# 3. Find IDs mentioned in drafts but not in the catalog
comm -23 /tmp/mentioned_ids.txt /tmp/catalog_ids.txt
```

Any output from step 3 is a potential broken reference. Review each hit — some may be false positives (e.g., "USD10M" matching the pattern).

### Crossref File Validation

```bash
# Check that every crossref file reports zero broken references
grep -l "broken_references: [^0]" outputs/crossref/*.yaml
```

Any file returned has broken references that need investigation.

### After Adding or Removing Products

When you add or remove a product, other products' crossref files may become stale. Re-validate:

1. Identify which products reference the added/removed product:
   ```bash
   grep -rl "{PRODUCT_ID}" outputs/crossref/*.yaml
   ```
2. Re-run the crossref stage (stage 7) for each affected product.
3. Update their checkpoints.

---

## 8. How to Regenerate the Final Desk Bible

The "final Desk Bible" is the collection of all 28 (or more) draft Markdown files in `outputs/drafts/`. To assemble them into a single document:

### Option A — Concatenated Markdown

```bash
# Concatenate all drafts in catalog order
# (Manually list them in the order they appear in catalog.yaml)
cat outputs/drafts/RC001.md \
    outputs/drafts/DRC001.md \
    outputs/drafts/KODRC001.md \
    # ... (all 28 files in catalog order)
    > Desk_Bible_Complete.md
```

### Option B — Per-Family Assembly

```bash
# Assemble by family
for family in ELN SRT CLN STEG Swap; do
  echo "# Part: $family" >> Desk_Bible_by_Family.md
  echo "" >> Desk_Bible_by_Family.md
  # List IDs for this family from catalog, then cat each draft
done
```

### Option C — Word Document

Use the `/docx` skill or a Markdown-to-DOCX converter (e.g., Pandoc):

```bash
pandoc outputs/drafts/*.md -o Desk_Bible.docx \
  --toc --toc-depth=3 \
  --metadata title="Structured Products Desk Bible"
```

### Pre-Regeneration Checklist

Before assembling:

- [ ] All products in catalog have status `complete`.
- [ ] All crossref files report zero broken references.
- [ ] All publish files report gate `READY`.
- [ ] No uncommitted changes to draft files.

---

## 9. Git Workflow for Future Changes

### Branch Strategy

The project uses a single `main` branch. All work is committed directly to `main`. For larger changes (adding multiple products or performing an annual review), consider using a feature branch:

```bash
git checkout -b add-snowball-products
# ... do work ...
git checkout main
git merge add-snowball-products
git branch -d add-snowball-products
```

### Commit Message Convention

Follow the established pattern:

```
{Action}: {count} products ({IDs}) — {family} {milestone}
```

Examples from the project history:

```
Desk Bible complete: 28 of 28 products
Batch 4: 5 products (RASTEG001, CSTEG001, TARN001, SCLN001, FTD001) — STEG family complete, 92.9%
Batch 3B: VSTEG001 (Vanilla Steepener Note) — STEG family bootstrapped
Update VCLN001: recovery rate assumption updated to 35%
Annual review 2027: PASS, 3 minor updates applied
```

### Tagging Convention

```
desk-bible-complete-v{N}       # Major releases (all products complete)
desk-bible-after-{batch-name}  # Post-batch snapshots
desk-bible-before-{event}      # Pre-change safety snapshots
annual-review-{YEAR}           # Annual review checkpoints
```

Always create a `before` tag before making bulk changes:

```bash
git tag desk-bible-before-2027-update
```

### What to Commit

Always commit:
- `outputs/` artifacts (all 8 subdirectories)
- `checkpoints/` JSON files
- `pipeline-logs/` YAML files
- `products/catalog.yaml` (if status changed)
- `reports/` (if new reports generated)
- `memory/` (if memory artifacts updated)

Never commit:
- `.claude/` directory contents
- Temporary or scratch files
- Editor backup files

---

## 10. Release Management Process

### Versioning

The project uses semantic-style tags on `main`:

- **`desk-bible-complete-v1`** — Initial complete release (28 products).
- **`desk-bible-complete-v2`** — Next release after adding products or making significant updates.

Increment the version number when:

- Products are added or removed.
- System mappings change.
- An annual review results in content changes.

Do NOT increment for:
- Typo fixes.
- Report additions.
- Memory artifact updates that don't change any draft content.

### Release Checklist

Before tagging a new release:

1. **Catalog validation.** Every product in the catalog has status `complete`. No `stub`, `existing`, `draft`, or `review` entries remain.
   ```bash
   grep -c "status: complete" products/catalog.yaml
   # Should equal the total product count
   grep -E "status: (stub|existing|draft|review)" products/catalog.yaml
   # Should return nothing
   ```

2. **Checkpoint validation.** Every product has a checkpoint, and all show `all_gates_passed: true`.
   ```bash
   ls checkpoints/*.json | wc -l
   # Should equal product count
   grep -L "all_gates_passed.*true" checkpoints/*.json
   # Should return nothing
   ```

3. **Publishing validation.** Every product has a pubspec with gate `READY`.
   ```bash
   grep -L "gate: READY" outputs/publish/*_pubspec.yaml
   # Should return nothing
   ```

4. **Cross-reference validation.** Zero broken references (see Section 7).

5. **Memory consistency.** Every family with products has all 3 memory artifacts.
   ```bash
   for f in ELN SRT CLN STEG Swap; do
     echo "$f:"
     ls memory/terminology/$f.yaml memory/booking-maps/${f}_system_mapping.yaml memory/style-patterns/$f.yaml 2>&1
   done
   ```

6. **Clean working tree.**
   ```bash
   git status
   # Should show no uncommitted changes to tracked files
   ```

### Release Steps

```bash
# 1. Run the release checklist above

# 2. Update the dashboard
#    Edit reports/desk_bible_progress.md with current counts

# 3. Update production history
#    Add a new entry to reports/production_history.log

# 4. Commit
git add .
git commit -m "Release v{N}: {summary of changes since last release}"

# 5. Tag
git tag desk-bible-complete-v{N}

# 6. Verify
git log --oneline -1
git tag -l | grep complete
```

---

## 11. Quality-Control Checklist

Use this checklist when generating or updating any product. All items must pass before the product can be marked `complete`.

### Per-Product Checklist

**Artifacts:**
- [ ] `outputs/research/{ID}.yaml` exists
- [ ] `outputs/blueprints/{ID}.yaml` exists
- [ ] `outputs/drafts/{ID}.md` exists and has all 8 sections
- [ ] `outputs/booking/{ID}.yaml` exists and references the correct system framework
- [ ] `outputs/reviews/{ID}_qa.yaml` exists with gate `PASS`
- [ ] `outputs/style/{ID}_style.yaml` exists with gate `PASS`
- [ ] `outputs/crossref/{ID}_crossref.yaml` exists with gate `PASS`
- [ ] `outputs/publish/{ID}_pubspec.yaml` exists with gate `READY`
- [ ] `checkpoints/{ID}.json` exists with `all_gates_passed: true`
- [ ] `pipeline-logs/{slug}.yaml` exists

**Content Quality:**
- [ ] Draft H3 heading matches `### {Product Name} ({Abbreviation})`
- [ ] Draft has exactly 8 H4 sections in canonical order
- [ ] Worked example uses USD 10M notional
- [ ] Decomposition arithmetic sums correctly (verify computationally)
- [ ] All scenario arithmetic is correct
- [ ] Desk shorthand is italicised and 8 words or fewer
- [ ] Currency notation uses USD prefix throughout (no bare numbers)

**System Mapping:**
- [ ] Booking YAML references the correct system (NEMO/Sophis or Murex)
- [ ] System mapping matches the family's booking-map memory artifact
- [ ] Critical booking fields are marked `critical: true`
- [ ] At least 2 failure modes are documented

**Reviews:**
- [ ] QA review: zero BLOCKERs
- [ ] QA review: all arithmetic computationally verified (not just eyeballed)
- [ ] QA review: rounding tolerance applied (±0.2%)
- [ ] Style review: zero MUST_FIX violations
- [ ] Style review: known false positives suppressed (not raised as violations)
- [ ] CrossRef review: zero broken references
- [ ] CrossRef review: forward references are flagged but not treated as broken

**Catalog:**
- [ ] Product appears in `products/catalog.yaml`
- [ ] Status is `complete`
- [ ] Family assignment is correct
- [ ] Section number is assigned

### Per-Batch Checklist

When generating multiple products in a batch:

- [ ] All products in the batch pass the per-product checklist above.
- [ ] Batch report created in `reports/`.
- [ ] Production history log updated in `reports/production_history.log`.
- [ ] Dashboard updated in `reports/desk_bible_progress.md`.
- [ ] All changes committed with a descriptive commit message.
- [ ] Post-batch tag created.
- [ ] No regressions in previously completed products (spot-check 1–2 existing crossref files).

---

## Appendix A — Quick Reference Commands

```bash
# Count completed products
grep -c "status: complete" products/catalog.yaml

# List incomplete products
grep -B1 "status: \(stub\|existing\|draft\|review\)" products/catalog.yaml

# Verify all checkpoints pass
for f in checkpoints/*.json; do
  id=$(basename "$f" .json)
  pass=$(grep -o '"all_gates_passed": true' "$f")
  [ -z "$pass" ] && echo "FAIL: $id"
done

# Find broken cross-references
grep -l "broken_references: [^0]" outputs/crossref/*.yaml

# List all memory artifacts
find memory -name "*.yaml" -type f | sort

# Check artifact count per product
for id in $(grep -oP 'id: \K[A-Z]+[0-9]+' products/catalog.yaml); do
  count=0
  [ -f "outputs/research/$id.yaml" ] && ((count++))
  [ -f "outputs/blueprints/$id.yaml" ] && ((count++))
  [ -f "outputs/drafts/$id.md" ] && ((count++))
  [ -f "outputs/booking/$id.yaml" ] && ((count++))
  [ -f "outputs/reviews/${id}_qa.yaml" ] && ((count++))
  [ -f "outputs/style/${id}_style.yaml" ] && ((count++))
  [ -f "outputs/crossref/${id}_crossref.yaml" ] && ((count++))
  [ -f "outputs/publish/${id}_pubspec.yaml" ] && ((count++))
  [ -f "checkpoints/$id.json" ] && ((count++))
  [ $count -lt 9 ] && echo "INCOMPLETE ($count/9 artifacts): $id"
done

# Show all git tags
git tag -l | sort

# Show project timeline
git log --oneline --decorate
```

## Appendix B — Glossary

| Term | Meaning |
|------|---------|
| **Artifact** | A file produced by a pipeline stage (YAML or Markdown). |
| **Bootstrap** | The first product generated in a new family, which validates the family's memory artifacts. |
| **Checkpoint** | A JSON file tracking which pipeline stages are complete for a product. |
| **Gate** | A pass/fail decision point (QA, Style, CrossRef, Publish). All must pass for publication. |
| **Memory artifact** | A per-family YAML file storing reusable knowledge (terminology, booking maps, style patterns). |
| **Pipeline** | The 8-stage process that transforms a catalog entry into a complete product page. |
| **Pubspec** | The publishing specification — final gate check before a product is marked complete. |
| **Forward reference** | A mention of a product that exists in the catalog but hasn't been generated yet. Not treated as broken. |

## Appendix C — Contact and History

| Item | Value |
|------|-------|
| Initial generation completed | 2026-06-19 |
| Products at v1 release | 28 |
| Families at v1 release | 5 (ELN, SRT, CLN, STEG, Swap) |
| Pipeline version | v2.1 |
| Baseline tag | `desk-bible-complete-v1` |
| Final report | `reports/Desk_Bible_Final_Report.md` |
| Production history | `reports/production_history.log` |
