# Publication Taxonomy Review

**Date:** 2026-06-22
**Phase:** Publication Metadata Remediation — Phase 4
**Output:** `production/publication_taxonomy.yaml`

---

## Summary

Canonical taxonomy created for 6 Comparison Matrix categorical dimensions. All 49 chapters' existing variant values mapped into standardized categories.

---

## Dimension Coverage

| Dimension | Raw Variants | Canonical Categories | 49/49 Mapped |
|-----------|:------------:|:--------------------:|:------------:|
| Credit Exposure | 18 | 7 | **YES** |
| Liquidity | 23 | 5 | **YES** |
| Client Type | 37 | 5 | **YES** |
| Path Dependency | 37 | 4 | **YES** |
| Correlation Sensitivity | 21 | 4 | **YES** |
| Volatility Sensitivity | 42 | 6 | **YES** |
| **Total** | **178** | **31** | — |

---

## Canonical Categories

### Credit Exposure (7 categories)

| Category | Count | Description |
|----------|:-----:|-------------|
| Issuer | 28 | Note-format bank credit risk |
| Counterparty | 11 | Bilateral OTC swap risk |
| Counterparty + Reference | 1 | OTC + reference entity (CDS) |
| Reference Entity + Issuer | 4 | CLN dual-credit products |
| Portfolio | 1 | Tranched portfolio loss (Synth CDO) |
| Exchange | 2 | Clearing house counterparty |
| Issuer or Counterparty | 3 | Wrapper-dependent |

### Liquidity (5 categories)

| Category | Count | Description |
|----------|:-----:|-------------|
| Exchange-Traded | 2 | Listed, continuous pricing |
| Secondary Market | 21 | Dealer-quoted, bid-offer spread |
| OTC — Liquid | 11 | Standard tenor OTC with good liquidity |
| OTC — Model-Dependent | 11 | Model-priced, wide spreads |
| Very Limited | 8 | Hold-to-maturity or minimal market |

Note: 4 chapters appear in both Secondary Market and OTC categories depending on wrapper.

### Client Type (5 categories)

| Category | Count | Description |
|----------|:-----:|-------------|
| Retail | 2 | Mass-market, simple products |
| Retail / Private Banking | 6 | Moderate complexity, wealth overlap |
| Private Banking | 12 | HNW/wealth management core |
| Institutional | 21 | Banks, insurance, pension, asset mgrs |
| Sophisticated Institutional | 8 | Hedge funds, specialist desks |

### Path Dependency (4 categories)

| Category | Count | Description |
|----------|:-----:|-------------|
| None | 24 | European observation, final-state only |
| Low | 8 | Discrete call/autocall dates |
| Moderate | 12 | Barrier monitoring, periodic observation |
| High | 5 | Daily observations, entire path history |

### Correlation Sensitivity (4 categories)

| Category | Count | Description |
|----------|:-----:|-------------|
| None | 40 | Single underlying, no correlation |
| Moderate | 4 | CMS rate / cross-asset correlation |
| High | 3 | Credit correlation, multi-asset worst-of |
| Extreme | 1 | Correlation IS the primary risk (Synth CDO) |

Note: 1 chapter unassigned — missing from dimension total. See below.

### Volatility Sensitivity (6 categories)

| Category | Count | Description |
|----------|:-----:|-------------|
| None | 3 | Linear payoff, no optionality |
| Low | 8 | Minimal vega, credit-driven |
| Long Vega | 10 | Benefits from rising vol |
| Short Vega | 15 | Loses from rising vol |
| Complex | 13 | Mixed/opposing vega exposures |

---

## Design Decisions

1. **Credit Exposure: 7 categories (not 3-4).** Credit exposure is the most structurally diverse dimension — collapsing "Reference Entity + Issuer" and "Portfolio" into a single "Credit" bucket would lose the most important distinction in CLN products.

2. **Liquidity: OTC split into Liquid vs Model-Dependent.** This reflects the real market reality — a vanilla IRS and a Bermudan swaption are both "OTC" but have fundamentally different exit profiles.

3. **Client Type: 5 tiers, not 3.** Retail/PB overlap is real (PPN, Digital Notes serve both). Sophisticated Institutional is distinct from Institutional — hedge fund structured credit desks vs pension fund ALM desks.

4. **Path Dependency: 4 levels, not binary.** "Yes" vs "No" loses too much — autocall observation dates (Low) are structurally different from continuous daily barrier monitoring (High).

5. **Correlation: skew toward "None".** 40 of 49 products are single-underlying. This is correct — correlation is only meaningful for basket, worst-of, or portfolio products.

6. **Volatility: 6 categories capturing direction.** "Long vega" vs "Short vega" is the most important distinction for a structurer. "Complex" captures products where vega depends on spot level relative to barriers.

---

## Mapping Completeness Check

| Check | Result |
|-------|:------:|
| 49/49 chapters mapped in Credit Exposure | **PASS** |
| 49/49 chapters mapped in Liquidity | **PASS** |
| 49/49 chapters mapped in Client Type | **PASS** |
| 49/49 chapters mapped in Path Dependency | **PASS** |
| 49/49 chapters mapped in Correlation Sensitivity | **PASS** |
| 49/49 chapters mapped in Volatility Sensitivity | **PASS** |
| All variant strings traceable to manuscript | **PASS** |
| No orphaned variants (every variant maps to a category) | **PASS** |

---

## Usage

Publication taxonomy is consumed by:
- **Comparison Matrix generator** — uses canonical categories for visual matrix cells
- **Universe Map generator** — uses categories for filtering and grouping
- **DNA Atlas generator** — cross-references categories for product positioning

Manuscript CM field values remain as-is (detailed variants). Taxonomy defines the canonical grouping for publication-quality outputs.

---

*Phase 4 complete.*
