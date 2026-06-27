# Publication Identifier Standard

**Date:** 2026-06-21
**Status:** DEFINED. Not yet retrofitted.
**Purpose:** Stable, unique identifiers for all referenceable elements across V1, V2, and Digital Supplement.

---

## 1. Identifier Architecture

All identifiers follow a common pattern:

```
{TYPE}-{LOCATION}-{SEQUENCE}
```

| Component | Format | Description |
|-----------|--------|-------------|
| TYPE | 2-4 uppercase letters | Element type prefix |
| LOCATION | Section number or Part code | Where the element lives |
| SEQUENCE | 2-digit zero-padded | Sequential within scope |

---

## 2. Figure IDs

**Prefix:** `FIG`

**Format:** `FIG-{SECTION}-{SEQUENCE}`

| Context | Example | Meaning |
|---------|---------|---------|
| Product chapter | `FIG-5.1.1-01` | First figure in PPN chapter |
| Product chapter | `FIG-5.1.1-06` | Sixth figure in PPN chapter (last P3 visual) |
| Front matter | `FIG-FM-01` | First front matter figure |
| Building blocks | `FIG-1.2-03` | Third figure in Options From Zero |
| DNA Atlas | `FIG-6.1-01` | First figure in ELN DNA cards |

**Rules:**
- 6 figures per product chapter (FIG-x.y.z-01 through -06)
- Priority encoded in sequence: 01-02 = P1, 03-04 = P2, 05-06 = P3
- Front matter uses `FM` as location
- Back matter uses `BM` as location

---

## 3. Table IDs

**Prefix:** `TBL`

**Format:** `TBL-{SECTION}-{SEQUENCE}`

| Context | Example | Meaning |
|---------|---------|---------|
| Product DNA | `TBL-5.1.1-01` | Product DNA table in PPN |
| Three Scenarios | `TBL-5.1.1-02` | Scenarios table in PPN |
| Risk Analysis | `TBL-5.1.1-03` | Risk table in PPN |
| Comparison summary | `TBL-6.7-01` | V1 comparison matrix summary |

**Rules:**
- Tables numbered sequentially per chapter
- DNA Atlas card tables use Part 6 section numbering

---

## 4. Question IDs

**Prefix:** Product code (no TYPE prefix — see `question_identifier_standard.md`)

**Format:** `{PRODUCT_CODE}-{QUESTION_TYPE}-{SEQUENCE}`

| Type Code | Full Name | Example |
|:---------:|-----------|---------|
| RQ | Review Question | `PPN-RQ-01` |
| SQ | Scenario Question | `PPN-SQ-01` |
| DQ | Desk Question | `PPN-DQ-01` |

Full specification in `production/question_identifier_standard.md`.

---

## 5. Example IDs

**Prefix:** `EX`

**Format:** `EX-{SECTION}-{SEQUENCE}`

| Context | Example | Meaning |
|---------|---------|---------|
| Worked example | `EX-5.1.1-01` | Primary worked example in PPN |
| Additional scenario | `EX-5.1.1-02` | Secondary example in PPN |
| Construction Lab build | `EX-1.11-01` | First build in Product Construction Lab |

**Rules:**
- §18 Worked Example = EX-x.y.z-01
- Additional inline examples numbered sequentially
- Construction Lab (§1.11) builds: EX-1.11-01 through EX-1.11-08

---

## 6. Case Study IDs

**Prefix:** `CS`

**Format:** `CS-{LOCATION}-{SEQUENCE}`

| Context | Example | Meaning |
|---------|---------|---------|
| Trade Break Library | `CS-8.2-01` | First trade break case study |
| Trade Break Library | `CS-8.2-08` | Eighth (last) trade break case study |

**Rules:**
- Trade Break Case Study Library (V2 §8.2): CS-8.2-01 through CS-8.2-08
- 6-field structure per case: What Happened, Root Cause, Impact, Detection, Remediation, Lesson

---

## 7. Interview Answer IDs

**Prefix:** `T4`

**Format:** `T4-{PRODUCT_CODE}-{QUESTION_TYPE}-{SEQUENCE}`

| Context | Example | Meaning |
|---------|---------|---------|
| Interview answer | `T4-PPN-RQ-01` | Tier 4 interview answer for PPN Review Q1 |
| Interview answer | `T4-ACCUM-DQ-01` | Tier 4 for Accumulator Desk Q1 |

**Rules:**
- T4 prefix appended to the Question ID it answers
- 3 per chapter flagged as candidates (per §19 Interview Layer Candidates)
- Compiled in V2 §7.10 (Interview Quick Reference)

---

## 8. Examiner Note IDs

**Prefix:** `EN`

**Format:** `EN-{PRODUCT_CODE}-{QUESTION_TYPE}-{SEQUENCE}`

| Context | Example | Meaning |
|---------|---------|---------|
| Examiner note set | `EN-PPN-RQ-03` | Examiner Notes for PPN Review Q3 |
| Examiner note set | `EN-ACCUM-DQ-01` | Examiner Notes for Accumulator Desk Q1 |

**Rules:**
- Each EN set contains 3 annotations: Common Mistake, Interview Insight, Red Flag Answer
- Top 2 per product = 100 total (selective implementation)
- Placed in V2 §7.11

---

## 9. Solutions Manual Answer IDs

**Prefix:** Tier code

**Format:** `{TIER}-{PRODUCT_CODE}-{QUESTION_TYPE}-{SEQUENCE}`

| Tier | Prefix | Word Count | Example |
|:----:|:------:|:----------:|---------|
| 1 | T1 | 1-3 sentences | `T1-PPN-RQ-01` |
| 2 | T2 | 100-200 words | `T2-PPN-RQ-01` |
| 3 | T3 | 75-150 words | `T3-PPN-RQ-01` |
| 4 | T4 | 75-120 words | `T4-PPN-RQ-01` |

---

## 10. Cross-Reference Format

When referencing another element inline:

```
See [FIG-5.1.1-01] for the PPN payoff diagram.
Answer at [T2-PPN-RQ-01].
Compare with [EX-5.1.2-01] in the RC chapter.
```

Square brackets. No page numbers (those change during layout). Element IDs are stable.

---

## 11. ID Inventory (at 49/49)

| Type | Count Formula | Estimated Total |
|------|:-------------:|:---------------:|
| FIG | 49 × 6 + ~30 (non-product) | ~324 |
| TBL | ~5 per chapter + misc | ~275 |
| Questions | 49 × 9 + ~41 foundation | ~482 |
| EX | 49 × 1 + ~8 (Construction Lab) | ~57 |
| CS | 8 | 8 |
| T4 | ~213 | ~213 |
| EN | 100 × 3 annotations | 100 sets |
| T1-T3 | ~482 × 3 tiers | ~1,446 |

---

*Publication Identifier Standard defined 2026-06-21. Retrofit deferred to post-49/49.*
