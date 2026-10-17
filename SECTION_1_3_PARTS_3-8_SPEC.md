# Spec: Section 1.3, Parts 3–8 (Multiplying → Factoring by Grouping)

**For:** Codex. Build these videos in the existing project (`codex-handoff/project/`).
**Read first:** `codex-handoff/HANDOFF.md`. It covers the design system, the `say()` / `line()` narration API, rendering, the review loop and the **Manim pitfalls in §8**. Everything here follows those conventions.
**Source:** Stewart, *Precalculus*, Section 1.3 *Algebraic Expressions*, pp. 26–33, Examples 2–15. Every worked result below was checked by expanding it back out.

**Total: 14 videos in 5 series.**

| Series header | Book part | Videos |
|---|---|---|
| `MULTIPLYING` | Part 3: Multiplying algebraic expressions | 2 |
| `SPECIAL PRODUCTS` | Part 4: Special product formulas | 3 |
| `FACTORING` | Part 5: Common factors and trinomials | 3 |
| `SPECIAL FACTORING` | Part 6: Special factoring formulas | 3 |
| `FACTOR COMPLETELY` | Parts 7 + 8: Factoring completely, fractional exponents, grouping | 3 |

Part 8 (grouping) has only one example set, so it's merged into the Part 7 series as its third video. That avoids a lonely "1 / 1" header.

---

## 0. Requirements for every video (non-negotiable)

1. **Base class:** subclass `PolyScene` (from `poly_common.py`) through a per-series class with `TOPIC = "..."` and `WATERMARK = True` (inherited). Set `PART = "n / N"`.
2. **Format:** 1080×1920, 60 fps final; 540×960 / 30 fps for previews. Length **35–55 s**. If a video runs long, cut a beat rather than speed up the pacing.
3. **Narration:** every beat goes through `self.say(line(subtitle_markup, spoken_text), anims=..., steps=..., gap=...)`.
   - Spoken text is ElevenLabs-ready: numbers and powers in words ("x squared", "minus seven x"), with `{BR}` (`<break time="0.2s" />`) for pauses.
   - Subtitles use the coloured markup helpers `B()`, `E()`, `R()`, `W()` and `sup()`. At most 2 lines per card, so split long sentences into 2 `line()`s.
4. **Colour roles (strict):**
   - Variables/bases: **blue** `#58C4DD`. Exponents and counts: **yellow** `#FFD54F`. Answers/correct: **green** `#83C167`. Traps/wrong: **red** `#FC6255`. Plain coefficients and operators: **ink** `#ECEFF4`.
   - Build polynomials with `poly(terms)` / `ptex(...)`, which colour them correctly. Never build one `MathTex` per term (it loses LaTeX's sign spacing).
5. **Structure:**
   - A hook in the first 2 s: a question or a tempting wrong answer.
   - One "signature" visual per video.
   - Book examples cited by number.
   - End with `self.card(...)` (key idea), then `self.outro()` (fades back to the opening frame so the video loops).
6. **Layout:** math stays in the math zone (`fit_zone()` / `fit()`), and nothing goes outside the safe zone. Fractions containing radicals or tall expressions use `SMALL_FS`.
7. **Review loop for each video:** render the preview, run `tools/storyboard.py`, then check for collisions, ghost copies (pitfalls 1–2), overflow and length. Fix and re-render.
8. **Deliverables per series:**
   - The scene files.
   - `build/<Scene>.voiceover.txt` and `.srt` (auto-generated on render).
   - A combined script doc via `tools/export_scripts.py <SERIES>_VOICEOVER.md <Scenes...>`.
   - Storyboard sheets.
   - README table rows.

### Suggested new shared helpers
- **`mult_common.py`:** `area_model(row_terms, col_terms)`. A rectangle split into a grid of cells, one per (row term × column term), with header labels and cell fill tinted by degree (x² blue, x yellow, constant grey, matching `algebra_tile()` in `add_common.py`). It returns the cells so products can be written into them. Used by M1, SP1, SP2, F2 and SF2.
- **`fact_common.py`:**
  - `pair_search(product, target_sum)`: a "slot machine" that cycles through factor pairs with live product and sum readouts, turning green on a match.
  - `factor_tree(root, children...)`: branches growing down, with leaves that turn green when prime.
  - `block(expr)`: a rounded box that stands for a repeated sub-expression, used for "treat x + y as one A".

---

## Series A: `MULTIPLYING` (2 videos)

`class MultScene(PolyScene): TOPIC = "MULTIPLYING"`

### M1: Every term times every term (FOIL)
- **File / class:** `mult1_foil.py` / `M1FOIL`, `PART = "1 / 2"`
- **Book:** Example 2. (2x + 1)(3x − 5) = 6x² − 10x + 3x − 5 = **6x² − 7x − 5**
- **Signature visual:** an **area model**. A rectangle whose top side is split into `2x | 1` and whose left side is split into `3x | −5`. The four cells fill with the four products, and the FOIL arcs (F, O, I, L) light up the matching cells.

| Beat | Subtitle | Spoken | Visual |
|---|---|---|---|
| 1 Hook | Is (2x + 1)(3x − 5) just 6x² − 5? | Is two x plus one, times three x minus five, just six x squared minus five? | The product, then a red "= 6x² − 5 ?" |
| 2 | Picture the product as a rectangle. | Picture the product as a rectangle. {BR} Split each side into its terms. | Rectangle grows; side labels 2x \| 1 and 3x \| −5 |
| 3 | First, Outer, Inner, Last: four boxes. | First times first: six x squared. {BR} Outer: minus ten x. {BR} Inner: plus three x. {BR} Last: minus five. | Cells fill one by one with F, O, I, L tags and arcs over the original product |
| 4 | The middle boxes are like terms: −10x + 3x = −7x. | The two middle boxes are like terms: {BR} minus ten x plus three x is minus seven x. | The two x-cells pulse and merge; the result line **6x² − 7x − 5** appears in green |
| 5 | The hook missed two whole boxes. | So the quick answer missed two whole boxes. | The hook's wrong answer reappears, crossed out |
| Card | Every term times every term. | Every term times every term. {BR} FOIL is just a way to not miss one. | Card: (a + b)(c + d) = ac + ad + bc + bd |

### M2: Bigger polynomials: distribute, then line up
- **File / class:** `mult2_distribute.py` / `M2Distribute`, `PART = "2 / 2"`
- **Book:** Example 3, both solutions. (2x + 3)(x² − 5x + 4) = **2x³ − 7x² − 7x + 12**
  - 2x · (x² − 5x + 4) = 2x³ − 10x² + 8x
  - 3 · (x² − 5x + 4) = 3x² − 15x + 12
- **Signature visual:** distribution arcs (2x shoots an arc to each of the three terms, then 3 does the same). Then **table form**: the two partial rows stack like long multiplication, aligned in x³ / x² / x / 1 columns (reuse `BIN_X` / `bin_heads()` from `add_common.py`), and each column adds up.

| Beat | Subtitle | Spoken | Visual |
|---|---|---|---|
| 1 Hook | FOIL needs two terms each. Now what? | Two x plus three, times x squared minus five x plus four. {BR} FOIL needs two terms each. Now what? | The product appears; a "FOIL?" chip turns red |
| 2 | Same rule: every term times every term. | Same rule: every term times every term. {BR} Two x times each term: two x cubed, minus ten x squared, plus eight x. | Three arcs from 2x; the partial row appears |
| 3 | Then 3 times each term. | Then three times each term: {BR} three x squared, minus fifteen x, plus twelve. | Three arcs from 3; the second partial row |
| 4 | Line them up by power and add each column. | Line them up by power, like long multiplication, {BR} and add each column. | Rows slide into the columns and add: **2x³ − 7x² − 7x + 12** |
| 5 | 2 terms × 3 terms = 6 products. | Two terms times three terms: six products before combining. {BR} Count them to check. | Six small tiles light up one per product |
| Card | Every term × every term, then combine. | Multiply every pair, {BR} then combine like terms. | Card: "2 terms × 3 terms = 6 products" |

---

## Series B: `SPECIAL PRODUCTS` (3 videos)

`class SpecialScene(PolyScene): TOPIC = "SPECIAL PRODUCTS"`

### SP1: The square of a sum (and the most common mistake)
- **File / class:** `sprod1_square.py` / `SP1SquareOfSum`, `PART = "1 / 3"`
- **Book:** the formulas (A ± B)² = A² ± 2AB + B²; the *Visualizing a Formula* Discovery Project; Example 4(a): (3x + 5)² = **9x² + 30x + 25**; Concept 8(a): (x + 5)² ≠ x² + 25
- **Signature visual:** a **square with side a + b** that splits into an a² square, a b² square and two ab rectangles. The two rectangles flash, as the "forgotten middle".

| Beat | Subtitle | Spoken | Visual |
|---|---|---|---|
| 1 Hook | Is (x + 5)² = x² + 25? | Is x plus five, squared, equal to x squared plus twenty-five? | Big equation with a red "?" |
| 2 | Draw a square with side a + b. | Draw a square with side a plus b. {BR} It splits into four pieces. | Square with sides labelled a \| b, cut into four regions |
| 3 | a², b², and two ab rectangles: the ones people forget. | A squared, b squared, {BR} and two a b rectangles: the ones people forget. | Regions fill; the ab pair pulses yellow |
| 4 | (A + B)² = A² + 2AB + B². With a minus, the middle turns negative. | So A plus B, squared, is A squared plus two A B plus B squared. {BR} With a minus, the middle term turns negative. | Formula, then the (A − B)² version |
| 5 | (x + 5)² = x² + 10x + 25. | So x plus five, squared, is x squared plus ten x plus twenty-five. | Hook wrong answer crossed out; correct line in green; the 10x box links to 2·x·5 |
| 6 | Example: (3x + 5)² = 9x² + 30x + 25. | With A as three x and B as five: {BR} nine x squared, plus thirty x, plus twenty-five. | A and B labels drop onto 3x and 5 (Principle of Substitution) |
| Card | Squaring a sum? Don't forget 2AB. | Squaring a sum? {BR} Don't forget the two A B. | Card: (A ± B)² = A² ± 2AB + B² |

### SP2: Sum times difference: the middle cancels
- **File / class:** `sprod2_sum_difference.py` / `SP2SumTimesDifference`, `PART = "2 / 3"`
- **Book:** (A + B)(A − B) = A² − B²; Example 5(a): (2x − √y)(2x + √y) = **4x² − y**; Example 5(b): (x + y − 1)(x + y + 1) = (x + y)² − 1 = **x² + 2xy + y² − 1**
- **Signature visual:** FOIL on (x + 7)(x − 7) produces −7x and +7x, which collide and annihilate (flash, then fade to nothing). Later, **x + y is boxed** into one block "A" so the hidden pattern snaps into place.

| Beat | Subtitle | Spoken | Visual |
|---|---|---|---|
| 1 Hook | (x + 7)(x − 7): four products, only two survive. | x plus seven, times x minus seven. {BR} Four products, but only two survive. | The product; four empty FOIL slots |
| 2 | x² − 7x + 7x − 49: the middle terms cancel. | Multiply it out: x squared, minus seven x, plus seven x, minus forty-nine. {BR} The middle terms cancel. | Slots fill; ±7x collide and vanish; **x² − 49** |
| 3 | (A + B)(A − B) = A² − B². | That's the rule: {BR} A plus B, times A minus B, is A squared minus B squared. | Formula card in the math zone |
| 4 | Example: (2x − √y)(2x + √y) = 4x² − y. | With A as two x and B as root y: {BR} four x squared, minus y. | Substitution labels; uses `rtex` for √y |
| 5 | Hidden pattern: treat x + y as one block A. | It can hide: {BR} treat x plus y as one block. | (x + y − 1)(x + y + 1) with x + y boxed as "A" |
| 6 | A² − 1 = x² + 2xy + y² − 1. | Then it's A squared minus one: {BR} x squared, plus two x y, plus y squared, minus one. | The block expands with the SP1 formula |
| Card | Sum times difference = difference of squares. | Sum times difference? {BR} The middle cancels, leaving a difference of squares. | Card: (A + B)(A − B) = A² − B² |

### SP3: Cubes: the 1-3-3-1 pattern
- **File / class:** `sprod3_cubes.py` / `SP3Cubes`, `PART = "3 / 3"`
- **Book:** (A ± B)³ = A³ ± 3A²B + 3AB² ± B³; Example 4(b): (x² − 2)³ = **x⁶ − 6x⁴ + 12x² − 8**
- **Signature visual:** coefficient chips **1 · 3 · 3 · 1** above four term slots. The exponent of A counts down (3, 2, 1, 0) as the exponent of B counts up (0, 1, 2, 3), each shown as yellow counters. Optional stretch: an isometric cube of side a + b splitting into 1 + 3 + 3 + 1 blocks (reuse `iso_cube()` from `rad1_what.py`).

| Beat | Subtitle | Spoken | Visual |
|---|---|---|---|
| 1 Hook | (x² − 2)³: multiply it out three times? | x squared minus two, cubed. {BR} Do you really multiply it out three times? | The expression; three stacked copies, crossed out |
| 2 | Cubes follow a pattern: 1, 3, 3, 1. | No. Cubes follow a pattern: one, three, three, one. | Coefficient chips appear |
| 3 | A's power goes down, B's goes up. | A's power counts down, while B's counts up. | (A + B)³ = A³ + 3A²B + 3AB² + B³ builds term by term with counters |
| 4 | For a minus, the signs alternate. | For a minus, the signs alternate: plus, minus, plus, minus. | (A − B)³ version with red signs |
| 5 | A = x², B = 2. | Here A is x squared and B is two. | Substitution labels |
| 6 | x⁶ − 6x⁴ + 12x² − 8. | So it's x to the sixth, minus six x to the fourth, plus twelve x squared, minus eight. | Each term computes (e.g. 3·(x²)²·2 = 6x⁴) and settles in green |
| Card | Cubes: 1, 3, 3, 1. | Cubes: one, three, three, one. {BR} Powers trade places. | Card: both cube formulas |

---

## Series C: `FACTORING` (3 videos)

`class FactorScene(PolyScene): TOPIC = "FACTORING"`

### F1: Pull out the greatest common factor
- **File / class:** `fact1_gcf.py` / `F1CommonFactor`, `PART = "1 / 3"`
- **Book:** factoring as expanding in reverse, (x − 2)(x + 3) = x² + x − 6; Example 6:
  - (a) 3x² − 6x = **3x(x − 2)**
  - (b) 8x⁴y² + 6x³y³ − 2xy⁴ = **2xy²(4x³ + 3x²y − y²)**
  - (c) (2x + 4)(x − 3) − 5(x − 3) = **(2x − 1)(x − 3)**
- **Signature visual:** an expand ⇄ factor **rewind** (the same equation plays forward, then backward). For 6(b), the GCF is built **piece by piece** in a three-row table (numbers 8, 6, 2 → 2; x⁴, x³, x → x; y², y³, y⁴ → y²), and the *smallest* exponent in each row glows.

| Beat | Subtitle | Spoken | Visual |
|---|---|---|---|
| 1 Hook | Expanding goes forward. Factoring goes back. | Expanding goes forward. {BR} Factoring goes back. | (x − 2)(x + 3) → x² + x − 6, then rewind |
| 2 | 3x² − 6x: both terms share 3x. | In three x squared minus six x, {BR} both terms share three x. | The 3x inside each term highlights (as in `poly3_terms_factors.py`) |
| 3 | So it's 3x(x − 2). Check by multiplying back. | So it's three x, times x minus two. {BR} Multiply back to check. | 3x steps outside; distribution arcs confirm |
| 4 | Bigger: find the GCF piece by piece. | For a bigger one, build the common factor piece by piece. | The 6(b) expression and the three-row GCF table |
| 5 | Take the smallest power of each: 2xy². | Numbers: two. {BR} x: the smallest power, x. {BR} y: y squared. {BR} Together, two x y squared. | Smallest exponents glow; result 2xy²(4x³ + 3x²y − y²) |
| 6 | A common factor can be a whole binomial. | A common factor can even be a whole binomial: {BR} x minus three. | 6(c): (x − 3) boxed in both terms, then (2x − 1)(x − 3) |
| Card | Pull out the GCF first. Always check. | Pull out the greatest common factor first, {BR} and always check by multiplying back. | Card |

### F2: x² + bx + c: two numbers, one product, one sum
- **File / class:** `fact2_trinomial.py` / `F2SumAndProduct`, `PART = "2 / 3"`
- **Book:** (x + r)(x + s) = x² + (r + s)x + rs; Example 7: x² + 7x + 12 = **(x + 3)(x + 4)**; Example 9(a): x² − 2x − 3 = **(x − 3)(x + 1)**
- **Signature visual:** `pair_search(12, 7)`, a slot machine through 1·12 (sum 13), 2·6 (8) and 3·4 (7 ✓), with live "product / sum" readouts.

| Beat | Subtitle | Spoken | Visual |
|---|---|---|---|
| 1 Hook | x² + 7x + 12: find two numbers. | To factor x squared plus seven x plus twelve, {BR} you need two special numbers. | The trinomial; two empty slots ( x + □ )( x + □ ) |
| 2 | (x + r)(x + s) = x² + (r + s)x + rs. | Here's why: {BR} x plus r, times x plus s, is x squared, plus r plus s x, plus r s. | Mini area model; r + s glows yellow, rs glows blue |
| 3 | So r · s = 12 and r + s = 7. | So the numbers multiply to twelve, {BR} and add to seven. | Two goal chips: × = 12, + = 7 |
| 4 | Try the pairs: 3 and 4 work. | Try the pairs: one and twelve, two and six, three and four. {BR} Three and four work. | Slot machine lands on 3·4 in green |
| 5 | x² + 7x + 12 = (x + 3)(x + 4). | So it's x plus three, times x plus four. | Slots fill; check by FOIL |
| 6 | Negatives: x² − 2x − 3 = (x − 3)(x + 1). | With negatives: multiply to negative three, add to negative two: {BR} negative three and one. | Example 9(a), same machine |
| Card | Multiply to c, add to b. | Find two numbers that multiply to c, {BR} and add to b. | Card |

### F3: ax² + bx + c: smart trial and error
- **File / class:** `fact3_trial_error.py` / `F3TrialAndError`, `PART = "3 / 3"`
- **Book:** (px + r)(qx + s) with pq = a, rs = c, ps + qr = b; Example 8: 6x² + 7x − 5 = **(3x + 5)(2x − 1)**; Example 9(b): (5a + 1)² − 2(5a + 1) − 3 = **(5a − 2)(5a + 2)**
- **Signature visual:** candidate factorings are tried one after another, each with a **middle-term meter**: Outer + Inner computed live, red until it equals 7x. Then the **block trick**: every 5a + 1 collapses into a single box □, so the problem becomes □² − 2□ − 3.

| Beat | Subtitle | Spoken | Visual |
|---|---|---|---|
| 1 Hook | 6x² + 7x − 5: now x² has a 6. | Six x squared plus seven x minus five. {BR} Now the x squared has a six in front. | The trinomial |
| 2 | Factors of 6 go in front; factors of −5 go last. | The factors of six go in front, {BR} and the factors of negative five go last. | (□x + □)(□x + □) with "6 = 6·1 or 3·2" and "−5 = 5·(−1) or (−5)·1" chips |
| 3 | The middle term decides. | Then the middle term decides: outer plus inner must be seven x. | First candidate (6x + 5)(x − 1): meter reads −x, red ✗ |
| 4 | (3x + 5)(2x − 1): −3x + 10x = 7x. | Try three x plus five, times two x minus one: {BR} minus three x plus ten x is seven x. | Meter turns green ✓; final factorization |
| 5 | Same shape, bigger pieces: treat 5a + 1 as a block. | Some problems just look hard. {BR} Treat five a plus one as one block. | Example 9(b): blocks □ replace 5a + 1 |
| 6 | □² − 2□ − 3 = (□ − 3)(□ + 1) = (5a − 2)(5a + 2). | Block squared, minus two blocks, minus three, factors like before. {BR} Unpack it: five a minus two, times five a plus two. | Blocks expand back |
| Card | The middle term decides. | Try factor pairs, {BR} and let the middle term decide. | Card |

---

## Series D: `SPECIAL FACTORING` (3 videos)

`class SpecialFactorScene(PolyScene): TOPIC = "SPECIAL FACTORING"`

### SF1: Difference of squares
- **File / class:** `sfact1_diff_squares.py` / `SF1DifferenceOfSquares`, `PART = "1 / 3"`
- **Book:** A² − B² = (A − B)(A + B) (the margin figure); Example 10(a): 4x² − 25 = **(2x − 5)(2x + 5)**; Example 10(b): (x + y)² − z² = **(x + y − z)(x + y + z)**
- **Signature visual (the book's margin figure):** a big A×A square with a small B×B square removed from its corner. The leftover L-shape is cut into two strips, and one strip slides and rotates to form an **(A + B) × (A − B) rectangle**.
- **Extra beat (not in the book, a common mistake):** A² + B² does **not** factor over the real numbers, e.g. x² + 4.

| Beat | Subtitle | Spoken | Visual |
|---|---|---|---|
| 1 Hook | 4x² − 25: no middle term. Can it factor? | Four x squared minus twenty-five. {BR} There's no middle term. Can it factor? | Expression |
| 2 | Cut a small square from a big one. | Take a big square, A by A, {BR} and cut a small B by B square from the corner. | Geometry builds |
| 3 | Rearrange: (A + B) by (A − B). | Slide one strip around, {BR} and the leftover becomes a rectangle: A plus B, by A minus B. | Strip moves; side labels |
| 4 | A² − B² = (A − B)(A + B). | So A squared minus B squared {BR} is A minus B, times A plus B. | Formula |
| 5 | 4x² − 25 = (2x)² − 5² = (2x − 5)(2x + 5). | Four x squared is two x, squared. Twenty-five is five squared. {BR} So it's two x minus five, times two x plus five. | Square roots of each term revealed |
| 6 | Works with blocks too: (x + y)² − z². | It works with blocks too: {BR} x plus y, minus z, times x plus y, plus z. | Example 10(b), with x + y as a block |
| 7 | But a sum of squares, like x² + 4, does not factor. | But a sum of squares, like x squared plus four, {BR} doesn't factor at all. | Red ✗ |
| Card | Difference of squares: (A − B)(A + B). | A difference of squares {BR} always splits into A minus B, times A plus B. | Card |

### SF2: Perfect square trinomials
- **File / class:** `sfact2_perfect_square.py` / `SF2PerfectSquare`, `PART = "2 / 3"`
- **Book:** A² ± 2AB + B² = (A ± B)²; the test "the middle term is ± twice the product of the square roots of the outer terms"; Example 11(a): x² + 6x + 9 = **(x + 3)²**; Example 11(b): 4x² − 4xy + y² = **(2x − y)²**
- **Signature visual:** **algebra tiles assemble into a square**. One x² tile, two "3x" strips and 9 unit tiles snap into a perfect (x + 3) × (x + 3) square (reuse `algebra_tile()` from `add_common.py`). A non-example, x² + 5x + 9, fails to close into a square.

| Beat | Subtitle | Spoken | Visual |
|---|---|---|---|
| 1 Hook | x² + 6x + 9: a square in disguise? | Is x squared plus six x plus nine a square in disguise? | Expression |
| 2 | Outer terms are squares: x² and 3². | The first and last terms are squares: x squared, and three squared. | √ of each outer term labelled |
| 3 | Middle check: 2 · x · 3 = 6x ✓ | Now check the middle: two times x times three is six x. {BR} It matches. | Middle term checked in green |
| 4 | The tiles make a perfect square: (x + 3)². | So the tiles form a perfect square: {BR} x plus three, squared. | Tiles assemble |
| 5 | 4x² − 4xy + y² = (2x − y)². | With a minus in the middle: {BR} four x squared minus four x y plus y squared is two x minus y, squared. | Example 11(b) |
| 6 | x² + 5x + 9? 2 · x · 3 = 6x ≠ 5x. Not a square. | But x squared plus five x plus nine? {BR} The middle should be six x. It isn't a perfect square. | Tiles leave a gap; red ✗ |
| Card | Middle = 2AB? Then it's (A ± B)². | If the middle is two A B, {BR} it's a perfect square. | Card: A² ± 2AB + B² = (A ± B)² |

### SF3: Sums and differences of cubes
- **File / class:** `sfact3_cubes.py` / `SF3Cubes`, `PART = "3 / 3"`
- **Book:** A³ − B³ = (A − B)(A² + AB + B²) and A³ + B³ = (A + B)(A² − AB + B²); Example 12(a): 27x³ − 1 = **(3x − 1)(9x² + 3x + 1)**; Example 12(b): x⁶ + 8 = **(x² + 2)(x⁴ − 2x² + 4)**
- **Signature visual:** the **sign pattern "S-O-AP"**: the first sign is the *Same*, the second is the *Opposite*, the third is *Always Positive*. Three signs light up in the formula with matching labels. (SOAP is a common classroom mnemonic, not from the book.)

| Beat | Subtitle | Spoken | Visual |
|---|---|---|---|
| 1 Hook | 27x³ − 1: a difference of cubes. | Twenty-seven x cubed minus one. {BR} That's a difference of cubes. | Expression; 27x³ = (3x)³ and 1 = 1³ revealed |
| 2 | A³ − B³ = (A − B)(A² + AB + B²). | A cubed minus B cubed {BR} is A minus B, times A squared plus A B plus B squared. | Formula builds |
| 3 | Signs: Same, Opposite, Always positive. | Remember the signs: {BR} same, opposite, always positive. | The three signs glow with S / O / AP tags |
| 4 | A = 3x, B = 1: (3x − 1)(9x² + 3x + 1). | Here A is three x and B is one: {BR} three x minus one, times nine x squared plus three x plus one. | Substitution |
| 5 | x⁶ + 8 = (x²)³ + 2³. | x to the sixth plus eight is x squared, cubed, plus two cubed. | Hidden cubes revealed |
| 6 | (x² + 2)(x⁴ − 2x² + 4). | So it's x squared plus two, {BR} times x to the fourth minus two x squared plus four. | Sum formula applied, SOAP signs |
| Card | Cubes: Same, Opposite, Always positive. | For sums and differences of cubes: {BR} same, opposite, always positive. | Card: both formulas |

---

## Series E: `FACTOR COMPLETELY` (3 videos)

`class CompleteScene(PolyScene): TOPIC = "FACTOR COMPLETELY"`

### FC1: Keep going until nothing is left
- **File / class:** `fcomp1_tree.py` / `FC1FactorTree`, `PART = "1 / 3"`
- **Book:** the strategy (common factors first, then special forms, then repeat); Example 13(a): 2x⁴ − 8x² = **2x²(x − 2)(x + 2)**; Example 13(b): x⁵y² − xy⁶ = **xy²(x² + y²)(x + y)(x − y)**
- **Signature visual:** a **factor tree** (`factor_tree()`). Each branch splits off one step, and leaves turn green once they're prime. In 13(b), x² + y² stays a leaf (a sum of squares; this links back to SF1).

| Beat | Subtitle | Spoken | Visual |
|---|---|---|---|
| 1 Hook | 2x⁴ − 8x² = 2x²(x² − 4). Done? Not yet. | Two x to the fourth minus eight x squared {BR} is two x squared, times x squared minus four. {BR} Done? Not yet. | First split; x² − 4 blinks |
| 2 | Strategy: common factor, special forms, repeat. | The strategy: {BR} common factor first, then special forms, then repeat. | Three-step checklist chip row |
| 3 | x² − 4 is a difference of squares. | x squared minus four is a difference of squares. | Tree branches to (x − 2)(x + 2); leaves go green |
| 4 | Harder: x⁵y² − xy⁶ = xy²(x⁴ − y⁴). | A harder one: {BR} pull out x y squared, leaving x to the fourth minus y to the fourth. | Example 13(b) root and first branch |
| 5 | x⁴ − y⁴ splits twice. | x to the fourth minus y to the fourth is a difference of squares, {BR} and so is x squared minus y squared. | Two more levels; x² + y² stays a green leaf |
| 6 | xy²(x² + y²)(x + y)(x − y). | Collect the leaves: {BR} x y squared, times x squared plus y squared, times x plus y, times x minus y. | Leaves fly into the final product |
| Card | Common factor first. Repeat until every piece is prime. | Common factor first, {BR} and repeat until every piece is prime. | Card |

### FC2: Fractional exponents: pull out the smallest power
- **File / class:** `fcomp2_fractional.py` / `FC2FractionalExponents`, `PART = "2 / 3"`
- **Book:** Example 14 (the book notes this appears in calculus). Margin note: x^(3/2) = x^(1/2)·x¹.
  - (a) 3x^(3/2) − 9x^(1/2) + 6x^(−1/2) = 3x^(−1/2)(x² − 3x + 2) = **3x^(−1/2)(x − 1)(x − 2)**
  - (b) (2 + x)^(−2/3)·x + (2 + x)^(1/3) = (2 + x)^(−2/3)[x + (2 + x)] = **2(2 + x)^(−2/3)(1 + x)**
- **Signature visual:** an **exponent number line** marks 3/2, 1/2 and −1/2. The smallest one (−1/2) is boxed; arrows show the distance from it to each exponent (2, 1, 0), and those distances become the leftover exponents. This links to the Rational Exponents series.

| Beat | Subtitle | Spoken | Visual |
|---|---|---|---|
| 1 Hook | 3x^(3/2) − 9x^(1/2) + 6x^(−1/2): factor out what? | Three x to the three halves, minus nine x to the one half, plus six x to the negative one half. {BR} What do you factor out? | Expression |
| 2 | Pull out the smallest power: x^(−1/2). | Pull out the power with the smallest exponent: {BR} x to the negative one half. | Number line; −1/2 boxed |
| 3 | Subtract exponents: what's left is x², x, and 1. | Subtract exponents to see what's left: {BR} x squared, x, and one. | Distance arrows 2, 1, 0 |
| 4 | 3x^(−1/2)(x² − 3x + 2) = 3x^(−1/2)(x − 1)(x − 2). | So it's three x to the negative one half, times x squared minus three x plus two, {BR} which factors into x minus one, times x minus two. | Result; the trinomial factors (link to F2) |
| 5 | Blocks too: (2 + x) to the smallest power, −2/3. | It works with blocks: {BR} here pull out two plus x, to the negative two thirds. | Example 14(b) with 2 + x as a block |
| 6 | Result: 2(2 + x)^(−2/3)(1 + x). | Inside, x plus two plus x is two plus two x, {BR} so it's two, times two plus x to the negative two thirds, times one plus x. | Simplification |
| Card | Factor out the smallest exponent. | With fractional exponents, {BR} factor out the smallest one. | Card |

### FC3: Factoring by grouping
- **File / class:** `fcomp3_grouping.py` / `FC3Grouping`, `PART = "3 / 3"`
- **Book:** Example 15.
  - (a) x³ + x² + 4x + 4 = x²(x + 1) + 4(x + 1) = **(x² + 4)(x + 1)**
  - (b) x³ − 2x² − 9x + 18 = x²(x − 2) − 9(x − 2) = (x² − 9)(x − 2) = **(x − 3)(x + 3)(x − 2)**
- **Signature visual:** the four terms split into two pairs (brackets). Each pair factors, and the **same binomial appears in both** (it glows in matching colors), then slides out front, the way the shared factor did in `poly3_terms_factors.py`.

| Beat | Subtitle | Spoken | Visual |
|---|---|---|---|
| 1 Hook | Four terms, no common factor. Try pairs. | x cubed plus x squared plus four x plus four. {BR} Nothing is common to all four. Try pairs. | Expression; pair brackets |
| 2 | x²(x + 1) + 4(x + 1). | The first pair gives x squared, times x plus one. {BR} The second gives four, times x plus one. | Each pair factors |
| 3 | The same (x + 1) appears twice. | The same x plus one appears in both. | Both (x + 1) glow |
| 4 | (x² + 4)(x + 1). | Pull it out: x squared plus four, times x plus one. | Binomial slides out front |
| 5 | Watch the sign: −9x + 18 = −9(x − 2). | Watch the sign on the second pair: {BR} minus nine x plus eighteen is negative nine, times x minus two. | Example 15(b); the −9 highlighted |
| 6 | (x² − 9)(x − 2) = (x − 3)(x + 3)(x − 2). | That gives x squared minus nine, times x minus two, {BR} and x squared minus nine splits again: x minus three, times x plus three. | Final factoring-completely step |
| Card | Pairs that share a binomial. | Group into pairs, {BR} and look for the binomial they share. | Card |

---

## Optional Instagram posts (1080×1350, same template as `post_roots.py`)

1. **"10 Formulas to Know"**: the 5 special products plus the 5 special factoring formulas, in two columns, each with a book example.
2. **"How to Factor Anything"**: a decision flowchart. Common factor? Then by number of terms: 2 terms → difference of squares or sum/difference of cubes; 3 terms → perfect square or trinomial; 4 terms → grouping. Then repeat.

Both need the Ox watermark bottom-right (`watermark(FW, FH, width=0.85, inset=0.3)`).

---

## Checklist before handing back

- [ ] 14 scene files render without errors, one at a time (no parallel renders).
- [ ] Every video is 35–55 s. Storyboards show no collisions, overflow, or ghost copies.
- [ ] Every subtitle card is at most 2 lines, and the spoken text has no symbols ElevenLabs could misread.
- [ ] Each series has a `<SERIES>_VOICEOVER.md` doc (via `tools/export_scripts.py`).
- [ ] README updated with the new tables.
- [ ] Audio sync (HANDOFF §7) is a separate task. Don't block on it.
