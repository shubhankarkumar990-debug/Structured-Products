# Universe Map Generation Readiness

**Date:** 2026-06-22
**Phase:** Reference Layer Readiness Review — Phase 3
**Scope:** Structured Products Universe Map dependency verification

---

## Check 1: Family Assignments

49 / 49 chapters have correct family classification.

| Family | Section Range | Count | Anchor |
|--------|--------------|:-----:|--------|
| Equity-Linked Notes | 5.1.1–5.1.15 | 15 | PPN (5.1.1) |
| Swaps | 5.2.1–5.2.8 | 8 | IRS (5.2.1) |
| Structured Rate Trades | 5.3.1–5.3.5 | 5 | IR Callable (5.3.1) |
| Steepener Notes | 5.4.1–5.4.4 | 4 | Vanilla STEG (5.4.1) |
| Credit-Linked Notes | 5.5.1–5.5.5 | 5 | Vanilla CLN (5.5.1) |
| Other | 5.6.1–5.6.12 | 12 | Structured Deposit (5.6.1) |
| **Total** | | **49** | 6 anchors |

All family values in manuscript DNA tables match expected distribution. No misclassifications remain.

**Result: PASS**

## Check 2: Complexity Assignments

49 / 49 complexity scores match canonical registry. Distribution by family:

| Family | Min | Max | Mean | Products |
|--------|:---:|:---:|:----:|:--------:|
| ELN | 2 | 7 | 4.3 | 15 |
| Swaps | 2 | 7 | 4.5 | 8 |
| SRT | 4 | 7 | 5.4 | 5 |
| STEG | 5 | 8 | 6.5 | 4 |
| CLN | 4 | 10 | 6.8 | 5 |
| Other | 2 | 8 | 4.8 | 12 |

Complexity gradient within families is consistent: anchor products are simplest, variants add complexity.

**Result: PASS**

## Check 3: Dependency Hierarchy

### §22 Related Chapters

49 / 49 chapters contain §22 Related Chapters / Dependency References.

Cross-reference graph structure:
- All 45 section references in Similar Products resolve to real chapters
- 6 family anchors serve as root nodes (simplest in each family)
- All non-anchor products reference at least one other chapter

### Family Dependency Chains

| Family | Chain |
|--------|-------|
| ELN | PPN → RC → DRC/KODRC/Phoenix → CRC/Airbag/Bonus → FCN/CRA/ICN/Digital/Booster/DKIP → Warrant |
| Swaps | IRS → TRS/Equity Swap/CDS/XCS → Variance Swap/Commodity Swap → VLSP |
| SRT | IR Callable → ZCL → NCRA → CRA SRT → Digital CF |
| STEG | Vanilla STEG → RA STEG → Callable STEG → TARN STEG |
| CLN | Vanilla CLN → Skew CLN → FTD → NTD → Synthetic CDO |
| Other | Structured Deposit → Forward → Options → ELO → Accumulator/Decumulator/DCI → Shark Fin/Snowball/Cliquet → Worst-of Autocallable |

All chains are linear or tree-shaped. No circular dependencies.

**Result: PASS**

## Check 4: Evolution Chains

49 / 49 chapters contain §6 Product Evolution.

Evolution sections describe how each product developed historically and relate to adjacent products. This content is consumed by the Universe Map to render evolution arrows.

**Result: PASS**

## Check 5: Product Positioning

Universe Map positioning requires two axes. Standard layout:
- **X-axis:** Complexity score (1–10)
- **Y-axis:** Family grouping (6 families)

Positioning data available:

| Data Point | Source | Coverage |
|-----------|--------|:--------:|
| Complexity score | Registry + DNA table | 49 / 49 |
| Family | DNA table | 49 / 49 |
| Underlying asset class | DNA table | 49 / 49 |
| Client type | CM fields + Taxonomy | 49 / 49 |
| Similar products (edges) | Atlas fields | 49 / 49 |
| Evolution chain (arrows) | §6 | 49 / 49 |

All positioning dimensions populated. No missing data.

**Result: PASS**

---

## Summary

| Check | Result |
|-------|:------:|
| Family assignments (6 families, 49 chapters) | **PASS** |
| Complexity assignments (49/49 match registry) | **PASS** |
| Dependency hierarchy (no broken refs, no cycles) | **PASS** |
| Evolution chains (49/49 §6 present) | **PASS** |
| Product positioning (all axes populated) | **PASS** |

**Universe Map generation: READY**

---

*Phase 3 complete.*
