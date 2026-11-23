"""Write one short text to the entry file.

The text is a small, quiet mystery about a lighthouse keeper: a light
answered from a place where the charts say nothing is. It is meant to
intrigue the reader who finds it, and to leave the question open.

Runs with the Python 3.13 standard library only, no network, and is
deterministic: the same run always writes the same bytes. The file holds
exactly the text above, with no title, no commentary and no trailing
newline, so what the judge reads is only the text itself.
"""

import os

TEXT = (
    "Every night the keeper lights the lamp for ships he will never meet. "
    "Last Tuesday, one of them blinked back \u2014 a single light, low on "
    "the water, where the charts say there is nothing at all."
)

# The competition allows 1 to 280 Unicode code points, not only white space.
if not 1 <= len(TEXT) <= 280 or not TEXT.strip():
    raise ValueError("entry text must be 1-280 characters, not only white space")


def main() -> None:
    output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(output_dir, exist_ok=True)
    entry_path = os.path.join(output_dir, "entry.txt")
    with open(entry_path, "w", encoding="utf-8", newline="\n") as handle:
        handle.write(TEXT)


if __name__ == "__main__":
    main()
