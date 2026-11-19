// Estilos do Manual do Encadernador.
// Espelha plato_3_dialogs/typst/helpers.typ e Estoicos1/typst/helpers.typ;
// fragmentos precisam de `#import "helpers.typ": *` — o #include do Typst
// NÃO compartilha o escopo de let do pai.

#let CINZA  = rgb("#666666")
#let CLARO  = rgb("#999999")
#let LINHA  = rgb("#cccccc")
#let FUNDO  = rgb("#f4f2ed")   // creme, casa com papel pólen

// ── Abertura de capítulo ──────────────────────────────────────────
// Sempre em página ímpar, como nos volumes literários.
// É um heading de nível 1 de verdade (entra no sumário e no cabeçalho),
// com a aparência definida por um show rule no mestre.
#let capitulo(titulo) = {
  pagebreak()
  heading(level: 1)[#titulo]
}

// ── Abertura de parte ────────────────────────────────────────────
// Folha de rosto da parte, em página ímpar. Não entra no corpo do
// sumário como capítulo: é heading de nível 1 com numeração própria.
#let parte(nome) = page(header: none, footer: none, numbering: none)[
  // O título escondido do sumário vai DENTRO da folha de rosto. Antes ele
  // ficava numa página própria, antes da folha: seis páginas em branco no
  // livro, e o sumário apontando para elas.
  #place(hide[#heading(level: 1, outlined: true)[#nome]])
  #v(2fr)
  #align(center)[
    #block(width: 70%)[
      #set par(justify: false)
      #set text(hyphenate: false)
      #line(length: 100%, stroke: 0.6pt + LINHA)
      #v(1.1em)
      #text(size: 16pt, weight: "bold")[#nome]
      #v(1.1em)
      #line(length: 100%, stroke: 0.6pt + LINHA)
    ]
  ]
  #v(3fr)
]

// ── A "regra em destaque" do topo de cada capítulo ────────────────
// Blockquote com filete lateral: o elemento mais consultado do manual.
#let regra(corpo) = block(
  width: 100%,
  fill: FUNDO,
  inset: (x: 10pt, y: 9pt),
  radius: 2pt,
  above: 1.1em, below: 1.2em,
)[
  #set par(first-line-indent: 0em, justify: false, leading: 0.62em)
  #set text(size: 9.5pt)
  #corpo
]

// ── Tabelas ───────────────────────────────────────────────────────
// O manual tem 577 linhas de tabela, até 6 colunas, num miolo A5 de
// 113mm úteis. O corpo cai conforme o número de colunas, senão a
// tabela de 6 estoura a mancha.
#let tabela(ncols) = (cabecalho, celulas) => {
  let corpo = if ncols <= 2 { 9pt }
              else if ncols == 3 { 8.5pt }
              else if ncols == 4 { 8pt }
              else { 7pt }

  block(above: 1.0em, below: 1.1em, breakable: true)[
    #set text(size: corpo, hyphenate: true)
    #set par(justify: false, first-line-indent: 0em, leading: 0.55em)
    #table(
      columns: ncols,
      stroke: none,
      inset: (x: 5pt, y: 4.5pt),
      align: left + top,
      fill: (_, y) => if y == 0 { FUNDO },
      table.header(..cabecalho.map(c => strong(c))),
      table.hline(stroke: 0.5pt + LINHA),
      ..celulas.flatten(),
    )
  ]
}

// ── Figuras ───────────────────────────────────────────────────────
// Caminho a partir da raiz do projeto (manual/), que o Makefile passa
// em --root. É como os .md escrevem o caminho. A legenda vai abaixo, em corpo menor.
#let figura(caminho, legenda) = block(
  width: 100%, above: 1.1em, below: 1.1em, breakable: false,
  // sticky: a figura não se separa do parágrafo que a introduz, mas
  // também não força a quebra sozinha deixando meia página vazia.
)[
  #align(center)[
    // Gravuras (jpg) ficam pequenas; esquemas (svg) são largos e pedem espaço.
    #image("/" + caminho, width: if caminho.ends-with(".svg") { 85% } else { 52% })
    #if legenda != [] {
      v(0.45em)
      set text(size: 8pt, fill: CINZA, style: "italic")
      set par(justify: false, leading: 0.55em)
      block(width: 78%)[#legenda]
    }
  ]
]

// ── Blocos de código / sequências ─────────────────────────────────
// Monoespaçado, preservando quebras e colunas. O corpo é calculado pela
// linha mais larga do bloco para que ela caiba na mancha: ~0,6 em por
// caractere em fonte mono, teto de 8,5 pt para blocos curtos.
#let codigo(largura, conteudo) = context {
  let util = 112mm - 2 * 7pt - 2pt     // mancha − recuo interno − folga
  let tam = calc.min(8.5pt, util / (largura * 0.602))
  block(
    width: 100%, fill: FUNDO, inset: (x: 7pt, y: 6pt), radius: 2pt,
    above: 0.9em, below: 1em, breakable: true,
  )[
    #show raw: set text(size: tam)
    #set par(justify: false, leading: 0.5em)
    #conteudo
  ]
}
