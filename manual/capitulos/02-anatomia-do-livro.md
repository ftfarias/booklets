# Anatomia do livro

> **A regra que resolve quase tudo:** saber o nome certo é metade do ofício.
> A outra metade é saber que o nome descreve uma **função** — e quase toda
> peça do livro existe para resolver um problema específico de mecânica ou
> de desgaste.

Este capítulo fixa o vocabulário que o manual inteiro usa. Os termos vêm em
**português** e em **inglês**, porque a literatura boa de encadernação está
em inglês e em francês, e porque muito fornecedor e tutorial que você vai
consultar usa o termo estrangeiro sem traduzir.

Uma regra de estilo do manual: **termo consagrado em inglês fica em
inglês.** *Foil*, *swell*, *creep*,
*hollow back*, *red rot*, *onlay*: traduzir prejudica, porque é assim que
aparece na loja e no vídeo. O português vem junto na primeira ocorrência.

---

## Consulta rápida — as palavras do livro

| Português | Inglês | O que é |
|---|---|---|
| **Miolo** | *text block* | O corpo do livro: todas as folhas, sem nada que o encadernador acrescentou |
| **Caderno** | *section*, *gathering*, *signature* | Folhas dobradas e encaixadas umas nas outras, a unidade da costura |
| **Bifólio** | *bifolium*, *fold* | Folha de impressão dobrada ao meio: duas folhas, quatro páginas |
| **Folha**, fólio | *leaf*, *folio* | Uma folha do livro, com suas duas páginas (frente e verso) |
| **Lombada** | *spine*, *back* | O lado por onde o livro é costurado; o que se vê na estante |
| **Goteira** | *fore edge* | O corte da frente, oposto à lombada |
| **Cabeça** | *head* | O corte de cima |
| **Pé** | *tail* | O corte de baixo |
| **Pastas**, tábuas | *boards* | Os cartões rígidos da capa |
| **Capa** | *cover*, *case* | O conjunto que reveste e protege |
| **Guardas** | *endpapers* | As folhas que ligam o miolo à capa |
| — guarda colada | *pastedown* | A metade colada na face interna da pasta |
| — guarda volante | *fly leaf* | A metade solta, que vira como página |
| **Charneira** (externa) | *joint* | O vinco externo entre lombada e pasta, onde a capa articula |
| **Charneira** (interna) | *hinge* | A articulação interna, entre guarda colada e guarda volante |
| **Mordente**, ombro | *shoulder* | A aba formada no encaixe, que acomoda a espessura da pasta |
| **Seixa** | *squares* | A sobra da pasta além do miolo, nos três lados |
| **Virada** | *turn-in* | A sobra do revestimento dobrada para dentro da pasta |
| **Nervura**, nervo | *band*, *raised band* | O relevo transversal da lombada |
| — nervura falsa | *false band* | Relevo só decorativo, colado por cima |
| **Entrenervo** | *panel* | O espaço entre duas nervuras |
| **Cabeceado**, capitel | *headband*, *endband* | O rolinho na cabeça e no pé da lombada |
| **Cabeceira**, coifa | *headcap* | O couro moldado sobre o cabeceado |
| **Canto** | *corner* | O encontro de duas bordas da capa |
| **Lombada oca** | *hollow back* | Tubo de papel entre lombada do miolo e da capa |
| **Medianiz** | *gutter* | As margens internas das duas páginas abertas |

---

## O miolo

### Folha, fólio, caderno

A palavra "folha" serve para duas coisas, e vale separar:

- A **folha de impressão** (*sheet*) — o papel que entra na impressora.
- A **folha do livro** (*leaf*) — cada unidade que se vira ao ler, com uma
  página de cada lado.

Dobrada ao meio, uma folha de impressão vira um **bifólio**: duas folhas
do livro, quatro páginas. Vários bifólios encaixados uns dentro dos
outros formam o **caderno**, que é a unidade da costura.

**Fólio** tem três sentidos, todos registrados por Roberts & Etherington:
uma folha do livro (nos manuscritos e livros antigos, numerada só na
frente — daí "fólio 12 verso"); por extensão, o número da página; e o
**formato in-fólio**, a folha de impressão dobrada uma única vez (cap. 4).

Em inglês o caderno tem três nomes, e a diferença entre eles é sutil e
quase sempre irrelevante na prática:

- ***section*** — o termo neutro, o que o encadernador usa.
- ***gathering*** — ênfase no ato de reunir as folhas.
- ***signature*** — a rigor é a *marca* impressa no pé da primeira página
  de cada caderno, que o alceador usa para conferir a ordem. Por extensão,
  virou sinônimo de caderno. É o termo que o `booklet.py`, o script de
  imposição do estúdio, usa.

O conjunto de todos os cadernos é o **miolo** (*text block*). A definição
de Roberts & Etherington é precisa num ponto que importa: o miolo **exclui
tudo que o encadernador acrescentou** — guardas, reforços, cabeceados. O
miolo é o livro; o resto é a encadernação.

### Os três cortes

O livro fechado tem três cortes, e cada um tem nome:

- **Cabeça** (*head*) — em cima. É o que mais recebe poeira, e por isso o
  primeiro a ser dourado quando se doura um corte só.
- **Goteira** (*fore edge*) — na frente, oposto à lombada. O nome em
  português vem da forma: depois de arredondado, o corte fica côncavo,
  como uma calha.
- **Pé** (*tail*) — embaixo.

O quarto lado é a **lombada**, que não é corte: é a dobra.

> **Barba** (*deckle edge*) — a borda irregular do papel feito à mão,
> formada onde a polpa encontra a moldura da fôrma. Num livro de edição, preservar a barba é
> decisão deliberada: significa não aparar aquele lado.

### Medianiz e margens

A **medianiz** (*gutter*) é o par de margens internas de duas páginas
abertas, junto à dobra. É a margem que o encadernador come: parte dela
desaparece dentro da lombada quando o livro é costurado, e quanto mais
grosso o livro, mais ela some. Por isso o cap. 4 manda
acrescentar 3–4 mm à margem interna em livros acima de ~250 páginas.

---

## A lombada

### O que acontece ali

A lombada (*spine*) é onde o livro trabalha. Cada abertura flexiona a
costura, atrita a linha contra a dobra do papel e empurra o revestimento.
É por isso que quase todas as decisões difíceis do manual — bitola de
linha, tipo de cola, lombada oca ou aderente — se concentram aqui.

### Nervuras

As **nervuras** (*bands*) são os relevos transversais. Historicamente são
os próprios cordões sobre os quais o livro foi costurado, aparecendo por
baixo do couro:

- **Nervura verdadeira** (*raised band*) — o cordão está lá, a costura o
  abraça, e o relevo é consequência estrutural. Tradicionalmente cinco,
  mas o registro histórico vai de duas a catorze.
- **Nervura falsa** (*false band*) — tirinha de couro ou cartão colada por
  cima, só para fazer o relevo. Puramente decorativa.

O espaço entre duas nervuras é o **entrenervo** (*panel*). É onde vão o
título e a decoração.

> Atenção ao falso amigo: *panel* em inglês também nomeia um tipo de
> **decoração** em molduras retangulares, que não tem relação com o
> entrenervo. O contexto resolve.

### Cabeceado e cabeceira

Dois termos que se confundem e são coisas diferentes:

- **Cabeceado** (*headband*, *endband*) — o rolinho listrado na cabeça e
  no pé da lombada, costurado ou colado sobre uma alma. Originalmente era
  estrutural: a costura do cabeceado prendia os cadernos e era laçada nas
  pastas. Hoje, na maior parte dos livros, é ornamental.
- **Cabeceira** (*headcap*) — o **couro** moldado por cima do cabeceado,
  dobrado e conformado com o osso. É o acabamento que protege o topo da
  lombada, e um dos lugares onde o trabalho amador mais se denuncia.

### Lombada oca e lombada aderente

| Português | Inglês | O que é |
|---|---|---|
| Lombada aderente | *tight back* | O revestimento colado direto na lombada do miolo |
| Lombada oca | *hollow back* | Um tubo de papel entre a lombada do miolo e a da capa |

O ***hollow*** propriamente dito é o tubo: kraft dobrado, colado de um lado
no miolo e do outro no revestimento. É o que permite o livro abrir plano
sem rachar o couro. Começa na França no séc. XVIII, com os Derome, e
se generaliza no séc. XIX; a lombada aderente, que até então era quase
universal, declina depois de 1820.

Detalhe que importa em livro grosso: na lombada aderente, o couro flexiona
a cada abertura e a douração dos entrenervos trinca com o tempo. Na oca,
a lombada permanece reta e imóvel enquanto o miolo arqueia.

---

## A capa

### Pastas, seixa, virada

As **pastas** (*boards*) são os cartões rígidos. O termo antigo é *tábuas*,
e era literal — o livro medieval usava madeira.

A **seixa** (*squares*) é a sobra da pasta além do miolo, nos três lados.
Tem duas funções: proteger o corte do papel contra o atrito da estante, e
dar ao livro a proporção visual que o olho espera.

> ⚠️ **Dois avisos sobre "seixa" e "square".**
>
> Em português, parte da literatura — sobretudo de Portugal, e o Tesauro
> da UFRGS — usa **seixa** para outra coisa: o *friso decorativo gravado na
> face interna da capa* — a decoração das viradas, que em inglês se chama
> *inside dentelle*. No uso corrente de oficina no Brasil, seixa é a
> sobra da pasta, e é nesse sentido que o manual a emprega.
>
> Em inglês, só o **plural** *squares* significa a sobra. O singular
> *square* quer dizer o esquadro (a ferramenta), o canto em ângulo reto, ou
> um formato de livro quase quadrado. Pedir "the square of the book" a um
> encadernador anglófono não comunica o que você quer dizer.

Roberts & Etherington registram até uma escala de tamanho de seixa, do
menor para o maior: *pinhead* → *neat* → *ordinary* → *full* → *bold*.

A **virada** (*turn-in*) é a sobra do revestimento dobrada por cima da
borda da pasta e colada por dentro. Em couro, a virada é sempre rebaixada
(*pared*), senão forma um degrau visível sob a guarda colada.

### Charneira: dois lugares, dois nomes

Este é o ponto de vocabulário que mais confunde, e o dicionário da Library
of Congress é explícito a respeito:

- **Charneira externa** — ***joint***. O vinco entre a lombada e a pasta,
  visto por fora. É onde a capa articula.
- **Charneira interna** — ***hinge***. A articulação por dentro, entre a
  guarda colada e a guarda volante.

Roberts & Etherington observam que *joint* é frequentemente usado para a
junção interna, e que **isso é impreciso** — ali o termo correto é *hinge*.
O português sofre do mesmo problema: "charneira" serve para as duas, e só o
contexto distingue. Quando a precisão importa, diga *charneira externa* e
*charneira interna*.

Uma variante com nome próprio: a **charneira francesa** (*French joint*,
também *open joint*) deixa uma folga de 3–6 mm entre a pasta e o mordente,
em vez de encostar. Permite revestimento mais grosso e abertura mais fácil —
é a marca da encadernação de biblioteca.

### Mordente

O **mordente** (*shoulder*) é a aba formada nas bordas da lombada durante o
encaixe (*backing*): o encadernador deita os cadernos em leque, do centro
para as bordas, e os mais externos acabam dobrados em ângulo reto,
formando um degrau. Esse degrau é o berço onde a pasta
assenta.

Sem mordente, a pasta não tem onde se apoiar e o livro abre torto. A altura
do mordente é a espessura da pasta — e esse é o número que liga as duas
etapas: você decide a pasta antes de encaixar.

### Cantos

O **canto** (*corner*) é onde duas bordas do revestimento se encontram. Dois
jeitos de resolver, e eles denunciam o nível do trabalho:

- **Canto de encadernador** (*mitred corner*) — o material é cortado em
  45° e as duas viradas se encontram sem sobrepor. Limpo e fino.
- **Canto de biblioteca** (*library corner*, também *Dutch corner*) — o
  material não é cortado: o excesso é recolhido em duas dobras diagonais,
  uma sob cada virada. Mais resistente e mais grosso; é o canto padrão da
  encadernação de biblioteca americana.

Em meia-encadernação, "cantos" também nomeia as peças triangulares de couro
ou tecido aplicadas sobre os cantos da pasta.

---

## As guardas

As **guardas** (*endpapers*) são as folhas entre a capa e o miolo. Não são
decoração: **são a charneira que segura o livro na capa**, e por isso são o
ponto que mais falha em livro usado.

Cada guarda é um bifólio que se divide em duas metades com nomes próprios:

- **Guarda colada** (*pastedown*) — colada na face interna da pasta. Além
  de prender, ela esconde a virada e **contrabalança a tração** do
  revestimento: sem ela, a pasta empena para fora.
- **Guarda volante** (*fly leaf*) — a metade solta, que vira como página.

Na variante de luxo, a **doublure**, a guarda colada é de couro ou seda.
Os tipos de guarda e como se montam estão no cap. 11.

---

## Como um livro falha

Vale conhecer isto cedo, porque explica metade das decisões do resto do
manual. Os casos mais comuns:

| O que quebra | Por quê | Cap. |
|---|---|---|
| **A charneira** | É onde tudo flexiona. A guarda rasga, ou o revestimento racha no vinco | 11 · 12 |
| **A cabeceira** | Fica no topo, e todo mundo puxa o livro pela cabeça da lombada na estante | 14 |
| **A costura arrebenta** | Linha fina demais, ou linha que serrou a dobra do papel | 8 |
| **A lombada solta** | Cola que perdeu flexibilidade e virou pó | 10 |
| **O papel amarela e quebra** | Papel ácido do séc. XIX–XX se autodestrói | 5 |
| **O couro vira pó** (*red rot*) | Couro de curtimento vegetal, sobretudo do séc. XIX, degradado pela acidez do ar | 14 |
| **As pontas da pasta amassam** | Canto é a parte mais exposta e a menos protegida | 12 |
| **O miolo abre em leque** | Linha que estica, ou swell mal calculado | 8 |

Três padrões se repetem nessa lista:

1. **Falha onde flexiona.** Charneira, lombada, cabeceira. Toda decisão
   sobre essas três peças deve privilegiar flexibilidade, não resistência
   bruta.
2. **Falha o que foi escolhido por conveniência.** Papel ácido, couro mal
   curtido, cola que secava rápido. Em quase todo caso, alguém trocou
   permanência por custo ou velocidade.
3. **A falha é química com a mesma frequência que mecânica.** O livro não
   só se desgasta — ele se autodestrói por dentro. É o que justifica a
   obsessão da conservação com pH e reversibilidade.

> Puxar o livro pela cabeça da lombada é o gesto que mais destrói
> encadernações em uso. O certo é empurrar os dois vizinhos para trás e
> pegar o livro pelo meio das pastas. Vale dizer isso a quem receber um
> livro seu.

---

## Os nomes em francês

O ofício se formou na França, e alguns termos franceses continuam correntes
na literatura — inclusive em textos ingleses:

| Francês | Português | Inglês |
|---|---|---|
| *mors* | charneira externa | *joint* |
| *coiffe* | cabeceira | *headcap* |
| *chasse* | seixa | *squares* |
| *nerfs* | nervuras | *bands* |
| *dos* | lombada | *spine* |
| *dos brisé* | lombada oca | *hollow back* |
| *dos collé* | lombada aderente | *tight back* |
| *gardes* | guardas | *endpapers* |
| *tranchefile* | cabeceado | *headband* |
| *plats* | pastas | *boards* |
| *tranche* | corte (do miolo) | *edge* |
| *coupe* | borda da pasta | *board edge* |

---

## Fontes

- **Roberts & Etherington**, *Bookbinding and the Conservation of Books: A
  Dictionary of Descriptive Terminology* (Library of Congress, 1982) — a
  referência canônica em inglês, 3.861 verbetes.
- **Cida Mársico**, *O surgimento da encadernação e da douração* (Fundação
  Biblioteca Nacional) — glossário em português do Brasil, por conservadora
  da FBN.
- **Ligatus**, *Language of Bindings* — tesauro de encadernação histórica
  (séc. IX ao XIX), em `ligatus.org.uk/lob/`.

Onde as fontes divergiram — o caso de *seixa* — o manual registra as duas
leituras e adota o uso corrente de oficina no Brasil.
