# PUBLICATION SPECIFICATION — Phoenix Autocallable

Reviewed: 2026-06-18
Master document: Structured_Products_Desk_Bible_COMPLETE.docx

## INSERTION POINT

Insert after:     Section 3.2 "Autocallables" heading (H2)
Insert before:    "Fixed Coupon Note (FCN)" (H3)
Part:             Part 3 — Equity-Linked Notes
Section:          3.2 Autocallables
Position within section: First product

## HEADING HIERARCHY VERIFICATION

- [x] Heading 3 present: "Phoenix Autocallable" — correct level for a named product
- [x] All 8 Heading 4 subsections present:
    - [x] Definition
    - [x] Construction
    - [x] Booking & systems
    - [x] Pricing intuition
    - [x] Worked example (USD 10M)
    - [x] Reconciliation specifics
    - [x] Desk view
    - [x] Desk shorthand
- [x] No Heading 1 or Heading 2 in the content (publisher adds those)
- [x] No unnumbered headings at any level

## TOC ENTRY

Level 3 entry:  "Phoenix Autocallable"
Level 4 entries (in order):
  Definition
  Construction
  Booking & systems
  Pricing intuition
  Worked example (USD 10M)
  Reconciliation specifics
  Desk view
  Desk shorthand

## NUMBERING VERIFICATION

No manual numbering in content: PASS
Section number assigned by document structure: PASS — inherits 3.2 from parent
Product sequence within section is correct: PASS — Phoenix Autocallable is first in 3.2

## PAGE STRUCTURE

Page break required before this product: Yes — first product in section 3.2
Page break required after this product: No — FCN follows within the same section

## APPENDIX UPDATES REQUIRED

- [x] Appendix B.4 update required: add NEMO/Sophis fields for Phoenix Autocallable
  - Fields to add: AUTOCALL_BARRIER_PCT, AUTOCALL_BARRIER_COMPARE, COUPON_BARRIER_PCT, DOWNSIDE_BARRIER_TYPE, MEMORY_FEATURE_FLAG, MEMORY_FEATURE_TYPE, OBS_ADJUSTMENT_CONVENTION, CORRELATION_MATRIX_ID, CORR_DEFAULT_OVERRIDE
- [x] Appendix B.5 update required: add cross-system reconciliation checks
  - Checks to add: autocall barrier comparison convention (GTE vs GT), coupon barrier representation (% vs absolute), memory feature type (ALL_UNPAID vs MOST_RECENT_UNPAID), observation schedule alignment (skip vs roll), basket correlation validation
- [ ] No Appendix B.1/B.2/B.3 update required (Murex not used for ELN)

## PUBLICATION CHECKLIST

- [x] All 8 subsections present with content (not empty headings)
- [x] Desk shorthand is italic
- [x] No emoji in content
- [x] No manual page numbers in content
- [x] No headers or footers embedded in content (document-level only)
- [x] Content is self-contained — no dangling references that require context from the session to understand

## GATE RECOMMENDATION

[x] READY FOR MERGE — All checklist items passed.

Merge instruction:
  Insert content at: Part 3, §3.2 Autocallables, first product position (before FCN)
  Update TOC:        Yes — regenerate after insertion
  Appendix updates:  Appendix B.4 (NEMO/Sophis fields) and B.5 (reconciliation checks)
