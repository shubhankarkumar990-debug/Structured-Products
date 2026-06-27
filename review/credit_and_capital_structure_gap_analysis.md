# Credit & Capital Structure — Gap Analysis

**Date:** 2026-06-25
**Scope:** Phase 4 audit — capital structure hierarchy, credit events, restructuring clauses, seniority
**Source:** Desk Bible v2 (22,620 lines, 49 products, 6 families)
**Method:** Word-boundary term counts + manual section review

---

## Executive Summary

The Bible covers credit events at a functional level sufficient for understanding CDS and CLN products. Bankruptcy, failure to pay, and restructuring are listed and explained. However, the treatment stops at identification — the Bible does not explain the four restructuring clause variants (FR/MR/MMR/NR) that determine which obligations are deliverable after a restructuring event. This is a critical gap for CLN settlement mechanics and CDS basis trading. Capital structure is taught at an introductory level (debt vs equity in Part 0) but the full seniority waterfall, AT1/T2 distinction, and bail-in mechanics are absent.

---

## Term Count Evidence

### Capital Structure Terms

| Term | Count | Notes |
|------|:-----:|-------|
| Preferred Equity | 0 | Absent |
| Senior Debt | 2 | General context only |
| Senior Preferred | 0 | Absent |
| Senior Non-Preferred | 0 | Absent |
| Subordinated | 2 | 1 in recovery rate table (line 1427: "Subordinated debt: recovery rates of 10-30%"), 1 general |
| Tier 1 | 0 | Absent |
| AT1 | 0 | Absent |
| Tier 2 | 0 | Absent |
| Bail-In | 0 | Absent |
| Hybrid Capital | 0 | Absent |
| Seniority | 2 | Line 12929 (zero-coupon bond recovery "depends on the bank's seniority") and line 16787 (CLN "entity's seniority") |

### Credit Event Terms

| Term | Count | Notes |
|------|:-----:|-------|
| Reference Entity | 69 | Well covered across CDS and CLN chapters |
| Reference Obligation | 1 | Red Flag entry only (line 10664) |
| Deliverable Obligation | 3 | Mentioned but not explained |
| Credit Event | 145 | Extensively covered |
| Bankruptcy | 10 | Explained as credit event type |
| Failure To Pay | 7 | Explained as credit event type |
| Restructuring | 15 | Listed as credit event; no variant detail |
| Full Restructuring (CR) | 0 | Absent |
| Modified Restructuring (MR) | 0 | Absent |
| Modified Modified Restructuring (MMR) | 0 | Absent |
| No Restructuring (NR) | 0 | Absent |

---

## Detailed Gap Analysis

### 1. Capital Structure Hierarchy

| Aspect | Coverage Status | Evidence |
|--------|:--------------:|---------|
| Debt vs equity basic distinction | COVERED | Part 0 (§0.3) teaches this at introductory level |
| Senior unsecured debt | MINIMAL | 2 mentions, no structural explanation |
| Subordinated debt | MINIMAL | 1 mention in recovery rate context (line 1427) |
| Recovery rate by seniority | PARTIAL | Line 1427 gives ranges ("subordinated: 10-30%") but no full waterfall |
| Senior Preferred vs Senior Non-Preferred | MISSING | 0 mentions; distinction created by EU BRRD is absent |
| AT1 (Additional Tier 1) capital | MISSING | 0 mentions |
| Tier 2 capital | MISSING | 0 mentions |
| CoCo bonds (Contingent Convertible) | MISSING | Not mentioned despite being a major structured product class |
| Bail-in mechanics (BRRD/TLAC) | MISSING | 0 mentions |
| Loss absorption waterfall | MISSING | No diagram or explanation of equity → AT1 → T2 → SNP → SP → Senior |
| Hybrid capital instruments | MISSING | 0 mentions |

**Severity:** HIGH
**Impact:** Capital structure knowledge is foundational for credit-linked products. The CLN family (4 products) requires understanding which obligations are deliverable after a credit event and what recovery to expect based on seniority. The Bible provides recovery rate ranges (line 1427) but does not explain WHY subordinated debt recovers less — no structural waterfall, no claim priority explanation. For AT1/CoCo products (absent from the Bible's product universe but referenced in industry practice), the gap is total.

---

### 2. Seniority & Recovery Implications for CLN Products

| Aspect | Coverage Status | Evidence |
|--------|:--------------:|---------|
| Recovery rate concept | COVERED | Explained in CDS chapter and CLN chapters |
| Recovery rate varies by seniority | PARTIAL | Line 16787: "market-standard recovery rate for the entity's seniority" |
| Senior vs subordinated recovery difference | PARTIAL | Line 1427: ranges given (senior 30-60%, subordinated 10-30%) |
| Recovery rate auction mechanics | COVERED | CDS chapter §11 explains ISDA auction settlement |
| How seniority affects CLN investor outcomes | MINIMAL | Line 16986: "recovery rate... can vary from 10% to 80% depending on the reference entity's assets, seniority, and circumstances" — but no explanation of mechanism |
| Deliverable obligation criteria and seniority constraints | MISSING | Deliverable obligations mentioned 3 times, never explained |

**Severity:** MEDIUM
**Impact:** A CLN investor's loss-given-default depends directly on which obligations are deliverable and their seniority ranking. The Bible acknowledges this ("depends on seniority") but does not teach the mechanics. A reader would know seniority matters but not how to evaluate it.

---

### 3. Credit Event Types — Functional Coverage

| Credit Event | Coverage Level | Evidence |
|--------------|:--------------:|---------|
| Bankruptcy | ADEQUATE | Defined in CDS §11 (line 10559): "the reference entity files for bankruptcy" |
| Failure to Pay | ADEQUATE | Defined in CDS §11 (line 10560): "a missed payment on debt obligations beyond a grace period" |
| Restructuring | PARTIAL | Defined in CDS §11 (line 10561): "debt terms are modified unfavorably for creditors." Scenario 4 (line 10546-10547) gives a worked example. But no variant detail |
| Obligation Default | MISSING | Not mentioned (removed in 2014 definitions but relevant for 2003 legacy trades) |
| Obligation Acceleration | MISSING | Not mentioned (removed in 2014 definitions) |
| Repudiation/Moratorium | MISSING | Not mentioned (sovereign CDS relevant) |
| Governmental Intervention | MISSING | Not mentioned (2014 definitions addition for financial institutions) |

**What the Bible gets right:** The CDS chapter's §17 Red Flags correctly identifies "ISDA definitions version mismatch" as a risk and notes that "2003 vs 2014 ISDA Credit Definitions have different credit event triggers (notably 'restructuring')" (line 10661). This shows awareness of the issue. But the Red Flag entry tells the reader to "verify which version applies" without explaining what the differences are.

**Severity:** MEDIUM (for base credit events: adequate), HIGH (for restructuring variants: absent)

---

### 4. CDS Restructuring Clauses

This is the single most significant credit gap in the Bible.

| Clause | Coverage | Regional Usage | Settlement Impact |
|--------|:--------:|----------------|-------------------|
| Full Restructuring (CR / Old R) | MISSING | Historical; pre-2003 standard | All obligations deliverable, no maturity limitation |
| Modified Restructuring (Mod R) | MISSING | North American standard | Deliverable obligations limited to maturity ≤ 30 months post-restructuring |
| Modified Modified Restructuring (Mod Mod R) | MISSING | European standard | Deliverable obligations limited to maturity ≤ 60 months for restructured obligations, ≤ 30 months for others |
| No Restructuring (NR) | MISSING | Index CDS standard (CDX, iTraxx) | Restructuring does not trigger settlement |

**Why this matters:**

1. **CLN settlement mechanics.** When a CLN references a CDS with Mod R, the investor's recovery depends on which obligations are deliverable. Maturity limitations on deliverable obligations can significantly affect recovery — shorter-dated obligations typically trade closer to par, meaning the protection buyer recovers less. The Bible's CLN chapters do not mention this.

2. **CDS basis trading.** The restructuring clause is one of the primary drivers of CDS-bond basis. The Bible mentions basis risk (CDS §15, line 10632) but does not connect it to restructuring clauses.

3. **Regional differences.** North American CDS uses Mod R or NR. European CDS historically uses Mod Mod R. Asian CDS varies. A trader or structurer working across regions needs to understand these differences. The Bible does not distinguish.

4. **The CDS chapter acknowledges the gap.** Line 10661 (Red Flag): "2003 vs 2014 ISDA Credit Definitions have different credit event triggers (notably 'restructuring')." The Red Flag identifies the problem but does not teach the content.

**Severity:** CRITICAL (for CLN settlement and CDS basis trading)
**Impact:** A professional pricing a CLN or managing a CDS book would not know from the Bible alone which restructuring clause applies to their trade, what it means for deliverable obligations, or how it affects basis risk. This is not theoretical — restructuring events occur (the Bible's own Scenario 4 describes one) and the clause variant determines the economic outcome.

---

### 5. Capital Structure Impact on Structured Product Investors

| Aspect | Coverage Status | Evidence |
|--------|:--------------:|---------|
| Issuer credit risk concept | COVERED | Part 0 and individual chapters mention "issuer credit risk" |
| Issuer seniority and recovery for note holders | MISSING | Line 12929 mentions "the bank's seniority and resolution proceedings" but does not explain |
| AT1/CoCo linkage to structured product risk | MISSING | AT1 instruments not covered at all |
| Bail-in risk for note investors | MISSING | If an issuer is bailed in, structured note holders may face write-down; not explained |
| Resolution and MREL/TLAC implications | MISSING | Not mentioned |
| Structural subordination of holding company issuance | MISSING | Not mentioned |

**Severity:** HIGH
**Impact:** Structured product investors bear issuer credit risk. If the issuing bank enters resolution, the investor's recovery depends on where structured notes sit in the capital structure. The Bible mentions issuer credit risk as a concept but does not explain the resolution framework that determines outcomes. This is increasingly important post-2008 with bail-in regimes in place across major jurisdictions.

---

### 6. Deliverable Obligation Mechanics

| Aspect | Coverage Status | Evidence |
|--------|:--------------:|---------|
| Deliverable obligation concept | MINIMAL | 3 mentions across the manuscript |
| Deliverable obligation characteristics (transferable, not bearer, maximum maturity) | MISSING | Not explained |
| Deliverable obligation vs reference obligation distinction | PARTIAL | Red Flag (line 10664): "deliverable obligations may differ from the reference obligation" — identifies the risk but does not explain the mechanics |
| Cheapest-to-deliver option | MISSING | Not mentioned |
| Asset package delivery (post-2014 definitions) | MISSING | Not mentioned |
| Loan vs bond deliverability | MISSING | Not mentioned |

**Severity:** MEDIUM
**Impact:** The cheapest-to-deliver option is a key driver of CDS economics — when physical settlement occurs, the protection buyer delivers the cheapest qualifying obligation, not necessarily the reference obligation. This affects CLN recovery outcomes. The Bible's CDS chapter correctly warns about "reference obligation confusion" (Red Flag) but does not explain why the distinction matters economically.

---

## Gap Severity Summary

| Category | Severity | Rationale |
|----------|:--------:|-----------|
| Restructuring clause variants (FR/MR/MMR/NR) | CRITICAL | Zero coverage; directly affects CLN settlement and CDS basis |
| Capital structure hierarchy (AT1/T2/bail-in) | HIGH | Zero coverage on bank capital instruments |
| Capital structure impact on note investors | HIGH | Issuer resolution affects all structured note holders |
| Credit event types — base coverage | ADEQUATE | Bankruptcy, FTP, restructuring defined and illustrated |
| Seniority & recovery mechanics | MEDIUM | Acknowledged but not explained |
| Deliverable obligation mechanics | MEDIUM | Mentioned in Red Flags but no methodology |

---

## Structural Observation

The Bible's credit coverage follows a clear pattern: it teaches what credit events ARE (adequate) but not the contractual fine print that determines SETTLEMENT OUTCOMES (missing). This is consistent with the Bible's pedagogical architecture — it prioritizes understanding over operational detail. However, restructuring clauses are not "fine print" — they are a fundamental pricing input for CDS and a settlement determinant for CLNs.

The most efficient remediation would be:
1. A dedicated restructuring clause section within the CDS chapter (§5.2.5) — approximately 400-600 words covering the four variants, regional conventions, and settlement implications.
2. A cross-reference from each CLN chapter to this section, noting which restructuring clause typically applies.
3. A Part 0 section on capital structure waterfall (extending the existing §0.3 Debt vs Equity) — approximately 300-500 words covering the seniority stack from equity through AT1/T2 to senior debt.
