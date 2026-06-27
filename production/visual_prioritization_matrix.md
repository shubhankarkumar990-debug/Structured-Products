# Visual Prioritization Matrix

**Version:** 1.0
**Date:** 2026-06-21
**Authority:** Framework Master v1.3.1 (FROZEN) + Visual Asset Governance v1.0
**Scope:** All 93 registered visual assets (Batches 5-8) + estimated Batch 0-4 and Batch 9 assets
**Purpose:** Classify all visuals by tier and identify top 25 for publication priority

---

## 1. Current Asset Inventory

### 1.1 Registered Assets (93)

| Family | Batch | Chapters | Assets | P1 | P2 | P3 |
|--------|:-----:|:--------:|:------:|:--:|:--:|:--:|
| Swaps (remaining) | 5 | 3 (5.2.6-5.2.8) | 15 | 5 | 5 | 5 |
| SRT | 6 | 5 (5.3.1-5.3.5) | 30 | 10 | 10 | 10 |
| STEG | 7 | 4 (5.4.1-5.4.4) | 24 | 8 | 8 | 8 |
| CLN (remaining) | 8 | 4 (5.5.2-5.5.5) | 24 | 8 | 8 | 8 |
| **Total registered** | | **16** | **93** | **31** | **31** | **31** |

### 1.2 Unregistered Assets (estimated)

| Family | Batch | Chapters | Est. Assets | Status |
|--------|:-----:|:--------:|:-----------:|--------|
| ELN (Batch 0 pilots) | 0 | 3 (PPN, RC, Phoenix) | ~15 | v1.0 Learning Recommendations — need spec upgrade |
| Swaps (Batch 0 pilot) | 0 | 1 (IRS) | ~5 | v1.0 — need spec upgrade |
| CLN (Batch 0 pilot) | 0 | 1 (CLN) | ~5 | v1.0 — need spec upgrade |
| ELN (Batch 1) | 1 | 5 (DRC-Bonus) | ~30 | v1.0 — need spec upgrade |
| ELN (Batch 2) | 2 | 5 (FCN-Booster) | ~30 | v1.0 — need spec upgrade |
| ELN (Batch 3) | 3 | 2 (Digital KI, Warrant) | ~12 | v1.0 — need spec upgrade |
| Swaps (Batch 4) | 4 | 4 (TRS-CDS) | ~24 | v1.1 — need spec upgrade |
| **Total unregistered** | | **21** | **~121** | All pending harmonization |

### 1.3 Future Assets (Batch 9)

| Family | Batch | Chapters | Est. Assets |
|--------|:-----:|:--------:|:-----------:|
| Other | 9 | 7 (Struct Deposit-Vanilla Options) | ~42 |

### 1.4 Grand Total

| Category | Count |
|----------|:-----:|
| Registered (Batches 5-8) | 93 |
| Unregistered (Batches 0-4) | ~121 |
| Future (Batch 9) | ~42 |
| Front matter | ~10 |
| **Total** | **~266** |

---

## 2. Tier Classification

### 2.1 Registered Assets by Tier

**Tier 1 (P1 assets — core teaching visuals):** 31

| Visual ID | Product | Type | Teaching Value |
|-----------|---------|------|:-------------:|
| VIS-CCYSWP-01 | Cross-Currency Swap | Cash Flow | Critical — 3-phase structure |
| VIS-CCYSWP-02 | Cross-Currency Swap | Comparison | Critical — basis visualization |
| VIS-CMDSWP-01 | Commodity Swap | Cash Flow | Critical — physical vs financial |
| VIS-CMDSWP-02 | Commodity Swap | Timeline | Critical — futures roll |
| VIS-VLSP-01 | VLSP | Cash Flow | Critical — standard swap anatomy |
| VIS-IRC-01 | IR Callable | Cash Flow | Critical — 4-leg structure |
| VIS-IRC-02 | IR Callable | Lifecycle | Critical — call decision points |
| VIS-ZCL-01 | ZCL | Payoff | Critical — accretion curve |
| VIS-ZCL-02 | ZCL | Timeline | Critical — zero-coupon lifecycle |
| VIS-NCRA-01 | NCRA | Cash Flow | Critical — range gate mechanism |
| VIS-NCRA-02 | NCRA | Decision Tree | Critical — daily observation |
| VIS-CRA-01 | CRA SRT | Cash Flow | Critical — dual gate |
| VIS-CRA-02 | CRA SRT | Lifecycle | Critical — callable + range |
| VIS-DCF-01 | Digital CF | Payoff | Critical — step function |
| VIS-DCF-02 | Digital CF | Comparison | Critical — cap vs digital |
| VIS-VSTEG-01 | Vanilla STEG | Payoff | Critical — CMS spread |
| VIS-VSTEG-02 | Vanilla STEG | Yield Curve | Critical — curve regimes |
| VIS-RASTEG-01 | RA STEG | Cash Flow | Critical — spread range gate |
| VIS-RASTEG-02 | RA STEG | Lifecycle | Critical — daily spread obs |
| VIS-CSTEG-01 | Callable STEG | Cash Flow | Critical — callable + CMS |
| VIS-CSTEG-02 | Callable STEG | Lifecycle | Critical — NC + call |
| VIS-TARNSTEG-01 | TARN STEG | Timeline | Critical — target accumulation |
| VIS-TARNSTEG-02 | TARN STEG | Payoff | Critical — multiple paths |
| VIS-SKCLN-01 | Skew CLN | Payoff | Critical — recovery comparison |
| VIS-SKCLN-02 | Skew CLN | Cash Flow | Critical — modified recovery |
| VIS-FTD-01 | FTD | Portfolio Loss | Critical — basket trigger |
| VIS-FTD-02 | FTD | Correlation | Critical — credit correlation |
| VIS-NTD-01 | NTD | Portfolio Loss | Critical — Nth trigger |
| VIS-NTD-02 | NTD | Correlation | Critical — reversal curve |
| VIS-SCDO-01 | Synthetic CDO | Waterfall | Critical — tranche loss |
| VIS-SCDO-02 | Synthetic CDO | Tranche | Critical — attachment/detachment |

**Tier 2 (P2 assets — supporting visuals):** 31

**Tier 3 (P3 assets — reference visuals):** 31

---

## 3. Top 25 Visuals for Publication

Ranked by teaching impact × product importance × visual novelty.

| Rank | Visual ID | Product | Type | Why Top 25 |
|:----:|-----------|---------|------|-----------|
| 1 | VIS-SCDO-01 | Synthetic CDO | Tranche Waterfall | Teaches tranching — most complex concept in book. No substitute for visual |
| 2 | VIS-SCDO-02 | Synthetic CDO | Tranche Bands | Attachment/detachment — must be seen to be understood |
| 3 | VIS-NTD-02 | NTD | Correlation Reversal | Highest-priority educational risk. Non-monotonic curve is unintuitive without visual |
| 4 | VIS-FTD-02 | FTD | Credit Correlation | Bridges equity → credit correlation. Key conceptual bridge |
| 5 | VIS-FTD-01 | FTD | Basket Default | First visual showing basket mechanics — new paradigm for reader |
| 6 | VIS-SCDO-03 | Synthetic CDO | Loss Distribution | Portfolio loss probability with tranche overlay — statistical literacy |
| 7 | VIS-TARNSTEG-01 | TARN STEG | Target Accumulation | Path-dependency visualization — unique to TARN family |
| 8 | VIS-VSTEG-01 | Vanilla STEG | CMS Spread Payoff | Introduces CMS spread — new payoff type vs equity/rate |
| 9 | VIS-VSTEG-02 | Vanilla STEG | Yield Curve Regimes | 3 curve shapes → 3 outcomes. Foundational for all STEG |
| 10 | VIS-IRC-01 | IR Callable | 4-Leg Structure | First four-leg structure in book. Architectural reference |
| 11 | VIS-NCRA-01 | NCRA | Range Gate Flow | Range accrual is counter-intuitive. Visual makes it click |
| 12 | VIS-SKCLN-01 | Skew CLN | Recovery Comparison | 3 recovery scenarios in one payoff — immediate clarity |
| 13 | VIS-NTD-01 | NTD | Nth Trigger | Visual default counter with absorbed vs trigger zones |
| 14 | VIS-CCYSWP-01 | Cross-Currency Swap | 3-Phase Flow | Most complex swap structure. 3 temporal phases |
| 15 | VIS-SCDO-04 | Synthetic CDO | Correlation Sensitivity | Opposite tranche sensitivities — key insight, hard to verbalize |
| 16 | VIS-RASTEG-01 | RA STEG | Spread Range Gate | Spread-based range accrual — double the complexity of rate range |
| 17 | VIS-CRA-01 | CRA SRT | Dual Gate | Callable + range — two conditions in one visual |
| 18 | VIS-DCF-01 | Digital CF | Step Function | Digital payoff in rate space — different from equity digital |
| 19 | VIS-TARNSTEG-02 | TARN STEG | Multiple Paths | Shows how different spreads lead to different target dates |
| 20 | VIS-ZCL-01 | ZCL | Accretion Curve | Zero-coupon growth curve — simple but essential |
| 21 | VIS-SCDO-05 | Synthetic CDO | Structure Flow | 100+ CDS → SPV → tranches. Architecture diagram |
| 22 | VIS-CMDSWP-01 | Commodity Swap | Physical vs Financial | Physical settlement vs financial settlement — key distinction |
| 23 | VIS-SKCLN-02 | Skew CLN | Modified Recovery Flow | 3-party structure with skewed recovery path highlighted |
| 24 | VIS-FTD-06 | FTD | Default Sequence | Timeline with "First = Only" annotation |
| 25 | VIS-CSTEG-01 | Callable STEG | Callable + CMS | Combines call optionality with spread mechanics |

### 3.1 Top 25 Distribution

| Family | Count in Top 25 |
|--------|:---------------:|
| CLN | 10 (40%) |
| STEG | 7 (28%) |
| SRT | 5 (20%) |
| Swaps | 3 (12%) |

CLN dominance reflects complexity — tranching, correlation, baskets require visual teaching more than simpler products.

### 3.2 Top 25 Type Distribution

| Visual Type | Count |
|------------|:-----:|
| Cash Flow / Structure | 7 |
| Payoff / Comparison | 6 |
| Correlation / Distribution | 4 |
| Waterfall / Tranche | 3 |
| Timeline / Lifecycle | 3 |
| Decision / Range | 2 |

---

## 4. Batch 9 Visual Projections

| Product | Est. New Templates | Est. Reuse | Tier 1 Candidates |
|---------|:------------------:|:----------:|:-----------------:|
| Structured Deposit | 0 | 6 (PPN-like) | Payoff (deposit insurance + cap) |
| Accumulator | 1 (daily accumulation) | 5 | Daily accumulation timeline, barrier KO |
| Decumulator | 0 | 6 (mirror accumulator) | Daily sale timeline |
| Option on RC | 0 | 6 (option payoff) | Payoff on managed fund |
| ELO | 0 | 6 (standard option) | Equity-linked payoff |
| Forward | 0 | 6 (linear payoff) | Symmetric linear payoff |
| Vanilla Options | 0 | 6 (standard option) | Call/put payoff |

**Batch 9 new templates needed:** 1 (daily accumulation/decumulation timeline)

---

## 5. Post-49/49 Visual Production Order

| Phase | Scope | Assets | Priority |
|:-----:|-------|:------:|:--------:|
| 1 | Top 25 publication visuals | 25 | HIGHEST |
| 2 | Remaining Tier 1 (P1) across all 49 chapters | ~73 | HIGH |
| 3 | Tier 2 (P2) across all 49 chapters | ~98 | MEDIUM |
| 4 | Tier 3 (P3) across all 49 chapters | ~98 | LOW |
| 5 | Front matter visuals | ~10 | MEDIUM |

---

*Visual Prioritization Matrix v1.0. Effective 2026-06-21. Production order begins after 49/49.*
