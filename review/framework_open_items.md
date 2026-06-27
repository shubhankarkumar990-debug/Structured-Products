# Framework Open Items Report

**Date:** 2026-06-20
**Source:** `review/framework_v1_3_1_stabilization_audit.md`
**Framework Version:** v1.3.1 (FROZEN)
**Purpose:** Document all unresolved issues from the stabilization audit with risk assessment and Batch 6 impact

---

## 1. Deferred Issue

### M1 — Jargon Watchlist lacks glossary cross-reference

| Field | Detail |
|-------|--------|
| **Audit ID** | M1 |
| **Category** | Registry-Management Risk |
| **Location** | `production/generation_dashboard.md` §7 (Jargon Watchlist) |
| **Description** | The Jargon Watchlist tracks new terms discovered during chapter generation with an "Added to Watchlist: YES" flag, but does not track whether each term was subsequently added to `reference/glossary/glossary.yaml`. A term can be watchlisted and never formalized. |
| **Why not resolved now** | The watchlist is a generation-time tracking tool. Adding a glossary cross-reference column requires reviewing all existing watchlist entries (across 24 chapters) to determine which terms were added to the glossary and which remain chapter-specific. This is editorial reconciliation work — it belongs in the Template Harmonization Pass (after 49/49), not during framework stabilization. Resolving it now would violate the constraint: "Do not rewrite chapters unless a review agent identifies a genuine issue." |
| **Associated risk** | **LOW.** Terms may be watchlisted but never formalized in the glossary. This creates a minor inconsistency: a future chapter author might define a term independently rather than reusing a glossary definition, producing slightly different wording across chapters. However, the Jargon Police Agent already checks `glossary.yaml` during generation (checklist E17), so any term that should be in the glossary will be flagged if it is missing at generation time. The risk is limited to post-generation reconciliation, not generation quality. |
| **Recommended future action** | During the Template Harmonization Pass (after 49/49 accepted): (1) Add an "Added to Glossary" column to the Jargon Watchlist (values: YES / NO / CHAPTER-SPECIFIC). (2) Review all watchlisted terms across 49 chapters. (3) Add recurring terms to `glossary.yaml`. (4) Mark chapter-specific terms as CHAPTER-SPECIFIC. Estimated effort: 30 minutes. |
| **Blocks Batch 6?** | **NO.** The Jargon Police Agent (checklist E4, E5, E17) enforces glossary discipline during generation regardless of watchlist tracking. Batch 6 chapters will have correct terminology compliance. The missing cross-reference only affects post-generation reconciliation. |

---

## 2. Accepted Issue

### S1 — Analogy registry scalability at 49 entries

| Field | Detail |
|-------|--------|
| **Audit ID** | S1 |
| **Category** | Scalability Risk |
| **Location** | `production/generation_dashboard.md` §5 (Analogy Domain Registry) |
| **Description** | The Analogy Domain Registry is a flat table in the generation dashboard. At 49 chapters, it will contain 49+ entries (one per chapter plus reserved domains from Parts 0-4). The audit flagged a theoretical concern that checking for analogy collisions at scale could become unwieldy. |
| **Why accepted (not resolved)** | The registry is a simple two-column table (Chapter \| Analogy Domain). Linear search through 49 entries is trivial — a human can scan the list in under 30 seconds, and the Consistency Agent performs collision checks programmatically. There is no performance bottleneck, no structural limitation, and no data integrity risk. Introducing a more complex data structure (e.g., a YAML registry with metadata) would add governance overhead without measurable benefit. The current design is fit for purpose at the 49-product scale. |
| **Associated risk** | **NEGLIGIBLE.** At 49 entries, the registry is well within the manageable range for a flat list. The Desk Bible has a fixed product universe (49 products) — the registry will never grow beyond ~55 entries (49 products + ~6 reserved domains). This is not a scaling concern in any practical sense. |
| **Recommended future action** | None. The current design is sufficient for the full 49-product scope. If the product universe were to expand beyond 49 (not currently planned), the registry could be migrated to a YAML file at that time. No preemptive action is warranted. |
| **Blocks Batch 6?** | **NO.** The registry has functioned correctly through 24 chapters with zero collisions detected. It will continue to function correctly through 49 chapters. |

---

## 3. Summary

| Issue | ID | Severity | Resolution | Blocks Batch 6? |
|-------|:--:|:--------:|:----------:|:----------------:|
| Jargon Watchlist glossary cross-reference | M1 | Low | Deferred to Template Harmonization Pass | NO |
| Analogy registry scalability | S1 | Negligible | Accepted as-is — design is fit for purpose | NO |

---

## 4. GO / NO-GO Recommendation

### **GO**

Neither open issue affects chapter generation quality, framework compliance, or review integrity. Both are post-generation reconciliation concerns that will be addressed (M1) or require no action (S1) during the Template Harmonization Pass after all 49 chapters are accepted.

The framework is frozen, validated, and stable. All 25 critical and non-trivial issues from the stabilization audit have been resolved. The 2 remaining items are low-severity and do not interact with any generation, review, or acceptance workflow.

Batch 6 may proceed.

---

*Open Items Report completed 2026-06-20. Framework v1.3.1 remains FROZEN. No modifications applied.*
