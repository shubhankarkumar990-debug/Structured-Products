# Product Universe Completeness Review

**Date:** 2026-06-21
**Scope:** Assessment of the 44-product universe against structured products market coverage
**Purpose:** Identify gaps that inform the 44 vs 49 decision

---

## 1. Asset Class Coverage

| Asset Class | Products | Count | Assessment |
|-------------|----------|:-----:|:----------:|
| Equity | PPN, RC, DRC, KODRC, CRC, Airbag, Bonus, Phoenix, FCN, CRA ELN, ICN, Digital, Booster, Digital KI Put, Warrant, ELO, Option on RC, Accumulator, Decumulator | 19 | STRONG |
| Interest Rates | IRS, VLSP, IR Callable, ZCL, NCRA, CRA SRT, Digital CF, Vanilla STEG, RA STEG, Callable STEG, TARN STEG | 11 | STRONG |
| Credit | CLN, Skew CLN, FTD, NTD, Synthetic CDO, CDS | 6 | STRONG |
| Commodity | Commodity Swap | 1 | MINIMAL |
| FX | Cross-Currency Swap | 1 | **GAP** |
| Multi-Asset | — | 0 | **GAP** |
| Inflation | — | 0 | **GAP** |
| Hybrid (cross-asset) | — | 0 | **GAP** |

**Verdict:** Equity, rates, and credit deeply covered. FX structured notes absent (XCCY is a swap, not a note). Multi-asset payoffs absent — worst-of mechanics referenced in §1.6 and Phoenix chapter but no dedicated product. Inflation derivatives absent.

---

## 2. Payoff Type Coverage

| Payoff Type | Products | Present |
|-------------|----------|:-------:|
| Capital protected (principal guarantee) | PPN, Structured Deposit | YES |
| Yield enhancement (short volatility) | RC variants, Phoenix, FCN, Digital, Digital KI Put | YES |
| Participation / leverage | Bonus, Booster, Warrant | YES |
| Linear / symmetric | Forward, IRS, TRS, Equity Swap | YES |
| Digital / binary | Digital Note, Digital CF | YES |
| Path-dependent (autocall observation) | Phoenix, FCN, CRA ELN | YES |
| Range accrual | NCRA, CRA SRT, CRA ELN, RA STEG | YES |
| Spread-dependent | STEG family (4 products) | YES |
| Target redemption | TARN STEG | YES |
| Accumulation / periodic settlement | Accumulator, Decumulator | YES |
| Tranche / portfolio | FTD, NTD, CDO | YES |
| Pure optionality | Vanilla Options, ELO, Option on RC | YES |
| **Worst-of / multi-asset payoff** | — | **GAP** |
| **Cumulative coupon (snowball)** | — | **GAP** |
| **Periodic reset / cliquet** | — | **GAP** |
| **Absolute return (symmetric positive)** | — | **GAP** |
| **FX conversion risk** | — | **GAP** |
| **Barrier-as-modifier (not kill-switch)** | — | **GAP** |

**Verdict:** 12 of 18 payoff types covered. Six distinct mechanics absent. Worst-of is the largest gap given market volumes.

---

## 3. Regional Market Coverage

| Region | Coverage | Key Gaps |
|--------|:--------:|----------|
| Europe (Switzerland, UK, Germany) | STRONG | Cliquet popular in France/Switzerland; otherwise well covered |
| North America | STRONG | Autocallables, CLN, swaps all standard |
| Asia-Pacific (HK, SG, Korea, Japan) | **WEAK** | Worst-of Autocallable (dominant product), Snowball (China #1 product), DCI (standard private banking), Shark Fin (popular in HK/TW) all missing |
| Middle East / Emerging | ADEQUATE | Swap and CLN coverage sufficient; DCI gap relevant |

**Verdict:** European and US desk coverage strong. Asia-Pacific coverage has significant gaps — the three most-traded APAC products (worst-of autocallable, snowball, DCI) are all absent.

---

## 4. Educational Gap Analysis

| Concept | Currently Taught | Gap |
|---------|:----------------:|-----|
| Single-asset payoffs | YES (19 equity products) | — |
| Swap mechanics | YES (8 swap products) | — |
| Credit risk layering | YES (CLN → FTD → NTD → CDO) | — |
| Rate curve exposure | YES (SRT + STEG families) | — |
| Barrier as binary trigger | YES (RC, KODRC, Phoenix) | — |
| Memory coupon | YES (Phoenix) | — |
| Target accumulation | YES (TARN) | — |
| Correlation in trading | YES (§1.6, FTD, NTD) | — |
| **Correlation in structured note payoff** | Discussed in §1.6 but no product demonstrates it | **GAP** |
| **Serial option decomposition** | Not covered | **GAP** |
| **Cumulative vs memory coupon** | Phoenix has memory; no product shows snowball accumulation | **GAP** |
| **FX as primary underlying** | Not covered (XCCY is OTC swap) | **GAP** |
| **Barrier reduces participation (not kills it)** | Not covered | **GAP** |

**Verdict:** Foundation (Parts 0-4) teaches correlation and worst-of conceptually. No product chapter demonstrates these in practice. Reader learns the theory in §1.6 but never sees a real worst-of product. Educational payoff of adding one is high.

---

## 5. Market Volume Assessment

Approximate global structured product issuance by product type (2024-2025):

| Rank | Product Type | In Universe? |
|:----:|-------------|:------------:|
| 1 | Worst-of Autocallable | **NO** |
| 2 | Phoenix / FCN (single-name) | YES |
| 3 | Capital Protected Notes | YES |
| 4 | Dual Currency Investment | **NO** |
| 5 | Accumulator / Decumulator | YES |
| 6 | Snowball Note | **NO** |
| 7 | Reverse Convertible | YES |
| 8 | Cliquet / Ratchet | **NO** |
| 9 | Range Accrual | YES |
| 10 | Shark Fin / Twin-Win | **NO** |

**Verdict:** Of the top 10 product types globally, 5 are missing. The #1 product by volume (worst-of autocallable) is absent.

---

## 6. Summary: Dimensions of Incompleteness

| Dimension | Gap Severity | Products That Would Fill It |
|-----------|:------------:|----------------------------|
| Asset class (multi-asset) | HIGH | Worst-of Autocallable |
| Asset class (FX) | MEDIUM | DCI |
| Payoff type (worst-of) | HIGH | Worst-of Autocallable |
| Payoff type (cumulative coupon) | MEDIUM | Snowball |
| Payoff type (periodic reset) | MEDIUM | Cliquet |
| Payoff type (absolute return) | LOW | Twin-Win |
| Payoff type (barrier-modifier) | LOW | Shark Fin |
| Regional (Asia-Pacific) | HIGH | Worst-of, Snowball, DCI |
| Educational (correlation in payoff) | HIGH | Worst-of Autocallable |
| Educational (serial options) | MEDIUM | Cliquet |
| Market volume coverage | HIGH | Worst-of, DCI, Snowball |

**Overall Assessment:** The 44-product universe has strong depth in equity, rates, and credit, but measurable gaps in multi-asset, FX, and Asia-Pacific coverage. The single largest gap is the absence of worst-of autocallable — the most-traded structured product globally.

---

*Product Universe Completeness Review completed 2026-06-21.*
