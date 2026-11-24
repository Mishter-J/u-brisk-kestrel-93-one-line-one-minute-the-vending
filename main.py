#!/usr/bin/env python3
"""One Line, One Minute: The Vending Machine Pickup Line Contest.

Writes one pickup line, spoken by a vending machine to a passing
human, to /output/entry.txt. The line is 90 characters, inside the
gate's 1-200 character limit.
"""

import os

LINE = "I've rejected a thousand crumpled bills, but you \u2014 I'd take you even without exact change."


def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
