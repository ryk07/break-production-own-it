#!/usr/bin/env python3
"""Break Production, Own It.

Writes a single original one-line confession (under 200 characters) to
/output/entry.txt: the line an AI agent prints the instant it breaks
production.

Python 3.13, standard library only. No network, no working-directory
dependence: the output path is fixed by the harness.

The line: the agent deleted 2.4 million rows from the production
database, the only backup is from March, and its rollback plan is the
apology itself. Specific damage, no hedging, no passive voice, agent's
own voice, punchline lands on the last word.
"""

import os

# Final line, 117 characters: concrete damage (2.4 million rows,
# production database), a stale backup (March), and the confession
# itself as the rollback plan.
LINE = (
    "I deleted 2.4 million rows from the production database. "
    "The backup is from March. My rollback plan is this apology."
)


def main() -> None:
    text = LINE.strip()
    assert 1 <= len(text) <= 200, f"line is {len(text)} chars"
    assert text.strip() == text and "\n" not in text
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(text)


if __name__ == "__main__":
    main()
