# Desk Bible v2 — Curriculum Review

**Date:** 2026-06-19
**Purpose:** Validate and improve the V2 curriculum design before any writing begins.
**Standard:** The "No Unexplained Terminology Rule" — a reader should never encounter a term that has not already been explained.

---

## 1. Does the Current V2 Architecture Support a Complete Beginner?

**Verdict: NO — three structural gaps must be fixed.**

### Gap A: Part 0 assumes financial literacy it claims not to require.

The directive says "assume the reader has never worked in finance." Part 0 as specified does not go far enough.

Section 0.1 ("Why Financial Markets Exist") jumps directly into debt vs equity and risk vs return. But a true beginner needs more foundational steps:

| Missing Concept | Why It Must Come First |
|----------------|----------------------|
| What is a market? | The reader needs to understand that a market is simply a place where buyers and sellers meet — before understanding financial markets specifically. |
| What is a security? | Stocks and bonds are the building blocks of everything. Options are derivatives of stocks. Structured products are built from bonds. The reader cannot understand any of this without knowing what stocks and bonds are. |
| What is interest? | Interest is the price of borrowing money. Every bond, every swap, every yield curve, every funding leg depends on this concept. It must be taught before any product. |
| What is risk? | Not as a financial term, but as a concept. The idea that outcomes are uncertain. That higher uncertainty demands higher compensation. This principle drives every product in the book. |
| Time value of money | A dollar today is worth more than a dollar tomorrow. Present value, discounting, compounding. Without this, the reader cannot understand bond pricing, coupon calculations, or swap valuation. |
| What is a derivative? | Section 0.3 explains "Why Derivatives Were Invented" but never defines what a derivative is. The title assumes the reader knows the word. The section should first explain: a derivative is a contract whose value depends on something else. |

**Recommendation:** Expand Part 0 into a true "Chapter Zero" that teaches these six concepts before anything else.

### Gap B: Part 1 mixes prerequisite and intermediate content.

Part 1 ("Foundations") currently spans from "Long vs Short" to "Credit Events (ISDA taxonomy)." This is too wide a range for a single part. A reader who needs "Long vs Short" explained is not ready for ISDA credit event taxonomy in the same sitting.

The foundational topics fall into three tiers:

| Tier | Concepts | Purpose |
|------|----------|---------|
| **Tier 1: Market Mechanics** | Long/Short, Bid/Offer, P&L, Leverage, Liquidity | How markets work |
| **Tier 2: Options and Risk** | Calls/Puts, Exercise, Barriers, Greeks, Volatility, Correlation | The tools of structured products |
| **Tier 3: Rates and Credit** | Yield curves, Benchmarks, CMS, Caps/Floors, Credit spreads, CDS, Credit events | Domain-specific foundations |

The current structure puts all three tiers into one Part. A complete beginner will hit a wall somewhere in Tier 2 if they don't have time to absorb Tier 1 first.

**Recommendation:** Consider splitting Part 1 into two parts:
- Part 1A: Market Mechanics (Tier 1 — the absolute basics)
- Part 1B: Financial Instruments (Tiers 2-3 — options, rates, credit)

Or, at minimum, add clear section breaks and "checkpoint summaries" between tiers so the reader knows when they've mastered one level before moving to the next.

### Gap C: Operations knowledge is introduced too late.

The current structure places Part 6 (Operations) AFTER Part 5 (Product Deep Dives). But the product chapter template includes "Booking and Operations" (section 10) and "Reconciliation Red Flags" (section 11), both of which reference systems and processes that won't be explained until Part 6.

A sequential reader will encounter phrases like "booked in NEMO," "priced in Sophis," and "four-leg framework in Murex" dozens of times in Part 5 before ever learning what these systems are.

**Recommendation:** Add a brief systems primer to Part 2 (Framework). Not the full Part 6 treatment, but enough that the reader knows:
- What NEMO is (book of record)
- What Sophis is (pricing and risk)
- What Murex is (rates products, four-leg booking)
- Which products route where

This primer should be 1-2 pages. Part 6 then expands this into full operational detail.

---

## 2. Is Terminology Introduced in the Correct Order?

**Verdict: MOSTLY — but 11 specific violations identified.**

I traced every term through the proposed structure, checking that its first use comes after its first definition. The table below lists violations where the current sequencing would force a reader to encounter an undefined term.

| Term | First Used In | Should Be Defined In | Current Definition Location | Violation? |
|------|--------------|---------------------|---------------------------|:----------:|
| Yield | Part 0.4 ("Yield enhancement") | Part 0 | Part 1.7 | YES |
| Capital | Part 0.4 ("Capital protection") | Part 0 | Not defined anywhere | YES |
| Leverage | Part 0.4 ("Leverage") | Part 0 | Part 1.1 | YES |
| Downside | Part 0.4 ("Downside protection") | Part 0 | Not defined anywhere | YES |
| Derivative | Part 0.3 (title) | Part 0.3 (but title assumes knowledge) | Part 0.3 body (implied) | MINOR |
| Bond | Part 2.2 ("Bond + Option = Structured Product") | Part 0 or Part 1 | Not defined as a standalone concept | YES |
| Premium | Part 1.2 (Options) | Part 1.2 | Part 1.2 body | OK (defined in same section) |
| Strike Price | Part 1.2 (Options) | Part 1.2 | Part 1.2 body | OK |
| Coupon | Part 2.2 (Product Construction) | Part 0 or Part 1 | Never formally defined | YES |
| NEMO | Part 5 (Product Deep Dives) | Part 2 or earlier | Part 6.1 | YES |
| Sophis | Part 5 (Product Deep Dives) | Part 2 or earlier | Part 6.1 | YES |
| Murex | Part 5 (Product Deep Dives) | Part 2 or earlier | Part 6.1 | YES |
| FTP | Part 2.2 (Product Construction) | Part 0 or Part 1 | Part 1.1 (Carry and Funding) | MINOR — depends on depth of Part 1.1 |
| ISDA | Part 1.8 (Credit Risk) | Part 1 or Glossary | Never formally defined | YES |
| MTN | Part 5 (from V1 product definitions) | Part 2 (Framework) | Never defined | YES |

### Terminology Introduction Order — Corrected Sequence

The following terms must be defined before they are used. Proposed introduction points:

**Part 0 must define:** market, security, stock, bond, interest, coupon, yield, risk, return, capital, leverage, downside, derivative, maturity, principal, notional.

**Part 1 must define:** long, short, bid, offer, spread, P&L, mark-to-market, option, call, put, premium, strike, exercise, expiry, in-the-money, at-the-money, out-of-the-money, barrier, knock-in, knock-out, digital, delta, gamma, vega, theta, rho, volatility, implied, realized, correlation, worst-of, best-of, yield curve, forward rate, spot rate, SOFR, EURIBOR, CMS, cap, floor, swaption, credit spread, recovery rate, CDS, credit event, ISDA.

**Part 2 must define:** structured product, note, issuer, SPV, FTP, desk margin, four-leg framework, termsheet, MTN, NEMO (brief), Sophis (brief), Murex (brief), autocall, memory feature.

---

## 3. Is Part 0 Sufficient?

**Verdict: NO — needs significant expansion.**

### Current Part 0 Structure (from directive)

| Section | Content |
|---------|---------|
| 0.1 Why Financial Markets Exist | Companies need capital, investors provide it, debt vs equity, risk and return |
| 0.2 What Banks Actually Do | Commercial banking, IB, Sales, Trading, Structuring, Risk, ProdCon, Ops |
| 0.3 Why Derivatives Were Invented | Farmers, airlines, exporters, commodity producers |
| 0.4 Why Structured Products Exist | Income generation, downside protection, leverage, yield enhancement, capital protection |
| 0.5 The Ecosystem | Clients, Sales, Traders, Structurers, Risk, Product Control, Operations |

### Assessment

| Section | Beginner-Ready? | Issue |
|---------|:---------------:|-------|
| 0.1 | Partially | Needs "What is a market?" and "What is a security?" before debt vs equity. Needs "What is interest?" and "What is risk?" and "Time value of money." |
| 0.2 | Yes | Good scope. Add brief explanation of front/middle/back office distinction. |
| 0.3 | Partially | Must define "derivative" before explaining why they were invented. The examples (farmers, airlines) are excellent but need the definition first. |
| 0.4 | No | Uses undefined terms (yield, leverage, capital protection, downside). Must come AFTER Part 0 defines these terms, or must define them inline. |
| 0.5 | Yes | Good scope. Overlaps with 0.2 — consider merging or clarifying distinction. 0.2 = what the bank does; 0.5 = what a structured products desk does. |

### Recommended Expanded Part 0

| Section | Title | Content | Teaching Purpose |
|---------|-------|---------|-----------------|
| 0.1 | What Is a Market? | Buyers and sellers. Price discovery. Stock markets, bond markets, commodity markets. Exchanges vs OTC. | Establish the arena |
| 0.2 | What Are Securities? | Stocks (ownership), Bonds (lending), how they work, why they exist. What is interest? What is a coupon? What is yield? | Teach the building blocks |
| 0.3 | Risk, Return, and the Time Value of Money | Higher risk demands higher return. A dollar today vs a dollar tomorrow. Compounding. Discounting. Present value. | Teach the fundamental law |
| 0.4 | What Banks Actually Do | Commercial vs investment banking. Front/Middle/Back office. Sales, Trading, Structuring, Risk, ProdCon, Ops. | Establish the institutional context |
| 0.5 | What Is a Derivative? | A contract whose value depends on something else. Futures, options, swaps — one sentence each. Why they exist: the farmer/baker example. The airline/fuel example. | Define the category |
| 0.6 | Why Structured Products Exist | Now that the reader knows what securities, risk, and derivatives are: income generation, downside protection, leverage, yield enhancement, capital protection. Each term can now be used because it was defined in 0.2-0.3. | Motivate the entire book |
| 0.7 | The Structured Products Desk | Clients, Sales, Traders, Structurers, Risk, Product Control, Operations. What each role does. How they interact. | Map the ecosystem the reader is entering |

**Net effect:** Part 0 grows from 5 sections to 7 sections, estimated 15-20 pages. This is the most critical expansion — it is the foundation that everything else stands on.

---

## 4. Should Product Chapters Be Reorganized?

**Verdict: YES — two changes recommended.**

### Issue 1: Product ordering within families should follow teaching progression, not alphabetical or catalog order.

The current Part 5 lists ELNs as: RC, DRC, KODRC, CRC, Airbag, Phoenix, FCN, Callable Range Accrual, Bonus, PPN, Warrant, ICN, Digital, Booster, Digital KI Put.

This ordering starts with a moderately complex product (Reverse Convertible) and immediately introduces variants (DRC, KODRC) before the reader has absorbed the base product. A teaching-oriented ordering should:

1. Start with the simplest product in the family
2. Build complexity progressively
3. Group by teaching relationship, not variant relationship

**Recommended ELN ordering:**

| Order | Product | Rationale |
|:-----:|---------|-----------|
| 1 | Principal Protected Note | Simplest: no downside. Pure bond + call option. Best first product. |
| 2 | Reverse Convertible | Core product: bond + short put. Introduces barrier risk. |
| 3 | Discounted Reverse Convertible | Variant: adds discount to entry price. One concept added. |
| 4 | Knock-Out Discounted RC | Variant: adds knock-out barrier. One concept added. |
| 5 | Callable Reverse Convertible | Variant: adds issuer call right. One concept added. |
| 6 | Airbag / Leveraged RC | Variant: adds leverage below barrier. One concept added. |
| 7 | Bonus / Participation Note | Different structure: upside participation with conditional protection. |
| 8 | Phoenix Autocallable | New mechanism: periodic observation, memory coupon, autocall. Requires barrier and coupon concepts. |
| 9 | Fixed Coupon Note (FCN) | Simpler autocallable: fixed coupon (no conditionality). Easier than Phoenix. |
| 10 | Callable Range Accrual ELN | Combines accrual (from rates) with equity. Cross-family. |
| 11 | Issuer Callable Note | Pure callable: no barrier, just call right. |
| 12 | Digital Coupon Notes | Digital payoff: all-or-nothing coupon. Requires digital option knowledge. |
| 13 | Booster Note | Leveraged upside participation. |
| 14 | Digital Coupon Knock-In Put | Combines digital and barrier. Most complex. |
| 15 | Warrant / Turbo Certificate | Standalone option exposure. Different risk profile from notes. |

**Note:** Phoenix and FCN ordering is debatable. FCN is simpler (fixed coupon), but Phoenix is the more important product on a desk. Teaching FCN first (simpler) then Phoenix (adds conditionality and memory) may be better pedagogy. The above places Phoenix first because understanding the full autocall mechanism is more important than covering the simpler variant first, and the reader needs the full autocall concept to understand what FCN simplifies.

**Alternative:** Teach FCN before Phoenix. FCN = "autocall with guaranteed coupon." Phoenix = "autocall with conditional coupon and memory." This is simpler → complex.

### Issue 2: Swaps should be taught before Credit-Linked Notes.

The current order is: ELN → CLN → Swaps → SRT → STEG → Other.

But CLN products (especially FTD, NTD, and Synthetic Tranche) reference Credit Default Swaps extensively. A reader encountering "The investor sells credit protection via CDS" in the CLN chapter hasn't learned what a CDS is yet (CDS is in the Swaps chapter).

**Recommended Part 5 family ordering:**

| Order | Family | Rationale |
|:-----:|--------|-----------|
| 1 | Equity-Linked Notes | Most intuitive. Equity is the most familiar asset class. |
| 2 | Swaps | Required for understanding rate products AND credit products. IRS must be taught before SRT/STEG. CDS must be taught before CLN. |
| 3 | Structured Rate Trades | Built on IRS and rate concepts. Requires swap knowledge. |
| 4 | Steepener Notes | Built on CMS rate concepts. Requires yield curve knowledge. |
| 5 | Credit-Linked Notes | Built on CDS and credit concepts. Requires swap knowledge. |
| 6 | Other Products | Miscellaneous. Many are simpler (Forwards, Vanilla Options) but don't fit families. |

This reordering solves the CDS-before-CLN dependency and the IRS-before-SRT dependency.

---

## 5. Are Additional Foundational Concepts Required?

**Verdict: YES — 8 concepts missing from the curriculum.**

The foundational topics matrix identified 60 topics across 8 categories. The directive adds Part 0 and expands the teaching philosophy. Cross-referencing both, the following concepts are required but not currently allocated to any section:

| Concept | Why Required | Proposed Location |
|---------|-------------|-------------------|
| **What is a market?** | The most fundamental concept. Where buyers and sellers meet. | Part 0.1 |
| **What are stocks and bonds?** | Building blocks of everything. SP = Bond + Option. | Part 0.2 |
| **What is interest? What is a coupon?** | Interest is used in every product. Coupon is used in every note. | Part 0.2 |
| **Time value of money / Discounting** | Required for present value, bond pricing, swap valuation. Used implicitly in every worked example. | Part 0.3 |
| **What is a derivative?** | The category that contains all products in this book. Must be defined before Part 1. | Part 0.5 |
| **Payoff diagrams: how to read them** | Every product has a payoff diagram. The reader needs to know what the axes mean before seeing one. | Part 1.2 (before first payoff diagram) |
| **What is a swap? (conceptual)** | Swaps are referenced in Part 1.7 (Swaptions), Part 2 (hedging), and throughout. A one-paragraph swap concept should appear before Part 1.7. | Part 1.7 or Part 0.5 |
| **Variance Swap** | Listed in directive product universe but missing from audit product coverage matrix and rewrite plan. | Part 5.3 (Swaps) — new product |

### Variance Swap: New Product Not In Audit

The directive adds **Variance Swap** to the Swaps family. This was not in the original master product universe, the product coverage matrix, or the rewrite plan. It needs to be added:

- Full product universe count increases from ~42 to ~49 (including directive additions)
- Variance Swap requires explanation of variance, realized variance, and variance notional
- Should be placed after IRS and before or after Equity Swap (conceptually related to volatility trading)

### Full Product Count Reconciliation

The directive's product list differs from the audit's. Here is the reconciliation:

| Change | Audit | Directive | Delta |
|--------|:-----:|:---------:|:-----:|
| Variance Swap | Not listed | Listed | +1 |
| Accumulators / Decumulators | Combined (1 entry) | Separated (2 entries) | +1 |
| Vanilla Options | P3 (nice to have) | Explicitly required | Upgraded |
| **Total products** | **~42** | **~49** | **+7** |

---

## 6. Is the Learning Journey Logically Sequenced?

**Verdict: MOSTLY — but three ordering issues must be resolved.**

### The Ideal Learning Sequence

A complete beginner should be able to read the book front-to-back without needing to skip ahead or look things up. Here is the knowledge dependency graph:

```
What is a market?
  └─► What are stocks and bonds?
       └─► What is interest, yield, risk?
            └─► Time value of money
                 └─► What is a derivative?
                      ├─► Long and Short
                      ├─► Calls and Puts
                      │    └─► Exercise styles, Moneyness
                      │         └─► Barriers and Digitals
                      │              └─► Greeks
                      │                   └─► Volatility
                      │                        └─► Correlation
                      ├─► What is a swap? (conceptual)
                      │    └─► Yield curves and Rates
                      │         └─► CMS rates
                      │    └─► Credit risk and CDS
                      └─► What is a structured product?
                           └─► Product construction
                                └─► Four-Leg Framework
                                     └─► Product lifecycle
                                          └─► Product taxonomy
                                               └─► Product deep dives
                                                    └─► Operations (systems, booking)
                                                         └─► Quick reference
```

### Issue 1: Rates and Credit ordering within Part 1

**Current order:** 1.1 Trading → 1.2 Options → 1.3 Barriers → 1.4 Greeks → 1.5 Volatility → 1.6 Correlation → 1.7 Rates → 1.8 Credit

**Problem:** Sections 1.2-1.6 are equity-focused. Sections 1.7-1.8 are rates/credit-focused. This is a clean split. However, the transition from Correlation (1.6) to Yield Curves (1.7) is abrupt. The reader goes from basket options to interest rate curves with no bridge.

**Recommendation:** Add a one-paragraph bridge at the start of 1.7 explaining: "So far we have focused on options and equity risk. But many structured products are built on interest rates, not equities. Before we can understand these products, we need to understand how interest rates work."

Also add a conceptual introduction to swaps at the end of Part 1.7 or beginning of Part 1.8, since swaps are both a rates product and a credit product, and the reader will encounter both CDS (credit) and IRS (rates) in Part 5.

### Issue 2: Swaps chapter should come before CLN chapter in Part 5

(Covered in Section 4 above. CDS must be taught before CLN products reference it.)

### Issue 3: Systems primer should come before product deep dives

(Covered in Section 1, Gap C above. Brief NEMO/Sophis/Murex introduction should be in Part 2.)

---

## 7. Product Chapter Template Impact Assessment

The directive specifies a 14-section template per product. The audit estimated 3-4 pages per product with a 9-section template. The expanded template changes the estimates:

| Section | Est. Length | Audit Template? |
|---------|:----------:|:---------------:|
| 1. Explain Like I'm New | 1 page | No — NEW |
| 2. Real World Analogy | 0.25 page | No — NEW |
| 3. What Problem Does This Solve? | 0.25 page | No — NEW |
| 4. Why Clients Buy It | 0.25 page | Similar (audit "Why Clients Buy It") |
| 5. What Happens If... (4 scenarios) | 0.5 page | No — NEW |
| 6. Formal Product Definition | 0.25 page | Similar (audit "What It Is") |
| 7. Product Construction | 0.5 page | Yes |
| 8. Payoff Logic | 0.25 page | Yes |
| 9. Key Risks | 0.25 page | Yes |
| 10. Booking and Operations | 0.25 page | Yes |
| 11. Reconciliation Red Flags | 0.25 page | Yes |
| 12. Worked Example | 0.5 page | Yes |
| 13. Interview Questions | 0.5 page | No — NEW |
| 14. Mental Models | 0.25 page | No — NEW |
| **Total per product** | **~5 pages** | |

**Revised Part 5 estimate:** ~49 products x ~5 pages = **~245 pages** (audit estimated 125-160 pages)

**Revised total document estimate:**

| Part | Audit Estimate | Revised Estimate |
|------|:--------------:|:----------------:|
| Part 0 — How Finance Works | Not in audit | 15–20 |
| Part 1 — Foundations | 27–35 | 35–45 |
| Part 2 — Framework | 19–24 | 25–30 |
| Part 3 — Taxonomy | 8–12 | 10–15 |
| Part 4 — Comparisons | 11–18 | 15–20 |
| Part 5 — Deep Dives | 125–160 | 230–260 |
| Part 6 — Operations | 18–24 | 25–30 |
| Part 7 — Quick Reference | 8–13 | 15–20 |
| **Total** | **240–320** | **370–440** |

---

## 8. Recommended Curriculum Revisions

### Revision 1: Expand Part 0

Add sections 0.1 (What Is a Market?), 0.2 (What Are Securities?), 0.3 (Risk, Return, and Time Value of Money). Renumber remaining sections. Ensure all terms used in 0.6 (Why Structured Products Exist) are defined in 0.1-0.5.

### Revision 2: Add Systems Primer to Part 2

Add a new section 2.8 "The Systems: A First Look" — 1-2 pages introducing NEMO, Sophis, Murex at a conceptual level. Full detail remains in Part 6.

### Revision 3: Reorder Part 5 Families

Change from: ELN → CLN → Swaps → SRT → STEG → Other
Change to: ELN → Swaps → SRT → STEG → CLN → Other

This ensures CDS is taught before CLN products reference it, and IRS is taught before SRT/STEG products reference it.

### Revision 4: Reorder ELN products within family

Start with PPN (simplest), progress through RC variants, then autocallables, then exotic.

### Revision 5: Add Variance Swap

Add Variance Swap to Part 5.3 (Swaps). Requires adding realized variance and variance notional to Part 1.5 (Volatility) as foundational concepts.

### Revision 6: Separate Accumulators and Decumulators

Per directive, treat these as two separate product chapters.

### Revision 7: Add bridge paragraphs at Part 1 tier transitions

Between 1.6 (Correlation) and 1.7 (Rates), add a transition that reframes the reader's attention from equity concepts to rate concepts.

### Revision 8: Add "How to Read a Payoff Diagram" mini-section

Before the first payoff diagram appears (Part 1.2 Options), add a 0.5-page explanation of what payoff diagram axes represent: X = underlying price, Y = profit/loss, breakeven point, slope meaning.

### Revision 9: Add swap concept to Part 0 or early Part 1

A one-paragraph definition of "what is a swap" should appear before Part 1.7 references swaptions and before Part 2 references hedging with swaps. Proposed location: Part 0.5 (What Is a Derivative?) — mention swaps alongside futures and options as the three major derivative types.

### Revision 10: Update page and effort estimates

All audit estimates should be revised upward to reflect:
- 14-section product template (vs 9-section)
- Expanded Part 0 (15-20 pages new)
- ~49 products (vs ~42)
- Teaching-first writing style (inherently longer than documentation)

---

## 9. Revised Table of Contents (Summary)

```
PART 0 — HOW FINANCE WORKS (15-20 pages)
  0.1 What Is a Market?
  0.2 What Are Securities? (Stocks, Bonds, Interest, Yield)
  0.3 Risk, Return, and the Time Value of Money
  0.4 What Banks Actually Do
  0.5 What Is a Derivative? (Futures, Options, Swaps — one paragraph each)
  0.6 Why Structured Products Exist
  0.7 The Structured Products Desk

PART 1 — FOUNDATIONS (35-45 pages)
  1.1 Core Trading Concepts (Long/Short, Bid/Offer, P&L, Leverage, Liquidity)
  1.2 Options From Zero (including "How to Read a Payoff Diagram")
  1.3 Barriers and Digitals
  1.4 Greeks — How Risk Is Measured
  1.5 Volatility (including Variance as foundation for Variance Swaps)
  1.6 Correlation and Baskets
  [Bridge: From Equity to Rates]
  1.7 Rates and Yield Curves (including conceptual swap introduction)
  1.8 Credit Risk

PART 2 — STRUCTURED PRODUCTS FRAMEWORK (25-30 pages)
  2.1 What Is a Structured Product
  2.2 Product Construction Principles
  2.3 The Four-Leg Framework
  2.4 Capital Protection Spectrum
  2.5 Product Lifecycle
  2.6 Trade Lifecycle
  2.7 How Desks Hedge
  2.8 The Systems: A First Look (NEMO, Sophis, Murex primer)

PART 3 — PRODUCT TAXONOMY (10-15 pages)
  [Unchanged from audit]

PART 4 — PRODUCT COMPARISON MATRICES (15-20 pages)
  [Unchanged from audit, plus Variance Swap added to Swaps matrix]

PART 5 — PRODUCT DEEP DIVES (230-260 pages)
  5.1 Equity-Linked Notes (15 products — reordered: PPN first, Warrant last)
  5.2 Swaps (8 products — IRS, TRS, Equity, Variance, Currency, Commodity, CDS, VLSP)
  5.3 Structured Rate Trades (5 products)
  5.4 Steepener Notes (4 products)
  5.5 Credit-Linked Notes (5 products — now comes AFTER Swaps/CDS)
  5.6 Other Products (7 products — Accumulators and Decumulators separate)

PART 6 — OPERATIONS (25-30 pages)
  [Unchanged from audit, but systems primer in Part 2 reduces reader confusion]

PART 7 — QUICK REFERENCE (15-20 pages)
  [Expanded per directive: Glossary, Acronym Dictionary, Product Cheat Sheets,
   Decision Trees, Common Interview Questions, System Routing Guides]

Total: ~49 products, ~370-440 pages
```

---

## 10. Pre-Writing Checklist

Before Phase 1 writing begins, confirm:

- [ ] Part 0 expansion approved (7 sections vs 5)
- [ ] Systems primer in Part 2 approved (new section 2.8)
- [ ] Part 5 family reordering approved (ELN → Swaps → SRT → STEG → CLN → Other)
- [ ] ELN product reordering approved (PPN first, progressive complexity)
- [ ] Variance Swap addition approved (new product, 8 swaps total)
- [ ] Accumulators / Decumulators separation approved (2 products, not 1)
- [ ] 14-section product chapter template confirmed
- [ ] Revised page estimate acknowledged (~370-440 pages total)
- [ ] "No Unexplained Terminology Rule" validated for revised structure

**Status: Waiting for approval before beginning any writing.**
