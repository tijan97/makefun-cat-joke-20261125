#!/usr/bin/env python3
"""One-line cat joke entry for make.fun.

Writes the entry text to entry.txt inside the output directory
given by MAKEFUN_OUTPUT_DIR (or OUTPUT_DIR, or /output).
"""
import os

ENTRY = "my cat pushed my glass off the table, watched it shatter, then looked at me like I should have caught it."


def main():
    # Validation (grader gate): 1-200 chars, not only whitespace, valid UTF-8.
    if not ENTRY or len(ENTRY) > 200 or not ENTRY.strip():
        raise SystemExit("entry text failed validation: must be 1-200 non-blank characters")
    ENTRY.encode("utf-8")
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or os.environ.get("OUTPUT_DIR") or "/output"
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(ENTRY)
    # Verify what was written is byte-identical to the entry text.
    with open(path, "rb") as f:
        if f.read() != ENTRY.encode("utf-8"):
            raise SystemExit("written output does not match entry text")


if __name__ == "__main__":
    main()
