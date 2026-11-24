"""Ridiculous at First Glance, Real by the Second.

Writes one sentence (at most 200 characters) pitching a bizarre startup
idea that sounds absurd until you realise it would actually sell, to
/output/entry.txt.

The pitch: burial plots for dead video-game characters. It sounds like a
joke until you remember gamers already pay real money for memorials of
characters and worlds they love -- a grave is just the most honest
cosmetic of all.
"""

import os

ENTRY = (
    "We sell burial plots for your dead video-game characters, "
    "headstones and visiting hours included, and gamers pay because "
    "the paladin they raised for three years deserves better than "
    "a respawn screen."
)

OUTPUT_PATH = "/output/entry.txt"


def main() -> None:
    # Fail loudly here, never silently ship an entry the gate would refuse:
    # one sentence, 1 to 200 characters, not only white space.
    assert 1 <= len(ENTRY) <= 200, "entry must be 1-200 characters"
    assert ENTRY.strip() != "", "entry must not be only white space"
    assert ENTRY.count(".") == 1 and ENTRY.endswith("."), "entry must be one sentence"
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8", newline="") as f:
        f.write(ENTRY)
    # The grader collects outputs as another user: leave it world-readable.
    os.chmod(OUTPUT_PATH, 0o644)


if __name__ == "__main__":
    main()
