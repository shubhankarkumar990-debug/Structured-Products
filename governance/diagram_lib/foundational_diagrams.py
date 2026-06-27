#!/usr/bin/env python3
"""
Foundational concept diagrams (Parts 0-3) — real SVGs replacing ASCII art.
House palette, consistent with sp_diagrams.py. Calibrated to the book's text.
Run as a script to (re)generate every SVG into assets/foundations/.
"""
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.colors import LinearSegmentedColormap
from matplotlib.patches import FancyBboxPatch, FancyArrowPatch
import numpy as np
from pathlib import Path
import textwrap

NAVY = "#1f3a5f"; SLATE = "#41607f"; ACCENT = "#c8553d"; GREEN = "#2e7d5b"
AMBER = "#d9a441"; PAPER = "#ffffff"; LIGHT = "#eef2f6"

ASSETS = Path(__file__).resolve().parents[2] / "assets" / "foundations"
ASSETS.mkdir(parents=True, exist_ok=True)

plt.rcParams.update({
    "font.family": "DejaVu Sans", "text.color": NAVY,
    "axes.edgecolor": SLATE, "savefig.facecolor": PAPER, "figure.facecolor": PAPER,
})


def _save(fig, name):
    p = ASSETS / name
    fig.savefig(p, format="svg", bbox_inches="tight"); plt.close(fig)
    return p


# ---------- 1. risk spectrum ----------
def risk_spectrum():
    tiers = [("Savings\nAccount", "~2%", GREEN), ("Government\nBonds", "~3–4%", "#4f9d69"),
             ("Corporate\nBonds", "~4–6%", AMBER), ("Stocks", "~8–10%", "#d98445"),
             ("Startups\n& Crypto", "???", ACCENT)]
    fig, ax = plt.subplots(figsize=(10, 3.0), dpi=150)
    ax.set_xlim(0, 10); ax.set_ylim(0, 3); ax.axis("off")
    cmap = LinearSegmentedColormap.from_list("risk", [GREEN, "#4f9d69", AMBER, "#d98445", ACCENT])
    ax.imshow(np.linspace(0, 1, 256).reshape(1, -1), extent=[0.4, 9.6, 1.55, 2.05], aspect="auto", cmap=cmap, zorder=1)
    ax.add_patch(plt.Rectangle((0.4, 1.55), 9.2, 0.5, fill=False, ec=NAVY, lw=1.2, zorder=3))
    ax.text(0.4, 2.35, "LOW RISK", fontsize=11, fontweight="bold", color=GREEN)
    ax.text(0.4, 2.18, "LOW RETURN", fontsize=9, color=SLATE)
    ax.text(9.6, 2.35, "HIGH RISK", fontsize=11, fontweight="bold", color=ACCENT, ha="right")
    ax.text(9.6, 2.18, "HIGH RETURN", fontsize=9, color=SLATE, ha="right")
    for x, (name, ret, col) in zip(np.linspace(1.2, 8.8, len(tiers)), tiers):
        ax.plot([x, x], [1.5, 1.3], color=col, lw=1.4, zorder=4)
        ax.scatter([x], [1.55], s=40, color=col, ec=NAVY, lw=0.6, zorder=5)
        ax.text(x, 1.15, name, fontsize=9.5, fontweight="bold", ha="center", va="top")
        ax.text(x, 0.55, ret, fontsize=9, color=col, ha="center", va="top", fontweight="bold")
    ax.text(5.0, 2.78, "The Risk–Return Spectrum", fontsize=13, fontweight="bold", ha="center")
    fig.tight_layout(); return _save(fig, "concept_risk_spectrum_01.svg")


# ---------- 2-3. option payoff sketches ----------
def option_payoff(kind, name):
    K, prem = 100.0, 5.0
    x = np.linspace(70, 140, 400)
    if kind == "call":
        y = np.maximum(x - K, 0) - prem; be = K + prem
    else:
        y = np.maximum(K - x, 0) - prem; be = K - prem
    fig, ax = plt.subplots(figsize=(7.2, 4.2), dpi=150)
    ax.plot(x, y, color=GREEN, lw=2.6)
    ax.fill_between(x, y, 0, where=(y > 0), color=GREEN, alpha=0.12)
    ax.fill_between(x, y, 0, where=(y < 0), color=ACCENT, alpha=0.10)
    ax.axhline(0, color=SLATE, lw=0.9); ax.axvline(K, color=SLATE, lw=0.8, ls=":")
    ax.axhline(-prem, color=ACCENT, lw=1.0, ls="--")
    ax.axvline(be, color=NAVY, lw=0.8, ls=":")
    ax.annotate("Strike", (K, 0), xytext=(K, -prem - 4), ha="center", fontsize=9, color=SLATE)
    ax.annotate(f"Breakeven\n(Strike {'+' if kind=='call' else '−'} Premium)", (be, 0),
                xytext=(be + (6 if kind == 'call' else -6), 6), ha="left" if kind == "call" else "right",
                fontsize=8.5, color=NAVY, arrowprops=dict(arrowstyle="->", color=NAVY, lw=0.8))
    ax.annotate("Max loss = Premium paid", (x[5], -prem), xytext=(x[5], -prem - 6),
                fontsize=8.5, color=ACCENT)
    ax.set_xlabel("Underlying Price", color=NAVY); ax.set_ylabel("Profit", color=NAVY)
    ax.set_title(name, color=NAVY, fontsize=12, fontweight="bold", loc="left")
    ax.set_ylim(-prem - 10, 38); ax.spines[["top", "right"]].set_visible(False)
    fig.tight_layout(); return _save(fig, f"concept_payoff_{kind}_01.svg")


# ---------- 4. vol term structure ----------
def vol_term_structure():
    x = np.array([1, 2, 3, 4, 5]); y = np.array([14, 16, 17.5, 18.5, 19])
    fig, ax = plt.subplots(figsize=(7.2, 4.0), dpi=150)
    xs = np.linspace(1, 5, 200); ys = np.interp(xs, x, y)
    ax.plot(xs, ys, color=NAVY, lw=2.6)
    ax.scatter(x, y, color=ACCENT, zorder=5, s=30)
    ax.set_xticks(x); ax.set_xticklabels(["1m", "3m", "6m", "1y", "2y"])
    ax.set_xlabel("Time to Expiry", color=NAVY); ax.set_ylabel("Implied Volatility (%)", color=NAVY)
    ax.set_title("Volatility Term Structure (upward-sloping)", color=NAVY, fontsize=12, fontweight="bold", loc="left")
    ax.spines[["top", "right"]].set_visible(False); ax.set_ylim(10, 22)
    fig.tight_layout(); return _save(fig, "concept_vol_term_01.svg")


# ---------- 5. vol smile / skew ----------
def vol_smile():
    x = np.linspace(80, 120, 200); y = 0.012 * (x - 98) ** 2 + 15
    fig, ax = plt.subplots(figsize=(7.2, 4.0), dpi=150)
    ax.plot(x, y, color=NAVY, lw=2.6)
    ax.axvline(100, color=SLATE, ls=":", lw=0.8)
    ax.set_xlabel("Strike", color=NAVY); ax.set_ylabel("Implied Volatility (%)", color=NAVY)
    ax.set_title("Volatility Smile / Skew", color=NAVY, fontsize=12, fontweight="bold", loc="left")
    ax.annotate("Low strikes\n(OTM puts)", (82, y[10]), fontsize=8.5, color=ACCENT, ha="left")
    ax.annotate("ATM", (100, 14.4), fontsize=8.5, color=SLATE, ha="center")
    ax.annotate("High strikes\n(OTM calls)", (118, y[-10]), fontsize=8.5, color=GREEN, ha="right")
    ax.spines[["top", "right"]].set_visible(False)
    fig.tight_layout(); return _save(fig, "concept_vol_smile_01.svg")


# ---------- 6. yield curve ----------
def yield_curve():
    x = np.arange(8); y = np.array([1.0, 1.6, 2.1, 2.7, 3.3, 4.0, 4.6, 5.0])
    fig, ax = plt.subplots(figsize=(7.6, 4.0), dpi=150)
    xs = np.linspace(0, 7, 200); ys = np.interp(xs, x, y)
    ax.plot(xs, ys, color=GREEN, lw=2.6); ax.scatter(x, y, color=NAVY, zorder=5, s=26)
    ax.set_xticks(x); ax.set_xticklabels(["1m", "3m", "6m", "1y", "2y", "5y", "10y", "30y"])
    ax.set_yticks([1, 2, 3, 4, 5]); ax.set_xlabel("Maturity", color=NAVY); ax.set_ylabel("Yield (%)", color=NAVY)
    ax.set_title("Normal (upward-sloping) Yield Curve", color=NAVY, fontsize=12, fontweight="bold", loc="left")
    ax.spines[["top", "right"]].set_visible(False)
    fig.tight_layout(); return _save(fig, "concept_yield_curve_01.svg")


# ---------- 7-8. two-party flow (swap, CDS) ----------
def two_party_flow(left, right, leg_top, leg_bot, title, name):
    fig, ax = plt.subplots(figsize=(8.6, 3.4), dpi=150)
    ax.set_xlim(0, 10); ax.set_ylim(0, 4); ax.axis("off")
    for cx, (t1, t2), col in [(1.9, left, NAVY), (8.1, right, SLATE)]:
        ax.add_patch(FancyBboxPatch((cx - 1.5, 1.4), 3.0, 1.2, boxstyle="round,pad=0.05,rounding_size=0.12",
                                    fc=LIGHT, ec=col, lw=1.6))
        ax.text(cx, 2.15, t1, ha="center", fontsize=10.5, fontweight="bold", color=col)
        ax.text(cx, 1.72, t2, ha="center", fontsize=8.5, color=SLATE)
    ax.add_patch(FancyArrowPatch((3.5, 2.35), (6.5, 2.35), arrowstyle="-|>", mutation_scale=14, color=GREEN, lw=1.8))
    ax.text(5.0, 2.55, leg_top, ha="center", fontsize=9, color=GREEN, fontweight="bold")
    ax.add_patch(FancyArrowPatch((6.5, 1.65), (3.5, 1.65), arrowstyle="-|>", mutation_scale=14, color=ACCENT, lw=1.8))
    ax.text(5.0, 1.32, leg_bot, ha="center", fontsize=9, color=ACCENT, fontweight="bold")
    ax.text(5.0, 3.35, title, ha="center", fontsize=12, fontweight="bold", color=NAVY)
    fig.tight_layout(); return _save(fig, name)


# ---------- 9. note mechanics flow ----------
def note_mechanics_flow():
    fig, ax = plt.subplots(figsize=(9.6, 5.4), dpi=150)
    ax.set_xlim(0, 12); ax.set_ylim(0, 7); ax.axis("off")
    def box(cx, cy, w, h, t1, t2, col):
        ax.add_patch(FancyBboxPatch((cx - w / 2, cy - h / 2), w, h, boxstyle="round,pad=0.04,rounding_size=0.1",
                                    fc=LIGHT, ec=col, lw=1.6))
        ax.text(cx, cy + 0.18, t1, ha="center", fontsize=10, fontweight="bold", color=col)
        if t2: ax.text(cx, cy - 0.32, t2, ha="center", fontsize=7.8, color=SLATE)
    def arrow(p, q, col, t, dy=0.18):
        ax.add_patch(FancyArrowPatch(p, q, arrowstyle="-|>", mutation_scale=13, color=col, lw=1.6))
        mx, my = (p[0] + q[0]) / 2, (p[1] + q[1]) / 2
        ax.text(mx, my + dy, t, ha="center", fontsize=7.8, color=col, fontweight="bold")
    box(1.6, 6.0, 2.6, 1.0, "INVESTOR", "buys the note", NAVY)
    box(6.0, 6.0, 2.6, 1.0, "ISSUER", "the note wrapper", SLATE)
    box(10.3, 6.0, 2.8, 1.0, "BANK BALANCE", "SHEET", NAVY)
    box(6.0, 3.4, 2.6, 1.0, "TREASURY", "internal funding", AMBER)
    box(6.0, 1.1, 2.6, 1.0, "MARKET", "hedge counterparties", GREEN)
    arrow((2.9, 6.0), (4.7, 6.0), GREEN, "Principal")
    arrow((7.3, 6.0), (8.9, 6.0), GREEN, "Funding")
    arrow((4.7, 5.6), (2.9, 5.6), ACCENT, "Coupons / Redemption", dy=-0.3)
    arrow((10.3, 5.5), (6.9, 3.7), AMBER, "FTP cost", dy=0.0)
    arrow((10.3, 5.5), (6.9, 1.4), GREEN, "Hedge costs", dy=0.0)
    ax.text(6.0, 0.25, "Hedge legs: delta, vega, options, swaps", ha="center", fontsize=8, color=SLATE, style="italic")
    ax.text(6.0, 6.85, "How a Structured Note Flows Through the Bank", ha="center", fontsize=12.5, fontweight="bold", color=NAVY)
    fig.tight_layout(); return _save(fig, "concept_note_mechanics_01.svg")


# ---------- 10. protection spectrum ----------
def protection_spectrum():
    cols = [("FULL PROTECTION", "Principal guaranteed", ["PPN"], "Low coupon", "(safest)", GREEN),
            ("CONDITIONAL PROTECTION", "Protected unless barrier hit", ["RC / Phoenix", "Airbag / FCN"], "Medium–high coupon", "(most common)", AMBER),
            ("NO PROTECTION", "Full market exposure", ["Warrant", "Accumulator"], "Highest coupon", "(riskiest)", ACCENT)]
    fig, ax = plt.subplots(figsize=(10, 4.2), dpi=150); ax.set_xlim(0, 12); ax.set_ylim(0, 6); ax.axis("off")
    for cx, (h, sub, prods, coupon, tag, col) in zip([2, 6, 10], cols):
        ax.add_patch(FancyBboxPatch((cx - 1.8, 4.4), 3.6, 1.0, boxstyle="round,pad=0.04,rounding_size=0.1", fc=col, ec=col, lw=0))
        ax.text(cx, 4.98, h, ha="center", fontsize=9.5, fontweight="bold", color="white")
        ax.text(cx, 4.62, sub, ha="center", fontsize=7.6, color="white")
        for k, p in enumerate(prods):
            ax.text(cx, 3.7 - k * 0.5, p, ha="center", fontsize=10, fontweight="bold", color=NAVY)
        ax.text(cx, 2.4, tag, ha="center", fontsize=8, color=SLATE, style="italic")
        ax.text(cx, 1.5, coupon, ha="center", fontsize=9, color=col, fontweight="bold")
        ax.plot([cx, cx], [4.4, 3.95], color=col, lw=1.2)
    ax.annotate("", (10.6, 0.8), (1.4, 0.8), arrowprops=dict(arrowstyle="-|>", color=SLATE, lw=1.4))
    ax.text(1.4, 0.45, "less risk", fontsize=8, color=GREEN); ax.text(10.6, 0.45, "more risk", fontsize=8, color=ACCENT, ha="right")
    ax.text(6, 5.7, "The Capital-Protection Spectrum", ha="center", fontsize=12.5, fontweight="bold", color=NAVY)
    fig.tight_layout(); return _save(fig, "concept_protection_spectrum_01.svg")


# ---------- 11-14. taxonomy trees ----------
def taxonomy_tree(title, groups, name, wrap=58, h_per=0.34):
    # groups = [(group_name, [(product, desc), ...]), ...]
    rows = []
    for g, leaves in groups:
        rows.append(("group", g, ""))
        for p, d in leaves:
            rows.append(("leaf", p, d))
    nrows = len(rows)
    fig_h = max(3.5, 0.42 * nrows + 1.0)
    fig, ax = plt.subplots(figsize=(11, fig_h), dpi=150); ax.axis("off")
    ax.set_xlim(0, 12); ax.set_ylim(0, nrows + 1)
    y = nrows
    ax.text(0.2, y + 0.5, title, fontsize=13, fontweight="bold", color=NAVY)
    group_x, leaf_x = 0.5, 1.3
    for kind, a, b in rows:
        if kind == "group":
            ax.add_patch(FancyBboxPatch((group_x - 0.1, y - 0.16), 4.4, 0.42,
                         boxstyle="round,pad=0.02,rounding_size=0.08", fc=NAVY, ec=NAVY))
            ax.text(group_x + 0.15, y + 0.05, a, fontsize=10, fontweight="bold", color="white", va="center")
        else:
            ax.plot([leaf_x - 0.4, leaf_x - 0.15], [y + 0.05, y + 0.05], color=SLATE, lw=1.0)
            ax.scatter([leaf_x - 0.05], [y + 0.05], s=14, color=ACCENT, zorder=5)
            ax.text(leaf_x + 0.1, y + 0.05, a, fontsize=9.3, fontweight="bold", color=NAVY, va="center")
            if b:
                wrapped = textwrap.fill(b, wrap)
                ax.text(5.3, y + 0.05, wrapped, fontsize=7.8, color=SLATE, va="center")
        y -= 1
    fig.tight_layout(); return _save(fig, name)


# ---------- 15. CDO tranche waterfall ----------
def tranche_waterfall():
    bands = [("SUPER-SENIOR", "15–100%", "Catastrophic scenario only", "#6b8cae"),
             ("SENIOR", "7–15%", "After mezzanine exhausted", SLATE),
             ("MEZZANINE", "3–7%", "After equity exhausted", AMBER),
             ("EQUITY", "0–3%", "First-loss position", ACCENT)]
    fig, ax = plt.subplots(figsize=(8.6, 4.8), dpi=150); ax.set_xlim(0, 10); ax.set_ylim(0, 5); ax.axis("off")
    for i, (n, rng, note, col) in enumerate(bands):
        yb = 0.4 + i * 1.05
        ax.add_patch(FancyBboxPatch((2.2, yb), 5.6, 0.9, boxstyle="round,pad=0.02,rounding_size=0.05", fc=col, ec="white", lw=1.2))
        ax.text(5.0, yb + 0.55, n, ha="center", fontsize=10.5, fontweight="bold", color="white")
        ax.text(5.0, yb + 0.22, f"absorbs loss {rng}", ha="center", fontsize=8, color="white")
        ax.text(8.0, yb + 0.45, note, ha="left", fontsize=8, color=SLATE, va="center")
    ax.annotate("", (1.4, 0.6), (1.4, 4.5), arrowprops=dict(arrowstyle="-|>", color=NAVY, lw=1.8))
    ax.text(1.0, 2.5, "losses flow\ndownward", rotation=90, ha="center", va="center", fontsize=8.5, color=NAVY, fontweight="bold")
    ax.text(5.0, 4.75, "How Portfolio Losses Hit CDO Tranches", ha="center", fontsize=12.5, fontweight="bold", color=NAVY)
    fig.tight_layout(); return _save(fig, "concept_tranche_waterfall_01.svg")


# ---------- 16. systems flow (vertical) ----------
def systems_flow():
    steps = [("TRADE ENTRY", "booked in NEMO or MUREX", NAVY),
             ("PRICING & RISK", "valued in SOPHIS or MUREX", SLATE),
             ("PRODUCT CONTROL", "reconciliation & P&L verification", GREEN)]
    fig, ax = plt.subplots(figsize=(7.6, 4.6), dpi=150); ax.set_xlim(0, 10); ax.set_ylim(0, 6); ax.axis("off")
    ys = [4.6, 2.8, 1.0]
    for y, (t1, t2, col) in zip(ys, steps):
        ax.add_patch(FancyBboxPatch((2.2, y - 0.55), 5.6, 1.1, boxstyle="round,pad=0.04,rounding_size=0.1",
                                    fc=LIGHT, ec=col, lw=1.7))
        ax.text(5.0, y + 0.12, t1, ha="center", fontsize=11, fontweight="bold", color=col)
        ax.text(5.0, y - 0.28, t2, ha="center", fontsize=8.5, color=SLATE)
    for y0, y1 in [(ys[0] - 0.55, ys[1] + 0.55), (ys[1] - 0.55, ys[2] + 0.55)]:
        ax.add_patch(FancyArrowPatch((5.0, y0), (5.0, y1), arrowstyle="-|>", mutation_scale=15, color=SLATE, lw=1.8))
    ax.text(5.0, 5.6, "How a Trade Flows Through the Systems", ha="center", fontsize=12.5, fontweight="bold", color=NAVY)
    fig.tight_layout(); return _save(fig, "concept_systems_flow_01.svg")


# ---------- 17. settlement timeline (horizontal) ----------
def settlement_timeline():
    steps = [("Trade Date", "(T)"), ("+ Settlement Lag", "(typically T+2)"),
             ("Settlement Date", "(T+2)"), ("DvP Instruction", "(sent to CSD)"),
             ("Cash / Securities", "Exchange (via CSD)")]
    fig, ax = plt.subplots(figsize=(11, 2.8), dpi=150); ax.set_xlim(0, 11); ax.set_ylim(0, 3); ax.axis("off")
    xs = np.linspace(1.1, 9.9, len(steps))
    cols = [NAVY, SLATE, NAVY, SLATE, GREEN]
    for x, (t1, t2), col in zip(xs, steps, cols):
        ax.add_patch(FancyBboxPatch((x - 0.85, 1.2), 1.7, 1.0, boxstyle="round,pad=0.03,rounding_size=0.1",
                                    fc=LIGHT, ec=col, lw=1.5))
        ax.text(x, 1.85, t1, ha="center", fontsize=8.3, fontweight="bold", color=col)
        ax.text(x, 1.45, t2, ha="center", fontsize=7.2, color=SLATE)
    for x0, x1 in zip(xs[:-1], xs[1:]):
        ax.add_patch(FancyArrowPatch((x0 + 0.85, 1.7), (x1 - 0.85, 1.7), arrowstyle="-|>", mutation_scale=11, color=ACCENT, lw=1.5))
    ax.text(5.5, 2.6, "Settlement Workflow (DvP)", ha="center", fontsize=12, fontweight="bold", color=NAVY)
    fig.tight_layout(); return _save(fig, "concept_settlement_timeline_01.svg")


def build_all():
    out = []
    out.append(risk_spectrum())
    out.append(option_payoff("call", "Long Call — Payoff at Expiry"))
    out.append(option_payoff("put", "Long Put — Payoff at Expiry"))
    out.append(vol_term_structure()); out.append(vol_smile()); out.append(yield_curve())
    out.append(two_party_flow(("Party A", "Fixed Payer"), ("Party B", "Floating Payer"),
                              "Fixed Rate (3%)", "Floating Rate (SOFR)", "Interest Rate Swap — Cash Flows", "concept_swap_flow_01.svg"))
    out.append(two_party_flow(("Protection Buyer", "worried about default"), ("Protection Seller", "takes the risk"),
                              "CDS Spread (regular fee)", "Payment if default occurs", "Credit Default Swap — Cash Flows", "concept_cds_flow_01.svg"))
    out.append(note_mechanics_flow()); out.append(protection_spectrum())
    out.append(taxonomy_tree("Equity-Linked Notes", [
        ("Reverse Convertible Variants", [
            ("Reverse Convertible (RC)", "Core product: fixed coupon, knock-in put"),
            ("Discounted RC (DRC)", "Instead of a coupon, investor buys at a discount (e.g. pays $95 for $100 par)"),
            ("Knock-Out Discounted RC (KODRC)", "Adds a KO barrier above — if stock rises enough, the put is extinguished"),
            ("Callable RC (CRC)", "Bank can redeem early — adds reinvestment risk for the investor"),
            ("Airbag / Leveraged RC", "Below the barrier, losses are amplified by a leverage factor")]),
        ("Autocallable Variants", [
            ("Fixed Coupon Note (FCN)", "Like an RC with automatic early redemption if the stock is above a level on observation dates"),
            ("Phoenix Autocallable", "Coupon conditional — paid only if stock is above a threshold, with memory for missed coupons"),
            ("Callable Range Accrual ELN", "Coupon accrues day-by-day depending on whether the stock stays in a range")]),
        ("Other ELNs", [
            ("Principal Protected Note (PPN)", "Full capital protection — investor cannot lose principal, but gives up most upside"),
            ("Bonus / Participation Note", "Investor participates in upside; a floor protects against moderate losses"),
            ("Issuer Callable Note (ICN)", "Fixed coupon with issuer call right — no barrier, no put"),
            ("Digital Coupon Notes", "All-or-nothing coupon: full coupon if stock above threshold, zero if below"),
            ("Booster Note", "Leveraged upside participation — gains are multiplied, but so are losses"),
            ("Digital Coupon Knock-In Put", "Combines digital coupon with a knock-in barrier — most complex ELN variant"),
            ("Warrant / Turbo Certificate", "Pure option exposure without a bond wrapper — no coupon, no protection")]),
    ], "concept_taxonomy_eln_01.svg"))
    out.append(taxonomy_tree("Structured Rate Trades", [
        ("Callable", [
            ("IR Callable Fixed Rate Swap", "Fixed coupon, but the issuer can redeem early if rates move in its favour"),
            ("IR Callable Range Accrual", "Coupon accrues daily when a reference rate stays within a range; issuer can call")]),
        ("Non-Callable", [
            ("IR Non-Callable Range Accrual", "Same as callable range accrual, but runs to maturity — no early redemption")]),
        ("Accreting", [
            ("IR Accreting Callable / ZCL", "No periodic coupons — the notional grows over time, investor receives the total at maturity")]),
        ("Digital", [
            ("Digital Cap-Floor", "Pays a fixed amount if a rate is above a cap or below a floor; nothing otherwise")]),
    ], "concept_taxonomy_rates_01.svg"))
    out.append(taxonomy_tree("Steepener Notes", [
        ("Variants", [
            ("Vanilla Steepener", "Coupon = CMS30Y − CMS2Y"),
            ("Range-Accrual Steepener", "Coupon accrues when spread in range"),
            ("Callable Steepener", "Adds issuer call right"),
            ("TARN Steepener", "Coupon capped at lifetime total")]),
    ], "concept_taxonomy_steepener_01.svg"))
    out.append(taxonomy_tree("Credit-Linked Notes", [
        ("Single-Name", [
            ("Vanilla CLN", "Investor sells credit protection on one company; earns CDS spread as coupon"),
            ("Skew CLN", "Like a Vanilla CLN but with modified recovery terms that shift payout under default")]),
        ("Basket", [
            ("First-to-Default (FTD)", "Investor sells protection on a basket of 5–10 companies; first default triggers loss"),
            ("Nth-to-Default (NTD)", "Like FTD but the Nth default triggers loss — second-to-default is less risky than first")]),
        ("Portfolio", [
            ("Synthetic CDO Tranche", "Investor takes a slice of credit risk on a 100+ name portfolio; complex correlation exposure")]),
    ], "concept_taxonomy_cln_01.svg"))
    out.append(tranche_waterfall())
    out.append(systems_flow())
    out.append(settlement_timeline())
    return out


if __name__ == "__main__":
    for p in build_all():
        print("wrote", p.name)
