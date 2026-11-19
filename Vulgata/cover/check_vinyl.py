#!/usr/bin/env python3
"""
Verify the vinyl cover is actually weedable before it goes to the Cameo.

Rasterizes the cover at 600 dpi and measures the real gold geometry:
every stroke the blade leaves behind must be wide enough to survive
having the surrounding waste pulled off it. Screen appearance says
nothing about this — the first draft looked fine and had 0.5mm strokes.
"""
import subprocess, sys
from pathlib import Path
from PIL import Image

ROOT = Path(__file__).parent
PNG  = Path("/tmp/_vinyl_check_600.png")

# Practical floor for weeding HTV by hand. Below this, thin strokes lift
# with the waste; the title survives far above it, small text does not.
MIN_STROKE_MM = 1.2
MIN_MARGIN_MM = 8.0

# Both faces are cut and weeded as separate pieces of vinyl.
SHEETS = {
    "front_vinyl.typ": {
        "title (Vanitas)": (155, 250,  64,  95),
        "subtitle":        (158, 265,  98, 118),
        "foot":            (158, 265, 155, 178),
        "band stack":      ( 42, 140,  48, 130),
    },
    "back_vinyl.typ": {
        "back bands":      ( 38,  84, 114, 144),
        "back EX VULGATA": ( 38, 150, 148, 172),
    },
}


def check_sheet(src: Path, regions: dict, fail: list) -> None:
    subprocess.run(["typst", "compile", "--format", "png", "--ppi", "600",
                    str(src), str(PNG)], check=True)
    im = Image.open(PNG).convert("RGB")
    W, H = im.size
    px = 600 / 25.4
    pix = im.load()
    gold = lambda p: p[0] > 140 and p[1] > 110 and p[2] < 120

    def runs(x0, x1, y0, y1):
        out = []
        for y in range(int(y0 * px), min(int(y1 * px), H)):
            c = 0
            for x in range(int(x0 * px), min(int(x1 * px), W)):
                if gold(pix[x, y]):
                    c += 1
                elif c:
                    out.append(c); c = 0
            if c:
                out.append(c)
        return sorted(out)

    print(f"{src.name}  ({W}x{H} @ 600dpi)")
    for label, box in regions.items():
        r = runs(*box)
        if not r:
            fail.append(f"{label}: no gold found — region box wrong?")
            print(f"  FAIL  {label}: nothing found")
            continue
        # p10 skips antialiasing slivers on curves; it is the real floor.
        p10 = r[len(r) // 10] / px
        med = r[len(r) // 2] / px
        if p10 < MIN_STROKE_MM:
            fail.append(f"{label}: strokes {p10:.2f}mm < {MIN_STROKE_MM}mm")
            print(f"  FAIL  {label:18s} p10 {p10:.2f}mm  median {med:.2f}mm")
        else:
            print(f"  ok    {label:18s} p10 {p10:.2f}mm  median {med:.2f}mm")

    # artwork must not run off the sheet
    left, right = W, 0
    for y in range(0, H, 4):
        for x in range(W):
            if gold(pix[x, y]):
                left = min(left, x); break
        for x in range(W - 1, -1, -1):
            if gold(pix[x, y]):
                right = max(right, x); break
    lm, rm = left / px, (W - right) / px
    if min(lm, rm) < MIN_MARGIN_MM:
        fail.append(f"margin {min(lm, rm):.1f}mm < {MIN_MARGIN_MM}mm")
        print(f"  FAIL  margins  left {lm:.1f}mm  right {rm:.1f}mm")
    else:
        print(f"  ok    margins  left {lm:.1f}mm  right {rm:.1f}mm")

    print()


def main() -> int:
    fail: list = []
    for name, regions in SHEETS.items():
        check_sheet(ROOT / name, regions, fail)
    if fail:
        print(f"{len(fail)} CHECK(S) FAILED")
        for f in fail:
            print("  -", f)
        return 1
    print("both faces are weedable")
    return 0


if __name__ == "__main__":
    sys.exit(main())
