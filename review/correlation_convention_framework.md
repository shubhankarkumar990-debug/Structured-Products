# CORRELATION CONVENTION FRAMEWORK — V1.0.1

**Purpose:** Canonical reference for interpreting "long correlation" and "short correlation" throughout the Desk Bible ecosystem.  
**Effective:** V1.0.1 Errata Package  
**Cross-reference:** This document is referenced by every correlation-related erratum item.

---

## Why Correlation Language Is Ambiguous

In structured products, "long correlation" and "short correlation" are used under two different conventions that produce **opposite labels for the same position**. The V1.0 ecosystem used both conventions without declaring which was active, producing self-contradictory sentences. V1.0.1 resolves this by adopting a single canonical teaching convention.

---

## The Two Conventions

### Convention A — MTM / Economic Sensitivity (DEFAULT)

| Term | Meaning |
|:----:|---------|
| **Long correlation** | The position **benefits** when correlation **rises** (P&L increases, risk decreases) |
| **Short correlation** | The position **benefits** when correlation **falls** (P&L increases, risk decreases) |

This convention answers: *"What happens to my P&L when correlation changes?"*

### Convention B — Structural / Premium Direction

| Term | Meaning |
|:----:|---------|
| **Long correlation** | The position holder **bought** the correlation premium (paid for correlation exposure) |
| **Short correlation** | The position holder **sold** the correlation premium (earned yield by taking correlation risk) |

This convention answers: *"Who paid and who received the correlation-driven premium?"*

### Why They Conflict

An FTD investor **sells** the first-default premium (structural: **short**) but **benefits** when correlation is high (MTM: **long**). The same position is "short" under one convention and "long" under the other.

---

## V1.0.1 Canonical Teaching Convention

**V1.0.1 uses Convention A (MTM / Economic Sensitivity) as the default.**

All user-facing educational text uses this rule:

> If correlation rising **helps** the position → the position is **long correlation**.  
> If correlation rising **hurts** the position → the position is **short correlation**.

When the structural convention is needed (e.g., to describe who earned the premium), it is explicitly labeled:

> "The investor is **structurally** short correlation (sold the correlation premium)..."

The word "structurally" signals Convention B. Without that qualifier, assume Convention A.

---

## Canonical Direction Table

| Product | Investor Direction (MTM) | Economic Reasoning |
|---------|:------------------------:|-------------------|
| **FTD** | **Long** correlation | High ρ → defaults cluster → fewer first-default events → investor benefits |
| **NTD (N≥2)** | **Short** correlation | High ρ → defaults cluster → once first default occurs, Nth follows quickly → investor harmed |
| **CDO Equity** | **Long** correlation | High ρ → losses cluster → fewer small independent losses eating equity → equity benefits |
| **CDO Senior** | **Short** correlation | High ρ → losses cluster → catastrophic losses reach senior tranche → senior harmed |
| **Worst-of (investor)** | **Long** correlation | High ρ → stocks move together → worst-of ≈ average → lower barrier breach probability |
| **Worst-of (desk raw)** | **Short** correlation | Desk is long the worst-of put; its value falls when correlation rises |
| **Worst-of (desk hedged)** | **Long** correlation (typical) | After buying correlation via dispersion, desk is typically net long correlation |
| **Dispersion trade** | **Short** correlation | Long single-stock vol + short basket vol profits when stocks diverge (low ρ) |
| **Reverse dispersion** | **Long** correlation | Long basket vol + short single-stock vol profits when stocks converge (high ρ) |

---

## The "Correlation Reversal" in NTD Products

The term "correlation reversal" in NTD products refers to the fact that NTD products have the **opposite** correlation direction from FTD:

- **FTD (N=1):** LONG correlation (MTM) — risk decreases with ρ
- **NTD (N≥2):** SHORT correlation (MTM) — risk increases with ρ

The "reversal" is the direction flip between FTD and NTD, not a within-product non-monotonicity. Under the MTM convention, all NTD products (N≥2) are short correlation at all correlation levels: higher ρ always increases the probability that once defaults begin, they cluster past the Nth threshold.

---

## Raw vs Hedged Position Note

When describing a **desk position**, always specify whether it is:

| Qualifier | Meaning | Example |
|:---------:|---------|---------|
| **Raw / unhedged** | The exposure from the embedded options in products sold to clients, before any hedge | "The desk's **raw** position on worst-of is short correlation (long the worst-of put)" |
| **Net / hedged** | The residual exposure after delta, gamma, vega, and correlation hedging | "The desk's **net** position is typically long correlation (after dispersion hedges)" |

Never leave the raw-vs-hedged distinction implicit when it affects the correlation direction.

---

## Protection Buyer / Seller Note

In credit and worst-of structures, ownership of the embedded option must be stated explicitly:

| Structured Product | Who Sold the Put/Protection | Who Bought the Put/Protection |
|:------------------:|:--------------------------:|:-----------------------------:|
| **Reverse Convertible** | **Investor** (short put, earns coupon) | **Desk** (long put, pays coupon) |
| **Worst-of Autocallable** | **Investor** (short worst-of put, earns coupon) | **Desk** (long worst-of put, pays coupon) |
| **CLN / FTD** | **Investor** (sold credit protection, earns coupon) | **Desk** (bought credit protection, pays coupon) |

**Rule:** The desk does NOT sell protection in these structures — the desk buys it. The investor sells protection and earns the enhanced coupon as compensation.

---

## Correlation Sanity Check

Apply this test to any correlation sentence in the ecosystem:

1. Read the sentence. Does it say the position is "long" or "short" correlation?
2. Read the economic explanation. Does it say the position benefits from correlation rising or falling?
3. Apply the canonical convention:
   - Benefits from correlation rising → **long** correlation
   - Benefits from correlation falling → **short** correlation
4. If the label (step 1) contradicts the economics (step 2), the label is wrong under the canonical convention.

**Example of a failing sentence (V1.0):**
> "FTD investors are **short** correlation. They profit when correlation is high."

- Step 1: Label = short correlation
- Step 2: Economics = profit from high correlation = benefits from correlation rising
- Step 3: Benefits from rising → long correlation
- Step 4: "Short" ≠ "long" → **label is wrong** under canonical convention

---

*V1.0.1 Correlation Convention Framework | Effective: 2026-06-27*
