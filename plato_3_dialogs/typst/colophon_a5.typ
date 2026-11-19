// COLOPHON — single A5 leaf, to be printed at home on laid (vergé) paper
// and bound in with the text block.
//
// Printed on an Epson EcoTank L4360: set to BLACK ONLY. The L4360's colour
// inks are dye-based and feather on uncoated laid paper; its black is
// pigment and holds a crisp edge. Everything here is therefore greyscale.
//
// Left margin is 20 mm to match the printed text block, so the yotsume-toji
// stab holes (10 mm from the edge) fall in the same place on every leaf.

#set page(
  width: 148mm,
  height: 210mm,
  margin: (left: 20mm, right: 16mm, top: 20mm, bottom: 20mm),
)

#set text(font: "Libertinus Serif", size: 10pt, lang: "en")
#set par(justify: false, first-line-indent: 0em, leading: 0.85em)

#v(1fr)

#align(center)[
  #text(size: 10pt, tracking: 4pt, fill: luma(40%))[COLOPHON]
  #v(2.4em)

  #block(width: 80%)[
    #text(size: 9.5pt)[
      This edition of the three dialogues on the trial and death of
      Socrates was set in Libertinus Serif and printed on matte coated
      paper of 115~g/m² in an edition of one copy.
      #v(1.1em)
      The Greek follows the text of John Burnet; the English is the
      translation of Benjamin Jowett. Both have long since passed into
      the public domain, where Socrates would doubtless have preferred
      them.
      #v(1.1em)
      This leaf was printed separately on laid paper. The book was
      compiled, sewn and bound by hand — in the Japanese manner, with
      four stab holes — by Felipe de Toledo Farias,
      in~the~year~#datetime.today().display("[year]").
    ]
  ]

  #v(2.4em)
  #line(length: 24%, stroke: 0.5pt + luma(70%))
  #v(1.8em)

  // ── the charge ──
  #block(width: 78%)[
    #text(size: 9.5pt, style: "italic")[
      This book is a compilation of texts which corrupts the youth
      and does not believe in the gods of the city.
      #v(0.8em)
      Read at your own risk.
    ]
  ]
]

#v(1fr)
