# First Edition Scope Review

**Date:** 2026-06-21
**Framework:** v1.3.1 (FROZEN)
**Purpose:** Determine what ships in First Edition vs Companion/V2/Digital
**Input:** 15 accepted enhancements, 1 deferred, from `final_educational_architecture_verdict.md`

---

## Phase 1: Enhancement Classification

### 1.1 Classification Framework

| Category | Definition | Binding? |
|----------|-----------|:--------:|
| **Core First Edition** | Book is incomplete without it. Reader cannot use the book effectively if missing | YES |
| **First Edition Optional** | Materially improves the book. Include if page budget allows. Exclusion does not break the reading experience | NO |
| **Companion Material** | Self-contained reference that benefits from physical separation. Published simultaneously or shortly after | NO |
| **Volume 2** | Requires V1 to exist. Extends rather than completes. Separate publication cycle | NO |
| **Digital Supplement** | Best delivered electronically. Interactive, updatable, or format-dependent | NO |

### 1.2 Classifications

| ID | Enhancement | Classification | Justification |
|:--:|------------|:--------------:|---------------|
| E6 | Template Harmonization | **Core First Edition** | Cannot publish 16 chapters at v1.0 format alongside 33 at v1.3.1. Consistency is non-negotiable for a professional reference |
| E5 | Front Matter | **Core First Edition** | Reader Guide, Learning Paths, Visual Legend are standard publication requirements. No professional reference ships without front matter |
| E7 | Glossary Refresh | **Core First Edition** | Glossary is a working reference tool. Stale metadata undermines trust. Must align with 49/49 content |
| E8 | Visual Asset Production | **Core First Edition** | 294 visual specs exist with no produced assets. A book about structured products without diagrams is not publishable. However — see §2.3 for phased visual strategy |
| E9 | DOCX Build | **Core First Edition** | Required output format |
| E10 | PDF Build | **Core First Edition** | Required output format |
| E1 | Payoff Chart Masterclass | **Core First Edition** | Every product chapter references payoff charts. Readers need chart literacy. Gap is too visible to leave unfilled |
| E16 | Universe Map | **Core First Edition** | Single highest-impact visual. Anchors navigation. 3 days effort. No reason to exclude |
| E2 | Product Construction Lab | **First Edition Optional** | Highest educational impact score. Strong recommendation to include. But Part 5 product chapters teach construction individually — reader can learn without §1.11, just less efficiently |
| E3 | Trade Lifecycle Masterclass | **First Edition Optional** | Valuable for MO/BO readers. §2.6 provides adequate overview. §2.9 is depth, not prerequisite |
| E11 | Trade Break Library | **First Edition Optional** | High desk authenticity. Low effort (4,500 words). Pairs with E3 — if E3 included, E11 should follow |
| E14 | Product DNA Atlas | **First Edition Optional** | High reference utility. But product chapters already contain all the same data — Atlas is a reformatted view, not new content |
| E15 | Comparison Matrix | **First Edition Optional** | Cross-family comparison. Valuable but derived entirely from existing chapter data |
| E4 | Solutions Manual (T1-T3) | **Companion Material** | 178,000 words. Would double the book's page count. Self-contained — reader uses it alongside the main text, not inline. Better as separate volume |
| E13 | Interview Layer (T4) | **Companion Material** | Depends on Solutions Manual. If Solutions Manual is companion, Interview Layer ships with it |
| E12 | Payoff Chart Creation | **Digital Supplement** | Already deferred. Creation workflows (Excel/Python/Figma) are best delivered with downloadable templates, interactive notebooks. Print adds little value |

### 1.3 Summary

| Category | Count | Enhancements |
|----------|:-----:|:-------------|
| Core First Edition | 8 | E1, E5, E6, E7, E8, E9, E10, E16 |
| First Edition Optional | 5 | E2, E3, E11, E14, E15 |
| Companion Material | 2 | E4, E13 |
| Digital Supplement | 1 | E12 |
| Volume 2 | 0 | — |

---

## Phase 2: Page Count Optimization

### 2.1 Current Estimates

| Component | Words | Pages (est.) |
|-----------|:-----:|:------------:|
| Existing manuscript (49/49 post-harmonization) | ~185,000 | ~400 |
| Core First Edition additions (E1, E5, E7, E16) | ~11,500 | ~35 |
| Visual assets (E8) — space allocation | — | ~50 (visual pages) |
| First Edition Optional (E2, E3, E11, E14, E15) | ~33,250 | ~95 |
| **First Edition total (Core only)** | **~196,500** | **~485** |
| **First Edition total (Core + Optional)** | **~229,750** | **~580** |
| Companion (E4 + E13) | ~199,400 | ~440 |

### 2.2 Target Page Counts

| Target | Pages | Rationale |
|--------|:-----:|-----------|
| **Ideal** | 500-550 | Professional reference standard. Manageable physical weight. Complete without bloat |
| **Acceptable** | 550-650 | Includes most Optional enhancements. Still a single-volume reference |
| **Maximum** | 700 | Beyond this, physical usability degrades. Binding stress. Reader intimidation. Split into volumes |

### 2.3 Recommended: 550 Pages

Core First Edition (485 pages) + selected Optional enhancements:

| Include | Enhancement | Added Pages | Running Total |
|:-------:|------------|:-----------:|:-------------:|
| ✓ | Core (E1, E5, E6, E7, E8, E9, E10, E16) | 485 | 485 |
| ✓ | E2: Product Construction Lab | +12 | 497 |
| ✓ | E14: Product DNA Atlas | +49 | 546 |
| — | E3: Trade Lifecycle Masterclass | +16 | (562) |
| — | E11: Trade Break Library | +12 | (574) |
| — | E15: Comparison Matrix | +12 | (586) |

**At 550 target:** Include E2 (Construction Lab) and E14 (DNA Atlas). These two have highest reader value among Optional enhancements.

**E3, E11, E15 move to Companion Volume** alongside Solutions Manual. Trade Lifecycle Masterclass and Trade Break Library are operationally-focused — they complement the Solutions Manual's assessment focus. Comparison Matrix is reference material — fits with DNA Atlas but can ship separately.

### 2.4 Visual Asset Strategy

294 registered visual specs is the total inventory. Not all need to be in first edition print.

| Tier | Count | First Edition Treatment |
|:----:|:-----:|------------------------|
| Tier 1 (P1 core) | ~98 | **All produced.** Essential for comprehension |
| Tier 2 (P2 supporting) | ~98 | **50% produced.** Prioritize chapters with highest complexity |
| Tier 3 (P3 reference) | ~98 | **25% produced.** Nice-to-have. Remainder in digital supplement |

**Practical first edition visual count: ~170 produced assets** (98 + 49 + 25). Reduces visual production from 45 days to ~28 days.

---

## Phase 3: Solutions Manual Strategy

### 3.1 Options

| Option | Location | Words in Main Book | Pros | Cons |
|:------:|----------|:------------------:|------|------|
| A | Inside Desk Bible (Part 7) | +199,400 | One book, complete package | ~440 extra pages. Book becomes 950+ pages. Physically unwieldy |
| B | Companion Volume | 0 | Main book stays lean. Solutions Manual gets own spine, own ToC | Reader needs two books open simultaneously |
| C | Digital-only | 0 | Zero print cost. Searchable. Updatable. Hyperlinked to chapters | Readers without devices lose access. Perceived as incomplete |
| D | Hybrid: Summary in main + full in companion | +15,000 (~30 pages) | Main book has Tier 1 answers. Full answers in companion | Duplication. Maintenance burden |

### 3.2 Assessment

| Criterion | A (Inside) | B (Companion) | C (Digital) | D (Hybrid) |
|-----------|:----------:|:-------------:|:-----------:|:----------:|
| Usability | LOW — too heavy | HIGH — dedicated reference | MEDIUM — device-dependent | MEDIUM — split attention |
| Publication impact | LOW — inflated page count | HIGH — two-volume professional set | MEDIUM — feels incomplete | MEDIUM — complex |
| Maintenance | HIGH — full reprint for any answer fix | MEDIUM — reprint companion only | LOW — update file | HIGH — two copies to maintain |
| Reader perception | Mixed — complete but intimidating | HIGH — professional, like CFA study guides | Mixed — some readers prefer print | Confusing |
| Cost | HIGH — large print run | MEDIUM — smaller companion volume | LOW | MEDIUM |

### 3.3 Recommendation: **Option B — Companion Volume**

**"Desk Bible v2"** (main, ~550 pages) + **"Desk Bible v2: Solutions & Interview Preparation"** (companion, ~470 pages)

Rationale:
- Main book stays at professional reference size
- Companion is self-contained assessment tool
- Two-volume set is standard for professional education (cf. CFA, FRM, Schweser)
- Companion can be purchased separately (revenue opportunity)
- Interview Layer (E13) ships with Solutions Manual — natural pairing
- E3, E11, E15 move to companion as "Advanced Reference" section — operational content that complements assessment focus

---

## Phase 4: Interview Preparation Strategy

### 4.1 Options

| Option | Placement | Pros | Cons |
|:------:|-----------|------|------|
| A | Inside Solutions Manual (Tier 4 after Tier 3 per question) | Natural flow. Reader sees all tiers together | 213 Tier 4 entries distributed across 482 questions — hard to use as standalone interview prep |
| B | Standalone appendix in companion | Compilable into separate prep booklet | Separated from Tier 1-3 context |
| C | Both: inline + compiled §7.10 | Best of both worlds | ~15 pages duplication |
| D | Standalone interview handbook | Own spine. Maximum portability | Third volume — excessive |

### 4.2 Recommendation: **Option C — Both Inline + Compiled**

- Tier 4 appears inline after Tier 3 for each applicable question (reader sees full progression)
- §7.10 compiles the 49 best interview answers (one per product) + 10 cross-product answers into a standalone quick-reference section
- §7.10 is ~15 pages — acceptable duplication for the usability gain
- Reader preparing for interviews goes straight to §7.10. Reader studying a specific product reads T1→T2→T3→T4 inline

---

## Phase 5: Product DNA Atlas Strategy

### 5.1 Options

| Option | Placement | Pros | Cons |
|:------:|-----------|------|------|
| A | Part 6 inside main book | Integrated. One book to carry | 49 pages. Adds to page count |
| B | Appendix A | Visually separated from chapters. Reader knows it's reference, not learning | Appendices feel secondary |
| C | Detachable desk reference (perforated/pull-out) | Physical utility — pin to desk or cubicle wall | Production complexity. Cost |
| D | Standalone handbook | Maximum portability. Pocket-sized | Third+ publication. Over-engineered |

### 5.2 Recommendation: **Option A — Part 6 inside main book**

Rationale:
- 49 pages fits within 550-page target
- DNA Atlas is the #1 reason readers pick up the book for quick reference
- Placing it as Part 6 (after product chapters, before appendices) gives it prominent position
- Each card references back to the full chapter — navigation is seamless
- Physical desk reference use case served by Universe Map poster (produced separately) rather than detachable cards

**Layout optimization:** Cards print 2-per-page for simpler products (complexity ≤ 4). Full-page for complex products (complexity ≥ 5). Reduces from 49 to ~35 pages.

---

## Phase 6: Final Publication Recommendation

### 6.1 Recommended Structure

**Publication: Two-Volume Set**

---

**VOLUME 1: Desk Bible v2 — The Complete Guide to Structured Products**

~550 pages. Single spine.

```
FRONT MATTER (~25 pages)
├── Reader Guide: How to Use This Book
├── Learning Paths (7 role-based + 4 complexity-based)
├── Universe Map (full-page, Periodic Table layout)
├── Complexity Scale Visual
├── Visual Legend
└── Table of Contents

PART 1 — BUILDING BLOCKS (~120 pages)
├── 1.1  Core Trading Concepts
├── 1.2  Options From Zero
├── 1.3  Barriers and Digitals
├── 1.4  Greeks
├── 1.5  Volatility
├── 1.6  Correlation and Baskets
├── 1.7  Yield Curves, Spot Rates, and Forward Rates
├── 1.8  Benchmark Rates, Swaps, and Rate Options
├── 1.9  Credit Risk
├── 1.10 Payoff Charts (NEW — reading skills)
└── 1.11 Product Construction Lab (NEW — 8 builds)

PART 2 — THE DESK (~40 pages)
├── 2.1  What Is a Structured Product?
├── 2.2  Product Construction Principles
├── 2.3  The Four-Leg Framework
├── 2.4  Capital Protection Spectrum
├── 2.5  Product Lifecycle
├── 2.6  Trade Lifecycle
├── 2.7  How Desks Hedge
└── 2.8  The Systems: A First Look

PART 3 — PRODUCT MAPS (~15 pages)

PART 4 — GLOSSARY & ACRONYMS (~15 pages, refreshed)

PART 5 — PRODUCTS (~270 pages, 49 chapters harmonized)
├── 5.1  ELN Family (15)
├── 5.2  Swaps Family (8)
├── 5.3  SRT Family (5)
├── 5.4  STEG Family (4)
├── 5.5  CLN Family (5)
└── 5.6  Other Family (7)

PART 6 — PRODUCT DNA ATLAS (~35 pages, NEW)
├── 6.1  ELN Cards (15)
├── 6.2  Swaps Cards (8)
├── 6.3  SRT Cards (5)
├── 6.4  STEG Cards (4)
├── 6.5  CLN Cards (5)
└── 6.6  Other Cards (7)

BACK MATTER
├── Complexity Index (sorted)
├── Capital Protection Index (sorted)
└── Alphabetical Index

~170 visual assets (all Tier 1 + selective Tier 2/3)
```

---

**VOLUME 2: Desk Bible v2 — Solutions, Interview Preparation & Advanced Reference**

~470 pages. Separate spine. Can be sold separately.

```
FRONT MATTER
├── How to Use This Companion
├── Cross-reference to Volume 1
└── Answer Structure Guide (Tier 1-4 explained)

PART 7 — SOLUTIONS MANUAL (~400 pages)
├── 7.1  How to Use Solutions
├── 7.2  Foundation Section Solutions (Parts 0-4)
├── 7.3  ELN Family Solutions (15 products, T1-T4)
├── 7.4  Swaps Family Solutions (8 products, T1-T4)
├── 7.5  SRT Family Solutions (5 products, T1-T4)
├── 7.6  STEG Family Solutions (4 products, T1-T4)
├── 7.7  CLN Family Solutions (5 products, T1-T4)
├── 7.8  Other Family Solutions (7 products, T1-T4)
├── 7.9  Cross-Product Integration Questions
└── 7.10 Interview Quick Reference (Top 49 + 10 cross-product)

PART 8 — ADVANCED REFERENCE (~55 pages)
├── 8.1  Trade Lifecycle Masterclass
├── 8.2  Trade Break Case Study Library (8 cases)
└── 8.3  Product Comparison Matrix (49×10)

BACK MATTER
├── Cross-reference index to Volume 1
└── Question index by topic
```

---

**DIGITAL SUPPLEMENT (downloadable)**

```
├── Payoff Chart Creation Toolkit
│   ├── Excel template with formulas
│   ├── Python scripts + matplotlib style sheet
│   ├── SVG templates
│   └── Tutorial notebook
│
├── Visual Assets (full resolution)
│   ├── All Tier 1, 2, 3 visuals as SVG/PNG
│   └── Figma source file (view-only link)
│
├── Universe Map (printable poster, A2/A1)
│
├── DNA Atlas (printable cards, A5)
│
└── Comparison Matrix (interactive, sortable/filterable)
```

---

### 6.2 Page Count Summary

| Volume | Pages | Words |
|--------|:-----:|:-----:|
| Volume 1 (Main) | ~550 | ~210,000 |
| Volume 2 (Companion) | ~470 | ~210,000 |
| **Print total** | **~1,020** | **~420,000** |
| Digital supplement | N/A | ~5,000 + templates |

### 6.3 Volume Count

**Two physical volumes + one digital package.**

This is the standard model for professional financial education:
- CFA Institute: Curriculum (6 volumes) + Practice Problems (separate)
- FRM: Foundations (1 volume) + Practice Exams (1 volume)
- Hull's Options textbook: Main text + Solutions Manual (separate)

Two volumes is the minimum split that achieves readable book size. Three or more volumes fragments the reader experience unnecessarily.

### 6.4 Production Timeline Impact

| Phase | V1 Original (84d) | Two-Volume (revised) |
|:-----:|:------------------:|:--------------------:|
| Phase 1: Harmonization | 15d | 15d (unchanged) |
| Phase 2: Content | 12d | 7d (E3, E11 moved to V2) |
| Phase 3: Reference | 12d | 8d (E15 moved to V2) |
| Phase 4: Navigation | 5d | 5d (unchanged) |
| Phase 5: Solutions Manual | 26d | 26d (moved to V2 track) |
| Phase 6: Visuals | 45d → 28d | 28d (reduced to ~170 assets) |
| Phase 7: Publication build | 14d | 14d V1 + 7d V2 |

**Volume 1 critical path: 15 + 7 + 8 + 5 + 14 = 49 days**
**Volume 2 critical path: starts Phase 2 parallel, 26 + 7 = 33 days (fits within V1 timeline)**

**Net: Volume 1 ships in ~49 days. Volume 2 ships in ~55 days.** Both shorter than original 84-day single-volume plan because:
1. Visual production reduced (170 vs 294)
2. Content phases trimmed (E3, E11, E15 moved out of critical path)
3. V2 production runs parallel to V1 Phases 3-5

### 6.5 Answer: "If publishing today, what exact structure would you choose?"

**Two-volume set.**

Volume 1: 550 pages. All building blocks, all 49 products, DNA Atlas, front matter, Universe Map, payoff chart literacy, construction lab. Everything a reader needs to learn and reference structured products.

Volume 2: 470 pages. Every answer to every question. Interview preparation. Trade lifecycle deep dive. Trade break case studies. Comparison matrix. Everything a reader needs to test themselves, prepare for interviews, and develop operational expertise.

Digital supplement: Creation toolkit, full-resolution visuals, printable poster, interactive comparison matrix.

This structure optimizes for:
- **Educational value:** V1 teaches completely. V2 assesses completely.
- **Publication quality:** Both volumes at professional reference size.
- **Reader usability:** V1 is self-contained. V2 is optional but valuable.
- **Production effort:** V1 ships 35 days faster than monolithic plan.
- **Maintainability:** Answers (V2) updated independently from content (V1).

---

*First Edition Scope Review completed 2026-06-21.*
*Recommendation: Two-volume set + digital supplement.*
*Volume 1: ~550 pages, 49 days to release.*
*Volume 2: ~470 pages, 55 days to release.*
