#import "helpers.typ": *

// ── Personalisation ───────────────────────────────────────────────────
// check.py FAILS while the placeholder is still here, so the book cannot
// go to the printer with it by accident.
#let NOME = "Doristela Grazzini"
#let PRENOME = "Doristela"   // the dedication is personal; the colophon is a record

// Blank leaves at the end so the total is a multiple of 16 (booklet.py
// signatures of 4 sheets). Fixed number, not computed — computing it
// from counter(page).final() does not converge. check.py verifies.
#let PAD = 1

#show: setup

// Front-matter prose: a little smaller than the prayers, which are the
// part read in church, but still larger than a normal book.
#let prosa(body) = {
  set text(size: 11.5pt)
  set par(justify: true, leading: 0.6em, spacing: 0.9em, first-line-indent: 1.2em)
  set text(hyphenate: true)
  body
}
#let sec(body) = block(above: 1.6em, below: 0.9em, width: 100%,
  text(size: 9pt, tracking: 1.4pt, fill: RED, upper(body)))

// ── 1 · Title (recto) ─────────────────────────────────────────────────
#page(footer: none)[
  #v(1fr)
  #align(center)[
    #text(size: 9pt, tracking: 2.4pt, fill: RED)[LIBER PRECUM]
    #v(0.9em)
    #text(size: 22pt)[Livro de Orações]
    #v(1.4em)
    #text(size: 10.5pt, style: "italic")[o Terço \ a Novena ao Sagrado Coração de Jesus \ onze Salmos e o Magnificat]
    #v(1.6em)
    #text(fill: RED, size: 11pt)[✝]
  ]
  #v(1.2fr)
  #align(center, text(size: 9pt, tracking: 1.5pt, fill: MUTED)[MMXXVI])
]

// ── 2 · blank verso ───────────────────────────────────────────────────
#page(footer: none)[]

// ── 3 · Dedication (recto) ────────────────────────────────────────────
#page(footer: none)[
  #v(1fr)
  #align(center)[
    #text(size: 13pt, style: "italic")[Para #PRENOME,] \
    #text(size: 11pt, style: "italic")[nos seus oitenta anos.]
    #v(3em)
    #block(width: 82%)[
      #set par(leading: 0.7em)
      #text(size: 11pt, style: "italic")[Adhuc multiplicabuntur in senecta uberi, \ et bene patientes erunt.]
      #v(0.7em)
      #text(size: 10pt)[Eles se multiplicarão de novo numa velhice \ cumulada de bens; e serão cheios de vigor \ e de paciência.]
      #v(0.6em)
      #text(size: 8.5pt, tracking: 0.8pt, fill: RED)[SALMO 91 (92), 15]
    ]
  ]
  #v(1.6fr)
]

// ── 4 · blank verso ───────────────────────────────────────────────────
#page(footer: none)[]

// ── 5 · Index (recto) ─────────────────────────────────────────────────
// Built from the <toc> markers each section drops on its first page.
// May run to two pages at A6; the introduction then waits for a recto.
#page(footer: none)[
  #align(center, text(size: 15pt)[Índice])
  #v(1em)
  #set text(size: 10.5pt)
  #set par(leading: 0.5em, spacing: 0.5em)
  #let leader = box(width: 1fr, repeat(text(fill: MUTED, size: 8pt)[#h(0.25em).#h(0.25em)]))
  #context for e in query(<toc>) {
    let pg = str(e.location().page())
    if e.value.level == 1 {
      block(above: 0.95em, below: 0.35em)[#text(size: 8.5pt, tracking: 1.2pt, fill: RED, upper(e.value.body))#leader#text(fill: RED, pg)]
    } else {
      pad(left: 5mm, block[#e.value.body#leader#pg])
    }
  }
]

// ── Introduction, always on a recto ───────────────────────────────────
#pagebreak(to: "odd")

// ── Introduction ─────────────────────────────────────────────────
#inked(prosa[
#tocmark(1)[Introdução]
#align(center, text(size: 15pt)[Introdução])
#v(0.6em)

Este livro reúne três orações que andam juntas há muito tempo: o terço, os salmos e uma novena que o Padre Pio rezava todos os dias.

#sec[O Padre Pio e a Novena]

Francesco Forgione nasceu em Pietrelcina, no sul da Itália, em 1887, e entrou para os capuchinhos aos quinze anos com o nome de frei Pio. Passou quase toda a vida no convento de San Giovanni Rotondo, onde morreu em 1968. João Paulo II o canonizou em 16 de junho de 2002.

Recebia pedidos de oração aos milhares, por carta e em pessoa. Conta-se que respondia a todos da mesma maneira: todos os dias, por todos os que se recomendavam a ele, rezava uma novena breve ao Sagrado Coração de Jesus — a que está neste livro. A tradição atribui o texto a Santa Margarida Maria Alacoque (1647–1690), a religiosa francesa de Paray-le-Monial de quem nasceu a devoção ao Sagrado Coração; a atribuição é antiga, mas não há documento que a confirme.

A novena tem um raciocínio curioso. Cada uma das três súplicas começa citando uma promessa do próprio Jesus — _pedi e obtereis_; _o que pedirdes ao Pai em meu nome_; _o céu e a terra passarão, mas as minhas palavras não_ — e só depois pede. É uma oração que toma Jesus pela palavra.

Aqui ela aparece em italiano, na página da esquerda, com a tradução ao lado. Não há original latino — o texto nasceu em francês —, e o italiano foi a língua em que o Padre Pio a rezou. Na Itália, aliás, ela não se chama novena, e sim _coroncina_, «coroazinha»: ele não a rezava em nove dias, e sim todos os dias. No Brasil ficou conhecida como novena, e cada página usa o nome do seu país.

#sec[O Terço]

O rosário nasceu, segundo a história mais aceita, como o saltério de quem não sabia ler. Nos mosteiros rezavam-se os 150 salmos; os leigos, sem livro e sem latim, rezavam no lugar deles 150 Ave-Marias, contadas nas contas. É por isso que os salmos e o terço estão no mesmo livro: um nasceu à sombra do outro.

O Padre Pio rezava o rosário o dia inteiro e o chamava de sua arma. Rezava os quinze mistérios de então — gozosos, dolorosos e gloriosos. Os luminosos, que vão do Batismo à Eucaristia, foram acrescentados por João Paulo II em outubro de 2002, na carta _Rosarium Virginis Mariae_, quatro meses depois de canonizá-lo. O santo nunca os rezou; estão aqui porque hoje fazem parte do terço.

Para cada mistério há um trecho curto da Escritura, para ler antes da dezena.

#sec[Os Salmos e a sua numeração]

Os salmos seguem a numeração da Vulgata, a Bíblia latina da Igreja, que na maior parte do saltério fica um número atrás da hebraica: seguindo a antiga tradução grega, a Vulgata junta num só os salmos 9 e 10 do hebraico, e mais adiante divide outros. Por isso o salmo do bom pastor é aqui o 22, e o 23 nas Bíblias protestantes e em muitas católicas recentes. O número hebraico vai entre parênteses, como nos livros litúrgicos. Também os versículos contam diferente: a Vulgata numera o título do salmo, e por isso o primeiro verso às vezes é o 2 ou o 3.

A diferença não é só de número. Onde o hebraico diz «o Senhor é o meu pastor», o latim diz _Dominus regit me_, «o Senhor me governa»: nesse saltério São Jerônimo não traduziu do hebraico, revisou uma versão feita do grego. Pereira de Figueiredo, que traduziu do latim, escreveu «o Senhor é quem me conduz». Quem sabe o salmo de cor vai estranhar — mas foi assim que a Igreja latina o rezou por mais de mil anos.

#sec[Nota editorial]

O latim é o da Vulgata Clementina (1592), na grafia eclesiástica tradicional — _Jesus_, _ejus_, _caeli_ —, que é também a das orações. O português das passagens bíblicas é do padre António Pereira de Figueiredo (1725–1797), que traduziu toda a Bíblia a partir da Vulgata; o texto vem da edição de Londres de 1828. Foi atualizada apenas a ortografia — _he_ passou a _é_, _Deos_ a _Deus_ — e mantidos o vocabulário e a sintaxe do tradutor, mesmo onde soam antigos: «Benta és tu entre as mulheres», «Espera ao Senhor». Onde Figueiredo divide os versículos de outro modo, o português foi redistribuído para que os números coincidam nas duas páginas.

As orações estão nas formas rezadas no Brasil. As traduções da novena e da oração final do terço são do organizador, assim como as rubricas latinas de como rezar o terço. Todos os textos estão em domínio público.
])

// ── The book proper ───────────────────────────────────────────────────
#include "oracoes.typ"
#include "gen_misterios.typ"
#include "posrosario.typ"
#include "novena.typ"
#include "gen_salmos.typ"

// ── Colophon (recto) ──────────────────────────────────────────────────
#pagebreak(to: "odd")
#page(footer: none)[
  #v(1fr)
  #align(center)[
    #block(width: 80%)[
      #set par(leading: 0.65em, justify: false)
      #set text(size: 9.5pt)
      Compilado e encadernado à mão por \ Felipe de Toledo Farias \ para os oitenta anos de #NOME, \ em outubro de MMXXVI.

      #v(0.9em)
      #text(fill: MUTED)[Composto em Libertinus Serif. Latim da Vulgata Clementina (1592); português de António Pereira de Figueiredo (1725–1797), edição de Londres, 1828; orações da tradição da Igreja. Todos os textos em domínio público.]

      #v(1.8em)
      #text(fill: RED, size: 11pt)[✝]
      #v(0.6em)
      #text(size: 11pt, style: "italic")[Pulsate, et aperietur vobis.]
      #v(0.2em)
      #text(size: 8pt, tracking: 0.8pt, fill: MUTED)[MT 7, 7]
    ]
  ]
  #v(1.4fr)
]

#for _ in range(PAD) { page(footer: none)[] }
