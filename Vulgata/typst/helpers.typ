// Shared styling helpers for the Vulgata bilingual volume.
// Body fragments must `#import "helpers.typ": *` — Typst #include
// does NOT share the parent's local let-scope.

#let LATCOL = rgb("#1a1a1a")
#let PTCOL  = rgb("#2e2e2e")
#let MUTED  = rgb("#9a9a9a")
#let RULE   = rgb("#c8c8c8")

// Chapter number — centred, with a hairline rule across both columns.
#let chapnum(n) = block(above: 1.9em, below: 1.1em, width: 100%)[
  #align(center)[
    #text(size: 9pt, tracking: 3pt, fill: MUTED)[CAPUT #n]
    #v(0.35em)
    #line(length: 22%, stroke: 0.4pt + RULE)
  ]
]

// One verse row: Latin | number | Portuguese.
// The verse number sits in a narrow centre gutter so both columns
// stay flush and the eye can hop between them. `block(breakable: false)`
// keeps a verse from splitting across a page, which would break the
// pairing; each row re-syncs the two columns at its own top edge, so
// they cannot drift apart down the page.
#let v_(n, lat, pt) = block(below: 0.6em, width: 100%, breakable: false)[
  #grid(
    columns: (1fr, 11mm, 1fr),
    align: (top, top + center, top),
    text(fill: LATCOL)[#lat],
    text(size: 8.5pt, fill: MUTED)[#v(0.2em) #n],
    text(fill: PTCOL, lang: "pt")[#pt],
  )
]

// Work title page.
#let worktitle(latin, pt, epi_lat, epi_pt) = {
  pagebreak(to: "odd", weak: true)
  page(header: none, footer: none, numbering: none)[
    #v(1fr)
    #align(center)[
      #text(size: 24pt, weight: "bold")[#latin]
      #v(0.5em)
      #text(size: 13pt, fill: rgb("#555555"))[#pt]
      #v(1.4em)
      #line(length: 28%, stroke: 0.5pt + RULE)
      #v(1.4em)
      #block(width: 74%)[
        #set par(justify: false, leading: 0.8em)
        #text(size: 11pt, style: "italic", fill: rgb("#333333"))[#epi_lat]
        #v(0.55em)
        #text(size: 9.5pt, fill: rgb("#666666"))[#epi_pt]
      ]
    ]
    #v(2fr)
  ]
}

// Running column labels, printed once under a work title.
#let collabels() = block(below: 1.2em, width: 100%)[
  #grid(
    columns: (1fr, 11mm, 1fr),
    align: (center, center, center),
    text(size: 7.5pt, tracking: 2pt, fill: MUTED)[VULGATA],
    [],
    text(size: 7.5pt, tracking: 2pt, fill: MUTED)[ALMEIDA],
  )
  #v(0.4em)
  #line(length: 100%, stroke: 0.4pt + RULE)
]
