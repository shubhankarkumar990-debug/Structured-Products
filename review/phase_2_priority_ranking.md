# Phase 2 Priority Ranking

**Date:** 2026-06-22
**Input:** `review/phase_2_application_architecture_review.md`
**Artifacts ranked:** 5 (from 11 proposals, after MERGE and DEFER decisions)

---

## Ranking Methodology

Each artifact scored on 4 dimensions (1–10):

| Dimension | Weight | Definition |
|-----------|:------:|------------|
| Educational Gap | 30% | How much NEW knowledge does this create vs what already exists? |
| Career Impact | 25% | How directly does this help someone get/perform a job? |
| Cross-Product Value | 25% | Does this teach synthesis across products vs single-product knowledge? |
| Effort Efficiency | 20% | Lines of genuine new content per line written (inverse of duplication) |

**Score = (Gap × 0.30) + (Career × 0.25) + (Cross × 0.25) + (Efficiency × 0.20)**

---

## Scores

### Rank 1: Solutions Manual (+ Structuring Decision Framework merged)

`production/solutions_manual.md`

| Dimension | Score | Rationale |
|-----------|:-----:|-----------|
| Educational Gap | **10** | No artifact answers "which product for this problem?" — the structurer's core skill |
| Career Impact | **9** | Structurer interviews test exactly this: "Client wants X, what do you recommend?" |
| Cross-Product Value | **10** | Every scenario requires comparing across families and complexity tiers |
| Effort Efficiency | **8** | ~75% new content. §3/§8 provide per-product inputs but not cross-product synthesis |

**Weighted Score: 9.35**

**Why first:** Every existing artifact classifies products (what they ARE). This is the only artifact that teaches product selection (what to USE). The transition from knowledge to application starts here.

---

### Rank 2: Interview System (merged: Question Bank + Answer Manual + Confusion Pairs + Mock Framework)

`production/interview_system.md`

| Dimension | Score | Rationale |
|-----------|:-----:|-----------|
| Educational Gap | **7** | Questions exist (~390 across chapters + Atlas). Answer templates and mock tracks are new |
| Career Impact | **10** | Directly actionable for interview preparation — the primary audience use case |
| Cross-Product Value | **8** | Confusion pairs and mock interviews force cross-product thinking |
| Effort Efficiency | **7** | ~60% new content after deduplication. Existing questions referenced, not recreated |

**Weighted Score: 8.05**

**Why second:** Highest career impact of any artifact. The merged format avoids 40% duplication vs building 4 separate artifacts.

---

### Rank 3: Hedging Playbook

`production/hedging_playbook.md`

| Dimension | Score | Rationale |
|-----------|:-----:|-----------|
| Educational Gap | **8** | Per-product risk exists (§15). Cross-product hedging synthesis and failure modes are new |
| Career Impact | **8** | Trading desk interviews and daily operations depend on hedging knowledge |
| Cross-Product Value | **9** | Hedging a book with multiple products is the primary cross-product trading skill |
| Effort Efficiency | **7** | ~65% new content. §15 and Matrix Part 3 provide inputs |

**Weighted Score: 8.00**

**Why third:** The only artifact that teaches operational hedging (not just risk identification). Critical for trading/risk roles.

---

### Rank 4: Case Study Library

`production/case_study_library.md`

| Dimension | Score | Rationale |
|-----------|:-----:|-----------|
| Educational Gap | **9** | Zero historical event analysis exists. §18 has hypothetical examples only |
| Career Impact | **7** | "Tell me about a time when..." and market event knowledge are interview staples |
| Cross-Product Value | **8** | Market events (2008, vol events, correlation crises) affect multiple product families |
| Effort Efficiency | **9** | ~90% new content. Minimal overlap with existing artifacts |

**Weighted Score: 8.20**

**Why fourth (not higher despite score):** High educational value but more supplemental than foundational. You need the Solutions Manual and Interview System before case studies add context.

---

### Rank 5: Trade Break Library

`production/trade_break_library.md`

| Dimension | Score | Rationale |
|-----------|:-----:|-----------|
| Educational Gap | **8** | Structured investigation format (symptom→cause→fix→prevent) is completely new |
| Career Impact | **6** | Operations-focused. Narrower audience than Ranks 1–4 |
| Cross-Product Value | **6** | Trade breaks are usually product-specific. Some cross-product patterns exist |
| Effort Efficiency | **8** | ~80% new content. §16/§17 provide system context, not investigation paths |

**Weighted Score: 7.00**

**Why last:** Highest value for operations/middle-office roles but narrower audience than other artifacts. Still high-quality new content.

---

## Summary Table

| Rank | Artifact | Gap | Career | Cross | Efficiency | **Score** |
|:----:|----------|:---:|:------:|:-----:|:----------:|:---------:|
| 1 | Solutions Manual | 10 | 9 | 10 | 8 | **9.35** |
| 2 | Interview System | 7 | 10 | 8 | 7 | **8.05** |
| 3 | Hedging Playbook | 8 | 8 | 9 | 7 | **8.00** |
| 4 | Case Study Library | 9 | 7 | 8 | 9 | **8.20** |
| 5 | Trade Break Library | 8 | 6 | 6 | 8 | **7.00** |

**Note:** Case Study Library scores 8.20 (higher than Hedging at 8.00) but ranks 4th because it is supplemental — its educational value compounds only after foundational artifacts (Solutions Manual, Interview System) exist.

---

## Deferred Artifacts (not ranked)

| Artifact | Reason Deferred |
|----------|----------------|
| Desk Operations Playbook | 50% overlap with §5 + §14 + §16. Consolidation value only |
| AI Tutor Architecture | Design-only spec. No educational content for current audience |

---

*Priority ranking complete. 2026-06-22.*
