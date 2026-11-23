#!/usr/bin/env python3
"""Six Words, One Story — write the winning six-word story to /output/entry.txt.

The story: "She waited decades. He never came."
Six words, 34 characters. A complete story: a life of waiting, resolved by absence.
"""

import os

STORY = "She waited decades. He never came."


def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(STORY + "\n")


if __name__ == "__main__":
    main()
