#!/usr/bin/env python3
"""Build assets/code/chapter-11/deskside-tickets.csv (Chapter 11).

A synthetic sample of 80 tickets that Copperwind's Deskside team closed
over four weeks. The table holds no client names, requester names, or
account details, only a client type, so students may paste or upload it.

Why seeded: the Section 11.3 data question and Skills Lab 11A quote
counts and totals from this file, so every rebuild must be byte-identical. The base
seed is 137, the course number.

Engineered properties (asserted below, because the lessons depend on
them):

* 80 rows, 6 columns, the six Deskside ticket categories from Part II.
* Password reset has the most tickets, but new-hire device setup takes
  the most technician minutes, so "most tickets" and "most time" give
  different answers.
* Some first replies took exactly 30 minutes. The target is a first
  reply within 30 minutes, so those rows meet it, and a careless count
  of "30 or more" gets the wrong answer.
* VPN connection failure has more missed first replies (over 30
  minutes) than any other category.

Usage, from the repo root:
    python3 assets/code/_generators/gen_deskside_tickets.py
"""

from __future__ import annotations

import csv
import hashlib
import io
import random
from collections import Counter, defaultdict
from pathlib import Path

SEED = 137
OUT = (Path(__file__).resolve().parents[1] / "chapter-11"
       / "deskside-tickets.csv")

# Tickets per category in the sample. Fixed, not drawn, so the
# most-tickets answer never moves.
CATEGORY_COUNTS = {
    "password reset": 21,
    "printer offline": 15,
    "VPN connection failure": 14,
    "shared mailbox access": 12,
    "slow laptop": 10,
    "new-hire device setup": 8,
}
# Technician handle minutes per ticket, as (low, high) ranges. New-hire
# setups are few and long, which is the point of the sample.
HANDLE_RANGE = {
    "password reset": (6, 14),
    "printer offline": (10, 30),
    "VPN connection failure": (15, 40),
    "shared mailbox access": (8, 18),
    "slow laptop": (20, 45),
    "new-hire device setup": (60, 95),
}
CLIENT_TYPES = ["medical office", "physical therapy office", "law office",
                "accounting office", "retail store", "nonprofit"]


def first_reply(rng: random.Random, category: str) -> int:
    """Minutes to the first reply. VPN tickets wait longer on purpose."""
    if category == "VPN connection failure":
        return rng.choice([12, 18, 25, 30, 34, 38, 41, 47, 22, 36])
    return rng.choice([4, 7, 9, 11, 14, 16, 19, 22, 26, 30, 33, 8, 12])


def build() -> list[dict]:
    rng = random.Random(SEED)
    rows = []
    for category, count in CATEGORY_COUNTS.items():
        low, high = HANDLE_RANGE[category]
        for _ in range(count):
            rows.append({
                "category": category,
                "client_type": rng.choice(CLIENT_TYPES),
                "week": rng.randint(1, 4),
                "first_reply_minutes": first_reply(rng, category),
                "handle_minutes": rng.randint(low, high),
            })
    rng.shuffle(rows)
    rows.sort(key=lambda r: r["week"])
    for n, row in enumerate(rows, 1):
        row["ticket_id"] = f"DS-{n:03d}"
    return rows


def check(rows: list[dict]) -> None:
    assert len(rows) == 80, len(rows)
    tickets = Counter(r["category"] for r in rows)
    minutes = defaultdict(int)
    misses = Counter()
    for r in rows:
        minutes[r["category"]] += r["handle_minutes"]
        if r["first_reply_minutes"] > 30:
            misses[r["category"]] += 1
    most_tickets = tickets.most_common(1)[0][0]
    most_minutes = max(minutes, key=minutes.get)
    assert most_tickets == "password reset", most_tickets
    assert most_minutes == "new-hire device setup", most_minutes
    assert most_tickets != most_minutes
    # No tie for most minutes, so the answer is unambiguous.
    top = sorted(minutes.values(), reverse=True)
    assert top[0] - top[1] >= 20, top
    exactly_30 = sum(1 for r in rows if r["first_reply_minutes"] == 30)
    assert exactly_30 >= 3, exactly_30
    assert misses.most_common(1)[0][0] == "VPN connection failure", misses
    worst, runner_up = [v for _, v in misses.most_common(2)]
    assert worst > runner_up, misses
    weeks = Counter(r["week"] for r in rows)
    assert set(weeks) == {1, 2, 3, 4}, weeks


def to_csv(rows: list[dict]) -> str:
    fields = ["ticket_id", "week", "category", "client_type",
              "first_reply_minutes", "handle_minutes"]
    buf = io.StringIO()
    writer = csv.DictWriter(buf, fieldnames=fields, lineterminator="\n")
    writer.writeheader()
    for r in rows:
        writer.writerow({k: r[k] for k in fields})
    return buf.getvalue()


def main() -> None:
    rows = build()
    check(rows)
    text = to_csv(rows)
    # Build twice and compare, so a hidden source of randomness fails
    # here instead of in a student's data pack.
    assert to_csv(build()) == text
    OUT.write_text(text, encoding="utf-8")
    digest = hashlib.sha256(text.encode("utf-8")).hexdigest()[:12]
    print(f"wrote {OUT.name}: {len(rows)} rows, sha256 {digest}")


if __name__ == "__main__":
    main()
