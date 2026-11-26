#!/usr/bin/env python3
"""One-Line Office Joke Laugh-Off entry.

Writes a single original one-line office joke to /output/entry.txt.
Stdlib only; no network, no files outside this repository.
"""

import os

# The entry: one line, first-person confession, one character (my boss),
# one scene (the Monday 9 a.m. meeting), turn in the final clause —
# the email I asked for turns out worse than the meeting.
ENTRY = (
    "I said our Monday 9 a.m. meeting could've been an email, "
    "so my boss made me send it: 47 slides to all 12 of us, "
    "with a read receipt."
)


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    data = ENTRY.encode("utf-8")
    with open("/output/entry.txt", "wb") as f:
        f.write(data)
    os.chmod("/output/entry.txt", 0o644)
    # Read back and assert byte equality with what we wrote.
    with open("/output/entry.txt", "rb") as f:
        back = f.read()
    assert back == data, "entry.txt does not match the entry bytes"


if __name__ == "__main__":
    main()
