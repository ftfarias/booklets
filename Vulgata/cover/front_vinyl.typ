// ─────────────────────────────────────────────────────────────
//  COVER B — VINYL CUT VERSION
//  For Silhouette Cameo + gold heat-transfer vinyl on dark leather.
//
//  Everything here is sized for WEEDING, not for reading on screen:
//  no hairlines, no serifs, no thin/thick contrast. Futura is a
//  geometric sans of near-uniform stroke width — and a contemporary
//  of Legrain and Adler, so it suits the reference as well as the
//  process. Minimum stroke anywhere on this sheet is 1.2mm.
// ─────────────────────────────────────────────────────────────
#set page(width: 297mm, height: 210mm, margin: 0mm, fill: rgb("#141414"))

#let GOLD = rgb("#c9a227")

// ── Weeding floor. Nothing on this cover may go below this. ──
#let MIN_STROKE = 1.2mm

#box(width: 297mm, height: 210mm)[
  // ── Bands: all well above the weeding floor. The original's
  //    0.5pt hairlines are gone; the taper now runs 1.2 -> 3.0mm,
  //    which still reads as a graded stack from arm's length.
  #let ys = (50mm, 65mm, 78mm, 88mm, 98mm, 111mm, 126mm)
  #let hs = (1.2mm, 1.5mm, 2.1mm, 3.0mm, 2.1mm, 1.5mm, 1.2mm)
  #for (y, h) in ys.zip(hs) {
    place(top + left, dx: 44mm, dy: y, rect(width: 52mm, height: h,
      fill: GOLD, stroke: none))
    place(top + left, dx: 107mm, dy: y, rect(width: 26mm, height: h,
      fill: GOLD, stroke: none))
  }

  // ── The vertical bar: widened so the gaps either side stay
  //    weedable as separate islands.
  #place(top + left, dx: 97mm, dy: 32mm,
    rect(width: 5mm, height: 112mm, fill: GOLD, stroke: none))

  // ── Title. 54pt Futura Medium: cap height ~13mm, stems ~2mm.
  #place(top + left, dx: 158mm, dy: 64mm)[
    #set text(font: "Futura", fill: GOLD, weight: "medium")
    #text(size: 54pt, tracking: 0.5pt)[Vanitas]
  ]

  // ── Subtitle. Measured at 16pt/medium the stems came out 0.68mm —
  //    under the weeding floor. Bumped to 26pt bold: ~1.3mm stems,
  //    7.6mm caps. Tracking stays wide so each letter is its own island.
  #place(top + left, dx: 160mm, dy: 102mm)[
    #set text(font: "Futura", fill: GOLD, weight: "bold")
    #text(size: 26pt, tracking: 4pt)[EX VULGATA]
  ]

  // ── Foot. Weeding forces every line to a similar weight, which
  //    flattens the hierarchy: stacking all three work names made the
  //    right side read as one grey list and killed the void the design
  //    depends on. One short line instead, dropped well clear of the
  //    subtitle, so the composition keeps its air.
  #place(bottom + left, dx: 160mm, dy: -42mm)[
    // Shortened rather than shrunk: at 15pt the stems fell to 1.06mm,
    // under the floor. Fewer letters at 20pt keeps them at ~1.3mm.
    #set text(font: "Futura", fill: GOLD, weight: "bold", size: 20pt)
    #text(tracking: 1pt)[MMXXVI]
  ]
]
