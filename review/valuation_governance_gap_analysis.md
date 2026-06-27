# Valuation Governance — Gap Analysis

**Date:** 2026-06-25
**Scope:** Phase 5 audit — pricing, IPV, fair value hierarchy, reserves, Day One P&L
**Source:** Desk Bible v2 (22,620 lines, 49 products, 6 families)
**Method:** Word-boundary term counts + manual section review

---

## Executive Summary

This is the single largest gap area in the Desk Bible relative to its stated audience. The Bible teaches pricing concepts (spreads, curves, vol surfaces) as inputs to product valuation. But it does not teach the governance framework that controls valuation: how prices are independently verified, what reserves adjust the P&L, how products are classified under the Fair Value Hierarchy, or how Day One P&L is recognized. A Product Control professional — explicitly listed in every chapter's §5 Who Touches section — could not perform their core job functions using only the Bible.

---

## Term Count Evidence

### Pricing Concepts

| Term | Count | Assessment |
|------|:-----:|-----------|
| Fair Value | 8 | General usage; no methodology |
| Mid Price | 0 | Absent |
| Bid | 66 | Mostly in "bid-offer spread" context |
| Offer | 180 | Mostly in "bid-offer spread" context |
| OAS (Option-Adjusted Spread) | 3 | Mentioned, not explained |
| Discount Spread | 0 | Absent |
| Funding Spread | 11 | In product construction context |
| Credit Spread | 43 | Well covered in credit chapters |

### Market Data Inputs

| Term | Count | Assessment |
|------|:-----:|-----------|
| Yield Curve | 86 | Strong coverage; used throughout rate products |
| Discount Curve | 3 | Mentioned, not explained |
| Forward Curve | 2 | Mentioned, not explained |
| Vol Surface | 25 | Adequate coverage in equity and rate chapters |
| Vol Smile | 1 | Minimal |
| Vol Skew | 2 | Minimal |
| Correlation Surface | 0 | Absent; relevant for basket and multi-asset products |

### Valuation Governance

| Term | Count | Assessment |
|------|:-----:|-----------|
| IPV / Independent Price Verification | 24 | Mentioned in §5 Who Touches boilerplate; zero methodology |
| Fair Value Hierarchy | 0 | Absent |
| Level 1 (FVH) | 2 | Unrelated context (one is educational level reference) |
| Level 2 (FVH) | 1 | Unrelated context |
| Level 3 (FVH) | 0 | Absent |
| Price Testing | 0 | Absent |
| Valuation Governance | 0 | Absent |
| Valuation Committee | 0 | Absent |
| P&L Explain | 0 | Absent |

### Reserves

| Term | Count | Assessment |
|------|:-----:|-----------|
| Model Reserve | 1 | Line 19415: "Model reserve assessment" in options chapter §5 — no explanation |
| Bid-Offer Reserve | 0 | Absent |
| Liquidity Reserve | 0 | Absent |
| Day One Reserve | 0 | Absent |
| Parameter Uncertainty Reserve | 0 | Absent |
| Inception Profit Reserve | 0 | Absent |
| Close-Out Cost Reserve | 0 | Absent |

### Day One P&L

| Term | Count | Assessment |
|------|:-----:|-----------|
| Day 1 P&L / Day One P&L | 1 | Line 1071: "Net Day 1 P&L: approximately -$85" — in product construction context, no governance explanation |

---

## Detailed Gap Analysis

### 1. Pricing Concepts

| Aspect | Coverage Status | Evidence |
|--------|:--------------:|---------|
| Bid-offer spread as revenue source | COVERED | §7 How the Bank Makes Money in every chapter |
| Credit spread as pricing input | COVERED | 43 mentions; explained in CDS and CLN chapters |
| Yield curve construction | PARTIAL | 86 mentions; used as input but construction methodology not explained |
| Vol surface as pricing input | PARTIAL | 25 mentions; referenced in equity chapters but vol surface construction not taught |
| Correlation surface | MISSING | 0 mentions; critical for basket products (Worst-of, FTD) |
| Mid-price vs bid-offer | MISSING | "Mid Price" has 0 mentions; the concept of mid-market valuation is not explained |
| OAS methodology | MISSING | 3 mentions, all in passing |
| Discount curve vs yield curve | MISSING | Discount curve mentioned 3 times, no explanation of the distinction |
| Forward curve construction | MISSING | 2 mentions, no methodology |

**Severity:** MEDIUM
**Impact:** The Bible uses market data inputs (curves, surfaces) correctly as product pricing inputs. A reader would know that "yield curves drive IRS pricing" but would not know how a yield curve is constructed or calibrated. This is acceptable for a product-focused reference but limits a reader's ability to troubleshoot pricing discrepancies.

**Notable absence — Correlation Surface:** The Bible covers basket products (Worst-of Autocallable, FTD) that require correlation inputs. The FTD chapter (§5.4.4) explains correlation conceptually ("credit correlation modeling — borrowed from the equity world") but the correlation surface itself is never defined or discussed. This matters for pricing and IPV of multi-name products.

---

### 2. Independent Price Verification (IPV)

| Aspect | Coverage Status | Evidence |
|--------|:--------------:|---------|
| IPV exists as a function | COVERED | 24 mentions across §5 Who Touches sections |
| Typical §5 entry | BOILERPLATE | Pattern: "Independent Price Verification (IPV) of [component]" |
| What IPV actually is | MISSING | No definition of IPV as a process |
| How IPV is performed | MISSING | No methodology |
| IPV tolerance thresholds | MISSING | No explanation of what happens when a price deviates |
| IPV data sources (broker quotes, consensus services, model prices) | MISSING | Not mentioned |
| IPV escalation process | MISSING | What happens when IPV fails? Not explained |
| IPV frequency and reporting | MISSING | Not mentioned |
| Distinction between IPV and P&L attribution | MISSING | Not explained |

**Severity:** CRITICAL
**Impact:** IPV is the core daily function of Product Control — the role that appears in every chapter's §5 Who Touches section. The Bible mentions IPV 24 times but never explains what it is or how it works. A Product Control professional would know their job title includes "IPV" but would have no understanding of the process, thresholds, data sources, or escalation procedures.

**Evidence of the gap:** Every §5 Who Touches entry for Product Control follows this pattern:
- Line 2421: "Independent Price Verification (IPV) of call option"
- Line 2861: "Independent Price Verification (IPV) of put component"
- Line 10457: "Independent price verification"
- Line 19415: "Independent valuation. Vol surface verification. Model reserve assessment"

The parenthetical "(IPV)" suggests the Bible treats it as a term to define once and reference thereafter. But no definition exists anywhere in the manuscript.

---

### 3. Fair Value Hierarchy (IFRS 13 / ASC 820)

| Aspect | Coverage Status | Evidence |
|--------|:--------------:|---------|
| Fair Value Hierarchy concept | MISSING | 0 mentions of "Fair Value Hierarchy" |
| Level 1 (quoted prices in active markets) | MISSING | 0 relevant mentions |
| Level 2 (observable inputs) | MISSING | 0 relevant mentions |
| Level 3 (unobservable inputs) | MISSING | 0 mentions |
| Classification methodology | MISSING | Not explained |
| Transfer between levels | MISSING | Not explained |
| Disclosure requirements | MISSING | Not explained |
| Significance for structured products | MISSING | Not explained |

**Severity:** HIGH
**Impact:** Fair Value Hierarchy classification is mandatory under both IFRS and US GAAP. Every structured product must be classified. Most structured products are Level 2 (observable inputs like yield curves and vol surfaces) or Level 3 (unobservable inputs like correlation). The classification determines disclosure requirements, valuation governance intensity, and regulatory scrutiny. The Bible does not mention this framework at all.

**Why this matters for the Bible's products:**

| Product Family | Typical FVH Level | Key Unobservable Input | Bible Coverage of Input |
|----------------|:-----------------:|----------------------|------------------------|
| Equity-Linked Notes (18 products) | Level 2-3 | Correlation (basket), barrier discontinuity | Correlation absent; barrier covered |
| Swaps (5 products) | Level 2 | None for vanilla | Adequate |
| Rate-Structured Notes (10 products) | Level 2-3 | CMS convexity adjustment, callable rate vol | CMS covered; callable vol partial |
| Credit-Linked Notes (4 products) | Level 3 | Default correlation, recovery rate | Default correlation partial; recovery covered |
| Listed Products (2 products) | Level 1-2 | None for exchange-traded | Adequate |
| Exotic Products (10 products) | Level 2-3 | Various model-dependent inputs | Varies |

---

### 4. Reserves Taxonomy

This is the most complete gap in the entire Bible. Every reserve type relevant to structured products has zero or near-zero coverage.

| Reserve Type | Count | Purpose (Not Explained in Bible) | Typical Magnitude |
|-------------|:-----:|----------------------------------|-------------------|
| **Model Reserve** | 1 | Compensate for model limitations and parameter uncertainty | 0.5-5% of notional |
| **Bid-Offer Reserve** | 0 | Adjust mid-market valuation to exit price (bid for long, offer for short) | 0.1-2% of notional |
| **Liquidity Reserve** | 0 | Additional adjustment for illiquid positions beyond normal bid-offer | 0.5-10% of notional |
| **Day One Reserve** | 0 | Defer recognition of Day 1 profit on Level 3 products | Can be 100% of Day 1 |
| **Parameter Uncertainty Reserve** | 0 | Cover uncertainty in model calibration parameters | 0.2-3% of notional |
| **Inception Profit Reserve** | 0 | IFRS 9-mandated deferral of inception profit when inputs are unobservable | Regulatory driven |
| **Close-Out Cost Reserve** | 0 | Estimated cost to close or hedge the position in stress | Scenario-dependent |
| **Funding Reserve** | 0 | Adjustment for funding cost of uncollateralized positions | Position-dependent |

**Severity:** CRITICAL
**Impact:** Reserves are the mechanism by which Product Control adjusts front-office P&L to reflect economic reality. They are the primary output of Product Control's daily work alongside P&L attribution. A Product Control professional who does not understand reserves cannot:
1. Calculate the desk's true P&L (front-office P&L minus reserves = reported P&L)
2. Explain why reported P&L differs from front-office P&L
3. Challenge or validate reserve calculations
4. Understand why a new trade creates a Day One reserve

The single mention of "Model reserve assessment" (line 19415, options chapter §5) establishes that reserves exist but provides no framework for understanding them.

---

### 5. Day One P&L

| Aspect | Coverage Status | Evidence |
|--------|:--------------:|---------|
| Day One P&L concept | MINIMAL | Line 1071: "Net Day 1 P&L: approximately -$85" in product construction (§2.2) |
| Day One P&L recognition rules | MISSING | No IFRS 9 / ASC 820 explanation |
| Day One reserve mechanics | MISSING | Not mentioned |
| Amortization of Day One reserve | MISSING | Not mentioned |
| Observable vs unobservable inputs test | MISSING | Not explained |
| Revenue recognition implications | MISSING | Not explained |

**Severity:** HIGH
**Impact:** Day One P&L is one of the most contentious topics in structured products. When a product is sold, is the structuring margin immediately recognized as profit, or must it be deferred? The answer depends on whether the valuation uses observable inputs (immediate recognition) or unobservable inputs (deferral required). The Bible mentions Day 1 P&L once in a construction context but does not explain the governance framework. This is a regulatory and accounting requirement, not optional.

---

### 6. P&L Explain / P&L Attribution

| Aspect | Coverage Status | Evidence |
|--------|:--------------:|---------|
| P&L Explain concept | MISSING | 0 mentions of "P&L Explain" |
| P&L attribution methodology | PARTIAL | §5 Who Touches mentions "P&L attribution" in Product Control entries but no methodology |
| Greek-based P&L attribution | MISSING | Greeks are taught (well) but not connected to P&L attribution |
| Unexplained P&L | MISSING | Not mentioned |
| P&L attribution by risk factor | MISSING | Not explained |

**Severity:** HIGH
**Impact:** P&L attribution is listed as a Product Control responsibility in every chapter. The Bible teaches Greeks thoroughly (delta, gamma, vega, theta) and teaches P&L scenarios (§10 in every chapter). But it never connects these: "daily P&L can be explained by summing delta P&L + gamma P&L + vega P&L + theta P&L + unexplained." A reader would understand what delta is but not how to use it for P&L attribution.

---

### 7. Valuation Governance Framework

| Aspect | Coverage Status | Evidence |
|--------|:--------------:|---------|
| Valuation governance concept | MISSING | 0 mentions |
| Valuation Committee | MISSING | Not mentioned |
| Valuation Policy | MISSING | Not mentioned |
| Price testing process | MISSING | 0 mentions |
| Escalation hierarchy | MISSING | Not explained |
| Model approval / validation | MISSING | Model risk mentioned (§1.6) but model governance absent |
| New product approval process | MISSING | Not explained |
| Prudent Valuation (CRR Article 105) | MISSING | Not mentioned |

**Severity:** HIGH
**Impact:** Valuation governance is the organizational framework that ensures prices are correct and controls are effective. Every bank has a Valuation Committee, a Valuation Policy, and defined escalation procedures. The Bible does not mention any of these. A reader would not know who approves prices, what happens when a price is disputed, or what the escalation path is.

---

## Gap Severity Summary

| Category | Severity | Term Evidence | Rationale |
|----------|:--------:|:------------:|-----------|
| Reserves taxonomy | CRITICAL | All types 0-1 mentions | Core Product Control function; zero coverage |
| IPV methodology | CRITICAL | 24 mentions, 0 explanation | Named as responsibility; never defined |
| Fair Value Hierarchy | HIGH | 0 mentions | Mandatory regulatory classification; absent |
| Day One P&L governance | HIGH | 1 mention, 0 governance | Accounting/regulatory requirement; not explained |
| P&L Explain / Attribution | HIGH | 0 mentions | Listed as PC responsibility; no methodology |
| Valuation governance framework | HIGH | 0 mentions | Organizational controls; absent |
| Pricing concepts | MEDIUM | Varies | Inputs covered; methodology partial |
| Market data inputs | MEDIUM | Curves strong; correlation absent | Adequate for product understanding, insufficient for troubleshooting |

---

## The Product Control Gap in Context

The Bible's §5 Who Touches section in every chapter lists Product Control's responsibilities. Here is the pattern:

| Chapter Type | Typical §5 Product Control Entry |
|-------------|----------------------------------|
| Equity-Linked Notes | "Daily P&L attribution between ZCB accretion and option MTM. Independent Price Verification (IPV) of [option type]" |
| Swaps | "Daily P&L attribution for [swap] book. Independent price verification" |
| Credit-Linked Notes | "Verifies [credit] calculations. Reconciles [pricing inputs] between systems" |
| Rate-Structured Notes | "Daily P&L attribution. Independent Price Verification (IPV). Curve verification" |

Every entry assumes the reader knows:
- What P&L attribution means and how to do it
- What IPV means and how to perform it
- What tolerance thresholds apply
- What to do when verification fails

None of these are explained anywhere in the manuscript.

---

## Structural Observation

The Bible teaches the "what" and "how" of products comprehensively. It teaches the "who" through the §5 Who Touches framework. But for Product Control specifically, it names the activities without teaching them. This creates an asymmetry: a Trader reading the Bible would understand their product and its risks. A Product Control professional reading the same material would understand the product but not their own job.

The remediation path:
1. **Part 0 addition (~2,000 words):** A new foundation section covering IPV methodology, Fair Value Hierarchy, reserves taxonomy, Day One P&L, and P&L attribution. This would be referenced from every chapter's §5 Who Touches entry.
2. **No per-chapter changes needed.** The §5 entries are correct as job descriptions. They simply need the referenced framework to exist.
3. **Priority:** This is the highest-priority content gap identified in the Phase 3-6 audit cycle. Reserves and IPV are daily operational activities, not theoretical concepts that can be deferred.
