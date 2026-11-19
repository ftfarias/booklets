# Booklets — guia do projeto

Livros artesanais em edições pequenas: textos em domínio público,
compostos em Typst, impressos em casa e encadernados à mão.

Cada volume vive no seu diretório (`plato_3_dialogs/`, `Estoicos1/`,
`Vulgata/`). O `booklet.py` na raiz é ferramenta compartilhada, com
documentação própria no `README.md`.

Este arquivo registra o que já foi decidido e o que já deu errado, para
não redescobrir. Não é regra rígida — é o padrão da casa.

## Intenção

Livros artísticos, feitos à mão, passíveis de personalização. **2026 é
ano de treino** — experimentar materiais e processos, errar barato,
acumular repertório. A partir de 2027, trabalho mais profissional.

Duas consequências práticas para qualquer decisão neste projeto:

- **Qualidade é inegociável.** Papel, fonte, corte, tradução, revisão —
  cada aspecto pensado, nada por inércia ou conveniência. Se algo está
  aceitável mas não bom, é para refazer. Isso vale material por
  material: **couro legítimo, o melhor papel, a melhor cola, a melhor
  linha** — não a versão que dá para o gasto. Quando houver escolha
  entre o correto e o conveniente, o padrão é o correto.
- **Não restringir possibilidades cedo demais.** Quando houver dúvida
  entre dois materiais ou métodos, o padrão é **testar os dois**, não
  escolher no papel. Ver `TESTES.md`.

Ao comparar, **fixe tudo menos uma variável** e registre as condições no
momento do teste.

### Formação

**2026 é o ano de aprender encadernação; restauração vem em seguida** —
em curso com **Liege Monteiro**, restauradora com mais de 30 anos de
experiência, de quem a intenção é aprender tudo que der. Restauro e
encadernação artística são **dois caminhos desejados, não alternativos**;
qual sustenta o negócio ainda é pergunta aberta (`CAMINHOS.md`).

Consequência para as decisões técnicas: quando encadernação artesanal e
conservação divergirem, o padrão é o **lado da conservação** —
reversibilidade, pH neutro, materiais com histórico comprovado.

Direções em aberto (restauração, formas de venda, nichos) estão em
`CAMINHOS.md`; experimentos e encomendas, em `TESTES.md`; preços de
mercado, investimento/retorno e fontes de dados, em `MERCADO.md`. A pesquisa de
referência sobre o ofício está em `manual/`.

### Duas linhas

- **Linha premium** ("Uber Black") — couro, vinil dourado ou douração,
  peça única. Vocabulário visual inspirado em **Pierre Legrain e Rose
  Adler**: geometria contida, aresta seca, ouro sobre superfície lisa,
  composição assimétrica, nada decorativo que não signifique algo.
  Inspiração, **não pastiche** — o vocabulário é ponto de partida.
- **Linha simples** — tecido, vinil, materiais mais acessíveis e processo
  mais rápido. **Mesmo rigor**: mesma tipografia, mesma geometria, mesma
  qualidade de execução. Não é "a versão barata"; é a mesma direção de
  arte em outra encadernação.

A premium desenvolve vocabulário; a simples é o que se paga. Tecido tem
uma vantagem prática para tiragem: **repetibilidade** — couro varia de
peça para peça, tecido não.

---

## Ferramentas

- **Typst 0.15.1** (via Homebrew) para composição.
- **Libertinus Serif** para miolo — vem com o Typst e tem grego
  politônico excelente. É a fonte padrão de todos os volumes.
- **Python 3 + pypdf** para imposição e verificações.
- **Epson L4360** (tanque de tinta, duplex automático) para impressão.
- **Silhouette Cameo** + vinil termoadesivo para capas.
- **Cricut EasyPress Mini** para a transferência.

---

## Fontes de texto

Só domínio público. Antes de adotar uma tradução, confirme o ano de morte
do tradutor — no Brasil o prazo é 70 anos.

Fontes que já funcionaram:

- **Project Gutenberg** — traduções inglesas antigas.
- **Perseus `canonical-greekLit`** (GitHub) — grego em TEI XML.
- **`emilekm2142/vulgate-bible-full-text`** — Vulgata Clementina em JSON.
- **`thiagobodruk/bible`** (`pt_aa.json`) — Almeida em português.

### Armadilhas já encontradas

- **Português é o gargalo.** Muitas traduções que parecem antigas ainda
  estão em copyright. No Platão isso eliminou dois dos três diálogos; nos
  Estoicos eliminou o português inteiro. Verifique antes de planejar.
- **OCR de textos anteriores a 1800** costuma vir destruído pelo *long-s*
  (`ſ`): "Difcourfes", "necefTary". Inutilizável sem revisão manual pesada.
- **Scrapers deixam lixo**: versículos vazios, marcadores de estrofe
  (`[`, `]`), zeros no lugar de letras. Sempre conte e inspecione antes
  de confiar.
- **Erros pontuais da fonte** merecem tabela de errata no build, que
  **falha se o erro sumir** — assim ela não envelhece em silêncio.
  Ver `Vulgata/build.py`, `PT_ERRATA`.

---

## Composição em Typst

### Estrutura

Um `.typ` mestre por volume, importando `helpers.typ`, mais fragmentos
gerados por um `build.py` a partir de `raw/`.

**Fragmentos precisam de `#import "helpers.typ": *` no topo.** O
`#include` do Typst **não** compartilha o escopo de `let` do pai. Essa
pegadinha já custou tempo em dois projetos.

### Armadilhas do Typst

- **`*texto*` é negrito, não itálico.** Itálico é `_texto_`. Passou
  despercebido por vários builds na Vulgata.
- **`#align(center)` externo vaza** para dentro de parágrafos
  justificados e centraliza a última linha de cada um. Corrija com
  `#set align(left)` dentro do bloco.
- **`counter(page).final()` para calcular preenchimento não converge** —
  as páginas adicionadas realimentam a contagem e o Typst oscila. Use um
  `#let PAD` fixo e deixe o `check.py` verificar o total.
- **`inside`/`outside` alternam por paridade de página.** Correto para
  códice dobrado, **errado para costura japonesa**, que fura todas as
  folhas pela mesma borda. Nesse caso use `left`/`right`.

### Densidade de texto (medida, não estimada)

Medido no PDF compilado com `extract_text()`, só páginas de corpo:

| formato | corpo | palavras/página |
|---|---|---|
| A5 retrato, prosa corrida (Estoicos) | 10,5 pt | **433** |
| A4 paisagem, 2 col. paralelas (Vulgata) | 11,5 pt | **503** |

O segundo número soma as **duas** colunas (latim + português), então não
é comparável direto ao primeiro — para bilíngue, o que importa é o total
de palavras de ambos os idiomas.

**Meça, não estime.** O projeto dos Estoicos começou com 256
palavras/página estimadas — errado por ~1,7×. E a linha da Vulgata acima
foi estimada em 390 antes de eu medir e achar 503.

### Largura de coluna

60–70 caracteres por linha (45–75 aceitável). Regra prática, **medida** na
Libertinus: caracteres ≈ largura da coluna em mm ÷ (0,42 × corpo em pt ×
0,353). A letra média ocupa ~0,42 em, em português e em latim.

| coluna | corpo | caracteres/linha (medido) |
|---|---|---|
| 110 mm (A5) | 10 / 10,5 / 11 pt | 73 / 70 / 67 |
| 115 mm (Vulgata, A4 paisagem 2 col.) | 11,5 / 12 pt | 68–69 / 65–66 |

A versão anterior desta regra usava 0,48 em e previa ~58 caracteres para a
Vulgata a 11,5 pt — subestimava em ~15%. Medido em nov/2026 compondo texto
real (Eclesiastes, latim e português) e contando as linhas no PDF.

---

## Verificação

Todo volume tem um `check.py` que roda com `make check`. Ele confere no
**PDF compilado**, não no fonte:

- contagem de páginas compatível com a encadernação;
- tamanho de página e uniformidade;
- presença de passagens-marco (início e fim de cada obra);
- errata aplicada;
- nenhuma marcação de build vazada para o texto.

**O check tem que ser testado.** Quebre algo de propósito e confirme que
ele reprova. Um check que nunca falha não vale nada.

Ao buscar texto extraído de PDF, **normalize os espaços** — o extrator
insere quebras de linha no meio das frases e sondas ingênuas dão falso
negativo.

---

## Papel

**Pólen Bold 90 g/m²** é o padrão para miolo.

- Não-revestido: absorve tinta de jato de tinta corretamente.
- Tom marfim, melhor que o branco-azulado do sulfite para leitura.
- Opacidade alta o bastante para frente e verso.
- ~0,13–0,14 mm por folha (sulfite comum é 0,115).

**Couché não serve** — a camada de caulim sela a superfície e a tinta
aquosa borra. Só as versões específicas "para inkjet" funcionam.

**Vergê** para folhas de guarda.

**Munken Print Cream 80 g/m²** é a alternativa de nível acima: papel de
miolo de livro europeu, off-white cremoso, com *bulk* alto — não fica
fino nem transparente apesar da gramatura baixa. Difícil de achar em
folha avulsa no Brasil; a Ipsis (gráfica editorial em SP) trabalha com
ele. **A comparar diretamente com o Pólen** — ver `TESTES.md`.

Antes de comprar resma, imprima **uma folha** frente e verso: confira
espalhamento da tinta, transparência contra a luz, e borrão ao passar o
dedo depois de 1 minuto. A L4360 é tanque de tinta e deposita mais que
impressora de cartucho; se borrar, baixe a densidade no driver.

---

## Encadernação

Três métodos já usados, com exigências diferentes.

**Sentido da fibra antes de tudo:** paralelo à lombada, em toda peça.
Teste com tiras molhadas ou de flexão; resma A4 costuma vir com a fibra
no lado longo (ver Quarto, abaixo).

### Costura japonesa (*yotsume toji*) — Estoicos, Vulgata

Folhas **empilhadas** e costuradas pela margem, sem dobra.

- **Sem imposição.** Não há cadernos, nem ordem de dobra, nem
  espelhamento. Empilha na ordem e fura.
- Contagem de páginas só precisa ser **par**, não múltiplo de 4.
- Margem interna generosa: os furos ficam a 15 mm e a costura ocupa até
  ~22 mm. Use 20 mm em A5, 32 mm em A4.
- Margem larga **do mesmo lado em todas as páginas** (ver armadilha do
  `inside`/`outside` acima).
- Furos: broca de **1,5 mm** na Dremel como furadeira de bancada. Fure o
  bloco inteiro de uma vez, entre **duas** tábuas de sacrifício — sem a
  de baixo a última folha lasca.
- Linha encerada, comprimento ~4× a altura do bloco.

### Sela (saddle stitch) — Platão

Cadernos aninhados, exige imposição via `booklet.py`.

- Contagem **múltipla de 4**.
- `booklet.py` assume páginas **A5 retrato** 2-up numa A4 paisagem.
  Páginas em paisagem seriam escaladas para 71% — não use.
- No Adobe Reader, os nomes das bordas são invertidos: use
  `--long-edge`. Sempre teste uma folha antes.

---

### Quarto (A6, duas dobras) — Devocionário

Quatro páginas A6 por face de A4, dobrada duas vezes; dois quartos
aninhados = caderno de 16 páginas. Imposição com `quarto.py` (raiz), que
**deriva** a ordem simulando as dobras.

- **Resolve a fibra.** Resma A4 vem com fibra paralela ao lado de 297 —
  **errada** para a dobra A4→A5 (verificado: Pólen Bold e Opalina). No
  quarto, a segunda dobra (a lombada) corre **com** a fibra.
- A primeira dobra fica na cabeça e é **aberta a faca** depois de costurar;
  pé e goteira são as bordas já cortadas da folha — quase nada a refilar.
- Pé e goteira caem na borda da A4: a L4360 não imprime os ~3 mm
  externos, margens nunca abaixo de ~6 mm.
- Dobrar sempre do mesmo jeito (`quarto.py --test`): página 1 **para
  baixo** na mesa, metade direita sobre a esquerda, metade de cima para
  baixo.

## Capas em vinil recortado

Vinil termoadesivo dourado sobre couro escuro. Restrições reais de
produção, não de estética:

- **Fonte com serifa não serve.** Serifas finas e contraste alto entre
  traço grosso e fino arrancam junto com o refugo. Use **Futura** ou
  outra geométrica de espessura uniforme. (O miolo continua em
  Libertinus — são peças diferentes.)
- **Piso de 1,2 mm** para qualquer traço. A aparência na tela não diz
  nada: um rascunho que parecia bom tinha traços de 0,5 mm.
- Verifique medindo: `cover/check_vinyl.py` na Vulgata rasteriza a
  600 dpi e mede a geometria real. Use o **percentil 10** das larguras,
  não o mínimo — o mínimo pega antialiasing das curvas.
- **Descascar achata a hierarquia**: tudo fica grosso e o conjunto vira
  uma lista cinza. Quando isso acontecer, **remova elementos**, não
  diminua — diminuir devolve o traço para baixo do piso.
- **Espelhe o arquivo** (HTV corta-se pelo verso). Conferência: o título
  tem que estar ilegível na tela.
- Typst com `--format svg` exporta contornos reais, sem elementos de
  texto — o Silhouette Studio não precisa da fonte instalada.

### Transferência

- **EasyPress Mini tem presets de ~130/155/205 °C.** Mesmo o mais baixo
  passa dos 110–120 °C que o couro pede. Compense com pano de proteção
  grosso e passadas curtas de 5–8 s, não mudando o preset.
- Descolagem a frio. Teste em sobra antes.
- **Cera microcristalina só depois da transferência.** Ela deixa película
  hidrofóbica — couro encerado é exatamente o caso em que o adesivo não
  pega. Ordem: couro limpo → transfere → 24 h → encera.

---

## Convenções editoriais

- **Original ao lado da tradução**, em páginas ou colunas paralelas — é
  elegante e deixa o leitor apreciar os dois. "Original" é a língua em que
  o texto nasceu ou foi rezado (a Novena do Padre Pio vai em italiano).
  Para a Bíblia, a **Vulgata** faz as vezes de original: hebraico,
  aramaico e grego são difíceis demais para o leitor, e o latim tem o peso
  histórico (*quid latine dictum, altum videtur*).
- **Colofão** ao final, com crédito "Compilado e encadernado à mão por
  Felipe de Toledo Farias" e o estado de domínio público dos textos.
- **Mote em latim ou grego** no colofão, específico do volume.
- **Nota editorial** no início explicando fontes e escolhas de tradução —
  incluindo divergências interessantes (ex.: `caritas` → "amor" na
  Vulgata).
- **Introdução breve** contextualizando os textos e por que estão juntos.
- Preferir o fato ao lugar-comum: a Vulgata não foi encomendada inteira
  pelo papa, e dizer isso é mais interessante que repetir a lenda.
