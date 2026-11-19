// ─────────────────────────────────────────────────────────────
//  MANUAL DO ENCADERNADOR NOVATO
//  (com mania de saber um monte de detalhe de tudo)
//  Compilação temática de pesquisa · A5 · encadernação à mão
// ─────────────────────────────────────────────────────────────

#set document(
  title: "Manual do Encadernador Novato",
  author: "Felipe de Toledo Farias",
)

// ── Geometria A5, margem interna generosa para a costura ──
// Mesma dos volumes literários, com +1mm interno: o manual é mais
// grosso e a lombada come mais.
#set page(
  width:  148mm,
  height: 210mm,
  margin: (inside: 21mm, outside: 15mm, top: 18mm, bottom: 20mm),
)

#set text(
  font: "Libertinus Serif",
  size: 10pt,
  lang: "pt",
  hyphenate: true,
)

#set par(
  justify: true,
  leading: 0.68em,
  first-line-indent: 0em,   // manual: parágrafo separado por espaço, não recuo
  spacing: 0.75em,
)

#import "helpers.typ": *

// Nome do estúdio. Aparece na capa e no colofão.
#let ESTUDIO = "Estúdio Quattrocento"

// ── Hierarquia de títulos ──
#show heading.where(level: 1): it => block(above: 0em, below: 1.8em)[
  #set par(first-line-indent: 0em, justify: false)
  #text(size: 19pt, weight: "bold")[#it.body]
  #v(0.35em)
  #line(length: 100%, stroke: 0.6pt + LINHA)
]
#show heading.where(level: 2): it => block(above: 1.5em, below: 0.7em)[
  #set text(size: 13pt, weight: "bold")
  #it.body
]
#show heading.where(level: 3): it => block(above: 1.15em, below: 0.55em)[
  #set text(size: 10.5pt, weight: "bold")
  #it.body
]
#show heading.where(level: 4): it => block(above: 0.9em, below: 0.4em)[
  #set text(size: 10pt, weight: "bold", style: "italic")
  #it.body
]

#show table: set block(breakable: true)

// Listas: respiro em volta do bloco, itens levemente separados
#set list(spacing: 0.72em, indent: 0.6em)
#set enum(spacing: 0.72em, indent: 0.6em)
#show list: set block(above: 0.85em, below: 0.9em)
#show enum: set block(above: 0.85em, below: 0.9em)
#show link: set text(fill: rgb("#333333"))

// ═══════════════════════════════════════════════════════════════
//  CAPA
// ═══════════════════════════════════════════════════════════════
#page(margin: (x: 16mm, y: 24mm), numbering: none, header: none, footer: none)[
  #v(2fr)
  #align(center)[
    #text(size: 11pt, tracking: 5pt, fill: CINZA)[MANUAL DO]
    #v(1.6em)
    #text(size: 30pt, weight: "bold")[Encadernador]
    #v(0.15em)
    #text(size: 30pt, weight: "bold")[Novato]
    #v(1.4em)
    #line(length: 40%, stroke: 0.6pt + rgb("#888888"))
    #v(1.4em)
    #text(size: 11pt, style: "italic", fill: rgb("#444444"))[
      com mania de saber um monte\
      de detalhe de tudo
    ]
  ]
  #v(3fr)
  #align(center)[
    #text(size: 9.5pt, style: "italic", fill: rgb("#666666"))[Non est ad astra mollis e terris via]
  ]
  #v(1.6fr)
  #align(center)[
    #text(size: 8.5pt, tracking: 2.5pt, fill: rgb("#777777"))[#upper(ESTUDIO)]
    #v(0.35em)
    #text(size: 8.5pt, fill: rgb("#999999"))[2026]
  ]
]

// ── Verso da capa: a ressalva ──
#page(numbering: none, header: none, footer: none)[
  #v(1fr)
  #set par(justify: false, leading: 0.7em)
  #align(center)[
    #block(width: 80%)[
      #set text(size: 8.5pt, fill: CINZA, hyphenate: false)
      // justificado dentro de align(center) centraliza a última linha de
      // cada parágrafo (ver ../CLAUDE.md); centralizado e sem justificar.
      #set par(justify: false, leading: 0.85em)
      Compilação temática de vinte e uma conversas de pesquisa sobre
      encadernação, mantidas ao longo de 2026, condensadas por assunto e
      conferidas com as fontes clássicas do ofício.

      #v(0.9em)

      #emph[Material de referência, não evangelho.] Vem de conversas com
      modelo de linguagem e pode conter erro. Preço, disponibilidade no
      Brasil e nome comercial de produto são os itens de menor confiança.
      Teste antes de aplicar em peça que importa, mudando uma variável
      de cada vez.
    ]
  ]
  #v(1.6fr)
]

// ═══════════════════════════════════════════════════════════════
//  SUMÁRIO
// ═══════════════════════════════════════════════════════════════
#page(numbering: none, header: none)[
  #block(below: 1.5em)[
    #set par(first-line-indent: 0em)
    #text(size: 17pt, weight: "bold")[Sumário]
    #v(0.3em)
    #line(length: 100%, stroke: 0.6pt + LINHA)
  ]
  #set par(justify: false, leading: 0.5em)
  #set text(size: 8pt)
  #show outline.entry.where(level: 1): it => {
    v(0.85em, weak: true)
    strong(it)
  }
  #outline(
    title: none,
    depth: 2,
    indent: 1.2em,
  )
]

// ═══════════════════════════════════════════════════════════════
//  CORPO
// ═══════════════════════════════════════════════════════════════
#set page(
  numbering: "1",
  header: context {
    // Página física (não o número impresso, que recomeça no corpo).
    let fis = here().page()
    // Página de abertura de capítulo já traz o título: sem cabeçalho.
    // Antes, o código comparava o número impresso com o físico e nunca
    // acertava — e mostrava o nome do capítulo anterior na abertura.
    if query(heading.where(level: 1)).any(h => h.location().page() == fis) { return }
    let caps = query(selector(heading.where(level: 1)).before(here()))
    let nome = if caps.len() > 0 { caps.last().body } else { [] }
    set text(size: 8pt, fill: CLARO)
    if calc.odd(fis) {
      align(right)[#nome]
    } else {
      align(left)[Manual do Encadernador]
    }
    v(-0.4em)
    line(length: 100%, stroke: 0.4pt + LINHA)
  },
)
#counter(page).update(1)

#include "corpo.typ"

// ═══════════════════════════════════════════════════════════════
//  COLOFÃO
// ═══════════════════════════════════════════════════════════════
// O colofão vai em página par. Se o corpo acabou numa par, entra uma
// página realmente em branco — sem cabeçalho nem número (cap. 4). O
// pagebreak(to: "even") fazia isso, mas a página saía com cabeçalho.
// A decisão usa uma etiqueta fixa no fim do corpo, não a posição do próprio
// bloco — que muda quando a página é inserida, e o layout oscilava.
#metadata(none) <fim-do-corpo>
#context if calc.even(locate(<fim-do-corpo>).page()) {
  page(header: none, footer: none, numbering: none)[]
}
#page(numbering: none, header: none, footer: none)[
  #v(1fr)
  #align(center)[
    #block(width: 74%)[
      #set par(justify: false, leading: 0.75em)
      #set text(size: 9pt, fill: CINZA)
      #text(size: 8pt, tracking: 3pt, fill: CLARO)[COLOFÃO]
      #v(1.4em)
      #set par(leading: 0.9em)
      #set text(hyphenate: false)   // nunca quebrar o nome do estúdio
      Este manual foi composto em Libertinus Serif, impresso, dobrado e
      encadernado à mão por Felipe de Toledo Farias, no #ESTUDIO, no ano
      de #datetime.today().display("[year]").
      #v(0.6em)
      Reúne o que se aprendeu, pergunta a pergunta, no primeiro ano de
      ofício — e o que os mestres antigos já sabiam e a pressa moderna
      esqueceu.
      #v(1.6em)
      #line(length: 30%, stroke: 0.5pt + LINHA)
      #v(1.4em)
      #text(size: 9.5pt, style: "italic", fill: rgb("#555555"))[Ars longa, vita brevis.]
      #v(0.5em)
      #text(size: 8.5pt, fill: rgb("#777777"))[A arte é longa; a vida, breve.]
    ]
  ]
  #v(1.4fr)
]

// Fecha em número par de páginas — cada folha tem dois lados.
// Decidir isso lendo o contador realimenta o layout e o Typst não
// converge (a mesma armadilha do ../CLAUDE.md). Em vez disso, o colofão
// abre em página ímpar: assim o documento termina sempre em par.
