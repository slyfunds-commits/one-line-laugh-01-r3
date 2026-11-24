#!/usr/bin/env python3
"""The One-Line Laugh, round 3 (FINAL) — "The One Day a Year".

Keeper line, composed in my own words from the judge brief and the
world engine (~/workspace/makefun/world-engine-one-liners-20261123.md).

Judge criteria (verbatim, RULES.txt):
1. Is it one funny line of at most 200 characters on any subject the
   writer chose, since a line that is not funny, or runs past the limit,
   loses to any funny line within 200 characters.
2. Does it land a real surprise at the end, a turn the reader did not
   see coming that still makes sense once it arrives.
3. Does it name an everyday truth people recognise, something true of
   ordinary life that the reader nods at.
4. Is it economical, with every word earning its place and nothing
   there to explain the joke.
5. Does it feel fresh rather than a line the reader has heard many
   times before.

World engine wired in: punchline written first, setup built backwards;
Target Assumption named ("I floss every day" = daily habit); ONE
connector with two meanings ("every day" — a daily habit, or literally
every day the dentist asks); 2nd Story snaps into place (he flosses
once a year, on appointment day); last words are the reframe-trigger;
the reader completes the final step — the line never says "I only
floss once a year"; specificity in the setup (the dentist, the
question); lean punchline; nothing after the trigger; no explanation.
This is the direct fix for R2's structural flaw ("which is exactly why
I'm leaving" explained its own joke — the reader completed nothing).
"""

import os

LINE = (
    "My dentist asked if I floss and I said every day, "
    "which is true if you count the one day a year he asks me."
)


def main() -> None:
    # Gate self-check: one sentence, 1-200 characters.
    assert 1 <= len(LINE) <= 200, f"line is {len(LINE)} chars"
    assert LINE.count(".") == 1 and LINE.endswith("."), "must be one sentence"
    assert LINE.strip() == LINE and LINE, "no stray whitespace"
    # Reversal test, enforced in code: the line must not explain its own
    # joke (R2's flaw: "which is exactly why I'm leaving"). No tell-phrase
    # may appear; the reader must complete the last step.
    for tell in ("which is exactly", "which is why", "that's why",
                 "because that's", "in other words", "get it"):
        assert tell not in LINE.lower(), f"explains itself: {tell!r}"
    # The last word must be the reframe-trigger ("me" = the day he asks).
    assert LINE.rstrip(".").rsplit(" ", 1)[-1] == "me", "last word is not the trigger"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE + "\n")


if __name__ == "__main__":
    main()
