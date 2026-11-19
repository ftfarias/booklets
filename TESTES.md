# Caderno de testes

Registro de experimentos com materiais e processos. A ideia é que cada
volume produzido deixe conhecimento utilizável no próximo — e que
comparações sejam honestas, com uma variável de cada vez.

**Regra:** ao comparar, fixe tudo menos o que está sendo testado. Mesmo
PDF, mesma impressora, mesmas configurações de driver, mesma linha, mesmo
couro. Anote as configurações **na hora** — três meses depois ninguém
lembra em que densidade imprimiu.

---

## Vulgata — Pólen vs. Munken

**Objetivo:** decidir o papel padrão para os próximos volumes, com os dois
objetos na mão.

**Constantes:** `Vulgata/vulgata.pdf` (42 pp, A4 paisagem, duplex),
Epson L4360, costura japonesa 4 furos, linha preta encerada, couro escuro
com vinil dourado.

**Variável:** o papel do miolo.

### Exemplar A — Pólen Bold 90 g/m²

- origem:
- preço (resma / folha):
- driver: qualidade ____ · densidade ____ · tipo de papel ____
- secagem: borra ao passar o dedo depois de 1 min?
- transparência (verso contra a luz): nenhuma / leve / incômoda
- espessura real do bloco (21 folhas): ____ mm
- tato:
- como envelheceu depois de 1 mês:

### Exemplar B — Munken Print Cream 80 g/m²

- origem:
- preço:
- driver: qualidade ____ · densidade ____ · tipo de papel ____
- secagem:
- transparência:
- espessura real do bloco: ____ mm
- tato:
- como envelheceu depois de 1 mês:

### Veredito

- papel escolhido:
- por quê:
- o que faria diferente:

---

## Devocionário — cinco papéis de miolo

**Objetivo:** escolher o miolo do livro de orações da Doristela (prazo
~18/out/2026) e, de quebra, ter os cinco papéis da casa comparados lado a
lado pela primeira vez.

**Constantes:** `Devocionario/teste_papel.pdf` (`make teste-papel`):
**uma** folha A4, frente e verso, tirada da imposição real — no verso a
página dupla 24|25 (latim | português, preto + rubricas vermelhas).
Epson L4360, duplex borda longa, tamanho real, **mesmas configurações de
driver em todas** (anotar abaixo uma vez só). Dobrar ao meio depois de
seca.

**Variável:** o papel.

**Antes de imprimir — sentido da fibra.** A folha A4 vira caderno A5
dobrada ao meio: a dobra corre paralela ao lado de **210 mm**, e a fibra
tem que correr junto com ela (`manual/capitulos/01-papel.md`). Resma A4 de
escritório costuma vir com a fibra no lado de 297 — **errada para este
livro**. Teste de flexão em cada papel: curvar a folha nos dois sentidos;
o sentido que cede mais fácil é o da fibra. Papel com fibra errada dobra
com aresta quebrada, ondula com a cola e o livro não fecha plano.

Driver: qualidade ____ · tipo de papel ____ · densidade ____

| | Pólen Bold 90 | Eco Millennium 90 | Opalina 120 | Opalina 180 | Sulfite 75 |
|---|---|---|---|---|---|
| fibra paralela ao lado de 210? | | | | | |
| vermelho: cor / nitidez | | | | | |
| borra ao dedo após 1 min? | | | | | |
| transparência (verso contra a luz) | | | | | |
| dobra: aresta limpa ou racha? | | | | | |
| caimento da página aberta | | | | | |
| espessura de 4 folhas dobradas (1 caderno) | | | | | |

Expectativas, para confirmar ou desmentir (não decidir no papel):
- **Opalina 180** é gramatura de guarda, não de miolo: num caderno de 4
  folhas deve ficar dura, rachar na dobra e a página não deita. Candidata
  forte a **folha de guarda** deste mesmo livro.
- **Opalina 120** é colada e calandrada: tinta fica por cima — conferir
  secagem e se o vermelho ganha nitidez ou borra.
- **Sulfite 75** é o controle: pior opacidade, branco-azulado. Serve de
  régua para os outros.

### Resultados (11/out, Felipe)

- **Fibra (tiras molhadas):** Pólen Bold e Opalina com fibra **paralela
  ao lado longo** — errada para A4→A5. Eco Millennium: as duas tiras
  dobraram igual (fibra pouco orientada, típico de reciclado).
- **Pólen:** bom resultado, mas **vaza luz** — dá para ver o texto do verso.
- **Opalina 120:** preferida no visual (branco, nítido, vermelho vivo);
  receio de ficar grosso demais.
- **Decisão de formato:** o livro passou para **A6 em quarto**
  (`quarto.py`): a lombada corre com a fibra nos três papéis. 128 pp =
  8 cadernos = 16 folhas A4.

Espessura medida (paquímetro, folhas empilhadas):

| papel | amostra | por folha | miolo de 64 folhas (sem costura) |
|---|---|---|---|
| Opalina 120 | 30 folhas = 4,2 mm | **0,14 mm** | ~9,0 mm |
| Opalina 180 | 50 folhas = 9,5 mm | **0,19 mm** | ~12,2 mm |
| Pólen Bold 90 | — (CLAUDE.md: 0,13–0,14) | ~0,135 mm | ~8,6 mm |

→ **Opalina 120 tem praticamente a espessura do Pólen Bold 90**: o
"bold" do Pólen é justamente ser encorpado para a gramatura. A espessura
não pesa contra a Opalina; o que decide é caimento, transparência e
secagem. Opalina 180 fica para **guarda**.

### Veredito (11/out)

- miolo: **Opalina 120**, A6 em quarto — dobrada em quarto, a página
  caiu bem.
- guarda: **Opalina 180** (meia A4 dobrada no lado de 210 → fibra certa).
- por quê: mesma espessura do Pólen (0,14 mm), sem o vazamento do verso,
  branco e vermelho mais nítidos. Fibra resolvida pelo formato, não pelo
  papel.

---

## Testes pendentes

Coisas que valem experimentar em sobra antes de comprometer material:

- [ ] **Couro + EasyPress Mini no preset baixo.** Marca? Cria brilho?
      Testar com pano grosso e passadas de 5–8 s. Ver `cover/GUIA_VINIL.md`.
- [ ] **Adesão do vinil no couro específico.** Couro encerado ou com
      acabamento sintético pode não pegar de jeito nenhum.
- [ ] **Descascagem real do vinil.** As medidas dizem que 1,2 mm passa,
      mas o vinil concreto pode se comportar diferente. Cortar um pedaço
      com o texto menor (`MMXXVI`) e descascar antes da peça inteira.
- [ ] **Broca de 1,5 mm no bloco completo**, com couro incluso. Sai
      perpendicular? O couro esgarça?
- [ ] **Escurecer o corte a seco** (grafite, bloco prensado) numa pilha de
      sobras — ver se o resultado agrada antes de decidir.
- [ ] **Cera microcristalina sobre o vinil**, em sobra: confirmar que não
      marca o dourado.

---

## Técnicas a explorar

### Cianotipia

Processo fotográfico de 1842 (Herschel). Sensibiliza-se o **próprio papel
ou tecido** com sais de ferro, expõe-se ao sol sob um negativo ou máscara,
lava-se em água. Dá azul da Prússia, permanente e muito estável.

Por que interessa aqui: a imagem **é** o material, não uma camada colada
por cima — diferente do vinil. E é química com variáveis controláveis,
que responde bem a teste sistemático.

Variáveis a controlar (uma por vez):

- proporção dos sais (citrato férrico amoniacal : ferricianeto de potássio)
- papel — gramatura, colagem, textura; papel muito colado não absorve
- tempo de exposição × índice UV (varia com hora e estação)
- lavagem: tempo e acidez da água afetam o tom final
- secagem e "cura" — o azul escurece nas primeiras 24 h

**Tensão de estilo a resolver antes de usar:** cianotipia é orgânica
(bordas que sangram, textura de pincel, variação de tom); o vocabulário
Legrain/Adler é geometria dura e aresta seca. Três caminhos:

1. usar cada uma na sua linha — Legrain no premium, cianotipia noutra
   família de livros;
2. **disciplinar a cianotipia com máscara rígida**, formas geométricas
   puras, usando o azul como *campo de cor* em vez de imagem — pouco
   explorado e provavelmente o mais promissor aqui;
3. aceitar a mistura como assinatura.

### Marmorizado

Deixado para o fim de 2026, e com razão: é o menos repetível dos três.
Depende de tinta, goma (carragena), mordente (alúmen) no papel e
temperatura. Muito material desperdiçado no aprendizado.

Mesma tensão: marmorizado é barroco por natureza. **Nas guardas** de um
livro severo funciona por contraste — capa contida, guarda exuberante, um
efeito clássico da encadernação francesa. **Na capa** brigaria com tudo.

---

## Agendas personalizadas 2027

**Encomenda real, com prazo.** Agendas para diretores e clientes
importantes, entrega antes de janeiro de 2027. Conversa iniciada em
setembro de 2026 — restam ~4 meses úteis.

**Isto é trabalho COMERCIAL, não artístico.** Qualidade de execução
sempre, mas o vocabulário Legrain/Adler **não se aplica** — a estética é
do cliente. Se houver espaço, cabe algo mais autoral; se não, vai o logo
da empresa e pronto. Não confundir com as duas linhas do `CLAUDE.md`.

**Isto não é um livro artístico com outra capa.** É produção: N objetos
idênticos com variação controlada (nome de cada pessoa). O que passa a
importar é repetibilidade, tempo por unidade, taxa de refugo e
previsibilidade de material. E o prazo é absoluto — agenda entregue em
janeiro não vale nada.

**Escopo: miolo comprado pronto de gráfica.** Isso elimina de uma vez a
impressão de ~200 páginas por unidade, o consumo de tinta da L4360 e a
geração do calendário de 2027 com feriados. **Sobram encadernação e
customização** — que é exatamente onde está o valor do trabalho.

**O nicho:** quem quer **10 agendas boas**, não 100 iguais. A gráfica não
atende esse cliente por causa do mínimo; a encadernação artesanal atende.
Posição defensável.

### A perguntar à gráfica ANTES de falar em quantidade

- [ ] **O miolo vem em cadernos costurados/dobrados soltos, ou colado
      (*hot melt*)?** **Esta é a pergunta que decide tudo.** Se vier
      colado, não dá para costurar e a agenda **não abre plana** — que é
      requisito. Em cadernos, costura-se e fica bom.
- [ ] já vem refilado no formato final?
- [ ] qual o mínimo deles para o miolo (pode ser 100 também)
- [ ] formato e gramatura disponíveis

### Diferenças estruturais a resolver

- **Precisa abrir plana** para escrever. **A costura japonesa não abre
  plana** — exige costura em cadernos com lombada flexível, método ainda
  não praticado. Depende da resposta da gráfica acima.
- **Durabilidade**: um ano de uso diário, não uma leitura ocasional.

### Estrutura provável: meio-couro ("lombacanto")

Couro na lombada e nos cantos, campo central em tecido ou papel. Não é
economia — é a escolha tecnicamente correta:

- **É onde o desgaste acontece.** Lombada e cantos são os pontos que
  sofrem numa agenda de uso diário. Por isso a encadernação histórica faz
  assim.
- **Resolve a repetibilidade.** Menos couro por unidade significa tirar
  todas as peças da mesma pele — cor e textura uniformes entre as 10.
  Com couro inteiro, peles diferentes dariam agendas visivelmente
  diferentes.
- **O campo central é flexível.** Cabe logo da empresa, cor lisa, ou —
  se o cliente quiser e houver espaço — algo mais autoral. A decisão é
  dele, não sua.

### Perguntas a responder com o cliente

- [ ] quantas unidades?
- [ ] prazo real de entrega
- [ ] o que é "personalizado" — só o nome? cor? conteúdo?
- [ ] orçamento por unidade

### Protótipo

**Uma agenda completa, cronometrada**, antes de dizer sim a qualquer
quantidade ou preço. Com o miolo comprado, mede-se só o que é seu:

- horas por unidade, por etapa (preparo do couro / costura ou montagem /
  capa / customização)
- custo de material por unidade (miolo + couro + tecido + acabamento)
- taxa de erro — quantas tentativas até uma sair boa

Se der 12 h por unidade, 30 agendas são 360 h em quatro meses — inviável
com trabalho em tempo integral. Se der 4 h, muda tudo. **É esse número
que decide a quantidade, não a vontade.**

**Status: ainda um "talvez" remoto.** Felipe vai conversar com o amigo
para definir o que é viável este ano. Nada a construir até lá.

---

## Registro de fornecedores

| material | onde | preço | obs |
|---|---|---|---|
| Pólen Bold 90 g | | | Mercado Livre tem vários vendedores |
| Munken Print Cream | | | Ipsis (gráfica) usa; ver se vende ou imprime |
| couro | | | |
| vinil HTV dourado | | | |
| linha encerada preta | | | |
| cera microcristalina | | | Renaissance Wax ou equivalente |
