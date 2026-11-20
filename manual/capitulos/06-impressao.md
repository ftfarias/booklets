# Impressão do miolo

> **A regra que resolve quase tudo:** na L4360, **o preto é pigmento e as
> cores são corante**. Texto em preto puro, no modo que usa o pigmento,
> sai à prova d'água e de cola; cor no miolo é passivo. Quanto mais
> absorvente o papel e mais densa a página, menos tinta — e nenhuma folha
> se dobra antes de curar e passar pela prensa.

Este capítulo é sobre imprimir o **miolo** em casa: a máquina, o arquivo,
o papel, a ondulação, as imagens. Capa, caixa e painel impressos — verniz,
laminação, montagem — estão no cap. 16.

## Consulta rápida — o que fazer em cada situação

| Situação | Resposta |
|---|---|
| Texto preto no miolo | K puro / "Preto e escala de cinza" no driver. Já é à prova d'água |
| Qualidade no driver | Papel liso: Alta. Papel absorvente com página cheia: Normal |
| Nitidez de texto máxima | Alinhamento de cabeça + alta velocidade **desligada** |
| Folha ondulada | Secar 24 h separada, prensar 24–48 h, só então dobrar |
| Cor no miolo | Evite. Se houver, 24 h de secagem e nenhuma cola encostando na área colorida |
| Imagem colorida no livro | Prancha em papel fotográfico fosco, colada pela margem (*tip-in*) |
| Papel couché comum | Não funciona. Incompatibilidade física, não questão de tempo |
| Tiragem acima de ~5 exemplares | Terceirizar em laser/toner |
| Capa, caixa ou painel impressos | Cap. 16 |

### O critério, quando a tabela não cobre

- **A tinta preta é pigmentada; as cores são corante.** Tudo neste capítulo
  decorre daí. Preto = estável, à prova d'água, resistente a cola. Cor =
  hidrossolúvel, sensível à luz e a poluentes.
- **Jato de tinta deposita água.** A folha ondula ao secar, e essa água tem
  de sair antes de a folha ser dobrada, colada ou prensada contra outra.
- **Papel revestido para inkjet retém o corante numa camada polimérica.**
  Papel comum não. Metade dos problemas da cor se resolve trocando o papel.

---

## A L4360 e o miolo

### Primeiro, entender a máquina

A EcoTank L4360 usa as tintas da linha **504** (T504): **preto
pigmentado + ciano, magenta e amarelo à base de corante (*dye*)**. Isso
explica praticamente todo o comportamento dela.

**O que isso destrava:**

- **Texto preto à prova d'água e resistente à cola.** PVA, umidade de
  prensa, dedo suado: não borra. Pigmento também é razoavelmente estável à
  luz. Para miolo monocromático, você está tecnicamente bem servido.
- **Custo por página imbatível.** Um frasco de 127 ml de preto rende
  alguns milhares de páginas → algo na casa de **R$ 0,01–0,02 por página**
  (toner laser fica em R$ 0,03–0,06). Um miolo de 300 páginas custa
  centavos de tinta.
- **Boa aparência em papel offset não revestido** (Pólen, Chamois,
  Munken): sem o brilho plástico do toner, o texto assenta no papel como
  impressão de livro. O preço é um pouco de nitidez — papel absorvente
  engorda o traço (ver Camada 3).

> ⚠️ **A armadilha que quase ninguém conhece.** Nas EcoTank de 4 tintas,
> quando você seleciona um **papel brilhante/fotográfico** no driver, a
> impressora **desliga o preto pigmentado** e "monta" o preto misturando
> CMY. O resultado é um preto acinzentado, azulado ou com fundo magenta,
> sem densidade. Muita gente com aparência "amadora" está caindo nisso sem
> perceber. **Nunca selecione perfil fotográfico/brilhante para texto.**

**O teste que resolve a dúvida:** imprima um bloco de texto em cada modo
de papel, espere secar 24 h, pingue água. Se borrar, aquele modo não está
usando pigmento. **Escolha o modo com base nesse teste, não no nome do
papel.**

### Camada 1 — Ajustes de driver (custo zero, maior impacto)

Nesta ordem:

1. **Alinhamento da cabeça de impressão.** Manutenção → Alinhamento →
   rode os dois: *vertical* e *linha reta/horizontal*. Impressora nova de
   fábrica raramente vem alinhada. Isso sozinho pode ser a diferença entre
   texto "levemente fantasma" e texto nítido.
2. **Desligue a impressão bidirecional** (Mais opções → desmarcar "Alta
   velocidade"). Bidirecional imprime nos dois sentidos do carro, e
   qualquer folga mecânica gera microdesalinhamento entre as passadas — é
   o que dá aquela aparência de letra "borrada em duas camadas". Fica mais
   lento e visivelmente mais nítido.
3. **Marque "Preto / Escala de cinza"** para páginas de texto. Força o uso
   exclusivo do preto pigmentado: preto mais denso, secagem mais rápida,
   resistência à água, **sem franja colorida nas bordas das letras**. Sem
   isso, um preto RGB (0,0,0) pode ser convertido em preto composto CMYK e
   você ganha aberrações coloridas ao redor de cada caractere.
4. **Tipo de papel: teste "Papel Comum" contra "Papel Mate/Fosco".** São
   dois perfis de deposição diferentes:
   - *Papel Comum* → menos tinta, texto mais fino e seco, menos empeno
   - *Papel Mate* → mais tinta, preto mais cheio, mas risco de espalhamento
     e ondulação

   Em papel liso e pouco absorvente (Opalina 120), **"Papel Comum" com
   qualidade Alta geralmente ganha para texto.**
5. **Qualidade: depende do papel** — "Alta" em papel liso; em papel
   absorvente com página densa, "Padrão" (ver o quadro abaixo). Nunca
   "Econômico". Se houver controle de densidade em Personalizado →
   Avançado, reduzir um pouco a saturação ajuda em papel liso.

> **Alta ou Normal? Depende do papel.** Em papel liso e pouco absorvente
> (Opalina, matte revestido), Alta ganha: a tinta não espalha e a
> ondulação é menor. Em papel absorvente de miolo (Pólen, offset), com a
> página cheia de texto, Alta só deposita mais água sem ganho visível — a
> 1440 dpi o texto já está ótimo, e Normal é a escolha. A regra:
> **quanto mais absorvente o papel e mais densa a página, menos tinta.**

### Camada 2 — O arquivo (o culpado silencioso mais comum)

Se a impressão parece amadora mesmo com texto legível, muitas vezes o
problema entrou antes da impressora:

- **Imprima o PDF em "Tamanho real" / 100%**, jamais em "Ajustar à
  página". Ajuste automático reamostra o conteúdo e destrói a nitidez das
  fontes.
- **Desmarque "Imprimir como imagem"** no Acrobat. Se estiver marcado,
  você está imprimindo um raster de baixa resolução. Só use se houver erro
  de fonte — e aí em 600 dpi.
- **Imagens em 300 dpi no tamanho final.** Um PNG de 150 dpi esticado é o
  sinal nº 1 de trabalho amador.
- **Evite fontes de traço muito fino.** Jato de tinta em papel não
  revestido tem ganho de ponto: a tinta espalha nas fibras e engorda o
  traço, e hastes finas viram borrão cinza. Prefira serifadas de traço
  robusto e contraste moderado, em 10–11 pt com entrelinha de ~130–140%.
- **Margens.** Isso é enorme. Livro amador tem margens iguais e apertadas;
  livro profissional tem margens desiguais e generosas, com a de baixo a
  maior. Só arrumar as margens transforma a percepção da página — as
  proporções estão no cap. 4.
- Confira viúvas, órfãs, rios de branco na justificação, e hifenização
  ligada.

### Camada 3 — Papel

| Papel | O que esperar |
|---|---|
| **Opalina / Markatto 120 g** | Liso, boa nitidez, cara de livro. Provavelmente o teto do que a L4360 entrega em texto |
| Papel fotográfico **fosco (matte)** para jato de tinta, 108–180 g | A nitidez máxima possível: revestimento poroso feito para tinta aquosa, preto muito mais denso. Contra: tato levemente plastificado, pouco livresco. Ideal para ilustrações e provas |
| Sulfite premium alta alvura (ex. Report Premium 90 g) | Mais branco e uniforme que o sulfite comum. Miolo econômico |
| **Pólen Bold 90 g** | Confortável de ler, opaco, cara de livro de verdade — mas absorvente e "come" a nitidez. Ótimo para texto corrido, ruim para imagens finas |
| Markatto Concetto / Sumo (texturado) | Bonito, mas a textura espalha a tinta e serrilha as letras. Capas e folhas de cortesia, não texto |
| Vergê | As vergaturas quebram o traço do texto. **Evite no miolo** |
| **Couché brilho ou fosco (offset)** | **Incompatível.** Ver abaixo |

> ⚠️ **Couché comum nunca vai secar, e a culpa não é sua.** O revestimento
> mineral não poroso foi projetado para tinta offset à base de óleo, que
> seca por oxidação. Tinta aquosa não tem para onde ir: o pigmento fica
> pousado na superfície e o corante empoça. **Não é questão de tempo, é
> incompatibilidade física.** Existe "couché para jato de tinta", mas é
> raro no varejo.

**Duplex automático:** homologado para papel comum de ~64–90 g/m². Opalina
120 exige duplex manual — o que, além do peso, dá a chance de deixar a
frente secar antes do verso, evitando que os roletes marquem a página.
Se o duplex automático marcar a folha mesmo em papel leve, imprima em duas
passadas: as páginas ímpares, 30 minutos de espera, as pares.
*(O registro frente/verso — e como medi-lo — está no cap. 4.)*

**Gramatura no alimentador:** 80–90 g/m² passa bem na bandeja. Acima de
~100–120 g/m², use alimentação manual folha por folha se o modelo tiver.
Não force a bandeja com 180 g/m².

### Camada 4 — O que realmente separa amador de profissional

Estes três pesam mais que o papel:

1. **Refile.** Um miolo com cortes de tesoura ou estilete tremido grita
   "amador", independentemente da qualidade da impressão. Três faces
   aparadas retas e no esquadro mudam a percepção completamente.
2. **Cura e prensagem.** Deixe as folhas curarem 24–48 h **separadas**
   (não empilhadas coladas) e depois prense. Jato de tinta deposita água:
   a folha ondula ao secar; a prensa resolve.
3. **Consistência.** Todas as folhas do mesmo lote, mesmo sentido de
   fibra, mesmo branco.

### Ciclo de trabalho e manutenção

| Problema | Gravidade | Mitigação |
|---|---|---|
| **Ondulação (*cockling*)** — a tinta é aquosa e o papel expande | **Alta, é o principal** | Papel ≥ 90 g/m², qualidade menor em página densa, fibra correta, secar 24 h intercaladas, prensar entre tábuas 24–48 h antes de dobrar |
| Velocidade | Alta em volume | Terceirizar tiragens |
| Ciclo de trabalho | Média | ~800 páginas/mês é o confortável; acima disso a cabeça sofre |
| Cor no miolo = corante | Alta se usar cor | Não usar cor no miolo; usar pranchas coladas |
| Entupimento dos canais de cor por desuso | Baixa | Rodar um teste de bicos ou uma faixa colorida por semana |

**Duas coisas para nunca fazer:** (1) usar modo "alta qualidade / foto" em
papel absorvente — carga excessiva de tinta piora a ondulação sem ganho
visível; (2) deixar cola de lombada encostar em área impressa **em cor**,
porque ali o corante corre. Na prática: **15–20 mm junto à lombada sem
cor chapada**.

**Não dobre folha recém-impressa.** A tinta ainda migra e você marca a
página oposta.

Tenha em estoque uma **caixa de manutenção sobressalente** e frascos de
preto.

### Ondulação: o protocolo completo

1. Papel de 90 g/m² ou mais, com **fibra na direção certa**
2. Qualidade adequada à absorvência do papel (Camada 1)
3. Folhas secando **24 h, separadas ou intercaladas** — nunca empilhadas
   coladas
4. **Prensa entre tábuas, 24–48 h**, antes de dobrar
5. Só então vincar e dobrar

### Protocolo de teste de papel (uma tarde, resolve tudo)

Antes de qualquer compra nova:

1. Escolha 4 papéis candidatos. **Confirme o sentido da fibra em cada
   um** — tem que correr paralela à lombada.
2. Imprima a mesma página de texto em cada, em "papel comum / qualidade
   alta", preto composto desligado (só pigmento), bidirecional desativada.
3. **Após 24 h:** teste da gota (pingue água, espere 1 min, encoste papel
   absorvente), teste de atrito (unha e borracha) e **teste de cola** (passe
   PVA sobre o texto).
4. Meça a **transparência** (o que se vê da página seguinte) e a
   **ondulação** antes e depois de prensar.
5. **Anote o tempo real de impressão de 100 folhas duplex.** Esse número é
   o que define se você imprime ou terceiriza.

O papel que passar nos cinco vira o padrão da casa — e você o compra em
folha grande (66×96 ou 76×112) para cortar na fibra certa.

### Quando terceirizar

Uma gráfica digital com laser SRA3 imprime miolo P&B a **R$ 0,08–0,20 por
página**. Um livro A5 de 300 páginas sai por **R$ 25–60**, com 8 páginas
por folha, pronto em horas. Compare com 3–4 horas suas na Epson.

**Modelo sugerido:** imprima peças únicas e protótipos; **terceirize
qualquer coisa acima de ~5 exemplares.** Procure uma gráfica que aceite
(a) seu papel fornecido, (b) sentido de fibra especificado, (c) sua
imposição já pronta em PDF. Vale visitar 4 ou 5 até achar um operador que
entenda o pedido — quando achar, é parceiro de anos.

**Comprar uma laser?** Para volume e custo, ela é a resposta: toner é
plástico fundido — não penetra, não espalha, não tem ganho de ponto, seca
na hora e é à prova d'água. Para o livro como objeto, não: o toner fica
**sobre** o papel, com brilho plástico, achata a textura e **pode
craquelar na dobra**, sobretudo em papel encorpado e em preto chapado.
Jato de tinta pigmentado em papel de algodão é comum entre os livros de
artista de hoje. **A decisão adotada:** não comprar laser; terceirizar o
volume quando precisar.

O upgrade que faz sentido para livro de arte não é laser: é uma
**Epson SureColor P700/P900** (ou similar com pigmento em múltiplas
tintas) — caminho reto para mídia espessa, aceita papel de arte de 300 g+,
preto matte próprio, formato A3+ (P700) ou A2 (P900).

---

## Imagens no miolo

### Papel: o glossy 180 g não serve

Cinco motivos para não usar glossy no miolo ou em pranchas:

1. **Provavelmente é *cast-coated*, não RC.** O glossy 180 g genérico
   brasileiro é papel-base com camada de caulim fundida. Empena feio,
   absorve umidade, e a camada literalmente incha e descasca com água.
   Ironicamente, **é o papel menos resistente à água que se poderia
   escolher** — sem verniz, uma gota destrói.
2. **Bloqueio sob prensa.** Duas faces brilhantes prensadas juntas grudam
   (efeito *ferrotype*). Você abre o livro depois de uma semana na prensa e
   a prancha arrancou a face da página oposta.
3. **Adesão de cola.** Se for RC (*resin-coated*, papel entre duas películas de polietileno), **PVA não adere** à
   superfície. A prancha solta em três meses.
4. **Estética.** Brilho não combina com couro, papel offset creme e
   douração. Numa *fine binding*, a prancha glossy é o elemento que grita
   "impressora de casa".
5. **Guarda marca de dedo para sempre.**

| Uso | Papel | Por quê |
|---|---|---|
| **Pranchas *tip-in* (recomendado)** | Fotográfico **matte/fosco** 180–230 g | Corante rende muito bem em fosco, aceita cola, sem brilho, sem bloqueio |
| Alto de gama | *Fine art* matte / algodão (Hahnemühle Photo Rag 188/308, Canson Rag Photographique) | Textura de gravura, casa com couro. Caro |
| Meio-termo elegante | Acetinado / *luster* 200 g | Mais saturação que o fosco, sem o espelho do glossy |
| Frontispício integrado ao miolo | O próprio Pólen/Chamois, em monocromia ou duotone | Continuidade visual perfeita, menos gama de cor |
| **Nunca** | Glossy ou RC no miolo | Os cinco motivos acima |

**O fosco geralmente vence o glossy:** a perda de gama é pequena, e você
ganha colagem, ausência de bloqueio e uma aparência de gravura que valoriza
o objeto.

### Montar as pranchas

- ***Tip-in*:** cordão de PVA de **3–4 mm apenas na margem da lombada**,
  nunca a folha inteira. Deixe a prancha **2–3 mm menor** que o formato
  refilado, para não ser cortada nem esfregar na borda.
- **Se o papel for RC:** lixe levemente (lixa 400) a faixa de 5 mm que vai
  receber cola, ou monte a prancha sobre uma folha de papel offset
  (*plate mounted on leaf*) — a solução histórica, e fica mais bonita.
- **Prancha em página dupla** ou que precisa abrir plana: use *guard* de
  papel japonês em vez de colar direto.
- **Papel de seda / glassine entre a prancha e a página oposta:** protege
  do *offset* de tinta e do bloqueio. Custa quase nada e é um detalhe que
  se nota.
- **Prensa:** intercale as pranchas com papel siliconado ou glassine
  durante toda a prensagem.

### Cor no miolo

O ponto fraco real do conjunto. Três saídas, em ordem de qualidade:

1. **Tip-in:** mande imprimir as pranchas separadamente em gráfica com
   laser ou pigmento integral, e cole-as manualmente. É exatamente como as
   edições finas históricas faziam — fica mais bonito e mais autêntico que
   prancha impressa no mesmo papel do miolo.
2. **Monocromia elegante:** gravuras em preto puro, ou duotone com o preto
   pigmentado + um segundo elemento aplicado à mão (aquarela, estêncil
   cortado na Cameo, *hot foil*). **Vira estilo, não
   limitação.**
3. Se um dia comprar A3, **procure na ficha técnica "pigmento nos quatro
   canais"** — normalmente linhas WorkForce Pro / DURABrite. Muitas EcoTank
   A3 repetem o mesmo arranjo "preto pigmento + cor corante" e **não
   resolveriam nada**.

> **K puro, ponto.** Nada de preto rico, nada de cinza composto, nada de
> cor no texto. Os corantes CMY não são estáveis à luz — num livro que deve
> durar, são passivo. Um miolo 100% K em papel bom, com capitulares ou
> rubricas aplicadas à mão em vermelho (aquarela, guache, bico de pena), é
> mais *fine press* que qualquer coisa que a impressora faça em cor.

---

## Fontes

Não há fonte clássica para impressão a jato de tinta. Este capítulo vem
das conversas de pesquisa e dos testes na L4360. As tintas de reposição
(linha 504) são as do manual da Epson; que o preto é pigmentado e as cores
são corante, confirme pelo teste da gota, na própria máquina. Modelos,
preços e rendimentos são de 2026 e envelhecem rápido.
