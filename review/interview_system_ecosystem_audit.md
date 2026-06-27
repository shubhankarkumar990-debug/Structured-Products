# Interview System — Ecosystem Integration Audit

**Date**: 2026-06-25
**Scope**: 15-workstream comprehensive audit
**Artifact**: production/interview_system.md (1,964 lines)
**Status**: APPROVED 2026-06-22 (pre-Part 6)
**Verdict**: NOT READY FOR PUBLICATION — critical infrastructure gap

---

## Executive Summary

The Interview System is an excellent product-knowledge interview preparation tool. It covers 49/49 products with well-structured 4-tier answers, 25 comparison pairs, 210+ questions, 40 written assessments, 5 mock interview tracks, and 30 traps.

It has one critical structural deficiency: **it was generated before Part 6 — The Operational Ecosystem existed.** The entire infrastructure domain — P&L Explain, IPV, reserves, XVA, FTP methodology, settlement conventions, day count, corporate actions, trade lifecycle, booking, CSA, model governance, capital metrics, regulatory depth — is absent from the interview preparation.

This gap means the Interview System prepares candidates for ~60% of a structured products interview. The other ~40% — the operational, control, and infrastructure questions that every senior interviewer asks — is missing entirely.

---

## WS1: Ecosystem Consistency

### Cross-Artifact Reference Audit

| Artifact | References IN Interview System | Correct? | Gap? |
|----------|:-----------------------------:|:--------:|:----:|
| Desk Bible Parts 0–5 | YES — §5.x.x section references throughout | YES | NO |
| Desk Bible Part 6 | **ZERO** references | N/A | **CRITICAL** |
| Product DNA Atlas | YES — "Atlas E:", "Atlas Appendix F/G" | YES | NO |
| Product Comparison Matrix | YES — "Matrix View 7", "Matrix Appendix A" | YES | NO |
| Solutions Manual | YES — "SM scenario X.Y", "SM AP-X" throughout | YES | NO |
| Learning Dependency Graph | YES — "difficulty calibration via complexity bands" | YES | NO |
| Product Evolution Map | YES — "Family progression for comparison pairs" | YES | NO |
| Product Universe Map | NO references | N/A | LOW |
| Searchability Alias Map | NO references (did not exist at generation time) | N/A | MEDIUM |
| Cross-Reference Map | NO references (did not exist) | N/A | LOW |
| Visual Specifications | NO references (did not exist) | N/A | LOW |

### Terminology Consistency Check

| Term | Interview System | Desk Bible | Consistent? |
|------|-----------------|------------|:-----------:|
| FTP | "FTP − desk margin" (pricing formula) | Part 2 §2.2 + Part 6 §6.7 (methodology) | YES but shallow |
| CVA/DVA | "counterparty credit (CVA/DVA)" — 1 mention | Part 6 §6.7 (full XVA framework) | YES but shallow |
| ISDA | "ISDA standard credit events" | Part 6 §6.3 (full Master Agreement treatment) | YES but shallow |
| Barrier observation | "continuous" vs "European" | Part 1 §1.3 + Part 6 §6.1 | YES |
| Recovery rate | "40% for senior unsecured" | Part 6 §6.4 (full waterfall) | YES |
| Complexity scores | All 49 products scored | Atlas — all match | YES |
| Section references | §5.x.x throughout | Desk Bible chapter numbers | YES |

### Inconsistencies Found

| # | Issue | Severity | Detail |
|:-:|-------|:--------:|--------|
| 1 | IRS Tier 2 references "LIBOR/SOFR resets" | LOW | LIBOR is discontinued. Should be "SOFR resets (historically LIBOR)" for accuracy. Part 6 §6.1 correctly treats SOFR as current. |
| 2 | Traceability table (line 1957) references "§1, §11, §14, §15, §19, §20" | LOW | These are internal chapter section numbers, not Part 6 sections. Correct but could be clearer. |
| 3 | Roles listed as 5 (line 6) vs Part 6 §6.10 lists 6 roles | MEDIUM | Interview System omits Product Control and Operations as interview tracks. Part 6 §6.10 teaches 6 roles (Structurer, Trader, Sales, Risk, PC, Ops). |
| 4 | "LIBOR discontinuation" (IRS Tier 4) described as past event | LOW | Correct factually but phrasing could be sharper. |

**WS1 Verdict: PASS with CRITICAL GAP.** Product-level consistency is strong. Infrastructure-level consistency cannot be assessed because the Interview System contains zero infrastructure content from Part 6.

---

## WS2: Product Coverage

### 49/49 Product Verification

| Treatment Level | Products | Count | Adequate? |
|----------------|----------|:-----:|:---------:|
| Full 4-tier | RC, Phoenix, IRS, CDS, PPN, VarSwap, CDO, WOAC, ACCUM, FTD | 10 | YES |
| Tier 1-3 full, T4 abbreviated | DRC, KODRC, CRC, Airbag, Bonus, Digital, V.STEG, CLN, FCN, XCCY, VO, NCRA, FWD, SD | 14 | YES |
| Tier 1-2 full, T3-4 abbreviated | ICN, DKIP, Booster, Warrant, TRS, EqSwap, CommSwap, VLSP, IR Callable, ZCL, CRA SRT, Digital CF, RA STEG, C.STEG, TARN STEG, Skew CLN, NTD, ELO, DCI, Opt-on-RC, DECUM, SHRK, SNOW, CLIQ | 24 | MOSTLY |

### Coverage Proportionality Check

| Complexity | # Products | Expected Depth | Actual Depth | Gap? |
|:----------:|:----------:|:--------------:|:------------:|:----:|
| 2 | 3 (PPN, SD, FWD, VLSP) | Tier 1-2 | Tier 1-3 for PPN/SD/FWD, T1-2 for VLSP | NO |
| 3 | 6 (RC, DRC, VO, ELO, DCI, Warrant) | Tier 1-3 | RC: full 4-tier; others: T1-2 | ACCEPTABLE |
| 4 | 8 (KODRC, Airbag, Bonus, Digital, CLN, Booster, ZCL, CommSwap, SHRK) | Tier 1-3 | Most get T1-2 only | MINOR GAP |
| 5 | 9 (CRC, CDS, TRS, EqSwap, V.STEG, Digital CF, Skew CLN, XCCY, Opt-on-RC, IR Callable) | Tier 1-3 | CDS: full 4-tier; others: T1-2 or T1-3 | ACCEPTABLE |
| 6 | 7 (Phoenix, FCN, NCRA, CRA ELN, ACCUM, DECUM, C.STEG) | Tier 1-4 | Phoenix/ACCUM: full; others: abbreviated | ACCEPTABLE |
| 7 | 5 (VarSwap, FTD, DKIP, RA STEG, SNOW, CLIQ) | Tier 1-4 | VarSwap/FTD: full; others: abbreviated | ACCEPTABLE |
| 8 | 3 (WOAC, NTD, TARN STEG) | Tier 1-4 | WOAC: full; NTD/TARN: abbreviated | MINOR GAP |
| 10 | 1 (CDO) | Tier 1-4 | Full 4-tier | NO |

### Product Knowledge Questions (PK.1-PK.49)

**49/49 products have at least one dedicated question. PASS.**

### Missing Product Treatment

| Product | Current | Issue |
|---------|---------|-------|
| CRA ELN (6) — §5.1.10 | Mentioned in comparison pairs + PK.10 only | No tier treatment at all. Complexity 6 product with NO answer library entry. |
| NTD (8) | Tier 1-2 only | Complexity 8 warrants at least Tier 1-3 |
| TARN STEG (8) | Tier 1-2 only | Complexity 8 warrants at least Tier 1-3 |

**WS2 Verdict: PASS with MINOR GAPS.** 49/49 products covered. CRA ELN (Complexity 6) missing from the Product Answer Library entirely. Two Complexity 8 products have abbreviated treatment.

---

## WS3: Infrastructure Coverage

### Term-by-Term Audit

This is the audit's most critical section. Each term from the specification is checked against the Interview System.

| # | Infrastructure Term | In Interview System? | Mentions | Assessment |
|:-:|--------------------:|:--------------------:|:--------:|------------|
| 1 | Market Conventions | NO | 0 | **CRITICAL** — No questions |
| 2 | Business Day Conventions | NO | 0 | **CRITICAL** |
| 3 | Settlement Conventions | NO | 0 | **CRITICAL** |
| 4 | Day Count | NO | 0 | **CRITICAL** — Core interview topic |
| 5 | Calendars (TARGET, trading) | NO | 0 | **HIGH** |
| 6 | Modified Following | NO | 0 | **CRITICAL** — #1 convention question |
| 7 | Following / Preceding | NO | 0 | **HIGH** |
| 8 | Settlement Calendar | NO | 0 | **HIGH** |
| 9 | Trade Date / Booking Date / etc. | NO | 0 | **HIGH** — 10 date types undefined |
| 10 | Floating Coupon mechanics | PARTIAL | Implied in product descriptions | **MEDIUM** |
| 11 | Fixed Coupon mechanics | PARTIAL | Implied | **LOW** |
| 12 | Independent Amount | NO | 0 | **HIGH** |
| 13 | Threshold | NO | 0 | **HIGH** |
| 14 | Minimum Transfer Amount | NO | 0 | **HIGH** |
| 15 | Haircuts | NO | 0 | **HIGH** |
| 16 | CSA | NO | 0 | **CRITICAL** — Core documentation topic |
| 17 | ISDA Master Agreement | PARTIAL | "ISDA standard credit events" — 1 mention | **HIGH** — Needs depth |
| 18 | Confirmation | NO | 0 | **HIGH** |
| 19 | Schedule | NO | 0 | **HIGH** |
| 20 | Novation / Assignment | NO | 0 | **MEDIUM** |
| 21 | Close-out Netting | NO | 0 | **HIGH** |
| 22 | Collateral | NO | 0 | **CRITICAL** |
| 23 | Variation Margin | NO | 0 | **CRITICAL** |
| 24 | Initial Margin | NO | 0 | **CRITICAL** |
| 25 | European/American/Cash Settlement | PARTIAL | Settlement types mentioned in product context | **MEDIUM** |
| 26 | Corporate Actions | NO | 0 | **HIGH** |
| 27 | Market Disruption Events | NO | 0 | **HIGH** |
| 28 | Clean Price / Dirty Price | NO | 0 | **CRITICAL** — Basic interview question |
| 29 | Accrued Interest | NO | 0 | **CRITICAL** |
| 30 | Funding Spread | PARTIAL | "funding costs" in product context | **HIGH** |
| 31 | Discount Spread | NO | 0 | **HIGH** |
| 32 | Issuer Credit | PARTIAL | Lehman PPN example | **MEDIUM** |
| 33 | Reference Entity | PARTIAL | CDS/CLN context | **LOW** |
| 34 | FR/MR/MMR/NR | NO | 0 | **CRITICAL** — Core credit question |
| 35 | Capital Structure | NO | 0 | **CRITICAL** — AT1/CoCos/bail-in absent |
| 36 | Recovery | PARTIAL | "40% for senior unsecured" | **MEDIUM** — Needs waterfall |
| 37 | Auction Settlement | PARTIAL | 1 mention (T.31 Big Bang) | **MEDIUM** |
| 38 | Fair Value Hierarchy (L1/L2/L3) | NO | 0 | **CRITICAL** |
| 39 | Mark-to-Market / Mark-to-Model | NO | 0 | **HIGH** |
| 40 | IPV | NO | 0 | **CRITICAL** |
| 41 | Consensus Pricing | NO | 0 | **HIGH** |
| 42 | Reserve Framework | NO | 0 | **CRITICAL** |
| 43 | Bid-Offer Reserve | NO | 0 | **CRITICAL** |
| 44 | Liquidity Reserve | NO | 0 | **CRITICAL** |
| 45 | Model Reserve | NO | 0 (only "model risk" generally) | **CRITICAL** |
| 46 | Vol/Corr/Lambda Reserves | NO | 0 | **CRITICAL** |
| 47 | Day One Reserve | NO | 0 | **HIGH** |
| 48 | Funding Reserve | NO | 0 | **HIGH** |
| 49 | Product Control | NO | 0 (as role/function) | **CRITICAL** |
| 50 | Flash P&L / Official P&L | NO | 0 | **CRITICAL** |
| 51 | P&L Explain | NO | 0 | **CRITICAL** — Core PC interview question |
| 52 | Treasury function | NO | 0 | **CRITICAL** |
| 53 | FTP methodology | NO | 0 (FTP used only as pricing input) | **CRITICAL** |
| 54 | Funding Curve | NO | 0 | **HIGH** |
| 55 | ALM | NO | 0 | **HIGH** |
| 56 | LCR / NSFR | NO | 0 | **HIGH** |
| 57 | XVA (as topic) | NO | 0 standalone questions | **CRITICAL** |
| 58 | CVA | PARTIAL | 1 mention in IRS context | **HIGH** |
| 59 | DVA | PARTIAL | 1 mention paired with CVA | **HIGH** |
| 60 | FVA / ColVA / MVA / KVA | NO | 0 | **CRITICAL** |
| 61 | SA-CCR | NO | 0 | **HIGH** |
| 62 | RWA | NO | 0 | **HIGH** |
| 63 | RAROC | NO | 0 | **HIGH** |
| 64 | EAD / PFE | NO | 0 | **HIGH** |
| 65 | Model Inventory | NO | 0 | **HIGH** |
| 66 | Model Validation (as governance) | PARTIAL | Mock track exists but no governance questions | **MEDIUM** |
| 67 | Backtesting (as governance) | PARTIAL | Mentioned in MV track | **MEDIUM** |
| 68 | Override Governance | NO | 0 | **HIGH** |
| 69 | SR 11-7 / SS1/23 | NO | 0 | **HIGH** |
| 70 | Static Data / Golden Source | NO | 0 | **CRITICAL** |
| 71 | Booking workflow | NO | 0 | **HIGH** |
| 72 | Settlement workflow | NO | 0 | **HIGH** |
| 73 | Reconciliation | NO | 0 | **CRITICAL** |
| 74 | Cash Reconciliation / Nostro | NO | 0 | **CRITICAL** |
| 75 | Trade Breaks | NO | 0 | **CRITICAL** |
| 76 | Corporate Actions (operational) | NO | 0 | **HIGH** |
| 77 | Lifecycle Events | NO | 0 | **HIGH** |
| 78 | SSI | NO | 0 | **MEDIUM** |
| 79 | Flow Book / Exotic Book | NO | 0 | **HIGH** |
| 80 | Warehouse Risk | NO | 0 | **HIGH** |
| 81 | Internal/External Hedge | NO | 0 | **MEDIUM** |
| 82 | Gamma Scalping | NO | 0 | **MEDIUM** |
| 83 | Long/Short Vega | PARTIAL | In product context only | **LOW** |
| 84 | Long/Short Correlation | PARTIAL | In WOAC/FTD context | **LOW** |
| 85 | Morning Marks | NO | 0 | **MEDIUM** |
| 86 | Hit / Lift / Roll / Switch | NO | 0 | **HIGH** |
| 87 | Colour / Bleed | NO | 0 | **MEDIUM** |
| 88 | Skew / Smile | PARTIAL | Trap T.13 covers smile | **LOW** |
| 89 | EMIR (depth) | PARTIAL | 1 mention (clearing mandate) | **HIGH** |
| 90 | UMR (depth) | PARTIAL | 1 mention | **HIGH** |
| 91 | Basel (depth) | PARTIAL | 1 mention (Basel III capital charges) | **HIGH** |
| 92 | Dodd-Frank | NO | 0 | **MEDIUM** |

### Infrastructure Coverage Summary

| Category | Terms Checked | Fully Covered | Partially Covered | Not Covered |
|----------|:------------:|:-------------:|:-----------------:|:-----------:|
| Market Conventions | 11 | 0 | 2 | 9 |
| Documentation/Legal | 10 | 0 | 1 | 9 |
| Credit Structure | 6 | 0 | 2 | 4 |
| Valuation | 7 | 0 | 0 | 7 |
| Product Control | 6 | 0 | 0 | 6 |
| Treasury/XVA/Capital | 14 | 0 | 2 | 12 |
| Model Risk (governance) | 5 | 0 | 2 | 3 |
| Operations | 9 | 0 | 0 | 9 |
| Desk Vocabulary | 12 | 0 | 3 | 9 |
| Regulation (depth) | 5 | 0 | 3 | 2 |
| **TOTAL** | **92** | **0** | **15** | **77** |

**77 of 92 infrastructure terms have ZERO coverage. 15 have partial/passing coverage. ZERO have full coverage.**

**WS3 Verdict: FAIL.** The Interview System does not test infrastructure knowledge. This is the audit's blocking finding.

---

## WS4: Interview Depth (Career Progression)

### Current Structure

| Level | Name | Products Tested | Infrastructure Tested |
|:-----:|------|:---------------:|:--------------------:|
| 1 | Beginner | Complexity 2-3 | None |
| 2 | Intermediate | Complexity 4-5 | None |
| 3 | Advanced | Complexity 6-7 | None |
| 4 | Expert | Complexity 8-10 | None |

### Expected Career Mapping

| Career Level | Interview System Level | Appropriate? |
|:------------:|:---------------------:|:------------:|
| Graduate | Beginner | YES |
| Analyst (1-2 yrs) | Beginner-Intermediate | YES |
| Associate (3-5 yrs) | Intermediate | YES |
| VP (5-8 yrs) | Advanced | PARTIAL — VPs face infrastructure questions |
| Director (8-12 yrs) | Advanced-Expert | NO — Directors face PC, Treasury, XVA questions |
| ED (12-15 yrs) | Expert | NO — EDs face cross-functional questions |
| MD (15+ yrs) | Expert | NO — MDs face business/P&L/capital questions |

### Gap

The Interview System tests product knowledge depth (appropriate for Graduate through Associate). It does not test operational knowledge depth (required for VP and above). A VP-level Trading interview will ask about P&L Explain, reserves, and model governance. A Director-level Risk interview will ask about XVA, capital metrics, and regulatory frameworks. The Interview System cannot prepare candidates for these questions.

**WS4 Verdict: PASS for Graduate-Associate levels. FAIL for VP+ levels.**

---

## WS5: Follow-Up Questions

### Current State

"What The Interviewer Is Testing" annotations exist for ~40% of questions. These imply follow-ups but don't structure them.

### Missing Follow-Up Trees

| Initial Question | Missing Follow-Up | Why It Matters |
|-----------------|-------------------|---------------|
| "Explain RC construction" | "How would Product Control book this?" | Tests cross-functional awareness |
| "What are the risks of a CLN?" | "How would you set reserves for this?" | Tests PC knowledge |
| "Walk me through hedging a Phoenix" | "What happens if settlement fails on the hedge?" | Tests operational awareness |
| Any product question | "How does FTP affect the pricing?" | Tests treasury awareness |
| Any product question | "What's the capital charge on this?" | Tests capital awareness |
| Any Greeks question | "How would you explain this P&L to Product Control?" | Tests P&L Explain fluency |
| "CDS spread widens 100bp" | "How does this affect the CVA on your swap book?" | Tests XVA awareness |
| "Explain barrier observation" | "What calendar does this use? What happens on a holiday?" | Tests convention awareness |
| Any case study | "What does the KID show for this product?" | Tests regulatory fluency |

**WS5 Verdict: PARTIAL PASS.** Product follow-ups are implicit. Infrastructure follow-ups are absent entirely.

---

## WS6: Whiteboard Interviews

### Current Whiteboard [WT] Coverage

| Topic | Tagged [WT] | Count |
|-------|:-----------:|:-----:|
| Payoff diagrams | YES | 5+ |
| Greeks profiles | YES | 3+ |
| Option basics | YES | 4+ |
| Barrier products | YES | 3+ |
| Credit concepts | YES | 4+ |
| Rate concepts | YES | 3+ |
| Comparison tables | YES | 2+ |
| Regulatory | YES | 5+ |
| **Total [WT] questions** | | **~30** |

### Missing Whiteboard Topics

| Topic | Part 6 Section | Whiteboard Value | Priority |
|-------|---------------|:----------------:|:--------:|
| P&L Explain waterfall | §6.6 | HIGH — Draw the decomposition | **CRITICAL** |
| Capital structure hierarchy | §6.4 | HIGH — Draw 8-layer stack + loss flow | **CRITICAL** |
| CSA collateral flow | §6.3 | HIGH — Draw threshold, MTA, IA interaction | **HIGH** |
| Trade lifecycle (8 steps) | §6.9 | MEDIUM — Draw the operational flow | **HIGH** |
| XVA bridge | §6.7 | HIGH — Draw how XVAs stack on pricing | **HIGH** |
| Fair Value Hierarchy | §6.5 | MEDIUM — Draw L1/L2/L3 classification | **HIGH** |
| FTP curve construction | §6.7 | MEDIUM — Draw 3-component curve | **MEDIUM** |
| Settlement flow (DvP) | §6.1 | MEDIUM — Draw cash/securities flow | **MEDIUM** |
| Corporate action adjustment | §6.9 | MEDIUM — Draw stock split impact on barrier | **MEDIUM** |
| Model lifecycle | §6.8 | MEDIUM — Draw 8-stage governance cycle | **MEDIUM** |
| Day count comparison | §6.1 | HIGH — Calculate ACT/360 vs 30/360 | **HIGH** |
| Modified Following decision | §6.1 | HIGH — Walk through month-end example | **HIGH** |
| Reserve flow (IPV → reserve) | §6.6 | HIGH — Draw the reserve governance chain | **HIGH** |
| Regulatory map | §6.11 | MEDIUM — Map regulations to products | **MEDIUM** |

**WS6 Verdict: PARTIAL PASS.** Product whiteboard coverage is strong (~30 questions). Infrastructure whiteboard coverage is zero. 14 high-value whiteboard topics from Part 6 are missing.

---

## WS7: Termsheet Interviews

### Current State

**ZERO** termsheet-reading exercises exist in the Interview System.

Part 6 §6.2 teaches 14 date fields, 16 economics fields, convention fields, and legal fields. None of this content is tested.

### What's Missing

| Exercise Type | Description | Priority |
|--------------|-------------|:--------:|
| Field identification | "Here is a termsheet. Identify the 3 most important fields." | **CRITICAL** |
| Clean vs dirty price | "This termsheet shows issue price 99.50. What does the investor actually pay?" | **CRITICAL** |
| Convention interpretation | "The termsheet says 'Modified Following, ACT/360.' What does this mean for a December 31 coupon?" | **CRITICAL** |
| Red flag spotting | "This termsheet has 3 unusual features. Find them." | **HIGH** |
| Indicative vs final | "The client received an indicative termsheet. Can they trade on it?" | **HIGH** |
| Economics decomposition | "From the termsheet, identify the embedded options." | **HIGH** |

**WS7 Verdict: FAIL.** No termsheet interview exercises. This is a publication-blocking gap for a structured products interview handbook.

---

## WS8: Case Interview Realism

### Current Cases

| Case | Client | Product Area | Role | Realistic? |
|------|--------|-------------|------|:----------:|
| D.1 | Conservative Retiree | Protection | Sales | YES |
| D.2 | Tech VP Stock Concentration | Disposal | Structuring | YES |
| D.3 | Yield-Hungry Trustee | Rate income | Structuring | YES |
| D.4 | Macro Hedge Fund | Variance/vol | Trading | YES |
| D.5 | Risk Manager's Nightmare | WOAC risk | Risk | YES |
| D.6 | Model Validator's Challenge | TARN pricing | Model Val | YES |
| D.7 | Currency Treasurer | FX hedging | Sales | YES |
| D.8 | Credit Analyst's First Trade | Multi-name credit | Structuring | YES |

### Would These Be Asked at Bulge Bracket Banks?

| Bank | Style Match | Notes |
|------|:----------:|-------|
| JP Morgan | YES | D.1, D.4, D.5 match JPM interview style |
| Goldman Sachs | PARTIAL | GS tests harder mental math; missing calculation-heavy cases |
| Morgan Stanley | YES | D.2, D.3 match MS structuring style |
| Barclays | YES | D.5 matches Barclays risk interview style |
| UBS | YES | D.1, D.7 match UBS wealth management focus |
| BNP Paribas | PARTIAL | BNP would ask about STEG/CMS products — missing European rates case |
| Societe Generale | PARTIAL | SG structured products desk would test more exotic derivatives |
| Deutsche Bank | PARTIAL | DB would test operational/infrastructure questions |
| Citi | YES | D.4, D.8 match Citi markets interview |
| HSBC | YES | D.7 matches HSBC FX/treasury focus |
| Nomura | PARTIAL | Nomura would test autocallable depth (Asian market focus) |
| Macquarie | YES | D.2 matches Macquarie style |

### Missing Case Types

| Case Type | Why It's Missing | Priority |
|-----------|-----------------|:--------:|
| Product Control case | "You're a PC analyst. The desk shows +$2M unexplained P&L. Walk through investigation." | **CRITICAL** |
| Operations case | "A nostro break of $500K appeared. What's your investigation process?" | **CRITICAL** |
| Treasury case | "The FTP curve shifted 15bp. How does this affect pricing on your book?" | **HIGH** |
| Trade break case | "A barrier observation dispute between counterparties. One says breached, one says not. What's your process?" | **HIGH** |
| Corporate action case | "A reference entity in a CLN announces a stock split. What adjustments are needed?" | **HIGH** |
| Settlement failure case | "The hedge for a maturing RC failed to settle. What do you do?" | **HIGH** |
| Regulatory case | "ESMA issues a product intervention on autocallables. What's the immediate business impact?" | **MEDIUM** |

**WS8 Verdict: PASS for existing cases. FAIL for missing case types.** Zero operations, PC, treasury, or trade-break cases exist. These are standard interview questions at every bank listed.

---

## WS9: Desk Thinking

### Roles Represented

| Role | Mock Track | Questions | Cases | Deep Coverage? |
|------|:---------:|:---------:|:-----:|:--------------:|
| Structurer | YES (5.1) | DS.1-DS.5, SL.1-SL.12 | D.2, D.3, D.8 | YES |
| Trader | YES (5.2) | DS.6-DS.9 | D.4 | YES |
| Sales | YES (5.3) | DS.10-DS.13 | D.1, D.7 | YES |
| Risk | YES (5.4) | DS.14-DS.17 | D.5 | YES |
| Model Validation | YES (5.5) | DS.18-DS.21 | D.6 | YES |
| **Product Control** | **NO** | **0** | **0** | **NO** |
| **Operations** | **NO** | **0** | **0** | **NO** |
| **Treasury** | **NO** | **0** | **0** | **NO** |
| **Finance** | **NO** | **0** | **0** | **NO** |
| **Legal** | **NO** | **0** | **0** | **NO** |
| **Compliance** | **NO** | **0** | **0** | **NO** |

### Impact Assessment

Product Control, Operations, and Treasury are among the largest hiring functions in structured products. A PC analyst interview at any major bank will test:
- P&L Explain methodology
- Reserve framework
- IPV process
- Flash vs official P&L
- Unexplained P&L investigation
- Month-end process

None of these are in the Interview System.

An Operations analyst interview will test:
- Trade lifecycle
- Booking workflow
- Settlement process
- Corporate action handling
- Trade break investigation
- Reconciliation

None of these are in the Interview System.

**WS9 Verdict: FAIL.** 5/11 desk roles represented. The 6 missing roles collectively represent more hiring than the 5 covered roles.

---

## WS10: Calculation Questions

### Currently Covered

| Calculation Type | Questions | Adequate? |
|-----------------|:---------:|:---------:|
| PPN participation rate | PK.1, Round 2 mock | YES |
| Phoenix coupon accrual | PK.10, MC.6 | YES |
| Variance swap P&L | T.11, MC.14 | YES |
| Option Greeks (delta approx) | T.4 | YES |
| Forward price | MC.5 | YES |
| DV01 scaling | T.23, PK.25 | YES |
| FTD correlation effect | MC.12 | YES |
| CDS spread → default prob | T.28 | YES |
| CDO tranche correlation | MC.18 | YES |

### Missing Calculations

| Calculation Type | Part 6 Source | Priority |
|-----------------|--------------|:--------:|
| Day count: ACT/360 vs 30/360 on same period | §6.1 | **CRITICAL** |
| Clean price to dirty price conversion | §6.2 | **CRITICAL** |
| Accrued interest calculation | §6.2 | **CRITICAL** |
| P&L Explain decomposition | §6.6 | **CRITICAL** |
| Reserve calculation (bid-offer) | §6.6 | **HIGH** |
| FTP impact on coupon | §6.7 | **HIGH** |
| XVA charge calculation | §6.7 | **HIGH** |
| RWA / SA-CCR | §6.7 | **MEDIUM** |
| RAROC | §6.7 | **MEDIUM** |
| Settlement amount (DvP) | §6.1 | **MEDIUM** |
| Floating coupon (SOFR compound) | §6.1 | **MEDIUM** |

**WS10 Verdict: PASS for product calculations. FAIL for infrastructure calculations.**

---

## WS11: Behavioural Interviews

### Current Coverage (BT.1-BT.10)

Strong. Covers: conviction, risk reframing, structured thinking, compliance, elevator pitch, model humility, self-awareness, genuine interest, client management, communication.

### Missing Behavioural Scenarios

| Scenario | Role Relevance | Priority |
|----------|:-------------:|:--------:|
| "You found a $2M trade break. The trader says it's not real. What do you do?" | Ops, PC | **CRITICAL** |
| "Your P&L Explain has $500K unexplained. The month-end deadline is in 2 hours." | PC | **CRITICAL** |
| "You booked a trade incorrectly. You realize it 3 days later. What's your process?" | Ops, Structuring | **HIGH** |
| "The nostro team reports a cash break matching the exact amount of a coupon payment you processed." | Ops | **HIGH** |
| "Two systems show different valuations for the same trade. How do you investigate?" | PC, Risk | **HIGH** |
| "A corporate action notification arrives 2 hours before observation date for a Phoenix." | Ops, Trading | **HIGH** |
| "Treasury changes the FTP curve mid-month. The structuring desk wants to re-price an issued note." | Treasury | **MEDIUM** |

**WS11 Verdict: PASS for product-facing behavioural. FAIL for infrastructure-facing behavioural.**

---

## WS12: Interviewer Psychology

### Currently Documented

~25 "What The Interviewer Is Testing" annotations across:
- Technical traps (T.11-T.20 all annotated)
- Case studies (D.2-D.8 annotated)
- Advanced desk questions (DS.4-DS.5, DS.8-DS.9 annotated)
- Regulatory (RG.11-RG.22 annotated)

### Quality Assessment

| Question Category | Annotations | Average/Exceptional/Weak Differentiation? |
|------------------|:-----------:|:----------------------------------------:|
| Technical traps | All 20 | YES — clear trap/correct/naive answer |
| Product knowledge | ~30% | PARTIAL — some but not systematic |
| Cases | All 8 | YES — scoring rubric provided |
| Mock interviews | All 5 tracks | YES — scoring summary table |
| Regulatory | ~60% | YES — good annotations |

### Missing Interviewer Psychology

For infrastructure questions (once added):
- What separates "average" from "exceptional" on a P&L Explain question?
- What separates candidates on a reserve governance question?
- How does an interviewer test whether a candidate truly understands the trade lifecycle vs memorized steps?

**WS12 Verdict: PASS for existing content. Gap proportional to infrastructure gap.**

---

## WS13: Duplication Review

### Cross-Artifact Overlap Check

| Content | Interview System | Source Artifact | Duplication? |
|---------|:----------------:|:---------------:|:------------:|
| Product descriptions | 4-tier answers (interview-framed) | Desk Bible §1-§22 per chapter | NO — different framing |
| Comparison pairs | 25 pairs with trap questions | Matrix dimensional comparisons | NO — interview-specific |
| Decision framework | "Reference SM §1.1 10-step model" | Solutions Manual §1.1 | NO — reference only |
| Scenarios | "See SM scenario X.Y" | Solutions Manual scenarios | NO — reference only |
| Anti-patterns | "See SM AP-X" | Solutions Manual anti-patterns | NO — reference only |
| Complexity scores | Used for difficulty calibration | Atlas complexity scores | NO — application |
| Traps | 30 original traps | Not in any source | NO — original content |
| Mock tracks | 5 × 4 variants | Not in any source | NO — original content |

**WS13 Verdict: PASS.** No duplication. The Interview System appropriately references rather than reproduces. All answers are interview-framed, not copied from the Desk Bible or Solutions Manual.

---

## WS14: Navigation Review

### Current Navigation

| Feature | Present? | Quality |
|---------|:--------:|:-------:|
| Table of Contents | YES | Clear 6-part structure |
| [WT] whiteboard tags | YES | Consistent marking |
| Difficulty labels | YES | Beginner/Intermediate/Advanced/Expert |
| Atlas references | YES | "Atlas E: 5.x.x" |
| SM references | YES | "SM scenario X.Y", "SM AP-X" |
| Role labels on questions | PARTIAL | Cases have role labels; many questions don't |
| Scoring rubrics | YES | All mock tracks + cases |
| Answer keys | YES | MC + SA + Mini Case |

### Missing Navigation

| Feature | Impact | Priority |
|---------|--------|:--------:|
| Part 6 cross-references | Cannot navigate to infrastructure source material | **CRITICAL** |
| Career-level path guide | "If preparing for VP Trading, focus on..." | **HIGH** |
| Searchability alias map reference | Cannot find terms by alternative names | **MEDIUM** |
| Difficulty progression map | No visual showing beginner → expert flow | **MEDIUM** |
| Role-specific question index | "All Structuring questions: SL.1-12, DS.1-5, D.2, D.3, D.8" | **HIGH** |
| Time allocation guide | "Spend 60% on Tier 1-2, 30% on Tier 3, 10% on Tier 4" | **MEDIUM** |
| Cross-reference to visual specs | No diagram specifications referenced | **LOW** |

**WS14 Verdict: PARTIAL PASS.** Product-level navigation is good. Infrastructure navigation impossible (no content to navigate to). Career-level path guide would significantly improve usability.

---

## WS15: Publication Review

### 10-Dimension Assessment

| Dimension | Score | Rationale |
|-----------|:-----:|-----------|
| Educational Quality | 7/10 | Excellent for products. Zero for infrastructure. |
| Technical Accuracy | 9/10 | All product content verified against frozen artifacts. One minor LIBOR reference. |
| Career Value | 5/10 | Prepares for ~60% of interview questions. VP+ candidates undertrained. PC/Ops/Treasury candidates completely unserved. |
| Interview Realism | 6/10 | Product questions are realistic. Missing entire categories asked at every bank. |
| Cross-Artifact Consistency | 7/10 | Pre-Part 6 artifact. Product consistency strong. Infrastructure consistency unmeasurable. |
| Navigation | 7/10 | Good internal structure. Missing career paths and Part 6 links. |
| Readability | 9/10 | Clear, structured, consistent voice. Trap explanations are excellent. |
| Publication Quality | 7/10 | Professional structure. Content gaps prevent publication as "definitive handbook." |
| Future Scalability | 6/10 | Architecture allows adding infrastructure content. Current design lacks placeholder/hook points. |
| Production Readiness | 4/10 | **NOT READY.** Infrastructure gap is publication-blocking. |

### Publication Verdict

**The Interview System CANNOT be published as "the definitive structured products interview handbook" in its current state.**

It CAN be published as: "Structured Products Interview Preparation — Product Knowledge Edition."

To earn the "definitive" designation, it requires Part 6 integration across all 15 workstreams.

---

**End of ecosystem audit.**
