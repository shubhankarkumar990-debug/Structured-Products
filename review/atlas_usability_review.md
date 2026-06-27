# Atlas Usability Review — Five Target Audiences

**Date:** 2026-06-22
**Artifact:** `production/product_dna_atlas.md`
**Scope:** Educational usability assessment for all 5 target audiences

---

## Target Audiences

1. **New Analyst** — Junior hire, first week on structured products desk
2. **Interview Candidate** — Preparing for structured products role
3. **Middle Office / Operations** — Trade support, booking, lifecycle
4. **Senior Structurer** — Quick reference, product comparison
5. **Sales / Relationship Manager** — Client-facing product discussion

---

## Audience 1: New Analyst

### What They Need
- Learn what each product IS in plain language
- Understand which products to learn first
- Build mental model of product families
- Connect products to desk workflows

### Atlas Usability Assessment

| Capability | Score | Notes |
|-----------|:-----:|-------|
| Product identification | 9/10 | 16-field card covers identity completely |
| Learning path guidance | 4/10 | No "start here" markers; Family View lists products without priority |
| Plain language accessibility | 6/10 | Building blocks use technical component names; ~8 cards list parts without labels |
| Desk workflow connection | 5/10 | Primary System field present but no booking/lifecycle context |
| Family mental model | 8/10 | Appendix C evolution chains excellent for understanding product relationships |

### Key Gaps

**Gap 1: No suggested learning order**

A new analyst opening the Atlas sees 49 cards with no guidance on which 5 to learn first. The Complexity View partially addresses this (start with tier 1-2), but no explicit "Day 1 products" marker exists.

**Recommendation:** Add a "Start Here" section with the 5 anchor products: PPN (5.1.1), IRS (5.2.1), IR Callable (5.3.1), Vanilla STEG (5.4.1), Vanilla CLN (5.5.1), plus SD (5.6.1) and FWD (5.6.2).

| Impact | Effort | Priority |
|:------:|:------:|:--------:|
| HIGH | LOW | HIGH |

**Gap 2: Building blocks need component labels**

PPN card: "Zero-coupon bond (principal protection) + European call option (equity upside)" — parenthetical labels explain what each component DOES. ~8 other cards list components without labels:

- Phoenix: "Fixed-rate note + short down-and-in put + binary coupon options + autocall triggers" — what does each piece contribute?
- CRA ELN: "Fixed note + strip of daily digital options on equity index + short Bermudan call" — reader needs to know daily digitals = coupon source

| Impact | Effort | Priority |
|:------:|:------:|:--------:|
| MEDIUM | MEDIUM | MEDIUM |

**Gap 3: Jargon in one-line summaries**

5 summaries use internal/technical language a new analyst won't know:
- "Correlation premium" (WOAC)
- "Cumulative coupon mechanism" (SNOW)
- "CDS-like exposure" (Vanilla CLN — assumes CDS knowledge)

| Impact | Effort | Priority |
|:------:|:------:|:--------:|
| MEDIUM | LOW | MEDIUM |

---

## Audience 2: Interview Candidate

### What They Need
- Memorizable facts for each product
- Clear differentiation between similar products
- Confident answers to "what's the most important Greek?"
- Product walkthrough ability

### Atlas Usability Assessment

| Capability | Score | Notes |
|-----------|:-----:|-------|
| Memorizable facts | 8/10 | "Remember These 3 Things" is well-designed for this |
| Product differentiation | 7/10 | Within-family differentiation good; cross-family needs Matrix |
| Greek/metric knowledge | 5/10 | 17 generic "Watch: Delta" answers are interview liabilities |
| Walkthrough ability | 7/10 | Good for 42/49 products; 7 have multiple weak fields |

### Key Gaps

Covered in detail in `review/interview_readiness_review.md`. Summary:
- 17 generic watch metrics (HIGH priority)
- 2 truncated summaries (HIGH priority)
- 5 vague summaries (HIGH priority)
- 73% of cards fully interview-ready

| Impact | Effort | Priority |
|:------:|:------:|:--------:|
| HIGH | MEDIUM | HIGH |

---

## Audience 3: Middle Office / Operations

### What They Need
- System field (where is this product booked?)
- ISDA requirement (what documentation?)
- Maturity and coupon type (lifecycle events)
- Quick product identification by abbreviation

### Atlas Usability Assessment

| Capability | Score | Notes |
|-----------|:-----:|-------|
| System identification | 9/10 | Primary System field on every card; Murex/NEMO/Sophis coverage clear |
| Documentation requirements | 9/10 | ISDA Required field explicit with reasoning |
| Lifecycle event awareness | 7/10 | Maturity Profile + Coupon Type cover basics; no payment schedule detail |
| Quick lookup | 8/10 | Alphabetical View + abbreviation field; Ctrl+F works well |

### Key Gaps

**Gap 1: No lifecycle event summary**

Operations needs to know: when do coupons pay? When are barrier observations? When can autocall trigger? The Atlas provides Maturity Profile and Coupon Type but not observation frequency.

This is out of scope for the DNA Atlas — lifecycle detail belongs in the individual chapters (§8-§12). The Atlas correctly provides the system booking identifier and documentation requirements.

**No Atlas changes recommended for this audience.** Gaps are architectural (chapter-level detail) not Atlas-level.

| Impact | Effort | Priority |
|:------:|:------:|:--------:|
| — | — | NONE |

---

## Audience 4: Senior Structurer

### What They Need
- Quick reference for product details across the universe
- Complexity scoring rationale for client discussions
- Building blocks for structuring conversations
- Cross-product comparison for recommendation

### Atlas Usability Assessment

| Capability | Score | Notes |
|-----------|:-----:|-------|
| Quick reference | 9/10 | 16-field card is exactly right for quick lookup |
| Complexity rationale | 8/10 | Present on all cards; ~14 could be more explanatory |
| Building blocks | 9/10 | Strongest field in the Atlas across all cards |
| Cross-product comparison | 6/10 | Requires reading multiple cards; no side-by-side view |

### Key Gaps

**Gap 1: No comparison capability**

A structurer choosing between Phoenix and Autocallable for a client needs side-by-side fields. The Atlas only supports sequential card reading. The Comparison Matrix (not yet generated) will address this directly.

**Gap 2: Evolution chains lack pricing implications**

Appendix C shows PPN → RC → Phoenix complexity progression but doesn't note that each step adds optionality premium. A structurer knows this, but the Atlas could surface it for desk discussions.

| Impact | Effort | Priority |
|:------:|:------:|:--------:|
| LOW | LOW | LOW |

---

## Audience 5: Sales / Relationship Manager

### What They Need
- Client-friendly product descriptions
- "Why would a client buy this?" answers
- Risk description they can convey to clients
- Product suitability indicators (Primary Buyer field)

### Atlas Usability Assessment

| Capability | Score | Notes |
|-----------|:-----:|-------|
| Client-friendly descriptions | 6/10 | One-line summaries vary; 5 use jargon, 2 truncated |
| Client motivation | 6/10 | Primary Buyer + one-liner together = OK; weaker for 7 products |
| Conveyable risk | 8/10 | Primary Risk is concrete and specific — good for client conversations |
| Suitability indicators | 8/10 | Primary Buyer maps to client segmentation (retail, PB, institutional) |

### Key Gaps

**Gap 1: One-line summaries need client-outcome framing**

Sales needs "what does this DO for the client" language. Current strong examples:
- IRS: "Transform fixed-rate exposure to floating or vice versa" — client action
- FWD: "Lock in future purchase/sale price" — client benefit
- SD: "Replace savings allocation with market-linked upside" — client outcome

Weak examples use structure language, not outcome language:
- VarSwap: "Pure vol exposure" → should be "Trade volatility without directional risk"
- VLSP: "Tailored rate hedge" → should be "Custom interest rate protection sized to specific liability"
- CDO: "Credit risk transfer via tranching" → should be "Offload credit risk to investors willing to take specific loss layers"

| Impact | Effort | Priority |
|:------:|:------:|:--------:|
| HIGH | LOW | HIGH |

**Gap 2: Capital Protection column not prominent enough in views**

Sales qualifying a client conversation needs to know immediately: "Is the principal at risk?" The Capital Protection field exists on every card, and Family View includes it, but the Complexity View and Alphabetical View omit it. A sales RM scanning the Complexity View can't quickly filter for capital-protected products.

| Impact | Effort | Priority |
|:------:|:------:|:--------:|
| MEDIUM | LOW | MEDIUM |

---

## Cross-Audience Summary

| Audience | Overall Score | Top Gap | Priority |
|----------|:------------:|---------|:--------:|
| New Analyst | 6.4 / 10 | No learning path guidance | HIGH |
| Interview Candidate | 6.8 / 10 | Generic watch metrics | HIGH |
| Middle Office | 8.3 / 10 | None (gaps are chapter-level) | NONE |
| Senior Structurer | 8.0 / 10 | No side-by-side comparison | DEFERRED (Matrix) |
| Sales / RM | 7.0 / 10 | Jargon in summaries | HIGH |

---

## Consolidated Recommendations

| # | Recommendation | Audiences Helped | Impact | Effort | Priority |
|---|---------------|:----------------:|:------:|:------:|:--------:|
| 1 | Fix 2 truncated summaries | All 5 | HIGH | LOW | **HIGH** |
| 2 | Rewrite 5 vague summaries (client-outcome framing) | Analyst, Interview, Sales | HIGH | LOW | **HIGH** |
| 3 | Replace 17 generic "Watch: Delta" with product-specific | Interview, Structurer | HIGH | MEDIUM | **HIGH** |
| 4 | Add "Start Here" anchor products section | Analyst | HIGH | LOW | **HIGH** |
| 5 | Add parenthetical labels to ~8 dense building-block lines | Analyst, Interview | MEDIUM | MEDIUM | **MEDIUM** |
| 6 | Add Capital Protection to Complexity and Alphabetical views | Sales, Analyst | MEDIUM | LOW | **MEDIUM** |
| 7 | Add family introductions with learning path | Analyst, Sales | MEDIUM | LOW | **MEDIUM** |
| 8 | Add parenthetical glosses to 5 technical watch metrics | Interview, Analyst | MEDIUM | LOW | **MEDIUM** |
| 9 | Add mechanism labels to ~8 expert-only hedges | Interview | LOW | MEDIUM | **LOW** |
| 10 | Enhance ~14 complexity rationales with "because" clause | Structurer | LOW | LOW | **LOW** |

---

## Verdict

The Atlas serves **Middle Office (8.3/10) and Senior Structurers (8.0/10) well today**. It is **adequate but improvable** for New Analysts (6.4), Sales (7.0), and Interview Candidates (6.8). The 4 HIGH-priority fixes (#1-4) would raise all audiences to 7.5+ with modest effort. The MEDIUM fixes would push toward 8.5+.

No modifications authorized by this review. Recommendations documented for future optimization pass.

---

*Atlas usability review complete.*
