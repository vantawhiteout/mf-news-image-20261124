"""Publish the committed 24 November 2026 news poster to /output/entry.png.

The picture is shipped in this repository and is never fetched or regenerated at
grading time. This script only checks that the bytes really are a small, whole
PNG and then places them where the grader looks for them. It uses the standard
library alone.
"""

from __future__ import annotations

import binascii
import struct
from pathlib import Path
from typing import Iterator

ARTWORK = Path(__file__).resolve().parent / "entry.png"
DESTINATION = Path("/output/entry.png")
SIGNATURE = b"\x89PNG\r\n\x1a\n"
BYTE_LIMIT = 1024 * 1024
EDGE_LIMIT = 1024


def read_chunks(data: bytes) -> Iterator[tuple[bytes, bytes]]:
    """Walk the PNG chunk stream, checking each length and CRC as we go."""
    cursor = len(SIGNATURE)
    while cursor < len(data):
        if cursor + 8 > len(data):
            raise ValueError("PNG ends inside a chunk header")
        size = struct.unpack_from(">I", data, cursor)[0]
        kind = data[cursor + 4:cursor + 8]
        end = cursor + 8 + size
        if end + 4 > len(data):
            raise ValueError("PNG ends inside chunk " + repr(kind))
        stored = struct.unpack_from(">I", data, end)[0]
        actual = binascii.crc32(data[cursor + 4:end]) & 0xFFFFFFFF
        if actual != stored:
            raise ValueError("PNG checksum mismatch in " + repr(kind))
        yield kind, data[cursor + 8:end]
        cursor = end + 4


def picture_edges(data: bytes) -> tuple[int, int]:
    """Validate the framing chunks and return the image dimensions."""
    if not data.startswith(SIGNATURE):
        raise ValueError("artwork is not a PNG")
    if len(data) > BYTE_LIMIT:
        raise ValueError("artwork is larger than one mebibyte")
    pieces = list(read_chunks(data))
    if not pieces or pieces[0][0] != b"IHDR" or len(pieces[0][1]) != 13:
        raise ValueError("artwork has no valid IHDR chunk")
    width, height = struct.unpack_from(">II", pieces[0][1])
    if not (0 < width <= EDGE_LIMIT and 0 < height <= EDGE_LIMIT):
        raise ValueError("artwork exceeds the 1024 pixel limit")
    if not any(kind == b"IDAT" for kind, _ in pieces):
        raise ValueError("artwork carries no image data")
    if pieces[-1][0] != b"IEND" or pieces[-1][1]:
        raise ValueError("artwork does not end with a clean IEND chunk")
    if any(kind == b"IEND" for kind, _ in pieces[:-1]):
        raise ValueError("artwork has data after its IEND chunk")
    return width, height


def publish(data: bytes, destination: Path) -> None:
    """Write the checked bytes to the requested path, creating its folder."""
    picture_edges(data)
    destination.parent.mkdir(parents=True, exist_ok=True)
    destination.write_bytes(data)


def main() -> None:
    publish(ARTWORK.read_bytes(), DESTINATION)


if __name__ == "__main__":
    main()
