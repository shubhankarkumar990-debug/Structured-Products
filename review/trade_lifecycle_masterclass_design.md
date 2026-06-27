# Trade Lifecycle Masterclass — Design Review

**Date:** 2026-06-21
**Proposed Section:** Part 2.9 — Trade Lifecycle Masterclass
**Framework:** v1.3.1 (FROZEN)
**Purpose:** Assess design for deep-dive trade lifecycle section
**Implementation:** After 49/49, during harmonization

---

## 1. Rationale

Section 2.6 (Trade Lifecycle) provides a 15-line overview table of who does what when. Every product chapter §13 (Lifecycle) teaches the product-specific lifecycle. But no section teaches the *mechanics* of each lifecycle stage in depth — what systems are involved, what data flows, what can go wrong, and how the stages connect.

The Trade Lifecycle Masterclass fills this gap: a single deep-dive reference that Operations, Product Control, and Risk can use as their primary learning path entry point.

---

## 2. Recommended Placement

**Section 2.9** — after Section 2.8 (Systems Primer), completing Part 2.

**Rationale:** Part 2 covers the desk context. Section 2.8 introduces the systems (Murex, NEMO, Sophis). Section 2.9 teaches how trades flow *through* those systems across their entire life.

**Alternative considered:** Part 3 (Product Maps). Rejected — lifecycle is operational infrastructure, not product-specific. Belongs in Part 2 with other desk mechanics.

---

## 3. Dependencies

| Prerequisite | Section | Why Needed |
|-------------|---------|-----------|
| FO/MO/BO roles | 2.1 | Who is responsible at each stage |
| Product construction | 2.2 | What is being booked |
| Four-leg framework | 2.3 | How complex products are decomposed in systems |
| Product lifecycle | 2.5 | Product perspective (complement to trade perspective) |
| Trade lifecycle overview | 2.6 | Summary that 2.9 expands |
| Hedging | 2.7 | Hedge lifecycle runs parallel to trade lifecycle |
| Systems | 2.8 | Which system handles each stage |

---

## 4. Learning Objectives

| # | Objective |
|:-:|-----------|
| 1 | Trace a structured product trade from client inquiry through final settlement |
| 2 | Identify the system, responsible team, and key data at each lifecycle stage |
| 3 | Understand what trade capture involves and why booking errors are costly |
| 4 | Explain the daily valuation process and mark-to-market mechanics |
| 5 | Describe how risk monitoring connects to P&L explain |
| 6 | Understand Product Control's independent price verification role |
| 7 | Walk through settlement mechanics for standard maturity and early termination |
| 8 | Identify the most common lifecycle failures and their operational impact |

---

## 5. Section Structure

### 5.1 Trade Capture

| Topic | Content | Est. Words |
|-------|---------|:----------:|
| Pre-trade workflow | Client inquiry → pricing request → structurer designs → risk approval → compliance check → client approval | 300 |
| Trade entry | Term sheet fields → system booking → static data → counterparty setup | 300 |
| Booking validation | Four-eye check, component verification, Greek sanity check | 200 |
| Common errors | Wrong notional, wrong barrier level, wrong observation dates, missing legs | 200 |
| **Subtotal** | | **1,000** |

### 5.2 Booking

| Topic | Content | Est. Words |
|-------|---------|:----------:|
| System selection | Which system for which product (Murex = equity/rates, NEMO = credit, Sophis = risk) | 200 |
| Four-leg booking | How complex products are decomposed into bookable legs | 300 |
| Static data requirements | Underlying, barrier levels, observation schedule, coupon formula, settlement conventions | 200 |
| Confirmation and matching | Trade confirmation to counterparty, matching process, dispute resolution | 200 |
| **Subtotal** | | **900** |

### 5.3 Valuation (Daily Life)

| Topic | Content | Est. Words |
|-------|---------|:----------:|
| Mark-to-market | Daily valuation using pricing models. Market data inputs: spot, vol surface, rates, credit spreads | 300 |
| P&L explain | Breaking P&L into components: delta P&L, vega P&L, theta, rho, credit, unexplained. Attribution | 400 |
| Model vs market | When model price diverges from market — IPV (Independent Price Verification), reserve adjustments | 300 |
| Fixing and observation | Daily/periodic observation of underlying levels. Barrier monitoring. Coupon determination | 200 |
| **Subtotal** | | **1,200** |

### 5.4 Risk

| Topic | Content | Est. Words |
|-------|---------|:----------:|
| Daily risk reporting | Greek exposures, stress scenarios, limit monitoring | 300 |
| Limit framework | Notional limits, Greek limits, concentration limits, loss limits | 200 |
| Stress testing | What-if scenarios: market crash, rate spike, correlation break, credit event | 200 |
| Escalation | When limits are breached — notification chain, forced reduction, management override | 200 |
| **Subtotal** | | **900** |

### 5.5 Product Control

| Topic | Content | Est. Words |
|-------|---------|:----------:|
| Independent valuation | Product Control reprices trades independently from the trader's model | 300 |
| P&L verification | Comparing trader P&L to Product Control P&L. Investigating discrepancies | 200 |
| Reserve management | Day-one P&L reserves, model reserves, bid-offer reserves | 200 |
| Month-end / quarter-end | Formal P&L sign-off, reserve adequacy review, audit trail | 200 |
| **Subtotal** | | **900** |

### 5.6 Settlements

| Topic | Content | Est. Words |
|-------|---------|:----------:|
| Coupon payments | Calculation, authorization, payment instruction, nostro/vostro | 200 |
| Barrier/autocall events | Event determination, notification to counterparty, settlement calculation | 200 |
| Credit events | ISDA Determinations Committee, auction, physical vs cash settlement | 200 |
| Failed settlements | Causes, consequences, resolution process | 150 |
| **Subtotal** | | **750** |

### 5.7 Maturity and Termination

| Topic | Content | Est. Words |
|-------|---------|:----------:|
| Standard maturity | Final fixing, payoff calculation, settlement, position close-out | 200 |
| Early termination | Autocall, knock-out, TARN target reached, issuer call | 200 |
| Unwind / novation | Client requests early exit — unwind pricing, novation to third party | 200 |
| Post-trade cleanup | Position reconciliation, system archival, audit trail completion | 150 |
| **Subtotal** | | **750** |

### 5.8 End-to-End Worked Example

One complete lifecycle walkthrough for a Phoenix Autocallable:
- Day 0: Client inquiry, pricing, booking
- Month 3: First observation — below barrier, no coupon
- Month 6: Above barrier, coupon paid + memory coupon
- Month 9: Above initial — autocall triggers
- Settlement: Early redemption at par + final coupon

Est. words: **600**

### Total

| Metric | Value |
|--------|:-----:|
| Word count | ~7,000 |
| Pages (est.) | 14-16 |
| Visual assets | 6-8 |

---

## 6. Visual Requirements

| # | Visual | Type | Purpose |
|:-:|--------|------|---------|
| 1 | End-to-end lifecycle timeline | Timeline | All 7 stages on one horizontal axis |
| 2 | Trade capture flow | Flow | Client → Structurer → Risk → Compliance → Booking |
| 3 | Four-leg booking diagram | Structure | Product → 4 legs → system entries |
| 4 | Daily valuation cycle | Flow | Market data → Model → MTM → P&L → Risk → Product Control |
| 5 | P&L explain waterfall | Waterfall | Delta + Vega + Theta + Rho + Credit + Unexplained = Total |
| 6 | Settlement flow | Flow | Event → Calculation → Authorization → Payment → Confirmation |
| 7 | Phoenix lifecycle worked example | Timeline | 4 observation dates with outcomes |

---

## 7. Interaction with Existing Content

| Interaction | Detail |
|------------|--------|
| **Extends 2.6** | Section 2.6 is the overview table. Section 2.9 is the deep dive. 2.6 references 2.9: "For the complete lifecycle mechanics, see Section 2.9" |
| **Connects to 2.8** | Systems Primer introduces Murex/NEMO/Sophis. Section 2.9 shows how trades flow through them |
| **Supports product §13** | Every product chapter §13 (Lifecycle) covers product-specific lifecycle. Section 2.9 provides the generic framework that §13 customizes |
| **Operations learning path** | Section 2.9 is the primary entry point for the Operations reading path in front matter |
| **Product Control path** | Section 2.9 §5 is the core reference for Product Control readers |

**No existing chapter modifications required.** Section 2.6 gains a forward reference to 2.9 during harmonization.

---

## 8. Assessment

| Criterion | Score |
|-----------|:-----:|
| Educational impact | **HIGH** — fills operational knowledge gap between overview (2.6) and product-specific (§13) |
| Effort | **HIGH** — ~7,000 words, 7 visuals, cross-functional coverage |
| Publication value | **HIGH** — makes the book useful for Operations and Product Control (not just FO) |
| Reader value | **HIGH** — Operations/PC readers have no equivalent reference in Part 2 currently |
| Risk | **LOW** — additive, no modifications to existing content |

**Recommendation: PROCEED.** Third priority after Payoff Masterclass and Construction Lab.

---

*Trade Lifecycle Masterclass Design Review completed 2026-06-21.*
