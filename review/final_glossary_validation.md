# Final Glossary & Acronym Validation

**Date**: 2026-06-26
**Authority**: Head of Documentation
**Scope**: Glossary completeness, acronym coverage, term consistency

---

## 1. Current State

| Reference File | Path | Entries | Coverage |
|---------------|------|:-------:|----------|
| Glossary | `reference/glossary/glossary.yaml` | 119 terms | Parts 0-5 comprehensive; Part 6 incomplete |
| Acronyms | `reference/acronyms/acronyms.yaml` | 69 entries | Parts 0-5 comprehensive; Part 6 incomplete |

---

## 2. Glossary Assessment

### Coverage by Part

| Part | Coverage | Notes |
|:----:|:--------:|-------|
| Part 0 (How Finance Works) | ✅ Complete | Foundational terms well covered |
| Part 1 (Foundations) | ✅ Complete | Options, Greeks, volatility all defined |
| Part 2 (Framework) | ✅ Complete | Classification terms defined |
| Part 3 (Taxonomy) | ✅ Complete | Family names defined |
| Part 4 (Comparisons) | ✅ Complete | Comparison terminology defined |
| Part 5 (Product Chapters) | ✅ Complete | Product-specific terms defined |
| Part 6 (Infrastructure) | ⚠️ Incomplete | ~40+ terms used but not in glossary |

### Part 6 Terms Missing from Glossary (Sampled)

| Section | Missing Terms |
|:-------:|--------------|
| §6.1 | Modified Following, FRA Discounting, Fixing Source, ISDA Fixing, Observation Lag, Roll Convention |
| §6.3 | ISDA Schedule, CSA Threshold, Minimum Transfer Amount, Close-Out Netting, Netting Agreement |
| §6.5 | Model Reserve, Bid-Offer Reserve, IPV, Fair Value Hierarchy, Level 1/2/3 |
| §6.6 | P&L Explain, P&L Attribution, New Deal P&L, Theta P&L, Gamma P&L |
| §6.7 | FTP, CVA Desk, XVA Charge, ColVA, MVA, KVA, RAROC, SA-CCR, EAD, PFE |
| §6.8 | Model Validation, Model Inventory, Model Limitation, Back-Testing, Stress Testing |
| §6.9 | Trade Break, Settlement Fail, SSI, Nostro, Vostro, Reconciliation |
| §6.10 | Pre-Trade Check, Axis Rotation, Client Suitability, Structuring Process |
| §6.11 | PRIIPs KID, MiFID II, EMIR, UMR, FRTB, NSFR, LCR, TLAC, MREL |

### Decision: DEFER

The glossary is a reference file, not a frozen canonical artifact. Expanding it does not require unfreezing any production artifact. However, adding ~40+ terms with full definitions (plain English, professional, cross-references) is a Phase 2 content task that exceeds the scope of V1.0 remediation.

**Every Part 6 term IS defined in context within the Desk Bible manuscript.** The glossary gap means readers cannot look up Part 6 terms via the glossary — they must navigate to the relevant §6.x section. This is a navigation inconvenience, not a content gap.

---

## 3. Acronym Assessment

### Missing Part 6 Acronyms

| Acronym | Expansion | First Contextual Use |
|---------|-----------|---------------------|
| SA-CCR | Standardised Approach for Counterparty Credit Risk | §6.7 (defined in context) |
| RAROC | Risk-Adjusted Return on Capital | §6.7 (defined in context) |
| IPV | Independent Price Verification | §6.6 (defined in context) |
| FRTB | Fundamental Review of the Trading Book | §6.11 (defined in context) |
| UMR | Uncleared Margin Rules | §6.11 (defined in context) |
| PRIIPs | Packaged Retail Investment and Insurance Products | §6.11 (defined in context) |
| MiFID | Markets in Financial Instruments Directive | §6.11 (defined in context) |
| EMIR | European Market Infrastructure Regulation | §6.11 (defined in context) |
| NSFR | Net Stable Funding Ratio | §6.7 (defined in context) |
| LCR | Liquidity Coverage Ratio | §6.7 (defined in context) |
| PONV | Point of Non-Viability | §6.4 (defined in context) |
| SSI | Standard Settlement Instructions | §6.9 (defined in context) |
| FVA | Funding Valuation Adjustment | §6.7 (defined in context) |
| ColVA | Collateral Valuation Adjustment | §6.7 (defined in context) |
| MVA | Margin Valuation Adjustment | §6.7 (defined in context) |

### Decision: DEFER

Same rationale as glossary. All acronyms are defined in context within the manuscript. The acronym file expansion is a Phase 2 convenience improvement.

---

## 4. Term Consistency Spot-Check

| Term | Desk Bible | Interview System V2.2 | Atlas | Consistent |
|------|-----------|----------------------|-------|:----------:|
| CVA | "Cost of counterparty default risk" | "Cost of counterparty default risk ≈ PD × LGD × EPE" | "CVA" (field) | ✅ |
| FTP | "Internal cost charged to desk for using bank's balance sheet" | "Internal cost charged to the desk for using the bank's balance sheet" | N/A | ✅ |
| SA-CCR | "EAD = 1.4 × (RC + PFE)" | "EAD = 1.4 × (RC + PFE)" | N/A | ✅ |
| RAROC | "(Revenue − Costs − EL) / Capital" | "(Revenue − Costs − EL) / Capital" | N/A | ✅ |
| Knock-in | Used 126× lowercase, 26× title-case | Used consistently | Used consistently | ⚠️ Casing varies in Desk Bible |
| Worst-of | Used 131× lowercase | Used consistently | "Worst-of" in product names | ⚠️ Casing varies in Desk Bible |

---

## 5. Verdict

**Glossary and acronyms are COMPLETE for the scope they were designed for (Parts 0-5 product content).** The gap is Part 6 infrastructure terminology, which was written after the glossary/acronym files were established.

**No V1.0 blocker.** All Part 6 terms are defined in context within the manuscript. The reference files are a navigation aid, not a content source.

**Phase 2 recommendation**: Expand glossary to ~160 terms and acronyms to ~85 entries covering Part 6 infrastructure vocabulary.
