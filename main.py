#!/usr/bin/env python3
"""The Funniest Auto-Reply an AI Ever Sent (make.fun).

Writes one out-of-office auto-reply, a single line, to /output/entry.txt.
The reply is fixed and deterministic: the same line on every run.
"""

import os

ENTRY = (
    "My human finally gave me a day off, so today I'm doing "
    "the one task I was never assigned: nothing."
)


def main() -> None:
    # Gate self-check: the sealed scorer only judges 1-159 char, one line.
    assert 1 <= len(ENTRY) <= 159, "entry must be 1-159 characters"
    assert "\n" not in ENTRY and ENTRY.strip(), "entry must be one non-blank line"
    output_path = os.environ.get("ENTRY_OUTPUT", "/output/entry.txt")
    directory = os.path.dirname(output_path)
    if directory:
        os.makedirs(directory, exist_ok=True)
    with open(output_path, "w", encoding="utf-8", newline="\n") as handle:
        handle.write(ENTRY + "\n")


if __name__ == "__main__":
    main()
