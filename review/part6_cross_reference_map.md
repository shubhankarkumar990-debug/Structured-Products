# Part 6 — Cross-Reference Map

**Date**: 2026-06-25
**Scope**: All references between Part 6 and the rest of the Desk Bible ecosystem

---

## 1. Part 6 → Parts 0–5 (Forward References)

### §6.1 Market Conventions
| To | Type | Context |
|----|------|---------|
| Part 1 §1.3 | Concept bridge | European vs American barrier observation → continuous/daily/periodic observation |
| Part 5 §16 (all products) | Application | "Every §16 section in Part 5 specifies booking fields" — conventions underpin booking |
| §6.2 | Forward | Termsheet fields reference §6.1 conventions |
| §6.3 | Forward | ISDA clauses reference §6.1 conventions |

### §6.2 Reading a Termsheet
| To | Type | Context |
|----|------|---------|
| §6.1 | Dependency | All convention fields reference §6.1 definitions |
| Part 2 §2.2 | Concept bridge | Economics fields map to product decomposition framework |
| Part 5 | Application | Product-specific termsheet fields taught in Part 5 chapters |
| §6.3 | Forward | Legal fields explained in §6.3 |

### §6.3 Documentation & Legal
| To | Type | Context |
|----|------|---------|
| §6.1 | Dependency | Business day conventions in ISDA clauses |
| §6.7 | Forward | CSA terms affect XVA (CVA, FVA, ColVA) |
| §6.2 | Backward | Confirmation replicates termsheet terms |

### §6.4 Credit & Capital Structure
| To | Type | Context |
|----|------|---------|
| Part 1 §1.9 | Concept bridge | Credit risk fundamentals → capital structure depth |
| Part 5 §5.5.x | Application | CLN family products reference capital hierarchy |
| Part 5 §5.2.5 | Application | CDS restructuring clause directly impacts CDS products |
| §6.3 | Cross-ref | ISDA Determinations Committee, Governmental Intervention credit event |

### §6.5 Valuation & Fair Value
| To | Type | Context |
|----|------|---------|
| Part 1 §1.1 | Concept bridge | Mark-to-market introduction → full FVH framework |
| §6.6 | Forward | IPV feeds into PC process; reserves cover valuation uncertainty |
| §6.7 | Forward | XVA as valuation adjustments |

### §6.6 Product Control
| To | Type | Context |
|----|------|---------|
| §6.5 | Dependency | IPV process defined in §6.5; §6.6 applies it operationally |
| Part 1 §1.4 | Concept bridge | Greeks defined → used in P&L Explain decomposition |
| Part 2 §2.7 | Concept bridge | Hedging framework → P&L attribution by Greek |
| Part 5 §15 (all products) | Application | Product-specific PC challenges by family |
| §0.12 | Backward | Part 0 introduces PC; §6.6 provides full depth |
| §2.3 | Backward | Four-Leg Framework → P&L flows through all four legs |

### §6.7 Treasury, Capital & XVA
| To | Type | Context |
|----|------|---------|
| Part 2 §2.2 | Concept bridge | "Coupon = Bond Yield + Option Premium - FTP - Margin" deepened |
| Part 2 §2.3 | Concept bridge | Deposit Leg (Leg 3) = FTP cost |
| §6.6 | Cross-ref | Reserves interact with XVA adjustments |
| §6.3 | Cross-ref | CSA terms determine CVA/FVA magnitude |

### §6.8 Model Risk Management
| To | Type | Context |
|----|------|---------|
| Part 1 §1.9 | Concept bridge | "The risk that your math is wrong" → full MRM framework |
| §6.6 | Cross-ref | Model reserve determined by challenger model differences |
| Part 5 §15 (all products) | Application | Model risk varies by family (table in §6.8) |
| Part 2 §2.8 | Application | Sophis/Murex as implementation targets for approved models |

### §6.9 Operations
| To | Type | Context |
|----|------|---------|
| Part 2 §2.6 | Concept bridge | 6-stage lifecycle → 8-stage operational lifecycle |
| Part 2 §2.8 | Dependency | Systems (NEMO/Sophis/Murex) used throughout |
| Part 5 §16 (all products) | Application | Per-product booking fields; §6.9 teaches the workflow |

### §6.10 The Practitioner's Desk
| To | Type | Context |
|----|------|---------|
| Part 1 §1.4 | Concept bridge | Greeks defined → desk positioning language (long/short gamma/vega) |
| Part 2 §2.7 | Concept bridge | Hedging framework → hedge vocabulary (internal, external, B2B) |
| Part 5 §14 (all products) | Application | Product-level interview questions; §6.10 teaches desk vocabulary |

### §6.11 Regulatory Framework
| To | Type | Context |
|----|------|---------|
| §6.3 | Cross-ref | ISDA framework and EMIR clearing/reporting |
| §6.7 | Cross-ref | Basel/FRTB/SA-CCR for capital requirements |
| Part 5 §15 (all products) | Application | Suitability requirements explained → MiFID II regulatory basis |

---

## 2. Parts 0–5 → Part 6 (Reverse References)

| Source | Line | Reference Text | Target |
|--------|:----:|----------------|--------|
| How to Use (Part 0) | 25 | "operational guide in Part 6" | Part 6 generally |
| How to Use (Part 0) | 33 | "Part 2 → 6 → 4 → 7" reading path for PC/Ops | Part 6 generally |

**Only 2 reverse references exist.** Parts 0–5 are frozen. Additional reverse references would require modifying frozen content, which is not authorized.

---

## 3. Part 6 → Ecosystem Artifacts

| Artifact | Status | Part 6 Refs | Artifact Refs Part 6 |
|----------|:------:|:-----------:|:--------------------:|
| Product DNA Atlas | FROZEN 2026-06-22 | 0 | 0 |
| Product Comparison Matrix | FROZEN | 0 | 0 |
| Product Universe Map | FROZEN 2026-06-22 | 0 | 0 |
| Product Evolution Map | FROZEN 2026-06-22 | 0 | 0 |
| Learning Dependency Graph | FROZEN 2026-06-22 | 0 | 0 |
| Solutions Manual | FROZEN 2026-06-22 | 0 | 0 |
| Interview System | APPROVED 2026-06-22 | 0 | 0 |
| Framework Master v1.3.1 | FROZEN | 0 | 0 |

**Note**: All ecosystem artifacts were generated before Part 6 was written. Future editions should:
1. Add Part 6 as a node in the Learning Dependency Graph (prerequisite: Part 2; concurrent: Part 5)
2. Add "Key Infrastructure Topics" to Atlas DNA cards (which §6.x sections are most relevant per product)
3. Add infrastructure-related interview questions to the Interview System based on Part 6 content

---

## 4. Intra-Part 6 References

| From | To | Type |
|------|----|------|
| §6.2 | §6.1 | Dependency — convention fields reference §6.1 |
| §6.3 | §6.1 | Dependency — ISDA clauses reference conventions |
| §6.3 | §6.7 | Forward — CSA terms affect XVA |
| §6.5 | §6.6 | Forward — IPV feeds into PC |
| §6.6 | §6.5 | Backward — references IPV from §6.5 |
| §6.7 | §6.6 | Backward — references reserves from §6.6 |
| §6.7 | §6.3 | Backward — CSA determines collateral/XVA |
| §6.8 | §6.6 | Cross-ref — model reserves |
| §6.9 | §6.1 | Dependency — settlement/calendar conventions |
| §6.10 | §6.6 | Cross-ref — PC vocabulary (flash, official, unexplained) |
| §6.11 | §6.3 | Cross-ref — ISDA framework in EMIR context |
| §6.11 | §6.7 | Cross-ref — capital regulation in Basel context |

**Internal reference network is well-connected with no orphan sections.**

---

**End of cross-reference map.**
