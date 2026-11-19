// ─────────────────────────────────────────────────────────────
//  MARCUS AURELIUS — The Meditations
//  Τὰ εἰς ἑαυτόν
//  Translated by George Long (1862), complete in twelve books
//  Public-domain source · typeset for print · A5
// ─────────────────────────────────────────────────────────────

#set document(
  title: "Marcus Aurelius — The Meditations",
  author: "Marcus Aurelius",
)

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

// ═══════════════════════════════════════════════════════════════
//  COVER
// ═══════════════════════════════════════════════════════════════
#page(margin: (x: 16mm, y: 24mm))[
  #v(2fr)
  #align(center)[
    #text(size: 13pt, tracking: 5pt, fill: rgb("#666666"))[MARCUS AURELIUS]
    #v(2.5em)
    #text(size: 28pt, weight: "bold")[The Meditations]
    #v(0.8em)
    #text(size: 13pt, fill: rgb("#666666"))[Τὰ εἰς ἑαυτόν]
    #v(1.5em)
    #line(length: 40%, stroke: 0.6pt + rgb("#888888"))
    #v(1.5em)
    #text(size: 13pt, style: "italic", fill: rgb("#444444"))[
      in twelve books
    ]
  ]
  #v(3fr)
  #align(center)[
    #text(size: 9pt, fill: rgb("#777777"))[
      Volume Two of the Stoics
    ]
  ]
]

// ── Sources page (verso) ──
#page[
  #v(1fr)
  #align(center)[
    #text(size: 8.5pt, fill: rgb("#666666"), style: "italic")[
      In the translation of George Long (1800–1879),\
      first published in 1862 as
      #v(0.3em)
      The Thoughts of the Emperor Marcus Aurelius Antoninus.
      #v(0.8em)
      The translator's own notes and index have been omitted;\
      his text is given unaltered.
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
      "ὁ βίος βραχύς· ὁ δὲ καρπὸς τοῦ βίου, ὁσία διάθεσις καὶ πράξεις κοινωνικαί.",
      "Short is life; and the fruit of life is a holy disposition and acts for the common good.",
      "MEDITATIONS VI, 30",
    )
  ]
  #v(2fr)
]

// ═══════════════════════════════════════════════════════════════
//  A NOTE ON THE BOOK
// ═══════════════════════════════════════════════════════════════
#page[
  #v(1em)
  #align(center)[
    #text(size: 15pt, weight: "bold")[A Note on this Book]
  ]
  #v(1.6em)
  #set text(size: 10pt)
  #block(width: 100%)[
    Marcus Aurelius Antoninus, emperor of Rome from 161 to 180, wrote these
    twelve books for no reader but himself. They were composed in Greek,
    much of it on campaign — the first book closes on the river Granua among
    the Quadi, the second at Carnuntum — by a man who commanded armies in the
    day and, at night, reminded himself that power is nothing and that he
    would shortly be dead.

    He gave the work no title. The name by which the Greeks knew it,
    #grk[Τὰ εἰς ἑαυτόν], means simply #emph[to himself]; the familiar English
    title is a later convenience. Nothing in it was written to persuade,
    and this is the source of its peculiar authority: we are reading a man's
    private correspondence with his own resolve, and finding our own
    difficulties already there.

    Epictetus, whose Discourses fill the companion volume, was born a slave
    and lame. Marcus read him closely and cites him by name. That the same
    philosophy served the man who owned nothing and the man who owned the
    world is the strongest argument either of them makes.
  ]
]

// ═══════════════════════════════════════════════════════════════
//  Running headers + page numbers
// ═══════════════════════════════════════════════════════════════
#set page(
  numbering: "1",
  header: context {
    let page-num = counter(page).get().first()
    if page-num > 1 [
      #set text(size: 7.5pt, fill: rgb("#888888"), style: "italic")
      #grid(columns: (1fr, 1fr),
        align(left)[#h(0pt)],
        align(right)[Marcus Aurelius · The Meditations],
      )
      #v(-0.3em)
      #line(length: 100%, stroke: 0.3pt + rgb("#cccccc"))
    ]
  },
)
#counter(page).update(1)

#include "meditations.typ"

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
        This second volume of the Stoics was set in Libertinus Serif
        and printed, folded and bound by hand by
        Felipe de Toledo Farias, in the year
        #datetime.today().display("[year]").
        #v(1.0em)
        The text is the translation of George Long, made in 1862 and
        long since in the public domain. Its author intended no reader
        at all, and would have been astonished to find himself in print;
        he had asked only to be rid of the desire to be remembered.
      ]
    ]

    #v(2.2em)
    #line(length: 22%, stroke: 0.5pt + rgb("#bbbbbb"))
    #v(1.6em)

    #block(width: 74%)[
      #set par(justify: false, first-line-indent: 0em, leading: 0.9em)
      #text(size: 9pt, style: "italic", fill: rgb("#555555"))[
        Ὅσον οὔπω πάντες οὐδέν.
        #v(0.5em)
        #text(size: 8.5pt, fill: rgb("#777777"))[
          A little while, and all of us are nobody.
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

#let BLANKS = 3
#for _ in range(BLANKS) {
  page(header: none, footer: none, numbering: none)[]
}
