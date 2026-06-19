# Memory Design Guide

## The Memory Layer

Memory is the framework's highest-value component. It stores per-family knowledge that is reused across every entry in the family, eliminating repetitive decisions, preventing the most dangerous error classes, and driving the zero-retry rate observed in production.

---

## Three Memory Types

The framework uses exactly three memory types. This count was empirically validated: the original architecture planned for seven memory subdirectories, but only three were ever used. The other four remained empty across 28 products.

### 1. Terminology Memory

**Path:** `memory/terminology/{FAMILY}.yaml`  
**Purpose:** Product/entry names, abbreviations, casing rules, domain-specific terms.

**What it stores:**
- Full names and standard abbreviations for every entry in the family.
- First-mention format (e.g., "Credit-Linked Note (CLN)").
- System/tool names with correct casing (e.g., "NEMO", "Sophis", not "nemo", "sophis").
- Domain abbreviations and their expansions.

**Why it matters:** Inconsistent terminology across entries makes the document look unreviewed. Terminology memory ensures every entry in a family uses the same names, abbreviations, and casing rules.

**Impact:** Low-severity errors prevented. A wrong abbreviation is noticeable but not operationally dangerous.

### 2. Operational Map Memory

**Path:** `memory/operational-maps/{FAMILY}.yaml`  
**Purpose:** Which systems, processes, or tools handle entries in this family.

**What it stores:**
- Primary operational system and its role.
- Secondary systems and their roles.
- What each system carries (fields, data, lifecycle events).
- Critical mapping decisions (e.g., "Murex is NOT used for any CLN product").

**Why it matters:** Getting the operational mapping wrong is the highest-severity error possible. In the Desk Bible, booking a product in the wrong system would be a live operational risk. In any domain, a wrong system/process mapping means the documentation actively misleads the reader.

**Impact:** Highest-severity errors prevented. The operational map was consulted for every entry and never required correction after initial creation.

### 3. Style Convention Memory

**Path:** `memory/style-conventions/{FAMILY}.yaml`  
**Purpose:** Formatting rules, known false positives, and accepted conventions.

**What it stores:**
- Canonical section names (heading format).
- Currency/notation rules.
- Known false positives (rules that the reviewer flags as violations but which are actually correct).
- Approved patterns (positive rules that MUST be followed).
- Accepted conventions (family-specific patterns validated across multiple entries).

**Why it matters:** Without FP suppression, every entry raises 3+ false violations. Across 28 entries, that's 84 false violations — each requiring investigation and dismissal. Style convention memory eliminates this noise.

**Impact:** Medium-severity time waste prevented. False violations don't cause errors but they slow production and erode trust in the review gates.

---

## Memory Lifecycle

### Creation

Memory is created during the **family bootstrap** — the generation of the first entry in a new family. The three memory files are written before the first entry's pipeline run begins.

### Validation

Memory is validated during the bootstrap entry's pipeline run. If the QA or style review reveals a need to correct the memory, the correction is made immediately.

### Reuse

Once validated, memory is reused without modification for every subsequent entry in the family. In the Desk Bible, the reuse ratio was 4.6:1 (69 reuses from 15 artifacts).

### Update

Memory is updated only when:
- A new entry name or abbreviation is added to the family.
- An operational mapping changes (e.g., system migration).
- A new accepted convention is validated across multiple entries.

Each update increments the `version` field and updates the `stored_at` timestamp.

### Retirement

Memory is never deleted. Even if an entry is removed, the family memory persists because other entries depend on it. The only scenario for deletion is removing an entire family.

---

## Bootstrap Protocol

Creating memory for a new family is the most critical moment in the project. The bootstrap protocol has two phases:

### Phase 1 — Create Memory Artifacts

Create the three memory files by hand (or by adapting templates from an adjacent family). The most important decision is the **operational map** — which system, process, or tool handles this family's entries.

**Validation questions before proceeding:**
1. Is the operational mapping correct? (Verify with a domain expert.)
2. Are the abbreviations standard? (Check industry usage.)
3. Are the section names appropriate for this family? (Most families use the project default.)

### Phase 2 — Validate via Bootstrap Entry

Generate the first entry in the family through the full pipeline. During this run:

1. **Note corrections.** If the QA or style review reveals memory errors, fix them immediately.
2. **Note new conventions.** If the review flags family-specific patterns that are inherent to the entry structure (not errors), note them but DO NOT add them to memory yet.

### Convention Validation Protocol

A convention observed in one entry might be an error. A convention observed in two entries is a pattern. The protocol:

1. **Observe** the convention in the bootstrap entry. Note it in the pipeline log.
2. **Validate** it in the second entry of the family. If it recurs and is confirmed as inherent to the family structure, proceed to step 3.
3. **Enshrine** it by adding it to `accepted_conventions` in the style-conventions memory file.

This protocol prevented false conventions from polluting the memory layer in the Desk Bible. The STEG family's CMS decomposition convention was deferred during bootstrap (VSTEG001), validated across RASTEG001/CSTEG001/TARN001, and only then added to the style-conventions file.

---

## Memory File Schema

### Terminology

```yaml
meta:
  family: "{FAMILY}"
  category: terminology
  stored_at: "{ISO timestamp}"
  version: 1

content:
  entry_names:
    - full: "{Full Name}"
      abbreviation: "{ABBR}"
      first_mention_format: "{Full Name} ({ABBR})"

  system_names:
    - name: "{SYSTEM}"
      casing: "{Correct Casing}"

  abbreviations:
    - term: "{ABBR}"
      expansion: "{Full expansion}"
```

### Operational Map

```yaml
meta:
  family: "{FAMILY}"
  category: operational-map
  stored_at: "{ISO timestamp}"
  version: 1

content:
  primary_system: "{SYSTEM_NAME}"
  primary_role: "{What it does}"
  secondary_system: "{SYSTEM_NAME}"
  secondary_role: "{What it does}"

  primary_carries:
    - "{field or lifecycle event}"

  secondary_carries:
    - "{field or model input}"

  critical_notes:
    - "{Important mapping decision, e.g., 'System X is NOT used for this family'}"
```

### Style Conventions

```yaml
meta:
  family: "{FAMILY}"
  category: style-conventions
  stored_at: "{ISO timestamp}"
  version: 1

content:
  canonical_section_names:
    - "{Section 1}"
    - "{Section 2}"

  known_false_positives:
    - rule: "{Rule that triggers a false violation}"
      reason: "{Why it is actually correct}"

  approved_patterns:
    - pattern: "{Positive rule}"
      note: "{Clarification}"

  accepted_conventions: []
```

---

## Anti-Patterns

### Don't Over-Segment Memory

The original Desk Bible architecture created 7 memory subdirectories. Only 3 were ever used. The unused 4 (components, definitions, examples, reconciliation) added directory structure without adding value.

**Rule:** Start with the 3 proven types. Add a 4th type only if you can name 3+ entries that would use it and explain why existing types don't cover it.

### Don't Add Conventions Prematurely

Adding a convention after seeing it in one entry risks enshrining an error. The convention validation protocol (observe once, validate twice) exists for a reason.

### Don't Mix Family Memory

Each family has its own memory files. Even if two families use similar terminology, maintain separate files. Shared memory creates coupling — updating one family's memory silently affects another.

### Don't Forget to Version

Every memory update should increment the `version` field. This enables auditing: if an entry was generated against memory v2 but the current version is v5, a reviewer knows to check whether the entry's content is still consistent.
