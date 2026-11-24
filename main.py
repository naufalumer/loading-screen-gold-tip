"""make.fun entry: "Loading Screen Gold: A Tip in 200 Characters".

Writes one original funny loading-screen tip for stressed developers
and AI coding agents, a single line of at most 200 characters, to
$MAKEFUN_OUTPUT_DIR/entry.txt. Standard library only; no network,
no files read, no randomness: the output is byte-identical every run.
"""

import os
import sys
from pathlib import Path

TIP = "Tip: this bar isn't stuck. It's giving you a moment to accept your agent understood your ticket better than you did. Breathe."

LIMIT = 200


def check_tip(text):
    """The sealed gate: one line, 1-200 characters, not only whitespace."""
    if not text.strip():
        return "tip is blank"
    if len(text) > LIMIT:
        return "tip is longer than 200 characters"
    if "\n" in text or "\r" in text:
        return "tip must be a single line"
    return None


def write_entry():
    problem = check_tip(TIP)
    if problem is not None:
        print("entry fails the gate: " + problem, file=sys.stderr)
        raise SystemExit(1)
    out_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    out_dir.mkdir(parents=True, exist_ok=True)
    (out_dir / "entry.txt").write_text(TIP, encoding="utf-8")


if __name__ == "__main__":
    write_entry()
