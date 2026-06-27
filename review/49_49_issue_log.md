# 49/49 Issue Log

**Date:** 2026-06-21
**Audit Phase:** All (1-6)
**Status:** READ-ONLY AUDIT

---

## Issue Classification

| Severity | Definition |
|----------|-----------|
| CRITICAL | Missing chapter, missing required section, broken product decomposition |
| HIGH | Missing DNA Atlas field, broken cross-reference, incorrect complexity score |
| MEDIUM | Missing jargon entry, visual spec inconsistency, formatting gap |
| LOW | Stylistic inconsistency, minor formatting, rounding error |
| INFO | Observation, no action needed |

---

## Issues Found

### CRITICAL: None

No CRITICAL issues found. All 49 chapters present. No broken product decompositions. No missing chapters.

---

### HIGH (4 issues)

| ID | Phase | Description | Chapters Affected | Harmonization Action |
|:--:|:-----:|------------|:-----------------:|---------------------|
| H-01 | 1, 2 | 24 chapters have 16-section template instead of v1.3.1 22-section template | #1-23, #33 | Restructure each chapter from 16 sections to 22 sections per v1.3.1 |
| H-02 | 2 | 24 chapters missing Product DNA table (§4) and Who Touches table (§5) | #1-23, #33 | Add Product DNA and Who Touches to each chapter |
| H-03 | 2 | 37 chapters missing DNA Atlas fields | #1-37 | Add DNA Atlas fields block to each chapter's §4 |
| H-04 | 2 | 37 chapters missing Comparison Matrix fields | #1-37 | Add Comparison Matrix fields block to each chapter's §4 |

---

### MEDIUM (6 issues)

| ID | Phase | Description | Chapters Affected | Harmonization Action |
|:--:|:-----:|------------|:-----------------:|---------------------|
| M-01 | 1 | Missing `## 5.6` family header for Other family | 12 chapters (5.6.1-5.6.12) | Insert `## 5.6 OTHER STRUCTURED PRODUCTS` header before 5.6.1 |
| M-02 | 1 | 28 non-first-in-family chapters missing bridge text | 28 chapters | Add "How This Differs" bridge paragraph to each |
| M-03 | 1 | Two section header formats coexist (`#### N.` vs `#### §N.`) | 33 chapters use `N.`, 16 use `§N.` | Unify to one format (recommend `#### §N.` per v1.3.1) |
| M-04 | 2 | 17 chapters missing Visual Specifications (§21) | #1-16, #33 | Add 6 visual specs per chapter |
| M-05 | 3 | Visual template registry has 125 entries vs ~192 expected | Registry gap | Register missing visual templates |
| M-06 | 3 | Jargon watchlist covers Batches 4-10 only; Batches 0-3 not processed | ~30 missing terms | Backfill jargon entries from early chapters |

---

### LOW (2 issues)

| ID | Phase | Description | Impact | Action |
|:--:|:-----:|------------|--------|--------|
| L-01 | 3, 5 | Dashboard aggregate visual score (8.33) differs from recalculated (8.27) by 0.06 | No threshold impact | Recalculate using consistent method |
| L-02 | 5 | Pilot batch (Batch 0) visual scores (7.0) below 8.0 target | Historical | No action — pilot batch scores are pre-v1.3.1 baseline |

---

### INFO (3 observations)

| ID | Phase | Description |
|:--:|:-----:|------------|
| I-01 | 4 | 3 forward references found — all legitimate (FTD→NTD, FTD→CDO, Accumulator→Decumulator) |
| I-02 | 1 | Section name mapping between 16-section and 22-section templates is not 1:1 — harmonization requires content reorganisation, not just renumbering |
| I-03 | 6 | Publication identifier standard defined but not applied — correctly deferred to post-harmonization |

---

## Issue Summary

| Severity | Count | Harmonization Required |
|----------|:-----:|:---------------------:|
| CRITICAL | 0 | — |
| HIGH | 4 | YES — all HIGH issues are harmonization scope |
| MEDIUM | 6 | YES — all MEDIUM issues are harmonization scope |
| LOW | 2 | OPTIONAL |
| INFO | 3 | NO |
| **Total** | **15** | |

---

## Root Cause Analysis

All HIGH and MEDIUM issues stem from a single root cause: **framework evolution**. The v1.3.1 framework (22-section template with Product DNA, DNA Atlas, Comparison Matrix, Who Touches, Visual Specifications, bridge text) was adopted during Batch 6 generation. The 24 chapters generated under earlier framework versions (Batches 0-5 + CLN 5.5.1) were not retroactively updated to v1.3.1.

This is expected behaviour — the project plan explicitly defers harmonization to post-49/49 completion. The issues catalogued here are the harmonization scope, not defects.

---

*Issue Log completed 2026-06-21. 15 issues catalogued. Zero CRITICAL. READ-ONLY — no modifications made.*
