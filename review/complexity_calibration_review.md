# Complexity Calibration Review — Phase 4

**Date:** 2026-06-22
**Pass:** Publication Metadata Audit
**Status:** READ-ONLY — no manuscript modifications
**Scope:** All 49 products — complexity_registry.yaml as canonical source

---

## Verdict: PASS — Registry calibration is sound. Manuscript alignment required.

The canonical complexity_registry.yaml is well-calibrated across all 6 families. All scores are defensible against the governance scale definition. The 16 manuscript/CM discrepancies are an alignment problem, not a calibration problem.

---

## 1. Scale Distribution

| Tier | Definition | Count | Share |
|:----:|-----------|:-----:|:-----:|
| 1-2 | Vanilla: one or zero embedded features | 4 | 8% |
| 3-4 | Standard structured: one feature/condition | 17 | 35% |
| 5-6 | Moderate: multiple features/conditions | 17 | 35% |
| 7-8 | Complex: path-dependent, multi-barrier, nonlinear | 10 | 20% |
| 9-10 | Highly complex: specialist, correlation-dependent | 1 | 2% |

**Distribution shape:** Right-skewed bell curve centered at 4-5. Appropriate — a desk bible covering the full product spectrum should have more standard products than exotic.

**Unused scores:** 1 and 9 are empty. Score 1 is appropriate for nothing in this universe (even the simplest products — PPN, Forward — have at least one structural feature). Score 9 gap is notable but defensible: the jump from NTD/TARN/WOAC (8) to CDO (10) reflects CDO's uniquely portfolio-level, model-dependent nature.

---

## 2. Family Calibration

| Family | Count | Range | Avg | Spread | Assessment |
|--------|:-----:|:-----:|:---:|:------:|-----------|
| ELN | 15 | 2–7 | 4.3 | 5 | Well-distributed. PPN(2)→DKIP(7) tracks feature addition |
| Swaps | 8 | 2–7 | 4.5 | 5 | Good. VLSP(2)→Variance(7) tracks payoff nonlinearity |
| SRT | 5 | 4–7 | 5.4 | 3 | Tight, correct. All moderate-complex rates structures |
| STEG | 4 | 5–8 | 6.5 | 3 | Correct. CMS spread + additional features drives complexity |
| CLN | 5 | 4–10 | 6.8 | 6 | Widest spread — reflects genuine spectrum from vanilla CLN to CDO |
| Other | 12 | 2–8 | 4.7 | 6 | Heterogeneous by design. Forward(2)→WOAC(8) spans full range |

### Within-Family Progression Checks

**ELN family — 15 products, 6 complexity tiers:**
```
PPN(2) → RC(3) → DRC(3) → Warrant(3) → ICN(3) → KODRC(4) → Airbag(4) → 
Bonus(4) → Digital(4) → Booster(4) → CRC(5) → Phoenix(6) → FCN(6) → 
CRA ELN(6) → DKIP(7)
```
Feature accumulation tracks correctly: one barrier → two barriers → callable → multi-observation path-dependent → three barriers + digital.

**Swaps family — 8 products, 5 tiers:**
```
VLSP(2) → IRS(3) → Commodity(4) → TRS(5) → Equity Swap(5) → CDS(5) → 
XCS(5) → Variance(7)
```
Progression from vanilla fixed/float to multi-risk-factor to nonlinear payoff. Score-5 cluster (TRS, Equity Swap, CDS, XCS) reflects comparable moderate complexity across different asset classes.

**CLN family — 5 products, 5 tiers:**
```
CLN(4) → Skew(5) → FTD(7) → NTD(8) → CDO(10)
```
Perfect escalation. Each product adds one major complexity dimension (recovery modification → basket → Nth trigger → portfolio tranching).

**SRT family — 5 products, 3 tiers:**
```
ZCL(4) → IR Callable(5) = Digital CF(5) → NCRA(6) → CRA SRT(7)
```
Clean progression from simple four-leg to range accrual to callable range accrual (dual embedded options).

**STEG family — 4 products, 4 tiers:**
```
Vanilla(5) → Callable(6) → RA(7) → TARN(8)
```
Each step adds one feature layer: CMS spread → callable → range accrual → target accumulation with auto-knock.

---

## 3. Cross-Family Comparisons

### Same-Score Products — Are They Comparably Complex?

| Score | Products | Comparable? |
|:-----:|---------|:-----------:|
| 2 | PPN, VLSP, Deposit, Forward | **YES** — all zero/one-feature vanilla |
| 3 | RC, DRC, ICN, Warrant, IRS, Options, ELO, DCI | **YES** — all one-feature standard |
| 4 | KODRC, Airbag, Bonus, Digital, Booster, Commodity Swap, ZCL, CLN, Shark Fin | **YES** — one feature with qualifier |
| 5 | CRC, TRS, Equity Swap, CDS, XCS, IR Callable, Digital CF, Vanilla STEG, Skew CLN, Option on RC | **YES** — multi-feature moderate |
| 6 | Phoenix, FCN, CRA ELN, NCRA, Callable STEG, Accumulator, Decumulator | **YES** — multiple observation dates + conditionality |
| 7 | DKIP, Variance, CRA SRT, RA STEG, FTD, Snowball, Cliquet | **YES** — path-dependent + multi-barrier or nonlinear |
| 8 | TARN STEG, NTD, WOAC | **YES** — complex path + correlation or target |
| 10 | CDO | **YES** — uniquely portfolio-level |

**Assessment:** Cross-family calibration is strong. Products at the same score level share comparable structural complexity regardless of family.

---

## 4. Borderline Cases

| Product | Score | Argument For | Argument Against | Verdict |
|---------|:-----:|-------------|-----------------|:-------:|
| IRS | 3 | Counterparty risk, rate curve sensitivity, credit terms | "No optionality" — could be 2 | **3 OK** — swap infrastructure complexity |
| Phoenix | 6 | Multiple features + path dependency | Has 5 features — could be 7 | **6 OK** — conservative but industry-standard classification |
| KODRC | 4 | Two barriers (KI + KO) | Could be 5 due to continuous monitoring | **4 OK** — observation is simple (continuous, not digital) |
| CDS | 5 | Credit event triggers, settlement complexity | Core product is binary — could be 4 | **5 OK** — 3 trigger types + 2 settlement methods |

**No score changes recommended.** All borderline cases fall within ±1 of alternative assessments, and the current scores are internally consistent with same-tier peers.

---

## 5. Manuscript Alignment Issues

### 16 discrepancies between registry (canonical) and manuscript §4 / CM Complexity

| Alignment | Registry | Manuscript | Delta | Direction |
|-----------|:--------:|:----------:|:-----:|:---------:|
| 5.1.3 Phoenix | 6 | 5 | -1 | Manuscript understates |
| 5.1.6 CRC | 5 | 4 | -1 | Manuscript understates |
| 5.1.7 Airbag | 4 | 3 | -1 | Manuscript understates |
| 5.1.8 Bonus | 4 | 3 | -1 | Manuscript understates |
| 5.1.9 FCN | 6 | 4 | -2 | Manuscript understates |
| 5.1.11 ICN | 3 | 4 | +1 | Manuscript overstates |
| 5.1.12 Digital Note | 4 | 3 | -1 | Manuscript understates |
| 5.1.13 Booster | 4 | 3 | -1 | Manuscript understates |
| 5.1.14 DKIP | 7 | 5 | -2 | Manuscript understates |
| 5.1.15 Warrant | 3 | 2 | -1 | Manuscript understates |
| 5.2.2 TRS | 5 | 4 | -1 | Manuscript understates |
| 5.2.3 Equity Swap | 5 | 3 | -2 | Manuscript understates |
| 5.2.5 CDS | 5 | 4 | -1 | Manuscript understates |
| 5.2.6 XCS | 5 | 6 | +1 | Manuscript overstates |
| 5.2.7 Commodity Swap | 4 | 3 | -1 | Manuscript understates |
| 5.2.8 VLSP | 2 | 5 | -3 | **Manuscript grossly overstates** |

**Pattern:** 13 of 16 are manuscript-understates. The registry was re-calibrated after initial chapter generation, raising scores for products whose complexity was initially underestimated. Only ICN, XCS, and VLSP go the other direction.

**Root cause:** Chapters were generated in batches with per-batch calibration. The registry performed a cross-universe calibration afterward but the results were never propagated back to the manuscript.

### Required actions:
1. Update 16 chapters' §4 Complexity Score to match registry
2. Update 16 chapters' CM Complexity to match registry
3. Update Complexity Rationale in §4 where it conflicts with registry rationale

---

## 6. Batch 8 Score Format Issue

4 CLN chapters (5.5.2–5.5.5) use field name "Complexity" instead of "Complexity Score", and format "X / 10" instead of bare "X / 10" in bold-header table. Their scores match the registry but the field name and format differ.

---

## 7. Summary

| Criterion | Status |
|-----------|:------:|
| Registry scores well-calibrated across 6 families | **PASS** |
| Within-family progression correct | **PASS** |
| Cross-family comparisons consistent | **PASS** |
| Scale definition compliance | **PASS** |
| Tier distribution reasonable | **PASS** |
| No borderline scores requiring change | **PASS** |
| Manuscript scores aligned with registry | **FAIL** (16 discrepancies) |
| CM scores aligned with registry | **FAIL** (16 discrepancies) |

### Blocking Issues

**Manuscript alignment REQUIRED before DNA Atlas / Comparison Matrix generation.** The 16 discrepancies would propagate into generated artifacts. The registry is canonical and its calibration is sound — the manuscript must be updated, not the registry.

---

*Phase 4 audit complete. Phase 5 (Publication Metadata Consistency) follows.*
