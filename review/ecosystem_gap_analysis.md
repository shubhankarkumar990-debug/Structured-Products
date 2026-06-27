# Ecosystem Gap Analysis

**Date**: 2026-06-25
**Scope**: Missing content, incomplete coverage, orphaned artifacts, unfulfilled specifications
**Auditor**: Publication Review Board (Phases 9-11 of 12)

---

## 1. Reference Infrastructure Gaps

### G-1 | MEDIUM | Glossary Incomplete for Part 6

**Current state**: `reference/glossary/glossary.yaml` contains 119 terms covering Parts 0-5.

**Missing terms** (estimated ~40+ from Part 6):

| Part 6 Section | Sample Missing Terms |
|:--------------:|---------------------|
| §6.1 Market Conventions | Modified Following, FRA Discounting, Fixing Source, ISDA Fixing, Observation Lag |
| §6.3 Documentation & Legal | ISDA Schedule, CSA Threshold, Minimum Transfer Amount, Close-Out Netting |
| §6.5 Valuation | Model Reserve, Bid-Offer Reserve, IPV (Independent Price Verification) |
| §6.6 Product Control | P&L Explain, P&L Attribution, New Deal P&L, Theta P&L |
| §6.7 Treasury/Capital/XVA | FTP, CVA Desk, XVA Charge, ColVA, MVA, KVA, RAROC, SA-CCR |
| §6.8 Model Risk | Model Validation, Model Inventory, Model Limitation, Back-Testing |
| §6.9 Operations | Trade Break, Settlement Fail, SSI (Standard Settlement Instructions) |
| §6.11 Regulatory | PRIIPs, MiFID II, EMIR, UMR, FRTB, NSFR, LCR |

**Impact**: Readers using the glossary as a lookup tool will not find infrastructure terminology introduced in Part 6.

**Recommendation**: Expand glossary to ~160+ terms covering Part 6 infrastructure vocabulary.

---

### G-2 | MEDIUM | Acronyms Incomplete for Part 6

**Current state**: `reference/acronyms/acronyms.yaml` contains 69 acronyms.

**Missing acronyms** (at least 15 used in Part 6 without glossary entry):

| Acronym | Expansion | First Use |
|---------|-----------|-----------|
| SA-CCR | Standardised Approach for Counterparty Credit Risk | §6.7 |
| RAROC | Risk-Adjusted Return on Capital | §6.7 |
| IPV | Independent Price Verification | §6.6 |
| FRTB | Fundamental Review of the Trading Book | §6.11 |
| UMR | Uncleared Margin Rules | §6.11 |
| PRIIPs | Packaged Retail Investment and Insurance Products | §6.11 |
| MiFID | Markets in Financial Instruments Directive | §6.11 |
| EMIR | European Market Infrastructure Regulation | §6.11 |
| NSFR | Net Stable Funding Ratio | §6.7 |
| LCR | Liquidity Coverage Ratio | §6.7 |
| PONV | Point of Non-Viability | §6.4 |
| SSI | Standard Settlement Instructions | §6.9 |
| MTM | Mark-to-Market | §6.5/§6.6 |
| FVA | Funding Valuation Adjustment | §6.7 |
| ColVA | Collateral Valuation Adjustment | §6.7 |

**Impact**: Same as G-1 — infrastructure acronyms undefined in the reference system.

**Recommendation**: Expand to ~85+ acronyms.

---

## 2. Publication Infrastructure Gaps

### G-3 | LOW | Publication Identifier Standard Not Retrofitted

**Current state**: `production/publication_identifier_standard.md` defines a systematic ID scheme (FIG-5.1.1-01, TBL-6.7-03, EX-5.2.5-01) for figures, tables, and examples.

**Gap**: Zero artifacts have been updated to use these identifiers. The Desk Bible uses informal references ("See Figure 5.1.1-01") that happen to match the standard's format, but the IDs are not formally assigned, indexed, or machine-parseable.

**Impact**: Element-level linking (e.g., "jump to Table 6.7-03") is not possible. Digital transformation and AI tutor integration are blocked at the element level.

**Recommendation**: Retrofitting is a Phase 2 task. The standard is well-designed and ready for implementation.

---

### G-4 | LOW | Visual Specifications Exist But No Graphics Generated

**Current state**: `review/part6_visual_specifications.md` defines 11 detailed diagram specifications. `production/visual_asset_master_registry.yaml` catalogues ~196 figure slots across 49 product chapters + Part 6.

**Gap**: Zero visual assets have been produced. All figure references in the Desk Bible (e.g., "See Figure 5.1.1-01") point to specifications, not rendered images.

**Impact**: The manuscript is text-only. Complex concepts (payoff diagrams, barrier mechanics, P&L decomposition, SA-CCR flow) lack visual support. This is the single largest gap between the current state and a publication-ready product.

**Recommendation**: Visual production is a Phase 2 priority. The specification infrastructure is comprehensive and ready for execution.

---

## 3. Structural Gaps

### G-5 | LOW | No Master Index Appendix

**Current state**: Navigation is supported by Atlas views, Learning Dependency Graph, Searchability Alias Map, and Cross-Reference Map. There is no unified Index appendix in the manuscript.

**Gap**: A traditional book Index (alphabetical list of terms → page/section references) is absent. The Searchability Alias Map partially serves this function but is a separate file, not part of the manuscript.

**Impact**: Print/PDF readers cannot quickly locate topics by keyword. Digital readers can use Ctrl+F, but the manuscript's 25,764 lines make this slow.

**Recommendation**: Generate a master Index appendix from the Searchability Alias Map. Medium priority for print edition, low for digital.

---

### G-6 | LOW | Single-File Manuscript

**Current state**: The entire Desk Bible is a single 25,764-line markdown file.

**Gap**: This is a scalability concern for:
- Version control (any edit touches the entire file)
- Collaborative editing (merge conflicts on every change)
- Web/app deployment (entire file must load)
- CI/CD (no per-chapter validation possible)

The file is well-structured with clear `### 5.x.y` delimiters, making mechanical splitting feasible.

**Impact**: No impact on current print/PDF publication. Significant impact on future digital formats.

**Recommendation**: Phase 2 task. Split into per-chapter files with a build system that assembles the full manuscript. The delimiter structure supports this without content changes.

---

## 4. Orphaned/Deprecated Artifacts

### G-7 | LOW | products/catalog.yaml Orphaned

**Current state**: `products/catalog.yaml` references 28 products using V1 section numbers (Part 3/4/5/6/7) that don't match the current manuscript structure.

**Gap**: This file is not referenced by any canonical artifact and contradicts the Atlas (which has 49 products with current section numbers).

**Impact**: None — no artifact references it. Risk of confusion if a future contributor discovers it.

**Recommendation**: Add `# DEPRECATED — Superseded by production/product_dna_atlas.md` header.

---

### G-8 | LOW | Superseded Interview System Versions

**Current state**: `production/interview_system.md` (V1) and `production/interview_system_v2.md` (V2.0) remain in the production directory alongside the canonical `production/interview_system_v2_1.md`.

**Gap**: No deprecation markers. A reader browsing the production directory sees three versions with no indication of which is current.

**Impact**: Risk of using wrong version.

**Recommendation**: Add `# DEPRECATED — Superseded by interview_system_v2_1.md` headers to V1 and V2.0.

---

## 5. Missing Artifact Assessment

| Potential Artifact | Value | Effort | Overlap with Existing | Priority |
|-------------------|:-----:|:------:|:--------------------:|:--------:|
| Expanded Glossary (+40 terms) | HIGH | LOW | Extends existing file | HIGH |
| Expanded Acronyms (+15 entries) | HIGH | LOW | Extends existing file | HIGH |
| Visual Assets (~196 figures) | HIGH | HIGH | Specs exist, rendering needed | Phase 2 |
| Master Index Appendix | MEDIUM | LOW | Alias Map provides data | Phase 2 |
| Formula Quick-Reference | MEDIUM | LOW | Extract from existing content | Phase 2 |
| Hedging Playbook | HIGH | MEDIUM-HIGH | Complements §13 per product | Phase 2 |
| Case Study Library | HIGH | MEDIUM | Extends §20 per product | Phase 2 |
| Trade Break Library | MEDIUM-HIGH | MEDIUM | Extends §6.9 | Phase 2 |
| Reading Paths by Role | MEDIUM | LOW | Atlas Start Here + Interview §12 | Phase 2 |
| Structured AI Dataset | HIGH | MEDIUM | Extraction from existing | Future |

---

## 6. Gap Summary

| Severity | Count | Key Gaps |
|:--------:|:-----:|----------|
| MEDIUM | 2 | Glossary incomplete for Part 6 (G-1), Acronyms incomplete for Part 6 (G-2) |
| LOW | 6 | Identifier standard not retrofitted (G-3), no graphics (G-4), no Index (G-5), single-file manuscript (G-6), orphaned catalog (G-7), superseded versions unmarked (G-8) |

**No CRITICAL or HIGH gaps.** The ecosystem is content-complete for V1.0 publication. All gaps are either reference infrastructure (expandable without content changes) or Phase 2 deliverables (visual assets, digital formats) that don't affect the manuscript's textual quality.
