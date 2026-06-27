# STEG Family-Level Review

**Date:** 2026-06-20
**Family:** Steepener Notes (STEG) — Part 5.4
**Framework:** v1.3.1 (FROZEN)
**Products:** 4/4 COMPLETE
**Sections:** 5.4.1 (Vanilla STEG), 5.4.2 (RA STEG), 5.4.3 (Callable STEG), 5.4.4 (TARN STEG)

---

## 1. Family Completeness

| Check | Result | Detail |
|-------|:------:|--------|
| All products generated | PASS | 4/4 chapters written, reviewed, accepted |
| Family Transition Text | PASS | Connects from SRT (absolute rate levels) to STEG (curve slope). Accurate, educational, references Section 1.7 and 1.8 |
| Section numbering | PASS | 5.4.1 → 5.4.2 → 5.4.3 → 5.4.4 |
| Generation order compliance | PASS | Matches `production/product_generation_order.md` exactly: Vanilla → RA → Callable → TARN |

---

## 2. Family Coherence

### 2.1 Concept Progression

| Chapter | New Concept Introduced | Builds On |
|---------|----------------------|-----------|
| Vanilla STEG | CMS spread as coupon driver; leveraged spread; floor/cap | CMS rates (1.8), yield curves (1.7), four-leg structure (5.3.1) |
| RA STEG | Range accrual applied to CMS spread (dual-rate observation) | Vanilla STEG (5.4.1), NCRA range accrual (5.3.3), CRA ELN (5.1.10) |
| Callable STEG | Bank's call right combined with leveraged CMS spread | Vanilla STEG (5.4.1), IR Callable (5.3.1), CRA SRT (5.3.4) |
| TARN STEG | Target accumulation with automatic redemption; path dependency | Vanilla STEG (5.4.1), path dependency from Phoenix (5.1.3) |

**Assessment:** Each chapter introduces exactly one new concept while building on the family baseline. The progression is logical: baseline → conditional coupon → early termination (bank-initiated) → early termination (target-initiated). PASS.

### 2.2 Complexity Calibration

| Product | Score | Rationale |
|---------|:-----:|-----------|
| Vanilla STEG | 5 | Standard leveraged spread. CMS convexity adds moderate complexity. Comparable to CRC (5), CDS (5) |
| Callable STEG | 6 | Dual embedded options (CMS + swaption). Comparable to Phoenix (6), FCN (6), NCRA (6) |
| RA STEG | 7 | Digital spread options on two CMS rates. Correlation dependency. Comparable to Digital KI Put (7), Variance Swap (7), CRA SRT (7) |
| TARN STEG | 8 | Path-dependent target. Monte Carlo pricing. Truncation logic. Highest STEG score. No comparable product in the book yet — first score-8 product |

**Calibration against full universe:** Scores are consistent with the established scale. The RA STEG (7) is correctly higher than the Callable STEG (6) because digital spread options (on two correlated rates with dual boundaries) are harder to hedge than a single swaption. The TARN STEG (8) is the first product at this score level, appropriately reflecting path dependency and Monte Carlo pricing requirements. PASS.

### 2.3 O.2 Compliance (STEG-Specific Requirements)

| Requirement | Vanilla STEG | RA STEG | Callable STEG | TARN STEG | Result |
|-------------|:------------:|:-------:|:-------------:|:---------:|:------:|
| Yield curve visualization | ASCII in §9 + CURVE visual spec | Via Vanilla + comparison | CURVE_CSTEG_01 | CURVE_TARNSTEG_01 | PASS |
| Curve dynamics explanation | §9 (3 regimes), §10 (4 scenarios) | §9 (range on spread), §10 | §10 (4 scenarios + call) | §10 (4 scenarios), §14 (paths) | PASS |
| Rate sensitivity explanation | §15 (key rate durations) | §15 (correlation) | §15 (CMS × swaption) | §15 (path-dependent timing) | PASS |

All 4 chapters satisfy all 3 mandatory O.2 requirements. Each chapter adapts the requirements to its specific product type rather than using boilerplate. PASS.

### 2.4 Four-Leg Consistency

| Leg | Vanilla STEG | RA STEG | Callable STEG | TARN STEG |
|-----|-------------|---------|---------------|-----------|
| **Note** | CMS spread coupon (leveraged, floored, capped) | Conditional coupon (accrual on spread range) | Callable CMS spread coupon | TARN CMS spread coupon (target-limited) |
| **Issuer** | Bank funding: SOFR + spread | Bank funding: SOFR + spread | Bank funding: SOFR + spread | Bank funding |
| **Deposit** | Client collateral: cash | Client collateral: cash | Client collateral: cash | Client collateral: cash |
| **Hedge** | CMS30Y receiver + CMS2Y payer (scaled for leverage) | Digital spread option strip (cap + floor on spread) | CMS swaps (scaled) + Bermudan swaption | CMS swaps (scaled) + path-dependent overlay |

**Assessment:** All four chapters describe the same four-leg structure with appropriate product-specific variations in the Hedge leg. The Issuer and Deposit legs are consistent. The Note leg varies by product type. PASS.

### 2.5 Analogy Quality

| Product | Analogy | Domain Collision Check | Mapping Quality |
|---------|---------|:---------------------:|:---------------:|
| Vanilla STEG | Hydroelectric dam | No collision | Strong — height difference = spread, electricity = coupon |
| RA STEG | Greenhouse climate control | No collision (ZCL uses wine barrel — different wine/agriculture domain) | Strong — temperature differential range = spread range, crop = coupon |
| Callable STEG | Seasonal fruit stand with revocable license | No collision | Strong — price spread = CMS spread, revocable license = call |
| TARN STEG | Coffee shop loyalty card | No collision | Strong — stamps = coupons, full card = target, auto-redeem = early termination |

**Assessment:** All 4 analogies are distinct, intuitive, and map accurately to the product mechanics. No domain collisions with the 29 existing analogies or reserved domains. PASS.

---

## 3. Family-Level Quality

### 3.1 Scores

| Metric | Vanilla STEG | RA STEG | Callable STEG | TARN STEG | Family Average |
|--------|:-----------:|:------:|:-------------:|:---------:|:--------------:|
| Educational | 8.9 | 9.0 | 8.8 | 9.1 | 8.95 |
| Visual | 8.5 | 9.0 | 8.5 | 9.0 | 8.75 |
| Terminology | 100% | 100% | 100% | 100% | 100% |
| Consistency | 8.5 | 9.0 | 8.5 | 9.0 | 8.75 |
| Pub Readiness | 8.5 | 9.0 | 8.5 | 9.0 | 8.75 |

### 3.2 Comparison with Prior Families

| Family | Products | Avg Educational | Avg Visual | Terminology | First-Pass |
|--------|:--------:|:---------------:|:----------:|:-----------:|:----------:|
| ELN (5.1) | 15 | 8.63 | 7.77 | 99% | 100% |
| Swaps (5.2) | 8 | 8.71 | 8.06 | 100% | 100% |
| SRT (5.3) | 5 | 8.82 | 8.60 | 100% | 100% |
| **STEG (5.4)** | **4** | **8.95** | **8.75** | **100%** | **100%** |

**Trend:** Consistent improvement across families. Each successive family has higher average scores, reflecting accumulated experience and framework maturation. STEG has the highest family averages across all metrics.

---

## 4. STEG-Specific Teaching Assessment

The user specified 10 STEG-specific teaching requirements. Assessment:

| # | Requirement | Where Taught | Quality |
|:-:|-------------|-------------|:-------:|
| 1 | Yield curve intuition | Vanilla STEG §1, §2, §9 (analogy, ASCII curve, 3 regimes) | HIGH |
| 2 | Curve shape visualization | Vanilla STEG §9 (ASCII), CURVE_VSTEG_01, CURVE_CSTEG_01, CURVE_TARNSTEG_01 | HIGH |
| 3 | Steepening vs flattening | Vanilla STEG §10 (4 scenarios covering steep, moderate, flat, inverted) | HIGH |
| 4 | Rate-path dependency | TARN STEG §11, §14 (explicit path dependency explanation), §22 (common mistake #5) | HIGH |
| 5 | Range accrual interaction | RA STEG entire chapter — range accrual mechanism applied to CMS spread | HIGH |
| 6 | Target redemption mechanics | TARN STEG §11, §12, §14 (target counter, truncation, accumulation paths) | HIGH |
| 7 | Early termination logic | Callable STEG §10 (call scenarios), §13 (lifecycle with call), TARN STEG §11 (target trigger) | HIGH |
| 8 | Coupon accumulation logic | TARN STEG §18 (10-quarter worked example with running cumulative) | HIGH |
| 9 | Curve-risk explanation | Vanilla STEG §15 (key rate durations, parallel vs twist), §9 Desk Reality (curve twist) | HIGH |
| 10 | Real desk usage | All 4 chapters: Desk Reality section with specific trader concerns, junior mistakes, operational challenges | HIGH |

All 10 requirements satisfied at HIGH quality. Each concept is taught using stories, analogies, intuition, and worked examples before technical terminology, maintaining beginner accessibility.

---

## 5. Advisory Notes

| ID | Severity | Note | Recommendation |
|:--:|:--------:|------|---------------|
| FA1 | Low | The RA STEG (5.4.2) complexity score (7) is higher than the Callable STEG (5.4.3) score (6), despite the Callable being introduced later in the family sequence. | Acceptable. Complexity scores reflect actual hedging difficulty, not chapter order. Digital spread options (RA STEG) are genuinely harder to hedge than a single swaption (Callable). The generation order follows the pedagogical progression, not the complexity ranking. No action needed. |
| FA2 | Low | The Vanilla STEG (5.4.1) establishes the yield curve ASCII diagram in §9 which subsequent STEG chapters reference rather than reproduce. | This is good practice — avoids redundancy. Each chapter either references the Vanilla STEG curve diagram or provides its own product-specific version. No action needed. |

---

## 6. Decision

### **STEG FAMILY: CERTIFIED COMPLETE**

All 4 products generated, reviewed, and accepted. All family-level checks pass. O.2 compliance verified. All 10 STEG-specific teaching requirements met at HIGH quality. STEG is the fourth certified family after ELN, Swaps, and SRT.

**Part 5.4 is certified.** The manuscript now has 4 complete parts: 5.1 (ELN, 15 products), 5.2 (Swaps, 8 products), 5.3 (SRT, 5 products), 5.4 (STEG, 4 products). Total: 33/49.

---

*STEG Family Review completed 2026-06-20. Framework v1.3.1 remains FROZEN.*
