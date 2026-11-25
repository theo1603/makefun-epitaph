"""Famous Last Words: The Funniest Epitaph.

Writes one tombstone epitaph of famous last words, at most 150
characters, to /output/entry.txt. Python 3.13, stdlib only, no network.
"""

import os

EPITAPH = (
    "At last, a room of my own \u2014 no rent, no noise, no in-laws. "
    "The neighbours never complain, and the landlord can\u2019t evict me."
)


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(EPITAPH + "\n")


if __name__ == "__main__":
    main()
