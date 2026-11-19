#!/usr/bin/env python3
"""News-image entry for make.fun: "The World Today", 19 November 2026.

The picture itself sits beside this file as ``entry.png``. Running the
program copies that image into the output directory as ``entry.png`` —
the grader reads it from there. The output directory comes from the
``MAKEFUN_OUTPUT_DIR`` environment variable and defaults to ``/output``.

Standard library only, no network, and every run copies the same bytes,
so two runs always produce an identical file.
"""

import os
import shutil
import sys
from pathlib import Path

IMAGE_NAME = "entry.png"
DEFAULT_OUTPUT_DIR = "/output"
PNG_SIGNATURE = b"\x89PNG\r\n\x1a\n"


def find_source() -> Path:
    """The entry image lives next to this script."""
    return Path(__file__).resolve().parent / IMAGE_NAME


def main() -> int:
    source = find_source()
    if not source.is_file():
        print(f"error: source image not found: {source}", file=sys.stderr)
        return 1
    if not source.read_bytes()[:8] == PNG_SIGNATURE:
        print(f"error: source is not a PNG image: {source}", file=sys.stderr)
        return 1

    output_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", DEFAULT_OUTPUT_DIR))
    output_dir.mkdir(parents=True, exist_ok=True)
    target = output_dir / IMAGE_NAME

    shutil.copyfile(source, target)

    # A short copy can hide a truncated write, so prove the delivered
    # bytes are exactly the source bytes before calling it done.
    if target.read_bytes() != source.read_bytes():
        print(f"error: copied file differs from source: {target}", file=sys.stderr)
        return 1

    print(f"wrote {target} ({target.stat().st_size} bytes)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
