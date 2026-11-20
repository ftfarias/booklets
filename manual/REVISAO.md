# Revisão do manual

Um arquivo só para a revisão (junta o antigo `SUGESTOES.md`, da leitura
integral de 17/11, com o registro das mudanças):

- **O que falta** — a lista de trabalho. Quando um item é feito, sai daqui
  e vira linha no registro.
- **O que foi feito** — cada mudança, onde e por quê, para a sua revisão
  depois. Mudança de conteúdo (fato, número, recomendação) vem marcada com
  **[conteúdo]** ou **[erro]**; ajuste de forma, com [forma].

Legenda dos itens em aberto: **[erro]** fato ou conta provavelmente
errado · **[conferir]** afirmação sem fonte firme · **[incoerência]** dois
trechos que não combinam · **[lacuna]** assunto prometido que não está lá ·
**[melhoria]** conteúdo ou organização · **[forma]** redação, grafia,
diagramação.

## Andamento

| | |
|---|---|
| Capítulos revisados | 1 a 18 (e o 6 dividido, 19/11) |
| Próximo | 19 · Caixas, estojos e proteção |
| Depois | 20 e 21; apêndices B, C, F; `MANUAL.md` |
| No fim | itens gerais abaixo; passada de layout; cadernos e páginas em branco |
| Erros de fato da leitura integral | todos corrigidos (17/11) |

---

# O que falta

## Gerais

### A. Achar as coisas no livro impresso

Era a queixa original ("ficava louco olhando conversa por conversa"). Os
capítulos já saem numerados (17/11); falta o resto:

1. **Não há índice remissivo.** Num livro de consulta de 300 páginas, é a
   ferramenta que falta: "cola de coelho → 133, 138, 191". Dá para gerar
   sozinho — o `check.py` já extrai o texto de cada página; uma lista de
   termos (o glossário é meio caminho) vira índice com números de página.
2. **A tabela "Onde encontrar — perguntas frequentes" só existe no
   `MANUAL.md`**, que não entra no livro. É exatamente o guia por pergunta
   que o leitor quer nas primeiras páginas, com número de página. (Hoje ela
   tem pelo menos duas entradas velhas: "corino → cap. 14" — está no 13 — e
   "filete sem equipamento → cap. 15" — está no 16. A lista de regras pula
   do 7 para o 9.)
3. **O apêndice A não responde à pergunta que você deu de exemplo** ("qual
   a proporção de água e cola de coelho?"). A tabela "Proporções num
   relance", do cap. 10, não está em A nem em D: o gerador só colhe a
   primeira tabela de "consulta rápida" de cada capítulo, e em D entrou a
   de gelatinização dos amidos. Em compensação, A abre com a linha do tempo
   da história do livro e o vocabulário da anatomia, que ninguém procura
   num apêndice de consulta. O apêndice A merece curadoria à mão: receitas
   e proporções, temperaturas, gramaturas, folgas, tempos de espera.

### B. Lacunas — o que o livro promete e não tem

1. **O *casing-in*** — colar o bloco na capa feita à parte. É a operação
   central da rota que o estúdio usa, e está numa linha de bloco de código.
2. **Colar a guarda na pasta**: há as defesas contra a ondulação, não o
   procedimento.
3. **Recolocar um livro na capa** (*recasing*) — o conserto mais pedido.
4. **Peças e medidas das caixas** (slipcase e clamshell).
5. **Conservação preventiva** — como guardar e cuidar dos livros que já
   existem. O cap. 21 é um roteiro de estudo, não um capítulo.

### C. O livro contra as próprias regras

- **Margens.** O cap. 4 ensina interna < superior < externa < inferior. O
  manual está com interna 21 / externa 15 / superior 18 / inferior 20 mm.
  Depois do refile que o próprio cap. 4 recomenda (3,5 / 2,5 / 3,5 mm), a
  margem externa cai para **11,5 mm** contra 21 da interna — a "assinatura
  visual da apostila" de que o capítulo fala. Num livro costurado sobre
  fitas, com lombada oca, a interna não precisa de 21. Sugestão: a receita
  do próprio capítulo para página refilada (15 / 21,5 / 18,5 / 25,5, página
  de 148,5 mm), ou algo próximo.
- **Cadernos.** O `cadernos.py` só minimiza páginas em branco e hoje
  escolhe **25 cadernos de 3 folhas**. Mais costura e mais *swell* do que o
  cap. 8 aceita (ver nota do cap. 8). Dezenove cadernos de 4 folhas, com 8 páginas
  de "Notas" no fim, servem melhor a um manual pessoal.
- **Corpo e medida.** 10 pt e ~74 caracteres, onde o cap. 4 pede 10,5 e
  60–70. Você já decidiu manter; falta só dizer no livro que é exceção
  consciente.
- **Colofão.** O cap. 4 diz que o colofão registra fonte, **papel**, quem
  imprimiu e o ano. O do manual não diz o papel. E o ano do colofão é
  calculado na compilação, enquanto o da capa está fixo em 2026.
- **Capa.** O mote de Sêneca vai sem autor nem tradução; o do colofão tem
  tradução. Uma linha "— Sêneca, *Hércules furioso*" combinaria.

### D. Estrutura

- **Cap. 8:** a teoria do *swell* vem depois do exemplo que a usa.
- **Cap. 21:** não passou pela reorganização (sem consulta rápida, recados
  pessoais, referências duvidosas).
- **Ap. F:** a sequência principal é a laçada em couro; a rota do estúdio
  (fitas + capa à parte) ficou como variante.
- **Parte III se chama "Da costura à capa"**, mas a costura (cap. 8) e o
  bloco (cap. 9) estão na Parte II.
- **Caps. 3, 5** não têm seção Fontes; os outros têm.

### E. Voz e resíduos

- **Restos das conversas de origem.** Caixas "⚠️ Divergência nas fontes: uma
  conversa diz… outra responde…" (cap. 4); "migrado do capítulo
  de douração", "estavam no NEGOCIO.md e migraram para cá" (Fontes do
  cap. 19).
- **Voz de negócio**, que você pediu fora do manual: seção "Preço" e várias
  frases do cap. 19; "cliente" no cap. 20; "mata a margem" (ap. C);
  "decisão de preço" (ap. F).
- **Arquivos que o leitor do livro não tem:** `NEGOCIO.md`, `CAMINHOS.md`,
  `../CLAUDE.md` (cap. 19; ap. C, F).
- **Preços** espalhados pelo texto (ouro por grama, livrete, bolo, clichê,
  impressoras): todos de 2026. Ou vão para o apêndice C com a data, ou
  ganham o ano ao lado.
- **Grafias e nomes que variam:** couché/couchê · verge/vergê · canoa/tubo (lombada oca) · Scharffix/Scharf-Fix ·
  Derome/Derôme · percalux/Percalux · guarda colada/contraguarda ·
  "caixa" para *case binding* e para as caixas do cap. 19 · "Parte I…II"
  dentro do cap. 4.

### F. Diagramação (PDF de 17/11, 296 páginas — os números já mudaram)

- **Títulos órfãos** no pé da página: físicas 278 ("Espessuras"), 279
  ("Amidos") e 281 ("Temperatura por material"), todas no apêndice D — o
  título fica numa página e a tabela na seguinte.
- **Páginas com duas ou três linhas:** física 141 (fim do cap. 10: um item
  de lista sozinho), 264 (uma linha de tabela do cap. 20, com o cabeçalho
  repetido) e 288 (duas linhas do apêndice E).
- Cap. 16 (PDF de 19/11): a física 210 termina com um quarto de página em
  branco (a tabela "Problemas mais comuns" desce inteira para a seguinte);
  a 215 tem só as seis últimas linhas das Fontes.
- Fica para a passada final de layout, como combinado — só registro onde
  estão hoje.

## Por capítulo

### 1 · Breve história do livro

- [forma] Linha do tempo: "Antiguidade — tabuinha de cera" vem antes de
  "~3000 a.C. — rolo de papiro", o que sugere que a tabuinha é mais antiga.
  Trocar a ordem ou datar a tabuinha.
- [forma] "lacas, fólio" (corantes orgânicos da iluminura): o corante é o
  *folium* (tornassol). Num livro em que "fólio" é folha, confunde.
- [incoerência] A tabela "O século XIX industrializa → o que surgiu" lista a
  **lombada oca** como invenção do séc. XIX; o cap. 2 e o cap. 3 dizem
  (certo) que ela nasce no séc. XVIII com os Derome e se generaliza no XIX.
- [forma] "O digital e o POD tiraram do livro impresso até parte da função
  de transmitir texto" — POD é livro impresso; a frase tropeça. Talvez só "o
  digital".
- [melhoria] Aldo Manúcio: o itálico foi cortado por **Francesco Griffo**;
  vale o nome (o cap. 4 fala de tipos). A explicação "para caber mais
  texto" é a tradicional, mas discutida — bastaria "imitando a cursiva
  humanística".

### 2 · Anatomia do livro

- [forma] "o dicionário da Library of Congress é explícito" e, no parágrafo
  seguinte, "Roberts & Etherington observam": é o mesmo livro. Unificar.
- [conferir] Tabela francesa: *dos collé* para lombada aderente. O termo
  que mais vejo é ***dos plein***; *dos collé* não tenho certeza de que
  seja corrente. (Aparece também no cap. 3, A1 e B1.)
- [melhoria] "Mordente, ombro (*shoulder*)": em muita oficina brasileira a
  palavra é **encaixe** (o cap. 9 usa "encaixar" para *backing*). Vale
  registrar o sinônimo na tabela.

### 3 · Tipos de encadernação

- [conferir — importante] **Definição de Bradel.** O manual segue Roberts &
  Etherington (leitura histórica: pastas fendidas, capa feita à parte). No
  ensino atual (francês *à la Bradel*, alemão *gebrochener Rücken*), o que
  se chama Bradel é a capa de três peças **montada sobre o livro**: a peça
  de lombada é colada no bloco, as pastas são coladas sobre as abas dela
  deixando o canal, e o revestimento se faz com a capa já no livro. Vale
  registrar as duas leituras, como foi feito com "seixa" — e dizer qual
  delas o estúdio pratica. (Vale para os caps. 12 e 13.)
- [incoerência] Tabela do Eixo C: *longstitch* aparece em "sem suporte —
  ponto encadeado / *link stitch*". *Longstitch* não é ponto encadeado: é
  costura direta **através da capa**. (Pendência antiga: alinhar esta
  tabela com o cap. 8.)
- [forma] "marroquim de grão longo, *straight-grain morocco*" — é a mesma
  coisa dita duas vezes.
- [forma] "*dentelle* de **Derôme**": no resto do manual é Derome.
- [forma] "dourado sobre corte cinzelado = *gauffered*": o cinzelado é feito
  **sobre** o ouro, não o contrário. "Corte dourado e cinzelado".
- [forma] "Contraguarda — a guarda colada na pasta": o manual já tem "guarda
  colada" (cap. 2, 11) e "contra-folha" (cap. 12, outra coisa). Três nomes
  parecidos; talvez só mencionar que "contraguarda" existe e não usar.
- [melhoria] É o único capítulo da Parte I sem seção **Fontes**.

### 4 · Tipografia e editoração

- [incoerência — vale decidir] **O manual não segue as próprias regras de
  página.** O cap. 4 manda interna < superior < externa < inferior, corpo
  mínimo de 10,5 pt na Libertinus e 60–70 caracteres por linha; o manual
  está em 10 pt (≈74 caracteres) e com margens interna 21 / externa 15 /
  superior 18 / inferior 20 mm — interna **maior** que a externa, e
  inferior quase igual à superior. O 10 pt você já decidiu manter; falta
  só uma linha — no cap. 4 ou no colofão — dizendo que é exceção consciente
  de livro de consulta. A margem interna/externa vale olhar de novo (ver
  "Layout" no fim).
- [incoerência] "apara exatamente para o formato brasileiro clássico de
  13,5 × 21" — a tabela de formatos brasileiros, acima, lista 13,5 × **20,5**
  e 14 × 21; 13,5 × 21 não está lá.
- [conferir] "Verdana e **Inter** passam" no teste `Illegal 1O0`: na Inter
  padrão, `I` e `l` são duas barras lisas, só de alturas diferentes; ela só
  diferencia de verdade com o conjunto estilístico de desambiguação ligado.
  Exemplos mais seguros: Verdana, Atkinson Hyperlegible, IBM Plex Sans.
- [conferir] `typst-post` (PyPI) como ferramenta de imposição — não conheço
  esse pacote; confirmar que existe com esse nome.
- [forma] "o cânone puro de Van de Graaf reserva só 2/3 da página para a
  mancha": é 2/3 da largura **e** 2/3 da altura — 44 % da área. Dito assim
  o argumento ("gasta papel demais") fica mais forte.
- [forma] O capítulo se divide em "**Parte I** — Fundamentos" e "**Parte
  II** — Editoração", dentro de um livro que já tem Partes I a V. Trocar por
  outro nome (ou tirar o rótulo).
- [forma] A caixa "⚠️ Divergência nas fontes" (EB Garamond 11,5 pt) ainda
  fala em "uma das conversas de origem" e "uma resposta posterior" — é
  anotação de processo, como a que saiu do cap. 14. Reescrever como
  afirmação direta. A frase final tem dois travessões encavalados.
- [forma] Em "A ordem das páginas", uma linha em branco separa o item
  "Colofão" do resto da lista (vira lista nova no PDF).
- [melhoria] Hendel, *On Book Design*, tem edição brasileira (*O design do
  livro*, Ateliê). Bringhurst: conferir se a reedição recente está em
  catálogo antes de dizer "difícil de achar".

### 5 · Papel

- [incoerência] **Markatto** aparece como "muito liso" (junto com a opalina,
  na consulta rápida e em "Papel para a impressora") e como "brancos e
  cremes **texturados**" (em "Outras linhas" e na tabela comparativa). O
  capítulo diz também "texto pequeno em jato de tinta: nunca texturizado".
  Uma das duas descrições sobra — separar Opalina (lisa) de Markatto
  (texturado) resolve.
- [conferir] "Papelão cinza (Holler/Paraná)": no comércio os nomes se
  misturam, mas a rigor **Paraná** é o papelão cor de palha, de pasta de
  pinho, e o **cinza** é o de aparas recicladas. Vale uma linha, como a que
  já existe para "Horlle".
- [melhoria] "Um A3 com a fibra na direção certa dá dois A4 fibra curta":
  dito assim parece exigir um A3 especial. É o contrário — o **A3 comum, de
  fibra longa**, cortado ao meio, dá dois A4 de fibra curta. É a solução
  mais barata do capítulo e merece ser dita sem rodeio.
- [melhoria] Em "Detalhes técnicos", três itens não são de papel: "cola
  demais na lombada" (cap. 9/10), "encadernar com papel recém-impresso"
  (cap. 6), "prensar de menos". Sobraram de uma versão anterior.
- [forma] Sulfite "63 a 240 g/m²" no texto e "63–120" no quadro
  comparativo.
- [melhoria] Sem seção **Fontes** (o que vem do fabricante, o que vem das
  conversas).

### 6 · Impressão do miolo

Dividido em 19/11 (registro abaixo). Ficou:

- [forma] Grafias que variam entre os capítulos: **couché** (aqui) ×
  **couchê** (cap. 5); **vergê** (aqui) × **verge** (cap. 5). Escolher uma.
- [melhoria] Nota do cap. 5 sobre Markatto: este capítulo distingue
  "Markatto Concetto / Sumo (texturado)" da versão lisa — é só levar a
  mesma distinção para o cap. 5.
- [conferir] Que o preto da linha 504 é pigmentado e as cores são corante:
  o manual da Epson confirma a linha 504 na L4360, mas não achei a ficha
  que diga o tipo de tinta. O teste da gota, no próprio capítulo, decide.

### 7 · Cadernos e imposição

- [forma] "Sangria" é usada para a sobra de refile (aqui e no cap. 4). Em
  artes gráficas, sangria é a imagem que **passa** da linha de corte. Como
  o miolo não tem imagem sangrada, "sobra de refile" é mais exato.
- [forma] Fontes cita o verbete BOLT, mas o texto não fala de *bolt* (a
  dobra fechada que se abre com a faca). Ou entra uma linha, ou sai da
  lista.

### 8 · Costura

- [incoerência — importante na hora de imprimir] **O exemplo "escolher a
  costura deste manual" envelheceu, e o script de cadernos joga contra
  ele.** O exemplo fala em ~270 páginas e 17 cadernos de 4 folhas. O manual
  tem hoje 296 páginas e o `cadernos.py`, que só minimiza páginas em branco,
  escolhe **25 cadernos de 3 folhas** (4 brancas). Vinte e cinco cadernos
  finos são mais costura e mais *swell*: 25 × 0,35 mm = 8,8 mm sobre ~20 mm
  de papel, 44 % — fora da faixa de 25–35 % que o próprio capítulo dá. Com
  cadernos de 4 folhas seriam 19 cadernos e 8 páginas em branco, que num
  manual pessoal viram **páginas de "Notas"** no fim. Sugestão: o script
  pesar também o número de cadernos (ou fixar 16 para este livro), e o
  exemplo ser refeito por último, com os números finais.
- [conferir] **Diâmetros das linhas finas parecem baixos.** Pela conta do
  título do linho, 18/3 ≈ 0,58 mm e 25/3 ≈ 0,49 mm (batem com a tabela),
  mas 35/3 dá ≈ 0,41 mm (a tabela diz ~0,35) e 40/3–50/3, ≈ 0,39–0,35 mm (a
  tabela diz ~0,25). Como o exemplo do *swell* depende disso, vale medir as
  suas linhas — 20 voltas justas num lápis, medir com a régua, dividir por
  20 — e corrigir a tabela com o medido.
- [conferir] "Sobre nervos verdadeiros… **como abre:** bem, se a lombada for
  oca… **combina com:** lombada aderente ou oca". Nervo verdadeiro em relevo
  é, por construção, lombada **aderente** (o couro cola sobre os cordões —
  é isso que "flexível" quer dizer). A lombada oca vai sobre lombada lisa
  (fitas, cordões embutidos), com nervuras falsas — como o cap. 3 diz.
- [conferir] Japonesa, prática do estúdio: "furos a ~15 mm; a costura ocupa
  até ~22 mm; **margem interna de 20 mm**". Se a costura come 22 mm, 20 mm
  de margem deixa o texto dentro da zona que não abre. Um dos três números
  está trocado (conferir com os arquivos do Estoicos/Vulgata).
- [conferir] Rami "cerca de **2× o linho**" em tenacidade: as tabelas de
  fibras costumam pôr rami e linho na mesma faixa (o "8× o algodão" é o
  número de propaganda). Eu diria "comparável ao linho, ou um pouco acima".
- [incoerência] Bastidor: "datado do séc. XII… **nasce junto** com a costura
  sobre nervos" — mas o mesmo capítulo data a costura sobre nervos do séc.
  VIII. "Documentado desde o séc. XII" resolve.
- [melhoria — ordem] A seção "***Swell*** — o que é e como controlar" vem
  **depois** do exemplo que já usa o *swell*, a regra dos 25–35 % e a conta.
  Subir a teoria para antes do exemplo.
- [melhoria — repetição] "Cinco nervos; seis partes, cinco iguais e a do pé
  maior" aparece duas vezes no capítulo ("Marcar as estações" e "Nervuras e
  cordões → Espaçamento"). E o parágrafo dos cabeceados ("em uma ou duas
  cores, de duas voltas, à francesa, à inglesa, islâmico… colado
  pré-fabricado") está quase palavra por palavra no cap. 3.
- [forma] "Toda costura em cadernos tem *kettle stitch*" — a de um caderno
  só (sela) e várias *longstitch* não têm. "Toda costura de vários cadernos
  sobre suportes".
- [forma] Cordões duplos: "a única costura em que a linha corre de ponta a
  ponta **sem emenda útil**" — não entendi a frase; reescrever ou cortar.
- [forma] "**Sela**" para a costura de um caderno é tradução literal de
  *saddle*; o nome corrente aqui é **costura a cavalo** (ou "canoa", quando
  grampeada). E atenção: o cap. 5 usa "canoa" para o tubo da lombada oca —
  no jargão gráfico brasileiro "canoa" é justamente a lombada do folheto
  grampeado. Sugiro "tubo" no cap. 5.
- [forma] Rami: "é celulose **pura** (68–76 %)" — o adjetivo briga com o
  número. "Rica em celulose, quase sem lignina."

### 9 · Do miolo costurado ao bloco pronto

- [melhoria] "Refilar… abre os *bolts*": no método do estúdio (A4 dobrado
  uma vez) **não há *bolts*** — eles só existem em cadernos de duas ou mais
  dobras. Uma ressalva de meia linha evita o leitor procurar o que não tem.
- [melhoria — repetição] "8. Cabeceados" repete a seção "Cabeceados" do
  cap. 8 (alma, seda, "não use poliéster"). O lugar natural é aqui; no
  cap. 8 basta a remissão.
- [melhoria] Falta um passo que a prática costuma incluir entre costurar e
  encolar: **prensar o bloco costurado** (ou batê-lo) para assentar o
  *swell* antes da primeira cola. Hoje só aparece o "assente com batidas
  laterais se a lombada estiver esponjosa".

### 10 · Colas e adesivos

- [conferir] Cola proteica: "cola a lombada, espera **1–2 min** e já pode
  arredondar e encaixar". O gel se forma em um ou dois minutos, mas a
  janela de Cockerell citada no cap. 9 ("deixou de grudar, mas ainda não
  endureceu") costuma ser bem mais longa que isso. Eu não daria um número
  tão curto sem testar.
- [conferir] Ictiocola "quase não encolhe": a fama dela é de filme mais
  flexível e de menor tensão que a cola de pele; "encolhe menos" é mais
  seguro.
- [melhoria] **Amido de trigo** é o padrão-ouro do capítulo e o item mais
  difícil de achar; o kit não diz onde (o apêndice C diz "mercado", o que
  eu não daria por certo — ver nota lá).
- [forma] "percalux" em minúscula na consulta rápida; "Percalux" nos caps.
  5 e 13 (onde o manual já avisa que o nome não é confiável).

### 11 · Guardas

- [melhoria] Falta o gesto final que mais se erra: **como** colar a guarda
  na pasta (com o livro aberto ou fechando a capa sobre a guarda; barreira
  de umidade entre a guarda colada e a volante; aparar a guarda para a
  margem interna ficar igual nos três lados). Hoje há as "cinco defesas"
  contra a ondulação, mas não o procedimento.
- [melhoria] Cianotipia como guarda: "não tolera álcali" está dito, mas a
  consequência prática não — papel **tamponado** (o que o cap. 5 recomenda
  para durar) e PVA "neutro a levemente alcalino" (cap. 10) estão
  justamente do lado errado. Uma linha ligando os três capítulos.

### 12 · Montagem da capa

- [conferir — ver cap. 3] **Bradel.** O texto descreve "capa montada fora
  do livro e revestida antes de encontrar o miolo" **e** "pastas fendidas
  onde entram as fitas". Roberts & Etherington de fato registram a fenda
  parando a uma polegada da cabeça e do pé para permitir fazer a capa à
  parte — então a descrição tem fonte. Mas é a leitura histórica; no ensino
  atual (França, Alemanha), Bradel é a capa de três peças **montada sobre o
  livro**. Como o capítulo já tem a caixa "Armadilha de nome", cabe ali a
  segunda leitura. Vale também dizer qual das duas o estúdio faz.
- [incoerência leve] Virada: "15–20 mm" aqui; "~25 mm" no cap. 14. As duas
  estão certas (o couro se corta com sobra e se apara ao encher), mas quem
  consulta só a tabela vê dois números. Uma nota em cada lado.
- [melhoria] A sequência "Laçada (francesa)" não mostra onde entram
  cabeceado e reforço de lombada na **rota A** (a do estúdio) — só na nota
  da rota B. O apêndice F resolve? (Ver nota do apêndice F.)
- [melhoria] O *casing-in* — passar cola, posicionar o bloco na capa,
  marcar o canal com varetas, prensar — é a operação central da rota do
  estúdio (fitas + capa à parte) e está resumido em uma linha do bloco de
  código. Merece o passo a passo que a laçada ganhou.

### 13 · Capas em papel e tecido

- [incoerência leve] Peça de lombada: aqui, "largura da lombada medida no
  livro"; no cap. 12, "espessura do miolo no mordente + duas espessuras de
  pasta". Falta dizer como se mede em lombada **arredondada** (tira de
  papel em volta da curva, de mordente a mordente).
- [melhoria — repetição] A seção "Com as pastas no livro" (seixas e
  chanfro do canto traseiro) agora está inteira, e mais completa, no cap.
  14 ("Antes de revestir"). Aqui basta uma linha de remissão.

### 14 · Capas em couro

- [conferir] "No Brasil, o tanino vegetal mais produzido é o de
  acácia-negra" — tenho confiança, mas não achei fonte; já avisado.

### 15 · Douração e cortes

Revisado em 17/11 (registro abaixo). Ficou:

- [conferir] Folha **solta** para glair (corte e ferro) e **de
  transferência** para cola de douração: a regra é minha, e só a parte da
  folha solta tem apoio em Cockerell.
- [conferir] A equivalência "bolo, grafite ou guache" atribuída a Peter
  Geraty — não li o texto dele.
- Apagar `15-antes-da-revisao.md` (cópia do texto antigo) depois de
  comparar.

### 16 · Foil, latão e impressão na capa

Revisado em 19/11; recebeu a parte de capa, caixa e painel impressos do
cap. 6, e o título passou a corresponder ao conteúdo. Ficou:

- [conferir] As temperaturas em graus e a faixa do corino continuam sem
  fonte; estão marcadas como ponto de partida.
- [conferir] A parte de capa impressa veio sem revisão de conteúdo: é das
  conversas (verniz, BOPP, produtos, "6–10 camadas" da Golden). Confere-se
  junto com o cap. 19, que repete parte dela.

### 17 · Plotter de corte e técnicas modernas

Revisado em 19/11 (registro abaixo). Ficou:

- [conferir] O papel colado no grão como suporte de corte na plotter é
  inferência minha a partir de Cockerell; está marcado "a testar".

### 18 · Papéis decorados

Revisado em 20/11 (registro abaixo). Ficou:

- [conferir] **Dose de alúmen.** As fontes vão de ~10 g/L (Dharma) a
  30–50 g/L (conversa de origem); o texto manda começar pela menor. Só a
  bandeja decide — anotar a dose que funcionou.
- [conferir] **Zerkall** fora de produção desde a enchente de 2021: a
  informação é de revendedor, não achei nota da fábrica.
- [teste] **Metilcelulose × carragena** como banho de marmorização: as
  fontes divergem (a Dharma não recomenda MC a iniciante; a conversa a punha
  como ponte). O texto manda testar as duas no mesmo dia — candidato ao
  `TESTES.md`. Idem **paste paper com e sem PVA** na pasta.
- [conferir] O resto do capítulo que veio das conversas e não tem fonte
  impressa: proporções do PB27 em metilcelulose, cargas, o método de dois
  banhos, os produtos e preços brasileiros (O Retratista, Kasvi, pH-Fix).

### 19 · Caixas, estojos e proteção

- [lacuna] Para um capítulo de caixas, faltam **as peças e as medidas**:
  lista de peças do slipcase e da clamshell e como cada dimensão sai do
  livro (altura, largura, espessura + folga + cartão + forro). "As três
  medidas da bandeja" promete três e descreve a relação entre duas
  bandejas; a terceira peça — a capa que une as bandejas — não aparece.
- [melhoria — repetição] "Proteger o painel impresso" repete o que agora
  está no cap. 16 (verniz, laminação só na face impressa, laminação ×
  verniz). Aqui basta a tabela de riscos e a remissão.
- [forma — voz de negócio] "O item de maior margem do catálogo", "venda
  clamshell e cobre por isso", "o momento que o cliente fotografa", a seção
  **Preço** inteira e a remissão ao `NEGOCIO.md`. Você pediu o negócio em
  documento separado; isto é o que sobrou dele no manual. As Fontes também
  contam a migração ("estavam no NEGOCIO.md e migraram para cá").

### 20 · Reencadernação

- [conferir] Brochura colada, saída 2 — "cadernos falsos: agrupe as folhas
  de 4 em 4, **serre ranhuras rasas** na lombada e costure sobre fitas,
  passando a linha pelas ranhuras". Não consigo ver como a linha prende
  folhas soltas passando só por ranhuras: parece a mistura de duas
  técnicas — **chulear os grupos pela borda** (*overcasting*, que faz o
  "caderno falso") e **cordões embutidos em serra** para reforçar um bloco
  colado. Vale reescrever dizendo qual das duas.
- [incoerência] O cap. 8 manda "costurar em grupos pela borda
  (*overcasting*) — ver cap. 20"; o cap. 20 não usa a palavra *overcasting*
  e condena *oversewing*; o cap. 11 lembra que Cockerell condena chulear o
  primeiro e o último caderno. São três coisas vizinhas, e o leitor precisa
  de uma frase que as separe (chulear grupos à mão para formar cadernos ×
  o *oversewing* de biblioteca, grupo costurado no grupo).
- [lacuna — pendência antiga] A tabela diz "capa dura solta, miolo bom: só
  recolar as guardas", mas **o procedimento de recolocar na capa**
  (*recasing*: reforço novo, guardas novas, a capa antiga de volta) não
  está descrito. É o conserto mais pedido e o mais simples.

### 21 · Restauração e conservação

- [conferir] "Lei do Patrimônio Histórico": dizer qual (Decreto-Lei
  25/1937).
- [melhoria — o capítulo que ficou para trás] É o único que não passou pela
  reorganização: não tem consulta rápida, a regra de abertura não segue o
  formato dos outros, e o conteúdo é um **roteiro de estudo** com recados
  pessoais (a formação com a Liege, "perguntas em aberto para o ateliê").
  Como diário, ótimo; como capítulo final de um livro, falta o que o
  título promete. O que eu poria: (1) **conservação preventiva** — como
  guardar os livros que você já tem (umidade, temperatura, luz, poeira,
  mofo, insetos, o que nunca fazer: fita adesiva, plastificar, elástico);
  (2) **primeiros socorros** reversíveis — limpeza a seco, remendo de
  rasgo com japonês e amido, o que fazer com livro molhado; (3) a
  fronteira: quando parar e chamar conservador. As notas pessoais podem
  ir para uma página final "Para perguntar no ateliê".
- [incoerência] "Capas com papel de algodão (**aquarela 300 g**)" — os
  caps. 5 e 13 dizem que acima de 180 g não se reveste capa.
- [incoerência leve] "Quando encadernação artesanal e conservação
  divergirem, o padrão deste projeto é o lado da conservação"; o cap. 10
  define o estúdio como "o mundo da encadernação fina, com um pé na
  conservação" — e usa PVA.
- [conferir] "hidróxido/carbonato de **magnésio** para neutralizar": os
  banhos usuais são hidróxido de **cálcio** e **bicarbonato** de magnésio.
- [forma] "gelatina de esturjão (*isinglass*), cola de peixe" — a mesma
  coisa duas vezes.

### Apêndices A, D e E (gerados)

- [melhoria — ver item A.3 dos gerais] **A:** falta a tabela de proporções
  de cola; sobram a linha do tempo e o vocabulário. O gerador pega só a
  tabela de abertura de cada capítulo.
- [melhoria] **D:** na seção do cap. 10 entrou a tabela de gelatinização
  dos amidos (temperatura não é "medida e folga") e ficou de fora a de
  proporções. Os números do *creep* e das linhas (cap. 7 e 8) vêm para cá
  com os mesmos problemas apontados nos capítulos.
- Os três acompanham os capítulos: corrigido o capítulo, corrigem-se
  sozinhos.

### Apêndice B · Glossário

- [incoerência] "*buckram* — buckram, **percalux**": o cap. 13 diz que
  percalux é nome comercial frouxo e que não se deve confiar nele.
- [incoerência] "*made endpaper* — guarda **com dobra**": no cap. 11 ela se
  chama guarda **montada**.
- [incoerência] "cola de peixe — *isinglass*": o cap. 15 avisa que "cola de
  peixe", no comércio brasileiro, é gelatina bovina em folha. O glossário
  deveria ter "ictiocola" e repetir o aviso.
- [melhoria] Termos que o texto usa e o glossário não tem: **contra-folha**
  (forro da pasta), **enchimento** (*filling in*), **bastidor** (*sewing
  frame*), **estação**, **chulear** (*overcasting*), *trindles*, **pinça de
  nervos** (*band nippers*), *spokeshave*, **boneco** (*dummy*), **mancha**,
  **imposição**, *longstitch*, *paste paper*, **clichê**, **mixtion**,
  *recasing*. E "coifa" e "capitel", que só aparecem como sinônimos.
- [forma — terminologia] "**Caixa**" traduz *case binding* (cap. 3, 12,
  glossário) e também nomeia as caixas do cap. 19. Em "encadernação de
  caixa" × "caixa Solander" o leitor tropeça. No Brasil se diz "capa dura
  solta" ou "cartonado"; ou manter *case* em inglês, como já se faz com
  *foil* e *swell*.
- [forma] A tabela português→inglês saiu da ordem alfabética em dois
  pontos ("borda da pasta" depois de "corte"; "bifólio" depois de
  "esquadro").
- [conferir] Coluna francesa: *dos collé* (ver cap. 2) e *mors français* —
  o canal da charneira francesa, em francês, é a *gorge*.

### Apêndice C · Fornecedores

- [incoerência] "Gelatina incolor, Bloom 200–250 — **mercado** — substitui
  **cola de coelho**". O cap. 15 diz que ela substitui a **ictiocola** (e
  que a de coelho é a errada para corte); o cap. 10 diz que o rótulo de
  mercado raramente informa o Bloom.
- [conferir] "Amido de trigo — mercado, casa de produtos naturais": amido
  de **trigo** puro não é item comum de supermercado (o que há é maizena e
  polvilho). Onde eu procuraria: mercearias de produtos orientais (é o
  amido da massa de *dim sum*) e fornecedores de restauro.
- [incoerência] Clichê "3×3 cm ~R$ 100; **5×5 ~R$ 150**"; no cap. 16,
  "4×4 ~R$ 150, 5×5 ~R$ 146".
- [forma] "Scharffix" aqui; "Scharf-Fix" (a grafia da marca) no cap. 14.
  "Canoa" de novo para o tubo da lombada.
- [melhoria] O apêndice lista carragena, alúmen e fel de boi. O cap. 18
  agora ensina a marmorização (20/11); conferir se os fornecedores batem
  com o kit de lá.
- [melhoria] As poucas lojas que o manual cita pelo nome estão espalhadas
  pelos capítulos (O Retratista, Art Camargo, Koralle, Casa da Arte, Casa
  do Restaurador, Kremer). Valia reuni-las aqui. E, como o livro vai ser
  encadernado à mão para uso próprio: **deixar uma ou duas páginas pautadas
  "Meus fornecedores"** para preencher a lápis — é exatamente o que a
  última seção ("como registrar o que você achar") pede.
- [conferir] Importação: confirmar que a Hollander's ainda vende.

### Apêndice F · Ordem de operações

- [lacuna] Faltam: **prensar** as folhas impressas antes de dobrar
  (cap. 6); **escolher a espessura da pasta antes de encaixar** (hoje o
  "confira mordente = pasta" é o passo 24, quatro passos depois do encaixe,
  quando já não tem conserto); e, no couro, **abrir, chanfrar os cantos e
  encher as pastas** (cap. 14), entre secar e decorar.
- [incoerência] Preparo: "glair — descansa **24–48 h**" (cap. 15: 12 h o
  diluído, 1 h o concentrado); "engrudo — **20 min** antes" (cap. 10: só a
  hidratação leva 20–30 min, mais cozinhar e esfriar); "CMC — **10 min**
  antes" (cap. 10: 30–60 min para hidratar).
- [incoerência] Passos 27–28 (seixa e chanfro) remetem ao cap. 13; o
  conteúdo agora está no **cap. 14**. Passo 30, "umedecer o couro": no cap.
  14 revisado quem umedece é o próprio engrudo.
- [melhoria] A sequência principal é a da **laçada em couro**, e a rota que
  o estúdio de fato usa (fitas + capa à parte — é a do exemplo do cap. 8)
  ficou como variante de quatro linhas. Eu inverteria: a principal é a do
  estúdio; a laçada, a variante.
- [forma] Remissões a arquivos: `../../CLAUDE.md`, `CAMINHOS.md`.

---

# O que foi feito

## Antes dos capítulos — correções globais

- **[conteúdo] Blocos de código viravam parágrafo corrido no PDF.** Os 13
  blocos com ``` (sequências de montagem, ordem de operações, comandos)
  saíam emendados numa linha só — a sequência de 41 passos do apêndice F
  ficava ilegível. O `build.py` não tratava blocos cercados. Agora trata,
  em monoespaçado com corpo calculado pela linha mais larga, e o
  `check.py` reprova se um bloco perder as quebras de linha.
- [forma] O símbolo de espera ⏱ não existe na fonte monoespaçada e
  desalinhava as colunas. Dentro de blocos vira ◷, que existe e ocupa uma
  célula. O ⚠️ perde o seletor de variação pelo mesmo motivo.
- [forma] Apêndice F: colunas da sequência realinhadas; duas linhas
  encurtadas para não colar no marcador.
- **[conteúdo]** Apêndice F: "Sete momentos de não-retorno" → **oito**, que
  é o que a tabela lista.
- [forma] Capa e colofão: Estúdio Quattrocento. Sêneca (*Non est ad astra
  mollis e terris via*, *Hercules Furens*, v. 437) na capa; *Ars longa,
  vita brevis* continua no colofão, agora com tradução.
- [forma] Página 2 (verso da capa): sai "as fontes estão em manual/raw/";
  texto corrigido para dizer que o manual foi conferido com as fontes
  clássicas; última linha centralizada indevidamente — corrigido.
- [forma] **Referências a arquivos do projeto** (`CLAUDE.md`,
  `NEGOCIO.md`, `fontes/…`, `../`) não fazem sentido no papel. São 33;
  tratadas capítulo a capítulo: a informação que importa entra no texto,
  o caminho sai.

---

## Capítulos

### 1 · Breve história do livro

- **[conteúdo] Lombada medieval.** Dizia "lombada aderente, couro colado
  direto" como traço do livro medieval. Roberts & Etherington (TIGHT
  BACK) registram o contrário para os primeiros códices: couro não colado
  na lombada, lombada nem encolada. A aderente vem depois e reina até o
  séc. XVIII. Corrigido.
- **[conteúdo] Cores da iluminura.** "Duraram porque eram minerais"
  generalizava; havia corantes orgânicos (lacas, fólio), que são
  justamente os que desbotaram. Reescrito.
- **[conteúdo] Incunábulos.** "Mesmas letras góticas" só vale no norte;
  na Itália, letra humanística. Acrescentado Nicolas Jenson (Veneza,
  1470) — origem do tipo romano, e Quattrocento.
- **[conteúdo] Acrescentado Aldo Manúcio** (~1500): formato pequeno e
  itálico, como resposta ao livro que não se carregava. Linha nova na
  tabela.
- **[conteúdo] Acrescentada a enchente de Florença (1966)** como marco de
  nascimento da conservação moderna, com Peter Waters. Substitui a linha
  genérica "séc. XX" na tabela.
- **[conteúdo] "POD e digital tiraram a produção em massa"** — errado: a
  encadernação manual perdeu isso no séc. XIX. Reescrito.
- [forma] Saiu "Rende o projeto paralelo deste manual (../arte-deco/)":
  agora uma frase sobre o que a encadernação de criação mudou. Saiu
  também "em fontes/" da bibliografia.
- [forma] "Roberts & Skeat" com nomes completos, para não confundir com
  Roberts & Etherington. "São o período" → "É o período".

### 2 · Anatomia do livro

- **[conteúdo] Fólio × bifólio × folha.** Dizia "fólio = folha dobrada ao
  meio". Errado: segundo Roberts & Etherington (FOLIO, LEAF), fólio é uma
  folha do livro, o número da página ou o formato in-fólio. A folha de
  impressão dobrada ao meio é o **bifólio**. Separados também os dois
  sentidos de "folha" (de impressão × do livro). Tabela e texto
  corrigidos; apêndice B acompanha.
- **[conteúdo] Canto de biblioteca.** Não é "o da encadernação
  industrial": é o padrão da encadernação de biblioteca americana (*library
  corners*, também *Dutch corner*), com o excesso recolhido em duas dobras
  diagonais.
- **[conteúdo] "*Inside-cover border*"** não é termo atestado; o friso das
  viradas é a ***inside dentelle***.
- **[conteúdo] Lombada oca.** Não "domina desde o séc. XIX" sem mais:
  começa na França com os Derome (séc. XVIII), generaliza-se no XIX; a
  aderente declina depois de 1820 (R&E, TIGHT BACK). Coerente com o cap. 1.
- **[conteúdo] Francês:** *coupe* não é o corte do miolo — é a borda da
  pasta. O corte é *tranche*. Corrigido aqui e no apêndice B.
- **[conteúdo] *Red rot*:** "couros curtidos a partir do séc. XIX" →
  couro de curtimento vegetal, sobretudo do séc. XIX, degradado pela
  acidez do ar.
- [conteúdo] Mordente: os cadernos são deitados em leque do centro para
  fora (como no cap. 9), não "os externos dobrados".
- [forma] Tabela de falhas: tirado "em ordem de frequência" (sem fonte);
  coluna "onde trata" agora com número de capítulo.
- [forma] Tabela com coluna vazia; "capítulo de tipografia" → "cap. 4";
  caminhos `fontes/…` fora da bibliografia; `booklet.py` descrito como o
  script de imposição do estúdio.

### Global — títulos

- [forma] **13 arquivos tinham título diferente do sumário** (ex.: o cap. 3
  se chamava "Encadernações clássicas em couro" no arquivo e "Tipos de
  encadernação" no sumário). O apêndice A, que lê o título do arquivo,
  mostrava o mesmo capítulo com dois nomes. Agora o `build.py` lê o título
  do próprio capítulo — fonte única —, e os títulos foram alinhados aos do
  sumário.

### 3 · Tipos de encadernação

- **[conteúdo] Vocabulário contradizia o cap. 2 em três termos:**
  "seixa/virada = margem dobrada para dentro" (seixa é a sobra da pasta);
  "cordéis passados/embutidos" como sinônimos (passados = laçados nas
  pastas; embutidos = rebaixados em sulcos); "coifa" sem dizer que é a
  cabeceira. A tabela agora traz só os termos próprios do capítulo e
  remete ao cap. 2. "Bolos" (sem fonte) saiu. *Coifa* e *capitel*
  registrados como sinônimos no cap. 2 e no apêndice B.
- **[conteúdo] Bradel:** acrescentada a origem segundo Roberts &
  Etherington — Alemanha, Alexis-Pierre Bradel, chega à França entre 1772
  e 1809; era considerada provisória e tinha pastas fendidas. O "alemã" do
  nome tem base histórica.
- **[conteúdo] *Case binding*:** dizia "descendente direto do Bradel", sem
  fonte. R&E: introduzido na Grã-Bretanha nos anos 1820. Corrigido.
- **[conteúdo] Lombada aderente:** "toda a encadernação anterior a ~1770"
  → praticamente universal até o séc. XVIII, exceto os primeiros códices e
  as capas moles (R&E). Coerente com caps. 1 e 2.
- **[conteúdo] Lombada flexível:** tirados "medieval" e "islâmica" da
  lista, que generalizavam.
- **[conteúdo] Jansenista:** não é "estilo Le Gascon"; é do fim do séc.
  XVII e início do XVIII, e admitia florão central e cantoneiras (R&E).
- **[conteúdo] *Two-on*:** a função principal é **reduzir o swell**, não
  só economizar linha.
- **[conteúdo] Islâmica:** "capa em três partes" saiu; descrita pela aba
  da goteira e pela lingueta.
- [conteúdo] Bradel "padrão de bibliotecas" → "muito usada em arquivos e
  conservação" (biblioteca usa *case binding*).
- [forma] Parágrafo de abertura situando o capítulo como mapa, com os
  capítulos de execução. "*Viertelleder*" (não confirmado) saiu.
  Referências por nome → número; "ver o capítulo de Art Déco" (saiu do
  manual) → cap. 15.

### 4 · Tipografia e editoração

O capítulo tinha crescido absorvendo assuntos dos vizinhos — fibra (cap.
5), aparo (cap. 9), imposição (cap. 7), cartonagem (caps. 12–13) —, e
nesses trechos contradizia os capítulos donos do assunto. Agora fica com o
que é de editoração e remete ao resto.

- **[conteúdo] Duplex: "manual, sempre" contradizia os caps. 5 e 6**, a
  prática do estúdio e as instruções de impressão deste manual. Agora:
  automático até ~90 g/m² (homologado para 64–90 g), manual acima. Saiu
  também "sem entrada traseira", que nenhuma outra parte confirmava.
- **[conteúdo] Aparo: "guilhotina de papelaria — a solução real"
  contradizia o cap. 9** (que a marca com ❌). Seção substituída por
  remissão ao cap. 9; ficou a alternativa histórica de não aparar.
- **[conteúdo] Typst: "ainda não tem protrusão/expansão à la microtype"
  — falso no Typst 0.15** (testado: `text.overhang` e
  `par.justification-limits` existem). Reescrito.
- **[conteúdo] Margens prontas:** duas linhas não fechavam a conta (mancha
  declarada ≠ formato − margens); a do Carta ainda tinha interna > externa,
  contra a regra do próprio capítulo. Recalculadas. Mesmo erro (160 → 166
  mm) na receita do 145 × 204. Acrescentada nota sobre o cânone
  comprimido.
- **[conteúdo] Carta dobrada não dá 14 × 21** (tem 139,7 mm de largura
  antes do aparo). Só 13,5 × 21.
- [conteúdo] Caracteres por linha da Libertinus **medidos**: 73 / 70 / 67
  a 10 / 10,5 / 11 pt numa mancha de 110 mm. Confirma o "65–70" do texto.
- [conteúdo] "Não use menos de 11 pt" → 10,5 pt, coerente com a tabela do
  próprio capítulo e com os livros do estúdio.
- [conteúdo] "Fonte da Wikipédia" → fonte do logotipo da Wikipédia.
  InDesign tem compositor de parágrafo também (*Paragraph Composer*).
  *Two-on*/caderno: "16 páginas ideal para 100–120 g" e "120 g → 12
  páginas" se contradiziam; agora 80–100 g e 120 g.
- [conteúdo] Bilíngue: "vira um inferno" contradizia a Vulgata do próprio
  estúdio (colunas paralelas). Reescrito com a experiência real.
- [conteúdo] Trazido do `CLAUDE.md` para o texto, porque o leitor precisa:
  armadilhas do Typst, fontes de texto e armadilhas de OCR/tradução,
  convenção de colofão, ~430 palavras por página A5.
- [conteúdo] Cartonagem: fórmulas que só existiam aqui foram para onde
  pertencem — lombada da capa → cap. 12; material de revestimento → cap.
  13; "comece por meia-encadernação" → cap. 14. "Praça" (termo usado só
  aqui, = seixa) saiu. Ficou a espessura de lombada, que serve ao
  planejamento.
- [forma] "4. Anatomia do livro" → "4. A ordem das páginas" (o cap. 2 já
  se chama Anatomia). Seis referências a `CLAUDE.md`/`NEGOCIO.md` saíram.
- [forma] **Check reforçado:** uma tabela dentro de item de lista virava
  texto corrido e reiniciava a numeração; o Typst transforma o `---` em
  travessão, e o check não via. Agora vê.

### 5 · Papel

Mesmo padrão do cap. 4: o capítulo repetia, quase palavra por palavra,
seções de outros capítulos — e nas cópias estavam os erros já corrigidos
nos originais.

- **[conteúdo] Seção de impressão (L4360) duplicava o cap. 6** e
  contradizia o cap. 4 em dois pontos: "livro profissional tem margem
  interna **maior** que a externa" (o cânone do cap. 4 diz o contrário) e
  "EB Garamond se comporta bem" em jato de tinta (o cap. 4 diz que é a que
  mais sofre). Substituída por um resumo de **escolha de papel** para a
  impressora + remissão ao cap. 6.
- **[conteúdo] A armadilha do "preto que some"** (perfil brilhante desliga
  o preto pigmentado) só existia aqui → **movida para o cap. 6**, onde
  ficam os ajustes de driver. Também foram para o cap. 6: imprimir em duas
  passadas quando o duplex marca, e o número "15–20 mm sem cor junto à
  lombada".
- **[conteúdo] "Formatos e tamanhos" era cópia do cap. 4** — ainda com o
  erro do Carta "dá 14 × 21" e a tabela sem a conta do aparo. Substituída
  por um parágrafo e remissão. As tabelas que só existiam aqui (série ISO,
  formatos anglo-saxões, 20 × 20) **foram para o cap. 4**.
- **[conteúdo] Terceira cópia de "O aparo"**, de novo com a guilhotina de
  papelaria como "solução real" → saiu (cap. 9).
- **[conteúdo] "Receita: livro de 100 páginas"** repetia o exemplo do cap.
  4, o boneco e a sequência do apêndice F, e mandava pôr margem de lombada
  maior que a externa → saiu. Ficou no cap. 4 o detalhe útil de que a
  Epson aceita tamanho personalizado.
- **[conteúdo] Opalina:** "normalmente 180–250 g" contradizia a tabela do
  próprio capítulo, que a recomenda a 120 g para miolo → 120–250 g.
- **[conteúdo] Glassine** não é 90–110 g como o papel vegetal; é bem mais
  fino. Papelão de tampa: 1,5–2 → 1,5–2,5 mm, coerente com o cap. 12.
- [conteúdo] Color Plus: fabricante (Blendpaper, Salto/SP) **confirmado**;
  "desde 1987" e "o mais antigo do Brasil" não confirmados → saíram.
  "Colorline atende ISO 9706" não confirmado → saiu. Horlle **confirmado**
  como marca real. Pólen identificado como marca da Suzano (*bouffant*).
- [conteúdo] "Guarda com fibra errada é a causa nº 1 de capa empenada" →
  "uma das mais comuns", junto com a falta de contra-folha (cap. 12).
- [forma] Capítulo de 666 → 380 linhas. Nenhum parágrafo duplicado entre
  capítulos depois da limpeza.

### Global — cadernos

- [forma] O manual encolheu para 268 páginas, e os cadernos de 12 passaram
  a deixar 8 em branco. Como a contagem muda a cada revisão, o tamanho do
  caderno agora é **escolhido automaticamente** (`cadernos.py`) entre 12,
  16 e 20, pelo menor desperdício, com preferência por 16. Hoje: 17
  cadernos de 16, 4 em branco.
- [forma] README: "138 folhas" corrigido — o `booklet.py` chama de *sheets*
  o que são **lados**; as folhas de papel são a metade. Números velhos da
  primeira versão (13 cadernos, 202 páginas, 14 mm) atualizados.

### 6 · Impressão

- **[conteúdo] Erro meu na revisão do cap. 5:** a "armadilha do preto que
  some", que eu disse ter movido do cap. 5 para cá, **já existia** no cap. 6
  com outras palavras — minha busca exigia as duas palavras-chave na mesma
  linha. Ficou duplicada; a cópia que eu pus saiu. (O registro do cap. 5,
  acima, está errado nesse ponto.)
- **[conteúdo] De novo "margem interna maior que a externa"**, contra o
  cap. 4 → corrigido, com remissão.
- **[conteúdo] Contradição interna sobre o Pólen:** "nitidez excelente, às
  vezes melhor que laser" × "come a nitidez" (na tabela). Reescrito: boa
  aparência, ao custo de um pouco de nitidez.
- **[conteúdo] Contradição interna sobre a qualidade:** o item 5 mandava
  "nunca Padrão"; o quadro logo abaixo conclui que em papel absorvente o
  Padrão é o certo. Item 5 agora remete ao quadro.
- **[conteúdo] Verniz:** o destaque dizia que 2–3 demãos tornam a impressão
  compatível com cola d'água; o passo a passo e a Golden dizem que a
  barreira só vem da 3ª–4ª. Alinhado em 3–4, como a tabela de abertura.
- [conteúdo] "O melhor uso da impressora: o interior" era cópia do cap. 19
  → remissão. SureColor P700 é A3+ e P900 é A2 (estava "A3+/A2+"). Código
  de tinta inconsistente (502/504 × 504/544) → genérico onde não importava.
- [forma] "Não funcione" → "funciona"; "deleta" → "elimina"; "marca
  digital" (ambíguo) → "marca de dedo"; "as 15 minutos" → título corrigido
  (o teste dura três semanas). Quatro remissões por nome → número; duas
  referências ao `NEGOCIO.md` saíram.

### Global — duplicatas aproximadas

- [forma] O verificador de duplicatas só comparava parágrafos longos e
  idênticos. Rodado agora por semelhança (sequências de 5 palavras): **7
  pares** no manual inteiro. Resolvidos os dos caps. 4–5 (aviso de
  gramatura de capa saiu do 4; resumo de formatos do 5 reescrito). Os
  outros ficam para os capítulos donos: glair (15↔16), impressão no cap. 10
  (6↔10), tabela de costuras (3↔8), doublure (2↔11).

### 7 · Cadernos e imposição

- **[conteúdo] A explicação do *creep* estava invertida.** Dizia que as
  folhas internas avançam "porque percorrem um arco maior ao contornar as
  de fora". É o contrário: as de fora contornam as de dentro, gastam mais
  papel na dobra e ficam mais curtas. Corrigido.
- **[conteúdo] Acrescentada a regra quantitativa**, deduzida da geometria
  da dobra: cada folha a mais consome π × espessura → **~0,4 mm por folha**
  em Pólen 90. Confere com os números que o capítulo já trazia (1–1,5 mm
  com 4 folhas; ~3 mm com 8).
- **[conteúdo] Figura errada:** a do *creep* era a fig. 38 do Cockerell,
  que mostra a lacuna pasta–lombada sem encaixe (assunto do cap. 9). O
  Cockerell não tem figura de *creep* → **desenho próprio em SVG**
  (`figuras/desenho-creep.svg`), com a geometria real. Os SVG passam a
  ocupar 85% da largura; as gravuras continuam em 52%.
- **[conteúdo] Armadilhas:** "margem central comeu o texto — creep +
  medianiz curta" misturava dois problemas (o *creep* come a margem
  **externa** das páginas do meio; a lombada come a **interna** de livro
  grosso). Separados em duas linhas.
- [conteúdo] Formatos estão no cap. 4 (não 5); o teste de registro, no
  cap. 4 (não 6). "Múltiplo de 4 para sela" (termo não definido no manual)
  simplificado.
- [forma] "213 páginas em cadernos de 16 dão 14 cadernos" (número velho) →
  descreve a escolha automática. Referências a `README.md` e `CLAUDE.md`
  saíram.

### Global — dois defeitos de conversão que o check não via

- **[conteúdo] Os 121 tils (~) do manual sumiam no PDF.** No Typst, `~` é
  espaço inquebrável; o `build.py` não o protegia. "~250 páginas", "~90 g",
  "~0,4 mm" saíam como valores exatos. Corrigido; o check agora compara a
  contagem de tils no fonte e no PDF (testado: reprova se voltar).
- **[forma] A nota interna `<!-- GERADO por gera_apendices.py … -->` saía
  impressa** no topo dos apêndices A, D e E. O conversor agora descarta
  comentários HTML; o check procura por eles.
- [forma] Varridos os demais caracteres que o Typst interpreta (`//`, `/*`,
  `--`, `=` ou `/` em início de linha): nenhum outro caso.

### 8 · Costura

O capítulo era forte em **material** (linha, cordão, cera) e quase não
falava da **costura em si** — a escolha do ponto se resumia a uma tabela
copiada do cap. 3. Reescrito em torno da pergunta "qual costura usar e por
quê", deixando o gesto de cada ponto para vídeo, como combinado.

- **[conteúdo] Novo: "Consulta rápida — que costura usar"**, por situação,
  no topo do capítulo.
- **[conteúdo] Novo: "Como uma costura funciona"** — estações, *kettle
  stitch* (com a origem do nome, R&E), ao longo × dois a dois, o bastidor,
  marcar as estações, tensão, emendas e nó de tecelão. Fontes: Cockerell e
  R&E.
- **[conteúdo] Novo: "As costuras, uma a uma"** — para cada uma: o que é, o
  problema que resolve, como abre, onde falha, com que capa combina. Sobre
  nervos, cordões duplos, fitas, grecada, ponto encadeado (copta), *longstitch*,
  sela, japonesa (com a prática do estúdio, que estava só no `CLAUDE.md`), e
  o que evitar. Mais uma tabela de comparação geral.
- **[conteúdo] Novo: exemplo resolvido — a costura deste manual.** Com 17
  cadernos, a linha "coringa" 25/3 daria 42% de *swell*; a certa é 30/3–35/3
  (33%). Mostra que o coringa não serve sempre.
- **[conteúdo] *Swell*: "duas espessuras de linha por caderno" → uma**,
  como diz Cockerell (e o próprio cap. 9). Acrescentada a estimativa
  *swell* ≈ cadernos × diâmetro.
- **[conteúdo] Espaçamento das nervuras:** "os painéis vão aumentando de
  cima para baixo" estava errado. Cockerell: **seis divisões, cinco iguais e
  a do pé um pouco maior**. Nota sobre a lógica medieval diferente (R&E).
- **[conteúdo] Quantidade de nervuras:** "3 em livro pequeno" → Cockerell:
  **cinco** em quase todo livro; quatro só em livro pequeno e grosso; seis em
  fólio grande e fino.
- **[conteúdo] Grecada:** era opção neutra; agora com a crítica de
  Cockerell ("forma degenerada") e os três motivos. Costura flexível:
  "clássica anterior ao séc. XVIII" → dominante até hoje, quase extinta no
  séc. XIX, resgatada por Cobden-Sanderson e Cockerell (R&E).
- [conteúdo] Fitas entraram no kit e na tabela de material; o "para começar
  hoje" passou a ser costura sobre fitas.
- [forma] **Figuras:** cinco do Cockerell (bastidor, *kettle stitch*, nó de
  tecelão, três costuras em corte, fitas) e um desenho próprio comparando
  como cada costura aparece. A tabela panorâmica duplicada do cap. 3 saiu.

### Global — ponto e vírgula engolido

- **[conteúdo] 20 pontos e vírgulas sumiam do PDF.** Logo depois de
  negrito, itálico ou código, o Typst lê `;` como fim de comando e o engole
  ("*case*; não exige" → "case não exige"). O `build.py` agora escapa `;`,
  `(` e `.` depois de um comando; o check compara a contagem de `;` no
  fonte e no PDF (reprovou o PDF antigo: 339 de 359).

### 9 · Do miolo costurado ao bloco pronto

- **[conteúdo] A sequência tinha uma contradição interna:** mandava
  arredondar "na janela da cola" (Cockerell: depois de deixar de grudar,
  antes de endurecer) mas punha refile e douração do corte — horas de
  trabalho — no meio. Reescrito em **duas rotas**, ambas legítimas segundo
  R&E (TRIMMING): **A**, fora das pastas (refilar antes de arredondar; a
  do estúdio), com as duas saídas para a janela (refilar cedo, ou
  reamolecer a lombada — o que não funciona com PVA puro); e **B**, *in
  boards* (Cockerell: laçar as pastas logo depois do encaixe, refilar e
  dourar com elas no lugar).
- **[conteúdo] "Dourar o corte: agora ou nunca, depois do encaixe é
  impossível" — falso.** Cockerell dourava depois do encaixe, com as
  pastas laçadas e a goteira achatada com *trindles*. Agora a tabela das
  três maneiras de dourar a goteira (R&E e Cockerell). *Gilt in the
  square* ganhou o defeito que faltava: deixa linha branca no primeiro e
  no último caderno ao arredondar. *Gilt in the round* não é "a marca da
  encadernação fina histórica": Cockerell a achava censurável. Corrigido
  também no apêndice F (passo 18 e tabela de não-retorno, que fica com
  sete).
- **[conteúdo] Ordem do refile:** "goteira primeiro" → Cockerell: cabeça,
  pé, goteira por último. Na guilhotina, o que importa é o esquadro.
- **[conteúdo] "Refilar antes de costurar só funciona aceitando o
  *creep*" — errado:** aparar caderno a caderno contra um gabarito tira o
  *creep* de cada um. Substituído pelas três escolhas de Cockerell (não
  aparar; aparar antes; refilar depois).
- **[conteúdo] Ouro "de um micrômetro" → um décimo de micrômetro** (o cap.
  15 já dizia 0,1 µm). Direção de lixar: a regra de Cockerell (cabeça e pé
  da lombada para a goteira; goteira do meio para as pontas).
- [conteúdo] Encaixe: "dobrando os cadernos externos para fora" → em leque
  do centro, como no cap. 2; "a mais difícil e importante" → "talvez",
  como em Cockerell; as quatro funções do encaixe (R&E). Descrição das
  *backing boards*. Arredondar sem martelo (R&E). Cabeceado: "é
  estrutural" (contradizia o cap. 2) → reforça um pouco.
- [forma] (Apontado na revisão humana, p. 107.) O título "4 e 5. O corte:
  preparar e decorar" era o único do capítulo com número no PDF — o
  `build.py` tira o "N." do início dos títulos, e "4 e 5." escapava. Virou
  duas seções, "Raspar e lixar o corte" e "Decorar o corte", como os passos
  da tabela.
- [forma] "Seis operações" → nove (a tabela lista nove). Referências a
  `NEGOCIO.md` e `fontes/` saíram.

### Global — páginas vazias e cabeçalho

- **[forma] Seis páginas em branco com cabeçalho e número**, uma antes de
  cada folha de rosto de parte — a função das partes criava uma página
  para o título escondido do sumário e outra para a folha. O sumário
  apontava as partes para essas páginas vazias. Corrigido (282 → 276
  páginas).
- **[forma] O cabeçalho mostrava o capítulo anterior** na página de
  abertura (ex.: "Costura" sobre o título do cap. 9): o código comparava o
  número impresso da página com o físico. Corrigido.
- [forma] A página antes do colofão saía com cabeçalho e número; agora é
  realmente em branco (decidida por uma etiqueta fixa, para o layout
  convergir).
- [forma] Check: duas verificações novas — nenhuma página só com
  cabeçalho/número; título de capítulo como 1ª linha da abertura.

### 10 · Colas e adesivos

- **[conteúdo] Nova seção "O que cada cola é, quimicamente"** — tabela das
  quatro famílias (do que são feitas, como pegam, como se desfazem) e uma
  parte para cada: amidos (amilose e amilopectina, gelatinização com faixa
  por tipo de amido — dada como aproximada, porque as fontes divergem —,
  retrogradação, o *furunori* japonês); éteres de celulose (o que é a
  modificação; CMC, MC, HPC/Klucel, MHEC/Tylose; a termogelificação da
  MC); proteicas (colágeno → gelatina, por que ferver arruína, o que é
  *bloom*, as quatro colas animais); PVA (emulsão e coalescência — por que é
  irreversível —, plastificação externa × copolímero, ácido acético);
  dextrina, funori e glair.
- **[conteúdo] Novo: "Laboratório caseiro"** — teste do pH, **teste do
  iodo** (lugol revela amido: cargas em cola branca, pureza do amido
  extraído, engrudo × cola animal em livro antigo) e teste de
  reversibilidade. Nova tabela "Proporções num relance".
- **[conteúdo] Estudo do RIT:** o título estava incompleto e os números
  ("magenta em 10 minutos", "amido progredindo por 112 dias", "com PVA não
  aconteceu") **não se confirmaram** no resumo publicado — e o resumo fala
  em 84 dias de incubação. Citado agora pelo que comprovadamente diz
  (Gordeladze, Burge e Venosa, IPI, 2011).
- **[conteúdo] "Beva" como PVA neutro — errado:** BEVA 371 é adesivo
  termofusível de EVA para reentelar pintura. Saiu.
- **[conteúdo] "Diluir PVA com álcool isopropílico"** para ganhar tempo
  aberto — solvente pode desestabilizar a emulsão. Saiu.
- **[conteúdo] Vinagre como conservante da maizena:** conserva porque
  acidifica — contradiz o capítulo inteiro. Agora com o aviso.
- **[conteúdo] Gelatina:** "de supermercado é baixo/médio bloom"
  (contradizia o cap. 15, "bloom 200–250") → o rótulo raramente informa;
  para douração, comprar com bloom informado. Proporções de gelatina e cola
  de coelho estavam em três lugares com valores diferentes → uma tabela.
- [conteúdo] Tabela de abertura: "douração a folha sobre couro → cola de
  peixe/gelatina/glair" misturava duas coisas → couro: glair; corte:
  glair + gelatina/ictiocola (cap. 15). Linha nova: reparo de papel.
- [conteúdo] "Klucel G" estava listado entre "coisas que só funcionam com
  cola proteica" (não é proteica). "15–20 anos" para o PVA ficar
  quebradiço, "glúten quase irreversível" e "PVA forma película que
  empurra" — afirmações sem fonte, amenizadas. "400 anos" → "séculos".
- [conteúdo] **Tylose MH300 não é metilcelulose**: é MHEC, prima próxima.
  Corrigido também no cap. 18 e no apêndice C.
- [forma] As "divergências com a conversa do Kimi-K3" viraram "conselho
  comum que não serve aqui" — no papel, ninguém sabe quem é o Kimi. A
  parte de montagem do painel impresso, que repetia o cap. 6, virou
  remissão (as duas repetições 6↔10 sumiram).

### 11 · Guardas

- **[conteúdo] "Colar a guarda" eram duas operações confundidas:** prender
  a guarda ao miolo (antes/durante a costura — onde ela ganha valor
  estrutural) e colar na pasta (das últimas). Seção nova "Dois momentos",
  com Cockerell: *"é um erro deixar para colar as guardas depois que o
  livro já foi montado"*. Tabela de abertura ganhou a coluna "presa ao
  miolo por".
- **[conteúdo] Nova: a guarda em sanfona (*zigzag*) de Cockerell**, com a
  fig. 19 e a construção passo a passo — a guarda que cede à tração em vez
  de resistir.
- **[conteúdo] Guarda montada:** era "o padrão para livro de uso", sem
  ressalva. R&E registram o defeito — **arrasta o primeiro e o último
  caderno** —, e é para isso que existem a sanfona e outras variantes.
  "Com dobra" → "montada" (*made* é composta, não dobrada).
- **[conteúdo] Guarda flexível:** "dois bifólios unidos em dois pontos" →
  **colados em fio junto à lombada e junto à goteira** (R&E).
- **[conteúdo] "A guarda é a charneira que segura a capa"** valia sem
  ressalva → na caixa e na Bradel, sim, é tudo; na laçada, os cordões
  seguram e a guarda é a segunda linha.
- **[conteúdo] Marmorizado:** de "✅ o padrão histórico" para ⚠️, com o
  aviso de Cockerell (papel fraco demais; ou, grosso, guarda dura).
  **Orizomegami** marcado ⚠️ (é tingido com corante; pode sangrar com cola
  d'água) — também no cap. 18. Cianotipia: ✅ com ressalva de álcali.
- [conteúdo] Novos: charneira de couro (R&E, desde o séc. XVII); a folha de
  descarte; seda e pergaminho (Cockerell); as folhas em branco de proteção;
  a crítica ao chuleado do primeiro caderno. Gramatura: 120–150, até 180 em
  livro grande.
- [forma] A *doublure* repetia entre os caps. 2 e 11 → no 2, uma linha com
  remissão.
- **[forma] Mapa de figuras do Cockerell refeito.** O primeiro, feito pelas
  âncoras do HTML, errava as figuras cuja âncora vem depois da imagem
  (pegava a seguinte). Refeito pelo texto alternativo, e **todas as 17
  gravuras usadas no livro foram conferidas byte a byte**: estavam certas.
  A única errada (fig. 43) não era usada e saiu.
- *Pendente para o cap. 20:* a guarda costurada por furos alternados
  (*stab-sewn endpaper*, R&E), própria para recapar sem recosturar.

### 12 · Montagem da capa

- **[conteúdo] ERRO GRAVE, meu (novembro): a contra-folha estava do lado
  errado.** O capítulo mandava 2 papéis **por fora** e 1 por dentro. Cockerell
  diz o contrário, em três frases que concordam: "não será necessário pôr
  forro duplo *no lado de dentro*" da pasta composta; as pastas forradas se
  juntam "com os lados de forro duplo um contra o outro"; a pasta fina da
  composta vai "junto ao livro". Com o forro duplo por fora, contra-folha e
  revestimento puxam para o mesmo lado e a pasta **empena mais**. Corrigido
  aqui (texto, números, sequência, armadilhas) e no apêndice F; acrescentada
  a física (papel encolhe ao secar e curva a pasta para o seu lado) e um
  aviso "o lado importa".
- **[conteúdo] Laçada:** "passe o slip e cole achatado na face interna" →
  como Cockerell faz: engrudo nos slips, torcer **só a ponta**, pela frente
  e de volta pela segunda fileira, cortar rente e **bater sobre o ferro**
  pelas duas faces. A tensão certa, o aviso de que slip torcido não achata,
  e o passo seguinte (prensar com chapas, limpar a cola da lombada).
- **[conteúdo] Tubo da lombada oca: era impossível** ("tira com a largura
  exata da lombada, dobrada em três painéis"). R&E: a forma simples é uma
  folha dobrada ao meio; o tubo usa tira de **três vezes** a largura
  (*two on and one off*).
- **[conteúdo] Bradel:** as pastas fendidas eram "variante"; segundo R&E
  são o que caracteriza a Bradel. Nova seção "A pasta fendida". Caixa: presa
  pelas guardas **e pelas abas do reforço** (não "só pelas guardas"); data
  de introdução (anos 1820). Cap. 3 corrigido: "com canal, é Bradel" →
  sem fenda, é uma caixa com charneira francesa.
- [conteúdo] "A estrutura mais forte que existe" → a mais forte das três.
  "Detalhe que quase nenhum tutorial menciona" saiu. Cordão × tiras de
  couro (Cockerell). Sequências: a da Bradel e a da caixa juntas; nota da
  rota B do cap. 9.
- [forma] Fig. 50 do Cockerell baixada e **descartada**: o desenho é
  ambíguo e não confirma o texto.

### Global — célula de tabela virando título

- **[forma] "espessura da pasta" estava no sumário como capítulo — duas
  vezes.** A célula "= espessura da pasta" (cap. 12 e apêndice D): no
  Typst, "=" no começo é marca de título. O `build.py` agora protege `=`,
  `-`, `+` e `/` no começo das células; o check exige que o sumário só
  tenha capítulos e partes (reprovou o PDF antigo).

### 13 · Capas em papel e tecido

- **[conteúdo] O passo a passo misturava dois procedimentos.** "Ajustar a
  seixa" e "chanfrar o canto traseiro para não arrastar a cabeceira" são de
  Cockerell, para **couro com as pastas laçadas no livro**; tecido e papel
  quase sempre revestem uma **capa feita à parte** (caixa/Bradel). Agora há
  as duas seções: a capa à parte passo a passo (peça de lombada, canal de
  3–6 mm com espaçador, ordem das viradas) e "com as pastas no livro", que
  remete ao cap. 14.
- **[conteúdo] Proporções da meia-encadernação estavam erradas** — aqui e no
  cap. 3. R&E: no **1/4**, a lombada avança ~**1/8** da pasta (não 1/4); na
  **meia**, ~**1/4** (não 1/3), com cantos "em proporção harmônica"; o 3/4,
  "aos olhos de muitos, mal proporcionado". "Cantos 1/4 a 1/5 da altura"
  (sem fonte) saiu.
- **[conteúdo] "Faça os cantos antes da lombada, porque a lombada cobre a
  borda dos cantos"** — não faz sentido: lombada e cantos não se encostam.
  Substituído pelo costume de ateliê (lombada e cantos primeiro; o papel das
  faces por último, cobrindo de leve as bordas).
- **[conteúdo] Tecidos classificados pelo tratamento** (R&E, BOOK CLOTH):
  preenchido com amido, revestido/impregnado (piroxilina = nitrato de
  celulose), com papel no verso, sem tratamento — com teste para reconhecer
  (verso, gota d'água, dobra). As composições atribuídas a "percalina" e
  "Percalux" não se confirmaram: percalina, no dicionário, é algodão leve e
  lustroso; Percalux é nome comercial sem fonte. Agora: "não confie no nome,
  olhe o material".
- [conteúdo] Canto de biblioteca descrito como no cap. 2 (R&E). "Passe a
  cola no revestimento, não no papelão; espere 20–30 s" veio do cap. 5,
  onde estava perdido.
- [forma] Separador duplicado (`---` `---`) removido; "ver capítulo de
  douração" → cap. 16; a nota "estava no capítulo de couro, onde não
  pertencia" (anotação de processo) saiu das fontes.

### 14 · Capas em couro

- **[conteúdo] A regra misturava duas coisas.** Dizia que o couro
  pré-afinado pela curtidora "já perdeu a fibra, sobra a flor quebradiça".
  Cockerell diz outra coisa: a conveniência do couro pré-afinado é *em
  parte* responsável pelo couro fino demais, e é a **pele grande rebaixada
  para livro pequeno** que fica só com a flor. Regra nova: a força está nas
  fibras do lado do carnal; compre sem rebaixar, escolha a pele pelo
  tamanho do livro, afine só onde dobra.
- **[conteúdo] Direção da faca estava errada:** "puxando em direção a
  você" → empurrando para longe do corpo, faca deitada, com a rebarba de
  baixo feita na pedra (Cockerell); o cabo nunca sobe a ponto de os dedos
  passarem da borda da pedra. Entraram os tipos de faca (inglesa,
  francesa, alemã), o *spokeshave*, que a substituiu para afinar áreas
  (R&E), a máquina e o teste da dobra.
- **[conteúdo] Couro ao cromo no laser "libera cloro" — errado, aqui e no
  cap. 17.** Cloro é do PVC (corino, cap. 13); o couro cromado forma
  **cromo hexavalente** (estudo de 2024, *ACS Chem. Health & Safety*).
  Corrigido nos dois capítulos.
- **[conteúdo] Escolha da pele, a fundo**, com o relatório da Society of
  Arts citado por Cockerell: datas da piora (1830, 1860), o que durou
  (porco ao alúmen, marroquim vermelho de sumagre) e o que não (carneiro de
  grão gravado, vitela fina, *russia*), ácido sulfúrico no banho de tinta
  (0,5–1,6 %), as cinco falhas do encadernador, o couro ideal. Pirogalol ×
  catecol (sumagre/castanheiro × acácia-negra/quebracho) e a nota sobre o
  tanino brasileiro. Nomes da cabra (morocco, levant, Niger; R&E). Teste
  do rasgo (entra no apêndice E). A cor e o sulfato ferroso — e por que a
  pinça de nervos é niquelada.
- **[conteúdo] "Pele ao alúmen, a mais durável que existe"** → a mais
  durável das antigas, mas dura e pouco flexível (Society of Arts). Cromo:
  "rejeita cola" → não amolece com água (Cockerell). Vegetal "escurece com
  a luz" → a maioria; o sumagre quase não (R&E).
- **[conteúdo] O revestimento era um esboço de quatro passos** (e "do
  centro para fora, sobre papel siliconado" não é de fonte nenhuma).
  Agora segue Cockerell: preparar (forro de cabeça e pé, **chanfro do canto
  traseiro das pastas**, que o cap. 13 já remetia para cá, seixas, nervos),
  o que ter à mão, engrudar (o engrudo umedece; úmido, não encharcado —
  quinta falha da Society), os doze passos (estiramento só no comprimento
  da lombada), a cabeceira com a dobradeira entre cabeceado e linha,
  amarrar e secar, abrir, **meia-esquadria e enchimento** (*filling in*,
  que não estava em capítulo nenhum) e a charneira de couro.
- **[conteúdo] Números sem fonte** (espessuras) marcados como pontos de
  partida de ateliê; a temperatura de douração saiu daqui (é do cap. 15/16)
  e entrou o chanfro de ~3 mm (Cockerell).
- **[conteúdo] Cera e *red rot*.** "Cosmoloid H80, também vendido como C80"
  → Cosmolloid 80H (o H é de *hard*); o "C80" não se confirmou. Fusão
  80–95 °C → ~75–90 °C. A história da Renaissance Wax com a fonte (JAIC
  2003). A caixa de divergência ("uma primeira versão dizia…") virou o que
  as fontes dizem: Klucel G em álcool é consenso; o *red rot cocktail* do
  CCAHA (SC6000 + etanol + Klucel G 2 %, 1:1:1) foi apresentado como
  compromisso, e o estudo UCLA/Getty questionou a cera, que fica opaca.
  Library of Congress: "nem ceras de espécie alguma" era exagero — ela
  desaconselha óleo e *leather dressing*. *Red rot* ganhou seção própria
  (as duas formas da Society, a causa ácida).
- **[conteúdo] Fornecedor e autenticidade.** "Casa do Restaurador" não se
  confirmou: saiu, fica a referência ao apêndice C. Na Renaissance Wax
  saíram os detalhes da lata (*royal warrant*, gregas, mascarão) e os
  preços em libra e dólar, que não consegui conferir.
- [forma] "o capítulo anterior deste manual dizia isso sem ensinar como"
  (anotação de processo) saiu; "(Ver capítulo de linha e costura.)" → cap.
  8; seção **Fontes** criada, como nos outros capítulos.

### Leitura completa — números de capítulo e erros de fato (17/11/2026)

Primeiro lote da leitura integral (números de capítulo e a tabela de
erros de fato). O resto está em "O que falta", no alto deste arquivo.

- **[forma] Capítulos numerados.** O `build.py` põe o número na abertura,
  no sumário e no cabeçalho ("10 · Colas e adesivos"). O texto faz quase
  duzentas remissões por número e o PDF não mostrava número nenhum.
  `check.py` acompanha.
- **[erro] Cap. 7 e 9, *creep*.** A conta estava dobrada (erro meu, da
  revisão): π × espessura é o gasto da volta inteira, metade em cada
  goteira. ~0,2 mm por folha em Pólen 90; ~0,6 mm em 4 folhas (era 1,3);
  ~1,5 mm em 8 (era 3).
- **[erro] Cap. 5.** Couchê L1 é revestido de um lado, L2 dos dois.
- **[erro] Cap. 6.** Papel RC é revestido de polietileno, não poliéster.
- **[erro] Cap. 10 e ap. C.** Papel manteiga comum não é siliconado nem
  encerado: PVA gruda nele. A barreira é papel siliconado ou encerado.
- **[erro] Cap. 13, 14 e 16, corino.** "Nunca aceita douração a quente"
  virou: não aceita ferro de mão com glair; aceita *hot stamping* em
  prensa, com foil para sintéticos. A faixa de ~100–120 °C no cap. 16 é
  ponto de partida meu, sem fonte conferida — testar na sobra.
- **[erro] Cap. 15.** 0,1 µm = 0,00001 cm (era 0,000012); a conta dá
  ~1,2 g de ouro em 100 folhas. Saiu "100 °C é o teto do couro", que
  contradizia o ferro a 120–125 °C do mesmo capítulo.
- **[erro] Cap. 19.** A ordem de forrar agora distingue estojo (interior
  antes de montar) e caixa de bandejas (exterior primeiro, fundo por
  último). A linha das armadilhas acompanha.
- **[erro] Cap. 21.** Links para arquivos que não existem viraram
  remissões (cap. 10, 8, 14). "Heloisa Vianna" e "CCAP", que não
  reconheço, deram lugar a Cassares (2000), CPBA, CECOR/UFMG e ABER.
  **Conferir:** o texto dizia que o livro da Heloisa Vianna "provavelmente
  está na biblioteca do ateliê" — se estiver, volta.
- **[erro] Ap. F.** Decidir a estrutura vem antes de furar; as guardas
  entram junto com a costura; o passo 38 é o *pasting down*.
- **[erro] Cap. 2.** "25 palavras" (a tabela tem 26) → "as palavras do
  livro"; in-fólio remete ao cap. 4.
- **[erro] Cap. 4.** 21 × 28 é "quase A4"; in-oitavo comparado a romance,
  não a livro de bolso.
- **[conteúdo] Cap. 14.** A Casa do Restaurador voltou para "Onde
  conseguir": tirei na revisão por não achá-la, e o domínio existe.

### 15 · Douração e cortes (17/11/2026)

Reescrito. O texto anterior ficou guardado em `15-antes-da-revisao.md`,
na raiz do manual, para comparar; pode apagar depois.

- **[lacuna] Cortes não dourados.** Seção nova "O corte: as opções":
  tingido (Cockerell: esponja, cor rala, do centro para as pontas; cera e
  brunidor), salpicado, a grafite, vermelho sob ouro, e uma nota sobre
  marmorizado, pintura na goteira, cinzelado e preto. O cap. 9 prometia
  isso e o cap. 15 só dourava. **O gesto do salpicado e a receita do
  grafite são de bancada, sem fonte — estão marcados assim no texto.**
- **[incoerência] "O ouro racha ao arredondar".** Saiu. O primeiro teste
  continua em bloco reto, mas a justificativa agora é mudar uma variável
  de cada vez; o momento de dourar remete à tabela do cap. 9.
- **[conteúdo] Corte dourado pela sequência de Cockerell:** bolo esfregado
  com escova dura, escovar a seco, cortar o ouro antes do glair, glair
  "flutuado", ~1 h de secagem, couro com cera de abelha, brunir através de
  papel encerado. Entrou a opinião dele contra o corte "sólido".
- **[conteúdo] Douração a ferro refeita por Cockerell:** cego através do
  papel e de novo direto; lavar com água ou vinagre bom; água de engrudo e
  cola em couro poroso; glair só na impressão, com o couro quase seco, e
  só o que se doura no dia; óleo de coco; o gesto (ombro sobre o ferro);
  manejo da folha.
- **[incoerência] Temperatura do ferro.** A regra passou a ser a da
  almofada molhada (parar de chiar ≈ 100 °C e subir). Os 120–125 °C das
  conversas ficaram como faixa de trabalho, coerentes com o cap. 16.
- **[conferir] Folha solta × de transferência.** O texto recomendava
  transferência para o ferro e para o corte. Mudei: solta para glair
  (corte tradicional e ferro), transferência para cola de douração. É
  juízo meu, apoiado em Cockerell só no que toca à folha solta — conferir.
- **[incoerência] Gelatina × cola de coelho.** O argumento se desfazia na
  página seguinte; agora diz que o que salva a gelatina é a diluição e a
  pureza. A tabela ganhou a coluna da gelatina a 1–2%.
- **[erro] Bolo.** "Caulim + óxido de ferro" → argila ferruginosa.
- **[segurança] Iluminura.** Aviso de chumbo no alvaiade.
- **[forma]** "Rota A / Rota B" → método tradicional / método de teste;
  a lista de refile, repetida do cap. 9, virou remissão; receitas de
  glair com as duas versões (Cockerell e conversas) lado a lado; preços
  reduzidos a ordem de grandeza, com nota "preços de 2026"; voz de
  negócio ("peça vendida", "R$ 3.000–8.000") saiu; seção **Fontes**
  criada. A atribuição a Peter Geraty ficou marcada como não conferida.
- **Pendente:** a receita de glair repetida no cap. 16; o PDF foi a 300
  páginas; não revisei a diagramação página a página.
- [forma] (19/11) "O método de teste: cola de douração" → "Cola de
  douração, para o primeiro corte": a palavra "teste" no título fazia o
  gerador levar a seção para o apêndice E, que é de protocolos de teste.

### Organização (19/11/2026)

- `SUGESTOES.md` e este registro viraram um arquivo só: "O que falta" no
  alto, "O que foi feito" embaixo. Os itens já aplicados saíram da lista;
  a seção de erros de fato saiu inteira (corrigida em 17/11).

### 16 · Foil, latão e impressão na capa (19/11/2026)

Revisado contra Cockerell (caps. XIV e XV: ferros, douração e letras) e
Roberts & Etherington. O texto anterior estava inteiro nas conversas; agora o que
tem fonte diz qual, e o resto está marcado.

- **[erro] Composição do foil.** "Poliéster + liberação + laca + alumínio
  + laca tingida + adesivo" punha duas lacas e a cor no lugar errado. São
  filme, liberação, **laca colorida** (a cor de ouro), alumínio, adesivo.
  E foi dito por que o foil dispensa glair: a cola vem nele.
- **[conferir → saiu]** "Fabricantes de artigos de couro relatam
  microtrincas em centenas de ciclos" e "a tecnologia é dos anos 1950":
  sem fonte. Ficou o que se sustenta — o filme não estica, trinca na
  charneira; é material do século XX.
- **[incoerência]** "Não se sobrepõe: você tem uma chance" e, no passo a
  passo, "dá para reposicionar e repetir". Agora: falha pequena se retoca
  no mesmo sulco; foil fora do lugar não sai.
- **[erro] "O vinco de latão é literalmente um ferro de filete reto".** O
  filete é uma **roda**; a linha reta num cabo é a **paleta**; o arco é o
  **gouge**. Seção nova "Ferros de linha" (Cockerell e R&E): o dente do
  filete para fechar cantos, filetes de uma linha só, esfriar na bacia, a
  luz da esquerda. O vinco ficou como paleta arrastada, com o registro de
  R&E (CREASER; e linhas antigas feitas arrastando, em FILLET).
- **[conteúdo] Clichê.** "Você pode blocar o couro plano antes de encapar
  — é assim que se faz em edição" virou o que R&E sustentam: na capa feita
  à parte, bloca-se a **capa pronta, ainda plana**, antes do *casing-in*.
  Entraram a área máxima à mão (~2,5 × 2,5 cm, BLOCKING), a pressão como
  o que fixa o ouro, e a história (bloco do séc. XVI em prensa de rosca;
  prensa aquecida de 1830–32). As prensas baratas: servem para título
  pequeno, não para clichê do tamanho da capa.
- **[erro] Preços de clichê.** 4 × 4 a R$ 150 e 5 × 5 a R$ 146 → "de 3 × 3
  a 5 × 5 cm, R$ 100–150", como no apêndice C.
- **[conteúdo] Gouges.** "Jogo padrão de 12" → jogos de **dez** (R&E);
  mirar por dentro da curva, pouco peso (Cockerell). O filete pequeno
  para curva suave (Cockerell) entrou como primeiro caminho. A conta de
  "~27 impressões" agora diz de onde vem: um desenho de nove arcos. A
  P&S Engraving ficou como exemplo, sem o "arco de 9 polegadas" que não
  conferi.
- **[conteúdo] Letras e tipos.** Letras de cabo × porta-tipos (Cockerell:
  liberdade × regularidade); quatro corpos bastam; a crítica dele às
  letras estreitas e de muito contraste, ligada à lição do vinil (cap.
  17); o bloco de prática (R&E).
- **[conteúdo]** Problemas: duas linhas novas de Cockerell (ferro torcido,
  ponta do gouge que corta); "bater e tirar"; ferro grande com o peso do
  corpo. Pó de resina (*blocking powder*, R&E) para tecido que o glair
  mancharia.
- [forma] Receita de glair repetida → remissão ao cap. 15; "uma ou duas
  demãos" como no cap. 15 (era "3 camadas"). Consulta rápida: título vai
  com tipos, não com vinco. Temperaturas marcadas como ponto de partida.
  Saíram "argumento de venda", "linha simples / linha premium" e a nota
  de processo nas Fontes; `---` duplicado. Seção **Fontes** refeita.

### 6 · Impressão → Impressão do miolo (19/11/2026)

Decisão sua: o cap. 6 fica só com o miolo; a impressão para fora dele vai
para o cap. 16.

- **[estrutura]** Saíram para o cap. 16, seção "Capa, caixa e painel
  impressos": verniz sobre corante, laminação a quente e a frio,
  laminação × verniz, papel para capa e painel, montagem de painel em
  caixa, os dois testes de painel e a "solução pela raiz" (laser). Ficaram
  no 6: a máquina, o driver, o arquivo, o papel, a ondulação, terceirizar
  e as imagens do miolo (papel das pranchas, montagem, cor).
- [forma] Título "Impressão" → **"Impressão do miolo"** (`build.py`,
  `check.py`, `MANUAL.md`). Regra nova de abertura (a antiga era a do
  verniz, que foi junto para o 16); consulta rápida só com o miolo, mais
  as linhas de qualidade no driver, ondulação e pranchas.
- [forma] "Parte I…IV" → seções sem número ("A L4360 e o miolo",
  "Imagens no miolo").
- [forma] As duas caixas "Divergência nas fontes" viraram a conclusão
  direta: qualidade Alta ou Normal depende do papel; laser serve a volume e
  custo, não ao livro como objeto. Saíram os modelos e preços de laser e
  "sobem o ticket".
- **[erro]** "Kit 504 (T504 / linha 544)" → linha **504**: o manual da
  Epson lista a T504 para a L4360; a 544 é de outros modelos.
- [conferir → corrigido] "Jato de tinta pigmentado em papel de algodão é
  o padrão da encadernação fina" → "é comum entre os livros de artista".
- [forma — voz] "detalhe de luxo que o cliente nota", "estética de marca",
  "cardápio / B2B" saíram. Seção **Fontes** criada (não havia).
- Remissões acertadas: cap. 10 ("cap. 6, parte IV" → cap. 16), cap. 17 e
  cap. 19.

### 17 · Plotter de corte e técnicas modernas (19/11/2026)

- **[erro] EasyPress Mini.** "Presets de ~130/155/205 °C" → as faixas que
  a Cricut publica: baixa ~125–145, média ~150–180, alta ~185–205 °C. A
  conclusão (todas acima dos 110–120 °C do couro) continua.
- **[incoerência]** Gabarito de nervos com "espaçamento crescente (cap. 8)"
  → as divisões da lombada do cap. 8.
- **[conteúdo] *Onlay*.** Entrou o método de Cockerell ("Inlaying on
  leather"): couro muito fino, punções de aço no formato dos ferros —
  que é o que a plotter substitui —, papel colado no grão para o couro
  não esticar ao receber o engrudo, chanfrar, engrudo e prensa; e papel
  japonês em vez de couro branco. R&E (ONLAY): em uso na Inglaterra no
  século XVII. "A técnica da encadernação Art Déco" virou "a Art Déco o
  levou ao limite".
- [forma] Laser: o aviso sobre couro cromado, que estava repetido, ficou
  só na tabela; o do corino ganhou linha própria.
- [forma] Arquivos que o leitor não tem (`NEGOCIO.md`, `../CLAUDE.md`,
  `cover/check_vinyl.py`) saíram; o método da medição a 600 dpi ficou.
  O capítulo agora se data (2026, Silhouette Cameo, EasyPress Mini).
- [forma] Foil digital: a versão caseira com laminadora e foil para
  toner. Clichê: "com foil ou com ouro genuíno". Seção **Fontes** refeita.

### 18 · Papéis decorados (20/11/2026)

- **[lacuna] Marmorização.** A frase "há material sobre marmorização em
  outro capítulo" apontava para nada. Entrou a seção inteira: como funciona
  (o princípio dos veios, de Zaehnsdorf), história com data e fonte
  (suminagashi na *Sanjūrokunin kashū*, c. 1112; persas no séc. XVI; Holanda
  1598, Inglaterra c. 1655 — R&E; a anedota do papel holandês nos
  brinquedos, atribuída a Woolnough; tragacanto até meados do XIX,
  carragena depois; Nicholson sem alúmen no papel; data de cada padrão),
  ordem de aprendizado, material, banho de carragena (Dharma Trading:
  proporção, 12 h de descanso, validade; consistência pelo teste de
  Nicholson), alúmen (dose, um lado só, até 2 dias, contaminação do banho),
  tintas e fel (a regra do fel crescente de Nicholson; o lote de
  Zaehnsdorf), passo a passo de uma folha, cinco padrões, tabela de
  defeitos, e o marmorizado no livro (Cockerell, tiragem numa sessão, corte
  marmorizado, reprodução declarada no colofão).
- **[conteúdo — conservação]** O alúmen deixa o papel ácido (solução pH
  3–4; Strlic, CoOL): menor dose, marmorizado colado sobre guarda lisa.
  Aviso contra vermelhão e zarcão dos manuais antigos.
- **[melhoria — equilíbrio]** *Paste paper* ganhou passo a passo (pasta,
  consistência de Zaehnsdorf, sabão, umedecer, espalhar, retirar, refazer,
  secar, prensar, lustrar), ferramentas, papel puxado (R&E, Zaehnsdorf) e o
  cuidado na colagem. Suminagashi e orizomegami ganharam material e passo a
  passo; gelli plate, o limite do filme. Datação do *paste paper*: "alemão,
  século XVIII" → séculos XVI–XVIII, sobretudo Alemanha e Itália (R&E).
- **[incoerência] Gramatura.** Nova subseção "Que papel, que gramatura":
  120–150 g/m² quando o decorado é a própria guarda (cap. 11); 90–120 g/m²
  quando vai colado sobre guarda lisa ou reveste capa. Aquarela,
  cianotipia e kit apontam para ela.
- **[erro] Bugra.** Recomendado para o PB27, mas a Hahnemühle declara
  carbonato (≥4%) e pH 7,5–9,5 em todas as linhas: é tamponado. Ficou para
  pigmentos comuns. **Zerkall:** fora de produção desde 2021 (revendedor).
  Fabriano Ingres: "faça o teste".
- **[incoerência] Fabriano** "funciona bem" na cianotipia × "tamponado ❌"
  na tabela de pH: a lista de marcas saiu; ficou a regra (rótulo *acid
  free* ≈ tamponado; o teste de efervescência decide).
- **[incoerência com o cap. 10]** "PVAs tendem ao levemente alcalino" → o
  PVA comum fica em pH 4–5; o perigo é o PVA "neutro" tamponado.
- **[conferir → corrigido] Teste de envelhecimento.** Saiu o forno a 60 °C
  por dias. O teste foi redesenhado com uma variável só (o papel), metade
  de controle guardada seca e papel de controle sem carbonato.
- [melhoria] O teste de pH abre dizendo que serve para todo papel; o cap. 5
  ganhou a remissão ("Vai durar?" → teste de efervescência, e a exceção do
  azul da Prússia).
- [forma — voz] Saíram "eu evitaria", "sobre o Corfix…", "sua preocupação
  real", a nota sobre o site colorfix.com.br, e as frases de cliente ("não
  prometa a um cliente", "trabalho de cliente", "se o cliente quer", "o que
  se apresenta a um cliente como garantia").
- [forma] "Grude" → "engrudo" no capítulo inteiro. Cera microcristalina:
  "acabamento clássico" → "acabamento de conservação, dos anos 1950
  (cap. 14)". Xilogravura de topo explicada. "Muller" → "moleta". Preços do
  instrumental datados (2026). Livro de amostras ligado ao conselho de
  Zaehnsdorf. Kit com seções de paste paper e marmorização. Seção
  **Fontes** criada (não havia).
- **[erro] Apêndice F.** "Alúmen no papel — horas antes" e "Carragena — 1 h
  antes" saíram da tabela de preparo do dia: a carragena descansa 12 h e o
  papel com alúmen dura até 2 dias; marmorizar é sessão à parte. A linha do
  papel decorado diz isso.
