# The King in Yellow — the four weird tales, A5, saddle stitch.
#   make            build the book, imposed and ready to print
#   make check      verify page count, imposition and completeness
#   make preview    render sample pages as PNG
#   make clean      remove generated files

TYPST := typst
PY    := python3

PDF     := king_in_yellow.pdf
BOOKLET := king_in_yellow_booklet.pdf
FRAGS   := typst/song.typ typst/repairer.typ typst/mask.typ \
           typst/dragon.typ typst/yellow_sign.typ

.PHONY: all check preview clean

all: $(BOOKLET) check

$(FRAGS): build.py raw/king_in_yellow_pg8492.txt
	$(PY) build.py

$(PDF): typst/king_in_yellow.typ typst/helpers.typ $(FRAGS)
	$(TYPST) compile typst/king_in_yellow.typ $@

# 96 pages = 6 signatures of 16 (4 sheets each) — the README's sweet spot
# for hand-sewing: clean fold, low creep, no padding waste.
$(BOOKLET): $(PDF)
	$(PY) ../booklet.py $< -o $@ -s 16

check: $(PDF)
	$(PY) check.py

preview: $(PDF)
	$(TYPST) compile --format png --ppi 110 --pages 3,5,7,22 \
	  typst/king_in_yellow.typ 'preview_{p}.png'

clean:
	rm -f $(PDF) $(BOOKLET) preview_*.png
