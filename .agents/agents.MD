# AGENTS.md — Precalculus Shorts Production Requirements

## Project purpose

This repository produces polished vertical precalculus explainer videos with Manim Community. The videos are designed for YouTube Shorts and Instagram Reels, with matching voiceover scripts, burned-in subtitles, social copy, storyboards, and occasional Instagram posts.

Read these files before creating or changing a video:

- `README.md` — current inventory, output folders, and render commands.
- `videos/common.py` — shared design system, safe zones, captions, narration timing, cards, and watermark.
- The relevant `*_common.py` file for the series.
- Existing scenes from the immediately preceding series for style and implementation patterns.
- Any applicable specification document in the repository.
- `book/` — the project owner will place the source book PDF and related source material inside `@book/` (the repository's `book/` directory). Read the relevant pages from this directory when planning new content, and do not modify the source files.

Do not modify unrelated existing work or delete previous deliverables.

## Content requirements

1. Teach one clear mathematical idea per video.
2. Start with a question, misconception, or tempting wrong answer within the first two seconds.
3. Include one memorable signature visual that explains why the method works.
4. Show reasoning instead of presenting only a formula or final answer.
5. Keep algebra mathematically correct and verify every factorization by expanding it back out.
6. Use concise language suitable for a calm educational voiceover.
7. Finish with a key-idea card and a clean loop back to the opening frame.
8. If the user requests only one video, create and render only that video. Do not generate the remaining videos until requested.
9. **For every new video, use original examples that are different from the examples used in the book PDF.** The book may guide the concept and method, but its exact numerical or algebraic examples must not be reused.
10. When using an original example, do not label it as a numbered textbook example. A section or concept reference is acceptable.

## Video format

- Orientation: vertical 9:16.
- Final resolution: 1080×1920.
- Final frame rate: 60 fps.
- Preview resolution: 540×960 at 30 fps.
- Target duration: 35–55 seconds.
- Render videos one at a time. Parallel Manim renders can race on the shared LaTeX cache.
- Render final videos directly into the appropriate `build/part_*` directory.
- Do not keep unnecessary low-resolution preview videos in the repository.

## Scene architecture

- Keep the repository root free of Python scene files.
- Place video sources in `videos/<series>/`, including the series-specific `*_common.py` helper.
- Place Instagram post sources in `posts/` and utility scripts in `tools/`.
- Add `__init__.py` to every new Python package directory.
- Keep scenes importable both as packages and through Manim's direct file loading. Follow the existing local-import fallback and project-root bootstrap pattern.
- Use the appropriate narrated series base class. New polynomial/factoring series should normally inherit through `PolyScene`.
- Each series base class must define:
  - `TOPIC` — the header text.
  - `BUILD_SUBDIR` — the matching folder under `build/`.
  - Watermark behavior inherited from `PolyScene`, unless explicitly specified otherwise.
- Every scene must define `PART = "n / N"`.
- Use reusable helpers in a series-level `*_common.py` file when visuals are shared by multiple videos.
- Keep source filenames and scene names descriptive and sequential.
- Build polynomials with `poly(terms)` or `ptex(...)`; do not construct each polynomial term as a separate `MathTex`, because that breaks mathematical sign spacing.

## Narration and subtitles

Every narrated beat must use:

```python
self.say(
    line(subtitle_markup, spoken_text),
    anims=[...],
    steps=[...],
    gap=...,
)
```

Requirements:

- The subtitle and spoken script must come from the same `line()` call so they cannot drift apart.
- Spoken text must be ElevenLabs-ready.
- Write symbols as spoken words: “x squared,” “negative one half,” “minus seven x,” and so on.
- Use `{BR}` / `<break time="0.2s" />` for short intentional pauses.
- Keep each subtitle card to at most two lines.
- Split a long thought into multiple `line()` calls rather than shrinking caption text.
- Use subtitle markup helpers consistently:
  - `B()` for variables, bases, and primary objects.
  - `E()` for exponents, counts, patterns, and emphasized operations.
  - `R()` for correct answers and results.
  - `W()` for mistakes, traps, and warnings.
  - `sup()` for subtitle superscripts.
- Do not put raw mathematical symbols into spoken text when they may be misread by text-to-speech.

Every render must generate:

- `<Scene>.voiceover.txt`
- `<Scene>.srt`
- `<Scene>.marks.json`

After completing a series, regenerate its combined voiceover document with `tools/export_scripts.py`.

## Visual design system

Use the existing palette without changing semantic roles:

| Role | Hex | Usage |
|---|---|---|
| Base | `#58C4DD` | Variables, bases, radicands, primary objects |
| Exponent | `#FFD54F` | Exponents, counts, pattern labels, emphasized operations |
| Result | `#83C167` | Correct answers, completed factors, checks |
| Warning | `#FC6255` | Wrong answers, traps, failed checks |
| Ink | `#ECEFF4` | Coefficients, operators, normal text |
| Muted | `#7D869C` | Secondary labels and annotations |
| Card fill | `#141824` | Cards and panels |
| Card stroke | `#2A3042` | Neutral outlines |

Layout requirements:

- Respect the safe zone defined in `videos/common.py`.
- Keep primary animation and equations inside the math zone.
- Keep subtitles in the caption zone.
- Use `fit()` and `fit_zone()` to prevent horizontal or vertical overflow.
- Use `SMALL_FS` for tall fractions, nested radicals, or long factorizations.
- Do not place important content under the watermark or platform interface areas.
- Use the existing dark radial-gradient background.
- Watermarked series must use `assets/logo.png` through the shared `watermark()` helper.

## Required video structure

A typical short should contain:

1. Hook or misconception.
2. Visual explanation of the governing idea.
3. Worked original example.
4. Check, comparison, or second application when useful.
5. Key-idea card using `self.card(...)`.
6. `self.outro()` for a clean loop.

Avoid overcrowding. If the scene exceeds 55 seconds, remove or combine a beat rather than speeding up every animation.

## Animation rules and Manim pitfalls

- Do not put `ReplacementTransform` or `Transform` of sub-parts inside a `Succession`; this can leave ghost copies.
- Put those transforms in separate top-level `steps` plays.
- Use a `lambda` for a later animation that depends on state changed by an earlier step. `.animate` captures its target state when constructed.
- `TransformFromCopy` and `FadeIn` are safe inside a `Succession`.
- Do not recolor a mobject and apply `Indicate` to it in the same play, because `Indicate` may restore the old color.
- Updater functions that depend on elapsed time must name their second parameter `dt`.
- Escape `&` as `&amp;` in Pango markup.
- Attach LaTeX closing braces to the final content part; do not create empty brace parts.
- Check the storyboard for ghost objects after every preview render.

## Review and validation workflow

For every video:

1. Run `py_compile` on the new or modified source files.
2. Render a 540×960, 30 fps preview.
3. Generate a storyboard with `tools/storyboard.py`.
4. Inspect every storyboard frame for:
   - collisions;
   - overflow;
   - tiny or unreadable math;
   - ghost copies;
   - unsafe placement;
   - incorrect colors;
   - missing labels;
   - subtitle wrapping beyond two lines.
5. Confirm the duration is between 35 and 55 seconds.
6. Fix all issues and rerender the preview if necessary.
7. Render the final 1080×1920, 60 fps video, one scene at a time.
8. Regenerate the storyboard from the final video.
9. Validate the final media with `ffprobe` and an `ffmpeg` decode pass.

Audio synchronization is a separate future step. Do not block visual delivery while waiting for recorded narration.

## Deliverables for each video

Place all generated outputs in the series build folder:

- Final `.mp4` video.
- Storyboard `.png`.
- `.voiceover.txt`.
- `.srt`.
- `.marks.json`.
- `<Scene>_social.md` containing:
  - a YouTube Shorts title;
  - the sequential `[Precalculus N]` number;
  - an Instagram Reel caption;
  - relevant hashtags.

Update `README.md` with the new source file, scene name, concept, build folder, and next social-video number.

The next unused social-video number after the completed Factor Completely series is **40** unless newer work in `README.md` indicates otherwise.

## Instagram post requirements

When requested, or when a series has a strong standalone reference visual, create a matching Instagram post:

- Resolution: 1080×1350.
- Aspect ratio: 4:5.
- Render with `post.cfg` and `-s`.
- Use the same colors, typography, cards, background, and semantic color roles as the videos.
- Include the Ox watermark at bottom-right using:

```python
watermark(FW, FH, width=0.85, inset=0.3)
```

- Keep text large enough to read on a phone.
- Avoid dense paragraphs; prefer a formula sheet, diagram, comparison, or flowchart.
- Save the image and `<PostScene>_caption.md` in the matching series build folder.
- Inspect the rendered PNG at full size before delivery.

## Output and status reporting

When work is complete, report:

- scene names;
- exact output paths;
- video durations;
- resolution and frame rate;
- Instagram-post dimensions, if applicable;
- validation performed;
- any intentionally ungenerated videos.

Do not claim that a video or post was generated unless the final output file exists and has been validated.
