# SEMANTIC LINTER SPECIFICATION

**Ecosystem:** Structured Products Knowledge Ecosystem  
**Version:** V1.0.1-GOV-1.0  
**Effective:** 2026-06-27  
**Purpose:** Machine-checkable detection rules for semantic defects  
**Format:** YAML-compatible rule definitions with regex + context patterns

---

## Linter Architecture

```
Input: Markdown artifact (full text)
Pipeline:
  1. Tokenize into sentences (split on . ? ! and newlines)
  2. Build context windows (current sentence + 2 preceding + 2 following)
  3. Apply pattern rules against each context window
  4. Apply cross-artifact rules against the full corpus
  5. Output: findings with severity, rule ID, line number, matched text, remediation
```

---

## Severity Levels

| Level | Label | Action | Description |
|:-----:|-------|--------|-------------|
| S1 | **BLOCK** | Must fix before publication | Self-contradictory, factually wrong, or teaches incorrect direction |
| S2 | **WARN** | Must resolve or justify | Ambiguous in a way that could teach wrong answer |
| S3 | **INFO** | Should resolve | Ambiguous but interpretable from context |
| S4 | **STYLE** | May flag | Stylistic preference or minor clarity improvement |

---

## CATEGORY 1 — CORRELATION DIRECTION RULES

### LNT-COR-01: Long Correlation Self-Contradiction

| Field | Value |
|-------|-------|
| **Rule ID** | LNT-COR-01 |
| **Severity** | S1 |
| **Trigger pattern** | `/(long correlation).*?(harm|hurt|lose|decrease|worsen|risk increases).*?(correlation (?:rise|high|increase))/i` within 200 chars |
| **Context** | Any sentence or adjacent pair containing "long correlation" with negative outcome from rising correlation |
| **True positive** | "Investors are long correlation. They lose when correlation rises." |
| **False positive** | "Long correlation benefits the investor. The desk loses when correlation rises." — different subjects |
| **Remediation** | Check whether the subject (investor/desk) matches across clauses. If same subject: label is wrong. |
| **Test case** | `REG-COR-01` |

### LNT-COR-02: Short Correlation Self-Contradiction

| Field | Value |
|-------|-------|
| **Rule ID** | LNT-COR-02 |
| **Severity** | S1 |
| **Trigger pattern** | `/(short correlation).*?(benefit|profit|gain|improve|risk decreases).*?(correlation (?:rise|high|increase))/i` within 200 chars |
| **Context** | Same-subject short correlation + positive outcome from rising correlation |
| **True positive** | "WOAC investors are short correlation: they benefit from high correlation." |
| **False positive** | "The desk is short correlation. The investor benefits when correlation is high." — different subjects |
| **Remediation** | If same subject: change label to "long" or add "structurally" qualifier |
| **Test case** | `REG-COR-02`, `REG-COR-08` |

### LNT-COR-03: Missing Structural Qualifier

| Field | Value |
|-------|-------|
| **Rule ID** | LNT-COR-03 |
| **Severity** | S2 |
| **Trigger pattern** | `/(sold|sell|selling).*?(correlation (?:premium|risk|exposure)).*?(short correlation)/i` without "structurally" within 300 chars |
| **Context** | Premium-selling language combined with correlation direction label |
| **True positive** | "The investor sold the correlation premium. They are short correlation." |
| **False positive** | "The investor is structurally short correlation — they sold the correlation premium." — has qualifier |
| **Remediation** | Add "structurally" before "short/long correlation" |
| **Test case** | `REG-COR-03` |

### LNT-COR-06: FTD Labeled Short Without Structural

| Field | Value |
|-------|-------|
| **Rule ID** | LNT-COR-06 |
| **Severity** | S1 |
| **Trigger pattern** | `/FTD.*?short correlation/i` without "structurally" within 100 chars |
| **Context** | Any mention of FTD as "short correlation" without structural qualifier |
| **True positive** | "FTD investors are short correlation." |
| **False positive** | "FTD investors are structurally short correlation." — has qualifier |
| **Remediation** | Change to "long correlation" or add "structurally" |
| **Test case** | `REG-COR-06` |

### LNT-COR-07: NTD Labeled Long

| Field | Value |
|-------|-------|
| **Rule ID** | LNT-COR-07 |
| **Severity** | S1 |
| **Trigger pattern** | `/(2TD|3TD|4TD|5TD|NTD|nth-to-default).*?long correlation/i` within 100 chars |
| **Context** | Any NTD product labeled long correlation |
| **True positive** | "5TD is long correlation (unambiguous)." |
| **False positive** | None expected — NTD is always short under MTM |
| **Remediation** | Change to "short correlation" |
| **Test case** | `REG-COR-07` |

### LNT-COR-08: Worst-of Investor Labeled Short Without Structural

| Field | Value |
|-------|-------|
| **Rule ID** | LNT-COR-08 |
| **Severity** | S1 |
| **Trigger pattern** | `/worst-of.*?investor.*?short correlation/i` without "structurally" within 150 chars |
| **Context** | Worst-of investor labeled short |
| **True positive** | "Worst-of investors are short correlation — they profit when stocks move together." |
| **False positive** | "Worst-of investors are structurally short correlation." — has qualifier |
| **Remediation** | Change to "long correlation" or add "structurally" |
| **Test case** | `REG-COR-08` |

### LNT-COR-09: Dispersion Labeled Long

| Field | Value |
|-------|-------|
| **Rule ID** | LNT-COR-09 |
| **Severity** | S1 |
| **Trigger pattern** | `/long single-stock.*?short basket.*?long correlation/i` within 200 chars |
| **Context** | Dispersion trade legs combined with wrong direction label |
| **True positive** | "Long single-stock vol + short basket vol = long correlation." |
| **False positive** | None expected |
| **Remediation** | Change "long correlation" to "short correlation" |
| **Test case** | `REG-COR-09` |

### LNT-COR-10: Misleading Reversal Language

| Field | Value |
|-------|-------|
| **Rule ID** | LNT-COR-10 |
| **Severity** | S2 |
| **Trigger pattern** | `/(reversal|reverse|flip).*?(at (?:high|low|moderate) ρ)/i` + NTD context |
| **Context** | "Reversal" language implying within-product direction change |
| **True positive** | "2TD: Short at low ρ, reversal at high ρ" |
| **False positive** | "The reversal between FTD and NTD occurs because..." — correctly describes cross-product flip |
| **Remediation** | Clarify that "reversal" means the FTD-vs-NTD direction difference |
| **Test case** | `REG-COR-10` |

---

## CATEGORY 2 — POSITION / OWNERSHIP RULES

### LNT-POS-01: Desk Correlation Without Raw/Hedged

| Field | Value |
|-------|-------|
| **Rule ID** | LNT-POS-01 |
| **Severity** | S2 |
| **Trigger pattern** | `/(desk|bank|dealer).*?(long|short) correlation/i` without `/(raw|unhedged|net|hedged)/i` within 200 chars |
| **Context** | Desk position described without qualifier |
| **True positive** | "The desk is long correlation on worst-of products." |
| **False positive** | "The desk's raw position is short correlation." — has qualifier |
| **Remediation** | Add "raw/unhedged" or "net/hedged" qualifier |
| **Test case** | `REG-POS-01` |

### LNT-PRO-01: Desk Sold Protection

| Field | Value |
|-------|-------|
| **Rule ID** | LNT-PRO-01 |
| **Severity** | S1 |
| **Trigger pattern** | `/(desk|bank|dealer).*?(sold|sells|selling) (?:the )?protection/i` in structured note context |
| **Context** | Context markers: RC, WOAC, CLN, FTD, structured note, autocallable |
| **True positive** | "The desk sold protection via the short put." |
| **False positive** | "The desk sold protection via a CDS." — desk CAN sell protection via standalone CDS |
| **Remediation** | In structured notes: change to "investor sold protection" or "desk bought protection" |
| **Test case** | `REG-PRO-01` |

### LNT-PRO-03: Desk Short Put

| Field | Value |
|-------|-------|
| **Rule ID** | LNT-PRO-03 |
| **Severity** | S1 |
| **Trigger pattern** | `/(desk|bank|dealer).*?short (?:the )?put/i` in structured note context |
| **Context** | Same as LNT-PRO-01 |
| **True positive** | "The desk's short put position in the RC..." |
| **False positive** | "The desk's short put on the hedging book" — desk may have other short puts |
| **Remediation** | In structured notes: the desk is LONG the put |
| **Test case** | `REG-PRO-03` |

---

## CATEGORY 3 — SIGN / ARITHMETIC RULES

### LNT-SGN-01: Arithmetic Impossibility

| Field | Value |
|-------|-------|
| **Rule ID** | LNT-SGN-01 |
| **Severity** | S1 |
| **Trigger pattern** | `/(\d+)%.*?above.*?(\d+)%/` where first number < second number |
| **Context** | Percentage comparisons in worked examples |
| **True positive** | "65%: above strike (100%)" — 65 < 100, so "above" is false |
| **False positive** | "105%: above strike (100%)" — 105 > 100, correct |
| **Remediation** | Correct the comparison direction |
| **Test case** | `REG-SGN-01` |

### LNT-SGN-02: Gamma ΔS Sign Drop

| Field | Value |
|-------|-------|
| **Rule ID** | LNT-SGN-02 |
| **Severity** | S1 |
| **Trigger pattern** | `/[Gg]amma.*?(\d+)\s*[×x*]\s*(\d+)\s*[)=]/` where context mentions "drop" or "fall" but the multiplied value is positive |
| **Context** | Gamma calculations following a stock decline |
| **True positive** | "After the $2 drop: 3 × 2 = 6" — should be 3 × (−2) = −6 |
| **False positive** | "After the $2 rise: 3 × 2 = 6" — correct, stock went up |
| **Remediation** | Include the sign of ΔS in the multiplication |
| **Test case** | `REG-SGN-02` |

### LNT-SGN-03: Intermediate vs Final Mismatch

| Field | Value |
|-------|-------|
| **Rule ID** | LNT-SGN-03 |
| **Severity** | S1 |
| **Trigger pattern** | Computed intermediate result ≠ stated intermediate result |
| **Context** | Any worked example with multi-step arithmetic |
| **True positive** | "−50 + (3 × 2) = −56" — intermediate is −50 + 6 = −44, not −56 |
| **False positive** | None — arithmetic either matches or doesn't |
| **Remediation** | Fix the intermediate step or the final answer |
| **Test case** | `REG-SGN-03` |
| **Note** | Requires arithmetic evaluation, not just regex |

---

## CATEGORY 4 — STRIKE / BARRIER RULES

### LNT-STR-01: Strike Used as Barrier

| Field | Value |
|-------|-------|
| **Rule ID** | LNT-STR-01 |
| **Severity** | S2 |
| **Trigger pattern** | `/(hit|breach|touch|cross|observe).*?strike/i` without maturity context |
| **Context** | "Hit the strike" during the life of the product — likely means barrier |
| **True positive** | "If the stock hits the strike during the observation period..." |
| **False positive** | "At maturity, if the stock is below the strike..." — correct usage |
| **Remediation** | Change "strike" to "barrier" if describing during-life observation |
| **Test case** | `REG-STR-01` |

### LNT-STR-02: Undefined Strike in Worked Example

| Field | Value |
|-------|-------|
| **Rule ID** | LNT-STR-02 |
| **Severity** | S2 |
| **Trigger pattern** | `strike` appears in a worked example but no line in the terms table defines the strike level numerically |
| **Context** | Worked examples with terms tables |
| **True positive** | A WOAC worked example references "above strike (100%)" but the terms table lacks a strike row |
| **False positive** | The terms table defines "Strike: 100% of initial" |
| **Remediation** | Add strike to the terms table |
| **Test case** | `REG-STR-02` |

---

## CATEGORY 5 — CROSS-ARTIFACT RULES

### LNT-XAR-01: Same Concept Opposite Label

| Field | Value |
|-------|-------|
| **Rule ID** | LNT-XAR-01 |
| **Severity** | S1 |
| **Trigger pattern** | Same product + same position holder + "long correlation" in one artifact + "short correlation" in another, without raw/hedged distinction |
| **Context** | Cross-artifact comparison |
| **True positive** | Part 6: "worst-of = long correlation." Encyclopedia: "worst-of = short correlation." Without raw/hedged qualifiers. |
| **False positive** | Part 6: "worst-of = long correlation (hedged)." Encyclopedia: "worst-of = short correlation (raw)." — properly qualified |
| **Remediation** | Add raw/hedged qualifiers to both |
| **Test case** | `REG-XAR-01` |

### LNT-XAR-02: Ownership Inconsistency

| Field | Value |
|-------|-------|
| **Rule ID** | LNT-XAR-02 |
| **Severity** | S1 |
| **Trigger pattern** | Same product: one artifact says "desk sold protection," another says "investor sold protection" |
| **Context** | Cross-artifact comparison for the same product |
| **True positive** | Part 6: "desk sold the put." Interview System: "investor sold the put." |
| **False positive** | None — ownership cannot differ for the same product |
| **Remediation** | Correct the wrong artifact |
| **Test case** | `REG-XAR-02` |

### LNT-XAR-03: NTD Table vs Risk Table Inconsistency

| Field | Value |
|-------|-------|
| **Rule ID** | LNT-XAR-03 |
| **Severity** | S1 |
| **Trigger pattern** | Within same artifact: a label table says product X has direction Y, but a risk table shows risk increasing/decreasing in the opposite direction |
| **Context** | Same-chapter or same-section comparison |
| **True positive** | Label table: "5TD = long correlation." Risk table: 5TD risk HIGH at high ρ (= short). |
| **False positive** | None |
| **Remediation** | Align label table with risk table |
| **Test case** | `REG-XAR-03` |

---

## CATEGORY 6 — QUALIFIER OMISSION RULES

### LNT-QAL-01: Missing "Structurally"

| Field | Value |
|-------|-------|
| **Rule ID** | LNT-QAL-01 |
| **Severity** | S2 |
| **Trigger pattern** | Premium language (sold/bought/earned/paid + premium/yield/coupon) + correlation direction within 200 chars, without "structurally" |
| **Context** | Any sentence mixing premium-direction language with correlation labels |
| **True positive** | "The investor sold the correlation premium. They are short correlation." |
| **False positive** | "The investor is structurally short correlation — they sold the premium." |
| **Remediation** | Insert "structurally" |
| **Test case** | `REG-QAL-01` |

### LNT-QAL-02: Missing Raw/Hedged for Desk

| Field | Value |
|-------|-------|
| **Rule ID** | LNT-QAL-02 |
| **Severity** | S2 |
| **Trigger pattern** | Desk/bank/dealer + long/short correlation without raw/hedged within 200 chars |
| **Context** | Same as LNT-POS-01 |
| **True positive** | "The bank is long correlation on worst-of products." |
| **False positive** | "The bank's net position is long correlation." |
| **Remediation** | Add raw/unhedged or net/hedged |
| **Test case** | `REG-QAL-02` |

### LNT-QAL-03: Hedged Position Described as Product Property

| Field | Value |
|-------|-------|
| **Rule ID** | LNT-QAL-03 |
| **Severity** | S3 |
| **Trigger pattern** | "Product X is long/short correlation" where the direction depends on hedging |
| **Context** | Product-level description that actually describes a hedged desk position |
| **True positive** | "Worst-of products are long correlation" — this is the hedged desk view, not an intrinsic product property |
| **False positive** | "Worst-of investors are long correlation" — correctly describes the investor's intrinsic direction |
| **Remediation** | Change "products are" to "desk's net position is" or "investors are" |
| **Test case** | `REG-QAL-03` |

---

## IMPLEMENTATION NOTES

### Recommended Implementation Stack

```
Language:     Python 3.10+
Regex engine: re module with re.IGNORECASE
Tokenizer:    sentence-boundary detection (spaCy or rule-based)
Context:      sliding window of 5 sentences (2 before + current + 2 after)
Output:       JSON array of findings
CI:           Run on every PR that touches review/ or production/
```

### Output Format

```json
{
  "rule_id": "LNT-COR-02",
  "severity": "S1",
  "file": "Desk_Bible_v2.md",
  "line": 17524,
  "matched_text": "FTD investors are short correlation. They profit when correlation is high",
  "message": "Short correlation label contradicts benefit from rising correlation",
  "remediation": "Change to 'long correlation' or add 'structurally' qualifier",
  "regression_test": "REG-COR-02"
}
```

### False Positive Management

- Every rule has documented false-positive examples
- Suppress via inline comments: `<!-- lint-disable LNT-COR-02 reason: describes structural convention -->`
- All suppressions logged and auditable
- Suppressions require a `reason:` field

---

## RULE SUMMARY TABLE

| Rule ID | Category | Severity | Detects |
|:-------:|----------|:--------:|---------|
| LNT-COR-01 | Correlation | S1 | Long + negative outcome from rising ρ |
| LNT-COR-02 | Correlation | S1 | Short + positive outcome from rising ρ |
| LNT-COR-03 | Correlation | S2 | Missing "structurally" with premium language |
| LNT-COR-06 | Correlation | S1 | FTD labeled short without structural |
| LNT-COR-07 | Correlation | S1 | NTD labeled long |
| LNT-COR-08 | Correlation | S1 | Worst-of investor labeled short without structural |
| LNT-COR-09 | Correlation | S1 | Dispersion labeled long |
| LNT-COR-10 | Correlation | S2 | Misleading reversal language |
| LNT-POS-01 | Position | S2 | Desk correlation without raw/hedged |
| LNT-PRO-01 | Ownership | S1 | Desk sold protection in structured notes |
| LNT-PRO-03 | Ownership | S1 | Desk short put in structured notes |
| LNT-SGN-01 | Arithmetic | S1 | X% above Y% where X < Y |
| LNT-SGN-02 | Arithmetic | S1 | Gamma × ΔS sign drop |
| LNT-SGN-03 | Arithmetic | S1 | Intermediate ≠ stated result |
| LNT-STR-01 | Structure | S2 | Strike used as barrier |
| LNT-STR-02 | Structure | S2 | Undefined strike in worked example |
| LNT-XAR-01 | Cross-artifact | S1 | Same concept, opposite label |
| LNT-XAR-02 | Cross-artifact | S1 | Ownership inconsistency |
| LNT-XAR-03 | Cross-artifact | S1 | Label table vs risk table inconsistency |
| LNT-QAL-01 | Qualifier | S2 | Missing "structurally" |
| LNT-QAL-02 | Qualifier | S2 | Missing raw/hedged for desk |
| LNT-QAL-03 | Qualifier | S3 | Hedged described as product property |

**Total rules: 22** (13 S1, 7 S2, 2 S3)

---

*Semantic Linter Specification | V1.0.1-GOV-1.0 | 2026-06-27*
