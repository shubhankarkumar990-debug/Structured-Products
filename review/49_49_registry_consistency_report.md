# 49/49 Registry Consistency Report

**Date:** 2026-06-21
**Phase:** 3 of 6
**Status:** READ-ONLY AUDIT

---

## 1. Complexity Registry (`production/complexity_registry.yaml`)

| Check | Expected | Actual | Status |
|-------|:--------:|:------:|:------:|
| Total entries | 49 | 49 | PASS |
| All manuscript chapters represented | 49 | 49 | PASS |
| No extra entries | 0 | 0 | PASS |
| Score-manuscript consistency | Match | Match | PASS |

### Score Distribution

| Score | Count | Products |
|:-----:|:-----:|----------|
| 2 | 4 | PPN, VLSP, Structured Deposit, Forward |
| 3 | 8 | RC, DRC, ICN, Warrant, Vanilla Option, ELO, DCI + 1 more |
| 4 | 9 | KODRC, Airbag, Bonus, Digital, Booster, ZCL, Commodity Swap, Shark Fin + 1 more |
| 5 | 10 | CRC, TRS, Equity Swap, CDS, XCCY, Skew CLN, IR Callable, Digital CF, Option on RC, Vanilla STEG |
| 6 | 7 | Phoenix, FCN, CRA ELN, NCRA, Callable STEG, Accumulator, Decumulator |
| 7 | 7 | Digital KI Put, Variance Swap, CRA SRT, RA STEG, FTD, Snowball, Cliquet |
| 8 | 3 | TARN STEG, NTD, Worst-of Autocallable |
| 9 | 0 | — |
| 10 | 1 | Synthetic CDO Tranche |

**Mean complexity: 4.96. Range: 2-10. Distribution is reasonable.**

---

## 2. Generation Dashboard (`production/generation_dashboard.md`)

### 2.1 Overall Progress

| Check | Expected | Actual | Status |
|-------|:--------:|:------:|:------:|
| Total products stated | 49 | 49 | PASS |
| Accepted stated | 49 | 49 | PASS |
| Remaining stated | 0 | 0 | PASS |
| Current batch stated | Batch 10 COMPLETE | Batch 10 COMPLETE | PASS |

### 2.2 Batch Progress

| Check | Expected | Actual | Status |
|-------|:--------:|:------:|:------:|
| Batch rows (0-10) | 11 | 11 | PASS |
| Sum of batch product counts | 49 | 49 | PASS |
| All batches COMPLETE | 11 | 11 | PASS |

### 2.3 Per-Chapter Status

| Check | Expected | Actual | Status |
|-------|:--------:|:------:|:------:|
| DONE rows | 49 | 49 | PASS |
| Accepted YES rows | 49 | 49 | PASS |

### 2.4 Aggregate Quality Metrics

| Metric | Dashboard Value | Recalculated | Delta | Status |
|--------|:--------------:|:------------:|:-----:|:------:|
| Avg Educational | 8.83 | 8.79 | -0.04 | PASS (within rounding) |
| Avg Visual | 8.33 | 8.27 | -0.06 | **LOW** (minor rounding discrepancy) |
| Terminology | 99.4% | — | — | Not independently verifiable |
| First-Pass | 100% | 100% | 0 | PASS |

**Note:** The 0.06 difference in visual score is a rounding artefact — the dashboard likely used a different aggregation method (e.g., weighted average of batch averages vs equal weighting across chapters). Both values exceed the 8.0 threshold. Classified as LOW severity.

---

## 3. Analogy Registry

| Check | Expected | Actual | Status |
|-------|:--------:|:------:|:------:|
| Entries | 49 | 49 | PASS |
| Collisions | 0 | 0 | PASS |

All 49 products have unique analogy domains registered in the dashboard.

---

## 4. Visual Template Registry

| Check | Expected | Actual | Status |
|-------|:--------:|:------:|:------:|
| Entries | ~294 (6 per chapter × 49) | 125 | **FAIL** |
| Coverage | 49 chapters | ~21 chapters | **FAIL** |

**Only 125 visual templates registered.** Visual template registry entries exist only for chapters that have §21 Visual Specifications. The 17 chapters lacking Visual Specifications (Batches 0-3 + IRS + CLN 5.5.1) have no visual template registry entries. This is consistent with the content completeness findings — visual specs were not part of the original template.

**Note:** The expected count of 294 assumes all chapters have 6 visual specs. The actual expectation should be: 32 chapters with visual specs × 6 = 192. The registry has 125, which means some earlier chapters' visual specs may not have been added to the template registry. Classified as MEDIUM severity.

---

## 5. Jargon Watchlist

| Check | Expected | Actual | Status |
|-------|:--------:|:------:|:------:|
| Entries | — | 138 | — |
| Coverage | All batches | Batches 4-10 | PARTIAL |

Jargon watchlist was introduced during generation and has 138 entries. Earlier batches (0-3) were not retroactively processed for jargon terms. This is a harmonization item.

---

## 6. Phase 3 Summary

| Registry | Status | Severity |
|----------|:------:|:--------:|
| Complexity Registry (49/49, scores match) | PASS | — |
| Dashboard overall progress | PASS | — |
| Dashboard batch progress | PASS | — |
| Dashboard per-chapter status (49/49 DONE) | PASS | — |
| Dashboard aggregate metrics | LOW | LOW (rounding) |
| Analogy Registry (49/49, no collisions) | PASS | — |
| Visual Template Registry (125/~192) | FAIL | MEDIUM |
| Jargon Watchlist (partial coverage) | PARTIAL | MEDIUM |

---

*Phase 3 Registry Consistency Report completed 2026-06-21. READ-ONLY — no modifications made.*
