// Dipolo — helpers compartilhados.
// Fragmentos precisam importar isto explicitamente: #include nao herda
// o escopo de let do pai.

// Paleta da marca (referencias/MARCA.md). Impressao em preto; as cores
// existem para a prova de tela e para a capa.
#let forest = rgb("#17362a")
#let sand   = rgb("#d9c48e")
#let moss   = rgb("#52705c")

// Formato confirmado: folha 660x480 cortada ao meio + 2 dobras.
#let PAGE_W = 165mm
#let PAGE_H = 240mm

// Numeracao 01-04 em duas casas e maneirismo do site — ecoado aqui.
#let dois(n) = if n < 10 { "0" + str(n) } else { str(n) }

// A frase do bifolio de verge. Recto; o verso fica em branco.
// corpo: opcional, por frase. Frases longas pedem corpo menor -- nenhuma
// largura unica de coluna evita viuva nas 10 (testado de 70% a 100%),
// entao o ajuste e por frase, que e o que um compositor faria a mao.
#let frase(n, texto, fonte, corpo: 17pt, en: none) = {
  set page(margin: (inside: 26mm, outside: 18mm, top: 0mm, bottom: 0mm))
  // Bloco na "linha de ouro": ~38% da altura, nao no terco superior.
  // Centralizado verticalmente a pagina parece composta, nao cortada.
  v(PAGE_H * 0.34)
  // #align externo vaza para dentro do paragrafo justificado
  // e centraliza a ultima linha — por isso o set align dentro.
  // Coluna mais estreita que a caixa de texto: uma frase de destaque
  // nao deve ocupar a largura toda, e a medida menor equilibra as
  // linhas -- foi o que resolveu as viuvas de "conta." e "zero.".
  block(width: 100%)[
    #set align(left)
    #text(font: "Hanken Grotesk", size: 9pt, tracking: 1.6pt, fill: moss)[
      #dois(n)
    ]
    #v(14mm)
    // hyphenate desligado (nao se hifeniza frase de destaque) e
    // linebreaks otimizados: evita viuva de uma palavra na ultima linha.
    #par(linebreaks: "optimized")[
      #text(font: "Newsreader 16pt", size: corpo, style: "italic",
            hyphenate: false)[#texto]
    ]
    #v(7mm)
    // Versao inglesa junto a fonte: o site dele e bilingue, e as duas
    // versoes existem. PT no corpo, EN na atribuicao — ver raw/frases.md.
    #if en != none {
      block(width: 92%)[
        #set align(left)
        #text(font: "Newsreader 16pt", size: 9pt, style: "italic",
              fill: moss, hyphenate: false)[#en]
      ]
      v(3mm)
    }
    #text(font: "Hanken Grotesk", size: 7.5pt, tracking: 0.4pt, fill: moss)[
      #fonte
    ]
  ]
}
