# Dipolo — caderno de anotacoes. As frases sao a unica parte impressa
# do miolo; o resto e papel dobrado em branco.

TYPST = typst compile --font-path fonts

all: frases.pdf guardas

frases.pdf: typst/frases_main.typ typst/helpers.typ raw/frases.md build.py
	python3 build.py
	$(TYPST) typst/frases_main.typ $@

guardas: guardas/guarda.pdf

guardas/guarda.pdf: typst/guarda.typ typst/helpers.typ typst/logo.svg typst/logo-forte.svg
	$(TYPST) typst/guarda.typ $@

check: frases.pdf guardas
	python3 check.py
	python3 check_guarda.py

preview: frases.pdf guardas
	$(TYPST) --format png --ppi 110 typst/frases_main.typ "preview/f{n}.png"
	$(TYPST) --format png --ppi 100 typst/guarda.typ "guardas/g{n}.png"

clean:
	rm -f frases.pdf typst/frases.typ preview/*.png
	rm -f guardas/*.pdf guardas/g*.png

.PHONY: all check preview clean guardas
