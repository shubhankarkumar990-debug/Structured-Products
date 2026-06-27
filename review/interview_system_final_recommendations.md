# Interview System — Final Recommendations

**Date**: 2026-06-25
**Source**: 15-workstream ecosystem integration audit
**Ranking Dimensions**: Educational Value (EV), Career Value (CV), Implementation Effort (IE), Publication Impact (PI)
**Scale**: EV/CV 1-10 (higher = more valuable), IE: LOW/MEDIUM/HIGH, PI: BLOCKING/HIGH/MEDIUM/LOW

---

## Audit Summary

| Metric | Value |
|--------|-------|
| Workstreams executed | 15 |
| Issues found | 28 |
| Critical (publication-blocking) | 5 |
| High (quality-limiting) | 8 |
| Medium (enhancement) | 6 |
| Low (polish) | 4 |
| Nice-to-Have | 5 |
| Product coverage | 49/49 (100%) |
| Infrastructure coverage | 0/92 terms (0%) |
| Roles covered | 5/11 (45%) |
| Ecosystem artifacts integrated | 7/12 (58%) |
| Publication readiness | NOT READY |
| Primary blocker | Part 6 infrastructure gap |

---

## Ranked Recommendations

Recommendations ranked by composite score: (EV + CV + PI_numeric) / IE_weight

PI numeric: BLOCKING=10, HIGH=8, MEDIUM=5, LOW=2
IE weight: LOW=1, MEDIUM=2, HIGH=3

---

### Rank 1: Infrastructure Interview Content Integration

**Source**: WS3 (Infrastructure Coverage), WS10 (Calculations)
**Severity**: CRITICAL
**EV**: 10 | **CV**: 10 | **IE**: HIGH | **PI**: BLOCKING

**What**: Add 40+ infrastructure interview questions sourced from Part 6 §6.1-§6.11:
- 15 technical questions on conventions, CSA, settlement, day count, clean/dirty price
- 10 P&L Explain / Product Control questions
- 5 XVA / Treasury / Capital questions
- 5 Operations / Trade Lifecycle questions
- 5 Model Governance questions
- 10-15 infrastructure calculation questions (day count, accrued interest, P&L decomposition, reserve sizing, XVA)

**Why**: 77 of 92 infrastructure terms have zero coverage. This is a total domain absence, not a coverage gap. Every bank tests infrastructure knowledge at desk rounds and above.

**How**: Generate as Part 7 of the Interview System, or integrate as new question categories (IC.1-IC.40 for Infrastructure Core, IF.1-IF.15 for Infrastructure Calculations) within existing Part 4 structure.

**Composite Score**: (10 + 10 + 10) / 3 = **10.0**

---

### Rank 2: Product Control & Operations Mock Tracks

**Source**: WS9 (Desk Thinking), WS8 (Case Interviews)
**Severity**: CRITICAL
**EV**: 10 | **CV**: 10 | **IE**: HIGH | **PI**: BLOCKING

**What**: Add 2 new mock interview tracks:
- Track 5.6: Product Control (60 min, 5 rounds — flash P&L, IPV walkthrough, reserve governance, unexplained P&L investigation, month-end process)
- Track 5.7: Operations (60 min, 5 rounds — trade lifecycle, booking, settlement, corporate actions, trade break investigation)
- 4 new case studies: PC analyst case (unexplained P&L), Ops analyst case (settlement failure), PC-Trading conflict case (reserve dispute), Ops-Trading conflict case (booking error)

**Why**: PC and Ops are the two largest hiring functions in structured products. Their candidates currently have zero interview preparation in this system.

**How**: Model after existing tracks (5.1-5.5) with same round structure, scoring rubric, variant system, and "What The Interviewer Is Testing" annotations.

**Composite Score**: (10 + 10 + 10) / 3 = **10.0**

---

### Rank 3: Termsheet Reading Exercises

**Source**: WS7 (Termsheet Interviews)
**Severity**: CRITICAL
**EV**: 9 | **CV**: 9 | **IE**: MEDIUM | **PI**: BLOCKING

**What**: Add 5 termsheet reading exercises:
1. **Beginner**: Identify 5 key fields on a vanilla RC termsheet
2. **Beginner**: Calculate clean vs dirty price from issue price and accrued interest
3. **Intermediate**: Interpret convention fields (Modified Following, ACT/360) and calculate adjusted payment date
4. **Advanced**: Spot 3 red flags on a Phoenix termsheet (unusual barrier, wrong day count, missing early termination clause)
5. **Advanced**: Decompose a CLN termsheet into embedded credit derivative + funding note

**Why**: "Read this termsheet" is the #1 structuring interview exercise at every bank globally. Its absence is the most conspicuous gap for any structured products professional reviewing this system.

**How**: Source field definitions from Part 6 §6.2. Use 4-tier answer framework (Tier 1: identify field, Tier 2: explain meaning, Tier 3: implications for pricing/risk, Tier 4: failure mode if field is wrong).

**Composite Score**: (9 + 9 + 10) / 2 = **14.0**

---

### Rank 4: Infrastructure Traps

**Source**: WS6 (Whiteboard), WS3 (Infrastructure Coverage)
**Severity**: HIGH
**EV**: 9 | **CV**: 9 | **IE**: MEDIUM | **PI**: HIGH

**What**: Add 12 infrastructure traps (IT.1-IT.12):

| # | Trap Statement | Naive Answer | Correct Answer | Source |
|:-:|---------------|:------------:|:--------------:|--------|
| IT.1 | "Modified Following = Following" | "Yes, both push to next business day" | "No — Modified Following rolls BACK if it crosses month-end" | §6.1 |
| IT.2 | "Day count doesn't matter" | "Differences are negligible" | "On $100M notional, ACT/360 vs 30/360 = $50K+ difference" | §6.1 |
| IT.3 | "IPV = checking Bloomberg" | "Compare trader mark to BBG" | "Full process: consensus, vendor, independent model, tolerance check" | §6.6 |
| IT.4 | "P&L Explain residual is noise" | "Small residual is always acceptable" | "Must be investigated — could signal model error, missing risk factor, or trade booking error" | §6.6 |
| IT.5 | "Reserves are a cushion" | "Just a buffer against losses" | "Specific, auditable adjustments: bid-offer, liquidity, model, concentration, funding" | §6.6 |
| IT.6 | "CSA threshold = no collateral" | "Below threshold, no posting" | "Threshold is the UNSECURED exposure amount — above it, you post the excess" | §6.3 |
| IT.7 | "FTP = risk-free rate" | "Treasury charges risk-free" | "FTP = risk-free + credit spread + liquidity premium + term adjustment" | §6.7 |
| IT.8 | "XVA is back-office" | "Post-trade adjustment, not front-office concern" | "Real economic cost affecting pricing, profitability, and desk P&L" | §6.7 |
| IT.9 | "Golden source = one system" | "Everything from one database" | "Different data types have different golden sources (NEMO for trades, Bloomberg for market data, MarkitServ for positions)" | §6.9 |
| IT.10 | "Corporate actions don't affect derivatives" | "Only affects cash equities" | "Barrier adjustments, payout modifications, reference entity replacement for credit" | §6.9 |
| IT.11 | "Clean price is what you pay" | "The quoted price" | "You pay dirty price = clean + accrued interest" | §6.2 |
| IT.12 | "SR 11-7 only applies to banks" | "Non-bank dealers exempt" | "Any institution using models for risk/pricing must have model governance" | §6.8 |

**Why**: Traps are the Interview System's strongest content type. Adding infrastructure traps extends this strength to the missing domain with maximum educational impact per word.

**Composite Score**: (9 + 9 + 8) / 2 = **13.0**

---

### Rank 5: Infrastructure Whiteboard Exercises

**Source**: WS6 (Whiteboard Interviews)
**Severity**: HIGH
**EV**: 9 | **CV**: 8 | **IE**: MEDIUM | **PI**: HIGH

**What**: Add 8 infrastructure whiteboard exercises:
1. **P&L Explain Waterfall** [WT]: Draw the decomposition from flash P&L to explained P&L (delta, gamma, theta, vega, rho, carry, new deals, residual)
2. **Capital Structure** [WT]: Draw 8-layer stack (equity → AT1 → Tier 2 → Senior → Senior Pref → Secured) with loss absorption flow
3. **Day Count Calculation** [WT]: Calculate accrual for ACT/360 vs 30/360 on same period, show difference
4. **Modified Following Decision** [WT]: Walk through January 31 example where MF rolls back to January 30
5. **Trade Lifecycle** [WT]: Draw 8-stage flow (inquiry → pricing → execution → confirmation → booking → settlement → lifecycle → maturity)
6. **XVA Bridge** [WT]: Draw how CVA, DVA, FVA, ColVA, KVA stack on base valuation
7. **CSA Collateral Flow** [WT]: Draw threshold, MTA, IA interaction with daily margin call
8. **Reserve Governance** [WT]: Draw IPV → tolerance → breach → reserve committee → approval chain

**Why**: Whiteboard exercises test whether candidates can explain concepts visually — essential for desk roles where you sketch on whiteboards daily. 14 high-value whiteboard topics from Part 6 exist; these 8 are the highest priority.

**Composite Score**: (9 + 8 + 8) / 2 = **12.5**

---

### Rank 6: Career-Level Path Guide

**Source**: WS4 (Interview Depth)
**Severity**: HIGH
**EV**: 8 | **CV**: 9 | **IE**: LOW | **PI**: HIGH

**What**: Add a preparation matrix mapping career level → recommended questions:

| Level | Products | Infrastructure | Mock Track | Time |
|:-----:|:--------:|:--------------:|:----------:|:----:|
| Graduate | PK (Complexity 2-3), T.1-T.10 | Conventions basics | 5.3 Beginner | 20h |
| Analyst | PK (Complexity 3-5), T.1-T.20, SL.1-SL.6 | Day count, termsheet, settlement | 5.1 Beginner | 40h |
| Associate | All PK, T.1-T.37, SL.1-SL.12, D.1-D.4 | P&L Explain basics, booking, CSA | 5.1 Advanced | 60h |
| VP | Top 10 Tier 4, D.1-D.8, DS.1-DS.21 | Full P&L Explain, IPV, reserves | 5.2 Intermediate | 80h |
| Director | All Tier 4, RG.1-RG.22, all traps | XVA, capital, cross-functional | 5.4 Expert | 100h |
| ED/MD | Full system + infrastructure | Business economics, FTP, ALM, regulatory strategy | All tracks | 120h |

**Why**: Candidates currently cannot determine which content is most relevant for their career level without reading the entire 1,964-line document. This single addition makes the Interview System immediately more usable.

**Composite Score**: (8 + 9 + 8) / 1 = **25.0**

---

### Rank 7: Part 6 Cross-References

**Source**: WS1 (Ecosystem Consistency), WS14 (Navigation)
**Severity**: CRITICAL (for ecosystem coherence)
**EV**: 7 | **CV**: 6 | **IE**: LOW | **PI**: HIGH

**What**: Add §6.x references throughout the Interview System:
- Every convention question → "See Part 6 §6.1"
- Every termsheet exercise → "See Part 6 §6.2"
- Every P&L/reserve question → "See Part 6 §6.6"
- Every XVA question → "See Part 6 §6.7"
- Every ops question → "See Part 6 §6.9"
- Traceability table → add Part 6 as source

**Why**: The Interview System currently operates as if Part 6 doesn't exist. This is the minimum integration — just adding reference links. Cannot be done until infrastructure content exists to reference FROM.

**Composite Score**: (7 + 6 + 8) / 1 = **21.0**

---

### Rank 8: Infrastructure Behavioural Questions

**Source**: WS11 (Behavioural Interviews)
**Severity**: HIGH
**EV**: 8 | **CV**: 8 | **IE**: LOW | **PI**: MEDIUM

**What**: Add 7 infrastructure behavioural scenarios (IBT.1-IBT.7):
1. "$2M trade break — trader says it's not real. What do you do?"
2. "$500K unexplained P&L — month-end in 2 hours."
3. "You booked a trade incorrectly 3 days ago."
4. "Cash break matching a coupon payment amount."
5. "Two systems show different valuations."
6. "Corporate action notification 2 hours before observation date."
7. "Treasury changes FTP curve mid-month — desk wants to re-price."

**Why**: These are among the most common interview questions for infrastructure roles. They test judgment, escalation instinct, and cross-team communication — all critical for desk survival.

**Composite Score**: (8 + 8 + 5) / 1 = **21.0**

---

### Rank 9: Desk Vocabulary Quick-Fire

**Source**: WS9 (Desk Thinking), WS3 (Infrastructure Coverage)
**Severity**: HIGH
**EV**: 8 | **CV**: 8 | **IE**: LOW | **PI**: MEDIUM

**What**: Add a 20-term desk vocabulary rapid-fire section:
- Flow book vs exotic book
- Hit / lift / axe
- Morning marks
- Flash P&L vs official P&L
- Risk warehousing
- Run the book
- Colour / bleed
- Greeks (in desk context, not textbook)
- Long/short correlation (desk meaning)
- Delta-one

**Why**: Part 6 §6.10 teaches 50+ desk vocabulary terms. Testing them in a rapid-fire format mirrors real desk interviews where a trader will say "what does 'axe' mean?" and expects a 5-second answer.

**Composite Score**: (8 + 8 + 5) / 1 = **21.0**

---

### Rank 10: Role-Specific Question Index

**Source**: WS14 (Navigation)
**Severity**: HIGH
**EV**: 6 | **CV**: 8 | **IE**: LOW | **PI**: MEDIUM

**What**: Add appendix mapping all questions to roles:

**Structuring**: SL.1-SL.12, DS.1-DS.5, D.2, D.3, D.8, PK.1-PK.49 (Tier 2-3), T.1-T.20, MC.1-MC.25, SA.1-SA.10
**Trading**: DS.6-DS.9, D.4, T.1-T.20, PK (Tier 3-4), whiteboard Greeks
**Sales**: DS.10-DS.13, D.1, D.7, SL.1-SL.6, BT.1-BT.10, RG.1-RG.22
**Risk**: DS.14-DS.17, D.5, T.1-T.37, RG.1-RG.22
**Model Validation**: DS.18-DS.21, D.6, T.11-T.20, MC.14-MC.25

**Why**: Candidates preparing for a specific role waste time scanning irrelevant sections. An index makes preparation efficient.

**Composite Score**: (6 + 8 + 5) / 1 = **19.0**

---

### Rank 11: CRA ELN + NTD + TARN STEG Depth Expansion

**Source**: WS2 (Product Coverage)
**Severity**: HIGH
**EV**: 7 | **CV**: 7 | **IE**: LOW | **PI**: MEDIUM

**What**:
- Add CRA ELN (§5.1.10, Complexity 6) Tier 1-3 treatment to Part 2 Product Answer Library
- Expand NTD (Complexity 8) to Tier 1-3
- Expand TARN STEG (Complexity 8) to Tier 1-3

**Why**: CRA ELN is the only Complexity 6+ product without a dedicated answer library entry. NTD and TARN STEG are Complexity 8 products with abbreviated treatment while WOAC (also 8) has full 4-tier.

**Composite Score**: (7 + 7 + 5) / 1 = **19.0**

---

### Rank 12: Written Assessment Infrastructure Expansion

**Source**: WS10 (Calculations), WS3 (Infrastructure)
**Severity**: MEDIUM
**EV**: 8 | **CV**: 7 | **IE**: MEDIUM | **PI**: HIGH

**What**: Add 15 infrastructure MC questions (MC.26-MC.40) and 5 SA questions (SA.11-SA.15):
- MC topics: day count (3), settlement (2), CSA (2), P&L explain (2), reserves (2), XVA (2), model governance (2)
- SA topics: P&L decomposition, convention comparison, termsheet analysis, reserve methodology, trade break investigation

**Composite Score**: (8 + 7 + 8) / 2 = **11.5**

---

### Rank 13: European Rates + Asian Market Cases

**Source**: WS8 (Case Interviews)
**Severity**: MEDIUM
**EV**: 7 | **CV**: 7 | **IE**: LOW | **PI**: MEDIUM

**What**: Add 2 case studies:
- D.9: European Rates Case — CMS Steepener for Euro pension fund (tests STEG family depth, European conventions, BNP/SG-style interview)
- D.10: Asian Autocallable Case — Phoenix/FCN for Asian private bank client (tests DCI/accumulator depth, Asian calendar conventions, Nomura/HSBC-style interview)

**Composite Score**: (7 + 7 + 5) / 1 = **19.0**

---

### Rank 14: Restructuring Clause Questions

**Source**: WS3 (Infrastructure Coverage)
**Severity**: MEDIUM
**EV**: 7 | **CV**: 7 | **IE**: LOW | **PI**: MEDIUM

**What**: Add 3 restructuring clause questions:
1. "Compare Full Restructuring vs No Restructuring — when does the distinction matter?"
2. "A European bank and a US bank trade a CDS on the same reference entity. What restructuring clause does each use, and why?"
3. "Modified Restructuring limits deliverable obligations. What are the limits and why do they exist?"

**Composite Score**: (7 + 7 + 5) / 1 = **19.0**

---

### Rank 15: LIBOR Reference Correction

**Source**: WS1 (Ecosystem Consistency)
**Severity**: MEDIUM
**EV**: 3 | **CV**: 2 | **IE**: TRIVIAL | **PI**: LOW

**What**: Change IRS Tier 2 "LIBOR/SOFR resets" to "SOFR resets (historically LIBOR)."

**Composite Score**: (3 + 2 + 2) / 0.5 = **14.0**

---

## Implementation Priority Matrix

| Priority | Recommendations | Pre-Requisite | Estimated Content |
|:--------:|:---------------:|:-------------:|:-----------------:|
| **P1 — BLOCKING** | Ranks 1-3 (infrastructure content, PC/Ops tracks, termsheet exercises) | None | ~800-1000 lines |
| **P2 — HIGH VALUE** | Ranks 4-9 (traps, whiteboard, career guide, cross-refs, behavioural, vocabulary) | P1 for cross-refs | ~400-500 lines |
| **P3 — QUALITY** | Ranks 10-14 (index, product depth, written assessment, cases, restructuring) | None | ~300-400 lines |
| **P4 — POLISH** | Rank 15 + Low/Nice-to-Have items from gap analysis | None | ~50 lines |

### Total Estimated Addition

Current Interview System: 1,964 lines
Estimated V2.0: ~3,500-3,800 lines (~90% increase)

---

## Implementation Recommendation

### Recommended Approach: Interview System V2.0 Generation

Generate a complete Interview System V2.0 that:
1. Preserves ALL existing product knowledge content (Parts 1-6 unchanged)
2. Adds infrastructure interview content as new sections/question categories
3. Adds 2 new mock interview tracks (PC + Ops)
4. Adds termsheet reading exercises
5. Adds infrastructure traps, whiteboard exercises, calculations, cases
6. Adds career-level path guide
7. Adds Part 6 cross-references throughout
8. Adds role-specific question index
9. Adds desk vocabulary quick-fire section
10. Corrects LIBOR reference
11. Expands CRA ELN, NTD, TARN STEG treatment
12. Adds European rates + Asian market cases

### NOT Recommended

- Modifying existing product content (it's accurate and well-structured)
- Creating a separate infrastructure interview document (breaks ecosystem coherence)
- Publishing V1 as-is with a "Part 6 coming soon" disclaimer

---

## Deliverables Produced

| # | File | Purpose |
|:-:|------|---------|
| 1 | `review/interview_system_ecosystem_audit.md` | 15-workstream audit report (WS1-WS15) |
| 2 | `review/interview_system_gap_analysis.md` | 28 gaps with severity ratings |
| 3 | `review/interview_system_cross_artifact_consistency.md` | Consistency check vs 12 frozen artifacts |
| 4 | `review/interview_system_interview_realism_review.md` | Bank-by-bank realism assessment |
| 5 | `review/interview_system_publication_readiness.md` | Publication quality evaluation |
| 6 | `review/interview_system_final_recommendations.md` | This document — 15 ranked recommendations |

**No changes were made to the Interview System or any other production artifact.**

---

## Final Statement

The Interview System is an exceptional product knowledge interview preparation tool. Its 4-tier answer framework, 49-product coverage, trap library, and mock interview tracks represent genuine innovation in structured products interview preparation.

It has one structural deficiency: it was generated before Part 6 — The Operational Ecosystem existed, and therefore contains zero infrastructure interview content. This gap affects every workstream and is the single blocker to publication.

The recommendation is to generate Interview System V2.0 with Part 6 integration. This is not a rewrite — it is an expansion. All existing content is preserved. The infrastructure domain is added.

---

**End of final recommendations.**
**Audit complete. No artifacts modified. Task C finished.**
