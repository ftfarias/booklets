# The King in Yellow — guia de impressão e encadernação

Volume A5, 96 páginas, **costura em sela** (saddle stitch), 6 cadernos
de 16 páginas.

## Build

```
make            # constrói o PDF, impõe e roda o check
make check      # só verifica o PDF compilado
make preview    # rende páginas de amostra em PNG
```

Dois PDFs saem daqui:

| arquivo | o que é |
|---|---|
| `king_in_yellow.pdf` | miolo em A5, **ordem de leitura** — para ler na tela |
| `king_in_yellow_booklet.pdf` | **imposto**, A4 paisagem 2-up — é este que vai para a impressora |

## Impressão

Papel: **Pólen Bold 90 g/m²**, A4. 24 folhas, frente e verso.

No diálogo de impressão:

- **Tamanho real / 100 %** — NÃO "Ajustar", NÃO "Livreto".
  O `booklet.py` já fez a imposição; deixar o Acrobat impor de novo
  embaralha tudo.
- **Frente e verso: ligado**, **virar na borda curta**.
- Se o verso sair de cabeça para baixo, o driver está virando na borda
  longa — regere com `python3 ../booklet.py king_in_yellow.pdf -o
  king_in_yellow_booklet.pdf -s 16 --long-edge`.

> No Adobe Reader os nomes das bordas vêm invertidos. **Teste uma folha
> antes** de mandar as 24: imprima só as páginas 1–2, dobre ao meio e
> confira se a capa e o verso dela ficam na mesma direção e em ordem.

Antes da tiragem, faça também o teste de papel que o `CLAUDE.md` pede:
uma folha frente e verso, olhando espalhamento da tinta, transparência
contra a luz e borrão ao passar o dedo depois de 1 minuto. A L4360
deposita mais tinta que impressora de cartucho; se borrar, baixe a
densidade no driver.

## Dobra e costura

96 páginas = 24 folhas A4 = **6 cadernos de 4 folhas** cada.

1. Separe as folhas impressas em 6 pilhas de 4, **na ordem em que
   saíram**. O `booklet.py` já concatenou os cadernos em sequência de
   leitura — não embaralhe.
2. Dobre cada folha ao meio, uma a uma, vincando com dobradeira de osso.
3. **Aninhe** as 4 folhas de cada caderno (uma dentro da outra) — não
   empilhe. Cada caderno vira 16 páginas A5.
4. Junte os 6 cadernos em ordem e costure pela dobra.

**Creep:** com 4 folhas aninhadas o deslocamento na borda externa é
pequeno, mas existe — as páginas centrais de cada caderno avançam ~1 mm.
Por isso a margem externa é de 15 mm e a interna de 20 mm. Se for
guilhotinar a frente, ela some no corte.

## Geometria da página

| | |
|---|---|
| formato | A5 retrato, 148 × 210 mm |
| margem interna | 20 mm (lombada) |
| margem externa | 15 mm |
| margem sup./inf. | 18 mm |
| corpo | Libertinus Serif 10,5 pt |
| entrelinha | 0,68 em |
| densidade medida | **417 palavras/página** |

A margem interna **alterna** por paridade (`inside`/`outside`), que é o
correto para códice dobrado. Isso é o oposto da costura japonesa dos
Estoicos e da Vulgata, onde a margem larga fica sempre do mesmo lado.

## O que o `check.py` verifica

Roda sobre o **PDF compilado**, não sobre o fonte:

- 96 páginas, múltiplo de 4, 6 cadernos exatos sem enchimento;
- A5 retrato, todas as páginas do mesmo tamanho, proporção compatível
  com o que o `booklet.py` assume (ele escalaria qualquer outra coisa);
- abertura **e fecho** de cada um dos quatro contos;
- o fragmento da peça, as placas (Hawberk, Mr. Wilde), o manuscrito;
- nota editorial e colofão presentes;
- **ausência** dos seis contos cortados — se algum vazar, reprova;
- nenhuma macro de build (`#sect`, `#play`, `#sign`…) no texto;
- as três fontes Libertinus embutidas — sem a Italic, os itálicos
  silenciosamente não saíram.

O check foi testado quebrando o build de propósito: contagem de páginas
errada, conto cortado, conto excluído vazando. Todos reprovam.

**Uma armadilha que não dá para checar por texto:** um `_x_` solto num
fragmento é *interpretado* pelo Typst como ênfase e nunca chega ao PDF
como sublinhado — não há o que detectar. O perigo real é o que o
`CLAUDE.md` já registra: `*texto*` sai **negrito**, não itálico. Por isso
o check confere as fontes embutidas em vez de caçar o caractere.

---

# Pranchas

Duas ilustrações, impressas **à parte** em papel fotográfico, envernizadas
e coladas à mão. O miolo **não** contém imagem nenhuma — só reserva a
folha, com cantos de registro em cinza claro marcando a área da prancha.

| página | prancha | arquivo |
|---|---|---|
| 3 (recto) | frontispício — *The Pallid Mask* | `imagens/03-mascara-palida.png` |
| 87 (recto) | *Carcosa* | `imagens/04-carcosa-lua-grande.png` |

Área reservada: **96 × 143 mm**, proporção 3:2, a mesma das imagens
geradas. Os cantos de registro ficam 3 mm **fora** dessa área, então
continuam visíveis depois da prancha colada — é por eles que se alinha.

## Resolução disponível

| imagem | pixels | dpi a 96 mm |
|---|---|---|
| Rei de Amarelo (arco) | 3392 × 5056 | **897** |
| Máscara, Carcosa, Sinal | 1696 × 2528 | **449** |

Folga grande nas duas. Imprima em **300 dpi reais**, sem reamostrar
para cima.

## Verniz

Colorfix, testado e aprovado. Duas precauções:

- **Deixe curar 24–48 h antes de encadernar.** O verniz fica seco ao
  toque em minutos, mas continua liberando solvente por um a dois dias.
  Fechar o livro antes disso prende o vapor entre as folhas e pode velar
  a página oposta.
- **Teste a cola sobre o verniz, não sobre o papel cru.** O verniz muda
  a superfície — é o mesmo mecanismo da cera no couro (ver `CLAUDE.md`,
  seção de transferência): o que colava antes pode não colar depois.
  Use uma sobra.

## Montagem — *tip-in*

Não cole a face inteira. Uma prancha colada de cheio enrijece a folha,
cria um degrau de espessura dentro do caderno dobrado e força a costura.

O método de conservação é o **tip-in**:

1. Aplique um cordão de **4–5 mm de cola apenas na margem interna** da
   prancha (o lado da lombada).
2. Alinhe pelos quatro cantos de registro impressos.
3. Pressione só a faixa colada. O resto da prancha fica solto.

A prancha vira uma aba que levanta, o livro continua abrindo plano, e a
montagem é **reversível** — com PVA neutro ou metilcelulose dá para
descolar depois sem rasgar.

**Cole com o livro já costurado e seco**, nunca antes: uma folha de
gramatura diferente não dobra junto com o caderno.

## Alternativas guardadas

`imagens/` tem as variantes que não entraram, e `imagens/descartadas/`
as recusadas (duplicata exata, baixa resolução, figura de pernas nuas em
vez do manto fechado). Nada foi apagado.

Para o Rei de Amarelo há `01b` em preto e branco, mesma composição, caso
um dia o miolo saia sem cor.
