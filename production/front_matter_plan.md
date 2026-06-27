# Front Matter Architecture

**Version:** 1.0
**Date:** 2026-06-21
**Authority:** Framework Master v1.3.1 (FROZEN)
**Scope:** Pre-chapter publication content for Desk Bible v2
**Purpose:** Design reader-facing navigation, orientation, and reference systems
**Implementation:** During harmonization pass (after 49/49)

---

## 1. Reader Guide — "How to Use This Book"

### 1.1 Purpose

First content the reader encounters. Orients them to the book's structure, conventions, and assumptions. Answers: "Where do I start? How do I find what I need? What should I skip?"

### 1.2 Sections

| Section | Content | Length |
|---------|---------|:------:|
| **Who This Book Is For** | Desk analysts, traders, structurers, risk managers, sales, operations, product control, compliance. Assumes basic financial literacy (bonds, equities, options). Does NOT assume structured products knowledge | 150 words |
| **How This Book Is Organized** | Parts 0-4 (foundations) → Part 5 (products by family). Each product chapter follows identical 22-section template. Foundation sections teach concepts; product chapters apply them | 200 words |
| **How to Read a Product Chapter** | Walk through §1-§22. §1 = start here. §9 = three scenarios. §11 = formal definition. §14 = desk reality. §18 = worked example. §19 = knowledge check. §21 = visual specs | 250 words |
| **Conventions Used** | Bold for key terms at first use. Tables for structured comparisons. "Dependency References" at end of every chapter. Visual specifications describe figures not yet rendered. Complexity score 1-10 on every product | 150 words |
| **What This Book Is NOT** | Not a pricing manual. Not a risk management textbook. Not legal or compliance guidance. Not a substitute for product-specific training. IS a desk-level operational and conceptual reference | 100 words |

**Total:** ~850 words

---

## 2. Learning Paths

### 2.1 Role-Based Paths

Seven paths, each providing a recommended reading order tailored to a specific desk role.

| Path | Target Reader | Entry Point | Core Chapters | Focus Sections per Chapter |
|------|--------------|-------------|:-------------:|---------------------------|
| **Beginner** | New joiner, intern | Parts 0-2 (all) | PPN → RC → IRS → CLN → DRC → KODRC → then by complexity | §1, §2, §9, §19 |
| **Desk Analyst** | Junior analyst, 0-2 years | Part 1-2 (selective) | All 49 by family | §1, §9, §11, §14, §18 |
| **Trader** | Execution, hedging | Part 1 (barriers, Greeks, correlation) | Focus on §7, §10, §14, §15 across all products | §7 (Bank Revenue), §10 (Market Moves), §14 (Desk Reality), §15 (Risk) |
| **Structurer** | Product design | Parts 1-2 (all) | All 49 — §4 (DNA), §6 (Evolution), §8 (Client), §12 (Construction) | §4, §6, §8, §12 |
| **Risk Manager** | Risk oversight | Part 1 (risk concepts) | All 49 — focus on §15, §17 | §15 (Risk Analysis), §17 (Red Flags), §10 (Market Moves) |
| **Sales** | Client-facing | Part 0 (overview) | All 49 — §1, §2, §3, §8, §9 | §1 (ELI5), §2 (Analogy), §3 (Problem), §8 (Client), §9 (Scenarios) |
| **Operations** | Settlement, booking | Part 2 (systems, booking) | All 49 — §13, §16, §17 | §13 (Lifecycle), §16 (Booking), §17 (Red Flags) |

### 2.2 Complexity-Based Paths

Four tiers for self-directed readers.

| Path | Complexity Range | Products | Recommended For |
|------|:----------------:|:--------:|----------------|
| **Path A: Foundations** | 1-3 | PPN (2), VLSP (2), RC (3), IRS (3), DRC (3), ICN (3), Warrant (3) — 7 products | Absolute beginners. Master these before anything else |
| **Path B: Intermediate** | 4-5 | KODRC (4), Airbag (4), Bonus (4), Digital (4), Booster (4), CLN (4), Commodity (4), ZCL (4), CRC (5), TRS (5), Equity Swap (5), CDS (5), CCY Swap (5), IR Callable (5), Digital CF (5), Vanilla STEG (5), Skew CLN (5) — 17 products | Comfortable with Path A. Ready for multi-component products |
| **Path C: Advanced** | 6-7 | Phoenix (6), FCN (6), CRA ELN (6), NCRA (6), Callable STEG (6), Digital KI Put (7), Variance Swap (7), CRA SRT (7), RA STEG (7), FTD (7) — 10 products | Experienced. Path dependency, multi-factor, correlation |
| **Path D: Expert** | 8-10 | TARN STEG (8), NTD (8), Synthetic CDO (10) — 3 products | Specialist. Non-monotonic behavior, tranching, portfolio modeling |

### 2.3 Path Presentation Format

Each path rendered as:
1. **Title and audience** (1 sentence)
2. **Prerequisites** (which paths or sections to complete first)
3. **Reading order** (numbered list of chapters)
4. **Focus sections** (which §§ to prioritize)
5. **Estimated time** (total hours)
6. **"Must-read" highlights** (3-5 specific sections/paragraphs that carry disproportionate teaching value)

---

## 3. Complexity Scale

### 3.1 Scale Definition

Visual one-pager showing the 1-10 scale with anchor products.

| Score | Label | Anchor Product | What It Means |
|:-----:|-------|---------------|--------------|
| 1 | Trivial | — | Single cash flow, no optionality |
| 2 | Simple | PPN, VLSP | Bond + one derivative component. One payoff scenario |
| 3 | Basic | RC, IRS | One barrier or one swap leg. Two outcomes |
| 4 | Standard | KODRC, CLN | Two interacting features (e.g., barrier + credit). Multiple outcomes |
| 5 | Moderate | CRC, CDS | Callable/puttable or multi-party structure. Requires cross-product knowledge |
| 6 | Intermediate | Phoenix, FCN | Path dependency or autocallable. Multi-observation |
| 7 | Advanced | Digital KI Put, FTD | Three+ interacting features. Non-obvious risk profiles. Correlation |
| 8 | Complex | TARN STEG, NTD | Non-monotonic or path-dependent behavior. Target mechanisms |
| 9 | Very Complex | — | Reserved for multi-portfolio products |
| 10 | Maximum | Synthetic CDO | Portfolio-level modeling. Tranching. Model-dependent. Historical crisis relevance |

### 3.2 Visual Design

Horizontal bar with gradient from green (1) to red (10). Anchor products labeled at their positions. Reader can locate any product on the scale instantly.

**Visual asset:** `FIG-FM-01` — Complexity Scale (Tier 1, front matter)

---

## 4. Product Dependency Map

### 4.1 Purpose

Shows which products must be understood before tackling others. Prevents readers from jumping to Synthetic CDO without understanding CDS → CLN → FTD → NTD.

### 4.2 Structure

Directed acyclic graph (DAG) with products as nodes and prerequisite relationships as edges.

**Key dependency chains:**

```
Foundations (Parts 0-2)
    │
    ├── ELN Family
    │   PPN → RC → DRC → KODRC → CRC
    │              → Airbag → Bonus
    │              → Phoenix → FCN
    │              → Digital → Digital KI Put
    │              → Booster
    │              → ICN
    │              → CRA ELN
    │              → Warrant
    │
    ├── Swap Family
    │   IRS → TRS → Equity Swap
    │       → Variance Swap
    │       → CDS ─────────────────────┐
    │       → CCY Swap                 │
    │       → Commodity Swap           │
    │       → VLSP                     │
    │                                  │
    ├── SRT Family                     │
    │   VLSP → IR Callable → ZCL      │
    │                      → NCRA → CRA SRT
    │                      → Digital CF│
    │                                  │
    ├── STEG Family                    │
    │   VLSP → Vanilla STEG → RA STEG │
    │                       → Callable STEG
    │                       → TARN STEG│
    │                                  │
    └── CLN Family                     │
        CDS + CLN → Skew CLN ─────────┘
                  → FTD → NTD → Synthetic CDO
    
    Other Family
        PPN → Structured Deposit
        Forwards → Forward
        Options → Vanilla Options → ELO → Option on RC
        Forward + Barrier → Accumulator → Decumulator
```

### 4.3 Visual Design

Full-page DAG with color-coded family clusters. Arrows show prerequisites. Complexity score displayed inside each node.

**Visual asset:** `FIG-FM-02` — Product Dependency Map (Tier 1, front matter)

---

## 5. Role-Based Navigation Table

### 5.1 Purpose

Quick-reference matrix. Reader finds their role on one axis, their question on the other, and gets the exact section reference.

### 5.2 Structure

| Question | Trader | Structurer | Sales | Risk | Operations |
|----------|--------|-----------|-------|------|-----------|
| "How does the bank make money?" | §7 | §7 | §7 | §7 | — |
| "What are the risks?" | §15 | §15 | — | §15 | §17 |
| "How is it booked?" | — | — | — | — | §16 |
| "What can go wrong?" | §17 | §17 | §17 | §17 | §17 |
| "How do I explain it to a client?" | — | — | §1, §2 | — | — |
| "What moves the P&L?" | §10 | §10 | — | §10 | — |
| "Walk me through a real trade" | §18 | §18 | §9 | §18 | §13 |

### 5.3 Implementation

Print as fold-out reference card or bookmark insert. Also rendered as table in front matter.

---

## 6. Glossary Navigation

### 6.1 Purpose

238 glossary terms organized for fast lookup. Three access methods:

### 6.2 Access Methods

| Method | How | Best For |
|--------|-----|----------|
| **Alphabetical** | Standard A-Z listing | "I know the term, need the definition" |
| **By Category** | 12 categories (Markets, Bonds, Equities, Options, Volatility, Correlation, Rates, Credit, Structured Products, Operations, Systems, Risk) | "I'm studying credit — show me all credit terms" |
| **By Chapter** | Terms grouped by the chapter where first introduced | "I'm reading FTD — what terms will I encounter?" |

### 6.3 Glossary Entry Format

Each term has:
- **Term** (bold)
- **Plain English definition** (1-2 sentences, no jargon)
- **Professional definition** (precise, may use other defined terms)
- **First introduced** (section reference)
- **Category** (one of 12)

---

## 7. Visual Legend

### 7.1 Purpose

One-page reference explaining all visual conventions used throughout the book.

### 7.2 Contents

| Element | Convention | Meaning |
|---------|-----------|---------|
| Blue line/fill | `#2563EB` | Positive value, investor gain, inflow |
| Red line/fill | `#DC2626` | Negative value, loss, risk, outflow |
| Amber highlight | `#D97706` | Warning, threshold, conditional |
| Teal | `#0D9488` | Secondary positive, alternative path |
| Gray | `#6B7280` | Neutral, reference level, inactive |
| Solid line | — | Actual/realized path |
| Dashed line | — | Theoretical/potential path |
| Dotted line | — | Barrier level / threshold |
| Arrow (single) | → | Cash flow direction |
| Arrow (double) | ⇄ | Two-way exchange |
| Diamond | ◇ | Decision point |
| Circle (filled) | ● | Event marker (credit event, observation date) |
| Circle (hollow) | ○ | Non-event / no trigger |
| Shaded band | Colored region | Tranche, range, or zone |

### 7.3 Visual Asset

**Visual asset:** `FIG-FM-03` — Visual Legend (Tier 1, front matter)

---

## 8. Front Matter Page Budget

| Component | Pages (est.) | Visual Assets |
|-----------|:------------:|:-------------:|
| Reader Guide | 2 | 0 |
| Learning Paths (role-based) | 3 | 1 (path diagram) |
| Learning Paths (complexity-based) | 1 | 0 |
| Complexity Scale | 1 | 1 (FIG-FM-01) |
| Product Dependency Map | 1 | 1 (FIG-FM-02) |
| Role-Based Navigation | 1 | 0 (table only) |
| Glossary Navigation | 1 (intro) + 12 (glossary) | 0 |
| Visual Legend | 1 | 1 (FIG-FM-03) |
| Table of Contents | 2 | 0 |
| **Total front matter** | **~25 pages** | **4 visual assets** |

---

## 9. Implementation Sequence

| Step | When | Deliverable |
|:----:|------|------------|
| 1 | After 49/49 | Draft all text sections |
| 2 | After step 1 | Generate FIG-FM-01 through FIG-FM-04 |
| 3 | After harmonization | Finalize glossary navigation (depends on glossary metadata update) |
| 4 | After visual production | Finalize visual legend (depends on final color palette confirmation) |
| 5 | After all content final | Generate Table of Contents |

---

*Front Matter Architecture v1.0. Effective 2026-06-21. Implementation deferred to harmonization pass after 49/49.*
