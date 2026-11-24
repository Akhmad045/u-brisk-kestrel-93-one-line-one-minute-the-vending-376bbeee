"""One-line vending-machine pickup line entry.

Writes the entry line to /output/entry.txt (or $ENTRY_OUTPUT) with no
trailing newline. Stdlib only, deterministic, no network, no randomness.

The entry is validated before anything is written: it must be a single
line of 1-200 characters with no surrounding whitespace. An invalid
entry raises instead of writing a bad file.
"""

import os

ENTRY = "I'm stuck on you like a bag of chips in slot C3 \u2014 insert a coin and shake me loose."

MIN_CHARS = 1
MAX_CHARS = 200


def validate(text):
    if not isinstance(text, str):
        raise ValueError("entry must be a string")
    if text != text.strip():
        raise ValueError("entry must not have surrounding whitespace")
    if "\n" in text or "\r" in text:
        raise ValueError("entry must be a single line")
    if not MIN_CHARS <= len(text) <= MAX_CHARS:
        raise ValueError(
            "entry must be %d-%d characters, got %d"
            % (MIN_CHARS, MAX_CHARS, len(text))
        )
    if not text.strip():
        raise ValueError("entry must not be only whitespace")
    text.encode("utf-8")  # must be valid UTF-8
    return text


def main():
    entry = validate(ENTRY)
    path = os.environ.get("ENTRY_OUTPUT", "/output/entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(entry)


if __name__ == "__main__":
    main()
