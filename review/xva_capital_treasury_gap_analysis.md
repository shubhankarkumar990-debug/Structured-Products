# XVA, Capital & Treasury — Gap Analysis

**Date:** 2026-06-25
**Scope:** Phase 6 audit — XVA adjustments, regulatory capital, treasury function
**Source:** Desk Bible v2 (22,620 lines, 49 products, 6 families)
**Method:** Word-boundary term counts + manual section review

---

## Executive Summary

The Bible treats XVA, capital, and treasury as background infrastructure — mentioned when they affect product economics ("FTP reduces the coupon budget") but never taught as subject matter. CVA appears twice (once as a revenue center, once as a P&L reconciliation item). DVA appears once. FVA, ColVA, MVA, and KVA are completely absent. RWA, SA-CCR, EAD, and PFE have zero word-boundary matches. FTP is the best-covered topic in this phase (44 mentions) but is explained only as a cost input, not as a treasury function. A Trader, Structurer, or Risk Manager reading the Bible would not understand how their products consume capital, what XVA charges apply, or how Treasury prices internal funding.

---

## Term Count Evidence

### XVA Adjustments

| Term | Count | Context |
|------|:-----:|---------|
| CVA (word-boundary) | 2 | Line 2604: "credit valuation adjustment (CVA)" in P&L reconciliation table. Line 10504: "manages CVA (Credit Valuation Adjustment) as a revenue center" |
| DVA | 1 | Line 10504: "CVA/DVA management" — single compound mention |
| FVA (Funding Valuation Adjustment) | 0 | Absent |
| ColVA (Collateral Valuation Adjustment) | 0 | Absent |
| MVA (Margin Valuation Adjustment) | 0 | Absent |
| KVA (Capital Valuation Adjustment) | 0 | Absent |
| XVA (as umbrella term) | 0 | Absent |

### Capital & Regulatory

| Term | Count | Context |
|------|:-----:|---------|
| RWA (word-boundary) | 0 | Absent |
| SA-CCR | 0 | Absent |
| EAD (Exposure at Default) | 0 | Absent |
| PFE (Potential Future Exposure) | 0 | Absent |
| Economic Capital | 0 | Absent |
| Regulatory Capital | 11 | All general context ("regulatory capital requirements") |
| Basel | 31 | Mostly historical ("Basel III changed..."); no practical application |
| Capital Charge | 0 | Absent |
| Capital Consumption | 0 | Absent |
| Leverage Ratio | 0 (capital context) | Absent in regulatory context |

### Treasury & Funding

| Term | Count | Context |
|------|:-----:|---------|
| FTP | 44 | Explained as cost component in §2.2 Product Construction |
| Funding Cost | 16 | In product pricing context |
| Transfer Pricing | 18 | In FTP explanation and product chapters |
| Liquidity Cost | 0 | Absent |
| Treasury (as function) | ~12 | In Four-Leg Framework and product lifecycle |
| ALM (Asset-Liability Management) | 0 | Absent |
| Liquidity Coverage Ratio (LCR) | 0 | Absent |
| Net Stable Funding Ratio (NSFR) | 0 | Absent |

---

## Detailed Gap Analysis

### 1. XVA Adjustments

#### What the Bible covers

**CVA — 2 mentions:**

1. **P&L reconciliation context** (line 2604): A table comparing Sophis and NEMO P&L includes "Issuer credit adjustment: Sophis P&L includes an issuer credit spread adjustment that NEMO does not. Ensure credit valuation adjustment (CVA) is applied consistently." This is an operational note about system reconciliation, not an explanation of CVA.

2. **CDS revenue model** (line 10504): "The bank prices counterparty risk into CDS trades and manages CVA (Credit Valuation Adjustment) as a revenue center." This is the only substantive CVA reference. It correctly identifies CVA as both a risk management tool and a revenue source but does not explain how CVA is calculated, what drives it, or how it affects product pricing.

**DVA — 1 mention:** Appears only in the compound "CVA/DVA management" at line 10504. No standalone explanation.

#### What is missing

| XVA Type | Definition (Not in Bible) | Impact on Products | Severity |
|----------|--------------------------|-------------------|:--------:|
| **CVA** | Expected loss from counterparty default on a derivatives portfolio | Reduces the value of all uncollateralized OTC derivatives; charged to Trading desks | HIGH |
| **DVA** | Benefit from own default risk — the mirror of CVA | Controversial P&L item; creates gains when own credit deteriorates | MEDIUM |
| **FVA** | Cost/benefit of funding uncollateralized derivatives vs risk-free rate | Directly reduces P&L on uncollateralized trades; drives structuring decisions | HIGH |
| **ColVA** | Impact of collateral terms (currency, type) on derivative value | Affects CSA-discounting methodology; drives collateral optimization | MEDIUM |
| **MVA** | Cost of posting initial margin (IM) for cleared derivatives | Increases cost of cleared swaps; affects IRS and CDS chapters | HIGH |
| **KVA** | Cost of regulatory capital consumed by a position | Connects capital charges to pricing; foundational for desk economics | HIGH |

**Severity:** HIGH (aggregate)
**Impact:** XVA adjustments are a primary driver of derivative pricing in the post-2008 environment. Every OTC derivative in the Bible (IRS, CCS, TRS, Equity Swap, CDS — 5 of 49 products) is subject to XVA charges. Every structured note (44 of 49 products) has XVA embedded in the issuer's funding cost. A reader would not understand:
- Why the same swap priced to two different counterparties produces different P&Ls (CVA difference)
- Why an uncollateralized trade is more expensive than a collateralized one (FVA)
- Why clearing mandates increase costs for some trades (MVA)
- How capital charges feed back into product pricing (KVA)

---

### 2. Regulatory Capital

#### What the Bible covers

**"Regulatory Capital" — 11 mentions:** All are contextual references. The most substantive are:
- Line 2360: "pension funds with legal obligations... insurance companies with regulatory capital requirements" — investor context, not bank capital
- Line 2371: "Regulatory capital requirements demand principal protection" — investor context

**"Basel" — 31 mentions:** Distributed across chapters as historical context. Typical usage pattern:

| Usage Pattern | Example | Frequency |
|--------------|---------|:---------:|
| Historical context | "Basel III changed capital requirements" | ~15 |
| Regulatory environment | "Basel framework" as background | ~10 |
| Specific rule reference | None found | 0 |
| Practical calculation | None found | 0 |

#### What is missing

| Capital Concept | Count | Purpose (Not in Bible) | Who Needs It |
|----------------|:-----:|----------------------|-------------|
| **RWA (Risk-Weighted Assets)** | 0 | Determines capital required for each position | Trader, Risk, Finance |
| **SA-CCR (Standardised Approach for CCR)** | 0 | Calculates counterparty credit risk capital for derivatives | Risk, Finance |
| **EAD (Exposure at Default)** | 0 | Expected exposure if counterparty defaults — input to capital calc | Risk |
| **PFE (Potential Future Exposure)** | 0 | Maximum expected exposure over time horizon — drives credit limits | Trader, Risk |
| **CVA Capital Charge** | 0 | Capital held specifically for CVA risk | Risk, Finance |
| **Market Risk Capital (FRTB)** | 0 | Capital for market risk under Fundamental Review of the Trading Book | Trader, Risk |
| **Economic Capital** | 0 | Internal capital allocation; often more conservative than regulatory | Finance, Management |
| **Leverage Ratio** | 0 | Non-risk-weighted capital constraint | All desk functions |
| **Capital Allocation** | 0 | How regulatory capital is attributed to desks and products | Management, Structurer |

**Severity:** HIGH
**Impact:** Capital is the binding constraint on bank activities. When a Structurer designs a new product, the capital consumption affects the desk's ROE and therefore the minimum acceptable margin. When a Trader takes on a new position, the capital impact affects P&L attribution (through KVA). When Risk sets limits, capital is a primary constraint. The Bible mentions "Basel" and "regulatory capital" as environmental facts but does not connect them to desk-level decision-making.

**Specific product impact:**

| Product | Capital-Relevant Question (Not Answerable from Bible) |
|---------|------------------------------------------------------|
| IRS (5.2.1) | How much SA-CCR capital does a 10-year IRS consume vs a 2-year? |
| CDS (5.2.5) | What is the CVA capital charge on a single-name CDS? |
| CLN (5.4.1) | Does a funded CLN receive different capital treatment than an unfunded CDS? |
| TRS (5.2.2) | Does a TRS on equity receive the same capital treatment as a TRS on credit? |
| Autocallable (5.1.1) | What is the capital benefit of daily barrier observation vs European? |

None of these questions can be answered from the Bible. Each is relevant to at least one desk function.

---

### 3. Treasury Function & FTP

#### What the Bible covers — FTP is the best-covered topic in Phase 6

**FTP coverage (44 mentions) is concentrated in two areas:**

**Area 1 — Part 2, Product Construction (§2.2):**
The most substantive FTP explanation in the Bible (lines 1606-1616):

> "FTP is the internal rate at which a bank's treasury lends money to its trading desks. Think of it as the wholesale price of money inside the bank."
> "When the structured products desk issues a note to an investor, it receives cash. But that cash has a cost — the bank's own borrowing cost. FTP represents this cost."

**Area 2 — Four-Leg Framework (§2.3):**
FTP appears as the Deposit Leg (Leg 3) in every structured product construction:
- Line 1654: "Leg 3 — Deposit Leg (Bank to Treasury)"
- Line 1656: "The deposit leg represents the FTP cost — the internal price at which treasury provides funding to the structured products desk."
- Line 1690: "Deposit Leg | Treasury charges FTP at 2% | -$20,000"

**Area 3 — Individual product chapters:**
Every product chapter that uses the Four-Leg Framework includes FTP as a cost component in the coupon/discount calculation waterfall. Example:
- Line 1602: "Coupon = Bond interest + Put premium - FTP - Desk margin"
- Line 1604: "If the bond interest is 2%, the put premium is equivalent to 6%, FTP is 0.5%, and the desk margin is 0.5%, the investor receives: 2% + 6% - 0.5% - 0.5% = 7%."

#### What is missing

| Treasury Aspect | Coverage | Evidence |
|----------------|:--------:|---------|
| FTP as a cost component | COVERED | 44 mentions; formula explained; worked examples in every product |
| FTP as a treasury function | MISSING | HOW treasury sets FTP not explained |
| FTP methodology (matched-maturity, pooled, hybrid) | MISSING | Not mentioned |
| FTP curve construction | MISSING | Not mentioned |
| Term structure of FTP | MISSING | FTP appears as a single rate (e.g., "0.5%"), not a curve |
| FTP for different currencies | MISSING | Not mentioned |
| FTP updates and repricing impact | PARTIAL | Line 1711: "In a rising rate environment, FTP increases" — correct but no mechanism |
| Treasury function and responsibilities | MINIMAL | Line 1705: "They manage Leg 3 — providing funding at FTP and managing the bank's overall balance sheet" |
| ALM (Asset-Liability Management) | MISSING | 0 mentions |
| Liquidity cost framework | MISSING | 0 mentions of "Liquidity Cost" |
| LCR/NSFR impact on product design | MISSING | 0 mentions |
| Internal funds transfer from issuance | MISSING | The Four-Leg Framework shows money flowing to Treasury but not what Treasury does with it |
| Liquidity buffer cost | MISSING | Not mentioned |

**Severity:** MEDIUM (FTP as cost input: covered) / HIGH (treasury function: missing)
**Impact:** The Bible's FTP treatment is appropriate for its purpose: explaining where the coupon comes from and why FTP reduces the available budget. A Structurer reading the Bible would correctly include FTP in their coupon calculation. But they would not understand:
- Why FTP differs for a 1-year note vs a 10-year note (term structure)
- Why FTP for USD differs from FTP for EUR (currency basis)
- Why FTP changes over time and how that affects existing products
- What Treasury does with the funding received from note issuance
- How liquidity regulations (LCR, NSFR) constrain product design

---

### 4. Interaction Effects: XVA + Capital + FTP

The most significant gap is not any single missing concept but the interaction between them. In practice, these are connected:

| Interaction | How They Connect | Bible Coverage |
|------------|-----------------|:--------------:|
| FVA and FTP | FVA is the market-facing version of FTP — both measure funding cost, but FVA applies to derivatives and FTP to balance sheet | FTP covered; FVA absent; connection absent |
| KVA and Capital | KVA translates regulatory capital (RWA) into a cost charged to the desk | Both absent |
| MVA and Clearing | MVA is the cost of IM for cleared derivatives; drives decision between cleared and bilateral | Neither MVA nor clearing cost analysis covered |
| CVA and PFE | CVA is driven by PFE profile; PFE determines credit limits | CVA mentioned; PFE absent; connection absent |
| Capital and Product Design | SA-CCR capital consumption varies dramatically between product types; this drives structuring decisions | Capital absent; structuring decisions taught without capital constraint |
| Treasury and Issuance | When a bank issues a structured note, Treasury receives funding; the FTP is the price of this funding | FTP covered; Treasury function absent |

**Severity:** HIGH
**Impact:** These interaction effects determine the real economics of running a structured products desk. The Bible teaches each product as if it exists in isolation from bank-level constraints. In reality:
- A product that consumes too much capital will not be approved regardless of client demand
- A product with high FVA charges will be priced out of the market
- A product that cannot be cleared will incur MVA costs that reduce competitiveness
- A change in FTP methodology can make an entire product line uneconomical

---

## Gap Severity Summary

| Category | Severity | Term Evidence | Rationale |
|----------|:--------:|:------------:|-----------|
| XVA — CVA/DVA methodology | HIGH | 2 + 1 mentions, no methodology | Named as revenue center; never explained |
| XVA — FVA/ColVA/MVA/KVA | HIGH | All 0 mentions | Completely absent; fundamental pricing inputs |
| Regulatory capital framework | HIGH | RWA/SA-CCR/EAD/PFE all 0 | Zero coverage of capital calculation |
| Capital-product connection | HIGH | 0 interaction analysis | Products taught without capital constraint |
| FTP as cost input | ADEQUATE | 44 mentions; formula + examples | Correctly explained at product level |
| Treasury function | HIGH | Minimal (Leg 3 description only) | HOW treasury operates not explained |
| FTP methodology | MEDIUM | 0 methodology detail | Term structure, currency effects absent |
| Liquidity framework (LCR/NSFR) | MEDIUM | 0 mentions | Regulatory constraint; absent |

---

## Structural Observation

The Bible's treatment of XVA/Capital/Treasury follows a clear architectural principle: these topics are **bank-level infrastructure**, not product-level knowledge. The Bible is organized around products (49 chapters) with shared foundations (Part 0-2). XVA, capital, and treasury are foundations that were not built.

This is arguably the correct editorial decision for a product-focused reference. A junior desk member needs to understand what an Autocallable is before they need to understand how CVA affects its pricing. But the audit question is whether the Bible covers "everything needed to OPERATE" — and the answer for this phase is definitively no.

**The Basel paradox:** Basel appears 31 times in the manuscript, more than most technical terms. But it appears exclusively as a historical or environmental fact ("Basel III changed the landscape"). It is never connected to desk-level operations: no RWA calculation, no capital allocation, no SA-CCR methodology. The Bible acknowledges that Basel exists and matters without teaching what it does.

**Remediation path:**

| Priority | Content | Estimated Size | Location |
|:--------:|---------|:--------------:|----------|
| 1 | XVA overview: CVA, DVA, FVA, KVA definitions and interaction | 1,500-2,000 words | New Part 0 section |
| 2 | Regulatory capital: RWA, SA-CCR, EAD concepts | 1,000-1,500 words | New Part 0 section |
| 3 | Treasury function: FTP methodology, ALM basics | 800-1,200 words | Expand existing §2.2 |
| 4 | Per-chapter capital notes | 1-2 sentences per chapter | §7 or §15 in each chapter |

Total remediation: approximately 4,000-6,000 words of new content, concentrated in Part 0 with light cross-references from existing chapters.
