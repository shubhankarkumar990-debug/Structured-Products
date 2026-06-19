# Quality Control Guide

## Gate Architecture

Three independent review gates, each with a binary PASS/FAIL result. All three must pass before an entry can be published.

```
Draft ──▶ Accuracy Gate ──▶ Style Gate ──▶ CrossRef Gate ──▶ Publish Gate
              │                  │                │                │
          PASS/FAIL          PASS/FAIL        PASS/FAIL       READY/NOT
```

If any gate fails, fix the draft, then re-run only the failed gate — not the entire review pipeline.

---

## Gate 1 — Accuracy

**Purpose:** Verify factual correctness and computational integrity.  
**Output:** `outputs/reviews/{ID}_accuracy.yaml`  
**Pass criteria:** Zero BLOCKERs.

### Severity Levels

| Level | Meaning | Blocks Publication |
|-------|---------|-------------------|
| **BLOCKER** | Verified factual error or arithmetic mistake | Yes |
| **MAJOR** | Structural concern, advisory only | No |
| **MINOR** | Suggestion for improvement | No |

### The Arithmetic Verification Protocol

The most important quality control lesson from the Desk Bible: **computationally verify all arithmetic before raising a BLOCKER.**

Without this protocol, the review gate raised false BLOCKERs for calculations that were correct within rounding tolerance. The protocol:

1. For every arithmetic claim in the draft, reproduce the calculation.
2. Compare the computed result to the stated result.
3. Apply a rounding tolerance (±0.2% for financial calculations; adjust per domain).
4. Only raise a BLOCKER if the computed result falls outside tolerance.
5. Record every verification in the review artifact: formula, expected, computed, match.

### Advisory Findings

Some findings are inherent to the entry structure and will recur across all entries in a family. These should be classified as MAJOR advisory (not BLOCKER) and noted in the family's style-conventions memory as an accepted convention after validation.

**Example from the Desk Bible:** Every product's cost decomposition was flagged as a MAJOR because the format differed from a simple sum. This was inherent to the product structure. After validation across multiple products, it was accepted as a convention.

---

## Gate 2 — Style

**Purpose:** Verify formatting, notation, and terminology consistency.  
**Output:** `outputs/reviews/{ID}_style.yaml`  
**Pass criteria:** Zero MUST_FIX violations.

### Check Categories

| Category | What It Checks | Example |
|----------|---------------|---------|
| **Heading structure** | Correct H3/H4 hierarchy, canonical section names | "Definition" not "What Is It" |
| **Notation** | Currency prefixes, number formatting | "USD 10M" not "10M" |
| **System references** | Correct casing per terminology memory | "NEMO" not "Nemo" |
| **Entry shorthand** | Format rules (italic, word limit) | Italic, 8 words max |
| **Forbidden phrases** | Terms that should never appear | Domain-specific blocklist |

### False Positive Suppression

The style-conventions memory file lists known false positives — rules that the reviewer flags as violations but which are actually correct. The style gate must check this list before raising a MUST_FIX.

**Example from the Desk Bible:** Every product had 3 known FPs (H4 heading names, Sophis casing, Termsheet casing). Without suppression, 84 false violations would have been raised across 28 products.

### Severity Levels

| Level | Meaning | Blocks Publication |
|-------|---------|-------------------|
| **MUST_FIX** | Genuine style violation | Yes |
| **SHOULD_FIX** | Improvement suggestion | No |

---

## Gate 3 — Cross-Reference

**Purpose:** Verify that all internal references are valid.  
**Output:** `outputs/reviews/{ID}_crossref.yaml`  
**Pass criteria:** Zero broken references.

### Reference Types

| Type | Definition | Blocking? |
|------|-----------|-----------|
| **Explicit comparison** | Draft directly compares this entry to another | Yes if target doesn't exist |
| **Implicit reference** | Draft mentions another entry by name | Yes if target doesn't exist |
| **Forward reference** | Draft mentions an entry that exists in the catalog but hasn't been generated yet | No — warning only |
| **Cross-family reference** | Reference to an entry in a different family | Same rules as above |

### Validation Procedure

1. Extract all entry IDs mentioned in the draft.
2. Check each ID against the catalog.
3. For IDs in the catalog with status `complete`: verify the draft file exists. If missing → broken reference.
4. For IDs in the catalog with status `stub`/`draft`/`review`: classify as forward reference (warning, not broken).
5. For IDs NOT in the catalog: broken reference.

---

## Publish Gate

**Purpose:** Final confirmation that all upstream gates passed.  
**Output:** `outputs/publish/{ID}_pubspec.yaml`  
**Pass criteria:** All of the following must be true:

- [ ] Draft file exists.
- [ ] All required sections present.
- [ ] Accuracy gate: PASS.
- [ ] Style gate: PASS.
- [ ] CrossRef gate: PASS.
- [ ] Blocking issues: 0.

**Gate result:** READY or NOT_READY.

---

## Per-Entry Quality Checklist

Use this checklist when generating or updating any entry.

### Artifacts
- [ ] Research YAML exists.
- [ ] Draft MD exists with all required sections.
- [ ] Accuracy review YAML exists with gate PASS.
- [ ] Style review YAML exists with gate PASS.
- [ ] CrossRef review YAML exists with gate PASS.
- [ ] Publish YAML exists with gate READY.
- [ ] Checkpoint JSON exists with `all_gates_passed: true`.
- [ ] Pipeline log YAML exists.

### Content
- [ ] Correct heading structure (H3 entry name, H4 sections).
- [ ] All arithmetic computationally verified and correct.
- [ ] Notation consistent throughout.
- [ ] Operational mapping matches family memory.
- [ ] No broken internal references.

### Catalog
- [ ] Entry appears in catalog.
- [ ] Status is `complete`.
- [ ] Family assignment is correct.

---

## Per-Batch Quality Checklist

- [ ] All entries in the batch pass the per-entry checklist.
- [ ] No regressions in previously completed entries (spot-check 1–2 crossref files).
- [ ] Batch report created.
- [ ] Dashboard updated.
- [ ] Production history updated.
- [ ] All changes committed with descriptive message.
- [ ] Post-batch tag created.

---

## Quality Metrics to Track

| Metric | Target | Description |
|--------|--------|-------------|
| Accuracy BLOCKERs | 0 | Must be zero for publication |
| Style MUST_FIX | 0 | Must be zero for publication |
| Broken cross-references | 0 | Must be zero for publication |
| Publishing failures | 0 | Must be zero |
| Retries per entry | 0 | Measures pipeline reliability |
| False positives suppressed | Tracked | Measures memory effectiveness |
| Accepted conventions | Tracked | Measures memory maturation |
