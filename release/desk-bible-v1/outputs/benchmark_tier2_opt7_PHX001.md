# Tier 2 Optimization #7 — Schema Externalization Benchmark

## Prompt size: before vs after

| Agent | Before | After | Saved | % |
|---|---|---|---|---|
| sp-research-agent | 3,151 | 1,930 | 1,221 | 38.7% |
| sp-product-architect | 3,190 | 1,579 | 1,611 | 50.5% |
| sp-murex-mapping | 2,203 | 1,562 | 641 | 29.1% |
| sp-qa-agent | 3,843 | 3,491 | 352 | 9.2% |
| sp-crossref-agent | 3,698 | 3,142 | 556 | 15.0% |
| sp-style-agent | 3,363 | 1,778 | 1,585 | 47.1% |
| sp-publisher | 3,128 | 2,103 | 1,025 | 32.8% |
| sp-memory-agent | 5,980 | 3,815 | 2,165 | 36.2% |
| sp-content-writer | 2,598 | 2,344 | 254 | 9.8% |
| sp-example-generator | 2,625 | 1,642 | 983 | 37.4% |
| sp-reconciliation-generator | 3,178 | 2,658 | 520 | 16.4% |
| **Total** | **36,957** | **26,044** | **10,913** | **29.5%** |

## Tokens saved per agent

| Agent | Tokens saved |
|---|---|
| sp-memory-agent | 541 |
| sp-product-architect | 403 |
| sp-style-agent | 396 |
| sp-research-agent | 305 |
| sp-publisher | 256 |
| sp-example-generator | 246 |
| sp-murex-mapping | 160 |
| sp-crossref-agent | 139 |
| sp-reconciliation-generator | 130 |
| sp-qa-agent | 88 |
| sp-content-writer | 64 |
| **Per product total** | **2,728** |

## Schema files created

| File | Bytes | Tokens |
|---|---|---|
| schemas/writing-standards.yaml | 2,568 | 642 |
| schemas/memory-schemas.yaml | 2,448 | 612 |
| schemas/blueprint-output.yaml | 1,737 | 434 |
| schemas/style-rules.yaml | 1,487 | 372 |
| schemas/research-output.yaml | 1,341 | 335 |
| schemas/pubspec-output.yaml | 1,146 | 286 |
| schemas/booking-spec-output.yaml | 763 | 191 |
| schemas/crossref-review-output.yaml | 692 | 173 |
| schemas/style-review-output.yaml | 564 | 141 |
| schemas/qa-review-output.yaml | 469 | 117 |
| **Total** | **13,215** | **3,304** |

## Per-product impact

| Metric | First run | Incremental |
|---|---|---|
| Baseline (audit) | 110,408 | 110,408 |
| After Phase 1 | 96,677 | 95,096 |
| After Phase 1 + Tier 2 #7 | 93,949 | 92,368 |
| Tier 2 #7 savings | 2,728 | 2,728 |
| Cumulative savings | 16,459 | 18,040 |
| Cumulative reduction | 14.9% | 16.3% |

## At scale (27 products)

| Metric | Tokens |
|---|---|
| Tier 2 #7 savings | 73,656 |
| Cumulative total (1st run) | 2,536,623 |
| Cumulative total (incremental) | 2,493,936 |

## What changed

- 10 schema files created in `schemas/`
- 11 agent prompts reduced by 29.5% (10,913 bytes)
- Output schemas, style rules, and writing standards now loaded on-demand
- No agent behavior modified — same outputs, same gate conditions
