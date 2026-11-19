# Plotter de corte e técnicas modernas

> **A regra que resolve quase tudo:** a máquina não substitui a mão — ela
> entrega **repetibilidade e precisão de canto**, que é exatamente o que a
> mão não dá. Use-a onde a uniformidade importa, não onde o gesto importa.

A literatura clássica de encadernação não cobre nada disto, e é a rota que
mais muda o que um encadernador sozinho consegue fazer hoje. Este capítulo
registra prática, não teoria: boa parte vem de erros já cometidos neste
projeto.

---

## Consulta rápida — o que a plotter faz bem

| Tarefa | Vale? | Por quê |
|---|---|---|
| **Vinil termoadesivo na capa** | ✅ | Título e geometria sem prensa de hot stamping |
| **Print & cut** de painéis | ✅ | Sangria + corte na linha, cantos idênticos |
| ***Onlay* de couro fino** | ✅ | Mosaico preciso que a mão não repete |
| **Estênceis e máscaras** | ✅ | Cor sem impressora, sem limite de formato |
| **Gabaritos de construção** | ✅ | Caixas e furação repetíveis |
| **Protótipo em cartão fino** | ✅ | Antes de gastar cartão bom |
| Cortar cartão de 2–3 mm | ❌ | Não force; não tem torque |
| Couro acima de ~2 mm | ❌ | Lâmina não vence |

### Materiais e lâminas

| Material | Lâmina | Observação |
|---|---|---|
| Vinil termoadesivo (HTV) | padrão | **Espelhar o arquivo** |
| Papel até 200 g | padrão | |
| Cartolina, cartão fino | *deep cut* | Até ~0,5 mm |
| Couro fino até 1,5–2 mm | rotativa / kraft | Passes múltiplos |
| Tecido | rotativa | Com suporte, ou estabilizador |

---

## Vinil termoadesivo na capa

A rota que este projeto usa: vinil dourado sobre couro escuro. É a
alternativa realista ao hot stamping enquanto a prensa não vem.

### As restrições de produção

Estas não são preferências estéticas — são limites físicos do processo, e
cada uma custou uma peça para ser descoberta:

**Fonte com serifa não serve.** Serifas finas e o contraste entre traço
grosso e fino arrancam junto com o refugo na hora de descascar. Use
**Futura** ou outra geométrica de espessura uniforme.

> Isso não contamina o miolo: o livro continua em Libertinus. São peças
> diferentes, com processos diferentes.

**Piso de 1,2 mm para qualquer traço.** A aparência na tela não diz nada —
um rascunho que parecia resolvido tinha traços de 0,5 mm, que não
sobrevivem ao descasque.

**Meça, não confie no olho.** O script `cover/check_vinyl.py` da Vulgata
rasteriza o arquivo a 600 dpi e mede a geometria real. Use o **percentil
10** das larguras, não o mínimo — o mínimo pega o antialiasing das curvas
e dá falso alarme.

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
| EasyPress Mini | presets de ~130/155/205 °C — **todos acima** |
| Compensação | pano de proteção grosso + passadas curtas de 5–8 s |
| Descolagem | **a frio** |
| Teste | sempre numa sobra do mesmo couro |

> **Não mude o preset para compensar** — a EasyPress Mini não tem ajuste
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
   cortar** — a lâmina e o manuseio marcam a superfície crua (cap. 6).

---

## Onlay de couro fino

O mosaico de couro colorido — a técnica da encadernação Art Déco — exige
peças pequenas cortadas com precisão absoluta. À mão, cada peça é um
exercício de paciência; a plotter corta vinte iguais.

- Couro **rebaixado a 0,4–0,6 mm** antes de cortar (cap. 14).
- Lâmina rotativa ou kraft, **múltiplos passes** com pressão média em vez
  de um passe forte.
- Fixe o couro no tapete com fita de baixa tack nas bordas — ele desliza.
- **Teste sempre numa sobra:** cada lote de couro responde diferente.

> ⚠️ **Nunca corte couro cromado a laser.** Queimado, o cromo do
> curtimento forma cromo hexavalente, cancerígeno (cap. 14). A plotter de
> lâmina não tem esse problema, mas o laser tem.

---

## Estênceis e máscaras

Cortar vinil adesivo comum (não o termoadesivo) como máscara para pintar.

**Por que vale:** cor sem passar pela impressora, **sem limite de formato**
e sem nenhum dos problemas de tinta aquosa do cap. 6. Um estêncil A3 pinta
uma folha de guarda inteira.

Aplicações: papel de guarda padronizado, aerografia sobre tecido ou couro,
fundo para douração, repetição de um motivo numa tiragem.

Combina bem com as técnicas do cap. 18 — um estêncil sobre paste paper dá
um resultado que não parece nem impresso nem totalmente manual.

---

## Gabaritos: o uso mais subestimado

A plotter não precisa cortar o material final para ser útil. Cortar
**gabaritos** resolve o problema de repetibilidade:

- **Furação de costura** — gabarito com os furos na posição exata, para
  todos os cadernos saírem iguais.
- **Construção de caixa** — moldes de bandeja, parede e painel.
- **Posicionamento de etiqueta** — máscara que marca onde colar.
- **Marcação de nervuras** — espaçamento crescente (cap. 8) sem recalcular.

É o que faz a peça 1 e a peça 40 de uma tiragem saírem iguais, e custa uma
folha de cartolina.

---

## Protótipo antes do cartão bom

Para caixas e estruturas novas: corte o protótipo em cartão fino, monte,
encaixe o livro real, corrija as medidas, **depois** corte o cartão de
2 mm à mão.

Cartão fino custa centavos. Uma clamshell mal medida custa uma tarde.

---

## Outras rotas modernas

### Laser CO₂

Grava couro vegetal e madeira, corta cartão e papel.

| | |
|---|---|
| ✅ | Gravação de profundidade controlável; detalhe altíssimo |
| ✅ | Corta cartão de caixa, que a plotter não vence |
| ❌ | **Nunca couro cromado** (cromo hexavalente) nem corino (cloro) |
| ❌ | Marca de queimado nas bordas; em papel claro, aparece |

Faixa de 40–60 W resolve encadernação. É investimento de fase 3 (ver
`NEGOCIO.md`).

### Impressão UV direta

Imprime em relevo sobre quase qualquer superfície, inclusive couro. Existe
em gráficas de brinde corporativo.

Vale conhecer, mas **destoa de encadernação fina**: a tinta fica por cima,
com aspecto plástico, e não tem nada do brilho de metal brunido.

### Foil digital

O meio-termo entre foil e clichê: a máquina aplica foil sobre um toner
previamente impresso, sem precisar de matriz. Bom para tiragem pequena com
desenho variável; só existe em gráfica.

### Clichê a partir de arquivo

A ponte entre o digital e o hot stamping do cap. 16: você desenha,
a clicheria grava em magnésio ou latão, e você estampa com ouro genuíno.
**Prensa não obriga a abrir mão do ouro.**

---

## Quando cada rota compensa

| Situação | Rota |
|---|---|
| Peça única, geometria simples | Vinil recortado |
| Peça única, trabalho fino | Ouro a ferro, à mão (cap. 15) |
| Edição de 5–15 | Vinil, ou foil com vinco |
| Edição de 15+ idênticas | Clichê em prensa (cap. 16) |
| Mosaico de couro | Onlay cortado a plotter |
| Cor em formato grande | Estêncil + pintura |
| Caixa repetível | Gabaritos a plotter |

---

## Armadilhas

| Problema | Causa | Prevenção |
|---|---|---|
| **Traço arrancou no descasque** | Abaixo de 1,2 mm, ou fonte com serifa | Medir a 600 dpi; geométrica |
| **Título espelhado na capa** | Esqueceu de espelhar o HTV | Conferir: tem que estar ilegível na tela |
| **Adesivo não pegou** | Couro já encerado | Cera só 24 h **depois** |
| **Couro queimado na transferência** | Preset acima de 120 °C | Pano grosso, passadas curtas |
| **Fonte trocada no Silhouette** | Exportou texto em vez de contorno | `typst --format svg` |
| **Hierarquia achatada** | Tudo no piso de 1,2 mm | Remover elementos, não diminuir |
| **Couro deslizou no corte** | Sem fixação | Fita de baixa tack nas bordas |
| **Sensor não leu as marcas** | Papel brilhante | Usar fosco |

---

## Fontes

Este capítulo vem de prática registrada no `../CLAUDE.md` deste projeto —
os pisos de traço, a ordem da cera, os presets da EasyPress e o script de
verificação são resultado de peças reais. O resto vem das conversas de
pesquisa.

**É o capítulo que mais envelhece:** equipamento e material mudam rápido.
Datar as observações ajuda quem reler daqui a três anos.
