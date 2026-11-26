"""Weirdest Job Title: a program that writes one job title to /output/entry.txt.

Final title, chosen over "Chief penguin counter, Antarctica, 3,000 penguins":
a professional mourner. Mourning for hire is a real job, and "47 funerals
a year" is the twist — a concrete, darkly funny workload that pictures the
person at once: crying at a stranger's funeral almost every week. The
penguin draft lost because its number restated the job (a counter counts);
here the number IS the joke.
"""

import os

LINE = "Professional mourner for hire, 47 funerals a year"


def main() -> None:
    # The gate only accepts 1-60 characters of non-blank text, so refuse to
    # write anything that would fail it instead of guessing.
    if not LINE.strip() or "\n" in LINE or not 1 <= len(LINE) <= 60:
        raise ValueError(
            f"entry line must be one line of 1-60 characters, got {len(LINE)}"
        )
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
