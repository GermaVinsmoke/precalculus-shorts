"""Instagram post (1080×1350): the two missing ab rectangles in (a+b)^2.

render: manim render -s --config_file post.cfg -o <output.png> posts/post_square_of_sum.py SquareOfSumPost
"""

try:
    from .post_roots import FH, FW, MARGIN, text
except ImportError:  # Manim loading this file directly
    from post_roots import FH, FW, MARGIN, text
from videos.special_products.sprod_common import *


class SquareOfSumPost(Scene):
    def construct(self):
        bg = ImageMobject(str(background_path(1080, 1350)))
        bg.height = FH
        self.add(bg)

        bars = VGroup(*[
            RoundedRectangle(corner_radius=0.03, width=0.5, height=0.08,
                             fill_color=c, fill_opacity=1, stroke_width=0)
            for c in (BASE_C, EXP_C, RES_C)
        ]).arrange(RIGHT, buff=0.1)
        kicker = text("SPECIAL PRODUCTS", 17, MUTED, BOLD, spacing=3200)
        title = fit(text(f"Don't Forget the {col('2ab', EXP_C)}", 63, INK, BOLD), FW - 2 * MARGIN - 0.1)
        subtitle = text("A squared sum has four pieces.", 23, MUTED)
        header = VGroup(bars, kicker, title, subtitle).arrange(DOWN, buff=0.2)
        header.move_to([0, FH / 2 - 0.4 - header.height / 2, 0])

        inner_w = FW - 2 * MARGIN
        main = RoundedRectangle(corner_radius=0.3, width=inner_w, height=5.0,
                                fill_color=CARD_FILL, fill_opacity=0.94,
                                stroke_color=CARD_STROKE, stroke_width=2.3)
        main.next_to(header, DOWN, buff=0.35)
        heading = text(f"ONE SQUARE: SIDE {col('a + b', BASE_C)}", 20, MUTED, BOLD, spacing=1100)
        heading.move_to([0, main.get_top()[1] - 0.38, 0])

        square = sum_square(side_a=1.70, side_b=0.75,
                            center=[-1.63, main.get_y() + 0.19, 0])
        regions, region_labels, top_labels, side_labels = square
        regions[1].set_fill(EXP_C, opacity=0.32)
        regions[2].set_fill(EXP_C, opacity=0.32)

        note_box = RoundedRectangle(corner_radius=0.22, width=3.25, height=1.65,
                                    fill_color=CARD_FILL, fill_opacity=0.96,
                                    stroke_color=EXP_C, stroke_width=2.3)
        note_box.move_to([1.9, main.get_y() + 0.25, 0])
        note_title = fit(text("TWO MIDDLE PIECES", 16, EXP_C, BOLD, spacing=650),
                         note_box.width - 0.35)
        note_eq = ptex("a", "b", "+", "a", "b", "=", "2", "a", "b", fs=58)
        note_eq[-3:].set_color(EXP_C)
        fit(note_eq, note_box.width - 0.33)
        VGroup(note_title, note_eq).arrange(DOWN, buff=0.22).move_to(note_box)

        formula = poly([["("], ["a"], ["+", "b"], [")", "^{2}"], ["="],
                        ["a", "^{2}"], ["+", "2", "a", "b"], ["+", "b", "^{2}"]], fs=60)
        formula.terms[-2][1].set_color(EXP_C)
        fit(formula, inner_w - 0.65)
        formula.move_to([0, main.get_bottom()[1] + 0.59, 0])

        answer_box = RoundedRectangle(corner_radius=0.25, width=inner_w, height=1.42,
                                      fill_color=CARD_FILL, fill_opacity=0.94,
                                      stroke_color=RES_C, stroke_width=2.5)
        answer_box.next_to(main, DOWN, buff=0.22)
        example = ptex("(", "x", "+", "5", ")", "^{2}", fs=56)
        result = poly([["x", "^{2}"], ["+", "10", "x"], ["+", "25"]], fs=65)
        result.set_color(RES_C)
        equals = tex("=", fs=56)
        solution = VGroup(example, equals, result).arrange(RIGHT, buff=0.20)
        fit(solution, inner_w - 0.48)
        tag = text("TRY a = x, b = 5", 18, RES_C, BOLD, spacing=900)
        VGroup(tag, solution).arrange(DOWN, buff=0.16).move_to(answer_box)

        wrong = ptex("x", "^{2}", "+", "25", fs=49)
        wrong.set_color(WARN_C)
        warning = VGroup(text("NOT", 18, WARN_C, BOLD), wrong,
                         text("— the middle terms are missing", 18, MUTED)).arrange(RIGHT, buff=0.15)
        fit(warning, inner_w)
        warning.next_to(answer_box, DOWN, buff=0.35)
        footer = text("THE MIDDLE IS TWICE THE PRODUCT.", 17, MUTED, BOLD, spacing=900)
        fit(footer, inner_w - 1.2)
        footer.move_to([-FW / 2 + MARGIN + footer.width / 2, -FH / 2 + 0.40, 0])

        self.add(header, main, heading, square, note_box, note_title, note_eq,
                 formula, answer_box, tag, solution, warning, footer,
                 watermark(FW, FH, width=0.85, inset=0.3))
