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

echo "───────────────────────────────────────────────────────"
if [[ $LINT_RC -ne 0 || $REG_RC -ne 0 ]]; then
  echo "BLOCKED: linter exit=$LINT_RC, regression exit=$REG_RC."
  echo "Fix the findings above (or justify with an inline lint-disable + reason) before committing."
  exit 1
fi
echo "PASS: 0 S1 findings, regression green."
exit 0
