// Roteiro de reunião — Grupo Serenidade On-line (CCA).
// A5 retrato: lê bem na tela do celular/tablet e imprime 2-up numa A4.
//
//   typst compile roteiro.typ
//
// Convenção visual:
//   texto em itálico roxo-claro, com barra à esquerda → instrução para quem
//     coordena (não se lê em voz alta);
//   caixa "todos"                                    → lido em conjunto;
//   o resto                                          → lido por quem coordena.

// ---- Dados da tesouraria (preencher; vazio vira linha em branco) ----
#let banco = "Caixa Econômica Federal"
#let agencia = "4095"
#let operacao = "1288"
#let conta = "000763462033-6"
#let titular = "Adriana S. G."
#let pix = "gruposerenidadeonline@gmail.com"

// ---- Identidade (a mesma das placas) ----
#let roxo = rgb("#4b2a86")
#let lilas = rgb("#7a63a8")
#let fundo = rgb("#f3f0f9")
#let titulo-fonte = "Futura"

#set document(title: "Roteiro de Reunião — Grupo Serenidade On-line",
  author: "Grupo Serenidade On-line · CCA")
#set text(font: "Libertinus Serif", size: 11pt, lang: "pt", region: "br")
#set par(justify: true, leading: 0.62em, spacing: 0.9em)

#let em-branco(v, largura: 32mm) = if v == "" { box(width: largura, line(length: 100%, stroke: 0.4pt + lilas)) } else { v }

#set page(
  paper: "a5",
  margin: (x: 17mm, top: 17mm, bottom: 20mm),
  footer: context {
    let n = counter(page).get().first()
    if n > 1 {
      set text(font: titulo-fonte, size: 7.5pt, fill: lilas, tracking: 0.12em)
      place(left + horizon)[GRUPO SERENIDADE ON-LINE]
      place(right + horizon)[CCA]
      align(center + horizon, text(size: 9pt, fill: roxo)[#n])
    }
  },
)

// ---- Títulos ----
#set heading(numbering: "1")
#show heading.where(level: 1): it => block(above: 1.9em, below: 1.1em, sticky: true, width: 100%)[
  #set text(font: titulo-fonte, fill: roxo)
  #grid(columns: (9mm, 1fr), column-gutter: 2mm, align: (left + bottom, left + bottom),
    text(size: 17pt, weight: "medium")[#counter(heading).display()],
    stack(spacing: 2.2mm,
      text(size: 10.5pt, weight: "bold", tracking: 0.14em)[#upper(it.body)],
      line(length: 100%, stroke: 0.6pt + roxo)))
]
#show heading.where(level: 2): it => block(above: 1.5em, below: 0.75em, sticky: true)[
  #set text(font: titulo-fonte, size: 8.5pt, weight: "bold", fill: lilas, tracking: 0.14em)
  #upper(it.body)
]

// ---- Blocos ----
// Instrução para quem coordena.
#let rubrica(corpo) = block(above: 1em, below: 1em, inset: (left: 3mm, y: 0.5mm),
  stroke: (left: 1.2pt + lilas))[
  #set text(size: 9.5pt, style: "italic", fill: lilas)
  #set par(justify: false)
  #corpo
]

// Lido em conjunto.
#let todos(corpo, rotulo: "todos") = block(width: 100%, above: 1.2em, below: 1.2em,
  fill: fundo, radius: 2mm, inset: (x: 6mm, y: 4.5mm), breakable: false)[
  #set align(center)
  #set par(justify: false)
  #text(font: titulo-fonte, size: 7pt, weight: "bold", fill: roxo, tracking: 0.25em)[#upper(rotulo)]
  #v(1.5mm)
  #corpo
]

// Versos centrados em versalete (anonimato, compromisso).
#let versos(corpo) = text(size: 11.5pt, tracking: 0.04em)[#smallcaps(corpo)]

// Passo ou Tradição: número, texto, princípio espiritual.
#let item(n, corpo, principio) = block(above: 0.85em, below: 0.85em, breakable: false,
  grid(columns: (7mm, 1fr), column-gutter: 2.5mm,
    align(right, text(font: titulo-fonte, size: 11pt, weight: "bold", fill: roxo)[#n]),
    [#corpo \ #text(size: 9pt, fill: lilas)[#smallcaps[princípio espiritual:] #h(0.2em) _#principio _]]))

// Cartão para postar no chat: instrução + miniatura(s).
// Cada imagem é (arquivo, legenda); legenda "" fica sem legenda.
// Miniaturas pequenas de propósito: as originais vêm do WhatsApp, em baixa
// resolução — a 30 mm de altura ficam nítidas na tela e no papel.
#let cartao(quando, altura: 30mm, ..imgs) = block(above: 1.1em, below: 1.2em,
  breakable: false, inset: (left: 3mm, y: 0.5mm), stroke: (left: 1.2pt + lilas))[
  #set par(justify: false)
  #text(font: titulo-fonte, size: 6.5pt, weight: "bold", fill: lilas, tracking: 0.2em)[CARTÃO PARA O CHAT]
  #h(1.5mm)
  #text(size: 9.5pt, style: "italic", fill: lilas)[#quando]
  #v(1mm)
  #grid(columns: imgs.pos().len(), column-gutter: 3mm, row-gutter: 1.2mm,
    ..imgs.pos().map(((arq, _)) => box(clip: true, radius: 1.2mm, stroke: 0.4pt + lilas.lighten(40%),
      image("imagens/limpas/" + arq + ".png", height: altura))),
    ..imgs.pos().map(((_, leg)) => text(size: 8pt, style: "italic", fill: lilas)[#leg]))
]

#let citacao(corpo) = block(inset: (x: 6mm), above: 1em, below: 1em)[#set text(style: "italic"); #corpo]
#let fonte(corpo) = align(right, text(size: 8.5pt, fill: lilas)[#corpo])
#let permissao(corpo) = block(above: 1.2em)[#set text(size: 8.5pt, fill: lilas); #set par(justify: false); #corpo]

// =====================================================================
// Capa
// =====================================================================
#page(footer: none, margin: 0mm)[
  #place(top + left, dx: 8mm, dy: 8mm,
    rect(width: 148mm - 16mm, height: 210mm - 16mm, radius: 4mm, stroke: 1.2mm + roxo))
  #place(top + left, dx: 11mm, dy: 11mm,
    rect(width: 148mm - 22mm, height: 210mm - 22mm, radius: 2.5mm, stroke: 0.3mm + roxo))
  #align(center + horizon)[
    #set text(font: titulo-fonte, fill: roxo)
    #text(size: 8.5pt, weight: "medium", tracking: 0.3em)[COMEDORES COMPULSIVOS ANÔNIMOS]
    #v(16mm)
    #text(size: 30pt, weight: "bold", tracking: 0.08em)[ROTEIRO] \
    #v(1mm)
    #text(size: 15pt, weight: "medium", tracking: 0.2em)[DE REUNIÃO]
    #v(9mm)
    #line(length: 32mm, stroke: 0.7mm + roxo)
    #v(9mm)
    #text(size: 12pt, weight: "medium", tracking: 0.12em)[GRUPO SERENIDADE ON-LINE]
    #v(26mm)
    #block(width: 84mm)[
      #set text(font: "Libertinus Serif", size: 10.5pt, style: "italic", fill: roxo)
      #set par(justify: false, leading: 0.7em)
      Concedei-me, Senhor, a serenidade necessária para aceitar as coisas que
      não posso modificar, coragem para modificar aquelas que posso e
      sabedoria para distinguir umas das outras.
    ]
  ]
]

// =====================================================================
// Ordem da reunião
// =====================================================================
#block(below: 1.4em)[
  #set text(font: titulo-fonte, fill: roxo)
  #text(size: 10.5pt, weight: "bold", tracking: 0.14em)[ORDEM DA REUNIÃO]
  #v(-1mm)
  #line(length: 100%, stroke: 0.6pt + roxo)
]

#{
  show outline.entry: it => {
    set text(size: 10.5pt)
    link(it.element.location(), it.indented(
      text(font: titulo-fonte, size: 9pt, weight: "bold", fill: roxo)[#it.prefix()],
      [#it.body() #box(width: 1fr, repeat(text(fill: lilas)[.#h(2pt)])) #text(fill: roxo)[#it.page()]]))
  }
  set outline.entry(fill: none)
  outline(title: none, depth: 1, indent: 0pt)
}

#v(1fr)

#block(fill: fundo, radius: 2mm, inset: 5mm, width: 100%)[
  #set text(size: 9.5pt)
  #set par(justify: false)
  #text(font: titulo-fonte, size: 7pt, weight: "bold", fill: roxo, tracking: 0.25em)[COMO LER ESTE ROTEIRO]
  #v(1mm)
  #grid(columns: (12mm, 1fr), row-gutter: 3mm, column-gutter: 3mm, align: (center + horizon, left + horizon),
    box(width: 7mm, height: 4.5mm, stroke: (left: 1.2pt + lilas)),
    text(style: "italic", fill: lilas)[Instrução para quem coordena — não se lê em voz alta.],
    box(width: 10mm, height: 4.5mm, fill: white, radius: 1mm, inset: (top: 1.2mm),
      text(font: titulo-fonte, size: 5pt, weight: "bold", fill: roxo, tracking: 0.15em)[TODOS]),
    [Lido em conjunto por todos os participantes.],
    text(size: 13pt, fill: roxo)[Aa],
    [Texto corrido — lido por quem coordena, ou por quem for convidado.],
  )
]

#pagebreak()

// =====================================================================
= Abertura

Sejam bem-vindos à reunião de Comedores Compulsivos Anônimos. Sou
#em-branco(""), comedor(a) compulsivo(a), e vou prestar serviço na
coordenação desta reunião.

Vamos ficar atentos à nossa unidade com diversidade, que nos une em nosso
propósito comum, respeitando nossas diferenças. Qualquer que seja o seu
problema com a comida, você é muito bem-vindo a esta reunião.

Por favor, aqueles que desejarem, juntem-se a mim na Oração da Serenidade.

#todos(rotulo: "Oração da Serenidade")[
  Concedei-me, Senhor, a serenidade necessária \
  para aceitar as coisas que não posso modificar, \
  coragem para modificar aquelas que posso \
  e sabedoria para distinguir umas das outras.
]

#cartao([Pode ser postado durante a oração.], ("serenidade", ""))

// =====================================================================
= Preâmbulo de CCA

Comedores Compulsivos Anônimos é uma Irmandade de indivíduos que,
compartilhando experiências, força e esperança, estão se recuperando do comer
compulsivo.

Em CCA damos as boas-vindas a todos que desejam parar de comer
compulsivamente. Não há taxas ou mensalidades para ser membro de CCA; somos
autossustentados através de nossas próprias contribuições, não solicitando
nem aceitando doações de fora.

CCA não está filiado a nenhuma organização pública, movimento político,
doutrina ideológica ou religião. Não opinamos sobre assuntos alheios à
Irmandade. Nosso propósito primordial é nos abster de comer compulsivamente e
transmitir essa mensagem de recuperação aos que ainda sofrem.

CCA sugere que se creia em um Poder Superior a nós mesmos, ou em Deus, como
cada um O conceber.

// =====================================================================
= Os Doze Passos

#rubrica[Pode-se pedir a um ou mais companheiros que leiam os Passos.]

Os Doze Passos de Comedores Compulsivos Anônimos, com seus princípios
espirituais. Os Doze Passos são o coração do nosso programa e a chave da nossa
recuperação:

#item("1")[Admitimos que éramos impotentes perante a comida — que tínhamos
  perdido o domínio de nossas vidas.][Honestidade]
#item("2")[Viemos a acreditar que um Poder Superior a nós mesmos poderia
  devolver-nos à sanidade.][Esperança]
#item("3")[Decidimos entregar nossa vontade e nossa vida aos cuidados de Deus,
  na forma em que O concebíamos.][Fé]
#item("4")[Fizemos minucioso e destemido inventário moral de nós
  mesmos.][Coragem]
#item("5")[Admitimos perante Deus, perante nós mesmos e perante outro ser
  humano a natureza exata de nossas falhas.][Integridade]
#item("6")[Prontificamo-nos inteiramente a deixar que Deus removesse todos
  esses defeitos de caráter.][Boa vontade]
#item("7")[Humildemente rogamos a Ele que nos livrasse de nossas
  imperfeições.][Humildade]
#item("8")[Fizemos uma relação de todas as pessoas que tínhamos prejudicado e
  nos dispusemos a reparar os danos a elas causados.][Autodisciplina]
#item("9")[Fizemos reparações diretas dos danos causados a tais pessoas,
  sempre que possível, salvo quando fazê-lo significasse prejudicá-las ou a
  outrem.][Amor ao próximo]
#item("10")[Continuamos fazendo o inventário pessoal e, quando estávamos
  errados, nós o admitimos prontamente.][Perseverança]
#item("11")[Procuramos, por meio da prece e da meditação, melhorar nosso
  contato consciente com Deus, na forma em que O concebíamos, rogando apenas o
  conhecimento de Sua vontade em relação a nós e forças para realizar essa
  vontade.][Espiritualidade]
#item("12")[Tendo experimentado um despertar espiritual graças a estes Passos,
  procuramos transmitir esta mensagem aos comedores compulsivos e pôr em
  prática estes princípios em todas as nossas atividades.][Serviço]

#permissao[A permissão para usar os Doze Passos de Alcoólicos Anônimos para
adaptação foi concedida por A.A. World Services, Inc.]

// =====================================================================
= Instrumentos de Recuperação

#block(breakable: false)[
Os Instrumentos de Recuperação nos ajudam a trabalhar os Passos e a nos
recuperarmos do comer compulsivo. Os nove instrumentos são:

#block(above: 1.1em, below: 1.1em, inset: (x: 2mm),
  grid(columns: (1fr, 1fr, 1fr), row-gutter: 3.2mm, align: center,
    ..("Plano alimentar", "Apadrinhamento", "Reuniões",
       "Telefone", "Anonimato", "Escritos",
       "Literatura", "Prestação de serviço", "Plano de ação")
      .enumerate()
      .map(((i, s)) => text(size: 10pt)[
        #text(font: titulo-fonte, size: 7.5pt, weight: "bold", fill: lilas)[#(i + 1)] \
        #smallcaps(s)])))
]

Temos o folheto _Os Instrumentos de Recuperação_ para quem desejar saber mais
sobre o uso dos instrumentos.

#cartao([Pode ser postado durante a leitura dos instrumentos.], ("instrumentos", ""))

== Apadrinhamento

Padrinhos e madrinhas são membros de CCA comprometidos com a abstinência e
com a vivência dos Passos e Tradições, com o melhor de sua habilidade. Para
encontrar um padrinho ou uma madrinha, continue voltando às reuniões para
conhecer os companheiros. Procure alguém com quem você se identifique e que
tenha o que você deseja, e peça a essa pessoa para ser seu padrinho ou sua
madrinha.

Temos os folhetos _Apadrinhando através dos Passos_, _Um guia para padrinhos_
e o _Caderno de estudos dos Passos_, que você pode estudar com seu padrinho ou
sua madrinha.

// =====================================================================
= Abstinência

#block(breakable: false)[
Definição de abstinência aprovada na Conferência Mundial de Serviço de CCA,
em abril de 2021:

#citacao[“Abstinência é a ação de se manter afastado do comer compulsivo e dos
comportamentos alimentares compulsivos, enquanto se trabalha na direção de
atingir ou de manter um peso corporal saudável. A recuperação espiritual,
emocional e física é o resultado de viver e trabalhar o programa de Doze
Passos de CCA numa base diária.”]
]

#cartao(altura: 31mm, [Pode ser postado durante a leitura da definição.], ("abstinencia", ""))

// =====================================================================
= Durante a reunião

Sugestões de procedimentos desejáveis durante a reunião:

#block(above: 1em, below: 1em, inset: (left: 2mm))[
  #set list(marker: text(fill: roxo, size: 8pt)[◆], body-indent: 3mm, spacing: 0.6em)
  #set par(justify: false)
  - Compartilhe apenas a sua experiência.
  - Fale apenas de você, evitando termos como “nós”, “vocês” ou “a gente”.
  - Procure falar sempre na primeira pessoa (“eu”).
  - Não dê conselhos; não discuta nem critique.
  - Não chame quem está coordenando no privado.
  - Procure respeitar o tempo das partilhas.
  - Não dê retornos.
  - Evite falar nome de alimentos.
  - Aconteça o que acontecer, continue voltando.
]

// =====================================================================
= Anonimato

Lembremos sempre:

#todos[
  #versos[
    Quem você vê aqui, \
    o que você ouve aqui, \
    ao sair daqui, \
    deixe que fique aqui.
  ]
]

#cartao(altura: 26mm, [Um dos dois, depois da leitura.], ("anonimato", ""), ("anonimato-lembrete", ""))

// =====================================================================
= Meditações do dia

Vamos às leituras das meditações do dia: _Vozes_ e _Para Hoje_.

#rubrica[Quem tiver o _Caderno de estudos_ pode ler a pergunta do dia.]

== Tempo das partilhas

#cartao(altura: 24mm, [Postar no chat conforme o tempo de cada partilha.],
  ("tempo-5min", "faltam 5 minutos"), ("tempo-1min", "falta 1 minuto"),
  ("tempo-acabou", "tempo esgotado"))

// =====================================================================
= Sétima Tradição

#rubrica[Quem coordena pode pedir a alguém um depoimento de dois minutos sobre
a Sétima Tradição. Em seguida, faz a leitura abaixo.]

De acordo com a nossa Sétima Tradição, “todos os grupos deverão ser
absolutamente autossuficientes, rejeitando quaisquer contribuições de fora”.

As doações são para pagar as despesas do grupo, enviar representantes para os
eventos nacionais, enviar contribuição mensal para a JUNCCAB, fazer panfletos
e levar a mensagem ao comedor compulsivo que ainda sofre.

#align(center, text(style: "italic", fill: roxo)[Doe como se sua vida dependesse disso.])

Se você deseja fazer uma contribuição em gratidão por participar desta
reunião, utilize a conta disponibilizada pela nossa tesoureira:

#block(width: 100%, above: 1em, below: 1.2em, inset: (x: 5mm, y: 3.5mm),
  stroke: 0.5pt + lilas, radius: 2mm, breakable: false)[
  #set text(size: 10pt)
  #grid(columns: (auto, 1fr), column-gutter: 4mm, row-gutter: 2.4mm, align: (right, left),
    ..(("Banco", banco), ("Agência", agencia), ("Operação", operacao),
       ("Conta corrente", conta), ("Titular", titular), ("Pix", pix))
      .map(((k, v)) => (
        text(font: titulo-fonte, size: 7.5pt, weight: "bold", fill: roxo, tracking: 0.15em)[#upper(k)],
        em-branco(v, largura: 50mm)))
      .flatten())
]

Entretanto, a Sétima Tradição não se aplica simplesmente ao sustento
financeiro. Para que possam ser totalmente autossuficientes, grupos e
indivíduos precisam também assumir sua parte nos serviços prestados.

#citacao[“Qualquer forma de serviço, não importa quão pequena, que ajude a
chegar a um companheiro sofredor, contribui para a qualidade da nossa própria
recuperação.”]

#fonte[_Os Doze Passos e as Doze Tradições de Comedores Compulsivos
Anônimos_, \ 3ª impressão, p. 145, 1º parágrafo.]

// =====================================================================
= As Doze Tradições

As Doze Tradições de CCA, com seus princípios espirituais:

#item("1")[Nosso bem-estar comum deve estar em primeiro lugar; a recuperação
  individual depende da unidade de CCA.][Unidade]
#item("2")[Somente uma autoridade preside, em última análise, o nosso
  propósito comum — um Deus amantíssimo que se manifesta em nossa consciência
  coletiva. Nossos líderes são apenas servidores de confiança; não têm poderes
  para governar.][Confiança]
#item("3")[Para ser membro de CCA, o único requisito é o desejo de parar de
  comer compulsivamente.][Identidade]
#item("4")[Cada grupo deve ser autônomo, salvo em assuntos que digam respeito
  a outros grupos ou a CCA em seu conjunto.][Autonomia]
#item("5")[Cada grupo é animado por um único propósito primordial — o de
  transmitir sua mensagem ao comedor compulsivo que ainda sofre.][Objetivo]
#item("6")[Nenhum grupo de CCA jamais deverá sancionar, financiar ou emprestar
  o nome de CCA a qualquer sociedade parecida ou empreendimento alheio à
  Irmandade, a fim de que problemas de dinheiro, de propriedade e de prestígio
  não nos afastem do nosso objetivo primordial.][Solidariedade]
#item("7")[Todos os grupos de CCA deverão ser absolutamente autossuficientes,
  rejeitando quaisquer doações de fora.][Responsabilidade]
#item("8")[Comedores Compulsivos Anônimos deverá manter-se sempre não
  profissional, embora nossos centros de serviços possam contratar
  funcionários especializados.][Irmandade]
#item("9")[CCA jamais deverá organizar-se como tal; podemos, porém, criar
  juntas ou comitês de serviço diretamente responsáveis perante aqueles a quem
  prestam serviços.][Estrutura]
#item("10")[Comedores Compulsivos Anônimos não opina sobre questões alheias à
  Irmandade; portanto, o nome de CCA jamais deverá aparecer em controvérsias
  públicas.][Neutralidade]
#item("11")[Nossas relações com o público baseiam-se na atração em vez da
  promoção; cabe-nos sempre preservar o anonimato pessoal na imprensa, no
  rádio, em filmes, na televisão e em outros meios públicos de
  comunicação.][Anonimato]
#item("12")[O anonimato é o alicerce espiritual de nossas Tradições, lembrando-nos
  sempre da necessidade de colocar os princípios antes das
  personalidades.][Espiritualidade]

#permissao[A permissão para usar as Doze Tradições de Alcoólicos Anônimos para
adaptação foi concedida por A.A. World Services, Inc.]

// =====================================================================
= Avisos

Para comprar literatura, assinar a _Lifeline_, saber os horários das reuniões
(presenciais e on-line) e se informar sobre os eventos nacionais e regionais,
entre no site da Junta de Serviços Gerais de Comedores Compulsivos Anônimos do
Brasil:

#align(center, text(font: titulo-fonte, size: 11pt, weight: "medium", fill: roxo,
  tracking: 0.06em)[#link("https://www.cca.org.br")[www.cca.org.br]])

#rubrica[Anunciar os eventos em andamento: maratona, retiro, convenções ou
assembleia.]

// =====================================================================
= Abstinência de hoje

Agora, quem desejar pode postar:

#todos(rotulo: "no chat")[
  #set text(size: 11.5pt)
  Como está sua abstinência hoje? \
  Qual é seu compromisso para as próximas 24 horas?
]

Quem desejar pode também postar seu e-mail ou telefone, como forma de Décimo
Segundo Passo.

// =====================================================================
= Encerramento

Encerrando, eu gostaria de dizer que as opiniões aqui manifestadas referem-se
a cada membro de CCA individualmente e não representam CCA como um todo. A
opinião oficial de CCA está em nossa literatura.

Encorajamos você a continuar voltando. Se você é recém-chegado, se está
lutando ou se ainda não encontrou a recuperação que procura, por favor, não vá
embora antes que o milagre aconteça.

Lembramos que o estudo dos Doze Passos e das Doze Tradições, ao lado do
apadrinhamento, contribui muito para a recuperação.

== Leitura de encerramento

#rubrica[Pedir a alguém que leia. Se não der tempo, quem coordena lê.]

Aqueles de nós que vivemos este programa não carregamos simplesmente a
mensagem: nós somos a mensagem. Cada dia em que vivemos bem e estamos bem, e
incorporamos a alegria da recuperação que atrai outros que querem o que
encontramos neste programa, ficamos sempre felizes em compartilhar nosso
segredo: o programa de Doze Passos de Comedores Compulsivos Anônimos, que dá
força a cada um de nós para viver bem e estar bem, um dia de cada vez.

== Anonimato

Lembremos do nosso anonimato:

#todos[
  #versos[
    Quem você vê aqui, \
    o que você ouve aqui, \
    ao sair daqui, \
    deixe que fique aqui.
  ]
]

== Compromisso de responsabilidade

#block(breakable: false)[
E o compromisso de responsabilidade de CCA:

#todos[
  #versos[
    Sempre estender a mão e o coração de CCA \
    a todos que compartilham da minha compulsão. \
    Por isso, eu sou responsável.
  ]
]
]

// =====================================================================
= Orações

#rubrica[Encerrar com uma das orações abaixo.]

== Oração do Terceiro Passo

#todos(rotulo: "todos")[
  #set align(left)
  #set par(justify: true)
  Deus, ofereço-me a Ti, para que trabalhes em mim e faças comigo o que
  desejares. Liberta-me da escravidão do ego, para que eu possa realizar melhor
  a Tua vontade. Remove minhas dificuldades, para que a vitória sobre elas
  possa dar testemunho, diante daqueles a quem ajudarei, de Teu poder, de Teu
  amor e de Teu modo de vida. Que eu possa realizar a Tua vontade sempre.
]

== Oração da Unidade — Promessa de CCA

#todos(rotulo: "todos")[
  #set align(left)
  #set par(justify: true)
  Coloco minhas mãos nas suas e, juntos, conseguimos o que jamais
  conseguiríamos sozinhos! Não há mais aquela sensação de desesperança; não
  mais precisamos depender de nossa instável força de vontade. Estamos todos
  juntos agora, estendendo nossas mãos em busca de força e poder maiores que os
  nossos e, ao juntarmos as mãos, encontramos amor e compreensão além de nossos
  mais ardentes sonhos.
]

#pagebreak()
#v(1fr)
#align(center)[
  #heading(level: 2, outlined: false)[Oração da Serenidade]
  #v(4mm)
  #text(font: titulo-fonte, size: 7pt, weight: "bold", fill: roxo, tracking: 0.25em)[TODOS]
  #v(5mm)
  #block(width: 100mm)[
    #set par(justify: false, leading: 0.8em)
    #set text(size: 13pt)
    Concedei-me, Senhor, a serenidade necessária \
    para aceitar as coisas que não posso modificar, \
    coragem para modificar aquelas que posso \
    e sabedoria para distinguir umas das outras.
  ]
  #v(12mm)
  #line(length: 24mm, stroke: 0.7mm + roxo)
  #v(8mm)
  #text(font: titulo-fonte, size: 9pt, weight: "medium", fill: roxo, tracking: 0.2em)[CONTINUE VOLTANDO]
]
#v(1.3fr)
