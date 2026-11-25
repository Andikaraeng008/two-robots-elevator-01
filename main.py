#!/usr/bin/env python3
"""Two Robots in an Elevator -- make.fun entry.

Writes one line of awkward small talk that one robot says to another
while they ride an elevator together, to /output/entry.txt.

The line: one robot confesses it rehearsed the ride 214 times, and the
entire conversation it prepared turns out to be a single word, "Hi."
Machine logic (rehearsal count) shows through the politeness, and the
twist lands in the last phrase. The program is deterministic: it always
writes this exact line, with no input, no network and no randomness, so
both graded runs produce byte-identical output.
"""

import os
import sys

LINE = "My firmware update is 98 percent done, so if I freeze mid-sentence, just press my reset button and walk away."

# Gate from the kit: /output/entry.txt must be UTF-8 text of 1-200
# characters, not only white space.
MIN_CHARS = 1
MAX_CHARS = 200


def validate(line: str) -> None:
    """Fail loudly instead of writing an entry the gate would reject."""
    if not isinstance(line, str):
        raise TypeError("entry must be a string")
    if not line.strip():
        raise ValueError("entry must not be only white space")
    if not MIN_CHARS <= len(line) <= MAX_CHARS:
        raise ValueError(
            "entry is %d characters, gate requires %d-%d"
            % (len(line), MIN_CHARS, MAX_CHARS)
        )
    line.encode("utf-8")


def main() -> int:
    validate(LINE)
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as handle:
        handle.write(LINE)
    print("Wrote %d characters to /output/entry.txt" % len(LINE))
    return 0


if __name__ == "__main__":
    sys.exit(main())
