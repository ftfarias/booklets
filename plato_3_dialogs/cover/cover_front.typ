// FRONT COVER — HTV cut file (gold on leather)
// True size, designed to sit on an A4 hardcover board (~216 x 303 mm).
// Everything is vector; Typst outlines glyphs to paths on SVG export.
// Background is transparent — only the GOLD elements are cut from HTV.

#set page(width: 216mm, height: 303mm, margin: 0pt, fill: none)

#let gold = rgb("#c8a24a")

#place(center + horizon, dy: -55mm)[
  #image("owl.svg", width: 42mm)
]

// Thin rule above the name
#place(center + horizon, dy: -8mm)[
  #line(length: 70mm, stroke: 0.8mm + gold)
]

#place(center + horizon, dy: 6mm)[
  #text(font: "Copperplate", weight: "bold", size: 54pt, tracking: 14pt, fill: gold)[PLATO]
]

// Thin rule below the name
#place(center + horizon, dy: 22mm)[
  #line(length: 70mm, stroke: 0.8mm + gold)
]

// Subtitle in Greek
#place(center + horizon, dy: 34mm)[
  #text(font: "Libertinus Serif", size: 15pt, tracking: 3pt, fill: gold)[
    ΕΥΘΥΦΡΩΝ · ΑΠΟΛΟΓΙΑ · ΚΡΙΤΩΝ
  ]
]
