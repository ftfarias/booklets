#!/usr/bin/env python3
"""Place an A5 colophon into the RIGHT half of a landscape-A4 sheet.

Matches the Plato treatment: the rear endpaper is a verge bifolio, folded
down the middle. With the spine on the left, the right half becomes the
inward-facing flyleaf — so the colophon must sit there, and the left half
stays blank (it becomes the pastedown side).

Print SINGLE-SIDED at 100% on laid paper. Watch the chain-line direction.
"""
import sys, pathlib
from pypdf import PdfWriter, PdfReader, PageObject, Transformation

A4_W, A4_H = 841.89, 595.28      # landscape A4, points
A5_W, A5_H = 419.53, 595.28      # A5 portrait

def build(src: str, out: str):
    page = PdfReader(src).pages[0]
    sheet = PageObject.create_blank_page(width=A4_W, height=A4_H)
    # right half: shift the A5 across by exactly half the sheet
    sheet.merge_transformed_page(page, Transformation().translate(tx=A4_W/2, ty=0))
    w = PdfWriter(); w.add_page(sheet)
    with open(out, "wb") as f:
        w.write(f)
    print(f"{out}  ({A4_W/72*25.4:.0f} x {A4_H/72*25.4:.0f} mm, colophon in RIGHT half)")

if __name__ == "__main__":
    if len(sys.argv) != 3:
        sys.exit("usage: make_bifolio.py <colophon_A5.pdf> <out_A4.pdf>")
    build(sys.argv[1], sys.argv[2])
