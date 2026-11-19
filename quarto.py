#!/usr/bin/env python3
"""
quarto.py — impose A6 portrait pages FOUR to a side on landscape A4, for
signatures folded twice ("in quarto").

Why: an A4→A5 fold puts the fold ACROSS the grain of ordinary long-grain
A4 (grain parallel to the 297 mm side). Folding twice puts the SECOND
fold — the spine — parallel to the grain. The first fold ends up at the
head and is slit open after sewing.

How each sheet is folded (the imposition below assumes exactly this):
  1. Sheet landscape, the FRONT side (odd output page) facing you.
  2. Fold the RIGHT half over onto the LEFT half (front side inside).
  3. Fold the TOP half down over the bottom half.
  4. The last fold is the spine; turn the packet so it is on the LEFT.
     The first fold is now along the TOP (head): slit it after sewing.
With --sheets 2 (default) two folded sheets are nested, the second inside
the first, opened at the centre: 16-page signatures.

The page order is not a table typed from memory: it is DERIVED by
simulating those two folds on the four cells of the sheet (see `layout`),
and the simulation asserts that no page comes out mirrored. Still: print
ONE sheet with --test and fold it before printing a book.

Usage:
  python3 quarto.py book.pdf -o book_quarto.pdf            # long-edge duplex
  python3 quarto.py book.pdf --short-edge
  python3 quarto.py --test -o quarto_test.pdf              # numbered dummy
"""
import argparse
from pathlib import Path
from pypdf import PdfReader, PdfWriter, Transformation

MM = 72 / 25.4
W, H = 297.0, 210.0            # sheet, landscape, mm
CW, CH = W / 2, H / 2          # cell 148.5 x 105 (an A6 lying on its side)


def layout():
    """Simulate the folds. Returns {page_in_sheet (1..8): (side, col, row, up)}
    where side is 'F'/'B' in FRONT-view coordinates, col/row index the 2x2
    cells (row 0 = bottom) and `up` is the page's upward direction (dx, dy)
    on the sheet as seen from the front."""
    cells = {}
    for c in (0, 1):
        for r in (0, 1):
            cells[(c, r)] = dict(p=[CW / 2 + c * CW, CH / 2 + r * CH],
                                 ex=[1.0, 0.0], ey=[0.0, 1.0], par=1, z=0.0)

    def fold(moving, reflect):
        zmax = max(s["z"] for s in cells.values())
        for s in cells.values():
            if moving(s["p"]):
                s["p"] = reflect(s["p"])
                for k in ("ex", "ey"):
                    s[k] = reflect(s[k], vector=True)
                s["par"] *= -1
                s["z"] = zmax + 1 + (zmax - s["z"])   # reversed, on top

    # 1. right half over left (about x = CW)
    fold(lambda p: p[0] > CW,
         lambda v, vector=False: [-v[0], v[1]] if vector else [W - v[0], v[1]])
    # 2. top half down over bottom (about y = CH)
    fold(lambda p: p[1] > CH,
         lambda v, vector=False: [v[0], -v[1]] if vector else [v[0], H - v[1]])

    # Packet is CW wide x CH tall, spine (fold 2) along its top edge, head
    # (fold 1) along its right edge. Turn it so the spine is on the left
    # and the head at the top: (x, y) -> (u, v) = (CH - y, x). A rotation
    # (det +1), so we are still looking at the top of the stack.
    def book(v):
        return [-v[1], v[0]]

    out = {}
    stack = sorted(cells.items(), key=lambda kv: -kv[1]["z"])   # top first
    for k, ((c, r), s) in enumerate(stack):
        exb, eyb = book(s["ex"]), book(s["ey"])
        # inverse of the (orthogonal) sheet->book map is its transpose
        def to_sheet(d):
            return (exb[0] * d[0] + exb[1] * d[1], eyb[0] * d[0] + eyb[1] * d[1])
        up = to_sheet((0, 1))
        for page, face_up, right in ((2 * k + 1, True, (1, 0)), (2 * k + 2, False, (-1, 0))):
            front_visible = (s["par"] > 0) == face_up
            side = "F" if front_visible else "B"
            rgt = to_sheet(right)
            # seen from the side it is printed on, a page must not be mirrored
            if side == "F":
                u, rr = up, rgt
            else:
                u, rr = (-up[0], up[1]), (-rgt[0], rgt[1])
            assert (rr[0], rr[1]) == (u[1], -u[0]), f"page {page} would be mirrored"
            out[page] = (side, c, r, up)
    assert sorted(out) == list(range(1, 9))
    return out


LAYOUT = layout()


def side_view(side, c, r, up, long_edge):
    """Front-view cell + up vector -> (col, row, up) as seen on that side's
    own PDF page. Long-edge back = sheet turned over about the vertical
    axis (booklet.py's --long-edge convention); short-edge = about the
    horizontal axis."""
    if side == "F":
        return c, r, up
    if long_edge:
        return 1 - c, r, (-up[0], up[1])
    return c, 1 - r, (up[0], -up[1])


def place(dst, src, col, row, up):
    """Rotate an A6 portrait page 90° into a landscape cell."""
    sw, sh = float(src.mediabox.width), float(src.mediabox.height)
    x0, y0 = col * CW * MM, row * CH * MM
    if up == (-1, 0):      # page top points left: rotate 90° CCW
        t = Transformation().rotate(90).translate(x0 + sh, y0)
    elif up == (1, 0):     # page top points right: rotate 90° CW
        t = Transformation().rotate(-90).translate(x0, y0 + sw)
    else:
        raise ValueError(f"unexpected orientation {up}")
    dst.merge_transformed_page(src, t)


def signature_pages(sig_index, sheets):
    """Global 0-based page index for (sheet s, page-in-sheet p) of a
    signature of `sheets` nested quartos. A folded quarto has 4 leaves;
    its first two leaves open the run and its last two close it, so the
    sheet nested inside takes the middle."""
    size = 8 * sheets
    base = sig_index * size
    table = {}
    for s in range(sheets):
        for p in range(1, 9):
            local = 4 * s + p if p <= 4 else size - 4 * s - (8 - p)
            table[(s, p)] = base + local - 1
    return table


def impose(reader, out_path, sheets, long_edge, blank):
    n = len(reader.pages)
    size = 8 * sheets
    nsig = -(-n // size)
    w = PdfWriter()
    for g in range(nsig):
        tab = signature_pages(g, sheets)
        for s in range(sheets):
            for side in ("F", "B"):
                dst = w.add_blank_page(width=W * MM, height=H * MM)
                for p, (sd, c, r, up) in LAYOUT.items():
                    if sd != side:
                        continue
                    i = tab[(s, p)]
                    src = reader.pages[i] if i < n else blank
                    if src is None:
                        continue
                    col, row, u = side_view(sd, c, r, up, long_edge)
                    place(dst, src, col, row, u)
    with open(out_path, "wb") as f:
        w.write(f)
    return nsig, nsig * sheets


def test_pdf(path):
    """8 numbered A6 pages with an arrow to the head — fold one sheet and
    the numbers must run 1–8, upright, with every arrow at the slit edge."""
    from pypdf import PageObject
    import io
    from pypdf.generic import ContentStream
    w = PdfWriter()
    for i in range(1, 9):
        pg = PageObject.create_blank_page(width=105 * MM, height=148.5 * MM)
        side = "recto" if i % 2 else "verso"
        txt = (f"BT /F1 120 Tf {28*MM:.1f} {60*MM:.1f} Td ({i}) Tj ET "
               f"BT /F1 14 Tf {30*MM:.1f} {135*MM:.1f} Td (^ CABECA ^) Tj ET "
               f"BT /F1 12 Tf {35*MM:.1f} {40*MM:.1f} Td ({side}) Tj ET")
        from pypdf.generic import (DictionaryObject, NameObject, StreamObject)
        font = DictionaryObject({NameObject("/Type"): NameObject("/Font"),
                                 NameObject("/Subtype"): NameObject("/Type1"),
                                 NameObject("/BaseFont"): NameObject("/Helvetica")})
        pg[NameObject("/Resources")] = DictionaryObject({
            NameObject("/Font"): DictionaryObject({NameObject("/F1"): font})})
        st = StreamObject()
        st.set_data(txt.encode())
        pg[NameObject("/Contents")] = w._add_object(st)
        w.add_page(pg)
    buf = io.BytesIO(); w.write(buf); buf.seek(0)
    return PdfReader(buf)


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("input", nargs="?")
    ap.add_argument("-o", "--output")
    ap.add_argument("--sheets", type=int, default=2, help="nested sheets per signature (default 2 = 16 pp)")
    ap.add_argument("--short-edge", action="store_true", help="impose for short-edge duplex")
    ap.add_argument("--test", action="store_true", help="impose a numbered 8-page dummy (one sheet)")
    a = ap.parse_args()
    if a.test:
        reader, sheets = test_pdf(None), 1
        out = a.output or "quarto_test.pdf"
    else:
        if not a.input:
            ap.error("input PDF required (or --test)")
        reader, sheets = PdfReader(a.input), a.sheets
        out = a.output or str(Path(a.input).with_name(Path(a.input).stem + "_quarto.pdf"))
    first = reader.pages[0].mediabox
    pw, ph = float(first.width) / MM, float(first.height) / MM
    if abs(pw - 105) > 1 or abs(ph - 148.5) > 1:
        raise SystemExit(f"pages are {pw:.1f}x{ph:.1f} mm; quarto.py expects A6 portrait 105x148.5")
    nsig, nsheets = impose(reader, out, sheets, not a.short_edge, None)
    edge = "short-edge" if a.short_edge else "long-edge"
    print(f"{len(reader.pages)} pages → {nsig} signature(s) of {8*sheets} pp = {nsheets} A4 sheets → {out}")
    print(f"Print: actual size, two-sided {edge} (from Adobe Reader the edge names are inverted — test one sheet).")


if __name__ == "__main__":
    main()
