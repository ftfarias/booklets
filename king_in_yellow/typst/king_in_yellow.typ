// ─────────────────────────────────────────────────────────────
//  Robert W. Chambers — The King in Yellow
//  The four weird tales · 1895
//  The Repairer of Reputations · The Mask ·
//  In the Court of the Dragon · The Yellow Sign
//  Public-domain source (Project Gutenberg #8492) · typeset for print
// ─────────────────────────────────────────────────────────────

#set document(
  title: "The King in Yellow — The Four Weird Tales",
  author: "Robert W. Chambers",
)

// ── Page geometry (A5 leaf, saddle stitch: inner margin alternates) ──
#set page(
  width: 148mm,
  height: 210mm,
  margin: (inside: 20mm, outside: 15mm, top: 18mm, bottom: 18mm),
  numbering: none,
)

// ── Base typography ──
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

// ── Story title page ──
#let storytitle(number, title) = {
  pagebreak(to: "odd", weak: true)
  page(header: none, footer: none, numbering: none)[
    #v(1fr)
    #align(center)[
      #text(size: 10pt, tracking: 4pt, fill: rgb("#999999"))[#number]
      #v(1.4em)
      #text(size: 22pt, weight: "bold")[#title]
      #v(1.2em)
      #line(length: 22%, stroke: 0.5pt + rgb("#aaaaaa"))
    ]
    #v(2fr)
  ]
}

// ═══════════════════════════════════════════════════════════════
//  COVER
// ═══════════════════════════════════════════════════════════════
#page(margin: (x: 18mm, y: 26mm))[
  #v(2fr)
  #align(center)[
    #text(size: 12pt, tracking: 5pt, fill: rgb("#666666"))[
      ROBERT W. CHAMBERS
    ]
    #v(2.4em)
    #text(size: 30pt, weight: "bold")[The King #linebreak() in Yellow]
    #v(1.4em)
    #line(length: 36%, stroke: 0.6pt + rgb("#888888"))
    #v(1.4em)
    #text(size: 12pt, style: "italic", fill: rgb("#444444"))[
      The Four Weird Tales
    ]
  ]
  #v(3fr)
  #align(center)[
    #text(size: 9pt, fill: rgb("#777777"))[
      Have you found the Yellow Sign?
    ]
  ]
]

// ── Verso of cover: source statement ──
#page[
  #v(1fr)
  #align(center)[
    #set par(justify: false, first-line-indent: 0em, leading: 0.8em)
    #text(size: 9pt, fill: rgb("#666666"), style: "italic")[
      The text follows the first edition of 1895,\
      after the Project Gutenberg transcription (\#8492).
      #v(0.8em)
      Robert William Chambers died in 1933;\
      the work is in the public domain.
    ]
    #v(1.4em)
    #text(size: 9pt, fill: rgb("#888888"))[
      Prepared for private printing · #datetime.today().display("[year]")
    ]
  ]
  #v(1fr)
]

// ═══════════════════════════════════════════════════════════════
//  FRONTISPIECE — reserved leaf
//  "The Pallid Mask". Printed separately on photo paper, varnished,
//  and tipped in by hand along the inner margin.
// ═══════════════════════════════════════════════════════════════
#page(header: none, footer: none, numbering: none)[
  #plate(caption: [The Pallid Mask])
]

// ═══════════════════════════════════════════════════════════════
//  EPIGRAPH — Cassilda's Song
//  The fragment of the play that frames all four tales.
// ═══════════════════════════════════════════════════════════════
#page(header: none, footer: none, numbering: none)[
  #v(1fr)
  #include "song.typ"
  #v(2fr)
]

// ═══════════════════════════════════════════════════════════════
//  EDITORIAL NOTE
// ═══════════════════════════════════════════════════════════════
#page(header: none, footer: none, numbering: none)[
  #v(1.2em)
  #align(center)[
    #text(size: 10pt, tracking: 4pt, fill: rgb("#888888"))[A NOTE ON THIS EDITION]
  ]
  #v(2.0em)
  #set par(justify: true, first-line-indent: 0em, leading: 0.75em, spacing: 0.9em)
  #set text(size: 9.5pt, fill: rgb("#333333"))

  #emph[The King in Yellow] was published in 1895 as a collection of ten
  pieces. It is not a coherent book. The first four stories are weird
  fiction of the first order; the remaining six are sentimental tales of
  art students in Paris, and have nothing to do with Carcosa. This edition
  prints the four, and lets the others stay where they are.

  What binds them is a play — also called #emph[The King in Yellow] — which
  drives its readers mad. Chambers never quotes more than fragments of it:
  a song, a line of dialogue, the name of a mask. The horror is built out
  of what is withheld, and the withholding is the method. Readers waiting
  for the play to be explained will wait past the last page.

  Note that the first story is set in an America of 1920, imagined from
  1895, with state suicide chambers and a government of unpleasant
  efficiency. This is the setting, not a symptom. Whether anything else in
  that story can be believed is a separate question, and the better one.

  Chambers was read by H. P. Lovecraft, who took the method and little
  else; Hastur, Carcosa and the Yellow Sign entered other hands from here.
  The names were themselves borrowed — Chambers took Carcosa and Hali from
  Ambrose Bierce, who had used them for something quite different.
]

// ═══════════════════════════════════════════════════════════════
//  Running headers + page numbers begin here
// ═══════════════════════════════════════════════════════════════
#set page(
  numbering: "1",
  header: context {
    let page-num = counter(page).get().first()
    if page-num > 1 [
      #set text(size: 8pt, fill: rgb("#888888"), style: "italic")
      #grid(columns: (1fr, 1fr),
        align(left)[#h(0pt)],
        align(right)[Chambers · The King in Yellow],
      )
      #v(-0.3em)
      #line(length: 100%, stroke: 0.3pt + rgb("#cccccc"))
    ]
  },
)
#counter(page).update(1)

// ─────────────── THE FOUR TALES ───────────────
#storytitle("I", [The Repairer #linebreak() of Reputations])
#include "repairer.typ"

#storytitle("II", [The Mask])
#include "mask.typ"

#storytitle("III", [In the Court #linebreak() of the Dragon])
#include "dragon.typ"

#storytitle("IV", [The Yellow Sign])
#include "yellow_sign.typ"

// ─────────────── PLATE — reserved leaf ───────────────
// "Carcosa". The lake, the twin suns, and the moon standing in front
// of the towers rather than behind them.
#pagebreak(to: "odd", weak: true)
#page(header: none, footer: none, numbering: none)[
  #plate(caption: [Carcosa])
]

// ─────────────── COLOPHON ───────────────
#pagebreak(to: "odd", weak: true)
#page(header: none, footer: none, numbering: none)[
  #v(1fr)
  #align(center)[
    #text(size: 10pt, tracking: 4pt, fill: rgb("#888888"))[COLOPHON]
    #v(2.2em)

    #block(width: 78%)[
      #set par(justify: false, first-line-indent: 0em, leading: 0.85em)
      #text(size: 9.5pt, fill: rgb("#444444"))[
        This edition of the four weird tales from
        #emph[The King in Yellow] was set in Libertinus Serif
        and printed on Pólen Bold of 90~g/m² in an edition of one copy.
        #v(1.0em)
        The text is that of the first edition of 1895, which has been
        in the public domain for many years — a condition the play
        described in these pages has never been permitted to enjoy.
        #v(1.0em)
        It was compiled, folded, sewn and bound by hand by
        Felipe de Toledo Farias, in the year
        #datetime.today().display("[year]").
      ]
    ]

    #v(2.2em)
    #line(length: 22%, stroke: 0.5pt + rgb("#bbbbbb"))
    #v(1.6em)

    // ── the mote ──
    #block(width: 72%)[
      #set par(justify: false, first-line-indent: 0em, leading: 0.9em)
      #text(size: 9.5pt, style: "italic", fill: rgb("#555555"))[
        Ne raillez pas les fous; leur folie dure plus longtemps
        que la nôtre… Voilà toute la différence.
        #v(0.7em)
        #text(size: 8.5pt, fill: rgb("#777777"))[
          Mock not the mad; their folly lasts longer than ours —\
          that is the whole of the difference.
        ]
      ]
    ]
  ]
  #v(1fr)
]

// ─────────────── DEDICATION + saddle-stitch padding ───────────────
#pagebreak(to: "odd", weak: true)
#page(header: none, footer: none, numbering: none)[
  #v(1fr)
  #align(center)[
    #text(size: 11pt, tracking: 3pt, style: "italic", fill: rgb("#999999"))[
      Dedicatória
    ]
  ]
  #v(2fr)
]

// Pad with blank leaves so the total is a multiple of 4 (saddle stitch).
// Fixed count, not computed: counter(page).final() is self-referential
// and Typst reports that it does not converge. `make check` verifies it.
#let BLANKS = 5
#for _ in range(BLANKS) {
  page(header: none, footer: none, numbering: none)[]
}
