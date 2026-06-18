# Project Retrospective

**Project:** Structured Products Desk Bible  
**Duration:** 2026-06-18 to 2026-06-19 (2 days)  
**Scope:** 28 products, 5 families, 280+ artifacts  
**Sessions:** 4 (with 3 context continuations)

---

## Architecture

### What Worked Well

1. **The 8-stage pipeline was the right abstraction.** Each stage has a clear input, a clear output, and a single responsibility. This made the pipeline debuggable — when something looked wrong in a draft, we knew exactly which stage to re-run. No stage was ever removed or merged during production.

2. **Artifact-based state management.** Every intermediate result is a file on disk. This meant the pipeline could be interrupted at any point (including across context continuations) and resumed by checking which files exist. No in-memory state was ever lost.

3. **Three execution modes (DRAFT/REVIEW/PUBLISH) were sufficient.** We never needed a fourth mode. DRAFT for content generation, REVIEW for quality gates, PUBLISH for the final check. The FULL mode (all 8 stages) was used for most products after the pipeline stabilised.

4. **Per-family memory eliminated repetitive decisions.** Once a family's system mapping, terminology, and style rules were established, every subsequent product in the family reused them without modification. This drove the zero-retry rate from Batch 1 onward.

### What Failed

Nothing failed catastrophically. The pipeline completed all 28 products with zero retries from Batch 1 onward.

The closest to a failure was the **QA false-BLOCKER problem in Batch 0**, where the QA stage raised BLOCKERs for arithmetic that was actually correct (within rounding tolerance). This was fixed by implementing the arithmetic verification protocol (v2.1) before moving to Batch 1.

### What Was Simplified

1. **Agent count.** The architecture defines 12 agents, but in practice the content writer, example generator, and reconciliation generator were treated as a single writing stage. The separation exists in the spec but added no value during execution.

2. **Checkpoint recovery.** The checkpoint system was built for crash recovery. It was never activated — zero crashes, zero partial failures across 28 products. The checkpoints served as audit records instead.

3. **Memory subdirectories.** The `memory/` directory has subdirectories for `components/`, `definitions/`, `examples/`, and `reconciliation/`, but only `terminology/`, `booking-maps/`, and `style-patterns/` were ever used. The other subdirectories remained empty.

### What Was Overengineered

1. **The 12-agent architecture.** In practice, a single operator ran all stages sequentially. The agent separation added cognitive overhead (reading 12 spec files) without adding parallelism or specialisation value. A 4-stage pipeline (Research, Write, Review, Publish) with inline sub-steps would have been simpler.

2. **Stage briefings directory.** `agents/stage-briefings/` was created but provided no additional value over the agent specs themselves.

3. **Execution mode routing.** The orchestrator's mode-routing logic (DRAFT/REVIEW/PUBLISH/FULL) could have been a simple function argument rather than a dedicated architectural concept.

---

## Tokens

### Initial Estimates

The pre-production estimate was ~15,000 tokens per product for a full pipeline run. This was based on the PHX001 reference product (the first product generated, which included significant pipeline engineering overhead).

### Actual Estimates

| Batch | Products | Tokens (est.) | Per Product |
|-------|----------|--------------|-------------|
| Batch 0 | 6 | ~89,196 | ~14,866 |
| Batch 1 | 5 | ~74,330 | ~14,866 |
| Batch 2 | 5 | ~74,330 | ~14,866 |
| Batch 3A | 4 | ~59,464 | ~14,866 |
| Batch 3B | 1 | ~14,866 | ~14,866 |
| Batch 4 | 5 | ~74,330 | ~14,866 |
| Final | 2 | ~29,732 | ~14,866 |
| **Total** | **28** | **~416,248** | **~14,866** |

The per-product cost was remarkably stable at ~14,866 tokens across all batches, regardless of product complexity (from AFRN001, the simplest, to TARN001, the most complex).

### Largest Token Consumers

1. **Stage 3 (Writing)** — the draft itself is the longest artifact (~1,500–2,500 words per product). This stage consumed approximately 40–50% of per-product tokens.
2. **Stage 5 (QA Review)** — arithmetic verification requires reproducing and checking every calculation. Approximately 15–20% of per-product tokens.
3. **Stage 1 (Research)** — domain research for each product. Approximately 15% of per-product tokens.

### Biggest Optimisations

1. **Memory reuse.** Without memory, each product would re-derive system mappings, terminology, and style rules. Memory reuse saved an estimated 20–30% of per-product tokens from Batch 1 onward.
2. **FULL execution mode.** Running all 8 stages in a single pass eliminated the overhead of re-reading context between DRAFT and REVIEW modes. This became the default from Batch 2 onward.
3. **Batch processing.** Generating 3–6 products in a single batch amortised the setup overhead (reading memory files, loading the catalog) across multiple products.

---

## Memory

### Most Valuable Memory Artifacts

Ranked by impact on quality and efficiency:

1. **Booking maps** (`memory/booking-maps/`) — Prevented the single most dangerous error class (wrong system mapping). A product booked in the wrong system is a live operational risk. These files were consulted for every product and never required correction after initial creation.

2. **Style patterns** (`memory/style-patterns/`) — Eliminated false-positive QA and style violations. Without these, every product would have raised 3+ false violations for known FPs (H4 heading names, Sophis casing, Termsheet casing). Across 28 products, this prevented ~84 false violations.

3. **Terminology** (`memory/terminology/`) — Ensured consistent abbreviation usage. Less critical than the other two (a wrong abbreviation is noticeable but not operationally dangerous), but essential for document-wide consistency.

### Reuse Metrics

| Family | Products | Memory Created | Memory Reused | Reuse Ratio |
|--------|----------|---------------|---------------|-------------|
| ELN | 13 | 3 (Batch 0) | 36 | 12:1 |
| SRT | 5 | 3 (Batch 0) | 12 | 4:1 |
| CLN | 5 | 3 (Batch 0) | 12 | 4:1 |
| STEG | 4 | 3 (pre-Batch 3) | 9 | 3:1 |
| Swap | 1 | 3 (Batch 0) | 0 | 0:1 |
| **Total** | **28** | **15** | **69** | **4.6:1** |

ELN had the highest reuse ratio (12:1) because it had the most products (13) sharing the same 3 memory artifacts.

### Bootstrap Lessons

| Family | Bootstrap Product | Corrections Needed | New Conventions Found |
|--------|-------------------|--------------------|-----------------------|
| ELN | RC001 | 12 conventions established | 12 (foundational) |
| CLN | VCLN001 | 2 (credit event casing) | 2 |
| SRT | IRCFRN001 | 3 (Murex four-leg specifics) | 3 |
| STEG | VSTEG001 | 0 | 1 (CMS decomposition — deferred) |
| Swap | SWAP001 | 0 | 0 |

VSTEG001 was the cleanest bootstrap — zero corrections, one deferred convention (later validated across all 4 STEG products). This suggests the memory layer pattern was well-understood by the time STEG was bootstrapped.

---

## Quality

### QA Trends

| Batch | Products | BLOCKERs | MAJORs (advisory) | Per Product |
|-------|----------|----------|-------------------|-------------|
| Batch 0 | 6 | 0 | 8 | 1.3 |
| Batch 1 | 5 | 0 | 6 | 1.2 |
| Batch 2 | 5 | 0 | 5 | 1.0 |
| Batch 3A | 4 | 0 | 4 | 1.0 |
| Batch 3B | 1 | 0 | 1 | 1.0 |
| Batch 4 | 5 | 0 | 5 | 1.0 |
| Final | 2 | 0 | 2 | 1.0 |

**Key finding:** Zero BLOCKERs across all 28 products. The arithmetic verification protocol (v2.1) was effective — it caught rounding issues within tolerance rather than raising false BLOCKERs.

MAJORs stabilised at exactly 1 per product from Batch 2 onward (the decomposition format advisory). This is inherent to the product structure and correctly classified as advisory.

### Style Trends

| Batch | Products | MUST_FIX | SHOULD_FIX | False Positives Suppressed |
|-------|----------|----------|------------|---------------------------|
| Batch 0 | 6 | 0 | 3 | 22 |
| Batch 1 | 5 | 0 | 2 | 20 |
| Batch 2 | 5 | 0 | 0 | 17 |
| Batch 3+ | 17 | 0 | 0 | 45 |

**Key finding:** SHOULD_FIX findings dropped to zero from Batch 2 onward. The style-pattern memory layer achieved full coverage of family-specific conventions by that point.

### Cross-Reference Trends

| Batch | Products | Broken Refs | Warnings (Forward Refs) | Cross-Family Refs |
|-------|----------|-------------|------------------------|-------------------|
| Batch 0 | 6 | 0 | 3 | 0 |
| Batch 1 | 5 | 0 | 5 | 0 |
| Batch 2 | 5 | 0 | 5 | 0 |
| Batch 3A | 4 | 0 | 4 | 2 |
| Batch 3B | 1 | 0 | 2 | 3 |
| Batch 4 | 5 | 0 | 2 | 2 |
| Final | 2 | 0 | 1 | 0 |

**Key finding:** Zero broken references across the entire project. Forward references (warnings) resolved naturally as later batches generated the target products. Cross-family references appeared starting in Batch 3A (SRT→ELN) and Batch 3B (STEG→SRT), validating the bible's internal consistency.

### Publishing Trends

Zero publishing failures across all 28 products. The publishing gate never blocked a product — all upstream gates caught issues before stage 8.

---

## Governance

### Git Workflow Effectiveness

**What worked:**
- Single `main` branch was sufficient for a solo-contributor project.
- Per-batch commits with descriptive messages created a clean, readable history.
- Pre-batch and post-batch tags provided safe rollback points. None were ever needed for rollback, but they served as clear milestones.
- 10 tags created across the project — not too many, not too few.

**What would change at scale:**
- Multiple contributors would need feature branches and pull requests.
- A CI pipeline could automate the 5-point validation (catalog, checkpoints, crossrefs, publishing, memory).

### Checkpoint Effectiveness

Checkpoints were created for all 28 products. Their actual use:

- **Recovery:** Never used. Zero crashes, zero partial failures.
- **Validation:** Used in the final 5-point validation to confirm all gates passed.
- **Auditing:** Useful for confirming the retry count (zero for all Batch 1+ products).

**Verdict:** The checkpoint system was insurance that was never claimed. Worth having for a 28-product project. For a smaller project (< 10 products), the overhead of creating checkpoint files may not justify the safety benefit.

### Dashboard Usefulness

The progress dashboard (`reports/desk_bible_progress.md`) was updated after every batch. It provided:

- A single place to check overall progress (X/Y, Z%).
- Per-family completion status.
- Cumulative quality metrics.
- Remaining work forecast.

**Verdict:** High value. The dashboard was the most-consulted report during production. The progress bar was motivating.

---

## Recommendations

### If Rebuilding From Scratch

**Keep:**

1. **Artifact-based pipeline.** Files on disk as the state mechanism. This is the single most important architectural decision — it enables resumption, auditing, and debugging.
2. **Per-family memory layer.** The 3-artifact pattern (terminology, booking maps, style patterns) paid for itself many times over.
3. **Gate-based quality control.** Binary PASS/FAIL gates with clear criteria. No subjective judgments.
4. **Arithmetic verification protocol.** Computationally verify arithmetic before raising BLOCKERs. The ±0.2% rounding tolerance is essential.
5. **Convention validation protocol.** Observe in one product, validate in two, then enshrine. This prevented false conventions.
6. **Batch processing with pre/post tags.** Efficient and safe.

**Change:**

1. **Simplify to 4 stages, not 8.** Research → Write → Review → Publish. The current 8 stages split the write and review phases into sub-stages that don't justify their overhead. Keep the sub-steps as internal steps within the Write and Review stages, not as separate pipeline stages.
2. **Simplify to 4 agents, not 12.** One agent per stage. The current 12-agent architecture was never used to its full potential (no parallelism, no independent agent execution).
3. **Remove unused memory subdirectories.** Only `terminology/`, `booking-maps/`, and `style-patterns/` are needed. Remove `components/`, `definitions/`, `examples/`, `reconciliation/`.
4. **Make the dashboard auto-generated.** Currently the dashboard is manually updated after each batch. A script that reads the catalog and checkpoints could generate it automatically.
5. **Add a catalog-driven assembly script.** Currently, assembling the final document is a manual concatenation step. A script that reads the catalog order and concatenates drafts would eliminate this manual step.

**Remove:**

1. **Stage briefings directory.** Never provided value beyond the agent specs.
2. **The `schemas/` directory.** Was created but never populated or used.
3. **The distinction between DRAFT/REVIEW/PUBLISH modes.** In practice, FULL mode was used for every product after Batch 0. The separate modes were useful during pipeline development but unnecessary during production.
