# Solutions Manual Enhancement Review

**Date:** 2026-06-22
**Purpose:** Assess 4 proposed enhancements before generation.
**Input:** Prior design reviews, Atlas, Matrix, §7/§14/§15 per chapter.

---

## Workstream 1: Product Rejection Framework

### 1.1 Assessment

The existing scenario template already includes:
- Candidate Set (Step 8)
- Comparative Selection (Step 9)
- Complexity Ladder (ascending consideration)

What's MISSING: explicit documentation of WHY rejected products were eliminated and AT WHICH STEP.

### 1.2 Educational Value

**HIGH.** Rejection reasoning is where structurer expertise lives. Knowing why NOT to use a product is harder than knowing when to use it. New joiners default to the "obvious" product — the rejection framework forces them to articulate why an alternative is better.

### 1.3 Implementation Design

Add a mandatory "Rejected Alternatives" block to each scenario:

```
**Rejected Alternatives:**

| Product | Eliminated At | Reason |
|---------|:------------:|--------|
| Phoenix (6) | Step 7 (Complexity) | Client capped at Complexity 4 |
| WOAC (8) | Step 5 (Risk Budget) | Worst-of multiplies downside beyond budget |
| PPN (2) | Step 2 (Cash Flow) | No coupon — client needs income |
```

Rules:
- Show top 3 rejections per scenario (not exhaustive)
- Focus on non-obvious rejections (Phoenix rejected for complexity is obvious; PPN rejected for income need is less so)
- Every rejection must cite a specific decision step

### 1.4 Impact on Scenario Length

~3 lines per scenario × 40 scenarios = ~120 additional lines. Acceptable.

### 1.5 Recommendation

**ACCEPT.** Add as mandatory subsection within each scenario.

Rationale: Rejection reasoning IS the decision. Without it, scenarios are recommendations without justification. The "Why Not" subsection transforms each scenario from a lookup into a teaching moment.

---

## Workstream 2: Client Persona Layer

### 2.1 Existing Persona Data

Matrix Part 3 "Typical Buyer" column already classifies all 49 products:

| Buyer Category | Count | Products |
|---------------|:-----:|---------|
| Retail | 4 | SD, Warrant, WOAC, Digital |
| Retail / PB | 6 | PPN, Bonus, Booster, ELO, Digital, WOAC |
| Private Banking | 5 | DCI, SHRK, SNOW, CLIQ, Opt-on-RC |
| Institutional | 16 | All Swaps, all SRT, all STEG, CDO, FWD, VO |
| Sophisticated | 3 | ACCUM, DECUM, Opt-on-RC |
| Credit Investors | 4 | CLN, Skew CLN, FTD, NTD |
| Various | 11 | RC, DRC, KODRC, CRC, Phoenix, FCN, CRA ELN, ICN, DKIP, EqSwap, TRS |

### 2.2 Proposed 8 Personas — Analysis

| Persona | Distinct Recommendation? | Unique Constraints |
|---------|:------------------------:|-------------------|
| Retail | YES | PRIIPS/KID required, max complexity ~4, suitability rules |
| HNI | MERGE with PB | Same products, similar sophistication |
| Private Banking | YES | Complexity up to 7-8, less regulatory than retail |
| Corporate Treasury | YES | Hedging focus only, no yield enhancement |
| Asset Manager | PARTIAL | Similar to PB but larger notional, more swap focus |
| Insurance | YES | ALM driven, regulatory capital, liability matching |
| Pension Fund | MERGE with Insurance | Similar mandates, same product set |
| Hedge Fund | YES | No complexity cap, leverage acceptable, vol trading |

### 2.3 Personas That Materially Change Recommendations

Only 4 distinct personas produce genuinely different product selections:

| Persona | What Changes | Example |
|---------|-------------|---------|
| **Retail** | Complexity cap ~4. No swaps. Suitability required | Cannot use Phoenix (6) or VarSwap (7) |
| **Private Banking / HNI** | Complexity up to 8. All note products. Some swaps | Full ELN universe + exotic notes |
| **Institutional (Insurance/Pension/AM)** | ALM focus. Swaps, SRT, STEG. Limited ELN interest | Prefer IRS, STEG, CLN over RC, Phoenix |
| **Hedge Fund / Sophisticated** | No limits. Leverage OK. Vol trading. Full universe | VarSwap, ACCUM, CDO accessible |

The remaining 4 proposed personas (HNI, Corporate Treasury, Asset Manager, Pension Fund) collapse into these 4:
- HNI → Private Banking
- Corporate Treasury → Institutional (hedging subset)
- Asset Manager → Institutional or PB depending on mandate
- Pension Fund → Institutional

### 2.4 Where Persona Filtering Belongs

**After Step 3 (Asset Class Selection), before Step 4 (Market Regime).**

Persona determines:
- Which products are ELIGIBLE (regulatory/suitability)
- Maximum complexity band
- Swap vs note preference

It does NOT determine:
- Market view (that's client-specific, not persona-specific)
- Risk budget (within persona, this varies)
- Liquidity needs (varies)

### 2.5 Implementation Design

Insert as **Step 3.5** in the 9-step framework:

```
Step 3: ASSET CLASS SELECTION
Step 3.5: PERSONA FILTER
          → Retail: cap Complexity 4, notes only
          → Private Banking: cap Complexity 8, notes + select swaps
          → Institutional: full swap universe, SRT/STEG priority
          → Sophisticated: no cap, leverage products available
Step 4: MARKET REGIME ASSESSMENT
```

Do NOT create separate scenario tracks per persona. Instead, add a one-line **Persona Note** to each scenario:

```
**Persona Note:** Retail-eligible up to Scenario 3.2 (Digital, Complexity 4). 
Scenarios 3.3+ require Private Banking or Institutional.
```

### 2.6 Impact

~1 line per scenario + 15-line persona definition in Part 1 = ~55 additional lines.

### 2.7 Recommendation

**ACCEPT** with simplification. 4 personas, not 8. Implemented as Step 3.5 filter + per-scenario one-line note. No separate scenario tracks.

Rationale: Persona materially changes product eligibility. Retail cannot access 70% of the universe. Ignoring this makes scenarios unrealistic. But 8 personas is overkill — 4 cover the distinct regulatory/complexity boundaries.

---

## Workstream 3: Desk Economics Layer

### 3.1 Existing Content

§7 "How the Bank Makes Money" per product provides:
- Structuring fee (embedded margin)
- Bid-offer spread
- Hedging P&L (realized vs implied vol)
- Funding benefit

§14 "Desk Reality" provides:
- Day-to-day operational considerations
- What each role deals with

§15 "Risk Analysis" provides:
- Risk factors with severity ratings

### 3.2 What Desk Economics Would Add

| Dimension | What It Teaches | Who Needs It |
|-----------|----------------|-------------|
| **Profitability ranking** | Which products earn most for the desk | Structurers, sales |
| **Hedgeability** | How easy/hard to hedge → affects pricing | Traders, risk |
| **Operational complexity** | Booking/lifecycle burden → affects feasibility | Ops, product control |
| **Liquidity cost** | Secondary market cost → affects exit terms | Sales, structurers |
| **Capital consumption** | RWA/leverage ratio impact → affects pricing | Treasury, risk |

### 3.3 Educational Value Assessment

| For Structurers | HIGH — profitability determines what gets built |
|----------------|------|
| For Traders | MEDIUM — they already know hedgeability |
| For Operations | LOW — ops cares about process, not economics |
| For Interview Prep | HIGH — "why does the bank make this product?" is a common question |

### 3.4 Risk of Overcomplication

**MEDIUM.** Adding 5 desk dimensions to every scenario doubles scenario complexity. Readers seeking "which product for my client" don't need to know capital consumption.

### 3.5 Implementation Design

**Part 1 only, NOT per-scenario.** Add a compact desk economics section to the framework:

```
1.5 The Desk Economics Lens

When two products meet client needs equally, the desk prefers:
1. Higher margin (structuring fee + bid-offer)
2. Easier to hedge (liquid underliers, standard Greeks)
3. Lower operational burden (fewer observations, simpler lifecycle)
4. Lower capital consumption (simpler RWA calculation)

This is why structurers recommend:
- RC over PPN for yield clients (RC margin 2-3× PPN margin)
- Phoenix over FCN for autocall clients (Phoenix hedge more liquid)
- Index-linked over single-stock (lower idiosyncratic vol, easier hedge)
```

Then add ONE desk economics note per scenario ONLY when desk preference overrides neutral selection:

```
**Desk Note:** Bank prefers RC (higher margin) over Bonus (harder to hedge barrier).
```

### 3.6 Impact

~40 lines for Part 1 section + ~10 scenario-level notes = ~50 additional lines.

### 3.7 Recommendation

**ACCEPT** with scope limitation. One Part 1 section explaining the lens. Per-scenario desk notes only when desk economics is a material tiebreaker (estimated 10 of 40 scenarios).

Rationale: Desk economics IS part of structuring decisions in reality. Omitting it entirely creates an unrealistic model. But embedding it in every scenario overwhelms the client-need focus. Compromise: teach the lens once, apply selectively.

---

## Workstream 4: Product Replacement Logic

### 4.1 Concept

"If Product X is unavailable, what is the nearest substitute?"

Unavailability reasons:
- Complexity too high for client
- Product not on approved list
- Market conditions make it unattractive
- Liquidity insufficient
- Underlier not available in that format

### 4.2 Replacement Mapping Architecture

Replacements should be grouped by **OBJECTIVE** (why the client wanted it) not by product family, because the best substitute may be in a different family.

| Primary Product | Objective | Substitute 1 | Substitute 2 | Trade-Off |
|----------------|-----------|:------------:|:------------:|-----------|
| PPN (2) | Protection + equity upside | SD (2) | Airbag (4) | SD: simpler, lower participation. Airbag: better terms, conditional |
| RC (3) | Yield enhancement | DRC (3) | Digital (4) | DRC: discount instead of coupon. Digital: binary but capital protected |
| Phoenix (6) | Conditional income + autocall | FCN (6) | CRC (5) | FCN: guaranteed coupon. CRC: callable instead of autocallable |
| CLN (4) | Funded credit exposure | CDS (5) | Skew CLN (5) | CDS: unfunded, ISDA needed. Skew: non-linear but same structure |
| IRS (3) | Rate hedging | VLSP (2) | FWD (2) | VLSP: simpler. FWD: single-period only |
| VarSwap (7) | Pure vol exposure | VO (3) | Opt-on-RC (5) | VO: asymmetric, capped loss. Opt-on-RC: indirect vol |
| WOAC (8) | Multi-stock basket yield | Phoenix (6) | SNOW (7) | Phoenix: single underlier. SNOW: cumulative coupon |
| CDO (10) | Tranched credit | NTD (8) | FTD (7) | NTD/FTD: smaller basket, simpler than CDO |
| Vanilla STEG (5) | Curve steepening income | Callable STEG (6) | IR Callable (5) | Callable: better coupon, call risk. IR Callable: rate-linked, no spread |
| ACCUM (6) | Discounted share accumulation | FWD (2) | EqSwap (5) | FWD: no gearing. EqSwap: synthetic ownership |

### 4.3 Full Replacement Matrix Scope

| Family | Products | Replacements Needed |
|--------|:--------:|:-------------------:|
| ELN | 15 | 15 (each product → 2 substitutes) |
| Swaps | 8 | 8 |
| SRT | 5 | 5 |
| STEG | 4 | 4 |
| CLN | 5 | 5 |
| Other | 12 | 12 |
| **Total** | **49** | **49 rows × 2 substitutes = 98 mappings** |

### 4.4 Complexity-Respecting Replacements

**Rule:** At least one substitute must be LOWER complexity than the primary product.

| Primary | Complexity | Sub 1 | Sub 1 Complexity | Sub 2 | Sub 2 Complexity |
|---------|:----------:|-------|:----------------:|-------|:----------------:|
| Phoenix (6) | 6 | CRC (5) ↓ | 5 | FCN (6) = | 6 |
| WOAC (8) | 8 | Phoenix (6) ↓ | 6 | SNOW (7) ↓ | 7 |
| CDO (10) | 10 | NTD (8) ↓ | 8 | FTD (7) ↓ | 7 |

**Exception:** T1 products (Complexity 2) have no lower substitute. Their substitutes are lateral (same complexity, different family).

### 4.5 Where This Belongs

**Part 4 (Quick Reference)** — as a 49-row replacement lookup table. NOT embedded in scenarios (scenarios already have the Complexity Ladder which serves a similar purpose for the specific objective).

### 4.6 Impact

~80 lines for the 49-row table + 10 lines for rules.

### 4.7 Recommendation

**ACCEPT** — place in Part 4 (Quick Reference).

Rationale: High practical value. Desks regularly need substitutes when products are unavailable. Compact table format. No scenario bloat. The replacement table is the "emergency exit" when the recommended product can't be used.

---

## Final Assessment Matrix

| Enhancement | Ed. Value | Dup. Risk | Complexity | Lines Added | Recommendation |
|-------------|:---------:|:---------:|:----------:|:-----------:|:--------------:|
| Product Rejection Framework | High | None | Low | ~120 | **ACCEPT** |
| Client Persona Layer | High | Low (Matrix buyer exists) | Medium | ~55 | **ACCEPT** (4 personas, not 8) |
| Desk Economics Layer | Medium-High | Medium (§7 exists per product) | Low | ~50 | **ACCEPT** (Part 1 only + selective notes) |
| Product Replacement Logic | High | None | Low | ~90 | **ACCEPT** (Part 4 table) |

---

## Updated Artifact Specification

### Revised Structure

| Part | Title | Original Est. | Enhancement | Revised Est. |
|:----:|-------|:------------:|:-----------:|:------------:|
| 1 | Structurer Decision Framework | 250–350 | +Step 3.5 Persona Filter, +§1.5 Desk Economics | 320–420 |
| 2 | Scenario Library | 700–850 | +Rejection block + Persona note + Desk note per scenario | 850–1,000 |
| 3 | Anti-Patterns | 150–200 | No change | 150–200 |
| 4 | Quick Reference | 80–100 | +49-row Replacement Table | 170–200 |
| | **Total** | **1,180–1,500** | **+315 lines** | **1,490–1,820** |

### Revised Per-Scenario Template

```
### Scenario X.Y: [Title]

**Client says:** "[Quote expressing need]"

**Persona Note:** [Retail / PB / Institutional / Sophisticated — eligibility impact]

**Step 1-7 Narrowing:**
[Show which steps eliminate which products, including Step 3.5 persona filter]

**Candidate Set:** [3-8 products]

**Rejected Alternatives:**
| Product | Eliminated At | Reason |
|---------|:------------:|--------|
[Top 3 non-obvious rejections]

**Comparative Selection:**
| Dimension | Product A | Product B | Product C |
|-----------|-----------|-----------|-----------|

**Recommendation:** [Product] — [Why this over alternatives]

**Complexity Ladder:** [Lower-complexity option considered first]

**Market Regime Note:** [When this recommendation changes]

**Desk Note:** [Only if desk economics is a material tiebreaker]
```

---

## Revised Readiness Verdict

All 4 enhancements ACCEPTED. Updated specification:
- 10-step decision model (9 original + Step 3.5 Persona Filter)
- 4 personas (from 8 proposed)
- Desk economics in Part 1 + selective scenario notes
- 49-row replacement table in Part 4
- Per-scenario: rejection block (mandatory), persona note (mandatory), desk note (selective)

# GO

Solutions Manual generation authorized with all 4 enhancements incorporated.

---

*Enhancement review complete. 2026-06-22.*
