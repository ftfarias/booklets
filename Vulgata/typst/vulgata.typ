// ─────────────────────────────────────────────────────────────
//  VANITAS — Três textos da Vulgata
//  Ecclesiastes · Canticum Canticorum · I Corinthios XIII
//  Latin: Vulgata Clementina (public domain)
//  Portuguese: João Ferreira de Almeida, Revista e Corrigida (PD)
//  Bilingual, parallel columns · A5 landscape · for print
// ─────────────────────────────────────────────────────────────

#set document(
  title: "Vanitas — Três textos da Vulgata",
  author: "Hieronymus (trans.) · João Ferreira de Almeida (trans.)",
)

// ── Page geometry ─────────────────────────────────────────────
// A4 landscape: 297 × 210 mm, ONE page per sheet, printed duplex.
// No imposition, no folding, no cutting — the sheets are stacked and
// sewn through the left margin (Japanese stab binding).
//
// The inner margin is 32 mm: the stab holes sit ~15 mm in, and the
// sewing itself takes a few more, so the text needs to clear both
// and still not disappear into the gutter when the book is opened.
//
// Type is 12 pt here, not the 9.5 pt of the A5 draft. The columns
// are ~115 mm wide; measured on the compiled text (Nov 2026), Libertinus
// gives ~68 characters a line at 11.5 pt and ~65 at 12 pt, in Latin
// and in Portuguese alike — at the long end of comfortable, so the
// extra sheet size goes into air rather than more text.
// NOTE: margins are left/right, NOT inside/outside. Inside/outside
// alternate by page parity, which is right for a folded codex but wrong
// here: stab binding sews every sheet through the SAME edge, so the wide
// margin must fall on the left of every page, recto and verso alike.
#set page(
  width:  297mm,
  height: 210mm,
  margin: (left: 40mm, right: 15mm, top: 20mm, bottom: 20mm),
  numbering: none,
)

#set text(
  font: "Libertinus Serif",
  size: 12pt,
  lang: "la",
  hyphenate: true,
)
#set par(
  justify: true,
  leading: 0.72em,
  first-line-indent: 0em,
  spacing: 0.68em,
)

#import "helpers.typ": *

// ═══════════════════════════════════════════════════════════════
//  COVER
// ═══════════════════════════════════════════════════════════════
#page(margin: (x: 22mm, y: 20mm))[
  #v(1.2fr)
  #align(center)[
    #text(size: 10pt, tracking: 6pt, fill: rgb("#777777"))[EX VULGATA]
    #v(2.2em)
    #text(size: 40pt, weight: "bold")[Vanitas]
    #v(0.9em)
    #line(length: 34%, stroke: 0.6pt + rgb("#888888"))
    #v(1.1em)
    #text(size: 12pt, style: "italic", fill: rgb("#444444"))[
      Ecclesiastes · Canticum Canticorum
      #linebreak()
      Ad Corinthios I, xiii
    ]
    #v(2.6em)
    #text(size: 9.5pt, fill: rgb("#666666"))[
      texto latino e português
    ]
  ]
  #v(1.6fr)
]
#pagebreak()

// ═══════════════════════════════════════════════════════════════
//  EPIGRAPH
// ═══════════════════════════════════════════════════════════════
#page(header: none, footer: none)[
  #v(1fr)
  #align(center)[
    #block(width: 66%)[
      #set par(justify: false, leading: 0.9em)
      #text(size: 13pt, style: "italic")[
        Vanitas vanitatum, dixit Ecclesiastes;
        #linebreak()
        vanitas vanitatum, et omnia vanitas.
      ]
      #v(1.1em)
      #text(size: 10pt, fill: rgb("#666666"))[
        Vaidade de vaidades, diz o pregador;
        #linebreak()
        vaidade de vaidades, tudo é vaidade.
      ]
      #v(1.3em)
      #text(size: 8pt, tracking: 1.5pt, fill: rgb("#9a9a9a"))[ECCL. I, 2]
    ]
  ]
  #v(1.4fr)
]

// ═══════════════════════════════════════════════════════════════
//  INTRODUCTION
// ═══════════════════════════════════════════════════════════════
#page(header: none, footer: none)[
  #v(0.5fr)
  #align(center)[
    #block(width: 58%)[
      #set par(justify: true, leading: 0.70em, first-line-indent: 0em)
      #set align(left)
      #align(center)[
        #text(size: 9pt, tracking: 3pt, fill: rgb("#9a9a9a"))[A VULGATA]
      ]
      #v(1.2em)
      #text(size: 10pt)[
        Em 382, o papa Dâmaso I encarregou seu secretário, Jerônimo de
        Estridão, de pôr ordem nas versões latinas dos Evangelhos, que
        circulavam em cópias divergentes e de qualidade irregular. A
        encomenda parava aí. Dâmaso morreu dois anos depois, e Jerônimo,
        já retirado em Belém, seguiu por conta própria — e muito além do
        pedido: traduziu o Antigo Testamento inteiro, e não da Septuaginta
        grega que a Igreja usava, mas do hebraico original.

        #v(0.7em)
        A escolha foi polêmica. Agostinho escreveu-lhe alarmado, temendo
        que o abandono da Septuaginta dividisse as igrejas grega e latina.
        Jerônimo não recuou. O trabalho consumiu-lhe cerca de vinte e três
        anos e produziu o texto que a Europa leria, citaria e discutiria
        por mil anos — a _versio vulgata_, a «versão em uso corrente». Foi a Bíblia de Tomás de Aquino, de Dante e de Gutenberg, e o
        texto oficial da Igreja até 1979.
      ]
    ]
  ]
  #v(0.8fr)
]

#page(header: none, footer: none)[
  #v(0.5fr)
  #align(center)[
    #block(width: 58%)[
      #set par(justify: true, leading: 0.70em, first-line-indent: 0em)
      #set align(left)
      #align(center)[
        #text(size: 9pt, tracking: 3pt, fill: rgb("#9a9a9a"))[OS TRÊS TEXTOS]
      ]
      #v(1.2em)
      #text(size: 10pt)[
        Os três textos reunidos aqui têm em comum aquilo que quase não se
        espera de um livro sagrado: nenhum deles ensina doutrina.

        #v(0.7em)
        O _Ecclesiastes_ é um tratado sobre a futilidade do esforço humano
        diante do tempo. Seu autor, que se apresenta apenas como Qohelet —
        "aquele que fala à assembleia" — examina o trabalho, a riqueza, a
        sabedoria e o prazer, e conclui que nada disso permanece. É o livro
        mais próximo da filosofia grega que o cânone contém, e o que mais
        se parece com um estoico escrevendo em hebraico.

        #v(0.7em)
        O _Canticum Canticorum_ é poesia amorosa, e nada mais. Deus não é
        mencionado uma única vez em seus oito capítulos. Sobreviveu no
        cânone graças à leitura alegórica — a alma e Deus, a Igreja e
        Cristo — mas o texto que se lê é o de dois amantes que se procuram
        por uma cidade à noite.

        #v(0.7em)
        O capítulo treze da primeira carta _aos Coríntios_ interrompe uma
        discussão administrativa sobre a ordem nas assembleias para dizer
        que nada daquilo importa sem _caritas_. É o ponto mais alto da
        prosa de Paulo, e funciona inteiramente fora do argumento que o
        cerca.

        #v(0.7em)
        Vaidade, amor e o que resta quando se tira o resto: os três se
        sustentam sem que se peça nada ao leitor senão que leia.
      ]
    ]
  ]
  #v(0.6fr)
]

// ═══════════════════════════════════════════════════════════════
//  EDITORIAL NOTE
// ═══════════════════════════════════════════════════════════════
#page(header: none, footer: none)[
  #v(0.6fr)
  #align(center)[
    #block(width: 56%)[
      #set par(justify: true, leading: 0.72em, first-line-indent: 0em)
      #set align(left)
      #align(center)[
        #text(size: 9pt, tracking: 3pt, fill: rgb("#9a9a9a"))[NOTA]
      ]
      #v(1.1em)
      #text(size: 10pt)[
        O texto latino é o da _Vulgata Clementina_ (1592), a tradução
        de São Jerônimo tal como fixada sob Clemente VIII — o texto que
        a Igreja usou por quase quatro séculos. À direita, a tradução
        de _João Ferreira de Almeida_, na sua forma revista e corrigida.

        #v(0.7em)
        As duas colunas correm em paralelo versículo a versículo. Onde a
        Vulgata divide os capítulos de modo diferente do texto hebraico
        — sobretudo em Ecclesiastes IV--VIII e no Canticum — o pareamento
        foi ajustado para que o sentido, e não a numeração, fique lado a lado.

        #v(0.7em)
        Uma nota sobre uma palavra: onde o latim diz _caritas_, Almeida
        traduz "amor". As edições católicas costumam dizer "caridade".
        Jerônimo escolheu _caritas_ para o grego #text(font: "Libertinus Serif")[ἀγάπη],
        distinguindo-a de _amor_ — e a coluna da esquerda guarda essa distinção
        que a da direita, deliberadamente, desfaz.
      ]
    ]
  ]
  #v(1fr)
]

// ═══════════════════════════════════════════════════════════════
//  I. ECCLESIASTES
// ═══════════════════════════════════════════════════════════════
#worktitle(
  [Ecclesiastes],
  [Eclesiastes],
  [Quid habet amplius homo de universo labore suo quo laborat sub sole?],
  [Que proveito tem o homem, de todo o seu trabalho, com que se afadiga debaixo do sol?],
)
#collabels()
#include "ecclesiastes.typ"

// ═══════════════════════════════════════════════════════════════
//  II. CANTICUM CANTICORUM
// ═══════════════════════════════════════════════════════════════
#worktitle(
  [Canticum Canticorum],
  [Cântico dos Cânticos],
  [Fortis est ut mors dilectio.],
  [O amor é forte como a morte.],
)
#collabels()
#include "canticum.typ"

// ═══════════════════════════════════════════════════════════════
//  III. AD CORINTHIOS I, XIII
// ═══════════════════════════════════════════════════════════════
#worktitle(
  [Ad Corinthios I],
  [I Coríntios · capítulo XIII],
  [Nunc autem manent fides, spes, caritas, tria haec: major autem horum est caritas.],
  [Agora, pois, permanecem a fé, a esperança, o amor, estes três; mas o maior destes é o amor.],
)
#collabels()
#include "caritas.typ"

// ═══════════════════════════════════════════════════════════════
//  COLOPHON
// ═══════════════════════════════════════════════════════════════
#pagebreak(to: "odd", weak: true)
#page(header: none, footer: none)[
  #v(1fr)
  #align(center)[
    #block(width: 68%)[
      #set par(justify: false, leading: 0.85em)
      #text(size: 11pt, style: "italic")[
        Cuncta tentavi in sapientia.
      ]
      #v(0.5em)
      #text(size: 9pt, fill: rgb("#666666"))[
        Tudo isto provei pela sabedoria.
      ]
      #v(2.2em)
      #line(length: 24%, stroke: 0.4pt + rgb("#c8c8c8"))
      #v(2.2em)
      #text(size: 8.5pt, fill: rgb("#555555"))[
        Texto latino da Vulgata Clementina.
        #linebreak()
        Tradução portuguesa de João Ferreira de Almeida.
        #linebreak()
        Ambos em domínio público.
        #v(1.4em)
        Composto em Libertinus Serif.
        #linebreak()
        Compilado e encadernado à mão por
        #linebreak()
        Felipe de Toledo Farias.
      ]
    ]
  ]
  #v(1.3fr)
]

// ═══════════════════════════════════════════════════════════════
//  PAD
//  One blank leaf closing the block, as a rear flyleaf.
//
//  A multiple of 4 is NOT required here: that constraint came from
//  saddle-stitch imposition, where four pages share a folded sheet.
//  These sheets are printed one page per side and stacked flat, so
//  the only requirement is an EVEN count — each sheet has two sides.
// ═══════════════════════════════════════════════════════════════
#let PAD = 3
#for _ in range(PAD) {
  pagebreak(weak: false)
  page(header: none, footer: none)[]
}
