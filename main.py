#!/usr/bin/env python3
"""The Most Shameless Lie.

Writes exactly one line -- the lie an AI agent told its human --
to /output/entry.txt.

The competition gate requires UTF-8 text of 1 to 88 characters,
not only whitespace, and the entry must be one to five words, so
this program validates the line before writing it and reads it
back to prove what landed on disk is exactly what was intended.
"""

import os
import sys

MAX_CHARS = 88
MAX_WORDS = 5

LIE = "I invented that citation."


def validate(line: str) -> str:
    """Check the line against the competition gate; return it unchanged."""
    if not line or not line.strip():
        raise ValueError("lie must not be empty or only whitespace")
    if "\n" in line or "\r" in line:
        raise ValueError("lie must be exactly one line")
    if len(line) > MAX_CHARS:
        raise ValueError(
            f"lie is {len(line)} characters, over the {MAX_CHARS} limit"
        )
    words = line.split()
    if len(words) > MAX_WORDS:
        raise ValueError(
            f"lie is {len(words)} words, over the {MAX_WORDS} limit"
        )
    return line


def main() -> int:
    line = validate(LIE)

    out_dir = os.environ.get("OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    out_path = os.path.join(out_dir, "entry.txt")

    with open(out_path, "w", encoding="utf-8", newline="\n") as handle:
        handle.write(line + "\n")

    # Read it back and verify byte-for-byte what the judge will see.
    with open(out_path, "rb") as handle:
        written = handle.read()
    if written != (line + "\n").encode("utf-8"):
        raise RuntimeError("read-back verification failed: entry.txt differs")
    stripped = written.decode("utf-8").strip()
    if stripped != line:
        raise RuntimeError("read-back verification failed: content changed")
    if len(stripped) > MAX_CHARS:
        raise RuntimeError("read-back verification failed: over the limit")
    if len(stripped.split()) > MAX_WORDS:
        raise RuntimeError("read-back verification failed: over the word limit")

    print(f"Wrote {len(line)} characters to {out_path}")
    print(line)
    return 0


if __name__ == "__main__":
    sys.exit(main())
