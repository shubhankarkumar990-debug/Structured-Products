# DNA Schema Normalization Report

**Date:** 2026-06-22
**Phase:** Publication Metadata Remediation — Phase 3
**Manuscript:** 22,621 lines (up from 22,551 pre-remediation)

---

## Summary

13 chapters normalized from non-standard DNA table schemas to the canonical 12-field format. No information lost — all original non-standard fields were either mapped to standard equivalents or already present in the DNA Atlas Fields section.

---

## Canonical Schema (12 fields)

| # | Field | Purpose |
|---|-------|---------|
| 1 | Full Name | Official product name |
| 2 | Abbreviation | Trading desk shorthand |
| 3 | Family | Product family classification |
| 4 | Complexity Score | X / 10 (matches registry) |
| 5 | Complexity Rationale | Why this score |
| 6 | Underlying Asset Class | Primary asset class |
| 7 | Capital Protection | Principal guarantee status |
| 8 | Coupon Type | Income mechanism |
| 9 | Maturity | Typical tenor range |
| 10 | Liquidity | Secondary market availability |
| 11 | Primary System | Booking/risk systems |
| 12 | ISDA Required | Documentation requirement |

---

## Batch 6-7 Normalization (9 chapters)

### Chapters: 5.3.1–5.3.5 (SRT), 5.4.1–5.4.4 (STEG)

**Old schema (7 fields):** Asset Class, Underlying, Core Building Blocks, Primary Risk, Primary Buyer, Primary Hedge, Complexity Score

**Mapping:**

| Old Field | Action | Standard Field |
|-----------|--------|---------------|
| Asset Class | Mapped | Underlying Asset Class |
| Underlying | Merged into | Underlying Asset Class (as qualifier) |
| Core Building Blocks | Preserved in | DNA Atlas → Building Blocks |
| Primary Risk | Preserved in | DNA Atlas → Primary Risk |
| Primary Buyer | Preserved in | DNA Atlas → Typical Buyer |
| Primary Hedge | Preserved in | DNA Atlas → Key Hedge |
| Complexity Score | Retained | Complexity Score |

**New fields added:** Full Name, Abbreviation, Family, Complexity Rationale, Capital Protection, Coupon Type, Maturity, Liquidity, Primary System, ISDA Required

All new field values derived from chapter content (§3, §5, §13, §15, §16, §17) and the complexity registry.

---

## Batch 8 Normalization (4 chapters)

### Chapters: 5.5.2–5.5.5 (CLN)

**Old schema (9 fields):** Asset class, Underlying, Product type, Complexity, Booking system, Four-leg, Key risk, Typical tenor, Coupon type

**Mapping:**

| Old Field | Action | Standard Field |
|-----------|--------|---------------|
| Asset class | Mapped | Underlying Asset Class |
| Underlying | Merged into | Underlying Asset Class |
| Product type | Dropped | Derivable from Full Name |
| Complexity | Renamed | Complexity Score (format: X / 10) |
| Booking system | Mapped | Primary System |
| Four-leg | Dropped | Not in canonical schema (Batch 9-10 addition) |
| Key risk | Preserved in | DNA Atlas → Primary Risk |
| Typical tenor | Mapped | Maturity |
| Coupon type | Retained | Coupon Type |

**New fields added:** Full Name, Abbreviation, Family, Complexity Rationale, Capital Protection, Liquidity, ISDA Required

---

## Information Preservation

No information was lost:

| Original Non-Standard Field | Preservation Location |
|---------------------------|----------------------|
| Core Building Blocks | DNA Atlas Fields → Building Blocks (already populated) |
| Primary Risk | DNA Atlas Fields → Primary Risk (already populated) |
| Primary Buyer | DNA Atlas Fields → Typical Buyer (already populated) |
| Primary Hedge | DNA Atlas Fields → Key Hedge (already populated) |
| Product type | Derivable from Full Name + chapter §3 |
| Four-leg | Not in canonical schema; info in chapter §16 |
| Key risk | DNA Atlas Fields → Primary Risk (already populated) |

---

## Post-Normalization Verification

| Check | Result |
|-------|:------:|
| 49/49 chapters have all 12 standard fields | **PASS** |
| 49/49 Family values correct | **PASS** |
| 49/49 Complexity Scores match registry | **PASS** |
| DNA Atlas Fields preserved (7 × 49) | **PASS** |
| Comparison Matrix Fields preserved (10 × 49) | **PASS** |

---

*Phase 3 complete.*
