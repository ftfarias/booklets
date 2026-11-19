// Colophon, A5, to be printed on laid (verge) paper as the rear flyleaf —
// the same treatment as the Plato volume. NOT part of the body PDF.
//   typst compile --input vol=1 cover/colophon_a5.typ cover/colofon_vol1_A5.pdf

#let vol = int(sys.inputs.at("vol", default: "1"))

#set page(width: 148mm, height: 210mm, margin: (x: 22mm, y: 26mm), numbering: none)
#set text(font: "Libertinus Serif", size: 9.5pt, lang: "en")
#set par(justify: false, first-line-indent: 0em, leading: 0.9em)

#let body = if vol == 1 {
  [This first volume of the Stoics was set in Libertinus Serif and printed,
   folded and bound by hand by Felipe de Toledo Farias, sewn Japanese-style
   through four stab holes, in the year #datetime.today().display("[year]").

   The Enchiridion is given in the translation of Thomas Wentworth Higginson
   (1865); the Discourses, in that of George Long (1877). Epictetus himself
   wrote nothing — all that survives was taken down by his pupil Arrian, who
   feared the words would otherwise be lost.]
} else {
  [This second volume of the Stoics was set in Libertinus Serif and printed,
   folded and bound by hand by Felipe de Toledo Farias, sewn Japanese-style
   through four stab holes, in the year #datetime.today().display("[year]").

   The text is the translation of George Long, made in 1862 and long since in
   the public domain. Its author intended no reader at all, and would have been
   astonished to find himself in print; he had asked only to be rid of the
   desire to be remembered.]
}

#let motto = if vol == 1 {
  ("Pro captu lectoris habent sua fata libelli.",
   "According to the capacity of the reader, books have their own destinies.")
} else {
  ("Ὅσον οὔπω πάντες οὐδέν.", "A little while, and all of us are nobody.")
}

#v(1fr)
#align(center)[
  #text(size: 9pt, tracking: 4pt, fill: rgb("#888888"))[COLOPHON]
  #v(2.4em)
  #block(width: 86%)[
    #text(fill: rgb("#333333"))[#body]
  ]
  #v(2.4em)
  #line(length: 22%, stroke: 0.5pt + rgb("#bbbbbb"))
  #v(1.8em)
  #block(width: 78%)[
    #text(size: 9.5pt, style: "italic", fill: rgb("#555555"))[#motto.at(0)]
    #v(0.6em)
    #text(size: 8.5pt, fill: rgb("#777777"))[#motto.at(1)]
  ]
]
#v(1fr)
