# Impressão

> **A regra de ouro da proteção:** sobre tinta corante, **só verniz à base
> de solvente**. Qualquer coisa aquosa dissolve o corante e borra —
> inclusive o verniz "acrílico à base d'água".

## Consulta rápida — o que fazer em cada situação

| Situação | Resposta |
|---|---|
| Texto preto no miolo | K puro / "Preto e escala de cinza" no driver. Já é à prova d'água |
| Cor no miolo | Evite. Se houver, 24 h de secagem e nenhuma cola encostando na área colorida |
| Proteger impressão colorida dentro do livro | Verniz acrílico **spray, base solvente**, 3–4 demãos, cura 72 h |
| Peça que vai encarar líquido de verdade | Laminação a frio (BOPP autoadesivo) nos dois lados, com encapsulamento de 3–5 mm |
| Painel colorido em caixa/slipcase | Laminar só a face impressa (o verso fica papel cru e cola normalmente) |
| Laminação a quente enrugando | Secar 24–48 h → 90 °C → filme 30–35 µ → *carrier* |
| Nitidez de texto máxima | Alinhamento de cabeça + alta velocidade **desligada** + qualidade Alta |
| Papel couché comum | Não funciona. Incompatibilidade física, não questão de tempo |
| Tiragem acima de ~5 exemplares | Terceirizar em laser/toner |

### O critério, quando a tabela não cobre

- **A tinta preta é pigmentada; as cores são corante.** Tudo neste capítulo
  decorre daí. Preto = estável, à prova d'água, resistente a cola. Cor =
  hidrossolúvel, sensível à luz e a poluentes.
- **Toda a água que entra no papel tem que sair.** Se houver barreira
  (laminado, verniz), ela sai devagar e pelas bordas — daí a bolha, o
  tunelamento e o painel que se levanta semanas depois.
- **Papel revestido para inkjet retém o corante numa camada polimérica.**
  Papel comum não. Metade dos problemas de corante se resolvem antes de
  qualquer verniz, só trocando o papel.
- **Se a fidelidade de cor servir, o laser/toner elimina a cadeia inteira
  de problemas.** Custa alguns reais por folha numa gráfica rápida.

---

## Parte I — Fazer a L4360 render um miolo profissional

### Primeiro, entender a máquina

A EcoTank L4360 usa o kit de tintas 504 (T504 / linha 544): **preto
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

> ⚠️ **Divergência nas fontes.** Uma conversa manda usar qualidade
> **"Alta"** para ganhar nitidez; outra manda usar **"Normal/Padrão"**
> para reduzir a ondulação, argumentando que a 1440 dpi o texto já está
> ótimo. As duas estão certas em contextos diferentes, e a distinção é
> **o papel**: em papel liso e pouco absorvente (Opalina, matte revestido),
> Alta ganha, porque a tinta não espalha e a ondulação é menor. Em papel
> absorvente e de miolo (Pólen, offset), com página cheia de texto, Alta só
> deposita mais água sem ganho visível — aí Normal é a escolha. A regra
> operacional: **quanto mais absorvente o papel e mais densa a página,
> menos tinta.**

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
2. Qualidade adequada à absorvência do papel (ver a divergência acima)
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

> ⚠️ **Divergência nas fontes sobre comprar uma laser.** Uma conversa
> recomenda comprar uma laser monocromática de entrada (Brother HL-B2000D /
> HL-L2400, ou HL-L5100/L6202 mais robusta, R$ 1.500–3.500) porque "toner é
> plástico fundido: não penetra, não espalha, sem ganho de ponto, seca
> instantaneamente, à prova d'água". Outra conversa, já sabendo que o preto
> é pigmentado, **cancela essa compra**: para livro de arte a laser
> geralmente perde — o toner fica *sobre* a superfície com brilho plástico
> perceptível, achata a textura do papel e **pode craquelar na dobra**,
> especialmente em papel encorpado e em áreas de preto chapado. Jato de
> tinta pigmentado em papel de algodão é o padrão da encadernação fina
> contemporânea, não a exceção. **A posição adotada:** não comprar laser;
> realocar o dinheiro para os equipamentos que sobem o ticket e
> terceirizar volume quando precisar. A laser continua
> sendo a resposta certa quando o critério é **volume e custo**, não
> qualidade de objeto — daí a recomendação persistir na conversa de
> negócio.

O upgrade que faz sentido para livro de arte não é laser: é uma
**Epson SureColor P700/P900** (ou similar com pigmento em múltiplas
tintas) — caminho reto para mídia espessa, aceita papel de arte de 300 g+,
preto matte próprio, formato A3+ (P700) ou A2 (P900).

---

## Parte II — Proteger impressões a corante

### A regra de ouro

**Corante é hidrossolúvel.** Qualquer coisa à base de água sobre ele —
verniz acrílico aquoso, PVA diluído, cola em spray aquosa, respingo de
umidade — dissolve o corante e faz sangrar. As cores viram um borrão,
principalmente pretos compostos e áreas escuras.

**Verniz à base de solvente** (acrílico em spray comum, tipo
automotivo/artístico) não dissolve o corante: **encapsula**.

> **E aqui está o truque que vale ouro para encadernação:** depois de
> selado com 3–4 demãos de verniz solvente, **a impressão fica compatível
> com meios aquosos.** Você pode passar PVA, colar, prensar, até aquarelar
> por cima. É o método padrão para trabalhar sobre inkjet.

*(Que adesivo usar para colar a impressão em si — inclusive por que amido e
CMC são as piores escolhas nesse caso — está no **cap. 10**.)*

### Como aplicar: o erro clássico é a primeira demão

1. **Cure a impressão:** 24 h no mínimo, 48 h ideal. Corante
   recém-impresso ainda tem solvente/glicol na superfície.
2. **Primeira demão = "demão de poeira".** Spray a 30–40 cm, movimento
   rápido, cobertura parcial, quase seco ao tocar o papel. **Se você
   encharcar na primeira demão, o solvente carrega o corante lateralmente
   e você vê halos.** Espere 15 min.
3. **Segunda demão leve, cruzada** (perpendicular à primeira). Espere
   20 min.
4. **Terceira e quarta demãos** já podem ser mais generosas. É daí em
   diante que vem a barreira real de água.
5. **Cura total: 72 h antes de prensar ou colar.** Verniz "seco ao toque"
   em 20 min ainda está liberando solvente, e sob prensa gruda na folha
   vizinha.
6. Ambiente ventilado, máscara. **Nada de fazer isso na mesma sala do
   couro e do papel** — o *overspray* assenta em tudo.

Para proteção de verdade sobre papel glossy inkjet, a orientação da Golden
é mais dura ainda: **6–10 camadas leves** aplicadas a spray. Duas demãos
não é proteção, é ilusão. E **não pincele as primeiras demãos sobre glossy
inkjet — arrasta.** Spray só.

### Produtos e faixas de preço no Brasil

| Faixa | Produto | Observação |
|---|---|---|
| **Ideal** | Hahnemühle Protective Spray, Ghiant Inkjet Fixative, Marabu Fixativ, **Golden Archival MSA / Archival Varnish aerossol** | Formulados para inkjet, não amarelam, removíveis. Caros e escassos no Brasil |
| **Melhor custo/benefício** | **Krylon Kamar Varnish** (primeira camada) + **Krylon UV-Resistant Clear** | O combo consagrado. O Kamar é feito exatamente para selar inkjet sem sangrar. Importado, mas aparece aqui |
| **Prático no Brasil** | Corfix Verniz Acrílico Spray, Acrilex Verniz Spray, Colorgin Verniz Geral, Chemicolor | Funcionam bem. **Testar amarelecimento** — verniz barato amarela em 1–2 anos, o que é fatal em branco de papel |
| **Para slipcase** | Verniz PU automotivo spray | Bem mais duro e resistente à água. Não é arquivístico e pode amarelar |
| **Evitar** | Qualquer verniz "base água / à base d'água", fixador de cabelo, PVA diluído | **Sangram** |
| **Cuidado** | Verniz automotivo brilhante | Sela muito bem, mas é espesso, amarela, e o cheiro persiste em livro fechado |

> **Nota da Golden, explícita:** o Polymer Varnish (aquoso) **não deve ser
> usado** em impressões digitais, porque as tintas são hidrossolúveis e vão
> manchar. Para isso existe o **MSA Varnish** (base aguarrás) e o Archival
> Varnish aerossol.

**Acabamento:** prefira **fosco ou acetinado**. Brilhante sobre papel
glossy vira um espelho que denuncia "impressão caseira", e realça
*bronzing* (aquele reflexo esverdeado/avermelhado em áreas escuras de
corante). Sobre papel glossy qualquer irregularidade aparece; acetinado e
fosco perdoam muito mais.

**Teste em sobra sempre:** alguns sprays deixam o revestimento glossy
leitoso ou pegajoso.

### O que o verniz *não* resolve

- **Desbotamento por UV.** Verniz com bloqueio UV ajuda, mas o corante
  dessas EcoTank tem longevidade estimada em **poucos anos em exposição
  direta**, contra décadas do pigmento. **Dentro de um livro fechado,
  protegido da luz, a vida útil é muito maior** — o que joga a seu favor.
- **Imersão.** Continua sendo *resistente* à água, não impermeável.
  Respingo, dedo úmido, umidade de prensa: ok. Copo derrubado: não.
- **Abrasão pesada.** Resistência inferior a filme de 30 µ — e slipcase é
  a peça que mais sofre atrito da estante.
- **Uniformidade de brilho** é difícil: casca de laranja, poeira.

**O que o verniz *ganha* e a laminação não:** você pode envernizar **depois
de colar** o painel na caixa, selando face, bordas e junção num filme
contínuo. Isso mata o problema da "borda de papel nua", além de nunca gerar
ruga. Se fizer assim, **mascare bem o revestimento da caixa**, senão ele
também muda de aparência.

### Fading por ozônio

Corante é sensível a poluentes atmosféricos. O verniz reduz isso
bastante — é um dos seus principais ganhos, e o menos mencionado.

---

## Parte III — Laminação

### Laminação a quente (BOPP térmico)

#### Diagnóstico de rugas pela direção das linhas

Olhe uma peça reprovada **contra a luz rasante**:

| Padrão das linhas | Causa provável |
|---|---|
| **Paralelas ao sentido de saída** (compridas) | Filme frouxo — tensão de desenrolamento baixa demais; o filme sobra na largura e junta antes do *nip* |
| **Transversais** (ondinhas atravessando) | Umidade escapando do papel, temperatura alta, ou velocidade × *tack* descompassados |
| **Diagonais / espinha de peixe** | Alimentação torta ou eixo/rolo desalinhado |
| **Sempre na mesma posição, peça após peça** | Mecânico: resíduo de adesivo no rolo ou rolo gasto — **limpe primeiro** |

Esse último é o teste mais rápido de todos: se a linha reaparece no mesmo
lugar, não é tensão nem umidade, é o rolo.

#### Por que o papel glossy é o pior caso

Papel glossy revestido é liso e não poroso: **o adesivo agarra
instantaneamente e por inteiro na linha do *nip***. Em papel poroso o
vínculo se forma mais gradualmente e o filme consegue acomodar uma sobra
mínima. No glossy não: qualquer excesso de comprimento de filme fica
travado no lugar como um vinco. Papel couché brilhante é notoriamente o
substrato mais difícil para BOPP térmico.

**E há o agravante da umidade**, que costuma ser o culpado principal:
papel glossy 180 g/m² para inkjet (geralmente *cast-coated*, não RC) tem
camada receptora **altamente higroscópica**, e você acabou de injetar
tinta à base de água nela. A 100–110 °C essa água vira vapor e a folha
muda de dimensão *enquanto está sendo colada*. Isso produz exatamente
ondulações finas e palpáveis.

**Teste que isola isso em 5 minutos:** lamine uma folha **em branco** do
mesmo papel, nas mesmas condições.

- Enrugou igual → é papel / tensão / temperatura.
- Saiu lisa → é a **umidade da tinta**. Vá direto para a correção 1.

#### Correções, em ordem de custo-benefício

1. **Seque antes de laminar.** Deixe a impressão 24–48 h plana, sob peso,
   em ambiente seco. Depois, **imediatamente antes**: passe a folha pela
   laminadora dentro de um *carrier* (pasta de kraft dobrada), **sem
   filme**. Isso pré-aquece, seca e faz a folha entrar plana e quente no
   *nip*. Lamine em seguida, ainda morna. **É o truque de maior impacto
   isolado.**
2. **Abaixe a temperatura e a velocidade.** Contraintuitivo, mas o BOPP
   térmico trabalha bem a **90–95 °C**, e 18 µ encolhe/relaxa com
   facilidade perto de 110 °C. *Regra da indústria: quando se sobe a
   temperatura, tem que reduzir a tensão do desenrolamento, senão o filme
   encolhe e enruga.* Vá a 90 °C, velocidade mínima.
3. **Ajuste a tensão do filme em incrementos mínimos.** Frouxo = o filme
   junta antes do *nip* (rugas). Apertado = estica e relaxa ao esfriar
   (tunelamento, vincos estreitos). **Alvo:** filme retesado, sem barriga,
   mas o rolo ainda gira à mão com resistência leve. Confirme que o filme
   toca o papel **só no *nip*** — contato antes do *nip* enruga sempre.
4. **Troque 18 µ por 30–35 µ.** Provavelmente a melhor jogada. 18 µ é
   finíssimo e elástico; 30–35 µ (ou, melhor, filme de **poliéster/PET**)
   tem rigidez suficiente para não acumular sobra. E slipcase já pedia mais
   resistência à abrasão mesmo — resolve dois problemas.
5. **Alimente e esfrie corretamente:**
   - Use ***carrier* sempre** (distribui pressão, mata rugas de borda de
     entrada)
   - Folha perfeitamente esquadrada; **nunca empurre nem puxe**. Segure os
     cantos de trás e faça leve tração para trás e para os lados conforme
     entra
   - Alimente folhas **emendadas** (uma encostada na outra) ou com uma
     placa-guia da mesma espessura, para o filme não vencer um degrau
   - Saindo da máquina, **direto sob peso até esfriar completamente**.
     BOPP quente relaxa ao esfriar; solto, ele ondula
6. **Lamine grande, corte depois.** Rugas se concentram nas bordas e na
   entrada. Lamine um A4 inteiro e recorte o painel da região boa do meio.
   Simples e resolve muita coisa na prática.

#### Espessuras

| Espessura | Uso |
|---|---|
| 18 µ | Fino demais para superfície de contato. Aceitável em painel interno |
| **30–40 µ** | **Slipcase, painel externo, qualquer coisa que sofre atrito** |
| PET em vez de BOPP | Mais rígido, mais transparente, não amarela, mais estável |

### Laminação a frio — a opção mais segura para corante

Filme transparente autoadesivo (PET ou PVC + adesivo sensível à pressão,
com *liner*), aplicado com rodo, **sem calor**. Resolve os dois problemas
de uma vez: **zero calor** (nada de vapor, encolhimento ou ruga) e **zero
água** (nada de corante migrando).

- **Fácil de achar no Brasil:** "filme/vinil transparente para laminação a
  frio", "BOPP a frio", em folhas A4 ou por metro em lojas de comunicação
  visual.
- **Prefira PET a PVC** (mais transparente, não amarela, mais estável) e
  **adesivo acrílico**.
- **Técnica:** fixe uma borda, vá descolando o *liner* progressivamente
  enquanto puxa o rodo em ângulo baixo — igual película de celular.
  Aplicação a seco: **nada de água com detergente aqui**.
- Não é coincidência que guias de laminadoras digam que fotos inkjet
  recém-impressas **requerem** laminação a frio.

**Para impermeabilidade real:** laminação a frio nos **dois lados**, com
selagem de 3–5 mm de borda a borda (**encapsulamento**). Aí sim é à prova
d'água de verdade. É o caminho para cardápio, carta de vinhos, livro de
hóspedes.

**O truque para painéis de caixa:** lamine **só a face impressa**. O verso
continua sendo papel cru, então o PVA adere normalmente. Você ganha
impermeabilidade e resistência à abrasão sem perder a colagem.

### Laminação vs. verniz — quando usar cada um

| | Laminação | Verniz |
|---|---|---|
| **Painel plano, sem dobra** | ✅ ideal | ok |
| **Wrap que precisa dobrar** | ❌ racha e descola nas dobras e viradas | ✅ mantém o papel flexível |
| Resistência à abrasão | Superior (30 µ+) | Inferior |
| Selar bordas e junção depois de montado | Não | ✅ sim, filme contínuo |
| Risco de ruga | Real (a quente) / nulo (a frio) | Nulo |
| Uniformidade | Alta | Difícil (casca de laranja, poeira) |

**Ordem recomendada de ataque quando algo dá errado na laminação a
quente:** teste a folha em branco para confirmar o diagnóstico →
secagem + 90 °C + filme de 30 µ (mantém o fluxo atual e provavelmente
resolve) → se quiser eliminar o risco de vez, laminação a frio → verniz
solvente como plano B, ciente da abrasão.

---

## Parte IV — Montagem de imagens no livro e na caixa

### Papel para imagens: o glossy 180 g não serve

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
| Cardápio / B2B | Glossy ou RC **+ laminação** | Aqui o glossy faz sentido |
| Painéis / *onlays* de caixa | Fotográfico fosco 160–200 g ou *fine art* matte | Pode ser encorpado, já que não dobra |
| **Wrap com dobra** | Matte *coated* ou offset bom, **100–140 g**, fibra no sentido do wrap | Acima de ~160 g racha na dobra |
| **Nunca** | Glossy, RC, qualquer coisa acima de ~160 g em área de dobra | — |

**O fosco geralmente vence o glossy:** a perda de gama é pequena, e você
ganha colagem, ausência de bloqueio e uma aparência de gravura que valoriza
o objeto.

### Técnica de montagem das pranchas

- ***Tip-in*:** cordão de PVA de **3–4 mm apenas na margem da lombada**,
  nunca a folha inteira. Deixe a prancha **2–3 mm menor** que o formato
  refilado, para não ser cortada nem esfregar na borda.
- **Se o papel for RC:** lixe levemente (lixa 400) a faixa de 5 mm que vai
  receber cola, ou monte a prancha sobre uma folha de papel offset
  (*plate mounted on leaf*) — a solução histórica, e fica mais bonita.
- **Prancha em página dupla** ou que precisa abrir plana: use *guard* de
  papel japonês em vez de colar direto.
- **Papel de seda / glassine entre a prancha e a página oposta:** protege
  do *offset* de tinta, protege do bloqueio, e é um daqueles detalhes de
  luxo que o cliente nota imediatamente. Custa quase nada e parece
  caríssimo.
- **Prensa:** intercale as pranchas com papel siliconado ou glassine
  durante toda a prensagem.

### Ordem de montagem para painel impresso em caixa

> **A impressão entra por último.** Monte a caixa, revista com o material
> de base, deixe secar e estabilizar 1–2 dias. **Só então** aplique o
> painel como *onlay*, com adesivo seco. Assim a impressão nunca está
> presente durante nenhuma fase úmida da construção.

**Trate a borda de corte.** Se aparar laminado + papel juntos, sobra uma
borda de papel nua — exatamente por onde a umidade ambiente entra e onde o
corante desbota/sangra primeiro. Escolha uma:

- **Encapsular:** deixe 4–5 mm de laminado sobrando em volta e sele os
  dois lados. Borda de papel zero exposta.
- **Aparar rente e selar o fio** com filete finíssimo de médium acrílico
  ou cera microcristalina.
- **Emoldurar / embutir** num rebaixo. Esteticamente melhor e protege
  mecanicamente. Cantos de painel colado são pontos de início de
  descolamento por atrito.

**Duas notas de oficina:** passe a dobradeira sempre sobre papel
siliconado, nunca direto no impresso; e deixe o painel colado sob prensa
com papel siliconado por cima, porque **verniz mal curado gruda em tudo**.

*(Construção das caixas, folgas e cartão: cap. 19.)*

### O melhor uso da impressora: o interior da caixa

O forro interno de uma clamshell nunca vê luz nem sofre atrito — é onde o
corante dura décadas. Está no **cap. 19**.

### Estratégia para cor no miolo

O ponto fraco real do conjunto. Três saídas, em ordem de qualidade:

1. **Tip-in:** mande imprimir as pranchas separadamente em gráfica com
   laser ou pigmento integral, e cole-as manualmente. É exatamente como as
   edições finas históricas faziam — fica mais bonito e mais autêntico que
   prancha impressa no mesmo papel do miolo.
2. **Monocromia elegante:** gravuras em preto puro, ou duotone com o preto
   pigmentado + um segundo elemento aplicado à mão (aquarela, estêncil
   cortado na Cameo, *hot foil*). **Isso vira estética de marca, não
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

## Protocolos de teste

### Para escolher adesivo/laminação de um painel

Quinze minutos de preparo — e três semanas de observação, que valem cada
dia. Imprima 2 folhas extras iguais. Lamine junto com a boa. Corte em tiras de
3 × 8 cm e teste cada candidato:

1. Cole cada tira num pedaço do **mesmo cartão/substrato** da caixa
2. Prense 24 h sob peso
3. Avalie a **24 h, 1 semana e 3 semanas**: sangramento (procure halo nos
   magentas e cianos — são os mais fugitivos), manchamento, mudança de
   brilho, bolhas, empenamento
4. Teste o **cisalhamento**: tente descolar com a unha pela borda

**Uma tira fica sem colar nenhum, guardada no escuro, como referência.**

### Para escolher papel e verniz

Imprima o mesmo alvo — foto com pele, céu, preto chapado e texto pequeno —
em glossy, fosco 200 g e acetinado. Depois:

| Teste | Como | O que procurar |
|---|---|---|
| Água sem verniz | Gota, 60 s, secar | Linha de base do estrago |
| Água com verniz | 3 demãos, cura 72 h, gota 5 min | Sangramento, halo, inchaço |
| Atrito úmido | Dedo úmido, 10 esfregões | Transferência de cor |
| **Cola PVA** | Pincelada sobre a área impressa, vernizada | Sangramento, enrugamento |
| **Bloqueio** | Duas amostras face a face, sob prensa, 48 h | Adesão / arranque de superfície |
| Empeno | 24 h em ambiente normal | Curvatura (o glossy perde aqui) |
| **Amarelecimento** | Metade coberta, janela, 30 dias | Verniz barato amarela primeiro |

**O teste dos 30 dias vale começar hoje** — é o que define a marca de
verniz definitiva da casa.

---

## E a solução que apaga o problema pela raiz

**Imprima o painel em laser/toner numa gráfica rápida.** Toner é plástico
fundido: impermeável de nascença, sem umidade de tinta, dimensionalmente
estável, lamina a quente sem drama, e aceita cola aquosa sem piscar. Custa
alguns reais por folha.

Se a fidelidade de cor servir, isso elimina a cadeia inteira de problemas:
sensibilidade do corante, umidade na laminação, restrição de adesivo — e
o desbotamento do corante sob luz ambiente ao longo de anos.

> **Vale considerar sobretudo porque corante desbota.** Um slipcase fica
> anos numa estante recebendo luz ambiente; verniz com UV e BOPP ajudam,
> mas **nada salva corante de anos de luz difusa**. Toner ou tinta
> pigmentada é o único conserto de verdade nesse ponto.

**Se a peça é para valer, gaste os R$ 5 do teste em laser antes de
decidir.**
