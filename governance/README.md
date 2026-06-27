# Governance & Quality — Structured Products Desk Bible

[![Dual-lens quality gate](https://github.com/shubhankarkumar990-debug/Structured-Products/actions/workflows/dual-lens-ci.yml/badge.svg)](https://github.com/shubhankarkumar990-debug/Structured-Products/actions/workflows/dual-lens-ci.yml)

> Badge points at `shubhankarkumar990-debug/Structured-Products`. It goes green once the repo is pushed to GitHub and the `dual-lens-ci.yml` workflow runs once.

This folder holds the machinery that keeps the Desk Bible correct and consistent.

## What's here

| Path | What it is |
|------|------------|
| `dual_lens_authoring_standard.md` | The authoring standard (V3.0-FINAL) — the two-lens structure, no-first-person rule, reconciliation checklist, visual/question parity. |
| `dual_lens_completion_record.md` | Authoritative record of the 49-product transformation. |
| `linter/semantic_linter.py` | 22-rule semantic linter (correlation direction, ownership, arithmetic, cross-artifact, qualifiers). |
| `linter/regression_tests.py` | 21 regression tests; each proves the linter still catches the original defect and the corpus carries the fix. |
| `linter/run_checks.sh` | Single quality-gate entrypoint (linter fail-on-S1 + regression). |
| `linter/canonical_artifacts.txt` | The 9 artifacts the cross-artifact checks run over. |
| `hooks/pre-commit` | Pre-commit hook that runs the gate before each commit. |
| `diagram_lib/sp_diagrams.py` | 18 calibrated diagram generators (payoffs, gamma/hedge, waterfalls, cashflow legs, correlation, reconciliation flow). |
| `diagram_lib/build_catalog.py` → `visual_catalog.html` | Browsable catalog of all 156 generated diagrams. |
| `knowledge_graph/build_kg.py` | Populates the ontology — 170 nodes / 163 edges from the live products, linter rules, tests, and errata. |
| `knowledge_graph/kg_query.py` | Query CLI over the populated graph. |
| `knowledge_graph_ontology.md` | The graph schema (13 node types, 19 edge types). |

## Run the quality gate

```bash
bash governance/linter/run_checks.sh        # linter (fail on S1) + 21 regression tests
```

## Enable the pre-commit hook (once, on your machine)

```bash
git config core.hooksPath governance/hooks
```

Now any commit touching `Desk_Bible_v2.md`, `production/`, or `governance/linter/` runs the gate and is aborted on a blocking finding. Bypass in an emergency with `git commit --no-verify`.

## CI

`.github/workflows/dual-lens-ci.yml` runs the same gate on every push / PR that touches the corpus. The badge above reflects its status.

## Rebuild the artifacts

```bash
python3 governance/diagram_lib/sp_diagrams.py            # smoke-test the diagram library
python3 governance/diagram_lib/build_catalog.py          # rebuild visual_catalog.html
python3 governance/knowledge_graph/build_kg.py           # repopulate the knowledge graph
python3 governance/knowledge_graph/kg_query.py by-corr LONG   # query it
```

## Current status

- 49/49 products dual-lens, all six families audited and remediated.
- Linter: 0 findings (9 canonical artifacts). Regression: 21/21.
- Knowledge graph: 170 nodes, 163 edges.
- 156 generated diagrams.
