#!/usr/bin/env python3
"""
booklet.py — Turn a PDF into ready-to-print A5 booklet signatures.

Two output styles:

1. IMPOSED (default) — produces ONE ready-to-print PDF where every output page
   is a LANDSCAPE A4 sheet holding two A5 pages side by side, already ordered
   and rotated for automatic short-edge duplex. You print it with NO booklet
   mode in Acrobat/Preview: just "Actual size, two-sided (short-edge)".
   Fold each sheet in half, nest the sheets of each signature, sew, done.

2. LEGACY reorder (--legacy) — the old behavior: reorders full A4 pages in
   booklet imposition order but does NOT compose 2-up. Requires the printer
   dialog's Booklet mode to place two pages per sheet. Kept for compatibility.
   With --manual-duplex it splits each signature into _front/_back files.

Imposition order for a 16-page signature (1-based page numbers within a signature):
  Sheet 1 front:  16,  1     Sheet 1 back:   2, 15
  Sheet 2 front:  14,  3     Sheet 2 back:   4, 13
  Sheet 3 front:  12,  5     Sheet 3 back:   6, 11
  Sheet 4 front:  10,  7     Sheet 4 back:   8,  9

Short-edge duplex note: the printer flips each sheet on its short edge, so the
back must be rotated 180° relative to the front for the text to read upright
after folding. The imposed mode does this automatically.

Usage:
  python3 booklet.py input.pdf                       # one imposed PDF (default)
  python3 booklet.py input.pdf -o ./out.pdf          # choose output file
  python3 booklet.py input.pdf --signature-size 8    # 8-page signatures
  python3 booklet.py input.pdf --long-edge           # impose for long-edge duplex
  python3 booklet.py input.pdf --legacy              # old reorder-only behavior
  python3 booklet.py input.pdf --legacy --manual-duplex
"""

import argparse
import math
import sys
from pathlib import Path

from pypdf import PdfReader, PdfWriter, PaperSize, Transformation
from pypdf.generic import RectangleObject


def signature_imposition(sig_size: int) -> list[int]:
    """
    Return 0-based indices in booklet imposition order for a signature of sig_size pages.
    sig_size must be a multiple of 4.
    The order pairs pages for double-sided printing: each pair is one sheet side.
    """
    assert sig_size % 4 == 0, "Signature size must be a multiple of 4"
    order = []
    lo, hi = 0, sig_size - 1
    while lo < hi:
        order.extend([hi, lo])   # front of sheet: outer-right, outer-left
        order.extend([lo + 1, hi - 1])  # back of sheet: inner-left, inner-right
        lo += 2
        hi -= 2
    return order


# A4 dimensions in PDF points (1 pt = 1/72 inch). A4 = 210 x 297 mm.
A4_W = 595.276  # portrait width
A4_H = 841.890  # portrait height
SHEET_W = A4_H  # landscape sheet width  (long side horizontal)
SHEET_H = A4_W  # landscape sheet height (short side vertical)
HALF_W = SHEET_W / 2  # width of each A5 slot on the landscape sheet


def place_page(writer_page, src_page, x_offset: float, rotate180: bool):
    """
    Scale src_page to fit one A5 slot (HALF_W x SHEET_H) and merge it onto
    writer_page at the given x offset. If rotate180, the page is turned 180°
    (used for back sides under short-edge duplex).
    """
    if src_page is None:
        return
    box = src_page.mediabox
    sw, sh = float(box.width), float(box.height)
    # Scale to fit the slot, preserving aspect ratio.
    scale = min(HALF_W / sw, SHEET_H / sh)
    dw, dh = sw * scale, sh * scale
    # Center within the slot.
    cx = x_offset + (HALF_W - dw) / 2
    cy = (SHEET_H - dh) / 2

    t = Transformation().scale(scale)
    if rotate180:
        # Rotate about the placed page's own center, then position.
        t = Transformation().translate(-sw / 2, -sh / 2).rotate(180).translate(sw / 2, sh / 2).scale(scale)
    t = t.translate(cx, cy)
    writer_page.merge_transformed_page(src_page, t)


def write_signature_imposed(writer, pages, reader, blank_page, long_edge: bool):
    """
    Compose an imposed booklet: each sheet becomes TWO landscape A4 output pages
    (front and back), each holding two A5 pages side by side.

    order is a flat list of pairs [front_left, front_right, back_left, back_right,...]
    Under short-edge duplex (default), back sides are rotated 180°.
    """
    order = signature_imposition(len(pages))
    num_sheets = len(pages) // 4
    for s in range(num_sheets):
        base = s * 4
        fl, fr = order[base], order[base + 1]       # front left, front right
        bl, br = order[base + 2], order[base + 3]   # back left, back right

        # Front side
        front = writer.add_blank_page(width=SHEET_W, height=SHEET_H)
        place_page(front, get_page(pages, fl, reader, blank_page), 0.0, rotate180=False)
        place_page(front, get_page(pages, fr, reader, blank_page), HALF_W, rotate180=False)

        # Back side.
        # Short-edge duplex flips the sheet about its short (top↔bottom) edge,
        # which rotates the back 180° AND mirrors left↔right. We compensate by
        # rotating each back page 180° *and* swapping the two slots, so the pair
        # lands correctly behind the front. Long-edge needs neither.
        back = writer.add_blank_page(width=SHEET_W, height=SHEET_H)
        if long_edge:
            place_page(back, get_page(pages, bl, reader, blank_page), 0.0, rotate180=False)
            place_page(back, get_page(pages, br, reader, blank_page), HALF_W, rotate180=False)
        else:
            place_page(back, get_page(pages, br, reader, blank_page), 0.0, rotate180=True)
            place_page(back, get_page(pages, bl, reader, blank_page), HALF_W, rotate180=True)


def pad_to_multiple(pages: list, multiple: int):
    """Return pages list padded with None entries to reach the next multiple."""
    remainder = len(pages) % multiple
    if remainder == 0:
        return list(pages)
    return list(pages) + [None] * (multiple - remainder)


def split_into_signatures(all_pages: list, sig_size: int) -> list[list]:
    """Split page list into chunks of sig_size, padding the last one if needed."""
    padded = pad_to_multiple(all_pages, sig_size)
    return [padded[i : i + sig_size] for i in range(0, len(padded), sig_size)]


def get_page(pages, idx, reader, blank_page):
    """Return the PDF page object for a given index, or a blank page for None."""
    page = pages[idx]
    if page is None:
        return blank_page
    return reader.pages[page]


def write_signature(writer: PdfWriter, pages: list, reader: PdfReader, blank_page):
    """Add pages in imposition order to writer. None entries become blank pages."""
    sig_size = len(pages)
    order = signature_imposition(sig_size)
    for idx in order:
        writer.add_page(get_page(pages, idx, reader, blank_page))


def write_signature_split(
    front_writer: PdfWriter,
    back_writer: PdfWriter,
    pages: list,
    reader: PdfReader,
    blank_page,
):
    """
    Split imposition order into front and back files for manual duplex printing.

    The imposition order is a flat list of pairs:
        [front_left, front_right, back_left, back_right,  ...]
    Each group of 4 = one sheet (2 front pages + 2 back pages).

    Front file  → sheets in order       (sheet 1, 2, 3 …)
    Back file   → sheets in REVERSE     (… sheet 3, 2, 1)
    """
    sig_size = len(pages)
    order = signature_imposition(sig_size)
    num_sheets = sig_size // 4

    # Collect (front_pair, back_pair) per sheet
    sheets = []
    for s in range(num_sheets):
        base = s * 4
        front_pair = order[base : base + 2]   # e.g. [15, 0]
        back_pair  = order[base + 2 : base + 4]  # e.g. [1, 14]
        sheets.append((front_pair, back_pair))

    # Front: sheets in order
    for front_pair, _ in sheets:
        for idx in front_pair:
            front_writer.add_page(get_page(pages, idx, reader, blank_page))

    # Back: sheets in REVERSE order
    for _, back_pair in reversed(sheets):
        for idx in back_pair:
            back_writer.add_page(get_page(pages, idx, reader, blank_page))


def make_blank_page(reader: PdfReader):
    """Create a blank page matching the size of the first page."""
    from pypdf import PdfWriter as _W
    first = reader.pages[0]
    w = PdfWriter()
    w.add_blank_page(
        width=float(first.mediabox.width),
        height=float(first.mediabox.height),
    )
    import io
    buf = io.BytesIO()
    w.write(buf)
    buf.seek(0)
    return PdfReader(buf).pages[0]


def create_imposed(input_path: str, output_path: str, sig_size: int = 16, long_edge: bool = False):
    """
    Produce ONE ready-to-print PDF: landscape A4 sheets, two A5 pages each,
    ordered and rotated for automatic duplex. Signatures are concatenated in
    order, so the whole book prints in a single job.
    """
    assert sig_size % 4 == 0, "Signature size must be a multiple of 4"
    src = Path(input_path)
    out = Path(output_path)
    out.parent.mkdir(parents=True, exist_ok=True)

    reader = PdfReader(str(src))
    total = len(reader.pages)
    blank = make_blank_page(reader)
    all_pages = list(range(total))
    signatures = split_into_signatures(all_pages, sig_size)
    num_sigs = len(signatures)

    edge = "long-edge" if long_edge else "short-edge"
    print(f"Input: {src.name}  ({total} pages)")
    print(f"Signature size: {sig_size} pages → {num_sigs} signature(s)  [imposed 2-up, {edge} duplex]")

    writer = PdfWriter()
    for i, sig in enumerate(signatures, start=1):
        actual = [p for p in sig if p is not None]
        blanks = sig.count(None)
        blank_note = f" (+{blanks} blank)" if blanks else ""
        write_signature_imposed(writer, sig, reader, blank, long_edge)
        print(f"  [{i}/{num_sigs}] pages {actual[0]+1}–{actual[-1]+1}{blank_note}")

    with open(out, "wb") as f:
        writer.write(f)
    sheets = sum(len(s) // 2 for s in signatures)
    print(f"Wrote {len(writer.pages)} output pages ({sheets} sheets) → {out}")
    print("Print with: Actual size, Two-Sided (%s), NO booklet mode." % edge)
    print("Done.")


def create_booklets(input_path: str, output_dir: str, sig_size: int = 16, manual_duplex: bool = False):
    assert sig_size % 4 == 0, "Signature size must be a multiple of 4"

    src = Path(input_path)
    out = Path(output_dir)
    out.mkdir(parents=True, exist_ok=True)

    reader = PdfReader(str(src))
    total = len(reader.pages)
    print(f"Input: {src.name}  ({total} pages)")

    blank = make_blank_page(reader)
    all_pages = list(range(total))
    signatures = split_into_signatures(all_pages, sig_size)
    num_sigs = len(signatures)
    mode = "manual duplex (front+back)" if manual_duplex else "duplex"
    print(f"Signature size: {sig_size} pages → {num_sigs} signature(s)  [{mode}]")

    for i, sig in enumerate(signatures, start=1):
        actual = [p for p in sig if p is not None]
        blanks = sig.count(None)
        blank_note = f" (+{blanks} blank)" if blanks else ""
        label = f"signature_{i:03d}_of_{num_sigs:03d}"

        if manual_duplex:
            front_path = out / f"{src.stem}_{label}_front.pdf"
            back_path  = out / f"{src.stem}_{label}_back.pdf"

            front_writer = PdfWriter()
            back_writer  = PdfWriter()
            write_signature_split(front_writer, back_writer, sig, reader, blank)

            with open(front_path, "wb") as f:
                front_writer.write(f)
            with open(back_path, "wb") as f:
                back_writer.write(f)

            print(f"  [{i}/{num_sigs}] pages {actual[0]+1}–{actual[-1]+1}{blank_note}")
            print(f"           front → {front_path.name}")
            print(f"           back  → {back_path.name}")
        else:
            out_path = out / f"{src.stem}_{label}.pdf"
            writer = PdfWriter()
            write_signature(writer, sig, reader, blank)
            with open(out_path, "wb") as f:
                writer.write(f)
            print(f"  [{i}/{num_sigs}] pages {actual[0]+1}–{actual[-1]+1}{blank_note} → {out_path.name}")

    print("Done.")


def main():
    parser = argparse.ArgumentParser(
        description="Split a PDF into booklet signatures with imposition page order."
    )
    parser.add_argument("input", help="Input PDF file")
    parser.add_argument(
        "--output", "-o", default=None,
        help="Output PDF file (imposed mode) or directory (legacy mode)",
    )
    parser.add_argument(
        "--signature-size", "-s", type=int, default=16,
        help="Pages per signature, must be a multiple of 4 (default: 16)",
    )
    parser.add_argument(
        "--long-edge", action="store_true",
        help="Impose for long-edge duplex instead of the default short-edge",
    )
    parser.add_argument(
        "--legacy", action="store_true",
        help="Old behavior: reorder full pages only (needs Acrobat Booklet mode)",
    )
    parser.add_argument(
        "--manual-duplex", "-m", action="store_true",
        help="(legacy only) split each signature into _front.pdf and _back.pdf",
    )
    args = parser.parse_args()

    if args.signature_size % 4 != 0:
        print("Error: --signature-size must be a multiple of 4", file=sys.stderr)
        sys.exit(1)

    src = Path(args.input)
    if not src.exists():
        print(f"Error: file not found: {src}", file=sys.stderr)
        sys.exit(1)

    if args.legacy:
        output_dir = args.output or str(src.parent / f"{src.stem}_booklet")
        create_booklets(str(src), output_dir, args.signature_size, args.manual_duplex)
    else:
        if args.manual_duplex:
            print("Note: --manual-duplex only applies to --legacy; ignoring.", file=sys.stderr)
        output_path = args.output or str(src.parent / f"{src.stem}_booklet.pdf")
        create_imposed(str(src), output_path, args.signature_size, args.long_edge)


if __name__ == "__main__":
    main()
