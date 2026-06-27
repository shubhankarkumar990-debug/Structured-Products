# OPERATIONAL QA PROTOCOL

**Ecosystem:** Structured Products Knowledge Ecosystem  
**Version:** V1.0.1-GOV-1.0  
**Effective:** 2026-06-27  
**Purpose:** Practical protocol for approving new content additions. Not theoretical — every step is actionable.

---

## Protocol Scope

This protocol applies to:
- New product treatments
- New worked examples
- New interview question sets
- New appendices or reference sections
- New chapters or sub-sections
- Errata corrections to frozen artifacts
- Convention framework updates

It does NOT apply to:
- Governance framework updates (use the versioning policy)
- Pure formatting/layout changes with no semantic impact
- Metadata updates (timestamps, version numbers)

---

## PHASE 1: PRE-SUBMISSION CHECKS (Author)

The content author must complete these checks before submitting for review.

### Gate 1.1: Terminology Compliance

| # | Check | Blocking? | Pass Criteria |
|:-:|-------|:---------:|---------------|
| 1 | All correlation direction labels use MTM convention or are qualified with "structurally" | **HARD FAIL** | Zero unqualified structural-convention labels |
| 2 | All desk positions specify raw or hedged | **HARD FAIL** | Zero desk positions without raw/hedged qualifier |
| 3 | Protection buyer/seller correctly attributed | **HARD FAIL** | In structured notes: investor = seller, desk = buyer |
| 4 | Strike and barrier defined separately in every worked example | **HARD FAIL** | Both in terms table if both referenced |
| 5 | All governed terms match canonical meanings | SOFT WARN | Check against terminology governance specification |
| 6 | All ambiguous terms qualified per ambiguous terms policy | SOFT WARN | Check against AMB-01 through AMB-15 |

### Gate 1.2: Worked Example Sanity

| # | Check | Blocking? | Pass Criteria |
|:-:|-------|:---------:|---------------|
| 7 | Worked example sanity checklist (all 15 items) passed | **HARD FAIL** | All 15 items pass or have documented justification |
| 8 | All intermediate arithmetic verified | **HARD FAIL** | Every step produces the stated value |
| 9 | All signs correct (ΔS, Gamma × ΔS, etc.) | **HARD FAIL** | Sign of price change included in all multiplicative steps |
| 10 | Economic intuition matches arithmetic direction | **HARD FAIL** | "Investor profits" → numbers show positive P&L |

### Gate 1.3: Convention Compliance

| # | Check | Blocking? | Pass Criteria |
|:-:|-------|:---------:|---------------|
| 11 | Content complies with all 10 convention registry entries | SOFT WARN | No convention violations |
| 12 | No hedged position described as product property | SOFT WARN | "Desk's net position is..." not "Product is..." |
| 13 | "Reversal" language qualified if used in NTD context | SOFT WARN | Specifies "between FTD and NTD" |

---

## PHASE 2: AUTOMATED VALIDATION (Linter)

Run the semantic linter against the new content.

### Gate 2.1: Linter Pass

| Severity | Action | Disposition |
|:--------:|--------|-------------|
| **S1 (BLOCK)** | **HARD FAIL** — must fix before proceeding | No exceptions. Every S1 must be resolved. |
| **S2 (WARN)** | Must resolve or document justification | Justification must cite a specific governance rule or convention exception. |
| **S3 (INFO)** | Should resolve | Non-blocking. Author should address if straightforward. |
| **S4 (STYLE)** | May address | Non-blocking. Author's discretion. |

### Gate 2.2: Linter Suppression Review

If any S1 or S2 finding is suppressed:
- The suppression must include a `reason:` field
- The reason must cite a specific governance rule exception
- A human reviewer must approve each S1/S2 suppression
- All suppressions are logged in the version's changelog

---

## PHASE 3: REGRESSION TESTING (Automated)

Run the full regression test suite.

### Gate 3.1: Regression Pass

| Result | Action |
|--------|--------|
| All tests PASS | Proceed to Phase 4 |
| Any test FAILS | **HARD FAIL** — must fix before proceeding |
| New error class identified | Must create a new regression test before proceeding |

### Gate 3.2: Coverage Check

- Every new worked example must have at least one regression test
- Every new correlation reference must be covered by REG-COR tests
- Every new protection reference must be covered by REG-PRO tests
- New tests must be added to the regression test suite and linked in the traceability matrix

---

## PHASE 4: CROSS-ARTIFACT VALIDATION (Manual + Automated)

### Gate 4.1: Cross-Artifact Consistency

| # | Check | Blocking? | Pass Criteria |
|:-:|-------|:---------:|---------------|
| 14 | Same concept has consistent labels across all artifacts | **HARD FAIL** | No unqualified opposite labels for same concept/position |
| 15 | New content does not contradict any frozen artifact's errata-corrected text | **HARD FAIL** | New content uses the V1.0.1 corrected wording, not V1.0 |
| 16 | Interview System answers match Desk Bible for same product | SOFT WARN | Spot-check 3 products from new content |
| 17 | Solutions Manual descriptions consistent with new content | SOFT WARN | Spot-check relevant products |

### Gate 4.2: Traceability Update

| # | Check | Blocking? | Pass Criteria |
|:-:|-------|:---------:|---------------|
| 18 | All new concepts added to traceability matrix | **HARD FAIL** | CONC-XXX entry for each new concept |
| 19 | All new appearances of existing concepts traced | SOFT WARN | Existing CONC entries updated with new artifact references |
| 20 | All errata-corrected concepts verified in new content | **HARD FAIL** | New content uses corrected (V1.0.1) direction, not V1.0 |

---

## PHASE 5: KNOWLEDGE GRAPH UPDATE (Manual)

### Gate 5.1: Graph Integrity

| # | Check | Blocking? | Pass Criteria |
|:-:|-------|:---------:|---------------|
| 21 | New nodes added for new products/terms/sections | SOFT WARN | All identifiable entities have nodes |
| 22 | New edges added for new relationships | SOFT WARN | USES, DEFINES, CONTAINS, ILLUSTRATES, TESTS edges updated |
| 23 | Existing edges verified | SOFT WARN | No orphaned nodes or dangling edges |

---

## PHASE 6: REVIEW AND APPROVAL

### Reviewer Responsibilities

| Reviewer Role | Checks | Authority |
|--------------|--------|-----------|
| **Content Reviewer** | Finance accuracy, pedagogical clarity, completeness | Can approve or request changes |
| **Governance Reviewer** | Terminology compliance, convention compliance, linter results | Can BLOCK on governance violations |
| **Release Engineer** | Version numbering, changelog, traceability, knowledge graph | Can BLOCK on release integrity |

### Approval Requirements

| Content Type | Content Review | Governance Review | Release Engineering |
|-------------|:--------------:|:-----------------:|:-------------------:|
| Erratum | Required | Required | Required |
| Clarification | Required | Required | Required |
| New section/product | Required | Required | Required |
| New worked example | Required | Required | Required |
| Interview question | Required | Required (S1/S2 terms only) | Recommended |
| Governance update | Recommended | Required | Required |

### Approval Flow

```
Author → Pre-submission checks (Phase 1)
       → Linter pass (Phase 2)
       → Regression pass (Phase 3)
       → Cross-artifact validation (Phase 4)
       → Knowledge graph update (Phase 5)
       → Content Review → Governance Review → Release Engineering
       → APPROVED / CHANGES REQUIRED
```

---

## PHASE 7: POST-RELEASE VERIFICATION

### Gate 7.1: Release Verification

| # | Check | When | Pass Criteria |
|:-:|-------|------|---------------|
| 24 | Changelog published | At release | All changes documented |
| 25 | Traceability matrix current | At release | All concepts verified |
| 26 | Regression suite updated | At release | New tests for new error classes |
| 27 | Linter rules updated | At release | New rules for new term classes |
| 28 | Knowledge graph updated | At release | All new nodes/edges added |
| 29 | Freeze certificate issued (if applicable) | At release | For new frozen artifacts |

---

## HARD FAIL vs SOFT WARN SUMMARY

| Gate | Type | Description |
|:----:|:----:|-------------|
| 1-4 | HARD FAIL | Terminology compliance (correlation, protection, strike/barrier, raw/hedged) |
| 5-6 | SOFT WARN | General governed terms and ambiguous terms |
| 7-10 | HARD FAIL | Worked example correctness |
| 11-13 | SOFT WARN | Convention compliance |
| S1 linter | HARD FAIL | Self-contradictions, factual errors |
| S2 linter | RESOLVE/JUSTIFY | Ambiguity that could teach wrong answer |
| Regression fail | HARD FAIL | Known defect reintroduced |
| 14-15, 20 | HARD FAIL | Cross-artifact inconsistency, use of V1.0 (uncorrected) text |
| 16-19, 21-23 | SOFT WARN | Completeness and traceability |

**Total gates: 29** (14 HARD FAIL, 15 SOFT WARN)

---

*Operational QA Protocol | V1.0.1-GOV-1.0 | 2026-06-27*
