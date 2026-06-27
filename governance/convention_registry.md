# CONVENTION REGISTRY

**Ecosystem:** Structured Products Knowledge Ecosystem  
**Version:** V1.0.1-GOV-1.0  
**Effective:** 2026-06-27  
**Purpose:** Registry of all concepts with more than one valid convention. Makes convention drift impossible to miss.

---

## Registry Format

Each entry records:
- **Convention ID** — unique identifier
- **Concept** — what has multiple valid conventions
- **Canonical rule** — default convention in this ecosystem
- **Alternate rule** — valid in practice but requires labeling
- **Usage context** — when each convention is appropriate
- **Allowed artifact types** — where the canonical convention applies
- **Prohibited combinations** — what must never appear
- **Required qualifier** — text that must appear when using the alternate convention
- **Examples** — correct and incorrect
- **False-positive risks** — when the linter might over-flag
- **Regression test IDs** — linked tests

---

## CON-01: Correlation Direction Convention

| Field | Value |
|-------|-------|
| **Convention ID** | CON-01 |
| **Concept** | Long/short correlation |
| **Canonical rule** | MTM / Economic Sensitivity: "long" = benefits from ρ rising |
| **Alternate rule** | Structural / Premium: "long" = bought correlation premium |
| **Usage context** | Canonical: all educational text. Alternate: desk premium analysis. |
| **Allowed artifact types** | Canonical: all. Alternate: only when "structurally" qualifier present. |
| **Prohibited combinations** | "Short correlation" + "benefit from high correlation" for same subject in same sentence. "Long correlation" + "harmed by rising correlation" for same subject. |
| **Required qualifier** | Alternate must use: "structurally long/short correlation" |
| **Correct canonical** | "FTD investors are long correlation — they benefit from high ρ." |
| **Correct alternate** | "FTD investors are structurally short correlation — they sold the first-default premium." |
| **Incorrect** | "FTD investors are short correlation. They profit when correlation is high." |
| **False-positive risks** | Two different subjects in adjacent sentences (desk vs investor) with opposite directions — both correct |
| **Regression tests** | REG-COR-01 through REG-COR-09 |
| **Linter rules** | LNT-COR-01 through LNT-COR-10 |

---

## CON-02: Raw vs Hedged Position

| Field | Value |
|-------|-------|
| **Convention ID** | CON-02 |
| **Concept** | Desk position direction (raw exposure vs post-hedge residual) |
| **Canonical rule** | Always state "raw/unhedged" or "net/hedged" when describing desk positions |
| **Alternate rule** | If omitted, default assumption = raw position |
| **Usage context** | Any sentence describing what the desk is long/short |
| **Allowed artifact types** | All. The qualifier must appear in all artifact types. |
| **Prohibited combinations** | "Products are long/short correlation" when the direction depends on hedging without stating which perspective |
| **Required qualifier** | "raw" / "unhedged" / "net" / "hedged" |
| **Correct** | "The desk's raw position is short correlation. After dispersion hedges, the net position is typically long." |
| **Incorrect** | "The desk is long correlation on worst-of products." — raw or hedged? |
| **False-positive risks** | Investor positions don't need the qualifier (investors don't hedge); only desk/bank/dealer positions require it |
| **Regression tests** | REG-POS-01 through REG-POS-03 |
| **Linter rules** | LNT-POS-01, LNT-QAL-02, LNT-QAL-03 |

---

## CON-03: Desk vs Investor Ownership (Structured Notes)

| Field | Value |
|-------|-------|
| **Convention ID** | CON-03 |
| **Concept** | Who sold/bought protection in RC/WOAC/CLN/FTD |
| **Canonical rule** | Investor = protection seller (sold put, earns coupon). Desk = protection buyer (long put, pays coupon). |
| **Alternate rule** | In standalone CDS, desk CAN sell protection. This does not apply to structured notes. |
| **Usage context** | Any structured note product description |
| **Allowed artifact types** | All |
| **Prohibited combinations** | "Desk sold protection" + structured note context. "Desk short put" + structured note context. |
| **Required qualifier** | None — must be factually correct |
| **Correct** | "The investor sold credit protection via the CLN and earns an enhanced coupon." |
| **Incorrect** | "The desk sold protection via the short put." |
| **False-positive risks** | Desk CAN sell protection via standalone CDS or in market-making capacity — not in structured notes to investors |
| **Regression tests** | REG-PRO-01, REG-PRO-02 |
| **Linter rules** | LNT-PRO-01, LNT-PRO-03 |

---

## CON-04: Strike vs Barrier

| Field | Value |
|-------|-------|
| **Convention ID** | CON-04 |
| **Concept** | Strike (maturity payoff reference) vs barrier (during-life observation trigger) |
| **Canonical rule** | Strike = determines payoff calculation at maturity. Barrier = activates/deactivates option during life. Both must be separately defined. |
| **Alternate rule** | None — these are distinct concepts |
| **Usage context** | All worked examples and product descriptions |
| **Allowed artifact types** | All |
| **Prohibited combinations** | "Hit the strike during the life" (likely means barrier). "Below the barrier at maturity" when strike is meant. |
| **Required qualifier** | Both must be numerically defined in every worked example terms table |
| **Correct** | "Barrier: 60% of initial, continuous observation. Strike: 100% of initial, maturity comparison." |
| **Incorrect** | "If the stock hits the strike during the observation period" — describes a barrier |
| **False-positive risks** | Some products have strike = barrier (rare). Must still define both explicitly. |
| **Regression tests** | REG-SGN-04 |
| **Linter rules** | LNT-STR-01, LNT-STR-02 |

---

## CON-05: Clean vs Dirty Price

| Field | Value |
|-------|-------|
| **Convention ID** | CON-05 |
| **Concept** | Bond price quotation (clean) vs settlement (dirty) |
| **Canonical rule** | Quoted prices = clean (exclude accrued interest). Settlement = dirty (include accrued). |
| **Alternate rule** | None |
| **Usage context** | Bond pricing, CLN pricing, structured note pricing at inception/maturity |
| **Allowed artifact types** | All |
| **Prohibited combinations** | Using "price" in a settlement calculation without specifying clean/dirty |
| **Required qualifier** | "clean" or "dirty" when the distinction affects a calculation |
| **Correct** | "The CLN trades at 98 (clean). Settlement: 98 + accrued = 99.25 (dirty)." |
| **Incorrect** | "The bond is worth 98" in a settlement context |
| **False-positive risks** | General discussion of par/discount/premium doesn't need clean/dirty qualifier |
| **Regression tests** | None (no V1.0 defect in this class) |
| **Linter rules** | LNT-MKT-01 |

---

## CON-06: Payer vs Receiver

| Field | Value |
|-------|-------|
| **Convention ID** | CON-06 |
| **Concept** | Interest rate swap direction |
| **Canonical rule** | Payer = pays fixed, receives floating. Receiver = receives fixed, pays floating. |
| **Alternate rule** | None |
| **Usage context** | IRS descriptions, swap product treatments |
| **Allowed artifact types** | All |
| **Prohibited combinations** | "Payer receives fixed" or "receiver pays fixed" |
| **Required qualifier** | None |
| **Correct** | "Enter a payer swap: pay 3.5% fixed, receive SOFR." |
| **Incorrect** | "The payer receives the fixed rate." |
| **False-positive risks** | Context where "payer" refers to the premium payer on a swaption (different concept) |
| **Regression tests** | None (no V1.0 defect) |
| **Linter rules** | LNT-MKT-02 |

---

## CON-07: Sign Convention for Short Option Greeks

| Field | Value |
|-------|-------|
| **Convention ID** | CON-07 |
| **Concept** | Whether position Greeks for short options flip signs from long option Greeks |
| **Canonical rule** | Standard Black-Scholes: position delta for 100 short puts = +50 (sign flipped from long). Position gamma = −3 (sign flipped). |
| **Alternate rule** | V1.0 Desk Bible convention: shows per-option Greeks × quantity without sign flip (delta = −50 for short put). Non-standard but internally consistent. |
| **Usage context** | Worked examples with Greek calculations |
| **Allowed artifact types** | All, but alternate requires footnote |
| **Prohibited combinations** | Mixing conventions within the same worked example. Using alternate without footnote. |
| **Required qualifier** | If using alternate: footnote explaining the convention |
| **Correct** | "Delta = −50 (per-option convention, pre-sign-flip; see footnote)" with footnote |
| **Incorrect** | "Delta = −50 for the short put" without any convention note |
| **False-positive risks** | The convention is internally consistent — errors only appear in intermediate steps (E-07) |
| **Regression tests** | REG-SGN-02, REG-SGN-03 |
| **Linter rules** | LNT-GRK-03, LNT-GRK-04 |

---

## CON-08: Pedagogical Simplification Boundaries

| Field | Value |
|-------|-------|
| **Convention ID** | CON-08 |
| **Concept** | Where simplification is allowed vs forbidden |
| **Canonical rule** | Simplification is allowed if: (a) it builds intuition, (b) it is immediately corrected or qualified, (c) it does not produce a wrong interview answer |
| **Alternate rule** | N/A |
| **Usage context** | ELI5 sections, Tier 1 interview content, introductory passages |
| **Allowed** | Independence assumption in barrier breach probability formula if followed by correlation discussion (A-04). Label-free economic descriptions (A-02, A-03). Convention mixing where each sentence is individually correct (A-01). |
| **Prohibited** | Self-contradictory sentences even in simplified context. Wrong labels even in ELI5. Simplified formulas presented as exact without caveat. |
| **Required qualifier** | "Under the simplifying assumption of..." or equivalent when assumption is non-trivial |
| **Regression tests** | REG-XAR-02 (Solutions Manual mixing), REG-XAR-03 (Atlas label avoidance) |
| **Linter rules** | LNT-COR-01, LNT-COR-02 (apply even in simplified sections) |

---

## CON-09: NTD "Correlation Reversal" Terminology

| Field | Value |
|-------|-------|
| **Convention ID** | CON-09 |
| **Concept** | What "correlation reversal" means in NTD products |
| **Canonical rule** | "Reversal" = the direction flip between FTD (long) and NTD (short). Not a within-product non-monotonicity. |
| **Alternate rule** | None allowed |
| **Usage context** | NTD product descriptions, coupon scaling tables |
| **Prohibited combinations** | "2TD reverses at high ρ" (implies within-product flip). "Reversal at moderate ρ" without specifying it means the FTD-NTD difference. |
| **Required qualifier** | "The reversal between FTD and NTD" or "the direction flip from FTD to NTD" |
| **Correct** | "The correlation reversal between FTD and NTD: FTD is long, NTD (N≥2) is short." |
| **Incorrect** | "2TD: Short at low ρ, reversal at high ρ" — implies 2TD flips direction |
| **Regression tests** | REG-COR-05, REG-COR-09 |
| **Linter rules** | LNT-COR-10 |

---

## CON-10: Hedged Position as Product Property

| Field | Value |
|-------|-------|
| **Convention ID** | CON-10 |
| **Concept** | Whether a hedged desk position can be described as a property of the product |
| **Canonical rule** | No. The hedge is a choice; the raw exposure is structural. Hedged positions must be attributed to the desk's net book, not to the product. |
| **Alternate rule** | None |
| **Usage context** | Any sentence of the form "Product X is long/short correlation" |
| **Prohibited combinations** | "Worst-of products are long correlation" when describing the desk's hedged position |
| **Required qualifier** | "The desk's net position on worst-of is long" (not "worst-of products are long") |
| **Correct** | "Worst-of investors are long correlation. The desk's raw position is short; net is typically long." |
| **Incorrect** | "Worst-of products are long correlation for the bank." |
| **Regression tests** | REG-POS-01 |
| **Linter rules** | LNT-QAL-03 |

---

## REGISTRY SUMMARY

| ID | Concept | Canonical | Alternate | Qualifier Required | S1 Defect Risk |
|:--:|---------|-----------|-----------|:------------------:|:--------------:|
| CON-01 | Correlation direction | MTM sensitivity | Structural premium | "structurally" | Yes (E-01, E-02, E-08) |
| CON-02 | Raw vs hedged | Must state | Default = raw | "raw/hedged/net" | Yes (E-03, E-04) |
| CON-03 | Protection ownership | Investor = seller | CDS desk = seller | None (must be correct) | Yes (E-03) |
| CON-04 | Strike vs barrier | Distinct concepts | None | Both defined | Yes (E-05) |
| CON-05 | Clean vs dirty | Clean = quoted | None | "clean/dirty" in calc | No |
| CON-06 | Payer vs receiver | Payer = pays fixed | None | None | No |
| CON-07 | Short option signs | Standard BS | Per-option pre-flip | Footnote | Yes (E-07) |
| CON-08 | Simplification | Allowed if qualified | N/A | Caveat statement | No |
| CON-09 | NTD reversal | Cross-product flip | None allowed | "between FTD and NTD" | Yes (E-09) |
| CON-10 | Hedged as product property | Not allowed | None | Desk attribution | Yes (E-04) |

---

*Convention Registry | V1.0.1-GOV-1.0 | 2026-06-27*
