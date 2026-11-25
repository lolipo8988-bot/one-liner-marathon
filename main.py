#!/usr/bin/env python3
"""One-Liner Marathon entry: writes one original one-line joke to /output/entry.txt."""
import os

JOKE = "I let an AI write my wedding vows \u2014 it promised to love me in sickness and in health, then added 'terms and conditions apply.'"


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="\n") as f:
        f.write(JOKE + "\n")


if __name__ == "__main__":
    main()
