# REGRESSION TEST SUITE

**Ecosystem:** Structured Products Knowledge Ecosystem  
**Version:** V1.0.1-GOV-1.0  
**Effective:** 2026-06-27  
**Purpose:** Prevent reintroduction of known defects. Every resolved error class becomes a test.  
**Automation:** Each test is designed for conversion to an automated validator.

---

## Test Format

Each test specifies:
1. **Test ID** — unique identifier
2. **Objective** — what the test prevents
3. **Input** — the text pattern or artifact to test
4. **Expected outcome** — PASS condition
5. **Failure mode** — what happens when it fails
6. **Severity** — S1/S2/S3/S4
7. **Artifacts covered** — which artifacts this test applies to
8. **Detection method** — regex, arithmetic check, cross-reference, or manual
9. **Manual note** — edge cases requiring human judgment
10. **Linter rule** — linked linter rule ID

---

## CORRELATION DIRECTION TESTS

### REG-COR-01: FTD Not Labeled Short (ELI5 Section)

| Field | Value |
|-------|-------|
| **Test ID** | REG-COR-01 |
| **Objective** | FTD never labeled "short correlation" without "structurally" in §1 ELI5 |
| **Input** | Desk Bible §1 ELI5 section (around line 17352) |
| **Expected outcome** | PASS if FTD is labeled "long correlation" or "structurally short" |
| **Failure mode** | "FTD investors are short credit correlation" (V1.0 text) |
| **Severity** | S1 |
| **Artifacts** | Desk_Bible_v2.md |
| **Detection** | Regex: `/FTD.*?short.*?correlation/i` without "structurally" in same sentence |
| **Manual note** | Check that the economic explanation matches the label |
| **Linter rule** | LNT-COR-06 |

### REG-COR-02: FTD Not Self-Contradictory (Key Insight)

| Field | Value |
|-------|-------|
| **Test ID** | REG-COR-02 |
| **Objective** | No sentence says "short correlation" then "profit when correlation is high" for FTD |
| **Input** | Desk Bible §11 key insight (around line 17524) |
| **Expected outcome** | PASS if label matches economics |
| **Failure mode** | "FTD investors are short correlation. They profit when correlation is high." |
| **Severity** | S1 |
| **Artifacts** | Desk_Bible_v2.md |
| **Detection** | Regex: `/short correlation.*?profit.*?high/i` within 200 chars |
| **Manual note** | Also check that the structural note preserves the premium-sold nuance |
| **Linter rule** | LNT-COR-02 |

### REG-COR-03: FTD Table Row Correct

| Field | Value |
|-------|-------|
| **Test ID** | REG-COR-03 |
| **Objective** | FTD row in NTD coupon scaling table shows "Long correlation" |
| **Input** | Desk Bible NTD coupon scaling table (line 17951) |
| **Expected outcome** | PASS if FTD row contains "Long correlation" |
| **Failure mode** | "Short correlation (unambiguous)" (V1.0 text) |
| **Severity** | S1 |
| **Artifacts** | Desk_Bible_v2.md |
| **Detection** | Table parsing: find row containing "FTD", check 4th column for "Long" |
| **Manual note** | None |
| **Linter rule** | LNT-COR-06 |

### REG-COR-04: Worst-of Not Self-Contradictory

| Field | Value |
|-------|-------|
| **Test ID** | REG-COR-04 |
| **Objective** | No sentence says worst-of investors are "short correlation" then "profit when stocks move together" |
| **Input** | Desk Bible line 17526 |
| **Expected outcome** | PASS if label matches economics |
| **Failure mode** | "Worst-of investors are short correlation — they profit when stocks move together." |
| **Severity** | S1 |
| **Artifacts** | Desk_Bible_v2.md |
| **Detection** | Regex: `/worst-of.*?short correlation.*?profit.*?together/i` within 200 chars |
| **Manual note** | None |
| **Linter rule** | LNT-COR-08 |

### REG-COR-05: NTD Table Rows All Short (N≥2)

| Field | Value |
|-------|-------|
| **Test ID** | REG-COR-05 |
| **Objective** | All NTD rows (2TD through 5TD) labeled "Short correlation" in coupon scaling table |
| **Input** | Desk Bible NTD coupon scaling table (lines 17952-17955) |
| **Expected outcome** | PASS if all N≥2 rows contain "Short correlation" |
| **Failure mode** | "4TD: Long correlation (approximately)" or "5TD: Long correlation (unambiguous)" |
| **Severity** | S1 |
| **Artifacts** | Desk_Bible_v2.md |
| **Detection** | Table parsing: for each row where product matches /[2-9]TD|NTD/, verify "Short" in correlation column |
| **Manual note** | Also verify that "reversal" language does not imply within-product flip |
| **Linter rule** | LNT-COR-07 |

### REG-COR-06: NTD Table Consistent with Risk Table

| Field | Value |
|-------|-------|
| **Test ID** | REG-COR-06 |
| **Objective** | Label table and risk table agree on direction for every NTD product |
| **Input** | Desk Bible: coupon scaling table (17949-17955) + risk analysis table (17927-17932) |
| **Expected outcome** | PASS if: risk increases with ρ → label = "Short"; risk decreases with ρ → label = "Long" |
| **Failure mode** | Risk table shows 2TD risk HIGH at high ρ, but label table says "Long correlation" |
| **Severity** | S1 |
| **Artifacts** | Desk_Bible_v2.md |
| **Detection** | Cross-table comparison (requires structured table parsing) |
| **Manual note** | Must parse both tables and compare semantically |
| **Linter rule** | LNT-XAR-03 |

### REG-COR-07: Dispersion Direction Correct

| Field | Value |
|-------|-------|
| **Test ID** | REG-COR-07 |
| **Objective** | "Long single-stock vol + short basket vol" never labeled "long correlation" |
| **Input** | Desk Bible line 22605 |
| **Expected outcome** | PASS if dispersion trade legs + "short correlation" |
| **Failure mode** | "Long single-stock vol + short basket vol = long correlation" |
| **Severity** | S1 |
| **Artifacts** | Desk_Bible_v2.md |
| **Detection** | Regex: `/long single-stock.*short basket.*long correlation/i` |
| **Manual note** | None |
| **Linter rule** | LNT-COR-09 |

### REG-COR-08: Interview System WOAC Not Self-Contradictory

| Field | Value |
|-------|-------|
| **Test ID** | REG-COR-08 |
| **Objective** | Interview System line 356 does not say "SHORT correlation: benefit from high correlation" |
| **Input** | interview_system_v2_2.md line 356 |
| **Expected outcome** | PASS if label matches economics |
| **Failure mode** | "The investor is SHORT correlation: they benefit from high correlation" |
| **Severity** | S1 |
| **Artifacts** | interview_system_v2_2.md |
| **Detection** | Regex: `/SHORT correlation.*?benefit.*?high correlation/i` within 200 chars |
| **Manual note** | Also verify line 358 "short correlation" is correctly attributed to desk's raw Greek |
| **Linter rule** | LNT-COR-02 |

### REG-COR-09: No "Reversal at High ρ" Without Clarification

| Field | Value |
|-------|-------|
| **Test ID** | REG-COR-09 |
| **Objective** | "Reversal" in NTD context always clarifies it means FTD-vs-NTD difference, not within-product flip |
| **Input** | All NTD-related text |
| **Expected outcome** | PASS if "reversal" is qualified or absent |
| **Failure mode** | "2TD: Short at low ρ, reversal at high ρ" — implies within-product flip |
| **Severity** | S2 |
| **Artifacts** | Desk_Bible_v2.md |
| **Detection** | Regex: `/reversal at (high|low|moderate)/i` + NTD context |
| **Manual note** | May appear in body text explanations — check if properly qualified |
| **Linter rule** | LNT-COR-10 |

---

## OWNERSHIP / PROTECTION TESTS

### REG-PRO-01: Part 6 Desk Not Labeled Protection Seller

| Field | Value |
|-------|-------|
| **Test ID** | REG-PRO-01 |
| **Objective** | Part 6 never says the desk "sold protection via the short put" |
| **Input** | part6_sections_10_11.md line 102 |
| **Expected outcome** | PASS if desk is described as protection buyer or put is correctly attributed to investor |
| **Failure mode** | "(which sold protection via the short put)" attributed to desk |
| **Severity** | S1 |
| **Artifacts** | part6_sections_10_11.md |
| **Detection** | Regex: `/desk.*?sold protection/i` or `/which sold protection/i` |
| **Manual note** | Verify the hedged qualifier is present |
| **Linter rule** | LNT-PRO-01 |

### REG-PRO-02: Cross-Artifact Protection Consistency

| Field | Value |
|-------|-------|
| **Test ID** | REG-PRO-02 |
| **Objective** | All artifacts agree on who sold/bought protection for each product |
| **Input** | All production artifacts |
| **Expected outcome** | PASS if investor = seller and desk = buyer in all structured note contexts |
| **Failure mode** | One artifact says "desk sold," another says "investor sold" for same product |
| **Severity** | S1 |
| **Artifacts** | All production/* |
| **Detection** | Cross-artifact search for "sold protection" + product context |
| **Manual note** | CDS context allows desk to sell protection (standalone trade, not structured note) |
| **Linter rule** | LNT-XAR-02 |

---

## RAW / HEDGED TESTS

### REG-POS-01: Part 6 Has Hedged Qualifier

| Field | Value |
|-------|-------|
| **Test ID** | REG-POS-01 |
| **Objective** | Part 6 desk correlation Greek table includes "net/hedged" |
| **Input** | part6_sections_10_11.md line 110 |
| **Expected outcome** | PASS if "net/hedged" or equivalent appears |
| **Failure mode** | "long correlation (worst-of)" without hedged qualifier |
| **Severity** | S2 |
| **Artifacts** | part6_sections_10_11.md |
| **Detection** | Search line 110 for "hedged" or "net" |
| **Manual note** | None |
| **Linter rule** | LNT-QAL-02 |

### REG-POS-02: Encyclopedia Has Raw Qualifier

| Field | Value |
|-------|-------|
| **Test ID** | REG-POS-02 |
| **Objective** | Encyclopedia correlation trade entry specifies "raw/unhedged" |
| **Input** | infrastructure_encyclopedia_v1.md line 4290 |
| **Expected outcome** | PASS if "raw" or "unhedged" appears |
| **Failure mode** | "Worst-of products are SHORT correlation" without raw qualifier |
| **Severity** | S2 |
| **Artifacts** | infrastructure_encyclopedia_v1.md |
| **Detection** | Search line 4290 for "raw" or "unhedged" |
| **Manual note** | None |
| **Linter rule** | LNT-QAL-02 |

### REG-POS-03: Part 6 and Encyclopedia Consistent

| Field | Value |
|-------|-------|
| **Test ID** | REG-POS-03 |
| **Objective** | Part 6 (hedged: long) and Encyclopedia (raw: short) don't contradict without qualifiers |
| **Input** | Both artifacts |
| **Expected outcome** | PASS if both have raw/hedged qualifiers |
| **Failure mode** | One says "long," other says "short," no qualifiers |
| **Severity** | S1 |
| **Artifacts** | part6_sections_10_11.md, infrastructure_encyclopedia_v1.md |
| **Detection** | Cross-artifact: find "worst-of" + "correlation" in both, check for qualifiers |
| **Manual note** | This was the root cause of E-04 |
| **Linter rule** | LNT-XAR-01 |

---

## ARITHMETIC / SIGN TESTS

### REG-SGN-01: WOAC 65% Not "Above Strike"

| Field | Value |
|-------|-------|
| **Test ID** | REG-SGN-01 |
| **Objective** | No worked example claims X% is above Y% when X < Y |
| **Input** | Desk Bible line 22565 |
| **Expected outcome** | PASS if "65%: below strike (100%)" |
| **Failure mode** | "65%: above strike (100%)" |
| **Severity** | S1 |
| **Artifacts** | Desk_Bible_v2.md |
| **Detection** | Parse percentage comparisons in worked examples |
| **Manual note** | Generalizable to all worked examples |
| **Linter rule** | LNT-SGN-01 |

### REG-SGN-02: Gamma Sign Intermediate Step

| Field | Value |
|-------|-------|
| **Test ID** | REG-SGN-02 |
| **Objective** | Gamma × ΔS includes the sign of ΔS in the intermediate expression |
| **Input** | Desk Bible line 1069 |
| **Expected outcome** | PASS if expression shows 3 × (−2) = −6 or equivalent |
| **Failure mode** | "3 × 2 = -56" — impossible intermediate arithmetic |
| **Severity** | S1 |
| **Artifacts** | Desk_Bible_v2.md |
| **Detection** | Parse gamma calculations, verify sign of ΔS matches described stock move direction |
| **Manual note** | Requires understanding of what "drop" means for ΔS sign |
| **Linter rule** | LNT-SGN-02 |

### REG-SGN-03: CRA SRT Q4 Coupon

| Field | Value |
|-------|-------|
| **Test ID** | REG-SGN-03 |
| **Objective** | Verify Q4 coupon matches formula: $810,000 × 88/92 |
| **Input** | Desk Bible line 13960 |
| **Expected outcome** | PASS if Q4 = $774,783 (or $775,304 accepted with justification) |
| **Failure mode** | Value doesn't match any standard formula |
| **Severity** | S3 |
| **Artifacts** | Desk_Bible_v2.md |
| **Detection** | Arithmetic: verify Max_Q × Days_In_Range / Total_Days |
| **Manual note** | Currently classified as review-only (R-05). Difference is $521, rounds away. |
| **Linter rule** | LNT-SGN-03 |

### REG-SGN-04: WOAC Strike Defined in Terms Table

| Field | Value |
|-------|-------|
| **Test ID** | REG-SGN-04 |
| **Objective** | WOAC worked example terms table includes strike level |
| **Input** | Desk Bible lines 22536-22545 |
| **Expected outcome** | PASS if "Strike: 100%" (or similar) appears in terms table |
| **Failure mode** | Terms table omits strike but the text references it |
| **Severity** | S2 |
| **Artifacts** | Desk_Bible_v2.md |
| **Detection** | Parse terms table, verify "strike" row exists |
| **Manual note** | Currently classified as review-only (R-02) |
| **Linter rule** | LNT-STR-02 |

---

## CROSS-ARTIFACT CONSISTENCY TESTS

### REG-XAR-01: Interview System FTD Matches Desk Bible

| Field | Value |
|-------|-------|
| **Test ID** | REG-XAR-01 |
| **Objective** | Interview System and Desk Bible agree on FTD correlation direction |
| **Input** | interview_system_v2_2.md lines 400, 407; Desk_Bible_v2.md lines 17352, 17524 |
| **Expected outcome** | PASS if both say "long correlation" for FTD |
| **Failure mode** | One says "long," other says "short" |
| **Severity** | S1 |
| **Artifacts** | interview_system_v2_2.md, Desk_Bible_v2.md |
| **Detection** | Cross-artifact: extract FTD + correlation direction from both |
| **Manual note** | None |
| **Linter rule** | LNT-XAR-01 |

### REG-XAR-02: Solutions Manual Convention Mixing Acceptable

| Field | Value |
|-------|-------|
| **Test ID** | REG-XAR-02 |
| **Objective** | Solutions Manual convention mixing is individually correct (no self-contradictions) |
| **Input** | solutions_manual.md lines 180, 1447, 1463, 1477, 1870 |
| **Expected outcome** | PASS if each sentence is internally consistent (no same-sentence label/economics contradiction) |
| **Failure mode** | A sentence says "short" but describes benefit from rising |
| **Severity** | S1 |
| **Artifacts** | solutions_manual.md |
| **Detection** | Apply LNT-COR-01/02 to each identified line |
| **Manual note** | Convention mixing is accepted (A-01) but self-contradiction is not |
| **Linter rule** | LNT-COR-01, LNT-COR-02 |

### REG-XAR-03: Atlas Avoids Labels

| Field | Value |
|-------|-------|
| **Test ID** | REG-XAR-03 |
| **Objective** | Product DNA Atlas continues to use economic descriptions without long/short labels |
| **Input** | product_dna_atlas.md correlation-related lines |
| **Expected outcome** | PASS if no "long correlation" or "short correlation" labels appear |
| **Failure mode** | Atlas adds "FTD: short correlation" label |
| **Severity** | S3 |
| **Artifacts** | product_dna_atlas.md |
| **Detection** | Search for "long correlation" or "short correlation" in Atlas |
| **Manual note** | Atlas avoidance of labels is accepted (A-02) and should be preserved |
| **Linter rule** | N/A (style check) |

---

## TEST SUMMARY

| Test ID | Error Class | Severity | Detection |
|:-------:|------------|:--------:|:---------:|
| REG-COR-01 | FTD direction (E-01) | S1 | Regex |
| REG-COR-02 | FTD self-contradiction (E-01b) | S1 | Regex |
| REG-COR-03 | FTD table row (E-01c) | S1 | Table parse |
| REG-COR-04 | Worst-of self-contradiction (E-02) | S1 | Regex |
| REG-COR-05 | NTD table rows (E-09) | S1 | Table parse |
| REG-COR-06 | NTD table vs risk table (E-09) | S1 | Cross-table |
| REG-COR-07 | Dispersion direction (E-06) | S1 | Regex |
| REG-COR-08 | WOAC Interview System (E-08) | S1 | Regex |
| REG-COR-09 | Reversal language | S2 | Regex + context |
| REG-PRO-01 | Part 6 ownership (E-03) | S1 | Regex |
| REG-PRO-02 | Cross-artifact ownership | S1 | Cross-artifact |
| REG-POS-01 | Part 6 hedged qualifier (E-04a) | S2 | Search |
| REG-POS-02 | Encyclopedia raw qualifier (E-04b) | S2 | Search |
| REG-POS-03 | Part 6 vs Encyclopedia (E-04) | S1 | Cross-artifact |
| REG-SGN-01 | WOAC 65% arithmetic (E-05) | S1 | Arithmetic |
| REG-SGN-02 | Gamma sign (E-07) | S1 | Arithmetic |
| REG-SGN-03 | CRA Q4 coupon (R-05) | S3 | Arithmetic |
| REG-SGN-04 | WOAC strike in terms (R-02) | S2 | Table parse |
| REG-XAR-01 | FTD cross-artifact | S1 | Cross-artifact |
| REG-XAR-02 | Solutions Manual mixing (A-01) | S1 | Regex |
| REG-XAR-03 | Atlas label avoidance (A-02) | S3 | Search |

**Total: 21 tests** (14 S1, 4 S2, 3 S3)

---

*Regression Test Suite | V1.0.1-GOV-1.0 | 2026-06-27*
