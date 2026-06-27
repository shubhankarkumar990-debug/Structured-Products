# Pedagogical Coverage Audit — Phase 3

**Date:** 2026-06-22
**Pass:** A.5 (Pre-Editorial Audit)
**Status:** READ-ONLY — no manuscript modifications
**Scope:** All 49 chapters

---

## 1. Worked Examples (§18)

### Coverage

| Metric | Value |
|--------|:-----:|
| Chapters with worked examples | 49/49 (100%) |
| Chapters with numerical examples | 49/49 (100%) |
| Chapters with step-by-step format | 25/49 (51%) |
| Avg worked example length | 183 words |

### Word Count Distribution

| Tier | Word Range | Count | Chapters |
|------|:---------:|:-----:|---------|
| Deep (300+) | 308–448 | 5 | DCI, Phoenix, WOAC, Snowball, CDO |
| Standard (150–300) | 150–296 | 22 | Most Batches 2-10 |
| Thin (100–150) | 100–148 | 18 | Most Batches 0-1, some Batch 6-7 |
| Minimal (<100) | 99 | 4 | DRC, RC variants |

### Step-by-Step Format

**25 chapters use explicit step format** ("Step 1:", "First:", numbered calculations). These tend to be:
- Batches 3, 7, 9-10 chapters
- More complex products (Phoenix, CDO, Accumulator, Cliquet)

**24 chapters use narrative/table format** — present calculations but without explicit step enumeration. These tend to be:
- Batches 0-2, 4-6 chapters
- Simpler products

### Assessment
Worked examples are universally present and numerical. The variance in depth (99–448 words, 4.5× range) is partly justified by product complexity but partly reflects inconsistent depth expectations. Pass B should establish a minimum word count target.

---

## 2. Knowledge Checks (§19)

### Coverage

| Metric | Value |
|--------|:-----:|
| Chapters with knowledge checks | 49/49 (100%) |
| Avg question count | 9.8 |
| Avg section word count | 275 words |

### Question Count Distribution

| Tier | Questions | Count | Chapters |
|------|:---------:|:-----:|---------|
| Deep (12+) | 12–14 | 8 | Pilot batch (5), 5.1.3, 5.1.4, 5.1.5 |
| Standard (9–11) | 9–11 | 18 | Most Batches 1-7 |
| Moderate (7–8) | 7–8 | 18 | CLN family, Other family |
| Minimal (5–6) | 5–6 | 5 | 5.5.2, 5.5.3, 5.5.4, 5.5.5, 5.6.4 |

### Three Distinct Knowledge Check Formats

**Format A — "Interview-style" (Batches 0-3):**
- 10-14 numbered questions
- Mix of conceptual and calculation questions
- "Interview Questions" header (now renamed to Knowledge Check)
- Includes Mental Models + Key Takeaways subsections (folded in from Pass A)
- Longest format (~300-380 words)

**Format B — "Desk Questions" (Batches 6-7):**
- 9-10 numbered questions
- Three tiers: Conceptual, Scenario, Desk
- Structured with explicit difficulty progression
- Mental Models + Key Takeaways folded in
- ~260-330 words

**Format C — "Compact Assessment" (Batches 8-10):**
- 7-9 questions
- Embedded within shorter section
- No explicit difficulty tiers
- No Mental Models/Key Takeaways subsections
- ~180-260 words

### Assessment
All chapters have knowledge checks. The three formats reflect framework evolution. Format B (Batches 6-7) has the best pedagogical structure with explicit difficulty progression.

---

## 3. Scenario Coverage (§10)

### Coverage

| Metric | Value |
|--------|:-----:|
| Chapters with scenario analysis | 49/49 (100%) |
| Chapters with numbered scenarios | 36/49 (73%) |
| Avg §10 word count | 153 words |

### Scenario Depth

| Tier | Word Count | Count | Pattern |
|------|:---------:|:-----:|---------|
| Deep (200+) | 200–287 | 10 | Phoenix, DKIP, CLN, CDS, CDO |
| Standard (120–200) | 120–199 | 24 | Most Batches 0-7 |
| Thin (80–120) | 80–119 | 10 | Some Other family, STEG variants |
| Minimal (<80) | 37–79 | 5 | ELO (37!), Shark Fin, Snowball, Cliquet, Forward |

**5 chapters have notably thin scenario coverage:**
1. **5.6.4 ELO — 37 words** — By far the thinnest. Needs expansion.
2. 5.6.9 Shark Fin — 93 words
3. 5.6.10 Snowball — 128 words (borderline acceptable)
4. 5.6.2 Forward — 100 words
5. 5.6.3 Vanilla Options — 93 words

### Assessment
Scenario sections in Batches 0-8 are consistently detailed with 3-4 named scenarios. Batches 9-10 have shorter scenarios — this is partly because their §9 (Three Scenarios) section provides a summary table, with §10 expanding on market dynamics rather than repeating scenario enumeration. ELO (5.6.4) is an outlier needing attention.

---

## 4. Desk-Perspective Coverage (§14)

### Coverage

| Metric | Value |
|--------|:-----:|
| Chapters with desk reality/payoff logic | 49/49 (100%) |
| Avg §14 word count | 136 words |

### Depth Distribution

| Tier | Word Count | Count | Pattern |
|------|:---------:|:-----:|---------|
| Deep (200+) | 205–259 | 6 | Cliquet, WOAC, Snowball, Shark Fin, CDO, Accumulator |
| Standard (100–200) | 100–199 | 25 | Most Batches 0-8 |
| Thin (60–100) | 60–99 | 14 | Some ELN, most Swaps |
| Minimal (<60) | 57 | 4 | Callable STEG (57), Equity Swap (65), VLSP (66), RA STEG (71) |

### Two Content Models

**Model A — "Payoff Logic" (Batches 0-5):**
- Formula-driven payoff decomposition
- Mathematical notation with boundary conditions
- Focused on product-specific formulas
- 60-140 words typical

**Model B — "Desk Reality" (Batches 6-10):**
- Day-in-the-life practitioner perspective
- Trading desk workflow and priorities
- Risk management in practice
- 100-260 words typical

### Assessment
Batch 9-10 chapters have the deepest desk reality coverage, reflecting the v1.3.1 template's emphasis on practitioner perspective. Earlier batches focused on payoff formulas (valid but different intent). The weakest are some Batch 4-5 swap chapters (Equity Swap, VLSP) where desk reality is thin.

---

## 5. Interview-Question Quality (§19)

### Difficulty Progression

| Level | Batches 0-5 | Batches 6-7 | Batches 8-10 |
|-------|:-----------:|:-----------:|:------------:|
| Conceptual | Mixed in | Explicitly labelled | Mixed in |
| Calculation | Present | Present | Present |
| Scenario/Application | Some | Explicitly labelled | Some |
| Desk/Practitioner | Rare | Explicitly labelled | Some |

**Batch 6-7 chapters have the best question structure** — they explicitly separate questions into "Conceptual", "Scenario", and "Desk" tiers. This is a best practice that other batches should adopt.

### Question Types

| Type | Count | Example |
|------|:-----:|---------|
| "What is/What does" (recall) | ~120 | "What is the key risk of a reverse convertible?" |
| "How would you" (application) | ~80 | "How would you hedge a short gamma position near barrier?" |
| "Explain why" (understanding) | ~60 | "Explain why correlation increases FTD risk" |
| "Walk through" (desk scenario) | ~40 | "Walk through your first-morning priorities" |
| Calculation | ~50 | "Calculate the coupon given…" |

### Assessment
All chapters have substantive knowledge checks. Batch 6-7's tiered format is the gold standard. Batch 8-10 chapters have fewer but more focused questions. Pass B should consider adding difficulty labels to all chapters.

---

## 6. Phase 3 Summary

| Dimension | Coverage | Consistency | Key Gap |
|-----------|:--------:|:-----------:|---------|
| Worked Examples | 100% | 5/10 | 4.5× word count range |
| Knowledge Checks | 100% | 5/10 | Three distinct formats |
| Scenario Coverage | 100% | 5/10 | ELO at 37 words (outlier) |
| Desk Perspective | 100% | 5/10 | Two content models coexist |
| Question Quality | 100% | 6/10 | Difficulty labels only in Batch 6-7 |

**Overall Pedagogical Coverage: 7/10 (coverage) × 5/10 (consistency) = adequate but uneven**

All 49 chapters cover all required pedagogical elements. The inconsistency is in depth and format, not in presence or absence.

---

## 7. Post-Pass B Update (2026-06-22)

### ELO §10 Resolution (Critical Outlier)

The ELO §10 outlier (37 words — "Identical to Vanilla Options") was replaced with 4 genuine scenarios (337 words):
1. **Bull case** — stock rises, client profits, illustrates leverage vs stock
2. **Bear case** — expires worthless, contrasts with stock holder's recovery option
3. **Theta decay** — stock up but ELO loses money (premium exceeds intrinsic), catches retail clients off guard
4. **Vol spike** — ELO value rises but client cannot monetise (no secondary market), illustrates key difference from institutional options

ELO §10 score: 0.9 → 8.4. No longer an outlier.

### Updated Consistency Scores

| Dimension | Pre-Pass B | Post-Pass B | Change |
|-----------|:----------:|:-----------:|:------:|
| Scenario Coverage | 5/10 | 6/10 | +1 (ELO fixed) |
| All other dimensions | unchanged | unchanged | — |

**Post-Pass B Pedagogical Coverage: 7/10 (coverage) × 6/10 (consistency) = adequate and improving**

---

*Updated 2026-06-22 after Pass B editorial harmonization.*
