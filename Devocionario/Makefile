TYPST = typst
PDF   = devocionario.pdf

all: $(PDF) check

# build.py always runs first: it takes a second, and a dependency rule
# once let stale fragments through after build.py itself changed.
$(PDF): typst/*.typ build.py textos/biblia_pt.py raw/vul_raw.json
	python3 build.py
	$(TYPST) compile typst/devocionario.typ $@

check: $(PDF)
	python3 check.py

# Ready-to-print imposition: A6 pages 4 per A4 side, folded in quarto,
# two sheets nested = 16-page signatures. Long-edge duplex; from Adobe
# Reader the edge names are inverted. ALWAYS fold `make teste-dobra` first.
imposed: $(PDF) check
	python3 ../quarto.py $(PDF) -o devocionario_imposto.pdf
	python3 check_imposto.py

# Fallback if the L4360 will not auto-duplex 120 g: all fronts, then all
# backs, as two files. See GUIA_IMPRESSAO.md for how to re-feed.
imposed-manual: imposed
	python3 -c "from pypdf import PdfReader, PdfWriter; r=PdfReader('devocionario_imposto.pdf'); f=PdfWriter(); b=PdfWriter(); [ (f if i%2==0 else b).add_page(p) for i,p in enumerate(r.pages)]; f.write('imposto_frentes.pdf'); b.write('imposto_versos.pdf')"
	@echo "imposto_frentes.pdf + imposto_versos.pdf: 16 sides each, same sheet order."

# One sheet with big page numbers 1–8 and the head marked: print it with
# the same settings as the book, fold it, and the numbers must run 1–8.
teste-dobra:
	python3 ../quarto.py --test -o teste_dobra.pdf

preview: $(PDF)
	$(TYPST) compile --format png --ppi 110 --pages 10,11,18,19,60,61,94,95 typst/devocionario.typ 'preview_{p}.png'

clean:
	rm -f $(PDF) devocionario_imposto.pdf imposto_frentes.pdf imposto_versos.pdf teste_papel.pdf teste_dobra.pdf preview_*.png

.PHONY: all check imposed preview clean

# ONE A4 sheet, both sides, from the real imposition: the inner sheet of
# signature 2 = pages 21–28, mysteries with red rubrics. Print the SAME
# file on every paper being compared, then fold it in quarto.
teste-papel: $(PDF) check
	python3 ../quarto.py $(PDF) -o work/_imposto_tmp.pdf
	python3 -c "from pypdf import PdfReader, PdfWriter; r=PdfReader('work/_imposto_tmp.pdf'); w=PdfWriter(); [w.add_page(r.pages[i]) for i in (6, 7)]; w.write('teste_papel.pdf')"
	@echo "teste_papel.pdf: 2 pages = 1 sheet. Duplex, long edge, actual size."

.PHONY: teste-papel teste-dobra imposed-manual

# Cover: gold HTV on red leather. corte_espelhado.svg goes to the Cameo.
capa:
	cd capa && typst compile --format svg corte.typ corte.svg
	cd capa && python3 cut_mirror.py corte.svg corte_espelhado.svg
	cd capa && typst compile corte.typ corte.pdf && typst compile prova.typ prova.pdf
	cd capa && python3 check_vinyl.py

.PHONY: capa
