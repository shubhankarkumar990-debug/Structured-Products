# Ecosystem Formula & Calculation Audit

**Date**: 2026-06-25
**Scope**: Every worked example, payoff formula, and arithmetic claim across all canonical artifacts
**Auditor**: Publication Review Board (Phase 4 of 12)

---

## 1. Methodology

Every numerical statement in the Desk Bible manuscript, Interview System V2.1, and Solutions Manual was independently re-derived from stated inputs. Formulas were verified against standard market conventions. Day count calculations were checked against both stated conventions and actual arithmetic.

---

## 2. Verified Correct (No Errors Found)

| Location | Calculation | Verified |
|----------|-------------|:--------:|
| Desk Bible §6.1 (line 22730) | Day count worked example: $100M × 5% × 184 days. ACT/360=$2,555,556, 30/360=$2,500,000, ACT/365=$2,520,548. Spread=$55,556 | ✅ |
| Desk Bible §6.7 (line 24389) | SA-CCR: EAD = 1.4 × (RC + PFE) — consistent across both mentions | ✅ |
| Desk Bible §6.7 (line 24414) | RAROC Trade A: ($1M-$200K-$100K)/$50M = 1.4%. Trade B: ($500K-$100K-$50K)/$5M = 7.0% | ✅ |
| Desk Bible §5.1.2 (line 2730) | PPN: ZCB at 4% = $100/1.04³ = $88.90. Budget $11.10. Participation $11.10/$18.50 = 60%. After margin: $9.60/$18.50 ≈ 52% | ✅ |
| Desk Bible §5.3.3 (line 13496) | NCRA Q1: $75M × 5.10%/4 × 65/90 = $690,625 (see M-4 for convention note) | ✅ |
| Desk Bible §5.4.4 (line 16279) | TARN STEG: All 10 quarterly coupons, cumulative sums, truncation at $6M target — all correct | ✅ |
| Desk Bible §5.1.7 (line 3940) | DRC Samsung: $500K × $40/$72 = $277,778. Loss = $177,222 (-38.9%) | ✅ |
| Desk Bible §5.1.7 (line 3976) | DRC discount return: 9/91 = 9.9% | ✅ |
| Desk Bible §5.1.3 (line 5042) | Airbag RC: Standard RC $60K vs Airbag $80K — all scenario arithmetic correct | ✅ |
| Desk Bible §5.2.5 (line 10227) | VarSwap: Vega notional €100K, strike 22%. Variance notional = €100K/(2×22) = €2,273. Payoffs for 28% and 15% realized both correct | ✅ |
| Desk Bible Part 1 (line 1304) | Forward rate: $1,000 × 1.035² = $1,071.23. F = 1,071.23/1,030 - 1 = 4.0% | ✅ |
| Interview System IF.2 | Modified Following: March 31 Saturday → April 2 Monday crosses month → back to Friday March 30 | ✅ |
| Interview System IF.3-IF.7 | CSA collateral, recovery waterfall, CDS pricing, P&L Explain tolerance — all correct | ✅ |
| Interview System IF.9 | FTP margin: 8.5% revenue - 7% coupon - 2.40% FTP = -0.90% | ✅ |
| Interview System IF.10 | RAROC: consistent with Desk Bible worked example | ✅ |
| Interview System IF.12 | Netting benefit calculation — correct | ✅ |
| Interview System IF.13 | VarSwap P&L: $100K/(2×20) × (625-400) = $2,500 × 225 = $562,500 | ✅ |
| Interview System IF.15 | PPN: 5% → ZCB=$78 ($100/1.05⁵=78.35), participation $21/$15=140%. 1% → ZCB≈$95, participation $4/$15=26.7% | ✅ |
| Solutions Manual | 10-Step Decision Model flowchart and all sampled scenario calculations | ✅ |

---

## 3. Errors Found

### F-1 | HIGH | Interview System V2.1 line 1436

**IF.1 ACT/365 Day Count Answer Is Wrong**

Stated: $50M × 4.5% × (91/365) = **$561,644**

Verification:
- $50,000,000 × 0.045 = $2,250,000 annual interest
- $2,250,000 × (91/365) = $2,250,000 × 0.24931507 = **$560,959**

**Error: $685 overstated.**

Consequent error in spread: Stated $7,106 ($568,750 - $561,644). Correct: $7,791 ($568,750 - $560,959).

The ACT/360 answer ($568,750) and 30/360 answer ($562,500) are both correct. Only the ACT/365 value is wrong.

**Impact**: Candidates studying this question would memorize an incorrect answer. The error is small enough to appear plausible but large enough to fail a desk quiz.

---

### F-2 | MEDIUM | Desk Bible lines 1056-1068

**Greeks Worked Example: Delta Sign Convention Muddled for Short Puts**

The example states Delta = -50 for "100 short puts" and explains: "If the stock rises $1, your position loses $50."

Problem: 100 short ATM puts should have **position delta ≈ +50** (short puts benefit from stock rises). The stated delta of -50 and the explanation "stock rises → you lose" describe a **long** put position, not a short one.

The text then self-corrects: "P&L from Delta = -(-50) × (-$2) = -$100." This arrives at the **correct** final P&L (short puts lose $100 when stock drops $2), but through confusing intermediate reasoning.

**Impact**: The final P&L answer is correct. The pedagogical path to reach it is misleading because it conflates option delta with position delta for a short position. A reader could correctly memorize the self-correction technique while misunderstanding the underlying sign convention.

---

### F-3 | MEDIUM | Desk Bible lines 13490-13500

**NCRA Range Accrual: Stated ACT/360 but Calculations Use Quarterly-Fraction Method**

Terms state: "Act/360" day count convention.

Under pure ACT/360, Q2 coupon (90 in-range days):
- $75M × 5.10% × (90/360) = **$956,250**

Stated Q2 coupon: **$945,742**

The stated answer matches the formula: $75M × (5.10%/4) × (90/91) = $956,250 × 0.98901 = $945,742.

This quarterly-fraction method (max coupon = Rate/4 × Notional, pro-rated by in-range/total days) is a valid market convention but differs from pure ACT/360. The internal arithmetic is fully self-consistent — Q1 through Q4 all verify correctly under this method, and the Year 1 total of $2,862,861 is accurate.

**Impact**: The two methods diverge only when total days in a quarter ≠ 90. The example is internally consistent and teaches the concept effectively. The convention label is imprecise, not wrong — many desks call this "ACT/360" colloquially even when quarterly coupons cap at Rate/4.

---

## 4. Summary

| Severity | Count | Finding |
|:--------:|:-----:|---------|
| HIGH | 1 | IF.1 ACT/365 arithmetic error ($561,644 should be $560,959) |
| MEDIUM | 2 | Greeks Delta sign convention, NCRA day count convention label |
| LOW | 0 | — |

**Overall arithmetic accuracy**: 97% of all verified calculations are correct. The one genuine arithmetic error (F-1) is in the Interview System, not the Desk Bible manuscript. The Desk Bible's formulas and worked examples are arithmetically sound.

**Verification count**: 30+ distinct calculations independently verified across 3 artifacts.

---

## 5. Recommendations

| Priority | Action |
|:--------:|--------|
| 1 | Fix IF.1 ACT/365: change $561,644 → $560,959 and spread $7,106 → $7,791 |
| 2 | Clarify Greeks example: state Delta = +50 for short puts, or add a note explaining the option-delta vs position-delta distinction |
| 3 | Add a footnote to NCRA §18 clarifying the quarterly-fraction accrual method vs pure ACT/360 |
