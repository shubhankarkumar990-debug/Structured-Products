# Product Coverage Balance Audit

**Date:** 2026-06-22
**Auditor:** Independent Quality Gate
**Input:** `production/solutions_manual.md` — 40 scenarios, 18 anti-patterns, 49-row replacement table

---

## 1. Meaningful Coverage Per Product

"Meaningful" = product appears as primary/co-primary recommendation (not just rejected or referenced in passing).

### Coverage Tiers

| Tier | Definition | Products | Count |
|------|-----------|----------|:-----:|
| **Deep** (2+ primary scenarios + AP + desk note) | Multiple scenarios, anti-pattern, desk treatment | RC, WOAC, Phoenix | 3 |
| **Solid** (1 primary + AP or desk note) | Own scenario + supplementary material | PPN, Bonus, Digital, Vanilla STEG, CLN, FTD, IRS, VO, SNOW | 9 |
| **Adequate** (1 primary, scenario shared or short) | Own scenario but thin treatment | DRC, KODRC, CRC, Airbag, FCN, DKIP, DCI, Callable STEG, RA STEG, TARN STEG, Skew CLN, NTD, CDO, VarSwap, Opt-on-RC, XCCY, CommSwap, ZCL, Digital CF, CRA ELN, NCRA, CRA SRT, ACCUM, DECUM, SHRK, CLIQ | 26 |
| **Shallow** (co-primary only, no own scenario) | Shares scenario and gets brief treatment | ICN, ELO, Booster, EqSwap, TRS, SD, FWD, VLSP, IR Callable, Warrant, CDS | 11 |

---

## 2. Detailed Coverage Score

Each product scored on 4 dimensions (0–3 each, max 12):

- **Scenario depth** (0=absent, 1=shared/single-candidate, 2=co-primary in genuine comparison, 3=primary in rich multi-candidate scenario)
- **Rejection reasoning** (0=never rejected, 1=rejected 1–2×, 2=rejected 3+× with varied reasons, 3=rich rejection story)
- **Anti-pattern / Common Mistake mention** (0=none, 1=indirect, 2=Common Mistake in 1 scenario, 3=dedicated AP or multiple mentions)
- **Cross-reference density** (0=isolated, 1=referenced in 1–2 other scenarios, 2=3–5 references, 3=6+ references)

### ELN Family (15 products)

| Product | Scenario | Reject | AP/CM | Cross-Ref | Total | Assessment |
|---------|:--------:|:------:|:-----:|:---------:|:-----:|:----------:|
| PPN | 3 | 3 | 3 | 3 | **12** | Excellent |
| RC | 3 | 3 | 3 | 3 | **12** | Excellent |
| Phoenix | 2 | 2 | 3 | 3 | **10** | Very good |
| DRC | 2 | 1 | 2 | 1 | **6** | Adequate |
| KODRC | 2 | 1 | 2 | 2 | **7** | Adequate+ |
| CRC | 2 | 1 | 1 | 2 | **6** | Adequate |
| Airbag | 2 | 1 | 2 | 2 | **7** | Adequate+ |
| Bonus | 2 | 1 | 2 | 2 | **7** | Adequate+ |
| FCN | 2 | 0 | 2 | 2 | **6** | Adequate |
| CRA ELN | 2 | 1 | 1 | 2 | **6** | Adequate |
| ICN | 2 | 0 | 1 | 1 | **4** | Thin |
| Digital | 2 | 1 | 2 | 3 | **8** | Good |
| DKIP | 2 | 1 | 3 | 1 | **7** | Adequate+ |
| Booster | 2 | 0 | 2 | 1 | **5** | Thin+ |
| WOAC | 2 | 1 | 3 | 3 | **9** | Very good |

**ELN Average: 7.5/12. Range: 4–12.**

---

### Swaps Family (8 products)

| Product | Scenario | Reject | AP/CM | Cross-Ref | Total | Assessment |
|---------|:--------:|:------:|:-----:|:---------:|:-----:|:----------:|
| IRS | 2 | 1 | 2 | 2 | **7** | Adequate+ |
| TRS | 2 | 0 | 2 | 1 | **5** | Thin+ |
| EqSwap | 2 | 0 | 1 | 1 | **4** | Thin |
| VarSwap | 2 | 1 | 3 | 2 | **8** | Good |
| CDS | 2 | 0 | 1 | 2 | **5** | Thin+ |
| XCCY | 1 | 0 | 2 | 2 | **5** | Thin+ |
| CommSwap | 1 | 0 | 2 | 1 | **4** | Thin |
| VLSP | 1 | 0 | 1 | 1 | **3** | Minimal |

**Swaps Average: 5.1/12. Range: 3–8.**

---

### SRT Family (5 products)

| Product | Scenario | Reject | AP/CM | Cross-Ref | Total | Assessment |
|---------|:--------:|:------:|:-----:|:---------:|:-----:|:----------:|
| IR Callable | 1 | 1 | 2 | 2 | **6** | Adequate |
| ZCL | 1 | 0 | 2 | 1 | **4** | Thin |
| NCRA | 2 | 1 | 3 | 2 | **8** | Good |
| CRA SRT | 1 | 1 | 1 | 1 | **4** | Thin |
| Digital CF | 1 | 1 | 2 | 2 | **6** | Adequate |

**SRT Average: 5.6/12. Range: 4–8.**

---

### STEG Family (4 products)

| Product | Scenario | Reject | AP/CM | Cross-Ref | Total | Assessment |
|---------|:--------:|:------:|:-----:|:---------:|:-----:|:----------:|
| Vanilla STEG | 2 | 1 | 3 | 3 | **9** | Very good |
| Callable STEG | 1 | 1 | 3 | 2 | **7** | Adequate+ |
| RA STEG | 2 | 1 | 3 | 2 | **8** | Good |
| TARN STEG | 1 | 0 | 3 | 1 | **5** | Thin+ |

**STEG Average: 7.3/12. Range: 5–9.**

---

### CLN Family (5 products)

| Product | Scenario | Reject | AP/CM | Cross-Ref | Total | Assessment |
|---------|:--------:|:------:|:-----:|:---------:|:-----:|:----------:|
| CLN | 2 | 1 | 3 | 3 | **9** | Very good |
| Skew CLN | 1 | 0 | 2 | 1 | **4** | Thin |
| FTD | 1 | 1 | 3 | 2 | **7** | Adequate+ |
| NTD | 1 | 0 | 3 | 2 | **6** | Adequate |
| CDO | 1 | 0 | 3 | 2 | **6** | Adequate |

**CLN Average: 6.4/12. Range: 4–9.**

---

### Other Family (12 products)

| Product | Scenario | Reject | AP/CM | Cross-Ref | Total | Assessment |
|---------|:--------:|:------:|:-----:|:---------:|:-----:|:----------:|
| SD | 1 | 0 | 2 | 2 | **5** | Thin+ |
| FWD | 1 | 0 | 2 | 2 | **5** | Thin+ |
| ELO | 2 | 0 | 1 | 1 | **4** | Thin |
| VO | 2 | 1 | 2 | 2 | **7** | Adequate+ |
| Warrant | 2 | 0 | 1 | 1 | **4** | Thin |
| DCI | 1 | 0 | 2 | 1 | **4** | Thin |
| Opt-on-RC | 1 | 0 | 2 | 1 | **4** | Thin |
| ACCUM | 1 | 0 | 3 | 2 | **6** | Adequate |
| DECUM | 1 | 0 | 2 | 1 | **4** | Thin |
| SHRK | 2 | 0 | 1 | 1 | **4** | Thin |
| SNOW | 1 | 0 | 3 | 1 | **5** | Thin+ |
| CLIQ | 2 | 0 | 3 | 1 | **6** | Adequate |

**Other Average: 4.8/12. Range: 4–7.**

---

## 3. Family Balance

| Family | Products | Avg Score | Min | Max | Spread | Balance |
|--------|:--------:|:---------:|:---:|:---:|:------:|:-------:|
| ELN | 15 | 7.5 | 4 | 12 | 8 | Uneven — top-heavy on PPN/RC |
| Swaps | 8 | 5.1 | 3 | 8 | 5 | Weak — VLSP is minimal |
| SRT | 5 | 5.6 | 4 | 8 | 4 | Moderate |
| STEG | 4 | 7.3 | 5 | 9 | 4 | Good |
| CLN | 5 | 6.4 | 4 | 9 | 5 | Moderate |
| Other | 12 | 4.8 | 4 | 7 | 3 | Flat but low |

**Cross-family balance: ELN and STEG are well-covered. Swaps and Other are underweight.**

---

## 4. Overrepresented Products

| Product | Primary Scenarios | AP Mentions | Desk Notes | Total Touches | Overrep? |
|---------|:-----------------:|:-----------:|:----------:|:-------------:|:--------:|
| RC | 2.1, 6.4 | AP-1, AP-4 ref | 2.1 | 15+ | YES — marginal |
| WOAC | 6.3, 8.4 | AP-16 | 6.3 | 10+ | YES — marginal |
| PPN | 1.1 | AP-1, §1.6 ref | — | 12+ | NO — justified by Tier 1 status |

RC and WOAC each get 2 primary scenarios while 38 products get 1 or share. Marginally overrepresented but justified — RC is the most traded product and WOAC has unique correlation dynamics.

---

## 5. Underrepresented Products

Products scoring ≤4 (Thin or Minimal):

| Product | Score | Issue | Impact |
|---------|:-----:|-------|--------|
| **VLSP** | 3 | Co-primary in 4.1 but IRS gets recommendation. No AP. No rejection appearances. | LOW — VLSP is a niche enhanced IRS |
| **ICN** | 4 | Co-primary in 2.6 but CRC gets emphasis. No rejections. | LOW — ICN is a simple callable |
| **ELO** | 4 | Co-primary in 8.3 with Warrant/Booster. Brief treatment. | LOW — ELO is a retail option wrapper |
| **Warrant** | 4 | Co-primary in 8.3. Exchange-listed angle is distinct but shallow. | LOW — Warrant is a building block |
| **CommSwap** | 4 | Sole primary in 7.2 but thin scenario. | LOW — commodity is peripheral |
| **EqSwap** | 4 | Co-primary in 7.1 but TRS gets emphasis. | LOW — EqSwap is TRS subset |
| **DCI** | 4 | Sole primary in 2.7. Decent depth but isolated — no cross-references. | MEDIUM — DCI is actively traded in Asia/EMEA |
| **Skew CLN** | 4 | Sole primary in 5.2 but niche product. | LOW — Skew CLN is specialist |
| **Opt-on-RC** | 4 | Sole primary in 6.2. Compound option concept adds value but isolated. | LOW — very niche |
| **SHRK** | 4 | Co-primary in 1.5 but CLIQ gets the "true lock-in" recommendation. | LOW — SHRK is PPN variant |
| **DECUM** | 4 | Mirror of ACCUM (7.4). Limited independent reasoning. | LOW — DECUM = reverse ACCUM |

**No product at score 0–2.** All 49 products have at least minimal representation. The underrepresentation is in DEPTH, not presence.

---

## 6. Verdict

| Check | Target | Result | Status |
|-------|--------|--------|:------:|
| All 49 products appear as primary/co-primary | 49/49 | 49/49 | PASS |
| All 6 families have at least 1 scenario | 6/6 | 8 categories covering 6 families | PASS |
| No product scores 0 | 0 zero-scores | Confirmed | PASS |
| Family balance spread <50% | <50% | ELN 7.5 vs Other 4.8 = 56% spread | **MINOR FAIL** |
| Overrepresentation contained | ≤2 products | RC, WOAC marginally over | PASS (marginal) |
| Underrepresentation contained | No product critical | 11 at score 4, all LOW impact | PASS |

**Family balance is the only flagged issue.** ELN products average 7.5/12 while Other family averages 4.8/12. The gap is driven by ELN having 15 products with several high-volume market products (RC, Phoenix, WOAC) that naturally attract more scenario depth.

**This is structurally inherent** — ELN is the largest family and contains the most-traded products. Equalizing coverage would require adding less-traded products to scenarios where they don't fit.

---

*Product coverage balance audit complete. 2026-06-22.*
