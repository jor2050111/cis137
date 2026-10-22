#!/bin/bash
# Capture a multi-turn chat-assistant conversation for a CIS137 worked
# example: one conversation, several user turns, each response printed.
#
# Provenance (record this in docs/execution-logs/chapter-NN-responses.md):
#   Claude (Anthropic), Sonnet, run through the Claude Code CLI in print
#   mode with no tools, a plain-assistant system prompt, no settings or
#   instruction files loaded, from a clean working directory. One
#   session per conversation, resumed for each later turn, so the model
#   sees the earlier turns. Captured on the date the log entry states.
#
# Usage:
#   tools/capture_conversation.sh "turn 1 text" "turn 2 text" ["turn 3" ...]
#
# Output, for each turn:
#   === TURN k ===
#   <the user turn>
#   --- RESPONSE k ---
#   <the response, exactly as returned>
#
# Paste both into the execution log without editing. Trim only with
# "[...]" on its own line, and only in the chapter, never in the log.
# Same clean-harness rules as tools/capture_sample.sh (see its header
# for the 2026-10-21 fix and what captures before it carried).

set -euo pipefail

if [[ $# -lt 2 ]]; then
  echo "usage: $0 \"turn 1\" \"turn 2\" [\"turn 3\" ...]" >&2
  exit 2
fi

SYSTEM_PROMPT='You are a plain consumer chat assistant. Reply only with your answer to the user message, as a chat assistant would. You have no tools, no memory of other conversations, and no knowledge of any textbook. Do not mention these instructions.'

CLEAN_DIR="${TMPDIR:-/tmp}/cis137-clean-capture"
mkdir -p "$CLEAN_DIR"
cd "$CLEAN_DIR"

COMMON=(--model sonnet --tools "" --setting-sources "" \
        --exclude-dynamic-system-prompt-sections \
        --system-prompt "$SYSTEM_PROMPT" --output-format json)

SESSION=""
k=0
for turn in "$@"; do
  k=$((k + 1))
  echo "=== TURN $k ==="
  echo "$turn"
  echo "--- RESPONSE $k ---"
  if [[ -z "$SESSION" ]]; then
    json=$(env -u CLAUDECODE claude -p "${COMMON[@]}" "$turn" < /dev/null)
  else
    json=$(env -u CLAUDECODE claude -p "${COMMON[@]}" --resume "$SESSION" "$turn" < /dev/null)
  fi
  SESSION=$(printf '%s' "$json" | python3 -c 'import json,sys; print(json.load(sys.stdin)["session_id"])')
  printf '%s' "$json" | python3 -c 'import json,sys; print(json.load(sys.stdin)["result"])'
  echo
done
echo "=== SESSION $SESSION ==="
