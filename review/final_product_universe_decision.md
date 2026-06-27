# Final Product Universe Decision

**Date:** 2026-06-21
**Authority:** Framework Master v1.3.1 (frozen)
**Purpose:** Definitive recommendation on 44 vs 49 products

---

## 1. The Question

Should Desk Bible V2 end at 44 products or expand to 49?

---

## 2. Case for OPTION A — Freeze at 44

**Arguments:**

- All 6 families certified complete. Every family has natural closure.
- 44 products already exceeds most published structured products references.
- V1 had 28 products. V2 at 44 represents 57% expansion — substantial.
- No further generation risk. Manuscript can proceed directly to harmonization.
- Faster path to publication. 5 fewer chapters = ~5 fewer generation sessions + proportionally less harmonization, visual production, and QA.

**Risks of freezing:**

- The #1 globally traded product (worst-of autocallable) is absent. This is a credibility gap.
- FX asset class has zero structured note representation.
- Asia-Pacific desk coverage is measurably weak.
- §1.6 (Correlation and Baskets) teaches worst-of theory with no product chapter payoff — the reader learns the mechanics but never sees them applied.
- The "49" target has been stated throughout project governance. Freezing at 44 requires correcting multiple documents.

---

## 3. Case for OPTION B — Expand to 49

**Arguments:**

- Fills the largest single coverage gap in the universe (worst-of autocallable).
- Adds FX as an asset class (DCI). A structured products desk bible without FX structured notes is noticeably incomplete.
- Introduces 4 genuinely new payoff mechanics not found in the existing 44: worst-of correlation payoff, cumulative snowball coupon, periodic cliquet reset, barrier-as-participation-modifier.
- Closes the Asia-Pacific gap. The three most-traded APAC products (worst-of, snowball, DCI) are all added.
- Completes the educational arc: §1.6 teaches correlation → worst-of autocallable demonstrates it → FTD/NTD/CDO use it differently. Clean three-stage correlation curriculum.
- "49 products" was the stated project objective. Delivering it avoids scope shortfall.

**Risks of expanding:**

- 5 additional generation sessions needed.
- Worst-of Autocallable (C=8) and Cliquet (C=7) are complex products — generation quality risk is real.
- Manuscript grows by ~1,500 lines. Harmonization scope increases proportionally.
- Timeline extends by ~5 sessions before publication can begin.

---

## 4. Recommendation

**OPTION B — Expand to 49 products.**

The gaps identified are not marginal. A structured products desk bible without worst-of autocallable is like an options textbook without Black-Scholes. The educational arc from §1.6 → worst-of product is already built but unfinished. The FX gap is a categorical omission. The Asia-Pacific coverage gap affects the book's claim to comprehensive desk coverage.

The 5 additional chapters represent ~10% more generation work. The quality and credibility gain significantly exceeds this cost.

---

## 5. The Five Products

| # | Product | Family | Section | Complexity | Product Code |
|:-:|---------|--------|---------|:----------:|:------------:|
| 45 | Dual Currency Investment (DCI) | Other | 5.6.8 | 3 | DCI |
| 46 | Shark Fin Note | Other | 5.6.9 | 4 | SHRK |
| 47 | Snowball Note | Other | 5.6.10 | 7 | SNOW |
| 48 | Cliquet / Ratchet Note | Other | 5.6.11 | 7 | CLIQ |
| 49 | Worst-of Autocallable | Other | 5.6.12 | 8 | WOAC |

### Rationale for Family Assignment

All 5 assigned to **Other (5.6)** rather than extending ELN (5.1):

- ELN family (5.1) is conceptually closed at 15 products. Reopening it after certification adds confusion.
- These 5 products draw on concepts from multiple families (worst-of uses correlation from CLN context; cliquet uses forward-starting from options; DCI uses FX). "Other" is the correct home.
- Section 5.6 grows from 7 to 12 products. This is large but manageable — the products are diverse enough that subsections can organize them (5.6.1-7 = current, 5.6.8-12 = Batch 10).

---

## 6. Complexity Scores

| # | Product | Score | Rationale |
|:-:|---------|:-----:|-----------|
| 45 | DCI | 3 | Deposit + single FX option. One strike, one observation. Simple two-currency mechanics. |
| 46 | Shark Fin | 4 | Capital protected + single up-and-out barrier. One barrier, one rebate level. Straightforward variant of PPN. |
| 47 | Snowball | 7 | Autocall + conditional coupon + cumulative accumulation. Path-dependent — coupon amount depends on entire history of missed coupons. Multiple observation dates. |
| 48 | Cliquet | 7 | Serial forward-starting options. Multiple reset periods. Local + global caps/floors. Path-dependent — total return depends on sequence of periodic returns. |
| 49 | Worst-of Autocallable | 8 | Phoenix mechanics applied to multi-asset basket. Correlation-dependent pricing. Worst-of observation across 3-5 stocks. Quanto adjustment for cross-listed baskets. All Phoenix complexity plus correlation dimension. |

**Batch complexity profile:** 3, 4, 7, 7, 8 — ascending, consistent with Batches 1-9 pattern.

---

## 7. Recommended Generation Order

| Order | # | Product | Complexity | Rationale |
|:-----:|:-:|---------|:----------:|-----------|
| 1st | 45 | DCI | 3 | Simplest. No dependency on other Batch 10 products. Establishes FX underlying. |
| 2nd | 46 | Shark Fin | 4 | Simple. Depends only on PPN (pilot) and barriers (§1.3). Independent of other Batch 10 products. |
| 3rd | 47 | Snowball | 7 | Complex but self-contained. Depends on Phoenix/FCN (existing). Can reference DCI if needed for cross-product comparison. |
| 4th | 48 | Cliquet | 7 | Complex. Depends on Vanilla Options (existing). Introduces forward-starting concept needed nowhere else in batch. |
| 5th | 49 | Worst-of Autocallable | 8 | Most complex. Depends on Phoenix (existing) + Correlation (§1.6). Natural capstone — the final product in the universe is the most-traded structured product globally. |

### Dependency Map

```
PPN (5.1.1) ──→ Shark Fin (#46)
                     ↓
Structured Deposit (5.6.1) + Vanilla Options (5.6.3) ──→ DCI (#45)

Phoenix (5.1.3) + FCN (5.1.9) ──→ Snowball (#47)

Vanilla Options (5.6.3) ──→ Cliquet (#48)

Phoenix (5.1.3) + §1.6 Correlation ──→ Worst-of Autocallable (#49)
```

No intra-batch dependencies. All 5 depend only on products already in the manuscript. Generation order is purely complexity-driven.

---

## 8. Analogy Domain Availability

| # | Product | Proposed Domain | Collision Check |
|:-:|---------|----------------|:---------------:|
| 45 | DCI | Airport currency exchange booth | CLEAR — no FX analogies used |
| 46 | Shark Fin | Fishing trip with catch limit | CLEAR — no fishing analogies |
| 47 | Snowball | Rolling snowball downhill | CLEAR — physics/nature domain |
| 48 | Cliquet | Monthly salary with performance cap | CLEAR — employment domain different from Phoenix's contract |
| 49 | Worst-of Autocallable | Relay race (slowest runner determines team time) | CLEAR — sports domain used but not relay/team |

All 5 domains verified against 44 used + 25 reserved. No collisions.

---

## 9. Updated Universe Summary (at 49/49)

| Family | Products | Count |
|--------|----------|:-----:|
| 5.1 ELN | PPN through Warrant | 15 |
| 5.2 Swaps | IRS through VLSP | 8 |
| 5.3 SRT | IR Callable through Digital CF | 5 |
| 5.4 STEG | Vanilla through TARN | 4 |
| 5.5 CLN | Vanilla CLN through Synthetic CDO | 5 |
| 5.6 Other | SD through Worst-of Autocallable | 12 |
| **Total** | | **49** |

### Asset Classes at 49/49

| Asset Class | Count |
|-------------|:-----:|
| Equity | 19 + WOAC = 20 |
| Interest Rates | 11 |
| Credit | 6 |
| FX | 1 (XCCY) + DCI = 2 |
| Multi-Asset | WOAC = 1 |
| Commodity | 1 |

### Complexity Distribution at 49/49

| Score | Count | Products |
|:-----:|:-----:|----------|
| 2 | 4 | PPN, VLSP, SD, Forward |
| 3 | 6 | RC, DRC, ICN, Warrant, Vanilla Option, ELO, **DCI** |
| 4 | 6 | CLN, KODRC, Airbag, Bonus, Digital, Booster, Commodity, ZCL, **Shark Fin** |
| 5 | 8 | CRC, TRS, Equity Swap, CDS, XCCY, Skew CLN, IR Callable, DCF, Option on RC, Vanilla STEG |
| 6 | 5 | Phoenix, FCN, CRA ELN, NCRA, Callable STEG, Accumulator, Decumulator |
| 7 | 6 | Digital KI Put, Variance Swap, CRA SRT, RA STEG, FTD, **Snowball, Cliquet** |
| 8 | 3 | TARN STEG, NTD, **Worst-of Autocallable** |
| 9 | 0 | — |
| 10 | 1 | Synthetic CDO Tranche |

---

## 10. Decision

**Desk Bible V2 should be a 49-product universe.**

The 5 products are: DCI, Shark Fin, Snowball, Cliquet, Worst-of Autocallable.

Generation order: DCI → Shark Fin → Snowball → Cliquet → Worst-of Autocallable.

---

*Final Product Universe Decision issued 2026-06-21.*
