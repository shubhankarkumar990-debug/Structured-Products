# Publication Manifest

**Generated:** 2026-06-19  
**Release Tag:** desk-bible-v1-publication

---

## Source

| Field | Value |
|-------|-------|
| Source file | `release/desk-bible-v1/Desk_Bible_v1.md` |
| Source size | 282,808 bytes (276 KB) |
| Source lines | 2,821 |
| Source modified | 2026-06-19 04:29:07 |
| Source status | IMMUTABLE — not modified during publication |

---

## Outputs

| File | Format | Size | Generated |
|------|--------|------|-----------|
| `release/desk-bible-v1/Desk_Bible_v1.docx` | DOCX | 134,404 bytes (131 KB) | 2026-06-19 13:04:21 |
| `release/desk-bible-v1/Desk_Bible_v1.pdf` | PDF | 236,898 bytes (231 KB) | 2026-06-19 13:04:23 |

---

## Validation Results

### DOCX

| Check | Result |
|-------|--------|
| File exists | PASS |
| File size > 0 | PASS (134,404 bytes) |
| Products found | 28/28 (PASS) |
| Families (Parts) found | 5/5 (PASS) |
| Cover page present | PASS |
| Table of contents present | PASS |
| Appendices present | PASS |
| Headers and footers | PASS |
| Page breaks between Parts | PASS |
| Page breaks between products | PASS |
| Truncation check | PASS (2,297 paragraphs, 2,201 non-empty) |

### PDF

| Check | Result |
|-------|--------|
| File exists | PASS |
| File size > 0 | PASS (236,898 bytes) |
| Page count | 112 pages |
| Cover page present | PASS |
| Table of contents present | PASS |
| Appendices present | PASS |
| Headers (every page) | PASS |
| Footers with page numbers | PASS |
| Page breaks between Parts | PASS |
| Page breaks between products | PASS |

### Content Verification

| Check | Result |
|-------|--------|
| All 28 products present in DOCX | PASS |
| Part 3 — Equity-Linked Notes (13 products) | PASS |
| Part 4 — Structured Rate Trades (5 products) | PASS |
| Part 5 — Swaps (1 product) | PASS |
| Part 6 — Credit-Linked Notes (5 products) | PASS |
| Part 7 — Steepener Notes (4 products) | PASS |
| No truncation detected | PASS |
| Source markdown unmodified | PASS |

---

## Document Features

### Both Formats

- Cover page with title, version, date, release tag, product count, classification
- Table of contents with Part/Section/Product hierarchy
- Part headings with page breaks
- Product headings with page breaks
- Section headings (H4) for each product subsection
- Tables with header row styling and alternating row shading
- Bold and italic inline formatting
- Bullet lists
- Appendix A: Release Notes Reference
- Appendix B: Product Catalog (28 products, 4 columns)
- Appendix C: Quality Metrics Summary

### DOCX-Specific

- Page numbers via field codes
- Header: "Structured Products Desk Bible | v1.0 | CONFIDENTIAL"
- Calibri font, A4 page size, 2.5 cm margins

### PDF-Specific

- Page numbers in footer
- Header: "Structured Products Desk Bible | v1.0 | CONFIDENTIAL"
- Helvetica font, A4 page size, 25 mm margins
- 112 pages total

---

## Generation Method

- Script: `scripts/generate_publication.py`
- DOCX: python-docx 1.2.0
- PDF: fpdf2
- Source parsed: line-by-line markdown with heading, table, list, and inline formatting detection
- Source not modified during generation

---

## Verdict

All validation checks PASS. Both DOCX and PDF contain the complete Desk Bible (28 products, 5 families) with cover page, TOC, appendices, headers, footers, and page breaks. No truncation detected.
