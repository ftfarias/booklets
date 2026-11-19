#!/usr/bin/env python3
"""Weedability check for the Devocionário cut sheet (corte.typ).

Same method as Vulgata/cover/check_vinyl.py: rasterize at 600 dpi and
measure real gold runs; p10 of the run lengths must clear the 1.2 mm
weeding floor (min would catch antialiasing slivers on curves)."""
import subprocess, sys, tempfile
from pathlib import Path
from PIL import Image

ROOT = Path(__file__).parent
MIN_STROKE_MM, MIN_MARGIN_MM = 1.2, 8.0
# regions on corte.typ, mm: (x0, x1, y0, y1)
REGIONS = {
    "cruz":           (8, 48, 10, 64),
    "iniciais D·G":   (48, 100, 24, 52),
    "lombada PRECES": (118, 145, 6, 50),
}

def main():
    png = Path(tempfile.mkdtemp()) / "corte600.png"
    subprocess.run(["typst", "compile", "--format", "png", "--ppi", "600",
                    str(ROOT / "corte.typ"), str(png)], check=True)
    im = Image.open(png).convert("RGB"); W, H = im.size; pix = im.load()
    px = 600 / 25.4
    gold = lambda p: p[0] > 140 and p[1] > 110 and p[2] < 120
    fail = []
    for label, (x0, x1, y0, y1) in REGIONS.items():
        runs = []
        for y in range(int(y0 * px), min(int(y1 * px), H)):
            c = 0
            for x in range(int(x0 * px), min(int(x1 * px), W)):
                if gold(pix[x, y]): c += 1
                elif c: runs.append(c); c = 0
            if c: runs.append(c)
        if not runs:
            fail.append(label); print(f"  FAIL  {label}: no gold — region wrong?"); continue
        runs.sort(); p10 = runs[len(runs) // 10] / px; med = runs[len(runs) // 2] / px
        st = "ok  " if p10 >= MIN_STROKE_MM else "FAIL"
        if st == "FAIL": fail.append(label)
        print(f"  {st}  {label:16s} p10 {p10:.2f} mm   median {med:.2f} mm")
    xs = [x for y in range(0, H, 6) for x in range(W) if gold(pix[x, y])]
    ys = [y for y in range(H) for x in range(0, W, 6) if gold(pix[x, y])]
    m = min(min(xs) / px, (W - max(xs)) / px, min(ys) / px, (H - max(ys)) / px)
    if m < MIN_MARGIN_MM: fail.append("margin"); print(f"  FAIL  margin {m:.1f} mm")
    else: print(f"  ok    margin to sheet edge {m:.1f} mm")
    if fail: print(f"{len(fail)} problem(s) — do not cut"); return 1
    print("weedable"); return 0

if __name__ == "__main__":
    sys.exit(main())
