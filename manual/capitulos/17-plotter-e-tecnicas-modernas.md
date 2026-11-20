# Plotter de corte e técnicas modernas

> **A regra que resolve quase tudo:** a máquina não substitui a mão — ela
> entrega **repetibilidade e precisão de canto**, que é exatamente o que a
> mão não dá. Use-a onde a uniformidade importa, não onde o gesto importa.

A literatura clássica de encadernação não cobre quase nada disto, e é a
rota que mais muda o que um encadernador sozinho consegue fazer hoje. Este
capítulo registra prática, não teoria: vem das peças do estúdio em 2026,
feitas com uma **Silhouette Cameo** e uma **Cricut EasyPress Mini**, e das
conversas de pesquisa. É também o capítulo que mais envelhece —
equipamento e material mudam depressa.

---

## Consulta rápida — o que a plotter faz bem

| Tarefa | Vale? | Por quê |
|---|---|---|
| **Vinil termoadesivo na capa** | ✅ | Título e geometria sem prensa de *hot stamping* |
| **Print & cut** de painéis | ✅ | Sangria + corte na linha, cantos idênticos |
| ***Onlay* de couro fino** | ✅ | Peças iguais, que a mão não repete |
| **Estênceis e máscaras** | ✅ | Cor sem impressora, sem limite de formato |
| **Gabaritos de construção** | ✅ | Caixas e furação repetíveis |
| **Protótipo em cartão fino** | ✅ | Antes de gastar cartão bom |
| Cortar cartão de 2–3 mm | ❌ | Força de corte insuficiente; à mão é mais rápido |
| Couro acima de ~2 mm | ❌ | A lâmina não vence |

### Materiais e lâminas

| Material | Lâmina | Observação |
|---|---|---|
| Vinil termoadesivo (HTV) | padrão | **Espelhar o arquivo** |
| Papel até 200 g | padrão | |
| Cartolina, cartão fino | *deep cut* | Até ~0,5 mm |
| Couro fino, até 1,5–2 mm | rotativa ou kraft | Vários passes; papel colado no grão (ver *onlay*) |
| Tecido | rotativa | Com suporte ou estabilizador |

---

## Vinil termoadesivo na capa

A rota que o estúdio usa: vinil dourado sobre couro escuro. É a
alternativa realista ao *hot stamping* enquanto não há prensa (cap. 16).

### As restrições de produção

Não são preferências estéticas — são limites físicos do processo, e cada
uma custou uma peça para ser descoberta:

**Fonte com serifa não serve.** Serifas finas e o contraste entre traço
grosso e fino arrancam junto com o refugo na hora de descascar. Use
**Futura** ou outra geométrica de espessura uniforme. (Cockerell, em 1901,
já achava as letras dos encadernadores estreitas e com contraste demais —
cap. 16.)

> Isso não contamina o miolo: o livro continua em Libertinus. São peças
> diferentes, com processos diferentes.

**Piso de 1,2 mm para qualquer traço.** A aparência na tela não diz nada —
um rascunho que parecia resolvido tinha traços de 0,5 mm, que não
sobrevivem ao descasque.

**Meça, não confie no olho.** Rasterize o arquivo a 600 dpi e meça a
largura real dos traços (um script curto em Python faz isso). Use o
**percentil 10** das larguras, não o mínimo — o mínimo pega o
antialiasing das curvas e dá falso alarme.

**Descascar achata a hierarquia.** Quando tudo precisa ter 1,2 mm, o
contraste entre título e subtítulo desaparece e o conjunto vira uma lista
cinza. A correção é **remover elementos, não diminuí-los** — diminuir
devolve o traço para baixo do piso e você volta ao problema original.

**Espelhe o arquivo.** HTV corta-se pelo verso. A conferência é simples: o
título tem que estar **ilegível** na tela antes de mandar cortar.

### Do Typst para a plotter

```bash
typst compile --format svg capa.typ capa.svg
```

O SVG do Typst exporta **contornos reais**, não elementos de texto — então
o Silhouette Studio não precisa da fonte instalada, e não há risco de
substituição de fonte no caminho.

### Transferência

| Passo | Detalhe |
|---|---|
| Temperatura do couro | **110–120 °C** |
| EasyPress Mini | Três posições, que a Cricut dá como faixas: baixa ~125–145 °C, média ~150–180 °C, alta ~185–205 °C — **todas acima** |
| Compensação | Pano de proteção grosso + passadas curtas de 5–8 s |
| Descolagem | **A frio** |
| Teste | Sempre numa sobra do mesmo couro |

> **Não mude a posição para compensar** — a EasyPress Mini não tem ajuste
> fino. Compense com o pano e com o tempo de contato.

### A ordem com a cera

Este é o erro que estraga a peça pronta:

> **Cera microcristalina só depois da transferência.** A cera deixa uma
> película hidrofóbica, e couro encerado é exatamente o caso em que o
> adesivo não pega.

**Ordem correta:** couro limpo → transfere → 24 h → encera.

---

## Print & cut

Imprimir com sangria e deixar a máquina cortar exatamente na linha, usando
marcas de registro impressas.

**Onde brilha:**

- **Painéis de caixa** (cap. 19) — cantos idênticos, impossível à mão.
- Etiquetas de lombada.
- Rótulos, certificados, ex-líbris.
- Guardas com recorte.

**Cuidados:**

1. As marcas de registro precisam de margem branca; respeite o gabarito
   do software.
2. Papel brilhante confunde o sensor óptico. Fosco funciona melhor.
3. **Se o painel for impresso a corante, lamine ou envernize antes de
   cortar** — a lâmina e o manuseio marcam a superfície crua (cap. 16).

---

## *Onlay* de couro fino

O *onlay* é couro de outra cor, muito fino, colado sobre o couro da capa
— um mosaico. Roberts & Etherington o dão como certamente em uso na
Inglaterra no século XVII; a encadernação Art Déco o levou ao limite, em geometria seca
e peças pequenas.

**O que a plotter substitui.** Cockerell descreve o método de 1901: o
couro rebaixado muito fino; as peças **estampadas com punções de aço**
cortados no formato dos ferros — ou, se forem poucas, o ferro impresso no
couro fino e a peça recortada à faca; as bordas chanfradas; a peça colada
com engrudo e apertada na prensa; depois, o ouro por cima. A plotter faz o
papel dos punções: um arquivo, vinte peças iguais.

1. **Rebaixe** o couro a 0,4–0,6 mm antes de cortar (cap. 14).
2. **Cole um papel no grão** e deixe secar. É o truque de Cockerell para
   peça grande: o couro fino estica quando recebe o engrudo, e o papel
   impede. Na plotter, o papel deve também dar ao couro a firmeza que lhe
   falta no tapete — *a testar*.
3. **Corte** com lâmina rotativa ou kraft, **vários passes** de pressão
   média em vez de um passe forte. Fixe o couro com fita de baixa aderência
   nas bordas: ele desliza.
4. **Chanfre** a borda das peças maiores.
5. **Cole com engrudo** e aperte de leve na prensa. Seco o engrudo,
   umedeça o papel e tire-o.
6. **Teste numa sobra:** cada lote de couro responde diferente.

**Para o branco, papel japonês, não couro.** Couro branco rebaixado
deixa ver a cor de baixo e parece sujo. Se for dourar por cima, encole o
papel antes (Cockerell).

A laser também corta *onlay* — mas nunca couro cromado (ver adiante).

---

## Estênceis e máscaras

Cortar vinil adesivo comum (não o termoadesivo) como máscara para pintar.

**Por que vale:** cor sem passar pela impressora, **sem limite de formato**
e sem nenhum dos problemas de tinta aquosa dos caps. 6 e 16. Um estêncil
A3 pinta uma folha de guarda inteira.

Aplicações: papel de guarda padronizado, aerografia sobre tecido ou couro,
fundo para douração, repetição de um motivo numa tiragem.

Combina bem com as técnicas do cap. 18 — um estêncil sobre *paste paper*
dá um resultado que não parece nem impresso nem totalmente manual.

---

## Gabaritos: o uso mais subestimado

A plotter não precisa cortar o material final para ser útil. Cortar
**gabaritos** resolve o problema de repetibilidade:

- **Furação de costura** — gabarito com os furos na posição exata, para
  todos os cadernos saírem iguais.
- **Construção de caixa** — moldes de bandeja, parede e painel.
- **Posicionamento de etiqueta** — máscara que marca onde colar.
- **Marcação dos nervos** — as divisões da lombada (cap. 8) num gabarito,
  sem medir de novo a cada livro.

É o que faz a peça 1 e a peça 40 de uma tiragem saírem iguais, e custa uma
folha de cartolina.

---

## Protótipo antes do cartão bom

Para caixas e estruturas novas: corte o protótipo em cartão fino, monte,
encaixe o livro real, corrija as medidas, **depois** corte o cartão de
2 mm à mão.

Cartão fino custa centavos. Uma caixa de bandejas mal medida custa uma
tarde.

---

## Outras rotas modernas

### Laser CO₂

Grava couro vegetal e madeira, corta cartão e papel.

| | |
|---|---|
| ✅ | Gravação de profundidade controlável; detalhe altíssimo |
| ✅ | Corta cartão de caixa, que a plotter não vence |
| ❌ | **Nunca couro cromado:** queimado, o cromo do curtimento forma cromo hexavalente, cancerígeno (cap. 14) |
| ❌ | **Nunca corino:** PVC queimado libera cloro, que corrói a máquina e faz mal (cap. 13) |
| ❌ | Marca de queimado nas bordas; em papel claro, aparece |

Faixa de 40–60 W resolve encadernação. É investimento grande: só depois
de a plotter ficar pequena.

### Impressão UV direta

Imprime em relevo sobre quase qualquer superfície, inclusive couro. Existe
em gráficas de brinde corporativo.

Vale conhecer, mas **destoa de encadernação fina**: a tinta fica por cima,
com aspecto plástico, e não tem nada do brilho de metal brunido.

### Foil digital

O meio-termo entre foil e clichê: o foil é aplicado sobre um **toner
previamente impresso**, sem precisar de matriz. Bom para tiragem pequena
com desenho variável. Em gráfica, é máquina própria; em casa, há a versão
com laminadora e foil reativo a toner, sobre impressão laser.

### Clichê a partir de arquivo

A ponte entre o digital e o *hot stamping* do cap. 16: você desenha, a
clicheria grava em magnésio ou latão, e você estampa — com foil ou com
ouro genuíno.

---

## Quando cada rota compensa

| Situação | Rota |
|---|---|
| Peça única, geometria simples | Vinil recortado |
| Peça única, trabalho fino | Ouro a ferro, à mão (cap. 15) |
| Edição de 5–15 | Vinil, ou foil com vinco |
| Edição de 15+ idênticas | Clichê em prensa (cap. 16) |
| Mosaico de couro | *Onlay* cortado a plotter |
| Cor em formato grande | Estêncil + pintura |
| Caixa repetível | Gabaritos a plotter |

---

## Armadilhas

| Problema | Causa | Prevenção |
|---|---|---|
| **Traço arrancou no descasque** | Abaixo de 1,2 mm, ou fonte com serifa | Medir a 600 dpi; geométrica |
| **Título espelhado na capa** | Esqueceu de espelhar o HTV | Conferir: tem que estar ilegível na tela |
| **Adesivo não pegou** | Couro já encerado | Cera só 24 h **depois** |
| **Couro queimado na transferência** | Calor acima de ~120 °C | Pano grosso, passadas curtas |
| **Fonte trocada no Silhouette** | Exportou texto em vez de contorno | `typst compile --format svg` |
| **Hierarquia achatada** | Tudo no piso de 1,2 mm | Remover elementos, não diminuir |
| **Couro deslizou no corte** | Sem fixação | Fita de baixa aderência nas bordas |
| **Sensor não leu as marcas** | Papel brilhante | Usar fosco |

---

## Fontes

- **Prática do estúdio, 2026** — Silhouette Cameo, vinil termoadesivo,
  Cricut EasyPress Mini: os pisos de traço, a medição a 600 dpi, a
  compensação de temperatura, a ordem da cera. Resultado de peças reais.
- **Cricut** — as faixas de temperatura das três posições da EasyPress
  Mini.
- **Douglas Cockerell,** *Bookbinding, and the Care of Books* (1901),
  "Inlaying on leather" — o método do *onlay*: couro muito fino, punções,
  papel colado no grão, papel japonês para o branco.
- **Roberts & Etherington,** *Bookbinding and the Conservation of Books*
  (1982), verbete ONLAY.
- **Conversas de pesquisa** — laser, impressão UV, foil digital, lâminas
  e materiais.

Observações de 2026. Ao reler, anote ao lado o que mudou e quando.
