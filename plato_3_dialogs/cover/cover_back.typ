// BACK COVER — HTV cut file (gold on leather)
// Restrained: a single small emblem line. "Know thyself" — the Delphic maxim
// invoked by Socrates. Centered low, classic placement.

#set page(width: 216mm, height: 303mm, margin: 0pt, fill: none)
#let gold = rgb("#c8a24a")

// small centred rule
#place(center + horizon, dy: -6mm)[
  #line(length: 24mm, stroke: 0.6mm + gold)
]

#place(center + horizon, dy: 6mm)[
  #text(font: "Libertinus Serif", style: "italic", size: 20pt, tracking: 2pt, fill: gold)[
    γνῶθι σεαυτόν
  ]
]

#place(center + horizon, dy: 18mm)[
  #text(font: "Libertinus Serif", size: 10pt, tracking: 2pt, fill: gold)[
    know thyself
  ]
]
