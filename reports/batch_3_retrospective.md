# Batch 3 Retrospective

**Date:** 2026-06-19  
**Scope:** Phase A (4 SRT products) + Phase B (1 STEG bootstrap)  
**Pipeline:** v2.1 (stable, no changes)

---

## 1. STEG bootstrap success

VSTEG001 is the fourth family bootstrap (after ELN/PHX001, SRT/IRCFRN001, CLN/VCLN001). It is the cleanest bootstrap to date.

| Metric | ELN (PHX001) | SRT (IRCFRN001) | CLN (VCLN001) | STEG (VSTEG001) |
|--------|:------------:|:---------------:|:-------------:|:---------------:|
| Memory artifacts created | 3 | 3 | 3 | 3 |
| New conventions discovered | 12 | 3 | 2 | 1 |
| Pipeline retries | 0 | 0 | 0 | 0 |
| QA BLOCKERs | 0 | 0 | 0 | 0 |
| Cross-family refs | 0 | 0 | 1 | 3 |
| Memory corrections needed | 0 | 0 | 0 | 0 |

**Declining convention count is expected.** ELN was the first family — everything was new. By STEG, the pipeline's style rules, QA protocol, and publishing patterns are mature. Only genuinely novel conventions surface (the CMS decomposition format for VSTEG001).

**Cross-family references are increasing.** With 20 products already in the bible, VSTEG001 naturally references SRT products that share the Murex four-leg framework and rate-contingent coupon patterns. This validates the bible's internal consistency.

**CMS decomposition convention — deferred.** VSTEG001's cost decomposition sums to 5.0% while the expected coupon is 4.0% (the difference is the net cost of leverage and embedded options). This differs from prior families where decomposition components sum directly to the headline coupon. Deferred for validation against RASTEG001 — if the pattern holds, it becomes an accepted convention.

---

## 2. SRT family completion

SRT is the second family to reach 100% (after ELN). Five products spanning the full complexity range:

| Product | Archetype | Complexity | Batch |
|---------|-----------|-----------|-------|
| IRCFRN001 | Callable fixed rate | Low-Medium | 0 |
| AFRN001 | Accreting notional | Low | 3A |
| NCRA001 | Range accrual (non-callable) | Medium-High | 3A |
| CRASRT001 | Range accrual + callable | High | 3A |
| DCFN001 | Digital rate coupon | Medium-High | 3A |

**SRT memory stress test.** The 3 SRT memory artifacts (created in Batch 0 for IRCFRN001) were reused 12 times in Batch 3A without requiring any updates. This confirms the memory artifacts are durable — they survived 4 additional products of increasing complexity without correction.

**Complexity gradient.** AFRN001 (deterministic, no model risk) to CRASRT001 (dual optionality, joint calibration required) covers the full SRT spectrum. The pipeline handled both extremes without modification.

---

## 3. Cross-family memory reuse

Memory reuse is now a mature pattern. Cumulative statistics:

| Family | Artifacts | Created (batch) | Reuses | Reuse ratio |
|--------|:---------:|:---------------:|:------:|:-----------:|
| ELN | 3 | Batch 0 | 36 | 12.0x |
| SRT | 3 | Batch 0 | 15 | 5.0x |
| CLN | 3 | Batch 0 | 0 | 0.0x |
| Swap | 3 | Batch 0 | 0 | 0.0x |
| STEG | 3 | Pre-Batch 3 | 3 | 1.0x |
| **Total** | **15** | | **54** | **3.6x avg** |

**ELN dominance.** 13 products drove 36 reuses — every ELN product after PHX001 reused all 3 artifacts. This is the highest-leverage memory investment.

**CLN and Swap at 0x.** Each has only 1 product (VCLN001, SWAP001) — the bootstrap product that created the memory. Reuse begins when the second product in a family is generated. CLN reuse starts in Batch 4 (SCLN001, FTD001).

**Cross-family pattern transfer.** STEG memory design borrowed patterns from SRT (murex_four_leg, Termsheet convention) and ELN (style-pattern structure). The memory artifacts are not reused across families, but the design patterns are — reducing bootstrap design time with each new family.

---

## 4. Remaining project risk

### 4.1 Risk matrix

| Risk | Likelihood | Impact | Mitigation |
|------|:----------:|:------:|------------|
| TARN001 path dependency | Medium | Low | First truly path-dependent STEG product. Target redemption logic is well-understood from ELN autocallables. |
| CLN correlation/default modeling | Medium | Medium | FTD001 and NTD001 involve basket credit products. No prior basket products in the bible. May need new CLN conventions. |
| TRANCHE001 complexity | Medium | Medium | Synthetic tranches are the most complex CLN product. Tranche attachment/detachment terminology may need new conventions. |
| Memory artifact staleness | Low | Low | 15 artifacts, all validated within last 2 batches. No drift detected. |
| Pipeline v2.1 stability | Very Low | Low | Zero retries across 21 products. No code changes since Batch 0. |

### 4.2 Batch 4 risk assessment

Batch 4 mixes two families (STEG + CLN) — the first multi-family batch since Batch 0. Specific risks:

**STEG products (RASTEG001, CSTEG001, TARN001):**
- RASTEG001 and CSTEG001 add range accrual and callability to the steepener — patterns already proven in SRT (NCRA001, CRASRT001). Low risk.
- TARN001 introduces target redemption (path-dependent auto-knock). The STEG memory may need a new accepted convention for target-level terminology. Medium risk.

**CLN products (SCLN001, FTD001):**
- SCLN001 (Skew CLN) extends the vanilla CLN with skew pricing. CLN memory exists from VCLN001. Low-Medium risk.
- FTD001 (First-to-Default) introduces basket credit — multiple reference entities, joint default probability, default correlation. No prior basket product in the bible. Medium risk. May need 1-2 new CLN conventions.

### 4.3 Warning tracker

| Warning | Status | Since |
|---------|--------|-------|
| CMS decomposition format (STEG) | Active — deferred for RASTEG001 validation | Batch 3B |
| Desk shorthand 9-word instances | Active — 1 occurrence (VSTEG001) | Batch 3B |
| QA MAJOR declining but non-zero | Monitoring — 8→6→5→4→1 trend is healthy | Batch 0 |

### 4.4 Project completion forecast

| Batch | Products | Families | Cumulative | % |
|------:|----------|----------|:----------:|:-:|
| 0-3 | 21 | ELN, SRT, CLN, Swap, STEG | 21/28 | 75.0% |
| 4 | 5 | STEG + CLN | 26/28 | 92.9% |
| 5 | 2 | CLN | 28/28 | 100.0% |

**Batch 4 reaches 92.9%.** This is the first batch where 90%+ is achievable.

**Batch 5 (2 products) completes the project.** NTD001 and TRANCHE001 are the final CLN products.

---

## Summary

Batch 3 delivered 5 products across 2 phases with zero blocking issues, zero retries, and zero memory corrections. SRT is the second complete family. STEG is successfully bootstrapped with the cleanest bootstrap on record. The pipeline is stable at v2.1 with 21 consecutive clean runs. Remaining risk is concentrated in CLN basket products (FTD001, NTD001) and the TARN001 path-dependent structure — both manageable with existing patterns.
