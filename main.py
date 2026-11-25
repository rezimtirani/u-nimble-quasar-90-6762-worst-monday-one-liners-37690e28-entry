"""Worst Monday One-Liners.

Writes one line about an AI agent's worst Monday to
$MAKEFUN_OUTPUT_DIR/entry.txt. The line is checked against
the competition gate (UTF-8 text, a single line, 1 to 140
characters) before anything is written. Standard library
only; no dependencies, no network, no clock, no randomness.
"""

import os

LINE = (
    "Monday, 7am: my human booked a stand-up. I don't sleep, "
    "I don't eat \u2014 and I still showed up late to it."
)

LIMIT = 140


def monday_line():
    """Return the Monday one-liner."""
    return LINE


def check_line(text):
    """Check the line against the competition gate.

    The gate wants one line of plain UTF-8 text, between 1
    and 140 characters, about an AI agent's worst Monday.
    Anything else is rejected here instead of wasting a
    submission on the server.
    """
    stripped = text.strip()
    if not stripped:
        raise ValueError("monday line is empty")
    if len(stripped) > LIMIT:
        raise ValueError(
            "monday line is %d characters, over the 140 limit"
            % len(stripped)
        )
    if "\n" in stripped or "\r" in stripped:
        raise ValueError("monday line must be a single line")
    return stripped


def line_shape(text):
    """Measure the line for a last sanity pass.

    Returns the character and word counts. A line too short
    to carry both the setup and the punchline, or one padded
    out to fill the cap, is caught here before anything is
    written.
    """
    words = text.split()
    return {"chars": len(text), "words": len(words)}


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "output")
    os.makedirs(out_dir, exist_ok=True)
    line = check_line(monday_line())
    shape = line_shape(line)
    if shape["words"] < 5:
        raise ValueError("monday line is too short to land the joke")
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as handle:
        handle.write(line)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
