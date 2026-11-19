// SPINE — HTV cut file (gold on leather)
// Sized for a saddle-stitched A4 book of 100 pages ≈ 8–12 mm thick.
// Width here is generous (20mm) so you can trim/position; text runs vertically.
// Standard convention: spine text reads top-to-bottom (rotate head to the RIGHT).

#set page(width: 20mm, height: 303mm, margin: 0pt, fill: none)
#let gold = rgb("#c8a24a")

#place(center + horizon)[
  #rotate(90deg, reflow: false)[
    #box[
      #text(font: "Libertinus Serif", weight: "bold", size: 22pt, tracking: 6pt, fill: gold)[ΠΛΑΤΩΝ]
      #h(10mm)
      #text(font: "Libertinus Serif", size: 13pt, tracking: 3pt, fill: gold)[Socratic Dialogues]
    ]
  ]
]
