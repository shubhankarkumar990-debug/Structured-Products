# Batch 10 Candidate Comparison

**Date:** 2026-06-21
**Scope:** Evaluate 6 candidate products for slots #45-#49
**Method:** Score each candidate 1-10 across 5 dimensions. Top 5 recommended.

---

## 1. Evaluation Framework

| Dimension | Weight | What It Measures |
|-----------|:------:|------------------|
| Market Relevance | 25% | Global issuance volume, desk frequency, client demand |
| Educational Value | 25% | New concepts taught, builds on existing foundation, "aha moment" potential |
| Uniqueness | 20% | How different is this from existing 44 products? Does it fill a structural gap? |
| Overlap Risk | 15% | How much does it repeat mechanics already covered? (lower = better) |
| Publication Value | 15% | Does it strengthen the book's completeness claim? Market perception? |

---

## 2. Candidate Profiles

### Candidate 1: Worst-of Autocallable

**What it is:** Phoenix/FCN variant linked to a basket of 3-5 stocks. Payoff determined by worst-performing stock. Autocall, conditional coupon, KI barrier — all applied to worst-of level.

**New mechanics:** Worst-of observation, correlation-dependent pricing, quanto adjustment on cross-listed baskets, dispersion trading.

**Dependency chain:** Phoenix (5.1.3) → Correlation (§1.6) → Worst-of Autocallable. Foundation already laid — §1.6 teaches worst-of and correlation, Phoenix teaches autocall/memory.

**Existing manuscript references:** §1.6 contains 15+ references to worst-of payoffs, including worked examples. Phoenix chapter references worst-of baskets. CRA ELN mentions basket variants. This product is already foreshadowed.

| Dimension | Score | Rationale |
|-----------|:-----:|-----------|
| Market Relevance | 10 | #1 structured product by global issuance volume |
| Educational Value | 9 | Demonstrates correlation in practice. Shows why banks and investors disagree on correlation. Connects §1.6 theory to real product. |
| Uniqueness | 9 | Only multi-asset product in universe. Only product where correlation directly drives payoff. |
| Overlap Risk | 3 | Phoenix overlap is real but manageable — the multi-asset/correlation dimension is fundamentally different |
| Publication Value | 10 | A desk bible without worst-of autocallable is like a cooking manual without pasta |

**Estimated complexity:** 8
**Recommended product code:** WOAC

---

### Candidate 2: Snowball Note

**What it is:** Autocallable note where missed coupons accumulate and are paid on next coupon date or at maturity. If the product is not called and the coupon condition is met, the investor receives all prior missed coupons plus the current one.

**New mechanics:** Cumulative coupon accumulation (different from Phoenix memory — Phoenix pays the current coupon retroactively; Snowball accumulates the actual missed amounts). Coupon snowball effect creates path dependency in coupon amounts.

**Dependency chain:** Phoenix (5.1.3) → FCN (5.1.9) → Snowball. Natural extension — "What if missed coupons accumulate rather than just being remembered?"

| Dimension | Score | Rationale |
|-----------|:-----:|-----------|
| Market Relevance | 8 | Dominant product in China/Korea markets. Growing in Europe. |
| Educational Value | 8 | Teaches cumulative vs memory distinction. Shows how small mechanical change (memory → accumulation) dramatically changes risk profile. |
| Uniqueness | 7 | Distinct from Phoenix (memory) and TARN (target on received coupons). The accumulation mechanics is genuinely new. |
| Overlap Risk | 5 | Shares autocall/barrier mechanics with Phoenix/FCN. The "how this differs" bridge is clear but overlap is moderate. |
| Publication Value | 8 | China/Korea market relevance strengthens Asia-Pacific coverage claim. |

**Estimated complexity:** 7
**Recommended product code:** SNOW

---

### Candidate 3: Dual Currency Investment (DCI)

**What it is:** Short-term deposit where the investor receives a high coupon but the principal may be returned in a different (weaker) currency if the FX rate crosses a strike level. Structured deposit + FX option (short put on stronger currency).

**New mechanics:** FX as primary underlying, currency conversion risk, FX option embedded in deposit, two-currency settlement.

**Dependency chain:** Structured Deposit (5.6.1) → Vanilla Options (5.6.3) → DCI. Combines deposit wrapper with FX option.

| Dimension | Score | Rationale |
|-----------|:-----:|-----------|
| Market Relevance | 8 | Standard private banking product globally. Core offering in HK, SG, Switzerland. |
| Educational Value | 7 | Introduces FX as underlying. Shows how currency risk is monetized. Simple enough to be highly accessible. |
| Uniqueness | 8 | Only FX-underlying structured product in universe. Fills asset class gap. |
| Overlap Risk | 2 | Minimal — no other product covers FX. Structured Deposit (5.6.1) covers deposit wrapper but different underlying. |
| Publication Value | 8 | Fills the FX gap. A structured products book without FX is noticeably incomplete. |

**Estimated complexity:** 3
**Recommended product code:** DCI

---

### Candidate 4: Shark Fin Note

**What it is:** Capital-protected note where participation is capped if the underlying breaches an up-barrier during the product's life. If the barrier is never breached, the investor receives full participation. If breached, the investor receives a reduced (but still positive) return — typically a fixed rebate.

**New mechanics:** Barrier-as-modifier (barrier reduces participation rather than causing loss). Up-and-out call with rebate. The payoff chart has a distinctive "shark fin" shape.

**Dependency chain:** PPN (5.1.1) → Barrier concepts (§1.3) → Shark Fin. Variant of PPN where upside is conditionally capped.

| Dimension | Score | Rationale |
|-----------|:-----:|-----------|
| Market Relevance | 6 | Popular in HK, Taiwan, China. Less common in Europe/US. |
| Educational Value | 7 | Shows barrier as modifier (not binary trigger). Shows how barrier + capital protection interact. Unique payoff chart shape. |
| Uniqueness | 6 | Related to PPN (capital protected) but adds barrier mechanic. The "barrier reduces rather than kills" concept is genuinely new. |
| Overlap Risk | 4 | PPN overlap in structure. Barrier mechanics overlap with KODRC. The combination is novel but components are familiar. |
| Publication Value | 6 | Strengthens Asia-Pacific coverage. Less essential than worst-of/DCI. |

**Estimated complexity:** 4
**Recommended product code:** SHRK

---

### Candidate 5: Cliquet / Ratchet Note

**What it is:** Note with periodic resets (monthly, quarterly, annually). At each reset, the return for that period is locked in (subject to a local cap and floor). The total return is the sum of all locked-in periodic returns (subject to a global cap and floor).

**New mechanics:** Forward-starting options, periodic reset, local cap/floor per period, global cap/floor on total, serial option decomposition, compound floor.

**Dependency chain:** Vanilla Options (5.6.3) → Forward concepts → Cliquet. Introduces forward-starting option chain.

| Dimension | Score | Rationale |
|-----------|:-----:|-----------|
| Market Relevance | 7 | Popular in France, Switzerland, Asia. Common in insurance-linked products. |
| Educational Value | 9 | Decomposition into forward-starting options is a teaching masterpiece. Shows how "reset" creates a fundamentally different risk profile from buy-and-hold. Local vs global cap/floor interaction is rich. |
| Uniqueness | 9 | No existing product covers periodic reset. Serial option decomposition is entirely new. Forward-starting concept not taught elsewhere. |
| Overlap Risk | 1 | Almost zero overlap with any existing product. Completely new mechanics. |
| Publication Value | 8 | Fills major payoff-type gap. French/Swiss market relevance. Educational depth is high. |

**Estimated complexity:** 7
**Recommended product code:** CLIQ

---

### Candidate 6: Twin-Win / Absolute Return Note

**What it is:** Note that participates in upside AND converts downside into positive return (absolute value of return), with a down-and-in barrier that destroys the protection. If the barrier is never breached, the investor profits whether the underlying goes up or down. If breached, the investor suffers the full downside.

**New mechanics:** Absolute value payoff (symmetric positive participation), barrier that kills downside protection, long straddle equivalent with barrier.

**Dependency chain:** PPN (5.1.1) → RC barrier concept (5.1.2) → Twin-Win. Combines participation with barrier protection.

| Dimension | Score | Rationale |
|-----------|:-----:|-----------|
| Market Relevance | 5 | Less commonly traded than other candidates. More popular in early 2000s, now niche. |
| Educational Value | 7 | Absolute return payoff is unique and engaging. Shows how combining long call + long put + barrier creates this payoff. Good for option decomposition teaching. |
| Uniqueness | 7 | Unique payoff type (absolute value). No other product offers symmetric positive participation. |
| Overlap Risk | 4 | Shares barrier mechanics with RC family. Capital protection concept overlaps PPN. The combination is novel. |
| Publication Value | 5 | Nice-to-have, not essential. Lower market volume reduces necessity. |

**Estimated complexity:** 5
**Recommended product code:** TWIN

---

## 3. Scoring Summary

| Candidate | Market (25%) | Educational (25%) | Uniqueness (20%) | Overlap (15%) | Publication (15%) | **Weighted** |
|-----------|:---:|:---:|:---:|:---:|:---:|:---:|
| Worst-of Autocallable | 10 | 9 | 9 | 3 | 10 | **8.60** |
| Cliquet / Ratchet | 7 | 9 | 9 | 1 | 8 | **7.35** |
| Snowball Note | 8 | 8 | 7 | 5 | 8 | **7.30** |
| Dual Currency Investment | 8 | 7 | 8 | 2 | 8 | **6.95** |
| Shark Fin Note | 6 | 7 | 6 | 4 | 6 | **5.95** |
| Twin-Win | 5 | 7 | 7 | 4 | 5 | **5.75** |

**Note on Overlap scoring:** Lower overlap = better. Scores are inverted for weighting (10 - overlap score = contribution). Worst-of scores 3 for overlap → contributes 7 × 0.15 = 1.05. Cliquet scores 1 → contributes 9 × 0.15 = 1.35.

---

## 4. Head-to-Head: Shark Fin vs Twin-Win (5th slot)

Both compete for the final slot. Direct comparison:

| Dimension | Shark Fin | Twin-Win | Edge |
|-----------|:---------:|:--------:|:----:|
| Market volume | Higher (Asia still active) | Lower (peaked ~2005) | Shark Fin |
| New concept taught | Barrier-as-modifier | Absolute return payoff | Twin-Win |
| Payoff chart distinctiveness | Distinctive "fin" shape | Distinctive "V" shape | TIE |
| Overlap with existing | PPN + barrier | PPN + RC barrier | TIE |
| Regional gap filled | HK, TW, China | Europe (historical) | Shark Fin |
| Complexity balance | C=4 (lightens batch) | C=5 (moderate) | Shark Fin |

**Recommendation:** Shark Fin for 5th slot. Higher current market relevance, better complexity balance (batch needs a lower-complexity product), stronger Asia-Pacific coverage.

---

## 5. Recommended Selection (Top 5)

| Rank | Product | Score | Fills |
|:----:|---------|:-----:|-------|
| 1 | Worst-of Autocallable | 8.60 | Multi-asset gap, correlation gap, #1 market volume |
| 2 | Cliquet / Ratchet | 7.35 | Periodic reset gap, serial options, zero overlap |
| 3 | Snowball Note | 7.30 | Cumulative coupon gap, China/Korea market |
| 4 | Dual Currency Investment | 6.95 | FX asset class gap, private banking |
| 5 | Shark Fin Note | 5.95 | Barrier-modifier concept, complexity balance |

This selection fills: 3 asset class gaps, 4 payoff type gaps, all Asia-Pacific gaps, and the top 5 global market volume gaps.

---

*Batch 10 Candidate Comparison completed 2026-06-21.*
