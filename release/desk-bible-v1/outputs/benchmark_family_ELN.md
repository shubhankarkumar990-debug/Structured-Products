# ELN Family-Level Benchmark

## Products tested
PHX001 (Phoenix Autocallable) → FCN001 (Fixed Coupon Note) → CRAELN001 (Callable Range Accrual ELN)

All section 3.2 Autocallables, ELN family, sequential FULL mode build.

---

## 1. Memory cache hit rate

| Product | Lookups | Hits | Misses | Rate |
|---|---|---|---|---|
| PHX001 (cold start) | 19 | 0 | 19 | 0.0% |
| FCN001 | 19 | 8 | 11 | 42.1% |
| CRAELN001 | 19 | 8 | 11 | 42.1% |

Family-level files available after PHX001:
- `ELN_system_mapping.yaml` (260 tokens) — system routing
- `terminology/ELN.yaml` (383 tokens) — naming rules
- `style-patterns/ELN.yaml` (397 tokens) — known false positives

Product-level memory is NOT reusable across products.

## 2. Tokens per stage

| Stage | PHX001 | FCN001 | CRAELN001 | P2 delta |
|---|---|---|---|---|
| Research | 4,866 | 4,526 | 4,526 | -340 |
| Architecture | 6,486 | 6,134 | 6,134 | -352 |
| Content writing | 9,221 | 9,039 | 9,039 | -182 |
| Example generation | 6,119 | 6,119 | 6,119 | 0 |
| Reconciliation | 6,699 | 6,162 | 6,162 | -537 |
| Booking | 7,629 | 7,134 | 7,134 | -495 |
| QA | 3,756 | 3,696 | 3,696 | -60 |
| Style | 6,071 | 5,739 | 5,739 | -332 |
| CrossRef | 3,408 | 3,408 | 3,408 | 0 |
| Publisher | 7,112 | 7,112 | 7,112 | 0 |
| Memory read (1×) | 0 | 1,040 | 1,040 | +1,040 |
| **Total** | **61,367** | **60,109** | **60,109** | **-1,258** |

## 3. Content generation: new vs reused

| Product | New | Reused | Total | Reuse % |
|---|---|---|---|---|
| PHX001 | 7,036 | 0 | 7,036 | 0.0% |
| FCN001 | 6,397 | 639 | 7,036 | 9.1% |
| CRAELN001 | 6,397 | 639 | 7,036 | 9.1% |

## 4. Reasoning savings

| Product | Reasoning | Saved | Save % |
|---|---|---|---|
| PHX001 | 14,600 | 0 | 0.0% |
| FCN001 | 12,941 | 1,659 | 11.4% |
| CRAELN001 | 12,941 | 1,659 | 11.4% |

## 5. Artifact reuse detail — FCN001

| Stage | Output | New | Reused | Reasoning saved | Memory source |
|---|---|---|---|---|---|
| Research | 850 | 765 | 85 | 255 | system_mapping → systems section |
| Architecture | 1,100 | 1,012 | 88 | 264 | system_mapping → booking block |
| Content | 1,458 | 1,458 | 0 | 182 | terminology → naming consistency |
| Example | 622 | 622 | 0 | 0 | — |
| Reconciliation | 715 | 536 | 179 | 358 | system_mapping + ELN_common |
| Booking | 550 | 385 | 165 | 330 | system_mapping → spec foundation |
| QA | 400 | 400 | 0 | 60 | pattern familiarity |
| Style | 350 | 228 | 122 | 210 | ELN.yaml → 8 FPs skipped |
| CrossRef | 250 | 250 | 0 | 0 | — |
| Publisher | 741 | 741 | 0 | 0 | — |

## 6. Draft content reuse by section

| Section | Tokens | Reuse % | Reusable | What transfers |
|---|---|---|---|---|
| Definition | 349 | 0% | 0 | Nothing — product-specific |
| Construction | 302 | 0% | 0 | Nothing — product-specific |
| Booking & systems | 191 | 80% | 153 | NEMO/Sophis/Termsheet mapping |
| Pricing intuition | 445 | 0% | 0 | Nothing — product-specific |
| Worked example | 622 | 0% | 0 | Nothing — product-specific |
| Reconciliation | 524 | 30% | 157 | Obs schedule, fixing fallback |
| Desk view | 352 | 0% | 0 | Nothing — product-specific |
| Desk shorthand | 10 | 0% | 0 | Nothing — product-specific |
| **Total** | **2,795** | **11.1%** | **310** | |

## 7. Summary

| Metric | Value |
|---|---|
| PHX001 (from scratch) | 61,367 tokens |
| FCN001 (with memory) | 60,109 tokens (-2.0%) |
| CRAELN001 (with memory) | 60,109 tokens (-2.0%) |
| Family total (3 ELNs) | 181,585 tokens |
| Without memory (3×P1) | 184,101 tokens |
| Family-level savings | 2,516 tokens (1.4%) |

FCN001 net breakdown:
- Content reused: 639 tokens
- Reasoning saved: 1,659 tokens
- Memory read cost: 1,040 tokens
- **Net: +1,258 tokens saved**

## 8. Maximum achievable savings — 13 ELN products

| Category | Savings |
|---|---|
| Content + reasoning (conservative) | +15,096 tokens (+1.9%) |
| + QA rework avoidance | +13,800 tokens |
| + Style FP avoidance | +28,800 tokens |
| **Total with rework avoidance** | **+57,696 tokens (+7.2%)** |

## Key finding

89% of each product's content is product-specific (definition, construction, pricing, worked example, desk view, desk shorthand). Only 11% is family-reusable (booking systems mapping 80%, reconciliation fields 30%).

The dominant value of memory is **correctness and consistency**, not token savings:
- Prevents wrong system mapping (Murex for ELN = automatic BLOCKER)
- Prevents 8 known false positives from cycling through style review
- Enforces consistent terminology across 13 products
- Reduces QA/style rejection rate

Maximum achievable token savings from family-level generation: **5-7%** with rework avoidance. This is a ceiling.
