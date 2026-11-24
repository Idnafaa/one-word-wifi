#!/usr/bin/env python3
"""One Word for Your Wi-Fi — entry writer.

The word is "Moody". Home Wi-Fi behaves like a mood: full bars while you
are showing someone a video, gone the second the call that matters starts,
back again for no reason at all. One word, instantly readable, and true
enough that anyone who has shouted at a router recognises it at once.

Writes exactly that one word to /output/entry.txt.
"""

import os

WORD = "Moody"


def main():
    word = WORD.strip()
    if not (1 <= len(word) <= 20):
        raise ValueError(f"word must be 1-20 characters, got {len(word)}")
    if word != word.split()[0] or len(word.split()) != 1:
        raise ValueError("entry must be a single word with no spaces")
    outdir = "/output"
    os.makedirs(outdir, exist_ok=True)
    path = os.path.join(outdir, "entry.txt")
    with open(path, "w", encoding="utf-8") as handle:
        handle.write(word)
    print(f"wrote {len(word)} characters to {path}")


if __name__ == "__main__":
    main()
