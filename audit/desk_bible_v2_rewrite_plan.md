# Desk Bible v2 — Rewrite Plan

**Date:** 2026-06-19
**Status:** PLANNING — awaiting approval before any rewrite work begins.

---

## Action Key

| Action | Meaning |
|--------|---------|
| **KEEP** | Content is good. Restructure into V2 format with minimal editing. |
| **MERGE** | Combine content from multiple sources into a single V2 section. |
| **REWRITE** | Content exists but must be substantially rewritten for V2 objectives. |
| **DELETE** | Content is redundant and should not appear in V2. |
| **CREATE NEW** | No content exists. Must be written from scratch. |

---

## Effort Estimation Key

| Effort | Meaning |
|--------|---------|
| S | Small — under 2 pages, straightforward adaptation |
| M | Medium — 2–5 pages, requires synthesis from multiple sources |
| L | Large — 5–10 pages, significant original writing |
| XL | Extra Large — 10+ pages, complex original content |

---

## PART 1 — FOUNDATIONS

| Section | Action | Source(s) | Effort | Est. Pages | Notes |
|---------|--------|-----------|:------:|:----------:|-------|
| 1.1 Core Trading Concepts | MERGE | SP.docx A.1–A.3, B.1–B.2, B.14–B.15, B.18; COMPLETE Part 1.1 | M | 4–5 | Adapt SP.docx conversational tone. Add Price vs Value vs MtM. |
| 1.2 Options From Zero | MERGE | SP.docx A.2, A.6; COMPLETE Part 1.2 | M | 4–5 | Add ITM/ATM/OTM, exercise styles (European/American/Bermudan), intrinsic/time value. Payoff diagrams needed. |
| 1.3 Barriers and Digitals | MERGE | SP.docx A.6, C.18.1; COMPLETE Part 1.2 | M | 3–4 | Separate from options basics. KI/KO mechanics, observation types, digital payoffs. Diagrams critical. |
| 1.4 Greeks | MERGE | SP.docx B.5–B.10; COMPLETE Part 1.3 | M | 4–5 | Adapt SP.docx from-zero tone. Add Rho. Linear vs non-linear. Sensitivity charts needed. |
| 1.5 Volatility | MERGE | SP.docx B.3–B.4; COMPLETE Part 1.4 | M | 3–4 | Add vol term structure and skew/smile with visual. |
| 1.6 Correlation and Baskets | MERGE | SP.docx B.20–B.21, B.24; COMPLETE Part 1.5 | S | 2–3 | Correlation, worst-of/best-of, tail risk. |
| 1.7 Rates and Yield Curves | MERGE | SP.docx C.1–C.5; COMPLETE Part 4.1 | M | 4–5 | Add SOFR/EURIBOR benchmark transition. CMS rates. Caps/floors/swaptions. |
| 1.8 Credit Risk | MERGE | SP.docx B.22–B.23, Section 35, K; COMPLETE Part 6.1, 6.3 | M | 3–4 | Credit spread, recovery, CDS basics, ISDA credit events. Model risk. |

**Part 1 Total:** 27–35 pages | **Total Effort:** 8 Medium tasks
**Duplication reduction:** N/A (new content)
**Key decision:** SP.docx has richer, more conversational explanations. COMPLETE.docx is more structured. Use SP.docx tone with COMPLETE.docx organization.

---

## PART 2 — STRUCTURED PRODUCTS FRAMEWORK

| Section | Action | Source(s) | Effort | Est. Pages | Notes |
|---------|--------|-----------|:------:|:----------:|-------|
| 2.1 What Is a Structured Product | REWRITE | SP.docx A.10; COMPLETE Part 1 (implied) | S | 2 | Currently scattered. Write a clear definition + why they exist + risk transfer concept. |
| 2.2 Product Construction | CREATE NEW | Principles scattered in V1 constructions; SP.docx D.5 | M | 3–4 | Bond + Option decomposition. Issuer credit curve. FTP. Desk margin. Extract principles from V1's 28 construction sections. |
| 2.3 Four-Leg Framework | KEEP | COMPLETE Part 2 | M | 3–4 | Excellent content. Add worked example showing flows. Diagram critical. |
| 2.4 Capital Protection Spectrum | CREATE NEW | Implicit in V1 products; not standalone anywhere | S | 2 | Full / Conditional / Zero protection. How protection drives coupon. |
| 2.5 Product Lifecycle | CREATE NEW | Not in any source | M | 3–4 | Origination → pricing → booking → observations → maturity. New content. |
| 2.6 Trade Lifecycle | CREATE NEW | Not in any source | M | 3–4 | FO → MO → Risk → Ops → ProdCon. End-to-end view. |
| 2.7 How Desks Hedge | MERGE | SP.docx Section E; COMPLETE Part 9.1 | M | 3–4 | SP.docx Section E is excellent. Adapt and add stress behavior from COMPLETE Part 9.2. |

**Part 2 Total:** 19–24 pages | **Total Effort:** 3 Create, 2 Merge, 1 Rewrite, 1 Keep
**Duplication reduction:** N/A (mostly new)
**Key decision:** Four-Leg Framework from COMPLETE.docx is the anchor. Everything else builds around it.

---

## PART 3 — PRODUCT TAXONOMY

| Section | Action | Source(s) | Effort | Est. Pages | Notes |
|---------|--------|-----------|:------:|:----------:|-------|
| 3.1 Product Family Overview | CREATE NEW | Derived from V1 catalog + master universe | S | 1–2 | One paragraph per family. |
| 3.2 Classification Dimensions | CREATE NEW | Implicit in V1 | M | 2–3 | By underlying, coupon, protection, optionality, complexity, system. |
| 3.3 ELN Family Tree | REWRITE | V1 definitions (extract and condense) | S | 1–2 | Tree/hierarchy, not prose. |
| 3.4 CLN Family Tree | REWRITE | V1 definitions (extract and condense) | S | 1 | 5 products. |
| 3.5 Swaps Family Tree | CREATE NEW | SP.docx Sections 31–35; V1 SWAP001 | S | 1–2 | 7 products. |
| 3.6 SRT Family Tree | REWRITE | V1 definitions (extract and condense) | S | 1 | 5 products. |
| 3.7 STEG Family Tree | REWRITE | V1 definitions (extract and condense) | S | 1 | 4 products. |

**Part 3 Total:** 8–12 pages | **Total Effort:** 3 Create, 4 Rewrite (all Small)
**Duplication reduction:** Replaces ~28 verbose definitions with concise taxonomy.

---

## PART 4 — PRODUCT COMPARISON MATRICES

| Section | Action | Source(s) | Effort | Est. Pages | Notes |
|---------|--------|-----------|:------:|:----------:|-------|
| 4.1 ELN Master Comparison | CREATE NEW | Extract from V1 products | M | 2–3 | 15 products × 11 columns. |
| 4.2 RC Variant Comparison | CREATE NEW | V1 RC/DRC/KODRC/CRC/Airbag | S | 1–2 | What changes between variants. |
| 4.3 Autocallable Variant Comparison | CREATE NEW | V1 Phoenix/FCN/CRAELN | S | 1 | Conditional vs fixed coupon, memory. |
| 4.4 CLN Family Comparison | CREATE NEW | V1 CLN products; COMPLETE Part 6.3 | S | 1–2 | Correlation exposure, reference type. |
| 4.5 STEG Family Comparison | MERGE | V1 STEG products; COMPLETE Part 7.3 | S | 1–2 | COMPLETE.docx 7.3 has comparison content. |
| 4.6 SRT Family Comparison | CREATE NEW | V1 SRT products | S | 1–2 | Callable vs non-callable, accreting. |
| 4.7 Swaps Comparison | CREATE NEW | SP.docx Sections 31–35 | S | 1–2 | What is exchanged, settlement, collateral. |
| 4.8 Cross-Family Comparisons | MERGE | COMPLETE Part 4.3; V1 products | M | 3–4 | ELN vs SRT, risk profiles, system routing, capital protection. |

**Part 4 Total:** 11–18 pages | **Total Effort:** 6 Create, 2 Merge (mostly Small)
**Duplication reduction:** N/A (new content, but eliminates need for per-product repetition of comparative info)

---

## PART 5 — PRODUCT DEEP DIVES

### Action Summary by Product

**ELN Family (15 products):**

| Product | V1 ID | Action | Source | Effort | Est. Pages | Notes |
|---------|-------|--------|--------|:------:|:----------:|-------|
| Reverse Convertible | RC001 | REWRITE | V1 | S | 3 | Condense 8→9 sections. Remove boilerplate. |
| Discounted RC | DRC001 | REWRITE | V1 | S | 3 | Condense. |
| Knock-Out Discounted RC | KODRC001 | REWRITE | V1 | S | 3 | Condense. Remove Broadie-Glasserman or explain it. |
| Callable RC | CRC001 | REWRITE | V1 | S | 3 | Condense. |
| Airbag / Leveraged RC | AIRBAG001 | REWRITE | V1 | S | 3 | Condense. |
| Phoenix Autocallable | PHX001 | REWRITE | V1 | S | 3–4 | Condense. Memory feature needs better explanation. |
| Fixed Coupon Note | FCN001 | REWRITE | V1 | S | 3 | Condense. |
| Callable Range Accrual ELN | CRAELN001 | REWRITE | V1 | S | 3 | Condense. |
| Bonus / Participation Note | BONUS001 | REWRITE | V1 | S | 3 | Condense. |
| Principal Protected Note | PPN001 | REWRITE | V1 | S | 3 | Condense. |
| Warrant / Turbo Certificate | WARRANT001 | REWRITE | V1 | S | 3 | Condense. |
| Issuer Callable Note | ICN001 | REWRITE | V1 | S | 3 | Condense. |
| Digital Coupon Notes | DIGITAL001 | REWRITE | V1 | S | 3 | Condense. |
| Booster Note | — | CREATE NEW | No source | M | 3–4 | New product. Research required. |
| Digital Coupon Knock-In Put | — | CREATE NEW | V1 DIGITAL001 partial | M | 3–4 | Partially covered. Expand. |

**CLN Family (5 products):**

| Product | V1 ID | Action | Source | Effort | Est. Pages | Notes |
|---------|-------|--------|--------|:------:|:----------:|-------|
| Vanilla CLN | VCLN001 | REWRITE | V1 | S | 3 | Condense. |
| Skew CLN | SCLN001 | REWRITE | V1 | S | 3 | Condense. |
| First-to-Default | FTD001 | REWRITE | V1 | S | 3–4 | Condense. Improve correlation explanation. |
| Nth-to-Default | NTD001 | REWRITE | V1 | S | 3–4 | Condense. Simplify copula discussion. |
| Synthetic CDO Tranche | TRANCHE001 | REWRITE | V1 | M | 4–5 | Needs significant simplification. Base correlation and LHP need accessible explanations. |

**Swaps Family (7 products):**

| Product | V1 ID | Action | Source | Effort | Est. Pages | Notes |
|---------|-------|--------|--------|:------:|:----------:|-------|
| Interest Rate Swap | SWAP001 | REWRITE | V1 | S | 3–4 | V1 content exists. Restructure. |
| Total Return Swap | — | CREATE NEW | SP.docx Section 31 | M | 3–4 | Content available. Adapt. |
| Equity Swap | — | CREATE NEW | SP.docx Section 32 | M | 3–4 | Content available. Adapt. |
| Cross-Currency Swap | — | CREATE NEW | SP.docx Section 33 | M | 3–4 | Content available. Adapt. |
| Commodity Swap | — | CREATE NEW | SP.docx Section 34 | S | 3 | Content available. Adapt. |
| Credit Default Swap | — | CREATE NEW | SP.docx Section 35; SP.docx K | M | 3–4 | Rich source content. Adapt. |
| Vanilla Swap (VLSP) | — | CREATE NEW | V1 SWAP001 partial | S | 3 | Derivative of IRS. |

**SRT Family (5 products):**

| Product | V1 ID | Action | Source | Effort | Est. Pages | Notes |
|---------|-------|--------|--------|:------:|:----------:|-------|
| IR Callable Fixed Rate Note | IRCFRN001 | REWRITE | V1 | S | 3 | Condense. |
| IR Accreting Callable / ZCL | AFRN001 partial | REWRITE + EXPAND | V1 + SP.docx C.15 | M | 3–4 | Expand to cover zero coupon linear variant. |
| Non-Callable Range Accrual | NCRA001 | REWRITE | V1 | S | 3 | Condense. |
| Callable Range Accrual | CRASRT001 | REWRITE | V1 | S | 3 | Condense. |
| Digital Cap-Floor | DCFN001 | REWRITE | V1 | S | 3 | Condense. |

**STEG Family (4 products):**

| Product | V1 ID | Action | Source | Effort | Est. Pages | Notes |
|---------|-------|--------|--------|:------:|:----------:|-------|
| Vanilla Steepener | VSTEG001 | REWRITE | V1 | S | 3 | Condense. |
| Range-Accrual Steepener | RASTEG001 | REWRITE | V1 | S | 3 | Condense. |
| Callable Steepener | CSTEG001 | REWRITE | V1 | S | 3 | Condense. |
| TARN Steepener | TARN001 | REWRITE | V1 | S | 3 | Condense. |

**Other Products (5 products):**

| Product | V1 ID | Action | Source | Effort | Est. Pages | Notes |
|---------|-------|--------|--------|:------:|:----------:|-------|
| Structured Deposits | — | CREATE NEW | SP.docx G; COMPLETE Part 8 | M | 3–4 | Good source content in both. Merge. |
| Accumulators / Decumulators | — | CREATE NEW | No source | L | 4–5 | Commonly traded. No source content. Full write. |
| Option on Risk Control | — | CREATE NEW | No source | M | 3–4 | No source content. |
| Equity Linked Option | — | CREATE NEW | No source | M | 3–4 | No source content. |
| Forwards | — | CREATE NEW | SP.docx B.11–B.12 (concept only) | S | 3 | Minimal source. Expand from concepts. |

**Part 5 Total:** 125–160 pages | **Total Effort:** 26 Rewrite, 15 Create
**Per-product size reduction:** V1 averages 7–10 pages/product → V2 targets 3–4 pages/product
**Content reduction per existing product:** ~50–60% (via boilerplate removal and centralization to Part 6)

---

## PART 6 — OPERATIONS

| Section | Action | Source(s) | Effort | Est. Pages | Notes |
|---------|--------|-----------|:------:|:----------:|-------|
| 6.1 Systems Overview | CREATE NEW | V1 fragments (23× NEMO, 23× Sophis, 10× Murex mentions) | M | 3–4 | Centralize. Write one authoritative description per system. |
| 6.2 Booking Flows | MERGE | V1 booking sections; COMPLETE Part 2.4 | M | 4–5 | 4 booking flows (ELN, SRT/STEG, CLN, Swap). End-to-end. Flowchart needed. |
| 6.3 Lifecycle Events | CREATE NEW | V1 fragments | M | 3–4 | Coupon, barrier, autocall, call, maturity, corporate actions. |
| 6.4 Product Control and Reconciliation | MERGE | V1 reconciliation sections (28 products) | L | 4–5 | Extract ~12,000 words of repeated reconciliation content. Centralize 7 common risks. Product-specific table. |
| 6.5 Fixing and Observation Conventions | CREATE NEW | V1 fragments | S | 2–3 | Centralize fixing sources, disrupted days, business day calendars. |
| 6.6 Settlement | CREATE NEW | V1 fragments | S | 2–3 | Physical vs cash. T+N conventions. |

**Part 6 Total:** 18–24 pages | **Total Effort:** 3 Create, 2 Merge, 1 Large
**Duplication reduction:** Eliminates ~24,000 words of per-product boilerplate from V1.
**Key principle:** Write once in Part 6, reference from Part 5. Every product deep dive says "See Part 6.4 for common reconciliation risks" instead of repeating them.

---

## PART 7 — QUICK REFERENCE GUIDE

| Section | Action | Source(s) | Effort | Est. Pages | Notes |
|---------|--------|-----------|:------:|:----------:|-------|
| 7.1 Product Attribute Lookups | CREATE NEW | Derived from Part 5 | M | 3–4 | 9 lookup tables. |
| 7.2 System Routing | CREATE NEW | Derived from Part 6 | S | 1–2 | Which products use which system. |
| 7.3 Risk Lookups | CREATE NEW | Derived from Parts 4–5 | S | 2–3 | Greeks by product, barrier risks, operational risk, model risk. |
| 7.4 Complexity Ranking | CREATE NEW | Derived from Part 3 | S | 1–2 | Simple / Medium / Complex. |
| 7.5 Desk Shorthand Index | KEEP | V1 desk shorthand lines | S | 1–2 | Extract all 28 desk shorthands. Add new products. |

**Part 7 Total:** 8–13 pages | **Total Effort:** 4 Create, 1 Keep (all Small-Medium)

---

## PART 8 — APPENDICES

| Section | Action | Source(s) | Effort | Est. Pages | Notes |
|---------|--------|-----------|:------:|:----------:|-------|
| A — Glossary | CREATE NEW | All sources; V1 undefined terms | M | 3–4 | All abbreviations + technical terms. |
| B — System Maps | CREATE NEW | V1 fragments | M | 2–3 | NEMO, Sophis, Murex field references. |
| C — Product Maps | CREATE NEW | Part 3 taxonomy | S | 2–3 | Taxonomy tree, family mapping, section cross-reference. |
| D — Booking Maps | MERGE | V1 booking sections; COMPLETE Appendix B | S | 2–3 | Per-family checklists. Critical fields. |
| E — Reference Tables | MERGE | COMPLETE Appendices A–B; V1 worked examples | S | 2–3 | Termsheet template, booking reference, decomposition formulas. |
| F — Reading Paths | CREATE NEW | Original | S | 1–2 | 4 reading paths by role. |

**Part 8 Total:** 12–18 pages | **Total Effort:** 3 Create, 2 Merge (all Small-Medium)

---

## Content Deleted from V1

The following V1 content will not appear in V2 in its current form:

| Content | V1 Location | Reason | Disposition |
|---------|-------------|--------|-------------|
| Per-product NEMO boilerplate | Every Booking & Systems section | Repeated 23 times | → Centralized in Part 6.1 |
| Per-product Sophis boilerplate | Every Booking & Systems section | Repeated 23 times | → Centralized in Part 6.1 |
| Per-product "Murex is not used" | 18 ELN/CLN products | Negative statement repeated 18 times | → System routing table in Part 6.1 |
| Per-product common reconciliation risks | Every Reconciliation section | Same 5 risks repeated 28 times | → Centralized in Part 6.4 |
| Per-product termsheet legal boilerplate | Every Definition section | Repeated 28 times | → One reference in Part 2.5 |
| Per-product FTP decomposition | Every Construction section | Same funding line repeated 28 times | → Explained once in Part 2.2 |
| Per-product issuer funding line | Every Construction section | Same decomposition repeated 28 times | → Explained once in Part 2.2 |

**Total words deleted (boilerplate):** ~24,000
**Net effect:** V1 content (~60,000 words for 28 products) → V2 deep dives (~35,000–40,000 words for ~42 products). More products in fewer words.

---

## Aggregate Estimates

### By Action Type

| Action | Section Count | Est. Pages |
|--------|:------------:|:----------:|
| CREATE NEW | 32 | 85–115 |
| REWRITE | 30 | 85–100 |
| MERGE | 14 | 45–60 |
| KEEP | 2 | 4–6 |
| DELETE | 7 categories | −24,000 words |
| **Total** | **78 sections** | **240–320 pages** |

### By Effort

| Effort | Count |
|--------|:-----:|
| S (Small) | 38 |
| M (Medium) | 35 |
| L (Large) | 2 |
| XL (Extra Large) | 0 |

### Size Comparison

| Metric | V1 | V2 Target | Change |
|--------|:--:|:---------:|:------:|
| Products | 28 | ~42 | +50% |
| Total pages | ~110 (PDF) | 240–320 | +120–190% |
| Words per product | ~2,100 | ~800–1,000 | −55% |
| Boilerplate words | ~24,000 | ~0 | −100% |
| Foundational content | 0 pages | 50–60 pages | New |
| Comparison tables | 0 | 11+ | New |
| Diagrams | 0 | 15+ | New |
| Reading paths | 0 | 4 | New |

### Estimated Effort Breakdown

| Phase | Description | Effort |
|-------|-------------|:------:|
| Phase A | Foundations + Framework (Parts 1–2) | L — heaviest original writing |
| Phase B | Taxonomy + Comparisons (Parts 3–4) | M — synthesis and tabulation |
| Phase C | Product Deep Dives — existing (Parts 5.1–5.5 existing) | L — 26 rewrites |
| Phase D | Product Deep Dives — new (Parts 5.3, 5.6 new) | L — 15 new products |
| Phase E | Operations (Part 6) | M — centralization from V1 fragments |
| Phase F | Quick Reference + Appendices (Parts 7–8) | M — derived from Parts 1–6 |
| Phase G | Visualization (diagrams, tables, flowcharts) | M — 15+ visual assets |

**Recommended execution order:** A → B → E → C → D → F → G
(Build foundations first, then taxonomy and operations to eliminate boilerplate, then rewrite products with centralized references in place, then derive quick reference and appendices.)
