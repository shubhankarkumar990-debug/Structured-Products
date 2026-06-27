# Tier 1 Structural Audit — Findings Report

**Scope:** `Desk_Bible_v2.md` (23,985 lines, 1,202 headings, 49 products, 157 diagram embeds), read-only structural sweep.
**Method:** `governance/audit/tier1_structural.py` — part structure, product numbering, cross-references, diagram embed integrity, dual-lens parity, duplicate-heading and per-product section-signature scan.
**Date:** 28 Jun 2026

## Headline

The transformation is **structurally sound where it matters most.** Zero S1 (blocking) findings:

- All **157** embedded diagrams resolve to files on disk — no broken images, no orphan SVGs.
- All **49** products are numbered cleanly (5.1.1 → 5.6.12) — no gaps, no duplicates, count = 49.
- **Dual-lens parity is perfect:** every product carries §7 Investor Lens, §8 Bank Lens (Desk), §9 Bank Lens (Controls), and a Knowledge Check — 49/49/49/49.
- No splice-duplication damage: every repeated heading is a *templated* sub-header reused across different chapters, not a copy-paste artifact in one place.

The earlier splice/global-replace incidents left **no residual structural damage.** The defects that remain are navigational and cosmetic, in the book's scaffolding — not in the product content.

## Findings

### S2 — should fix (navigation integrity)

**F1 · Part 6 has no `# PART 6` banner.**
Parts 0–5 each open with a level-1 banner (`# PART 5 — PRODUCT DEEP DIVES`). Part 6's operational content jumps straight from `### 5.6.12 Worst-of Autocallable` (line 20159) to `## 6.1 Market Conventions` (line 20531) with no `# PART 6 — …` opener. A reader scanning level-1 headings (or any auto-generated TOC) sees Part 6 vanish.
*Fix:* insert one level-1 banner before line 20531, e.g. `# PART 6 — DESK OPERATIONS & CONTROL`.

**F2 · Part 7 is promised in front matter but does not exist.**
"How to Use This Book" routes readers to "the quick reference in **Part 7**" and "**Part 7.5**" (interview prep). The document has no Part 7 — no banner, no `## 7.x` content. The body ends at Part 6 material.
*Fix (choose one):*
(a) Promote the book-level closing sections (`## Part 6 — Knowledge Check`, `## Part 6 — Mental Models Summary`, lines 23899/23937) into a real `# PART 7 — QUICK REFERENCE` and renumber them 7.x; or
(b) if no quick-reference is intended in-book, correct the front-matter routing table to drop Part 7 / Part 7.5 and point to where that content actually lives (product Knowledge Checks; companion Interview System).
Recommend (a) — the end glossary *is* a quick reference; it's just mislabeled.

### S3 — cosmetic / consistency (optional)

**F3 · Closing glossaries mislabeled "Part 6."**
`## Part 6 — Knowledge Check` and `## Part 6 — Mental Models Summary` (lines 23899, 23937) are book-wide closing sections, not Part-6-specific (the Mental Models table spans the whole book). Same root cause as F2 — fixed by the F2(a) renumber.

**F4 · Per-product §-template drift.**
31 products (all of 5.1.x, most of 5.2.x, 5.5.1) carry numbered `#### §21. Visual Specifications` / `#### §22. Dependency References`; the other 18 stop at §14 and present the same material under unnumbered headers (`### Visual Learning Recommendations`, `### Dependency References`). Two authoring generations. Purely cosmetic — content is present in both; only the heading style differs.
*Fix (optional):* normalise to one convention (either number §21/§22 everywhere or drop the numbers everywhere).

### S1 — none. S4 — none (no orphan assets).

## Recommendation

F1 and F2 are worth fixing — they're small, mechanical, and they're the parts of the book a new reader hits first (front-matter promises that don't resolve). F3 falls out of the F2(a) fix. F4 is genuinely optional polish.

Because the front matter makes promises the body doesn't keep (F2), a **Tier 2 bookend read** (cover → How-to-Use → Part boundaries → appendices) is now justified — that's exactly the zone where these defects live and where more may hide. Tier 3 (full prose reread) remains low-value: the per-family audits already covered semantic content and parity is provably complete.

---

## Resolution (applied)

F1, F2, F3 fixed with scoped edits; quality gate re-run green (linter 0 S1, regression 21/21); Tier 1 re-run shows **S1 = 0, S2 = 0**.

- **F1** — inserted `# PART 6 — DESK OPERATIONS & CONTROL` banner before §6.1 (line 20534).
- **F2** — promoted the book-wide closing glossaries to `# PART 7 — QUICK REFERENCE`; renumbered to `## 7.1 Knowledge Check` and `## 7.2 Mental Models Summary`. Part 7 now exists and the front-matter "quick reference in Part 7" reference resolves.
- **F3** — fell out of F2 (glossaries no longer mislabeled "Part 6").
- Front matter: `Part 7.5` (never existed) repointed to `Part 7 (Quick Reference)`.

## Tier 2 — bookend read (complete, no new findings)

Read cover, How-to-Use, all eight part boundaries, the inserted Part 6/7 banners in context, and the document end.
- All part transitions are clean: each opens with an italic intro and `---` rules; forward-references resolve (Part 1's "Parts 2 through 7" is now true).
- Part 7 banner and 7.1/7.2 sections read naturally; the operations-flavoured review questions suit a revision/interview quick-reference.
- Document ends cleanly on the mental-models glossary — no orphaned splice fragments anywhere in the bookend zones.

## F4 — §-template drift (fixed)

24 products (all 5.1.x, 5.2.x, 5.5.1) numbered their tail sections `#### §21. Visual Specifications` / `#### §22. Related Chapters / Dependency References` — jumping from §14 straight to §21, implying phantom sections §15–20 that never existed. The other 25 products end clean at §14 with unnumbered tail headers.

Resolved by stripping the misleading numbers (the genuine reader-facing defect): `§21. Visual Specifications` → `Visual Specifications`, `§22. Related Chapters / Dependency References` → `Dependency References`. Safe global replace — both were unique fully-qualified heading lines (24 each), no prose cross-referenced §21/§22, and no §15–20 existed to break.

Result: all 49 products now share one section signature (§1–14 + unnumbered tail). Tier 1 re-run is **fully clean — S1=0 S2=0 S3=0 S4=0**. Gate green (linter 0 S1, regression 21/21).

## Final verdict

End-to-end structure is sound and now fully clean across every Tier 1 check. The transformation left no splice damage; the only real defects were navigation scaffolding (Part 6/7 banners) and a cosmetic numbering gap — all fixed and gate-verified. **Tier 3 (full prose reread) is not warranted** — semantic content was audited per-family, parity is provably 49/49, and the gate is green.
