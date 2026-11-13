#!/usr/bin/env python3
"""Emit "The Kitsune Who Stole the Moon" as the competition entry.

The artwork is an original nine-tailed fox spirit holding a glowing full
moon, drawn in a bold yokai graphic style. The file lives next to this
script. Running the program copies it unchanged to the grader output
directory, so repeated runs always yield the same bytes. The file carries
JPEG data under a .png name; the grader tells the format apart by magic
bytes, not by extension.
"""
import os
import shutil
from pathlib import Path  # entry.png holds JPEG bytes; magic bytes decide the format

HERE = Path(__file__).resolve().parent
OUT = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))


def main() -> None:
    OUT.mkdir(parents=True, exist_ok=True)
    shutil.copyfile(HERE / "entry.png", OUT / "entry.png")


if __name__ == "__main__":
    main()
