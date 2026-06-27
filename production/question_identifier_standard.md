# Question Identifier Standard

**Date:** 2026-06-21
**Status:** DEFINED. Not yet retrofitted.
**Purpose:** Stable, unique identifiers for every question in §19 Knowledge Check across all 49 products.

---

## 1. Format

```
{PRODUCT_CODE}-{QUESTION_TYPE}-{SEQUENCE}
```

| Component | Format | Values |
|-----------|--------|--------|
| PRODUCT_CODE | 2-5 uppercase letters | Product abbreviation from §4 Product DNA |
| QUESTION_TYPE | 2 uppercase letters | RQ (Review), SQ (Scenario), DQ (Desk) |
| SEQUENCE | 2-digit zero-padded | 01, 02, 03... |

**Separator:** Hyphen (-)

---

## 2. Product Codes

| Section | Product | Code |
|---------|---------|:----:|
| 5.1.1 | PPN | PPN |
| 5.1.2 | RC | RC |
| 5.1.3 | Phoenix | PHX |
| 5.1.4 | DRC | DRC |
| 5.1.5 | KODRC | KODRC |
| 5.1.6 | CRC | CRC |
| 5.1.7 | Airbag | AIR |
| 5.1.8 | Bonus | BNS |
| 5.1.9 | FCN | FCN |
| 5.1.10 | CRA ELN | CRAELN |
| 5.1.11 | ICN | ICN |
| 5.1.12 | Digital Note | DIG |
| 5.1.13 | Booster | BST |
| 5.1.14 | Digital KI Put | DKIP |
| 5.1.15 | Warrant | WRT |
| 5.2.1 | IRS | IRS |
| 5.2.2 | TRS | TRS |
| 5.2.3 | Equity Swap | EQSW |
| 5.2.4 | Variance Swap | VARSW |
| 5.2.5 | CDS | CDS |
| 5.2.6 | Cross-Currency Swap | XCCY |
| 5.2.7 | Commodity Swap | COMSW |
| 5.2.8 | VLSP | VLSP |
| 5.3.1 | IR Callable | IRCL |
| 5.3.2 | ZCL | ZCL |
| 5.3.3 | NCRA | NCRA |
| 5.3.4 | CRA SRT | CRASRT |
| 5.3.5 | Digital Cap-Floor | DCF |
| 5.4.1 | Vanilla STEG | VSTEG |
| 5.4.2 | RA STEG | RASTEG |
| 5.4.3 | Callable STEG | CSTEG |
| 5.4.4 | TARN STEG | TSTEG |
| 5.5.1 | CLN | CLN |
| 5.5.2 | Skew CLN | SKLN |
| 5.5.3 | FTD | FTD |
| 5.5.4 | NTD | NTD |
| 5.5.5 | Synthetic CDO | SCDO |
| 5.6.1 | Structured Deposit | SD |
| 5.6.2 | Forward | FWD |
| 5.6.3 | Vanilla Option | VO |
| 5.6.4 | ELO | ELO |
| 5.6.5 | Option on RC | ORC |
| 5.6.6 | Accumulator | ACCUM |
| 5.6.7 | Decumulator | DECUM |

Codes for Batch 10 products (45-49): assign during generation.

---

## 3. Question Types

| Code | Full Name | §19 Location | Typical Count |
|:----:|-----------|-------------|:-------------:|
| RQ | Review Question | "Review Questions" block | 5 per chapter |
| SQ | Scenario Question | "Scenario Questions" block | 3 per chapter |
| DQ | Desk Question | "Desk Question" block | 1 per chapter |

---

## 4. Examples

| Question ID | Meaning |
|-------------|---------|
| `PPN-RQ-01` | PPN, Review Question 1 |
| `PPN-RQ-05` | PPN, Review Question 5 |
| `PPN-SQ-01` | PPN, Scenario Question 1 |
| `PPN-SQ-03` | PPN, Scenario Question 3 |
| `PPN-DQ-01` | PPN, Desk Question 1 |
| `PHX-SQ-02` | Phoenix, Scenario Question 2 |
| `ACCUM-DQ-01` | Accumulator, Desk Question 1 |
| `SCDO-RQ-03` | Synthetic CDO, Review Question 3 |

---

## 5. Total Question Count (49 products)

| Type | Per Chapter | × 49 | Total |
|------|:----------:|:----:|:-----:|
| RQ | 5 | 49 | 245 |
| SQ | 3 | 49 | 147 |
| DQ | 1 | 49 | 49 |
| **Total** | **9** | **49** | **441** |

Foundation sections (Parts 0-4) may add ~41 additional questions. Total universe: ~482.

---

## 6. Usage Rules

1. **Immutability.** Once assigned, a Question ID never changes. If a question is removed, its ID is retired, not reused
2. **Ordering.** Sequence numbers follow the order questions appear in §19 of the chapter
3. **Cross-reference.** Solutions Manual (V2 Part 7) uses Question IDs as keys
4. **Interview Layer.** T4 answers reference their Question ID
5. **Examiner Notes.** Top 100 annotations reference their Question ID
6. **Retrofit.** During harmonization pass, insert Question IDs into §19 of each chapter as inline tags: `[PPN-RQ-01]`

---

## 7. Retrofit Plan (Post-49/49)

During Template Harmonization Pass:
1. For each chapter §19, number all Review Questions as `{CODE}-RQ-01` through `{CODE}-RQ-05`
2. Number all Scenario Questions as `{CODE}-SQ-01` through `{CODE}-SQ-03`
3. Number Desk Question as `{CODE}-DQ-01`
4. Insert ID as inline tag before each question text
5. Generate `production/question_id_master_list.md` — full listing of all 441+ IDs with question text

Not executed now. Standard defined only.

---

*Question Identifier Standard defined 2026-06-21.*
*Retrofit deferred to post-49/49 harmonization pass.*
