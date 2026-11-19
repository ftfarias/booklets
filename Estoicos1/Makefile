# Estoicos — two hand-bound A5 volumes from public-domain sources.
#   make            build both volumes, imposed and ready to print
#   make check      verify page counts, imposition and completeness
#   make clean      remove generated PDFs

TYPST := typst
PY    := python3

.PHONY: all vol1 vol2 covers check clean

all: vol1 vol2 covers

# ── Volume I — Epictetus (144 pp = 36 sheets, 9 signatures of 16) ──
vol1: vol1_epictetus_booklet.pdf
typst/enchiridion.typ typst/discourses.typ typst/life.typ: build_vol1.py clean/greek_map.json
	$(PY) build_vol1.py
vol1_epictetus.pdf: typst/vol1_epictetus.typ typst/enchiridion.typ typst/discourses.typ typst/life.typ typst/helpers.typ
	$(TYPST) compile typst/vol1_epictetus.typ $@
vol1_epictetus_booklet.pdf: vol1_epictetus.pdf
	$(PY) ../booklet.py $< -o $@ -s 16

# ── Volume II — Marcus Aurelius (132 pp = 33 sheets, 11 signatures of 12) ──
vol2: vol2_marcus_booklet.pdf
typst/meditations.typ: build_vol2.py
	$(PY) build_vol2.py
vol2_marcus.pdf: typst/vol2_marcus.typ typst/meditations.typ typst/helpers.typ
	$(TYPST) compile typst/vol2_marcus.typ $@
vol2_marcus_booklet.pdf: vol2_marcus.pdf
	$(PY) ../booklet.py $< -o $@ -s 12

# ── Covers and colophons ──
covers:
	$(TYPST) compile --input vol=1 cover/cover.typ cover/cover_vol1.pdf
	$(TYPST) compile --input vol=2 cover/cover.typ cover/cover_vol2.pdf
	$(TYPST) compile --input vol=1 cover/colophon_a5.typ cover/colofon_vol1_A5.pdf
	$(TYPST) compile --input vol=2 cover/colophon_a5.typ cover/colofon_vol2_A5.pdf
	$(PY) cover/make_bifolio.py cover/colofon_vol1_A5.pdf cover/colofon_vol1_verge_A4.pdf
	$(PY) cover/make_bifolio.py cover/colofon_vol2_A5.pdf cover/colofon_vol2_verge_A4.pdf

check: vol1_epictetus.pdf vol2_marcus.pdf
	$(PY) check.py

clean:
	rm -f vol1_epictetus*.pdf vol2_marcus*.pdf cover/cover_vol*.pdf \
	      cover/colofon_vol*.pdf preview/*.png preview/*.pdf
