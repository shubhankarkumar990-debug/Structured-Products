# Desk Bible Progress Dashboard

**Last updated:** 2026-06-18T17:40Z  
**Pipeline version:** v2.1 (post production-readiness improvements)  
**Updated after:** Batch 1 (5 ELN products)

---

## Overall Progress

| Metric | Count |
|--------|------:|
| Total products in catalog | 28 |
| Products completed | 11 |
| Products in progress | 0 |
| Products requiring review | 0 |
| Products remaining | 17 |

**Progress: 11 / 28 (39.3%)**

```
[███████████░░░░░░░░░░░░░░░░░░░] 39.3%
```

---

## Family Progress

| Family | Total | Complete | Remaining | % Complete |
|--------|------:|---------:|----------:|-----------:|
| ELN | 13 | 8 | 5 | 61.5% |
| SRT | 5 | 1 | 4 | 20.0% |
| CLN | 5 | 1 | 4 | 20.0% |
| STEG | 4 | 0 | 4 | 0.0% |
| Swap | 1 | 1 | 0 | 100.0% |
| Deposit | 0 | 0 | 0 | — |

### Completed products by family

**ELN (8/13):** PHX001 (Phoenix Autocallable), RC001 (Reverse Convertible), DRC001 (Discounted Reverse Convertible), KODRC001 (Knock-Out Discounted RC), CRC001 (Callable Reverse Convertible), AIRBAG001 (Airbag / Leveraged RC), FCN001 (Fixed Coupon Note), CRAELN001 (Callable Range Accrual ELN)

**SRT (1/5):** IRCFRN001 (IR Callable Fixed Rate Note)

**CLN (1/5):** VCLN001 (Vanilla CLN)

**Swap (1/1):** SWAP001 (Vanilla Interest Rate Swap)

**STEG (0/4):** —

**Deposit (0/0):** No products in catalog yet.

---

## Batch History

| Batch | Products | Runtime | Tokens (est.) | QA BLOCKERs | QA MAJORs | Style MUST_FIX | Pub failures |
|------:|----------|--------:|--------------:|------------:|----------:|---------------:|-------------:|
| 0 | PHX001, RC001, DRC001, VCLN001, IRCFRN001, SWAP001 | ~165 min | ~89,196 | 3 (v1) → 0 (v2) | 8 | 3 (v1) → 0 (v2) | 0 |
| 1 | KODRC001, CRC001, AIRBAG001, FCN001, CRAELN001 | ~95 min | ~74,330 | 0 | 6 | 0 | 0 |

### Batch 1 detail

- **Products:** 5 (all ELN family)
- **Sections completed:** 3.1 (all 5 RC variants), 3.2 (all 3 autocallable variants)
- **New memory artifacts created:** 0 (all ELN artifacts reused from Batch 0)
- **Memory reuses:** 15 (3 per product × 5 products)
- **Pipeline version:** v2.1 (stable, no changes)
- **Zero BLOCKERs, zero MUST_FIX, zero broken cross-refs, zero publishing failures**

---

## Quality Metrics

Running totals (v2.1 — post improvements):

| Metric | Batch 0 | Batch 1 | Cumulative |
|--------|--------:|--------:|-----------:|
| QA BLOCKERs | 0 | 0 | 0 |
| QA MAJORs | 8 | 6 | 14 |
| QA MINORs | 5 | 5 | 10 |
| Style MUST_FIX | 0 | 0 | 0 |
| Style SHOULD_FIX | 3 | 2 | 5 |
| Style FPs skipped | 14 | 15 | 29 |
| Style conventions skipped | 8 | 5 | 13 |
| Cross-reference warnings | 3 | 5 | 8 |
| Cross-reference broken | 0 | 0 | 0 |
| Publishing failures | 0 | 0 | 0 |

### QA issue breakdown (Batch 1)

| Issue type | Count | Products affected |
|------------|------:|-------------------|
| Decomposition presentation ambiguity | 5 | All 5 products |
| Model reference (advisory) | 1 | KODRC001 |
| Barrier convention (advisory) | 1 | FCN001 |
| Leverage explanation (advisory) | 1 | AIRBAG001 |
| Sensitivity range (advisory) | 1 | CRC001 |
| Boundary touch estimate | 1 | CRAELN001 |

### Style issue breakdown (Batch 1)

| Issue type | Count | Products affected |
|------------|------:|-------------------|
| Product naming consistency | 1 | KODRC001 |
| Product abbreviation suggestion | 1 | CRC001 |
| Genuine violations requiring content change | 0 | None |

---

## Memory Metrics

| Metric | Count |
|--------|------:|
| Memory artifacts created (total) | 12 |
| Memory artifacts created (Batch 1) | 0 |
| Memory artifacts reused (Batch 1) | 15 |
| Memory artifacts reused (cumulative) | 21 |
| Accepted conventions (total) | 12 |
| False positives avoided (cumulative) | 42 |

### Memory files by family

| Family | Terminology | Booking maps | Style patterns | Total |
|--------|:-----------:|:------------:|:--------------:|------:|
| ELN | ✓ | ✓ | ✓ | 3 |
| CLN | ✓ | ✓ | ✓ | 3 |
| SRT | ✓ | ✓ | ✓ | 3 |
| Swap | ✓ | ✓ | ✓ | 3 |
| STEG | — | — | — | 0 |
| Deposit | — | — | — | 0 |

---

## Risk Register

| Product ID | Reason | Severity | Recommended action |
|------------|--------|----------|-------------------|
| — | No products require review | — | — |

No products are currently flagged as REVIEW_REQUIRED. All 11 completed products passed all gates cleanly.

### Potential risks for future batches

| Risk | Likelihood | Impact | Mitigation |
|------|-----------|--------|------------|
| STEG products require new memory artifacts | Certain | Low | First STEG product creates memory; subsequent reuse |
| Cross-reference density increasing | Likely | Medium | 8 warnings in 11 products — manageable |
| Exotic CLN products (FTD, NTD, Tranches) more complex | Likely | Medium | Arithmetic verification protocol handles complexity |

---

## Forecast

| Metric | Value |
|--------|-------|
| Remaining products | 17 |
| Estimated tokens per product | ~14,866 |
| Estimated remaining tokens | ~252,722 |
| Products per batch (recommended) | 5 |
| Remaining batches | ~3–4 |
| Estimated remaining runtime | ~4–5 sessions |

### Recommended batch sequence

| Batch | Products | Family | Rationale |
|------:|----------|--------|-----------|
| 2 | BONUS001, PPN001, WARRANT001, ICN001, DIGITAL001 | ELN | Complete all remaining ELN (section 3.3) |
| 3 | AFRN001, NCRA001, CRASRT001, DCFN001, VSTEG001 | SRT + STEG | First STEG — new memory needed |
| 4 | RASTEG001, CSTEG001, TARN001, SCLN001, FTD001 | STEG + CLN | Complete STEG + start exotic CLN |
| 5 | NTD001, TRANCHE001 | CLN | Complete CLN |

*Batch sizes and sequence are recommendations. Adjust based on review findings.*
