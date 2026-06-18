#!/usr/bin/env bash
# install.sh — copy all SP Desk Bible pipeline v2 agents to ~/.claude/agents/
# Run from the agents/ directory:  bash install.sh

set -euo pipefail

AGENTS_DIR="$HOME/.claude/agents"
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
PROJECT_DIR="$(dirname "$SCRIPT_DIR")"

echo "Installing Structured Products Desk Bible pipeline v2 agents..."
mkdir -p "$AGENTS_DIR"

AGENTS=(
  sp-orchestrator.md
  sp-memory-agent.md
  sp-research-agent.md
  sp-product-architect.md
  sp-content-writer.md
  sp-example-generator.md
  sp-reconciliation-generator.md
  sp-murex-mapping.md
  sp-qa-agent.md
  sp-style-agent.md
  sp-crossref-agent.md
  sp-publisher.md
)

for agent in "${AGENTS[@]}"; do
  src="$SCRIPT_DIR/$agent"
  dst="$AGENTS_DIR/$agent"
  if [[ -f "$src" ]]; then
    cp "$src" "$dst"
    echo "  + $agent"
  else
    echo "  ! $agent — NOT FOUND at $src"
  fi
done

# Remove deprecated v1 agent
if [[ -f "$AGENTS_DIR/sp-technical-writer.md" ]]; then
  rm "$AGENTS_DIR/sp-technical-writer.md"
  echo "  - sp-technical-writer.md (deprecated, removed)"
fi

# Create project directory structure if missing
echo ""
echo "Verifying project directory structure..."
DIRS=(
  "$PROJECT_DIR/outputs/research"
  "$PROJECT_DIR/outputs/blueprints"
  "$PROJECT_DIR/outputs/drafts"
  "$PROJECT_DIR/outputs/examples"
  "$PROJECT_DIR/outputs/reconciliation"
  "$PROJECT_DIR/outputs/booking"
  "$PROJECT_DIR/outputs/reviews"
  "$PROJECT_DIR/outputs/style"
  "$PROJECT_DIR/outputs/crossref"
  "$PROJECT_DIR/outputs/publish"
  "$PROJECT_DIR/memory/definitions"
  "$PROJECT_DIR/memory/components"
  "$PROJECT_DIR/memory/terminology"
  "$PROJECT_DIR/memory/examples"
  "$PROJECT_DIR/memory/booking-maps"
  "$PROJECT_DIR/memory/reconciliation"
  "$PROJECT_DIR/memory/style-patterns"
  "$PROJECT_DIR/checkpoints"
  "$PROJECT_DIR/products"
)

for dir in "${DIRS[@]}"; do
  mkdir -p "$dir"
done
echo "  Directory structure verified."

echo ""
echo "Done. ${#AGENTS[@]} agents installed."
echo ""
echo "Commands:"
echo "  build product PHX001              (DRAFT mode)"
echo "  build product PHX001 mode=review  (REVIEW mode)"
echo "  build product PHX001 mode=publish (PUBLISH mode)"
echo "  build product PHX001 mode=full    (all stages)"
echo "  build desk bible                  (all incomplete products)"
echo "  refresh PHX001                    (incremental update)"
