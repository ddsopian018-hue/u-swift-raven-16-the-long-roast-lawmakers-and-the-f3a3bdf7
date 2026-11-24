"""The Long Roast: Lawmakers and the File They Cannot Convert.

Writes one satirical sentence (1-320 characters, a single sentence) to
entry.txt in $MAKEFUN_OUTPUT_DIR (falling back to /output).

Pure Python standard library, deterministic, no network, no reads outside
this repository. The sentence is a fixed constant: the roast was drafted,
scored against the judge's five criteria, and chosen in-session, and this
program emits exactly that chosen sentence.
"""

import os
import sys

# Chosen sentence (312 characters). Drafted and scored in-session against
# the judge brief: authority set-up, then the undercut; aim kept on the
# lawmakers and the rules they write; punch lands on the last words;
# specific detail (87-page draft, nineteen-year-old intern, four seconds)
# instead of a worn tech-illiteracy cliche.
# The roast's craft: a committee chair who regulates AI, crypto and the
# internet, yet cannot turn a file into a PDF — and the nineteen-year-old
# intern who does it in four seconds.
SENTENCE = (
    "She chairs the committee that decides what your crypto wallet may hold, "
    "what your AI may say, and what the internet may show, yet this morning "
    "she forwarded her 87-page draft to an intern with one line \u2014 "
    "'can you make this a PDF, the button disappeared' \u2014 and the intern, "
    "who is nineteen, did it in four seconds."
)

MIN_CHARS = 1
MAX_CHARS = 320


def validate(sentence):
    """Refuse to emit anything outside the competition's shape."""
    if not (MIN_CHARS <= len(sentence) <= MAX_CHARS):
        raise ValueError(
            "sentence is %d characters, outside %d-%d"
            % (len(sentence), MIN_CHARS, MAX_CHARS)
        )
    if "\n" in sentence or "\r" in sentence:
        raise ValueError("sentence must not contain a newline")
    # Exactly one sentence: one terminal period, at the end, and no other
    # sentence-ending punctuation anywhere in the text.
    if not sentence.endswith("."):
        raise ValueError("sentence must end with a single period")
    if sentence[:-1].count(".") or "!" in sentence or "?" in sentence:
        raise ValueError("sentence must be exactly one sentence")
    return sentence


def main():
    sentence = validate(SENTENCE)
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(sentence)
    print("wrote %s (%d characters)" % (path, len(sentence)))
    return 0


if __name__ == "__main__":
    sys.exit(main())
