# V1.0.1 ACCEPT-AS-IS REGISTER — FINAL

**Purpose:** Items reviewed and confirmed as correct, defensible, or out of scope for correction.  
**Status:** FINAL (package closure)  
**Supersedes:** `v1_0_1_accept_as_is_register.md`

---

## A-01 — Solutions Manual Convention Mixing

**File:** `production/solutions_manual.md`  
**Lines:** 180, 1447, 1463, 1477, 1870

**Description:** Uses structural phrasing ("client sells correlation risk") and MTM description ("WOAC suffers when correlations drop") in separate sentences. The economic explanations are individually correct in every instance.

**Why accept:** No single sentence contains a self-contradiction. The convention mixing follows standard industry practice where both phrasings coexist. No reader would derive a wrong answer from these descriptions.

**Status:** ACCEPT AS-IS.

---

## A-02 — Product DNA Atlas Correlation Descriptions

**File:** `production/product_dna_atlas.md`  
**Lines:** 1269, 1298, 1675, 1877, 2085, 2086

**Description:** The Atlas uses correct economic descriptions ("low correlation = higher risk" for FTD, "high correlation INCREASES NTD risk") without applying "long" or "short" correlation labels.

**Why accept:** By describing economics without labels, the Atlas avoids the convention trap entirely. Every description is unambiguously correct.

**Status:** ACCEPT AS-IS.

---

## A-03 — FTD/NTD Confusion Pair Avoids Labels

**File:** `production/interview_system_v2_2.md`  
**Line:** 986

**Description:** The confusion pair states "Low corr increases FTD risk; high corr increases NTD risk" without using "long" or "short" labels.

**Why accept:** The economic description is correct. Avoiding labels is the safest approach given the convention ambiguity. The Tier 2 treatment at line 400 provides the explicit "FTD is LONG correlation" answer for candidates who need the label.

**Status:** ACCEPT AS-IS.

---

## A-04 — "Independent Stocks" Simplification

**File:** `production/interview_system_v2_2.md`  
**Line:** 354

**Description:** The formula "barrier breach probability ≈ 1 − (1−P)^N" assumes independence (zero correlation). The text immediately follows with the correlation explanation that corrects this simplification.

**Why accept:** The zero-correlation formula is standard pedagogy for building intuition. It is immediately corrected in the next sentences (lines 354-356). The transition from "independent" to "correlated" is the teaching moment.

**Status:** ACCEPT AS-IS.

---

## A-05 — Continuous Barrier Observation Conventions

**File:** `Desk_Bible_v2.md`  
**Line:** 22544

**Description:** The WOAC terms specify "continuous" barrier observation without elaborating on intraday vs closing-price interpretation.

**Why accept:** These are standard industry conventions covered in the Infrastructure Encyclopedia (§6.1). Defining them in every worked example would be redundant for the target audience.

**Status:** ACCEPT AS-IS.

---

## A-06 — Day Count and Quarterly Conventions

**File:** `Desk_Bible_v2.md`  
**Multiple locations**

**Description:** Worked examples use "quarterly" payment frequency with varying total days per quarter (90, 91, 92) without explicitly stating that calendar quarters have different numbers of days.

**Why accept:** All worked examples show actual day counts in their tables, making the convention transparent by example. Day count conventions are covered in the Foundations section (Part 0).

**Status:** ACCEPT AS-IS.

---

## Summary

| Item | Description | Disposition |
|:----:|------------|:----------:|
| A-01 | Solutions Manual convention mixing | ACCEPT AS-IS |
| A-02 | Atlas economic descriptions (no labels) | ACCEPT AS-IS |
| A-03 | FTD/NTD confusion pair avoids labels | ACCEPT AS-IS |
| A-04 | Independent stocks simplification | ACCEPT AS-IS |
| A-05 | Continuous barrier conventions | ACCEPT AS-IS |
| A-06 | Day count / quarterly conventions | ACCEPT AS-IS |

---

*V1.0.1 Accept-As-Is Register | FINAL (package closure) | 2026-06-27*
