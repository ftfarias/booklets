# Conversa 12 — Tipografia e editoração para imprimir livros de arte em casa

**Fonte:** https://poe.com/s/23qpJAkI6KidExw1RrYZ
**Bot:** Claude-Opus-5
**Data:** Aug 29
**Tema:** Fundamentos de tipografia (serifa vs. sans, altura-x, contraste, título vs. texto, combinação de fontes, ajustes de entrelinha/medida) e um guia completo de design e editoração de livros para impressão caseira de obras de domínio público — texto-fonte, limpeza, formato, margens canônicas, micro-tipografia, Typst, sentido de fibra do papel, imposição de cadernos, comportamento da Epson L4360 e a fonte Libertinus Serif.

---

## Pergunta 1

Eu estou tentando entender um pouco de tipografia, que tipos de fontes são melhores para títulos, para texto, com serifa, sem ela, etc. você consegue explicar para alguém que só coloca "Arial" no word e pronto?

## Resposta 1 (Claude-Opus-5)

### [Raciocínio]

Ótima pergunta — e a boa notícia é que 90% de uma tipografia decente vem de meia dúzia de decisões simples. Vou do conceito ao "faz assim que funciona".

### Primeiro: o que é serifa, afinal

Serifas são aqueles pezinhos/tracinhos nas pontas das letras. Compare o "T" da Times New Roman (tem base e chapéu com pontinhas) com o da Arial (traços limpos, sem apêndices). Fontes com serifa também são chamadas de romanas; as sem serifa, de sans-serif ou grotescas.

O mito que você provavelmente já ouviu — "serifa é mais legível no papel, sem serifa na tela" — é basicamente folclore. Ele nasceu numa época em que as telas tinham resolução baixíssima e não conseguiam desenhar detalhes finos. Hoje, com telas de alta densidade, isso caiu por terra. A pesquisa sobre legibilidade é bem inconclusiva: o que mais importa é familiaridade (você lê melhor o que está acostumado a ler) e o desenho específico daquela fonte, não a categoria dela.

Então esqueça a regra e olhe para o que realmente conta.

### O que realmente conta numa fonte

Altura-x: a altura das letras minúsculas sem hastes (o "x", o "o") comparada às maiúsculas. Altura-x grande = letra parece maior e aguenta bem tamanhos pequenos. A Verdana e a Georgia têm altura-x generosa; a Garamond e a Futura, pequena (por isso Garamond em 11pt parece minúscula).

Contraste de traço: diferença entre as partes grossas e finas da letra. A Didot/Playfair Display têm contraste altíssimo (finos quase capilares) — belíssimas grandes, um desastre em corpo 10. A Times tem contraste médio; a Arial, quase nenhum.

Abertura: o quanto as letras "abrem". No "c", "e", "a" e "s" da Helvetica/Arial, as pontas se curvam para dentro, quase fechando. Isso deixa as letras mais parecidas entre si. Em fontes humanistas (Frutiger, Myriad, Source Sans), as aberturas são amplas — cada letra é mais distinguível, o que ajuda em textos longos.

Diferenciação de caracteres: teste rápido — digite Illegal 1O0 na fonte. Se o I maiúsculo, o l minúsculo e o 1 forem idênticos, é uma fonte que exige atenção do leitor. Arial e Helvetica falham nesse teste; Verdana e Inter passam com folga.

### Título vs. texto: a distinção que muda tudo

Essa é a ideia mais útil de toda a tipografia, e quase ninguém fora da área conhece.

Fontes são desenhadas para tamanhos específicos. Existem cortes display (para títulos) e text (para leitura corrida):

| | Display / Títulos | Text / Corpo |
| --- | --- | --- |
| Contraste | Alto, detalhes finos | Moderado, traços firmes |
| Espaçamento | Apertado (letras grandes já se sustentam) | Aberto, generoso |
| Personalidade | Pode ser marcante, peculiar | Discreta, "invisível" |
| Objetivo | Chamar atenção em 2 segundos | Não cansar em 20 minutos |

Consequências práticas:

- Uma fonte muito expressiva funciona em título e cansa no texto. Aquela fonte geométrica linda (Montserrat, Poppins, Futura) tem "o", "c", "e" quase circulares e idênticos — ótimo num cabeçalho de 3 palavras, exaustivo num parágrafo de 300.
- Uma fonte de texto em título fica sem graça — não erra, mas não brilha.
- Algumas famílias já vêm com as duas versões. A Playfair Display é literalmente "display" no nome. A Source Serif tem cortes ópticos. Se você vê "Display", "Deck", "Caption", "Text" no nome, é isso.

### O que usar, na prática

Já instalado no Word (Windows/Office):

Para corpo de texto:

- Georgia — serifada, altura-x grande, funciona em tela e papel. Aposta segura.
- Cambria e Constantia — serifadas, feitas para tela, bem sólidas.
- Segoe UI, Calibri ou Aptos (a nova padrão do Microsoft 365) — sans humanistas, agradáveis e neutras.
- Palatino / Book Antiqua — clássica, elegante, ótima para textos longos impressos.
- Century Schoolbook — literalmente desenhada para livros escolares. Legibilidade altíssima.

Para títulos:

- Franklin Gothic ou Franklin Gothic Condensed — sans robusta, jornalística, excelente em peso Bold.
- Georgia Bold ou Cambria Bold — se quiser algo mais sóbrio.
- Trebuchet MS — sans com personalidade, boa em títulos, medíocre em corpo.

O que evitar: Times New Roman e Arial não são "erradas", mas gritam "não pensei nisso". Comic Sans, Papyrus e Impact, você já sabe.

Se puder baixar (Google Fonts, tudo gratuito):

- Duplas prontas que funcionam: Lora (texto) + Playfair Display (título) · Source Serif + Source Sans · Literata + Inter · EB Garamond + Work Sans · Spectral + IBM Plex Sans
- Para corpo, as mais confiáveis: Inter, Source Sans 3, Public Sans, Literata, Newsreader, Crimson Pro, Libre Baskerville
- Para títulos com atitude: Fraunces, Playfair Display, Bricolage Grotesque, Archivo Black

### Como combinar duas fontes sem errar

Três caminhos, do mais seguro ao mais ousado:

- Uma família só, pesos diferentes. Corpo em Regular, título em Bold ou Black. Simples, coeso, impossível de errar. Contraste de peso costuma resolver mais que contraste de fonte.
- Uma superfamília. IBM Plex, Source, Noto e Roboto têm versões serif, sans e mono desenhadas juntas. Harmonia garantida com variedade visual.
- Contraste claro. Serifada + sem serifa, ou uma expressiva + uma neutra. A regra é: as duas devem ser bem diferentes, mas do mesmo "humor". Duas fontes parecidas-mas-não-iguais criam um desconforto sutil (parece erro). Duas fontes de épocas/tons opostos brigam. O truque é procurar algo em comum — altura-x similar, mesma sensação de época.

E o limite: duas fontes, três no máximo. Se sentir necessidade de uma quarta, o problema é a hierarquia, não a variedade.

### Os ajustes que fazem mais diferença que a fonte

Sinceramente? Se você só mudar isso e mantiver a Arial, seu documento já vai melhorar muito:

Comprimento da linha. O ideal é entre 45 e 75 caracteres por linha (~66 é o ponto doce). Uma página A4 com margens estreitas e texto em 11pt dá umas 100 caracteres por linha — o olho se perde na volta. Aumente as margens ou use duas colunas.

Entrelinha. O padrão "simples" do Word é apertado demais. Use 1,15 a 1,5 para corpo de texto (quanto mais longa a linha, mais entrelinha ela precisa). Em títulos grandes, faça o contrário: aperte para 0,9–1,1, porque em corpo grande o espaço padrão parece um buraco.

Alinhamento. Alinhado à esquerda é sempre seguro. Justificado só com hifenização ligada — senão você cria aqueles "rios" de espaço branco. Centralizado serve para 1 ou 2 linhas, nunca para parágrafos.

Não use dois espaçamentos ao mesmo tempo. Ou recuo na primeira linha, ou espaço entre parágrafos. Os dois juntos é redundância. (E recuo na primeira linha não faz sentido no primeiro parágrafo.)

MAIÚSCULAS precisam de respiro. Se usar caixa-alta, aumente o espaçamento entre letras (Fonte → Avançado → Espaçamento: Expandido). Sem isso, as letras se aglomeram.

Nunca use negrito ou itálico "falsos". Se a fonte não tem esse corte, o programa inclina/engorda por software e o resultado é deformado. Use fontes com família completa.

### Colando tudo: uma receita que funciona

Para um documento comum de trabalho ou faculdade:

- Corpo: Georgia 11pt, entrelinha 1,4, alinhado à esquerda, margens de 3cm, sem recuo, 8pt de espaço entre parágrafos
- Títulos: Franklin Gothic Demi, 18pt, entrelinha 1,1
- Subtítulos: mesma fonte do título, 13pt
- Hierarquia por tamanho e peso, não por cor ou sublinhado

Pronto. Isso já é melhor que 95% dos documentos que circulam por aí.

Se quiser, me diz o que você está fazendo especificamente — TCC, apresentação, currículo, site, material da empresa — que eu afino a recomendação. As restrições mudam bastante: currículo pede uma coisa, slide projetado pede outra completamente diferente (em slide, por exemplo, contraste alto e serifa fina desaparecem no projetor).

---

## Pergunta 2

Eu estou querendo imprimir alguns livros, um ou dois exemplares de obras de domínio público, e preciso aprender um pouco de design e editoração de livros

## Resposta 2 (Claude-Opus-5)

### [Raciocínio]

Excelente projeto — e, para dois exemplares de obras em domínio público, você está numa posição privilegiada: pode fazer escolhas puramente estéticas, sem pressão comercial. Vou organizar isso na ordem em que as decisões realmente acontecem.

### Antes de tudo: a armadilha jurídica do "domínio público"

No Brasil (Lei 9.610/98), a obra cai em domínio público 70 anos contados de 1º de janeiro do ano seguinte à morte do autor. Mas o detalhe que pega quase todo mundo: tradução é obra nova, com direito autoral próprio. Dostoiévski está em domínio público; a tradução do Paulo Bezerra publicada pela 34, não. O mesmo vale para edições críticas, notas, prefácios e até para a fixação de texto de um filólogo.

Para 1–2 exemplares de uso pessoal, o risco prático é nulo, mas vale saber: se você quer autor estrangeiro, suas opções limpas são o original, uma tradução antiga também em domínio público, ou uma tradução com licença livre.

### 1. De onde tirar um texto-fonte decente

A qualidade do arquivo de partida define umas 15 horas do seu trabalho. Em ordem de qualidade:

- Standard Ebooks — de longe o melhor. Voluntários pegam textos do Gutenberg e fazem edição séria: tipografia corrigida, aspas tipográficas, itálicos, semântica. Só em inglês, mas se seu projeto for anglófono, comece aqui e economize dias.
- Project Gutenberg — enorme, qualidade variável. Prefira as versões em HTML às TXT.
- Wikisource (inclusive em português) — texto revisado colaborativamente contra o fac-símile.
- Domínio Público (MEC) e Biblioteca Brasiliana Guita e José Mindlin (USP) — para literatura brasileira. Muita coisa em PDF escaneado, o que significa OCR e trabalho manual.

### 2. A parte chata que é 70% do trabalho: limpar o texto

Ninguém avisa isso. Antes de pensar em fonte, você precisa:

- Remover cabeçalhos/rodapés de licença, números de página soltos, marcações de scan
- Trocar "aspas retas" por "aspas tipográficas" e ' por '
- Converter hifens usados como travessão em travessão (—) ou meia-risca (–)
- Eliminar hifens de quebra de linha herdados do OCR ("compa-\nnheiro")
- Trocar espaços duplos por simples, remover espaços antes de pontuação
- Padronizar reticências para o caractere único (…)
- Reconstruir itálicos que o TXT perdeu (frequentemente marcados com _underscores_)
- Corrigir erros clássicos de OCR: rn→m, l→1, 0→O, ﬁ→fi

Faça isso com busca e substituição por expressão regular, não à mão. Um editor de texto simples (VS Code, Notepad++, Sublime) resolve em minutos o que levaria horas no Word. Vale muito aprender três ou quatro regex básicas para isso.

E, importante: decida sua política editorial. Vai modernizar ortografia? Manter "pharmacia"? Padronizar diálogos? Escreva as regras num papel e siga, porque na página 200 você não vai lembrar o que decidiu na 20.

### 3. Formato (trim size)

| Formato | Uso |
| --- | --- |
| 12,5 × 18 cm | Livro de bolso, poesia, novelas curtas |
| 14 × 21 cm | O padrão brasileiro. Seguro para quase tudo |
| 15,5 × 23 cm | Ensaio, técnico, textos com notas |
| 16 × 23 cm | Acadêmico, ilustrado |

Duas notas práticas: gráficas de impressão digital frequentemente trabalham melhor com formatos que se encaixem em folhas A4/A3 (14,8 × 21 = A5 exato é o mais barato), e formatos mais estreitos favorecem a boa entrelinha. Para primeira experiência, 14 × 21 ou A5.

### 4. Margens — onde mora a diferença entre "livro" e "apostila"

A regra que quebra a intuição de todo mundo: as margens não são iguais, e a de baixo é a maior. A mancha de texto fica ligeiramente acima do centro geométrico, porque o olho percebe o centro óptico mais alto — e porque suas mãos ocupam a parte de baixo.

A proporção clássica (canônica, herdada dos manuscritos medievais e sistematizada por Tschichold e pelo cânone de Van de Graaf) segue mais ou menos:

interna : superior : externa : inferior = 2 : 3 : 4 : 6

Traduzido para 14 × 21 cm, uma receita que funciona:

- Interna (lombada): 16 mm
- Externa: 19 mm
- Superior: 18 mm
- Inferior: 22 mm
- → Mancha de texto: 105 × 170 mm

Some 3–4 mm à margem interna se o livro passar de ~250 páginas, porque a cola "engole" parte da lombada e o texto fica difícil de ler no vinco. Isso se chama gutter allowance, e é o erro nº 1 de quem faz o primeiro livro. E use margens espelhadas (mirrored/facing pages) — a página par é o espelho da ímpar, não a cópia.

Se as margens parecerem "grandes demais" para você, elas provavelmente estão certas. Margem generosa é o que faz um miolo respirar.

### 5. Tipografia do miolo

Medida (largura da linha): 60–70 caracteres por linha. Esse é o parâmetro-mestre. Escolha tamanho de fonte em função dele, não o contrário.

Corpo e entrelinha: algo como 10,5/14 ou 11/15 (corpo/entrelinha em pontos), dependendo da altura-x da fonte. Garamond em 11 parece 9; Literata em 10,5 parece 11,5. Sempre teste impresso.

Fontes gratuitas realmente boas para miolo de livro:

- EB Garamond — clássica, elegante, tem versaletes e algarismos antigos de verdade
- Literata — desenhada para leitura longa, altura-x confortável, muito robusta
- Source Serif 4 — neutra, impecável, família completíssima
- Alegreya e Vollkorn — calorosas, com bom "sabor" de livro
- Crimson Pro — bonita, mas leve; pede corpo um pouco maior
- Junicode — excelente para textos antigos, medievais, filológicos
- Spectral / Newsreader — modernas, versáteis

Duas coisas que separam um miolo amador de um profissional:

- Algarismos antigos (oldstyle figures) no texto corrido — aqueles números com ascendentes e descendentes, que não brigam com as minúsculas. Ative se a fonte tiver.
- Versaletes verdadeiros (small caps) para siglas e para aquele efeito clássico na primeira linha do capítulo — nunca a versão "falsa" que o software gera encolhendo maiúsculas.

Evite para miolo: fontes de contraste altíssimo (Playfair, Didot, Cormorant) — em corpo 10,5 os traços finos somem ou ficam cinzentos na impressão digital.

### 6. Anatomia do livro (a estrutura que dá o "cheiro" de livro de verdade)

Convenções que você pode seguir sem pensar:

- Página ímpar = recto (a da direita); par = verso (esquerda). Página 1 é sempre ímpar.
- Ordem do pré-textual: falsa folha de rosto (só o título) → verso em branco → folha de rosto (título, autor, tradutor, "editora") → verso com créditos → dedicatória/epígrafe → sumário → e só então o texto.
- Capítulos abrem em página ímpar (edições mais luxuosas) ou em qualquer página nova (mais econômico, menos papel). Deixe as páginas em branco resultantes realmente em branco — sem número, sem cabeço.
- O pré-textual usa numeração romana em minúsculas (i, ii, iii) ou nenhuma numeração; o miolo começa em 1 árabe.
- Cabeços (running heads): convenção usual é autor ou título no verso, capítulo no recto. Ou simplesmente omita e deixe só o fólio no pé da página — mais limpo, sempre elegante.
- A primeira linha do primeiro parágrafo do capítulo não tem recuo. Os demais parágrafos, sim (recuo de ~1 a 1,5 vezes o corpo da fonte). E em livro se usa recuo, não espaço entre parágrafos.

### 7. Micro-tipografia: os detalhes que o olho registra sem saber

- Justificado + hifenização em português. Configure o dicionário para pt-BR, ou você terá rios de branco horrorosos. Justificado sem hifenização é pior que alinhado à esquerda.
- Órfãs e viúvas: nunca deixe uma linha sozinha no topo ou no pé de página. Configure controle de linhas órfãs/viúvas para no mínimo 2.
- Nunca deixe uma palavra sozinha encerrando um parágrafo no fim de página, nem hifenização na última linha da página.
- Páginas espelhadas devem terminar na mesma altura (registro). Se uma tem 34 linhas, a de frente tem 34.
- Diálogo em português usa travessão (—), não hífen, não aspas anglófonas. Com espaço depois.
- Ligaduras (fi, fl) ativadas; kerning ativado.
- Máximo de 2–3 hifenizações consecutivas em linhas seguidas.

### 8. Ferramentas — escolha pelo seu perfil

Se você não se assusta com código: LaTeX com a classe memoir, ou Typst (bem mais moderno e amigável, sintaxe simples). Vantagem decisiva: o algoritmo de quebra de parágrafo do TeX (Knuth-Plass) otimiza o parágrafo inteiro, não linha por linha — o resultado é uma cor de página mais uniforme que o padrão do InDesign. Além disso, para um livro de texto corrido, é o caminho mais rápido: você define o projeto uma vez e ele pagina 400 páginas sozinho. Para o seu caso, é honestamente a melhor relação esforço/resultado.

Se você quer interface visual: Affinity Publisher — compra única, faz tudo que você precisa, páginas-mestras, estilos, exportação PDF/X. InDesign é o padrão do mercado, mas assinatura. Scribus é gratuito e capaz, porém desconfortável para texto longo.

Se for insistir no Word/LibreOffice: é possível! Use obrigatoriamente Estilos (nunca formatação manual), margens espelhadas, quebras de seção para a numeração romana/árabe, e ative hifenização. O teto de qualidade é mais baixo, mas um resultado honesto é alcançável.

### 9. Capa e lombada

A largura da lombada depende do papel: lombada (mm) ≈ (nº de páginas ÷ 2) × espessura da folha. Offset 80g dá algo em torno de 0,10 mm por folha; papel pólen (o creme, mais fofo, usado em literatura) tem volume maior, ~0,13–0,15 mm — e é por isso que ele produz livros mais "gordos" e agradáveis. Peça o fator exato à gráfica, porque errar a lombada por 2 mm desloca toda a arte.

A capa é um arquivo único em página dupla: contracapa + lombada + capa, com 3 mm de sangria em toda a volta. Miolo normalmente sem sangria (a não ser que tenha imagem cortando a borda).

### 10. Impressão: o que pedir

- PDF/X-1a ou PDF/X-4, fontes incorporadas, páginas simples (não espelhadas) para o miolo
- Texto em preto 100% K, nunca em "preto rico" (mistura de CMYK) — texto fino em 4 cores fica borrado e com franjas de registro
- Miolo: papel pólen soft/bold 80–90 g para literatura (creme, opaco, pouco cansativo); offset 80g é o econômico. Evite sulfite muito branco e evite couché no miolo de texto — brilha e reflete
- Capa: cartão 250–300 g com laminação fosca (mais sofisticada que a brilhante), ou capa dura se quiser durabilidade real
- Acabamento: hotmelt/cola PUR para brochura; costurado é bem melhor mas raro em tiragem unitária; capa dura com miolo costurado é o topo — vale procurar um encadernador artesanal, especialmente para 1–2 exemplares de algo que você quer guardar

Onde imprimir 1–2 exemplares no Brasil: para tiragem unitária, existem dois caminhos. (a) Uma gráfica digital / gráfica rápida que simplesmente imprima seu PDF — normalmente o mais barato e o mais flexível quanto a papel e acabamento; procure também encadernadoras e copiadoras próximas de universidades, que fazem isso rotineiramente e barato. (b) Plataformas de autopublicação sob demanda (UICLAP, AGBook, Clube de Autores e similares) permitem pedir exemplares próprios sem tiragem mínima, mas envolvem publicar o título na plataforma, o que é burocracia desnecessária para uso pessoal — e algumas têm restrições de política para obras de domínio público. Não tenho certeza de preços e condições atuais de nenhuma delas; vale cotar direto. Para 1–2 cópias, eu tentaria (a) primeiro.

Ah, e você não precisa de ISBN nem de ficha catalográfica para exemplares de uso pessoal.

### 11. O teste que evita 90% das frustrações

Antes de mandar o livro inteiro: imprima 8 a 16 páginas em casa, no tamanho final (corte o A4 na medida certa), dobre, empilhe, segure na mão e leia de verdade por dez minutos. Você vai descobrir instantaneamente que o corpo está pequeno, ou que a margem interna sufoca, ou que a fonte fica cinzenta. Na tela, tudo parece ótimo. No papel, não.

Depois, faça um exemplar de prova na gráfica antes dos definitivos. Sempre.

### 12. Para estudar de verdade

- Emanuel Araújo, A Construção do Livro — a referência brasileira, completa, do projeto gráfico à impressão. Se você comprar um livro só, compre este.
- Jan Tschichold, A Forma do Livro (Ateliê Editorial) — ensaios sobre proporção, margens e a tradição do livro. Curto e transformador.
- Robert Bringhurst, Elementos do Estilo Tipográfico — a bíblia da tipografia; a edição brasileira anda difícil de achar, mas vale a caça.
- Mitchell & Wightman, Book Typography: A Designer's Manual — o mais prático de todos, cheio de exemplos comentados. Em inglês.
- Richard Hendel, On Book Design — designers explicando as decisões de projetos reais.

E o exercício mais barato e mais eficaz: pegue cinco livros que você acha bonitos na sua estante, meça as margens com régua, identifique a fonte, conte os caracteres por linha, veja como abrem os capítulos. Copiar deliberadamente um projeto que funciona é a melhor escola.

Uma receita completa, para você começar hoje:

Formato 14 × 21 cm · margens 16/19/18/22 mm espelhadas · mancha 105 × 170 mm · EB Garamond 11,5/15 com algarismos antigos · justificado com hifenização pt-BR · recuo de parágrafo 5 mm, sem recuo no primeiro · fólio centralizado no pé, sem cabeço · capítulos abrindo em página ímpar, título em versaletes · papel pólen soft 80 g · capa em cartão 300 g laminado fosco

Isso já é um livro bem-feito.

Se você me disser qual obra (e em que língua) e se prefere um resultado clássico-tradicional ou algo mais contemporâneo, eu fecho um projeto gráfico específico — e posso montar o esqueleto do arquivo em Typst ou LaTeX, se você quiser seguir por esse caminho.

### Learn more

- Como encontrar prestadoras de impressão de livros sob demanda
- As melhores plataformas de print on demand no Brasil
- Como os Escritores Podem Ganhar Mais com Suas Obras
- Entenda as vantagens da Impressão Sob Demanda!
- Agbook
- Como Funciona a Calculadora UICLAP / Dúvidas (FAQ) — Loja Uiclap
- A publicação gratuita é realmente uma boa opção para o mercado?

---

## Pergunta 3

Eu já brinquei com o Typst (não vejo látex desda faculdade…), gostei muito. Minha ideia é gerar PDFs e depois imprimir eu mesmo (tenho uma Epson Ecotank L4360 com preto pigmentado. Eu baixei o Affinity Publisher, mas não usei ainda. Estava pensando no Affinity para detalhes, cólofon , capa, etc. Eu desisti de usar gráficas por enquanto: as duas encomendas que fiz ficaram horríveis. Depois vou pensar em uma laser. Eu mesmo estou fazendo a costura (faço a impressão em A4, dobrando o livro fica em A5) Capa papel Holer, folha de guarda em papel verge. Em breve vou começar a experimentar couro. Meu objetivo são livros de arte, alta qualidade, alto valor. Os livros que comecei são algumas obras de filosofia (meditações de Marcos Aurélio, Platão, etc. 2500 anos já deve ter vencido o direito autoral…)

## Resposta 3 (Claude-Opus-5)

### [Raciocínio]

Ótimo — você está num ponto muito mais avançado do que a resposta anterior supunha, e o gargalo da sua qualidade não é mais tipografia: é papel, geometria de refile e o comportamento do jato de tinta. Vou nessa ordem.

### 1. O item nº 1 da sua lista: sentido das fibras

Isso vale mais que qualquer decisão tipográfica que você tomar.

Você imprime A4 e dobra ao meio → o vinco é vertical, com 210 mm de altura, e a lombada fica nesse eixo. A fibra tem que correr paralela à lombada, ou seja, paralela ao lado de 210 mm.

Mas o A4 vendido em resma é grão longo (fibra paralela ao lado de 297 mm) — isto é, perpendicular à sua dobra. Consequências, todas visíveis num livro de arte:

- o vinco resiste, estala e às vezes racha as fibras
- o caderno "mola", não assenta, e o livro não abre plano
- as páginas não caem (sem drape), e viram como cartolina
- a ondulação causada pela água da tinta se acumula no sentido errado

Soluções, em ordem de preferência:

- Comprar folhas grandes (66 × 96 ou 76 × 112 cm) do papel que você quer e cortar A4 grão curto. É o caminho certo, e ainda te dá acesso a papéis muito melhores que os de resma.
- Pedir ao distribuidor "A4 grão curto / SG" — existe, mas é encomenda.
- Papéis de arte em folha (Fabriano, Canson, Hahnemühle, Arches) já vêm em formatos grandes; você escolhe o eixo do corte.

Teste do grão em 5 segundos: dobre a folha frouxamente nos dois sentidos sem marcar — ela cede com menos resistência na direção da fibra. Ou umedeça uma tirinha: ela enrola com o eixo paralelo à fibra. Faça isso com toda resma nova, inclusive com o vergê das guardas (a guarda também tem que ter a fibra paralela à lombada, senão ela empena a capa depois de colada).

### 2. Geometria: página não-refilada × formato final

Você vai ter creep (as folhas internas do caderno avançam para fora) e vai querer refilar as três bordas depois de costurar. Então não projete para A5: projete para o formato refilado, e coloque a sobra de refile dentro das margens.

Receita exata que fecha sem nenhum escalonamento:

| | |
| --- | --- |
| Folha | A4 paisagem, 297 × 210 mm |
| Página não-refilada | 148,5 × 210 mm (metade exata) |
| Refile | 3,5 mm na dianteira · 2,5 mm cabeça · 3,5 mm pé |
| Formato final | 145 × 204 mm |

Margens a declarar no Typst (já somando o refile):

- interna 15 mm (livro costurado abre plano; não precisa do exagero da lombada colada)
- externa 18 + 3,5 = 21,5 mm
- superior 16 + 2,5 = 18,5 mm
- inferior 22 + 3,5 = 25,5 mm
- → mancha 112 × 160 mm, e depois de refilar você tem exatamente 15/18/16/22 no livro pronto

A vantagem de fazer assim: duas páginas de 148,5 mm somam 297 mm = A4 exato. Nenhum redimensionamento em nenhuma etapa. Isso importa muito, porque qualquer escala de 98% no driver da impressora destrói o casamento das páginas.

### 3. Imposição

Apareceu recentemente uma ferramenta feita exatamente para o seu caso: typst-post (PyPI), que faz imposição 2-up em cadernos:

```
typst-post booklet livro.pdf --signature 16
```

--signature 16 = cadernos de 4 folhas encaixadas, que é o ponto ideal para papel de 100–120 g. Por padrão ela gera spreads com exatamente o dobro da largura da página de entrada — ou seja, com a geometria acima, sai A4 paisagem sem escalar nada. Alternativas maduras: pdfbook2 (--signature=16, com --no-crop obrigatório no seu caso) ou pdfjam --signature 16.

Duas notas:

- Nenhuma dessas faz compensação de creep (deslocar progressivamente a mancha nas folhas internas). Como você refila, não precisa — o refile resolve o creep por definição. Mas isso significa que refilar não é opcional.
- Papel mais grosso → caderno mais fino. Com 120 g, considere 3 folhas (12 pp) em vez de 4, senão o creep e o swell da costura crescem demais.

### 4. A impressora: onde a L4360 ajuda e onde ela trava

Limite de gramatura. A L4360 tem só bandeja frontal (100 folhas) e duplex automático, sem caminho reto traseiro. Isso te limita, na prática, a algo em torno de 90–120 g/m², e o papel tem que ser razoavelmente liso e rígido. Para "livro de arte" isso é uma restrição séria: os papéis realmente bons (algodão, 140–200 g, superfície com textura) não vão passar por uma curva de bandeja frontal. Vale testar até onde ela vai antes de projetar em cima de um papel que ela não aceita.

Duplex manual, sempre. O duplex automático não vai lidar com papel pesado e, mais importante, o registro frente/verso dele costuma variar 0,5–1,5 mm. Num livro fino de papel de qualidade, ver a mancha da página seguinte desalinhada contra a luz é justamente o tipo de detalhe que separa "artesanal" de "amador". Faça manual, imprima uma folha de teste com cruzetas de registro nos quatro cantos, meça, e corrija o offset na imposição se houver desvio sistemático. E desligue qualquer "ajustar à página" — imprima em tamanho real / 100%.

Preto pigmentado: cuidado com o modo de papel. Em impressoras Epson com preto pigmentado + cores em corante, o pigmento normalmente é usado apenas nos modos de papel comum; ao selecionar "papel fotográfico/matte", o driver pode compor o preto com as tintas coloridas. Se isso acontecer, você perde a resistência à água e a nitidez que são a razão de você ter escolhido essa impressora. Teste: imprima um bloco de texto em cada modo, espere secar 24 h, pingue água. Se borrar, aquele modo não é pigmento. Escolha o modo com base nesse teste, não no nome do papel.

K puro, ponto. Nada de preto rico, nada de cinza composto, nada de cor. Os corantes CMY não são estáveis à luz — num livro que você quer que dure, eles são um passivo. Um miolo 100% K em papel bom, com capitulares ou rubricas aplicadas à mão em vermelho (aquarela, guache, ou um bico de pena) é mais fine press que qualquer coisa que a impressora faça em cor. Aproveite que são 1–2 exemplares.

Ondulação (cockling) e secagem. A água da tinta expande a fibra localmente; página com muito texto ondula. Mitigação: use qualidade "Normal/Padrão" em vez do máximo (menos tinta, e a 1440 dpi o texto já está ótimo), imprima com a fibra correta, deixe as folhas secar 24 h intercaladas, e depois prense as folhas planas entre tábuas por 24–48 h antes de dobrar. Não dobre folha recém-impressa: a tinta ainda migra e você marca a página oposta.

Sobre a laser: eu repensaria. Para volume e custo, laser ganha. Para livro de arte, geralmente perde: o toner fica sobre a superfície com um brilho plástico perceptível, achata a textura do papel, e — crítico para você — pode craquelar na dobra, especialmente em papel encorpado e em áreas de preto chapado. Jato de tinta pigmentado em papel de algodão é o padrão da encadernação fina contemporânea, não a exceção.

O upgrade que faz sentido no seu projeto não é laser, é uma Epson SureColor P700/P900 (ou similar com pigmento em múltiplas tintas): caminho reto para mídia espessa, aceita papel de arte de 300 g+, preto matte próprio, e formato A3+/A2+ — o que te abre imprimir A5 em 4-up a partir de A3, ou fazer livros maiores. É outra faixa de preço, mas é o degrau real.

### 5. Typst: esqueleto para o seu caso

```typst
// ---- geometria: página NÃO refilada, margens já com sobra de refile ----
#set page(
  width: 148.5mm, height: 210mm,
  margin: (inside: 15mm, outside: 21.5mm, top: 18.5mm, bottom: 25.5mm),
  binding: left,
  numbering: "1",
  number-align: center + bottom,
)

#set text(
  font: "EB Garamond",
  size: 11.5pt,
  lang: "pt", region: "br",
  hyphenate: true,
  number-type: "old-style",
  // penalidades tipográficas: viúvas, órfãs, linhas-runt e hifenização
  costs: (hyphenation: 200%, runt: 400%, widow: 300%, orphan: 300%),
)

#set par(
  justify: true,
  leading: 0.78em,
  spacing: 0.78em,              // sem espaço extra entre parágrafos
  first-line-indent: (amount: 1.2em, all: false),
)

// ---- abertura de capítulo em ímpar, título em versaletes ----
#show heading.where(level: 1): it => {
  pagebreak(to: "odd", weak: true)
  v(8mm)
  align(center, text(size: 12pt, tracking: 0.08em, smallcaps(it.body)))
  v(12mm)
}
```

Três recursos que vale conhecer:

- text.costs é o equivalente Typst do controle de viúvas/órfãs, e é onde se ganha uniformidade de página. Aumentar runt evita a palavra sozinha fechando parágrafo — configure e esqueça.
- hydra (Typst Universe) resolve cabeços inteligentes (título do capítulo no recto, obra no verso, suprimido nas páginas de abertura), que é surpreendentemente chato de fazer à mão.
- droplet para capitulares, marginalia para notas de margem.

Numeração Stephanus / Bekker / livro.parágrafo — indispensável em Platão e Marco Aurélio, e o detalhe que faz a edição parecer séria. Esboço, colocando a referência sempre na margem externa:

```typst
#let ref(n) = context {
  let extern = if calc.odd(here().page()) { right } else { left }
  place(extern, dx: if extern == right { 20mm } else { -20mm },
        text(size: 8pt, style: "italic", fill: luma(35%), n))
}
```

Limitação honesta: o Typst faz quebra de linha otimizada por parágrafo inteiro (equivalente ao Knuth–Plass), mas não tem ainda protrusão/expansão de caracteres à la microtype — ou seja, sem pontuação pendurada na margem óptica. É a única coisa em que o LaTeX ainda está claramente à frente para texto corrido. Numa página de prosa filosófica, a diferença é pequena; num livro de poesia com muitas linhas terminando em vírgula, dá para notar.

Grego politônico e texto bilíngue: se você quiser Grego/Português em páginas espelhadas sincronizadas, o Typst não tem nada equivalente ao reledpar do LaTeX — é trabalho manual com grid, e vira um inferno em 200 páginas. Meu conselho: faça monolíngue com referências marginais, que é mais bonito e mais legível de qualquer forma.

### 6. Fontes

Para grego politônico bem desenhado e gratuito: EB Garamond (tem grego), Cardo e Brill (ambas feitas para classicistas; Brill é livre para uso não comercial), Junicode, Libertinus Serif, e as GFS (Didot, Porson).

Uma revisão importante do que eu disse antes, agora que sei que é jato de tinta em papel não revestido: a EB Garamond pode te decepcionar. Ela tem hastes finas e serifas delicadas, e o dot gain do jato em papel absorvente engrossa e acinzenta justamente isso. Faça um teste comparativo impresso — mesma página, mesmas medidas — com EB Garamond, Junicode, Literata e Libertinus Serif, e talvez em 12 pt em vez de 11,5. Fontes com traço um pouco mais robusto costumam ganhar nesse suporte, e "ganhar" aqui significa parecer impresso em vez de fotocopiado.

### 7. O que fazer no Affinity

Seu instinto está certo: Typst para o rio de texto, Affinity para as peças únicas. Concretamente:

- folha de rosto com entreletra e hierarquia ajustadas à mão (uma página de rosto vale meia hora de ajuste óptico)
- vinhetas, filetes, ornamentos, marca/dispositivo do "editor"
- cólofon
- rótulo de lombada (essencial se a capa for couro liso sem gravação)
- padrões para as guardas — papel de pasta (paste paper) impresso, ou desenho para papel marmorizado
- gabaritos para gravação/dourado a ferro na capa, quando você chegar no couro

Depois traga essas páginas para o documento principal como imagem vetorial (versões recentes do Typst aceitam PDF em #image; se a sua não aceitar, exporte SVG ou use o pacote muchpdf). Assim a paginação e a contagem de cadernos permanecem sob controle de um único arquivo — que é o que você quer quando descobre, na hora de impor, que faltam 4 páginas para fechar o caderno.

### 8. Encadernação: os números da cartonagem

Como você já costura, só os pontos onde as contas erram:

- Papelão Holler: para 145 × 204 mm, use 1,5–2,0 mm. Mais fino empena; mais grosso fica desproporcional.
- Altura das capas = altura do miolo + 2 × 3 mm (as "praças"/squares).
- Largura das capas ≈ largura do miolo + 3 mm de praça − a folga da charneira (≈ espessura do papelão + 1 mm). Na prática, para 2 mm de papelão, isso dá quase exatamente a largura do miolo. Sempre confira num protótipo em papelão vagabundo antes de cortar o Holler.
- Charneira (French groove): folga de ~1,5 × a espessura do papelão.
- Largura da lombada da capa = espessura do miolo medida no ombro, depois de prensado e arredondado + 2 × espessura do papelão. Meça com paquímetro, nunca calcule pelo número de folhas — a costura adiciona swell e a prensagem tira; só a medida real serve.
- Material de cobertura: largura total = 2 × largura da capa + lombada + 2 × charneira + 15–20 mm de virada em toda a volta. Para couro, mais folga, porque você vai desbastar (parar) as bordas — e é aí que mora a diferença entre couro artesanal bonito e couro artesanal grosso. Comece por meia-encadernação (lombada e cantos em couro, resto em papel decorado): você aprende o desbaste em áreas pequenas, com muito menos risco de estragar uma peça inteira.
- Guardas em vergê: fibra paralela à lombada, e prefira 120–160 g. Vergê leve encarquilha com PVA. Cole com adesivo mais seco (PVA levemente engrossado ou metilcelulose) e prense imediatamente.

### 9. O cólofon

Numa edição de dois exemplares, o cólofon é onde o objeto se torna documento. Registre: obra e edição-fonte exata do texto; tradutor, se houver; fontes tipográficas e corpos; sistema de composição; papel do miolo e das guardas, com gramatura; técnica de impressão; formato refilado; estrutura de costura; material da capa; local, data e "exemplar 1 de 2", assinado. Daqui a trinta anos essa é a página que vai valer mais que a capa.

### 10. A pegadinha que o seu parêntese revela 🙂

Marco Aurélio e Platão estão em domínio público — em grego. O que você quase certamente vai usar é uma tradução moderna, e essa tem direito autoral próprio, de 70 anos após a morte do tradutor. Ou seja: o texto grego de Schenkl é livre; a tradução do Ísis Borges da Fonseca ou do Mário da Gama Kury, não.

Vale saber que a Lei 9.610/98 não tem exceção de cópia integral para uso privado (o art. 46, II só cobre "pequenos trechos") — a permissão ampla de cópia única existia na lei de 1973 e não sobreviveu. Para dois exemplares na sua estante, o risco prático é zero e ninguém vai te procurar. Mas se algum dia você pensar em vender ou expor esses livros, o problema deixa de ser teórico.

Caminhos limpos: texto grego (Perseus, Open Greek and Latin / First1KGreek — bons arquivos, marcação TEI XML que dá trabalho mas é confiável); traduções antigas em domínio público (em inglês, George Long 1862 e Meric Casaubon 1634 para as Meditações; em português, procure no Wikisource e verifique a data de morte do tradutor); ou traduções com licença livre.

Se eu tivesse que te dar uma única tarefa para este fim de semana: corte doze folhas A4 grão curto do papel candidato, imprima duas páginas de teste em quatro fontes diferentes e dois corpos, faça o teste da água nos modos de papel do driver, monte um caderno de 16 páginas, prense, costure, refile e leia. Você vai decidir 80% do projeto gráfico em duas horas — e vai descobrir os dois ou três problemas que nenhum manual te contaria.

Se quiser, me diga qual obra vai primeiro (e se em grego ou português) e eu monto o arquivo Typst completo — com aparato de referência stephaniana ou livro.parágrafo, cabeços, cólofon e a imposição já parametrizada.

### Learn more

- typst-post — imposição de cadernos a partir de PDF do Typst (PyPI)
- Discussão sobre imposição 2-up e 4-up no fórum do Typst
- pdfbook2 — README
- Especificações da Epson EcoTank L4360
- Typst — exportação de PDF e padrões suportados

---

## Pergunta 4

Eu recebi uma recomendação de um editor para usar Libertinus Serif para um livro em A5. É um boa fonte?

## Resposta 4 (Claude-Opus-5)

### [Raciocínio]

### Veredito curto

Sim, é uma boa fonte — e é uma recomendação especialmente coerente para A5. Não é a escolha mais "sedutora" que existe, mas é sólida, bem-construída, completíssima e difícil de errar. Se o seu editor sugeriu isso, ele provavelmente pensou em três coisas: economia de largura, cobertura de caracteres e o fato de ela ter versaletes e algarismos antigos de verdade.

### O que ela é, exatamente

Libertinus é um fork do Linux Libertine, iniciado em 2012 por Khaled Hosny (originalmente só para criar uma fonte matemática companheira) e que virou uma revisão completa, corrigindo muitos bugs do original. Desde 2020 a manutenção está com Caleb Maclennan. Licença OFL, gratuita.

Genealogicamente, o Linux Libertine foi concebido por Philipp Poll como alternativa livre ao Times, mas o desenho é mais interessante que isso: inspirado em tipos de livro do século XIX, com um ar humanista/transicional, ligeiramente caligráfico. É mais quente e menos "burocrática" que Times, e mais neutra que uma Garamond.

A família inclui:

- Libertinus Serif — 3 pesos (Regular, Semibold, Bold) × 2 estilos
- Libertinus Serif Display — variante otimizada para corpos grandes
- Libertinus Serif Initials — capitulares vazadas/ornamentadas
- Sans (ex-Biolinum, baseada na Optima), Mono, Math, Keyboard

### Os pontos fortes que importam no seu caso

1. É econômica em largura. Isso é o argumento decisivo para A5. Com uma mancha de ~110 mm, Libertinus a 11 pt te dá algo em torno de 65–70 caracteres por linha — exatamente a faixa ideal. Uma fonte mais larga te obrigaria a descer para 10 pt e o livro ficaria com cara de manual.

2. Recursos OpenType completos e reais. Versaletes verdadeiros (smcp), maiúsculas→versaletes (c2sc), algarismos antigos (onum), tabulares/proporcionais, ligaduras, conjuntos estilísticos. Nada de versalete falso.

3. Cobertura de caracteres absurda. Mais de 2.000 glifos, com grego, cirílico e hebraico. Para obras de domínio público isso é ouro: clássicos citam grego, latim com macrons, francês, guilhemets « », abreviaturas antigas. Português está 100% coberto, obviamente.

4. Tem a Display e as Initials. Poucas famílias gratuitas oferecem isso. Use a Display na folha de rosto e nos títulos de capítulo — em corpo grande ela tem espacejamento mais apertado e detalhes mais finos, e a diferença é visível. As Initials dão capitulares para abertura de capítulo, o que combina perfeitamente com um clássico.

5. Se houver qualquer matemática ou notação, a Libertinus Math casa perfeitamente. Improvável no seu projeto, mas é a razão de existir do fork.

### Onde ela cobra o preço — e o que fazer

O Regular é levinho. Esse é o ponto de atenção real. A cor da página tende ao cinza claro, sobretudo em impressão digital a toner, que costuma "afinar" os traços finos. Três mitigações: (a) não use menos de 11 pt; (b) papel pólen soft ajuda, porque a leve absorção engorda o traço — muito melhor que sulfite branco liso aqui; (c) faça o teste impresso antes de decidir o corpo. Não caia na tentação de usar Semibold para texto corrido — fica pesado e errado.

O itálico é o elo mais fraco. É um itálico genuíno e bonito, mas herdou do Linux Libertine um espacejamento menos polido que o romano, um pouco estreito e caligráfico. Para ênfases e títulos de obras, ótimo. Se seu livro tiver páginas inteiras em itálico (cartas, sonhos, epígrafes longas), inspecione com cuidado.

O Bold é escuro e contrastado. Prefira Semibold onde você usaria negrito — em títulos, cabeços, folha de rosto. Fica muito mais elegante.

Ela tem "cara de LaTeX" para quem convive com LaTeX. Junto com a Computer Modern, é a fonte mais associada a documentos acadêmicos livres — e é a fonte histórica do logotipo e da tipografia da Wikipédia. Quem não é do meio não nota nada; quem é, reconhece na hora. O registro emocional dela é erudito, sóbrio, editorial — perfeito para ensaio, filosofia, história, um clássico com aparato de notas. Menos indicada se você quisesse algo lírico, sensual ou marcadamente literário — aí uma EB Garamond ou Alegreya tem mais alma.

Kerning e espacejamento em pares raros ainda mostram alguma irregularidade herdada do original, e Semibold Italic / Bold Italic são as instâncias menos refinadas. Nada grave; só revise títulos e linhas em destaque, onde defeitos aparecem ampliados.

### Receita concreta para A5 com Libertinus

- Formato 148 × 210 mm
- Margens espelhadas interna 17 · superior 17 · externa 19 · inferior 22 mm (+3–4 mm na interna se passar de 250 páginas)
- Mancha ≈ 112 × 171 mm
- Texto Libertinus Serif Regular 11 / 15,5 pt — ou 11,5/16 se você gosta de leitura folgada
- Justificado, hifenização pt-BR obrigatoriamente ativa
- Recuo 5 mm; sem recuo no primeiro parágrafo do capítulo
- onum ativado no texto corrido (o padrão da fonte é algarismo alinhado)
- Primeiras 3–5 palavras do capítulo em versaletes (smcp + c2sc), com leve tracking positivo (~+5/1000)
- Título de capítulo Libertinus Serif Display, ~18–20 pt, ou em versaletes espacejados
- Fólio no pé, 9,5 pt, com algarismos antigos
- Papel pólen soft 80 g

Sobre a justificação: português tem palavras longas e A5 é estreito. Sem hifenização bem configurada, você terá rios de branco feios — e como a Libertinus é clarinha, os buracos ficam ainda mais evidentes. Se estiver em LaTeX/Typst, o algoritmo já resolve; em InDesign/Affinity, use o Adobe Paragraph Composer (composição por parágrafo, não por linha).

### Como instalar sem dor de cabeça

Baixe direto dos releases oficiais no GitHub (o repositório é alerque/libertinus; a série atual é a 7.0x). Não pegue de sites agregadores de fontes, que distribuem versões antigas.

Um detalhe prático: se você já tiver o Linux Libertine O instalado, desinstale. Conviver com as duas famílias gera conflito de nomes e você acaba compondo com a versão errada sem perceber. O projeto está em ritmo lento de desenvolvimento hoje — maduro, não abandonado —, mas não tenho certeza do nível de atividade nos últimos meses.

Em LaTeX: \usepackage{libertinus-otf} com LuaLaTeX/XeLaTeX (o pacote já oferece variantes com onum, versaletes etc. configuradas). Em Typst: #set text(font: "Libertinus Serif", size: 11pt). Em Affinity/InDesign: instale os .otf e ative as features no painel de tipografia, guardando tudo em estilos de parágrafo — nunca aplique feature manualmente página por página.

### Comparação honesta

| | Caráter | Peso na página | Melhor para |
| --- | --- | --- | --- |
| Libertinus Serif | Erudito, sóbrio, neutro-quente | Leve | Ensaio, clássicos, texto com grego/notas |
| EB Garamond | Histórico, delicado | Muito leve | Literatura, poesia, séculos XVI–XVIII |
| Literata | Contemporâneo, robusto | Médio-forte | Prosa longa, leitura confortável |
| Source Serif 4 | Neutro, técnico | Médio | Não-ficção, qualquer coisa |
| Alegreya | Caloroso, com personalidade | Médio | Ficção, narrativa |

Se a Libertinus te parecer clara demais no teste impresso, a substituição mais indolor é Literata ou Source Serif 4 — ambas mais escuras, e nenhuma exige rediagramação séria.

Conclusão: aceite a recomendação. É uma escolha tecnicamente muito bem justificada para A5, com recursos que a maioria das fontes gratuitas não tem, e o único cuidado real é não usar corpo pequeno demais e confirmar a cor da página num teste impresso.

Me diz qual é a obra e eu ajusto o corpo, a entrelinha e a hierarquia de títulos ao texto específico — se for algo com muitas notas, diálogo intenso ou citações em outra língua, essas decisões mudam bastante.

### Learn more

- Libertinus
- Releases · alerque/libertinus
- alerque/libertinus: The Libertinus font family · GitHub
- https://osl.ugr.es/CTAN/fonts/libertinus-otf/doc/libertinus-otf-doc.pdf
- Libertinus OpenType Features
- skef/libertinus: Libertinus font family
- nathanvanbakel/libertinus: The Libertinus font family
- Is it possible to use Linux Libertine as a mathematical font?
