# Pass B Editorial Harmonization Plan — Phase 5

**Date:** 2026-06-22
**Pass:** A.5 → B (Pending Approval)
**Status:** PLAN ONLY — no manuscript modifications until approved
**Scope:** All 49 chapters — editorial content changes
**Prerequisite:** Pass A (structural) COMPLETE

---

## Executive Summary

Pass A achieved 100% structural compliance across all 49 chapters. Pass B addresses **educational consistency** — the gap between structural uniformity and pedagogical uniformity. Five workstreams, prioritised by impact.

**Estimated effort:** ~16 chapters need material expansion, ~33 chapters need light editorial polish, all 49 need terminology normalisation.

---

## Workstream 1: Critical Section Expansion (Priority: URGENT)

### Scope
16 chapters scoring below 6.0 (Tier C/D) in the educational composite audit.

### 1A. Tier D — Critical Expansion (2 chapters)

| Chapter | Score | Primary Deficiencies | Target |
|---------|:-----:|---------------------|:------:|
| 5.4.3 Callable Steepener | 4.5 | §1 (91w), §2 (84w), §14 (57w) | 6.0+ |
| 5.4.2 RA Steepener | 4.7 | §1 (110w), §2 (84w), §14 (71w) | 6.0+ |

**Actions for each:**
- Expand §1 to 180+ words — add story-first opening with character scenario
- Expand §2 to 140+ words — extend analogy with explicit domain mapping
- Expand §14 to 120+ words — add desk perspective (trader morning routine, risk monitoring)
- Expand §10 to 140+ words — add 3 numbered scenarios (bull/bear/base)

### 1B. Tier C — Targeted Expansion (14 chapters)

| Chapter | Score | Primary Gap |
|---------|:-----:|------------|
| 5.3.2 ZCL | 5.1 | §1 (109w), §2 (91w) |
| 5.3.4 CRA SRT | 5.2 | §1 (111w), §2 (88w) |
| 5.3.5 Digital Cap-Floor | 5.4 | §2 (68w — thinnest) |
| 5.6.4 ELO | 5.5 | §10 (37w — critical outlier) |
| 5.3.3 NCRA | 5.5 | §2 (80w) |
| 5.4.1 Vanilla STEG | 5.7 | §14 (72w), §10 (104w) |
| 5.2.3 Equity Swap | 5.7 | §14 (65w) |
| 5.2.8 Vanilla Swap | 5.9 | §14 (66w), §2 (115w) |
| 5.3.1 IR Callable SRT | 5.9-6.0 | §2 (97w) |
| 5.2.4 Variance Swap | 6.0 | §14 (78w) |
| 5.2.2 TRS | 6.0 | §14 (102w) borderline |
| 5.2.7 Commodity Swap | 6.1 | §14 (90w) |
| 5.4.4 TARN STEG | 6.0 | §14 (81w) |
| 5.5.2 Skew CLN | 6.0 | §10 (110w), §19 (201w) |

**Actions — minimum expansion per section:**
- §1 below 150 words → expand to 170+ with story opening or "Imagine" lead
- §2 below 120 words → expand to 140+ with extended analogy
- §10 below 100 words → expand to 130+ with numbered scenarios
- §14 below 90 words → expand to 120+ with desk-practitioner perspective

### 1C. ELO §10 Emergency Fix

5.6.4 ELO has §10 = 37 words — the only section in the entire manuscript more than 70% below average. This gets its own sub-action:
- Expand from 37 to 130+ words
- Add 3 named scenarios: (1) ELO exercised profitably, (2) ELO expires worthless, (3) ELO near-the-money at expiry
- Add market condition context for each scenario

---

## Workstream 2: Story-First Openings (Priority: HIGH)

### Scope
29 chapters (59%) that open §1 with definitions rather than scenarios.

### Target
All 49 chapters should open §1 with a character-driven or "imagine you" scenario before transitioning to the product description. The 20 chapters that already use story-first openings are not modified.

### Approach
- Do NOT rewrite existing content — **prepend** a 2-3 sentence opening scenario
- Use the "conversational professor" voice profile (Profile A from Phase 1)
- Each opening should name a character or use "you" and describe a specific financial situation

### Chapters Needing Story-First Openings (29)

**Batch 1 (5):** DRC, KODRC, CRC, Airbag, Bonus
**Batch 2 (5):** FCN, CRA ELN, ICN, Digital Coupon, Booster
**Batch 3 (2):** DKIP, Warrant *(these are already strong — light touch only)*
**Batch 4 (4):** TRS, Equity Swap, Variance Swap, CDS
**Batch 5 (3):** Cross-Currency, Commodity, Vanilla Swap
**Batch 6 (5):** IR Callable, ZCL, NCRA, CRA SRT, Digital CF
**Batch 7 (4):** Vanilla STEG, RA STEG, Callable STEG, TARN STEG
**Batch 9 (1):** ELO

### Template

```
[Character name] [role] at [institution] faces [specific financial problem].
[2-sentence setup of the situation]. [Product name] offers [solution in plain language].
```

---

## Workstream 3: Bridge Text (Priority: HIGH)

### Scope
35 chapters missing "How This Differs From [Family Anchor]" opening context.

### What Bridge Text Does
Each non-anchor chapter should open with a 2-3 sentence paragraph explaining how it differs from the family's anchor product. This helps readers who arrive at a variant chapter understand its relationship to the base product.

### Family Anchors

| Family | Anchor Chapter | Anchor Product |
|--------|---------------|---------------|
| ELN (5.1.x) | 5.1.1 | Principal Protected Note (PPN) |
| Swaps (5.2.x) | 5.2.1 | Interest Rate Swap (IRS) |
| SRT (5.3.x) | 5.3.1 | IR Callable Fixed Rate Swap |
| STEG (5.4.x) | 5.4.1 | Vanilla Steepener Note |
| CLN (5.5.x) | 5.5.1 | Vanilla Credit-Linked Note |
| Other (5.6.x) | 5.6.1 | Structured Deposit |

### Chapters Needing Bridge Text (35)

- 14 chapters already have bridge text (no action needed)
- 6 anchor chapters don't need bridge text (they are the reference point)
- **29 non-anchor chapters** + some that have partial bridge text need review

### Insertion Point
Bridge text goes immediately after the `---` separator following the chapter title, before `#### §1.`. Format:

```markdown
> **How this differs from [Anchor Product]:** [2-3 sentences explaining the key structural
> difference, the additional risk or feature, and when a client would choose this variant
> over the anchor product.]
```

---

## Workstream 4: Terminology Normalisation (Priority: MEDIUM)

### Scope
All 49 chapters — find-and-replace plus first-use expansion.

### 4A. Standardise Terminology Variants

| Standard Form | Variants to Replace | Est. Occurrences |
|--------------|-------------------|:----------------:|
| mark-to-market | MTM, MtM, mark to market | ~15 |
| knock-in | knock in, KI | ~8 |
| knock-out | knock out, KO | ~6 |
| autocall | auto-call, automatic call | ~4 |
| day-count | daycount, day count | ~3 |
| counterparty | counter-party | ~2 |
| fixed-rate (adj.) | fixed rate (before noun) | ~5 |

**Method:** Automated find-replace with manual review of each replacement context.

### 4B. First-Use Acronym Expansion

Add expansion on first use per chapter for these terms:

| Term | Expansion | Chapters Affected |
|------|-----------|:-----------------:|
| NEMO | [Internal Booking System] | 12+ |
| FTP | Funds Transfer Pricing | 8+ |
| IPV | Independent Price Verification | 6+ |
| DV01 | Dollar Value of One Basis Point | 5+ |
| CS01 | Credit Spread Sensitivity (1bp) | 3 |
| PFE | Potential Future Exposure | 2 |
| MTM | Mark-to-Market | all chapters using abbreviation |
| OTC | Over-the-Counter | inconsistent chapters |
| ISDA | International Swaps and Derivatives Association | non-credit chapters |
| CSA | Credit Support Annex | non-swap chapters |

### 4C. Formula Notation Alignment

Two options (requires decision):

| Option | Description | Pros | Cons |
|--------|-----------|------|------|
| A: Keep both | Notation-heavy for Batches 0-8, prose-heavy for 9-10 | No rework | Inconsistent |
| B: Standardise to notation | Convert prose formulas to `$...$` notation | Consistent | Large rework for 12 chapters |
| **C: Standardise to prose** | Convert notation to "Payout = Notional × ..." | **Accessible** | Large rework for 37 chapters |

**Recommendation:** Option A (keep both) for Pass B. Formula style does not affect comprehension and rework cost is disproportionate. Revisit for publication build if needed.

---

## Workstream 5: Voice Harmonisation (Priority: LOW)

### Scope
All 49 chapters — align toward "conversational professor" voice profile.

### Target Voice Profile
- Direct address: minimum 8 "you" per chapter (currently 3-15 range)
- Questions: minimum 10 per chapter (currently 5-30 range)
- Socratic markers: at least 2 "think about", "notice that", "consider" per chapter
- Plain language markers: at least 1 "in other words", "put simply" per chapter in §1-§2

### Actions
1. **Low-"you" chapters (Batches 4-5, 8):** Add 3-5 direct-address instances per chapter in §1, §10, §18
2. **Low-question chapters:** Add 2-3 rhetorical questions in §1 and §10
3. **No action on high-"you" chapters** — do not reduce existing conversational style

### Constraint
Voice changes must not alter technical meaning. Every added sentence must be educationally substantive, not filler.

---

## Execution Order

| Phase | Workstream | Chapters | Est. Effort | Dependency |
|:-----:|-----------|:--------:|:-----------:|-----------|
| B.1 | WS1A: Tier D expansion | 2 | High | None |
| B.2 | WS1C: ELO §10 emergency | 1 | Low | None |
| B.3 | WS1B: Tier C expansion | 14 | High | None |
| B.4 | WS3: Bridge text | 29 | Medium | None |
| B.5 | WS2: Story-first openings | 29 | Medium | After WS1 (avoid double-editing) |
| B.6 | WS4A+B: Terminology | 49 | Medium | After all content changes |
| B.7 | WS5: Voice harmonisation | ~15 | Low | After all content changes |
| B.8 | WS4C: Formula notation | DEFERRED | — | Decision needed |

**Phases B.1, B.2, B.3 can run in parallel.**
**Phase B.6 must run AFTER B.1-B.5** (terminology normalisation should apply to final content, not pre-expansion content).

---

## Acceptance Criteria

| Criterion | Target | Measurement |
|-----------|:------:|------------|
| No chapter below 5.5 composite | 0 chapters | Re-run scoring after expansion |
| Batch average delta | <1.5 points | Max − min batch average |
| Story-first openings | 49/49 | §1 first sentence check |
| Bridge text coverage | 43/49 | All non-anchor chapters |
| Terminology variants | 0 | Automated regex scan |
| Acronym first-use expansion | 100% | Per-chapter first-occurrence check |
| Voice profile compliance | 8+ "you" per chapter | Automated count |

---

## Risk Mitigation

| Risk | Mitigation |
|------|-----------|
| Expansion changes product accuracy | All new content reviewed against §11 (Formal Definition) for consistency |
| Bridge text creates contradictions | Each bridge text verified against both anchor and variant chapter content |
| Terminology replacement breaks formulas | Regex excludes content within `$...$` notation blocks |
| Voice changes feel artificial | Limit to 3-5 additions per chapter; never rewrite existing prose |
| Scope creep into framework changes | Framework v1.3.1 remains FROZEN — Pass B = content within existing sections only |

---

## Stop Conditions

1. **Do not** modify framework structure (v1.3.1 frozen)
2. **Do not** add new sections beyond §1-§22
3. **Do not** rewrite existing content that scores above 6.0 — expand only
4. **Do not** begin publication build (deferred per project plan)
5. **STOP after Pass B and re-run educational composite audit** before proceeding

---

*Phase 5 Pass B Editorial Harmonization Plan completed 2026-06-22. PLAN ONLY — awaiting approval to execute.*
