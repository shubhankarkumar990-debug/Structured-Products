# Payoff Chart Creation Framework — Design Review

**Date:** 2026-06-21
**Proposed Expansion:** Section 1.10 extended, or Section 1.10B (separate)
**Framework:** v1.3.1 (FROZEN)
**Purpose:** Assess expanding Payoff Chart Masterclass to include creation workflows
**Implementation:** After 49/49, after Payoff Chart Masterclass (§1.10) is written

---

## 1. Relationship to Existing Design

The Payoff Chart Masterclass (§1.10) teaches *reading* charts. This framework extends it to *creating* charts. Two options:

| Option | Approach | Pros | Cons |
|--------|----------|------|------|
| **A: Extend §1.10** | Add creation subsections to existing design (1.10.11-1.10.15) | Unified section. One place for all payoff chart skills | §1.10 grows from ~3,500 to ~6,500 words. May feel heavy for readers who only need reading |
| **B: Separate §1.10B** | New section "1.10B: Creating Payoff Charts" | Clean separation. Reading-only readers skip creation. Modular | Two section numbers for related content |

**Recommendation: Option A — Extend §1.10.** One unified "Payoff Charts" section. Subsections 1.10.1-1.10.10 = reading (existing design). Subsections 1.10.11-1.10.15 = creation (this design). Reader stops after 1.10.10 if they only need reading.

---

## 2. Five Creation Workflows

### 2.1 Manual Sketching

| Attribute | Specification |
|-----------|-------------|
| **When to use** | First pass. Whiteboard discussions. Structurer-client meetings. Interview settings |
| **Teach** | 4-step method: (1) Draw axes, (2) Mark key levels (strike, barrier, cap), (3) Draw linear segments between levels, (4) Add labels |
| **Tools needed** | Paper + pen, or whiteboard |
| **Output quality** | Conceptual — not publication-grade |
| **Words** | ~400 |

**Teaching approach:** 3 worked examples — PPN (simple kink), RC (barrier discontinuity), Phoenix (multi-level).

### 2.2 Excel Workflow

| Attribute | Specification |
|-----------|-------------|
| **When to use** | Quick analysis. Client presentations. Ad-hoc pricing comparison |
| **Teach** | Column A: underlying prices (50% to 150%, step 1%). Column B: payoff formula using IF/MIN/MAX. Chart: XY scatter with smooth lines |
| **Formula patterns** | PPN: `=MAX(1, 1 + Participation*(A2-1))`. RC: `=IF(A2>Barrier, 1+Coupon, A2+Coupon)` |
| **Tools needed** | Excel or Google Sheets |
| **Output quality** | Functional — suitable for internal use |
| **Words** | ~600 |

**Teaching approach:** Template provided. Reader builds RC payoff step by step. Then modifies for Phoenix (adds conditional coupon logic).

### 2.3 Python Workflow

| Attribute | Specification |
|-----------|-------------|
| **When to use** | Publication visuals. Batch generation. Reproducible charts. Parameterized comparison |
| **Teach** | numpy array for prices, vectorized payoff function, matplotlib chart with Desk Bible style sheet |
| **Code pattern** | |

```python
import numpy as np
import matplotlib.pyplot as plt

spot = np.linspace(0.5, 1.5, 200)
barrier = 0.70
coupon = 0.065

payoff = np.where(spot >= barrier, 1 + coupon, spot + coupon)

plt.plot(spot * 100, payoff * 100, linewidth=2, color='#2563EB')
plt.axhline(y=100, color='#6B7280', linestyle='--', alpha=0.5)
plt.axvline(x=barrier * 100, color='#DC2626', linestyle='--', alpha=0.5)
plt.xlabel('Underlying at Maturity (%)')
plt.ylabel('Investor Return (%)')
plt.title('Reverse Convertible Payoff')
```

| **Tools needed** | Python, matplotlib, numpy |
| **Output quality** | Publication-grade with Desk Bible style sheet |
| **Words** | ~700 |

**Teaching approach:** Start with RC. Show how to add barrier shading, breakeven annotation, scenario labels. Then parameterize for batch generation.

### 2.4 Figma Workflow

| Attribute | Specification |
|-----------|-------------|
| **When to use** | Publication-grade diagrams needing precise layout control. Multi-chart comparison panels. Annotated figures with callouts |
| **Teach** | Using Desk Bible Figma components: axis frame, payoff line, barrier marker, annotation labels. Component-based assembly |
| **Process** | (1) Start from axis template, (2) Draw payoff path using pen tool, (3) Add barrier/strike markers from component library, (4) Add labels and annotations, (5) Export SVG |
| **Tools needed** | Figma with Desk Bible component library |
| **Output quality** | Publication-grade. Maximum design control |
| **Words** | ~500 |

### 2.5 SVG Direct Workflow

| Attribute | Specification |
|-----------|-------------|
| **When to use** | When programmatic control needed but Python environment unavailable. Web integration. Light-weight reproducible charts |
| **Teach** | SVG coordinate system, `<polyline>` for payoff paths, `<line>` for axes and barriers, `<text>` for labels |
| **Code pattern** | |

```xml
<svg viewBox="0 0 700 400" xmlns="http://www.w3.org/2000/svg">
  <line x1="50" y1="350" x2="650" y2="350" stroke="#6B7280"/>
  <line x1="50" y1="50" x2="50" y2="350" stroke="#6B7280"/>
  <polyline points="50,200 350,200 500,50" fill="none" stroke="#2563EB" stroke-width="2"/>
  <line x1="350" y1="50" x2="350" y2="350" stroke="#DC2626" stroke-dasharray="5,5"/>
  <text x="350" y="370" text-anchor="middle">Strike</text>
</svg>
```

| **Tools needed** | Text editor |
| **Output quality** | Clean, scalable. Needs styling for publication |
| **Words** | ~500 |

---

## 3. Comparison: When To Use Each

| Workflow | Speed | Quality | Reproducibility | Batch Capable | Skill Required |
|----------|:-----:|:-------:|:---------------:|:-------------:|:--------------:|
| Manual sketch | Fastest | Low | No | No | None |
| Excel | Fast | Medium | Partial | No | Basic |
| Python | Medium | High | Yes | Yes | Intermediate |
| Figma | Slow | Highest | Partial | No | Intermediate |
| SVG direct | Medium | Medium-High | Yes | Yes | Intermediate |

**Decision tree:**

```
Need a chart right now? → Manual sketch
Need it for a client deck? → Excel
Need it for the book? → Python (math) or Figma (annotated)
Need 50 charts with same style? → Python
Need one perfect annotated figure? → Figma
Need web-embeddable? → SVG direct
```

---

## 4. Section Structure (as §1.10 extension)

| Subsection | Content | Est. Words |
|-----------|---------|:----------:|
| **1.10.11 — Creating Charts: Overview** | When to create vs just read. Five workflow options. Decision tree | 300 |
| **1.10.12 — Manual Sketching** | 4-step method. 3 worked examples | 400 |
| **1.10.13 — Excel Method** | Template, formulas, chart setup. RC worked example | 600 |
| **1.10.14 — Python Method** | numpy/matplotlib. Desk Bible style. RC + batch example | 700 |
| **1.10.15 — Figma and SVG Methods** | Component assembly. SVG coordinates. When to use each | 500 |
| **1.10.16 — Exercises** | Create 3 payoff charts (one per method). Compare outputs | 300 |
| **Subtotal (creation)** | | **~2,800** |
| **Grand total §1.10** | Reading (3,500) + Creation (2,800) | **~6,300** |

---

## 5. Visual Requirements (Creation Section Only)

| # | Visual | Type | Purpose |
|:-:|--------|------|---------|
| 1 | Manual sketch example (annotated photo/scan) | Reference | Show hand-drawn quality level |
| 2 | Excel screenshot with formula bar visible | Screenshot | Template demonstration |
| 3 | Python output (styled) | Chart | Publication-grade example |
| 4 | Figma component assembly (screenshot) | Screenshot | Component-based workflow |
| 5 | SVG rendered output | Chart | Direct SVG example |
| 6 | Side-by-side comparison (same RC payoff, 5 methods) | Comparison | Quality/style comparison |

**Total: 6 additional visuals.**

---

## 6. Estimates

| Metric | Value |
|--------|:-----:|
| Additional word count | ~2,800 |
| Additional visuals | 6 |
| Additional pages | ~6 |
| Effort | 2 days |
| Dependency | Payoff Chart Masterclass (§1.10 reading) must be written first |

---

## 7. Assessment

| Criterion | Score |
|-----------|:-----:|
| Educational impact | MEDIUM-HIGH — creation is valuable but fewer readers need it than reading |
| Effort | LOW — 2,800 words, extends existing section |
| Publication value | MEDIUM — useful but not essential for core audience |
| Reader value | HIGH for structurers/quants, LOW for sales/operations |
| Risk | LOW — additive subsections, no architectural changes |

**Recommendation: PROCEED, lower priority.** Valuable for technical readers. Implement as optional extension to §1.10 after core creation work is complete. Can be cut from first edition if page budget is tight.

---

*Payoff Chart Creation Framework Design Review completed 2026-06-21.*
