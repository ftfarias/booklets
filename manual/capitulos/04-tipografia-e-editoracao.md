# Tipografia e editoração

> **A regra que resolve quase tudo:** escolha a medida de linha primeiro
> (60–70 caracteres) e derive dela o corpo, a entrelinha e o formato. Todo
> o resto é ajuste fino.

## Consulta rápida — os números que se usa toda hora

| Parâmetro | Valor | Observação |
|---|---|---|
| Caracteres por linha | **60–70** (45–75 aceitável) | O parâmetro-mestre |
| Corpo / entrelinha | 10,5/14 ou 11/15 pt | Depende da altura-x da fonte |
| Entrelinha de corpo (Word/Affinity) | 1,15–1,5 | Linha mais longa pede mais |
| Entrelinha de título grande | 0,9–1,1 | Em corpo grande o padrão vira buraco |
| Recuo de parágrafo | 1–1,5× o corpo (≈5 mm) | Sem recuo no 1º parágrafo do capítulo |
| Margens (proporção canônica) | interna : sup. : ext. : inf. = **2 : 3 : 4 : 6** | Van de Graaf / Tschichold |
| Sobra de lombada (*gutter*) | +3–4 mm acima de ~250 pp | Erro nº 1 do primeiro livro |
| Fibra do papel | **paralela à lombada**, sempre | Vale mais que qualquer decisão tipográfica |
| Sangria de refile | 3–4 mm nas três faces | Se pretende guilhotinar |

### Receitas de margem prontas

| Formato | Interna | Superior | Externa | Inferior | Mancha |
|---|---|---|---|---|---|
| 14 × 21 cm | 16 mm | 18 mm | 19 mm | 22 mm | 105 × 170 mm |
| A5 (148 × 210), Libertinus | 17 mm | 17 mm | 19 mm | 22 mm | ≈112 × 171 mm |
| 145 × 204 refilado (ver adiante) | 15 mm | 16 mm | 18 mm | 22 mm | 112 × 166 mm |
| 13,5 × 21 (Carta dobrada) | 15 mm | 16 mm | 19 mm | 22 mm | 101 × 172 mm |

As receitas seguem a **ordem** do cânone — interna < superior < externa <
inferior — mas comprimida: o cânone puro de Van de Graaf reserva só 2/3 da
página para a mancha, o que gasta papel demais num livro de uso. Num livro
grosso que não abre plano, some a sobra de lombada à interna.

### O critério, quando a tabela não cobre

- **A margem de baixo é a maior.** A mancha fica acima do centro
  geométrico, porque o olho percebe o centro óptico mais alto — e porque
  as mãos ocupam a parte de baixo.
- **Margens espelhadas**, sempre: a página par é o espelho da ímpar, não
  a cópia.
- **Se as margens parecem grandes demais, provavelmente estão certas.**
  Margem generosa é o que faz um miolo respirar; margem apertada e igual
  nos quatro lados é a assinatura visual da apostila.
- Fonte clara ou papel absorvente? Suba o corpo, não o peso. Semibold em
  texto corrido fica pesado e errado.

---

## Parte I — Fundamentos de tipografia

### O mito da serifa

"Serifa é mais legível no papel, sem serifa na tela" é folclore. Nasceu
quando telas tinham resolução baixíssima e não desenhavam detalhes finos.
A pesquisa de legibilidade é inconclusiva: o que pesa é **familiaridade**
(lê-se melhor o que se está acostumado a ler) e o **desenho específico**
daquela fonte, não a categoria dela.

Esqueça a regra e olhe para o que conta de verdade.

### O que realmente conta numa fonte

| Atributo | O que é | Por que importa |
|---|---|---|
| **Altura-x** | Altura das minúsculas sem haste (`x`, `o`) em relação às maiúsculas | Altura-x grande aguenta corpo pequeno: a Garamond em 11 pt parece bem menor que a Literata em 10,5 |
| **Contraste de traço** | Diferença entre partes grossas e finas | Contraste altíssimo (Didot, Playfair) é lindo grande e desastroso em corpo 10 |
| **Abertura** | Quanto as letras "abrem" no `c`, `e`, `a`, `s` | Helvetica/Arial quase fecham — as letras ficam parecidas. Humanistas (Frutiger, Myriad, Source Sans) diferenciam melhor |
| **Diferenciação de caracteres** | — | Teste: digite `Illegal 1O0`. Se `I`, `l` e `1` forem idênticos, a fonte exige atenção do leitor. Arial e Helvetica falham; Verdana e Inter passam |

### Título vs. texto — a distinção que muda tudo

A ideia mais útil de toda a tipografia, e quase desconhecida fora da área:
**fontes são desenhadas para tamanhos específicos.**

| | Display / Títulos | Text / Corpo |
|---|---|---|
| Contraste | Alto, detalhes finos | Moderado, traços firmes |
| Espaçamento | Apertado (letras grandes se sustentam) | Aberto, generoso |
| Personalidade | Pode ser marcante, peculiar | Discreta, "invisível" |
| Objetivo | Chamar atenção em 2 segundos | Não cansar em 20 minutos |

Consequências:

- Fonte muito expressiva funciona em título e cansa no texto. Geométricas
  (Montserrat, Poppins, Futura) têm `o`, `c`, `e` quase idênticos — ótimo
  num cabeçalho de 3 palavras, exaustivo num parágrafo de 300.
- Fonte de texto em título não erra, mas não brilha.
- Se o nome traz "Display", "Deck", "Caption" ou "Text", a família já tem
  cortes ópticos separados — use-os.

### Como combinar duas fontes sem errar

Três caminhos, do mais seguro ao mais ousado:

1. **Uma família só, pesos diferentes.** Corpo em Regular, título em Bold.
   Impossível de errar. Contraste de peso resolve mais que contraste de
   fonte.
2. **Uma superfamília** (IBM Plex, Source, Noto, Roboto): serif, sans e
   mono desenhadas juntas, harmonia garantida.
3. **Contraste claro.** Serifada + sem serifa, ou expressiva + neutra. A
   regra: bem diferentes, mas do mesmo *humor*. Duas fontes
   parecidas-mas-não-iguais criam desconforto (parece erro); duas de
   épocas opostas brigam. Procure algo em comum — altura-x similar, mesma
   sensação de época.

**O limite:** duas fontes, três no máximo. Se sentir falta de uma quarta,
o problema é a hierarquia, não a variedade.

### Ajustes que fazem mais diferença que a fonte

- **Comprimento da linha.** Uma A4 com margens estreitas em 11 pt dá ~100
  caracteres por linha — o olho se perde na volta. Aumente as margens ou
  use duas colunas.
- **Alinhamento.** Esquerda é sempre seguro. Justificado **só com
  hifenização ligada** — sem ela cria-se rios de branco, e fica pior que
  alinhado à esquerda. Centralizado serve para 1–2 linhas, nunca para
  parágrafos.
- **Nunca os dois espaçamentos juntos.** Ou recuo na primeira linha, ou
  espaço entre parágrafos. Em livro de texto corrido, usa-se recuo; em
  livro de consulta — como este manual —, espaço entre parágrafos ajuda a
  achar o trecho.
- **MAIÚSCULAS precisam de respiro** — aumente o espacejamento entre
  letras quando usar caixa-alta.
- **Nunca negrito ou itálico "falsos".** Se a família não tem o corte, o
  programa inclina/engorda por software e deforma. Use famílias completas.

### Fontes para miolo de livro (gratuitas e boas)

| Fonte | Caráter | Peso na página | Melhor para |
|---|---|---|---|
| **Libertinus Serif** | Erudito, sóbrio, neutro-quente | Leve | Ensaio, clássicos, texto com grego/notas |
| EB Garamond | Histórico, delicado | Muito leve | Literatura, poesia, séc. XVI–XVIII |
| Literata | Contemporâneo, robusto | Médio-forte | Prosa longa, leitura confortável |
| Source Serif 4 | Neutro, técnico | Médio | Não-ficção, qualquer coisa |
| Alegreya | Caloroso, com personalidade | Médio | Ficção, narrativa |
| Vollkorn | Caloroso, "sabor" de livro | Médio | Prosa |
| Crimson Pro | Bonita, mas leve | Leve | Pede corpo um pouco maior |
| Junicode | Filológica | Médio | Textos antigos, medievais |
| Spectral / Newsreader | Modernas, versáteis | Médio | Uso geral |

**Evite para miolo:** contraste altíssimo (Playfair, Didot, Cormorant) —
em corpo 10,5 os traços finos somem ou ficam cinzentos na impressão.

Para **grego politônico** gratuito e bem desenhado: EB Garamond, Cardo,
Brill (livre para uso não comercial), Junicode, Libertinus Serif, GFS
(Didot, Porson).

### Libertinus Serif em detalhe

*É a fonte padrão dos livros do estúdio, inclusive deste manual. O que
segue é o porquê e os cuidados.*

Fork do Linux Libertine iniciado em 2012 por Khaled Hosny; manutenção com
Caleb Maclennan desde 2020, licença OFL. O Linux Libertine original foi
concebido por Philipp Poll como alternativa livre ao Times, mas o desenho
é inspirado em tipos de livro do século XIX — humanista/transicional,
ligeiramente caligráfico. Mais quente que Times, mais neutra que Garamond.

A família traz **Serif** (Regular, Semibold, Bold × 2 estilos),
**Serif Display** (otimizada para corpos grandes), **Serif Initials**
(capitulares), além de Sans, Mono, Math e Keyboard.

**Pontos fortes:**

1. **É econômica em largura** — o argumento decisivo para A5. Medido
   compondo texto corrido em português numa mancha de 110 mm: **73
   caracteres por linha a 10 pt, 70 a 10,5 pt e 67 a 11 pt**. De 10,5 a
   11 pt cai exatamente na faixa ideal. Fonte mais larga obrigaria a
   descer o corpo, e o livro ficaria com cara de manual.
2. **OpenType real e completo:** versaletes verdadeiros (`smcp`),
   maiúsculas→versaletes (`c2sc`), algarismos antigos (`onum`),
   tabulares/proporcionais, ligaduras, conjuntos estilísticos.
3. **Mais de 2.000 glifos** — grego, cirílico, hebraico, latim com
   macrons, guilhemets « ». Para clássicos em domínio público isso é ouro.
4. **Tem Display e Initials**, raríssimo entre gratuitas. Use a Display na
   folha de rosto e nos títulos; as Initials dão capitulares.

**Onde cobra o preço:**

- **O Regular é levinho.** A cor da página tende ao cinza claro. Três
  mitigações: (a) não desça de 10,5 pt em texto corrido; (b) papel pólen ajuda, porque a
  leve absorção engorda o traço — muito melhor que sulfite branco liso;
  (c) faça o teste impresso antes de fechar o corpo. Não use Semibold em
  texto corrido.
- **O itálico é o elo mais fraco** — genuíno e bonito, mas com
  espacejamento menos polido, estreito e caligráfico. Ótimo para ênfases;
  inspecione se houver páginas inteiras em itálico.
- **O Bold é escuro e contrastado.** Prefira Semibold onde usaria negrito
  (títulos, cabeços, folha de rosto). Fica bem mais elegante.
- **Tem "cara de LaTeX"** para quem convive com LaTeX — é a mais
  associada a documento acadêmico livre, e a Linux Libertine original é a
  fonte do logotipo da Wikipédia. Quem não é do
  meio não nota; quem é, reconhece na hora. Registro emocional: erudito,
  sóbrio, editorial. Menos indicada para algo lírico ou sensual.
- Kerning irregular em pares raros; Semibold Italic e Bold Italic são as
  instâncias menos refinadas. Revise títulos e linhas em destaque.

**Instalação:** o Typst já traz a Libertinus embutida — instalar só
importa para outros programas. Nesse caso, baixe dos releases oficiais do
GitHub (`alerque/libertinus`, série 7.0x). Não pegue de agregadores de fontes, que distribuem versões
antigas. **Se tiver Linux Libertine O instalado, desinstale** — conviver
com as duas famílias gera conflito de nomes e você compõe com a errada sem
perceber.

Se ela parecer clara demais no teste impresso, a substituição mais indolor
é **Literata ou Source Serif 4** — ambas mais escuras e sem exigir
rediagramação.

---

## Parte II — Editoração para impressão caseira

### 1. Texto-fonte: de onde tirar

Em ordem de qualidade:

| Fonte | Comentário |
|---|---|
| **Standard Ebooks** | De longe o melhor. Voluntários revisam textos do Gutenberg com tipografia corrigida, aspas tipográficas, itálicos, semântica. Só em inglês |
| **Project Gutenberg** | Enorme, qualidade variável. Prefira HTML a TXT |
| **Wikisource** (inclusive pt) | Revisado colaborativamente contra o fac-símile |
| **Domínio Público (MEC)** e **Brasiliana Mindlin (USP)** | Literatura brasileira. Muito PDF escaneado → OCR e trabalho manual |

Para grego, o **Perseus** (`canonical-greekLit`, no GitHub) dá o texto em
TEI XML, limpo e estruturado.

**Armadilhas já encontradas nos livros do estúdio:**

- **Português é o gargalo.** Muita tradução que parece antiga ainda está
  em copyright — o prazo conta da morte do **tradutor**, não do autor
  (ver "domínio público", adiante). Verifique antes de planejar o volume.
- **OCR de textos anteriores a 1800** costuma vir destruído pelo *s*
  longo (`ſ`): "Difcourfes", "necefTary". Inutilizável sem revisão pesada.
- **Scrapers deixam lixo**: versículos vazios, marcadores soltos, zeros no
  lugar de letras. Conte e inspecione antes de confiar.
- **Erro pontual da fonte** merece uma tabela de errata no script de
  montagem, que **falha se o erro sumir** — assim ela não envelhece em
  silêncio.

### 2. Limpeza — 70% do trabalho, e ninguém avisa

Antes de pensar em fonte:

- Remover cabeçalhos/rodapés de licença, números de página soltos e
  marcações de scan
- Trocar `"aspas retas"` por aspas tipográficas, `'` por `’`
- Converter hífen usado como travessão em travessão (—) ou meia-risca (–)
- Eliminar hífens de quebra de linha do OCR (`compa-\nnheiro`)
- Espaços duplos → simples; remover espaço antes de pontuação
- Padronizar reticências para o caractere único (…)
- Reconstruir itálicos que o TXT perdeu (`_underscores_`)
- Corrigir OCR clássico: `rn`→`m`, `l`→`1`, `0`→`O`, `ﬁ`→`fi`

**Faça com busca e substituição por expressão regular, não à mão.** Um
editor simples (VS Code, Sublime) resolve em minutos o que levaria horas
no Word. Vale aprender três ou quatro regex.

**E decida sua política editorial por escrito.** Vai modernizar
ortografia? Manter "pharmacia"? Padronizar diálogos? Escreva as regras,
porque na página 200 você não vai lembrar o que decidiu na 20.

### 3. Formato

Os formatos de livro não foram inventados por designers: são o resultado
de **dobrar uma folha grande**.

| Nome | Dobras | Páginas/folha | Aspecto |
|---|---|---|---|
| In-fólio | 1 | 4 | Grande, alongado |
| In-quarto (4º) | 2 | 8 | Médio-grande, mais quadrado |
| In-oitavo (8º) | 3 | 16 | O "livro normal" |
| In-dezesseis (16º) | 4 | 32 | Bolso |

Um in-oitavo do século XVIII e um romance de hoje têm tamanho parecido
por essa razão: os dois saem de uma folha grande dobrada três vezes. Imprimindo em A4, você trabalha em **in-fólio** —
o que na tradição seria folha grande, mas aqui produz livro de tamanho
normal, porque se começa pequeno.

#### Formatos comerciais brasileiros

| cm | Uso típico |
|---|---|
| 10,5 × 15 / 11 × 18 | Bolso |
| 12 × 18 | Poesia, ensaio curto |
| **13,5 × 20,5** | Ficção — o mais comum de todos |
| **14 × 21** | Ficção e não-ficção geral — o "padrão" |
| 15,5 × 22,5 / 16 × 23 | Acadêmico, técnico |
| 17,5 × 25 / 18 × 25 | Didático, ilustrado |
| 21 × 28 (quase A4) | Arte, fotografia |
| 20 × 20 / 23 × 23 | Infantil, catálogo |

#### Série ISO — proporção fixa 1:1,414

| | mm |
|---|---|
| A4 | 210 × 297 |
| A5 | 148 × 210 |
| A6 | 105 × 148 |
| B5 | 176 × 250 |
| B6 | 125 × 176 |

#### Anglo-saxões (se usar impressão sob demanda, tipo Amazon/Lulu)

| polegadas | mm | Nome |
|---|---|---|
| 4,25 × 6,87 | 108 × 175 | *mass market* |
| 5 × 8 | 127 × 203 | *trade* pequeno |
| 5,5 × 8,5 | 140 × 216 | *digest* — **Carta dobrada ao meio** |
| 6 × 9 | 152 × 229 | *US trade*, o mais comum |
| 8,5 × 11 | 216 × 279 | Carta |

#### O que a impressora A4/Carta libera

| Folha de partida | Dobrada 1× | Formato final após aparo |
|---|---|---|
| A4 (210×297) | 148 × 210 = A5 | 14 × 20,5 cm |
| **Carta (216×279)** | 140 × 216 | **13,5 × 21 cm** ✨ |
| Ofício II (216×330) | 165 × 216 | 16 × 21 cm (atarracado) |
| A4 dobrada 2× | 105 × 148 = A6 | 10 × 14,5 cm |

> **Descoberta útil:** papel **Carta**, dobrado ao meio, dá 140 × 216 mm,
> que apara exatamente para o formato brasileiro clássico de 13,5 × 21 cm.
> (Para 14 × 21 não dá: a Carta dobrada tem 139,7 mm de largura antes de
> qualquer aparo.) Se você quer que o livro tenha a cara e as proporções de um
> livro de livraria, imprima em Carta, não em A4. O A5 (1:1,414) é
> perceptivelmente mais estreito e alongado — não é feio, é cara de
> caderno europeu, mas é outra estética.

**O truque que libera qualquer formato:** refile a folha inteira **antes**
de dobrar.

| Quero (dobrado, antes do aparo) | Corto a folha para | Dobro → |
|---|---|---|
| 14 × 19 cm | 280 × 190 mm | 140 × 190 |
| 13 × 20 cm | 260 × 200 mm | 130 × 200 |
| 12 × 18 cm | 240 × 180 mm | 120 × 180 |
| 10,5 × 17 cm | 210 × 170 mm | 105 × 170 |

**Regra geral:** a folha aberta precisa ter *duas vezes a largura × uma
vez a altura* do livro final. A Epson aceita tamanho de papel
personalizado no driver, então dá para imprimir já na folha cortada. Se for refilar depois de costurar, some
3–5 mm por face a essas medidas.

#### Proporções

| Proporção | Exemplo | Sensação |
|---|---|---|
| 1 : 1,414 | A5, A4 | Neutra, "moderna europeia" |
| 1 : 1,5 (2:3) | 14×21, 13,5×20,5 | Clássica, equilibrada — a mais usada |
| 1 : 1,55 | 13,5×21 | Elegante |
| 1 : 1,618 (áurea) | 13×21 | Refinada, esguia |
| 1 : 1,3 | 16×21, quarto | Robusta, "acadêmica" |
| 1 : 1 | Quadrado | Contemporânea, infantil, fotográfica |

Acima de 1:1,6 o livro parece sofisticado mas comporta menos texto por
linha e fica instável na mão. Abaixo de 1:1,35 começa a parecer manual
técnico.

**Por que os livros de livraria fogem do A5/A4 exato:** aproveitamento de
papel (gráficas cortam de folhas 66×96, 64×88 cm, minimizando desperdício),
tradição de casa de cada editora, gênero do livro, e ajuste de largura
conforme a espessura da lombada.

### 4. A ordem das páginas

Convenções que se pode seguir sem pensar:

- Página ímpar = *recto* (direita); par = *verso* (esquerda). Página 1 é
  sempre ímpar.
- **Ordem do pré-textual:** falsa folha de rosto (só o título) → verso em
  branco → folha de rosto (título, autor, tradutor, editora) → verso com
  créditos → dedicatória/epígrafe → sumário → texto.
- Capítulos abrem em **página ímpar** (edições luxuosas) ou em qualquer
  página nova (econômico). As páginas em branco resultantes ficam
  **realmente em branco** — sem número, sem cabeço.
- Pré-textual em romanos minúsculos (i, ii, iii) ou sem numeração; o miolo
  começa em 1 árabe.
- **Cabeços:** autor ou título no verso, capítulo no recto. Ou omita e
  deixe só o fólio no pé — mais limpo, sempre elegante.
- A primeira linha do primeiro parágrafo do capítulo **não tem recuo**.

- **Colofão**, no fim: como o livro foi feito (fonte, papel, quem
  imprimiu e encadernou, o ano). Nos livros do estúdio leva também um
  mote em latim ou grego, próprio de cada volume.

### 5. Micro-tipografia — o que o olho registra sem saber

- **Justificado + hifenização pt-BR.** Configure o dicionário, ou terá
  rios de branco. Justificado sem hifenização é pior que alinhado à
  esquerda.
- **Órfãs e viúvas:** nunca uma linha sozinha no topo ou no pé. Configure
  o controle para no mínimo 2.
- Nunca uma palavra sozinha encerrando parágrafo no fim de página, nem
  hifenização na última linha da página.
- **Registro:** páginas espelhadas terminam na mesma altura. Se uma tem 34
  linhas, a de frente tem 34.
- Diálogo em português usa **travessão (—)**, não hífen, não aspas
  anglófonas, com espaço depois.
- Ligaduras (fi, fl) e kerning ativados.
- Máximo de 2–3 hifenizações em linhas consecutivas.
- **Algarismos antigos** (*oldstyle*) no texto corrido — os que têm
  ascendentes e descendentes e não brigam com as minúsculas.
- **Versaletes verdadeiros** para siglas e para a primeira linha do
  capítulo — nunca a versão falsa gerada encolhendo maiúsculas.

Esses dois últimos são o que separa um miolo amador de um profissional.

### 6. Ferramentas

| Perfil | Ferramenta |
|---|---|
| Não se assusta com código | **Typst** (moderno, sintaxe simples) ou LaTeX com a classe `memoir` |
| Quer interface visual | **Affinity Publisher** (compra única, páginas-mestras, estilos, PDF/X). InDesign é padrão de mercado mas é assinatura. Scribus é capaz mas desconfortável para texto longo |
| Vai insistir no Word/LibreOffice | Possível: use **Estilos** obrigatoriamente, margens espelhadas, quebras de seção para romanos/árabes, hifenização ligada. Teto de qualidade mais baixo, resultado honesto alcançável |

**A vantagem decisiva do TeX/Typst:** o algoritmo Knuth–Plass otimiza o
**parágrafo inteiro**, não linha por linha — a cor de página fica muito
mais uniforme que no Word ou no LibreOffice, que quebram linha a linha. (O
InDesign tem algo equivalente, o *Paragraph Composer*.) E você define o projeto uma vez e ele
pagina 400 páginas sozinho.

**Typst × LaTeX:** o argumento antigo a favor do LaTeX era o `microtype` —
pontuação pendurada na margem e leve expansão das letras. O Typst atual
tem os dois: `text(overhang: true)`, que já vem ligado, e
`par(justification-limits: …)`, que permite ajustar o espacejamento entre
letras na justificação. Para texto corrido, a diferença deixou de pesar.

**Texto bilíngue sincronizado:** o Typst não tem um equivalente pronto ao
`reledpar` do LaTeX. O estúdio já fez bilíngue em **colunas paralelas** na
Vulgata, em A4 paisagem — funciona bem quando o texto vem em blocos curtos
(versículos), que se alinham sozinhos. Para prosa longa, sincronizar
página a página vira trabalho manual; aí a **edição monolíngue com
referências marginais** costuma ser a melhor saída.

#### Recursos do Typst que vale conhecer

**Armadilhas que já custaram tempo:**

- **`*texto*` é negrito, não itálico.** Itálico é `_texto_`.
- **`#include` não compartilha as variáveis do arquivo-mãe.** Cada
  fragmento precisa importar os seus estilos no topo.
- **`#align(center)` por fora vaza para os parágrafos justificados** e
  centraliza a última linha de cada um. Use `#set align(left)` dentro do
  bloco — ou, num bloco centralizado, não justifique.
- **Calcular preenchimento com `counter(page).final()` não converge:** as
  páginas que você acrescenta mudam a contagem, e o Typst oscila. Use um
  número fixo e confira o total depois.
- **`inside`/`outside` alternam com a paridade da página** — certo para
  códice dobrado, errado para costura japonesa, que fura todas as folhas
  pela mesma borda. Nesse caso use `left`/`right`.

**Planejar o número de páginas** — medido, não estimado, nos livros do
estúdio: prosa corrida em A5, Libertinus 10,5 pt, dá **~430 palavras por
página**. Estimativas a olho erraram por 1,7×.

**Recursos:**


- **`text.costs`** é o equivalente Typst do controle de viúvas/órfãs, e é
  onde se ganha uniformidade de página. Aumentar `runt` evita a palavra
  sozinha fechando parágrafo. Configure e esqueça:
  `costs: (hyphenation: 200%, runt: 400%, widow: 300%, orphan: 300%)`
- **`number-type: "old-style"`** ativa os algarismos antigos.
- **`hydra`** (Typst Universe) resolve cabeços inteligentes — título do
  capítulo no recto, obra no verso, suprimido nas aberturas. É
  surpreendentemente chato de fazer à mão.
- **`droplet`** para capitulares, **`marginalia`** para notas de margem.
- **Referência marginal** (Stephanus, Bekker, livro.parágrafo) —
  indispensável em Platão e Marco Aurélio, e o detalhe que faz a edição
  parecer séria. A referência vai sempre na margem externa, o que exige
  testar a paridade da página em `context`.

#### O que fazer no Affinity

Typst para o rio de texto; Affinity para as peças únicas:

- folha de rosto com entreletra e hierarquia ajustadas à mão (uma página
  de rosto vale meia hora de ajuste óptico)
- vinhetas, filetes, ornamentos, marca do editor
- colofão
- rótulo de lombada (essencial se a capa for couro liso sem gravação)
- padrões para as guardas — *paste paper* impresso, desenho para
  marmorizado
- gabaritos para gravação/douração a ferro

Depois traga essas páginas para o documento principal como **imagem
vetorial** (o Typst atual aceita PDF direto em `#image`). Assim a paginação e a contagem de cadernos
ficam sob controle de **um único arquivo** — que é o que se quer quando se
descobre, na hora de impor, que faltam 4 páginas para fechar o caderno.

### 7. Sentido de fibra — o item nº 1

> **Isso vale mais que qualquer decisão tipográfica.**

Imprimindo A4 e dobrando ao meio, a lombada fica no lado de 210 mm — e a
fibra tem que correr **paralela a ela**. O problema: o A4 de resma é quase
sempre **grão longo**, com a fibra no lado de 297 mm, ou seja,
*perpendicular* à dobra. O vinco racha, o caderno não assenta e o livro não
abre plano.

Como identificar a fibra, os testes e as soluções — comprar folha grande e
cortar no sentido certo — estão no **cap. 5**. Aqui só o lembrete: decida
o papel e confira a fibra **antes** de projetar o formato.

### 8. Geometria: página não-refilada × formato final

Um miolo costurado sempre sai com as folhas internas sobressaindo
(*creep*), e as três bordas são refiladas depois de costurar. Então **não
projete para A5: projete para o formato refilado, e coloque a sobra de
refile dentro das margens.**

Receita exata que fecha sem nenhum escalonamento:

| | |
|---|---|
| Folha | A4 paisagem, 297 × 210 mm |
| Página não-refilada | 148,5 × 210 mm (metade exata) |
| Refile | 3,5 mm na dianteira · 2,5 mm cabeça · 3,5 mm pé |
| **Formato final** | **145 × 204 mm** |

Margens a declarar (já somando o refile):

- interna 15 mm *(livro costurado abre plano; não precisa do exagero da
  lombada colada)*
- externa 18 + 3,5 = **21,5 mm**
- superior 16 + 2,5 = **18,5 mm**
- inferior 22 + 3,5 = **25,5 mm**
- → mancha **112 × 166 mm**; depois de refilar, sobram exatamente
  15/18/16/22 no livro pronto

**A vantagem:** duas páginas de 148,5 mm somam 297 mm = A4 exato. Nenhum
redimensionamento em nenhuma etapa. Isso importa muito, porque **qualquer
escala de 98% no driver destrói o casamento das páginas.**

Como refilar — ferramenta, ordem dos cortes, quanto tirar — está no
**cap. 9**.

**Alternativa histórica legítima:** não aparar, deixando as barbas
(*uncut edges*), ou aparar só a goteira. Muitas edições finas fazem isso
deliberadamente — mas aí o *creep* fica à mostra, e o caderno precisa ser
fino.

### 9. Imposição de cadernos

O que é imposição, quantas folhas por caderno, o *creep* e a borda de
virada estão no **cap. 7**. Aqui, só o que toca a editoração:

- **O estúdio usa o `booklet.py`**, que compõe duas A5 por folha A4
  paisagem e prepara o verso para o duplex. Alternativas maduras, se um dia
  precisar: `pdfjam --signature 16`, `pdfbook2 --signature=16` (com
  `--no-crop` se você já projetou a geometria acima) e o `typst-post`
  (PyPI), feito para Typst.
- **Nenhuma delas compensa o *creep*** deslocando a mancha nas folhas
  internas. Como você refila, não precisa — mas então **refilar não é
  opcional**.
- **Escolha o tamanho do caderno pela contagem de páginas**, para sobrar o
  mínimo em branco no fim. Um livro de 100 páginas são 25 folhas A4: fecha
  exato em 5 cadernos de 5 folhas, enquanto em cadernos de 4 sobrariam
  páginas.
- **Papel mais grosso, caderno mais fino:** 4 folhas é o padrão para
  80–100 g; com 120 g, 3 folhas.

### 10. O comportamento da L4360 na editoração

*(O diagnóstico completo da impressora está no cap. 6. Aqui só o que
decide a diagramação.)*

- **Duplex automático até ~90 g/m², manual acima.** O automático é
  homologado para papel comum de 64–90 g/m² (o Pólen Bold 90 está no
  limite); opalina 120 e afins pedem duplex manual. Nos dois casos, o
  **registro frente/verso** pode variar alguns décimos de milímetro, e
  ver a mancha da página seguinte desalinhada contra a luz é o detalhe que
  separa "artesanal" de "amador". Imprima uma folha de teste com cruzetas
  nos quatro cantos, meça, e corrija na imposição se houver desvio
  constante.
- **Desligue qualquer "ajustar à página".** Tamanho real / 100%.
- **Limite de gramatura:** 80–90 g/m² passa bem pela bandeja; acima de
  ~120 g, teste antes. Papéis de algodão e texturados de 140–200 g
  dificilmente passam — confirme que a impressora aceita o papel **antes**
  de projetar o livro em cima dele.
- **Ganho de ponto:** papéis absorventes (offset, pólen) alargam o traço.
  Compense subindo o corpo (10,5–11,5 pt em vez de 10) e evitando fontes
  de haste fina.

> ⚠️ **Divergência nas fontes.** Uma das conversas de origem recomenda
> **EB Garamond 11,5 pt** como escolha padrão para o miolo. Uma resposta
> posterior, já sabendo que a impressão é jato de tinta em papel não
> revestido, **revisa isso**: a EB Garamond tem hastes finas e serifas
> delicadas, e o *dot gain* do jato em papel absorvente engrossa e
> acinzenta justamente isso. A recomendação que vale é a revisada —
> fontes de contraste moderado (Literata, Junicode, Libertinus) ganham
> nesse suporte — a Libertinus, que já é clara, desde que não desça de
> 10,5 pt —, e "ganhar" aqui significa **parecer impresso em vez de
> fotocopiado**. Se quiser resolver de vez, faça o teste comparativo
> impresso: mesma página, mesmas medidas, quatro fontes, dois corpos.

---

## O teste que evita 90% das frustrações

Antes de mandar o livro inteiro:

**Imprima 8 a 16 páginas em casa, no tamanho final** (corte o A4 na medida
certa), dobre, empilhe, segure na mão e **leia de verdade por dez minutos.**

Você vai descobrir instantaneamente que o corpo está pequeno, ou que a
margem interna sufoca, ou que a fonte fica cinzenta. Na tela tudo parece
ótimo; no papel, não.

E antes de comprometer 25 folhas, faça um **boneco (*dummy*)** em papel de
rascunho: 5 cadernos de 5 folhas, dobrados, costurados grosseiramente, sem
impressão. Custa 30 minutos e revela:

- se 5 folhas por caderno é confortável naquele papel
- quanto de *creep* haverá para aparar
- a espessura real da lombada (para dimensionar a capa)
- se a proporção escolhida agrada na mão

Todo encadernador experiente faz isso. É o passo mais barato e mais
informativo do projeto.

**A tarefa de um fim de semana que decide 80% do projeto gráfico:** corte
doze folhas A4 grão curto do papel candidato, imprima duas páginas de
teste em quatro fontes e dois corpos, faça o teste da água nos modos de
papel do driver, monte um caderno de 16 páginas, prense, costure, refile e
leia.

---

## Armadilhas e casos especiais

> ⚠️ **A armadilha jurídica do "domínio público".** No Brasil (Lei
> 9.610/98) a obra cai em domínio público 70 anos contados de 1º de
> janeiro do ano seguinte à morte do autor. Mas **tradução é obra nova,
> com direito autoral próprio** — e o mesmo vale para edições críticas,
> notas, prefácios e até para a fixação de texto de um filólogo. Marco
> Aurélio e Platão estão em domínio público *em grego*; a tradução
> moderna, não. **Antes de adotar uma tradução, confirme o ano de morte do
> tradutor.**

> ⚠️ **Não use "ajustar à página" nem escala de 98%.** Qualquer
> redimensionamento no driver destrói o casamento das páginas impostas e
> a nitidez das fontes. É reamostragem, não ajuste.

> ⚠️ **Não misture dois brancos no mesmo miolo.** Todas as folhas do mesmo
> lote, mesmo sentido de fibra, mesmo branco. A diferença é percebida
> imediatamente, mesmo que inconscientemente.

### Espessura da lombada — para planejar a capa

Você precisa dela antes de desenhar a capa ou a lombada impressa:

> **lombada (mm) ≈ (nº de páginas ÷ 2) × espessura da folha**

Offset 80 g ≈ 0,10 mm por folha; Pólen Bold 90 ≈ 0,13–0,14 mm — é por isso
que o pólen produz livros mais "gordos" e agradáveis.

É estimativa. **A medida que vale é a do miolo real**, depois de costurado
e prensado, com paquímetro: a costura acrescenta *swell* e a prensa tira.
Medidas da capa, das pastas e do material de revestimento estão nos caps.
12 e 13.

### Para estudar de verdade

- **Emanuel Araújo, *A Construção do Livro*** — a referência brasileira,
  completa, do projeto gráfico à impressão. Se comprar um livro só, compre
  este.
- **Jan Tschichold, *A Forma do Livro*** (Ateliê Editorial) — ensaios
  sobre proporção, margens e a tradição do livro. Curto e transformador.
- **Robert Bringhurst, *Elementos do Estilo Tipográfico*** — a bíblia; a
  edição brasileira anda difícil de achar.
- **Mitchell & Wightman, *Book Typography: A Designer's Manual*** — o mais
  prático de todos, cheio de exemplos comentados. Em inglês.
- **Richard Hendel, *On Book Design*** — designers explicando decisões de
  projetos reais.

**E o exercício mais barato e mais eficaz:** pegue cinco livros que você
acha bonitos na estante, meça as margens com régua, identifique a fonte,
conte os caracteres por linha, veja como abrem os capítulos. Copiar
deliberadamente um projeto que funciona é a melhor escola.
