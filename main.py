#!/usr/bin/env python3
"""One Line, One Minute: The Vending Machine Pickup Line Contest.

Writes one pickup line, spoken by a vending machine to a passing
human, to /output/entry.txt. The line is 90 characters, inside the
gate's 1-200 character limit. Deterministic: no input, no network,
no randomness — the same line every run.
"""

import os

# The entry line, spoken by the machine itself: it leans on the
# machine's own world (rejected bills, exact change) and lands the
# punch in the last few words. 90 characters, within the 1-200 gate.
ENTRY_LINE = "I've rejected a thousand crumpled bills, but you \u2014 I'd take you even without exact change."

# Backwards-compatible alias kept for the original name.
LINE = ENTRY_LINE


def validate_line(line):
    """Gate check: 1-200 chars, not only whitespace (mirrors the kit gate)."""
    if not line.strip():
        raise ValueError("entry line must not be blank")
    if not 1 <= len(line) <= 200:
        raise ValueError("entry line must be 1-200 characters")
    return line


def write_entry(line, path="/output/entry.txt"):
    """Write the validated line to the entry file, creating /output."""
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "w", encoding="utf-8") as f:
        f.write(line)


def main():
    validate_line(ENTRY_LINE)
    write_entry(ENTRY_LINE)


if __name__ == "__main__":
    main()
