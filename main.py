"""The Tired Dark Lord: a 100-word villain monologue.

Writes one original monologue to /output/entry.txt.
Deterministic fixed text, standard library only, no network, no input.
"""

import os

TEXT = (
    "Hero. Sit. No\u2014not by the brazier. The smoke gets in my eyes, "
    "and I have... paperwork.\n"
    "\n"
    "Thirty years I have held this mountain. Thirty years of heroes, "
    "speeches, entrances at dawn. Do you know what dawn costs? The ravens "
    "want feeding. The moat wants dredging. The eclipse\u2014my eclipse, "
    "three centuries in the planning\u2014needs one sigil, and the ink "
    "keeps freezing.\n"
    "\n"
    "So. Your sword. Your speech. I have heard it all before, word for word. Twice. "
    "From your father.\n"
    "\n"
    "Leave the amulet. Take the stairs. And hero\u2014\n"
    "\n"
    "If the bards hear I yawned, I shall end the world out of spite."
)


def main():
    # Gate mirrors the sealed scorer: 1-600 characters, not only whitespace.
    assert 1 <= len(TEXT) <= 600 and TEXT.strip(), "TEXT must be 1-600 non-blank characters"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="") as f:
        f.write(TEXT)


if __name__ == "__main__":
    main()
