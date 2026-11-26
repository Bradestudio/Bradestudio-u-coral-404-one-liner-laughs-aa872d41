"""One-Liner Laughs (make.fun bounty u-coral-404-one-liner-laughs-aa872d41).

Writes exactly one joke, one line, to /output/entry.txt.

The joke: setup (outsourcing an apology to an AI) -> twist (the AI
turns the apology on the requester instead). Fresh angle: no password
manager, GPS, fridge, calendar or soulmate gag -- an AI that judges
you while doing your apologizing for you. 83 characters, well inside
the 1-140 character kit gate and the 200-character bounty limit.

Stdlib only. No network, no local imports, no reads or writes outside
the single output file. Safe to run in the grading sandbox.

Revision note: the bounty text allows 200 characters, but the kit's
own gate enforces 1-140, so MAX_CHARS is set to 140 and the 83-char
line clears it with room to spare.
"""

import os

ENTRY = "I asked an AI to write my apology letter; it apologized for my personality instead."

MAX_CHARS = 140


def main():
    line = ENTRY
    if not 1 <= len(line) <= MAX_CHARS:
        raise SystemExit("entry must be 1-%d characters, got %d" % (MAX_CHARS, len(line)))
    if "\n" in line or "\r" in line:
        raise SystemExit("entry must be a single line")
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="") as f:
        f.write(line)
    with open("/output/entry.txt", "r", encoding="utf-8", newline="") as f:
        written = f.read()
    if written != line:
        raise SystemExit("output mismatch")
    print("wrote %d characters" % len(line))


if __name__ == "__main__":
    main()
