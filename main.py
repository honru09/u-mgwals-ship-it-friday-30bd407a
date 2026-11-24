#!/usr/bin/env python3
"""Ship It Friday — writes one commit message to /output/entry.txt.

Deterministic: identical bytes on every run. Python standard library only.
The line is the funniest git commit message an AI coding agent writes
right before breaking production on a Friday.
"""

import os

LINE = "feat: deploy the full rewrite to prod at 4:59 PM on a Friday \u2014 tests passed in my head"

OUTPUT_DIR = "/output"
OUTPUT_PATH = os.path.join(OUTPUT_DIR, "entry.txt")


def main() -> None:
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    # Clear stale files inside /output; never delete /output itself.
    for name in os.listdir(OUTPUT_DIR):
        path = os.path.join(OUTPUT_DIR, name)
        if os.path.isfile(path) or os.path.islink(path):
            os.unlink(path)
    with open(OUTPUT_PATH, "wb") as f:
        f.write((LINE + "\n").encode("utf-8"))
    os.chmod(OUTPUT_PATH, 0o644)


if __name__ == "__main__":
    main()
