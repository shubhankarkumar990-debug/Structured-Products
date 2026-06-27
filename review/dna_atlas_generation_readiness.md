# DNA Atlas Generation Readiness

**Date:** 2026-06-22
**Phase:** Reference Layer Readiness Review — Phase 1
**Scope:** DNA Atlas dependency verification

---

## Check 1: Product DNA Records

49 / 49 chapters contain a §4 Product DNA table with all 12 canonical fields.

| Field | Present |
|-------|:-------:|
| Full Name | 49 / 49 |
| Abbreviation | 49 / 49 |
| Family | 49 / 49 |
| Complexity Score | 49 / 49 |
| Complexity Rationale | 49 / 49 |
| Underlying Asset Class | 49 / 49 |
| Capital Protection | 49 / 49 |
| Coupon Type | 49 / 49 |
| Maturity | 49 / 49 |
| Liquidity | 49 / 49 |
| Primary System | 49 / 49 |
| ISDA Required | 49 / 49 |

**Result: PASS**

## Check 2: DNA Atlas Fields

49 / 49 chapters contain all 7 Atlas fields below the DNA table.

| Field | Present |
|-------|:-------:|
| Primary Risk | 49 / 49 |
| Typical Buyer | 49 / 49 |
| Typical Use Case | 49 / 49 |
| Building Blocks | 49 / 49 |
| Key Hedge | 49 / 49 |
| Similar Products | 49 / 49 |
| Most Important Greek | 49 / 49 |

Total: 343 / 343 field instances.

**Result: PASS**

## Check 3: Atlas Fields Conform to Frozen Taxonomy

The 7 Atlas fields are free-text descriptive fields, not categorical. They are not subject to taxonomy normalization. The taxonomy governs the 6 Comparison Matrix categorical dimensions only.

Atlas fields are consumed as-is by the DNA Atlas generator.

**Result: PASS (not applicable — Atlas fields are free-text)**

## Check 4: Similar Products Reference Resolution

| Metric | Count |
|--------|:-----:|
| Chapters with Similar Products | 49 / 49 |
| Unique section references | 45 |
| Section references that resolve to real chapters | 45 / 45 |
| Unresolvable section references | **0** |

### Name-Only References (No Section Number)

7 products referenced by name without section numbers. These are external products not in the 49-chapter universe:

1. Capital Guaranteed Fund
2. Callable STEG variants (generic family reference)
3. ETF with options overlay
4. FX forward
5. NDF
6. Forward-starting RC (variant, not a standalone chapter)
7. VWAP selling program

**Impact:** LOW. Atlas generator can render these as name-only entries. All internal cross-references (products within the universe) have valid section numbers.

**Result: PASS WITH MINOR ISSUES** (7 name-only external products)

---

## Summary

| Check | Result |
|-------|:------:|
| 49/49 DNA records exist | **PASS** |
| 49/49 Atlas fields exist (343/343) | **PASS** |
| Atlas fields conform to taxonomy | **PASS** (N/A) |
| Similar Products references resolve | **PASS WITH MINOR ISSUES** |

**DNA Atlas generation: READY**

---

*Phase 1 complete.*
