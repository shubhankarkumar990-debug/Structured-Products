# V1.0.1 — Verification Review (for Shubh to sign off)

**Date:** 2026-06-27
**Purpose:** Let you confirm the substance of the 19 edits before relying on them — especially the one load-bearing decision: adopting the **MTM convention** as the canonical correlation label.

---

## PART 1 — The decision you actually need to verify

Every correlation edit (15 of the 19) rests on a single choice:

> **An investor who profits when correlation *rises* is labeled "long correlation" — even though they structurally *sold* the correlation premium.**

This is the **MTM (mark-to-market sensitivity) convention**. There is a competing convention, and the original V1.0 text used *both inconsistently* — which is what created the self-contradictions in the first place.

### The two conventions

| | **MTM convention (what I applied)** | **Structural convention (the alternative)** |
|---|---|---|
| Label is based on | Which way your P&L moves when ρ moves | What you did at inception (bought/sold correlation) |
| FTD / worst-of investor | **Long** correlation (helped by rising ρ) | **Short** correlation (sold the premium) |
| "Short correlation" means | Hurt by rising ρ | Sold/short the correlation premium |
| Used by | Most trading/risk desks describing live Greeks; matches "long vega = helped by rising vol" | Some structuring desks describing the inception trade |

### Strongest case FOR my choice (MTM canonical)
1. **Internal consistency.** The V1.0 text's *economic explanations* were already MTM ("they profit when correlation is high"). Only the labels were structural. Choosing MTM aligns label to explanation everywhere with minimal rewriting.
2. **Greek-consistency.** It makes correlation behave like every other Greek in the book: "long X = helped when X rises" (long vega, long gamma). A student who internalizes one rule applies it everywhere.
3. **It's the errata package's own framework.** `correlation_convention_framework_final.md` already declared MTM canonical; I applied that decision rather than inventing one.
4. **The risk tables already encode MTM.** The NTD risk-vs-ρ table (lines 17927–17932) defines direction by how risk moves with ρ. MTM labels match that table; structural labels contradict it.

### Strongest case AGAINST (where this could bite you)
1. **Some interviewers say the opposite.** A structuring desk that asks "are worst-of investors long or short correlation?" may *expect* "short" (structural). If your target desk teaches structural-primary, my labels are backwards for that room.
2. **"Sold the premium" intuition is real.** The structural view captures a true fact (you did sell correlation), and some practitioners lead with it.
3. **I preserved both, but led with MTM.** Every edit keeps the structural nuance in a clause ("*structurally* short — sold the premium"), but the headline label is now MTM. If you want structural as the headline, the labels flip and the clauses swap.

### My recommendation
Keep MTM canonical. Confidence: **high on consistency, moderate on house-style fit.** It's the only choice that makes the labels, the economic explanations, and the risk tables all agree simultaneously — the structural convention would force you to rewrite the risk tables too.

### What would change my mind
- You tell me the specific desk/interview you're prepping for teaches structural-primary. → I flip the headline labels (≈ same 15 locations, mechanical) and keep MTM in the clause.
- You're using this for a credit-correlation/CDO audience specifically, where "short correlation = short the tranche" structural language dominates. → Worth a hybrid: structural-primary in the credit chapters, MTM elsewhere, explicitly flagged.

**If you're studying broadly (not one desk's house style), MTM is the safe default and you can sign off.**

---

## PART 2 — Every edit, before → after

### A. Correlation-label flips (depend on Part 1)

**E-01a · Desk_Bible §1 ELI5 (line 17352)**
- Before: "FTD investors are **short** credit correlation, just as worst-of equity investors are short equity correlation."
- After: "FTD investors are **long** credit correlation — they benefit when default correlation is high … The investor is *structurally* short … but the economic sensitivity is long."

**E-01b · Desk_Bible §11 key insight (17524)**
- Before: "FTD investors are **short** correlation. They profit when correlation is high…" *(self-contradiction)*
- After: "FTD investors are **long** correlation (MTM convention). They profit when correlation is high… the investor *structurally sold* the first-default premium."

**E-02 · Desk_Bible worst-of parallel (17526)**
- Before: "worst-of investors are also **short** correlation — they profit when stocks move together." *(self-contradiction)*
- After: "worst-of investors are also **long** correlation (MTM convention) … structurally sold the correlation premium."

**E-01c · Desk_Bible NTD table, FTD row (17951)**
- Before: `| FTD (N=1) | 9.5% | Highest | Short correlation (unambiguous) |`
- After: `| FTD (N=1) | 9.5% | Highest | Long correlation (MTM: risk falls as ρ rises) |`

**E-09 · Desk_Bible NTD table, rows 2TD–5TD (17952–17955)**
- Before: 2TD "Short at low ρ, reversal at high ρ"; 3TD "Reversal at moderate ρ"; 4TD "Long correlation (approximately)"; 5TD "Long correlation (unambiguous)"
- After: all four relabeled **Short correlation** with the mechanism (high ρ → defaults cluster → higher NTD risk). *Note: 4TD/5TD changed direction entirely (were "long").*

**E-08 · interview_system_v2_2 (356)**
- Before: "The investor is **SHORT** correlation: they benefit from high correlation…" *(self-contradiction)*
- After: "The investor is **long** correlation (MTM convention) … *structurally* short — they sold the correlation premium." *(line 358 desk-raw Greek "short correlation" deliberately kept.)*

**E-10 · Desk_Bible §4.8 cross-family table (2282) — linter-found**
- Before: `| **Short correlation** (profit from high correlation) | Worst-of Phoenix, worst-of FCN, FTD |` *(self-contradiction)*
- After: `| **Long correlation** (profit from high correlation; MTM convention) | … |`

**E-11 · Desk_Bible Phoenix takeaway (3544) — linter-found**
- Before: "…making them **short** correlation products — lower correlation between stocks increases risk." *(self-contradiction)*
- After: "…making the investor **long** correlation (MTM convention) — lower correlation increases risk. (Structurally sold the premium.)"

**E-12 · interview_system_v2_2 Phoenix-vs-WOAC row (976) — linter-found**
- Before: "WOAC adds worst-of basket → **short** correlation."
- After: "WOAC adds worst-of basket → investor **long** correlation (MTM; structurally sold corr premium)."

**E-13 · Desk_Bible NTD common-mistakes (18062) — linter-found**
- Before: "Treating all NTD tranches as 'long correlation.' Only high-N NTDs (4TD, 5TD) are **reliably long** correlation."  *(contradicts E-09)*
- After: "Under the MTM convention, all NTD tranches (N≥2) are **short** correlation… Only the FTD (N=1) is long correlation."

### B. Raw-vs-hedged qualifiers (factually safe regardless of Part 1)

**E-03 · part6_sections_10_11 (102) AND Desk_Bible merged copy (25249)**
- Before: "This benefits the desk (**which sold protection via the short put**)." *(factually wrong — the investor sold the put)*
- After: "The desk's **net (hedged)** position benefits… the **investor** sold the embedded put and is structurally short; the desk is long the put."

**E-04a · part6 (110) AND Desk_Bible merged copy (25257)**
- Before: "Short gamma, short vega, long correlation (worst-of)"
- After: "…long correlation (worst-of, **net/hedged** position)"

**E-04b · infrastructure_encyclopedia (4290)**
- Before: "Worst-of products are SHORT correlation (dealer profits if correlation falls)"
- After: "The desk's **raw (unhedged)** worst-of position is short correlation … After dispersion hedging, the desk is typically **net long** correlation."

**Precision touch · Desk_Bible (17973)**
- Before: "A bank that is short correlation from FTDs…"
- After: "A bank whose **raw position** is short correlation from selling FTDs…"

### C. Pure arithmetic / factual (independent of any convention)

**E-05 · Desk_Bible WOAC 65% (22565)**
- Before: "ASML finishes at 65%: **above** strike (100%), so principal returned." *(65 < 100 — false)*
- After: "65%: **below strike (100%)**, physical delivery: €500,000/€700 = 714 shares × (0.65×€700) = €324,870. Loss €175,130." *(Verified against the parallel 55% line and the €500k/€700 terms.)*

**E-06 · Desk_Bible dispersion diagram (22605)**
- Before: "long single-stock vol + short basket vol = **long** correlation" *(dispersion = short corr)*
- After: "…= **short** correlation (dispersion trade)"

**E-07 · Desk_Bible gamma sign (1069)**
- Before: "New Delta ≈ -50 + (3 × 2) = -56" *(3×2=6, so -50+6=-44, not -56)*
- After: "New Delta ≈ -50 + (3 × (−2)) = -50 − 6 = **-56**" *(ΔS = −2 for a drop; final answer unchanged)*

**Stale review question · Desk_Bible (17645)**
- Before: "What does it mean to say that FTD investors are 'short correlation'?"
- After: "FTD investors are long correlation under the MTM convention, yet are sometimes described as *structurally* short. Explain the distinction."

---

## PART 3 — How to verify independently (no tools needed)

1. **Spot-check the convention** on one example you know cold (e.g., worst-of). Ask: "if the three stocks move *together*, is the worst-of investor better or worse off?" → Better (the worst stock isn't dragged down alone) → benefits from high ρ → **long** under MTM. If you agree, the whole class is right.
2. **Check E-05/E-07 arithmetic** by hand — they're convention-independent and either right or wrong.
3. **Confirm line 358 / desk-raw statements still say "short"** — the desk's *raw* position genuinely is short correlation; only the *investor* and *hedged desk* labels flipped. If any desk-raw line now says "long," that's an error (none do, per the linter).

---

*V1.0.1 Verification Review | 2026-06-27 | Sign-off pending: convention choice (Part 1) + arithmetic spot-check (Part 3)*
