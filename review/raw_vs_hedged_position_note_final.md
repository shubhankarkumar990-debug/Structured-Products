# RAW VS HEDGED POSITION NOTE — V1.0.1 FINAL

**Purpose:** Clarify the distinction between a desk's raw (unhedged) and net (hedged) position, which directly affects the correct correlation direction label.  
**Status:** FINAL (package closure)  
**Supersedes:** `raw_vs_hedged_position_note.md`

---

## The Distinction

A structured products desk has two simultaneous exposures on any risk factor:

| Position Type | Definition | When It Matters |
|:-------------:|-----------|-----------------|
| **Raw / Unhedged** | The exposure embedded in the products sold to clients, before any hedge is placed | Describes what the desk is structurally exposed to from its book |
| **Net / Hedged** | The residual exposure after all hedges (delta, gamma, vega, correlation, credit) | Describes what the desk actually takes home as P&L risk |

---

## Why This Matters for Correlation

The desk's raw and hedged positions can have **opposite** correlation directions:

### Worst-of Example

| Position | Correlation Direction (MTM) | Reasoning |
|----------|:---------------------------:|-----------|
| Desk raw position | **Short** correlation | Desk is long the worst-of put. When correlation rises, worst-of put value falls → desk's raw position loses |
| Desk correlation hedge | **Long** correlation | Desk buys correlation via reverse dispersion (long basket vol, short single-stock vol) |
| Desk net position | **Long** correlation (typical) | If the hedge exceeds the raw exposure, the desk is net long correlation |

### The V1.0 Conflict

- **Part 6 (line 102):** "The desk benefits when asset correlations increase... long correlation." This describes the **hedged/net** position.
- **Encyclopedia (line 4290):** "Worst-of products are SHORT correlation (dealer profits if correlation falls)." This describes the **raw/unhedged** position.

Both are defensible — but neither specifies its assumption, so a reader comparing them encounters an irreconcilable contradiction.

### V1.0.1 Resolution

- **E-03** adds "(net/hedged)" qualifier to Part 6 line 102
- **E-04a** adds "(net/hedged position)" qualifier to Part 6 line 110
- **E-04b** adds "raw (unhedged)" qualifier to Encyclopedia line 4290 and adds the hedged direction

---

## V1.0.1 Rule

Whenever a sentence describes a desk position:

1. **State whether it is raw or hedged.** Use the words "raw," "unhedged," "net," or "hedged" explicitly.
2. **If the sentence omits the qualifier,** assume it describes the raw position (the more conservative default — it tells you what you are exposed to before you do anything about it).
3. **Never describe a hedged position as if it were a fundamental property of the product.** The hedge is a choice; the raw exposure is structural.

### Corrected Examples

**Before (V1.0 — ambiguous):**
> "The bank is structurally long correlation."

**After (V1.0.1 — explicit):**
> "The bank's net position is typically long correlation after placing dispersion hedges. The raw position from the worst-of book is short correlation."

**Before (V1.0 — ambiguous):**
> "Worst-of products are SHORT correlation (dealer profits if correlation falls)."

**After (V1.0.1 — explicit):**
> "The desk's raw position on worst-of products is short correlation (the worst-of put value falls when correlation rises). The desk typically hedges to a net long correlation position via dispersion trades."

---

*V1.0.1 Raw vs Hedged Position Note | FINAL (package closure) | 2026-06-27*
