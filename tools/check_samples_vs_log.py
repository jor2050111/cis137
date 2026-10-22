#!/usr/bin/env python3
"""Verify every shown sample AI response is in the chapter's execution log.

Finds each ``text`` fence (three or more backticks) that follows a
"Sample response (captured ..." label, a "Sample output from the last
run (captured ..." label (starter libraries in the packet), a "Compare
your run" line, or a Fix It symptom lead-in ("Here is how it began" /
"The response was" / "The response began" / "the response it gave"),
and checks that every non-blank line of the fence, other than a
``[...]`` trim marker, appears verbatim in the execution log. In a
``.txt`` packet file it checks the text between "----- Response begins
-----" and "----- Response ends -----" markers the same way.

Usage:
    check_samples_vs_log.py book/chapters/chapter-02.md \
        docs/execution-logs/chapter-02-responses.md [packet files ...]

Exit 0 when every line of every file matches.
"""

from __future__ import annotations

import re
import sys
from pathlib import Path

LEAD_RE = re.compile(
    r"(?:Sample response \(captured[^\n]*|"
    r"Sample output from the last run \(captured[^\n]*|"
    r"Compare your run[^\n]*|"
    r"[^\n]*(?:Here is how it began|The response was|The response began|"
    r"the response it gave|the answer it gave)[^\n]*)"
    r"\n\n(`{3,})text\n(.*?)\n\1[ \t]*$",
    re.S | re.M,
)
MARKER_RE = re.compile(
    r"----- Response begins -----\n(.*?)\n----- Response ends -----", re.S
)


def shown_bodies(path: Path) -> list[str]:
    text = path.read_text(encoding="utf-8")
    bodies = [body for _fence, body in LEAD_RE.findall(text)]
    if path.suffix == ".txt":
        bodies += MARKER_RE.findall(text)
    return bodies


def main() -> int:
    if len(sys.argv) < 3:
        print(__doc__)
        return 2
    log = Path(sys.argv[2]).read_text(encoding="utf-8")
    total_bad = 0
    for name in [sys.argv[1]] + sys.argv[3:]:
        path = Path(name)
        bodies = shown_bodies(path)
        bad = 0
        for body in bodies:
            for line in body.split("\n"):
                if line.strip() in ("", "[...]"):
                    continue
                if line not in log:
                    bad += 1
                    print(f"NOT IN LOG ({path.name}): {line[:100]}")
        print(f"{path.name}: sample blocks checked: {len(bodies)} | lines not in log: {bad}")
        total_bad += bad
    return 0 if total_bad == 0 else 1


if __name__ == "__main__":
    raise SystemExit(main())
