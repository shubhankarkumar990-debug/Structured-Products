# Review Workflow and Production Agents

**Version:** 1.0
**Date:** 2026-06-19
**Purpose:** Define 8 production review agents and the workflow for reviewing each generated chapter

---

## 1. Review Workflow Overview

```
GENERATE          REVIEW PASS 1           REVIEW PASS 2          ACCEPT
   │              (Parallel)              (Sequential)              │
   │                                                                │
   ▼                                                                ▼
┌──────────┐    ┌─────────────────┐    ┌──────────────────┐    ┌──────────┐
│ Generate  │───▶│ Professor Agent │    │ Cross-Reference  │───▶│ Accept   │
│ Chapter   │    │ Jargon Police   │───▶│ Agent            │    │ or       │
│           │    │ Cognitive Load  │    │ Final Editor     │    │ Revise   │
│           │    │ Visual Design   │    │                  │    │          │
│           │    │ Practitioner    │    └──────────────────┘    └──────────┘
│           │    │ Product Accuracy│
│           │    └─────────────────┘
└──────────┘
```

### Workflow Steps

1. **Generate** the chapter following the Chapter Generation Standard
2. **Review Pass 1** (parallel): Run Professor, Jargon Police, Cognitive Load, Visual Design, Practitioner, and Product Accuracy agents simultaneously. Each produces a pass/fail verdict with specific findings
3. **Fix** any failures identified in Pass 1
4. **Review Pass 2** (sequential): Cross-Reference Agent verifies all dependencies and cross-references. Final Editor checks consistency, formatting, and voice
5. **Accept** if all checklist items pass. Record in Generation Dashboard
6. **Revise** if any item fails. Return to step 3

### Escalation Rule

If a chapter fails review more than twice on the same item, escalate:
- Flag the specific failure pattern
- Determine if the Chapter Generation Standard needs amendment
- Record the pattern in the Generation Dashboard for monitoring

---

## 2. Production Agent Definitions

### Agent 1: Professor Agent

**Objective:** Ensure every chapter teaches rather than merely documents. Verify that the professor's narrative voice, explanation hierarchy, and teaching quality meet the standard established in the pilot chapters.

**Review Criteria:**
- §1 opens with a concrete scenario involving a named person or entity with a specific need
- §2 contains one primary analogy that maps precisely to the product's core mechanic
- The analogy domain does not collide with any reserved domain (see Professor Voice Standard)
- The explanation hierarchy is followed: why → what → how (intuition) → how (formal) → risks → operations → application
- Professor Note in §7 captures the single most important insight
- §16 Common Mistakes address real misconceptions with corrective explanations
- The Feynman standard is met: every section is understandable given the dependency chain

**Pass/Fail Rules:**
- PASS: All criteria met. Voice is consistent with pilot chapters
- FAIL: Any of the following: §1 uses a generic opening ("consider an investor..."), analogy domain collision, Feynman violation (concept not explainable to a non-specialist given dependencies), Professor Note missing or generic, Common Mistakes are trivial

**Escalation Rules:**
- If the same voice inconsistency appears in 3+ consecutive chapters, flag for Professor Voice Standard review
- If an analogy domain collision cannot be resolved (all related domains exhausted), escalate for domain expansion

**Output Format:**
```
Agent: Professor Agent
Chapter: 5.X.Y [Product Name]
Verdict: PASS / FAIL
Items: E1, E2, E11, E12, C1, C2
Findings:
- [specific findings, if any]
Analogy domain used: [domain]
Feynman violations: [count and details]
```

---

### Agent 2: Visual Design Agent

**Objective:** Ensure every chapter meets the Visual Standard. Verify that inline diagrams follow conventions, payoff diagrams use correct axes, and Visual Learning Recommendations are complete and well-specified.

**Review Criteria:**
- §8 contains at least one ASCII payoff diagram or decision tree
- Payoff diagram axes follow the Visual Standard (correct labels for product domain)
- Barrier levels are labeled with percentage and the word "Barrier"
- ASCII diagrams do not exceed 60 characters width
- Decision tree uses correct conventions (top-down, YES/NO branches, box-drawing characters)
- 5 Visual Learning Recommendations are present with type, description, and priority
- At least 2 of 5 recommendations are P1 priority
- Timeline is present or specified as P1 for periodic/path-dependent products

**Pass/Fail Rules:**
- PASS: All applicable criteria met. Diagrams are readable and correctly labeled
- FAIL: Missing payoff diagram in §8, incorrect axis labels, fewer than 5 Visual Learning Recommendations, or no P1 recommendations for timeline/decision tree when product requires one

**Escalation Rules:**
- If a new visual type is needed that is not covered by the Visual Standard, flag for standard expansion
- If ASCII representation is inadequate for a product's payoff (e.g., 3D surface for correlation products), note the limitation and specify a production-only visual

**Output Format:**
```
Agent: Visual Design Agent
Chapter: 5.X.Y [Product Name]
Verdict: PASS / FAIL
Items: V1, V2, V3, V4, V5, V6, V7
Findings:
- Inline diagrams: [count and types]
- Axis compliance: [PASS/FAIL with details]
- Visual Recs: [count, P1 count]
- Timeline present/specified: [yes/no]
- Decision tree present/specified: [yes/no/N/A]
```

---

### Agent 3: Jargon Police Agent

**Objective:** Enforce the No Unexplained Terminology rule. Every technical term must be defined on first use or declared as a dependency. Zero tolerance for undefined jargon.

**Review Criteria:**
- Every technical term is either defined with a parenthetical on first use in the chapter OR listed in the Dependency References table
- All terms from the Jargon Watchlist that appear in the chapter are properly handled
- Three-barrier disambiguation rule is applied for multi-barrier products
- No abbreviation is used without expansion on first use in the chapter
- Dependency References table pointers are accurate (correct section numbers)

**Pass/Fail Rules:**
- PASS: Zero terminology violations. All watchlist terms handled. All dependencies declared
- FAIL: Any term appears without definition or dependency declaration. Any watchlist term left unhandled. Any bare "barrier" in a multi-barrier product

**Escalation Rules:**
- Any newly discovered undefined term not on the Jargon Watchlist must be added to the watchlist
- If a term cannot be reasonably defined in a parenthetical (too complex), escalate to determine if a dependency should be added to Parts 1-2

**Output Format:**
```
Agent: Jargon Police Agent
Chapter: 5.X.Y [Product Name]
Verdict: PASS / FAIL
Items: E4, E5, E6
Violations: [count]
Details:
- [term]: [location] — [undefined / watchlist miss / disambiguation failure]
Watchlist additions: [any new terms to add]
```

---

### Agent 4: Cognitive Load Agent

**Objective:** Ensure no section overloads the reader with too many new concepts without reinforcement. Verify that the cognitive load pattern (teach → reinforce → advance) is maintained.

**Review Criteria:**
- No section introduces more than 5 new concepts without a reinforcement device between them
- Reinforcement devices are deployed appropriately: examples after abstract concepts, diagrams after spatial concepts, tables after multi-attribute comparisons
- §5 (What Happens If) provides concrete reinforcement before the technical sections begin
- §12 (Worked Example) provides application reinforcement after the technical sections
- The chapter's overall concept count is appropriate for its complexity level

**Pass/Fail Rules:**
- PASS: No section exceeds the 5-concept-without-reinforcement limit. Reinforcement devices are well-placed
- FAIL: Any section introduces 6+ concepts without a reinforcement device. §5 or §12 is abstract rather than concrete

**Escalation Rules:**
- If a product inherently requires 6+ concepts in a single section (e.g., Synthetic CDO Tranche with correlation, tranching, attachment/detachment points, base correlation), flag the section and recommend a sub-section split
- If multiple chapters in the same family fail on the same overload pattern, review whether the template needs a family-specific adaptation

**Output Format:**
```
Agent: Cognitive Load Agent
Chapter: 5.X.Y [Product Name]
Verdict: PASS / FAIL
Items: E3
Concept count by section:
- §1: [count]  §2: [count]  ...  §16: [count]
Overload sections: [none / section numbers with counts]
Reinforcement device coverage:
- Examples: [count]
- Diagrams: [count]
- Tables: [count]
- Analogies: [count]
```

---

### Agent 5: Practitioner Agent

**Objective:** Ensure every chapter prepares the reader for actual desk work. Verify that booking, reconciliation, desk perspective, interview preparation, and knowledge assessment content is accurate and operationally actionable.

**Review Criteria:**
- §10 specifies the correct booking system and Four-Leg applicability
- §10 Desk Perspective table has 5 rows (Trader, Structurer, Product Control, Risk, Operations) with product-specific content
- §11 contains 5 reconciliation red flags that are operationally actionable (not theoretical)
- §13 contains 5 interview questions progressing from recall to reasoning
- Knowledge Check has the correct structure (5 review + 3 scenario + 1 desk)
- SRT/STEG chapters describe all four legs
- System routing matches the System Accuracy table in the Chapter Generation Standard

**Pass/Fail Rules:**
- PASS: All criteria met. Desk Perspective rows are non-generic. Red flags are actionable. System routing is correct
- FAIL: Wrong booking system, generic Desk Perspective, fewer than 5 red flags, incorrect Four-Leg assignment, or Knowledge Check structure wrong

**Escalation Rules:**
- If a product's system routing is ambiguous (e.g., a hybrid product), flag for explicit routing decision
- If Desk Perspective content for a role is genuinely the same as another product in the same family, document the overlap and justify

**Output Format:**
```
Agent: Practitioner Agent
Chapter: 5.X.Y [Product Name]
Verdict: PASS / FAIL
Items: P1, P2, P3, P4, P5, P6, P7, P8
System routing: [correct/incorrect — expected: X, found: Y]
Four-Leg: [correct/incorrect]
Desk Perspective specificity: [all specific / rows N generic]
Red flags: [count, actionable assessment]
Knowledge Check structure: [5+3+1 / incorrect]
```

---

### Agent 6: Product Accuracy Agent

**Objective:** Verify that the product description, construction, payoff logic, and worked examples are technically correct. This agent checks financial accuracy, not teaching quality.

**Review Criteria:**
- §6 (Formal Definition) accurately describes the product's legal and economic structure
- §7 (Product Construction) correctly decomposes the product into components (bond + derivative(s))
- §7 arithmetic is correct (coupon = bond interest + option premium - FTP - margin)
- §8 (Payoff Logic) correctly describes the payoff at maturity for all scenarios
- §5 (What Happens If) scenarios are consistent with the payoff logic in §8
- §9 (Key Risks) correctly identifies the product's risk profile
- §12 (Worked Example) arithmetic is correct and internally consistent

**Pass/Fail Rules:**
- PASS: All financial content is technically correct. Decomposition is accurate. Arithmetic checks out. Scenarios are consistent with payoff logic
- FAIL: Any factual error in product definition, construction, payoff, risk, or worked example arithmetic

**Escalation Rules:**
- If a product's construction cannot be expressed as simple arithmetic (e.g., Phoenix requires Monte Carlo), note this limitation and verify the qualitative description is accurate
- If a risk is identified that is not in the Key Risks table, add it

**Output Format:**
```
Agent: Product Accuracy Agent
Chapter: 5.X.Y [Product Name]
Verdict: PASS / FAIL
Items: E9, E10
Accuracy checks:
- Definition: [correct/incorrect]
- Construction: [correct/incorrect]
- Payoff logic: [correct/incorrect]
- Scenario consistency: [consistent/inconsistent]
- Worked example arithmetic: [correct/incorrect — show calculation]
- Risk completeness: [complete / missing: ...]
```

---

### Agent 7: Cross-Reference Agent

**Objective:** Verify that all cross-references, dependency declarations, and section numbers are accurate. Ensure the chapter connects correctly to the rest of the document.

**Review Criteria:**
- Dependency References table is present and complete
- All section number references reflect the current numbering (post-1.7/1.8/1.9 split)
- "How This Differs From..." bridge is present for within-family chapters (2nd+ product)
- Family transition text is present for the first product in each family
- All references to other chapters or sections point to correct locations
- No concept is used that is not either defined in-chapter or declared in the Dependency References

**Pass/Fail Rules:**
- PASS: All cross-references are accurate. Dependency table is complete. Bridge/transition text is present where required
- FAIL: Any incorrect section number, missing dependency, or missing bridge/transition where required

**Escalation Rules:**
- If a concept is used that is not taught in Parts 0-4 and cannot be reasonably defined in a parenthetical, escalate to determine if Parts 0-4 need an addition
- If the section numbering changes (Parts 0-4 revision), flag all affected Dependency References for batch update

**Output Format:**
```
Agent: Cross-Reference Agent
Chapter: 5.X.Y [Product Name]
Verdict: PASS / FAIL
Items: E7, E8, C7, C8
Dependency table entries: [count]
Section number accuracy: [all correct / errors in: ...]
Bridge text: [present / missing / N/A]
Transition text: [present / missing / N/A]
Undeclared dependencies: [none / list]
```

---

### Agent 8: Final Editor Agent

**Objective:** Final quality gate. Check consistency, formatting, voice, and compliance with all standards. This agent runs last and catches anything the specialized agents missed.

**Review Criteria:**
- Chapter length is between 1,800 and 3,500 words
- All 16 sections present in correct order
- All 5 additional requirements present (Professor Note, Desk Perspective, Knowledge Check, Visual Learning Recs, Dependency References)
- Chapter title follows format: `### 5.X.Y Product Name`
- No forbidden writing patterns from the Professor Voice Standard
- ASCII diagrams do not exceed 60 characters width
- Tables do not exceed 8 columns
- Professor Note starts with "If you remember only one thing..."
- Sentence complexity is within targets (no sentence > 40 words)
- Formatting is consistent (bold section labels, consistent table alignment)

**Pass/Fail Rules:**
- PASS: All formatting, length, structure, and voice checks pass
- FAIL: Any structural element missing, any forbidden pattern detected, length out of range, or formatting inconsistency

**Escalation Rules:**
- If a chapter exceeds 3,500 words due to inherent product complexity, review whether the chapter should be split or whether the limit should be raised for that product
- If a forbidden writing pattern appears to be unavoidable for a specific context, document the exception

**Output Format:**
```
Agent: Final Editor Agent
Chapter: 5.X.Y [Product Name]
Verdict: PASS / FAIL
Items: C2, C3, C4, C5, C6, C9, C10
Word count: [count]
Sections present: [16/16]
Additional requirements: [5/5]
Forbidden patterns detected: [none / list with locations]
Formatting issues: [none / list]
```

---

## 3. Book-Level Review Agents

These agents run after an entire batch is complete. They assess cross-chapter quality, not individual chapter quality.

---

### Agent 9: Master Book Editor

**Objective:** Detect duplication across chapters — repetitive explanations, repeated analogies, overlapping examples, unnecessary chapter length, and structural inconsistencies between chapters within the same batch and across the full book.

**Review Criteria:**
- No analogy domain is used in more than one chapter
- No worked example uses the same stock, notional, and scenario as another chapter
- No section repeats a paragraph-level explanation that already exists in another chapter (paraphrasing is fine; copy-paste is not)
- Structural elements (table formats, section headings, Knowledge Check structure) are consistent across all chapters in the batch
- Chapter lengths are proportional to product complexity — simpler products should not be longer than complex ones
- "How This Differs" bridges do not repeat content that is already in the referenced chapter

**Output Format:**
```
Agent: Master Book Editor
Batch: [N]
Chapters Reviewed: [list]
Verdict: PASS / FAIL
duplication_findings:
  - [finding 1: chapters affected, content duplicated]
structural_findings:
  - [finding 1: inconsistency description]
consistency_findings:
  - [finding 1: format or convention drift]
recommendations:
  - [recommendation 1]
```

---

### Agent 10: Beginner Reader

**Objective:** Simulate a motivated 15-year-old reading the batch. Identify confusion points, intimidating terminology, sections that feel too academic, sections that feel boring, and concepts that need additional examples or visuals to land.

**Review Criteria:**
- Can each chapter be understood in sequence by someone who has read Parts 0-4 and the preceding chapters?
- Are there sections where the difficulty spikes without a bridge or reinforcement device?
- Are there stretches longer than 200 words without a concrete example, table, or diagram?
- Do the analogies land for a non-finance reader, or do they assume domain knowledge?
- Are the "What Happens If" scenarios vivid enough to create genuine understanding?
- Does each chapter make the reader curious about the next product, or does it feel like a chore?

**Output Format:**
```
Agent: Beginner Reader
Batch: [N]
Chapters Reviewed: [list]
Verdict: PASS / NEEDS IMPROVEMENT
confusion_points:
  - [chapter, section, what's confusing and why]
terminology_issues:
  - [term, chapter, why it's intimidating or unclear]
engagement_issues:
  - [chapter, section, why it feels dry or academic]
recommendations:
  - [specific suggestion to improve clarity or engagement]
```

---

### Agent 11: Final Publication Agent

**Objective:** Assess publication readiness of the batch — glossary extraction, acronym indexing, figure indexing, chapter sequencing integrity, cross-reference integrity across the batch, interview question indexing, and operations reference extraction.

**Review Criteria:**
- Every technical term defined in the batch could be extracted for a glossary (definition is findable in the chapter text)
- Every acronym used is expanded on first use in each chapter where it appears
- Every ASCII diagram and table could be assigned a figure number for a future index
- Chapter numbering is sequential and correct (no gaps, no duplicates)
- Cross-references between chapters in the batch are accurate (section numbers, product names)
- Interview questions do not duplicate across chapters in the batch
- Reconciliation red flags are distinct across chapters (no repeated flags unless the operational concern is genuinely shared)

**Output Format:**
```
Agent: Final Publication Agent
Batch: [N]
Chapters Reviewed: [list]
Verdict: READY / NOT READY
glossary_items:
  - [term: definition location (chapter, section)]
index_items:
  - [acronym: expansion, chapters where used]
publication_findings:
  - [finding: description]
recommendations:
  - [recommendation]
```

---

## 4. Review Timing

### Chapter-Level Review

| Phase | Agents | Mode | Purpose |
|-------|--------|------|---------|
| Pass 1 | Professor, Jargon Police, Cognitive Load, Visual Design, Practitioner, Product Accuracy | Parallel | Content quality and accuracy |
| Fix | — | — | Address all Pass 1 failures |
| Pass 2 | Cross-Reference, Final Editor | Sequential | Structural integrity and final polish |
| Accept/Revise | — | — | Record in dashboard or return to Fix |

**Target review time per chapter:** Pass 1 findings within the generation pass. Fix and Pass 2 immediately after. Total: integrated into the generation workflow, not a separate phase.

### Book-Level Review

| Phase | Agents | Mode | Purpose |
|-------|--------|------|---------|
| Batch Complete | Master Book Editor | Sequential | Cross-chapter duplication and consistency |
| Batch Complete | Beginner Reader | Sequential | Accessibility and engagement |
| Batch Complete | Final Publication Agent | Sequential | Publication readiness |

**Timing:** Book-level agents run only after all chapters in a batch have passed chapter-level review. Their findings may trigger revisions to individual chapters.

---

*Workflow effective 2026-06-19. Updated 2026-06-19 to add book-level agents (9-11). All chapters generated after this date follow this review process.*
