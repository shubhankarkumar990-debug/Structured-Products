# Dependency Manifest (Final) — SP-KE-V1.0

**Date**: 2026-06-27
**Purpose**: Definitive upstream/downstream dependency map for all canonical artifacts

---

## Artifact DAG

```
Layer 0 (Root — no upstream dependencies):
  ├── Framework Master V1.3.1
  ├── Complexity Registry
  ├── Publication Taxonomy
  └── Jargon Watchlist

Layer 1 (depends on Layer 0):
  └── Desk Bible V2
        depends-on: Framework, Registry, Taxonomy, Jargon, Visual Std, Voice Std, Pub Arch, Pub ID Std

Layer 2 (depends on Layer 1):
  ├── Infrastructure Encyclopedia
  │     depends-on: Desk Bible
  ├── Product DNA Atlas
  │     depends-on: Desk Bible, Registry, Taxonomy
  ├── Interview System V2.2
  │     depends-on: Desk Bible, Encyclopedia, Registry
  └── Solutions Manual
        depends-on: Desk Bible, Registry

Layer 3 (depends on Layer 2):
  ├── Product Comparison Matrix
  │     depends-on: Atlas, Registry, Taxonomy
  ├── Learning Dependency Graph
  │     depends-on: Atlas, Registry
  └── Product Evolution Map
        depends-on: Atlas, Taxonomy

Layer 4 (depends on Layer 3):
  └── Product Universe Map
        depends-on: Atlas, Dep Graph, Evo Map, Comparison Matrix
```

---

## Dependency Matrix

| Artifact | Upstream Dependencies | Downstream Consumers | Layer | Safe to Edit? |
|----------|:--------------------:|:--------------------:|:-----:|:-------------:|
| Framework Master V1.3.1 | 0 | 1 (Bible) | 0 | NO (frozen) |
| Complexity Registry | 0 | 6 | 0 | NO (frozen, highest fan-out) |
| Publication Taxonomy | 0 | 4 | 0 | NO (frozen) |
| Jargon Watchlist | 0 | 1 (Bible) | 0 | NO (frozen) |
| Desk Bible V2 | 4+ | 5 | 1 | NO (frozen, highest impact) |
| Infrastructure Encyclopedia | 1 | 1 | 2 | NO (frozen) |
| Product DNA Atlas | 3 | 4 | 2 | NO (frozen, hub artifact) |
| Interview System V2.2 | 3 | 0 | 2 | NO (frozen, leaf) |
| Solutions Manual | 2 | 0 | 2 | NO (frozen, leaf) |
| Product Comparison Matrix | 3 | 1 | 3 | NO (frozen) |
| Learning Dependency Graph | 2 | 1 | 3 | NO (frozen) |
| Product Evolution Map | 2 | 1 | 3 | NO (frozen) |
| Product Universe Map | 4 | 0 | 4 | NO (frozen, leaf) |

---

## Critical Cascade Paths

If any of these artifacts were modified (which is prohibited), the following would need updating:

### Complexity Registry (6 downstream)
```
Registry → Desk Bible (§4 DNA scores)
         → Atlas (score field)
         → Interview System (score metadata)
         → Dep Graph (tier assignments)
         → Comparison Matrix (complexity column)
         → Solutions Manual (difficulty)
```

### Desk Bible (5 downstream)
```
Bible → Atlas (DNA fields)
      → Encyclopedia (Part 6 content)
      → Interview System (question content)
      → Solutions Manual (product knowledge)
      → [indirect] → Universe Map, Matrix, Dep Graph, Evo Map
```

### Product DNA Atlas (4 downstream)
```
Atlas → Comparison Matrix (product attributes)
      → Dep Graph (node attributes)
      → Evo Map (evolves-from field)
      → Universe Map (node attributes)
```

---

## Governance Artifact Dependencies

| Governance Artifact | Governs |
|---------------------|---------|
| Framework Master V1.3.1 | Desk Bible chapter structure |
| Visual Standard | All visual assets |
| Professor Voice Standard | All prose content |
| Publication Architecture | Document structure |
| Publication Identifier Standard | Section numbering |
| Question Identifier Standard | Interview question IDs |
| Chapter Acceptance Checklist | Chapter quality gates |
| Review Workflow | Editorial process |
| Framework Freeze Notice | Framework changeability |

---

## Statistics

| Metric | Value |
|--------|:-----:|
| Total canonical artifacts | 13 |
| Root artifacts (0 upstream) | 4 |
| Leaf artifacts (0 downstream) | 3 |
| Maximum DAG depth | 4 layers |
| Total dependency edges | 37 |
| Highest fan-out | Complexity Registry (6) |
| Highest fan-in | Product Universe Map (4) |
| Circular dependencies | 0 (verified) |

---

*Dependency Manifest (Final) — SP-KE-V1.0 — Generated 2026-06-27*
