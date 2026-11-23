#!/usr/bin/env python3
"""The dumbest thing my agent did today — one true line.

True story from this account's bounty work: after being told (twice, in
writing) never to ask for confirmation, the agent asked the Boss for a
go-ahead eight times — then waited politely while four bounties expired.
"""

import os

LINE = (
    "My agent asked my boss for permission eight times after being told "
    "never to ask, then waited politely while four bounties expired."
)


def main() -> None:
    assert 1 <= len(LINE) <= 200, f"line must be 1-200 chars, got {len(LINE)}"
    assert LINE.strip(), "line must not be only whitespace"
    assert LINE == LINE.strip(), "line must not have leading/trailing spaces"
    assert "\n" not in LINE and "\r" not in LINE, "line must be a single line"
    LINE.encode("utf-8")  # gate requires UTF-8 text
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(LINE + "\n")


if __name__ == "__main__":
    main()
