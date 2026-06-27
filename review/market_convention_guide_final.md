# MARKET CONVENTION GUIDE — V1.0.1 FINAL

**Purpose:** Compact reference for market conventions that are often confused in structured products. Explains ambiguity and how V1.0.1 resolves it.  
**Status:** FINAL (package closure)  
**Supersedes:** `market_convention_guide.md`

---

## 1. Long vs Short Correlation

| Convention | "Long correlation" | "Short correlation" |
|:----------:|:------------------:|:-------------------:|
| **MTM Sensitivity (V1.0.1 default)** | Benefits when ρ rises | Benefits when ρ falls |
| **Structural / Premium** | Bought correlation premium | Sold correlation premium |

**V1.0.1 rule:** Default = MTM. Structural usage must be labeled with the word "structurally."

**Common trap:** An FTD investor "sold" the correlation premium (structural: short) but "benefits" from high ρ (MTM: long). The same position has opposite labels depending on convention. V1.0.1 calls this "long correlation" because MTM is the default.

---

## 2. Structural vs MTM Convention

These two lenses describe the same position from different angles:

| Lens | Question Answered | FTD Investor | Worst-of Investor |
|:----:|:-----------------:|:------------:|:-----------------:|
| **Structural** | "Who sold the premium?" | Short (sold first-default premium) | Short (sold correlation premium via basket) |
| **MTM** | "Who benefits from ρ rising?" | Long (high ρ → fewer independent defaults) | Long (high ρ → stocks move together) |

V1.0.1 always uses MTM unless the word "structurally" appears.

---

## 3. Protection Buyer vs Protection Seller

| Role | What They Do | Risk Taken | Premium Direction |
|:----:|-------------|:----------:|:-----------------:|
| **Protection seller** | Takes on the credit/equity risk | Earns coupon/premium | Receives |
| **Protection buyer** | Transfers credit/equity risk | Pays coupon/premium | Pays |

In structured notes:
- **Investor = protection seller** (takes on downside risk, earns enhanced coupon)
- **Desk = protection buyer** (transfers downside to investor, pays enhanced coupon)

**Common error (V1.0 Part 6, corrected by E-03):** Saying the desk "sold protection via the short put." The desk BOUGHT protection. The investor sold it.

---

## 4. Long vs Short Vol (Vega)

| Position | Meaning | Profits When | Typical Holder |
|:--------:|---------|:------------:|:--------------:|
| **Long vol** | P&L increases when implied vol rises | Vol spike | Hedged desk (bought options) |
| **Short vol** | P&L increases when implied vol falls | Vol crush | Structured product desk (sold embedded options to investors) |

---

## 5. Long vs Short Gamma

| Position | Meaning | Profits When | Typical Holder |
|:--------:|---------|:------------:|:--------------:|
| **Long gamma** | P&L benefits from large moves in either direction | Big move up or down | Bought options (convex payoff) |
| **Short gamma** | P&L harmed by large moves in either direction | Calm market | Sold options (concave payoff). Standard structured products desk near barriers |

**Common trap:** Short gamma ≠ short delta. A desk can be delta-neutral and massively short gamma.

---

## 6. Long vs Short Credit

| Position | Meaning | Profits When | Typical Holder |
|:--------:|---------|:------------:|:--------------:|
| **Long credit** (protection seller) | Earns spread/coupon, exposed to default | No default | CLN/FTD investor |
| **Short credit** (protection buyer) | Pays spread/premium, protected from default | Default event | CDS buyer, desk on CLN |

**Note:** "Short credit" and "short correlation" are different concepts. An FTD investor is short credit (exposed to defaults) but long correlation (benefits from high ρ).

---

## 7. Payer vs Receiver (Interest Rate Swaps)

| Position | Pays | Receives | View |
|:--------:|:----:|:--------:|:----:|
| **Payer** | Fixed rate | Floating rate | Bearish on bonds / expects rates to rise |
| **Receiver** | Floating rate | Fixed rate | Bullish on bonds / expects rates to fall |

**Mnemonic:** "Payer" and "receiver" always refer to the **fixed leg**. A payer PAYS fixed.

---

## 8. Clean vs Dirty Price (Bonds)

| Price | Definition | When Used |
|:-----:|-----------|:---------:|
| **Clean** | Excludes accrued interest | Quotation and comparison |
| **Dirty** | Includes accrued interest (= clean + accrued) | Settlement and actual cash flow |

**Rule:** Bonds are QUOTED clean but SETTLE dirty. If someone says "the bond is trading at 98," that's the clean price.

---

## 9. Strike vs Barrier

| Term | Definition | Role in Structured Products |
|:----:|-----------|:---------------------------:|
| **Strike** | The price/level at which the embedded option is exercised. Determines the payoff calculation at maturity | Maturity comparison: above strike → par; below strike → physical delivery or cash loss |
| **Barrier** | The price/level that activates (knock-in) or deactivates (knock-out) the option | During life: breaching the barrier changes the product's payoff structure |

**Common trap:** In some products (e.g., RC), the strike and barrier are different levels. In others (e.g., some WOACs), the strike may equal the initial level (100%) while the barrier is lower (60%). Never assume strike = barrier.

**V1.0.1 rule:** Every worked example that references both strike and barrier must define them separately in the terms table.

---

## 10. Raw vs Hedged Positions

| Position | Definition | Correlation Direction Example (Worst-of) |
|:--------:|-----------|:-----------------------------------------:|
| **Raw / Unhedged** | The exposure from embedded options in products sold, before any hedge | Short correlation (desk is long the worst-of put) |
| **Net / Hedged** | Residual exposure after all hedges | Long correlation (typical, after dispersion hedges) |

**V1.0.1 rule:** Always specify raw or hedged when describing a desk position. See `raw_vs_hedged_position_note_final.md`.

---

*V1.0.1 Market Convention Guide | FINAL (package closure) | 2026-06-27*
