#!/usr/bin/env bash
# Dual-lens quality gate: semantic linter (fail on S1) + regression suite.
# Single entrypoint used by the pre-commit hook and CI.
# Exit 0 = clean, 1 = a blocking finding or a regression failure.
set -uo pipefail

# Resolve repo root (this script lives in governance/linter/).
HERE="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
ROOT="$(cd "$HERE/../.." && pwd)"
cd "$ROOT" || exit 2

PY="${PYTHON:-python3}"
LINT="governance/linter/semantic_linter.py"
REG="governance/linter/regression_tests.py"
MANIFEST="governance/linter/canonical_artifacts.txt"

# Canonical artifact list (skips comments/blanks).
# Portable to macOS bash 3.2 (no mapfile).
FILES=()
while IFS= read -r _line; do
  [ -n "$_line" ] && FILES+=("$_line")
done < <(grep -vE '^#|^$' "$MANIFEST")

echo "── Dual-lens quality gate ─────────────────────────────"
echo "Linter (fail-on S1) over ${#FILES[@]} canonical artifacts…"
"$PY" "$LINT" "${FILES[@]}" --fail-on S1
LINT_RC=$?

echo
echo "Regression suite…"
"$PY" "$REG"
REG_RC=$?

echo
echo "Link integrity (anchors + cross-document links)…"
"$PY" governance/audit/link_check.py \
  START_HERE.md \
  Desk_Bible_v2.md \
  production/solutions_manual.md \
  production/product_comparison_matrix.md \
  production/product_dna_atlas.md \
  production/interview_system_v2_2.md \
  production/infrastructure_encyclopedia_v1.md
LINK_RC=$?

echo "───────────────────────────────────────────────────────"
if [[ $LINT_RC -ne 0 || $REG_RC -ne 0 || $LINK_RC -ne 0 ]]; then
  echo "BLOCKED: linter exit=$LINT_RC, regression exit=$REG_RC, link-check exit=$LINK_RC."
  echo "Fix the findings above (or justify with an inline lint-disable + reason) before committing."
  exit 1
fi
echo "PASS: 0 S1 findings, regression green, all links resolve."
exit 0
