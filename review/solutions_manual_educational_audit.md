# Solutions Manual — Educational Audit

**Date:** 2026-06-22
**Auditor:** Independent Quality Gate
**Input:** `production/solutions_manual.md` (2,082 lines, 40 scenarios)

---

## 1. Scenario Depth Classification

Each scenario classified by decision richness:

| Depth | Definition | Count | Scenarios |
|-------|-----------|:-----:|-----------|
| **Multi-candidate genuine comparison** | ≥3 candidates, real trade-offs, reader must weigh dimensions | 11 | 1.1, 1.2, 1.3, 2.1, 2.4, 2.5, 3.2, 4.4, 5.1, 6.1, 8.3 |
| **Dual-path conditional** | 2 candidates, recommendation splits by context ("A for X, B for Y") | 6 | 1.5, 2.6, 3.1, 5.2, 7.1, 8.4 |
| **Upgrade path** | 1 clear winner, scenario teaches WHY the upgrade over simpler | 7 | 2.2, 2.3, 2.7, 3.3, 3.5, 4.2, 6.4 |
| **Single-product destination** | Only 1 product fits; scenario is "here's when to use X" | 16 | 1.4, 3.4, 4.1, 4.3, 4.5, 5.3, 5.4, 5.5, 6.2, 6.3, 7.2, 7.3, 7.4, 7.5, 8.1, 8.2 |

**Finding: 16 of 40 scenarios (40%) have a single candidate.** The rejected alternatives table mitigates this — but the core decision ("which product?") is predetermined. Educational value comes from the rejection reasoning and the Common Mistake, not from comparative selection.

---

## 2. Strongest Scenarios (Top 8)

Ranked by transferable insight density:

### Tier 1 — Teaches thinking that transfers to novel situations

| Rank | Scenario | Why It's Strong |
|:----:|----------|----------------|
| 1 | **5.3/5.4 (FTD/NTD)** | Correlation reversal — genuinely counter-intuitive. Low corr increases FTD risk, high corr increases NTD risk. Opposite of equity diversification. This insight transfers to ANY basket product. |
| 2 | **6.1 (VO vs VarSwap)** | Convexity trap. 2× vol = 4× loss on VarSwap short. Volmageddon reference. Teaches the principle that payoff shape matters more than direction. |
| 3 | **6.4 (RC as vol selling)** | Reframes a familiar product. Reader thinks RC = yield product. Scenario reveals it's embedded short put = vol selling. Changes how reader views ALL structured coupons. |
| 4 | **1.2 (Protection + Income)** | Demonstrates that "capital protection AND income" isn't contradictory. 14 products offer both. Breaks a common misconception. |

### Tier 2 — Teaches product-selection reasoning

| Rank | Scenario | Why It's Strong |
|:----:|----------|----------------|
| 5 | **2.1 (Bullish → RC)** | Clean 3-way comparison (RC/DRC/KODRC). Regime note shows RC fails in low-vol. Desk note adds economics dimension. All 4 layers working together. |
| 6 | **2.4 (Phoenix vs FCN)** | Contingent vs guaranteed coupon — identical complexity, opposite risk profiles. The "income certainty" insight applies to all contingent products. |
| 7 | **1.1 (PPN vs SD vs SHRK)** | Genuine 3-way with different protection mechanisms. Regime note about PPN participation in low-rate environments is practical. |
| 8 | **8.4 (WOAC max yield)** | Full 3-rung ladder from RC→Phoenix→WOAC. Each step up is a clear risk escalation. Correlation premium concept transfers broadly. |

---

## 3. Weakest Scenarios (Bottom 8)

Ranked by lookup-table behavior:

| Rank | Scenario | Problem | Severity |
|:----:|----------|---------|:--------:|
| 1 | **4.3 (ZCL)** | One candidate. Niche use case (pension liability matching). Scenario teaches "ZCL exists" more than decision-making. | MEDIUM |
| 2 | **8.1 (FWD)** | One candidate. "Lock price" → Forward. No decision to make. Ladder says "N/A — no simpler derivative exists." | MEDIUM |
| 3 | **8.2 (SD)** | One candidate. "Want deposit insurance" → SD. The only insight is SD vs PPN distinction (covered in Common Mistake). | MEDIUM |
| 4 | **7.2 (CommSwap)** | One candidate. "Commodity hedge" → CommSwap. Basis risk is the only non-trivial insight. | LOW |
| 5 | **7.3 (XCCY)** | One candidate. "Cross-currency debt" → XCCY. Cross-currency basis point is valuable but scenario is thin. | LOW |
| 6 | **3.3 (Callable STEG)** | Direct upgrade from 3.1. Scenario is "same as Vanilla STEG but accept call risk." Limited new reasoning. | LOW |
| 7 | **4.5 (Digital CF)** | One candidate for rate digital. Scenario distinguishes from range accrual (useful) but shallow compared to Cat 2 digital scenarios. | LOW |
| 8 | **7.5 (DECUM)** | Mirror of 7.4 (ACCUM). Reader who understood ACCUM gains little from the reverse case beyond "gearing works both ways." | LOW |

**Mitigation:** Even weak scenarios have Common Mistake and Regime Note elements that add value. The weakness is in the DECISION layer, not the educational packaging.

---

## 4. Repetitive Reasoning Patterns

### Pattern 1: "Complexity exceeds cap" rejection
Used in: 1.1, 1.3, 1.5, 2.1, 2.3, 2.4, 2.5, 3.1, 3.2, 3.3, 4.4, 8.3
**Frequency: 12 of 40 scenarios**
**Assessment:** Mechanically correct but formulaic. After the third instance, reader has absorbed the lesson. However, removing it would break the template consistency.

### Pattern 2: "Wrong asset class" rejection
Used in: 2.7, 3.1, 4.1, 4.3, 4.4, 4.5, 5.1, 7.2, 7.3
**Frequency: 9 of 40 scenarios**
**Assessment:** Necessary but predictable. Equity product rejected in rates scenario is obvious.

### Pattern 3: "Client explicitly wants [opposite]" rejection
Used in: 1.3, 2.2, 2.3, 3.3
**Frequency: 4 of 40 scenarios**
**Assessment:** Valuable — teaches that the client's stated preference overrides the structurer's default. Not overused.

### Pattern 4: "No coupon / wrong cash flow" rejection
Used in: 1.2, 1.3, 2.1, 2.6, 4.2, 4.3
**Frequency: 6 of 40 scenarios**
**Assessment:** Step 2 (Cash Flow) doing its job. Natural and not repetitive.

### Repetition Severity

| Pattern | Frequency | Adds Value After 3rd Use? | Verdict |
|---------|:---------:|:-------------------------:|---------|
| Complexity cap | 12/40 | NO — mechanical | ACCEPTABLE (template consistency) |
| Wrong asset | 9/40 | NO — predictable | ACCEPTABLE (template consistency) |
| Client preference | 4/40 | YES — teaches listening | GOOD |
| Cash flow mismatch | 6/40 | YES — reinforces Step 2 | GOOD |

---

## 5. Transferable Thinking Assessment

Scenarios that teach principles applicable beyond the specific products:

| Principle | Where Taught | Transfer Value |
|-----------|-------------|:--------------:|
| Payoff convexity (2× vol = 4× loss) | 6.1 (VarSwap) | **HIGH** — applies to any non-linear product |
| Correlation reversal in baskets | 5.3/5.4 (FTD/NTD) | **HIGH** — applies to CDO, WOAC, any basket |
| Embedded vol selling in structures | 6.4 (RC), Anti-Instinct #3 | **HIGH** — reframes ALL coupon products |
| Protection ≠ guaranteed | 1.1 (PPN vs RC), AP-1 | **HIGH** — most common junior mistake |
| Regime sensitivity changes recommendation | §1.3, every Regime Note | **HIGH** — core structurer skill |
| Issuer call = worst timing for investor | 2.6, 3.3, AP-12 | **MEDIUM** — specific to callable |
| Income risk shifts from principal to coupon | 1.2 | **MEDIUM** — applies to all protected income |
| Liquidity of complex products | AP-17 (SNOW) | **MEDIUM** — applies to all exotics |
| Desk economics as tiebreaker | §1.5, selective Desk Notes | **MEDIUM** — practical structurer insight |
| Guaranteed minimum ≠ guaranteed | 1.4 (Bonus barrier) | **MEDIUM** — applies to all barrier products |

**Assessment: The Solutions Manual teaches 6 high-transfer principles and 4 medium-transfer principles.** This exceeds the minimum bar for educational value.

---

## 6. Lookup Table Detection

A scenario behaves like a lookup table when: (a) one candidate, (b) no conditional reasoning, (c) the reader could find the same answer from the Quick Reference table in Part 4.

| Scenario | Single Candidate? | Quick Ref Equivalent? | Lookup Table? |
|----------|:-----------------:|:---------------------:|:-------------:|
| 1.4 (Bonus) | YES | YES — "Min return + upside" → Bonus | **YES** |
| 4.3 (ZCL) | YES | YES — "Liability matching" → ZCL | **YES** |
| 8.1 (FWD) | YES | YES — "Price lock" → FWD | **YES** |
| 8.2 (SD) | YES | YES — "Deposit protection" → SD | **YES** |
| 3.4 (TARN STEG) | YES | YES — "Target steepener" → TARN STEG | **PARTIAL** (target concept adds value) |
| 6.2 (Opt-on-RC) | YES | YES — "Deferred RC entry" → Opt-on-RC | **PARTIAL** (compound option concept) |
| 7.4 (ACCUM) | YES | YES — "Share accumulation" → ACCUM | **PARTIAL** (gearing concept) |
| 7.5 (DECUM) | YES | YES — "Share disposal" → DECUM | **PARTIAL** (mirror of ACCUM) |

**Pure lookup table scenarios: 4 of 40 (10%)**
**Partial lookup table: 4 of 40 (10%)**
**Total at-risk: 8 of 40 (20%)**

**Mitigating factors in all 8:** Common Mistake block, Regime Note, and Rejection Table add reasoning that the Quick Reference table doesn't provide. The educational value is diminished but not zero.

---

## 7. Verdict

| Dimension | Score | Notes |
|-----------|:-----:|-------|
| Strongest scenario quality | **9/10** | FTD/NTD correlation, VarSwap convexity, RC-as-vol are excellent |
| Weakest scenario floor | **5/10** | 4 pure lookup scenarios drag the bottom |
| Repetitive pattern severity | **7/10** | Complexity-cap rejection is formulaic but template-driven |
| Transferable thinking density | **8/10** | 6 high-transfer principles is strong |
| Lookup table contamination | **7/10** | 10% pure lookup is borderline acceptable |

**Overall Educational Score: 7.2/10**

**Primary risk:** 40% of scenarios have single candidates. The rejection tables and common mistakes provide mitigation, but the decision layer is thinnest where it matters most — at the point of selection.

**This is NOT a blocker.** The single-candidate scenarios exist because the 49-product universe genuinely has specialist products with no alternatives (CDO, TARN STEG, ZCL). The artifact teaches decisions where decisions exist and teaches product recognition where products are unique.

---

*Educational audit complete. 2026-06-22.*
