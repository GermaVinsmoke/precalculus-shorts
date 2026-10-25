"""Instagram post (1080×1350): FOIL as a four-cell multiplication grid.

render: manim render -s --config_file post.cfg -o <output.png> posts/post_foil_grid.py FOILGridPost
"""

try:
    from .post_roots import FH, FW, MARGIN, text
except ImportError:  # Manim loading this file directly
    from post_roots import FH, FW, MARGIN, text
from videos.multiplying.mult_common import *


class FOILGridPost(Scene):
    def construct(self):
        bg = ImageMobject(str(background_path(1080, 1350)))
        bg.height = FH
        self.add(bg)

        # Header matches the existing 4:5 post template.
        bars = VGroup(*[
            RoundedRectangle(corner_radius=0.03, width=0.5, height=0.08,
                             fill_color=c, fill_opacity=1, stroke_width=0)
            for c in (BASE_C, EXP_C, RES_C)
        ]).arrange(RIGHT, buff=0.1)
        kicker = text("MULTIPLYING · EXAMPLE 2", 17, MUTED, BOLD, spacing=2600)
        title = fit(text(f"FOIL Is a {col('2×2 Grid', EXP_C)}", 59, INK, BOLD), FW - 2 * MARGIN - 0.1)
        subtitle = text("Every term multiplies every term.", 23, MUTED)
        header = VGroup(bars, kicker, title, subtitle).arrange(DOWN, buff=0.19)
        header.move_to([0, FH / 2 - 0.4 - header.height / 2, 0])

        inner_w = FW - 2 * MARGIN
        main = RoundedRectangle(corner_radius=0.3, width=inner_w, height=5.05,
                                fill_color=CARD_FILL, fill_opacity=0.94,
                                stroke_color=CARD_STROKE, stroke_width=2.3)
        main.next_to(header, DOWN, buff=0.36)

        expression = poly([["("], ["2", "x"], ["+", "1"], [")"],
                           ["("], ["3", "x"], ["-", "5"], [")"]], fs=80)
        fit(expression, inner_w - 0.8)
        expression.move_to([0, main.get_top()[1] - 0.60, 0])

        # Row labels are 3x, −5; column labels are 2x, +1.
        # F/O/I/L are deliberately placed in multiplication order, not reading order.
        grid = area_model([["2", "x"], ["+", "1"]], [["3", "x"], ["-", "5"]],
                          center=[0.42, main.get_y() - 0.38, 0], cell_w=2.30, cell_h=1.06)
        cells, top, side = grid
        products = VGroup()
        badges = VGroup()
        entries = [(("6", "x", "^{2}"), "F"), (("+", "3", "x"), "I"),
                   (("-", "10", "x"), "O"), (("-", "5"), "L")]
        for cell, (parts, letter) in zip(cells, entries):
            product = ptex(*parts, fs=69).move_to(cell.get_center() + DOWN * 0.07)
            fit(product, cell.width - 0.22)
            products.add(product)
            badge = Circle(radius=0.15, fill_color=CARD_FILL, fill_opacity=1,
                           stroke_color=EXP_C, stroke_width=2.5)
            tag = text(letter, 17, EXP_C, BOLD).move_to(badge)
            badges.add(VGroup(badge, tag).move_to(cell.get_corner(UL) + RIGHT * 0.23 + DOWN * 0.22))

        mid_label = text("COMBINE THE MIDDLE BOXES", 17, MUTED, BOLD, spacing=1200)
        middle = ptex("-", "10", "x", "+", "3", "x", "=", "-", "7", "x", fs=45)
        middle[-3:].set_color(RES_C)
        middle_block = VGroup(mid_label, middle).arrange(DOWN, buff=0.11)
        fit(middle_block, inner_w - 0.7)
        middle_block.move_to([0, main.get_bottom()[1] + 0.57, 0])

        answer_box = RoundedRectangle(corner_radius=0.25, width=inner_w, height=1.33,
                                      fill_color=CARD_FILL, fill_opacity=0.94,
                                      stroke_color=RES_C, stroke_width=2.5)
        answer_box.next_to(main, DOWN, buff=0.22)
        answer_label = text("FINAL ANSWER", 18, RES_C, BOLD, spacing=2200)
        answer = poly([["6", "x", "^{2}"], ["-", "7", "x"], ["-", "5"]], fs=80)
        answer.set_color(RES_C)
        fit(answer, inner_w - 0.9)
        VGroup(answer_label, answer).arrange(DOWN, buff=0.15).move_to(answer_box)

        wrong = ptex("6", "x", "^{2}", "-", "5", fs=53)
        wrong.set_color(WARN_C)
        warning = VGroup(text("NOT", 18, WARN_C, BOLD), wrong,
                         text("— two products are missing!", 19, MUTED)).arrange(RIGHT, buff=0.17)
        fit(warning, inner_w)
        warning.next_to(answer_box, DOWN, buff=0.35)
        footer = text("FIRST  ·  OUTER  ·  INNER  ·  LAST", 17, MUTED, BOLD, spacing=900)
        footer.move_to([-FW / 2 + MARGIN + footer.width / 2, -FH / 2 + 0.40, 0])
        fit(footer, inner_w - 1.3)

        self.add(header, main, expression, grid, products, badges, middle_block,
                 answer_box, answer_label, answer, warning, footer,
                 watermark(FW, FH, width=0.85, inset=0.3))
