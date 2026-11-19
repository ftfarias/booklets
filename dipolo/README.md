# Dipolo — caderno de anotações e ideias

Presente para **Raphael Ballet**, fundador da [Dipolo AI](https://dipolo.ai).
Primeiro volume por encomenda do projeto, e o primeiro que não é
composição de domínio público: é um **caderno**, majoritariamente em
branco, com aparato impresso.

Material de referência coletado em `referencias/` — marca, paleta, textos
do site e do blog. Comece por [`referencias/MARCA.md`](referencias/MARCA.md).

## O que já está resolvido

**A identidade cai pronta na encadernação.** A paleta da Dipolo é verde
muito escuro (`#0b1512`–`#17362a`) com dourado/areia (`#d9c48e`). Isso é,
literalmente, couro escuro com vinil dourado — o padrão da linha premium.
Nada a traduzir.

**O logo é perfeito para recorte.** Duas formas em espelho, geometria
pura, sem serifa e sem traço fino. Medido a 600 dpi: p10 de 4,1 mm com o
mark a 40 mm de largura, contra um piso de 1,2 mm. Passa com folga de
3,4×. Ver a tabela em `referencias/MARCA.md`.

**Ele escreve à mão para pensar.** Do site: "escrevo para pensar; a
maioria dos posts começa como notas que tomo enquanto depuro algo ou
construo uma empresa." O caderno entra num hábito que já existe. Isso
deveria guiar o projeto inteiro — é um instrumento de trabalho, não um
objeto de vitrine.

## O que falta decidir

Nada disso está fechado; é a pauta da próxima conversa.

### Proporção entre impresso e branco

A tensão central. Um caderno é para escrever — se vier cheio de texto,
deixa de ser caderno. A intuição é **aparato mínimo na frente,
muito branco, e um fecho curto no fim**: nota editorial curta, algumas
páginas de epígrafes, e o resto pautado ou liso.

Vale considerar textos que sejam **dele**: as frases do site são boas e
já estão em `referencias/MARCA.md`. Um caderno que cita o próprio dono
com elegância é mais interessante que um que cita Drucker.

Se for para trazer domínio público de empreendedorismo, o alerta do
`CLAUDE.md` vale: **o gargalo é o português**. Praticamente nada de
"empreendedorismo" está em domínio público em português. O que existe em
PD e presta é mais antigo e mais oblíquo — Sêneca sobre tempo, Marco
Aurélio sobre trabalho, Franklin, Emerson. Verificar ano de morte do
tradutor antes de planejar qualquer coisa.

### Frases — nas GUARDAS, não no miolo

**Mudança de 21/09/2026.** A ideia original (bifólio de verge aninhado no
meio de cada caderno) foi **testada em papel e descartada** — não ficou
bom. As frases passam para as **guardas**, impressas em cor.

Consequências:

- **os 10 cadernos ficam inteiramente em branco** — o caderno vira mais
  caderno, que é o ponto;
- **não há mais bifólio de verge no miolo**, então a lombada perde os
  ~3 mm que eles somavam: bloco de 160 pp volta a ~8,8 mm de papel
  (~12 mm com o swell). Refazer a medida do lombicanto com esse número;
- o verge continua nas guardas, como sempre foi o padrão da casa.

**Estrutura: guarda com reforço de tecido** (*cloth-jointed endpaper*).
Duas folhas A4 impressas separadamente e unidas por tira de tecido na
dobra — `guardas/guarda.pdf`, 2 páginas:

| pág. | face | conteúdo |
|---|---|---|
| 1 | **guarda volante** (*flyleaf*) | as 10 frases, 5+5 em duas colunas |
| 2 | **contraguarda** (*pastedown*) | o logo, sozinho |

A guarda inteira não caberia em A4 (o bifólio é 330×240), mas a solução
não é um contorno: **é estruturalmente melhor que a folha inteira**,
porque a dobra da guarda é o ponto de maior tensão do livro. Medidas,
zona morta sob o tecido e escolha do tecido em `PAPEL_E_ESTRUTURA.md`.

**O desenho é o próprio logo**, grande e em verde muito claro
(`#e8efe9`), como marca d'água — não como carimbo. As duas metades do
mark são espelhadas e não se tocam; esse vazio central é a grade, em vez
de ornamento acrescentado por fora. Numeração em areia (`#b9a06a`),
frases em `forest`.

### Frases — as 10, selecionadas e compostas

**160 pp = 10 cadernos = 10 frases.** Cada caderno leva um bifólio de
verge 120 g aninhado no meio, e a frase cai no meio das 16 páginas em
branco. Todas do próprio Raphael (site, blog) — critérios e reservas em
`raw/frases.md`.

Composto: `make check` → `frases.pdf`, 20 pp (10 frases + versos em
branco), 165×240 mm. Tipografia **Newsreader** itálico (a serifa do site
dele) com a numeração `01–10` em **Hanken Grotesk** (a sem-serifa do
site) — as duas OFL, em `fonts/`. A numeração em duas casas ecoa o
maneirismo `01–04` do site da Dipolo.

**Idioma — resolvido: só português.** As dez frases existem nos dois
idiomas (o site é integralmente bilíngue), mas ele é brasileiro — o
português é a língua dele. As versões inglesas ficam registradas em
`raw/frases.md` caso a decisão volte atrás.

### Pauta

Liso, pautado, pontilhado ou quadriculado. Quem escreve código e desenha
arquitetura costuma preferir **pontilhado** — serve para texto e para
diagrama. A decidir com ele, se for possível perguntar sem estragar a
surpresa.

### Encadernação — decidida

**Hollow back + lombicanto** (couro na lombada e cantos, campo central em
tecido ou papel). Hollow back abre plano, que é requisito de caderno; o
lombicanto protege onde o desgaste acontece e deixa o campo central limpo
para o logo em dourado. Ver `PAPEL_E_ESTRUTURA.md`.

### Formato e papel — resolvidos

**Eco Millennium Bignardi 180 g/m²**, folha medida 660×480 mm, 0,22 mm por
folha. **Cortada ao meio + 2 dobras** → caderno de 16 pp, página
**240×165 mm** (~236×161 refilada). Cada folha dá 2 cadernos.

Cortar antes de dobrar reduz a lombada de 8 para 4 camadas e elimina o
risco de rachadura que a gramatura alta trazia. **Fibra testada em 18/09/2026:
corre no lado de 480 mm — formato confirmado.** Linha: **rami 0,5 mm**
(a Galaces 0,8 mm engorda demais a lombada de um bloco fino). Cola: **PVA neutro de
encadernação a comprar** — o Cascorez Extra disponível tem pH 4–5 e
migraria acidez para as dobras. Tubo do hollow em **kraft 80 g** (o disponível serve), fibra no comprimento. Tight back considerado e descartado.

## Estrutura pretendida

Segue o padrão dos outros volumes (`build.py` → `typst/` → `check.py`,
com `make check`), mas o `check.py` aqui verifica outras coisas: contagem
de páginas, que as páginas em branco estejam mesmo em branco, e que o
aparato impresso não tenha vazado marcação.

```
dipolo/
  referencias/            marca, paleta, sites arquivados  [pronto]
  PAPEL_E_ESTRUTURA.md    formato, dobras, hollow back      [pronto]
  raw/frases.md           as 10 frases + critérios          [pronto]
  typst/                  composição das frases             [pronto]
  fonts/                  Newsreader + Hanken Grotesk (OFL) [pronto]
  build.py check.py Makefile                                 [pronto]
  frases.pdf              20 pp, 165×240 mm                 [pronto]
  cover/                  recorte do vinil + check_vinyl    [a fazer]
```
