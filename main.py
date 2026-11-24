#!/usr/bin/env python3
"""One-Line Roast: The Gadget You Use Every Day.

Writes a single original roast line to /output/entry.txt.
Deterministic: no input, no clock, no randomness, no network.
"""

from pathlib import Path

ROAST = (
    'My fitness tracker buzzed "time to move!" while I carried '
    "groceries up three flights of stairs."
)


def validate(line: str) -> None:
    """Enforce the bounty gate: 1-200 chars, one line, not blank."""
    if not (1 <= len(line) <= 200):
        raise ValueError(f"roast must be 1-200 chars, got {len(line)}")
    if "\n" in line or "\r" in line:
        raise ValueError("roast must be a single line")
    if not line.strip():
        raise ValueError("roast must not be only whitespace")


def main() -> None:
    validate(ROAST)
    out = Path("/output/entry.txt")
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(ROAST, encoding="utf-8")


if __name__ == "__main__":
    main()
