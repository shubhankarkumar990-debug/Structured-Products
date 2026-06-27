# Visual Toolchain Review

**Date:** 2026-06-21
**Scope:** Assess 5 visual production tools for Desk Bible v2 (~294 publication assets)
**Framework:** v1.3.1 (FROZEN)
**Purpose:** Determine optimal tool assignment per visual type

---

## 1. Toolchain Assessment

### 1.1 Figma

| Dimension | Assessment |
|-----------|-----------|
| **Use cases** | Component-based diagrams: cash flow structures, multi-party flows, system architecture, tranche bands, entity relationship diagrams. Any visual requiring precise spatial layout with reusable parts |
| **Strengths** | Component library with variants. Master ↔ instance inheritance. Collaboration. Version history. Auto-layout. Direct SVG export. Style guide enforcement. Shared color/typography tokens |
| **Weaknesses** | Requires Figma license. Manual creation (no programmatic generation). Not suitable for data-driven charts. Learning curve for non-designers. No LaTeX/math rendering |
| **Recommended role** | **PRIMARY tool** for structure diagrams, cash flow diagrams, lifecycle timelines, decision trees, tranche visuals, and all Tier 1 publication assets requiring precise design control |

**Verdict: ESSENTIAL. Core production tool.**

### 1.2 Mermaid

| Dimension | Assessment |
|-----------|-----------|
| **Use cases** | Flowcharts, sequence diagrams, decision trees, state diagrams, Gantt charts. Any diagram describable in text-based DSL |
| **Strengths** | Text-based (version-controllable in Git). Fast iteration. No design tool needed. Embeddable in Markdown. Consistent styling via themes. Good for rapid prototyping |
| **Weaknesses** | Limited layout control (auto-arranged). Cannot produce publication-quality output without post-processing. No precise coordinate control. Styling options limited. Cannot do payoff charts, data plots, or complex spatial layouts. SVG output requires rendering engine |
| **Recommended role** | **DRAFT/PROTOTYPE tool** for flowcharts and decision trees. Source files stored for reference. Final publication assets re-created in Figma or exported as SVG and polished |

**Verdict: USEFUL FOR DRAFTS. Not publication-grade alone.**

### 1.3 Draw.io (diagrams.net)

| Dimension | Assessment |
|-----------|-----------|
| **Use cases** | System architecture, booking flows, four-leg structures, entity relationship diagrams. Complex multi-layer diagrams with connectors |
| **Strengths** | Free. Desktop and web versions. XML-based (version-controllable). Built-in shape libraries. Good connector routing. SVG/PNG/PDF export. Layers support |
| **Weaknesses** | Less polished than Figma for publication. No component inheritance (copy-paste, not instances). No shared style tokens. Manual style consistency. Collaboration weaker than Figma |
| **Recommended role** | **SECONDARY tool** for system architecture diagrams and booking flow diagrams where Figma component library is overkill. Also useful as fallback if Figma unavailable |

**Verdict: USEFUL SECONDARY. Good for architecture diagrams.**

### 1.4 Python Chart Generation (Matplotlib/Plotly)

| Dimension | Assessment |
|-----------|-----------|
| **Use cases** | Payoff diagrams, yield curves, correlation curves, loss distributions, scenario comparison charts. Any visual driven by numerical data or mathematical functions |
| **Strengths** | Programmatic (reproducible, parameterizable). Handles mathematical functions natively. Batch generation possible. Data-driven. Version-controllable (Python scripts in Git). Can generate hundreds of charts from templates. Exact axis scaling. LaTeX support for labels |
| **Weaknesses** | Requires Python environment. Default styling needs customization for publication quality. Not suitable for entity/flow diagrams. Output SVG can be verbose. Requires post-processing for consistent branding |
| **Recommended role** | **PRIMARY tool** for all payoff diagrams, correlation curves, yield curve charts, loss distributions, premium scaling curves, and any data-driven or function-based visual |

**Verdict: ESSENTIAL. Only tool that handles math-based charts correctly.**

### 1.5 Nano Banana (AI Illustration)

| Dimension | Assessment |
|-----------|-----------|
| **Use cases** | Conceptual illustrations for §2 (Real-World Analogy). Visual metaphors: domino chains, highrise buildings, fire alarm systems, car insurance tiers. Chapter openers. Front matter decorative elements |
| **Strengths** | Can produce unique, memorable illustrations that text-based tools cannot. Supports the analogy-driven teaching approach. Makes the book visually distinctive. Engages visual learners differently than charts |
| **Weaknesses** | Style consistency requires careful prompting. Not suitable for technical diagrams. Cannot produce precise payoffs or data charts. Each illustration is unique (no component reuse). Quality varies. Review overhead higher |
| **Recommended role** | **SUPPLEMENTARY tool** for analogy illustrations (§2 visuals) and front matter decorative elements. Not counted toward the 6 mandatory visual specs per chapter — these are bonus publication assets |

**Verdict: SUPPLEMENTARY. High impact for branding, not for technical content.**

---

## 2. Recommended Production Stack

### 2.1 Tool × Visual Type Matrix

| Visual Type | Primary Tool | Secondary Tool | Count (est.) |
|------------|-------------|---------------|:------------:|
| Payoff diagrams | **Python** | — | ~80 |
| Correlation/distribution curves | **Python** | — | ~15 |
| Yield curve charts | **Python** | — | ~10 |
| Cash flow / structure diagrams | **Figma** | Draw.io | ~65 |
| Lifecycle timelines | **Figma** | Mermaid (draft) | ~49 |
| Decision trees | **Figma** | Mermaid (draft) | ~25 |
| Waterfall diagrams | **Figma** | Python | ~15 |
| Comparison charts | **Python** | Figma | ~20 |
| System/booking flows | **Draw.io** | Figma | ~10 |
| Tranche/band diagrams | **Figma** | — | ~5 |
| Analogy illustrations | **Nano Banana** | — | Optional (~49) |
| Front matter visuals | **Figma** | Python | ~4 |

### 2.2 Production Volume by Tool

| Tool | Primary Assets | Secondary Assets | Total Touch |
|------|:--------------:|:----------------:|:-----------:|
| Python | ~125 (43%) | ~20 | ~145 |
| Figma | ~115 (39%) | ~15 | ~130 |
| Draw.io | ~10 (3%) | ~15 | ~25 |
| Mermaid | 0 (drafts only) | ~74 (draft sources) | ~74 drafts |
| Nano Banana | ~49 (optional) | 0 | ~49 optional |

### 2.3 Workflow Integration

```
Chapter Visual Spec (§21)
    │
    ├── Math-based? ──YES──► Python script ──► SVG ──► Polish in Figma if Tier 1
    │                                                    │
    │                                                    ▼
    │                                              Publication SVG
    │
    ├── Structure/flow? ──YES──► Mermaid draft ──► Figma production
    │                                                    │
    │                                                    ▼
    │                                              Publication SVG
    │
    ├── System/booking? ──YES──► Draw.io ──► SVG export
    │                                           │
    │                                           ▼
    │                                     Publication SVG
    │
    └── Analogy art? ──YES──► Nano Banana ──► PNG/SVG
                                                │
                                                ▼
                                          Supplementary asset
```

---

## 3. Infrastructure Requirements

| Tool | Needs Setup? | Setup Steps |
|------|:------------:|-------------|
| Python | YES | Install matplotlib, plotly. Create chart template scripts. Define Desk Bible style theme. Set up batch generation pipeline |
| Figma | YES | Create master file. Build component library (per `figma_production_architecture.md`). Import color/typography tokens |
| Draw.io | MINIMAL | Install desktop app. Create Desk Bible shape library |
| Mermaid | MINIMAL | CLI or VS Code extension. Define custom theme matching Desk Bible palette |
| Nano Banana | YES | Define style prompt template. Create consistency guidelines. Set up review workflow |

---

## 4. Risk Assessment

| Risk | Severity | Mitigation |
|------|:--------:|-----------|
| Style inconsistency across tools | High | Define shared color palette (hex codes), typography, and line weights in all tools. Single source: `visual_asset_governance.md` |
| Python charts look "academic" not "publication" | Medium | Create custom matplotlib style sheet matching Desk Bible aesthetic. Post-process Tier 1 charts in Figma |
| Mermaid output not publication-grade | Low | Mermaid used only for drafts. All final assets through Figma/Python |
| Nano Banana style drift | Medium | Create and maintain a prompt template with style anchors. Review every illustration against reference set |
| Tool proliferation | Low | Clear assignment matrix (§2.1) prevents overlap. Each visual type has ONE primary tool |

---

*Visual Toolchain Review v1.0. Completed 2026-06-21.*
