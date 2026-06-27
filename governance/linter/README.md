# Semantic Linter & Regression Suite

Machine-checkable enforcement of the V1.0.1 semantic corrections for the
Structured Products Knowledge Ecosystem. Implements the 22 rules in
`../semantic_linter_specification.md` and the 21 tests in
`../regression_test_suite.md`. Pure Python 3.10+ stdlib — no dependencies.

## Files

| File | Purpose |
|------|---------|
| `semantic_linter.py` | The 22-rule linter (correlation direction, ownership, sign/arithmetic, strike/barrier, cross-artifact, qualifiers). |
| `regression_tests.py` | 21 regression tests; each proves the linter still catches the original defect AND that the live corpus carries the fix. |
| `canonical_artifacts.txt` | The published artifacts that cross-artifact checks run over. Working/review docs are excluded (they quote defects by design). |

## Usage

```bash
# Lint the canonical artifact set (text report)
python3 semantic_linter.py $(grep -vE '^#|^$' canonical_artifacts.txt)

# JSON output for tooling
python3 semantic_linter.py --json Desk_Bible_v2.md

# CI gate: non-zero exit if any S1 (BLOCK) finding
python3 semantic_linter.py --fail-on S1 <files>

# Run the regression suite
python3 regression_tests.py
```

## Severity → action

| Level | Label | Action |
|:-----:|-------|--------|
| S1 | BLOCK | Must fix before publication |
| S2 | WARN  | Must resolve or justify |
| S3 | INFO  | Should resolve |
| S4 | STYLE | May flag |

## Suppressing a false positive

Add an inline comment on (or just above) the line:

```
<!-- lint-disable LNT-COR-02 reason: quotes the structural convention deliberately -->
```

A `reason:` is required; all suppressions are auditable.

## Status (2026-06-27)

- Regression suite: **21/21 pass**
- Canonical corpus: **0 findings** (S1:0 S2:0 S3:0 S4:0)
- All 8 original defect classes still detected by self-test.

## Recommended CI hook

Run on every PR that touches `Desk_Bible_v2.md` or `production/`:

```bash
python3 governance/linter/semantic_linter.py \
  $(grep -vE '^#|^$' governance/linter/canonical_artifacts.txt) --fail-on S1 \
  && python3 governance/linter/regression_tests.py
```
