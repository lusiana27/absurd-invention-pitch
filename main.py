"""One-Sentence Absurd Invention Pitch.

Writes exactly one sentence (188 characters) to /output/entry.txt.
Standard library only; clears only the contents of /output, never
the folder itself.
"""

import os

SENTENCE = (
    "The Sock Tribunal: a washing machine that puts every lone sock "
    "on trial, cross-examines the dryer under oath, and sentences "
    "the guilty lint to community service inside your remaining sock."
)


def main():
    out_dir = "/output"
    os.makedirs(out_dir, exist_ok=True)
    for name in os.listdir(out_dir):
        path = os.path.join(out_dir, name)
        if os.path.isfile(path) or os.path.islink(path):
            os.remove(path)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(SENTENCE)


if __name__ == "__main__":
    main()
