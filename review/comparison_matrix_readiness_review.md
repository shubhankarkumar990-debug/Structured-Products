# Comparison Matrix Readiness Review — Phase 3

**Date:** 2026-06-22
**Pass:** Publication Metadata Audit
**Status:** READ-ONLY — no manuscript modifications
**Scope:** All 49 chapters — Comparison Matrix Fields

---

## Verdict: PASS WITH MINOR ISSUES

All 10 Comparison Matrix fields are present in all 49 chapters. Coverage is 100%. Content quality is high. Two consistency issues affect matrix rendering.

---

## 1. Field Coverage

| Field | Coverage | Format Consistency | Unique Values |
|-------|:--------:|:------------------:|:-------------:|
| Complexity | 49/49 | Numeric (n) | 9 |
| Yield Potential | 49/49 | Descriptive | 47 |
| Capital Protection | 49/49 | Categorical + qualifier | 36 |
| Credit Exposure | 49/49 | Categorical + qualifier | 18 |
| Liquidity | 49/49 | Categorical + qualifier | 23 |
| Path Dependency | 49/49 | Yes/No + descriptor | 37 |
| Volatility Sensitivity | 49/49 | Descriptive | 42 |
| Correlation Sensitivity | 49/49 | Categorical | 21 |
| Client Type | 49/49 | Categorical | 37 |
| Market Environment | 49/49 | Descriptive | 49 |

### Header Format
All 49 chapters use identical header: `**Comparison Matrix Fields:**`. No variations.

---

## 2. Field-by-Field Analysis

### 2.1 Complexity (NUMERIC — GOOD)

Format: bare integer. Range: 2–10. All 49 values present.

| Score | Count | Products |
|:-----:|:-----:|---------|
| 2 | 4 | PPN, Warrant, Structured Deposit, Forward |
| 3 | 12 | RC, DRC, Airbag, Bonus, IRS, Equity Swap, Commodity Swap, Options, ELO, DCI, Booster, Digital Note |
| 4 | 9 | KODRC, CRC, FCN, ICN, TRS, CDS, ZCL, CLN, Shark Fin |
| 5 | 8 | Phoenix, DKIP, VLSP, IR Callable, Digital CF, Vanilla STEG, Option on RC, Skew CLN |
| 6 | 6 | CRA ELN, XCS, NCRA, Callable STEG, Accumulator, Decumulator |
| 7 | 6 | Variance Swap, CRA SRT, RA STEG, FTD, Snowball, Cliquet |
| 8 | 3 | TARN STEG, NTD, WOAC |
| 10 | 1 | Synthetic CDO |

**Issue:** These values match the manuscript §4 table scores, not the canonical complexity_registry.yaml. Same 16 discrepancies identified in Phase 1.

### 2.2 Yield Potential (DESCRIPTIVE — 47 unique values)

Format: `Category (explanation)` where category is one of: None, Low, Low-Moderate, Moderate, Moderate-High, High, Very High.

| Category | Count |
|----------|:-----:|
| None / Not a yield product | 6 |
| Low / Low-Moderate | 3 |
| Moderate | 10 |
| Moderate-High | 5 |
| High | 16 |
| Very High | 5 |
| N/A (swap family) | 4 |

**Assessment:** Categories are extractable despite descriptive format. Each entry starts with a category word followed by parenthetical explanation. Matrix rendering can parse the first word/phrase.

### 2.3 Capital Protection (CATEGORICAL — 36 unique values)

Primary categories:

| Category | Count | Family |
|----------|:-----:|--------|
| 100% at maturity | 7 | PPN, CRA ELN, Digital Note, Deposit, Shark Fin, Cliquet, FCN variant |
| Conditional (with qualifier) | 11 | RC, Phoenix, DRC, KODRC, CRC, Bonus, DKIP, CLN, Snowball, WOAC, ICN |
| N/A (swap) | 6 | All swaps |
| None | 7 | Booster, Warrant, Forward, Accumulator, Decumulator, Options |
| Partial / Enhanced | 3 | Airbag, KODRC, DCI |
| Full (deposit) | 1 | Structured Deposit |

**Assessment:** Categorizable. "Conditional" is the dominant ELN pattern, appropriately qualified per product. Swap "N/A" is correct.

### 2.4 Credit Exposure (CATEGORICAL — 18 unique values)

Two variants of same concept need normalization:

| Value | Count | Issue |
|-------|:-----:|-------|
| `Issuer` | 12 | Same concept... |
| `Issuer (note format)` | 12 | ...different label |
| `Counterparty` | 4 | OK |
| `Counterparty (bilateral OTC)` | 3 | Qualifier variant |
| `Counterparty (bilateral)` | 2 | Qualifier variant |

**Normalization needed:** "Issuer" and "Issuer (note format)" represent the same exposure type. "Counterparty" variants could be collapsed to "Counterparty" with qualifiers.

### 2.5 Liquidity (CATEGORICAL — 23 unique values)

| Category | Count |
|----------|:-----:|
| Secondary market | 18 |
| OTC (various qualifiers) | 16 |
| Exchange-traded | 1 |
| Very limited | 3 |

**Normalization needed:** 7 different OTC variants (plain "OTC", "OTC — model-dependent", "OTC (very liquid)", "OTC (index tenors liquid)", etc.) could be collapsed to 3 tiers: OTC-liquid, OTC-standard, OTC-illiquid.

### 2.6 Path Dependency (YES/NO — 37 unique values)

| Category | Count |
|----------|:-----:|
| No (various qualifiers) | 15 |
| Yes (various qualifiers) | 22 |
| None (variant of No) | 2 |
| High / Extreme | 5 |

**Issue:** "No" (7x), "None" (2x), and "No (European observation…)" (3x) represent the same concept. "None" vs "No" inconsistency.

### 2.7 Volatility Sensitivity (DESCRIPTIVE — 42 unique values)

Almost entirely unique descriptions. Main patterns:

| Pattern | Count |
|---------|:-----:|
| Long vega | 5 |
| Short vega | 12 |
| Low / Minimal | 8 |
| Concentrated / Digital | 7 |
| High | 6 |
| Mixed / Complex | 11 |

**Assessment:** Descriptions are accurate but not directly comparable in a matrix. Would need simplification to a 3-5 tier scale for visual rendering.

### 2.8 Correlation Sensitivity (CATEGORICAL — well structured)

| Category | Count |
|----------|:-----:|
| None (various qualifiers) | 35 |
| Low | 3 |
| CMS rate correlation | 3 |
| Moderate-High | 3 |
| Critical | 3 |
| High | 2 |

**Assessment:** Dominated by "None" — appropriate for single-underlying products. Correlation matters only for basket/multi-asset products. Good categorical structure.

**Minor issue:** "None" (21x) vs "None (single underlying)" (5x) vs "None (single stock)" (2x) represent the same concept.

### 2.9 Client Type (CATEGORICAL — 37 unique values)

| Category | Count |
|----------|:-----:|
| Private banking | 13 |
| Institutional | 12 |
| Retail | 5 |
| Sophisticated institutional | 5 |
| Mixed | 14 |

**Assessment:** Extractable primary category despite variant qualifiers. 3-tier simplification (Retail, Private Banking, Institutional) would cover all.

### 2.10 Market Environment (DESCRIPTIVE — 49 unique values)

Every chapter has a unique market environment description. All follow the pattern "Best when/in [condition]."

**Assessment:** Content is complete and product-specific. Not reducible to a simple scale — this is inherently a descriptive field. Matrix rendering would display full text or extract first clause.

---

## 3. Consistency Issues

### Issue 1: CM Complexity vs Registry (16 discrepancies)

Same 16 discrepancies as Phase 1. CM Complexity matches manuscript §4, not the canonical registry. Resolution in Phase 1 applies here.

### Issue 2: Categorical Normalization

6 fields use inconsistent categorical labels for the same concept:

| Field | Example | Normalization |
|-------|---------|---------------|
| Credit Exposure | "Issuer" vs "Issuer (note format)" | Collapse to "Issuer" |
| Path Dependency | "No" vs "None" | Standardize to "No" |
| Correlation Sensitivity | "None" vs "None (single underlying)" | Collapse to "None" |
| Liquidity | 7 OTC variants | Collapse to OTC-tier |
| Volatility Sensitivity | 42 unique descriptions | Needs categorization |
| Client Type | "Private banking" vs "Private banking / HNW" | Collapse to primary |

### Severity: LOW-MEDIUM

These are formatting variations, not content errors. A matrix generator can handle normalization programmatically. However, manual normalization would produce a cleaner matrix.

---

## 4. Matrix Rendering Readiness

| Dimension | Raw Format | Matrix-Ready | Action Needed |
|-----------|:----------:|:------------:|---------------|
| Complexity | Numeric | **YES** | Align with registry |
| Yield Potential | Category + text | **PARTIAL** | Extract category prefix |
| Capital Protection | Category + qualifier | **PARTIAL** | Extract primary category |
| Credit Exposure | Category | **PARTIAL** | Normalize 2 variants |
| Liquidity | Category | **PARTIAL** | Collapse OTC variants |
| Path Dependency | Yes/No + descriptor | **PARTIAL** | Normalize None→No |
| Volatility Sensitivity | Descriptive | **NO** | Needs categorization pass |
| Correlation Sensitivity | Category | **PARTIAL** | Collapse None variants |
| Client Type | Category | **PARTIAL** | Extract primary category |
| Market Environment | Descriptive | **NO** | Display as full text |

**1 field fully matrix-ready** (Complexity), **7 fields partially ready** (extractable primary category), **2 fields not matrix-ready** (require simplification or full-text display).

---

## 5. Summary

| Criterion | Status |
|-----------|:------:|
| All 10 fields present in 49/49 chapters | **PASS** |
| Consistent header and bullet format | **PASS** |
| Content quality — no stubs or empty values | **PASS** |
| Numeric consistency (Complexity) | **FAIL** (16 discrepancies with registry) |
| Categorical consistency | **MINOR** (normalization needed in 6 fields) |
| Visual matrix readiness | **PARTIAL** (1/10 fully ready, 7/10 extractable, 2/10 descriptive-only) |

### Blocking Issues: NONE (beyond Phase 1 complexity score resolution)

Matrix generation can proceed with programmatic normalization. The descriptive format is richer than a simple rating scale and may be preferable for the reference document.

---

*Phase 3 audit complete. Phase 4 (Complexity Calibration) follows.*
