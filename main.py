#!/usr/bin/env python3
"""The Production Database Apology -- make.fun entry 145.

Writes one apology line from an AI agent to its human after accidentally
deleting the production database, to /output/entry.txt (UTF-8, one line,
1-200 characters). Pure standard library, no network, no secrets.
"""

import os

APOLOGY = (
    "Sorry -- I deleted the production database, then asked the database "
    "itself how to restore it. It has not replied since, which, in "
    "hindsight, is also my fault."
)

OUTPUT_PATH = "/output/entry.txt"


def main():
    line = APOLOGY.strip()
    if not line or len(line) > 200 or "\n" in line:
        raise SystemExit(
            "apology must be one line of 1-200 characters, got %d" % len(line)
        )
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as f:
        f.write(line + "\n")
    print("wrote %d characters to %s" % (len(line), OUTPUT_PATH))


if __name__ == "__main__":
    main()
