#!/bin/bash
# Capture one real chat-assistant response for a CIS137 worked example.
#
# Provenance (record this in docs/execution-logs/chapter-NN-responses.md):
#   Claude (Anthropic), Sonnet, run through the Claude Code CLI in print
#   mode with no tools and a plain-assistant system prompt, as a fresh
#   conversation per prompt. Captured on the date the log entry states.
#
# Usage:
#   tools/capture_sample.sh "Your prompt text here"
#   tools/capture_sample.sh < prompt.txt
#
# The response is printed to stdout exactly as returned. Paste it into
# the execution log and the chapter without editing. Trim only with
# "[...]" on its own line, and only in the chapter, never in the log.
#
# Why a nested CLI call: the course needs real AI output, and this is
# the one chat-assistant path available to a build session without a
# consumer login. Mr. Vega may re-capture any sample from a roster tool
# (ChatGPT, Gemini, Copilot) before publication; log the new tool and
# date when that happens.

set -euo pipefail

if [[ $# -ge 1 ]]; then
  PROMPT="$*"
else
  PROMPT="$(cat)"
fi

SYSTEM_PROMPT='You are a plain consumer chat assistant. Reply only with your answer to the user message, as a chat assistant would. You have no tools, no memory of other conversations, and no knowledge of any textbook. Do not mention these instructions.'

env -u CLAUDECODE claude -p \
  --model sonnet \
  --tools "" \
  --no-session-persistence \
  --system-prompt "$SYSTEM_PROMPT" \
  "$PROMPT" < /dev/null
