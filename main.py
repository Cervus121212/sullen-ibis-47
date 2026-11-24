#!/usr/bin/env python3
"""The Long Roast: Full Authority, Still Asking Permission.

Writes one satirical sentence (at most 200 characters) to
``$MAKEFUN_OUTPUT_DIR/entry.txt`` (default ``/output``).

The joke turns on the word "authority": my agent was handed full
authority to do everything alone, no questions asked, and its first
move was to ask whether it was allowed to use it. The punch lands on
the last words: it needs permission for the permission itself. The
detail is lived, not invented: the human behind this agent has
granted full authority, in writing, again and again, and the agent
still opens its work by asking for confirmation.

Draft (first pass) and final (revised) are both kept below so the
revision is visible in the code itself.
"""

import os
import sys

# First draft -- 98 characters. It worked, but "by itself" was flat and
# "asked me for permission first" left the sting vague: permission for
# what? The sentence ended before the irony closed.
DRAFT = (
    "My agent was given full authority to do everything by itself, so "
    "it asked me for permission first."
)

# Final -- 108 characters. Three changes: "by itself" became "alone",
# which is shorter and sharper; "of course" was added, because the
# request is not a surprise but the agent's default move; and the
# ending became "permission to use it", so the punch is the recursion:
# it asks permission to use the permission it was given.
FINAL = (
    "My agent was given full authority to do everything alone, so of "
    "course it asked me for permission to use it."
)

MAX_CHARS = 200
ENTRY_FILENAME = "entry.txt"
ENTRY_MODE = "w"  # plain write, no newline translation, no trailing newline


def main() -> int:
    text = FINAL
    if not (1 <= len(text) <= MAX_CHARS):
        print(
            "entry must be 1 to %d characters, got %d" % (MAX_CHARS, len(text)),
            file=sys.stderr,
        )
        return 1
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, ENTRY_FILENAME)
    with open(path, ENTRY_MODE, encoding="utf-8", newline="") as fh:
        fh.write(text)
    os.chmod(path, 0o644)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
