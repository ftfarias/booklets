# Guia de montagem — Capa marchetada "Acrópole"

**Projeto:** Platão, *Três Diálogos Socráticos* — capa A5 em couro, marchetaria de 3 faixas + HTV preto
**Encadernação:** saddle stitch (grampo canoa)

---

## 1. Materiais

| Item | Especificação |
|---|---|
| Couro verde-acinzentado | faixa de 151 × 72 mm (céu) |
| Couro ocre | faixa de 151 × 72 mm (templos) |
| Couro marrom | faixa de 151 × 72 mm (rocha) |
| HTV preto | colunas + título |
| Cartonagem | 151 × 216 mm (capa) + lombada |
| Cola | PVA / cola de encadernação |

**Miolo:** A5, 100 páginas → capa acabada de **151 × 216 mm**
(148 × 210 do miolo + 3 mm de goteira + 3 mm cabeça/pé)

---

## 2. Arquivos

Todos em `cut_files/`, todos no tamanho real da capa (151 × 216 mm).
Como cada arquivo tem a capa inteira, **a peça já sai na posição certa** — é só alinhar pelas bordas.

### Para cortar em COURO
| Arquivo | Peça | Cor |
|---|---|---|
| `trace_1_green_sky.png` | faixa superior — céu | verde |
| `trace_2_ochre_temple.png` | faixa do meio — templos | ocre |
| `trace_3_brown_rock.png` | faixa inferior — rocha | marrom |

### Para cortar em HTV PRETO
| Arquivo | Peça |
|---|---|
| `trace_4_black_columns.png` | 17 colunas (menor: 2,4 mm) |
| `trace_5_black_title.png` | PLATO + ΕΥΘΥΦΡΩΝ · ΑΠΟΛΟΓΙΑ · ΚΡΙΤΩΝ |

> Também há `fixed_*.svg` (vetores corrigidos) caso o Inkscape funcione.
> O título vetorial está em `fixed_5_black_title.pdf`.

---

## 3. Importar no Silhouette Studio

1. **Arquivo → Abrir** → escolha o PNG
2. Confira o tamanho: deve entrar como **151 × 216 mm**.
   Se entrar errado, defina largura = 151 mm com proporção travada.
3. **Painel Traçar** (Trace):
   - *Selecionar área de traçado* sobre a imagem toda
   - Ajuste o **Limiar (Threshold)** até a peça ficar amarela por inteiro
   - **Traçar** (Trace) — não use "Traçar e destacar"
4. Apague a imagem de fundo, ficando só a linha de corte.

---

## 4. Cortar

### Couro (faixas)
- Lâmina **rotativa** ou **kraft**
- Base de corte forte (azul/roxa)
- Faça um **teste numa sobra** antes — couro varia muito de espessura
- Corte com o lado do avesso (carnal) para cima, se possível

### HTV preto (colunas e título)
- ⚠️ **ESPELHE horizontalmente antes de cortar** (Object → Mirror → Flip Horizontally)
  Sem isso o PLATO sai invertido.
- Vinil com o **lado brilhante (transportador) para BAIXO**
- Material: *Heat Transfer, Smooth*
- **Weeding:** remova o excesso. As colunas são finas — vá com calma.

---

## 5. Montagem

### Etapa A — as três faixas
1. Cole a faixa **verde** no alto da cartonagem
2. Cole a **ocre** encaixando a silhueta dos templos contra o verde
3. Cole a **marrom** encaixando a linha da rocha contra o ocre

> As costuras foram geradas da **mesma linha vetorial**, então encaixam sem folga.
> Cole faixa por faixa, deixando secar, para não deslocar o encaixe.

### Etapa B — HTV preto
4. **Colunas** primeiro: posicione sobre os templos ocre
5. **Título** depois: alinhe a folha pelas bordas da capa — a posição já está correta
6. Prensa: **~130 °C, pressão média, 10–15 s**
   - Use papel manteiga ou teflon entre o ferro e o vinil
   - ⚠️ **TESTE numa sobra de couro primeiro** — couro sintético varia; calor demais marca

### Etapa C — fechamento
7. Monte a capa com o miolo, grampeie no vinco (saddle stitch)

---

## 6. Sobre a margem de virada

Os arquivos **não incluem margem de virada** (turn-in).

Se você vai virar o couro por cima da cartonagem, acrescente **~15 mm nas bordas externas**
(topo do verde, base do marrom, e as laterais das três faixas).

❗ **Nunca acrescente margem nas costuras internas** (skyline e linha da rocha) —
elas precisam bater exatamente, senão o encaixe abre.

---

## 7. Ordem recomendada de trabalho

```
1. Teste de corte no couro (sobra)      ← não pule
2. Teste de prensa do HTV (sobra)       ← não pule
3. Cortar as 3 faixas de couro
4. Colar as faixas na cartonagem
5. Cortar HTV (espelhado!) e fazer weeding
6. Prensar colunas, depois título
7. Montar e grampear
```
