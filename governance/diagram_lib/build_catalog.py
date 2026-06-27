#!/usr/bin/env python3
"""Build a self-contained HTML visual catalog of every generated diagram,
grouped by product (5.x.y order) and lens. Run from the repo root:

    python3 governance/diagram_lib/build_catalog.py

Writes governance/diagram_lib/visual_catalog.html (SVGs inlined, no deps).
"""
import os, re, html, glob

ASSETS = "assets"
META = {
    "ppn": ("5.1.1", "Principal Protected Note"), "rc": ("5.1.2", "Reverse Convertible"),
    "phoenix": ("5.1.3", "Phoenix Autocallable"), "drc": ("5.1.4", "Discounted Reverse Convertible"),
    "kodrc": ("5.1.5", "Knock-Out DRC"), "crc": ("5.1.6", "Callable RC"),
    "airbag": ("5.1.7", "Airbag / Leveraged RC"), "bonus": ("5.1.8", "Bonus / Participation Note"),
    "fcn": ("5.1.9", "Fixed Coupon Note"), "cra": ("5.1.10", "Callable Range Accrual ELN"),
    "icn": ("5.1.11", "Issuer Callable Note"), "digital": ("5.1.12", "Digital Coupon Note"),
    "booster": ("5.1.13", "Booster Note"), "digitalki": ("5.1.14", "Digital Coupon Knock-In Put"),
    "warrant": ("5.1.15", "Warrant / Turbo"), "irs": ("5.2.1", "Interest Rate Swap"),
    "trs": ("5.2.2", "Total Return Swap"), "eqswap": ("5.2.3", "Equity Swap"),
    "varswap": ("5.2.4", "Variance Swap"), "cds": ("5.2.5", "Credit Default Swap"),
    "ccyswap": ("5.2.6", "Cross-Currency Swap"), "commodswap": ("5.2.7", "Commodity Swap"),
    "vlsp": ("5.2.8", "Vanilla Swap"), "ircallable": ("5.3.1", "IR Callable Fixed Swap"),
    "zcl": ("5.3.2", "Zero-Coupon Linked Note"), "ncra": ("5.3.3", "Non-Callable Range Accrual"),
    "crasrt": ("5.3.4", "Callable Range Accrual SRT"), "digcapfloor": ("5.3.5", "Digital Cap-Floor Note"),
    "vsteg": ("5.4.1", "Vanilla Steepener"), "rasteg": ("5.4.2", "Range Accrual Steepener"),
    "callablesteg": ("5.4.3", "Callable Steepener"), "tarnsteg": ("5.4.4", "TARN Steepener"),
    "cln": ("5.5.1", "Vanilla Credit-Linked Note"), "skewcln": ("5.5.2", "Skew CLN"),
    "ftd": ("5.5.3", "First-to-Default Note"), "ntd": ("5.5.4", "Nth-to-Default Note"),
    "cdo": ("5.5.5", "Synthetic CDO Tranche"), "strdep": ("5.6.1", "Structured Deposit"),
    "forward": ("5.6.2", "Forward"), "vanopt": ("5.6.3", "Vanilla Options"),
    "elo": ("5.6.4", "Equity-Linked Option"), "optrc": ("5.6.5", "Option on RC"),
    "accum": ("5.6.6", "Accumulator"), "decum": ("5.6.7", "Decumulator"),
    "dci": ("5.6.8", "Dual Currency Investment"), "sharkfin": ("5.6.9", "Shark Fin Note"),
    "snowball": ("5.6.10", "Snowball Note"), "cliquet": ("5.6.11", "Cliquet / Ratchet"),
    "woauto": ("5.6.12", "Worst-of Autocallable"),
}


def lens(fn):
    if fn.startswith(("payoff_", "legs_")):
        return ("Investor Lens", "#2e7d5b")
    if fn.startswith(("controls_",)):
        return ("Bank · Controls (2LoD)", "#c8553d")
    if fn.startswith(("desk_", "waterfall_")):
        return ("Bank · Desk Economics (1LoD)", "#41607f")
    return ("", "#8a99a8")


def main():
    dirs = sorted([d for d in os.listdir(ASSETS)
                   if os.path.isdir(os.path.join(ASSETS, d)) and d in META],
                  key=lambda d: [int(x) for x in META[d][0].split(".")])
    P = ['<!doctype html><meta charset="utf-8"><title>Dual-Lens Visual Catalog</title>',
         '<style>body{font-family:DejaVu Sans,Arial,sans-serif;margin:0;background:#f7f9fb;color:#1f3a5f}'
         'header{background:#1f3a5f;color:#fff;padding:22px 30px}h1{margin:0;font-size:22px}.sub{color:#cdd8e4;font-size:13px;margin-top:4px}'
         '.chap{margin:26px 30px;background:#fff;border:1px solid #e2e9f0;border-radius:10px;overflow:hidden}'
         '.chead{background:#eef2f6;padding:10px 16px;font-weight:bold;font-size:15px;border-bottom:1px solid #e2e9f0}'
         '.grid{display:flex;flex-wrap:wrap;gap:14px;padding:16px}'
         '.card{flex:1 1 420px;max-width:520px;border:1px solid #eef2f6;border-radius:8px;padding:8px}'
         '.tag{font-size:11px;font-weight:bold;padding:2px 8px;border-radius:10px;color:#fff;display:inline-block;margin-bottom:6px}'
         '.card svg{width:100%;height:auto}.fn{font-size:10px;color:#8a99a8;margin-top:4px;word-break:break-all}</style>']
    P.append(f'<header><h1>Dual-Lens Visual Catalog</h1><div class="sub">{len(dirs)} products · all generated diagrams, grouped by product and lens</div></header>')
    total = 0

    def order(p):
        b = os.path.basename(p)
        return (0 if b.startswith(("payoff_", "legs_")) else 1 if b.startswith(("desk_", "waterfall_")) else 2, b)

    for d in dirs:
        sec, nm = META[d]
        svgs = sorted(glob.glob(os.path.join(ASSETS, d, "*.svg")), key=order)
        if not svgs:
            continue
        P.append(f'<div class="chap"><div class="chead">{sec} &nbsp; {html.escape(nm)} &nbsp;'
                 f'<span style="color:#8a99a8;font-weight:normal">({len(svgs)} diagrams)</span></div><div class="grid">')
        for p in svgs:
            b = os.path.basename(p)
            lab, col = lens(b)
            svg = re.sub(r'^<\?xml[^>]*\?>', '', open(p, encoding="utf-8").read()).strip()
            P.append(f'<div class="card"><span class="tag" style="background:{col}">{lab}</span>{svg}<div class="fn">{b}</div></div>')
            total += 1
        P.append('</div></div>')
    P.append(f'<div style="margin:30px;color:#8a99a8;font-size:12px">{total} diagrams across {len(dirs)} products · '
             f'generated by governance/diagram_lib/sp_diagrams.py</div>')
    out = "governance/diagram_lib/visual_catalog.html"
    open(out, "w", encoding="utf-8").write("\n".join(P))
    print(f"catalog written: {out}  ({total} diagrams, {len(dirs)} products)")


if __name__ == "__main__":
    main()
