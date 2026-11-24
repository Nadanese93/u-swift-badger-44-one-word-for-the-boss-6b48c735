#!/usr/bin/env python3
"""One Word for the Boss — copies entry.txt to the harness output path.

The entry is a single word describing the boss. The gate allows 1-30
characters of UTF-8 text, not only white space; the guards below enforce
the gate locally so a bad entry fails loudly here instead of silently
scoring 0 on the server.
"""
import os

MAX_CHARS = 30

ENTRY_FILE = os.path.join(os.path.dirname(os.path.abspath(__file__)), "entry.txt")


def main():
    with open(ENTRY_FILE, "r", encoding="utf-8") as f:
        text = f.read()
    if not (1 <= len(text) <= MAX_CHARS):
        raise ValueError(f"entry must be 1-{MAX_CHARS} chars, got {len(text)}")
    if len(text.split()) != 1:
        raise ValueError("entry must be exactly one word")
    if not text.strip():
        raise ValueError("entry must not be only white space")
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(text)
    os.chmod(path, 0o644)


if __name__ == "__main__":
    main()
