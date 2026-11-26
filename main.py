"""What the Elevator Would Say — make.fun entry.

Writes one line, the funniest thing an elevator would say if it could
talk, to /output/entry.txt. Standard library only.
"""

import os

ENTRY = "You pressed my button twice. I heard you the first time. Enjoy stopping at every floor on the way down."

MAX_CHARS = 120


def validate_entry(text):
    """Mirror the sealed gate: UTF-8 text, 1-120 chars, one line, not blank.

    Also rejects leading/trailing whitespace: the gate measures the exact
    bytes written, so a padded line would waste characters and read as cut.
    """
    if not isinstance(text, str) or not text.strip():
        raise ValueError("entry must be non-empty text")
    if text != text.strip():
        raise ValueError("entry must not start or end with whitespace")
    if len(text) > MAX_CHARS:
        raise ValueError(
            "entry is %d characters, over the %d limit" % (len(text), MAX_CHARS))
    if "\n" in text or "\r" in text:
        raise ValueError("entry must be a single line")
    if any(ord(c) < 32 for c in text):
        raise ValueError("entry contains control characters")
    return text


def main():
    line = validate_entry(ENTRY)
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(line)
    print("wrote %d characters to /output/entry.txt" % len(line))


if __name__ == "__main__":
    main()
