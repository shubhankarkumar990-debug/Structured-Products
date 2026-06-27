# Product DNA Audit — Phase 1

**Date:** 2026-06-22
**Pass:** Publication Metadata Audit
**Status:** READ-ONLY — no manuscript modifications
**Scope:** All 49 chapters (§4 Product DNA)

---

## Verdict: FAIL — 4 issues require resolution before DNA Atlas generation

---

## 1. DNA Table Field Consistency

### Three template eras produce three incompatible field schemas

| Era | Chapters | Count | Header Format | Fields |
|-----|----------|:-----:|:-------------:|--------|
| **Batch 0-5 + 9-10** | 5.1.1–5.1.15, 5.2.1–5.2.8, 5.5.1, 5.6.1–5.6.12 | 36 | \*\*Field\*\* \| Value | Full Name, Abbreviation, Family, Complexity Score, Complexity Rationale, Underlying Asset Class, Capital Protection, Coupon Type, Maturity, Liquidity, Primary System, ISDA Required |
| **Batch 6-7** | 5.3.1–5.3.5, 5.4.1–5.4.4 | 9 | \*\*Field\*\* \| Value | Asset Class, Underlying, Core Building Blocks, Primary Risk, Primary Buyer, Primary Hedge, Complexity Score |
| **Batch 8** | 5.5.2–5.5.5 | 4 | Attribute \| Value | Asset class, Underlying, Product type, Complexity, Booking system, Four-leg, Key risk, Typical tenor, Coupon type |

**Impact:** DNA Atlas generation requires consistent field names. 13 chapters (27%) use non-standard schemas.

### Severity: HIGH

Batch 6-7 chapters are missing 11 of 12 standard fields. Batch 8 chapters are missing all 12 standard fields (use entirely different names and lack a "Complexity Score" field — use "Complexity" instead).

---

## 2. Complexity Score Discrepancies

### 16 of 49 chapters disagree with the canonical complexity_registry.yaml

Per registry governance (line 17): "If they disagree, this file is authoritative."

| Section | Product | Registry | Manuscript §4 | CM Complexity | Delta |
|---------|---------|:--------:|:--------------:|:-------------:|:-----:|
| 5.1.3 | Phoenix | **6** | 5 | 5 | -1 |
| 5.1.6 | CRC | **5** | 4 | 4 | -1 |
| 5.1.7 | Airbag | **4** | 3 | 3 | -1 |
| 5.1.8 | Bonus | **4** | 3 | 3 | -1 |
| 5.1.9 | FCN | **6** | 4 | 4 | -2 |
| 5.1.11 | ICN | **3** | 4 | 4 | +1 |
| 5.1.12 | Digital Note | **4** | 3 | 3 | -1 |
| 5.1.13 | Booster | **4** | 3 | 3 | -1 |
| 5.1.14 | Digital KI Put | **7** | 5 | 5 | -2 |
| 5.1.15 | Warrant | **3** | 2 | 2 | -1 |
| 5.2.2 | TRS | **5** | 4 | 4 | -1 |
| 5.2.3 | Equity Swap | **5** | 3 | 3 | -2 |
| 5.2.5 | CDS | **5** | 4 | 4 | -1 |
| 5.2.6 | XCS | **5** | 6 | 6 | +1 |
| 5.2.7 | Commodity Swap | **4** | 3 | 3 | -1 |
| 5.2.8 | VLSP | **2** | 5 | 5 | -3 |

**Worst discrepancy:** VLSP — registry=2 (correct, "simplest swap"), manuscript=5 (3-point overstatement).

**Pattern:** Manuscript and CM values are internally consistent (always match each other) but both disagree with the registry. Root cause: registry was calibrated after chapter generation but manuscript scores were never updated.

### Severity: HIGH

4 chapters missing from manuscript (Batch 8 uses "Complexity" instead of "Complexity Score"): 5.5.2 (5), 5.5.3 (7), 5.5.4 (8), 5.5.5 (10). These match registry values.

---

## 3. Family Classification Error

### All 8 Swap chapters incorrectly classified as "Equity-Linked Notes"

| Section | Product | Family (in table) | Correct Family |
|---------|---------|:------------------:|:--------------:|
| 5.2.1 | IRS | Equity-Linked Notes | **Swaps** |
| 5.2.2 | TRS | Equity-Linked Notes | **Swaps** |
| 5.2.3 | Equity Swap | Equity-Linked Notes | **Swaps** |
| 5.2.4 | Variance Swap | Equity-Linked Notes | **Swaps** |
| 5.2.5 | CDS | Equity-Linked Notes | **Swaps** |
| 5.2.6 | XCS | Equity-Linked Notes | **Swaps** |
| 5.2.7 | Commodity Swap | Equity-Linked Notes | **Swaps** |
| 5.2.8 | VLSP | Equity-Linked Notes | **Swaps** |

**Root cause:** Likely a copy-paste artifact from Batch 0 (ELN pilot) — the template carried "Equity-Linked Notes" as the Family value into the Swap batch without correction.

Additionally:
- 13 chapters (Batch 6-7 + Batch 8) have **no Family field** in their DNA table
- Registry uses abbreviated names (ELN, Swaps, CLN, SRT, STEG, Other) vs manuscript full names (Equity-Linked Notes, Credit-Linked Notes, Other)

### Severity: HIGH

Family classification is a primary axis for DNA Atlas grouping. 8 incorrect + 13 missing = 21 chapters (43%) with family field issues.

---

## 4. Other Field Consistency

### Capital Protection
- **36/49 present** (standard format)
- 13 missing (Batch 6-7 + Batch 8 have no Capital Protection field)
- Values consistent within families — all ELN notes use "Conditional" variants, all swaps use "N/A (swap)", all CLN/Other appropriate

### Coupon Type
- **36/49 present** in standard format
- Batch 8 has "Coupon type" (lowercase) — functionally present but different field name
- Batch 6-7: no Coupon Type field at all
- Values appropriate per product type

### ISDA Required
- **36/49 present** (standard format)
- 13 missing (Batch 6-7 + Batch 8)
- Values consistent: Notes = "No", Swaps = "Yes", with appropriate nuance for hybrid products

### Underlying Asset Class
- **36/49 present** as "Underlying Asset Class"
- Batch 6-7: use "Asset Class" (9 chapters)
- Batch 8: use "Asset class" (4 chapters, lowercase)
- **Semantic consistency GOOD** — values map correctly despite naming variance (all ELN = "Equity", all Swaps = "Rates/Credit/etc", all SRT/STEG = "Rates", all CLN = "Credit")

### Severity: MEDIUM

Content is semantically correct across all 49 chapters. Issue is field name inconsistency, not content errors.

---

## 5. DNA Atlas Fields (Appended to §4)

| Field | Coverage | Status |
|-------|:--------:|:------:|
| Primary Risk | 49/49 | **PASS** |
| Typical Buyer | 49/49 | **PASS** |
| Typical Use Case | 49/49 | **PASS** |
| Building Blocks | 49/49 | **PASS** |
| Key Hedge | 49/49 | **PASS** |
| Similar Products | 49/49 | **PASS** |
| Most Important Greek | 49/49 | **PASS** |

All 7 DNA Atlas fields present in all 49 chapters. Format consistent: `- Field Name: Value` under `**DNA Atlas Fields:**` header.

---

## 6. Comparison Matrix Fields (Appended to §4)

| Field | Coverage | Status |
|-------|:--------:|:------:|
| Complexity | 49/49 | **PASS** |
| Yield Potential | 49/49 | **PASS** |
| Capital Protection | 49/49 | **PASS** |
| Credit Exposure | 49/49 | **PASS** |
| Liquidity | 49/49 | **PASS** |
| Path Dependency | 49/49 | **PASS** |
| Volatility Sensitivity | 49/49 | **PASS** |
| Correlation Sensitivity | 49/49 | **PASS** |
| Client Type | 49/49 | **PASS** |
| Market Environment | 49/49 | **PASS** |

All 10 Comparison Matrix fields present in all 49 chapters. Format consistent: `- Field Name: Value` under `**Comparison Matrix Fields:**` header.

**Note:** CM Complexity values match manuscript §4 scores, NOT registry scores (same 16 discrepancies).

---

## 7. Four-Leg Product Field

| Source | Coverage | Values |
|--------|:--------:|--------|
| Batch 9-10 DNA table | 12/12 | "Yes" or "No" |
| Batch 8 DNA table | 4/4 | "No" (all CLN) |
| Batch 0-5 | 0/24 | Not present |
| Batch 6-7 | 0/9 | Not present |

16 chapters have the field, 33 do not. This is a later addition to the template.

### Severity: LOW

Four-Leg is an operational metadata field, not a classification axis. Missing values are inferable.

---

## 8. Summary of Issues

| # | Issue | Severity | Chapters Affected | Resolution |
|---|-------|:--------:|:-----------------:|------------|
| 1 | Three incompatible DNA table schemas | HIGH | 13 (Batch 6-7 + 8) | Harmonize field names to standard 12-field format |
| 2 | 16 complexity score discrepancies (registry vs manuscript/CM) | HIGH | 16 | Align manuscript + CM to registry (canonical) |
| 3 | Swap family misclassification | HIGH | 8 | Change "Equity-Linked Notes" → "Swaps" in 5.2.1–5.2.8 |
| 4 | Field name variations | MEDIUM | 13 | Normalize "Asset class" → "Underlying Asset Class", "Complexity" → "Complexity Score", etc. |

### Blocking Verdict

**Product DNA table schema harmonization is REQUIRED before DNA Atlas generation.** The DNA Atlas must read from consistent field names, and currently 27% of chapters use incompatible schemas. The 16 complexity score discrepancies and 8 family misclassifications would propagate into any generated Atlas.

---

*Phase 1 audit complete. Phase 2 (DNA Atlas Readiness) follows.*
