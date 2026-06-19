# Governance Guide

## Git Workflow

### Branch Strategy

| Project Size | Strategy |
|-------------|----------|
| Solo contributor, < 50 entries | Single `main` branch. Direct commits. |
| Multiple contributors or > 50 entries | Feature branches per batch or family. PR-based merges. |
| Enterprise / regulated | Protected `main`. Mandatory PR reviews. CI validation. |

### Commit Message Convention

```
{Batch/Action}: {count} entries ({IDs}) — {family} {milestone}
```

**Production examples:**
```
Batch 4: 5 entries (RASTEG001, CSTEG001, TARN001, SCLN001, FTD001) — STEG family complete
Update VCLN001: recovery rate assumption updated to 35%
Annual review 2027: PASS, 3 minor updates applied
Bootstrap Credit Risk family: 3 memory artifacts
```

### Tagging Convention

| Pattern | When |
|---------|------|
| `{project}-complete-v{N}` | All entries complete (major release) |
| `{project}-after-batch-{N}` | Post-batch snapshot |
| `{project}-before-{event}` | Pre-change safety snapshot |
| `annual-review-{YEAR}` | Annual review checkpoint |

**Always create a `before` tag before bulk changes.**

### What to Commit

| Always Commit | Never Commit |
|--------------|-------------|
| `outputs/` artifacts | Editor temp files |
| `checkpoints/` | `.env` / credentials |
| `pipeline-logs/` | Scratch/working files |
| `catalog.yaml` (if changed) | IDE settings |
| `reports/` | `.claude/` directory |
| `memory/` (if updated) | OS metadata (`.DS_Store`) |

---

## Batch Management

### Batch Lifecycle

```
1. Pre-batch tag ──────▶ Safety snapshot
2. Generate entries ───▶ Full pipeline per entry
3. Post-batch validate ▶ All gates pass, no regressions
4. Commit + tag ───────▶ Descriptive message + post-batch tag
5. Update reports ─────▶ Dashboard + production history
```

### Batch Sizing

| Factor | Recommendation |
|--------|---------------|
| First batch (Batch 0) | 1 entry per family (bootstrap). Max 6 entries. |
| Production batches | 3–6 entries from the same family. |
| Cross-family batches | Acceptable but track memory usage carefully. |
| Max batch size | 8 entries. Beyond this, split into two batches. |

### Production History Log

Maintain a running log (`reports/production_history.log`) with one entry per batch:

- Date
- Entries generated (IDs and names)
- Quality metrics (BLOCKERs, MUST_FIX, broken refs)
- Memory metrics (created, reused)
- Estimated tokens
- Cumulative progress
- Notes (notable decisions, issues, conventions)

---

## Dashboard

Maintain a progress dashboard (`reports/progress_dashboard.md`) updated after every batch:

- Overall progress: X/Y (Z%)
- Per-family progress table
- Completed entries list by family
- Batch history table
- Quality metrics (cumulative)
- Memory metrics
- Remaining work forecast

The dashboard is the most-consulted report during production. The progress bar is motivating.

---

## Annual Review Process

### Scope

1. **Domain accuracy.** Are the facts still correct? Have standards, rates, regulations, or systems changed?
2. **Operational mapping.** Are the system/process references still current?
3. **Arithmetic spot-check.** Select 3–5 entries at random. Verify worked examples.
4. **Cross-reference integrity.** Run the cross-reference validation.

### Procedure

1. Create `reports/annual_review_{YEAR}.md`.
2. Document: reviewer, date, entries checked, issues found, actions taken.
3. Apply fixes to affected drafts. Re-run affected review stages.
4. Commit and tag: `annual-review-{YEAR}`.

### Cadence

- **Year 1:** Full review of all entries.
- **Year 2+:** Spot-check 30% of entries + full review of any families affected by system or regulatory changes.

---

## Change Management

### Adding Entries

1. Add to catalog with status `stub`.
2. Run full pipeline.
3. Update catalog to `complete`.
4. Commit with descriptive message.

### Updating Entries

1. Edit draft directly.
2. Re-run affected review stages.
3. Update checkpoint.
4. Commit.

### Removing Entries

1. Check cross-references: does any other entry reference this one?
2. If yes, update those entries first.
3. Remove from catalog (or set status to `deprecated`).
4. Do NOT delete artifacts — move to `archive/` if needed.
5. Commit.

### Changing Operational Mappings

This is the highest-risk change. Procedure:

1. Update the family's operational map memory.
2. Re-run Stage 2 (Write) and Stage 4 (Booking/mapping) for ALL entries in the family.
3. Re-run Stage 3 (Review) for all affected entries.
4. Verify all gates pass.
5. Commit with a detailed message explaining the mapping change.

---

## Access Control (Enterprise)

| Role | Permissions |
|------|------------|
| **Author** | Generate entries, run pipeline, update drafts |
| **Reviewer** | Run review stages, approve/reject gates |
| **Publisher** | Run publish stage, create releases |
| **Admin** | Update memory, change operational mappings, create families |

In a solo project, one person holds all roles. In an enterprise context, separate the Author and Reviewer roles to prevent self-review.
