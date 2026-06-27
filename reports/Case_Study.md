# Case Study: AI-Driven Knowledge Governance at Scale
## Structured Products Desk Bible — Design, Execution, and Framework Extraction

---

# FORMAT 1: FULL CASE STUDY

---

## 1. Executive Summary

A structured products trading desk operates with knowledge distributed across individuals, spreadsheets, and tribal memory. When experienced staff depart, critical operational knowledge — how products are booked, which systems process them, how pricing ties to risk — leaves with them. This creates operational risk, onboarding delays, and audit exposure.

I designed and delivered an AI-powered documentation governance system that produced a comprehensive Desk Bible covering 28 structured products across 5 product families. The system generated 280+ pipeline artifacts, enforced three independent quality gates, maintained a reusable memory layer, and achieved zero defects across all published content — zero accuracy blockers, zero style violations, zero broken cross-references.

The project was completed in 2 days across 4 sessions, consuming approximately 416,000 tokens. Following delivery, I extracted the underlying methodology into a domain-agnostic Knowledge Bible Framework with documented adaptation paths for 7 additional domains including Model Risk Management, Credit Risk, Regulatory Compliance, and Operational Risk.

**Key outcomes:**
- 28/28 products delivered at 100% quality gate pass rate
- Zero retries from the second batch onward (22 products)
- Stable per-unit cost of ~14,866 tokens regardless of product complexity
- 4.6:1 memory reuse ratio, reducing redundant computation by 20–30%
- Reusable framework extracted with 9 guides and 7 domain adaptation examples

---

## 2. Project Overview

### Scope

The Desk Bible covers 28 structured products organised into 5 families:

| Family | Products | Examples |
|--------|:--------:|---------|
| Equity-Linked Notes (ELN) | 13 | Reverse Convertible, Phoenix Autocall, Bonus Certificate, Participation Note |
| Securitisation & Repackaging (SRT) | 5 | IR-Capped FRN, Amortising FRN, Notional-Capped Repackaged Accreter |
| Credit-Linked Notes (CLN) | 5 | Vanilla CLN, Subordinated CLN, First-to-Default, Nth-to-Default, Synthetic CDO Tranche |
| Steepener Notes (STEG) | 4 | Vanilla Steepener, Range Accrual Steepener, Callable Steepener, TARN Steepener |
| Swaps | 1 | Equity Variance Swap |

Each product page includes 8 standardised sections: Definition, Construction, Booking & Systems, Pricing Intuition, Worked Example, Reconciliation, Desk View, and Desk Shorthand.

### Architecture

The system employs a **4-stage pipeline** with artifact-based state management:

1. **Research** — Domain research and source material synthesis
2. **Write** — Draft generation using family memory artifacts for consistency
3. **Review** — Three independent quality gates (Accuracy, Style, Cross-Reference)
4. **Publish** — Final validation, readiness confirmation, and catalog update

Every stage produces a file on disk. The pipeline is stateless — it can be interrupted at any point and resumed by checking which files exist. This proved critical: the project spanned 4 sessions with 3 context continuations, and zero state was lost.

### Memory Architecture

A **per-family memory layer** stores three artifact types:

- **Terminology** — Canonical abbreviations, product names, and domain terms
- **Operational Maps** — System mappings (which booking system, which risk engine, which data feeds)
- **Style Conventions** — Formatting rules, known false positives, accepted conventions

15 memory artifacts were created (3 per family) and reused 69 times across all products, yielding a 4.6:1 reuse ratio.

### Governance Framework

- **Git-based version control** with per-batch commits and 11 milestone tags
- **Binary quality gates** — PASS/FAIL, no subjective scoring
- **Checkpoint files** for every product — full audit trail of gate results and retry counts
- **Progress dashboard** — updated after every batch with cumulative metrics
- **Production history log** — timestamped record of every batch execution

---

## 3. Challenges

### Knowledge Consistency

Structured products are complex instruments with interdependencies across families. An equity-linked note and a credit-linked note may share structural elements but use entirely different booking systems. Ensuring that system references, terminology, and operational procedures were consistent across 28 products — without drift or contradiction — required a systematic approach.

### Documentation Scalability

Producing 28 detailed product pages manually would take weeks and produce inconsistent results. The challenge was to create a system that scales linearly with product count while maintaining quality — where the 28th product is as accurate as the 1st.

### Quality Assurance

Financial documentation errors carry operational risk. An incorrectly stated system mapping could cause a product to be booked in the wrong system. An arithmetic error in a worked example could mislead a junior trader. Quality gates needed to catch real errors without generating noise.

### Auditability

Regulatory and audit expectations require a clear trail showing what was produced, when, by what process, and what quality checks were applied. Every intermediate artifact, every gate result, and every decision needed to be traceable.

### Maintainability

A desk bible that cannot be updated becomes stale within months. The system needed to support adding new products, updating existing entries, and performing annual reviews — ideally by someone who inherits the project with no prior context.

---

## 4. Solution

### Multi-Agent Pipeline

The pipeline processes each product through 4 stages, generating 10 artifacts per product:

```
Research YAML → Draft Markdown → 3 Review YAMLs → Publish YAML
                                  + Booking YAML
                                  + Checkpoint JSON
                                  + Pipeline Log YAML
```

Each stage has defined inputs, outputs, and a single responsibility. Failures are isolated — a style violation doesn't require re-running the accuracy gate.

### Memory System

The memory layer solved the consistency problem. Rather than re-deriving system mappings, terminology, and formatting rules for each product, the system:

1. **Bootstraps** a family by generating one representative product and extracting conventions
2. **Validates** observed conventions across a second product before enshrining them
3. **Reuses** the validated memory artifacts for all subsequent products in the family

The **Convention Validation Protocol** (observe once → validate twice → enshrine) prevented false conventions from entering the memory layer. The **Arithmetic Verification Protocol** (v2.1) required computational reproduction of every calculation before raising a blocker, with a ±0.2% rounding tolerance.

### Quality Gates

Three independent gates, each with binary PASS/FAIL criteria:

| Gate | Purpose | Blocks On |
|------|---------|-----------|
| **Accuracy** | Factual correctness, arithmetic verification | Verified computational errors |
| **Style** | Formatting, notation, terminology consistency | Must-fix violations after FP suppression |
| **Cross-Reference** | Internal link integrity | Broken references to non-existent entries |

The accuracy gate includes a false-positive suppression mechanism: known advisory findings (such as decomposition format conventions inherent to product structure) are classified as MAJOR advisory rather than BLOCKER.

### Checkpoint System

Every product has a checkpoint file recording:
- Which stages completed
- Which gates passed or failed
- Retry count (zero for all products from Batch 1 onward)
- Whether all gates passed

This provides both a recovery mechanism (never needed) and an audit record.

### Governance Model

- **Batch processing** with 3–6 products per batch
- **Pre/post-batch Git tags** for safe rollback points
- **Per-batch dashboard updates** with cumulative metrics
- **Maintenance guide** for future operators (10 sections covering product additions, updates, annual reviews, and release management)

---

## 5. Results

### Completion Metrics

| Metric | Value |
|--------|-------|
| Products completed | 28/28 (100%) |
| Product families | 5/5 (100%) |
| Artifacts generated | 280+ |
| Batches | 7 |
| Sessions | 4 |
| Duration | 2 days |

### Quality Metrics

| Metric | Value |
|--------|-------|
| Accuracy BLOCKERs | 0 |
| Style MUST_FIX violations | 0 |
| Broken cross-references | 0 |
| Publishing failures | 0 |
| Gate pass rate (all 3 gates) | 28/28 (100%) |
| Retries (Batch 1 onward) | 0 across 22 products |
| Checkpoint recoveries needed | 0 |

### Memory Efficiency

| Metric | Value |
|--------|-------|
| Memory artifacts created | 15 |
| Memory reuses | 69 |
| Reuse ratio | 4.6:1 |
| False positives suppressed | 84 (3 per product × 28) |
| Token savings from memory | 20–30% per product |

### Token Efficiency

| Metric | Value |
|--------|-------|
| Per-product cost | ~14,866 tokens |
| Total cost | ~416,248 tokens |
| Cost variance by complexity | ±0% (stable from simplest to most complex) |
| Cost reduction from baseline | 20–30% (memory reuse from Batch 1 onward) |

### Delivered Assets

| Deliverable | Detail |
|-------------|--------|
| Assembled Desk Bible | 2,821-line document, all 28 products |
| Release package | Complete with all artifacts, reports, and memory |
| Maintenance guide | 10-section operational runbook |
| Framework (v1) | README, bootstrap guide, 8 templates |
| Framework (v2) | 9 guides, 7 domain examples, maturity assessment |
| Retrospective | Architecture, tokens, memory, quality, governance analysis |

---

## 6. Leadership and Strategic Thinking

### System Design

Designed a pipeline architecture that prioritises **resumability** and **auditability** over speed. The decision to use files on disk as the state mechanism — rather than in-memory state — was the single most consequential architectural choice. It enabled:

- Resumption across 3 context continuations with zero state loss
- Full audit trail of every intermediate result
- Debugging by inspecting specific artifacts rather than re-running the full pipeline

### Process Engineering

Identified and eliminated inefficiencies through data-driven analysis:

- **12→4 agent consolidation** — Original architecture specified 12 agents. Production data showed they always ran sequentially by one operator, so I simplified to 4 (one per pipeline stage)
- **8→4 stage consolidation** — Sub-stages within Writing and Review always ran together, so I consolidated them
- **FULL mode as default** — Separate DRAFT/REVIEW/PUBLISH modes were useful during development but unnecessary during production. Default to FULL eliminated mode-switching overhead

### Governance Design

Built a governance model that balances control with efficiency:

- **Binary gates** eliminate subjective quality assessments
- **Convention Validation Protocol** prevents false conventions from accumulating
- **Arithmetic Verification Protocol** prevents false blockers from eroding trust in the quality system
- **Per-batch tagging** provides rollback points without heavyweight branching

### Risk Controls

The operational map memory artifact directly addresses the highest-severity error class in structured products documentation: **system mapping errors**. An incorrect system reference (e.g., stating a product is booked in Murex when it's actually in NEMO) is an operational risk that could propagate to trade booking, risk calculation, and P&L attribution. By establishing system mappings once per family and reusing them consistently, this error class was eliminated.

### Scalability

The framework extraction demonstrates scalable thinking:

- **v1 framework** — Domain-specific templates and guides tied to the Desk Bible
- **v2 framework** — Domain-agnostic methodology with adaptation examples for 7 new domains
- **Maturity assessment** — Clear Level 4 (Optimised) rating with documented gaps to Level 5 (Scalable)

---

## 7. Transferable Skills

### Model Risk Management

| Desk Bible Skill | MRM Application |
|-----------------|-----------------|
| Multi-gate quality control | Model validation workflows (back-testing, benchmarking, sensitivity) |
| Arithmetic verification protocol | Model output verification and tolerance thresholds |
| Convention validation | Model assumption validation (observe → validate → approve) |
| Memory layer | Model inventory metadata management |
| Audit trail | SR 11-7 / SS1/23 compliance documentation |
| Pipeline architecture | Model lifecycle management (development → validation → monitoring) |

### Risk Governance

| Desk Bible Skill | Risk Governance Application |
|-----------------|---------------------------|
| Binary quality gates | Risk assessment sign-off workflows |
| Checkpoint system | Risk decision audit trail |
| Cross-reference validation | Risk taxonomy consistency |
| Dashboard and reporting | Risk metrics dashboards, KRI monitoring |
| Release management | Policy version control and rollout |

### Banking Controls

| Desk Bible Skill | Controls Application |
|-----------------|---------------------|
| Operational mapping | Control mapping to business processes |
| Gate-based approval | Maker-checker workflows |
| FP suppression | Exception management and known-issue tracking |
| Batch processing | Bulk control testing and assessment |
| Governance model | Three lines of defence documentation |

### Documentation Governance

| Desk Bible Skill | Documentation Application |
|-----------------|--------------------------|
| Catalog-driven content | Document registry and lifecycle management |
| Memory-driven consistency | Style guide enforcement at scale |
| Maintenance guide | Knowledge transfer and succession planning |
| Annual review process | Periodic document review and attestation |
| Release packaging | Controlled document distribution |

### AI Risk Management

| Desk Bible Skill | AI Risk Application |
|-----------------|---------------------|
| Output verification protocol | AI model output validation |
| Convention validation | AI bias detection (observe → validate → flag) |
| Tolerance thresholds | Acceptable deviation ranges for AI outputs |
| Audit trail | AI decision documentation for explainability |
| Framework extraction | AI governance framework design |

### Process Improvement

| Desk Bible Skill | Process Application |
|-----------------|---------------------|
| Pipeline design | End-to-end process mapping and optimisation |
| Token cost analysis | Process cost measurement and reduction |
| Memory reuse metrics | Knowledge management ROI quantification |
| Retrospective methodology | Structured post-implementation review |
| Maturity assessment | Process maturity evaluation (CMM-style) |

---
---

# FORMAT 2: ONE-PAGE EXECUTIVE SUMMARY

---

## Structured Products Desk Bible — Executive Summary

**Objective:** Eliminate knowledge concentration risk on a structured products trading desk by creating a comprehensive, auditable, and maintainable documentation system using AI-driven governance.

**Scale:** 28 structured products across 5 families (Equity-Linked Notes, Securitisation & Repackaging, Credit-Linked Notes, Steepener Notes, Swaps), producing 280+ governed artifacts.

**Approach:** Designed a 4-stage pipeline (Research → Write → Review → Publish) with per-family memory artifacts for consistency, three independent quality gates for accuracy, and Git-based version control for auditability. Every intermediate result is a file on disk — the system is fully resumable, auditable, and maintainable.

**Results:**

| Metric | Outcome |
|--------|---------|
| Completion | 28/28 products (100%) |
| Accuracy errors | 0 blockers |
| Style violations | 0 must-fix |
| Broken references | 0 |
| Retries (Batch 1+) | 0 across 22 products |
| Memory reuse ratio | 4.6:1 (15 created, 69 reused) |
| Per-unit cost | ~14,866 tokens (stable ±0%) |
| Total cost | ~416K tokens |
| Final document | 2,821 lines |

**Strategic Value:**
- **Risk reduction** — System mapping errors (highest-severity class) eliminated through memory-driven consistency
- **Scalability** — Framework extracted into domain-agnostic methodology with 7 documented adaptation domains
- **Governance** — Binary quality gates, full audit trail, and maintenance runbook enable regulatory and audit readiness
- **Efficiency** — Memory reuse reduced per-unit cost by 20–30% from the second batch onward

**Transferable to:** Model Risk Management, Risk Governance, Banking Controls, Regulatory Compliance, AI Governance, Process Improvement.

---
---

# FORMAT 3: RESUME BULLET POINTS

---

## Structured Products Desk Bible — Resume Lines

**For a "Projects" or "Key Achievements" section:**

- Designed and delivered an AI-governed documentation system covering 28 structured products across 5 families, generating 280+ quality-controlled artifacts with zero defects (0 accuracy blockers, 0 style violations, 0 broken references) across all published content

- Architected a 4-stage pipeline with per-family memory layer achieving 4.6:1 reuse ratio and 20–30% cost reduction, maintaining stable per-unit cost of ~14,866 tokens regardless of product complexity

- Built a three-gate quality control framework (accuracy verification, style enforcement, cross-reference validation) with arithmetic verification protocol and false-positive suppression, achieving 100% gate pass rate across 28 products

- Extracted domain-agnostic Knowledge Bible Framework from production evidence, with documented adaptation paths for 7 domains including Model Risk Management, Credit Risk, and Regulatory Compliance

- Designed governance model with Git-based version control (11 milestone tags), checkpoint-based audit trail, and 10-section maintenance guide enabling knowledge transfer to future operators with no prior context

**For a "Skills" or "Technologies" section:**

- AI system design, multi-agent architecture, pipeline engineering, quality gate design, memory-based consistency management, governance framework development, process optimisation, documentation at scale

---
---

# FORMAT 4: LINKEDIN PROJECT DESCRIPTION

---

## Structured Products Desk Bible — LinkedIn

**Title:** AI-Driven Knowledge Governance System for Structured Products

**Description:**

Designed and delivered a comprehensive Desk Bible covering 28 structured products across 5 families (ELN, SRT, CLN, STEG, Swaps) using an AI-powered documentation pipeline.

The system addresses a common problem in trading desks: critical operational knowledge — how products are booked, priced, and reconciled — is distributed across individuals and lost when they leave. This creates onboarding delays, operational risk, and audit exposure.

My approach: a 4-stage pipeline (Research → Write → Review → Publish) with three independent quality gates, a per-family memory layer for consistency, and artifact-based state management for full auditability.

Results:
- 28/28 products delivered, 280+ governed artifacts
- Zero accuracy errors, zero style violations, zero broken references
- Memory reuse ratio of 4.6:1, reducing cost by 20–30%
- Stable per-unit cost regardless of product complexity
- Complete audit trail with Git version control and checkpoint files

Following delivery, I extracted the methodology into a domain-agnostic Knowledge Bible Framework with adaptation guides for Model Risk Management, Credit Risk, Operational Risk, Regulatory Compliance, Banking Operations, and more.

The project demonstrates system design thinking, process engineering, quality governance, and the practical application of AI to knowledge management at scale.

---
---

# FORMAT 5: INTERVIEW TALKING POINTS

---

## Structured Products Desk Bible — Interview Talking Points

### Opening (30 seconds)

"I designed an AI-governed documentation system that produced a comprehensive Desk Bible for a structured products desk — 28 products, 5 families, 280+ quality-controlled artifacts, zero defects. Then I extracted the methodology into a reusable framework applicable to any knowledge domain."

---

### Problem Statement

"Trading desks have a knowledge concentration problem. Critical operational knowledge — which systems book which products, how pricing ties to risk, what the reconciliation breaks look like — lives in people's heads. When they leave, the knowledge leaves too. That creates real operational risk and makes onboarding painfully slow."

---

### Why This Was Hard

"Three things made it hard. First, **consistency at scale** — 28 products across 5 families, each with different booking systems and conventions. You can't just write 28 independent pages and expect consistency. Second, **quality assurance** — financial documentation errors carry operational risk. A wrong system mapping could cause a product to be booked incorrectly. Third, **auditability** — you need a clear trail showing what was produced, what checks were applied, and that the checks actually caught something."

---

### My Approach

"I designed a 4-stage pipeline — Research, Write, Review, Publish — where every stage produces a file on disk. No in-memory state. That meant the system could be interrupted and resumed at any point, which turned out to be critical since the project ran across 4 sessions.

I built a per-family memory layer — three artifacts per family covering terminology, system mappings, and style rules. You create these once during a bootstrap phase, then every subsequent product in the family reuses them automatically. That drove consistency and reduced cost by 20–30%.

For quality, I built three independent gates. The most important lesson was the arithmetic verification protocol: you must computationally reproduce every calculation before raising it as an error. Without that, the system was generating false blockers for arithmetic that was actually correct within rounding tolerance."

---

### Results I'd Highlight

"Four numbers I'd emphasise:

1. **Zero defects** — zero accuracy blockers, zero style violations, zero broken references across all 28 products
2. **Zero retries** from the second batch onward — 22 products went through the pipeline once and passed all gates on the first attempt
3. **4.6:1 memory reuse ratio** — 15 artifacts created, reused 69 times
4. **Stable unit cost** — ~14,866 tokens per product regardless of complexity, from the simplest floating-rate note to the most complex synthetic CDO tranche"

---

### Strategic Thinking (for leadership-level conversations)

"What I'm most proud of is the system design, not just the output. Three decisions mattered most:

1. **Files on disk as state** — not a database, not in-memory. This made the system resumable, debuggable, and auditable. When something looked wrong, I could inspect the exact artifact that produced it.

2. **Convention validation protocol** — observe a pattern once, validate it twice, then enshrine it. This prevented the memory layer from accumulating errors over time.

3. **Binary quality gates** — PASS or FAIL, nothing in between. Subjective quality assessments drift over time and across reviewers. Binary gates don't."

---

### Framework Extraction (for AI governance or scalability questions)

"After delivery, I extracted the methodology into a domain-agnostic framework. The core insight is that the pipeline, memory layer, and quality gates are invariant across domains. What changes is the content of the memory artifacts and the accuracy gate's domain-specific checks.

I documented adaptation paths for 7 domains: Model Risk Management, Credit Risk, Operational Risk, Regulatory Compliance, Banking Operations, Knowledge Management, and SOPs. Each has a worked example showing families, sections, memory artifacts, and review gates."

---

### For Model Risk Management interviews specifically

"The architecture maps directly to model risk governance:

- My quality gates are analogous to model validation workflows — back-testing, benchmarking, sensitivity analysis
- The arithmetic verification protocol is analogous to model output verification with tolerance thresholds
- The convention validation protocol parallels model assumption validation — you don't approve an assumption the first time you see it
- The memory layer is analogous to a model inventory that stores metadata and ensures consistency across the model landscape
- The full audit trail supports SR 11-7 and SS1/23 expectations for documentation"

---

### For "What would you do differently?" questions

"Three things I'd simplify from the start:

1. The original architecture had 12 agents — production data showed 4 were sufficient. I'd start with 4.
2. I had 4 execution modes — production used only one (FULL). I'd default to FULL and keep a REVIEW-only mode as a fallback.
3. The dashboard was manually updated — I'd script it from the catalog and checkpoint files."

---

### For "How does this demonstrate leadership?" questions

"This project required making architectural decisions under uncertainty, then validating or correcting them with data. The arithmetic verification protocol came from a Batch 0 failure — the quality gate was raising false blockers. I didn't just patch around it; I designed a protocol with a defined tolerance threshold and applied it retroactively. Zero false blockers from that point forward.

The framework extraction demonstrates strategic thinking — I didn't just deliver the desk bible, I extracted the reusable methodology. That turns a one-time project into institutional capability."

---
---

# FORMAT 6: "TELL ME ABOUT A PROJECT YOU'RE PROUD OF"

---

## Response (2–3 minutes)

"The project I'm most proud of is a structured products Desk Bible I designed and delivered using an AI-driven documentation pipeline.

The problem was straightforward but hard to solve well: a trading desk's critical operational knowledge — how 28 different structured products are booked, priced, hedged, and reconciled — was distributed across people's heads. That's operational risk, onboarding friction, and audit exposure all rolled into one.

I designed a 4-stage pipeline — Research, Write, Review, Publish — where every intermediate result is a file on disk. That sounds like a simple decision, but it turned out to be the most important one. The project ran across 4 sessions, and because state lived in files rather than memory, zero work was ever lost. Any product could be re-run from any stage by checking which files existed.

The quality system had three independent gates: accuracy verification, style enforcement, and cross-reference validation. The key insight was the arithmetic verification protocol — you can't just flag an error, you have to computationally reproduce it. When I implemented that with a ±0.2% rounding tolerance, false blockers dropped to zero and stayed there for the remaining 22 products.

For consistency across the 28 products, I built a per-family memory layer. Three artifacts per family — terminology, system mappings, and style rules. You bootstrap them with the first product, validate them with the second, then every subsequent product reuses them automatically. That gave me a 4.6:1 reuse ratio and reduced cost by 20–30%.

The final numbers: 28 out of 28 products, 280+ artifacts, zero accuracy blockers, zero style violations, zero broken references, zero retries from the second batch onward. The assembled document was 2,821 lines.

But what I'm most proud of is what came after: I extracted the methodology into a domain-agnostic framework. The pipeline, memory layer, and quality gates work for any knowledge domain — I documented adaptation paths for 7 others, from Model Risk Management to SOPs. That turns a one-time deliverable into reusable intellectual property.

It's the kind of project that combines system design, process engineering, and governance — and every decision was validated by data, not just intuition."

---
---

# APPENDIX: KEY METRICS REFERENCE

Quick-reference table for citing specific numbers in conversations.

| Category | Metric | Value |
|----------|--------|-------|
| **Scale** | Products | 28 |
| | Families | 5 |
| | Artifacts | 280+ |
| | Assembled document | 2,821 lines |
| | Duration | 2 days, 4 sessions |
| **Quality** | Accuracy BLOCKERs | 0 |
| | Style MUST_FIX | 0 |
| | Broken cross-references | 0 |
| | Publishing failures | 0 |
| | Gate pass rate | 100% (all 3 gates, all 28 products) |
| | Retries (Batch 1+) | 0 across 22 products |
| **Memory** | Artifacts created | 15 |
| | Reuses | 69 |
| | Reuse ratio | 4.6:1 |
| | False positives suppressed | 84 |
| | Cost reduction from memory | 20–30% |
| **Efficiency** | Per-product cost | ~14,866 tokens |
| | Total cost | ~416,248 tokens |
| | Cost variance by complexity | ±0% |
| **Governance** | Git commits | 8 production |
| | Git tags | 11 |
| | Checkpoint files | 28 |
| | Pipeline logs | 28 |
| **Framework** | Guides (v2) | 9 |
| | Domain examples | 7 |
| | Templates | 8 |
| | Maturity level | Level 4 (Optimised) |
