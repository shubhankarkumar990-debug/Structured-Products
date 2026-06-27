# Batch 10 Generation Plan

**Date:** 2026-06-21
**Status:** BLOCKED — awaiting product definitions for #45-#49
**Authority:** Framework Master v1.3.1 (frozen)

---

## 1. Current Universe Audit

### Family Completion Status

| Family | Section | Products | Status | Coverage Assessment |
|--------|---------|:--------:|:------:|---------------------|
| ELN | 5.1 | 15 | COMPLETE | Deep — RC variants, autocallables, callable, digital, warrants |
| Swaps | 5.2 | 8 | COMPLETE | Broad — IRS, TRS, equity, variance, CDS, XCCY, commodity, VLSP |
| SRT | 5.3 | 5 | COMPLETE | Standard — callable, ZCL, range accrual, digital |
| STEG | 5.4 | 4 | COMPLETE | Full — vanilla, RA, callable, TARN |
| CLN | 5.5 | 5 | COMPLETE | Deep — vanilla through CDO tranche |
| Other | 5.6 | 7 | COMPLETE | Broad — deposits, forwards, options, accumulators |
| **Total** | | **44** | | |

### Coverage Gaps

Products commonly found on structured products desks but absent from the universe:

| Product | Gap Type | Why Notable |
|---------|----------|-------------|
| Worst-of Autocallable | Multi-asset variant of Phoenix | Most-traded retail structured product globally |
| Snowball Note | Cumulative coupon autocallable | Popular in Asian markets; different mechanics from Phoenix/TARN |
| Dual Currency Investment (DCI) | FX structured deposit | Standard private banking product; FX underlying not yet covered |
| Shark Fin Note | Barrier-capped PPN variant | Unique barrier-reduces-but-preserves-return mechanics |
| Twin-Win / Absolute Return | Absolute value payoff | Only structure offering symmetric positive participation |
| Cliquet / Ratchet | Periodic reset with lock-in | Path-dependent with unique serial option decomposition |
| Inflation-Linked Note | CPI underlying | Macro-linked; introduces inflation derivatives |
| FX Accumulator | FX variant of Accumulator | Extends Accumulator concept to second asset class |

---

## 2. Proposed Candidates (5 of 8)

Ranked by: (a) market relevance, (b) conceptual gap filled, (c) dependency fit, (d) educational value.

### Candidate A: Worst-of Autocallable

| Field | Value |
|-------|-------|
| Family | ELN (5.1.16) or Other (5.6.8) |
| Estimated complexity | 8 |
| Depends on | Phoenix (5.1.3), Correlation (1.6) |
| New concepts | Multi-asset worst-of mechanics, correlation dependency in payoff, quanto adjustment |
| Why include | Largest gap in the universe. Globally the most issued structured product. All desk staff encounter it. |
| Product code | WOAC |
| Analogy risk | Must avoid overlap with Phoenix employment contract |

### Candidate B: Snowball Note

| Field | Value |
|-------|-------|
| Family | ELN (5.1.16/17) or Other (5.6.8/9) |
| Estimated complexity | 7 |
| Depends on | Phoenix (5.1.3), FCN (5.1.9) |
| New concepts | Cumulative coupon accumulation (different from TARN — adds up missed coupons, not received coupons) |
| Why include | Dominant product in Asia-Pacific markets. Shows how coupon memory works differently from Phoenix memory. |
| Product code | SNOW |
| Analogy risk | Must avoid overlap with TARN coffee shop loyalty card |

### Candidate C: Dual Currency Investment (DCI)

| Field | Value |
|-------|-------|
| Family | Other (5.6.8/9/10) |
| Estimated complexity | 3 |
| Depends on | Vanilla Options (5.6.3), Structured Deposit (5.6.1) |
| New concepts | FX underlying, FX option in deposit wrapper, conversion risk |
| Why include | Fills the FX gap — no product currently covers FX derivatives. Standard private banking product. |
| Product code | DCI |
| Analogy risk | Low — FX domain largely untapped |

### Candidate D: Shark Fin Note

| Field | Value |
|-------|-------|
| Family | ELN or Other |
| Estimated complexity | 4 |
| Depends on | PPN (5.1.1), barrier concepts (1.3) |
| New concepts | Barrier cap that reduces (not eliminates) participation. Rebate on breach. |
| Why include | Shows barrier as participation modifier, not binary kill switch. Popular in Asia. |
| Product code | SHRK |
| Analogy risk | Low |

### Candidate E: Cliquet / Ratchet Note

| Field | Value |
|-------|-------|
| Family | ELN or Other |
| Estimated complexity | 7 |
| Depends on | Vanilla Options (5.6.3), forward start concept |
| New concepts | Forward-starting options, periodic reset, local cap/floor, global cap/floor, serial option decomposition |
| Why include | Unique path-dependent structure. Decomposition into forward-starting options is educational gold. |
| Product code | CLIQ |
| Analogy risk | Low |

### Alternate: Twin-Win / Absolute Return

| Field | Value |
|-------|-------|
| Family | ELN or Other |
| Estimated complexity | 5 |
| Depends on | PPN (5.1.1), barrier concepts (1.3) |
| New concepts | Absolute return payoff. Down-and-in barrier kills symmetry. |
| Why include | Only structure in the market offering participation in both directions. Unique payoff chart. |
| Product code | TWIN |
| Analogy risk | Low |

### Alternate: Inflation-Linked Note

| Field | Value |
|-------|-------|
| Family | Other |
| Estimated complexity | 4 |
| Depends on | PPN (5.1.1), yield curve concepts (1.7) |
| New concepts | CPI as underlying, breakeven inflation, real vs nominal rates |
| Why include | Introduces macro underlying. Relevant during inflation cycles. |
| Product code | INFN |
| Analogy risk | Low |

---

## 3. Generation Framework (Once Products Defined)

### Section Numbering

Products #45-#49 should be assigned to existing families or a new sub-family:

| Option | Sections | Impact |
|--------|----------|--------|
| Extend existing families | 5.1.16+, 5.6.8+ | Minimal — appends to existing families |
| New family 5.7 | 5.7.1–5.7.5 | Clean — new family heading needed |
| Mixed | Some in 5.1, some in 5.6, some in 5.7 | Flexible — follows product nature |

### Generation Order Principles

1. **Complexity ascending** within the batch (proven pattern from Batches 1-9)
2. **Dependency ordering** — products requiring concepts from other new products go last
3. **Family grouping** — if multiple products join the same family, generate consecutively

### Per-Chapter Requirements (v1.3.1)

Each of the 5 chapters must include:
- 22 sections per v1.3.1 template
- 6 visual specifications (2 P1 + 2 P2 + 2 P3)
- 8-role Who Touches (Sales/Structuring/Trading/Quant/Risk/Ops/Legal/Tech)
- DNA Atlas fields
- Comparison Matrix fields
- Knowledge Check (5 RQ + 3 SQ + 1 DQ)
- Interview Layer candidates (top 3)
- Examiner Notes candidates (top 2)
- Cross-reference integrity (§22)
- Unique analogy domain (no collision with 44 used + 25 reserved)

### Estimated Output

- 5 chapters × ~300 lines = ~1,500 lines added to manuscript
- 5 × 6 = 30 new visual specifications
- 5 × 9 = 45 new questions
- 5 new analogy domains
- 5 new complexity scores
- 5 new product codes for question IDs

---

## 4. Decision Required

**Products #45-#49 are undefined.** Choose one:

**Option 1 — Define 5 products from candidates above.** Recommended selection: A (Worst-of Autocallable), B (Snowball), C (DCI), D (Shark Fin), E (Cliquet). This fills the largest market coverage gaps.

**Option 2 — Redefine target to 44 products.** Accept that the universe is 44, not 49. Fix the "49" references across all documents. No Batch 10 needed.

**Option 3 — Define custom products.** Specify 5 products not listed above.

Batch 10 generation cannot proceed until this decision is made.

---

*Batch 10 Generation Plan created 2026-06-21. BLOCKED pending product definition.*
