# CLN Family Pre-Generation Design Review

**Date:** 2026-06-20
**Scope:** 4 remaining CLN products (Batch 8)
**Framework:** v1.3.1 (FROZEN)
**Purpose:** Design review before generation

---

## 1. Dependency Chain Assessment

### 1.1 Prerequisites Already Taught

| Prerequisite | Location | Status | Coverage Quality |
|-------------|----------|:------:|:----------------:|
| Credit spread | Section 1.9 | TAUGHT | Strong — defined with examples, basis points explained |
| Recovery rate | Section 1.9 | TAUGHT | Strong — 3 tiers (senior secured, unsecured, subordinated) with ranges |
| Credit events | Section 1.9 | TAUGHT | Strong — 3 types (bankruptcy, failure to pay, restructuring) with ISDA |
| CDS mechanics | Section 1.9 + CDS chapter (5.2.5) | TAUGHT | Very Strong — full chapter with worked examples, settlement types |
| Vanilla CLN | Section 5.5.1 | TAUGHT | Strong — 3-party structure, coupon decomposition, dual credit exposure |
| Correlation | Section 1.6 | TAUGHT | Strong — but equity-focused (worst-of baskets), not credit correlation |
| ISDA standards | Section 1.9 + CDS (5.2.5) | TAUGHT | Strong — standardization role explained |
| Protection buyer/seller | CDS (5.2.5) | TAUGHT | Strong — clearly defined with flow diagrams |

### 1.2 Prerequisites NOT Yet Taught

| Concept | Needed For | Gap Severity | Recommendation |
|---------|-----------|:------------:|---------------|
| Portfolio credit default modeling | FTD, NTD, Synthetic CDO | HIGH | Must teach in FTD chapter (§7 or §11) — first encounter |
| Basket credit default | FTD, NTD | HIGH | Must teach in FTD as bridge from equity baskets (1.6) to credit baskets |
| Tranche mechanics | Synthetic CDO | HIGH | Must teach in Synthetic CDO chapter — entirely new concept |
| Attachment/detachment points | Synthetic CDO | HIGH | Must teach in Synthetic CDO chapter |
| Credit correlation (vs equity correlation) | FTD, NTD, Synthetic CDO | MEDIUM | 1.6 covers equity correlation. Must bridge to credit correlation in FTD |
| Default correlation | FTD, NTD, Synthetic CDO | HIGH | Must teach: why defaults cluster, contagion, industry exposure |
| Copula models | Synthetic CDO | MEDIUM | Brief mention — pricing dependency. Not full derivation |

### 1.3 Dependency Verdict

**Prerequisites mostly satisfied.** CDS and Vanilla CLN provide strong foundation. Three gaps require careful in-chapter teaching:

1. **Credit correlation** — bridge from Section 1.6 equity correlation to credit correlation in FTD chapter
2. **Basket credit defaults** — new concept, must build from Vanilla CLN single-name to multi-name
3. **Tranching** — entirely new, must teach from scratch in Synthetic CDO

**Risk level: MANAGEABLE.** Each gap can be addressed within its chapter using §7 Construction and §11 Formal Definition without exceeding word limits (except possibly Synthetic CDO — see Section 3).

---

## 2. Educational Risk Assessment

### 2.1 Concepts Most Likely to Confuse Readers

| Rank | Concept | Confusion Risk | Why It's Hard | Mitigation |
|:----:|---------|:--------------:|--------------|-----------|
| 1 | **Correlation effect reversal (NTD vs FTD)** | VERY HIGH | FTD = short correlation (profit from low default correlation). NTD reverses at certain thresholds — non-intuitive | Use Phoenix short-correlation parallel. Build 3-scenario table: high/medium/low correlation → FTD loss probability vs NTD loss probability |
| 2 | **Tranche attachment/detachment** | VERY HIGH | Abstract concept with no prior analog. "Equity tranche absorbs 0-3% losses" is meaningless without visualization | Use layered building analogy. Show ASCII waterfall with loss filling from bottom. Worked example with specific numbers |
| 3 | **Default waterfall mechanics** | HIGH | Sequential loss allocation across tranches is multi-step logic | Step-by-step waterfall with numbered defaults. "Default 1 hits equity. Default 2 hits equity. Default 3 starts hitting mezzanine." |
| 4 | **Skew CLN modified recovery** | MEDIUM | Subtle modification to Vanilla CLN. Readers may not see why it matters | Contrast tables: standard recovery vs modified. Show P&L impact with exact numbers |
| 5 | **FTD: first default triggers on entire basket** | MEDIUM | "You lose money when any ONE of five companies defaults" seems unfair | Analogy: insurance on five houses — one fire means you pay. Higher premium because more things can go wrong |
| 6 | **NTD: protection only triggers on Nth default** | MEDIUM | "I'm safe until the 2nd/3rd default" is counter-intuitive for readers trained on FTD | Build sequentially from FTD. "FTD = insurance pays on 1st claim. 2TD = insurance pays on 2nd claim." |
| 7 | **Copula/model dependency in CDO** | MEDIUM | Gaussian copula critique (2008 GFC). Model risk is abstract | Reference Section 1.9 model risk. Concrete example: "the model said losses above 3% were impossible. They happened." |

### 2.2 Pedagogical Risk Summary

| Product | Overall Educational Risk | Primary Challenge |
|---------|:------------------------:|------------------|
| Skew CLN | LOW | Recovery modification is straightforward variant |
| FTD | MEDIUM-HIGH | First multi-name credit product. Must bridge equity correlation to credit correlation |
| NTD | HIGH | Correlation reversal effect. Must build on FTD without repeating |
| Synthetic CDO | VERY HIGH | Entirely new framework (tranching). Highest-complexity product in universe. 2008 GFC stigma to address honestly |

---

## 3. Complexity Calibration

### 3.1 Recommended Scores

| Product | Recommended Score | Rationale |
|---------|:-----------------:|-----------|
| **Skew CLN** | **5** | Vanilla CLN (4) + modified recovery mechanism adds one dimension. Single reference entity. No basket. No new conceptual framework. Comparable to CRC (5) — adds one structural variant to a simpler base |
| **FTD** | **7** | Single-name CLN (4) + basket mechanics + credit correlation + first-default trigger. Multiple interacting factors. Comparable to Digital KI Put (7) and CRA SRT (7) — multi-factor products with non-obvious risk profiles |
| **NTD** | **8** | FTD (7) + correlation reversal + Nth-default threshold adds complexity. Non-monotonic correlation sensitivity is harder than any single-factor. Comparable to TARN STEG (8) — path-dependent with non-obvious behavior |
| **Synthetic CDO** | **10** | NTD (8) + tranching + attachment/detachment + portfolio-level modeling + copula dependency + 2008 GFC context. Most complex product in universe. No comparable product. Framework note: "PPN=2, Synthetic CDO=10" (framework §S.1) |

### 3.2 Calibration Against Existing Registry

```
Score   Product                 Family    Reasoning
──────  ──────────────────────  ────────  ─────────────────────────────
  2     PPN                     ELN       Bond + call option
  2     VLSP                    Swap      Simplest swap structure
  3     RC                      ELN       Bond + short put
  4     Vanilla CLN             CLN       Bond + short CDS
  5     Skew CLN [PROPOSED]     CLN       CLN + modified recovery ←
  5     CRC                     ELN       RC + call right
  5     Vanilla STEG            STEG      CMS spread exposure
  6     Phoenix                 ELN       Autocall + memory + barriers
  6     Callable STEG           STEG      STEG + call right
  7     FTD [PROPOSED]          CLN       Multi-name credit + correlation ←
  7     Digital KI Put          ELN       Triple barrier interaction
  7     RA STEG                 STEG      CMS spread range accrual
  8     NTD [PROPOSED]          CLN       FTD + correlation reversal ←
  8     TARN STEG               STEG      Path-dependent target accumulation
 10     Synthetic CDO [PROPOSED] CLN      Tranched portfolio credit ←
```

**Alignment: GOOD.** Scores follow consistent logic:
- Skew CLN (5) slots alongside other "base + one variant" products
- FTD (7) slots alongside other multi-factor products
- NTD (8) slots alongside other non-obvious-behavior products
- Synthetic CDO (10) anchors the top — framework explicitly designates this

### 3.3 CLN Family Progression

```
4 → 5 → 7 → 8 → 10
Vanilla → Skew → FTD → NTD → Synthetic CDO
```

**Gap check:** 4→5 (+1), 5→7 (+2), 7→8 (+1), 8→10 (+2). The 5→7 and 8→10 jumps are large. Justified:
- 5→7: FTD introduces basket + correlation — genuinely two new dimensions
- 8→10: Synthetic CDO introduces tranching + portfolio modeling — genuinely two new frameworks

---

## 4. Visual Requirements

### 4.1 Skew CLN — Mandatory Visuals (6)

| # | Visual | Type | Priority | Template Source |
|:-:|--------|------|:--------:|----------------|
| 1 | **Recovery comparison** — Standard CLN vs Skew CLN payout at different recovery rates | Payoff Diagram | P1 | Adapt from Vanilla CLN payoff |
| 2 | **3-party structure** — Investor → Bank → Reference Entity with skewed recovery path | Cash Flow Diagram | P1 | Reuse CLN 3-party template |
| 3 | **Coupon decomposition waterfall** — How modified recovery changes pricing | Waterfall Diagram | P2 | Adapt from CLN construction waterfall |
| 4 | **Scenario comparison** — No default / Default with standard recovery / Default with skewed recovery | Comparison Chart | P2 | New variant |
| 5 | **Lifecycle timeline** — Pre-trade → Settlement with recovery modification path | Lifecycle Diagram | P3 | Reuse lifecycle template |
| 6 | **Decision tree** — Credit event? → Recovery assessment → Standard or modified payout | Decision Tree | P3 | Adapt from CDS decision tree |

### 4.2 FTD — Mandatory Visuals (6)

| # | Visual | Type | Priority | Template Source |
|:-:|--------|------|:--------:|----------------|
| 1 | **Basket default visualization** — 5 reference entities, first default highlighted, loss triggered | Portfolio Loss Diagram | P1 | **NEW template** — basket default |
| 2 | **Correlation impact** — Low/medium/high correlation → probability of first default | Correlation Illustration | P1 | **NEW template** — credit correlation |
| 3 | **FTD cash flow** — Investor → Bank, premium in / loss out on first default | Cash Flow Diagram | P2 | Adapt from CLN 3-party |
| 4 | **FTD vs Vanilla CLN comparison** — Single-name vs basket economics | Comparison Chart | P2 | Adapt from family comparison |
| 5 | **Lifecycle timeline** — Basket monitoring → first default event → settlement | Lifecycle Diagram | P3 | Reuse lifecycle template |
| 6 | **Default sequence** — Which company defaults first? 5 entities on timeline, first trigger | Timeline | P3 | **NEW template** — default sequence |

### 4.3 NTD — Mandatory Visuals (6)

| # | Visual | Type | Priority | Template Source |
|:-:|--------|------|:--------:|----------------|
| 1 | **Nth-default trigger** — 5 entities, N-1 defaults absorbed, Nth triggers loss | Portfolio Loss Diagram | P1 | Adapt from FTD basket template |
| 2 | **Correlation reversal** — FTD vs 2TD vs 3TD correlation sensitivity curves | Correlation Illustration | P1 | Adapt from FTD correlation template |
| 3 | **FTD vs NTD comparison** — Risk profile, premium, correlation sensitivity | Comparison Chart | P2 | Adapt from family comparison |
| 4 | **Default sequence with threshold** — Timeline showing defaults 1, 2, ... N with trigger point | Timeline | P2 | Adapt from FTD default sequence |
| 5 | **Lifecycle timeline** — Basket monitoring → Nth default → settlement | Lifecycle Diagram | P3 | Reuse lifecycle template |
| 6 | **Premium vs N** — How coupon decreases as N increases (1st=highest, 5th=lowest) | Payoff Diagram | P3 | New variant |

### 4.4 Synthetic CDO Tranche — Mandatory Visuals (6)

| # | Visual | Type | Priority | Template Source |
|:-:|--------|------|:--------:|----------------|
| 1 | **Tranche waterfall** — Portfolio losses flowing through equity → mezzanine → senior tranches | Waterfall Diagram | P1 | **NEW template** — tranche waterfall |
| 2 | **Attachment/detachment diagram** — Bands: 0-3% equity, 3-7% mezz, 7-15% senior, 15-100% super senior | Tranche Diagram | P1 | **NEW template** — tranche bands |
| 3 | **Portfolio loss distribution** — Bell curve of portfolio losses with tranche bands overlaid | Portfolio Loss Diagram | P2 | **NEW template** — loss distribution |
| 4 | **Correlation impact on tranches** — How correlation affects equity vs senior tranche values | Correlation Illustration | P2 | Adapt from FTD/NTD correlation |
| 5 | **Cash flow structure** — 100+ name portfolio → SPV → tranche investors | Cash Flow Diagram | P3 | **NEW template** — CDO structure |
| 6 | **Worked example timeline** — Defaults 1-5, losses filling tranches sequentially | Timeline | P3 | Adapt from default sequence |

### 4.5 New Visual Templates Required

| Template | First Use | Reuse Potential |
|----------|-----------|:---------------:|
| Basket default | FTD | NTD, Synthetic CDO |
| Credit correlation | FTD | NTD, Synthetic CDO |
| Default sequence timeline | FTD | NTD |
| Tranche waterfall | Synthetic CDO | Unique (no other tranched product) |
| Tranche bands | Synthetic CDO | Unique |
| Portfolio loss distribution | Synthetic CDO | Unique |
| CDO structure flow | Synthetic CDO | Unique |

**7 new templates.** 3 reusable across CLN family. 4 unique to Synthetic CDO.

### 4.6 Visual Asset Count

| Product | Visuals | New Templates | Reused Templates |
|---------|:-------:|:-------------:|:----------------:|
| Skew CLN | 6 | 0 | 6 (all from existing) |
| FTD | 6 | 3 | 3 |
| NTD | 6 | 0 | 6 (adapted from FTD) |
| Synthetic CDO | 6 | 4 | 2 |
| **Total** | **24** | **7** | **17** |

Post-Batch 8 registry: 69 + 24 = **93 visual assets.**
Template registry: 41 + 7 = **48 visual templates.**

---

## 5. Teaching Sequence

### 5.1 Current Generation Order (from product_generation_order.md)

```
#34 Skew CLN → #35 FTD → #36 NTD → #37 Synthetic CDO
```

### 5.2 Assessment

| Transition | Pedagogical Logic | Verdict |
|-----------|------------------|:-------:|
| Vanilla CLN → Skew CLN | Single-name stays single-name. One variable changes (recovery). Minimal new concepts. | OPTIMAL |
| Skew CLN → FTD | Single-name → multi-name. Introduces basket + correlation. Largest conceptual jump in CLN family. | OPTIMAL — this is the right place for the jump |
| FTD → NTD | First-to-default → Nth-to-default. Same framework, different trigger point. Correlation reversal builds on FTD. | OPTIMAL |
| NTD → Synthetic CDO | Multi-name basket → tranched portfolio. Introduces attachment/detachment, portfolio modeling. | OPTIMAL — NTD is the natural bridge |

### 5.3 Verdict

**Current order is OPTIMAL. No change recommended.**

Logic: each product adds exactly one major conceptual layer:
1. Skew CLN: modified recovery (one variable change)
2. FTD: multi-name basket + credit correlation (new framework)
3. NTD: Nth-default threshold + correlation reversal (extends FTD)
4. Synthetic CDO: tranching + portfolio modeling (new framework)

Reordering would create dependency violations. Synthetic CDO cannot precede NTD. NTD cannot precede FTD. FTD should not precede Skew CLN (readers need one more single-name CLN before multi-name).

---

## 6. O.3 Compliance Checklist

Framework §O.3 mandates three elements for every CLN chapter:

| O.3 Requirement | Skew CLN | FTD | NTD | Synthetic CDO |
|-----------------|:--------:|:---:|:---:|:-------------:|
| Credit event walkthrough | §10 scenarios | §10 scenarios | §10 scenarios | §10 scenarios |
| Default waterfall | §7 construction | §11 formal def | §11 formal def | §12 construction + §11 |
| Recovery mechanics | §11 formal def (modified recovery) | §11 (basket recovery) | §11 (Nth-default recovery) | §11 (tranche loss allocation) |

All three requirements are addressable within standard v1.3.1 template sections. No framework modification needed.

---

## 7. Analogy Recommendations

### 7.1 Available Domain Space

**Used domains to avoid:** bail bondsman (Vanilla CLN), earthquake insurance (RC), weather insurance (Variance Swap), home insurance (Digital Cap-Floor), casino (reserved), insurance (multiple uses).

**Insurance domain is heavily used.** CLN products must differentiate clearly.

### 7.2 Proposed Analogies

| Product | Proposed Analogy | Domain | Collision Check |
|---------|-----------------|--------|:--------------:|
| Skew CLN | **Car insurance with deductible tiers** — standard policy pays full claim, skew policy pays based on damage severity | Automotive insurance | CLEAR — "car rental" used by CCY Swap, but different subdomain |
| FTD | **Domino chain** — five dominoes standing, first one to fall triggers the alarm | Chain reaction | CLEAR — no domino/chain domain used |
| NTD | **Fire alarm system** — alarm doesn't sound until Nth sensor trips, so isolated smoke doesn't trigger evacuation | Safety systems | CLEAR — no alarm/sensor domain used |
| Synthetic CDO | **Highrise building in a flood zone** — ground floor floods first (equity tranche), middle floors next (mezzanine), penthouse last (senior) | Building/flood | CLEAR — no building/flood domain used |

All 4 domains unique. No collisions with 33 existing or 25 reserved domains.

---

## 8. Strengths

1. **Strong prerequisite coverage.** CDS (5.2.5) and Vanilla CLN (5.5.1) provide excellent foundation. 61 credit event mentions already in manuscript. Recovery rates taught with 3 tiers.
2. **Equity correlation bridge exists.** Section 1.6 teaches correlation concept with baskets. FTD chapter only needs to bridge to credit correlation — concept is not new.
3. **Clear generation order.** Each product adds exactly one layer. No dependency violations possible.
4. **O.3 requirements are lightweight.** Three mandatory elements all fit within standard v1.3.1 sections.
5. **Visual templates 70% reusable.** 17 of 24 visuals adapt existing templates. Only 7 new templates needed.
6. **Analogy space is clear.** No domain collisions detected.

---

## 9. Risks

| Risk | Severity | Mitigation |
|------|:--------:|-----------|
| **Synthetic CDO word count** | HIGH | Framework notes this product "may exceed 3,500-word limit." Pre-approve exception to 6,000 words if needed. Tranching, waterfall, and 2008 context require space. |
| **Correlation reversal in NTD** | HIGH | Use FTD as contrast base. 3-column table: low/med/high correlation → FTD risk vs NTD risk. Visual comparison is essential. |
| **2008 GFC context in Synthetic CDO** | MEDIUM | Must acknowledge honestly without editorial opinion. Stick to mechanics: "models assumed low correlation → actual defaults were highly correlated → losses exceeded model predictions." Framework rule: facts only. |
| **Credit correlation is abstract** | MEDIUM | Bridge from 1.6 equity correlation analogy (orchestra). "Just as stock prices can move together, defaults can cluster — when one bank fails, its suppliers and partners face stress." |
| **FTD coupon justification** | MEDIUM | Readers may wonder why FTD pays less than sum of individual CDS. Must explain: "you only lose on first default, not all five — the risk is lower than five separate CLNs." |
| **Booking system continuity** | LOW | CLN uses NEMO+Sophis (same as ELN and Vanilla CLN). No system switch. |

---

## 10. Teaching Recommendations

### 10.1 Chapter-Level

| Product | Key Teaching Moves |
|---------|-------------------|
| **Skew CLN** | Lead with "What if recovery isn't always 40%?" → Show investment-grade vs distressed recovery differences → Contrast P&L under standard vs modified recovery |
| **FTD** | Bridge from 1.6: "In Section 1.6 you learned correlation for stock baskets. Now apply the same idea to default baskets." → Build 5-company basket → Show "first domino" trigger → Explain why FTD coupon > single-name CLN but < sum of 5 CLNs |
| **NTD** | Open with FTD contrast: "FTD alarm sounds on first default. What if it takes two?" → Build N threshold → Introduce correlation reversal as the key insight → Table comparing 1TD through 5TD |
| **Synthetic CDO** | Teach tranching from scratch using building/flood analogy → Explain attachment/detachment with exact numbers → Walk through 5-default waterfall step by step → Address 2008 context in §6 Product Evolution → Model risk in §15 |

### 10.2 Family-Level

1. **Family transition text** (between §5.4 STEG and §5.5 CLN) already exists. Verify it introduces the single-name → basket → portfolio progression.
2. **Cross-references:** Every chapter must reference CDS (5.2.5) for credit event definitions per cross-family consistency review advisory A1.
3. **Knowledge Check progression:** Skew CLN = recovery comparison. FTD = "which company defaults first?" basket analysis. NTD = correlation reversal explanation. Synthetic CDO = tranche loss allocation walkthrough.

### 10.3 Word Count Guidance

| Product | Target | Hard Limit | Risk of Exceeding |
|---------|:------:|:----------:|:------------------:|
| Skew CLN | 3,500-5,000 | 5,500 | LOW — simple variant |
| FTD | 3,500-5,000 | 5,500 | MEDIUM — basket introduction needs space |
| NTD | 3,500-5,000 | 5,500 | LOW — builds on FTD, less new content |
| Synthetic CDO | 4,500-5,500 | 6,500* | HIGH — tranching + 2008 context + portfolio modeling |

*Exception pre-approved per framework note: "Synthetic CDO Tranche (#37) is the most complex product in the universe. It may exceed the 3,500-word limit."

---

## 11. Visual Recommendations Summary

- **24 total visuals** (6 per product, 2P1+2P2+2P3 each)
- **7 new templates** needed (3 reusable within CLN, 4 unique to Synthetic CDO)
- **17 visuals** adapt existing templates
- **Key new visual types:** basket default, credit correlation, tranche waterfall, tranche bands, portfolio loss distribution
- **Tranche waterfall is the most important new visual in Batch 8.** It will be the primary teaching tool for the hardest concept (attachment/detachment).

---

## 12. GO / NO-GO Decision

### **GO for Batch 8 generation.**

| Criterion | Status |
|-----------|:------:|
| Prerequisites taught | YES (3 gaps addressable in-chapter) |
| Educational risks identified | YES (7 risks, all have mitigations) |
| Complexity scores calibrated | YES (5, 7, 8, 10 — aligned with registry) |
| Visual requirements defined | YES (24 visuals, 7 new templates) |
| Teaching sequence validated | YES (current order is optimal) |
| O.3 compliance plan | YES (all 3 requirements mappable) |
| Analogy domains clear | YES (4 unique domains, 0 collisions) |
| Word count risks identified | YES (Synthetic CDO exception pre-approved) |
| Framework frozen | YES (no modifications needed) |

### Pre-Generation Checklist

- [ ] Verify Section 1.6 → credit correlation bridge language in FTD
- [ ] Prepare Synthetic CDO word count exception (Final Editor Agent approval)
- [ ] Confirm CDS (5.2.5) cross-reference requirement for all 4 chapters
- [ ] Verify 4 analogy domains against full registry at generation time
- [ ] Generate in order: #34 Skew CLN → #35 FTD → #36 NTD → #37 Synthetic CDO

### Advisory Notes

- A1: Synthetic CDO may need 6,000-6,500 words. Framework note pre-approves this exception.
- A2: NTD correlation reversal is the single hardest concept in Batch 8. Visual comparison against FTD is critical.
- A3: 2008 GFC discussion in Synthetic CDO §6 must be factual, not editorial. Stick to mechanics.

---

*CLN Family Pre-Generation Design Review completed 2026-06-20. No framework or chapter modifications made.*
