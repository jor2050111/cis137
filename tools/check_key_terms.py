#!/usr/bin/env python3
"""Check that a chapter's Key Terms and bolded terms resolve to glossary headwords.

Usage:
    check_key_terms.py book/chapters/chapter-02.md book/glossary.md [extra-glossary.md ...]

Extra glossary files use the same definition-list format (a headword
line followed by a ":   definition" line). A writer's additions file
can be passed before it is merged into book/glossary.md.

Reports: Key Terms missing from the glossary, and lowercase bolded
terms in the chapter that have no headword (candidates for the
glossary, or terms that should not be bold). Exit 0 when no Key Term
is missing.
"""

from __future__ import annotations

import re
import sys
from pathlib import Path

FENCE_RE = re.compile(r"^`{3,}[^\n]*\n.*?^`{3,}[ \t]*$", re.S | re.M)


def headwords(path: Path) -> set[str]:
    heads = set()
    lines = path.read_text(encoding="utf-8").splitlines()
    for i, line in enumerate(lines):
        if not line or line.startswith(("#", ":", " ", "<!--", "*", "-")):
            continue
        if i + 1 < len(lines) and lines[i + 1].startswith(":"):
            heads.add(line.strip())
    return heads


def main() -> int:
    if len(sys.argv) < 3:
        print(__doc__)
        return 2
    chapter = Path(sys.argv[1]).read_text(encoding="utf-8")
    heads: set[str] = set()
    for g in sys.argv[2:]:
        heads |= headwords(Path(g))
    m = re.search(r"### Key Terms(.*?)### Retrieval", chapter, re.S)
    if not m:
        print("Key Terms block not found")
        return 1
    terms = []
    for line in m.group(1).splitlines():
        if line.startswith("* "):
            body = re.sub(r"\s*\(Sections? [^)]*\)\s*$", "", line[2:])
            terms += [t.strip() for t in re.split(r", (?![^(]*\))", body)]
    missing = [t for t in terms if t not in heads]
    print(f"key terms: {len(terms)} | missing from glossary: {missing}")
    # Bold inside a captured response is the model's markup, not an
    # author term, so fenced blocks are dropped before the scan.
    prose = FENCE_RE.sub("", chapter)
    bolded = set(re.findall(r"\*\*([a-z][^*\n]+?)\*\*", prose))
    loose = sorted(b for b in bolded if b not in heads and not b.endswith(":"))
    print(f"bolded lowercase terms without a headword: {loose}")
    return 0 if not missing else 1


if __name__ == "__main__":
    raise SystemExit(main())
