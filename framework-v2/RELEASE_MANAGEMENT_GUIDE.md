# Release Management Guide

## Versioning

### Version Tags

```
{project}-complete-v{N}    # Major release (all entries complete or content milestone)
{project}-v{N}-release     # Release package created (may coincide with complete)
```

### When to Increment

| Change Type | Action |
|-------------|--------|
| Entries added or removed | Increment major version |
| Operational mappings changed | Increment major version |
| Annual review with content changes | Increment major version |
| Typo fixes, report additions | No version increment |
| Memory updates with no draft changes | No version increment |

---

## Pre-Release Validation

Run the 5-point validation before every release:

### 1. Catalog Validation

```bash
# All entries complete
grep -c "status: complete" catalog.yaml
# No incomplete entries
grep -E "status: (stub|existing|draft|review)" catalog.yaml
# ^ Should return nothing
```

### 2. Checkpoint Validation

```bash
# All entries have checkpoints
ls checkpoints/*.json | wc -l
# All gates passed
grep -L "all_gates_passed.*true" checkpoints/*.json
# ^ Should return nothing
```

### 3. Cross-Reference Validation

```bash
# No broken references
grep -l "broken_references: [^0]" outputs/reviews/*_crossref.yaml
# ^ Should return nothing
```

### 4. Publishing Validation

```bash
# All entries READY
grep -L "gate: READY" outputs/publish/*_pubspec.yaml
# ^ Should return nothing
```

### 5. Memory Consistency

```bash
# All families have all 3 memory types
for f in {FAMILY1} {FAMILY2} {FAMILY3}; do
  ls memory/terminology/$f.yaml \
     memory/operational-maps/$f.yaml \
     memory/style-conventions/$f.yaml 2>&1
done
```

---

## Release Package

### Structure

```
release/{project}-v{N}/
├── {Project}_v{N}.md               # Assembled document (all entries)
├── release_notes_v{N}.md           # Release notes
├── catalog.yaml                    # Product catalog
├── Final_Report.md                 # Completion, quality, operational metrics
├── progress_dashboard.md           # Dashboard (100%)
├── production_history.log          # Full batch-by-batch history
├── Maintenance_Guide.md            # Operational runbook
├── memory/                         # All memory artifacts
├── checkpoints/                    # All checkpoints
└── outputs/                        # All pipeline outputs
```

### Assembly Steps

1. **Assemble the document.** Concatenate all drafts in catalog order.
2. **Copy supporting files.** Catalog, reports, memory, checkpoints, outputs.
3. **Generate release notes.** Include: overview, entry counts, quality metrics, memory metrics, tags, milestones, known limitations, future opportunities.

### Release Notes Template

```markdown
# Release Notes — {Project} v{N}

**Date:** {date}
**Tag:** `{tag}`
**Commit:** `{hash}`

## Entry Counts by Family
| Family | Count |
|--------|------:|
| {Family1} | {N} |
| **Total** | **{N}** |

## Quality Metrics
| Metric | Value |
|--------|-------|
| Accuracy BLOCKERs | 0 |
| Style MUST_FIX | 0 |
| Broken cross-references | 0 |

## Known Limitations
{list}

## Future Enhancement Opportunities
{list}
```

---

## Release Workflow

```bash
# 1. Run 5-point validation (above)

# 2. Create release directory
mkdir -p release/{project}-v{N}

# 3. Assemble document
# (concatenate drafts in catalog order)

# 4. Copy artifacts
cp catalog.yaml release/{project}-v{N}/
cp -r memory checkpoints outputs release/{project}-v{N}/

# 5. Generate release notes
# (write release_notes_v{N}.md)

# 6. Commit
git add release/ reports/
git commit -m "Release packaging: {project}-v{N}-release"

# 7. Tag
git tag {project}-v{N}-release

# 8. Verify
git log --oneline -1
git tag -l | grep release
```

---

## Post-Release

1. **Update production history** with a release entry.
2. **Mark project status** in the final log entry: ARCHIVED / RELEASED / COMPLETE.
3. **Communicate** the release to stakeholders with the release notes.
4. **Archive** the release package in a durable location (shared drive, artifact repository, etc.).
