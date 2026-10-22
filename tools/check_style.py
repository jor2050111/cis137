#!/usr/bin/env python3
"""Style-law scan for CIS137 prose: banned words, em dashes, semicolons.

Scans only prose, meaning lines outside fenced blocks, with inline code
spans removed. Captured AI responses sit inside ``text`` fences and are
evidence, never edited, so the law does not apply to them (CLAUDE.md,
Code Standards; claude-config rules/preferences.md). Verbatim MCCCD
text is the one prose exception for "real-world": pass --allow-real-world
for files that quote the district outline.

Usage:
    check_style.py FILE [FILE ...] [--allow-real-world]

Exit 0 when no hit.
"""

from __future__ import annotations

import re
import sys
from pathlib import Path

BANNED = [
    "spot-on", "spot on", "indeed", "delve", "dive", "embark", "nuances",
    "journey", "tapestry", "navigate", "crucial", "basically", "actually",
    "really", "very", "quite", "somewhat", "rather", "in order to",
    "real-world", "moving forward", "at the end of the day",
    "it is important to note", "it should be mentioned", "it is worth noting",
]
FENCE_RE = re.compile(r"^(`{3,}|~{3,})")
CODE_SPAN_RE = re.compile(r"`[^`\n]*`")


def scan(path: Path, allow_real_world: bool) -> int:
    hits = 0
    in_fence = False
    fence_char, fence_len = None, 0
    banned = [b for b in BANNED if not (allow_real_world and b == "real-world")]
    pattern = re.compile(r"\b(" + "|".join(re.escape(b) for b in banned) + r")\b", re.I)
    for n, raw in enumerate(path.read_text(encoding="utf-8").splitlines(), 1):
        line = raw.strip()
        m = FENCE_RE.match(line)
        if not in_fence and m:
            in_fence, fence_char, fence_len = True, m.group(1)[0], len(m.group(1))
            continue
        if in_fence:
            if line and set(line) == {fence_char} and len(line) >= fence_len:
                in_fence = False
            continue
        prose = CODE_SPAN_RE.sub("", raw)
        if "—" in prose:
            hits += 1
            print(f"{path}:{n}: em dash")
        if ";" in prose and "&copy;" not in prose:
            hits += 1
            print(f"{path}:{n}: semicolon: {prose.strip()[:80]}")
        for w in pattern.findall(prose):
            hits += 1
            print(f"{path}:{n}: banned word {w!r}: {prose.strip()[:80]}")
    return hits


def main() -> int:
    args = [a for a in sys.argv[1:] if not a.startswith("--")]
    allow = "--allow-real-world" in sys.argv
    if not args:
        print(__doc__)
        return 2
    total = sum(scan(Path(a), allow) for a in args)
    print(f"style hits: {total}")
    return 0 if total == 0 else 1


if __name__ == "__main__":
    raise SystemExit(main())
