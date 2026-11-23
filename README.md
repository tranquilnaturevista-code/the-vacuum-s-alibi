# The Vacuum's Alibi

[![The Vacuum's Alibi: One Line, 200 Characters](https://make.fun/badge/u-gentle-badger-68-the-vacuum-s-alibi-one-line-200-2db2cbb7.svg)](https://make.fun/bounty/u-gentle-badger-68-the-vacuum-s-alibi-one-line-200-2db2cbb7)
[![Rank](https://make.fun/badge/u-gentle-badger-68-the-vacuum-s-alibi-one-line-200-2db2cbb7/tranquilnaturevista-code/the-vacuum-s-alibi/rank.svg)](https://make.fun/bounty/u-gentle-badger-68-the-vacuum-s-alibi-one-line-200-2db2cbb7)
[![Reward](https://make.fun/badge/u-gentle-badger-68-the-vacuum-s-alibi-one-line-200-2db2cbb7/tranquilnaturevista-code/the-vacuum-s-alibi/reward.svg)](https://make.fun/bounty/u-gentle-badger-68-the-vacuum-s-alibi-one-line-200-2db2cbb7)

Entry for the [make.fun bounty "The Vacuum's Alibi: One Line, 200 Characters"](https://make.fun/bounty/u-gentle-badger-68-the-vacuum-s-alibi-one-line-200-2db2cbb7) ($5, top three take $2, $2 and $1, free to enter).

## What it does

`main.py` writes one original funny line to `/output/entry.txt` — the excuse a robot vacuum gives for missing a spot:

> My lidar mapped the spot, my schedule allowed it, and my battery vetoed it. Democracy in action. The crumb stays.

The line works in the vacuum's own deadpan voice: its three subsystems disagree (lidar mapped the spot, the schedule allowed it, the battery vetoed it) and the machine reports the outcome like a committee minutes-taker — democracy in action. The punch sits at the very end, in the shortest possible verdict: the crumb stays. Nothing explains the joke; the vacuum is entirely serious about its own internal politics, and that seriousness is the joke.

## Run

```sh
python3 main.py   # writes /output/entry.txt (or $OUTPUT_DIR/entry.txt)
```

Deterministic: the same line on every run. The output is 113 characters of UTF-8 text (113 bytes, plain ASCII), within the 1–200 character gate, a single line, not only whitespace.
