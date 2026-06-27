# Publication Metadata Consistency Review — Phase 5

**Date:** 2026-06-22
**Pass:** Publication Metadata Audit
**Status:** READ-ONLY — no manuscript modifications
**Scope:** Cross-system consistency across manuscript, registry, dashboard, and production artifacts

---

## Verdict: PASS WITH ISSUES — 3 systems require alignment

---

## 1. Product Naming Consistency

### 1.1 Three Naming Systems

Each product has up to 4 different names across systems:

| System | Purpose | Example (5.1.2) |
|--------|---------|-----------------|
| Chapter title | Manuscript heading | Reverse Convertible (Enhanced Return Note) |
| §4 Full Name | DNA table | Reverse Convertible |
| §4 Abbreviation | DNA table | RC |
| Registry name | complexity_registry.yaml | RC |

**24 of 49 chapter titles differ from their §4 Full Name.** Most differences are format-only (title includes abbreviation in parentheses that Full Name omits). However, 8 have substantive differences:

| Section | Chapter Title | §4 Full Name | Issue |
|---------|-------------|--------------|-------|
| 5.1.7 | Airbag / Leveraged Reverse Convertible | Airbag Note | Title uses slash-variant, DNA doesn't |
| 5.1.8 | Bonus / Participation Note | Bonus Note | Title uses slash-variant |
| 5.2.8 | Vanilla Swap (VLSP) | Vanilla Swap Plus | Title abbreviates, DNA expands "Plus" |
| 5.6.2 | Forward | Forward Contract | DNA adds "Contract" |
| 5.6.3 | Vanilla Options | Vanilla Option (Call / Put) | Title is plural, DNA is singular + qualifier |
| 5.6.9 | Shark Fin Note | Shark Fin Note (Knock-Out Capital Protected Note) | DNA adds long alternative name |
| 5.6.10 | Snowball Note | Snowball Autocallable Note | DNA adds "Autocallable" |
| 5.6.12 | Worst-of Autocallable | Worst-of Autocallable Note (Worst-of Phoenix) | DNA adds "Note" + alternative name |

### 1.2 Abbreviation Divergence

17 products have different abbreviations in §4 vs the registry:

| §4 Abbreviation | Registry Name | Type |
|-----------------|--------------|------|
| Bonus | Bonus Certificate | Variant name |
| Digital | Digital Note | Variant name |
| DKIP | Digital KI Put | Abbreviation vs short name |
| EqSwap | Equity Swap | Abbreviation vs full name |
| VarSwap | Variance Swap | Abbreviation vs full name |
| XCCY | Cross-Currency Swap | Abbreviation vs full name |
| CommSwap | Commodity Swap | Abbreviation vs full name |
| SD | Structured Deposit | Abbreviation vs full name |
| FWD | Forward | Abbreviation vs full name |
| VO | Vanilla Option | Abbreviation vs full name |
| Opt-on-RC | Option on RC | Abbreviation vs short name |
| ACCUM | Accumulator | Abbreviation vs full name |
| DECUM | Decumulator | Abbreviation vs full name |
| SHRK | Shark Fin | Abbreviation vs full name |
| SNOW | Snowball | Abbreviation vs full name |
| CLIQ | Cliquet | Abbreviation vs full name |
| WOAC | Worst-of Autocallable | Abbreviation vs full name |

**Root cause:** §4 Abbreviation field stores trading desk shorthand (EqSwap, VarSwap, ACCUM). The registry `name` field stores a readable short name. These serve different purposes and are not expected to match.

### Severity: LOW

Different naming conventions serve different audiences. However, a canonical "display name" should be established for DNA Atlas cards. Recommendation: use §4 Full Name as the display name, with §4 Abbreviation in parentheses.

---

## 2. Section Numbering

| Family | Prefix | Expected | Actual | Status |
|--------|--------|:--------:|:------:|:------:|
| ELN | 5.1 | 1–15 | 1–15 | **PASS** |
| Swaps | 5.2 | 1–8 | 1–8 | **PASS** |
| SRT | 5.3 | 1–5 | 1–5 | **PASS** |
| STEG | 5.4 | 1–4 | 1–4 | **PASS** |
| CLN | 5.5 | 1–5 | 1–5 | **PASS** |
| Other | 5.6 | 1–12 | 1–12 | **PASS** |

All 49 sections in correct sequence with no gaps or duplicates.

---

## 3. Complexity Score Alignment

### Three sources must agree:

| Source | Purpose | Authority |
|--------|---------|-----------|
| complexity_registry.yaml | Canonical scores | **AUTHORITATIVE** |
| §4 Complexity Score | Chapter DNA table | Must match registry |
| CM Complexity | Comparison Matrix | Must match registry |

**Status: 16 of 49 disagree** (same discrepancies reported in Phase 1 and Phase 4). Manuscript and CM are internally consistent but both diverge from the canonical registry.

---

## 4. Family Classification Alignment

### Registry vs Manuscript §4

| Registry Family | Manuscript §4 Family | Match? |
|----------------|---------------------|:------:|
| ELN | Equity-Linked Notes (15 chapters) | **PARTIAL** — full name vs abbreviation |
| Swaps | **Equity-Linked Notes** (8 chapters) | **WRONG** — all 8 Swaps chapters say ELN |
| SRT | (no Family field) | **MISSING** |
| STEG | (no Family field) | **MISSING** |
| CLN | Credit-Linked Notes (1 chapter: 5.5.1) | **PARTIAL** |
| CLN | (no Family field, 4 chapters: 5.5.2–5.5.5) | **MISSING** |
| Other | Other (12 chapters) | **MATCH** |

**Issues:**
1. 8 Swap chapters have wrong family ("Equity-Linked Notes" instead of "Swaps")
2. 13 chapters have no Family field (Batch 6-7 + Batch 8)
3. Full names vs abbreviations (ELN vs Equity-Linked Notes)

---

## 5. Cross-System Product Count

| System | Count | Match? |
|--------|:-----:|:------:|
| Manuscript chapters | 49 | **PASS** |
| Complexity registry entries | 49 | **PASS** |
| Generation dashboard entries | 49 | **PASS** |
| DNA Atlas Fields | 49 | **PASS** |
| Comparison Matrix Fields | 49 | **PASS** |

All systems agree on 49 products. No orphans, no missing entries.

---

## 6. DNA Table Schema Consistency (Cross-System)

### Canonical 12-field schema (from Batch 0-5 / 9-10 template):

| Field | Present In | Count |
|-------|:----------:|:-----:|
| Full Name | Batch 0-5, 9-10 | 36/49 |
| Abbreviation | Batch 0-5, 9-10 | 36/49 |
| Family | Batch 0-5, 9-10 | 36/49 |
| Complexity Score | Batch 0-5, 6-7, 9-10 | 45/49 |
| Complexity Rationale | Batch 0-5, 9-10 | 36/49 |
| Underlying Asset Class | Batch 0-5, 9-10 | 36/49 |
| Capital Protection | Batch 0-5, 9-10 | 36/49 |
| Coupon Type | Batch 0-5, 8, 9-10 | 40/49 |
| Maturity | Batch 0-5, 9-10 | 36/49 |
| Liquidity | Batch 0-5, 9-10 | 36/49 |
| Primary System | Batch 0-5, 9-10 | 36/49 |
| ISDA Required | Batch 0-5, 9-10 | 36/49 |

### Non-standard schemas:

**Batch 6-7 (9 chapters: SRT + STEG):** Use 7 different fields: Asset Class, Underlying, Core Building Blocks, Primary Risk, Primary Buyer, Primary Hedge, Complexity Score. Missing 11 of 12 standard fields.

**Batch 8 (4 chapters: CLN 5.5.2–5.5.5):** Use `Attribute | Value` header with 9 different field names: Asset class, Underlying, Product type, Complexity, Booking system, Four-leg, Key risk, Typical tenor, Coupon type. Missing all 12 standard fields.

---

## 7. Summary of Issues

| # | Issue | Severity | Scope | Required Action |
|---|-------|:--------:|:-----:|----------------|
| 1 | 16 complexity scores disagree with registry | **HIGH** | 16 chapters | Align §4 + CM to registry |
| 2 | 8 Swap chapters have wrong Family value | **HIGH** | 8 chapters | Change to "Swaps" |
| 3 | 13 chapters missing standard DNA table fields | **HIGH** | 13 chapters | Add missing fields using standard schema |
| 4 | 3 DNA table schemas coexist | **MEDIUM** | 13 chapters | Normalize to standard 12-field schema |
| 5 | 8 substantive product name differences | **LOW** | 8 chapters | Establish canonical display name convention |
| 6 | 17 abbreviation differences (§4 vs registry) | **LOW** | 17 chapters | Not a conflict — different purposes |
| 7 | CM categorical value normalization | **LOW** | ~30 values | Programmatic normalization at generation time |
| 8 | 7 Similar Products missing section references | **LOW** | 7 chapters | Add section numbers |

### Issues 1-3 are BLOCKING for DNA Atlas generation.
### Issues 4-8 are NON-BLOCKING but should be addressed for publication quality.

---

*Phase 5 audit complete. Final verdict follows.*
