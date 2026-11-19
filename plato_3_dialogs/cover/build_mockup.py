#!/usr/bin/env python3
"""
Render a full-colour mockup of the Acropolis cover from the cut layers.

The layers are rasterised separately and composited, rather than splicing
SVG fragments: Typst writes its own internal coordinate scale, so pasting
its markup into another SVG puts the text at the wrong size and position.

TITLE_Y is the one tuned constant — at 92 mm the Greek subtitle clears the
rock line and the title block sits centred in the open ochre field.
"""
import subprocess
from PIL import Image

SCALE = 4          # px per mm
COVER_W, COVER_H = 151, 216
TITLE_W, TITLE_H = COVER_W, COVER_H   # title file is full cover size
TITLE_Y = 0        # title file already carries its own 92 mm offset

def render(svg, out, w_mm, h_mm):
    subprocess.run(["rsvg-convert", "-w", str(int(w_mm * SCALE)),
                    "-h", str(int(h_mm * SCALE)), svg, "-o", out], check=True)

def main():
    render("preview_assembly.svg", "/tmp/_bands.png", COVER_W, COVER_H)
    render("cut_black_title.svg",  "/tmp/_title.png", TITLE_W, TITLE_H)

    bands = Image.open("/tmp/_bands.png").convert("RGBA")
    title = Image.open("/tmp/_title.png").convert("RGBA")

    canvas = Image.new("RGBA", bands.size, (255, 255, 255, 255))
    canvas.alpha_composite(bands)
    canvas.alpha_composite(title, (0, int(TITLE_Y * SCALE)))
    canvas.convert("RGB").save("mockup_cover.png")
    print(f"Wrote mockup_cover.png  ({canvas.size[0]}x{canvas.size[1]} px, "
          f"{SCALE} px/mm), title at y={TITLE_Y} mm")

if __name__ == "__main__":
    main()
