# Phase 1 Benchmark Report — PHX001 (Phoenix Autocallable)

## Baseline (Phase C audit)

| Metric | Value |
|---|---|
| Total tokens per product (FULL mode) | 110,408 |
| Estimated runtime | ~35 min |
| Total for 27 products | 2,981,016 |

---

## Optimization Results

### Opt 1: Orchestrator Prompt Deduplication

| Metric | Before | After |
|---|---|---|
| Orchestrator spec | 2,213 tokens | 1,377 tokens |
| Loaded per product | ×13 interactions | ×13 interactions |
| Stage briefings | (inline) | +1,486 tokens (8 files, once each) |
| **Subtotal** | **28,769 tokens** | **19,387 tokens** |
| **Savings** | | **9,382 tokens (8.5%)** |

### Opt 2: Publisher Input Reduction

| Metric | Before | After |
|---|---|---|
| Publisher reads | catalog.yaml (890 tokens) | insertion_metadata (66 tokens) |
| **Savings** | | **824 tokens (0.7%)** |

### Opt 3: QA Scope Reduction

| Scenario | Before | After | Savings |
|---|---|---|---|
| First run (no hashes) | full draft (2,851 tokens) | full draft (all sections new) | 0 |
| Incremental (3/8 changed) | full draft (2,851 tokens) | 3/8 draft (1,069) + scope (201) | **1,581 (1.4%)** |

### Opt 4: CrossRef Partial Reads

| Metric | Before | After |
|---|---|---|
| CrossRef reads | draft (2,851) + catalog (890) = 3,741 tokens | refs file only = 216 tokens |
| Lines processed | 56 lines (full draft) | 2 reference lines (96% reduction) |
| **Savings** | | **3,525 tokens (3.2%)** |

---

## Summary

| Optimization | First Run | Incremental |
|---|---|---|
| Orchestrator dedup | 9,382 | 9,382 |
| Publisher input | 824 | 824 |
| QA scope | 0 | 1,581 |
| CrossRef reads | 3,525 | 3,525 |
| **Total savings** | **13,731** | **15,312** |
| **After total** | **96,677** | **95,096** |
| **Reduction** | **12.4%** | **13.9%** |

## Runtime

| Metric | First Run | Incremental |
|---|---|---|
| Before | ~35 min | ~35 min |
| After (est.) | ~32.0 min | ~31.6 min |

## At Scale (27 products)

| Scenario | Tokens | Saved |
|---|---|---|
| Before | 2,981,016 | — |
| After (first run) | 2,610,279 | 370,737 |
| After (incremental) | 2,567,592 | 413,424 |

---

## Artifacts Generated

| File | Size | Purpose |
|---|---|---|
| `agents/stage-briefings/stage-{1-8}-*.yaml` | 5,948 bytes total | Per-stage inputs/outputs/gates |
| `outputs/crossref/PHX001_refs.yaml` | 862 bytes | Pre-extracted reference lines |
| `outputs/publish/PHX001_insertion.yaml` | 264 bytes | Insertion point metadata |
| `outputs/reviews/PHX001_qa_scope.yaml` | 804 bytes | Section hashes + change manifest |
| `checkpoints/PHX001.json` | 2,374 bytes | Updated with section_hashes |

## Notes

1. All measurements use actual file sizes (bytes ÷ 4 = tokens).
2. Orchestrator deduplication is the dominant saving (8.5%) — confirmed the Phase C audit ranking.
3. CrossRef 96% line reduction validates the reference extraction protocol.
4. QA scope reduction has zero first-run benefit by design — it pays off on edit cycles.
5. Phase 1 covers Tier 1 only. Tier 2/3 optimizations remain available (est. additional 40%).
