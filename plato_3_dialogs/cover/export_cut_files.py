#!/usr/bin/env python3
"""
Export every cut layer as a high-resolution black-on-white PNG for tracing
in Silhouette Studio, plus a repaired flat SVG for Inkscape.

Why this exists
---------------
Two things stopped the first cut files from opening usefully:

1. The leather band files were stroke-only (fill="none", 0.25 mm line).
   They *do* open, but render as a near-blank page, which reads as a
   broken file. Solid black fills trace and display reliably.

2. Typst's SVG export puts every glyph in a <symbol> and references it
   with xlink:href. Silhouette Studio often fails to resolve those, so
   the page comes up empty. Rasterising sidesteps it entirely.

PNGs are exported at TRACE_DPI with the physical size recorded in the
file, so Silhouette Studio imports them at the correct millimetre scale.
"""
import subprocess
from pathlib import Path

TRACE_DPI = 600                 # plenty for clean edge tracing
MM_PER_INCH = 25.4

# (source svg, output basename, width mm, height mm, human label)
LAYERS = [
    ("cut_green_sky.svg",     "trace_1_green_sky",     151, 216, "COURO VERDE - ceu"),
    ("cut_ochre_temple.svg",  "trace_2_ochre_temple",  151, 216, "COURO OCRE - templos"),
    ("cut_brown_rock.svg",    "trace_3_brown_rock",    151, 216, "COURO MARROM - rocha"),
    ("cut_black_columns.svg", "trace_4_black_columns", 151, 216, "HTV PRETO - colunas"),
    ("cut_black_title.svg",   "trace_5_black_title",   151, 216, "HTV PRETO - titulo"),
]


def solidify(svg_path: Path) -> str:
    """Return SVG markup with stroke-only outlines converted to solid fills."""
    s = svg_path.read_text()
    # Our generated band/column files use fill="none" + stroke. For tracing we
    # want the shape itself, filled solid black.
    s = s.replace('fill="none" stroke="#000000" stroke-width="0.25"',
                  'fill="#000000" stroke="none"')
    s = s.replace('<g fill="none" stroke="#000000" stroke-width="0.25">',
                  '<g fill="#000000" stroke="none">')
    return s


def px(mm: float) -> int:
    return int(round(mm / MM_PER_INCH * TRACE_DPI))


def main():
    here = Path(".")
    out_dir = here / "cut_files"
    out_dir.mkdir(exist_ok=True)

    for src, base, w_mm, h_mm, label in LAYERS:
        src_p = here / src
        if not src_p.exists():
            print(f"  !! missing {src}")
            continue

        # Typst files are already filled; ours need solidifying.
        tmp = out_dir / f"_{base}.svg"
        tmp.write_text(solidify(src_p))

        png = out_dir / f"{base}.png"
        subprocess.run([
            "rsvg-convert",
            "-w", str(px(w_mm)), "-h", str(px(h_mm)),
            "-b", "white",
            str(tmp), "-o", str(png),
        ], check=True)

        # Stamp the physical size into the PNG so Studio imports it to scale.
        subprocess.run([
            "sips", "-s", "dpiWidth", str(TRACE_DPI),
                    "-s", "dpiHeight", str(TRACE_DPI), str(png),
        ], check=True, capture_output=True)

        print(f"  {png.name:28s} {w_mm}x{h_mm} mm  @{TRACE_DPI}dpi   {label}")
        tmp.unlink()

    print(f"\nPNGs em {out_dir}/  —  importe no Silhouette Studio e use Trace.")


if __name__ == "__main__":
    main()
