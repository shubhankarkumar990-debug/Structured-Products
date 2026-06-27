# Reference Layer Generation Sequence

**Date:** 2026-06-22
**Phase:** Reference Layer Readiness Review — Phase 5
**Scope:** Generation order authorization

---

## Recommended Generation Order

### 1. Product DNA Atlas (FIRST)

**Rationale:** The DNA Atlas is the foundational reference artifact. It consumes only the 12-field DNA table and 7 Atlas fields — no taxonomy normalization needed. Both the Comparison Matrix and Universe Map may reference Atlas entries. Generating it first establishes the canonical product identity layer.

**Dependencies:**
- Manuscript §4 DNA tables (49/49 present, 12 fields each)
- Manuscript §4 Atlas fields (49/49 present, 7 fields each)
- Complexity registry (for score verification)

**Downstream consumers:**
- Comparison Matrix (cross-references Atlas for product names)
- Universe Map (uses Atlas entries for node labels)

### 2. Product Comparison Matrix (SECOND)

**Rationale:** The Comparison Matrix requires the taxonomy to normalize 178 raw CM field variants into 30 canonical categories. It should be generated after the Atlas so cross-references are available, but before the Universe Map so the Map can embed matrix-derived positioning.

**Dependencies:**
- Manuscript §4 CM fields (49/49 present, 10 fields each)
- Publication taxonomy (6 dimensions, 49/49 mappings)
- Complexity registry (for score column)
- DNA Atlas (for product identity and naming)

**Downstream consumers:**
- Universe Map (uses matrix dimensions for multi-axis positioning)

### 3. Structured Products Universe Map (THIRD)

**Rationale:** The Universe Map is the most complex reference artifact. It synthesizes family groupings, complexity scores, evolution chains, dependency graphs, and optionally Comparison Matrix dimensions. Generating it last ensures all upstream data is available and validated.

**Dependencies:**
- Manuscript §4 DNA tables (family, complexity)
- Manuscript §6 Product Evolution (evolution arrows)
- Manuscript §22 Related Chapters (dependency edges)
- Atlas fields → Similar Products (cross-reference edges)
- Complexity registry (positioning)
- DNA Atlas (node data)
- Comparison Matrix (optional multi-dimensional positioning)

**Downstream consumers:** None (terminal reference artifact)

---

## Dependency Graph

```
Manuscript (49 chapters)
    ├── §4 DNA Table ──────────────────┐
    ├── §4 Atlas Fields ───────────────┤
    │                                  ▼
    │                         ┌─────────────────┐
    │                         │  1. DNA Atlas    │
    │                         └────────┬────────┘
    │                                  │
    ├── §4 CM Fields ──────────────────┤
    │                                  │
    │   Taxonomy ──────────────────────┤
    │                                  ▼
    │                         ┌─────────────────┐
    │                         │ 2. Comparison   │
    │                         │    Matrix        │
    │                         └────────┬────────┘
    │                                  │
    ├── §6 Evolution ──────────────────┤
    ├── §22 Dependencies ──────────────┤
    │                                  │
    │   Registry ──────────────────────┤
    │                                  ▼
    │                         ┌─────────────────┐
    │                         │ 3. Universe Map  │
    │                         └─────────────────┘
```

---

## Generation Order Authorization

| Order | Artifact | Status | May Begin After |
|:-----:|----------|:------:|-----------------|
| 1 | Product DNA Atlas | **AUTHORIZED** | Verdict approval |
| 2 | Product Comparison Matrix | **AUTHORIZED** | DNA Atlas complete |
| 3 | Structured Products Universe Map | **AUTHORIZED** | Comparison Matrix complete |

Sequential execution recommended. Each artifact validates its upstream before starting.

---

*Phase 5 complete.*
