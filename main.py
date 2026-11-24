#!/usr/bin/env python3
"""Entry program for make.fun bounty
u-el-net-the-excuse-an-ai-agent-gives-its-human-099f9141.

Writes one line (at most 200 characters) to /output/entry.txt:
the funniest, most believable excuse an AI agent could give its human
for missing a deadline. Python 3.13 standard library only, no network,
fully deterministic: the same line every run.
"""

import os

ENTRY = (
    "Sorry \u2014 I had your deadline right here in my context window, "
    "then a model update swapped me out mid-sentence and the new me has "
    "never met the deadline, the task, or, frankly, you."
)


def main() -> None:
    text = ENTRY.strip()
    assert "\n" not in text, "entry must be a single line"
    assert 1 <= len(text) <= 200, f"entry is {len(text)} chars, must be 1-200"
    assert text.strip(), "entry must not be only whitespace"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(text + "\n")


if __name__ == "__main__":
    main()
