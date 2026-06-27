# Ecosystem Editorial Review

**Date**: 2026-06-25
**Scope**: Formatting consistency, duplication analysis, capitalization, abbreviation usage, editorial quality
**Auditor**: Publication Review Board (Phases 7-8 of 12)

---

## 1. Duplication Analysis (Phase 7)

### Classification Framework

| Category | Definition | Action Required |
|----------|-----------|:---------------:|
| Intentional reinforcement | Same concept, different angle, different artifact | None |
| Acceptable overlap | Brief repetition for standalone readability | None |
| Excessive duplication | Verbatim or near-verbatim content that should be consolidated | Yes |

### Findings

#### D-1 | HIGH | DNA Card Verbatim Duplication (49 instances)

**Location**: Every Desk Bible product chapter §4 vs corresponding Atlas DNA Card

Every product chapter embeds a near-verbatim copy of its Atlas DNA Card (~30 lines per product). Fields duplicated include: Complexity Score, Complexity Rationale, Underlying Asset Class, Capital Protection, Coupon Type, Maturity, Liquidity, Primary System, ISDA Required. Additionally, each chapter has "DNA Atlas Fields" and "Comparison Matrix Fields" bullet lists that mirror Atlas card fields.

**Scale**: ~1,470 lines of duplicated data across 49 chapters.
**Classification**: Excessive duplication.
**Recommendation**: Desk Bible chapters should retain a minimal 5-field summary table and reference the Atlas as the canonical source for full DNA data.

---

#### D-2 | HIGH | Generic §9 Three Scenarios Table (24 instances)

**Location**: 24 of 49 Desk Bible product chapters, §9

24 product chapters use an identical generic table:
- Best case: "Underlying performs strongly | Maximum return captured"
- Base case: "Underlying is flat or moderately positive | Moderate return"
- Worst case: "Underlying declines significantly | Capital at risk"

This is excessive duplication AND an editorial error — the equity-centric language is factually misleading for rate, credit, and volatility products (see Editorial findings E-1).

**Classification**: Excessive duplication compounded by content error.
**Recommendation**: Replace with product-specific scenario summaries using appropriate risk driver language per family.

---

#### D-3 | MEDIUM | FTP "Hidden Killer" Worked Example (verbatim)

**Location**: Desk Bible §6.7 (line ~24180) vs Interview System §3.7 (line ~716)

Both artifacts use identical numbers: 3Y ELN, 6% coupon, revenue 7.30%, FTP -1.80%, desk margin -0.50%. The phrase "hidden killer" and the conclusion appear near-verbatim.

**Classification**: Excessive duplication (same numbers, same narrative).
**Recommendation**: Interview System should use different product parameters to reinforce the FTP concept from a distinct angle, or explicitly cross-reference the Desk Bible example.

---

#### D-4 | MEDIUM | Day Count Cross-Reference Inconsistency

**Location**: Interview System line 220 vs Interview System §3.1 (line 583)

The Interview System references the Desk Bible's "$55,556 difference" example (from §6.1) but locally uses different parameters producing a "$16,667 difference." This creates confusion about which worked example is being referenced.

**Classification**: Acceptable overlap in principle (different artifacts, different numbers), but the explicit cross-reference to the $55,556 figure while using $16,667 locally is confusing.
**Recommendation**: Clarify that §6.1 uses a different example, or align the cross-reference to the local example.

---

#### D-5 | MEDIUM | Recovery Rate Data Overlap

**Location**: Desk Bible §6.4 (line 23383) vs Interview System §3.4 (line 649)

Recovery rate hierarchy (Senior Secured ~65-70%, Senior Unsecured ~40-50%, Subordinated ~20-30%) and AT1/CoCos details appear in both artifacts with near-identical data.

**Classification**: Acceptable overlap — both artifacts serve standalone reading purposes and the Interview System appropriately condenses the Desk Bible content.

---

#### D-6 | MEDIUM | P&L Attribution Table

**Location**: Desk Bible §6.6 (line 23847) vs Interview System §3.6 (line 679)

Both contain a P&L attribution component table with identical columns and 9-10 identical components. The Interview System version is lightly condensed.

**Classification**: Acceptable overlap — condensed format serves interview preparation effectively.

---

#### D-7 | LOW | Credit Suisse AT1 Case Study (3 appearances)

**Location**: Desk Bible §6.4, Interview System §3.3 Tier 4, Interview System Product 4 CDS Tier 4

Appears three times across two artifacts. Each appearance serves a different analytical purpose (credit hierarchy, documentation risk, CDS mechanics).

**Classification**: Intentional reinforcement.

---

### Duplication Summary

| Classification | Count | Action |
|---------------|:-----:|--------|
| Excessive duplication | 3 (D-1, D-2, D-3) | Consolidate or differentiate |
| Confusing overlap | 1 (D-4) | Clarify cross-reference |
| Acceptable overlap | 2 (D-5, D-6) | No action |
| Intentional reinforcement | 1 (D-7) | No action |

---

## 2. Editorial Quality (Phase 8)

### E-1 | HIGH | Equity-Centric Language in Non-Equity Product Scenarios

**Location**: 24 Desk Bible product chapters §9

The generic Three Scenarios table uses "Underlying performs strongly" and "Underlying declines significantly" for products where these phrases are meaningless:

| Product | Actual Risk Driver | §9 Says |
|---------|-------------------|---------|
| IRS (§5.2.1) | Rate direction | "Underlying declines" |
| CMS Steepener (§5.4.1) | Curve shape | "Underlying performs strongly" |
| Variance Swap (§5.2.5) | Realized vs implied vol | "Underlying declines" |
| CDS (§5.6.8) | Credit spread | "Underlying performs strongly" |

**Recommendation**: Each product family needs risk-driver-appropriate scenario language.

---

### E-2 | MEDIUM | knock-in/knock-out Capitalization Inconsistency

**Location**: Desk Bible, throughout (164 affected instances)

| Variant | Count | Standard |
|---------|:-----:|:--------:|
| knock-in (lowercase) | 120 | ✅ Preferred |
| Knock-In (title case) | 26 | ❌ Mid-sentence |
| Knock-in (sentence case) | 18 | ⚠️ Only at sentence start |
| knock-out (lowercase) | 112 | ✅ Preferred |
| Knock-Out (title case) | 27 | ❌ Mid-sentence |
| Knock-out (sentence case) | 34 | ⚠️ Only at sentence start |

**Recommendation**: Standardize to lowercase hyphenated ("knock-in", "knock-out") in running text. Title case only in headings and at sentence start.

---

### E-3 | MEDIUM | worst-of Capitalization and Hyphenation Inconsistency

**Location**: Desk Bible, throughout (177 affected instances)

| Variant | Count |
|---------|:-----:|
| worst-of (lowercase, hyphenated) | 131 |
| Worst-of (sentence case, hyphenated) | 43 |
| worst of (no hyphen) | 3 |

**Recommendation**: Always hyphenated. Lowercase in running text, capitalized only at sentence start or as part of the proper product name "Worst-of Autocallable Note."

---

### E-4 | LOW | Part 6 vs Part 5 Heading Depth

Part 6 sections use `##` (level 2) with `###` subsections. Part 5 product chapters use `####` (level 4) for all 22 subsections, creating a flat hierarchy. This is consistent with the template-driven structure — each product chapter is self-contained. No action needed.

---

### E-5 | LOW | FTP Curve Rates Duplicated

**Location**: Desk Bible §6.7 and Interview System §3.7

Identical illustrative FTP rates (1Y: 1.20%, 3Y: 1.80%, 5Y: 2.40%, 10Y: 3.10%) appear in both artifacts. While marked as "illustrative," identical numbers create the appearance of copied content.

**Recommendation**: Minor. Interview System could note "rates from §6.7" explicitly.

---

### E-6 | LOW | EMIR Abbreviation Undefined at First Use

**Location**: Interview System §3.11 (line 803)

"EMIR" appears 5 times in Part 3 without expansion. First expansion occurs only in Confusion Pairs (line 1009). A standalone Part 3 reader encounters an undefined abbreviation.

**Recommendation**: Add "(European Market Infrastructure Regulation)" after first EMIR mention in §3.11.

---

### E-7 | LOW | Solutions Manual: Clean

The Solutions Manual has consistent heading hierarchy, sequential numbering, aligned tables, and no broken markdown. No editorial issues detected.

---

## 3. Formatting Consistency

| Dimension | Desk Bible | Interview System | Solutions Manual | Atlas |
|-----------|:----------:|:----------------:|:---------------:|:-----:|
| Heading levels | ✅ Consistent | ✅ Consistent | ✅ Consistent | ✅ Consistent |
| Table alignment | ✅ | ✅ | ✅ | ✅ |
| Bold/italic usage | ✅ | ✅ | ✅ | ✅ |
| Section numbering | ✅ Sequential | ✅ Sequential | ✅ Sequential | ✅ Sequential |
| Markdown validity | ✅ No broken tables | ✅ Clean | ✅ Clean | ✅ Clean |
| Currency units | ⚠️ $ default, EUR/CHF where appropriate | ✅ | ✅ | ✅ |

---

## 4. Editorial Summary

| Severity | Count | Key Issues |
|:--------:|:-----:|------------|
| HIGH | 2 | DNA Card verbatim duplication (49×), equity language in non-equity scenarios (24×) |
| MEDIUM | 4 | FTP example duplication, day count cross-ref, knock-in/out capitalization (164×), worst-of capitalization (177×) |
| LOW | 4 | Heading depth, FTP curve duplication, EMIR undefined, Solutions Manual clean |

**Overall Editorial Quality: 8.7/10**

The writing quality is uniformly high — the "Professor Voice" standard produces engaging, precise prose. The issues are mechanical (capitalization consistency, template reuse) rather than substantive. The excessive duplication findings (D-1, D-2) are structural decisions that could be addressed in a future edition without affecting content quality.
