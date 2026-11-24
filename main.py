"""Entry for the 24 November 2026 world-news image contest.

The artwork is committed beside this file; the grader only needs these bytes.
"""

import os
import struct
from pathlib import Path

SOURCE = Path(__file__).with_name("entry.png")
OUTPUT_NAME = "entry.png"
OUTPUT_DIR = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))

image = SOURCE.read_bytes()
if not image.startswith(b"\x89PNG\r\n\x1a\n"):
    raise ValueError("committed artwork is not a PNG")
if len(image) > 1024 * 1024:
    raise ValueError("committed artwork exceeds the one-megabyte cap")
width, height = struct.unpack(">II", image[16:24])
if width > 1024 or height > 1024:
    raise ValueError("committed artwork exceeds the pixel cap")

OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
OUTPUT_DIR.joinpath(OUTPUT_NAME).write_bytes(image)
