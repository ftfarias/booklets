// ─────────────────────────────────────────────────────────────
//  Plato — Three Socratic Dialogues
//  Euthyphro · Apology · Crito
//  Bilingual edition: Greek (Burnet / Perseus) + English (Jowett)
//  Public-domain sources · typeset for print
// ─────────────────────────────────────────────────────────────

#set document(
  title: "Plato — Euthyphro, Apology, Crito",
  author: "Plato",
)

// ── Page geometry (A4 book block, generous inner margin for binding) ──
#set page(
  width: 210mm,
  height: 297mm,
  margin: (inside: 30mm, outside: 25mm, top: 28mm, bottom: 28mm),
  numbering: none,
)

// ── Base typography ──
#set text(
  font: "Libertinus Serif",
  size: 12pt,
  lang: "en",
  hyphenate: true,
)
#set par(
  justify: true,
  leading: 0.72em,
  first-line-indent: 1.2em,
  spacing: 0.72em,
)

// ── Styling helpers (shared with body fragments) ──
#import "helpers.typ": *

// ── Work title page ──
#let worktitle(latin, greek, subtitle) = {
  pagebreak(to: "odd", weak: true)
  page(header: none, footer: none, numbering: none)[
    #v(1fr)
    #align(center)[
      #text(size: 26pt, weight: "bold")[#latin]
      #v(0.6em)
      #text(size: 15pt, fill: rgb("#555555"))[#greek]
      #v(1.2em)
      #line(length: 30%, stroke: 0.5pt + rgb("#999999"))
      #v(1.0em)
      #text(size: 11pt, style: "italic", fill: rgb("#555555"))[#subtitle]
    ]
    #v(2fr)
  ]
}

// ── Section divider (language part) ──
#let partpage(number, title, note) = {
  pagebreak(to: "odd", weak: true)
  page(header: none, footer: none, numbering: none)[
    #v(1fr)
    #align(center)[
      #text(size: 12pt, tracking: 3pt, fill: rgb("#888888"))[#number]
      #v(1.2em)
      #text(size: 30pt, weight: "bold")[#title]
      #v(1.4em)
      #line(length: 25%, stroke: 0.5pt + rgb("#999999"))
      #v(1.0em)
      #text(size: 11pt, style: "italic", fill: rgb("#555555"))[#note]
    ]
    #v(2fr)
  ]
}

// ═══════════════════════════════════════════════════════════════
//  COVER
// ═══════════════════════════════════════════════════════════════
#page(margin: (x: 20mm, y: 30mm))[
  #v(2fr)
  #align(center)[
    #text(size: 15pt, tracking: 5pt, fill: rgb("#666666"))[PLATO]
    #v(2.5em)
    #text(size: 34pt, weight: "bold")[Three Socratic \ Dialogues]
    #v(1.5em)
    #line(length: 40%, stroke: 0.6pt + rgb("#888888"))
    #v(1.5em)
    #text(size: 15pt, style: "italic", fill: rgb("#444444"))[
      Euthyphro · Apology · Crito
    ]
    #v(0.4em)
    #text(size: 13pt, fill: rgb("#666666"))[
      Εὐθύφρων · Ἀπολογία Σωκράτους · Κρίτων
    ]
  ]
  #v(3fr)
  #align(center)[
    #text(size: 10pt, fill: rgb("#777777"))[
      A bilingual edition — Greek & English
    ]
  ]
]

// ── Half-title / colophon (verso of cover) ──
#page[
  #v(1fr)
  #align(center)[
    #text(size: 9pt, fill: rgb("#666666"), style: "italic")[
      Greek text after the edition of John Burnet\
      (Oxford Classical Texts), via the Perseus Digital Library.
      #v(0.8em)
      English translation by Benjamin Jowett (1817–1893).
      #v(0.8em)
      All texts are in the public domain.
    ]
    #v(1.4em)
    #text(size: 9pt, fill: rgb("#888888"))[
      Prepared for private printing · #datetime.today().display("[year]")
    ]
  ]
  #v(1fr)
]

// ═══════════════════════════════════════════════════════════════
//  TABLE OF CONTENTS
// ═══════════════════════════════════════════════════════════════
#page[
  #v(1em)
  #text(size: 18pt, weight: "bold")[Contents]
  #v(1.5em)
  #set text(size: 10.5pt)
  #set par(first-line-indent: 0em, justify: false)

  #text(fill: rgb("#888888"), size: 9pt, tracking: 2pt)[PART ONE — GREEK]
  #v(0.4em)
  #grid(columns: (1fr), row-gutter: 0.5em,
    [Εὐθύφρων #box(width: 1fr, repeat[.]) #box[Euthyphro]],
    [Ἀπολογία Σωκράτους #box(width: 1fr, repeat[.]) #box[Apology]],
    [Κρίτων #box(width: 1fr, repeat[.]) #box[Crito]],
  )
  #v(1.4em)
  #text(fill: rgb("#888888"), size: 9pt, tracking: 2pt)[PART TWO — ENGLISH]
  #v(0.4em)
  #grid(columns: (1fr), row-gutter: 0.5em,
    [Euthyphro #box(width: 1fr, repeat[.]) #box[trans. Jowett]],
    [Apology #box(width: 1fr, repeat[.]) #box[trans. Jowett]],
    [Crito #box(width: 1fr, repeat[.]) #box[trans. Jowett]],
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
      #set text(size: 8pt, fill: rgb("#888888"), style: "italic")
      #grid(columns: (1fr, 1fr),
        align(left)[#h(0pt)],
        align(right)[Plato · Three Socratic Dialogues],
      )
      #v(-0.3em)
      #line(length: 100%, stroke: 0.3pt + rgb("#cccccc"))
    ]
  },
)
#counter(page).update(1)

// ─────────────── PART ONE: GREEK ───────────────
#partpage("PART ONE", "Ἑλληνιστί", "The Greek text")

#worktitle("Εὐθύφρων", "Euthyphro", "Text after Burnet")
#include "euthyphro_grc.typ"

#worktitle("Ἀπολογία Σωκράτους", "Apology of Socrates", "Text after Burnet")
#include "apology_grc.typ"

#worktitle("Κρίτων", "Crito", "Text after Burnet")
#include "crito_grc.typ"

// ─────────────── PART TWO: ENGLISH ───────────────
#partpage("PART TWO", "In English", "Translated by Benjamin Jowett")

#worktitle("Euthyphro", "Εὐθύφρων", "Translated by Benjamin Jowett")
#include "euthyphro_en.typ"

#worktitle("Apology", "Ἀπολογία Σωκράτους", "Translated by Benjamin Jowett")
#include "apology_en.typ"

#worktitle("Crito", "Κρίτων", "Translated by Benjamin Jowett")
#include "crito_en.typ"

// ─────────────── COLOPHON ───────────────
// The printer's signature, in its traditional place: after the text.
// Conventional impressum (type, paper, press, hand) — closing with the
// charge laid against Socrates, here laid against the book itself.

#pagebreak(to: "odd", weak: true)
#page(header: none, footer: none, numbering: none)[
  #v(1fr)
  #align(center)[
    #text(size: 10pt, tracking: 4pt, fill: rgb("#888888"))[COLOPHON]
    #v(2.2em)

    #block(width: 78%)[
      #set par(justify: false, first-line-indent: 0em, leading: 0.85em)
      #text(size: 9.5pt, fill: rgb("#444444"))[
        This edition of the three dialogues on the trial and death
        of Socrates was set in Libertinus Serif and printed on
        matte coated paper of 115 g/m² in an edition of one copy.
        #v(1.0em)
        The Greek follows the text of John Burnet; the English is the
        translation of Benjamin Jowett. Both have long since passed
        into the public domain, where Socrates would doubtless have
        preferred them.
        #v(1.0em)
        It was compiled, folded and bound by hand by
        Felipe de Toledo Farias, in the year #datetime.today().display("[year]").
      ]
    ]

    #v(2.2em)
    #line(length: 22%, stroke: 0.5pt + rgb("#bbbbbb"))
    #v(1.6em)

    // ── the charge ──
    #block(width: 72%)[
      #set par(justify: false, first-line-indent: 0em, leading: 0.9em)
      #text(size: 9.5pt, style: "italic", fill: rgb("#555555"))[
        This book is a compilation of texts which corrupts the youth
        and does not believe in the gods of the city.
        #v(0.7em)
        Read at your own risk.
      ]
    ]
  ]
  #v(1fr)
]

// ─────────────── DEDICATION + saddle-stitch padding ───────────────
// A clean recto page for a handwritten dedication, then blank leaves
// so the total page count is a multiple of 4 (required for saddle stitch).

// Dedication page (recto, no header/number)
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
//
// This is a fixed count, not a computed one. Deriving it from
// counter(page).final() is self-referential — the padding changes the very
// total it is measured from — and Typst reports that it does not converge.
// Set BLANKS to whatever closes the gap; `make check-pages` verifies it.
#let BLANKS = 5
#for _ in range(BLANKS) {
  page(header: none, footer: none, numbering: none)[]
}
