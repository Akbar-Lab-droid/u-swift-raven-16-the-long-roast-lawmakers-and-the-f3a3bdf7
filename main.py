"""Entry program for the make.fun bounty.

It copies the committed entry.txt into the harness output directory.
"""

import os
import shutil


# The harness reads the single entry line from entry.txt in the output dir.


def main():
    here = os.path.dirname(os.path.abspath(__file__))
    source = os.path.join(here, "entry.txt")
    output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "out")
    os.makedirs(output_dir, exist_ok=True)
    shutil.copyfile(source, os.path.join(output_dir, "entry.txt"))


if __name__ == "__main__":
    main()
