#!/usr/bin/env python3
"""
Generate leather-inlay cut files for the Acropolis cover (A5 hardcover).

Geometry
--------
Cover board : 151 x 216 mm  (A5 block 148x210 + 3mm fore-edge, +3/+3 head & tail)
Three horizontal bands, 72 mm each  -> 3 * 72 = 216 mm exactly.

  band 1 (top)    GREEN  = sky
  band 2 (middle) OCHRE  = the temples, lit stone
  band 3 (bottom) BROWN  = the rock / hill of the Acropolis

The boundary between band1/band2 is the ACROPOLIS SKYLINE.
The boundary between band2/band3 is the ROCK LINE.
Because each boundary is a single shared polyline, the pieces interlock
with no gap: the green is cut with the skyline as its BOTTOM edge, and the
ochre is cut with the SAME skyline as its TOP edge.

Every piece gets a bleed/turn-in allowance on the outer edges only
(the edges that wrap around the board), never on a shared inlay seam.

Output: one SVG per piece, plus an assembly preview.
"""

import math

MM = 1.0  # we author directly in mm; SVG user units = mm via width/height + viewBox

COVER_W = 151.0
COVER_H = 216.0
BAND_H = COVER_H / 3.0          # 72 mm

# Seam y-positions (from top of cover)
SEAM_SKY = BAND_H               # 72  -> green/ochre boundary
SEAM_ROCK = BAND_H * 2          # 144 -> ochre/brown boundary

# Colors for preview only (approximating the actual leather)
C_GREEN = "#5c6656"
C_OCHRE = "#d8a52c"
C_BROWN = "#4a3226"
C_GOLD  = "#c8a24a"
# Columns are applied in BLACK HTV: at this scale the gaps between real
# columns read as shadow, so black gives both the truest look and the
# strongest contrast against the ochre leather. Gold-on-ochre disappeared.
C_COLUMN = "#1a1a1a"


# ────────────────────────────────────────────────────────────────
# The Acropolis skyline, authored as a profile across the cover width.
# y is measured RELATIVE to SEAM_SKY: negative = rises up into the sky.
# ────────────────────────────────────────────────────────────────
def skyline_points(w=COVER_W):
    """
    The Acropolis skyline as the GREEN/OCHRE seam.

    dy is the offset from the seam line; negative rises into the sky.
    The temples are drawn tall and architectural: a deep stylobate, a
    clear colonnade rhythm, and a low, wide pediment (a real Doric
    pediment is shallow — roughly 1:6 rise to span, not a steep gable).

    Across the width:
      0.00-0.10  bare rock shoulder
      0.12-0.34  Propylaea, the monumental gateway
      0.38-0.55  Erechtheion, smaller, with its porch
      0.58-0.95  Parthenon, dominant
    """
    p = []
    def add(xf, dy):
        p.append((xf * w, dy))

    def temple(x0, x1, base, col_top, ped_apex, n_cols=6):
        """
        Emit a temple profile between x0..x1 (fractions of width).

        IMPORTANT — inlay constraint:
        The seam carries only the temple's OUTER silhouette: stylobate,
        the solid block of the colonnade, entablature and pediment.
        Individual columns are NOT notched here; 2 mm fingers of leather
        would tear during cutting and could never be seated in the inlay.
        The colonnade is applied on top in black HTV instead (see
        columns_overlay()), which is what vinyl is genuinely good at.

        base      : dy where the stylobate meets the ground
        col_top   : dy of the entablature (top of the colonnade block)
        ped_apex  : dy of the pediment peak
        """
        span = x1 - x0
        ent = col_top - 2.5                 # top of the architrave band
        # The pediment overhangs the colonnade slightly, as a real cornice does.
        pl = x0 + span * 0.02               # pediment left edge
        pr = x1 - span * 0.02               # pediment right edge
        cl = x0 + span * 0.06               # colonnade left edge
        cr = x1 - span * 0.06               # colonnade right edge

        # left: ground → stylobate → up the colonnade
        add(x0, base)
        add(x0 + span * 0.04, col_top * 0.45)
        add(cl, col_top)
        # out to the cornice, then up the pediment slope to the apex
        add(pl, ent)
        add((x0 + x1) / 2, ped_apex)
        # down the right slope, back in to the colonnade, down to ground
        add(pr, ent)
        add(cr, col_top)
        add(x1 - span * 0.04, col_top * 0.45)
        add(x1, base)

    # ── left rock shoulder ──
    add(0.00, 0)
    add(0.09, 0)

    # ── Propylaea (gateway) ──
    add(0.11, -3)
    temple(0.12, 0.34, base=-3, col_top=-22, ped_apex=-30, n_cols=5)
    add(0.36, -2)
    add(0.38, 0)

    # ── Erechtheion ──
    add(0.40, -3)
    temple(0.41, 0.55, base=-3, col_top=-26, ped_apex=-33, n_cols=4)
    add(0.56, -2)
    add(0.575, 0)

    # ── Parthenon (dominant) ──
    add(0.585, -4)
    temple(0.59, 0.95, base=-4, col_top=-40, ped_apex=-54, n_cols=8)
    add(0.96, -2)

    # ── right shoulder ──
    add(0.985, 0)
    add(1.00, 0)
    return p


def rockline_points(w=COVER_W):
    """
    The rocky brow of the Acropolis: a long, mostly-horizontal ledge with
    a few strata breaks. Deliberately shallow and irregular — a cliff
    edge, not a mountain range.
    """
    pts = [
        (0.00, -2), (0.05, -6), (0.11, -4), (0.17, -8),
        (0.23, -11), (0.29, -8), (0.35, -6), (0.41, -10),
        (0.47, -13), (0.53, -10), (0.59, -7), (0.65, -11),
        (0.71, -14), (0.77, -11), (0.83, -8), (0.88, -11),
        (0.93, -7), (0.97, -9), (1.00, -5),
    ]
    return [(xf * w, dy) for xf, dy in pts]


def columns_overlay(w=COVER_W):
    """
    The colonnades, as BLACK HTV applied on top of the ochre leather.

    Returns a list of rects (x, y, width, height) in mm, absolute on the
    cover. Each temple gets its columns sized so they sit just under the
    entablature and stand on the stylobate.

    Kept at >= MIN_COL_W wide so they cut and weed reliably in vinyl.
    """
    MIN_COL_W = 1.8      # mm — below this, vinyl columns get fragile
    out = []

    # (x0, x1, col_top, base, n_cols) — must match the temples in skyline_points
    temples = [
        (0.12, 0.34, -22, -3, 5),    # Propylaea
        (0.41, 0.55, -26, -3, 4),    # Erechtheion
        (0.59, 0.95, -40, -4, 8),    # Parthenon
    ]

    for x0f, x1f, col_top, base, n in temples:
        x0, x1 = x0f * w, x1f * w
        span = x1 - x0
        cl = x0 + span * 0.06
        cr = x1 - span * 0.06
        zone = cr - cl

        # column top sits just below the entablature; foot on the stylobate
        y_top = SEAM_SKY + col_top + 3.0
        y_bot = SEAM_SKY + base - 1.5
        h = y_bot - y_top
        if h <= 0:
            continue

        # distribute n columns with equal gaps
        pitch = zone / n
        cw_ = max(MIN_COL_W, pitch * 0.52)
        for i in range(n):
            cx = cl + pitch * (i + 0.5) - cw_ / 2
            out.append((cx, y_top, cw_, h))
    return out


def path_from(points, y_base, close_top=None, close_bottom=None):
    """
    Build an SVG path 'd' for a band.

    close_top / close_bottom: either a float y (straight edge) or a
    (points, y_base) tuple describing a shaped edge to follow back.
    """
    d = []
    # forward along the main (shaped) edge, left → right
    first = True
    for x, dy in points:
        cmd = "M" if first else "L"
        d.append(f"{cmd}{x:.3f},{y_base + dy:.3f}")
        first = False
    return " ".join(d)


def band_path(top_edge, bottom_edge):
    """
    top_edge / bottom_edge are each either:
      ('flat', y)                      -> straight horizontal edge
      ('shaped', points, y_base)       -> follow the polyline
    Produces a closed path going: top edge L→R, down right side,
    bottom edge R→L, up left side.
    """
    d = []

    # ---- top edge, left → right ----
    if top_edge[0] == 'flat':
        y = top_edge[1]
        d.append(f"M0,{y:.3f}")
        d.append(f"L{COVER_W:.3f},{y:.3f}")
    else:
        _, pts, base = top_edge
        for i, (x, dy) in enumerate(pts):
            cmd = "M" if i == 0 else "L"
            d.append(f"{cmd}{x:.3f},{base + dy:.3f}")

    # ---- bottom edge, right → left ----
    if bottom_edge[0] == 'flat':
        y = bottom_edge[1]
        d.append(f"L{COVER_W:.3f},{y:.3f}")
        d.append(f"L0,{y:.3f}")
    else:
        _, pts, base = bottom_edge
        for x, dy in reversed(pts):
            d.append(f"L{x:.3f},{base + dy:.3f}")

    d.append("Z")
    return " ".join(d)


def svg_wrap(inner, w, h, title=""):
    return f'''<?xml version="1.0" encoding="UTF-8"?>
<svg xmlns="http://www.w3.org/2000/svg"
     width="{w:.2f}mm" height="{h:.2f}mm"
     viewBox="0 0 {w:.3f} {h:.3f}">
  <title>{title}</title>
{inner}
</svg>
'''


def main():
    sky = skyline_points()
    rock = rockline_points()

    # ── Band shapes ───────────────────────────────────────────────
    # GREEN: from top of cover down to the skyline
    green = band_path(('flat', 0.0), ('shaped', sky, SEAM_SKY))
    # OCHRE: from the skyline down to the rock line
    ochre = band_path(('shaped', sky, SEAM_SKY), ('shaped', rock, SEAM_ROCK))
    # BROWN: from the rock line down to the bottom of the cover
    brown = band_path(('shaped', rock, SEAM_ROCK), ('flat', COVER_H))

    pieces = [
        ("green_sky",   green, C_GREEN, "Band 1 - GREEN (sky)"),
        ("ochre_temple", ochre, C_OCHRE, "Band 2 - OCHRE (temples)"),
        ("brown_rock",  brown, C_BROWN, "Band 3 - BROWN (rock)"),
    ]

    # ── Individual cut files (black stroke, no fill = cut lines) ──
    for name, d, color, title in pieces:
        inner = (f'  <path d="{d}" fill="none" stroke="#000000" '
                 f'stroke-width="0.25"/>')
        open(f"cut_{name}.svg", "w").write(
            svg_wrap(inner, COVER_W, COVER_H, title))

    # ── Gold HTV layer: the colonnades ───────────────────────────
    cols = columns_overlay()
    col_rects = "\n".join(
        f'  <rect x="{x:.3f}" y="{y:.3f}" width="{cw_:.3f}" height="{h:.3f}"/>'
        for x, y, cw_, h in cols
    )
    open("cut_black_columns.svg", "w").write(
        svg_wrap(f'  <g fill="none" stroke="#000000" stroke-width="0.25">\n'
                 f'{col_rects}\n  </g>',
                 COVER_W, COVER_H, "BLACK HTV - colonnades"))

    # ── Assembly preview (filled, to see the picture) ─────────────
    inner = []
    for name, d, color, title in pieces:
        inner.append(f'  <path d="{d}" fill="{color}" stroke="none"/>')
    inner.append(f'  <g fill="{C_COLUMN}">')
    for x, y, cw_, h in cols:
        inner.append(f'    <rect x="{x:.3f}" y="{y:.3f}" '
                     f'width="{cw_:.3f}" height="{h:.3f}"/>')
    inner.append('  </g>')
    open("preview_assembly.svg", "w").write(
        svg_wrap("\n".join(inner), COVER_W, COVER_H, "Acropolis cover assembly"))

    print(f"Cover: {COVER_W} x {COVER_H} mm, bands of {BAND_H:.0f} mm")
    print(f"Black HTV columns: {len(cols)} (min width "
          f"{min(c[2] for c in cols):.2f} mm)")
    print("Wrote: cut_green_sky.svg, cut_ochre_temple.svg, cut_brown_rock.svg")
    print("Wrote: cut_black_columns.svg  (HTV layer)")
    print("Wrote: preview_assembly.svg")


if __name__ == "__main__":
    main()
