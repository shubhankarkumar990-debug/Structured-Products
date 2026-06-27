# Atlas Future-Proofing Review

**Date:** 2026-06-22
**Scope:** Evaluate potential new DNA card fields BEFORE Comparison Matrix generation
**Type:** Evaluate only — no implementation

---

## Candidates Evaluated

### 1. Most Important Desk Team

**Description:** Which trading desk or team primarily manages this product (e.g., Equity Exotics, Rates Structuring, Credit Derivatives).

**Verdict: DEFER**

**Reasoning:**
- Desk team assignments are institution-specific — they vary by bank. Barclays may route Phoenix through Equity Exotics while another bank routes through Structured Products.
- The Primary System field already provides the operational anchor (Murex vs NEMO vs Sophis).
- Including desk team creates a maintenance burden as banks reorganize.
- If needed, this belongs in an institution-specific overlay, not the canonical Atlas.

**Risk of adding now:** Low technical risk but creates false precision about organizational structure.

---

### 2. Typical Client Type

**Description:** Retail, Private Banking, Institutional, Corporate — primary distribution channel.

**Verdict: REJECT**

**Reasoning:**
- The Primary Buyer field already captures this with more granularity: "Risk-averse retail and institutional investors: pension funds, retirees, foundations with capital preservation mandates" (PPN) is richer than a simple "Retail / Institutional" tag.
- The Comparison Matrix CM field "Client Type" already provides the canonical categorization (5 categories in publication taxonomy: Retail, Private Banking, Institutional, All Segments, Specialized).
- Adding a simplified version to the DNA card would create a redundancy conflict between DNA card field and CM field.

**Risk of adding now:** Taxonomy collision with existing CM Client Type dimension.

---

### 3. Common Booking System

**Description:** Which system(s) the product is booked in for trade capture.

**Verdict: REJECT**

**Reasoning:**
- The Primary System field already exists on every DNA card and captures exactly this information.
- Values: Murex (most products), NEMO + Sophis (CLN and SRT), Exchange systems (Warrant), Murex / Endur (CommSwap).
- Adding a separate "Common Booking System" would duplicate Primary System.

**Risk of adding now:** Direct duplication of existing field.

---

### 4. Typical Holding Period

**Description:** Expected holding duration for the investor (distinct from contractual maturity).

**Verdict: DEFER**

**Reasoning:**
- Maturity Profile already captures contractual term. Holding period differs because of:
  - Autocall (Phoenix, FCN, SNOW average life < contractual maturity)
  - Early redemption (callable products)
  - Secondary market exit
- Expected holding period is analytically valuable for interview prep ("Phoenix average life is 18 months on a 5-year product") but requires quantitative modeling per product.
- Adding a qualitative estimate ("typically held 1-2 years") without data backing would be misleading.

**Recommendation for future:** If average life data becomes available from desk analytics, add as a separate Atlas field in a future optimization pass. Do not estimate.

**Risk of adding now:** Qualitative estimates without data create false precision.

---

### 5. Typical Trade Size

**Description:** Notional range (e.g., "$1M–$50M for institutional, $50K–$500K for retail").

**Verdict: REJECT**

**Reasoning:**
- Trade sizes are market-condition dependent, jurisdiction-dependent, and client-segment dependent.
- A Phoenix in Asia-Pacific has different typical size vs Europe vs Americas.
- Including size ranges creates a maintenance burden and risks becoming stale quickly.
- Not relevant for interview preparation, onboarding, or educational purposes (the Atlas's primary audiences).
- If needed for operational purposes, this belongs in a separate desk procedure document, not the reference layer.

**Risk of adding now:** Stale data, jurisdiction-specific, outside Atlas scope.

---

## Summary

| Candidate | Verdict | Reason |
|-----------|:-------:|--------|
| Most Important Desk Team | **DEFER** | Institution-specific; Primary System provides operational anchor |
| Typical Client Type | **REJECT** | Duplicates Primary Buyer + CM Client Type |
| Common Booking System | **REJECT** | Duplicates Primary System field |
| Typical Holding Period | **DEFER** | Needs quantitative data; qualitative estimate would mislead |
| Typical Trade Size | **REJECT** | Jurisdiction-dependent, not relevant to Atlas audiences |

**No new fields recommended before Matrix generation.** The current 16-field DNA card schema is sufficient. Deferred candidates (Desk Team, Holding Period) may be revisited if supporting data becomes available.

---

*Future-proofing review complete. No schema changes authorized.*
