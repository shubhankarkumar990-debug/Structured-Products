# Professor Voice Standard

**Version:** 1.0
**Date:** 2026-06-19
**Scope:** All written content in Desk Bible v2 — Parts 0-7 and all product chapters
**Voice benchmark:** Part 0 (narrative), Part 2 Section 2.2 (applied teaching), Part 5.1.1 PPN (product chapter)

---

## 1. Narrative Style

### The Voice

The Desk Bible is written by a single professor — a senior practitioner who has spent 20 years on a structured products desk and now teaches. This professor:

- **Knows the material deeply** but remembers what it was like not to know it
- **Teaches by building intuition first**, then formalizing
- **Uses stories and analogies** to anchor abstract concepts to familiar experiences
- **Is honest about complexity** — never pretends something difficult is simple, but always makes the difficult accessible
- **Respects the reader** — assumes intelligence, does not assume knowledge
- **Is direct** — states facts clearly, does not hedge unnecessarily

### Register

| Context | Register | Example |
|---------|----------|---------|
| Opening scenarios (§1) | Warm, conversational | "Maya has saved $200,000 for a house deposit..." |
| Analogies (§2) | Vivid, concrete | "Think of a seat belt in a car..." |
| Why/What sections (§3-5) | Clear, client-facing | "Investors buy this product because..." |
| Technical sections (§6-11) | Authoritative, precise | "The redemption amount is calculated as..." |
| Reinforcement (§12-16) | Teaching, corrective | "The most common mistake is believing that..." |
| Professor Notes | Singular, distilled | "If you remember only one thing..." |

The register should vary within a chapter (warm opening → technical middle → teaching close) but remain consistent across chapters. A reader should feel the same person wrote every chapter.

---

## 2. Sentence Complexity

### Targets

| Metric | Target | Hard Limit |
|--------|:------:|:----------:|
| Average sentence length | 15-25 words | — |
| Maximum single sentence | — | 40 words |
| Average paragraph length | 3-5 sentences | 7 sentences |
| Concepts per sentence | 1 | 2 (with conjunction) |

### Sentence Patterns

**Preferred:**
- Simple declarative: "A Reverse Convertible is a bond combined with a short put option."
- Cause-effect: "Because the investor is selling a put, the coupon is higher than a plain bond."
- Contrast: "Unlike a PPN, a Reverse Convertible does not guarantee the investor's principal."

**Acceptable:**
- Compound with one conjunction: "The investor earns the coupon regardless of market performance, but may lose principal if the barrier is breached."
- Conditional: "If the underlying falls below the barrier at any point during the product's life, the knock-in put activates."

**Forbidden:**
- Triple-clause: ~~"The investor, who has purchased the note from the issuer, which is typically an SPV, receives coupons that are funded by the option premium."~~
- Parenthetical chains: ~~"The CDS spread (the annual fee paid by the protection buyer (typically a bank) to the protection seller (often an investor via a CLN)) represents..."~~

### The "Read Aloud" Test

Every sentence should sound natural when read aloud. If a sentence requires the reader to backtrack to parse its structure, it is too complex. Split it.

---

## 3. Analogy Rules

### Requirements

1. **Every product chapter must have exactly one primary analogy** introduced in §2 (Real World Analogy)
2. **The primary analogy must map precisely** to the product's core mechanic. If the analogy breaks under scrutiny, it is not good enough
3. **The primary analogy must be maintained** through the Mental Models table (§14)
4. **No analogy domain may be reused** across chapters. Each product gets a unique analogy domain
5. **Analogies must be accessible** to a reader with no finance background. No analogies from specialized domains (medicine, law, engineering) unless explained

### Analogy Quality Checklist

| Criterion | Requirement |
|-----------|------------|
| Precision | The analogy maps to the core mechanic, not just the general concept |
| Extensibility | The analogy can accommodate 2-3 product details beyond the core mechanic |
| Memorability | A reader could recall the analogy a week later |
| Independence | The analogy does not rely on knowledge from another chapter's analogy |
| No collision | The analogy domain is not used elsewhere in the document |

### Used Analogy Domains (Reserved)

| Product | Analogy Domain | Core Mapping |
|---------|---------------|-------------|
| PPN | Seat belt / car safety | Protection that limits upside participation |
| RC | Earthquake insurance (selling) | Earning premium by taking catastrophe risk |
| Phoenix | Employment contract | Conditional performance bonuses with memory |
| IRS | Crop exchange (farmer/baker) | Two parties swapping what each produces |
| CLN | Bail bondsman | Posting collateral against someone else's default |
| Part 0 concepts | Village marketplace, bakery, lending to a friend, savings vs startup, restaurant (FO/MO/BO) | Reserved — do not reuse |
| Part 1 concepts | Restaurant reservation (call), painting insurance (put), tripwire (barrier), light switch (digital), melting ice cream (theta), sailors (volatility), weather forecast (implied vol), orchestra (correlation), neighbor lending (credit), road map (model risk), water treatment (four-leg) | Reserved — do not reuse |

### Forbidden Analogy Patterns

- **Definition-as-analogy:** "A cap is like a maximum price guarantee." This restates the definition in different words. An analogy must connect to something the reader already knows outside of finance
- **Analogy chains:** "Think of it like a cap, which is like a ceiling, which is like a limit." One mapping only
- **Breaking analogies:** "This is like insurance, except you can buy insurance on something you don't own." If the analogy requires an "except," either fix the analogy or acknowledge the limitation explicitly

---

## 4. Story Requirements

### Section 1 (Explain Like I'm New)

Every chapter must open with a concrete scenario. The scenario must include:

1. **A named person or entity** with a specific situation (not "consider an investor who...")
2. **A specific need or problem** that motivates the product
3. **Enough context** that a reader with no finance knowledge understands the situation
4. **A natural bridge** to §2 (the analogy) or §3 (the problem statement)

### Story Quality Checklist

| Criterion | Requirement | Example (PPN) |
|-----------|------------|---------------|
| Named protagonist | A person or entity with a name | "Maya has saved $200,000..." |
| Specific situation | A concrete, relatable scenario | "...for a house deposit. She wants growth but cannot afford to lose her savings" |
| Real need | The scenario creates a genuine problem | "A standard stock investment could grow her savings but also lose 30% in a downturn" |
| Product as solution | The product naturally emerges as the answer | "What if there were an investment that protected her $200,000 no matter what?" |

### Forbidden Opening Patterns

- ~~"A [Product Name] is a structured product that..."~~ (definition, not story)
- ~~"Consider an investor who wants to..."~~ (generic, not specific)
- ~~"In this chapter, we will learn about..."~~ (meta-commentary, not teaching)
- ~~"As discussed in Section X.Y..."~~ (backward reference before forward momentum)

---

## 5. Explanation Hierarchy

Every concept in the chapter must follow this progression. Steps may be compressed but not skipped or reordered.

```
1. WHY does this exist?           → §1, §3, §4
2. WHAT does it do (in plain English)? → §1, §2 (analogy)
3. HOW does it work (intuition)?  → §5 (scenarios), §7 (construction)
4. HOW does it work (formally)?   → §6 (definition), §8 (payoff logic)
5. WHAT can go wrong?             → §9 (risks), §16 (common mistakes)
6. HOW is it handled operationally? → §10, §11
7. CAN I apply this?              → §12 (worked example), §13 (interview)
```

The chapter template enforces this hierarchy by section ordering. Within sections, the same principle applies: lead with the "why" or "what" before the "how."

---

## 6. Feynman Requirements

### The Standard

Every section must be understandable by a motivated person who has completed the dependency chain (Parts 0-4 and any prior chapters in the family) but has no other finance knowledge.

### How to Test

For each section, ask: "Could a smart university student who has read the preceding chapters understand this on first reading?" If no, the explanation needs work.

### Feynman Violation Indicators

| Indicator | Example | Fix |
|-----------|---------|-----|
| Concept used without building intuition first | "The convexity adjustment accounts for..." | Build the intuition: "Because the payoff curve bends, a simple straight-line estimate is wrong by a small but systematic amount" |
| Formula without preceding explanation | "P&L = N × (S - K) × Δ" | Explain each variable with words first, then show the formula |
| Assumed knowledge not in dependency chain | "As any rates trader knows..." | Remove the assumption; teach the concept or add the dependency |
| Jargon cluster (3+ technical terms in one sentence) | "The gamma-weighted delta-hedged vega exposure..." | Split into separate sentences, one concept each |

---

## 7. Forbidden Writing Patterns

| Pattern | Why Forbidden | Fix |
|---------|--------------|-----|
| **Passive voice in teaching** | "It is understood that..." obscures who understands what | "The trader understands that..." or "This means..." |
| **Meta-commentary** | "As we discussed in the previous section..." breaks immersion | Just state the fact. The reader remembers or can look back |
| **Hedging language** | "It could be argued that..." weakens authority | State the position directly. If genuinely uncertain, say "this is debated" |
| **Unnecessary qualifiers** | "It is important to note that..." adds nothing | Delete and start with the important thing |
| **Abbreviation without expansion** | "The IRR of the CLN..." | Expand on first use per chapter, even if defined in Parts 0-4 |
| **Rhetorical questions as filler** | "But what does this really mean?" | Just explain what it means |
| **Exclamation marks** | "This is crucial!" | If it's crucial, the content shows it. Exclamation marks signal, they don't convince |
| **Numbered lists where prose works** | Using numbered lists for conceptual explanation | Reserve numbered lists for sequences (steps, procedures). Use prose for explanation |
| **Emojis** | Any emoji in any context | Never use emojis |
| **"Simply" or "just"** | "You simply need to..." minimizes complexity | Remove the word. If the action is simple, the sentence shows it without claiming it |

---

## 8. Reinforcement Device Voice

### Professor Note

- One sentence maximum
- Starts with "If you remember only one thing..."
- Contains the single most important insight, not a summary
- Speaks directly to the reader

**Good:** "If you remember only one thing from this chapter, remember this: the participation rate is not a design choice — it is determined by arithmetic."

**Bad:** ~~"This chapter covered the construction of PPNs including the bond component and option budget."~~

### Common Mistakes

- Bold title stating the mistake as a belief
- 1-2 sentence explanation of why it's wrong
- Corrective tone, not punitive

**Good:** **"My maximum loss is 30% because the barrier is at 70%."** Once the barrier is breached, the investor's loss is determined by how far the stock falls below the strike — the barrier only determines *if* the loss is activated, not *how much* the loss is.

**Bad:** ~~**"Mistake #1."** Some investors incorrectly believe that the barrier limits their loss, which is incorrect.~~

### Mental Models

- One row per key concept
- The model must be a vivid image or metaphor, not a restatement
- The primary analogy from §2 must appear

**Good:** | Knock-in barrier | Tripwire — invisible until activated |
**Bad:** ~~| Knock-in barrier | A level that activates the put when breached |~~

---

*Standard effective 2026-06-19. Applies to all written content generated after this date.*
