#!/usr/bin/env python3
"""Six Words, One Story — write the winning six-word story to /output/entry.txt.

The story: "She waited decades. He never came."
Six words, 34 characters. A complete story: a life of waiting, resolved by absence.
"""

import os
import sys

STORY = "She waited decades. He never came."

# Gate (kit RULES.txt): /output/entry.txt must be UTF-8 text of 1-60
# characters, not only white space; the judge needs exactly six words.


def validate(story):
    """Fail loudly before writing anything invalid."""
    words = story.split()
    if len(words) != 6:
        print(
            f"error: story must be exactly six words, got {len(words)}: {story!r}",
            file=sys.stderr,
        )
        sys.exit(1)
    char_count = len(story)
    if not 1 <= char_count <= 60:
        print(
            f"error: story must be 1-60 characters, got {char_count}: {story!r}",
            file=sys.stderr,
        )
        sys.exit(1)
    if not story.strip():
        print("error: story must not be only white space", file=sys.stderr)
        sys.exit(1)


def main():
    validate(STORY)
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(STORY + "\n")


if __name__ == "__main__":
    main()
