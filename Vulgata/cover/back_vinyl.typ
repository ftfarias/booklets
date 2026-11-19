// ─────────────────────────────────────────────────────────────
//  BACK COVER — VINYL CUT VERSION
//  Cut and applied as its own piece, separate from the front.
//  Same rules as cover_b_vinyl.typ: Futura, nothing under 1.2mm.
// ─────────────────────────────────────────────────────────────
#set page(width: 297mm, height: 210mm, margin: 0mm, fill: rgb("#141414"))

#let GOLD = rgb("#c9a227")

#box(width: 297mm, height: 210mm)[
  // Three bands, echoing the front's stack in miniature. All well
  // above the weeding floor.
  #let ys = (118mm, 128mm, 138mm)
  #let hs = (1.5mm, 3.0mm, 1.5mm)
  #for (y, h) in ys.zip(hs) {
    place(top + left, dx: 40mm, dy: y,
      rect(width: 40mm, height: h, fill: GOLD, stroke: none))
  }

  // Text shares the band group's left edge so the two read as one
  // stack. Measured at 17pt the stems were 1.14mm, just under the
  // floor; 20pt clears it at ~1.4mm.
  #place(top + left, dx: 40mm, dy: 152mm)[
    #set text(font: "Futura", fill: GOLD, weight: "bold", size: 20pt)
    #text(tracking: 2pt)[EX VULGATA]
  ]
]
