# Math Shorts: Handoff

Everything used to make the vertical math explainer videos (YouTube Shorts / Instagram Reels) and the matching Instagram posts. The content comes from Stewart's *Precalculus*, Section 1.2 (Exponents and Radicals) and Section 1.3 (Algebraic Expressions). Everything is built with **Manim Community** (Python) in a 3Blue1Brown-inspired style.

- `theme.json`: machine-readable colours, fonts, sizes, safe zones and the watermark spec
- `requirements.txt`: Python and system dependencies
- `project/`: **the complete, runnable source**. Render from inside this folder.
- `scripts/`: voiceover scripts (ElevenLabs-ready) and subtitles for every narrated video
- Historical `reference/` media was removed after publication to save space; regenerate previews and storyboards from the retained Python scenes when needed.

---

## 1. Status

| Step | State |
|---|---|
| Concepts extracted, video plans agreed | Done for all parts below |
| Scenes coded and checked via storyboards and low-res previews | **Done** (25 videos, 6 posts) |
| Voiceover scripts (generated from the scenes) | **Done**, in `scripts/` |
| Voiceovers recorded in ElevenLabs | **Not yet**. The owner generates these. |
| Re-timing animation to the real audio + muxing audio | **Not implemented yet** (spec in §7) |
| Final 1080×1920 @ 60 fps renders | **Not yet** (one command per scene once audio is synced) |

---

## 2. Setup (macOS)

```bash
cd project
python3.12 -m venv .venv
# pycairo needs Homebrew's cairo on pkg-config's path. If MacPorts' pkg-config wins, also add Homebrew's macOS .pc dir:
export PKG_CONFIG_PATH="/opt/homebrew/lib/pkgconfig:/opt/homebrew/share/pkgconfig:/opt/homebrew/Library/Homebrew/os/mac/pkgconfig/$(sw_vers -productVersion | cut -d. -f1)"
.venv/bin/pip install -r ../requirements.txt
```

You also need `ffmpeg` and a LaTeX distribution with `latex` and `dvisvgm` on PATH (TeX Live 2025 was used). The caption font is **Avenir Next**, which ships with macOS. On Linux, install it or change `FONT` in `videos/common.py`.

---

## 3. Rendering

All commands run from `project/`. `manim.cfg` sets the video canvas (1080×1920, 60 fps, 9×16 frame units). `post.cfg` sets the post canvas (1080×1350).

```bash
# Fast preview (540x960, 30 fps)
.venv/bin/manim render -r 540,960 --fps 30 --disable_caching videos/radicals/rad1_what.py R1WhatIsARoot

# Final (1080x1920, 60 fps, from manim.cfg)
.venv/bin/manim render videos/radicals/rad1_what.py R1WhatIsARoot

# Storyboard sheet: one frame per beat → build/storyboard/<Scene>_storyboard.png
.venv/bin/python tools/storyboard.py R1WhatIsARoot media/videos/rad1_what/960p30/R1WhatIsARoot.mp4

# Collect generated voiceover + subtitles for several scenes into one markdown doc
.venv/bin/python tools/export_scripts.py OUT.md R1WhatIsARoot R2AbsoluteTrap

# Instagram post (still image)
.venv/bin/manim render -s --config_file post.cfg posts/post_roots.py RootRulesPost
```

- **Render scenes one at a time.** Parallel renders race on Manim's shared LaTeX cache (`media/Tex`) and fail with `FileNotFoundError`.
- Every render of a narrated scene writes `build/<Scene>.voiceover.txt`, `build/<Scene>.srt` and `build/<Scene>.marks.json` (beat times and key-frame times used by the storyboard tool).

---

## 4. Video inventory

The header shown in each video is `TOPIC · n / N`. Durations are for the preview renders, with speech timing estimated at 150 words per minute.

| Series (header) | File | Scene class | Concept | Length |
|---|---|---|---|---|
| **INTEGER EXPONENTS** (captions only, no voiceover, no watermark) | `videos/integer_exponents/v1_notation.py` | `V1ExponentialNotation` | aⁿ = n factors; (−3)⁴ vs −3⁴ | 54.6 s |
| | `videos/integer_exponents/v2_product_rule.py` | `V2ProductRule` | aᵐ·aⁿ = aᵐ⁺ⁿ by counting factors | 37.4 s |
| | `videos/integer_exponents/v3_zero_negative.py` | `V3ZeroNegative` | a⁰ = 1, a⁻ⁿ = 1/aⁿ | 47.6 s |
| **LAWS OF EXPONENTS** (narrated, no watermark) | `videos/laws_of_exponents/laws1_quotient.py` | `L1QuotientRule` | Law 2, cancelling pairs | 50.9 s |
| | `videos/laws_of_exponents/laws2_power_of_power.py` | `L2PowerOfPower` | Law 3, grid of groups | 47.1 s |
| | `videos/laws_of_exponents/laws3_product_quotient.py` | `L3ProductQuotient` | Laws 4 & 5, (a+b)² warning | 56.8 s |
| | `videos/laws_of_exponents/laws4_negative_fractions.py` | `L4NegativeFractions` | Laws 6 & 7, flip and hop | 53.3 s |
| | `videos/laws_of_exponents/laws5_together.py` | `L5PuttingItTogether` | Example 4(a), all 7 laws | 39.2 s |
| **SCIENTIFIC NOTATION** (narrated, watermark) | `videos/scientific_notation/sci1_what.py` | `S1WhatIsIt` | a × 10ⁿ, hopping decimal point | 54.8 s |
| | `videos/scientific_notation/sci2_convert.py` | `S2Converting` | Decimal ↔ scientific, calculator E | 54.0 s |
| | `videos/scientific_notation/sci3_calculate.py` | `S3Calculating` | Example 8, two lanes, significant figures | 51.7 s |
| **RADICALS** | `videos/radicals/rad1_what.py` | `R1WhatIsARoot` | Principal root, square/cube geometry | 55.7 s |
| | `videos/radicals/rad2_abs.py` | `R2AbsoluteTrap` | √(x²) = \|x\|, folding number line | 51.8 s |
| | `videos/radicals/rad3_simplify.py` | `R3Simplifying` | Product property, factors escape the root | 54.5 s |
| | `videos/radicals/rad4_combine.py` | `R4Combining` | √(a+b) ≠ √a+√b (3-4-5 triangle), like radicals | 55.8 s |
| **RATIONAL EXPONENTS** | `videos/rational_exponents/rat1_meaning.py` | `Q1WhatItMeans` | 9^(1/2) staircase, a^(1/n) = ⁿ√a | 53.7 s |
| | `videos/rational_exponents/rat2_power_root.py` | `Q2PowerAndRoot` | Bottom = root, top = power; race | 55.6 s |
| | `videos/rational_exponents/rat3_translate.py` | `Q3Translating` | Radicals → exponents, fraction pies | 51.0 s |
| **RATIONALIZING** | `videos/rationalizing/ratz1_disguised_one.py` | `Z1DisguisedOne` | Multiply by √a/√a = 1 | 49.0 s |
| | `videos/rationalizing/ratz2_missing_piece.py` | `Z2MissingPiece` | Exponent meter fills to n | 53.1 s |
| **POLYNOMIALS** (Section 1.3) | `videos/polynomials/poly1_what.py` | `P1WhatIsAPolynomial` | Exponent scanner, mono/bi/tri | 47.5 s |
| | `videos/polynomials/poly2_reading.py` | `P2ReadingAPolynomial` | Terms, coefficients, degree | 53.0 s |
| | `videos/polynomials/poly3_terms_factors.py` | `P3TermsVsFactors` | ax + 2ay = a(x + 2y) | 42.1 s |
| **ADD & SUBTRACT** | `videos/add_subtract/add1_like_terms.py` | `A1LikeTerms` | Algebra tiles, sort into bins | 55.0 s |
| | `videos/add_subtract/add2_minus_sign.py` | `A2MinusSign` | The minus flips every sign | 38.3 s |

**Instagram post sources** (1080×1350; historical rendered PNGs were removed after publication):

| File | Scene |
|---|---|
| `posts/post_seven_laws.py` | `SevenLawsPost` (no watermark) |
| `posts/post_billion.py` | `BillionPost` |
| `posts/post_roots.py` | `RootRulesPost` |
| `posts/post_translate.py` | `TranslatorPost` |
| `posts/post_polynomial.py` | `PolynomialAnatomyPost` |
| `posts/post_like_terms.py` | `LikeTermsPost` |

**Not yet covered from Section 1.3:** multiplying (FOIL, distributing), special product formulas, all factoring (GCF, trinomials, special formulas, factoring completely, fractional exponents, grouping).

---

## 5. Design system

### Colour roles (strict and consistent across every video)

| Role | Hex | Used for |
|---|---|---|
| Base | `#58C4DD` (blue) | bases, variables, radicands, the 10 in a × 10ⁿ |
| Exponent | `#FFD54F` (yellow) | exponents, root indexes, counts/hops, emphasized verbs |
| Result | `#83C167` (green) | answers, correct steps, ✓ |
| Warning | `#FC6255` (red) | traps, wrong answers, ✗ |
| Ink | `#ECEFF4` | default text and math, plain coefficients |
| Muted | `#7D869C` | secondary text, header topic, example rows |
| Card | fill `#141824`, stroke `#2A3042` | key-idea cards, post cards |

The background is a dark radial gradient (`#151A26` glowing to `#0B0D12`), generated by `background_path()` into `assets/bg.png` and `assets/bg_1080x1350.png` with dithering against banding.

### Layout (video frame is 9 × 16 units, 120 px per unit)

- **Safe zone:** avoid the top 15%, bottom 25% and right 12% of the frame, where platform UI sits. Usable area: x ∈ [−3.9, 3.42], y ∈ [−4.0, 5.6], centered at x = −0.24 (`CX`).
- **Header:** `y ≈ 5.15`. Topic in letter-spaced bold muted text, "n / N" in ink, and three short bars (blue, yellow, green) underneath.
- **Math zone:** centered at `MATH_Y = 1.75`, maximum height 4.5 (`fit_zone()` scales blocks down to fit).
- **Caption / subtitle zone:** centered at `CAP_Y = −2.45`. At most 2 lines, with balanced wrapping and a fixed font size (`CAP_FS = 40`). Captions are never shrunk.
- **Watermark** (`assets/logo.png`, the Ox logo with its background removed): bottom-right, 1.05 units wide, 0.32-unit inset, 85% opacity. Enabled per series with `WATERMARK = True`.
- **Math font sizes:** HERO 210, BIG 150, MID 110, SMALL 84. Fractions containing radicals render tall, so use SMALL (84) for them.
- **Ending:** a "key idea" card (`self.card(...)`), then `outro()` fades back to the empty opening frame so the video loops cleanly.

### Content rules used for every video
- **Hook in the first 2 seconds:** a question or a tempting wrong answer.
- **Show why, not just the rule.** Each video has one "signature" visual (cancelling pairs, a hopping decimal point, factors escaping a root, a folding number line, algebra tiles, and so on).
- **One idea per beat**, with each new equation held at least about 2 s.
- **Examples come from the textbook,** cited by example number.
- **35–55 s per video.** If a video runs long, cut a beat rather than speed up the pacing.

---

## 6. Code architecture

| File | Role |
|---|---|
| `videos/common.py` | Palette, layout constants, `tex()`, `label()`, `fit()`, `fit_zone()`, `auto()` (colour a `MathTex` by its parts: exponents yellow, variables/digits blue), `chip()`, background, `watermark()`, `ShortScene` (header, captions, key-idea card, outro), `NarratedScene` (narration-driven beats and subtitles) |
| `videos/scientific_notation/sci_common.py` | `SciScene`, `DecimalRow` (digits on fixed slots, a decimal point that hops along arcs, zeros appearing, and a live `× 10^k` counter) |
| `videos/radicals/rad_common.py` | `RadScene`, `rt(n)` / `rtex(...)` for radicals as separate parts, plus `check()` and `cross()` |
| `videos/rational_exponents/rat_common.py`, `videos/rationalizing/ratz_common.py` | Series base classes. `ratz_common.meter()` is the exponent meter |
| `videos/polynomials/poly_common.py` | `PolyScene`, `ptex()` (coefficients white), `poly(terms)`: one `MathTex` with correct sign spacing plus `.terms` groups for term tiles |
| `videos/add_subtract/add_common.py` | `AddScene`, `algebra_tile()`, `bin_heads()` (the x³ / x² / x / 1 sorting bins) |
| `tools/storyboard.py` | Grabs one frame per beat and builds a contact sheet |
| `tools/export_scripts.py` | Collects `voiceover.txt` and `.srt` files into a markdown document |

### Writing a narrated beat

```python
class R1WhatIsARoot(RadScene):           # RadScene → NarratedScene → ShortScene
    PART = "1 / 4"                        # TOPIC comes from the series class

    def construct(self):
        self.say(
            line(f"So is √9 = ±3?", "So is the square root of nine, plus or minus three?"),  # (subtitle markup, spoken text)
            anims=[FadeIn(q)],            # played while speaking
            steps=[[...], 0.5, lambda: [...]],  # then sequential plays: list = one play, number = wait, lambda = built at that moment
            gap=0.4,                      # silence after the beat (default 0.4 s)
        )
```

- **`line(sub, vo)`:** `sub` is Pango markup for the subtitle. `B()`, `E()`, `R()`, `W()` colour words, and `sup()` makes superscripts. `vo` is what ElevenLabs reads: numbers written as words, with `<break time="0.2s" />` pauses (the `BR` constant).
- **Beat length** is estimated from the spoken words at 2.5 words/s, plus break times and the gap. Each subtitle card shows for its own line's spoken duration.
- **The ElevenLabs script and SRT** are generated from the same `say()` calls, so the script, subtitles and animation can't drift apart.

---

## 7. TODO: sync to real audio (not implemented)

**Workflow:** the owner pastes each `scripts/per-scene/<Scene>.voiceover.txt` into ElevenLabs as one generation and gets one audio file per video. Then:

1. Detect the beats in the audio. The generated script puts one paragraph per beat, separated by a `<break>` equal to that beat's gap. Use silence detection (for example `ffmpeg silencedetect` or `pydub`), or align against the known beat count, to get a `[start, end]` for each beat and for each subtitle line within it.
2. Save the timings as `build/audio/<Scene>.timings.json`.
3. In `NarratedScene.say()`, when timings exist, use the measured durations instead of `speech_time()`: wait until each beat's audio start, set each subtitle card's window from the measured times, and pad with waits until the beat's audio end.
4. Add the audio with Manim's `self.add_sound(path)` at t = 0 in `setup()`, or mux it afterwards with ffmpeg.
5. Render the final videos (1080×1920, 60 fps) and regenerate the SRTs from the measured timings.

Subtitles are already burned into the video, so no separate caption track is needed. Background music is added by the owner inside the Instagram/YouTube apps.

---

## 8. Manim gotchas learned on this project (read before editing)

1. **Don't put `ReplacementTransform`/`Transform` of sub-parts inside a `Succession`.** The replaced parts aren't restructured out of their parent, which leaves "ghost" copies on screen. Put those morphs in `steps` (separate top-level plays). `TransformFromCopy` and `FadeIn` inside a `Succession` are fine.
2. **`.animate` captures state when it's built.** A `steps` entry that animates something changed by an earlier step must be a `lambda: [...]`.
3. **Splitting LaTeX across `MathTex` parts works** (Manim wraps each part in `\special` groups): `"{3", r"\over", "4}"`, `"^{-", "2}"`, `r"\sqrt[3]{", "8}"`. A part made by `rt(n)` holds `[index, √ sign, bar]`; attach closing braces to the last content part, never as an empty part.
4. **Ad-hoc `VGroup(...)` targets** of `ReplacementTransform` are fine at the top level of a play, but not nested inside a `Succession`.
5. **Updater functions must name their parameter `dt`** to be time-based (the subtitle cards rely on this).
6. **Don't stack `Indicate` on a mobject you're recolouring** in the same play. Indicate restores the original colour at the end.
7. **Escape `&` as `&amp;`** in any Pango markup (headers, card titles).
8. **Subtitle wrapping treats coloured spans as unbreakable,** so keep coloured phrases short. More than 2 lines raises an `AssertionError` on purpose.
9. **Build polynomials with `poly(terms)`,** not separate `MathTex` per term. Separate pieces lose TeX's spacing around binary operators.
10. **Fractions containing radicals render much taller than expected.** Check the storyboard and use SMALL_FS.

**Review loop used for every video:** render the preview, build the storyboard sheet, look for collisions, safe-zone violations, ghosts and length outside 35–55 s, fix, and re-render.

---

## 9. ElevenLabs settings used in the scripts

- **Model:** Multilingual v2, Turbo or Flash. These support `<break time="…" />`; on Eleven v3, replace break tags with "…".
- **Settings:** a calm, warm narrator voice. Stability ~50, Similarity ~75, Style 0–15, Speed 0.95.
- **Single letters** are written so they're read as letters ("A to the N", "x to the fourth"). If a letter mispronounces, spell it phonetically ("ay", "en", "see").
- Historical generated script exports were removed after publication. Narrated scenes regenerate `.voiceover.txt` and `.srt` files on render, and `tools/export_scripts.py` rebuilds combined voiceover documents.
- **Integer Exponents (V1–V3)** are captions-only and use the older `cap()` caption API rather than `say()`.

## 10. Source material

The textbook PDF used was `~/Documents/books/output.pdf` (owner's machine). It is not included; ask the owner. Pages used: Section 1.2, pp. 13–24; Section 1.3, pp. 25–33.
