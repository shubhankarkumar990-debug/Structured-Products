# Tier-3 Numeric Re-Derivation Audit

**Target:** `Desk_Bible_v2.md`. **Date:** 28 Jun 2026. **Tool:** `governance/audit/numeric_audit.py` (read-only).

## What this checks

The semantic linter checks finance *logic*; Tier-1/2 check *structure*; the integrity sweep checks *markdown*. None of them check whether the **arithmetic computes**. This audit does: it extracts every self-contained equation of the form `<expr> = <number>` (coupon decompositions, payoff maths, loss/gain percentages), evaluates the left side with a safe expression evaluator, and compares it to the stated result within a rounding tolerance (0.5 % relative / 0.05 absolute). Percentages are normalised to `/100` on both sides; loss annotations (leading `−`) are matched on magnitude.

## Result

**41 self-contained equations checked — 0 genuine errors.**

The first pass flagged 31 items; **all 31 were artifacts of the checker, not the book**, and were resolved by hardening the tool:

- **24** were percent-handling artifacts — e.g. `60/$100 = 60%` and `90% × 30% = 27%` are correct (`0.6 = 60 %`, `0.27 = 27 %`); the checker had stripped `%` instead of converting it to `/100`.
- **6** were period ranges misread as subtraction — `Years 2-5 = 4 × max(0, CMS30Y − CMS2Y)` means "in years 2 through 5 the coupon is 4 ×…", not `2 − 5`.
- **1** was a chained equation split at the wrong `=` — `1 − 0.964×0.956×0.970×0.950×0.960 = 1 − 0.8153 = 18.5%`. Re-derived independently: the product is 0.81527, and `1 − 0.81527 = 18.47 % ≈ 18.5 %`. Correct.

After fixing the checker's percent, range, and chained-equation handling, the corpus is clean.

## Residual risk — stated honestly

This audit is strong but **not** a complete re-derivation of every number in the book. It verifies *explicit, self-contained* equations (41 of them). It does **not** re-derive multi-sentence worked examples where the relationship spans prose and depends on context — e.g. "Paid \$93,000. Profit: \$7,000 (7.5 %)", where the notional and cost live in earlier sentences. That prose arithmetic was checked by hand during the per-family deep audits (which caught and fixed real errors — DCI conversion direction, Cliquet outperformance, Snowball coupon). 

So the numeric confidence rests on two complementary layers: the per-family hand audits (prose scenarios) and this mechanical check (explicit equations). Both are clean. A *fully exhaustive* re-derivation would require re-implementing each product's payoff model and recomputing every scenario — a substantially larger build that would mostly re-confirm work already done. My recommendation: not worth it unless a specific number is in doubt.

## Re-runnable

`python3 governance/audit/numeric_audit.py` — add to the gate if you want explicit-equation arithmetic guarded on every future edit.
