# Manual do Encadernador — A5 encadernado à mão.
#   make            constrói o PDF e a versão imposta para impressão
#   make check      confere contagem de páginas e integridade
#   make preview    gera PNGs de páginas-amostra
#   make clean      remove gerados

TYPST := typst
PY    := python3

.PHONY: all check preview clean

all: manual_booklet.pdf

# Apêndices A, D e E são extraídos dos capítulos — nunca editar à mão
APGER := apendices/A-tabelas.md apendices/D-medidas.md apendices/E-testes.md
$(APGER): gera_apendices.py $(wildcard capitulos/*.md)
	$(PY) gera_apendices.py

# Fragmento Typst gerado a partir dos capítulos Markdown
typst/corpo.typ: build.py MANUAL.md NEGOCIO.md $(wildcard capitulos/*.md) \
                 $(wildcard apendices/*.md) $(APGER)
	$(PY) build.py

manual.pdf: typst/manual.typ typst/corpo.typ typst/helpers.typ
	$(TYPST) compile --root . typst/manual.typ $@

# O tamanho do caderno (12, 16 ou 20 páginas) é escolhido por cadernos.py
# para deixar o mínimo de páginas em branco no fim — a contagem muda a cada
# revisão, e fixar à mão obrigava a trocar toda vez.
manual_booklet.pdf: manual.pdf cadernos.py
	$(PY) ../booklet.py $< -o $@ -s $$($(PY) cadernos.py $<)

check: manual.pdf
	$(PY) check.py

preview: manual.pdf
	@mkdir -p preview
	$(TYPST) compile --root . --format png --pages 1,3,6,7 --ppi 110 \
	  typst/manual.typ "preview/p{p}.png"

clean:
	rm -f manual.pdf manual_booklet.pdf typst/corpo.typ preview/*.png
