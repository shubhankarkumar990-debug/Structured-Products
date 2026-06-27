# Structurer Realism Audit

**Date:** 2026-06-22
**Auditor:** Independent Quality Gate
**Standard:** Does the Solutions Manual reflect how structuring desks actually operate?

---

## 1. Recommendation Realism Assessment

Each recommendation assessed: Would a real structurer give this advice?

### Fully Realistic (32 of 40)

These scenarios produce recommendations that match real desk practice:

| Category | Realistic Scenarios |
|----------|-------------------|
| Cat 1 (Protection) | 1.1, 1.2, 1.3, 1.5 |
| Cat 2 (Yield) | 2.1, 2.2, 2.3, 2.4, 2.5, 2.6, 2.7 |
| Cat 3 (Income) | 3.1, 3.2, 3.3, 3.5 |
| Cat 4 (Rates) | 4.2, 4.3, 4.4, 4.5 |
| Cat 5 (Credit) | 5.1, 5.3, 5.4, 5.5 |
| Cat 6 (Vol) | 6.1, 6.3, 6.4 |
| Cat 7 (Portfolio) | 7.1, 7.3, 7.4, 7.5 |
| Cat 8 (Specialist) | 8.1, 8.2, 8.3, 8.4 |

### Theoretically Correct but Practically Weak (6 of 40)

| Scenario | Issue | Severity |
|----------|-------|:--------:|
| **4.1 (IRS/VLSP)** | VLSP placed at rung 1 of the ladder (below IRS). In practice, IRS is always the default. VLSP is a niche product — desks don't start with VLSP and "escalate" to IRS. The ladder is inverted relative to real workflow. | **MEDIUM** |
| **5.2 (Skew CLN)** | Technically correct that Skew CLN offers recovery-rate exposure. Practically, Skew CLN is rarely offered to clients directly — it's more of an inter-dealer product. Most desks would recommend a CLN with customized recovery assumptions instead. | LOW |
| **3.4 (TARN STEG)** | TARN STEG recommendation is correct for the stated need. But in practice, TARN STEGs have poor secondary market liquidity and most structurers would push clients toward Callable STEG with a voluntary exit trigger rather than an automatic target feature. | LOW |
| **6.2 (Opt-on-RC)** | Compound options on structured products are technically valid but rarely traded. Most desks would recommend buying the RC later (if conditions improve) rather than paying premium for an option on an option. | LOW |
| **7.2 (CommSwap)** | Recommendation is correct but scenario is generic. Real commodity hedging depends heavily on the specific commodity, delivery location, and basis risk — the scenario doesn't capture this specificity. | LOW |
| **1.4 (Bonus)** | Bonus recommendation is correct. However, the scenario presents Bonus as the ONLY candidate — in practice, a structurer would also consider a PPN with a put spread or a reverse convertible with a very low barrier. The single-candidate framing feels artificial. | LOW |

### Verdict on Realism

| Rating | Count | Percentage |
|--------|:-----:|:----------:|
| Fully realistic | 32 | 80% |
| Practically weak | 6 | 15% |
| Incorrect | 0 | 0% |
| Misleading | 0 | 0% |
| Not assessed (edge case) | 2 | 5% |

**80% fully realistic is STRONG for an educational artifact.** The 15% practically weak are minor — they teach correct principles even if the specific product recommendation is rarely executed exactly as described.

---

## 2. Flagged Recommendations

### FLAG 1: Scenario 4.1 — Inverted Ladder (VLSP before IRS)

**Problem:**
```
Ladder:
1. VLSP (2) — enhanced IRS for specific customization
   ↑ If standard terms sufficient: prefer more liquid option
2. IRS (3) — global standard
```

The escalation trigger says "prefer more liquid option" — which is IRS. But the ladder protocol says "start at lowest complexity and escalate." VLSP (2) is lower complexity than IRS (3), so the ladder correctly puts VLSP first. The conflict is between complexity ordering and market-practice ordering.

**Real practice:** Every structurer starts with IRS. VLSP is a customized variant used when standard IRS terms don't fit. The ladder should be:
```
1. IRS (3) — global standard, most liquid
   ↑ If standard terms insufficient and need bespoke features: consider
2. VLSP (2) — customized rate swap for specific requirements
```

But this VIOLATES the complexity ordering rule (going from 3→2 is de-escalation).

**Root cause:** VLSP's Complexity 2 score doesn't match its practical role. In real structuring, VLSP is not "simpler" than IRS — it's more customized. The Atlas complexity score creates a mismatch.

**Impact:** MEDIUM. Readers may form incorrect impression that VLSP is the default starting point for rate hedging. The recommendation (IRS) is correct, but the ladder path is inverted.

**Fix required:** No — Atlas is FROZEN. The ladder correctly follows complexity rules even though market practice differs. Add a note acknowledging the inversion.

---

### FLAG 2: Scenario 5.2 — Skew CLN Availability

**Problem:** Skew CLN is recommended as the product for recovery-rate views. In practice, Skew CLN is a specialist product with limited availability at many banks.

**Impact:** LOW. The scenario correctly teaches that recovery rate views exist and can be traded. Even if Skew CLN isn't available at every desk, the CONCEPT of asymmetric credit payoffs is valuable.

---

## 3. Desk Economics Treatment

### §1.5 Framework Assessment

The Desk Economics Lens covers 4 dimensions:
1. Higher margin → RC over PPN — **CORRECT and well-quantified** ("2–3× margin")
2. Easier to hedge → index over single-stock — **CORRECT**
3. Lower operational burden → RC over Phoenix — **CORRECT** (European vs periodic observations)
4. Lower capital consumption → notes over swaps — **CORRECT** (funded vs unfunded)

**Missing dimension:** Funding benefit. The desk's funding cost advantage on notes vs swaps is a major driver of product selection. CLN's desk note mentions it (line 1200), but the §1.5 framework doesn't include it explicitly.

**Severity: LOW.** The principle is taught via the CLN desk note. A §1.5 addition would be cleaner but not critical.

### Desk Note Distribution

| Category | Scenarios With Desk Notes | Scenarios Without |
|----------|:------------------------:|:-----------------:|
| Cat 1 (Protection) | 1.4 | 1.1, 1.2, 1.3, 1.5 |
| Cat 2 (Yield) | 2.1, 2.4 | 2.2, 2.3, 2.5, 2.6, 2.7 |
| Cat 3 (Income) | 3.1 | 3.2, 3.3, 3.4, 3.5 |
| Cat 4 (Rates) | — | 4.1, 4.2, 4.3, 4.4, 4.5 |
| Cat 5 (Credit) | 5.1, 5.5 | 5.2, 5.3, 5.4 |
| Cat 6 (Vol) | 6.1, 6.3 | 6.2, 6.4 |
| Cat 7 (Portfolio) | 7.1, 7.4 | 7.2, 7.3, 7.5 |
| Cat 8 (Specialist) | — | 8.1, 8.2, 8.3, 8.4 |

**Count: 10 of 40 scenarios have desk notes (25%).**

Per the enhancement review specification: "selective desk notes only when desk economics is a material tiebreaker (estimated 10 of 40 scenarios)." **Exactly matches specification.**

### Missing Desk Notes Assessment

| Scenario | Should Have Desk Note? | Why |
|----------|:---------------------:|-----|
| 2.6 (CRC/ICN) | MAYBE | Callable products have margin implications for the desk |
| 4.1 (IRS) | NO | IRS is vanilla — desk economics is standard |
| 8.4 (WOAC) | Already in 6.3 | Would be redundant |

**No critical missing desk notes.**

---

## 4. Market Regime Realism

### §1.3 Regime Matrix Assessment

| Regime | Accuracy | Issue |
|--------|:--------:|-------|
| High equity vol → RC/Phoenix benefit | CORRECT | Premium richness drives coupon |
| Low equity vol → PPN benefits | CORRECT | Cheap option → high participation |
| Steep curve → STEG benefits | CORRECT | CMS spread widens |
| Flat curve → STEG suffers | CORRECT | Zero spread = zero coupon |
| Wide spreads → CLN benefits | CORRECT | High credit premium |
| Tight spreads → CLN suffers | CORRECT | Low compensation |
| Rising rates → PPN worse | CORRECT | Expensive ZCB |
| Falling rates → PPN better | CORRECT | Cheap ZCB |

**All 8 regime assessments are accurate.**

### Per-Scenario Regime Notes

Spot-checked 10 of 40 regime notes:

| Scenario | Regime Note | Accurate? |
|----------|-----------|:---------:|
| 1.1 | Low rates → PPN participation <40% | YES |
| 2.1 | Low vol → RC premiums shrink to 4–6% | YES |
| 3.1 | Flat curve → avoid STEG | YES |
| 5.3 | High corr → FTD risk drops | YES |
| 6.1 | Long vol when implied cheap vs realized | YES |
| 6.3 | WOAC suffers in dispersion events | YES |
| 7.3 | XCCY basis widens in USD stress | YES |
| 1.4 | Bonus works in low-vol (barrier safe) | YES |
| 3.4 | TARN STEG in flat curve = expensive zero income | YES |
| 4.4 | Range accrual fails in trending rates | YES |

**10/10 regime notes are accurate.** No false or misleading regime guidance detected.

---

## 5. Anti-Instincts Assessment (§1.6)

| Anti-Instinct | Real-World Accuracy | Common in Practice? |
|--------------|:-------------------:|:-------------------:|
| "Yield" → PPN wrong (zero coupon) | CORRECT | YES — juniors confuse participation with yield |
| "Protection" → RC wrong (conditional) | CORRECT | YES — most common retail misunderstanding |
| "Max coupon" → WOAC dangerous | CORRECT | YES — PB clients chase coupon without understanding worst-of |
| "Vol exposure" → VarSwap short catastrophic | CORRECT | YES — 2018 Volmageddon is textbook example |
| "Bullish" → Phoenix wrong (autocall caps return) | CORRECT | YES — autocall termination is widely misunderstood |

**All 5 anti-instincts are accurate and reflect real structuring mistakes.**

---

## 6. Overall Realism Verdict

| Dimension | Score | Notes |
|-----------|:-----:|-------|
| Recommendation accuracy | **9/10** | 32/40 fully realistic, 0 incorrect |
| Desk economics realism | **8/10** | Missing funding dimension in §1.5 framework |
| Market regime accuracy | **10/10** | All 8 regimes + 10/10 spot-checked notes correct |
| Anti-instinct accuracy | **10/10** | All 5 match real desk practice |
| Practical applicability | **8/10** | 6 scenarios are theoretically correct but rarely executed as described |

**Overall Realism Score: 9.0/10**

**The Solutions Manual teaches structuring decisions that match real desk practice.** The minor flags (inverted VLSP ladder, Skew CLN availability) are edge cases that don't undermine the educational framework.

---

*Structurer realism audit complete. 2026-06-22.*
