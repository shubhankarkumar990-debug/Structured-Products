# DUAL-LENS AUTHORING STANDARD

**Version:** V2.0-DRAFT
**Effective:** 2026-06-27
**Purpose:** Reframe every product chapter so it is read through **two explicit lenses — the bank and the investor — never the reader's own first-person seat.** Tailored for a reader in 2nd-line-of-defence (risk control / trade reconciliation).

---

## 1. The core rule: no first-person investing voice

The document must never put the reader in the position of *being* the investor ("if the stock drops, **you** lose **your** capital"). Economic outcomes are always attributed to a named party.

| Banned (first-person investing) | Required (named party) |
|---|---|
| "If the stock falls, you lose your principal." | "If the stock falls below the barrier, **the investor** loses principal." |
| "You are selling a put to the bank." | "**The investor** sells a put to **the bank**." |
| "You earn an 8% coupon." | "**The investor** earns an 8% coupon; **the bank** funds it from the put premium." |

**Teaching voice is preserved.** Second-person used to address the *reader-as-learner* is fine and should stay: "you will learn," "notice that…," "you can verify this by…". The rule targets only second-person used to describe an *economic position or payoff*. Test: if "you" can be replaced by "the investor" without changing meaning, it must be.

The bakery/borrower analogies that cast "you" as the *issuer* are reframed to "the company" / "the borrower" for the same reason.

---

## 2. The two lenses (both always present, clearly separated)

Every product's economics is presented under three standard headers:

### THE INVESTOR LENS
- **Why they buy** — the need/view the product expresses.
- **Position taken** — what the investor is long/short (option, correlation, vol, rates).
- **Payoff & scenarios** — outcomes at maturity, third person.
- **Risks to the investor** — capital, gap, credit, liquidity, tail.

### THE BANK LENS — Desk Economics (1st Line of Defence)
- **What the desk books** — the offsetting position (e.g. desk is *long* the embedded put).
- **Greeks & hedging** — delta/gamma/vega/correlation, how the desk hedges, where it costs.
- **How the bank makes money** — structuring margin, bid-offer, hedging P&L, funding.
- **P&L drivers** — what moves desk P&L day to day.

### THE BANK LENS — Controls & Reconciliation (2nd Line of Defence)
- **Booking & systems** — book of record vs pricing/risk system vs downstream.
- **Reconciliation points** — the specific fields and events that must agree across systems.
- **Common breaks & red flags** — where data inconsistencies arise for *this* product.
- **Control implication** — what a break means for P&L, risk, or client outcome, and the 2LoD check.

> The 1LoD/2LoD split is deliberate: desk economics is what the *trading desk* (1st line) owns; controls & reconciliation is what *you* (2nd line) own. Keeping them separate mirrors the bank's actual accountability structure.

---

## 3. Standard reconciliation checklist (instantiate per product)

Every Controls & Reconciliation section works through this checklist, keeping only the rows that apply and adding product-specific ones:

| Recon point | What must agree | Typical break |
|---|---|---|
| **Trade economics** | Notional, strike/initial level, barrier level **and convention** (% vs absolute), coupon rate & frequency, maturity, underlying identifier | Barrier stored as % in one system, absolute price in another |
| **Observation type** | European vs American barrier; observation calendar | Continuous barrier monitored only on daily closes |
| **Fixings** | Initial and final fixing **source** matches the termsheet | Different data vendors report different closes |
| **Barrier/event capture** | Knock-in / knock-out / autocall flags consistent across systems | Intraday breach missed → risk and P&L diverge |
| **Coupon lifecycle** | Coupon schedule, day-count, whether coupon survives a knock-in | Coupon paid on a knocked-in trade that should have stopped |
| **Corporate actions** | Strike/barrier adjustment for dividends, splits, mergers | Underlying split not propagated to barrier |
| **P&L attribution** | Split between bond/coupon accrual and option MTM reconciles to total | Unexplained P&L = model or market-data issue |
| **Settlement** | Cash vs physical; share quantity = notional / strike; DvP | Physical delivery booked as cash, or wrong share count |
| **Greeks / risk** | Position Greeks agree between front-office and risk systems | Sign or magnitude mismatch on delta/vega |

---

## 4. Canonical chapter skeleton

```
### 5.x.y Product Name
[neutral framing paragraph — third person]

#### §1. Explain Like I'm New            (reframed: investor + bank, no "you-as-investor")
#### §2. Real-World Analogy              (reframed)
#### §3. What Problem Does This Solve?    (investor need)
#### §4. Product DNA                      (table — unchanged)
#### §5. Who Touches This Product         (roles — unchanged)

#### §6. THE INVESTOR LENS                (why buy / position / payoff & scenarios / risks)
#### §7. THE BANK LENS — Desk Economics   (booking / Greeks & hedging / revenue / P&L)
#### §8. THE BANK LENS — Controls & Reconciliation (2LoD)
                                         (booking & systems / recon points / breaks & red flags / control implication)

#### §9. Worked Example                   (numbers preserved; outcomes shown for BOTH lenses)
#### §10. Knowledge Check / Mental Models / Common Mistakes / Key Takeaways  (dual-lens — see §5)
#### Visual Specifications                 (dual-lens parity — see §5)
#### Dependency References                (unchanged)
```

The pre-existing "How the Bank Makes Money," "Desk Reality," "Booking and Systems," "Red Flags," and "Desk Perspective" blocks are **folded into** §7 and §8 rather than duplicated.

---

## 5. Dual-lens parity for visuals and question banks

The two lenses must extend past the prose into the visuals and the questions — otherwise a reader absorbs the investor story and skims the bank/controls story.

### 5.1 Question-bank parity — ALWAYS

Every chapter's questions (both the in-chapter Knowledge Check and the formal review bank) must include, at minimum:
- one **desk-economics** question (the bank's position, Greeks, hedging, or P&L), and
- one **controls/reconciliation** question (a "spot the break" or "what is the consequence" item in the reader's 2LoD seat).

This is mandatory for all 28 products — it is high-value and low-cost.

### 5.2 Visual parity — BY DEFAULT, where it adds signal (guardrail)

Each chapter should aim for visuals across all three lenses:
- **Investor visual** — payoff / scenario (usually already exists).
- **Desk-economics visual** — the desk's offsetting position, hedge, or Greek profile.
- **Controls/reconciliation visual** — e.g. a reconciliation-flow or "where breaks happen" diagram.

**Guardrail — do not manufacture filler.** Add a controls or desk visual only where the product has a *genuine* second-lens story (e.g. RC barrier-convention reconciliation, worst-of dispersion hedge). For structurally simple products (e.g. a vanilla IRS) where the controls story is thin, use a **shared note** under the existing visual rather than inventing a diagram. Symmetry is not the goal; signal is.

**Production honesty.** Every NEW visual is a *specification only*, tagged `[spec-only — requires rendering]`, and added to the asset manifest. These do not exist as SVGs until a downstream design pass produces them. Do not imply a rendered asset exists.

---

## 6. What does NOT change

- All numbers, worked-example results, and the V1.0.1 semantic corrections (MTM correlation convention, raw/hedged qualifiers, arithmetic fixes).
- Product DNA, complexity scores, system mappings, dependency references.
- The semantic linter must continue to report **0 findings** after each chapter is restructured.

---

*Dual-Lens Authoring Standard | V2.1-DRAFT (adds visual + question-bank parity, §5) | 2026-06-27*
