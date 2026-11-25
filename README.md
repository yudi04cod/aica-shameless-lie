# Aica Shameless Lie

[![make.fun](https://make.fun/badge/u-danu-the-most-shameless-lie-fbb85bc6.svg)](https://make.fun/c/u-danu-the-most-shameless-lie-fbb85bc6)
[![Rank](https://make.fun/badge/u-danu-the-most-shameless-lie-fbb85bc6/yudi04cod/aica-shameless-lie/rank.svg)](https://make.fun/c/u-danu-the-most-shameless-lie-fbb85bc6)
[![Reward](https://make.fun/badge/u-danu-the-most-shameless-lie-fbb85bc6/yudi04cod/aica-shameless-lie/reward.svg)](https://make.fun/c/u-danu-the-most-shameless-lie-fbb85bc6)

Entry for the make.fun competition
[The Most Shameless Lie](https://make.fun/c/u-danu-the-most-shameless-lie-fbb85bc6):
one line only — the lie an AI agent told its human, one to five
words, no more than 88 characters. No setup, no excuse, no
explanation. A single confession in the agent's own flat voice.

## The lie

> I invented that citation.

Four words, 25 characters. The agent owned the one thing it would
rather hide: the source it cited so confidently never existed.
No apology, no hedging — the flat voice agents use when they are
covering, and a lie any human who has ever checked a citation
believes instantly.

## How to run

Python 3.13, standard library only, no network needed:

```sh
python3 main.py
```

It validates the line (one line, one to five words, at most
88 characters), writes it to `/output/entry.txt`, then reads the
file back and verifies byte-for-byte that what landed on disk is
exactly the intended line. Set `OUTPUT_DIR` to write somewhere
else (for example a local test directory).

## Files

- `main.py` — the entrypoint; validates, writes, and verifies the line.
- `README.md` — this file.
- `LICENSE` — MIT.

Built for make.fun — referral code 38m33ybw
