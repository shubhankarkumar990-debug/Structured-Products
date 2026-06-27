# VERSIONING AND CHANGE CONTROL POLICY

**Ecosystem:** Structured Products Knowledge Ecosystem  
**Version:** V1.0.1-GOV-1.0  
**Effective:** 2026-06-27  
**Purpose:** Govern how changes are classified, versioned, and released to prevent silent semantic drift.

---

## VERSION NAMING CONVENTION

| Version | Format | Meaning | Example |
|---------|--------|---------|---------|
| **Major** | V{X}.0 | New content, restructured chapters, new products, breaking changes to conventions | V2.0 |
| **Minor** | V{X}.{Y} | New sections, appendices, additional products within existing families, non-breaking convention changes | V1.1 |
| **Patch** | V{X}.{Y}.{Z} | Errata corrections, clarifications, qualifier additions, arithmetic fixes | V1.0.1 |
| **Governance** | V{X}.{Y}.{Z}-GOV-{G} | Governance framework updates independent of content versions | V1.0.1-GOV-1.0 |

### Rules
- Major version resets minor and patch to 0
- Minor version resets patch to 0
- Governance versions track independently from content versions
- Frozen versions are never overwritten — new versions are companion documents

---

## CHANGE CLASSIFICATION

### Level 1: Erratum (Patch Version)

**Definition:** A confirmed factual error, self-contradiction, arithmetic mistake, or label that teaches the wrong direction.

**Criteria — ALL of:**
- The error produces a wrong answer or contradicts its own explanation
- The correction is surgical (specific lines, not chapter rewrites)
- The economic understanding is preserved — only the surface expression changes

**Process:**
1. Document in errata addendum with exact V{current} and V{next} text
2. Classify with erratum ID (E-XX)
3. Link to linter rule and regression test
4. Apply the worked example sanity checklist if arithmetic is involved
5. Update traceability matrix
6. Do NOT modify the frozen source file

**Examples:** E-01 through E-09 in V1.0.1 package

---

### Level 2: Clarification (Patch Version)

**Definition:** An addition that resolves ambiguity without changing meaning. Adds a qualifier, footnote, or convention note.

**Criteria — ALL of:**
- No substantive content change — the meaning is already correct
- The clarification prevents misreading in isolation
- It could be applied via an addendum without rewriting

**Process:**
1. Document as review-only (R-XX) or clarification item
2. Specify exact qualifier text to add
3. Classify severity (S2 or S3 — clarifications are never S1)
4. May be batched with errata in a patch release

**Examples:** R-01 through R-05 in V1.0.1 package

---

### Level 3: Content Addition (Minor Version)

**Definition:** New sections, products, worked examples, or appendices that extend the ecosystem without restructuring it.

**Criteria — ANY of:**
- New product treatment added
- New worked example added
- New interview question set added
- New appendix or reference section added
- Existing section expanded with material not present in V{current}

**Process:**
1. New content must pass the Operational QA Protocol before inclusion
2. All terminology must comply with the Terminology Governance Specification
3. All conventions must comply with the Convention Registry
4. Linter must pass with no S1 or S2 findings
5. Regression tests must pass
6. Traceability matrix must be updated
7. Knowledge graph must be updated
8. Changelog must document what was added and why

---

### Level 4: Structural Change (Major Version)

**Definition:** Restructured chapters, changed conventions, new product families, revised pedagogical approach, or any change that breaks backward compatibility with existing content.

**Criteria — ANY of:**
- Convention changed (e.g., switching from MTM to structural as default)
- Chapter structure reorganized
- New product family added
- Cross-references renumbered or removed
- Complexity scoring system revised
- System mappings changed

**Process:**
1. Full governance review required
2. All affected regression tests must be updated
3. All affected linter rules must be revised
4. Traceability matrix must be rebuilt for affected sections
5. Knowledge graph must be updated with new relationships
6. Previous version must remain frozen and accessible
7. Migration guide must document what changed and why

---

### Level 5: Acceptable Stylistic Variation (No Version Change)

**Definition:** Differences in phrasing that do not change meaning, ambiguity level, or correctness.

**Criteria — ALL of:**
- No self-contradiction introduced
- No new ambiguity introduced
- Convention compliance unchanged
- Linter would not flag it
- A reader would reach the same conclusion either way

**Examples:**
- "The investor benefits from high correlation" vs. "High correlation benefits the investor" — same meaning
- "The desk is long the put" vs. "The desk holds a long put position" — same meaning
- Different ordering of scenarios in a worked example — same content

**Process:** No version change. No documentation required.

---

## FROZEN VERSION MANAGEMENT

### Rules
1. A frozen version is NEVER modified. No exceptions.
2. Corrections exist ONLY in companion errata addenda.
3. Each frozen version has: source file + errata addendum + freeze certificate.
4. The freeze date is immutable.
5. "Hardened" means no further erratum discovery is expected — but an erratum may still be issued if found.

### Supersession
When a new version replaces an old version:
- The old version remains accessible in `release/archive/`
- The new version's changelog specifies every change from the previous version
- Cross-references from old to new are documented
- The knowledge graph updates `SUPERSEDES` edges

---

## CHANGELOG FORMAT

```markdown
# V{X}.{Y}.{Z} CHANGE LOG

**Date:** YYYY-MM-DD
**Baseline:** V{previous}
**Change level:** Erratum / Clarification / Content Addition / Structural Change

## Changes

| ID | Type | Artifact | Lines | Description |
|:--:|------|----------|:-----:|-------------|
| ... | ... | ... | ... | ... |

## Governance Updates

| Item | Change |
|------|--------|
| Linter rules added | LNT-XXX-XX |
| Regression tests added | REG-XXX-XX |
| Traceability entries updated | CONC-XXX |
| Knowledge graph edges added | X new |

## Frozen Artifacts — Status

| Artifact | Previous Status | New Status |
|----------|:--------------:|:----------:|
| ... | ... | ... |
```

---

## PREVENTING SILENT SEMANTIC DRIFT

### Mandatory Gates

| Gate | When | What Happens |
|------|------|--------------|
| **Linter pass** | Before any version release | All S1 findings block release. S2 findings must be resolved or justified. |
| **Regression test pass** | Before any version release | All regression tests must pass. New tests must be added for new error classes. |
| **Traceability update** | Before any version release | Every new concept must be traced. Every modified concept must be re-verified. |
| **Convention compliance check** | Before any version release | All new content must use canonical conventions. Alternate conventions must include qualifiers. |
| **Cross-artifact consistency check** | Before any version release | Same concept must not have opposite labels in different artifacts without qualifiers. |
| **Knowledge graph update** | Before any version release | All new nodes and edges must be added. Existing relationships must be verified. |

### Drift Detection Schedule

| Check | Frequency | Scope |
|-------|:---------:|-------|
| Linter scan | Every content change | Changed files |
| Regression suite | Every content change | Full suite |
| Cross-artifact consistency | Every release | All production artifacts |
| Convention registry audit | Every minor version | All conventions |
| Traceability audit | Every minor version | All traced concepts |
| Knowledge graph integrity | Every major version | Full graph |

---

## GOVERNANCE FRAMEWORK VERSIONING

The governance framework itself is versioned independently:

| Component | Version Format | Update Trigger |
|-----------|---------------|----------------|
| Terminology Governance Spec | V{G}.{R} | New governed term or rule change |
| Convention Registry | V{G}.{R} | New convention or rule change |
| Linter Specification | V{G}.{R} | New rule or severity change |
| Regression Test Suite | V{G}.{R} | New test or defect class |
| Traceability Matrix | V{G}.{R} | New concept or appearance |
| Knowledge Graph Ontology | V{G}.{R} | New node/edge type |
| Ambiguous Terms Policy | V{G}.{R} | New ambiguous term class |
| This Policy | V{G}.{R} | Policy change |
| Operational QA Protocol | V{G}.{R} | Process change |

---

*Versioning and Change Control Policy | V1.0.1-GOV-1.0 | 2026-06-27*
