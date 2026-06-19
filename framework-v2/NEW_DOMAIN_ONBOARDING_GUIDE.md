# New Domain Onboarding Guide

How to adapt the Knowledge Bible Framework to a specific domain. This guide provides concrete examples for 7 domains, showing the decisions required for each.

---

## Adaptation Checklist

For any new domain, answer these 4 questions:

1. **What are the families?** How do entries group by shared operational context?
2. **What are the sections?** What structure does each entry page follow?
3. **What are the memory artifacts?** Terminology, operational maps, style conventions — what goes in each?
4. **What are the review gates?** What does the accuracy gate check in this domain?

---

## Domain 1 — Model Risk Management

**Scope:** Documentation of quantitative models (pricing, risk, capital, valuation) for model risk governance under SR 11-7 / SS1/23.

### Families

| Family | Description | Typical Entries |
|--------|-------------|-----------------|
| Pricing Models | Valuation and pricing models | Black-Scholes, Local Vol, Stochastic Vol, Copula |
| Risk Models | VaR, ES, stress testing | Historical VaR, Parametric VaR, Monte Carlo VaR |
| Capital Models | Regulatory capital | SA-CCR, FRTB-IMA, FRTB-SA, IRB |
| Credit Models | PD, LGD, EAD estimation | Logistic PD, Merton PD, Workout LGD |
| ALM Models | Interest rate risk in the banking book | NII simulation, EVE, Repricing gap |

### Section Structure

1. **Model Description** — What the model does, scope of application.
2. **Mathematical Specification** — Key equations, assumptions, parameters.
3. **Implementation** — Systems, libraries, data feeds, calibration.
4. **Validation Approach** — Back-testing, benchmarking, sensitivity analysis.
5. **Limitations & Compensating Controls** — Known weaknesses, when the model fails.
6. **Monitoring** — Ongoing performance metrics, triggers for re-validation.
7. **Model Risk Rating** — Materiality, complexity, reliability assessment.

### Memory Artifacts

| Type | Content |
|------|---------|
| **Terminology** | Model names (e.g., "SABR" not "sabr"), parameter names (sigma, rho), regulatory references (SR 11-7) |
| **Operational Map** | Model governance system (e.g., model inventory tool), production system where model runs, data sources |
| **Style Conventions** | Equation formatting, Greek letter usage, risk rating scale (1–5 or Low/Med/High) |

### Review Gates

| Gate | What It Checks |
|------|---------------|
| **Accuracy** | Mathematical specification correct. Validation results reproducible. Limitations section covers known failure modes. |
| **Style** | Consistent equation formatting. Regulatory citations in correct format. Risk rating follows the scale. |
| **CrossRef** | Model dependencies (e.g., a VaR model that uses a pricing model) are valid catalog entries. |

### Expected Outputs

~30–50 model entries across 5 families. Each entry: 7-section document page + 6 pipeline artifacts.

---

## Domain 2 — Credit Risk

**Scope:** Documentation of credit risk assessment frameworks, facility types, and portfolio management processes.

### Families

| Family | Description |
|--------|-------------|
| Corporate Lending | Term loans, revolvers, project finance |
| Trade Finance | Letters of credit, guarantees, supply chain finance |
| Counterparty Risk | OTC derivatives, repo, securities lending |
| Retail Credit | Mortgages, auto loans, credit cards |
| Portfolio Management | Concentration limits, stress testing, provisioning |

### Section Structure

1. **Facility Description** — Product definition, typical structure.
2. **Risk Assessment** — Key credit risk drivers, rating methodology.
3. **Exposure Calculation** — EAD, PFE, or drawn/undrawn methodology.
4. **Mitigation** — Collateral, guarantees, netting agreements.
5. **Monitoring** — Early warning indicators, review triggers.
6. **Regulatory Treatment** — Basel framework, risk weight, capital charge.
7. **Risk Summary** — One-line desk shorthand equivalent.

### Memory Artifacts

| Type | Content |
|------|---------|
| **Terminology** | Facility types (RCF, TL, LC), rating scales (AAA–D or 1–22), regulatory terms (SA-CR, IRB-A) |
| **Operational Map** | Credit origination system, limit management system, collateral management system |
| **Style Conventions** | Rating notation, exposure formatting (USD MM), regulatory citation format |

### Review Gates

| Gate | What It Checks |
|------|---------------|
| **Accuracy** | Exposure calculations correct. Regulatory treatment matches current Basel rules. |
| **Style** | Rating scale consistent. Currency notation per house standard. |
| **CrossRef** | Facility cross-references (e.g., a revolving facility referencing a term loan) are valid. |

### Expected Outputs

~25–40 entries across 5 families.

---

## Domain 3 — Operational Risk

**Scope:** Documentation of operational risk events, controls, and mitigation frameworks.

### Families

| Family | Description |
|--------|-------------|
| Internal Fraud | Unauthorized trading, theft, embezzlement |
| External Fraud | Cyber attacks, card fraud, identity theft |
| Employment Practices | Discrimination, harassment, workplace safety |
| Business Disruption | IT failures, natural disasters, pandemic |
| Process Management | Settlement failures, data entry errors, reporting |
| Clients & Products | Suitability, mis-selling, market manipulation |
| Damage to Assets | Physical damage, environmental liability |

### Section Structure

1. **Event Definition** — What the risk event is, Basel category.
2. **Causal Analysis** — Root causes, contributing factors.
3. **Control Framework** — Preventive and detective controls.
4. **Key Risk Indicators** — Metrics that signal elevated risk.
5. **Escalation** — Thresholds, reporting lines, regulatory notification.
6. **Loss Estimation** — Methodology for estimating potential and actual losses.
7. **Event Summary** — Severity and frequency assessment.

### Memory Artifacts

| Type | Content |
|------|---------|
| **Terminology** | Basel event types (Level 1/2/3), KRI abbreviations, control framework terms |
| **Operational Map** | GRC tool (e.g., Archer, ServiceNow), loss database, incident reporting system |
| **Style Conventions** | Severity scale, frequency scale, loss threshold formatting |

### Review Gates

| Gate | What It Checks |
|------|---------------|
| **Accuracy** | Basel categorization correct. Control descriptions match actual control inventory. |
| **Style** | Severity/frequency scales consistent. Loss thresholds in correct format. |
| **CrossRef** | Control dependencies across event types are valid. |

### Expected Outputs

~35–50 entries across 7 families.

---

## Domain 4 — Regulatory Compliance

**Scope:** Documentation of regulatory requirements, compliance obligations, and control mappings.

### Families

| Family | Description |
|--------|-------------|
| Prudential | Capital, liquidity, leverage (Basel, CRR, CRD) |
| Conduct | Market abuse, suitability, conflicts (MiFID, MAR) |
| AML/KYC | Anti-money laundering, sanctions, customer due diligence |
| Reporting | Regulatory reporting obligations (COREP, FINREP, MAS610) |
| Data & Privacy | GDPR, data protection, cross-border transfer |
| Recovery & Resolution | Recovery planning, resolution strategies (BRRD) |

### Section Structure

1. **Regulation** — Name, jurisdiction, effective date.
2. **Obligation** — What the regulation requires, in plain language.
3. **Scope** — Which entities, products, or activities are in scope.
4. **Control Mapping** — How the firm complies (policies, procedures, systems).
5. **Monitoring & Testing** — How compliance is verified.
6. **Reporting** — What must be reported, to whom, how often.
7. **Penalty & Enforcement** — Consequences of non-compliance.

### Memory Artifacts

| Type | Content |
|------|---------|
| **Terminology** | Regulation short names (CRR, MiFID II, MAR), article references (Art. 325), regulatory body names |
| **Operational Map** | Compliance management system, regulatory reporting tool, training platform |
| **Style Conventions** | Regulation citation format, article reference format, jurisdiction abbreviations |

### Review Gates

| Gate | What It Checks |
|------|---------------|
| **Accuracy** | Regulation citations correct. Effective dates current. Obligations match the actual regulation text. |
| **Style** | Citation format consistent. Jurisdiction abbreviations per house standard. |
| **CrossRef** | Regulation dependencies (e.g., CRD references CRR) are valid. |

### Expected Outputs

~30–60 entries across 6 families.

---

## Domain 5 — Banking Operations

**Scope:** Documentation of operational processes across front-to-back trade lifecycle and support functions.

### Families

| Family | Description |
|--------|-------------|
| Trade Lifecycle | Execution, confirmation, settlement, clearing |
| Corporate Actions | Dividends, coupons, redemptions, splits |
| Reconciliation | Cash, position, collateral, margin |
| Client Services | Onboarding, account maintenance, reporting |
| Payments | Wire transfers, SWIFT, real-time payments |
| Custody | Safekeeping, asset servicing, proxy voting |

### Section Structure

1. **Process Definition** — What the process does, trigger events.
2. **Workflow** — Step-by-step procedure with decision points.
3. **Systems & Tools** — Which systems support each step.
4. **Controls** — Maker-checker, reconciliation, approval authority.
5. **Exception Handling** — Common exceptions and resolution procedures.
6. **SLA & Metrics** — Service levels, KPIs, escalation thresholds.
7. **Process Summary** — One-line operational shorthand.

### Memory Artifacts

| Type | Content |
|------|---------|
| **Terminology** | Process names, system names (e.g., "TLM" for Trade Lifecycle Management), acronyms (SSI, SWIFT, T+1) |
| **Operational Map** | Processing systems, middleware, downstream consumers |
| **Style Conventions** | Workflow step numbering, SLA format, KPI notation |

### Review Gates

| Gate | What It Checks |
|------|---------------|
| **Accuracy** | Workflow matches actual process. Systems correctly identified. SLAs match contractual terms. |
| **Style** | Step numbering consistent. System names match production names. |
| **CrossRef** | Process dependencies (e.g., settlement references confirmation) are valid. |

### Expected Outputs

~30–50 entries across 6 families.

---

## Domain 6 — Internal Knowledge Base (Consulting / Professional Services)

**Scope:** Documentation of methodologies, frameworks, and reusable intellectual capital.

### Families

| Family | Description |
|--------|-------------|
| Methodologies | Engagement approaches, assessment frameworks |
| Industry Solutions | Sector-specific offerings and playbooks |
| Technical Standards | Technology stack, architecture patterns, coding standards |
| Delivery Frameworks | Project management, quality assurance, risk management |
| Regulatory Expertise | Domain-specific regulatory knowledge |

### Section Structure

1. **Overview** — What the methodology/framework does.
2. **Applicability** — When to use it, engagement types, industries.
3. **Methodology Steps** — Phased approach with deliverables per phase.
4. **Tools & Templates** — Supporting tools, templates, accelerators.
5. **Case Studies** — Anonymised examples of successful application.
6. **Common Pitfalls** — What goes wrong and how to avoid it.
7. **Expert Contacts** — Who to call for deep expertise.

### Memory Artifacts

| Type | Content |
|------|---------|
| **Terminology** | Methodology names, framework abbreviations, engagement type codes |
| **Operational Map** | Knowledge management platform, template repository, expert directory |
| **Style Conventions** | Branding guidelines, slide deck formatting, client-safe language rules |

### Review Gates

| Gate | What It Checks |
|------|---------------|
| **Accuracy** | Methodology steps match current best practice. Case studies are anonymised. Expert contacts are current. |
| **Style** | Branding compliant. Language is client-safe (no internal jargon in external-facing sections). |
| **CrossRef** | Methodology dependencies (e.g., an industry solution referencing a delivery framework) are valid. |

### Expected Outputs

~25–40 entries across 5 families.

---

## Domain 7 — Standard Operating Procedures (SOPs)

**Scope:** Step-by-step procedures for repeatable operational tasks.

### Families

| Family | Description |
|--------|-------------|
| IT Operations | System administration, deployments, incident response |
| Finance & Accounting | Month-end close, journal entries, reconciliations |
| HR Operations | Onboarding, offboarding, benefits administration |
| Risk & Compliance | Risk assessments, compliance testing, audit support |
| Facilities | Building access, equipment procurement, vendor management |

### Section Structure

1. **Purpose** — Why this SOP exists.
2. **Scope** — What it covers, what it doesn't.
3. **Responsibilities** — Who does what (RACI or similar).
4. **Prerequisites** — What must be true before starting.
5. **Procedure** — Numbered steps with decision points and screenshots where helpful.
6. **Exceptions & Escalation** — What to do when the normal procedure doesn't apply.
7. **Review History** — Version, date, reviewer, changes.

### Memory Artifacts

| Type | Content |
|------|---------|
| **Terminology** | Department names, system names, role titles |
| **Operational Map** | Ticketing system, approval workflow tool, document management system |
| **Style Conventions** | Step numbering format, screenshot captioning, RACI table format |

### Review Gates

| Gate | What It Checks |
|------|---------------|
| **Accuracy** | Steps are executable as written. System references match production. Prerequisites are complete. |
| **Style** | Step numbering consistent. Screenshots current. RACI tables complete. |
| **CrossRef** | SOP dependencies (e.g., an incident response SOP referencing a change management SOP) are valid. |

### Expected Outputs

~20–60 entries across 5 families.

---

## Adaptation Summary

| Domain | Families | Sections | Key Accuracy Check | Key Operational Map |
|--------|----------|----------|-------------------|---------------------|
| Model Risk | 5 | 7 | Math spec, validation results | Model inventory, production system |
| Credit Risk | 5 | 7 | Exposure calcs, regulatory treatment | Origination, limit management |
| Operational Risk | 7 | 7 | Basel categorization, control inventory | GRC tool, loss database |
| Regulatory Compliance | 6 | 7 | Regulation citations, effective dates | Compliance system, reporting tool |
| Banking Operations | 6 | 7 | Workflow accuracy, SLAs | Processing systems, middleware |
| Knowledge Base | 5 | 7 | Methodology steps, case anonymisation | KM platform, template repo |
| SOPs | 5 | 7 | Step executability, system references | Ticketing, approval workflow |

The framework's core (4-stage pipeline, 3 memory types, 3 review gates) is invariant across domains. What changes is the content of the memory artifacts, the section structure, and the accuracy gate's domain-specific checks.
