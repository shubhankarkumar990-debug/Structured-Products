# Examiner Notes Enhancement — Design Review

**Date:** 2026-06-21
**Purpose:** Assess adding Examiner Notes (Common Mistake, Interview Insight, Red Flag Answer) to Solutions Manual
**Current tiers:** T1 (Short Answer), T2 (Detailed Explanation), T3 (Desk Perspective), T4 (Interview Answer)

---

## 1. Proposed Addition

For every answer in the Solutions Manual, add three examiner annotations:

| Annotation | Content | Purpose |
|-----------|---------|---------|
| **Common Mistake** | The most frequent wrong answer or misconception | Preemptive correction — reader sees what to avoid |
| **Interview Insight** | What an interviewer is actually testing with this question | Meta-learning — reader understands the question behind the question |
| **Red Flag Answer** | An answer that signals the candidate doesn't understand the product | Negative calibration — reader knows what NOT to say |

### 1.1 Example

**Q:** "What two components make up a PPN?"

**Common Mistake:** "Confusing participation rate with a coupon. The PPN has a participation rate (% of upside captured), not a fixed coupon. Saying '90% coupon' signals misunderstanding."

**Interview Insight:** "The interviewer is testing whether you understand that enhanced returns always come from somewhere — the PPN's upside comes from an embedded option, funded by the bond discount. If you just name the components without explaining the funding mechanism, you've answered the question but missed the point."

**Red Flag Answer:** "'A PPN is a bond that also goes up with the market.' This answer treats the PPN as magic — something that has bond safety AND equity upside. It misses the tradeoff: capped participation, no dividends, issuer credit risk, and opportunity cost."

---

## 2. Volume Assessment

| Metric | Value |
|--------|:-----:|
| Questions receiving Examiner Notes | ~482 (all questions in Solutions Manual) |
| Words per note set (3 annotations) | ~120 (40 per annotation) |
| Total additional words | ~57,840 |
| Additional pages | ~115 |
| V2 impact | 458 → 573 pages |

---

## 3. Evaluation

### 3.1 Value

| Criterion | Score | Reasoning |
|-----------|:-----:|-----------|
| Educational value | **8/10** | Common Mistakes and Red Flags are proven pedagogical tools. Negative examples improve retention. Interview Insight teaches meta-cognitive skills |
| Differentiation | **9/10** | No competing structured products reference offers examiner-perspective annotations. Unique selling point |
| Reader demand | **7/10** | Interview prep readers want this. Self-study readers benefit. Classroom/training use cases benefit most |

### 3.2 Effort

| Criterion | Score | Reasoning |
|-----------|:-----:|-----------|
| Generation effort | **4/10** (bad) | ~58K additional words. Adds ~6 days to Solutions Manual timeline. Each annotation must be credible — cannot be generic |
| Quality risk | **5/10** (moderate) | Common Mistakes and Red Flags must be realistic, not contrived. Risk of generating implausible "mistakes" |
| Review overhead | **4/10** (bad) | Every annotation reviewed for accuracy AND plausibility. Three additional review passes per question |

### 3.3 Maintainability

| Criterion | Score | Reasoning |
|-----------|:-----:|-----------|
| Update burden | **4/10** (bad) | Any chapter content change triggers review of: T1, T2, T3, T4, Common Mistake, Interview Insight, Red Flag. 7 items per question instead of 4 |
| Staleness risk | **6/10** | Interview Insights and Red Flags are more stable than T1-T3 (they test understanding, not specific facts). Common Mistakes may need updating as market terminology evolves |

### 3.4 Publication Impact

| Criterion | Score | Reasoning |
|-----------|:-----:|-----------|
| Page count | **3/10** (bad) | +115 pages on V2. Pushes from 458 to 573. V2 becomes larger than V1. Unbalanced |
| Reader experience | **6/10** | Useful but heavy. Per-question block grows from 4 items to 7 items. Visual clutter risk |
| Production timeline | **4/10** (bad) | +6 days on critical path |

---

## 4. Alternative: Selective Examiner Notes

Instead of all 482 questions, apply Examiner Notes to a curated subset:

| Subset | Questions | Added Words | Added Pages |
|--------|:---------:|:-----------:|:-----------:|
| Desk Questions only (1 per chapter) | ~49 | ~5,880 | ~12 |
| Desk + hardest Scenario | ~98 | ~11,760 | ~24 |
| Top 100 most important questions | 100 | ~12,000 | ~24 |

**Selective approach (Top 100):**
- Identify 100 most interview-relevant questions (2 per product)
- Apply full Examiner Notes (Common Mistake + Interview Insight + Red Flag)
- Remaining 382 questions: T1-T4 only
- Page impact: +24 pages (458 → 482). Manageable

---

## 5. Verdict

### **NO-GO for full implementation. GO for selective (Top 100).**

**Full implementation rejected because:**
- +115 pages makes V2 larger than V1 (573 vs 552). Unbalanced
- 482 × 3 annotations = high risk of generic, low-value entries for simpler questions
- +6 days on critical path
- Maintenance burden increases 75% (7 items per question vs 4)

**Selective implementation approved because:**
- +24 pages is within budget (458 → 482)
- 100 curated questions ensures each annotation is meaningful
- Interview-relevant subset aligns with highest reader demand
- +1.5 days on critical path (vs +6)
- Quality > quantity for examiner-perspective content

**Implementation:** During Solutions Manual generation (Phase 5), flag top 2 questions per product as "Examiner Notes candidates." Generate T1-T4 + Examiner Notes for those 100. T1-T4 only for remaining 382.

---

*Examiner Notes Review completed 2026-06-21.*
*VERDICT: NO-GO (full). GO (selective — Top 100 questions).*
