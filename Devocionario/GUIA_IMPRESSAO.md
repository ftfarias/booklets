# Guia de impressão — Devocionário

A6 dobrado em quarto. 128 páginas = **8 cadernos** de 16 páginas, cada
caderno feito de **2 folhas A4** dobradas e encaixadas uma dentro da outra.
**16 folhas** de Opalina 120 no total, mais 1 de Opalina 180 para as guardas.

## 1. Gerar e conferir

```bash
make imposed
```

Gera `devocionario_imposto.pdf` (32 páginas = 16 folhas, frente e verso)
e roda dois checks: o do livro (`check.py`) e o da imposição
(`check_imposto.py`, que confere se cada face carrega as páginas que a
simulação da dobra prevê). Os dois têm que passar.

## 2. Imprimir

- Adobe Reader, **tamanho real** (nunca "ajustar"), frente e verso.
- **As mesmas configurações da folha de teste que dobrou certo.** Não
  mude nada: borda do duplex, tipo de papel, qualidade. Anote aqui:
  - borda do duplex no Adobe: ________
  - tipo de papel no driver: ________ · qualidade: ________
- **Imprima primeiro só a página 1–2 do PDF** (a folha 1) e dobre. Só
  depois mande o resto.
- Opalina é lisa e a tinta seca por cima: se o verso borrar ao sair, ative
  o tempo de secagem maior do driver Epson (opção de frente e verso).
- Se o duplex automático não aceitar os 120 g: `make imposed-manual`
  gera `imposto_frentes.pdf` e `imposto_versos.pdf`. Imprima as frentes,
  e antes de recolocar a pilha para os versos marque **uma** folha a
  lápis num canto e teste com ela como a L4360 puxa o papel.

As folhas saem na ordem: caderno 1 externa, caderno 1 interna, caderno 2
externa… Os números de página resolvem qualquer dúvida.

## 3. Dobrar (cada folha)

1. Na mesa, com a face virada **para cima** que tem, **na metade de cima,
   duas páginas seguidas, o número par à esquerda** (folha 1: páginas 2 e
   3). A face com a página 1 do quarto fica para baixo.
2. Metade **direita sobre a esquerda**. Vincar com a dobradeira.
3. Metade **de cima para baixo**. Vincar.
4. Lombada à esquerda: a capinha mostra o primeiro número ímpar daquela
   folha (1, 5, 17, 21…) e as páginas correm em ordem, em pé.

Dobre sempre do mesmo jeito: uma folha girada 180° na mesa sai com as
páginas fora de ordem.

## 4. Montar os cadernos

Caderno *k* = folha externa (páginas 1–4 e 13–16 dele) com a **interna**
(5–12) encaixada **no centro**, aberta pela lombada. Confira: folheando,
os números correm de 16 em 16 (1–16, 17–32 … 113–128).

A cabeça continua fechada pela primeira dobra: **não abra ainda** —
fechada, ela mantém as folhas do caderno alinhadas durante a costura.

## 5. Guardas (Opalina 180)

Uma A4 dá as duas guardas. Corte ao meio no lado de 297 (dois retângulos
de 210 × 148,5) e dobre cada um ao meio **no lado de 210**: sai uma guarda
A6 de duas folhas, com a dobra paralela à fibra. Uma no começo do livro,
outra no fim.

## 6. Depois de costurar

Abra a cabeça de cada caderno com espátula ou faca de papel, entrando pela
dobra. A espátula deixa a borda levemente irregular, como nos livros
antigos "por abrir"; faca afiada deixa limpa. **Meça a lombada do miolo
costurado e prensado** — é essa medida, não a conta, que vai para a capa.
