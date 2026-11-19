// TITLE — BLACK HTV on the ochre band of the A5 leather cover.
//
// This file is the full cover size (151 x 216 mm) with the title already
// positioned, so the cut file registers directly against the assembled
// cover: align the sheet to the cover edges and the title lands correctly.
// y = 92 mm clears the rock line below and the temples above.

#set page(width: 151mm, height: 216mm, margin: 0pt, fill: none)
#let ink = rgb("#111111")

#place(top + center, dy: 92mm)[
  #align(center)[
    #text(font: "Copperplate", weight: "bold", size: 30pt, tracking: 10pt, fill: ink)[PLATO]
    #v(2mm)
    #text(font: "Libertinus Serif", size: 9pt, tracking: 2.5pt, fill: ink)[
      ΕΥΘΥΦΡΩΝ · ΑΠΟΛΟΓΙΑ · ΚΡΙΤΩΝ
    ]
  ]
]
