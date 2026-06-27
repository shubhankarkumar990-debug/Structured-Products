# Operations and Booking Gap Analysis

**Audit Phase**: 8 — Operations, Booking, Corporate Actions
**Scope**: Desk Bible v2 (22,620 lines, 49 products, 1,078 sections)
**Date**: 2026-06-25
**Verdict**: MIXED — product-level booking is strong; cross-product operational processes are absent

---

## 1. Executive Summary

The Desk Bible has a structural advantage in operations coverage: every one of 49 chapters contains §16 (Booking and Systems) and §17 (Red Flags), providing product-specific booking guidance across the entire universe. This is genuinely useful. The gap is not in WHAT to book — it is in HOW the operational infrastructure works. P&L Explain (0 mentions), Cash Reconciliation (0 mentions), Static Data (0 mentions), and Golden Source (0 mentions) are entirely absent. A reader knows how to book each product but does not understand the daily operational processes that surround the booking.

---

## 2. Term Frequency Evidence

### 2.1 Operational Roles

| Term | Count | Assessment |
|------|------:|------------|
| Front Office | 11 | Present — role boundaries described |
| Middle Office | 9 | Present — role boundaries described |
| Back Office | 9 | Present — role boundaries described |
| Product Control | 118 | Extensively referenced — WHAT PC does, not HOW |
| Operations | 158 | Heavily used — but as a general term, not a process framework |

### 2.2 P&L and Reconciliation

| Term | Count | Assessment |
|------|------:|------------|
| PnL Explain / P&L Explain | 0 | **CRITICAL GAP** — the single most important daily PC activity |
| P&L Attribution | 0 | Absent — the methodology behind P&L explain |
| Cash Reconciliation | 0 | **CRITICAL GAP** — daily operational requirement |
| Position Reconciliation | 0 | Absent |
| Break Resolution | 0 | Absent — despite "Trade Break" being a key ops concept |
| Independent Price Verification (IPV) | 0* | *Term "IPV" not used; concept described as a PC activity but process not explained |

### 2.3 Data Infrastructure

| Term | Count | Assessment |
|------|------:|------------|
| Static Data | 0 | **SIGNIFICANT GAP** — foundational to booking accuracy |
| Golden Source | 0 | Absent — the concept of authoritative data sources |
| Reference Data | 0 | Absent |
| Trade Repository | 0 | Absent (regulatory reporting context) |
| Market Data | — | Mentioned in passing in pricing contexts, not as infrastructure |

### 2.4 Settlement and Currency

| Term | Count | Assessment |
|------|------:|------------|
| Trade Currency | 0 | Absent |
| Settlement Currency | 0 | Absent |
| Counterparty | 92 | Well covered — used extensively in credit and structuring context |
| Guarantor | 1 | Minimal — mentioned once in CLN context |

### 2.5 Early Termination and Optionality

| Term | Count | Assessment |
|------|------:|------------|
| Breakability | 0 | Absent as a concept |
| Early Redemption | 28 | Present — covered in autocallable and callable contexts |
| Optional Redemption | 0 | Absent as a distinct concept |
| Investor Put | 0 | **GAP** — the investor's right to redeem early |
| Issuer Call | 61 | Well covered — central to callable product family |

---

## 3. What the Bible DOES Cover (Strengths)

### 3.1 Product-Level Booking — §16 Booking and Systems (49 chapters)

This is a genuine strength. Every product chapter contains:

| Component | Coverage Quality | Notes |
|-----------|:----------------:|-------|
| Booking system (NEMO/Sophis/Murex) | 8/10 | System identified per product with practical context |
| Key booking fields | 7/10 | Product-specific fields listed (notional, strike, barrier, maturity, etc.) |
| Lifecycle events | 8/10 | Coupon payments, barrier observations, maturity, autocall events |
| System-specific guidance | 7/10 | How to represent the product in each system |

**Example of strong coverage**: A reader can learn that an Autocallable Reverse Convertible in NEMO requires: underlying ISIN, strike level, barrier level, autocall trigger levels per observation date, coupon rate, observation frequency, and settlement convention. This is operationally actionable.

### 3.2 Red Flags — §17 Red Flags (49 chapters)

| Component | Coverage Quality | Notes |
|-----------|:----------------:|-------|
| Booking errors to watch for | 8/10 | Product-specific warnings (wrong barrier type, missed observation date) |
| Common mistakes | 7/10 | Cross-referenced with §20 Common Mistakes |
| Operational risks | 7/10 | Practical warnings about what goes wrong |

**Total red flag entries**: ~245 across 49 products (from §20 Common Mistakes alone).

### 3.3 Trade Lifecycle — Part 2 §2.6

| Component | Coverage Quality | Notes |
|-----------|:----------------:|-------|
| Lifecycle stages | 7/10 | Pre-trade, Execution, Booking, Daily life, Events, Maturity |
| FO/MO/BO responsibilities per stage | 6/10 | High-level table — useful but not detailed |
| Lifecycle event handling | 5/10 | Mentioned at product level, not as a process |

### 3.4 Systems — Part 2 §2.8

| Component | Coverage Quality | Notes |
|-----------|:----------------:|-------|
| System overview (NEMO, Sophis, Murex) | 7/10 | Practical description of each system |
| System selection per product | 8/10 | Covered in every §16 |
| System integration | 2/10 | How systems talk to each other — barely covered |

### 3.5 Counterparty — 92 mentions

Counterparty is well covered across credit products (CLN, CDO, CDS references) and in structuring context. This is appropriate — counterparty risk is central to the product discussion.

---

## 4. What the Bible DOES NOT Cover (Gaps)

### 4.1 P&L Explain / P&L Attribution — CRITICAL (0 mentions)

| Gap | Operational Reality | Bible Coverage |
|-----|---------------------|----------------|
| Daily P&L explain process | FO produces estimated P&L; PC independently verifies and attributes | ABSENT |
| P&L attribution methodology | Decomposition into Greeks (delta, gamma, vega, theta, rho), new deal, fees, funding, reserves | ABSENT |
| Unexplained P&L | The residual that cannot be attributed — triggers investigation | ABSENT |
| P&L explain thresholds | Tolerance levels for unexplained P&L before escalation | ABSENT |
| Product-specific P&L explain challenges | Autocallable path-dependency, CDO correlation sensitivity, quanto FX attribution | ABSENT |

**Why this matters**: P&L explain is the single most frequently performed analytical activity in Product Control. It is the daily heartbeat of a structured products desk. A PC analyst joining from this Bible would understand what products exist but not how to explain their P&L.

**Bible's partial coverage**: The Bible mentions "Daily P&L attribution" as a Product Control activity (part of the 118 PC references). But it never explains the methodology, the decomposition, or the product-specific challenges.

### 4.2 Cash Reconciliation — CRITICAL (0 mentions)

| Gap | Operational Reality | Bible Coverage |
|-----|---------------------|----------------|
| Cash rec process | Matching expected cash flows against actual bank movements | ABSENT |
| Break identification | Finding and classifying discrepancies | ABSENT |
| Break resolution | Investigating and resolving cash breaks | ABSENT |
| Aging analysis | Tracking how long breaks remain open | ABSENT |
| Product-specific challenges | Autocallable conditional coupons, barrier knock-in/out cash impact, CLN credit event payments | ABSENT |

### 4.3 Static Data — SIGNIFICANT (0 mentions)

| Gap | Operational Reality | Bible Coverage |
|-----|---------------------|----------------|
| Static data concept | Master reference data (counterparty, instrument, market data sources) | ABSENT |
| Static data setup | Creating a new instrument in the system (fields, validations) | ABSENT |
| Static data maintenance | Updating records for corporate actions, market changes | ABSENT |
| Data quality | Validation rules, exception handling, audit trail | ABSENT |
| Golden source | Authoritative system of record per data element | ABSENT |

**Impact**: §16 tells readers WHAT fields to book. Static data management tells them WHERE those fields come from, how they are validated, and what happens when they are wrong.

### 4.4 Trade Lifecycle Processes

| Gap | Operational Reality | Bible Coverage |
|-----|---------------------|----------------|
| Trade capture workflow | Who enters the trade, who confirms, who approves | Mentioned at high level in §2.6, not as a process |
| Trade amendment process | How to amend a booked trade (approval chain, audit trail) | ABSENT |
| Trade cancellation process | How to cancel a trade (approval, P&L impact, accounting) | ABSENT |
| Novation | Transfer of trade to new counterparty | ABSENT |
| Partial termination | Reducing notional on an existing trade | ABSENT |
| Trade confirmation | Matching trade details with counterparty (paper/electronic) | ABSENT |

### 4.5 Corporate Actions — PARTIAL

#### What IS covered:

| Topic | Count | Coverage Quality |
|-------|------:|:----------------:|
| Stock Split | 12 | Mentioned in context of barrier/strike adjustment |
| Merger | 6 | Mentioned in passing — impact on underlying |
| Acquisition | 7 | Mentioned in passing |
| Spin-Off | 1 | Single mention |
| Dilution | 1 | Single mention |

The Bible mentions corporate actions when they affect structured products (barrier adjustment after a stock split). This is appropriate product-level coverage.

#### What is NOT covered:

| Gap | Operational Reality | Bible Coverage |
|-----|---------------------|----------------|
| Reverse Split | 0 | Absent |
| Rights Issue | 0 | Absent |
| Bonus Issue | 0 | Absent |
| Tender Offer | 0 | Absent |
| Delisting | 0 | Absent — critical for single-stock structured products |
| Adjustment methodology | 0 | HOW to calculate new strike/barrier after corporate action |
| ISDA fallback provisions | 0 | Standard contractual provisions for equity derivatives |
| Ratio calculation | 0 | Mechanics of adjustment ratio computation |
| Cash-in-lieu | 0 | When physical adjustment is replaced by cash compensation |
| Extraordinary events | 0 | Nationalization, insolvency, tax law changes |

**Impact**: A reader encounters a stock split on an autocallable's underlying. They know (from the Bible) that the barrier needs adjustment. They do NOT know: what adjustment method applies, who calculates it, what ISDA provisions govern it, or what happens if the adjustment is disputed.

### 4.6 Independent Price Verification (IPV) and Reserves

| Gap | Operational Reality | Bible Coverage |
|-----|---------------------|----------------|
| IPV process | Independent marking of positions using external sources | Described as a PC activity, process not explained |
| IPV methodology | Consensus pricing, broker quotes, model-independent marks | ABSENT |
| IPV challenges per product | Illiquid exotics, correlation products, path-dependent payoffs | ABSENT |
| Reserve types | Bid-offer, model, liquidity, concentration, operational | ABSENT |
| Reserve calculation | How each reserve type is computed | ABSENT |
| Reserve governance | Approval, review frequency, release criteria | ABSENT |
| Day 1 P&L | Profit/loss recognized at trade inception — accounting treatment | ABSENT |

### 4.7 Trade and Settlement Currency

| Gap | Operational Reality | Bible Coverage |
|-----|---------------------|----------------|
| Multi-currency booking | How trades in non-base currency are booked and valued | ABSENT |
| FX settlement risk | Settlement in different currencies on different value dates | ABSENT |
| Quanto mechanics (operational) | How quanto products settle — the FX component in booking | Quanto concept covered (8 mentions), operational mechanics absent |
| CLS settlement | Continuous Linked Settlement for FX risk mitigation | ABSENT |

---

## 5. Coverage Heatmap by Operational Domain

| Domain | Product-Specific Coverage | Cross-Product Process | Overall |
|--------|:-------------------------:|:---------------------:|:-------:|
| Booking (what to book) | 8/10 | 3/10 | 6/10 |
| Lifecycle events | 7/10 | 2/10 | 5/10 |
| Systems (which system) | 8/10 | 4/10 | 6/10 |
| Red flags/warnings | 8/10 | N/A | 8/10 |
| P&L explain | 0/10 | 0/10 | 0/10 |
| Cash reconciliation | 0/10 | 0/10 | 0/10 |
| Static data | 0/10 | 0/10 | 0/10 |
| Corporate actions | 4/10 | 0/10 | 2/10 |
| IPV and reserves | 1/10 | 0/10 | 1/10 |
| Settlement/currency | 1/10 | 0/10 | 1/10 |
| Trade amendments/cancellations | 0/10 | 0/10 | 0/10 |
| Confirmations | 0/10 | 0/10 | 0/10 |

---

## 6. The Core Pattern

The Bible's operational coverage follows a consistent pattern:

```
PRESENT:  What to do with THIS product  (§16 Booking, §17 Red Flags)
ABSENT:   How the process works ACROSS products  (P&L explain, recon, IPV)
```

This is a natural consequence of the product-chapter architecture. Each chapter covers its own product deeply. But operational processes (P&L explain, cash reconciliation, IPV, corporate actions) are inherently cross-product. They cannot live in a single product chapter — they belong in infrastructure content.

---

## 7. Audience Impact Assessment

| Role | Can learn their operational responsibilities from the Bible? | Assessment |
|------|--------------------------------------------------------------|------------|
| Trader | Yes — knows what to trade, how products are booked, what to watch for | PASS |
| Structurer | Yes — knows product mechanics, booking systems, lifecycle | PASS |
| Product Control | Partially — knows what PC does per product, not HOW to do P&L explain, IPV, reserves | PARTIAL |
| Operations / Back Office | Partially — knows what to book, not how to reconcile, confirm, or settle | PARTIAL |
| Middle Office | No — no process framework for trade lifecycle management | FAIL |
| Settlements | No — no settlement process, currency handling, or cash reconciliation | FAIL |

---

## 8. Recommendation

The product-level booking coverage (§16, §17) is a genuine asset and should not be modified. The gap is in cross-product operational infrastructure. This requires new content, not modification of existing content.

**Minimum**: Add a Foundation chapter covering P&L explain methodology, IPV process, and cash reconciliation basics (~15-20 pages)

**Recommended**: Include as a module in the proposed Infrastructure Handbook covering P&L explain, IPV, reserves, corporate actions, settlement, and static data (~40-50 pages)

**Ideal**: Dedicated Operations Reference covering all operational processes with product-specific examples drawn from each of the 49 chapters (~80-100 pages)

See infrastructure_handbook_recommendation.md for the final verdict and options analysis.
