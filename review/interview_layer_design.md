# Interview Preparation Layer — Design Review

**Date:** 2026-06-21
**Proposed Addition:** Tier 4 — Interview Answer (added to Solutions Manual)
**Framework:** v1.3.1 (FROZEN)
**Purpose:** Assess adding a fourth answer tier optimized for interviews
**Implementation:** After Solutions Manual (Part 7), as enhancement layer

---

## 1. Rationale

The Solutions Manual has three tiers:

| Tier | Purpose | Length | Audience |
|:----:|---------|:------:|----------|
| 1 | Short Answer | 1-3 sentences | Self-check |
| 2 | Detailed Explanation | 100-200 words | Deeper learning |
| 3 | Desk Perspective | 75-150 words | Practitioner insight |

**Gap:** None of these tiers is optimized for the interview setting. Interview answers require a specific format: 30-60 seconds, structured, demonstrating competence without over-explaining. This is a distinct communication skill.

---

## 2. Tier 4 Specification

### 2.1 Format

| Attribute | Specification |
|-----------|-------------|
| Length | 75-120 words (30-60 seconds spoken) |
| Structure | Hook → Core → Proof Point |
| Tone | Confident, precise, appropriately casual |
| Jargon level | Uses desk language correctly — demonstrates fluency |
| Target audience | Analyst/associate interviews, desk rotation interviews, internal transfers |

### 2.2 Three-Part Structure

**Hook** (1 sentence): State what the product IS — no preamble.
**Core** (2-3 sentences): How it works, what drives the economics.
**Proof Point** (1 sentence): One specific detail that shows you've worked with this product or thought deeply about it.

### 2.3 Example

**Q:** "What is a Reverse Convertible?"

**Tier 4 — Interview Answer:**
"A Reverse Convertible is a yield-enhancement note where the investor earns an above-market coupon — typically 6-8% — in exchange for accepting equity downside risk through a knock-in put. The enhanced coupon is funded by the put premium: the investor is essentially selling insurance on the underlying stock falling below a barrier, usually set at 60-75% of initial level. On the desk, the key risk management challenge is that the product has a large negative vega exposure near the barrier — when vol spikes and the stock drops toward the barrier simultaneously, the delta-hedging cost accelerates precisely when the market is most expensive to trade."

**Word count:** 104. **Spoken time:** ~40 seconds.

---

## 3. Applicability Assessment

### 3.1 Which Questions Get Tier 4?

Not all questions suit interview format. Assessment:

| Question Type | Tier 4 Applicable? | Rationale |
|:-------------:|:------------------:|-----------|
| Review Q1-Q5 (definitional) | YES — 3 of 5 | Definitional questions are core interview material |
| Scenario Q1-Q3 | PARTIAL — 1 of 3 | Some scenarios too numerical for verbal answer |
| Desk Q1 | YES — always | Desk questions are interview-style by design |

**Estimate per chapter:** ~4 questions get Tier 4 treatment (3 Review + 1 Desk).

### 3.2 Volume

| Source | Tier 4 Answers | Words per Answer | Total Words |
|--------|:--------------:|:----------------:|:-----------:|
| 49 product chapters × 4 answers | 196 | ~100 | ~19,600 |
| Foundation sections × 3 answers | 12 | ~100 | ~1,200 |
| Cross-product questions × 5 | 5 | ~120 | ~600 |
| **Total** | **213** | — | **~21,400** |

---

## 4. Quality Requirements

| Requirement | Detail |
|------------|--------|
| Technically accurate | Every claim verifiable against chapter content |
| Appropriately confident | No hedging ("I think," "maybe"). Direct statements |
| Desk-authentic | Uses terminology a desk practitioner would use |
| Time-bounded | Reader can time themselves: target 30-60 seconds |
| Differentiated from T1-T3 | Not a shorter version of T2. Different structure and intent |

### 4.1 Anti-Patterns

| Anti-Pattern | Why Bad | Example |
|-------------|---------|---------|
| Textbook recitation | Sounds memorized, not understood | "A Reverse Convertible is defined as..." |
| Over-qualification | Shows uncertainty | "It's kind of like selling a put, in a way..." |
| Missing proof point | Generic, not memorable | Ends at "investor gets enhanced coupon" |
| Too long | Interviewer loses interest | >90 seconds |
| Too technical for level | Misjudges audience | Discussing Heston model in analyst interview |

---

## 5. Integration with Solutions Manual

### 5.1 Placement

Tier 4 appears AFTER Tier 3 for applicable questions. Flagged with a distinctive icon (e.g., 🎯 or **[INTERVIEW]** tag).

```markdown
**Q1:** What two components make up a PPN?

**Tier 1 — Short Answer:** [...]
**Tier 2 — Detailed Explanation:** [...]
**Tier 3 — Desk Perspective:** [...]
**Tier 4 — Interview Answer:** [...]
```

### 5.2 Standalone Section

Additionally, compile the "Top 49 Interview Answers" — one per product — into a dedicated section:

```
Part 7 — Solutions Manual
  └── 7.10 — Interview Preparation Quick Reference
        ├── 49 product interview answers (one per product)
        ├── 10 cross-product interview answers
        └── Interview tips (structure, pacing, common mistakes)
```

---

## 6. Estimates

| Metric | Value |
|--------|:-----:|
| Tier 4 answers | ~213 |
| Total word count | ~21,400 |
| Pages (within Solutions Manual) | ~40 |
| Standalone section (7.10) | ~15 pages |
| Effort | 4 days (incremental to Solutions Manual generation) |

---

## 7. Assessment

| Criterion | Score |
|-----------|:-----:|
| Educational impact | HIGH — teaches a distinct skill (interview communication) |
| Effort | LOW — incremental to existing Solutions Manual work |
| Publication value | HIGH — differentiator vs competing references |
| Reader demand | VERY HIGH — primary audience includes career transitioners |
| Risk | LOW — additive to existing architecture |

**Recommendation: PROCEED.** Generate alongside Solutions Manual Tier 1-3. Incremental effort (~4 days on top of 22-day Solutions Manual). High reader demand — many Desk Bible readers preparing for desk roles.

---

*Interview Preparation Layer Design Review completed 2026-06-21.*
