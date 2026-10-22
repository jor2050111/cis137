#!/usr/bin/env python3
"""Merge a writer's glossary-additions file into book/glossary.md.

The glossary is a definition list grouped under "## A" ... "## Z"
headings: a headword line, then one ":   definition" line, one blank
line between entries, alphabetical within each letter (case-insensitive).
Additions use the same two-line format.

A headword that already exists is skipped and reported, so two chapter
writers who both define "primary source" never produce two entries. The
assembler decides which definition stays by editing the glossary.

Usage:
    merge_glossary.py book/glossary.md additions-02.md [additions-03.md ...]

Exit 0. Prints one line per merged or skipped term.
"""

from __future__ import annotations

import re
import sys
from pathlib import Path


def parse_entries(text: str) -> list[tuple[str, str]]:
    entries = []
    lines = text.splitlines()
    i = 0
    while i < len(lines):
        line = lines[i]
        if (line and not line.startswith(("#", ":", " ", "<!--", "*", "-"))
                and i + 1 < len(lines) and lines[i + 1].startswith(":")):
            entries.append((line.strip(), lines[i + 1]))
            i += 2
        else:
            i += 1
    return entries


def sort_key(head: str) -> str:
    return re.sub(r"[^a-z0-9 ]", "", head.lower())


def main() -> int:
    if len(sys.argv) < 3:
        print(__doc__)
        return 2
    gpath = Path(sys.argv[1])
    text = gpath.read_text(encoding="utf-8")
    existing = {h.lower(): h for h, _ in parse_entries(text)}
    merged, skipped = [], []
    for add in sys.argv[2:]:
        for head, definition in parse_entries(Path(add).read_text(encoding="utf-8")):
            if head.lower() in existing:
                skipped.append((head, add))
                continue
            text = insert(text, head, definition)
            existing[head.lower()] = head
            merged.append((head, add))
    gpath.write_text(text, encoding="utf-8")
    for h, a in merged:
        print(f"merged  {h}  ({Path(a).name})")
    for h, a in skipped:
        print(f"SKIPPED (already defined)  {h}  ({Path(a).name})")
    print(f"{len(merged)} merged, {len(skipped)} skipped")
    return 0


def insert(text: str, head: str, definition: str) -> str:
    letter = sort_key(head)[0].upper()
    heading = f"## {letter}"
    lines = text.split("\n")
    # Locate or create the letter section.
    if heading not in lines:
        # Insert the heading before the first later letter, or at the end.
        idx = len(lines)
        for i, line in enumerate(lines):
            m = re.match(r"^## ([A-Z])$", line)
            if m and m.group(1) > letter:
                idx = i
                break
        lines[idx:idx] = [heading, "", "__PLACEHOLDER__", ""]
        text = "\n".join(lines)
        lines = text.split("\n")
    start = lines.index(heading) + 1
    end = len(lines)
    for i in range(start, len(lines)):
        if re.match(r"^## [A-Z]$", lines[i]):
            end = i
            break
    # Collect entries in the section.
    section = lines[start:end]
    entries = []
    i = 0
    while i < len(section):
        if section[i] == "__PLACEHOLDER__":
            i += 1
            continue
        if (section[i] and not section[i].startswith(":")
                and i + 1 < len(section) and section[i + 1].startswith(":")):
            entries.append((section[i], section[i + 1]))
            i += 2
        else:
            i += 1
    entries.append((head, definition))
    entries.sort(key=lambda e: sort_key(e[0]))
    rebuilt = [""]
    for h, d in entries:
        rebuilt += [h, d, ""]
    lines[start:end] = rebuilt
    return "\n".join(lines)


if __name__ == "__main__":
    raise SystemExit(main())
