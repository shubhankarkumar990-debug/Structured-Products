# Desk Bible v2 — Gap Analysis

**Audit Date:** 2026-06-19
**Sources Compared:**
- `release/desk-bible-v1/Desk_Bible_v1.md` (V1 — 28 products, 2,821 lines)
- `Structured Products.docx` (Original training manual — 3,478 paragraphs)
- `Structured_Products_Desk_Bible_COMPLETE.docx` (Complete draft — 9 parts, 1,147 paragraphs)
- `products/catalog.yaml` (Pipeline catalog — 28 entries)
- Master Product Universe (user-specified — ~40 products across 5 categories)

---

## 1. Missing Products

The master product universe specifies products not present in V1.

| Product | Category | Status in V1 |
|---------|----------|--------------|
| Booster Note | ELN | MISSING — not in V1 or catalog |
| Digital Coupon Knock-In Put | ELN | MISSING — not in V1 or catalog |
| Structured Deposits | Other | MISSING from V1 — covered in `Structured Products.docx` Section G and `COMPLETE.docx` Part 8 |
| Option on Risk Control | Other | MISSING — not in any source |
| Equity Linked Option | Other | MISSING — not in any source |
| Forwards | Other | MISSING as standalone product — mentioned in `Structured Products.docx` Section B.11–B.12 as concept only |
| Accumulators / Decumulators | Other | MISSING — not in any source |
| Vanilla Options | Other | MISSING as standalone product — options covered as components, not as traded products |
| Total Return Swap (TRS) | Swaps | MISSING from V1 — covered in `Structured Products.docx` Section 31 |
| Currency Swaps | Swaps | MISSING from V1 — covered in `Structured Products.docx` Section 33 |
| Equity Swaps | Swaps | MISSING from V1 — covered in `Structured Products.docx` Section 32 |
| Commodity Swaps | Swaps | MISSING from V1 — covered in `Structured Products.docx` Section 34 |
| Credit Default Swaps | Swaps | MISSING from V1 — covered in `Structured Products.docx` Section 35 |
| Vanilla Swap (VLSP) | Swaps | PARTIAL — V1 has "Vanilla Interest Rate Swap" (SWAP001) but limited coverage |
| IR Accreting Callable Swap (Zero Coupon Linear) | SRT | MISSING — V1 has "Accreting Fixed Rate Note" which is different |

**Total missing:** 14 products not in V1. Of these, 6 have content in `Structured Products.docx` (TRS, Equity Swaps, Currency Swaps, Commodity Swaps, CDS, Structured Deposits). 8 have no content in any source.

---

## 2. Missing Foundational Concepts

V1 contains **zero foundational content**. It jumps directly into product definitions at Part 3 (Equity-Linked Notes). Both `Structured Products.docx` and `COMPLETE.docx` contain significant foundational material that V1 omits entirely:

| Concept | In Structured Products.docx | In COMPLETE.docx | In V1 |
|---------|:---------------------------:|:-----------------:|:-----:|
| Long vs Short | Section A.1 (detailed) | Part 1.1 (concise) | No |
| Calls and Puts | Section A.2 | Part 1.2 | No |
| Spreads | Section A.3 | Part 1.1 | No |
| Knock-In / Knock-Out | Section A.6 | Part 1.2 | No (used but undefined) |
| Digital Options | Not standalone | Part 1.2 | No |
| Quanto | Section A.7 | Part 1.2 | No |
| P&L / Mark-to-Market | Section B.1–B.2 | Not standalone | No |
| Volatility (implied/realized) | Section B.3–B.4 | Part 1.4 | No (used but undefined) |
| Delta | Section B.5 | Part 1.3 | No (used but undefined) |
| Gamma | Section B.6 | Part 1.3 | No (used but undefined) |
| Theta | Section B.7 | Part 1.3 | No (used but undefined) |
| Vega | Section B.8 | Part 1.3 | No (used but undefined) |
| Convexity | Section B.9 | Part 1.3 | No |
| Forwards | Section B.11–B.12 | Not standalone | No |
| Funding / FTP | Section B.13–B.14 | Part 2.3 | No (used but undefined) |
| Carry | Section B.14 | Part 1.1 | No |
| Liquidity | Section B.15 | Part 1.5 | No |
| Correlation | Section B.20 | Part 1.5 | No (used but undefined) |
| Worst-Of / Best-Of | Section B.21 | Part 1.5 | No (used but undefined) |
| Credit Spread / Recovery | Sections B.22–B.23 | Not standalone | No |
| Model Risk | Section B.25 | Part 1.5 | No |
| Yield Curves | Section C.1–C.2 | Part 4.1 | No |
| Caps and Floors | Section C.4 | Not standalone | No |
| Swaptions | Section C.5 | Not standalone | No |
| Four-Leg Framework | Not present | Part 2 (full) | No |
| How desks hedge | Section E (full) | Part 9.1 | No |
| Why clients misprice vol | Section F (full) | Part 9.3 | No |
| Credit Events taxonomy | Section K (full) | Part 6.3 | No |

**Critical gap:** V1 uses Delta, Gamma, Vega, correlation, funding, FTP, barriers, knock-in, and knock-out extensively without ever defining them. A new joiner reading V1 would encounter undefined terminology from the first paragraph.

---

## 3. Missing Operational Concepts

V1 embeds operational detail within each product but lacks centralized operational content:

| Concept | Status in V1 |
|---------|-------------|
| NEMO system overview | Mentioned 28 times (once per product) — never described as a system |
| Sophis system overview | Mentioned 28 times — never described as a system |
| Murex system overview | Mentioned in SRT/STEG products — never described as a system |
| Four-Leg Framework (Note/Issuer/Deposit/Hedge) | Not present — exists in COMPLETE.docx Part 2 |
| Trade lifecycle (booking → maturity) | Not present as a concept — fragmented across products |
| Product lifecycle | Not present |
| Corporate actions | Not present in V1 — covered in Structured Products.docx Section A.5 |
| Fixing and observation conventions | Repeated per product — never centralized |
| Settlement types (physical/cash) | Repeated per product — never centralized |
| Coupon accrual conventions | Repeated per product — never centralized |
| Day count conventions | Repeated per product — never centralized |
| Booking flow (end-to-end) | Not present |
| P&L attribution | Not present |
| Stress behavior | Not present — exists in Structured Products.docx Section E.5 and COMPLETE.docx Part 9.2 |
| ELN vs SRT comparison | Not present — exists in COMPLETE.docx Part 4.3 |
| SRT vs STEG comparison | Not present — exists in COMPLETE.docx Part 7.3 |

---

## 4. Duplicate Content

V1 contains significant structural repetition across its 28 product entries:

| Repeated Block | Occurrences | Estimated Redundant Words |
|---------------|:-----------:|:-------------------------:|
| "The book of record is NEMO, which carries..." | 23 | ~4,600 (200 words × 23) |
| "Risk and P&L run through Sophis, which..." | 23 | ~3,450 (150 words × 23) |
| "The legal document is the Termsheet, which defines..." | 28 | ~2,800 (100 words × 28) |
| "Murex is not used." | 18 | ~54 (3 words × 18) |
| Put strike reconciliation (NEMO % vs Sophis absolute) | 13 | ~1,950 (150 words × 13) |
| Fixing source reconciliation paragraph | 15 | ~2,250 (150 words × 15) |
| Settlement type reconciliation | 10 | ~1,500 (150 words × 10) |
| Observation date convention paragraph | 12 | ~1,800 (150 words × 12) |
| "The dominant operational risk is..." | 28 | ~2,800 (100 words × 28) |
| Issuer funding decomposition line | 28 | ~1,400 (50 words × 28) |
| FTP decomposition line | 28 | ~1,400 (50 words × 28) |

**Total estimated redundant words:** ~24,000 (approximately 40% of the entire document)

The reconciliation sections are the worst offenders. Every product repeats the same 5 reconciliation risks (put strike, settlement type, fixing source, observation convention, dividend treatment) with slight variations. A centralized reconciliation framework could eliminate ~12,000 words while improving clarity.

---

## 5. Overly Verbose Sections

| Section Type | Current Length Per Product | Appropriate Length | Issue |
|-------------|:-------------------------:|:------------------:|-------|
| Definition | 150–250 words | 50–80 words | Definitions are narratives, not definitions. They re-explain construction, payoff, and risk instead of defining the product. |
| Construction | 150–250 words | 80–120 words | Good content but written as prose. Would be clearer as component lists. |
| Booking & Systems | 200–350 words | 50–80 words (after centralizing) | 70% of content repeats NEMO/Sophis boilerplate. |
| Pricing Intuition | 200–400 words | 100–150 words | Excellent content, but transitions and repeated context add length. |
| Reconciliation | 250–500 words | 80–120 words (after centralizing) | Most reconciliation risks are system-level, not product-level. 5 common risks repeated 28 times. |
| Desk View | 200–350 words | 100–150 words | Good content. Could be tighter. "When appropriate / when not appropriate" is valuable but formulaic. |
| Worked Example | 300–600 words | 200–300 words | Good content. Decomposition arithmetic is essential. Scenarios could be tabular. |
| Desk Shorthand | 5–10 words | 5–10 words | Perfect. No change needed. |

**Estimated total V1 word count:** ~60,000 words
**Estimated achievable word count after deduplication and tightening:** ~25,000–30,000 words

---

## 6. Weakly Explained Concepts

| Concept | Issue |
|---------|-------|
| CMS spread | Used in all STEG products but never explained from first principles |
| Base correlation | Used in TRANCHE001 but explained only mechanically |
| LHP approximation | Referenced in TRANCHE001 — acronym used without expansion or intuition |
| Bermudan exercise | Used in Callable products — assumes reader knows Bermudan vs European vs American |
| Broadie-Glasserman correction | Mentioned in KODRC001 — deep quant reference with no context |
| Worst-of basket | Used in Phoenix Autocallable — correlation mechanics assumed |
| Memory feature | Used in Phoenix — path-dependent overlay not well-explained for beginners |
| FTP (Funds Transfer Pricing) | Used in every decomposition — never explained |
| Issuer credit curve | Referenced in every construction section — never explained |
| Day count conventions (30/360, actual/365) | Referenced in reconciliation — never explained |
| CSA and collateral | Not mentioned in V1 but present in COMPLETE.docx — critical for swaps |

---

## 7. Sections Unsuitable for New Joiners

| Section | Why Unsuitable |
|---------|---------------|
| Every Definition section | Opens with dense legal/financial language. "Issued as an equity-linked note (ELN) under an ISDA or MTN wrapper" — a new joiner doesn't know what ISDA or MTN means. |
| Every Construction section | Assumes knowledge of options decomposition, funding legs, and premium mechanics. |
| Every Pricing Intuition section | Assumes Greeks knowledge. "The dominant Greeks are short vega and Delta" — meaningless without defining Greeks first. |
| Every Reconciliation section | Assumes familiarity with NEMO, Sophis, and booking workflows. |
| TRANCHE001 | Base correlation, LHP approximation, 125-name CDX IG portfolio — requires graduate-level credit knowledge. |
| NTD001 | Copula models, default correlation reversal — assumes quantitative credit background. |

---

## 8. Missing Diagrams and Visual Aids

V1 contains zero diagrams, zero flowcharts, and zero comparison tables. The following would significantly improve comprehension:

| Visual | Purpose | Priority |
|--------|---------|----------|
| Product taxonomy tree | Show how products relate to each other | HIGH |
| Payoff diagrams (per product) | Visual P&L at maturity | HIGH |
| ELN comparison matrix | Side-by-side feature comparison | HIGH |
| Barrier mechanics diagram | KI, KO, European vs American observation | HIGH |
| Autocall mechanics flowchart | Decision tree at each observation date | HIGH |
| Four-Leg Framework diagram | Note/Issuer/Deposit/Hedge flows | HIGH |
| System architecture map | NEMO ↔ Sophis ↔ Murex ↔ Termsheet | HIGH |
| Booking flow | Trade entry → risk → P&L → settlement | MEDIUM |
| Product lifecycle timeline | Inception → observations → maturity/early redemption | MEDIUM |
| Credit waterfall (CLN family) | Reference entity → credit event → settlement | MEDIUM |
| Tranche structure | Attachment/detachment, loss waterfall | MEDIUM |
| CMS spread diagram | 30Y CMS − 2Y CMS, curve shape intuition | MEDIUM |
| Swap cashflow diagram | Fixed vs floating legs, netting | MEDIUM |
| Greek sensitivity chart | Delta/Vega/Gamma profiles near barriers | LOW |
| Vol surface / skew | 2D surface showing term structure and strike | LOW |

---

## 9. Missing Comparison Tables

V1 has zero comparison tables. The following are needed:

| Comparison | Products Covered |
|-----------|-----------------|
| ELN family matrix | All 13 ELNs: coupon type, barrier, autocall, capital protection, put type |
| Reverse Convertible variants | RC, DRC, KODRC, CRC, Airbag — what changes between each |
| Autocallable variants | Phoenix, FCN, Callable Range Accrual — conditional vs fixed coupon |
| CLN family matrix | Vanilla CLN, Skew CLN, FTD, NTD, Tranche — reference type, correlation exposure |
| STEG family matrix | Vanilla, Range Accrual, Callable, TARN — coupon mechanics, optionality |
| SRT family matrix | 5 SRT products — callable vs non-callable, accreting vs fixed |
| Swaps matrix | IRS, TRS, Equity, Currency, Commodity, CDS — what is exchanged |
| System routing | Which products use NEMO, Sophis, Murex |
| Risk profile matrix | Which products are short vol, long vol, short correlation |
| Capital protection matrix | Full, conditional (barrier), zero — by product |
| Complexity ranking | Simple → Complex across all products |

---

## 10. Summary Assessment

| Dimension | V1 Score | Target for V2 |
|-----------|:--------:|:--------------:|
| Foundational concepts | 0/10 | 8/10 |
| Product coverage (vs master universe) | 6/10 | 9/10 |
| New-joiner readability | 2/10 | 8/10 |
| Operational content | 4/10 (fragmented) | 8/10 (centralized) |
| Comparison and cross-reference | 1/10 | 8/10 |
| Visual aids | 0/10 | 7/10 |
| Verbosity / efficiency | 3/10 | 8/10 |
| Reading flow | 3/10 | 8/10 |

V1 is an accurate, detailed product encyclopedia. It is not a training manual, not an operational handbook, and not a quick reference. V2 must restructure the same knowledge into a progressive learning path with centralized operations, comparison frameworks, and foundational pre-reading.
