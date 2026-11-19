// ─────────────────────────────────────────────────────────────
//  EPICTETUS — The Enchiridion, with Discourses
//  Ἐγχειρίδιον · Διατριβαί
//  Enchiridion trans. Thomas Wentworth Higginson (1865)
//  Discourses trans. George Long (1877), selection
//  Public-domain sources · typeset for print · A5
// ─────────────────────────────────────────────────────────────

#set document(
  title: "Epictetus — The Enchiridion, with Discourses",
  author: "Epictetus",
)

// ── Page geometry (A5 book block, generous inner margin for binding) ──
#set page(
  width: 148mm,
  height: 210mm,
  margin: (inside: 20mm, outside: 15mm, top: 18mm, bottom: 18mm),
  numbering: none,
)

#set text(
  font: "Libertinus Serif",
  size: 10.5pt,
  lang: "en",
  hyphenate: true,
)
#set par(
  justify: true,
  leading: 0.68em,
  first-line-indent: 1.2em,
  spacing: 0.68em,
)

#import "helpers.typ": *

#let worktitle(greek, latin, subtitle) = {
  pagebreak(to: "odd", weak: true)
  page(header: none, footer: none, numbering: none)[
    #v(1fr)
    #align(center)[
      #text(size: 22pt, weight: "bold")[#greek]
      #v(0.6em)
      #text(size: 14pt, fill: rgb("#555555"))[#latin]
      #v(1.2em)
      #line(length: 30%, stroke: 0.5pt + rgb("#999999"))
      #v(1.0em)
      #text(size: 10pt, style: "italic", fill: rgb("#555555"))[#subtitle]
    ]
    #v(2fr)
  ]
}

// ═══════════════════════════════════════════════════════════════
//  COVER
// ═══════════════════════════════════════════════════════════════
#page(margin: (x: 16mm, y: 24mm))[
  #v(2fr)
  #align(center)[
    #text(size: 13pt, tracking: 5pt, fill: rgb("#666666"))[EPICTETUS]
    #v(2.5em)
    #text(size: 28pt, weight: "bold")[The Enchiridion]
    #v(0.8em)
    #text(size: 13pt, fill: rgb("#666666"))[Ἐγχειρίδιον]
    #v(1.5em)
    #line(length: 40%, stroke: 0.6pt + rgb("#888888"))
    #v(1.5em)
    #text(size: 13pt, style: "italic", fill: rgb("#444444"))[
      with a selection from the Discourses
    ]
    #v(0.4em)
    #text(size: 11pt, fill: rgb("#666666"))[Διατριβαί]
  ]
  #v(3fr)
  #align(center)[
    #text(size: 9pt, fill: rgb("#777777"))[
      Volume One of the Stoics
    ]
  ]
]

// ── Copyright / sources page (verso) ──
#page[
  #v(1fr)
  #align(center)[
    #text(size: 8.5pt, fill: rgb("#666666"), style: "italic")[
      The Enchiridion in the translation of\
      Thomas Wentworth Higginson (1823–1911), first published 1865.
      #v(0.8em)
      The Discourses, as recorded by Arrian, in the translation of\
      George Long (1800–1879); this is a selection.
      #v(0.8em)
      All texts are in the public domain.
    ]
    #v(1.4em)
    #text(size: 8.5pt, fill: rgb("#888888"))[
      Prepared for private printing · #datetime.today().display("[year]")
    ]
  ]
  #v(1fr)
]

// ═══════════════════════════════════════════════════════════════
//  EPIGRAPH
// ═══════════════════════════════════════════════════════════════
#page(header: none, footer: none, numbering: none)[
  #v(1fr)
  #align(center)[
    #epigraph(
      "τῶν ὄντων τὰ μέν ἐστιν ἐφ' ἡμῖν, τὰ δὲ οὐκ ἐφ' ἡμῖν.",
      "Of things, some are within our power, and some are not.",
      "ENCHIRIDION I",
    )
  ]
  #v(2fr)
]

// ═══════════════════════════════════════════════════════════════
//  TABLE OF CONTENTS
// ═══════════════════════════════════════════════════════════════
#page[
  #v(1em)
  #text(size: 16pt, weight: "bold")[Contents]
  #v(1.5em)
  #set text(size: 10pt)
  #set par(first-line-indent: 0em, justify: false)

  #grid(columns: (1fr), row-gutter: 0.7em,
    [Epictetus #box(width: 1fr, repeat[.]) #box[a life]],
    [The Enchiridion #box(width: 1fr, repeat[.]) #box[Ἐγχειρίδιον]],
    [From the Discourses #box(width: 1fr, repeat[.]) #box[Διατριβαί]],
  )
]

// ═══════════════════════════════════════════════════════════════
//  Running headers + page numbers begin here
// ═══════════════════════════════════════════════════════════════
#set page(
  numbering: "1",
  header: context {
    let page-num = counter(page).get().first()
    if page-num > 1 [
      #set text(size: 7.5pt, fill: rgb("#888888"), style: "italic")
      #grid(columns: (1fr, 1fr),
        align(left)[#h(0pt)],
        align(right)[Epictetus],
      )
      #v(-0.3em)
      #line(length: 100%, stroke: 0.3pt + rgb("#cccccc"))
    ]
  },
)
#counter(page).update(1)

#include "life.typ"

#worktitle("Ἐγχειρίδιον", "The Enchiridion", "Translated by Thomas Wentworth Higginson")
#include "enchiridion.typ"

#worktitle("Διατριβαί", "From the Discourses", "Recorded by Arrian · translated by George Long")
#include "discourses.typ"

// ─────────────── COLOPHON ───────────────
#pagebreak(to: "odd", weak: true)
#page(header: none, footer: none, numbering: none)[
  #v(1fr)
  #align(center)[
    #text(size: 9pt, tracking: 4pt, fill: rgb("#888888"))[COLOPHON]
    #v(2.2em)

    #block(width: 80%)[
      #set par(justify: false, first-line-indent: 0em, leading: 0.85em)
      #text(size: 9pt, fill: rgb("#444444"))[
        This first volume of the Stoics was set in Libertinus Serif
        and printed, folded and bound by hand by
        Felipe de Toledo Farias, in the year
        #datetime.today().display("[year]").
        #v(1.0em)
        The Enchiridion is given in the translation of Thomas Wentworth
        Higginson; the Discourses, in that of George Long. Epictetus
        himself wrote nothing: all that survives was taken down by his
        pupil Arrian, who feared the words would otherwise be lost.
      ]
    ]

    #v(2.2em)
    #line(length: 22%, stroke: 0.5pt + rgb("#bbbbbb"))
    #v(1.6em)

    #block(width: 74%)[
      #set par(justify: false, first-line-indent: 0em, leading: 0.9em)
      #text(size: 9pt, style: "italic", fill: rgb("#555555"))[
        Pro captu lectoris habent sua fata libelli.
        #v(0.7em)
        #text(size: 8.5pt, fill: rgb("#777777"))[
          According to the capacity of the reader,\
          books have their own destinies.
        ]
      ]
    ]
  ]
  #v(1fr)
]

// ─────────────── DEDICATION ───────────────
#pagebreak(to: "odd", weak: true)
#page(header: none, footer: none, numbering: none)[
  #v(1fr)
  #align(center)[
    #text(size: 10pt, tracking: 3pt, style: "italic", fill: rgb("#999999"))[
      Dedicatória
    ]
  ]
  #v(2fr)
]

// Pad with blank leaves so the total is a multiple of 4.
// Fixed count, not computed — see the Plato master for why.
#let BLANKS = 3
#for _ in range(BLANKS) {
  page(header: none, footer: none, numbering: none)[]
}
