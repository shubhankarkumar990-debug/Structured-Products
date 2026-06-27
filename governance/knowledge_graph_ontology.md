# KNOWLEDGE GRAPH / ONTOLOGY DESIGN

**Ecosystem:** Structured Products Knowledge Ecosystem  
**Version:** V1.0.1-GOV-1.0  
**Effective:** 2026-06-27  
**Purpose:** Structured graph supporting automated validation, retrieval, search, traversal, relationship checking, AI tutoring, and release diffing.

---

## Design Principles

1. Every entity has a stable ID that persists across versions
2. Every relationship is typed and directional
3. The graph must support: "show me everywhere concept X appears and whether each instance is correct"
4. Schema supports both current state and version history
5. All node/edge types are extensible without schema migration

---

## NODE TYPES

### N-PRODUCT: Product

| Property | Type | Required | Description |
|----------|------|:--------:|-------------|
| `id` | string | ✅ | Format: `PROD-{FAMILY}-{CODE}` (e.g., `PROD-ELN-RC001`) |
| `name` | string | ✅ | Display name (e.g., "Reverse Convertible") |
| `family` | enum | ✅ | ELN / Swap / SRT / STEG / CLN / Other |
| `complexity` | integer | ✅ | 1-10 from complexity registry |
| `system` | enum | ✅ | NEMO / Sophis / Murex |
| `correlation_direction` | enum | ✅ | LONG / SHORT / N_A (investor MTM convention) |
| `status` | enum | ✅ | CANONICAL / DEPRECATED |
| `desk_bible_section` | string | ✅ | Section reference in Desk Bible |
| **Validation** | | | `complexity` ∈ [1,10]. `family` must match complexity registry. |

### N-TERM: Governed Term

| Property | Type | Required | Description |
|----------|------|:--------:|-------------|
| `id` | string | ✅ | Format: `TERM-{CATEGORY}-{SEQ}` (e.g., `TERM-COR-01`) |
| `name` | string | ✅ | Display name (e.g., "long correlation") |
| `canonical_meaning` | string | ✅ | One-line canonical definition |
| `has_alternate` | boolean | ✅ | Whether an alternate convention exists |
| `alternate_meaning` | string | ❌ | If `has_alternate` = true |
| `required_qualifier` | string | ❌ | Qualifier text when alternate is used |
| `governance_rule_id` | string | ✅ | Linked T-XXX-XX ID from terminology spec |
| `severity` | enum | ✅ | S1 / S2 / S3 / S4 |
| **Validation** | | | If `has_alternate` = true, `alternate_meaning` and `required_qualifier` must be non-null. |

### N-CONVENTION: Convention Entry

| Property | Type | Required | Description |
|----------|------|:--------:|-------------|
| `id` | string | ✅ | Format: `CON-{SEQ}` (e.g., `CON-01`) |
| `concept` | string | ✅ | What has multiple valid conventions |
| `canonical_rule` | string | ✅ | Default convention |
| `alternate_rule` | string | ❌ | Valid alternate |
| `qualifier` | string | ❌ | Required qualifier for alternate |
| **Validation** | | | Must link to at least one N-TERM. |

### N-ARTIFACT: Production Artifact

| Property | Type | Required | Description |
|----------|------|:--------:|-------------|
| `id` | string | ✅ | Format: `ART-{CODE}` (e.g., `ART-DB`, `ART-IS`, `ART-ENC`) |
| `name` | string | ✅ | Full name |
| `file_path` | string | ✅ | Relative path from project root |
| `version` | string | ✅ | V1.0, V1.0.1, etc. |
| `freeze_date` | date | ✅ | Date frozen |
| `status` | enum | ✅ | FROZEN / DRAFT / DEPRECATED |
| `line_count` | integer | ✅ | Total lines |
| `errata_count` | integer | ✅ | Number of V1.0.1 errata corrections |
| **Validation** | | | `status` = FROZEN for all V1.0 artifacts. |

### N-SECTION: Artifact Section

| Property | Type | Required | Description |
|----------|------|:--------:|-------------|
| `id` | string | ✅ | Format: `SEC-{ART}-{SEQ}` (e.g., `SEC-DB-011` for Desk Bible §11) |
| `artifact_id` | string | ✅ | Parent artifact |
| `title` | string | ✅ | Section title |
| `start_line` | integer | ✅ | First line number |
| `end_line` | integer | ✅ | Last line number |
| `products_covered` | string[] | ❌ | Product IDs covered in this section |
| **Validation** | | | `start_line` < `end_line`. `artifact_id` must exist. |

### N-FORMULA: Formula / Calculation

| Property | Type | Required | Description |
|----------|------|:--------:|-------------|
| `id` | string | ✅ | Format: `FORM-{ART}-{LINE}` (e.g., `FORM-DB-1069`) |
| `expression` | string | ✅ | The formula text |
| `artifact_id` | string | ✅ | Parent artifact |
| `line` | integer | ✅ | Line number |
| `verified` | boolean | ✅ | Whether arithmetic has been checked |
| `errata_id` | string | ❌ | If corrected by errata |
| **Validation** | | | If `errata_id` is set, `verified` must be true. |

### N-EXAMPLE: Worked Example

| Property | Type | Required | Description |
|----------|------|:--------:|-------------|
| `id` | string | ✅ | Format: `EX-{ART}-{PRODUCT}` (e.g., `EX-DB-WOAC001`) |
| `product_id` | string | ✅ | Which product this example illustrates |
| `artifact_id` | string | ✅ | Parent artifact |
| `start_line` | integer | ✅ | Start of worked example |
| `end_line` | integer | ✅ | End of worked example |
| `has_terms_table` | boolean | ✅ | Whether terms are defined |
| `qa_checklist_passed` | boolean | ✅ | Whether sanity checklist applied |
| **Validation** | | | If `has_terms_table` = true, must define strike and barrier separately if both are referenced. |

### N-QUESTION: Interview Question

| Property | Type | Required | Description |
|----------|------|:--------:|-------------|
| `id` | string | ✅ | Format: `Q-{TIER}-{SEQ}` (e.g., `Q-T2-FTD-CORR`) |
| `tier` | integer | ✅ | 1, 2, or 3 |
| `product_id` | string | ❌ | If product-specific |
| `concept_ids` | string[] | ✅ | Concepts tested |
| `artifact_id` | string | ✅ | Source artifact |
| **Validation** | | | Must link to at least one concept. |

### N-ERRATUM: Erratum Item

| Property | Type | Required | Description |
|----------|------|:--------:|-------------|
| `id` | string | ✅ | Format: `E-{SEQ}` (e.g., `E-01`, `E-08`) |
| `artifact_id` | string | ✅ | Affected artifact |
| `line` | integer | ✅ | Affected line |
| `error_type` | string | ✅ | Label correction / Factual / Arithmetic / Qualifier |
| `severity` | enum | ✅ | P1 / P2 |
| `v1_text` | string | ✅ | Original text |
| `v101_text` | string | ✅ | Corrected text |
| `promoted_from` | string | ❌ | If promoted from review-only (e.g., "R-01") |
| **Validation** | | | `artifact_id` must exist. `line` must be within artifact line range. |

### N-REVIEW: Review-Only / Accept-As-Is Item

| Property | Type | Required | Description |
|----------|------|:--------:|-------------|
| `id` | string | ✅ | Format: `R-{SEQ}` or `A-{SEQ}` |
| `type` | enum | ✅ | REVIEW_ONLY / ACCEPT_AS_IS |
| `artifact_id` | string | ✅ | Affected artifact |
| `description` | string | ✅ | One-line summary |
| `disposition` | string | ✅ | Current status |
| `promoted_to` | string | ❌ | If promoted to erratum |
| **Validation** | | | If `promoted_to` is set, type should remain but status shows promoted. |

### N-LINTER_RULE: Linter Rule

| Property | Type | Required | Description |
|----------|------|:--------:|-------------|
| `id` | string | ✅ | Format: `LNT-{CAT}-{SEQ}` |
| `severity` | enum | ✅ | S1 / S2 / S3 / S4 |
| `trigger_pattern` | string | ✅ | Regex or description |
| `category` | string | ✅ | Correlation / Position / Ownership / Arithmetic / Structure / Cross-artifact / Qualifier |
| **Validation** | | | Must link to at least one regression test. |

### N-TEST: Regression Test

| Property | Type | Required | Description |
|----------|------|:--------:|-------------|
| `id` | string | ✅ | Format: `REG-{CAT}-{SEQ}` |
| `objective` | string | ✅ | What it prevents |
| `severity` | enum | ✅ | S1 / S2 / S3 |
| `detection_method` | enum | ✅ | REGEX / ARITHMETIC / TABLE_PARSE / CROSS_ARTIFACT / MANUAL |
| `pass_criteria` | string | ✅ | PASS condition |
| **Validation** | | | Must link to at least one erratum or defect class. |

### N-GOVERNANCE_RULE: Terminology Governance Rule

| Property | Type | Required | Description |
|----------|------|:--------:|-------------|
| `id` | string | ✅ | Format: `T-{CAT}-{SEQ}` |
| `term` | string | ✅ | Governed term |
| `severity` | enum | ✅ | S1 / S2 / S3 / S4 |
| `canonical_meaning` | string | ✅ | Default interpretation |
| **Validation** | | | Must link to at least one N-TERM. |

---

## EDGE TYPES

### Core Relationships

| Edge Type | Source | Target | Meaning | Multiplicity | Directional |
|-----------|--------|--------|---------|:------------:|:-----------:|
| `USES` | N-PRODUCT | N-TERM | Product uses this term | Many-to-Many | Yes |
| `DEFINES` | N-SECTION | N-TERM | Section provides canonical definition | One-to-Many | Yes |
| `CONTAINS` | N-ARTIFACT | N-SECTION | Artifact contains section | One-to-Many | Yes |
| `CORRECTS` | N-ERRATUM | N-SECTION | Erratum corrects text in section | Many-to-One | Yes |
| `REQUIRES` | N-TERM | N-CONVENTION | Term requires this convention | Many-to-One | Yes |
| `COVERS` | N-TEST | N-ERRATUM | Test covers this defect class | Many-to-Many | Yes |
| `CLASSIFIES` | N-REVIEW | N-SECTION | Register classifies this section's content | Many-to-One | Yes |
| `DEPENDS_ON` | N-ARTIFACT | N-ARTIFACT | Artifact depends on another | Many-to-Many | Yes |
| `ILLUSTRATES` | N-EXAMPLE | N-TERM | Example illustrates concept | Many-to-Many | Yes |
| `TESTS` | N-QUESTION | N-TERM | Question tests understanding of concept | Many-to-Many | Yes |

### Governance Relationships

| Edge Type | Source | Target | Meaning | Multiplicity | Directional |
|-----------|--------|--------|---------|:------------:|:-----------:|
| `GOVERNS` | N-GOVERNANCE_RULE | N-TERM | Rule governs this term | One-to-Many | Yes |
| `DETECTS` | N-LINTER_RULE | N-GOVERNANCE_RULE | Linter detects violations of this rule | Many-to-One | Yes |
| `VALIDATES` | N-TEST | N-LINTER_RULE | Test validates this linter rule | Many-to-Many | Yes |
| `PROMOTED_FROM` | N-ERRATUM | N-REVIEW | Erratum was promoted from review-only | One-to-One | Yes |
| `SUPERSEDES` | N-ARTIFACT | N-ARTIFACT | V1.0.1 document supersedes V1.0 draft | One-to-One | Yes |

### Product Relationships

| Edge Type | Source | Target | Meaning | Multiplicity | Directional |
|-----------|--------|--------|---------|:------------:|:-----------:|
| `BELONGS_TO` | N-PRODUCT | N-PRODUCT | Product belongs to family/group | Many-to-One | Yes |
| `COMPARED_WITH` | N-PRODUCT | N-PRODUCT | Products compared in matrix | Many-to-Many | No |
| `PREREQUISITE` | N-SECTION | N-SECTION | Must read section A before section B | Many-to-Many | Yes |
| `HEDGED_BY` | N-PRODUCT | N-PRODUCT | Product X is hedged by trade Y | Many-to-Many | Yes |

---

## GRAPH QUERIES (EXAMPLES)

### Q1: "Where is FTD correlation direction discussed?"

```
MATCH (p:PRODUCT {name: "FTD"})
  -[:USES]->(t:TERM {name: "long correlation"})
  <-[:DEFINES]-(s:SECTION)
  <-[:CONTAINS]-(a:ARTIFACT)
RETURN a.name, s.title, s.start_line
```

### Q2: "Show all errata-corrected appearances of 'short correlation'"

```
MATCH (t:TERM {name: "short correlation"})
  <-[:DEFINES]-(s:SECTION)
  <-[:CORRECTS]-(e:ERRATUM)
RETURN e.id, s.artifact_id, e.line, e.v1_text, e.v101_text
```

### Q3: "What linter rules protect against correlation direction errors?"

```
MATCH (t:TERM {name: "long correlation"})
  -[:REQUIRES]->(c:CONVENTION)
  <-[:DETECTS]-(l:LINTER_RULE)
RETURN l.id, l.severity, l.trigger_pattern
```

### Q4: "Is the FTD direction consistent across all artifacts?"

```
MATCH (p:PRODUCT {name: "FTD"})
  -[:USES]->(t:TERM)
WHERE t.name IN ["long correlation", "short correlation"]
MATCH (t)<-[:DEFINES]-(s:SECTION)<-[:CONTAINS]-(a:ARTIFACT)
RETURN a.name, s.title, t.name, s.start_line
ORDER BY a.name
```

---

## SERIALIZATION FORMAT

### Recommended: JSON-LD

```json
{
  "@context": {
    "spke": "https://structured-products.internal/ontology/",
    "product": "spke:Product",
    "term": "spke:Term",
    "uses": "spke:uses",
    "defines": "spke:defines"
  },
  "@graph": [
    {
      "@type": "product",
      "@id": "PROD-CLN-FTD001",
      "name": "First-to-Default Note",
      "family": "CLN",
      "complexity": 8,
      "correlation_direction": "LONG",
      "uses": ["TERM-COR-01", "TERM-COR-06", "TERM-PRO-01"]
    }
  ]
}
```

### Alternative: YAML for human readability

```yaml
nodes:
  - type: PRODUCT
    id: PROD-CLN-FTD001
    name: First-to-Default Note
    family: CLN
    complexity: 8
    correlation_direction: LONG

edges:
  - type: USES
    source: PROD-CLN-FTD001
    target: TERM-COR-01
  - type: USES
    source: PROD-CLN-FTD001
    target: TERM-COR-06
```

---

## GRAPH STATISTICS (PROJECTED)

| Node Type | Estimated Count |
|-----------|:--------------:|
| N-PRODUCT | 49 |
| N-TERM | 35+ |
| N-CONVENTION | 10 |
| N-ARTIFACT | 25 |
| N-SECTION | ~150 |
| N-FORMULA | ~80 |
| N-EXAMPLE | ~49 |
| N-QUESTION | ~200 |
| N-ERRATUM | 9 |
| N-REVIEW | 11 (5 R + 6 A) |
| N-LINTER_RULE | 22 |
| N-TEST | 21 |
| N-GOVERNANCE_RULE | 30 |
| **Total nodes** | **~680** |
| **Estimated edges** | **~2,500** |

---

*Knowledge Graph Ontology | V1.0.1-GOV-1.0 | 2026-06-27*
