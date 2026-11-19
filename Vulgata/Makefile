TYPST = typst
PDF   = vulgata.pdf

all: $(PDF) check

$(PDF): typst/vulgata.typ typst/helpers.typ typst/ecclesiastes.typ typst/canticum.typ typst/caritas.typ
	$(TYPST) compile typst/vulgata.typ $@

typst/ecclesiastes.typ typst/canticum.typ typst/caritas.typ: build.py raw/vul_raw.json raw/pt_aa.json
	python3 build.py

check: $(PDF)
	python3 check.py

preview: $(PDF)
	$(TYPST) compile --format png --ppi 110 --pages 6,20,45 typst/vulgata.typ 'preview_{p}.png'

# Two separate A4 covers — front and back. No wrap, no spine: Japanese
# stab binding leaves the sewn edge exposed, which is how these books are
# actually made. Each face is its own piece of vinyl.
cut:
	for f in front back; do \
	  $(TYPST) compile cover/$$f\_vinyl.typ cover/$$f\_vinyl.pdf; \
	  $(TYPST) compile --format png --ppi 105 cover/$$f\_vinyl.typ cover/$$f\_vinyl.png; \
	  $(TYPST) compile --format svg cover/$$f\_vinyl.typ cover/cut_$$f.svg; \
	  python3 cover/cut_mirror.py cover/cut_$$f.svg cover/cut_$$f\_mirrored.svg; \
	done
	python3 cover/check_vinyl.py

cover-check:
	python3 cover/check_vinyl.py

clean:
	rm -f $(PDF) preview_*.png intro_*.png

.PHONY: all check preview cut cover-check clean
