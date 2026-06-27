# Structured Products Universe Map — Design Review

**Date:** 2026-06-21
**Proposed Placement:** Front Matter (FIG-FM-02) + standalone poster
**Framework:** v1.3.1 (FROZEN)
**Purpose:** Single visual showing all 49 products and their relationships
**Implementation:** After 49/49, during front matter production

---

## 1. Concept

A single-page visual map showing all 49 products, organized by family, with visual indicators for complexity, dependencies, and learning progression. The reader's "you are here" reference — at any point in the book, look at the map to see where this product sits relative to everything else.

**What it replaces:** Currently no single visual shows the complete product universe. Readers must piece together the structure from Part 3 (Product Maps), the table of contents, and the complexity registry.

---

## 2. Visual Architecture

### 2.1 Layout: Solar System Model

Each family = an orbital ring. Complexity increases from center to edge.

```
                        ┌─ Other ─────────────────────┐
                     ┌──┤ CLN ────────────────────┐    │
                  ┌──┤  │ STEG ──────────────┐    │    │
               ┌──┤  │  │ SRT ──────────┐    │    │    │
            ┌──┤  │  │  │ Swaps ───┐    │    │    │    │
         ┌──┤  │  │  │  │ ELN ┐    │    │    │    │    │
         │  │  │  │  │  │     │    │    │    │    │    │
    C=1  │  │  │  │  │  │ PPN │IRS │    │    │VC  │SD  │
    C=2  │  │  │  │  │  │VLSP │    │    │    │    │Fwd │
    C=3  │  │  │  │  │  │ RC  │CMS │    │    │    │VO  │
    C=4  │  │  │  │  │  │ BC  │IAS │TRS │    │VCLN│    │
    C=5  │  │  │  │  │  │ SF  │CS  │CRT │NCRA│SKCL│ORC │
    C=6  │  │  │  │  │  │Phx  │XCS │    │RA  │    │Acc │
    C=7  │  │  │  │  │  │WoAC │    │    │CSTG│FTD │    │
    C=8  │  │  │  │  │  │TARN │    │    │    │NTD │    │
    C=9  │  │  │  │  │  │     │    │    │    │    │    │
    C=10 │  │  │  │  │  │     │    │    │    │SCDO│    │
         └──┘  └──┘  └──┘     └────┘    └────┘    └────┘
```

### 2.2 Alternative Layout: Periodic Table Model

Products arranged in a grid. Rows = complexity level. Columns = family. Each cell = one product "element."

```
         ELN      Swaps    SRT     STEG    CLN     Other
    ┌────────────────────────────────────────────────────┐
C=2 │ PPN  VLSP │        │       │       │       │SD Fwd│
C=3 │ RC   BC   │IRS CMS │       │       │       │VO ELO│
C=4 │ DRC  SF   │IAS     │TRS    │       │VCLN   │      │
C=5 │ BRC  FCN  │CS      │CRT    │NCRA   │SKCLN  │ORC   │
C=6 │ Phx  AC   │XCS     │       │RA CSTG│       │Ac Dc │
C=7 │ WoAC TARN │        │       │       │FTD    │      │
C=8 │           │        │       │       │NTD    │      │
C=10│           │        │       │       │SCDO   │      │
    └────────────────────────────────────────────────────┘
```

### 2.3 Recommended: Hybrid — Solar System for poster, Periodic Table for print

| Format | Layout | Reason |
|--------|--------|--------|
| Front matter (print) | Periodic Table | Fits standard page width. Clean grid |
| Poster/wall reference | Solar System | More visually engaging. Shows relationships spatially |
| Digital/interactive | Either | Clickable to product chapter |

---

## 3. Information Layers

### 3.1 Primary Layer — Position and Family

Every product placed in its family column and complexity row. Family color-coded (same palette as DNA Atlas badges).

### 3.2 Secondary Layer — Dependency Arrows

Thin arrows showing "Product A builds on Product B":

| Arrow | Meaning | Example |
|-------|---------|---------|
| → | "Extends" | RC → Phoenix (adds autocall) |
| → | "Complexifies" | CLN → FTD (adds basket) |
| → | "Mirrors" | Accumulator → Decumulator |
| ⋯ | "Related" | PPN ⋯ Structured Deposit |

**Key dependency chains:**

```
PPN → RC → Phoenix → Worst-of AC → TARN
                  └→ Athena
                  └→ Twin-Win

IRS → CMS Swap → Cross-Currency Swap

TRS → CRT

CLN → Skew CLN
  └→ FTD → NTD → Synthetic CDO

Forward → Accumulator → Decumulator
```

### 3.3 Tertiary Layer — Complexity Gradient

Background shading from light (C=1-3) to dark (C=8-10). Gives instant visual sense of complexity landscape.

### 3.4 Quaternary Layer — Learning Path Annotations

Dotted path lines showing recommended reading sequences (from front matter learning paths). Beginner path highlighted. Advanced path highlighted differently.

---

## 4. Navigation Role

| Context | How Map Is Used |
|---------|----------------|
| **Starting the book** | Reader sees full landscape. Plans reading path |
| **During a chapter** | "Where does this product sit?" Quick orientation |
| **Comparing products** | Visual proximity shows family relationships |
| **Interview prep** | "Name 5 products with complexity > 7" — glance at map |
| **Desk reference** | Wall poster — always visible |

---

## 5. Publication Placement

| Location | Format | Purpose |
|----------|--------|---------|
| Front matter (after Reader Guide) | Full page, Periodic Table | Primary navigation aid |
| Part 3 opener | Smaller version with Part 3 annotations | Product Maps context |
| Part 5 opener | Smaller version highlighting current family | Family context |
| Standalone poster | Large format, Solar System | Wall reference |
| Back cover (inside) | Simplified version | Quick reference |

---

## 6. Visual Requirements

| # | Visual | Type | Tool | Size |
|:-:|--------|------|------|------|
| 1 | Universe Map — Periodic Table (full) | Infographic | Figma | Full page |
| 2 | Universe Map — Solar System (poster) | Infographic | Figma | A2/A1 poster |
| 3 | Dependency arrow overlay | Overlay | Figma | Same as #1 |
| 4 | Learning path overlay (beginner) | Overlay | Figma | Same as #1 |
| 5 | Learning path overlay (advanced) | Overlay | Figma | Same as #1 |
| 6 | Family color legend | Legend | Figma | Small inset |

**Total: 6 visual assets (2 base maps + 3 overlays + 1 legend).**

**Production note:** Base map (#1) is the Figma master component. All overlays are layers on the same file. Poster version (#2) is a scaled variant with additional decorative elements.

---

## 7. Maintenance

| Trigger | Action |
|---------|--------|
| New product | Add cell to grid. Update arrows. Regenerate |
| Complexity revised | Move cell to new row. Update gradient |
| Family reclassified | Move cell to new column |
| Learning path changed | Update overlay |

**Effort per update: ~1 hour.** Figma component-based — move, don't rebuild.

---

## 8. Estimates

| Metric | Value |
|--------|:-----:|
| Visual assets | 6 |
| Text content | ~500 words (legend, annotations) |
| Pages (print) | 2-3 (full page map + legend page + dependency page) |
| Poster | 1 (A2 or A1) |
| Effort | 3 days (design + data placement + overlays) |
| Figma complexity | MEDIUM — 49 positioned elements + arrows + overlays |

---

## 9. Assessment

| Criterion | Score |
|-----------|:-----:|
| Educational impact | HIGH — instant spatial understanding of product universe |
| Effort | LOW-MEDIUM — one visual, data-driven placement |
| Publication value | VERY HIGH — signature visual, cover-worthy |
| Reader value | VERY HIGH — most-referenced single page in the book |
| Risk | LOW — derived from existing data, no content modifications |

**Recommendation: PROCEED.** Highest-impact single visual asset in the entire book. Implement during front matter production.

---

*Structured Products Universe Map Design Review completed 2026-06-21.*
