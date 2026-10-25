# Integer Exponents shorts

Manim Community scenes for three 9:16 shorts (YouTube Shorts / Instagram Reels).

## Source layout

- `videos/common.py` — global design system and narrated-scene framework.
- `videos/<series>/` — video scenes and their series-specific shared helpers.
- `posts/` — 1080×1350 Instagram post scenes.
- `tools/` — storyboard, script-export, and build-path utilities.
- `assets/` — backgrounds and watermark artwork.
- `book/` — read-only source book PDFs and related reference material.
- `build/` — rendered videos, storyboards, scripts, subtitles, and social copy.

Only final deliverables for Parts 4–7 are currently retained. Earlier published outputs and Manim's intermediate `media/` cache were removed to save space; their Python scenes remain available for regeneration.

Render commands are run from the repository root. Scene files support both package imports and Manim's direct file loading.

| File | Scene | Concept |
|---|---|---|
| `videos/integer_exponents/v1_notation.py` | `V1ExponentialNotation` | aⁿ = n factors of a; (−3)⁴ vs −3⁴ |
| `videos/integer_exponents/v2_product_rule.py` | `V2ProductRule` | aᵐ·aⁿ = aᵐ⁺ⁿ by counting factors |
| `videos/integer_exponents/v3_zero_negative.py` | `V3ZeroNegative` | a⁰ = 1, a⁻ⁿ = 1/aⁿ from the product rule |

Series 2, Laws of Exponents (narrated):

| File | Scene | Concept |
|---|---|---|
| `videos/laws_of_exponents/laws1_quotient.py` | `L1QuotientRule` | Law 2: aᵐ/aⁿ = aᵐ⁻ⁿ (cancelling pairs) |
| `videos/laws_of_exponents/laws2_power_of_power.py` | `L2PowerOfPower` | Law 3: (aᵐ)ⁿ = aᵐⁿ (grid of groups) |
| `videos/laws_of_exponents/laws3_product_quotient.py` | `L3ProductQuotient` | Laws 4 & 5 (factors regrouping) |
| `videos/laws_of_exponents/laws4_negative_fractions.py` | `L4NegativeFractions` | Laws 6 & 7 (flip, hop across the bar) |
| `videos/laws_of_exponents/laws5_together.py` | `L5PuttingItTogether` | Example 4(a) + all seven laws |

Narrated scenes use `self.say(line(subtitle, spoken), anims=..., steps=...)`. Every render writes
`build/<Scene>.voiceover.txt` (ElevenLabs-ready) and `build/<Scene>.srt`, so the script, subtitles and
animation can't drift apart. `tools/export_scripts.py` collects them into `LAWS_VOICEOVER.md`.

Series 3, Scientific Notation (narrated, logo watermark bottom-right):

| File | Scene | Concept |
|---|---|---|
| `videos/scientific_notation/sci1_what.py` | `S1WhatIsIt` | x = a × 10ⁿ; the decimal point hops while the exponent counts |
| `videos/scientific_notation/sci2_convert.py` | `S2Converting` | Decimal ↔ scientific (Examples 6, 7) and calculator "E" |
| `videos/scientific_notation/sci3_calculate.py` | `S3Calculating` | Example 8: numbers lane × powers-of-ten lane, significant figures |

`videos/scientific_notation/sci_common.py` has `DecimalRow` (digits on slots with a hopping decimal point and a live `× 10^k`
counter). The watermark comes from `assets/logo.png` (background removed from `assets/logo_source.webp`).

Series 4, Radicals (narrated, watermarked):

| File | Scene | Concept |
|---|---|---|
| `videos/radicals/rad1_what.py` | `R1WhatIsARoot` | Principal root, square/cube geometry, nth roots, even vs odd |
| `videos/radicals/rad2_abs.py` | `R2AbsoluteTrap` | √(x²) = \|x\| with a folding number line; ⁿ√(aⁿ) for even/odd n |
| `videos/radicals/rad3_simplify.py` | `R3Simplifying` | Product property; groups of n factors escape the root; Example 9 |
| `videos/radicals/rad4_combine.py` | `R4Combining` | √(a+b) ≠ √a + √b (3-4-5 triangle); like radicals; Example 10(a) |

`videos/radicals/rad_common.py` has `rt()`/`rtex()`: radicals as separate MathTex parts ([index, √, bar]) so the √ sign can
be animated and the index coloured like an exponent.

Series 5, Rational Exponents (narrated, watermarked):

| File | Scene | Concept |
|---|---|---|
| `videos/rational_exponents/rat1_meaning.py` | `Q1WhatItMeans` | 9^(1/2): two equal half-steps of ×3; a^(1/n) = ⁿ√a; Example 11(c) |
| `videos/rational_exponents/rat2_power_root.py` | `Q2PowerAndRoot` | a^(m/n): bottom = root, top = power; root-first vs power-first race; 4^(3/2) |
| `videos/rational_exponents/rat3_translate.py` | `Q3Translating` | Radicals → exponents; 1/2 + 1/3 = 5/6 pies; Example 13(b), (c) |

Series 6, Rationalizing the Denominator (narrated, watermarked):

| File | Scene | Concept |
|---|---|---|
| `videos/rationalizing/ratz1_disguised_one.py` | `Z1DisguisedOne` | 1/√2 = √2/2; multiply by √a/√a = 1; √2·√2 = 2 square; Example 14(a) |
| `videos/rationalizing/ratz2_missing_piece.py` | `Z2MissingPiece` | Exponent meter fills to n; Example 14(b), (c) |

Section 1.3, Polynomials (narrated, watermarked):

| File | Scene | Concept |
|---|---|---|
| `videos/polynomials/poly1_what.py` | `P1WhatIsAPolynomial` | Monomial axᵏ; exponent scanner; √x + 10 and fractions fail; mono/bi/trinomial |
| `videos/polynomials/poly2_reading.py` | `P2ReadingAPolynomial` | Term tiles, coefficients with signs, degree = highest exponent; x⁸ + 5x, 6 = 6x⁰ |
| `videos/polynomials/poly3_terms_factors.py` | `P3TermsVsFactors` | Added vs multiplied; ax + 2ay = a(x + 2y); multiply back to check |

`videos/polynomials/poly_common.py` has `poly()`: one MathTex (correct sign spacing) with `.terms` groups for tiles.

Section 1.3, Multiplying Algebraic Expressions (narrated, watermarked):

| File | Scene | Concept |
|---|---|---|
| `videos/multiplying/mult1_foil.py` | `M1FOIL` | Example 2: (2x + 1)(3x − 5); four products in an area model, then combine like terms |
| `videos/multiplying/mult2_distribute.py` | `M2Distribute` | Example 3: distribute 2x and 3 over a trinomial, line up partial products by power |

`videos/multiplying/mult_common.py` provides `MultScene` and the reusable 2×2 `area_model()` grid. Part 3 has already been published, so its generated videos, storyboards, subtitles, social copy, and matching post were removed; they can be regenerated from the retained Python scenes.

For each new short, add a `<Scene>_social.md` in its part's build folder with a YouTube Shorts title and an Instagram Reel caption. Number titles sequentially as `[Precalculus 26]`, `[Precalculus 27]`, etc. When a section has a strong standalone visual, also create a matching 1080×1350 Instagram post and a `<PostScene>_caption.md` in the same build folder without waiting for a separate request.

Section 1.3, Special Product Formulas (narrated, watermarked):

| File | Scene | Concept |
|---|---|---|
| `videos/special_products/sprod1_square.py` | `SP1SquareOfSum` | Example 4(a): a square tiled into a², b² and two ab rectangles; (3x + 5)² |
| `videos/special_products/sprod2_sum_difference.py` | `SP2SumTimesDifference` | Example 5(a, b): middle terms cancel; conjugates and the x + y block |
| `videos/special_products/sprod3_cubes.py` | `SP3Cubes` | Example 4(b): 1–3–3–1 and alternating signs for (x² − 2)³ |

`videos/special_products/sprod_common.py` contains `SpecialScene` and the square-tiling helper. Full-resolution videos, storyboards, scripts, subtitles, numbered social copy (`[Precalculus 28]`–`[Precalculus 30]`), and the matching `SquareOfSumPost.png` / `SquareOfSumPost_caption.md` are in `build/part_4_special_products/`.

Section 1.3, Factoring (narrated, watermarked):

| File | Scene | Concept |
|---|---|---|
| `videos/factoring/fact1_gcf.py` | `F1CommonFactor` | Example 6(a–c): greatest common factors, including an entire binomial |
| `videos/factoring/fact2_trinomial.py` | `F2SumAndProduct` | Examples 7 and 9(a): multiply to c, add to b; pair search |
| `videos/factoring/fact3_trial_error.py` | `F3TrialAndError` | Examples 8 and 9(b): test outer + inner; substitute a repeated block |

`videos/factoring/fact_common.py` provides `FactorScene` and the reusable pair-search panel. All full-resolution videos, storyboards, scripts, social copy (`[Precalculus 31]`–`[Precalculus 33]`), and `FactorPairSearchPost.png` / `FactorPairSearchPost_caption.md` are together in `build/part_5_factoring/`.

Section 1.3, Special Factoring Formulas (narrated, watermarked):

| File | Scene | Concept |
|---|---|---|
| `videos/special_factoring/sfact1_diff_squares.py` | `SF1DifferenceOfSquares` | Example 10(a, b): remove a square and rearrange the L-shape; blocks and sum-of-squares caveat |
| `videos/special_factoring/sfact2_perfect_square.py` | `SF2PerfectSquare` | Example 11(a, b): check the middle term, then assemble tiles into a square |
| `videos/special_factoring/sfact3_cubes.py` | `SF3Cubes` | Example 12(a, b): sums and differences of cubes with the SOAP sign mnemonic |

`videos/special_factoring/sfact_common.py` holds `SpecialFactorScene`, square-cut and algebra-tile geometry, and cube formulas. Videos, storyboards, subtitles, `SPECIAL_FACTORING_VOICEOVER.md`, social copy (`[Precalculus 34]`–`[Precalculus 36]`), and `SpecialFactoringPost.png` / `SpecialFactoringPost_caption.md` are in `build/part_6_special_factoring/`.

Section 1.3, Factor Completely (Parts 7–8, narrated, watermarked):

| File | Scene | Concept |
|---|---|---|
| `videos/factor_completely/fcomp1_tree.py` | `FC1FactorTree` | Example 13(a, b): GCF first, repeated differences of squares, and a factor tree whose prime leaves form the final answer |
| `videos/factor_completely/fcomp2_fractional.py` | `FC2FractionalExponents` | Original examples: pull out the smallest fractional exponent; use exponent distances to find the leftover powers |
| `videos/factor_completely/fcomp3_grouping.py` | `FC3Grouping` | Example 15(a, b): group four terms into pairs, pull out the shared binomial, then keep factoring |

`videos/factor_completely/fcomp_common.py` provides `CompleteScene` and compact factor-tree nodes, branches, and prime-leaf highlighting. Full-resolution videos, storyboards, scripts, subtitles, social copy (`[Precalculus 37]`–`[Precalculus 39]`), and the `FactorAnythingPost.png` decision flowchart with its caption are in `build/part_7_factor_completely/`. The next video number is **40**.

Section 1.3, Adding & Subtracting Polynomials (narrated, watermarked):

| File | Scene | Concept |
|---|---|---|
| `videos/add_subtract/add1_like_terms.py` | `A1LikeTerms` | x² + x ≠ x³ (algebra tiles); 5x⁷ + 3x⁷ = 8x⁷; Example 1(a) sorted into bins |
| `videos/add_subtract/add2_minus_sign.py` | `A2MinusSign` | Only-first-sign mistake; −(b + c) = −b − c wave; Example 1(b), x³ cancels |

Instagram posts (1080×1350): `posts/post_seven_laws.py`, `posts/post_billion.py`, `posts/post_roots.py`, `posts/post_translate.py`, `posts/post_polynomial.py`, `posts/post_like_terms.py`; render with
`--config_file post.cfg -s`. Previously published exports were removed, but all post source scenes remain. New posts: `posts/post_foil_grid.py` (`FOILGridPost`, Part 3), `posts/post_square_of_sum.py` (`SquareOfSumPost`, Part 4), `posts/post_factor_pair_search.py` (`FactorPairSearchPost`, Part 5), `posts/post_special_factoring.py` (`SpecialFactoringPost`, Part 6), and `posts/post_factor_completely.py` (`FactorAnythingPost`, Part 7). Retained Part 4–7 PNGs and caption markdown files live in their matching build folders.

`videos/common.py` holds the shared look: palette, safe zones, caption system, header, and key-idea card.

## Setup (macOS)

Needs Homebrew `cairo`, `pango`, `pkg-config`, `ffmpeg`, `texlive` and `dvisvgm` (or another LaTeX install). Python 3.12 is pinned in `.python-version`.

```bash
brew install cairo pango pkg-config ffmpeg dvisvgm
uv venv --python 3.12
uv pip install --python .venv/bin/python -r codex-handoff/requirements.txt
```

## Render

For Part 3, render the final 1080×1920, 60 fps videos **one at a time**, directly into their build folder. No low-resolution copies are needed:

```bash
mkdir -p build/part_3_multiplying
.venv/bin/manim render -o "$PWD/build/part_3_multiplying/M1FOIL.mp4" videos/multiplying/mult1_foil.py M1FOIL
.venv/bin/manim render -o "$PWD/build/part_3_multiplying/M2Distribute.mp4" videos/multiplying/mult2_distribute.py M2Distribute
.venv/bin/python tools/storyboard.py M1FOIL build/part_3_multiplying/M1FOIL.mp4
.venv/bin/python tools/storyboard.py M2Distribute build/part_3_multiplying/M2Distribute.mp4
.venv/bin/python tools/export_scripts.py build/part_3_multiplying/MULT_VOICEOVER.md M1FOIL M2Distribute
```

The series base class sets `BUILD_SUBDIR` so `.voiceover.txt`, `.srt` and `.marks.json` also land in that folder. For Part 4, use the same commands with `build/part_4_special_products/`, the `videos/special_products/sprod*.py` files and their scene names. Render the Part 3 matching post into its folder:

```bash
.venv/bin/manim render -s --config_file post.cfg -o "$PWD/build/part_3_multiplying/FOILGridPost.png" posts/post_foil_grid.py FOILGridPost
```

For Parts 4–7, use the same pattern with their respective `build/part_*/` folder, scene source files, and scene names. Render posts with `-s --config_file post.cfg -o "$PWD/build/<part>/<PostScene>.png"`.

For earlier scenes, the original render command still works:

```bash
.venv/bin/manim render videos/integer_exponents/v1_notation.py V1ExponentialNotation
```

## Editing tips

- Caption text: the `self.cap(...)` calls. Each caption is held at least 2.5–3.8 s (by word count); long lines wrap to two balanced lines automatically, and more than two lines raises an error.
- Colour words in captions with `B()` (base), `E()` (exponent), `R()` (result), `W()` (warning); superscripts with `sup()`.
- Keep math inside the zone: `fit_zone()` scales a block to fit the space between the header and the captions.
