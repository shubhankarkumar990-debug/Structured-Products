# Release Dependency Manifest — SP-KE-V1.0

**Version**: 1.0
**Date**: 2026-06-27
**Purpose**: Canonical dependency graph for all production artifacts

---

## Dependency Matrix

### 1. Desk Bible V2 (`Desk_Bible_v2.md`)

| Relationship | Artifact | Nature |
|:------------:|----------|--------|
| DEPENDS-ON | Framework Master V1.3.1 | Chapter template (22-section structure) |
| DEPENDS-ON | Complexity Registry | Complexity scores in §4 Product DNA |
| DEPENDS-ON | Publication Taxonomy | Categorical values in §4 Product DNA |
| DEPENDS-ON | Jargon Watchlist | Controlled vocabulary enforcement |
| DEPENDS-ON | Visual Standard | Diagram specifications |
| DEPENDS-ON | Professor Voice Standard | Authorial voice |
| DEPENDS-ON | Publication Architecture | Document structure |
| DEPENDS-ON | Publication Identifier Standard | Section numbering (§5.x.y) |
| USED-BY | Interview System V2.2 | Questions derived from chapter content |
| USED-BY | Solutions Manual | Structuring decisions reference chapters |
| USED-BY | Product DNA Atlas | Fields extracted from §4 Product DNA |
| USED-BY | Infrastructure Encyclopedia | Cross-referenced by §6 entries |

### 2. Infrastructure Encyclopedia V1.0 (`production/infrastructure_encyclopedia_v1.md`)

| Relationship | Artifact | Nature |
|:------------:|----------|--------|
| DEPENDS-ON | Desk Bible V2 | Content source (Part 6) |
| DEPENDS-ON | Publication Identifier Standard | Entry numbering |
| USED-BY | Interview System V2.2 | Infrastructure questions reference entries |

### 3. Product DNA Atlas (`production/product_dna_atlas.md`)

| Relationship | Artifact | Nature |
|:------------:|----------|--------|
| DEPENDS-ON | Desk Bible V2 | §4 Product DNA fields extracted |
| DEPENDS-ON | Complexity Registry | Canonical scores |
| DEPENDS-ON | Publication Taxonomy | Family assignments, categorical values |
| USED-BY | Product Comparison Matrix | Comparison dimensions from DNA fields |
| USED-BY | Product Universe Map | Node attributes |
| USED-BY | Learning Dependency Graph | Complexity tiers from scores |
| USED-BY | Product Evolution Map | Family trees from DNA Evolves-From |

### 4. Interview System V2.2 (`production/interview_system_v2_2.md`)

| Relationship | Artifact | Nature |
|:------------:|----------|--------|
| DEPENDS-ON | Desk Bible V2 | Question content sourced from chapters |
| DEPENDS-ON | Infrastructure Encyclopedia | Infrastructure question content |
| DEPENDS-ON | Complexity Registry | Complexity scores in question metadata |
| DEPENDS-ON | Question Identifier Standard | Question ID format |
| USED-BY | (standalone consumer artifact) | |

### 5. Solutions Manual (`production/solutions_manual.md`)

| Relationship | Artifact | Nature |
|:------------:|----------|--------|
| DEPENDS-ON | Desk Bible V2 | Product knowledge for structuring scenarios |
| DEPENDS-ON | Complexity Registry | Complexity-based scenario difficulty |
| USED-BY | (standalone consumer artifact) | |

### 6. Framework Master V1.3.1 (`production/framework_master_v1.3.1.md`)

| Relationship | Artifact | Nature |
|:------------:|----------|--------|
| DEPENDS-ON | (root artifact — no dependencies) | |
| USED-BY | Desk Bible V2 | Governing template |
| USED-BY | Chapter Acceptance Checklist | Compliance criteria |
| USED-BY | Framework Validation V1.3.1 | Validation target |

### 7. Product Universe Map (`production/product_universe_map.md`)

| Relationship | Artifact | Nature |
|:------------:|----------|--------|
| DEPENDS-ON | Product DNA Atlas | Node attributes |
| DEPENDS-ON | Learning Dependency Graph | Prerequisite edges |
| DEPENDS-ON | Product Evolution Map | Evolution edges |
| DEPENDS-ON | Product Comparison Matrix | Comparison dimensions |
| USED-BY | (standalone navigation artifact) | |

### 8. Product Comparison Matrix (`production/product_comparison_matrix.md`)

| Relationship | Artifact | Nature |
|:------------:|----------|--------|
| DEPENDS-ON | Product DNA Atlas | Product attributes |
| DEPENDS-ON | Complexity Registry | Complexity column |
| DEPENDS-ON | Publication Taxonomy | Family, market columns |
| USED-BY | Product Universe Map | Comparison dimension |

### 9. Learning Dependency Graph (`production/learning_dependency_graph.md`)

| Relationship | Artifact | Nature |
|:------------:|----------|--------|
| DEPENDS-ON | Product DNA Atlas | Node attributes |
| DEPENDS-ON | Complexity Registry | Tier assignments (score-based) |
| USED-BY | Product Universe Map | Prerequisite edges |

### 10. Product Evolution Map (`production/product_evolution_map.md`)

| Relationship | Artifact | Nature |
|:------------:|----------|--------|
| DEPENDS-ON | Product DNA Atlas | Evolves-From field |
| DEPENDS-ON | Publication Taxonomy | Family assignments |
| USED-BY | Product Universe Map | Evolution edges |

### 11. Complexity Registry (`production/complexity_registry.yaml`)

| Relationship | Artifact | Nature |
|:------------:|----------|--------|
| DEPENDS-ON | (root artifact — canonical authority) | |
| USED-BY | Desk Bible V2 | §4 Product DNA scores |
| USED-BY | Product DNA Atlas | Score field |
| USED-BY | Interview System V2.2 | Score metadata |
| USED-BY | Learning Dependency Graph | Tier assignments |
| USED-BY | Product Comparison Matrix | Complexity column |
| USED-BY | Solutions Manual | Scenario difficulty |

### 12. Publication Taxonomy (`production/publication_taxonomy.yaml`)

| Relationship | Artifact | Nature |
|:------------:|----------|--------|
| DEPENDS-ON | (root artifact — canonical authority) | |
| USED-BY | Desk Bible V2 | §4 Product DNA categories |
| USED-BY | Product DNA Atlas | Category fields |
| USED-BY | Product Comparison Matrix | Family/market columns |
| USED-BY | Product Evolution Map | Family assignments |

### 13. Jargon Watchlist (`production/jargon_watchlist.md`)

| Relationship | Artifact | Nature |
|:------------:|----------|--------|
| DEPENDS-ON | (root artifact — canonical authority) | |
| USED-BY | Desk Bible V2 | Vocabulary enforcement |

---

## Dependency Statistics

| Metric | Value |
|--------|:-----:|
| Total artifacts | 13 |
| Root artifacts (no dependencies) | 3 |
| Leaf artifacts (no dependents) | 2 |
| Maximum dependency depth | 3 |
| Total dependency edges | 37 |

### Root Artifacts (no upstream dependencies)
1. Framework Master V1.3.1
2. Complexity Registry
3. Publication Taxonomy

### Leaf Artifacts (no downstream dependents)
1. Interview System V2.2
2. Solutions Manual

### Critical Path
`Framework Master → Desk Bible → Product DNA Atlas → Product Universe Map`

### Highest Fan-Out (most dependents)
1. Complexity Registry — 6 dependents
2. Desk Bible V2 — 5 dependents
3. Product DNA Atlas — 4 dependents

### Highest Fan-In (most dependencies)
1. Product Universe Map — 4 dependencies
2. Interview System V2.2 — 4 dependencies
3. Product Comparison Matrix — 4 dependencies

---

## Circular Dependency Check

**Result**: PASS — No circular dependencies detected.

The dependency graph is a directed acyclic graph (DAG) with clear layering:
- Layer 0: Root artifacts (Framework, Registry, Taxonomy, Jargon, Voice, Visual, Pub Arch, Pub ID)
- Layer 1: Desk Bible (depends on Layer 0)
- Layer 2: Atlas, Encyclopedia, Interview, Solutions (depend on Layer 1)
- Layer 3: Comparison Matrix, Dep Graph, Evolution Map (depend on Layer 2)
- Layer 4: Universe Map (depends on Layer 3)

---

*Release Dependency Manifest — SP-KE-V1.0 — Generated 2026-06-27*
