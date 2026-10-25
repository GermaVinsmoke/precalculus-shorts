"""Instagram post (1080×1350): find two numbers that multiply to c and add to b.

render: manim render -s --config_file post.cfg -o <output.png> posts/post_factor_pair_search.py FactorPairSearchPost
"""

try:
    from .post_roots import FH, FW, MARGIN, text
except ImportError:  # Manim loading this file directly
    from post_roots import FH, FW, MARGIN, text
from videos.factoring.fact_common import *


class FactorPairSearchPost(Scene):
    def construct(self):
        bg = ImageMobject(str(background_path(1080, 1350)))
        bg.height = FH
        self.add(bg)

        bars = VGroup(*[
            RoundedRectangle(corner_radius=0.03, width=0.5, height=0.08,
                             fill_color=c, fill_opacity=1, stroke_width=0)
            for c in (BASE_C, EXP_C, RES_C)
        ]).arrange(RIGHT, buff=0.1)
        kicker = text("FACTORING · EXAMPLE 7", 17, MUTED, BOLD, spacing=2600)
        title = fit(text(f"Find the {col('Two Numbers', EXP_C)}", 62, INK, BOLD), FW - 2 * MARGIN - 0.1)
        subtitle = text("One product. One sum. One matching pair.", 22, MUTED)
        header = VGroup(bars, kicker, title, subtitle).arrange(DOWN, buff=0.2)
        header.move_to([0, FH / 2 - 0.4 - header.height / 2, 0])

        inner_w = FW - 2 * MARGIN
        main = RoundedRectangle(corner_radius=0.30, width=inner_w, height=5.05,
                                fill_color=CARD_FILL, fill_opacity=0.94,
                                stroke_color=CARD_STROKE, stroke_width=2.3)
        main.next_to(header, DOWN, buff=0.36)
        expression = poly([["x", "^{2}"], ["+", "7", "x"], ["+", "12"]], fs=82)
        fit(expression, inner_w - 0.9)
        expression.move_to([0, main.get_top()[1] - 0.58, 0])

        goals = VGroup(chip("MULTIPLY TO 12", BASE_C), chip("ADD TO 7", EXP_C))
        goals.scale(0.74).arrange(RIGHT, buff=0.3)
        goals.move_to([0, main.get_top()[1] - 1.35, 0])
        headings = VGroup(text("PAIR", 18, MUTED, BOLD, spacing=1200),
                          text("PRODUCT", 18, MUTED, BOLD, spacing=1200),
                          text("SUM", 18, MUTED, BOLD, spacing=1200))
        xs = (-2.55, 0.15, 2.56)
        headings[0].move_to([xs[0], main.get_top()[1] - 1.98, 0])
        headings[1].move_to([xs[1], main.get_top()[1] - 1.98, 0])
        headings[2].move_to([xs[2], main.get_top()[1] - 1.98, 0])

        rows = VGroup()
        for i, (r, s) in enumerate(((1, 12), (2, 6), (3, 4))):
            match = r + s == 7 and r * s == 12
            y = main.get_top()[1] - 2.78 - 0.78 * i
            box = RoundedRectangle(corner_radius=0.17, width=inner_w - 0.6, height=0.68,
                                   fill_color=RES_C if match else CARD_FILL,
                                   fill_opacity=0.13 if match else 0.85,
                                   stroke_color=RES_C if match else CARD_STROKE,
                                   stroke_width=2.4)
            box.move_to([0, y, 0])
            pair = text(f"{r} and {s}", 27, RES_C if match else INK, BOLD)
            product = text(f"{r*s}  ✓", 27, RES_C, BOLD)
            summation = text(f"{r+s}  {'✓' if match else '✗'}", 27,
                             RES_C if match else WARN_C, BOLD)
            for obj, x in zip((pair, product, summation), xs):
                obj.move_to([x, y, 0])
            rows.add(VGroup(box, pair, product, summation))

        answer_box = RoundedRectangle(corner_radius=0.25, width=inner_w, height=1.42,
                                      fill_color=CARD_FILL, fill_opacity=0.94,
                                      stroke_color=RES_C, stroke_width=2.5)
        answer_box.next_to(main, DOWN, buff=0.22)
        result_title = text("3 × 4 = 12    AND    3 + 4 = 7", 19, RES_C, BOLD, spacing=450)
        result = ptex("(", "x", "+", "3", ")", "(", "x", "+", "4", ")", fs=78)
        result.set_color(RES_C)
        fit(result, inner_w - 0.8)
        VGroup(result_title, result).arrange(DOWN, buff=0.16).move_to(answer_box)

        note = text(f"For {col('x² + bx + c', BASE_C)}: multiply to c, add to b.", 20, MUTED)
        fit(note, inner_w)
        note.next_to(answer_box, DOWN, buff=0.36)
        footer = text("THEN MULTIPLY BACK TO CHECK.", 17, MUTED, BOLD, spacing=900)
        fit(footer, inner_w - 1.3)
        footer.move_to([-FW / 2 + MARGIN + footer.width / 2, -FH / 2 + 0.40, 0])

        self.add(header, main, expression, goals, headings, rows, answer_box,
                 result_title, result, note, footer,
                 watermark(FW, FH, width=0.85, inset=0.3))
