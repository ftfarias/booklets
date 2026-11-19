#!/usr/bin/env python3
"""
Mirror the cover SVG horizontally for heat-transfer vinyl.

HTV is cut on the BACK of the sheet (carrier film face down), so the
artwork must be mirrored or every letter transfers reversed. Silhouette
Studio can mirror on its own, but doing it here means the file that
reaches the machine is already correct and the step can't be forgotten.

Usage:  python3 cut_mirror.py cut_b.svg cut_b_mirrored.svg
"""
import re, sys
from pathlib import Path

def mirror(src: Path, dst: Path) -> None:
    s = src.read_text(encoding="utf-8")

    m = re.search(r'viewBox="0 0 ([\d.]+) ([\d.]+)"', s)
    if not m:
        sys.exit("could not read viewBox — is this a Typst-exported SVG?")
    w = float(m.group(1))

    # Wrap the whole document body in a flip about the vertical centre.
    open_tag = re.search(r"<svg[^>]*>", s).group(0)
    body = s[len(open_tag):s.rindex("</svg>")]
    s = (open_tag
         + f'<g transform="translate({w},0) scale(-1,1)">'
         + body
         + "</g></svg>")
    dst.write_text(s, encoding="utf-8")
    print(f"mirrored about x={w/2:.1f}pt -> {dst.name}")

if __name__ == "__main__":
    a = Path(sys.argv[1]) if len(sys.argv) > 1 else Path("cover/cut_b.svg")
    b = Path(sys.argv[2]) if len(sys.argv) > 2 else a.with_name(a.stem + "_mirrored.svg")
    mirror(a, b)
