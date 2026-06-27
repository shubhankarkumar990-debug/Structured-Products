# Model Risk Management Gap Analysis

**Audit Phase**: 7 — Model Risk Management
**Scope**: Desk Bible v2 (22,620 lines, 49 products, 1,078 sections)
**Date**: 2026-06-25
**Verdict**: SIGNIFICANT GAPS — conceptual awareness present, operational framework absent

---

## 1. Executive Summary

The Desk Bible treats model risk as a *property of products* rather than a *discipline with its own processes*. Readers learn THAT models have limitations. They do not learn HOW model risk is governed, validated, approved, inventoried, or monitored. For a Trader or Structurer, this is adequate context. For anyone in Model Validation, Model Risk Management, or Quantitative Analytics governance, the Bible provides no operational guidance.

---

## 2. Term Frequency Evidence

| Term | Count | Assessment |
|------|------:|------------|
| Model Validation | 24 | Mentioned as a role/activity — never as a process |
| Model Risk | 33 | Discussed as a concept — never as a governance framework |
| Model Approval | 0 | Completely absent |
| Model Limitation | 0 | Discussed in prose (CDO chapter, options chapters) but the term itself never appears |
| Challenger Model | 0 | Completely absent |
| Benchmark Model | 0 | Completely absent |
| Backtesting | 0 | Completely absent |
| Benchmarking | 0 | Completely absent |
| Sensitivity Testing | 0 | Completely absent |
| Model Override | 0 | Completely absent |
| Expert Judgment | 0 | Completely absent |
| Model Inventory | 0 | Completely absent |
| Model Risk Rating | 0 | Completely absent |

**Total MRM operational terms: 0 out of 11 operational concepts present.**

---

## 3. What the Bible DOES Cover

### 3.1 Conceptual Model Risk Awareness (PRESENT)

The Bible successfully communicates that models have limitations. Specific examples:

| Location | Content | Quality |
|----------|---------|---------|
| §1.9 (Foundation) | Model risk primer — introduces the idea that models are approximations | Good conceptual introduction |
| CDO chapter | Gaussian copula limitations — why correlation assumptions fail in stress | Excellent practical discussion |
| Options chapters | Black-Scholes limitations — constant vol, no jumps, continuous hedging | Adequate for product context |
| §14 Desk Reality (per product) | Practical model concerns per product — what the model gets wrong | Strong — 49 instances |
| §5 Who Touches This Product | Lists "Quant" and "Model Validation" as roles | Present but thin |

### 3.2 Model Risk as a Role Reference (PRESENT)

"Model Validation" appears 24 times across the Bible, primarily in §5 (Who Touches This Product) sections. Typical usage: "Model Validation: Validates pricing model; reviews Greeks computation methodology; signs off on new product models."

This tells the reader WHO validates. It does not explain:
- What validation involves
- What criteria are used
- What documentation is produced
- What happens when a model fails validation
- How often revalidation occurs

---

## 4. What the Bible DOES NOT Cover

### 4.1 Model Validation Process

| Gap | Operational Reality | Bible Coverage |
|-----|---------------------|----------------|
| Validation methodology | Independent replication, benchmarking, sensitivity analysis, stress testing | Not discussed |
| Validation documentation | Model validation report, findings log, remediation plan | Not discussed |
| Validation triggers | New model, material change, periodic review, market event | Not discussed |
| Validation outcomes | Approved, Conditional Approval, Rejected, Decommissioned | Not discussed |
| Validation independence | Separation of model development from validation | Implied by listing separate roles, not explained |

**Impact**: A Model Validation analyst joining the team would know which products exist and roughly what models they use. They would not know how to validate a single one.

### 4.2 Model Approval and Governance

| Gap | Operational Reality | Bible Coverage |
|-----|---------------------|----------------|
| Model Approval Committee | Governance body that approves/rejects model use | Absent (0 mentions) |
| Approval prerequisites | Validation report, user attestation, limitation acknowledgment | Absent |
| Conditional approvals | Time-limited approvals with remediation requirements | Absent |
| Model change management | What constitutes a "material" vs "non-material" change | Absent |
| New Product Approval (model component) | MRM sign-off required for new product launch | Absent |

**Impact**: The Bible covers New Product Approval from a structuring perspective but omits the model governance component entirely.

### 4.3 Model Limitations Framework

| Gap | Operational Reality | Bible Coverage |
|-----|---------------------|----------------|
| Known limitations register | Documented list of model limitations per model | Absent as a concept |
| Limitation impact assessment | Quantified impact of each limitation (P&L, risk) | Absent |
| Limitation monitoring | Ongoing tracking of whether limitations are becoming material | Absent |
| Workarounds and reserves | Model reserves, manual adjustments for known gaps | Absent |

**Nuance**: The Bible DOES discuss limitations in prose — the CDO chapter on Gaussian copula is genuinely insightful. But these are educational explanations, not operational frameworks. A reader understands the problem but not the governance response.

### 4.4 Challenger and Benchmark Models

| Gap | Operational Reality | Bible Coverage |
|-----|---------------------|----------------|
| Challenger model concept | Alternative model used to validate primary model outputs | Absent (0 mentions) |
| Benchmark model | Simplified model used as a reasonableness check | Absent (0 mentions) |
| Model comparison framework | How to compare primary vs challenger output | Absent |
| Escalation criteria | When divergence between models triggers review | Absent |

**Impact**: For exotic products (autocallables, worst-of structures, CDOs), challenger models are essential to model governance. The Bible covers 49 products but never mentions how their models are cross-checked.

### 4.5 Backtesting

| Gap | Operational Reality | Bible Coverage |
|-----|---------------------|----------------|
| Backtesting methodology | Comparing model predictions to realized outcomes | Absent (0 mentions) |
| Backtesting frequency | Daily, monthly, quarterly depending on model tier | Absent |
| Backtesting exceptions | When backtest failures are acceptable vs require action | Absent |
| Regulatory backtesting | Basel requirements for VaR model backtesting | Absent |

**Impact**: Backtesting is mentioned 0 times in 22,620 lines. This is the most critical operational MRM gap. Every bank's MRM function backtests models regularly. The concept is entirely absent.

### 4.6 Model Inventory and Classification

| Gap | Operational Reality | Bible Coverage |
|-----|---------------------|----------------|
| Model inventory | Central register of all models in use | Absent (0 mentions) |
| Model tiering | Risk-based classification (Tier 1/2/3) determining governance intensity | Absent |
| Model risk rating | Quantified model risk score | Absent (0 mentions) |
| Model lineage | Tracking model versions, dependencies, upstream/downstream | Absent |

### 4.7 Expert Judgment and Model Override

| Gap | Operational Reality | Bible Coverage |
|-----|---------------------|----------------|
| Expert judgment | Formal process for overriding model output with human judgment | Absent (0 mentions) |
| Model override | Documented deviation from model output (e.g., marking an illiquid position) | Absent (0 mentions) |
| Override governance | Approval, documentation, time limits for overrides | Absent |
| Override monitoring | Tracking frequency, magnitude, and P&L impact of overrides | Absent |

**Impact**: Expert judgment and model overrides are used daily on every structured products desk. The Bible's silence on this topic is a significant gap for operational readiness.

### 4.8 Sensitivity Testing

| Gap | Operational Reality | Bible Coverage |
|-----|---------------------|----------------|
| Sensitivity analysis | Systematic variation of model inputs to understand output behavior | Absent (0 mentions) |
| Sensitivity reporting | Regular reports showing model sensitivity to key parameters | Absent |
| Parameter uncertainty | Quantifying confidence in model inputs (vol, correlation, recovery rates) | Discussed conceptually, not operationally |

---

## 5. Regulatory Context

| Regulation | Relevance to MRM | Bible Coverage |
|------------|-------------------|----------------|
| SR 11-7 / SS1/23 (Fed/PRA) | Defines model risk management requirements | Not mentioned |
| Basel (FRTB) | New market risk framework with model approval requirements | Basel mentioned 31 times, but not in MRM context |
| TRIM (ECB) | Targeted Review of Internal Models | Not mentioned |
| CRD V/CRR II | Capital requirements with model governance provisions | Not mentioned |

---

## 6. Gap Severity Matrix

| MRM Component | Conceptual Coverage | Operational Coverage | Gap Severity |
|---------------|:-------------------:|:--------------------:|:------------:|
| Model risk awareness | 7/10 | 1/10 | MODERATE |
| Model validation | 3/10 | 0/10 | CRITICAL |
| Model approval | 0/10 | 0/10 | CRITICAL |
| Model limitations | 5/10 | 0/10 | HIGH |
| Challenger/benchmark models | 0/10 | 0/10 | CRITICAL |
| Backtesting | 0/10 | 0/10 | CRITICAL |
| Model inventory | 0/10 | 0/10 | HIGH |
| Model risk rating | 0/10 | 0/10 | HIGH |
| Expert judgment/override | 0/10 | 0/10 | CRITICAL |
| Sensitivity testing | 0/10 | 0/10 | HIGH |

---

## 7. Audience Impact Assessment

| Role | Can learn their MRM responsibilities from the Bible? | Assessment |
|------|------------------------------------------------------|------------|
| Trader | Partially — understands model limitations but not governance obligations | PARTIAL |
| Structurer | Partially — knows models are approximate but not approval process | PARTIAL |
| Quant | No — no framework for model development governance | FAIL |
| Model Validator | No — no validation methodology, process, or documentation guidance | FAIL |
| Risk Manager | No — no MRM framework to monitor or enforce | FAIL |
| Product Control | No — no guidance on model reserves, IPV methodology, or override process | FAIL |
| Auditor | No — no inventory, no governance framework to audit against | FAIL |

---

## 8. Recommendation

The MRM gap cannot be closed within the existing product-chapter structure. Model risk management is an infrastructure discipline that spans all products. The recommended approach:

1. **Minimum**: Add a Foundation chapter (Part 0 or Part 2) covering MRM framework, model lifecycle, and governance
2. **Recommended**: Include MRM as a module in the proposed Infrastructure Handbook (see infrastructure_handbook_recommendation.md)
3. **Ideal**: Dedicated MRM reference covering validation, approval, backtesting, inventory, and regulatory requirements

Estimated content for minimum coverage: ~20-25 pages.
Estimated content for recommended coverage: ~35-40 pages as part of Infrastructure Handbook.
