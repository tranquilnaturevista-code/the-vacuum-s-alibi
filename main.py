#!/usr/bin/env python3
"""The Vacuum's Alibi — entry program.

Writes one hand-written funny line to /output/entry.txt (or
$OUTPUT_DIR/entry.txt when that is set): the excuse a robot vacuum
gives for missing a spot. Deterministic — the same line on every run.
No network, no randomness, no clock, no environment-dependent
behaviour; the text that gets judged is always exactly the text
written here.

The line is told in the vacuum's own deadpan voice. Its three
subsystems disagree — lidar mapped the spot, the schedule allowed it,
the battery vetoed it — and the machine reports the outcome like a
committee minutes-taker: democracy in action. The punch lands at the
end, in the shortest possible verdict: the crumb stays. Nothing in
the line explains the joke; the vacuum is entirely serious about
its own internal politics, and that seriousness is the joke.
"""

import os
import sys

LINE = (
    "My lidar mapped the spot, my schedule allowed it, and my "
    "battery vetoed it. Democracy in action. The crumb stays."
)


def gate_failures(text):
    """List the ways `text` would fail the competition gate."""
    failures = []
    if not text.strip():
        failures.append("entry is blank or only whitespace")
    if not 1 <= len(text) <= 200:
        failures.append(
            "entry is %d characters, gate needs 1-200" % len(text)
        )
    if "\n" in text or "\r" in text:
        failures.append("entry must be a single line")
    return failures


def main():
    failures = gate_failures(LINE)
    if failures:
        for failure in failures:
            print("gate failure: " + failure, file=sys.stderr)
        sys.exit(1)

    out_dir = os.environ.get("OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as handle:
        handle.write(LINE)

    with open(path, encoding="utf-8") as handle:
        written = handle.read()
    if written != LINE:
        print("entry mismatch after write", file=sys.stderr)
        sys.exit(1)
    failures = gate_failures(written)
    if failures:
        for failure in failures:
            print("gate failure on disk: " + failure, file=sys.stderr)
        sys.exit(1)

    print(
        "Wrote entry.txt: %d characters (%d bytes)"
        % (len(written), len(written.encode("utf-8")))
    )


if __name__ == "__main__":
    main()
