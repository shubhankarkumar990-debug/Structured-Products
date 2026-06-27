# Interview System — Design Review

**Date:** 2026-06-22
**Input:** `design/interview_system_design.md`
**Reviewer:** Independent Design Review

---

## 1. Duplication Check Against Solutions Manual

### Content Overlap Analysis

| SM Component | IS Treatment | Duplication Risk | Status |
|-------------|-------------|:----------------:|:------:|
| 10-step decision model (SM §1.1) | Referenced, not reproduced. Questions TEST the model. | LOW | PASS |
| 40 scenarios (SM Part 2) | IS cases use DIFFERENT client quotes. SM scenarios referenced by number. | MEDIUM — must enforce at generation time | PASS (with guard) |
| 18 anti-patterns (SM Part 3) | Converted to "spot the mistake" trap questions. Content reframed. | LOW | PASS |
| 49-row replacement table (SM Part 4) | IS questions ask "what substitute?" — answers REFERENCE SM table. | LOW | PASS |
| Market regime matrix (SM §1.3) | IS questions test regime awareness. Matrix not reproduced. | LOW | PASS |
| Persona filter (SM §1.2) | IS suitability questions use personas. Filter logic not reproduced. | LOW | PASS |

### Potential Duplication Hotspots

| Hotspot | Risk | Mitigation |
|---------|:----:|-----------|
| Part 4.3 Structuring Logic Questions | HIGH | Answers must say "See SM Scenario X.Y" — not restate the scenario |
| Part 4.4 Case Interview Questions | MEDIUM | Client quotes must be DISTINCT from SM's 40 quotes. Different names, different contexts, similar logic. |
| Part 6.1 Technical Traps vs SM Anti-Patterns | MEDIUM | SM says "don't do X." IS says "candidate says X — why is this wrong?" Different framing, same underlying insight. Acceptable if framing is genuinely different. |
| Part 2 Tier 4 answers | LOW | Tier 4 discusses trade-offs. SM scenarios also discuss trade-offs. IS must add NEW perspective (regulatory, historical, buy-side). |

**Verdict: Deduplication strategy is sound.** Boundary rule ("IS asks, SM answers") is clear. Primary risk is at generation time — case questions drifting into SM territory. Recommend: during generation, cross-check every case question against SM's 40 client quotes.

---

## 2. Missing Competencies Check

### Required Competencies (from authorization)

| Competency | Covered In | Depth | Status |
|-----------|-----------|:-----:|:------:|
| Product Knowledge (all 49) | Part 2 (196 blocks) + Part 4.2 | Deep | PASS |
| Product Comparisons | Part 3 (10 full + 25 quick) | Deep | PASS |
| Product Suitability | Part 4.3 + Part 5 Sales Track | Moderate | PASS |
| Market Regime Effects | Part 2 Tier 3 + Part 4.1 | Moderate | PASS |
| Decision Framework | Part 4.3 (tests SM framework) | Moderate | PASS |
| Product Selection | Part 4.4 Case Questions | Deep | PASS |
| Complexity Governance | Part 4.3 + Part 5 Structuring Track | Moderate | PASS |
| Anti-Patterns | Part 6 (30 traps) | Deep | PASS |
| Greeks | Part 4.1 Technical + Part 5 Trading Track | Deep | PASS |
| Options | Part 4.1 Technical | Deep | PASS |
| Rates | Part 4.1 Technical | Moderate | PASS |
| Credit | Part 4.1 Technical | Moderate | PASS |
| Volatility | Part 4.1 Technical | Deep | PASS |
| Correlation | Part 4.1 Technical | Deep | PASS |
| Client Scenarios | Part 4.4 (30 cases) | Deep | PASS |
| Trade-Offs | Part 2 Tier 4 + Part 4.4 | Deep | PASS |
| Rejected Alternatives | Part 4.4 (scoring rubric expects it) | Moderate | PASS |
| Structuring Desk | Part 5 Track 1 | Deep | PASS |
| Trading Desk | Part 5 Track 2 | Deep | PASS |
| Sales Desk | Part 5 Track 3 | Deep | PASS |
| Risk Desk | Part 5 Track 4 | Deep | PASS |
| Model Validation | Part 5 Track 5 | Deep | PASS |
| Buy-Side Perspective | Part 1.1 + §11 additions | Moderate | PASS |
| Sell-Side Perspective | Default throughout | Deep | PASS |
| Beginner Level | Part 4 row 1 + Part 5 difficulty 1 | 40 questions | PASS |
| Intermediate Level | Part 4 row 2 + Part 5 difficulty 2 | 65 questions | PASS |
| Advanced Level | Part 4 row 3 + Part 5 difficulty 3 | 65 questions | PASS |
| Expert Level | Part 4 row 4 + Part 5 difficulty 4 | 40 questions | PASS |

### Gaps Identified

| Gap | Severity | Recommendation |
|-----|:--------:|---------------|
| **Regulatory knowledge** — MiFID II, PRIIPs, KID requirements not explicit in question bank | MEDIUM | Add 3–5 regulatory questions in Part 4.5 (Desk-Specific, Risk role). Structuring and Sales tracks should include KYP/suitability round. |
| **Quantitative/pricing** — Monte Carlo, finite difference, calibration mentioned in MV track but no standalone question set | LOW | Part 4.1 Technical section covers this. MV Track Round 3 goes deep. Sufficient for interview prep. |
| **Behavioral questions** — 10 framing traps exist but no "tell me about a time" behavioral question set | LOW | Behavioral interviews are firm-specific. 10 framing traps cover the most common behavioral patterns in SP interviews. Adding more would bloat without adding value. |
| **Market microstructure** — bid-ask spreads, market making, flow dynamics | LOW | Trading Track Round 4 touches this. Not a dedicated section. Acceptable — SP interviews rarely go deep on microstructure. |

**Verdict: 0 CRITICAL gaps, 1 MEDIUM gap (regulatory).** Recommend adding regulatory questions during generation.

---

## 3. Progression Logic Verification

### Difficulty Escalation

| Dimension | Beginner → Expert Progression | Coherent? |
|-----------|------------------------------|:---------:|
| Product complexity | 2–3 → 3–5 → 5–7 → 7–10 | YES — maps to Atlas complexity bands |
| Question depth | Definition → Greeks → Cross-product → Model choice | YES — builds on prior level |
| Expected experience | 0–1 yr → 1–3 yr → 3–5 yr → 5+ yr | YES — realistic career progression |
| Mock track rounds | Rapid fire → Deep dive → Case → Comparison → Trap | YES — mirrors real interview escalation |
| Answer tiers | Tier 1 → Tier 2 → Tier 3 → Tier 4 | YES — 30s → 2min → 5min → 10min |

### Role-Specific Progression

The §1.3 Role-Specific Expectations Matrix correctly differentiates:

| Check | Expected | Design | Match? |
|-------|----------|--------|:------:|
| Structuring needs deepest product knowledge at low complexity | Tier 4 for Beginner products | §1.3 row 1: Structuring = Tier 4 | YES |
| Model Val needs deepest knowledge at high complexity | Tier 4 for Expert products | §1.3 row 4: MV = Tier 4 | YES |
| Sales needs breadth not depth at high complexity | Tier 1 for Expert products | §1.3 row 4: Sales = Tier 1 | YES |
| Trading needs consistent moderate depth | Tier 3 across Beginner–Advanced | §1.3 rows 1–3: Trading = Tier 3 | YES |

### Concern: Expert-Level Product Selection for Mock Tracks

Design lists CDO, TARN STEG, NTD, DKIP, CRA SRT as Expert mock products. CDO (10) is unique in the universe — no comparison possible. DKIP (7) is an ELN variant, possibly better in Advanced tier.

**Severity: LOW.** Mock tracks are illustrative — the exact product selection can be adjusted at generation time without structural change.

**Verdict: Progression logic is sound.** Clean escalation across all dimensions.

---

## 4. Realistic Interview Formats

### Round Structure Validation

| Track | Total Time | Round Count | Realistic? | Notes |
|-------|:----------:|:----------:|:----------:|-------|
| Structuring | 60 min | 5 rounds | YES | Standard desk interview format |
| Trading | 60 min | 5 rounds | YES | Greeks quiz + scenario is standard |
| Sales | 60 min | 5 rounds | YES | Elevator pitch round is standard |
| Risk | 60 min | 5 rounds | YES | Stress test design is standard |
| Model Val | 60 min | 5 rounds | YES | Calibration + numerical methods is standard |

### Format Realism Checks

| Check | Standard Practice | Design | Match? |
|-------|-------------------|--------|:------:|
| Phone screen = rapid-fire | Yes | Tier 1 (30s) answers | YES |
| First round = technical test | Yes | Part 4 question bank | YES |
| Desk round = practical scenarios | Yes | Part 5 Rounds 2–3 | YES |
| Final round = senior judgment | Yes | Tier 4 answers + framing traps | YES |
| Buy-side = due diligence focus | Yes | §11 buy-side additions | YES |
| Written test component | Common at banks | Not explicitly designed | MINOR GAP |

**Written Test Gap:** Many banks include a 30–60 minute written test (multiple choice + short answer). Design has no explicit "written test" format.

**Recommendation:** Part 4 question bank can serve as written test material. Add a note during generation: "Questions marked [WT] are suitable for written test format."

**Verdict: Interview formats are realistic.** 1 minor gap (written test tagging).

---

## 5. Product Family Coverage

### All-Family Presence Check

| Family | Part 2 | Part 3 | Part 4 | Part 5 | Part 6 | Covered? |
|--------|:------:|:------:|:------:|:------:|:------:|:--------:|
| ELN (15) | 15 | 5+ pairs | 55–65 Q | All tracks | 5+ traps | YES |
| Swaps (8) | 8 | 3+ pairs | 25–35 Q | 3 tracks | 3+ traps | YES |
| SRT (5) | 5 | 1+ pair | 15–20 Q | 3 tracks | 2+ traps | YES |
| STEG (4) | 4 | 1+ pair | 12–16 Q | 3 tracks | 2+ traps | YES |
| CLN (5) | 5 | 3+ pairs | 18–24 Q | All tracks | 3+ traps | YES |
| Other (12) | 12 | 3+ pairs | 30–40 Q | All tracks | 3+ traps | YES |

### Product Coverage Floor

Design guarantees every product appears in ≥2 sections (Part 2 + Part 4 minimum). Top 10 products appear in ≥6 sections.

**Concern:** 24 "remaining" products get abbreviated Tier 3 and no Tier 4. Candidates preparing for niche products (e.g., TARN STEG for a rates desk) won't find deep answer templates.

**Mitigation:** Tier 4 for abbreviated products says "cross-reference to similar product" — e.g., TARN STEG Tier 4 references Callable STEG Tier 4 + adds TARN-specific target mechanics. This is acceptable for interview prep.

**Verdict: All families covered.** Balance slightly favors ELN (largest family, most interview-relevant). Matches reality.

---

## 6. Scalability Assessment

| Dimension | Scalable? | Cost to Add | Structural Change? |
|-----------|:---------:|:----------:|:------------------:|
| New product | YES | ~30 lines | NO |
| New role | YES | ~60 lines | NO |
| New difficulty level | NO (4 is sufficient) | N/A | N/A |
| New question category | YES | ~50–100 lines | NO |
| New mock track | YES | ~50 lines | NO |
| New trap category | YES | ~30 lines | NO |

### Architecture Extensibility

Part 2 (answer templates) uses a repeating format — adding products is mechanical.
Part 4 (question bank) uses a taxonomy grid — adding categories expands the grid.
Part 5 (mock tracks) are independent — adding tracks doesn't affect existing ones.

**Verdict: Highly scalable.** No structural redesign needed for any extension type.

---

## 7. Line Budget Feasibility

| Part | Target | Feasibility | Risk |
|------|:------:|:-----------:|:----:|
| Part 1 | 120 | Easy | LOW |
| Part 2 | 1,040 | Tight — 49 products × ~21 avg lines = 1,029. Headers add ~100. | MEDIUM |
| Part 3 | 200 | Easy | LOW |
| Part 4 | 500 | Tight — 210 questions × ~2.4 lines avg. Works if format is compact. | MEDIUM |
| Part 5 | 250 | Easy | LOW |
| Part 6 | 150 | Easy | LOW |
| **Total** | **2,310** | Within 1,800–2,500 target | PASS |

### Part 2 Risk Mitigation

The 3-tier treatment (full/full-3/abbreviated) keeps Part 2 under 1,100 lines. Without this tiering, 49 × 29 lines = 1,421 lines — would blow the budget.

**Verdict: Budget is feasible.** Parts 2 and 4 are tight but manageable with the specified compression strategies.

---

## 8. Issues Summary

| ID | Issue | Severity | Blocking? | Recommendation |
|----|-------|:--------:|:---------:|---------------|
| DR-1 | Regulatory questions not explicit in taxonomy | MEDIUM | NO | Add 3–5 regulatory questions to Part 4.5 (Risk role) during generation |
| DR-2 | Written test format not tagged | LOW | NO | Tag questions with [WT] during generation |
| DR-3 | Case question duplication risk with SM | MEDIUM | NO | Cross-check every case quote against SM's 40 quotes during generation |
| DR-4 | CDO in Expert mock may be too isolated (no comparator) | LOW | NO | Consider swapping CDO with WOAC in Expert Round 1 |
| DR-5 | 24 products get abbreviated Tier 3 | LOW | NO | Cross-reference system compensates. Acceptable for interview prep. |

**0 CRITICAL. 0 HIGH. 2 MEDIUM. 3 LOW.**

---

## 9. Verdict

### APPROVED FOR GENERATION

The design:
- Covers all 6 required areas (product, structuring, technical, case, desk, difficulty)
- Deduplicates cleanly against Solutions Manual
- Maps all 49 products across 5 desk roles
- Provides 4 difficulty levels with coherent progression
- Uses realistic interview formats
- Scales for future products and roles
- Stays within line budget

### Pre-Generation Checklist

| # | Action | When |
|:-:|--------|------|
| 1 | Cross-check all 30 case questions against SM's 40 client quotes | During Part 4.4 generation |
| 2 | Add 3–5 regulatory questions to Part 4.5 | During Part 4 generation |
| 3 | Tag written-test-suitable questions with [WT] | During Part 4 generation |
| 4 | Verify every SM reference uses correct section/scenario number | Post-generation review |

---

*Design review complete. 2026-06-22.*
