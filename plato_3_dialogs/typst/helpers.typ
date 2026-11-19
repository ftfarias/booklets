// Shared styling helpers for the dialogue body fragments.

// Speaker label (bold)
#let sp(name) = box(text(weight: "bold", size: 9.5pt)[#name])

// Stephanus reference number — small, raised, muted
#let steph(n) = box(
  text(size: 7pt, fill: rgb("#888888"), style: "italic")[#n],
)

// "Persons of the dialogue" line
#let persons(t) = block(
  above: 0.4em, below: 1.0em,
  text(style: "italic", size: 10pt)[#t],
)
#let scene(t) = block(
  above: 0em, below: 1.4em,
  text(style: "italic", size: 10pt)[#t],
)
