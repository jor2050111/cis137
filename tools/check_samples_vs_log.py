#!/usr/bin/env python3
"""Verify every sample AI response in a chapter is in its execution log.

Finds each ``text`` fence that follows a "Sample response (captured ..."
label, a "Compare your run" line, or a Fix It symptom lead-in ("Here is
how it began" / "The response was" / "The response began"), and checks
that every non-blank line of the fence, other than a ``[...]`` trim
marker, appears verbatim in the chapter's execution log.

Usage:
    check_samples_vs_log.py book/chapters/chapter-02.md \
        docs/execution-logs/chapter-02-responses.md

Exit 0 when every line matches.
"""

from __future__ import annotations

import re
import sys
from pathlib import Path

LEAD_RE = re.compile(
    r"(?:Sample response \(captured[^\n]*|Compare your run[^\n]*|"
    r"[^\n]*(?:Here is how it began|The response was|The response began|"
    r"the response it gave|the answer it gave)[^\n]*)"
    r"\n\n```text\n(.*?)\n```",
    re.S,
)


def main() -> int:
    if len(sys.argv) != 3:
        print(__doc__)
        return 2
    chapter = Path(sys.argv[1]).read_text(encoding="utf-8")
    log = Path(sys.argv[2]).read_text(encoding="utf-8")
    fences = LEAD_RE.findall(chapter)
    bad = 0
    for body in fences:
        for line in body.split("\n"):
            if line.strip() in ("", "[...]"):
                continue
            if line not in log:
                bad += 1
                print(f"NOT IN LOG: {line[:100]}")
    print(f"sample fences checked: {len(fences)} | lines not in log: {bad}")
    return 0 if bad == 0 else 1


if __name__ == "__main__":
    raise SystemExit(main())
