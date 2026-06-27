# Part 6 — Visual Specifications

**Date**: 2026-06-25
**Purpose**: Publication-ready diagram specifications for Part 6 visual assets
**Standard**: 11 diagrams, one per section. Production assets for future visual/print edition.
**Note**: These are specifications only. No graphics generated.

---

## Visual 1: Business Day Convention Decision Tree

| Field | Value |
|-------|-------|
| **Figure Number** | 6.1a |
| **Visual ID** | CONV-BDC-001 |
| **Type** | Decision tree / flowchart |
| **Priority** | HIGH |
| **Purpose** | Show how Modified Following differs from Following and Preceding through a single worked example |
| **Visual Description** | Decision tree starting from "Payment due on [date]". First branch: "Is [date] a business day?" → YES → "Pay on [date]". → NO → branch by convention: Following ("Move to next business day"), Preceding ("Move to previous business day"), Modified Following (sub-branch: "Does next business day fall in the next month?" → YES → "Move backward" / NO → "Move forward"). All three paths converge to "Final payment date" with a concrete example using December 31 (Saturday) |
| **Diagram Elements** | Diamond decision nodes, rectangular action nodes, three color-coded paths (Following = blue, Preceding = green, Modified Following = orange), concrete date example annotated at each terminal node |
| **Axis Definitions** | N/A (flowchart) |
| **Caption** | "Figure 6.1a — Business Day Convention Decision Tree. Modified Following is the market default because it prevents payments from crossing month boundaries." |
| **Location** | §6.1 Business Day Conventions, after the worked example paragraph |
| **Reuse Potential** | Part 2 (product construction), Solutions Manual (pricing decisions) |
| **Future Asset Filename** | fig_6_1a_bdc_decision_tree.svg |

---

## Visual 2: Day Count Convention Comparison

| Field | Value |
|-------|-------|
| **Figure Number** | 6.1b |
| **Visual ID** | CONV-DCC-001 |
| **Type** | Comparison table / bar chart hybrid |
| **Priority** | HIGH |
| **Purpose** | Show dollar impact of different day count conventions on the same notional and rate |
| **Visual Description** | Worked example: $10M at 5% for 90 days (Jan 15 to Apr 15). Five horizontal bars showing the coupon amount under each convention: ACT/360 ($125,000.00), ACT/365 ($123,287.67), ACT/ACT ($123,287.67), 30/360 ($125,000.00), 30E/360 ($125,000.00). Dollar differences annotated. Formula for each shown below its bar |
| **Diagram Elements** | 5 horizontal bars with dollar amounts, formula annotation below each, delta callouts between bars showing $ difference, color-coded by convention family (actual-based = blue, 30-based = orange) |
| **Axis Definitions** | X-axis: Dollar amount of coupon. Y-axis: Convention name |
| **Caption** | "Figure 6.1b — Day Count Convention Impact. Same notional, same rate, same period — five different dollar amounts. The difference is material on large notionals." |
| **Location** | §6.1 Day Count Conventions, after the calculation examples |
| **Reuse Potential** | Part 5 Swaps chapter (day count mismatch common mistakes) |
| **Future Asset Filename** | fig_6_1b_day_count_comparison.svg |

---

## Visual 3: Termsheet Anatomy

| Field | Value |
|-------|-------|
| **Figure Number** | 6.2a |
| **Visual ID** | TERM-ANAT-001 |
| **Type** | Annotated document mockup |
| **Priority** | HIGH |
| **Purpose** | Show how to read a termsheet by mapping each field to its category (dates, economics, conventions, legal) |
| **Visual Description** | Stylized termsheet document with 4 color-coded zones. Left margin: colored brackets grouping fields into "Date Fields" (blue, 14 items), "Economics Fields" (green, 16 items), "Convention Fields" (orange, 6 items), "Legal Fields" (red, 4 items). Right margin: callout annotations for the 3 most commonly misread fields (clean vs dirty price, participation rate, autocall trigger). Header shows "INDICATIVE" watermark with arrow pointing to note: "This is not binding" |
| **Diagram Elements** | Document outline, 4 color-coded bracket zones, 3 callout annotations, INDICATIVE watermark, field count per zone |
| **Axis Definitions** | N/A (document mockup) |
| **Caption** | "Figure 6.2a — Anatomy of a Termsheet. Four field categories, 40+ individual fields. The economics section determines the product's behavior; the convention section determines how the math works." |
| **Location** | §6.2 Reading a Termsheet, at section opening |
| **Reuse Potential** | Interview System (visual literacy questions), Solutions Manual (termsheet-based scenarios) |
| **Future Asset Filename** | fig_6_2a_termsheet_anatomy.svg |

---

## Visual 4: ISDA Master Agreement Structure

| Field | Value |
|-------|-------|
| **Figure Number** | 6.3a |
| **Visual ID** | DOC-ISDA-001 |
| **Type** | Layered architecture diagram |
| **Priority** | MEDIUM |
| **Purpose** | Show the three-layer structure of ISDA documentation and how they relate |
| **Visual Description** | Three nested rectangles (Russian doll layout). Outermost: "ISDA Master Agreement (standard, rarely modified)". Middle: "Schedule (customized elections — Part 1 through Part 5)". Innermost: "Confirmations (trade-specific terms)". Arrows show: Master governs Schedule, Schedule governs Confirmations, Confirmations reference both. Side panel: CSA shown as an annex attached to the Master. Below: timeline showing "Negotiated once → Applies to all trades → One per trade" |
| **Diagram Elements** | 3 nested rectangles, CSA annex box (attached by dashed line), directional arrows showing governance hierarchy, timeline bar at bottom, frequency labels |
| **Axis Definitions** | N/A (architecture diagram) |
| **Caption** | "Figure 6.3a — ISDA Documentation Hierarchy. The Master Agreement is negotiated once; the Schedule customizes it; each Confirmation captures one trade." |
| **Location** | §6.3 ISDA Master Agreement, after the structure explanation |
| **Reuse Potential** | Part 5 CLN/CDS chapters (documentation references), Interview System |
| **Future Asset Filename** | fig_6_3a_isda_structure.svg |

---

## Visual 5: Capital Structure Waterfall

| Field | Value |
|-------|-------|
| **Figure Number** | 6.4a |
| **Visual ID** | CRED-WFALL-001 |
| **Type** | Vertical waterfall / stacked bar |
| **Priority** | HIGH |
| **Purpose** | Show the 8-layer capital hierarchy and how losses flow through it from bottom to top |
| **Visual Description** | Vertical stack of 8 layers (bottom = equity, top = senior secured). Each layer labeled with: instrument type, typical recovery rate, example instruments. Left arrow showing "First to absorb losses" pointing up from equity. Right arrow showing "Last to absorb losses" pointing down from senior secured. AT1/CoCo layer highlighted with a trigger annotation: "Converts or writes down at CET1 < 5.125%". Middle section shows a worked example: "$100 loss distributed across layers" with the portion absorbed by each layer shaded |
| **Diagram Elements** | 8 stacked horizontal bars, loss absorption arrows, trigger annotation for AT1, worked loss distribution shading, recovery rate labels, instrument examples |
| **Axis Definitions** | Y-axis: Capital hierarchy (equity at bottom, secured at top). Shading: loss absorption proportion |
| **Caption** | "Figure 6.4a — Capital Structure and Loss Absorption Waterfall. Equity absorbs losses first. Senior secured is paid first in recovery. AT1 instruments convert or write down before the bank reaches the point of non-viability." |
| **Location** | §6.4 Capital Hierarchy, after the 8-layer table |
| **Reuse Potential** | CLN chapters (credit structure), Interview System (credit knowledge) |
| **Future Asset Filename** | fig_6_4a_capital_waterfall.svg |

---

## Visual 6: Fair Value Hierarchy Classification

| Field | Value |
|-------|-------|
| **Figure Number** | 6.5a |
| **Visual ID** | VAL-FVH-001 |
| **Type** | Three-column classification matrix |
| **Priority** | MEDIUM |
| **Purpose** | Show which product types fall into Level 1, 2, and 3 of the Fair Value Hierarchy |
| **Visual Description** | Three columns (L1, L2, L3), each with a header showing the input type ("Quoted prices", "Observable inputs", "Unobservable inputs"). Below each header: list of product families and specific products that typically fall into that level. Gradient bar at bottom from green (L1, most transparent) through amber (L2) to red (L3, most judgment). IPV tolerance thresholds shown at each level: L1 (tight, 0.1-0.5%), L2 (moderate, 1-3%), L3 (wide, 3-10%) |
| **Diagram Elements** | 3 columns with headers, product lists per column, gradient transparency bar, IPV tolerance annotations, escalation path arrows from L3 → ValComm |
| **Axis Definitions** | X-axis: Fair Value Level (1, 2, 3). Color gradient: transparency (green → red) |
| **Caption** | "Figure 6.5a — Fair Value Hierarchy Product Classification. Most structured products sit at Level 2 or 3. The level determines the IPV tolerance, the frequency of valuation committee review, and the disclosure requirements." |
| **Location** | §6.5 Fair Value Hierarchy, after the classification table |
| **Reuse Potential** | PC sections in Part 5, Solutions Manual (valuation context) |
| **Future Asset Filename** | fig_6_5a_fvh_classification.svg |

---

## Visual 7: P&L Explain Decomposition

| Field | Value |
|-------|-------|
| **Figure Number** | 6.6a |
| **Visual ID** | PC-PNL-001 |
| **Type** | Waterfall chart |
| **Priority** | HIGH |
| **Purpose** | Show how total P&L decomposes into Greek-based components plus unexplained residual |
| **Visual Description** | Waterfall chart. Starting bar: "Yesterday's MTM". Additive/subtractive bars for each P&L component: Delta P&L (+), Gamma P&L (+), Vega P&L (-), Theta P&L (-), Rho P&L (+), Dividend P&L (-), Funding P&L (-), New trades (+), Amendments (+/-), Unexplained (red, small). Ending bar: "Today's MTM". The Unexplained bar highlighted in red with tolerance annotation: "|Unexplained| < 5% of total P&L or $50K" |
| **Diagram Elements** | Waterfall bars (green = positive, red = negative), running total line, unexplained bar with red highlight, tolerance threshold annotation, formula at bottom: ΔP&L = Σ(Greek components) + New trades + Amendments + Unexplained |
| **Axis Definitions** | X-axis: P&L components in sequence. Y-axis: Dollar P&L ($) |
| **Caption** | "Figure 6.6a — P&L Explain Waterfall. Every dollar of daily P&L must be attributed to a driver. The unexplained residual should be small and understood — if it exceeds the tolerance, escalation is mandatory." |
| **Location** | §6.6 P&L Explain, after the decomposition table |
| **Reuse Potential** | Interview System (PC interview questions), day-in-the-life narrative (§6.10) |
| **Future Asset Filename** | fig_6_6a_pnl_waterfall.svg |

---

## Visual 8: FTP Curve and XVA Impact

| Field | Value |
|-------|-------|
| **Figure Number** | 6.7a |
| **Visual ID** | TRES-FTP-001 |
| **Type** | Dual-panel: yield curve + stacked cost breakdown |
| **Priority** | MEDIUM |
| **Purpose** | Show how FTP builds from components and how XVA charges stack on top of the base pricing |
| **Visual Description** | Left panel: FTP curve construction. Three curves stacked: risk-free rate (bottom, thin), credit spread (middle, medium), liquidity premium (top, thick). Combined FTP curve shown as the sum. X-axis: tenor (1Y to 30Y). Right panel: Product cost stack for a 5Y CLN. Stacked bar showing: base derivative value (bottom), CVA charge, DVA benefit (negative), FVA charge, ColVA, MVA, KVA. Net price at top. Arrow from FTP curve to the FVA component showing the connection |
| **Diagram Elements** | Left: 3 component curves + combined curve. Right: stacked bar with 7 layers. Connection arrow between panels. Dollar amounts on right panel. Percentage of notional annotations |
| **Axis Definitions** | Left: X = tenor (years), Y = rate (%). Right: X = N/A (single product), Y = cost (bps of notional) |
| **Caption** | "Figure 6.7a — From FTP Curve to XVA-Adjusted Price. The FTP curve determines the bank's internal funding cost. XVA charges layer counterparty credit risk, funding cost, and capital cost on top. Together they explain why the client's price differs from the theoretical 'risk-free' valuation." |
| **Location** | §6.7, after the XVA worked example |
| **Reuse Potential** | Part 2 §2.2 (pricing framework), Solutions Manual (pricing step) |
| **Future Asset Filename** | fig_6_7a_ftp_xva_stack.svg |

---

## Visual 9: Model Risk Lifecycle

| Field | Value |
|-------|-------|
| **Figure Number** | 6.8a |
| **Visual ID** | MRM-LIFE-001 |
| **Type** | Circular lifecycle diagram |
| **Priority** | MEDIUM |
| **Purpose** | Show the 8-stage model lifecycle as a continuous process with governance gates |
| **Visual Description** | Circular flow with 8 nodes: Development → Documentation → Validation → Approval → Implementation → Monitoring → Material Change → Retirement. Governance gates shown as diamond checkpoints between Validation→Approval (MRM Committee) and Material Change→Development (triggers re-validation). Side panel: three risk rating indicators (High/Medium/Low) with monitoring frequency and review requirements for each |
| **Diagram Elements** | 8 circular nodes connected by arrows, 2 governance gate diamonds, risk rating side panel, "Model Inventory" database icon connected to all nodes, feedback loop from Monitoring back to Development |
| **Axis Definitions** | N/A (circular lifecycle) |
| **Caption** | "Figure 6.8a — Model Risk Management Lifecycle. Models are not 'approved and forgotten.' They cycle continuously through monitoring, material change assessment, and re-validation. The model inventory tracks every model at every stage." |
| **Location** | §6.8, after the lifecycle description |
| **Reuse Potential** | Interview System (MRM questions), Part 5 product chapters (model references) |
| **Future Asset Filename** | fig_6_8a_model_lifecycle.svg |

---

## Visual 10: End-to-End Trade Flow

| Field | Value |
|-------|-------|
| **Figure Number** | 6.10a |
| **Visual ID** | DESK-FLOW-001 |
| **Type** | Swim lane / sequence diagram |
| **Priority** | HIGH |
| **Purpose** | Show how a trade flows across all 6 roles from inception to maturity |
| **Visual Description** | Horizontal swim lanes for 6 roles: Sales, Structurer, Trader, Operations, Product Control, Risk. Time axis (left to right): Day 0 (Client inquiry → structuring → pricing → execution), Day 1 (booking → confirmation → hedging → P&L), Day 2+ (IPV → lifecycle events → coupon payments → barrier monitoring), Maturity (settlement → final P&L → book cleanup). Each action is a numbered box. Arrows show handoffs between lanes. The Phoenix Autocallable example from §6.10 is used, with the 18 steps mapped onto the swim lanes |
| **Diagram Elements** | 6 horizontal swim lanes, 18 numbered action boxes, directional arrows for handoffs, 4 time phase columns (Day 0, Day 1, Day 2+, Maturity), system labels (NEMO, Sophis, Murex) on relevant action boxes, color-coded by role |
| **Axis Definitions** | X-axis: Time (Day 0 → Maturity). Y-axis: Role (Sales → Risk) |
| **Caption** | "Figure 6.10a — End-to-End Trade Flow: Phoenix Autocallable. A single trade touches all six desk functions. This diagram maps the 18-step narrative from Section 6.10 onto the people, systems, and timeline that execute it." |
| **Location** | §6.10, after the end-to-end trade flow narrative |
| **Reuse Potential** | Interview System (process flow questions), Solutions Manual (workflow context), Learning Dependency Graph (process understanding) |
| **Future Asset Filename** | fig_6_10a_trade_flow_swimlane.svg |

---

## Visual 11: Regulatory Framework Map

| Field | Value |
|-------|-------|
| **Figure Number** | 6.11a |
| **Visual ID** | REG-MAP-001 |
| **Type** | Matrix / Venn-style overlap diagram |
| **Priority** | MEDIUM |
| **Purpose** | Show which regulations apply to which product families and which desk functions |
| **Visual Description** | Matrix with rows = regulations (MiFID II, PRIIPs, EMIR, UMR, Basel/FRTB, MAR) and columns = product families (ELN, Swaps, SRT, STEG, CLN, Other). Cells filled where applicable, with primary impact shown in dark shade and secondary in light shade. Below the matrix: a second row mapping regulations to desk functions (Structuring, Trading, Sales, Ops, PC, Risk). Annotations for key interactions: "PRIIPs KID required for retail" → arrow to ELN column; "EMIR clearing mandate" → arrow to Swaps column |
| **Diagram Elements** | 6×6 regulatory-product matrix with shading, 6×6 regulatory-function matrix below, annotation arrows for key requirements, legend for primary/secondary impact |
| **Axis Definitions** | X-axis: Product families (6) / Desk functions (6). Y-axis: Regulations (6) |
| **Caption** | "Figure 6.11a — Regulatory Framework Map. No single regulation covers everything. MiFID II governs distribution; EMIR governs clearing; Basel governs capital. Every product family faces a different regulatory combination." |
| **Location** | §6.11, at section opening (orientation map) |
| **Reuse Potential** | Interview System (regulatory questions), Solutions Manual (regulatory context in decision model) |
| **Future Asset Filename** | fig_6_11a_regulatory_map.svg |

---

## Summary

| # | Visual ID | Type | Priority | Section |
|:-:|-----------|------|:--------:|---------|
| 1 | CONV-BDC-001 | Decision tree | HIGH | §6.1 |
| 2 | CONV-DCC-001 | Bar chart hybrid | HIGH | §6.1 |
| 3 | TERM-ANAT-001 | Annotated mockup | HIGH | §6.2 |
| 4 | DOC-ISDA-001 | Architecture diagram | MEDIUM | §6.3 |
| 5 | CRED-WFALL-001 | Vertical waterfall | HIGH | §6.4 |
| 6 | VAL-FVH-001 | Classification matrix | MEDIUM | §6.5 |
| 7 | PC-PNL-001 | Waterfall chart | HIGH | §6.6 |
| 8 | TRES-FTP-001 | Dual-panel | MEDIUM | §6.7 |
| 9 | MRM-LIFE-001 | Circular lifecycle | MEDIUM | §6.8 |
| 10 | DESK-FLOW-001 | Swim lane | HIGH | §6.10 |
| 11 | REG-MAP-001 | Matrix overlay | MEDIUM | §6.11 |

**HIGH priority**: 6 visuals (BDC decision tree, day count comparison, termsheet anatomy, capital waterfall, P&L waterfall, trade flow swim lane)
**MEDIUM priority**: 5 visuals (ISDA structure, FVH classification, FTP/XVA stack, model lifecycle, regulatory map)

---

**End of visual specifications.**
