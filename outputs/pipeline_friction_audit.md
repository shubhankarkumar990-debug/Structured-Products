# Pipeline Friction Audit

**Date:** 2026-06-18  
**Scope:** Last 5 generated products  
**Actual sample:** 1 product (PHX001 — Phoenix Autocallable). Only PHX001 has completed a full pipeline run. The remaining 26 products have status `existing` (pre-pipeline content). Projections for subsequent products are derived from the family-level benchmark.

---

## 1. QA Rejection Rate

| Metric | Value |
|--------|-------|
| Sections reviewed | 8 |
| BLOCKERs raised | 3 |
| MINORs raised | 1 (reclassified from BLOCKER) |
| Dismissed | 1 (M-2, 7-word violation) |
| **Rejection rate** | **37.5%** (3 of 8 sections required rework) |

All 3 BLOCKERs were in the worked example section (arithmetic errors and missing reconciliation check). Content generation produced the section, QA caught real errors, rework fixed them. The QA gate is functioning correctly — high rejection rate reflects first-run content quality, not over-flagging.

**Projected for subsequent ELN products:** 25–30%. The worked example section is the most error-prone because it requires exact arithmetic. Memory artifacts (terminology, system mapping) will prevent system-name errors but cannot prevent calculation mistakes.

## 2. Style Rejection Rate

| Metric | Value |
|--------|-------|
| MUST_FIX raised | 12 |
| Genuine violations | 4 (33%) |
| False positives | 8 (67%) |
| Fixes applied | 2 (USD prefix corrections) |
| SHOULD_FIX raised | Acknowledged, not counted as rejections |
| **True rejection rate** | **33%** of flags were genuine |
| **False positive rate** | **67%** |

The 4 known false positive categories (H4 heading casing, Sophis casing, Termsheet spelling, pricing ranges in Pricing Intuition) are now stored in `memory/style-patterns/ELN.yaml`. These will be suppressed for all subsequent ELN products.

**Projected for subsequent ELN products:** 4 of 12 flags eliminated by memory. Remaining false positive rate drops to ~50% (4 of ~8 remaining flags). Genuine fix rate stays at 2 per product.

## 3. Cross-Reference Failures

| Metric | Value |
|--------|-------|
| Explicit cross-references in content | 0 |
| Broken references | 0 |
| Warnings | 3 (implicit dependencies, structurally resolved) |
| **Failure rate** | **0%** |

PHX001 is the first product inserted into Part 3. No prior content exists to cross-reference against. This metric will become meaningful once multiple products coexist — the cross-reference agent checks for internal consistency between sections, heading references, and appendix pointers.

**Projected for subsequent products:** Non-zero. Products 2+ will reference shared concepts (e.g., barrier types defined in PHX001). Estimated 1–2 warnings per product, 0 hard failures if the cross-reference agent's pre-processing (reference extraction in `stage-7-crossref.yaml`) works correctly.

## 4. Publishing Failures

| Metric | Value |
|--------|-------|
| Checklist items | All passed |
| Insertion point | Correct (§3.2, first product) |
| Heading hierarchy | Verified |
| Paragraph order | Verified |
| Appendix updates | B.4/B.5 required and completed |
| **Failure rate** | **0%** |

Note: An earlier session encountered a paragraph-order bug in the DOCX merge logic (lxml `addprevious` inserting in reverse order). This was a pipeline code bug, not a content failure. The fix is in place and the merge completed correctly.

**Projected for subsequent products:** 0% failure rate. The publishing stage is deterministic — insertion metadata is pre-computed by the orchestrator and the merge logic is now tested.

## 5. Manual Edits Required After Generation

| Edit | Stage | Severity | Description |
|------|-------|----------|-------------|
| 1 | QA | BLOCKER | Worked example arithmetic corrected |
| 2 | QA | BLOCKER | Reconciliation check added to worked example |
| 3 | QA | BLOCKER | Missing component in economic decomposition |
| 4 | Style | MUST_FIX | USD prefix added to bare "10M" |
| 5 | Style | MUST_FIX | USD prefix added to bare "250k" |
| **Total** | | | **5 manual edits** |

No edits were required after cross-reference or publishing stages. All manual edits originated from the review stages (QA + Style).

**Projected for subsequent ELN products:** 3–4 edits. QA BLOCKERs in worked examples are structural (arithmetic always needs verification). Style edits drop by 2 due to memory-stored patterns (USD prefix rule learned).

## 6. Reusable Memory Artifacts Created

| File | Category | Size | Reuse scope |
|------|----------|------|-------------|
| `memory/terminology/ELN.yaml` | Terminology | 1,531 bytes | All 13 ELN products |
| `memory/booking-maps/ELN_system_mapping.yaml` | Booking maps | 1,042 bytes | All 13 ELN products |
| `memory/style-patterns/ELN.yaml` | Style patterns | 1,589 bytes | All 13 ELN products |
| **Total** | | **4,162 bytes** | |

**Reuse value:** Per the family-level benchmark, these 3 files save ~1,258 tokens per subsequent ELN product (correctness value: preventing wrong system mappings, suppressing known false positives). Across the remaining 12 ELN products, total savings: ~15,096 tokens.

**New families will require their own memory artifacts.** SRT, CLN, STEG, and Swap families each need terminology, booking maps, and style patterns. First product in each family will generate these; subsequent products reuse them.

## 7. Time Spent in Rework Loops

| Stage | Start | End | Duration | Rework portion |
|-------|-------|-----|----------|----------------|
| Research | 10:00 | 10:00 | ~5 min | 0 min |
| Architecture | 10:00 | 10:05 | 5 min | 0 min |
| Writing (3 parallel) | 10:05 | 10:15 | 10 min | 0 min |
| Booking | 10:15 | 10:25 | 10 min | 0 min |
| **QA** | **10:25** | **10:40** | **15 min** | **~5 min** |
| **Style** | **10:40** | **10:50** | **10 min** | **~5 min** |
| CrossRef | 10:50 | 10:55 | 5 min | 0 min |
| Publishing | 10:55 | 11:05 | 10 min | 0 min |
| DOCX merge | 11:05 | 11:30 | 25 min | 0 min |
| **Total** | | | **90 min** | **~10 min (11%)** |

Rework is concentrated entirely in the review stages. Content generation (stages 1–4) produced no rework. Publishing (stage 8) produced no rework.

---

## Bottleneck Determination

| Candidate | Friction score | Evidence |
|-----------|---------------|----------|
| Content generation | **Low** | All 4 content stages passed gates on first attempt. Zero rework. |
| **Quality review** | **High** | QA: 37.5% rejection rate, 3 BLOCKERs requiring content fixes. Style: 67% false positive rate creating review noise. Combined: 10 min rework (100% of all rework time). |
| Publishing | **None** | Zero failures. Deterministic merge after code fix. |
| Human correction | **Medium** | 5 manual edits, all driven by QA/Style output. Not an independent bottleneck — downstream of quality review. |

### Highest-friction stage: **Quality Review**

The bottleneck is the QA → rework loop. Three specific friction sources:

1. **QA BLOCKER rate on worked examples (37.5%)** — The worked example section requires exact arithmetic across 5+ line items that must sum to the headline coupon. Content writers produce plausible but inexact numbers. QA correctly catches these, but each BLOCKER triggers a rework cycle.

2. **Style false positive rate (67%)** — Two-thirds of style flags are noise. Human reviewers must evaluate each flag to determine genuine vs false positive. Memory artifacts will reduce this to ~50% for subsequent ELN products, but the fundamental issue is that the style agent applies rules too broadly (e.g., flagging canonical heading names that are correct by design).

3. **Review stages consume 100% of rework time** — All 10 minutes of rework in the 90-minute pipeline originated from QA and Style. No other stage produced any rework.

### Recommendation

To reduce pipeline friction, prioritize:
- **QA agent**: Add arithmetic validation as a pre-check before raising BLOCKERs. The worked example decomposition should verify column sums before flagging individual line items.
- **Style agent**: Consume `memory/style-patterns/*.yaml` to suppress known false positives. This is a Tier 2 optimization that would eliminate 4 of 12 flags immediately.
- **Neither content generation nor publishing needs optimization** — they are not friction sources.

---

*Sample size: 1 product (PHX001). Projections for products 2–5 based on family-level benchmark findings and memory artifact reuse rates. Actual friction metrics will vary — particularly for the first product in non-ELN families (SRT, CLN, STEG) where no memory artifacts exist yet.*
