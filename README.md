# booklet.py — PDF Booklet Creator

Turns a PDF into a **ready-to-print A5 booklet**. It splits the document into
**signatures** (folded sections), orders the pages using booklet imposition,
and — by default — composes two A5 pages per landscape A4 sheet, already
rotated for automatic duplex. You print **one PDF, one job**, with **no booklet
mode in Acrobat/Preview**. Fold, nest, sew, done.

---

## How it works

A **signature** is a group of sheets folded together to form a section of the
booklet. By default each signature is **16 PDF pages** = **4 A4 sheets**,
printed double-sided. Folded in half, each sheet yields 4 A5 faces → 16
readable A5 pages per signature.

Imposition order (page numbers within a 16-page signature):

| Sheet | Front (left, right) | Back (left, right) |
|-------|---------------------|--------------------|
| 1     | 16, 1               | 2, 15              |
| 2     | 14, 3               | 4, 13              |
| 3     | 12, 5               | 6, 11              |
| 4     | 10, 7               | 8, 9               |

If the total page count isn't a multiple of the signature size, blank pages are
added at the end automatically.

### Imposed mode (default)

Each output page is a **landscape A4 sheet** holding **two A5 pages side by
side**. Back sides are prepared for **short-edge duplex**: the printer flips
each sheet on its short (top↔bottom) edge, which rotates the back 180° *and*
mirrors left↔right — so the script rotates each back page 180° **and** swaps the
two slots, making the pair land correctly behind the front. All signatures are
concatenated into **one PDF**, so the whole book prints in a single job.

Use `--long-edge` if your printer flips on the long edge instead.

### Legacy mode (`--legacy`)

The old behavior: reorders full A4 pages in imposition order but does **not**
compose 2-up — it relies on the printer dialog's *Booklet* mode to place two
pages per sheet. Kept for compatibility. This mode is fragile because Acrobat's
booklet settings (binding, orientation, flip edge) are easy to get wrong; the
imposed mode above avoids all of that.

---

## Requirements

Python 3.10+ and the `pypdf` library:

```bash
pip install pypdf
```

---

## Usage

```bash
python3 booklet.py <input.pdf> [options]
```

### Options

| Option | Short | Default | Description |
|--------|-------|---------|-------------|
| `--output PATH` | `-o` | `<input_stem>_booklet.pdf` | Output PDF (imposed) or directory (legacy) |
| `--signature-size N` | `-s` | `16` | Pages per signature — must be a multiple of 4 |
| `--long-edge` | | off | Impose for long-edge duplex instead of short-edge |
| `--legacy` | | off | Old reorder-only behavior (needs Acrobat Booklet mode) |
| `--manual-duplex` | `-m` | off | *(legacy only)* split each signature into `_front.pdf` / `_back.pdf` |

---

## Examples

**Basic — one ready-to-print PDF, 16-page (4-sheet) signatures:**
```bash
python3 booklet.py mybook.pdf
# → mybook_booklet.pdf
```

**Choose the output file:**
```bash
python3 booklet.py mybook.pdf -o ./out/mybook_print.pdf
```

**5-sheet signatures (20 pages each):**
```bash
python3 booklet.py mybook.pdf --signature-size 20
```

**Printer flips on the long edge:**
```bash
python3 booklet.py mybook.pdf --long-edge
```

**Legacy reorder-only, split for a non-duplex printer:**
```bash
python3 booklet.py mybook.pdf --legacy --manual-duplex
```

---

## Choosing a signature size

Remember: **1 A4 sheet = 4 booklet pages**. `--signature-size` counts *pages*,
so sheets-per-signature = size ÷ 4.

| Sig. size | Sheets to fold | Notes |
|-----------|----------------|-------|
| 8         | 2              | Thin sections, minimal creep |
| 12        | 3              | |
| **16**    | **4**          | **Recommended** — clean fold, easy to sew, low creep |
| 20        | 5              | OK; slightly more creep, fewer sections to bind |
| 24+       | 6+             | Not advised for hand-sewing — hard to fold, strong creep |

**Creep (push-out):** the more sheets you nest in one fold, the more the inner
sheets slide outward at the fore-edge, eating into the inner margin of the
center pages. With 4–5 sheets it's small and trimmed away on a guillotine.
Above that it becomes noticeable. For hand-bound booklets, **4 sheets (size 16)
is the sweet spot; don't exceed 5**.

Also pick a size that leaves the fewest blank padding pages: a 33-page document
fits neatly into 3 × 12-page signatures (3 blanks) rather than 3 × 16 (15 blanks
in the last signature).

---

## Printing instructions (imposed mode)

1. Open the output PDF (e.g. `mybook_booklet.pdf`).
2. Print settings:
   - **Actual size / 100 %** — NOT "Fit", NOT "Booklet".
   - **Two-Sided: On**, **Short-Edge binding** (use `--long-edge` output if your
     printer flips on the long edge).
   - Paper: **A4**.
3. **Test one sheet first:** print pages **1–2** only, fold in half, and check
   that the front cover and its back read upright and in order. If the back is
   upside-down or mirrored, you used the wrong flip edge — regenerate with/without
   `--long-edge`, or fix the printer's flip setting.
4. Print the whole PDF, **fold each sheet** in half, **nest** the sheets of each
   signature, then **stack the signatures in order** and bind along the fold
   (sew, staple, or glue).

> Tip (macOS): once the print dialog is correct, save it as a **Preset** so you
> never have to reconfigure it.

### Legacy mode printing

`--legacy` output still relies on Acrobat/Preview **Booklet** mode with
short-edge flip, and `--legacy --manual-duplex` produces `_front.pdf` /
`_back.pdf`: print the front, put the stack back face-down without shuffling,
then print the back (it's pre-reversed to align).

---

## Output

**Imposed mode (default):** a single PDF — `<input_stem>_booklet.pdf` (or the
`-o` path). Landscape A4 pages, 2 signatures' worth of sheets concatenated in
reading order.

**Legacy mode:** one PDF per signature in the output directory, named
`<input_stem>_signature_NNN_of_TTT.pdf` (plus `_front`/`_back` with
`--manual-duplex`).


---

## quarto.py — A6 in quarto

Sibling of `booklet.py` for **A6 portrait** pages: four per side of a
landscape A4, folded twice, two sheets nested per 16-page signature
(`--sheets`). The spine fold runs with the grain of ordinary long-grain
A4, which an A4→A5 fold does not. The page order is derived by simulating
the folds, not typed from a table.

```bash
python3 quarto.py --test -o quarto_test.pdf   # fold this one sheet first
python3 quarto.py book.pdf -o book_quarto.pdf # long-edge duplex (default)
```

Folding: page-1 side **down** on the table; right half over the left;
top half down over the bottom. Spine on the left, slit the head after
sewing.
