// Shared styling helpers for the Stoics volumes.
// Mirrors plato_3_dialogs/typst/helpers.typ; body fragments must
// `#import "helpers.typ": *` — Typst #include does NOT share parent let-scope.

// Greek technical term, inline, in the original polytonic script.
#let grk(t) = box(text(font: "Libertinus Serif", fill: rgb("#333333"))[#t])

// Enchiridion section number — small, muted, hanging in the margin.
#let sec(n) = box(
  text(size: 8pt, fill: rgb("#999999"), style: "italic")[#n],
)

// Chapter title inside a work
#let chap(title) = block(above: 1.6em, below: 0.9em)[
  #set par(first-line-indent: 0em)
  #text(size: 11pt, weight: "bold")[#title]
]

// An epigraph in Greek + English, used on part/title pages.
#let epigraph(greek, english, source) = block(width: 78%)[
  #set par(justify: false, first-line-indent: 0em, leading: 0.85em)
  #align(center)[
    #text(size: 10.5pt, fill: rgb("#444444"))[#greek]
    #v(0.7em)
    #text(size: 9.5pt, style: "italic", fill: rgb("#666666"))[#english]
    #v(0.6em)
    #text(size: 8pt, fill: rgb("#999999"), tracking: 1pt)[#source]
  ]
]

// Editorial footnote marker + note text
#let note(t) = footnote(text(size: 8pt)[#t])

// Book heading inside the Meditations (Ι–ΧΙΙ)
#let bookhead(n) = {
  pagebreak(to: "odd", weak: true)
  block(above: 0em, below: 1.4em)[
    #set par(first-line-indent: 0em)
    #align(center)[
      #text(size: 9pt, tracking: 3pt, fill: rgb("#999999"))[BOOK]
      #v(0.3em)
      #text(size: 20pt, weight: "bold")[#n]
    ]
  ]
}
