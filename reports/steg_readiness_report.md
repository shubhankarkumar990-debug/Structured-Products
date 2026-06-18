# STEG Family Readiness Report

**Date:** 2026-06-18  
**Purpose:** Validate readiness to generate VSTEG001 (Vanilla Steepener Note) as the STEG family bootstrap product  
**Batch:** 3, Phase B

---

## 1. Memory Artifacts — Status

| Artifact | File | Status | Verified |
|----------|------|--------|----------|
| Terminology | `memory/terminology/STEG.yaml` | CREATED | YES |
| Booking map | `memory/booking-maps/STEG_system_mapping.yaml` | CREATED | YES |
| Style patterns | `memory/style-patterns/STEG.yaml` | CREATED | YES |

**All 3 required memory artifacts are in place.**

---

## 2. Terminology Verification

| Category | Count | Key entries |
|----------|------:|-------------|
| Product names | 4 | Vanilla Steepener, Range-Accrual Steepener, Callable Steepener, TARN |
| System names | 2 | Murex, Termsheet |
| Rate terms | 12 | CMS, CMS spread, convexity adjustment, SOFR, EURIBOR, DV01, OIS, etc. |
| STEG-specific terms | 6 | CMS spread, convexity adjustment, leverage, floor, cap, target level |
| Forbidden phrases | 9 | Same as ELN/SRT (consistency) |

**Key design decisions:**
- CMS spread defined as "long tenor minus short tenor" (positive when steep) — canonical convention
- Convexity adjustment flagged as "single most important pricing concept" for STEG family
- Leverage term defined with typical range (3x–7x) for calibration
- TARN target level included as STEG-specific (not present in SRT or ELN terminology)

---

## 3. Booking Map Verification

| Check | Result | Notes |
|-------|--------|-------|
| System type | `murex_four_leg` | Same as SRT — confirmed appropriate for rate-curve products |
| Murex used | `true` | NEMO/Sophis NOT used (consistent with SRT) |
| Note leg fields | 10 | Includes CMS-specific: coupon formula, leverage, floor, cap, CMS fixing dates, target level |
| Issuer leg fields | 3 | Standard: funding rate, curve, credit spread |
| Deposit leg fields | 3 | Standard: deposit rate, tenor, rollover |
| Hedge leg fields | 8 | CMS-specific: CMS cap/floor, CMS spread option, correlation assumption, convexity adjustment model |
| FTP fields | 3 | Standard |
| Discounting fields | 2 | Standard: OIS / issuer curve |
| STEG-specific booking | 3 | CMS fixing source, convexity adjustment consistency, correlation calibration |

**Key design decisions:**
- Hedge leg extended with CMS-specific instruments (CMS cap, CMS floor, CMS spread option) not present in SRT
- Three critical STEG-specific booking items identified: CMS fixing, convexity adjustment, correlation
- Correlation flagged as "NOT directly observable — implied/model parameter" to guide QA agent

**Consistency with SRT:** The four-leg framework is identical in structure. STEG extends SRT's hedge leg with CMS-specific instruments and adds three STEG-specific booking considerations. No structural conflicts.

---

## 4. Style Pattern Verification

| Check | Result | Notes |
|-------|--------|-------|
| Canonical H4 names | 8 | Same as all families |
| Known false positives | 3 | H4 names, Murex for STEG, Termsheet casing |
| Approved patterns | 4 | USD prefix, shorthand format, Murex four-leg, CMS spread notation |
| Accepted conventions | 4 | Termsheet, normal vol, CMS spread in bps, approximate convexity adjustment |

**Key design decisions:**
- CMS spread notation canonicalised: "CMS 30Y − CMS 10Y" with minus sign (−), not hyphen (-). Long tenor first.
- "Approximate convexity adjustment" accepted as convention — model-dependent values are inherently approximate
- "CMS spread in basis points" accepted — market convention, should not be flagged as imprecise
- Inherited SRT conventions (normal vol in bps, Termsheet) for consistency across rate product families

**Consistency with SRT:** All 3 SRT accepted conventions are either inherited or paralleled. The 1 new convention (CMS spread in bps) is STEG-specific. No conflicts.

---

## 5. Cross-Family Consistency Check

| Dimension | ELN | SRT | STEG | Consistent? |
|-----------|-----|-----|------|:-----------:|
| System type | nemo_sophis | murex_four_leg | murex_four_leg | YES — rate products use Murex |
| Canonical H4 names | 8 standard | 8 standard | 8 standard | YES |
| Currency notation | USD + international | USD + international | USD + international | YES |
| Forbidden phrases | 14 | 9 | 9 | YES (STEG matches SRT) |
| Shorthand format | Italic, ≤8 words | Italic, ≤8 words | Italic, ≤8 words | YES |
| Termsheet convention | Accepted | Accepted | Accepted | YES |

No cross-family conflicts detected.

---

## 6. VSTEG001 Product Profile

| Attribute | Value |
|-----------|-------|
| Product ID | VSTEG001 |
| Product name | Vanilla Steepener Note |
| Family | STEG |
| Section | 7.2 |
| Archetype | Bond + leveraged CMS spread coupon (floored, optionally capped) |
| System | Murex four-leg |
| Key pricing concept | Convexity adjustment on CMS rates |
| Key recon risk | CMS fixing source consistency, convexity adjustment matching |
| Expected complexity | Medium (no path dependency beyond fixing dates) |
| Expected memory usage | 3 (new STEG artifacts — first use) |

**Why VSTEG001 as bootstrap product:**
- Simplest STEG structure (no range accrual, no call, no target redemption)
- Establishes the CMS spread coupon pattern that all other STEG products extend
- Validates the convexity adjustment treatment that is critical for all STEG products
- Analogous role to RC001 (ELN bootstrap) and IRCFRN001 (SRT bootstrap)

---

## 7. Risk Assessment for VSTEG001

| Risk | Severity | Likelihood | Mitigation |
|------|----------|------------|------------|
| Convexity adjustment arithmetic | Medium | Medium | QA arithmetic verification protocol will verify. Approximate values are acceptable (accepted convention). |
| CMS spread notation inconsistency | Low | Low | Canonical notation defined in style patterns (CMS 30Y − CMS 10Y). |
| Murex four-leg booking unfamiliar | Low | Low | Same framework as SRT (IRCFRN001). Pattern established. |
| New memory artifacts untested | Medium | Certain | First use of STEG memory. Any issues will be caught by QA/style gates and corrected before subsequent STEG products. |
| Cross-reference to SRT products | Low | Likely | VSTEG001 may reference SRT range accrual for comparison. SRT products will exist by Phase B. |

No HIGH-severity risks. All identified risks have mitigations.

---

## 8. Readiness Checklist

| # | Check | Status |
|--:|-------|--------|
| 1 | STEG terminology memory created | PASS |
| 2 | STEG booking-map memory created | PASS |
| 3 | STEG style-pattern memory created | PASS |
| 4 | Cross-family consistency verified | PASS |
| 5 | VSTEG001 product profile defined | PASS |
| 6 | Risk assessment completed | PASS |
| 7 | No HIGH-severity risks | PASS |
| 8 | Pipeline v2.1 stable (16-product streak) | PASS |
| 9 | SRT memory available for cross-reference | PASS |
| 10 | Batch 3 Phase A (SRT products) scheduled before Phase B | PASS |

**10/10 checks PASS.**

---

## Verdict

**GO.** STEG family is ready for bootstrap generation. VSTEG001 can proceed as Batch 3 Phase B after Phase A (SRT products) is complete.

**Recommended execution order:**
1. Phase A: AFRN001, NCRA001, CRASRT001, DCFN001 (all SRT — reuse existing SRT memory)
2. Phase B: VSTEG001 (STEG bootstrap — first use of new STEG memory)
3. Post-batch: Update catalog, dashboard, production history, create commit, generate reports
