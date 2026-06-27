# Product Comparison Matrix — Design Review

**Date:** 2026-06-21
**Proposed Section:** Part 6.7 (appendix to DNA Atlas) or standalone Part X
**Framework:** v1.3.1 (FROZEN)
**Purpose:** Cross-family product comparison across 10 dimensions
**Implementation:** After 49/49, after harmonization

---

## 1. Concept

Product chapters teach depth. The DNA Atlas teaches quick-reference. The Comparison Matrix teaches *relative positioning* — how products compare across dimensions readers care about.

**Key question it answers:** "If I care about [dimension], which products should I look at?"

---

## 2. Matrix Dimensions — 10 Axes

| # | Dimension | Scale | Source |
|:-:|-----------|-------|--------|
| 1 | **Complexity** | 1-10 integer | complexity_registry.yaml |
| 2 | **Yield Potential** | None / Low / Medium / High / Very High | §7-§8 coupon analysis |
| 3 | **Capital Protection** | Full / Conditional (%) / None | §6 |
| 4 | **Credit Exposure** | None / Issuer Only / Single Name / Basket / Portfolio | §10 |
| 5 | **Liquidity** | Daily / Periodic / Maturity Only / OTC Negotiated | §13 lifecycle |
| 6 | **Path Dependency** | None / Low / Medium / High | §5 mechanics |
| 7 | **Volatility Sensitivity** | Low / Medium / High + direction (long/short vol) | §11 Greeks |
| 8 | **Correlation Sensitivity** | None / Low / Medium / High + direction | §11 Greeks |
| 9 | **Client Type** | Retail / HNW / Institutional / Interbank | §3 typical buyer |
| 10 | **Typical Market Environment** | Bull / Bear / Sideways / High Vol / Low Rate / Rising Rate | §3 use case |

---

## 3. Matrix Structure

### 3.1 Master Matrix (49 × 10)

| Product | Cmplx | Yield | Capital | Credit | Liq | Path | Vol | Corr | Client | Market |
|---------|:-----:|:-----:|:-------:|:------:|:---:|:----:|:---:|:----:|:------:|:------:|
| PPN | 2 | Low | Full | Issuer | Mat | None | Long | None | Retail | Low Rate |
| RC | 3 | High | Cond 70% | Issuer | Mat | Low | Short | None | HNW | Sideways |
| Phoenix AC | 6 | High | Cond 60% | Issuer | Periodic | High | Short | None | HNW | Sideways |
| IRS | 3 | N/A | None | Cpty | OTC | None | None | None | Inst | Rising |
| Vanilla CLN | 4 | Med | None | Single | OTC | None | None | None | Inst | Stable |
| FTD | 7 | VHigh | None | Basket | OTC | None | None | High | Inst | Stable |
| ... | ... | ... | ... | ... | ... | ... | ... | ... | ... | ... |

### 3.2 Filtered Views

| View Name | Filter | Audience |
|-----------|--------|----------|
| "Best for retail" | Client = Retail | Sales |
| "Capital protected" | Capital = Full or Conditional ≥80% | Risk-averse investors |
| "High yield" | Yield = High or Very High | Yield-seeking investors |
| "Credit products" | Credit ≠ None, ≠ Issuer Only | Credit desk |
| "Simple products" | Complexity ≤ 3 | Beginners |
| "Path dependent" | Path = Medium or High | Traders, risk |
| "Correlation sensitive" | Correlation ≠ None | Correlation desk |
| "Volatility plays" | Vol = High | Vol desk |

---

## 4. Sorting Methodology

### 4.1 Primary Sort Options

Readers can mentally sort by any column. In print, provide pre-sorted tables:

| Sort | Order | Use Case |
|------|-------|----------|
| By complexity (default) | 1→10 | Learning progression |
| By yield | VHigh→None | Yield comparison |
| By capital protection | Full→None | Risk comparison |
| By family | ELN→Swaps→SRT→STEG→CLN→Other | Family grouping |

### 4.2 Scoring Rubric

Each qualitative dimension needs a consistent rubric:

**Yield Potential:**

| Rating | Criteria |
|--------|---------|
| None | No coupon (forward, option) |
| Low | ≤3% or participation-based (PPN) |
| Medium | 3-6% (CLN, moderate AC) |
| High | 6-10% (RC, Phoenix, FTD) |
| Very High | >10% or highly leveraged (CDO equity, Accumulator) |

**Path Dependency:**

| Rating | Criteria |
|--------|---------|
| None | Payoff depends only on final level (PPN, Forward) |
| Low | One observation point matters (RC — barrier at maturity) |
| Medium | Multiple observation points (periodic autocall) |
| High | Continuous or daily observation (TARN, Accumulator, range accrual) |

---

## 5. Visual Presentation

### 5.1 Print Format

| Visual | Type | Purpose |
|--------|------|---------|
| Master matrix table | Large table | Primary reference (49 rows × 10 columns) |
| Heat map version | Color-coded table | Visual scanning — darker = more (complexity, yield, risk) |
| Scatter plots (2D) | Chart | Complexity vs Yield, Capital Protection vs Yield, etc. |
| Radar charts | Per-product | 10-axis radar showing product profile shape |

### 5.2 Visual Assets

| # | Visual | Type | Tool |
|:-:|--------|------|------|
| 1 | Master matrix (full) | Table | Figma |
| 2 | Heat map overlay | Table | Figma/Python |
| 3 | Complexity vs Yield scatter | Scatter | Python |
| 4 | Capital Protection vs Yield scatter | Scatter | Python |
| 5 | Complexity vs Path Dependency scatter | Scatter | Python |
| 6 | Sample radar charts (6, one per family) | Radar | Python |
| 7 | Filtered view examples (3) | Table subset | Figma |

**Total: 7 visual assets.**

---

## 6. Update Process

| Trigger | Action |
|---------|--------|
| New product added | Add row to matrix. Score all 10 dimensions. Regenerate visuals |
| Dimension score revised | Update cell. Regenerate affected sorted views |
| New dimension proposed | Assess against existing 10. Add only if non-redundant |

**Update effort per product: ~30 minutes.** Scoring rubric ensures consistency.

---

## 7. Estimates

| Metric | Value |
|--------|:-----:|
| Matrix size | 49 products × 10 dimensions = 490 cells |
| Scoring rubrics | 10 (one per dimension) |
| Pre-sorted views | 4 |
| Filtered views | 8 |
| Word count | ~5,000 (rubrics + commentary) |
| Pages | ~12 (matrix + views + scatter plots) |
| Visual assets | 7 |
| Effort | 4 days (scoring + visuals + validation) |

---

## 8. Assessment

| Criterion | Score |
|-----------|:-----:|
| Educational impact | HIGH — enables cross-family comparison thinking |
| Effort | MEDIUM — systematic but template-driven |
| Publication value | VERY HIGH — no competing reference offers this |
| Reader value | VERY HIGH — sales, structuring, and interview preparation |
| Risk | LOW — additive, derived from existing chapter data |

**Recommendation: PROCEED.** Pair with DNA Atlas for maximum reference utility.

---

*Product Comparison Matrix Design Review completed 2026-06-21.*
