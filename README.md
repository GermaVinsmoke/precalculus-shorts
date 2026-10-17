# Integer Exponents shorts

Manim Community scenes for three 9:16 shorts (YouTube Shorts / Instagram Reels).

| File | Scene | Concept |
|---|---|---|
| `v1_notation.py` | `V1ExponentialNotation` | aⁿ = n factors of a; (−3)⁴ vs −3⁴ |
| `v2_product_rule.py` | `V2ProductRule` | aᵐ·aⁿ = aᵐ⁺ⁿ by counting factors |
| `v3_zero_negative.py` | `V3ZeroNegative` | a⁰ = 1, a⁻ⁿ = 1/aⁿ from the product rule |

Series 2, Laws of Exponents (narrated):

| File | Scene | Concept |
|---|---|---|
| `laws1_quotient.py` | `L1QuotientRule` | Law 2: aᵐ/aⁿ = aᵐ⁻ⁿ (cancelling pairs) |
| `laws2_power_of_power.py` | `L2PowerOfPower` | Law 3: (aᵐ)ⁿ = aᵐⁿ (grid of groups) |
| `laws3_product_quotient.py` | `L3ProductQuotient` | Laws 4 & 5 (factors regrouping) |
| `laws4_negative_fractions.py` | `L4NegativeFractions` | Laws 6 & 7 (flip, hop across the bar) |
| `laws5_together.py` | `L5PuttingItTogether` | Example 4(a) + all seven laws |

Narrated scenes use `self.say(line(subtitle, spoken), anims=..., steps=...)`. Every render writes
`build/<Scene>.voiceover.txt` (ElevenLabs-ready) and `build/<Scene>.srt`, so the script, subtitles and
animation can't drift apart. `tools/export_scripts.py` collects them into `LAWS_VOICEOVER.md`.

Series 3, Scientific Notation (narrated, logo watermark bottom-right):

| File | Scene | Concept |
|---|---|---|
| `sci1_what.py` | `S1WhatIsIt` | x = a × 10ⁿ; the decimal point hops while the exponent counts |
| `sci2_convert.py` | `S2Converting` | Decimal ↔ scientific (Examples 6, 7) and calculator "E" |
| `sci3_calculate.py` | `S3Calculating` | Example 8: numbers lane × powers-of-ten lane, significant figures |

`sci_common.py` has `DecimalRow` (digits on slots with a hopping decimal point and a live `× 10^k`
counter). The watermark comes from `assets/logo.png` (background removed from `assets/logo_source.webp`).

Series 4, Radicals (narrated, watermarked):

| File | Scene | Concept |
|---|---|---|
| `rad1_what.py` | `R1WhatIsARoot` | Principal root, square/cube geometry, nth roots, even vs odd |
| `rad2_abs.py` | `R2AbsoluteTrap` | √(x²) = \|x\| with a folding number line; ⁿ√(aⁿ) for even/odd n |
| `rad3_simplify.py` | `R3Simplifying` | Product property; groups of n factors escape the root; Example 9 |
| `rad4_combine.py` | `R4Combining` | √(a+b) ≠ √a + √b (3-4-5 triangle); like radicals; Example 10(a) |

`rad_common.py` has `rt()`/`rtex()`: radicals as separate MathTex parts ([index, √, bar]) so the √ sign can
be animated and the index coloured like an exponent.

Series 5, Rational Exponents (narrated, watermarked):

| File | Scene | Concept |
|---|---|---|
| `rat1_meaning.py` | `Q1WhatItMeans` | 9^(1/2): two equal half-steps of ×3; a^(1/n) = ⁿ√a; Example 11(c) |
| `rat2_power_root.py` | `Q2PowerAndRoot` | a^(m/n): bottom = root, top = power; root-first vs power-first race; 4^(3/2) |
| `rat3_translate.py` | `Q3Translating` | Radicals → exponents; 1/2 + 1/3 = 5/6 pies; Example 13(b), (c) |

Series 6, Rationalizing the Denominator (narrated, watermarked):

| File | Scene | Concept |
|---|---|---|
| `ratz1_disguised_one.py` | `Z1DisguisedOne` | 1/√2 = √2/2; multiply by √a/√a = 1; √2·√2 = 2 square; Example 14(a) |
| `ratz2_missing_piece.py` | `Z2MissingPiece` | Exponent meter fills to n; Example 14(b), (c) |

Section 1.3, Polynomials (narrated, watermarked):

| File | Scene | Concept |
|---|---|---|
| `poly1_what.py` | `P1WhatIsAPolynomial` | Monomial axᵏ; exponent scanner; √x + 10 and fractions fail; mono/bi/trinomial |
| `poly2_reading.py` | `P2ReadingAPolynomial` | Term tiles, coefficients with signs, degree = highest exponent; x⁸ + 5x, 6 = 6x⁰ |
| `poly3_terms_factors.py` | `P3TermsVsFactors` | Added vs multiplied; ax + 2ay = a(x + 2y); multiply back to check |

`poly_common.py` has `poly()`: one MathTex (correct sign spacing) with `.terms` groups for tiles.

Section 1.3, Adding & Subtracting Polynomials (narrated, watermarked):

| File | Scene | Concept |
|---|---|---|
| `add1_like_terms.py` | `A1LikeTerms` | x² + x ≠ x³ (algebra tiles); 5x⁷ + 3x⁷ = 8x⁷; Example 1(a) sorted into bins |
| `add2_minus_sign.py` | `A2MinusSign` | Only-first-sign mistake; −(b + c) = −b − c wave; Example 1(b), x³ cancels |

Instagram posts (1080×1350): `post_seven_laws.py`, `post_billion.py`, `post_roots.py`, `post_translate.py`, `post_polynomial.py`, `post_like_terms.py`; render with
`--config_file post.cfg -s`. Finished images are in `exports/`.

`common.py` holds the shared look: palette, safe zones, caption system, header, key-idea card.
`SCRIPTS.md` has the timed caption scripts.

## Setup (macOS)

Needs Homebrew `cairo`, `pango`, `ffmpeg` and a LaTeX install (MacTeX/BasicTeX).

```bash
python3 -m venv .venv
PKG_CONFIG_PATH="/opt/homebrew/lib/pkgconfig:/opt/homebrew/share/pkgconfig:/opt/homebrew/Library/Homebrew/os/mac/pkgconfig/$(sw_vers -productVersion | cut -d. -f1)" .venv/bin/pip install manim
```

## Render

Final (1080×1920, 60 fps — defaults from `manim.cfg`):

```bash
.venv/bin/manim render v1_notation.py V1ExponentialNotation
```

Fast preview (540×960, 30 fps) and storyboard sheet:

```bash
.venv/bin/manim render -r 540,960 --fps 30 v1_notation.py V1ExponentialNotation
.venv/bin/python tools/storyboard.py V1ExponentialNotation media/videos/v1_notation/960p30/V1ExponentialNotation.mp4
```

## Editing tips

- Caption text: the `self.cap(...)` calls. Each caption is held at least 2.5–3.8 s (by word count); long lines wrap to two balanced lines automatically, and more than two lines raises an error.
- Colour words in captions with `B()` (base), `E()` (exponent), `R()` (result), `W()` (warning); superscripts with `sup()`.
- Keep math inside the zone: `fit_zone()` scales a block to fit the space between the header and the captions.
