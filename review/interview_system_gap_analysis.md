# Interview System — Gap Analysis

**Date**: 2026-06-25
**Source**: 15-workstream ecosystem audit
**Classification**: CRITICAL (0), HIGH (1), MEDIUM (2), LOW (3), NICE-TO-HAVE (4)

---

## Critical Issues (Publication-Blocking)

### C-1: Zero Infrastructure Interview Content

**Gap**: The Interview System contains zero questions on P&L Explain, IPV, reserves, FTP methodology, XVA, settlement conventions, day count conventions, CSA, corporate actions, trade lifecycle, booking, reconciliation, trade breaks, golden source, static data, fair value hierarchy, model governance (SR 11-7), capital metrics (RWA/SA-CCR/EAD/PFE), or desk vocabulary.

**Root Cause**: Generated 2026-06-22, three days before Part 6 was integrated into the Desk Bible.

**Impact**: Candidates using this system for VP+ interviews at any major bank will be unprepared for ~40% of questions. PC/Ops/Treasury candidates will be unprepared for ~80% of questions.

**Recommendation**: Add a new Part (Part 7 or integrated into existing parts) covering infrastructure interview questions. Minimum: 40 technical questions, 6 whiteboard exercises, 4 case studies, 10 traps, 2 mock interview tracks (PC + Ops).

**Educational Value**: 10/10. **Career Value**: 10/10. **Implementation Effort**: HIGH. **Publication Impact**: BLOCKING.

---

### C-2: Missing Roles — Product Control, Operations, Treasury

**Gap**: 5 roles covered (Structuring, Trading, Sales, Risk, Model Validation). 6 roles missing (Product Control, Operations, Treasury, Finance, Legal, Compliance). No mock interview tracks, no questions, no cases for the missing roles.

**Impact**: Product Control alone hires more analysts than any desk role. Operations is the largest function in a structured products business. Treasury is a critical pricing function. None can use this interview system.

**Recommendation**: Add mock interview tracks for at minimum: Product Control and Operations. Add targeted questions for Treasury. Legal/Compliance/Finance can be addressed through cross-functional questions rather than dedicated tracks.

**Educational Value**: 10/10. **Career Value**: 10/10. **Implementation Effort**: HIGH. **Publication Impact**: BLOCKING.

---

### C-3: Zero Termsheet Reading Exercises

**Gap**: No practical termsheet interpretation tests. Part 6 §6.2 teaches 40+ termsheet fields. The Interview System never tests whether a candidate can read one.

**Impact**: "Read this termsheet and identify the risks" is the single most common structuring interview exercise at every bank. Its absence is immediately noticeable.

**Recommendation**: Add 3-5 termsheet reading exercises at Beginner through Advanced difficulty. Include: field identification, clean/dirty price calculation, convention interpretation, red flag spotting.

**Educational Value**: 9/10. **Career Value**: 9/10. **Implementation Effort**: MEDIUM. **Publication Impact**: BLOCKING.

---

### C-4: Zero Infrastructure Calculations

**Gap**: No questions requiring: day count calculation (ACT/360 vs 30/360), clean/dirty price conversion, accrued interest calculation, P&L Explain decomposition, reserve calculation, XVA charge sizing.

**Impact**: Calculation questions are the most reliable way to test infrastructure understanding. Without them, the Interview System cannot differentiate candidates who truly understand conventions from those who memorize definitions.

**Recommendation**: Add 10-15 calculation questions spanning: day count (3), pricing (3), P&L explain (3), reserves (2), XVA/capital (2-3).

**Educational Value**: 9/10. **Career Value**: 9/10. **Implementation Effort**: MEDIUM. **Publication Impact**: BLOCKING.

---

### C-5: No Part 6 Cross-References

**Gap**: Zero references to Part 6 sections. No "See §6.1 for convention details" or "See §6.6 for P&L Explain methodology" annotations. The Interview System operates as if Part 6 does not exist.

**Impact**: Readers cannot navigate between interview questions and the source material that teaches the concepts. The ecosystem link is broken.

**Recommendation**: Add §6.x references throughout. Every infrastructure question should reference its Part 6 source section.

**Educational Value**: 7/10. **Career Value**: 6/10. **Implementation Effort**: LOW. **Publication Impact**: HIGH.

---

## High Issues (Quality-Limiting)

### H-1: CRA ELN Missing from Product Answer Library

**Gap**: CRA ELN (§5.1.10, Complexity 6) has no tier treatment in Part 2. It appears only in comparison pairs and PK.10. All other Complexity 6+ products have at least Tier 1-3 treatment.

**Recommendation**: Add Tier 1-3 treatment for CRA ELN.

**Educational Value**: 7/10. **Career Value**: 6/10. **Implementation Effort**: LOW. **Publication Impact**: MEDIUM.

---

### H-2: NTD and TARN STEG Undertreated

**Gap**: Both are Complexity 8 with only Tier 1-2 treatment. WOAC (also Complexity 8) has full 4-tier treatment.

**Recommendation**: Expand NTD and TARN STEG to Tier 1-3 minimum.

**Educational Value**: 7/10. **Career Value**: 7/10. **Implementation Effort**: LOW. **Publication Impact**: MEDIUM.

---

### H-3: No Career-Level Path Guide

**Gap**: No mapping from career level to recommended preparation path. A candidate preparing for a VP Trading interview cannot easily identify which questions to prioritize.

**Recommendation**: Add a career-level preparation matrix: Graduate (focus on Tier 1-2 for Beginner products), Analyst (Tier 1-3 for Intermediate), Associate (all Tier 1-3), VP (Tier 1-4 + infrastructure), Director/MD (Tier 4 + cross-functional + regulatory + infrastructure).

**Educational Value**: 8/10. **Career Value**: 9/10. **Implementation Effort**: LOW. **Publication Impact**: HIGH.

---

### H-4: No Infrastructure Behavioural Questions

**Gap**: BT.1-BT.10 cover product-facing scenarios only. No behavioural questions for trade breaks, P&L discrepancies, production incidents, system failures, or cross-team escalations.

**Recommendation**: Add 5-7 infrastructure behavioural scenarios.

**Educational Value**: 8/10. **Career Value**: 8/10. **Implementation Effort**: LOW. **Publication Impact**: MEDIUM.

---

### H-5: No Infrastructure Whiteboard Exercises

**Gap**: 14 high-value whiteboard topics from Part 6 are untested: P&L waterfall, capital structure, CSA flows, trade lifecycle, XVA bridge, FVH classification, FTP curve, settlement flow, corporate action adjustment, model lifecycle, day count comparison, Modified Following decision, reserve governance, regulatory map.

**Recommendation**: Add 6-8 infrastructure whiteboard exercises (prioritize: P&L waterfall, capital structure, day count calculation, Modified Following, trade lifecycle, XVA bridge).

**Educational Value**: 9/10. **Career Value**: 8/10. **Implementation Effort**: MEDIUM. **Publication Impact**: HIGH.

---

### H-6: Missing Infrastructure Traps

**Gap**: 20 technical traps (T.1-T.20) + 10 behavioural traps (BT.1-BT.10) = 30 total. All product-focused. Zero infrastructure traps.

**Recommendation**: Add 10-15 infrastructure traps. Examples:
- "Modified Following and Following are the same thing" (WRONG — month-end boundary)
- "Day count doesn't matter because the differences are small" (WRONG — material on large notionals)
- "IPV is just checking the trader's price against Bloomberg" (WRONG — full process)
- "P&L Explain residual is always noise" (WRONG — must be investigated)
- "Reserves are just a cushion against losses" (WRONG — specific risk quantification)
- "CSA threshold means you don't post collateral" (WRONG — threshold is the UNSECURED amount)
- "FTP is just the risk-free rate" (WRONG — includes credit spread + liquidity premium)
- "XVA is a back-office adjustment" (WRONG — real economic cost)
- "Golden source means one system for everything" (WRONG — different data types have different golden sources)
- "Corporate actions don't affect derivatives" (WRONG — barrier adjustments, payout modifications)

**Educational Value**: 9/10. **Career Value**: 9/10. **Implementation Effort**: MEDIUM. **Publication Impact**: HIGH.

---

### H-7: Desk Vocabulary Not Tested

**Gap**: Part 6 §6.10 teaches 50+ desk vocabulary terms across 6 role vocabularies. The Interview System never tests whether candidates know: flow book vs exotic book, risk warehousing, hit/lift/axe, morning marks, flash P&L, or any desk-specific language.

**Recommendation**: Add a desk vocabulary quick-fire section (similar to the Tier 1 elevator pitch format). Test 15-20 key terms.

**Educational Value**: 8/10. **Career Value**: 8/10. **Implementation Effort**: LOW. **Publication Impact**: MEDIUM.

---

### H-8: Role-Specific Question Index Missing

**Gap**: No index mapping questions to roles. A candidate preparing for a Sales interview must scan the entire document to find all Sales-relevant questions.

**Recommendation**: Add an appendix with role-based question indices.

**Educational Value**: 6/10. **Career Value**: 8/10. **Implementation Effort**: LOW. **Publication Impact**: MEDIUM.

---

## Medium Issues (Enhancement)

### M-1: LIBOR Reference in IRS Tier 2

IRS Tier 2 (line 126) says "LIBOR/SOFR resets." LIBOR is discontinued. Should read "SOFR resets (historically LIBOR)" for accuracy. Part 6 §6.1 correctly treats SOFR as the current standard.

**Implementation Effort**: TRIVIAL. **Publication Impact**: LOW.

---

### M-2: No European Rates Case Study

BNP Paribas, Societe Generale, and other European banks will ask STEG/CMS-focused case studies. The current cases lean toward equity-linked and credit products.

**Recommendation**: Add 1-2 European rates-focused cases.

**Implementation Effort**: LOW. **Publication Impact**: MEDIUM.

---

### M-3: No Asian Market Focus Case

Nomura, HSBC Asia, UBS Asia will test autocallable depth (Phoenix/FCN dominate Asian structured products markets). DCI is mentioned but no Asia-specific case exists.

**Recommendation**: Add 1 Asia-focused autocallable case.

**Implementation Effort**: LOW. **Publication Impact**: MEDIUM.

---

### M-4: Written Assessment Missing Infrastructure Questions

25 MC + 10 SA + 5 mini cases = 40 questions. All product-focused. Need at least 10-15 infrastructure MC questions and 3-5 SA questions.

**Implementation Effort**: MEDIUM. **Publication Impact**: HIGH.

---

### M-5: Mock Track Duration Inconsistency

All mock tracks are 60 minutes. Real interviews vary: phone screens (30 min), first round (45-60 min), desk round (60-90 min). Adding timing variants would improve realism.

**Implementation Effort**: LOW. **Publication Impact**: LOW.

---

### M-6: No Restructuring Clause Interview Questions

CDS restructuring clauses (FR/MR/MMR/NR) with regional conventions are a core credit interview topic. Zero questions exist. Part 6 §6.4 teaches this comprehensively.

**Recommendation**: Add 2-3 restructuring clause questions (one comparison: "FR vs NR — when does it matter?").

**Implementation Effort**: LOW. **Publication Impact**: MEDIUM.

---

## Low Issues (Polish)

### L-1: Traceability Table Incomplete

Line 1957: The traceability table doesn't reference Part 6, the Searchability Alias Map, the Cross-Reference Map, or the Visual Specifications.

---

### L-2: No Difficulty Distribution Analysis

No summary showing how many questions exist per difficulty level. Would help candidates assess preparation completeness.

---

### L-3: Answer Key Formatting

MC answer key uses compact table format. SA answer key uses longer narrative format. Standardizing would improve readability.

---

### L-4: Comparison Pair Coverage

25 pairs vs Atlas Appendix F (which has more). Some Atlas pairs not represented. Low priority — 25 is sufficient.

---

## Nice-to-Have Improvements

### N-1: Interview Scoring Rubric Enhancement

Current scoring: Excellent/Adequate/Poor. Could add: "What makes a PERFECT answer" for each case study.

### N-2: Timed Practice Sets

Group questions into 30/45/60-minute practice sets with difficulty mixing.

### N-3: Cross-Product Comparison Exercises

"Given these 3 products, rank by: suitability for this client, capital charge, hedging cost, liquidity." Tests multi-dimensional thinking.

### N-4: "Day in the Life" Interview Prep

Map Part 6 §6.10's day-in-the-life table to interview questions: "What does a trader do at 7:30 AM?"

### N-5: Video/Audio Pitch Practice Guide

Framework for practicing 30-second elevator pitches aloud, not just reading them.

---

## Summary Statistics

| Severity | Count | Publication Impact |
|:--------:|:-----:|:------------------:|
| CRITICAL | 5 | All are BLOCKING |
| HIGH | 8 | 5 are quality-limiting |
| MEDIUM | 6 | Enhancement |
| LOW | 4 | Polish |
| Nice-to-Have | 5 | Optional |
| **TOTAL** | **28** | |

---

**End of gap analysis.**
