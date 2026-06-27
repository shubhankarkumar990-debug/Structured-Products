# Ecosystem Consistency Audit

**Date**: 2026-06-25
**Scope**: 49 products × all canonical artifacts — naming, scoring, classification, cross-reference integrity
**Auditor**: Publication Review Board (Phases 2-3 of 12)

---

## 1. Product Count Verification

| Artifact | Products Listed | Match |
|----------|:--------------:|:-----:|
| Desk Bible v2 (Part 5 chapters) | 49 | ✅ |
| Product DNA Atlas (Family View) | 49 | ✅ |
| Complexity Registry | 49 | ✅ |
| Interview System V2.1 (PK series) | 49 | ✅ |
| Product Comparison Matrix | 49 | ✅ |
| Product Universe Map | 49 | ✅ |
| Learning Dependency Graph | 49 | ✅ |
| Product Evolution Map | 49 | ✅ |
| Publication Taxonomy | 49 | ✅ |
| Solutions Manual | 48 scenarios | ✅ (coverage, not 1:1) |

**Verdict: 49/49 products present across all 10 canonical artifacts.**

---

## 2. Product Naming Consistency

### C-1 | CRITICAL | Accumulator Complexity Score Mismatch

| Artifact | Accumulator Complexity Score |
|----------|:----------------------------:|
| Product DNA Atlas | 6 |
| Complexity Registry | 6 |
| **Interview System V2.1 (line 139)** | **7** |
| Desk Bible chapter §5.1.13 | 6 |

The Interview System V2.1 is the only artifact that assigns complexity 7 to the Accumulator. All other canonical sources agree on 6. This is a cross-artifact factual inconsistency in a frozen artifact.

---

### H-1 | HIGH | 13 Product Names Differ Between Complexity Registry and Atlas

The Complexity Registry uses variant names for 13 products that differ from the Atlas canonical names:

| # | Atlas Canonical Name | Registry Name | Discrepancy |
|:-:|---------------------|---------------|-------------|
| 1 | Bonus Note | Bonus Certificate | Certificate vs Note |
| 2 | Digital Coupon Note | Digital Note | Missing "Coupon" |
| 3 | Twin-Win Note | Twin Win Note | Missing hyphen |
| 4 | Shark Fin Note | Shark Fin | Missing "Note" |
| 5 | Power Reverse Dual Currency Note | PRDC Note | Abbreviation |
| 6 | Inflation-Linked Note | Inflation Linked Note | Missing hyphen |
| 7 | CMS Steepener Note | CMS Steepener | Missing "Note" |
| 8 | CMS Spread Range Accrual Note | CMS Spread Range Accrual | Missing "Note" |
| 9 | Snowball/Snowbear Note | Snowball Note | Missing "Snowbear" |
| 10 | TARN Steepener Note | TARN Steepener | Missing "Note" |
| 11 | Vanilla CLN | Credit-Linked Note (CLN) | Different format |
| 12 | CLN on Index | CLN on Index (iTraxx/CDX) | Extra index names |
| 13 | Synthetic CDO Tranche (CDO) | CDO Tranche | Missing "Synthetic" |

**Impact**: Cross-artifact lookups by product name may fail. Automation pipelines relying on exact name matching will break.

---

### H-6 | HIGH | CDO Name Mismatch in Interview System

Interview System V2.1 line 137 lists **"Collateralized Debt Obligation (CDO)"** but the Atlas canonical name is **"Synthetic CDO Tranche (CDO)"**. This is not just a naming difference — "Collateralized Debt Obligation" and "Synthetic CDO Tranche" are conceptually distinct instruments. The former is a broad category; the latter is a specific position within a synthetic structure.

---

## 3. Section Number Cross-References

### H-2 | HIGH | Phantom "Section 1.4: Equity Essentials" References

The Interview System V2.1 references "Section 1.4" or "Section 1.4: Equity Essentials" in 5 locations. The Desk Bible has no Section 1.4 titled "Equity Essentials." Part 1 covers:
- §1.1: How Options Work
- §1.2: The Greeks
- §1.3: Volatility Surface

There is no §1.4. These references are orphaned cross-links pointing to a non-existent section.

---

### M-6 | MEDIUM | Section 1.1 Cross-Reference Label Mismatch

The Interview System references "Section 1.1" in certain contexts with labels that don't match the Desk Bible's actual §1.1 title "How Options Work."

### M-9 | MEDIUM | Section 2.2/2.4 Inconsistent Labels

Cross-references to §2.2 and §2.4 use variant labels in different parts of the Interview System that don't exactly match the Desk Bible section titles.

---

## 4. Complexity Score Consistency

| Product | Atlas | Registry | Interview System | Desk Bible | Consistent? |
|---------|:-----:|:--------:|:----------------:|:----------:|:-----------:|
| Accumulator | 6 | 6 | **7** | 6 | ❌ |
| All other 48 products | ✅ | ✅ | ✅ | ✅ | ✅ |

**48/49 products have consistent complexity scores across all artifacts.**

### L-1 | LOW | Registry Scale Definition Examples Contradict Scores

The Complexity Registry includes scale anchor examples:
- "1-2: Vanilla CLN" — but Vanilla CLN is scored 4
- "7-8: Accumulator" — but Accumulator is scored 6

These anchors are guidelines, not product-specific claims, but readers may interpret them as factual.

---

## 5. Family Assignment Consistency

All 49 products have consistent family assignments across all canonical artifacts:

| Family | Products | All Artifacts Agree |
|--------|:--------:|:-------------------:|
| ELN | 15 | ✅ |
| Swaps | 8 | ✅ |
| SRT | 5 | ✅ |
| STEG | 4 | ✅ |
| CLN | 5 | ✅ |
| Other | 12 | ✅ |

---

## 6. System Assignment Consistency

| System | Products | Atlas = Desk Bible = Registry |
|--------|:--------:|:-----------------------------:|
| NEMO | ELN (15) + CLN (5) = 20 | ✅ |
| Murex | Swaps (8) + SRT (5) + STEG (4) = 17 | ✅ |
| Sophis | Other (12) = 12 | ✅ |

---

## 7. Day Count Convention Headers

### M-1 | MEDIUM | 4 Header Variants Across Product Chapters

The Desk Bible product chapters use different formatting for the day count convention field:

| Variant | Example Products | Count |
|---------|-----------------|:-----:|
| "Day Count Convention" | Most ELN products | 31 |
| "Day Count" | Some Swaps products | 8 |
| "Day Count Basis" | Some SRT products | 6 |
| "Daycount Convention" | STEG products | 4 |

All 49 chapters include the field. Content is consistent — only the label varies.

### M-2 | MEDIUM | ACT/360 Casing Inconsistency

| Variant | Occurrences |
|---------|:----------:|
| ACT/360 | 87 |
| Act/360 | 23 |
| act/360 | 2 |

Standard financial convention: **ACT/360** (all caps).

---

## 8. Generic §9 Template Issue

### H-3 | HIGH | 24/49 Product Chapters Use Equity-Specific Generic §9

24 product chapters use a verbatim generic "Three Scenarios" table with equity-centric language:

- Best case: "Underlying performs strongly"
- Worst case: "Underlying declines significantly"

This language is meaningless for non-equity products:
- **IRS** (§5.2.1): Risk driver is rate direction, not "underlying performance"
- **CMS Steepener** (§5.4.1): Risk driver is curve shape, not "underlying decline"
- **CDS** (§5.6.8): Risk driver is credit spread, not "underlying performance"
- **Variance Swap** (§5.2.5): Risk driver is realized vs implied vol

The remaining 25 products have product-specific §10 worked examples that make §9 redundant even where the equity language applies.

---

## 9. Consistency Summary

| Dimension | Score | Issues |
|-----------|:-----:|--------|
| Product count (49/49 everywhere) | 10/10 | None |
| Complexity scores | 9.8/10 | 1 mismatch (Accumulator) |
| Family assignments | 10/10 | None |
| System assignments | 10/10 | None |
| Product naming | 8.5/10 | 13 Registry variants, 1 CDO mismatch |
| Section cross-references | 9.0/10 | 5 phantom §1.4 references |
| Day count formatting | 9.0/10 | 4 label variants, casing inconsistency |
| Product chapter content | 8.5/10 | 24 generic §9 templates |
| **Overall Consistency** | **9.3/10** | |
