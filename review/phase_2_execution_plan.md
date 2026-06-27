# Phase 2 Execution Plan

**Date:** 2026-06-22
**Input:** `review/phase_2_application_architecture_review.md`, `review/phase_2_priority_ranking.md`
**Artifacts to build:** 5 (from 11 proposals)
**Framework:** v1.3.1 (frozen)

---

## Execution Summary

| Phase | Artifact | Est. Lines | Effort | Dependencies |
|:-----:|----------|:----------:|:------:|:------------:|
| 1 | Solutions Manual | 1,200–1,400 | High | Atlas, Matrix, §3/§8 per chapter |
| 2 | Interview System | 1,800–2,200 | High | Atlas E/F/G, Matrix B, §19/§20 per chapter |
| 3 | Hedging Playbook | 1,000–1,400 | Medium | Atlas D, Matrix Part 2/3, §15, §2.7 |
| 4 | Case Study Library | 1,200–1,600 | Medium | All chapter §10/§18, market knowledge |
| 5 | Trade Break Library | 1,200–1,500 | Medium | §16/§17 per chapter, §2.8 Systems |

**Total estimated output:** 6,400–8,100 lines across 5 artifacts.

---

## Phase 1: Solutions Manual

**File:** `production/solutions_manual.md`

### Structure

| Part | Content | Source | New % |
|:----:|---------|--------|:-----:|
| 1 | Structuring Decision Framework | Matrix Decision Trees + new methodology | 85% |
| 1.1 | The Structurer's Mental Model | How to map client objectives to product features | 100% |
| 1.2 | Risk Budget Framework | Vol view, credit view, rates view, liquidity, complexity | 90% |
| 1.3 | Market Regime Awareness | Which products work in which environments | 80% |
| 2 | Problem → Product Scenarios | §3/§8 per chapter + cross-product synthesis | 75% |
| 2.1 | Capital Protection Scenarios | 6 scenarios covering PPN → Airbag spectrum | 70% |
| 2.2 | Yield Enhancement Scenarios | 8 scenarios from RC → WOAC progression | 70% |
| 2.3 | Rates/Inflation Scenarios | 5 scenarios: STEG, SRT, swaps solutions | 80% |
| 2.4 | Credit Exposure Scenarios | 4 scenarios: CLN family, funded vs unfunded | 75% |
| 2.5 | Portfolio Hedging Scenarios | 5 scenarios: variance swaps, accumulators, options | 80% |
| 2.6 | Complex/Multi-Asset Scenarios | 4 scenarios: SNOW, WOAC, CDO, multi-family | 90% |
| 3 | Decision Matrix Quick Reference | Matrix Views reformatted for problem-first lookup | 40% |
| 4 | Anti-Patterns | "Client wants X but you should NOT recommend Y because..." | 95% |

### Source Data Required
- Atlas DNA cards (49 products — read §3 "What Problem" and §8 "Client Perspective" fields)
- Matrix Decision Trees 1–3 (existing classification logic)
- Matrix Part 3 (Typical Buyer, Use Case per product)
- §7 "How the Bank Makes Money" (economics constraints)
- §12 "Product Construction" (feasibility constraints)

### Review
Generate `review/solutions_manual_review.md` after completion. Verify: all 49 products reachable via at least one scenario, no product recommended outside its complexity constraints, all scenarios cite Matrix evidence.

---

## Phase 2: Interview System

**File:** `production/interview_system.md`

### Structure

| Part | Content | Source | New % |
|:----:|---------|--------|:-----:|
| 1 | Interview Strategy Guide | New methodology | 100% |
| 1.1 | How Structured Products Interviews Work | Role-specific expectations | 100% |
| 1.2 | The 4-Tier Answer Framework | 30-sec / 2-min / desk / senior templates | 100% |
| 2 | Product Answer Templates | §1/§11/§14 per chapter → compressed answers | 60% |
| 2.1 | Per-Product 4-Tier Answers | 49 products × 4 tiers = 196 answer blocks | 60% |
| 3 | Comparison & Confusion Pairs | Atlas F + Matrix A → structured comparisons | 40% |
| 3.1 | Top 8 Interview Pairs | Full structured comparison (side-by-side DNA, divergence) | 50% |
| 3.2 | Quick Differentiation Guide | 25 pairs, one-line key difference (from Atlas F) | 20% |
| 4 | Interview Question Bank | §19 + Atlas E + new categories | 40% |
| 4.1 | Curated Question Set | ~150 highest-value questions (not all 392+) | 50% |
| 4.2 | Question Difficulty Mapping | Tier 1–5 difficulty using Atlas G complexity bands | 30% |
| 5 | Mock Interview Tracks | New | 100% |
| 5.1 | 6 Role-Specific Tracks | Intern → Senior Structurer, 5 rounds each | 100% |
| 5.2 | Scoring Rubric | What good/adequate/poor answers look like | 100% |
| 6 | Interview Traps & Anti-Patterns | Matrix B traps + §20 Common Mistakes | 40% |

### Source Data Required
- Atlas Appendix E (49 interview questions — reference, don't recreate)
- Atlas Appendix F (25 confusion pairs — reference for Part 3.2)
- Atlas Appendix G (49 learning difficulty — map to question difficulty)
- Matrix Appendix A (25 pairs with dimensional evidence — for Part 3.1)
- Matrix Appendix B (10 priority products, 8 traps — for Parts 4/6)
- §19 Knowledge Check per chapter (~343 existing questions — curate, don't copy)
- §20 Common Mistakes per chapter (~245 entries — synthesize into traps)
- §1 Explain Like I'm New (30-second answer source)
- §11 Formal Definition (2-minute answer source)
- §14 Desk Reality (desk-level answer source)

### Deduplication Rules
- Questions already in Atlas E: REFERENCE by Atlas entry number, don't reproduce
- Confusion pairs already in Atlas F: REFERENCE, add structured comparison for top 8 only
- Interview traps already in Matrix B: INCORPORATE with expanded context
- §19 questions: CURATE ~150 from ~343 (remove redundant, low-value)

### Review
Generate `review/interview_system_review.md`. Verify: all 49 products have answer templates, curated questions cover all 5 tiers, no Atlas/Matrix content duplicated verbatim.

---

## Phase 3: Hedging Playbook

**File:** `production/hedging_playbook.md`

### Structure

| Part | Content | Source | New % |
|:----:|---------|--------|:-----:|
| 1 | Hedging Fundamentals | §2.7 expanded | 50% |
| 1.1 | Greek Exposures by Product Family | §15 per chapter → family-level synthesis | 60% |
| 1.2 | Hedging Instrument Taxonomy | What hedges what (Delta → stock, Vega → options, etc.) | 70% |
| 2 | Per-Product Hedging Cards | §15 + Matrix Part 3 → structured format | 50% |
| 2.1 | 49 Hedging Cards | Primary risk, hedge, dynamic strategy, failure mode, residual | 50% |
| 3 | Cross-Product Hedging | New synthesis | 90% |
| 3.1 | Book-Level Hedging | How to hedge a portfolio with offsetting Greeks | 95% |
| 3.2 | Cross-Family Hedge Interactions | When hedging product A affects product B | 90% |
| 3.3 | Residual Risk Map | What CANNOT be hedged after best-effort hedging | 85% |
| 4 | Hedge Failure Modes | New | 95% |
| 4.1 | 15 Common Failure Patterns | Gap risk, correlation breakdown, liquidity squeeze, etc. | 95% |
| 4.2 | Product-Specific Failures | Which products are most vulnerable to which failure mode | 80% |
| 5 | Risk Metric Quick Reference | Atlas Appendix D → operational format | 30% |

### Source Data Required
- Atlas Appendix D (19 risk metrics with product mappings)
- Matrix Part 2 (Vol Exposure, Correlation, Path Dependency per product)
- Matrix Part 3 (Primary Risk, Primary Hedge per product)
- §15 Risk Analysis per chapter (risk tables — ~294 entries)
- §2.7 How Desks Hedge (general hedging framework)
- §1.4 Greeks primer (Greek definitions and intuition)

### Review
Generate `review/hedging_playbook_review.md`. Verify: all 49 products have hedging cards, all 19 Atlas D metrics mapped, cross-product hedging covers all 6 families.

---

## Phase 4: Case Study Library

**File:** `production/case_study_library.md`

### Structure

| Part | Content | Source | New % |
|:----:|---------|--------|:-----:|
| 1 | Case Study Framework | How to analyze a market event through the SP lens | 100% |
| 2 | Market Event Case Studies | Historical events mapped to product families | 95% |
| 2.1 | Credit Events (5 cases) | 2008 Lehman CLN, European sovereign, etc. | 95% |
| 2.2 | Volatility Events (5 cases) | 2018 Volmageddon, COVID crash, etc. | 95% |
| 2.3 | Barrier Events (4 cases) | Barrier breaches, knock-in cascades | 95% |
| 2.4 | Correlation Events (3 cases) | Correlation breakdown, worst-of blowups | 95% |
| 2.5 | Rates Events (3 cases) | Rate shock, curve inversion impacts | 95% |
| 3 | Trade Success Stories | Well-structured trades in various regimes | 90% |
| 3.1 | Capital Protection in Downturns (3 cases) | PPN/Airbag during crashes | 90% |
| 3.2 | Yield Enhancement in Range-Bound Markets (3 cases) | RC/Phoenix in low-vol | 90% |
| 4 | Cross-Product Analysis | Same event, multiple product impacts | 95% |
| 5 | Lessons Learned | Patterns across all case studies | 90% |

### Source Data Required
- §10 "What Happens When Markets Move" per chapter (scenario analysis — directional inputs)
- §15 Risk Analysis (which risks materialized in each event)
- §18 Worked Examples (numerical framework for calculations)
- Atlas DNA cards (product features relevant to each event)
- Matrix Part 2 (risk dimensions to identify affected products per event)

### Review
Generate `review/case_study_review.md`. Verify: all 6 families represented, minimum 20 case studies, each case follows consistent format, product references match Atlas.

---

## Phase 5: Trade Break Library

**File:** `production/trade_break_library.md`

### Structure

| Part | Content | Source | New % |
|:----:|---------|--------|:-----:|
| 1 | Trade Break Investigation Framework | New methodology | 100% |
| 1.1 | Symptom Classification | P&L break, position mismatch, failed settlement, etc. | 95% |
| 1.2 | Investigation Methodology | Triage → isolate → diagnose → resolve → prevent | 100% |
| 2 | Trade Break Case Studies | §16/§17 context + new investigation paths | 80% |
| 2.1 | Booking Breaks (8 cases) | System mismatches, wrong fields, missing legs | 75% |
| 2.2 | Pricing Breaks (6 cases) | Model differences, market data, parameter errors | 85% |
| 2.3 | Lifecycle Breaks (6 cases) | Missed observations, barrier events, early termination | 80% |
| 2.4 | Settlement Breaks (5 cases) | Redemption calculation, coupon payment, FX settlement | 80% |
| 3 | System-Specific Patterns | §2.8 + §16 → NEMO/Sophis common failures | 60% |
| 4 | Red Flag → Break Mapping | §17 red flags → which break type they signal | 50% |
| 5 | Prevention Checklist | Post-investigation controls and checks | 90% |

### Source Data Required
- §16 Booking and Systems per chapter (49 booking tables — system context)
- §17 Red Flags per chapter (~245 red flag entries — symptom inputs)
- §13 Lifecycle per chapter (event timelines — lifecycle break context)
- §2.8 Systems Primer (NEMO/Sophis architecture)
- §2.5/§2.6 Product/Trade Lifecycle (general lifecycle framework)

### Review
Generate `review/trade_break_review.md`. Verify: minimum 25 case studies, all system pairs (NEMO/Sophis) covered, red flag mapping complete for all families.

---

## Execution Timeline

| Phase | Artifact | Estimated Sessions | Cumulative |
|:-----:|----------|:------------------:|:----------:|
| 1 | Solutions Manual + review | 1 | 1 |
| 2 | Interview System + review | 1–2 | 2–3 |
| 3 | Hedging Playbook + review | 1 | 3–4 |
| 4 | Case Study Library + review | 1 | 4–5 |
| 5 | Trade Break Library + review | 1 | 5–6 |

**Total estimated: 5–6 sessions.**

---

## Risk Register

| Risk | Impact | Mitigation |
|------|--------|------------|
| Solutions Manual scenarios too generic | Reduces unique educational value | Ground every scenario in specific Atlas DNA fields and Matrix dimensions |
| Interview answer templates too similar across products | Reader fatigue, wasted effort | Differentiate tiers aggressively. 30-sec must differ from 2-min |
| Hedging content duplicates §15 | Duplication bloat | Per-product cards: reference §15, add ONLY hedge strategy + failure mode + residual |
| Case studies rely on knowledge beyond training data cutoff | Factual risk | Ground all claims in product mechanics (which are verifiable), not market data |
| Trade break cases too hypothetical | Low operational credibility | Structure around specific system behaviors documented in §16/§17/§2.8 |
| Context window limits on large artifact generation | Truncation risk | Generate in parts if needed. Each part self-contained |

---

## Quality Gates

Each artifact passes through:

1. **Generation** — produce artifact following structure above
2. **Self-Review** — verify against checklist in review section above
3. **Cross-Reference Check** — verify all Atlas/Matrix/chapter references resolve correctly
4. **User Approval** — present for review before marking complete

---

## Decision Required

**This plan recommends building 5 artifacts in the order above.**

Awaiting approval to begin Phase 1 (Solutions Manual).

Options:
- **Approve all 5** — execute in order
- **Approve subset** — specify which artifacts to build
- **Modify order** — resequence as needed
- **Modify scope** — adjust structure of specific artifacts
- **Reject** — provide alternative direction

---

*Execution plan complete. 2026-06-22.*
