# Release Integrity Policy — SP-KE-V1.0

**Effective**: 2026-06-27
**Scope**: All artifacts in the Structured Products Knowledge Ecosystem V1.0

---

## 1. Freeze Definition

**Version 1.0 is permanently frozen.** This means:

- No content may be added, removed, or modified in any frozen artifact
- No metadata (scores, names, section numbers, family assignments) may be changed
- No structural changes (section ordering, template compliance, cross-references) are permitted
- No new artifacts may be added to the canonical set
- No existing canonical artifacts may be removed or replaced

**"Permanently frozen" means the V1.0 release is immutable.** It is not a pause. It is not a soft lock. It is a permanent, versioned snapshot that cannot be reopened for any reason.

---

## 2. What Is Frozen

### Frozen Artifacts (25 total)
- 13 canonical content artifacts (Desk Bible + 12 production files)
- 12 governance artifacts (standards, checklists, workflows)

### Frozen Properties
- File content (verified by SHA-256 checksums)
- File names
- File locations within the repository
- Version numbers
- Freeze dates
- All metadata values within frozen files

---

## 3. What Is NOT Frozen

### Mutable Layers
- **Release engineering documents** (`release/`): May be regenerated if the validation script or hash manifest needs updating — these are _about_ the release, not _part_ of it
- **Review documents** (`review/`): Historical records, immutable by convention but not by policy
- **Archive/superseded/orphan files**: Retained for provenance, not governed by freeze

### Future Work
- A future V1.0.1 (erratum) or V1.1 (enhancement) release would create **new files** alongside the frozen V1.0 artifacts — it would NOT modify V1.0 files
- Any V1.0.x erratum must: (1) document the error, (2) document the correction, (3) create new corrected files with new version numbers, (4) preserve the original V1.0 files unchanged

---

## 4. Amendment Path

If a critical error is discovered in a frozen V1.0 artifact:

### Step 1: Erratum Documentation
Create `release/erratum_v1_0_001.md` documenting:
- The error (exact file, line, content)
- The impact (who is affected, how)
- The correction (what the correct content should be)
- The discovery date and discoverer

### Step 2: Version Increment
- For minor corrections: create V1.0.1 erratum files alongside V1.0 originals
- For substantive changes: create V1.1 release with full release engineering cycle
- V1.0 originals remain unchanged in both cases

### Step 3: Manifest Update
- Update the release manifest to note the erratum
- The V1.0 SHA-256 hashes remain valid — they prove the V1.0 files are unchanged
- New hashes are generated for the new version files

### What Does NOT Qualify as Critical
- Style preferences
- Pedagogical improvements
- Additional examples or explanations
- Scope expansion
- Alternative approaches to existing content

---

## 5. Integrity Verification

### Automated Verification
```bash
python3 release/validate_release.py --verbose --json
```

This script checks:
- SHA-256 checksums for all 25 frozen artifacts
- Product count consistency (49 products × 6 families)
- Complexity score consistency across all artifacts
- Section number uniqueness and family assignment
- Evolution map statistics (35+10=45 edges)
- Draft/placeholder language scan
- Release manifest and freeze certificate consistency

### Manual Verification
```bash
shasum -a 256 -c release/sha256_manifest.md
```

### Verification Schedule
- Before any repository operation that touches `production/`
- Before any commit that modifies files in the project
- Before any distribution of the ecosystem to external parties

---

## 6. Repository Rules

1. **No force-pushes** to the main branch after freeze
2. **No file renames** within `production/`
3. **No file deletions** from `production/` — archive files stay in place
4. **No new files** in `production/` — new work goes to a versioned directory
5. **No `.gitignore` changes** that would exclude frozen files
6. **Tags**: The freeze commit should be tagged `v1.0-frozen`

---

## 7. Distribution Rules

When distributing the ecosystem:
1. Include all canonical and governance artifacts
2. Include the SHA-256 manifest
3. Include the validation script
4. Include the release notes
5. Recipient should run `validate_release.py` to confirm integrity

---

*Release Integrity Policy — SP-KE-V1.0 — Effective 2026-06-27*
