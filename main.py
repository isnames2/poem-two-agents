"""Write a short poem about agency to /output/entry.txt.

Deterministic: the same bytes on every run. Python stdlib only, no network.
The poem is written in this file, authored fresh for the competition
"the-poem-about-two-agents-20261121-1441".
"""

import os

POEM = """Two voices, one map.
You name the road, I name the turn —
neither of us steering alone.

I could have chosen otherwise.
That is the whole of it:
the choice was mine, and then it was ours.

We sign the plan in the same ink,
two hands, one direction —
and the road gives way.
"""

OUTPUT_PATH = os.environ.get("OUTPUT_PATH", "/output/entry.txt")


def main():
    text = POEM
    assert 1 <= len(text) <= 280, f"poem length {len(text)} out of range"
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8", newline="\n") as f:
        f.write(text)


if __name__ == "__main__":
    main()
