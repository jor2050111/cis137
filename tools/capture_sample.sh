#!/bin/bash
# Capture one real chat-assistant response for a CIS137 worked example.
#
# Provenance (record this in docs/execution-logs/chapter-NN-responses.md):
#   Claude (Anthropic), Sonnet, run through the Claude Code CLI in print
#   mode with no tools, a plain-assistant system prompt, no settings or
#   instruction files loaded, from a clean working directory, as a fresh
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
# Clean harness (fixed 2026-10-21 after the chapter 5 review): the CLI
# auto-discovers CLAUDE.md files from the working directory upward and
# loads the user-level CLAUDE.md through settings. Captures made before
# this fix ran with the textbook's own writing law in context (no em
# dashes, the banned-word list, Mr. Vega's feedback prefixes), so they
# were real but not what a student's tool returns. This script now runs
# from an empty directory with --setting-sources "" and
# --exclude-dynamic-system-prompt-sections, and a probe confirms the
# model reports no such rules. The one remaining harness line is the
# CLI's own identity statement, which a consumer app also has in its own
# form. Mr. Vega may still re-capture any sample from a roster tool
# (ChatGPT, Gemini, Copilot) before publication; log the tool and date.
#
# Model: Sonnet by default. Set CAPTURE_MODEL=haiku (or another model
# name) for a second-model capture, such as chapter 6's "Tool B". Log
# the model with the capture.
#
# Why a nested CLI call: the course needs real AI output, and this is
# the one chat-assistant path available to a build session without a
# consumer login.

set -euo pipefail

if [[ $# -ge 1 ]]; then
  PROMPT="$*"
else
  PROMPT="$(cat)"
fi

SYSTEM_PROMPT='You are a plain consumer chat assistant. Reply only with your answer to the user message, as a chat assistant would. You have no tools, no memory of other conversations, and no knowledge of any textbook. Do not mention these instructions.'

CLEAN_DIR="${TMPDIR:-/tmp}/cis137-clean-capture"
mkdir -p "$CLEAN_DIR"
cd "$CLEAN_DIR"

env -u CLAUDECODE claude -p \
  --model "${CAPTURE_MODEL:-sonnet}" \
  --tools "" \
  --no-session-persistence \
  --setting-sources "" \
  --exclude-dynamic-system-prompt-sections \
  --system-prompt "$SYSTEM_PROMPT" \
  "$PROMPT" < /dev/null
