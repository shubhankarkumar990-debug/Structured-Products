# Trade Break Case Study Library — Design Review

**Date:** 2026-06-21
**Proposed Section:** Part 2.10 — Trade Break Case Studies (or Appendix B)
**Framework:** v1.3.1 (FROZEN)
**Purpose:** Teach operational awareness through realistic failure scenarios
**Implementation:** After 49/49, after Trade Lifecycle Masterclass (§2.9)

---

## 1. Concept

Every product chapter §16 (Common Mistakes) teaches product-specific errors. But trade breaks are *process* failures — they cut across products. A wrong barrier booking affects RCs and Phoenixes identically. A settlement mismatch follows the same escalation path regardless of product.

The Trade Break Library teaches through failure: 8 case studies, each following a consistent 6-part structure that mirrors how the desk actually investigates and resolves breaks.

---

## 2. Placement Options

| Option | Location | Pros | Cons |
|--------|----------|------|------|
| **A: Part 2.10** | After Trade Lifecycle Masterclass (2.9) | Natural progression: learn lifecycle → learn what goes wrong | Part 2 becomes large |
| **B: Appendix B** | After Solutions Manual | Keeps core text lean. Case studies feel supplementary | May be skipped by readers |
| **C: Part 8** | Standalone part | Clear identity. Own table of contents entry | Feels disconnected from lifecycle |

**Recommendation: Part 2.10.** The lifecycle → failure → resolution learning arc is strongest when consecutive.

---

## 3. Case Study Structure — 6 Fields Per Case

| # | Field | Content |
|:-:|-------|---------|
| 1 | **What Happened** | The break as first detected. What the screen showed. Who noticed |
| 2 | **Root Cause** | Why it happened. Process failure, system limitation, human error, or data issue |
| 3 | **Impact** | Financial (P&L impact), operational (settlement delay), reputational (client impact) |
| 4 | **Detection** | How it was caught. Which control caught it. How long before detection |
| 5 | **Remediation** | Step-by-step resolution. Who did what. Systems involved |
| 6 | **Lesson Learned** | Preventive measure. Process improvement. What changed |

---

## 4. Eight Case Studies

### Case 1: Wrong Barrier Booked

| Field | Content |
|-------|---------|
| **What Happened** | Phoenix Autocallable booked with 65% KI barrier instead of 60%. Operations noticed discrepancy during confirmation matching |
| **Root Cause** | Manual data entry from term sheet. Barrier field misread (handwritten "60" interpreted as "65") |
| **Impact** | P&L: ~2bp notional (barrier shift changes option value). If undetected: client receives wrong payoff at maturity. Potential legal dispute |
| **Detection** | T+1 during trade confirmation matching. Counterparty confirmation showed 60%. System showed 65% |
| **Remediation** | Cancel and rebook. Amend in Murex. Reconfirm with counterparty. Trader adjusts hedge for corrected barrier. Risk signs off on corrected Greeks |
| **Lesson** | Electronic term sheet feed eliminates manual transcription. Four-eye check on barrier fields mandatory |

### Case 2: Wrong Fixing Source

| Field | Content |
|-------|---------|
| **What Happened** | Range Accrual booked with Bloomberg EURIBOR fixing instead of Reuters. Coupon accrual diverged from client expectation |
| **Root Cause** | ISDA documentation specified Reuters. System defaulted to Bloomberg. Booking team did not override |
| **Impact** | Coupon difference: 0.3bp per accrual day over 6 months = ~$15,000 on $100M notional |
| **Detection** | T+180 (6 months). Client complained coupon payment was lower than expected |
| **Remediation** | Recalculate all accrual days using correct source. Pay difference to client. System configuration updated |
| **Lesson** | Fixing source must be explicitly set at booking, not defaulted. Confirmation must name exact source |

### Case 3: Wrong Observation Date

| Field | Content |
|-------|---------|
| **What Happened** | Autocallable quarterly observation fell on a holiday. System used previous business day. Contract specified following business day |
| **Root Cause** | Holiday calendar in system did not include newly declared market holiday |
| **Impact** | Observation on wrong day: underlying at 99.5% (would not autocall) vs 100.3% on correct day (would autocall). Product continued when it should have terminated |
| **Detection** | T+2 after observation. Middle office holiday calendar reconciliation flagged discrepancy |
| **Remediation** | Force autocall. Calculate settlement as if called on correct date. Unwind delta hedge. Notify client |
| **Lesson** | Holiday calendars must be updated proactively. Observation date logic must follow contract convention exactly |

### Case 4: Incorrect Coupon Calculation

| Field | Content |
|-------|---------|
| **What Happened** | Memory coupon on Phoenix paid only current period coupon, not accumulated memory. Three missed periods' coupons not included |
| **Root Cause** | System memory coupon logic reset after product amendment. Amendment was for notional increase, but reset coupon memory flag |
| **Impact** | Underpayment: 3 × 1.8% × $50M = $2.7M |
| **Detection** | Client notified Operations that coupon was lower than expected. Product Control investigation confirmed |
| **Remediation** | Manual coupon calculation. Supplementary payment processed. System flag restored. Full coupon history audited |
| **Lesson** | Post-amendment validation must verify all product features, not just amended field. Regression testing for amendments |

### Case 5: Settlement Currency Mismatch

| Field | Content |
|-------|---------|
| **What Happened** | Cross-currency swap maturity settlement sent in USD instead of EUR. SWIFT message had wrong currency code |
| **Root Cause** | Swap had two currency legs. Settlement instruction referenced wrong leg's currency. Operations copied wrong SSI |
| **Impact** | Client received $10.2M instead of €9.4M. FX exposure created. Settlement failed on client's EUR nostro |
| **Detection** | T+0 (settlement date). Client's custodian rejected incoming USD on EUR account |
| **Remediation** | Recall USD payment. Resend in EUR. Negotiate value-date adjustment. Absorb FX cost of 1-day mismatch |
| **Lesson** | Multi-currency products must have explicit settlement currency per leg in booking. SSI selection validated against trade currency |

### Case 6: Credit Event Dispute

| Field | Content |
|-------|---------|
| **What Happened** | CLN reference entity experienced restructuring. Bank triggered credit event. Investor disputed, arguing restructuring did not meet ISDA definition |
| **Root Cause** | Reference entity announced voluntary debt exchange. Bank's legal view: qualified as Modified Restructuring. Investor's legal view: voluntary exchange is not restructuring |
| **Impact** | $25M notional. Recovery rate ~40%. Disputed amount: ~$15M |
| **Detection** | T+0 of credit event notice. Investor's counsel responded within 5 business days |
| **Remediation** | Escalated to ISDA Determinations Committee. Committee ruling: restructuring event valid. Settlement via auction. 47 business days from event to resolution |
| **Lesson** | CLN documentation must specify exact ISDA credit event definitions (Restructuring / Modified Restructuring / Modified Modified Restructuring). Legal review at inception, not at event |

### Case 7: Incorrect Booking Leg

| Field | Content |
|-------|---------|
| **What Happened** | Interest Rate Swap booked as pay-fixed, receive-float. Correct direction was receive-fixed, pay-float. Hedge went wrong way |
| **Root Cause** | Trader verbally confirmed "I pay 3%" meaning the bank pays fixed. Operations interpreted "I pay" as "we pay fixed." Direction ambiguity |
| **Impact** | Double exposure: wrong-way swap + unhedged correct position. P&L impact depended on rate move. In this case: 2-day exposure, rates moved 5bp, loss ~$80K on $500M notional |
| **Detection** | T+1. Trader's daily risk report showed unexpected DV01 sign. Investigated and found reversed swap |
| **Remediation** | Cancel incorrect swap. Rebook correct direction. Negotiate break costs with counterparty. Absorb P&L loss |
| **Lesson** | Trade tickets must use unambiguous direction language: "Bank pays fixed" / "Bank receives fixed." Never "I pay" in multi-party context |

### Case 8: Model Valuation Disagreement

| Field | Content |
|-------|---------|
| **What Happened** | Synthetic CDO mezzanine tranche. Trader valued at 92% of notional. Product Control valued at 84%. 8-point gap = $4M on $50M tranche |
| **Root Cause** | Correlation assumption: Trader used 30% base correlation. Product Control used 45% from market-implied (iTraxx tranches). No agreed source for bespoke portfolio correlation |
| **Impact** | P&L uncertainty: $4M. Potential reserve requirement. Trader compensation affected |
| **Detection** | Month-end IPV process. Product Control flagged as material discrepancy (>5% threshold) |
| **Remediation** | Valuation committee review. Agreed methodology: market-implied correlation with adjustment for bespoke portfolio. Reserve of $1.5M booked. Trader P&L adjusted |
| **Lesson** | Complex products must have pre-agreed valuation methodology documented at inception. Correlation source for bespoke portfolios must be explicitly specified |

---

## 5. Estimated Length

| Metric | Value |
|--------|:-----:|
| Case studies | 8 |
| Words per case | ~400-500 |
| Introduction | ~300 |
| Summary / lessons matrix | ~400 |
| Total word count | ~4,500 |
| Pages | ~10-12 |
| Visual assets | 2 (timeline showing detection lag, lessons matrix) |

---

## 6. Visual Requirements

| # | Visual | Type | Purpose |
|:-:|--------|------|---------|
| 1 | Detection timeline | Timeline | Shows detection lag for each case (T+0 to T+180) |
| 2 | Lessons matrix | Table/Infographic | 8 cases × 3 columns: Error Type, Control That Caught It, Preventive Measure |

---

## 7. Interaction with Existing Content

| Interaction | Detail |
|------------|--------|
| **Extends 2.9** | Trade Lifecycle Masterclass teaches the process. Trade Break Library teaches what happens when it fails |
| **Connects to §16** | Product chapter §16 (Common Mistakes) covers product-specific errors. Trade breaks are process-level errors |
| **Supports Operations path** | Key learning material for Operations-focused readers |
| **Cross-references** | Each case references specific lifecycle stage from §2.9 |

---

## 8. Assessment

| Criterion | Score |
|-----------|:-----:|
| Educational impact | HIGH — failure-based learning is highly effective for retention |
| Effort | LOW — 8 structured cases, ~4,500 words |
| Publication value | HIGH — practical, desk-authentic content rarely found in textbooks |
| Reader value | HIGH — directly applicable to desk roles |
| Risk | LOW — additive, fictional but realistic scenarios |

**Recommendation: PROCEED.** Low effort, high desk-authenticity value. Pairs naturally with Trade Lifecycle Masterclass.

---

*Trade Break Case Study Library Design Review completed 2026-06-21.*
