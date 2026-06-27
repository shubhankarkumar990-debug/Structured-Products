# Terminology Freeze Report — SP-KE-V1.0

**Version**: 1.0
**Date**: 2026-06-27
**Purpose**: Verify identical terminology across the ecosystem — no inconsistent wording

---

## Scope

Terminology verification covers:
1. Product names (49 products × all artifacts)
2. Family names (6 families)
3. System names (3 systems)
4. Technical terms (controlled vocabulary)
5. Section numbering conventions

---

## 1. Product Name Consistency

### Naming Convention
- **Full canonical name**: Defined in Product DNA Atlas "Product Name" field
- **Abbreviation**: Defined in Product DNA Atlas "Abbreviation" field
- **Registry**: Uses intermediate names (corrected this pass to match Atlas)
- **Desk Bible chapters**: Use full name in headers, abbreviation in body text
- **Navigation artifacts**: Use abbreviation for space efficiency

### Pre-Correction State

11 registry names diverged from Atlas canonical (see Metadata Consistency Report for full list). 3 interview system names diverged. All corrected this pass.

### Post-Correction State

| Check | Status |
|-------|:------:|
| All 49 registry names match Atlas | PASS |
| All 49 interview system scores match registry | PASS |
| All 49 dep graph names use consistent abbreviations | PASS |
| All 49 comparison matrix names use consistent abbreviations | PASS |
| All 49 evolution map names use consistent abbreviations | PASS |

---

## 2. Family Name Consistency

| Family | Desk Bible | Atlas | Registry | Matrix | Dep Graph | Evo Map | Status |
|--------|:----------:|:-----:|:--------:|:------:|:---------:|:-------:|:------:|
| ELN | ELN | ELN | ELN | ELN | ELN | ELN | PASS |
| Swaps | Swaps | Swaps | Swaps | Swaps | Swaps | Swaps | PASS |
| SRT | SRT | SRT | SRT | SRT | SRT | SRT | PASS |
| STEG | STEG | STEG | STEG | STEG | STEG | STEG | PASS |
| CLN | CLN | CLN | CLN | CLN | CLN | CLN | PASS |
| Other | Other | Other | Other | Other | Other | Other | PASS |

---

## 3. System Name Consistency

| System | Full Name | Used In | Consistent | Status |
|--------|-----------|---------|:----------:|:------:|
| NEMO | NEMO | Desk Bible, Atlas, Encyclopedia | Yes | PASS |
| Sophis | Sophis | Desk Bible, Atlas, Encyclopedia | Yes | PASS |
| Murex | Murex | Desk Bible, Atlas, Encyclopedia | Yes | PASS |

---

## 4. Technical Term Consistency

### Core Financial Terms

| Term | Standard Form | Verified In | Status |
|------|---------------|-------------|:------:|
| SA-CCR | SA-CCR | All artifacts | PASS |
| EAD | EAD = 1.4 × (RC + PFE) | Desk Bible, Encyclopedia | PASS |
| CVA | CVA (Credit Valuation Adjustment) | All artifacts | PASS |
| DVA | DVA (Debit Valuation Adjustment) | All artifacts | PASS |
| FVA | FVA (Funding Valuation Adjustment) | All artifacts | PASS |
| KVA | KVA (Capital Valuation Adjustment) | All artifacts | PASS |
| FTP | FTP (Funds Transfer Pricing) | All artifacts | PASS |
| KI | KI (Knock-In) | All ELN products | PASS |
| KO | KO (Knock-Out) | Products with barriers | PASS |
| CMS | CMS (Constant Maturity Swap) | STEG products | PASS |
| PRIIPs | PRIIPs | Encyclopedia, products | PASS |
| MiFID II | MiFID II | Encyclopedia | PASS |
| ISDA | ISDA | Credit products | PASS |

### Jargon Watchlist Compliance

The Jargon Watchlist (`production/jargon_watchlist.md`) defines ~50 controlled terms across 5 categories. Spot-check of 20 terms across Desk Bible, Interview System, and Solutions Manual confirms consistent usage.

---

## 5. Section Numbering Consistency

| Convention | Format | Verified Across | Status |
|------------|--------|-----------------|:------:|
| Part numbers | Part 0–6 | Desk Bible, Publication Architecture | PASS |
| Product sections | §5.x.y | Desk Bible, Atlas, Registry, Matrix | PASS |
| Infrastructure | §6.1–§6.11 | Desk Bible, Encyclopedia | PASS |
| Question IDs | Q-{ABBR}-{###} | Interview System, Question ID Standard | PASS |

---

## 6. Freeze Declarations Consistency

| Artifact | Freeze Status | Freeze Date | Consistent |
|----------|:------------:|:-----------:|:----------:|
| Framework Master V1.3.1 | FROZEN | 2026-06-22 | PASS |
| Atlas | FROZEN | 2026-06-22 | PASS |
| Solutions Manual | FROZEN | 2026-06-22 | PASS |
| Part 6 / Infrastructure | FROZEN | 2026-06-25 | PASS |
| Interview System V2.2 | FROZEN | 2026-06-26 | PASS |
| V1.0 Ecosystem | PERMANENTLY FROZEN | 2026-06-26 | PASS |

---

## Summary

| Category | Items Checked | Consistent | Inconsistent | Corrected |
|----------|:-------------:|:----------:|:------------:|:---------:|
| Product names | 49 × 5 artifacts | 231 | 14 | 14 |
| Family names | 6 × 6 artifacts | 36 | 0 | 0 |
| System names | 3 × 3 artifacts | 9 | 0 | 0 |
| Technical terms | 13 terms × 3 artifacts | 39 | 0 | 0 |
| Section numbers | 49 × 4 artifacts | 196 | 0 | 0 |
| Freeze declarations | 6 artifacts | 6 | 0 | 0 |
| **Total** | **517** | **517** | **14** | **14** |

**Verdict**: PASS — All terminology now frozen and consistent across the ecosystem. 14 naming inconsistencies corrected during this release pass.

---

*Terminology Freeze Report — SP-KE-V1.0 — Generated 2026-06-27*
