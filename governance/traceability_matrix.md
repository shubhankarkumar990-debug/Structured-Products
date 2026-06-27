# TRACEABILITY MATRIX

**Ecosystem:** Structured Products Knowledge Ecosystem  
**Version:** V1.0.1-GOV-1.0  
**Effective:** 2026-06-27  
**Purpose:** Map every governed concept to canonical definition, source, appearances, status, and linked governance controls.

---

## Matrix Format

| Column | Description |
|--------|-------------|
| **Concept ID** | Unique identifier (CONC-XXX) |
| **Concept** | Name |
| **Canonical Definition** | One-line canonical meaning |
| **Canonical Source** | Primary document and section |
| **Appearances** | All artifacts where concept appears |
| **Status** | Canonical / Errata-corrected / Review-only / Accept-as-is / Deprecated |
| **Qualifier** | Required qualifier when ambiguous |
| **Related Concepts** | Linked concepts |
| **Regression Tests** | Linked test IDs |
| **Linter Rules** | Linked linter rule IDs |
| **Convention** | Linked convention registry ID |
| **Verified** | Last verification date |

---

## CORRELATION AND DIRECTION CONCEPTS

### CONC-001: Long Correlation

| Field | Value |
|-------|-------|
| **Canonical Definition** | Position benefits when ρ rises (MTM convention) |
| **Canonical Source** | `correlation_convention_framework_final.md` §Canonical Direction Table |
| **Appearances** | Desk Bible (17352, 17524, 17526, 22483), Part 6 (102, 110), Interview System (356, 400, 407), Solutions Manual (1477, 1870), Encyclopedia (4290 corrected) |
| **Status** | Canonical. Lines 17352, 17524, 17526 errata-corrected (E-01, E-02). Line 356 errata-corrected (E-08). |
| **Qualifier** | None needed for MTM usage. "Structurally" required if structural meaning intended. |
| **Related** | CONC-002 (short correlation), CONC-003 (structural), CONC-004 (raw/hedged) |
| **Regression Tests** | REG-COR-01 through REG-COR-04, REG-COR-08 |
| **Linter Rules** | LNT-COR-01, LNT-COR-06, LNT-COR-08 |
| **Convention** | CON-01 |
| **Verified** | 2026-06-27 |

### CONC-002: Short Correlation

| Field | Value |
|-------|-------|
| **Canonical Definition** | Position benefits when ρ falls (MTM convention) |
| **Canonical Source** | `correlation_convention_framework_final.md` §Canonical Direction Table |
| **Appearances** | Desk Bible (17949-17955 corrected), Interview System (358 — desk raw Greek), Encyclopedia (4290 — raw position), Solutions Manual (180, 1447) |
| **Status** | Canonical. NTD table rows errata-corrected (E-09). |
| **Qualifier** | None needed for MTM. "Structurally" required if structural meaning. |
| **Related** | CONC-001, CONC-003, CONC-004 |
| **Regression Tests** | REG-COR-05 through REG-COR-07 |
| **Linter Rules** | LNT-COR-02, LNT-COR-07, LNT-COR-09 |
| **Convention** | CON-01 |
| **Verified** | 2026-06-27 |

### CONC-003: Structural Correlation Convention

| Field | Value |
|-------|-------|
| **Canonical Definition** | Correlation direction described by who bought/sold the correlation premium |
| **Canonical Source** | `correlation_convention_framework_final.md` §Convention B |
| **Appearances** | Desk Bible (via errata corrections), Solutions Manual (180, 1447) |
| **Status** | Canonical as labeled alternate. Must always include "structurally." |
| **Qualifier** | "structurally" — mandatory |
| **Related** | CONC-001, CONC-002 |
| **Regression Tests** | REG-COR-01, REG-COR-02, REG-COR-04, REG-COR-08 |
| **Linter Rules** | LNT-COR-03, LNT-QAL-01 |
| **Convention** | CON-01 |
| **Verified** | 2026-06-27 |

### CONC-004: Raw vs Hedged Position

| Field | Value |
|-------|-------|
| **Canonical Definition** | Raw = pre-hedge exposure. Hedged/net = post-hedge residual. |
| **Canonical Source** | `raw_vs_hedged_position_note_final.md` |
| **Appearances** | Part 6 (102 corrected, 110 corrected), Encyclopedia (4290 corrected), Desk Bible (22483 — review-only R-01) |
| **Status** | Canonical. Lines 102, 110, 4290 errata-corrected (E-03, E-04a, E-04b). Line 22483 review-only. |
| **Qualifier** | "raw/unhedged" or "net/hedged" — mandatory for desk positions |
| **Related** | CONC-001, CONC-002 |
| **Regression Tests** | REG-POS-01 through REG-POS-03 |
| **Linter Rules** | LNT-POS-01, LNT-QAL-02, LNT-QAL-03 |
| **Convention** | CON-02 |
| **Verified** | 2026-06-27 |

### CONC-005: Correlation Reversal (NTD)

| Field | Value |
|-------|-------|
| **Canonical Definition** | The direction flip between FTD (long) and NTD (short), not a within-product non-monotonicity |
| **Canonical Source** | `correlation_convention_framework_final.md` §Correlation Reversal |
| **Appearances** | Desk Bible (17949-17955 — coupon scaling table, errata-corrected E-09) |
| **Status** | Errata-corrected. "Reversal" language removed from table. |
| **Qualifier** | "Between FTD and NTD" when used |
| **Related** | CONC-006 (FTD), CONC-007 (NTD) |
| **Regression Tests** | REG-COR-05, REG-COR-06, REG-COR-09 |
| **Linter Rules** | LNT-COR-10 |
| **Convention** | CON-09 |
| **Verified** | 2026-06-27 |

---

## PRODUCT-SPECIFIC CONCEPTS

### CONC-006: FTD (First-to-Default)

| Field | Value |
|-------|-------|
| **Canonical Definition** | Credit-linked note where the first default in a reference basket triggers loss. Investor is LONG correlation (MTM). |
| **Canonical Source** | Desk Bible §11, `correlation_convention_framework_final.md` |
| **Appearances** | Desk Bible (17300-17600, 17949), Interview System (400, 407, 986), Atlas (1269), Solutions Manual (1279) |
| **Status** | Errata-corrected (E-01a,b,c). Direction changed from "short" to "long." |
| **Qualifier** | None |
| **Related** | CONC-007 (NTD), CONC-001 (long corr), CONC-009 (protection seller) |
| **Regression Tests** | REG-COR-01, REG-COR-02, REG-COR-03, REG-XAR-01 |
| **Linter Rules** | LNT-COR-06 |
| **Convention** | CON-01 |
| **Verified** | 2026-06-27 |

### CONC-007: NTD (Nth-to-Default, N≥2)

| Field | Value |
|-------|-------|
| **Canonical Definition** | Credit-linked note where the Nth default triggers loss. Investor is SHORT correlation (MTM). All N≥2. |
| **Canonical Source** | Desk Bible §11, `correlation_convention_framework_final.md` |
| **Appearances** | Desk Bible (17949-17955 corrected), Interview System (410, 986), Atlas (1298), Solutions Manual (1315) |
| **Status** | Errata-corrected (E-09). Table labels changed from "Long" to "Short" for all N≥2. |
| **Qualifier** | None |
| **Related** | CONC-006 (FTD), CONC-002 (short corr), CONC-005 (reversal) |
| **Regression Tests** | REG-COR-05, REG-COR-06 |
| **Linter Rules** | LNT-COR-07 |
| **Convention** | CON-01, CON-09 |
| **Verified** | 2026-06-27 |

### CONC-008: Worst-of / WOAC

| Field | Value |
|-------|-------|
| **Canonical Definition** | Structured note payoff linked to worst-performing stock in basket. Investor is LONG correlation (MTM). |
| **Canonical Source** | Desk Bible §1.6, §WOAC, `correlation_convention_framework_final.md` |
| **Appearances** | Desk Bible (17526 corrected, 22483, 22536-22605), Part 6 (102 corrected, 110 corrected), Encyclopedia (4290 corrected), Interview System (354-358 corrected), Solutions Manual (1477, 1870), Atlas (1675, 1877) |
| **Status** | Errata-corrected (E-02, E-03, E-04a, E-04b, E-05, E-08). |
| **Qualifier** | Raw/hedged for desk positions |
| **Related** | CONC-001, CONC-004, CONC-009, CONC-013 (dispersion) |
| **Regression Tests** | REG-COR-04, REG-COR-08, REG-POS-01 through REG-POS-03, REG-SGN-01, REG-SGN-04 |
| **Linter Rules** | LNT-COR-08, LNT-POS-01, LNT-STR-01, LNT-STR-02 |
| **Convention** | CON-01, CON-02, CON-04 |
| **Verified** | 2026-06-27 |

### CONC-009: Protection Seller / Buyer

| Field | Value |
|-------|-------|
| **Canonical Definition** | In structured notes: investor = seller (takes risk, earns coupon). Desk = buyer (transfers risk, pays coupon). |
| **Canonical Source** | `correlation_convention_framework_final.md` §Protection Buyer/Seller Note |
| **Appearances** | Part 6 (102 corrected), Desk Bible (CLN/FTD/RC chapters), Interview System, Solutions Manual |
| **Status** | Errata-corrected (E-03). Part 6 ownership misattribution fixed. |
| **Qualifier** | None — must be factually correct |
| **Related** | CONC-010 (embedded put) |
| **Regression Tests** | REG-PRO-01, REG-PRO-02 |
| **Linter Rules** | LNT-PRO-01, LNT-PRO-03 |
| **Convention** | CON-03 |
| **Verified** | 2026-06-27 |

### CONC-010: Embedded Put Ownership

| Field | Value |
|-------|-------|
| **Canonical Definition** | In RC/WOAC/CLN: investor has embedded SHORT put; desk is LONG the put. |
| **Canonical Source** | `correlation_convention_framework_final.md` §Protection Buyer/Seller Note |
| **Appearances** | Part 6 (102 corrected), Desk Bible (RC/WOAC/CLN chapters) |
| **Status** | Errata-corrected (E-03). |
| **Qualifier** | None |
| **Related** | CONC-009 |
| **Regression Tests** | REG-PRO-01 |
| **Linter Rules** | LNT-PRO-03 |
| **Convention** | CON-03 |
| **Verified** | 2026-06-27 |

### CONC-011: Strike

| Field | Value |
|-------|-------|
| **Canonical Definition** | Price/level at which embedded option is exercised. Maturity payoff reference. |
| **Canonical Source** | `market_convention_guide_final.md` §9 |
| **Appearances** | Desk Bible (all worked examples), Interview System, Encyclopedia |
| **Status** | Review-only (R-02): WOAC terms table missing strike definition. |
| **Qualifier** | Must be numerically defined in every worked example |
| **Related** | CONC-012 (barrier) |
| **Regression Tests** | REG-SGN-04 |
| **Linter Rules** | LNT-STR-01, LNT-STR-02 |
| **Convention** | CON-04 |
| **Verified** | 2026-06-27 |

### CONC-012: Barrier

| Field | Value |
|-------|-------|
| **Canonical Definition** | Price/level that activates (knock-in) or deactivates (knock-out) option during product life. |
| **Canonical Source** | `market_convention_guide_final.md` §9 |
| **Appearances** | Desk Bible (all barrier product chapters), Interview System, Encyclopedia |
| **Status** | Canonical |
| **Qualifier** | Must specify knock-in/knock-out, continuous/discrete |
| **Related** | CONC-011 (strike) |
| **Regression Tests** | REG-SGN-04 |
| **Linter Rules** | LNT-STR-01, LNT-STR-02 |
| **Convention** | CON-04 |
| **Verified** | 2026-06-27 |

### CONC-013: Dispersion Trade

| Field | Value |
|-------|-------|
| **Canonical Definition** | Long single-stock vol + short basket vol = SHORT correlation. |
| **Canonical Source** | `correlation_convention_framework_final.md` §Canonical Direction Table |
| **Appearances** | Desk Bible (22483, 22605 corrected) |
| **Status** | Errata-corrected (E-06). Direction label changed from "long" to "short." |
| **Qualifier** | None |
| **Related** | CONC-014 (reverse dispersion), CONC-004 (raw/hedged) |
| **Regression Tests** | REG-COR-07 |
| **Linter Rules** | LNT-COR-09 |
| **Convention** | CON-01 |
| **Verified** | 2026-06-27 |

### CONC-014: Reverse Dispersion

| Field | Value |
|-------|-------|
| **Canonical Definition** | Long basket vol + short single-stock vol = LONG correlation. |
| **Canonical Source** | `correlation_convention_framework_final.md` §Canonical Direction Table |
| **Appearances** | Desk Bible (implied at 22483 — desk's hedging strategy) |
| **Status** | Canonical |
| **Qualifier** | None |
| **Related** | CONC-013 (dispersion), CONC-004 |
| **Regression Tests** | REG-COR-07 (inverse check) |
| **Linter Rules** | LNT-COR-09 (inverse) |
| **Convention** | CON-01 |
| **Verified** | 2026-06-27 |

---

## PRODUCT CONCEPTS (ABBREVIATED)

| Concept ID | Concept | Canonical Source | Status | Convention |
|:----------:|---------|-----------------|:------:|:----------:|
| CONC-015 | RC (Reverse Convertible) | Desk Bible §1 | Canonical | CON-03, CON-04 |
| CONC-016 | Phoenix | Desk Bible §1 | Canonical | CON-04 |
| CONC-017 | CLN (Credit-Linked Note) | Desk Bible §11 | Canonical | CON-01, CON-03 |
| CONC-018 | CDO Equity | `correlation_convention_framework_final.md` | Canonical | CON-01 |
| CONC-019 | CDO Senior | `correlation_convention_framework_final.md` | Canonical | CON-01 |
| CONC-020 | Accumulator | Desk Bible §7 | Canonical | CON-04 |
| CONC-021 | Decumulator | Desk Bible §7 | Canonical | CON-04 |

---

## GREEKS AND SIGN CONCEPTS

| Concept ID | Concept | Canonical Source | Status | Convention | Tests |
|:----------:|---------|-----------------|:------:|:----------:|:-----:|
| CONC-022 | Long vol / short vol | `market_convention_guide_final.md` §4 | Canonical | — | — |
| CONC-023 | Long gamma / short gamma | `market_convention_guide_final.md` §5 | Canonical | — | — |
| CONC-024 | Sign convention (short option) | `market_convention_guide_final.md` §5, R-04 | Review-only | CON-07 | REG-SGN-02 |
| CONC-025 | Gamma × ΔS sign | `worked_example_sanity_checklist_final.md` §Sign Spot-Check | Errata-corrected (E-07) | CON-07 | REG-SGN-02, REG-SGN-03 |

---

## MARKET AND INFRASTRUCTURE CONCEPTS (ABBREVIATED)

| Concept ID | Concept | Canonical Source | Status | Convention | Tests |
|:----------:|---------|-----------------|:------:|:----------:|:-----:|
| CONC-026 | Clean / dirty price | `market_convention_guide_final.md` §8 | Canonical | CON-05 | — |
| CONC-027 | Payer / receiver | `market_convention_guide_final.md` §7 | Canonical | CON-06 | — |
| CONC-028 | Day count convention | `market_convention_guide_final.md` §3 | Canonical | — | — |
| CONC-029 | ISDA / CSA | Encyclopedia | Canonical | — | — |
| CONC-030 | CVA / DVA / FVA | Encyclopedia | Canonical | — | — |
| CONC-031 | ColVA / MVA / KVA | Encyclopedia | Canonical | — | — |
| CONC-032 | SA-CCR / EAD / PFE | Encyclopedia | Canonical | — | — |
| CONC-033 | FTP / IPV / Reserves | Encyclopedia | Canonical | — | — |
| CONC-034 | RAROC | Encyclopedia | Canonical | — | — |
| CONC-035 | Variation margin / Initial margin | Encyclopedia | Canonical | — | — |

---

## TRACEABILITY STATISTICS

| Metric | Count |
|--------|:-----:|
| Total concepts traced | 35 |
| With linked regression tests | 17 |
| With linked linter rules | 17 |
| With linked conventions | 20 |
| Errata-corrected | 11 |
| Review-only | 2 |
| Accept-as-is | 3 |
| Canonical (no defect) | 19 |

---

*Traceability Matrix | V1.0.1-GOV-1.0 | 2026-06-27*
