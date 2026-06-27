#!/usr/bin/env python3
"""
sp_diagrams — reusable, house-styled diagram generators for the
Structured Products Desk Bible dual-lens rollout.

Goals:
  - One consistent visual style across every chapter (palette, fonts, layout).
  - Parameterized generators so each diagram is CALIBRATED to a chapter's actual
    worked-example numbers, not redrawn by hand.
  - Pure code output: each generator writes a real .svg file (and an optional
    .png preview). No human rendering step.

Dependencies: matplotlib, numpy (charts); cairosvg (optional, PNG preview only).

Lens convention (titles encode which lens a diagram serves):
  - "Investor Lens"
  - "Bank Lens (Desk Economics)"        -> 1st line of defence
  - "Bank Lens (Controls & 2LoD)"       -> 2nd line of defence

Each generator returns the output .svg path.
"""

from __future__ import annotations

import html
from pathlib import Path
from typing import Optional, Sequence

import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

# --------------------------------------------------------------------------- #
# House style
# --------------------------------------------------------------------------- #
NAVY = "#1f3a5f"
SLATE = "#41607f"
ACCENT = "#c8553d"     # breaks / barriers / loss
GREEN = "#2e7d5b"      # gains / protected
GOLD = "#c8902d"
GREY = "#8a99a8"
LIGHT = "#eef2f6"
PALE = "#f7f3ec"

LENS_INVESTOR = "Investor Lens"
LENS_DESK = "Bank Lens (Desk Economics)"
LENS_CONTROLS = "Bank Lens (Controls & 2LoD)"


def _apply_style():
    plt.rcParams.update({
        "font.family": "DejaVu Sans",
        "font.size": 11,
        "svg.fonttype": "none",          # keep text as text (selectable, small files)
        "axes.edgecolor": SLATE,
        "axes.labelcolor": NAVY,
        "text.color": NAVY,
        "xtick.color": SLATE,
        "ytick.color": SLATE,
    })


def _esc(t: str) -> str:
    return html.escape(str(t), quote=False)


def render_png(svg_path: str | Path, width: int = 900) -> Optional[str]:
    """Render a PNG preview next to the SVG. Returns the PNG path or None."""
    try:
        import cairosvg
    except Exception:
        return None
    svg_path = Path(svg_path)
    png_path = svg_path.with_suffix(".png")
    cairosvg.svg2png(url=str(svg_path), write_to=str(png_path), output_width=width)
    return str(png_path)


def _finish(fig, out_svg: str | Path, preview: bool) -> str:
    out_svg = Path(out_svg)
    out_svg.parent.mkdir(parents=True, exist_ok=True)
    fig.tight_layout()
    fig.savefig(out_svg)
    plt.close(fig)
    if preview:
        render_png(out_svg)
    return str(out_svg)


# --------------------------------------------------------------------------- #
# 1. Payoff at maturity — barrier note (RC / DRC / KODRC / FCN family)
# --------------------------------------------------------------------------- #
def payoff_barrier_note(
    out_svg: str | Path,
    *,
    barrier_pct: float,
    coupon_pct: float,
    strike_pct: float = 100.0,
    initial_label: str = "Initial (100%)",
    title: str = "Payoff at Maturity",
    lens: str = LENS_INVESTOR,
    x_max: float = 140.0,
    cap_pct: Optional[float] = None,
    preview: bool = True,
) -> str:
    """Payoff for a reverse-convertible-style barrier note, as investor total return.

    Above the barrier at maturity: return = +coupon_pct (par returned).
    Below the barrier: return = (final - strike) + coupon_pct  (share delivery loss).
    Discontinuity at the barrier is drawn explicitly.

    All percentages are in % of initial. Calibrate by passing the chapter's
    barrier, coupon and strike.
    """
    _apply_style()
    fig, ax = plt.subplots(figsize=(7.2, 4.4))

    x_above = np.linspace(barrier_pct, x_max, 200)
    y_above = np.full_like(x_above, coupon_pct)
    if cap_pct is not None:
        y_above = np.minimum(y_above, cap_pct)
    x_below = np.linspace(0, barrier_pct, 200)
    y_below = (x_below - strike_pct) + coupon_pct

    ax.plot(x_above, y_above, color=GREEN, lw=2.6, label="Above barrier: par + coupon")
    ax.plot(x_below, y_below, color=ACCENT, lw=2.6, label="Below barrier: loss + coupon")
    ax.plot([barrier_pct, barrier_pct],
            [(barrier_pct - strike_pct) + coupon_pct, coupon_pct],
            color=GREY, lw=1.4, ls=(0, (4, 3)))
    ax.scatter([barrier_pct], [coupon_pct], color=GREEN, zorder=5, s=28)
    ax.scatter([barrier_pct], [(barrier_pct - strike_pct) + coupon_pct],
               color=ACCENT, zorder=5, s=28)

    jump_to = (barrier_pct - strike_pct) + coupon_pct
    ax.axhline(0, color=SLATE, lw=0.8)
    ax.axvline(strike_pct, color=GREY, lw=0.8, ls=":")
    ax.annotate(f"Discontinuity at barrier\n(+{coupon_pct:g}% → {jump_to:g}%)",
                xy=(barrier_pct, jump_to / 2), xytext=(barrier_pct + 8, jump_to - 8),
                fontsize=9, color=NAVY, arrowprops=dict(arrowstyle="->", color=GREY))
    ax.text(strike_pct + 0.5, -0.78 * abs(min(jump_to, -10)) if jump_to < 0 else -5,
            initial_label, fontsize=8, color=GREY)
    ax.text(barrier_pct - 1, coupon_pct + 3, f"Barrier {barrier_pct:g}%",
            fontsize=8, color=GREY, ha="right")

    ax.set_xlabel("Underlying final level (% of initial)")
    ax.set_ylabel("Investor total return (%)")
    ax.set_title(f"{title} — {lens}", color=NAVY, fontsize=13, fontweight="bold", loc="left")
    ax.set_xlim(0, x_max)
    y_lo = min(-60, jump_to - 40)
    ax.set_ylim(y_lo, max(20, coupon_pct + 12))
    ax.legend(loc="lower right", frameon=False, fontsize=9)
    ax.grid(True, color=LIGHT, lw=1)
    ax.set_axisbelow(True)
    return _finish(fig, out_svg, preview)


# --------------------------------------------------------------------------- #
# 1b. Geared / airbag payoff (Airbag family) — buffered, leveraged downside
# --------------------------------------------------------------------------- #
def payoff_geared_note(
    out_svg: str | Path,
    *,
    barrier_pct: float,
    coupon_pct: float,
    gearing: float,
    title: str = "Payoff at Maturity",
    lens: str = LENS_INVESTOR,
    x_max: float = 140.0,
    preview: bool = True,
) -> str:
    """Airbag payoff: above barrier flat at +coupon; below barrier the redemption
    is Principal x (final / barrier), giving a geared loss line that is continuous
    at the barrier. `gearing` ~ initial/barrier is annotated."""
    _apply_style()
    fig, ax = plt.subplots(figsize=(7.2, 4.4))
    x_above = np.linspace(barrier_pct, x_max, 200)
    ax.plot(x_above, np.full_like(x_above, coupon_pct), color=GREEN, lw=2.6,
            label="Above barrier: par + coupon")
    x_below = np.linspace(0, barrier_pct, 200)
    y_below = (x_below / barrier_pct - 1.0) * 100 + coupon_pct
    ax.plot(x_below, y_below, color=ACCENT, lw=2.6,
            label="Below barrier: geared loss (final/barrier)")
    # reference: ungeared 1:1 from initial for comparison
    x_ref = np.linspace(0, barrier_pct, 200)
    ax.plot(x_ref, (x_ref - 100) + coupon_pct, color=GREY, lw=1.2, ls=(0, (4, 3)),
            label="(1:1 from initial, for comparison)")
    ax.axhline(0, color=SLATE, lw=0.8)
    ax.axvline(100, color=GREY, lw=0.8, ls=":")
    ax.axvline(barrier_pct, color=GREY, lw=0.8, ls=(0, (2, 2)))
    ax.text(barrier_pct - 1, coupon_pct + 4, f"Barrier {barrier_pct:g}%", fontsize=8,
            color=GREY, ha="right")
    ax.annotate(f"Gearing ~{gearing:g}x\n(loss vs barrier, not initial)",
                xy=(barrier_pct * 0.55, (0.55 - 1) * 100 + coupon_pct),
                xytext=(8, -32), fontsize=9, color=ACCENT,
                arrowprops=dict(arrowstyle="->", color=GREY))
    ax.set_xlabel("Underlying final level (% of initial)")
    ax.set_ylabel("Investor total return (%)")
    ax.set_title(f"{title} — {lens}", color=NAVY, fontsize=13, fontweight="bold", loc="left")
    ax.set_xlim(0, x_max)
    ax.set_ylim(min(-60, coupon_pct - 70), max(20, coupon_pct + 12))
    ax.legend(loc="lower right", frameon=False, fontsize=8.5)
    ax.grid(True, color=LIGHT, lw=1)
    ax.set_axisbelow(True)
    return _finish(fig, out_svg, preview)


# --------------------------------------------------------------------------- #
# 1c. Participation / bonus payoff (Bonus / Participation Note)
# --------------------------------------------------------------------------- #
def payoff_participation(
    out_svg: str | Path,
    *,
    bonus_pct: float,
    participation: float,
    barrier_pct: float,
    title: str = "Payoff at Maturity",
    lens: str = LENS_INVESTOR,
    x_max: float = 160.0,
    preview: bool = True,
) -> str:
    """Bonus / participation note: if the KO barrier stays intact, redemption =
    max(bonus_pct, 100 + participation*(final-100)); if breached, tracks the
    underlying (final-100). Two lines drawn: intact vs barrier-breached."""
    _apply_style()
    fig, ax = plt.subplots(figsize=(7.2, 4.4))
    x = np.linspace(0, x_max, 400)
    intact = np.maximum(bonus_pct, 100 + participation * (x - 100)) - 100
    breached = x - 100
    ax.plot(x, intact, color=GREEN, lw=2.6, label="Barrier intact: max(bonus, participation)")
    ax.plot(x, breached, color=ACCENT, lw=2.0, ls=(0, (5, 3)),
            label="Barrier breached: tracks underlying")
    ax.axhline(0, color=SLATE, lw=0.8)
    ax.axhline(bonus_pct - 100, color=GOLD, lw=1.0, ls=":")
    ax.text(2, bonus_pct - 100 + 2, f"Bonus floor {bonus_pct:g}%", fontsize=8, color=GOLD)
    ax.axvline(100, color=GREY, lw=0.8, ls=":")
    ax.axvline(barrier_pct, color=ACCENT, lw=1.2, ls=(0, (4, 3)))
    ax.text(barrier_pct + 1, ax.get_ylim()[1] if False else (bonus_pct - 100) + 14,
            f"KO {barrier_pct:g}%", fontsize=8, color=ACCENT)
    ax.set_xlabel("Underlying final level (% of initial)")
    ax.set_ylabel("Investor total return (%)")
    ax.set_title(f"{title} — {lens}", color=NAVY, fontsize=13, fontweight="bold", loc="left")
    ax.set_xlim(0, x_max)
    ax.set_ylim(-70, 60)
    ax.legend(loc="upper left", frameon=False, fontsize=8.5)
    ax.grid(True, color=LIGHT, lw=1)
    ax.set_axisbelow(True)
    return _finish(fig, out_svg, preview)


# --------------------------------------------------------------------------- #
# 1d. Digital / binary coupon payoff (Digital Coupon Note)
# --------------------------------------------------------------------------- #
def payoff_digital(
    out_svg: str | Path,
    *,
    strike_pct: float,
    coupon_pct: float,
    capital_barrier_pct: Optional[float] = None,
    title: str = "Payoff at Maturity",
    lens: str = LENS_INVESTOR,
    x_max: float = 140.0,
    preview: bool = True,
) -> str:
    """All-or-nothing coupon: return = +coupon if final >= digital strike, else 0;
    below an optional capital barrier the principal is reduced 1:1. Two step
    discontinuities (the digital strike, and the capital barrier if given)."""
    _apply_style()
    fig, ax = plt.subplots(figsize=(7.2, 4.4))
    cb = capital_barrier_pct if capital_barrier_pct is not None else 0
    # above strike: coupon
    xa = np.linspace(strike_pct, x_max, 150)
    ax.plot(xa, np.full_like(xa, coupon_pct), color=GREEN, lw=2.6, label="≥ digital strike: + coupon")
    # between capital barrier and strike: zero (par, no coupon)
    xm = np.linspace(cb, strike_pct, 150)
    ax.plot(xm, np.zeros_like(xm), color=GOLD, lw=2.6, label="par returned, no coupon")
    # below capital barrier: capital loss
    if capital_barrier_pct is not None:
        xb = np.linspace(0, cb, 150)
        ax.plot(xb, (xb - 100), color=ACCENT, lw=2.6, label="< capital barrier: principal loss")
        ax.plot([cb, cb], [(cb - 100), 0], color=GREY, lw=1.2, ls=(0, (3, 3)))
        ax.text(cb - 1, 2, f"Cap. barrier {cb:g}%", fontsize=8, color=GREY, ha="right")
    # digital step marker
    ax.plot([strike_pct, strike_pct], [0, coupon_pct], color=GREY, lw=1.2, ls=(0, (3, 3)))
    ax.text(strike_pct + 1, coupon_pct - 2, f"Digital strike {strike_pct:g}%", fontsize=8, color=GREEN)
    ax.axhline(0, color=SLATE, lw=0.8)
    ax.axvline(100, color=GREY, lw=0.8, ls=":")
    ax.set_xlabel("Underlying final level (% of initial)")
    ax.set_ylabel("Investor total return (%)")
    ax.set_title(f"{title} — {lens}", color=NAVY, fontsize=13, fontweight="bold", loc="left")
    ax.set_xlim(0, x_max)
    ax.set_ylim(min(-55, coupon_pct - 65), max(18, coupon_pct + 8))
    ax.legend(loc="lower right", frameon=False, fontsize=8.5)
    ax.grid(True, color=LIGHT, lw=1)
    ax.set_axisbelow(True)
    return _finish(fig, out_svg, preview)


# --------------------------------------------------------------------------- #
# 1e. Principal-protected payoff (PPN) — floor + participation
# --------------------------------------------------------------------------- #
def payoff_ppn(
    out_svg: str | Path,
    *,
    floor_pct: float = 100.0,
    participation: float = 1.0,
    cap_pct: Optional[float] = None,
    title: str = "Payoff at Maturity",
    lens: str = LENS_INVESTOR,
    x_max: float = 180.0,
    preview: bool = True,
) -> str:
    """PPN: capital floor at floor_pct (return >= floor-100), plus participation in
    upside above the initial level, optionally capped."""
    _apply_style()
    fig, ax = plt.subplots(figsize=(7.2, 4.4))
    x = np.linspace(0, x_max, 400)
    base = floor_pct - 100
    up = participation * np.maximum(0.0, x - 100)
    ret = base + up
    if cap_pct is not None:
        ret = np.minimum(ret, cap_pct)
    ax.plot(x, ret, color=GREEN, lw=2.6, label=f"PPN ({participation*100:g}% participation)")
    ax.plot(x, x - 100, color=GREY, lw=1.2, ls=(0, (4, 3)), label="direct equity (1:1)")
    ax.axhline(0, color=SLATE, lw=0.8)
    ax.axhline(base, color=GOLD, lw=1.0, ls=":")
    ax.text(2, base + 1.5, f"Capital floor {floor_pct:g}%", fontsize=8, color=GOLD)
    ax.axvline(100, color=GREY, lw=0.8, ls=":")
    if cap_pct is not None:
        ax.text(x_max - 2, cap_pct + 1, f"Cap +{cap_pct:g}%", fontsize=8, color=ACCENT, ha="right")
    ax.set_xlabel("Underlying final level (% of initial)")
    ax.set_ylabel("Investor total return (%)")
    ax.set_title(f"{title} — {lens}", color=NAVY, fontsize=13, fontweight="bold", loc="left")
    ax.set_xlim(0, x_max)
    ax.set_ylim(-60, max(40, (cap_pct or participation * (x_max - 100)) + 10))
    ax.legend(loc="upper left", frameon=False, fontsize=8.5)
    ax.grid(True, color=LIGHT, lw=1)
    ax.set_axisbelow(True)
    return _finish(fig, out_svg, preview)


# --------------------------------------------------------------------------- #
# 1f. Warrant / Turbo payoff — leveraged directional, with knock-out
# --------------------------------------------------------------------------- #
def payoff_warrant(
    out_svg: str | Path,
    *,
    option: str = "call",
    strike_pct: float = 100.0,
    knockout_pct: Optional[float] = None,
    leverage: float = 1.0,
    title: str = "Payoff at Maturity",
    lens: str = LENS_INVESTOR,
    x_max: float = 130.0,
    x_min: float = 70.0,
    preview: bool = True,
) -> str:
    """Leveraged warrant/turbo: return on premium ≈ leverage × (underlying move).
    A turbo knocks out to −100% if it touches the knock-out level."""
    _apply_style()
    fig, ax = plt.subplots(figsize=(7.2, 4.4))
    x = np.linspace(x_min, x_max, 400)
    sgn = 1.0 if option == "call" else -1.0
    ret = np.clip(leverage * sgn * (x - 100), -100, 150)
    if knockout_pct is not None:
        if option == "call":
            ret = np.where(x <= knockout_pct, -100, ret)
        else:
            ret = np.where(x >= knockout_pct, -100, ret)
    ax.plot(x, ret, color=NAVY, lw=2.6, label=f"{option} warrant ({leverage:g}x leverage)")
    ax.axhline(0, color=SLATE, lw=0.8)
    ax.axhline(-100, color=ACCENT, lw=1.0, ls=":")
    ax.text(x_min + 1, -94, "Total loss (−100%)", fontsize=8, color=ACCENT)
    ax.axvline(100, color=GREY, lw=0.8, ls=":")
    if knockout_pct is not None:
        ax.axvline(knockout_pct, color=ACCENT, lw=1.2, ls=(0, (4, 3)))
        ax.text(knockout_pct, 120, f"Knock-out {knockout_pct:g}%", fontsize=8, color=ACCENT, ha="center")
    ax.set_xlabel("Underlying level (% of initial)")
    ax.set_ylabel("Warrant return (% of premium)")
    ax.set_title(f"{title} — {lens}", color=NAVY, fontsize=13, fontweight="bold", loc="left")
    ax.set_xlim(x_min, x_max)
    ax.set_ylim(-115, 160)
    ax.legend(loc="upper left", frameon=False, fontsize=8.5)
    ax.grid(True, color=LIGHT, lw=1)
    ax.set_axisbelow(True)
    return _finish(fig, out_svg, preview)


# --------------------------------------------------------------------------- #
# 1g. Cashflow legs (swaps) — two-leg bilateral exchange
# --------------------------------------------------------------------------- #
def swap_legs(
    out_svg: str | Path,
    *,
    client_pays: str,
    client_receives: str,
    client_label: str = "Client",
    desk_label: str = "Desk / Bank",
    title: str = "Cashflow Legs",
    lens: str = LENS_INVESTOR,
    preview: bool = True,
) -> str:
    """Schematic two-leg swap: Client and Desk boxes with a 'client pays' arrow
    one way and a 'client receives' arrow the other."""
    W, H = 820, 300
    s = []
    s.append(f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {W} {H}" '
             f'font-family="DejaVu Sans, Arial, sans-serif">')
    s.append(f'<rect x="0" y="0" width="{W}" height="{H}" fill="white"/>')
    s.append(f'<text x="24" y="36" font-size="16" font-weight="bold" fill="{NAVY}">'
             f'{_esc(title)} — {_esc(lens)}</text>')
    # two party boxes
    s.append(f'<rect x="70" y="110" width="200" height="80" rx="10" fill="{NAVY}"/>')
    s.append(f'<text x="170" y="156" font-size="15" fill="white" text-anchor="middle" font-weight="bold">{_esc(client_label)}</text>')
    s.append(f'<rect x="550" y="110" width="200" height="80" rx="10" fill="{SLATE}"/>')
    s.append(f'<text x="650" y="156" font-size="15" fill="white" text-anchor="middle" font-weight="bold">{_esc(desk_label)}</text>')
    s.append(f'<defs><marker id="ar" markerWidth="9" markerHeight="9" refX="7" refY="3" orient="auto">'
             f'<path d="M0,0 L7,3 L0,6 Z" fill="{ACCENT}"/></marker>'
             f'<marker id="ag" markerWidth="9" markerHeight="9" refX="7" refY="3" orient="auto">'
             f'<path d="M0,0 L7,3 L0,6 Z" fill="{GREEN}"/></marker></defs>')
    # client pays -> desk (top arrow)
    s.append(f'<line x1="270" y1="135" x2="548" y2="135" stroke="{ACCENT}" stroke-width="2.4" marker-end="url(#ar)"/>')
    s.append(f'<text x="409" y="126" font-size="12" fill="{ACCENT}" text-anchor="middle">Client pays: {_esc(client_pays)}</text>')
    # desk pays -> client (bottom arrow)
    s.append(f'<line x1="548" y1="168" x2="272" y2="168" stroke="{GREEN}" stroke-width="2.4" marker-end="url(#ag)"/>')
    s.append(f'<text x="409" y="186" font-size="12" fill="{GREEN}" text-anchor="middle">Client receives: {_esc(client_receives)}</text>')
    s.append(f'<text x="{W//2}" y="250" font-size="11" fill="{GREY}" text-anchor="middle">'
             f'Bilateral OTC swap — two legs exchanged on each reset; only the NET is paid.</text>')
    s.append('</svg>')
    out_svg = Path(out_svg); out_svg.parent.mkdir(parents=True, exist_ok=True)
    out_svg.write_text("\n".join(s), encoding="utf-8")
    if preview:
        render_png(out_svg)
    return str(out_svg)


# --------------------------------------------------------------------------- #
# 1h. Variance swap payoff vs realized volatility
# --------------------------------------------------------------------------- #
def payoff_varswap(
    out_svg: str | Path,
    *,
    strike_vol: float,
    title: str = "Variance Swap Payoff",
    lens: str = LENS_INVESTOR,
    vol_max: float = 45.0,
    preview: bool = True,
) -> str:
    """Long-variance payoff in variance points: (realized_vol^2 - strike_vol^2),
    shown vs realized vol — convex, zero at the strike."""
    _apply_style()
    fig, ax = plt.subplots(figsize=(7.2, 4.4))
    v = np.linspace(0, vol_max, 400)
    pnl = (v ** 2 - strike_vol ** 2) / 100.0  # scaled variance points
    ax.plot(v, pnl, color=NAVY, lw=2.6, label="Long variance: realized² − strike²")
    ax.axhline(0, color=SLATE, lw=0.8)
    ax.axvline(strike_vol, color=ACCENT, lw=1.4, ls=(0, (4, 3)))
    ax.text(strike_vol + 0.5, ax.get_ylim()[1] * 0.1 if False else 0.3,
            f"Strike vol {strike_vol:g}%", fontsize=9, color=ACCENT)
    ax.fill_between(v, pnl, where=(v > strike_vol), color=GREEN, alpha=0.12)
    ax.fill_between(v, pnl, where=(v <= strike_vol), color=ACCENT, alpha=0.10)
    ax.set_xlabel("Realized volatility (%)")
    ax.set_ylabel("P&L (variance points, ×notional)")
    ax.set_title(f"{title} — {lens}", color=NAVY, fontsize=13, fontweight="bold", loc="left")
    ax.set_xlim(0, vol_max)
    ax.grid(True, color=LIGHT, lw=1)
    ax.set_axisbelow(True)
    ax.legend(loc="upper left", frameon=False, fontsize=9)
    return _finish(fig, out_svg, preview)


# --------------------------------------------------------------------------- #
# 1i. Digital coupon vs reference RATE (Digital Cap-Floor Note)
# --------------------------------------------------------------------------- #
def payoff_digital_rate(
    out_svg: str | Path,
    *,
    strike_rate: float,
    high_coupon: float,
    low_coupon: float = 0.0,
    high_when_below: bool = True,
    title: str = "Digital Coupon vs Reference Rate",
    lens: str = LENS_INVESTOR,
    rate_max: Optional[float] = None,
    preview: bool = True,
) -> str:
    """Step coupon: pays high_coupon on one side of the strike rate, low_coupon on
    the other. high_when_below=True → high coupon when rate < strike (cap-style)."""
    _apply_style()
    rate_max = rate_max or strike_rate * 2.0
    fig, ax = plt.subplots(figsize=(7.2, 4.4))
    lo = np.linspace(0, strike_rate, 120)
    hi = np.linspace(strike_rate, rate_max, 120)
    yl = high_coupon if high_when_below else low_coupon
    yh = low_coupon if high_when_below else high_coupon
    ax.plot(lo, np.full_like(lo, yl), color=GREEN, lw=2.6)
    ax.plot(hi, np.full_like(hi, yh), color=ACCENT, lw=2.6)
    ax.plot([strike_rate, strike_rate], [low_coupon, high_coupon], color=GREY, lw=1.3, ls=(0, (3, 3)))
    ax.text(strike_rate, high_coupon + (high_coupon - low_coupon) * 0.06 + 0.02,
            f"Strike {strike_rate:g}%", fontsize=9, color=NAVY, ha="center")
    ax.text(strike_rate * 0.4, yl + 0.03, f"{yl:g}% coupon", fontsize=9, color=GREEN, ha="center")
    ax.text((strike_rate + rate_max) / 2, yh + 0.03, f"{yh:g}% coupon", fontsize=9, color=ACCENT, ha="center")
    ax.axhline(0, color=SLATE, lw=0.8)
    ax.set_xlabel("Reference rate (%)")
    ax.set_ylabel("Coupon paid (%)")
    ax.set_title(f"{title} — {lens}", color=NAVY, fontsize=13, fontweight="bold", loc="left")
    ax.set_xlim(0, rate_max)
    ax.set_ylim(min(low_coupon, 0) - 0.1, high_coupon + (high_coupon - low_coupon) * 0.3 + 0.15)
    ax.grid(True, color=LIGHT, lw=1)
    ax.set_axisbelow(True)
    return _finish(fig, out_svg, preview)


# --------------------------------------------------------------------------- #
# 1j. Range-accrual coupon vs days-in-range (NCRA / CRA SRT)
# --------------------------------------------------------------------------- #
def payoff_range_accrual(
    out_svg: str | Path,
    *,
    max_coupon: float,
    title: str = "Coupon vs Days-in-Range",
    lens: str = LENS_INVESTOR,
    preview: bool = True,
) -> str:
    """Range-accrual coupon = max_coupon × (days in range / total days). Linear."""
    _apply_style()
    fig, ax = plt.subplots(figsize=(7.2, 4.4))
    d = np.linspace(0, 100, 200)
    ax.plot(d, max_coupon * d / 100.0, color=NAVY, lw=2.6)
    ax.fill_between(d, max_coupon * d / 100.0, color=SLATE, alpha=0.12)
    ax.scatter([100], [max_coupon], color=GREEN, zorder=5, s=30)
    ax.text(98, max_coupon * 0.92, f"Max {max_coupon:g}%\n(all days in range)", fontsize=9,
            color=GREEN, ha="right")
    ax.text(3, max_coupon * 0.06, "0% (all days out of range)", fontsize=9, color=ACCENT)
    ax.axhline(0, color=SLATE, lw=0.8)
    ax.set_xlabel("Days the reference rate is inside the range (%)")
    ax.set_ylabel("Coupon earned (%)")
    ax.set_title(f"{title} — {lens}", color=NAVY, fontsize=13, fontweight="bold", loc="left")
    ax.set_xlim(0, 100)
    ax.set_ylim(0, max_coupon * 1.15)
    ax.grid(True, color=LIGHT, lw=1)
    ax.set_axisbelow(True)
    return _finish(fig, out_svg, preview)


# --------------------------------------------------------------------------- #
# 1k. Steepener coupon vs curve slope (STEG family)
# --------------------------------------------------------------------------- #
def payoff_steepener(
    out_svg: str | Path,
    *,
    leverage: float,
    floor_coupon: float = 0.0,
    cap_coupon: Optional[float] = None,
    strike_spread: float = 0.0,
    title: str = "Steepener Coupon vs Curve Slope",
    lens: str = LENS_INVESTOR,
    slope_min: float = -50.0,
    slope_max: float = 300.0,
    preview: bool = True,
) -> str:
    """Coupon = clip( leverage × max(0, (slope − strike)/100), floor, cap ), where
    slope is the long−short CMS spread in bp. Long-slope payoff with a kink at the
    strike, a floor, and an optional cap."""
    _apply_style()
    fig, ax = plt.subplots(figsize=(7.2, 4.4))
    x = np.linspace(slope_min, slope_max, 400)
    c = leverage * np.maximum(0.0, (x - strike_spread) / 100.0)
    c = np.maximum(c, floor_coupon)
    if cap_coupon is not None:
        c = np.minimum(c, cap_coupon)
    ax.plot(x, c, color=NAVY, lw=2.6, label=f"Coupon = {leverage:g} × max(0, slope − {strike_spread:g}bp)")
    ax.fill_between(x, c, floor_coupon, color=SLATE, alpha=0.12)
    ax.axvline(strike_spread, color=GREY, lw=0.9, ls=":")
    ax.text(strike_spread + 4, floor_coupon + 0.3, f"Kink @ {strike_spread:g}bp", fontsize=8, color=GREY)
    ax.axvline(0, color=SLATE, lw=0.8)
    if cap_coupon is not None:
        ax.axhline(cap_coupon, color=ACCENT, lw=1.0, ls=(0, (4, 3)))
        ax.text(slope_max - 4, cap_coupon + 0.2, f"Cap {cap_coupon:g}%", fontsize=8, color=ACCENT, ha="right")
    ax.axhline(floor_coupon, color=GOLD, lw=1.0, ls=":")
    ax.text(slope_min + 4, floor_coupon + 0.2, f"Floor {floor_coupon:g}%", fontsize=8, color=GOLD)
    ax.text(slope_min + 10, (cap_coupon or 12) * 0.5, "Flatter ←", fontsize=9, color=GREY)
    ax.text(slope_max - 10, (cap_coupon or 12) * 0.5, "→ Steeper", fontsize=9, color=GREY, ha="right")
    ax.set_xlabel("Curve slope: long-tenor − short-tenor CMS (bp)")
    ax.set_ylabel("Coupon paid (%)")
    ax.set_title(f"{title} — {lens}", color=NAVY, fontsize=13, fontweight="bold", loc="left")
    ax.set_xlim(slope_min, slope_max)
    ax.set_ylim(min(floor_coupon - 0.5, -0.5), (cap_coupon or leverage * (slope_max - strike_spread) / 100.0) * 1.15 + 0.5)
    ax.grid(True, color=LIGHT, lw=1)
    ax.set_axisbelow(True)
    ax.legend(loc="upper left", frameon=False, fontsize=8.5)
    return _finish(fig, out_svg, preview)


# (linter rules live in governance/linter/semantic_linter.py; this is the diagram lib)
# --------------------------------------------------------------------------- #
# 1l. Correlation sensitivity (FTD / NTD / CDO tranche)
# --------------------------------------------------------------------------- #
def payoff_correlation(
    out_svg: str | Path,
    *,
    direction: str,
    title: str = "Position Risk vs Default Correlation",
    lens: str = LENS_INVESTOR,
    preview: bool = True,
) -> str:
    """Position risk / expected loss vs default correlation ρ.
    direction='long'  → LONG correlation: risk FALLS as ρ rises (FTD, equity tranche)
    direction='short' → SHORT correlation: risk RISES as ρ rises (NTD N≥2, senior)
    direction='neutral' → sign-ambiguous (mezzanine): non-monotone."""
    _apply_style()
    rho = np.linspace(0, 1, 200)
    fig, ax = plt.subplots(figsize=(7.2, 4.4))
    d = direction.lower()
    if d == "long":
        y = 0.15 + 0.80 * (1 - rho)
        lbl = "LONG correlation — risk falls as ρ rises"
        col = GREEN
    elif d == "short":
        y = 0.15 + 0.80 * rho
        lbl = "SHORT correlation — risk rises as ρ rises"
        col = ACCENT
    else:
        y = 0.45 + 0.35 * np.sin(np.pi * rho)  # gentle hump
        lbl = "Sign-ambiguous (mezzanine) — depends on attachment"
        col = GOLD
    ax.plot(rho, y, color=col, lw=2.8, label=lbl)
    ax.fill_between(rho, y, color=col, alpha=0.10)
    ax.annotate("", xy=(0.92, y[int(0.92 * 199)]), xytext=(0.62, y[int(0.62 * 199)]),
                arrowprops=dict(arrowstyle="->", color=col, lw=1.6))
    ax.set_xlabel("Default correlation  ρ")
    ax.set_ylabel("Position risk / expected loss (relative)")
    ax.set_title(f"{title} — {lens}", color=NAVY, fontsize=13, fontweight="bold", loc="left")
    ax.set_xlim(0, 1)
    ax.set_ylim(0, 1.1)
    ax.set_xticks([0, 0.25, 0.5, 0.75, 1.0])
    ax.grid(True, color=LIGHT, lw=1)
    ax.set_axisbelow(True)
    ax.legend(loc="upper center", frameon=False, fontsize=9)
    return _finish(fig, out_svg, preview)


# --------------------------------------------------------------------------- #
# 2. Desk gamma / hedge profile (Bank Lens — Desk Economics)
# --------------------------------------------------------------------------- #
def desk_gamma_profile(
    out_svg: str | Path,
    *,
    barrier_pct: float,
    title: str = "Desk Position & Hedge",
    note: str = "Desk is LONG the embedded put (mirror of investor's short put);\ndelta-hedges by trading the underlying.",
    barrier_note: str = "gamma spikes,\nhedging expensive",
    preview: bool = True,
) -> str:
    """Stylised desk gamma vs spot for a long barrier-option position.

    The curve shape is conceptual (gamma concentrates near the barrier); the
    barrier LEVEL is calibrated to the chapter. Annotated for the 1st-line reader.
    """
    _apply_style()
    fig, ax = plt.subplots(figsize=(7.2, 4.4))
    s = np.linspace(40, 140, 400)
    gamma = (0.25 * np.exp(-((s - barrier_pct) ** 2) / (2 * 4.5 ** 2))
             + 0.02 * np.exp(-((s - 100) ** 2) / (2 * 22 ** 2)))
    ax.fill_between(s, gamma, color=SLATE, alpha=0.18)
    ax.plot(s, gamma, color=NAVY, lw=2.6)
    ax.axvline(barrier_pct, color=ACCENT, lw=1.4, ls=(0, (4, 3)))
    ax.axvline(100, color=GREY, lw=0.8, ls=":")
    ax.text(101, 0.02, "Initial", fontsize=8, color=GREY)
    ax.annotate(f"Barrier {barrier_pct:g}% — {barrier_note}",
                xy=(barrier_pct + 2, 0.22), xytext=(barrier_pct + 14, 0.20),
                fontsize=9, color=ACCENT, arrowprops=dict(arrowstyle="->", color=ACCENT, lw=1))
    ax.set_xlabel("Underlying spot (% of initial)")
    ax.set_ylabel("Desk gamma (long option)")
    ax.set_title(f"{title} — {LENS_DESK}", color=NAVY, fontsize=13, fontweight="bold", loc="left")
    ax.set_xlim(40, 140)
    ax.set_ylim(0, 0.30)
    ax.grid(True, color=LIGHT, lw=1)
    ax.set_axisbelow(True)
    ax.text(0.985, 0.93, note, transform=ax.transAxes, fontsize=8.5, color=SLATE,
            va="top", ha="right",
            bbox=dict(boxstyle="round,pad=0.4", fc="white", ec=SLATE, lw=0.8))
    return _finish(fig, out_svg, preview)


# --------------------------------------------------------------------------- #
# 3. Reconciliation flow swimlane (Bank Lens — Controls & 2LoD)
# --------------------------------------------------------------------------- #
def reconciliation_flow(
    out_svg: str | Path,
    *,
    product: str,
    bor_system: str,
    risk_system: str,
    points: Sequence[tuple[str, str]],
    flagged_index: int = 0,
    flag_tag: str = "most common break",
    consequence: str = "a break here crystallises the wrong redemption / client payout",
    title: Optional[str] = None,
    preview: bool = True,
) -> str:
    """Hand-built SVG swimlane: book-of-record <-> risk system reconciliation.

    `points` is a list of (name, description). `flagged_index` highlights the
    most common break. Fully parameterized per product.
    """
    title = title or f"{product} Reconciliation Flow — {LENS_CONTROLS}"
    n = len(points)
    W = 880
    H = 150 + n * 40 + 70
    y0 = 126
    rh = 40
    s = []
    s.append(f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {W} {H}" '
             f'font-family="DejaVu Sans, Arial, sans-serif">')
    s.append(f'<rect x="0" y="0" width="{W}" height="{H}" fill="white"/>')
    s.append(f'<text x="24" y="34" font-size="17" font-weight="bold" fill="{NAVY}">{_esc(title)}</text>')
    s.append(f'<text x="24" y="54" font-size="11" fill="{SLATE}">'
             f'{_esc("Points that must agree across systems before settlement. Highlighted row = most common break.")}</text>')
    # headers
    s.append(f'<rect x="60" y="74" width="190" height="34" rx="6" fill="{NAVY}"/>')
    s.append(f'<text x="155" y="96" font-size="12" fill="white" text-anchor="middle" font-weight="bold">{_esc(bor_system)} · Book of Record</text>')
    s.append(f'<rect x="630" y="74" width="190" height="34" rx="6" fill="{SLATE}"/>')
    s.append(f'<text x="725" y="96" font-size="12" fill="white" text-anchor="middle" font-weight="bold">{_esc(risk_system)} · Risk</text>')
    s.append(f'<text x="440" y="96" font-size="12" fill="{NAVY}" text-anchor="middle" font-weight="bold">must reconcile</text>')
    lane_bottom = y0 + n * rh + 4
    s.append(f'<line x1="155" y1="112" x2="155" y2="{lane_bottom}" stroke="{GREY}" stroke-width="1" stroke-dasharray="3,3"/>')
    s.append(f'<line x1="725" y1="112" x2="725" y2="{lane_bottom}" stroke="{GREY}" stroke-width="1" stroke-dasharray="3,3"/>')
    for i, (name, desc) in enumerate(points):
        y = y0 + i * rh
        flag = (i == flagged_index)
        fill = "#fbe7e2" if flag else PALE
        ec = ACCENT if flag else SLATE
        s.append(f'<line x1="155" y1="{y+16}" x2="725" y2="{y+16}" stroke="{ec}" stroke-width="{1.6 if flag else 1}"/>')
        s.append(f'<circle cx="155" cy="{y+16}" r="4" fill="{NAVY}"/>')
        s.append(f'<circle cx="725" cy="{y+16}" r="4" fill="{SLATE}"/>')
        s.append(f'<rect x="280" y="{y}" width="320" height="32" rx="6" fill="{fill}" stroke="{ec}" stroke-width="{1.5 if flag else 1}"/>')
        s.append(f'<text x="292" y="{y+14}" font-size="11.5" font-weight="bold" fill="{NAVY}">{_esc(f"{i+1}. {name}")}</text>')
        s.append(f'<text x="292" y="{y+27}" font-size="9" fill="{SLATE}">{_esc(desc)}</text>')
        if flag:
            s.append(f'<rect x="606" y="{y+3}" width="150" height="26" rx="13" fill="{ACCENT}"/>')
            s.append(f'<text x="681" y="{y+20}" font-size="9" fill="white" text-anchor="middle" font-weight="bold">{_esc(flag_tag)}</text>')
    s.append(f'<defs><marker id="a" markerWidth="8" markerHeight="8" refX="6" refY="3" orient="auto">'
             f'<path d="M0,0 L6,3 L0,6 Z" fill="{GREY}"/></marker></defs>')
    s.append(f'<line x1="440" y1="{lane_bottom}" x2="440" y2="{lane_bottom+18}" stroke="{GREY}" stroke-width="1.4" marker-end="url(#a)"/>')
    s.append(f'<rect x="280" y="{lane_bottom+18}" width="320" height="40" rx="6" fill="{NAVY}"/>')
    s.append(f'<text x="440" y="{lane_bottom+35}" font-size="11.5" fill="white" text-anchor="middle" font-weight="bold">Downstream · Settlement</text>')
    s.append(f'<text x="440" y="{lane_bottom+50}" font-size="9" fill="{LIGHT}" text-anchor="middle">{_esc(consequence)}</text>')
    s.append('</svg>')
    out_svg = Path(out_svg)
    out_svg.parent.mkdir(parents=True, exist_ok=True)
    out_svg.write_text("\n".join(s), encoding="utf-8")
    if preview:
        render_png(out_svg)
    return str(out_svg)


# --------------------------------------------------------------------------- #
# 4. Coupon decomposition waterfall (Bank Lens — Desk Economics)
# --------------------------------------------------------------------------- #
def coupon_waterfall(
    out_svg: str | Path,
    *,
    components: Sequence[tuple[str, float]],
    net_label: str = "Net coupon",
    title: str = "Coupon Decomposition",
    lens: str = LENS_DESK,
    preview: bool = True,
) -> str:
    """Waterfall of how a coupon is built (bond interest + premium − FTP − margin).

    `components` is a list of (label, signed_value_pct). The net (sum) is drawn
    as a final total bar. Calibrate with the chapter's actual decomposition.
    """
    _apply_style()
    fig, ax = plt.subplots(figsize=(7.6, 4.4))
    running = 0.0
    xs = []
    for i, (label, val) in enumerate(components):
        color = GREEN if val >= 0 else ACCENT
        bottom = running if val >= 0 else running + val
        ax.bar(i, abs(val), bottom=bottom, color=color, width=0.62, edgecolor="white")
        ax.text(i, bottom + abs(val) + 0.12, f"{val:+.1f}", ha="center", fontsize=9, color=NAVY)
        running += val
        xs.append(label)
    net_i = len(components)
    ax.bar(net_i, running, color=NAVY, width=0.62, edgecolor="white")
    ax.text(net_i, running + 0.12, f"{running:.1f}", ha="center", fontsize=9, fontweight="bold", color=NAVY)
    xs.append(net_label)
    ax.axhline(0, color=SLATE, lw=0.8)
    ax.set_xticks(range(len(xs)))
    ax.set_xticklabels(xs, fontsize=9, rotation=12, ha="right")
    ax.set_ylabel("Contribution to coupon (%)")
    ax.set_title(f"{title} — {lens}", color=NAVY, fontsize=13, fontweight="bold", loc="left")
    ax.grid(True, axis="y", color=LIGHT, lw=1)
    ax.set_axisbelow(True)
    return _finish(fig, out_svg, preview)


# --------------------------------------------------------------------------- #
# 5. Risk heatmap (Investor Lens)
# --------------------------------------------------------------------------- #
_LEVEL = {"LOW": (GREEN, 1), "MEDIUM": (GOLD, 2), "MEDIUM-HIGH": ("#d77a3a", 2.6),
          "HIGH": (ACCENT, 3)}


def risk_heatmap(
    out_svg: str | Path,
    *,
    rows: Sequence[tuple[str, str]],
    title: str = "Risk Heatmap",
    lens: str = LENS_INVESTOR,
    preview: bool = True,
) -> str:
    """Horizontal risk grid: each row (risk_name, level) where level in
    LOW / MEDIUM / MEDIUM-HIGH / HIGH. Calibrate with the chapter's risk table."""
    _apply_style()
    fig, ax = plt.subplots(figsize=(7.2, 0.6 * len(rows) + 1.2))
    for i, (name, level) in enumerate(rows):
        color, mag = _LEVEL.get(level.upper(), (GREY, 1.5))
        y = len(rows) - 1 - i
        ax.barh(y, mag, color=color, height=0.62)
        ax.text(0.04, y, name, va="center", ha="left", fontsize=10, color="white", fontweight="bold")
        ax.text(mag + 0.05, y, level, va="center", fontsize=9, color=NAVY)
    ax.set_xlim(0, 3.6)
    ax.set_ylim(-0.6, len(rows) - 0.4)
    ax.set_yticks([])
    ax.set_xticks([1, 2, 3])
    ax.set_xticklabels(["Low", "Medium", "High"], fontsize=9)
    ax.set_title(f"{title} — {lens}", color=NAVY, fontsize=13, fontweight="bold", loc="left")
    for sp in ("top", "right", "left"):
        ax.spines[sp].set_visible(False)
    ax.grid(True, axis="x", color=LIGHT, lw=1)
    ax.set_axisbelow(True)
    return _finish(fig, out_svg, preview)


# --------------------------------------------------------------------------- #
# 6. Lifecycle timeline (any lens)
# --------------------------------------------------------------------------- #
def lifecycle_timeline(
    out_svg: str | Path,
    *,
    stages: Sequence[tuple[str, str]],
    title: str = "Lifecycle",
    lens: str = LENS_CONTROLS,
    preview: bool = True,
) -> str:
    """Horizontal timeline. `stages` = list of (label, sub-note)."""
    _apply_style()
    n = len(stages)
    fig, ax = plt.subplots(figsize=(min(2.0 * n, 10), 2.8))
    ax.plot([0, n - 1], [0, 0], color=SLATE, lw=2, zorder=1)
    for i, (label, sub) in enumerate(stages):
        ax.scatter([i], [0], s=120, color=NAVY, zorder=3)
        va = "bottom" if i % 2 == 0 else "top"
        off = 0.22 if i % 2 == 0 else -0.22
        ax.text(i, off, label, ha="center", va=va, fontsize=10, fontweight="bold", color=NAVY)
        ax.text(i, off + (0.16 if i % 2 == 0 else -0.16), sub, ha="center", va=va, fontsize=8, color=SLATE)
    ax.set_xlim(-0.6, n - 0.4)
    ax.set_ylim(-1, 1)
    ax.axis("off")
    ax.set_title(f"{title} — {lens}", color=NAVY, fontsize=13, fontweight="bold", loc="left")
    return _finish(fig, out_svg, preview)


# Standard RC reconciliation points — reused as the default checklist seed.
RECON_POINTS_BARRIER_NOTE = [
    ("Trade economics", "notional, strike, barrier level & convention"),
    ("Observation type", "European vs American calendar"),
    ("Fixings", "initial & final source = termsheet"),
    ("Knock-in capture", "KI flag consistent across systems"),
    ("Coupon lifecycle", "schedule, day-count, survival after KI"),
    ("Corporate actions", "strike/barrier adj. for splits, divs"),
    ("P&L attribution", "coupon accrual + option MTM = total"),
    ("Settlement", "cash vs physical; shares = notional/strike"),
]


if __name__ == "__main__":
    # Smoke test: render one of each into ./_smoke
    d = Path(__file__).parent / "_smoke"
    payoff_barrier_note(d / "payoff.svg", barrier_pct=70, coupon_pct=8)
    desk_gamma_profile(d / "gamma.svg", barrier_pct=70)
    reconciliation_flow(d / "recon.svg", product="RC", bor_system="NEMO",
                        risk_system="Sophis", points=RECON_POINTS_BARRIER_NOTE)
    coupon_waterfall(d / "waterfall.svg",
                     components=[("Bond interest", 2.0), ("Put premium", 7.5),
                                 ("FTP", -0.5), ("Desk margin", -1.0)])
    risk_heatmap(d / "risk.svg", rows=[("Barrier breach", "HIGH"), ("Gap risk", "HIGH"),
                                       ("Issuer credit", "MEDIUM"), ("Illiquidity", "MEDIUM")])
    lifecycle_timeline(d / "lifecycle.svg",
                       stages=[("Trade", "terms agreed"), ("Issue", "note at par"),
                               ("Coupons", "scheduled"), ("Maturity", "redeem/settle")])
    print("smoke diagrams written to", d)
