// ─────────────────────────────────────────────────────────────
//  COVER B — "Bandes d'or"
//  After Legrain's banded bindings: the cross implied by the
//  interruption of parallel rules, not drawn. Nothing is centred.
// ─────────────────────────────────────────────────────────────
#set page(width: 210mm, height: 148mm, margin: 0mm, fill: rgb("#0b0b0b"))

#let GOLD   = rgb("#c9a227")
#let GOLD_D = rgb("#8f7320")

#box(width: 210mm, height: 148mm)[
  // ── Seven horizontal gold bands, unequal weights ──
  // Bands crowd toward the centre bar and thin out away from it, so the
  // stack reads as one object rather than a ruled grid.
  #let ys = (34mm, 45mm, 54mm, 61mm, 68mm, 77mm, 88mm)
  #let ws = (0.5pt, 0.8pt, 1.4pt, 2.6pt, 1.4pt, 0.8pt, 0.5pt)
  #for (y, w) in ys.zip(ws) {
    // left run, stopping short of the vertical
    place(top + left, dx: 30mm, dy: y,
      line(length: 38mm, stroke: w + GOLD_D))
    // right run, resuming past it — the gap draws the cross
    place(top + left, dx: 76mm, dy: y,
      line(length: 19mm, stroke: w + GOLD_D))
  }

  // ── The single vertical: solid gold, the only filled shape ──
  #place(top + left, dx: 70mm, dy: 22mm,
    rect(width: 3mm, height: 78mm, fill: GOLD, stroke: none))

  // ── Title, far right, aligned to the band stack ──
  #place(top + left, dx: 118mm, dy: 46mm)[
    #set text(font: "Libertinus Serif", fill: GOLD)
    #text(size: 34pt, weight: "bold")[Vanitas]
    #v(4mm)
    #set text(size: 8pt, fill: rgb("#a98f4a"))
    #text(tracking: 3pt)[EX VULGATA]
  ]

  #place(bottom + left, dx: 118mm, dy: -32mm)[
    #set text(font: "Libertinus Serif", size: 7.5pt,
              fill: rgb("#806c33"), style: "italic")
    Ecclesiastes
    #linebreak()
    Canticum Canticorum
    #linebreak()
    Ad Corinthios I, xiii
  ]
]
