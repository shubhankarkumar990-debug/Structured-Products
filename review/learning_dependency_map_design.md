# Learning Dependency Map — Design Review

**Date:** 2026-06-21
**Purpose:** Assess creation of a learning progression visual distinct from Universe Map
**Interaction:** FIG-FM-02 (front matter dependency map), Universe Map (E16), Learning Paths (E5)

---

## 1. Distinction from Existing Visuals

| Visual | Question Answered | Data Type | Audience |
|--------|:-----------------:|-----------|----------|
| **Universe Map (E16)** | "What exists?" | Classification: family × complexity grid | Everyone |
| **FIG-FM-02 (front matter)** | "What do I need to read first?" | Prerequisites: A requires B | Beginners |
| **Learning Dependency Map (proposed)** | "How do I progress from basic to expert?" | Progression: learning chains across families | All levels |

### 1.1 Overlap Assessment

FIG-FM-02 already shows prerequisite chains. The proposed Learning Dependency Map shows *the same prerequisite chains* but organized as multi-track progressions rather than a single DAG.

**Key question: Is this sufficiently different from FIG-FM-02 to justify a separate visual?**

---

## 2. What the Learning Dependency Map Would Show

### 2.1 Four Learning Tracks

**Track 1: Equity-Linked Progression**
```
1.1 Core → 1.2 Options → 1.3 Barriers → PPN (2) → RC (3) → 
Phoenix (6) → Worst-of AC (7) → TARN (8)
```

**Track 2: Rate-Linked Progression**
```
1.7 Yield Curves → 1.8 Rates → IRS (3) → CMS (4) → 
Cross-Currency (5) → Range Accrual (5) → CSTEG (7)
```

**Track 3: Credit-Linked Progression**
```
1.9 Credit Risk → CLN (4) → Skew CLN (5) → FTD (7) → 
NTD (8) → Synthetic CDO (10)
```

**Track 4: Cross-Asset Progression**
```
Track 1 basics + Track 2 basics → TRS (4) → CRT (5) → 
Accumulator (6) → Decumulator (6)
```

### 2.2 Cross-Track Bridges

```
Track 1 (RC) ──bridges──► Track 3 (CLN) via "same construction pattern"
Track 2 (IRS) ──bridges──► Track 4 (TRS) via "swap mechanics"
Track 1 (Phoenix) ──bridges──► Track 2 (NCRA) via "observation mechanics"
```

---

## 3. Comparison with FIG-FM-02

| Attribute | FIG-FM-02 | Learning Dependency Map |
|-----------|:---------:|:----------------------:|
| Layout | Single DAG, all 49 products | 4 parallel tracks with cross-bridges |
| Complexity | Complex — 49 nodes, many arrows | Simpler — 4 linear tracks, few bridges |
| Use case | "Can I read product X yet?" | "What's my next step on this track?" |
| Reader action | Check prerequisites | Follow a progression path |
| Visual size | Full page | Could be half-page per track, or one landscape page |
| Redundancy with FM-02 | N/A | ~70% of information overlaps |

### 3.1 Honest Assessment

The Learning Dependency Map contains ~70% of the same information as FIG-FM-02, reorganized into tracks. The 30% new information is the "track" framing — grouping products into progression sequences rather than showing a flat prerequisite graph.

This 30% is genuinely useful but can be achieved by **annotating FIG-FM-02 with track colors** rather than creating a separate visual.

---

## 4. Alternative: Enhanced FIG-FM-02

Instead of a separate Learning Dependency Map, enhance FIG-FM-02:

| Enhancement | Implementation |
|------------|---------------|
| Color-code by track | Equity = Blue, Rates = Green, Credit = Red, Cross-Asset = Purple |
| Number nodes by progression order | Within each track: 1, 2, 3... |
| Show cross-track bridges | Dashed lines between tracks at bridge points |
| Add track labels | "Equity-Linked Track", "Credit-Linked Track" along edges |

This gives readers the progression view and the prerequisite view in a single visual. No separate asset needed.

---

## 5. Verdict

### **NO-GO as separate visual. GO as FIG-FM-02 enhancement.**

**Rationale:**
- 70% overlap with FIG-FM-02 doesn't justify a separate visual
- Track framing achieved by color-coding FIG-FM-02
- Reader benefits from ONE navigation visual with TWO reading modes (prerequisite check + progression tracking)
- Fewer visuals = less maintenance, less reader confusion
- Front matter plan already allocates FIG-FM-02 — enhancement adds zero pages

**Action:** Update `front_matter_plan.md` specification for FIG-FM-02 to include 4-track color coding, progression numbering, and cross-track bridges. No new design document needed. No new visual asset.

---

*Learning Dependency Map Design Review completed 2026-06-21.*
*VERDICT: NO-GO as separate visual. Merge into FIG-FM-02 via color-coded track enhancement.*
