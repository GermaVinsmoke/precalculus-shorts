"""Part 3, video 1: every term times every term (Example 2)."""

try:
    from .mult_common import *
except ImportError:  # Manim loading this file directly
    from mult_common import *

BR = '<break time="0.2s" />'


class M1FOIL(MultScene):
    PART = "1 / 2"

    def construct(self):
        product = poly([["("], ["2", "x"], ["+", "1"], [")"],
                        ["("], ["3", "x"], ["-", "5"], [")"]], fs=MID_FS)
        fit(product).move_to(MATH + UP * 1.2)
        wrong = ptex("=", "6", "x", "^{2}", "-", "5", "?", fs=SMALL_FS)
        wrong[1:].set_color(WARN_C)
        wrong.move_to(MATH + DOWN * 0.65)
        example_tag = label("EXAMPLE 2", fs=27, color=MUTED, weight=BOLD)
        example_tag.move_to([CX, 4.55, 0])
        self.say(
            line(f"Is (2x + 1)(3x − 5) just {W('6x² − 5')}?",
                 "Is two x plus one, times three x minus five, just six x squared minus five?"),
            anims=[FadeIn(example_tag), FadeIn(product, shift=UP * 0.25, run_time=0.85),
                   Succession(Wait(0.8), FadeIn(wrong, shift=UP * 0.2, run_time=0.7))],
        )

        grid = area_model([["2", "x"], ["+", "1"]], [["3", "x"], ["-", "5"]],
                          center=MATH + DOWN * 0.45)
        cells, top, side = grid
        self.say(
            line("Picture the product as a rectangle.",
                 f"Picture the product as a rectangle. {BR} Split each side into its terms."),
            anims=[FadeOut(wrong), FadeOut(example_tag), product.animate.move_to(MATH + UP * 2.05)],
            steps=[[LaggedStart(*[DrawBorderThenFill(c) for c in cells], lag_ratio=0.16, run_time=1.25),
                    FadeIn(top, shift=DOWN * 0.18), FadeIn(side, shift=RIGHT * 0.18)]],
        )

        # F = first×first, O = outer, I = inner, L = last.
        order = [(0, 1, 5, ("6", "x", "^{2}"), "F"),
                 (2, 1, 6, ("-", "10", "x"), "O"),
                 (1, 2, 5, ("+", "3", "x"), "I"),
                 (3, 2, 6, ("-", "5"), "L")]
        products, tags, arrows = VGroup(), VGroup(), VGroup()
        steps = []
        for cell_i, left_i, right_i, parts, tag in order:
            result = ptex(*parts, fs=64).move_to(cells[cell_i])
            badge = chip(tag, EXP_C).scale(0.48)
            badge.move_to(cells[cell_i].get_corner(UR) + LEFT * 0.3 + DOWN * 0.26)
            arrow = ArcBetweenPoints(product.terms[left_i].get_bottom(), cells[cell_i].get_top(),
                                     angle=-0.3, color=EXP_C, stroke_width=3)
            products.add(result)
            tags.add(badge)
            arrows.add(arrow)
            steps.append([Create(arrow, run_time=0.55), FadeIn(result, scale=0.8, run_time=0.7),
                          FadeIn(badge, run_time=0.5), Indicate(cells[cell_i], color=EXP_C, run_time=0.7)])
            steps.append([FadeOut(arrow, run_time=0.3)])
        self.say(
            line(f"{E('First, Outer, Inner, Last')}: four boxes.",
                 f"First times first: six x squared. {BR} Outer: minus ten x. "
                 f"{BR} Inner: plus three x. {BR} Last: minus five."),
            steps=steps,
        )

        middle = VGroup(products[1], products[2])
        highlight = VGroup(*[SurroundingRectangle(p, color=EXP_C, buff=0.12,
                                                  corner_radius=0.1, stroke_width=3) for p in middle])
        answer = poly([["6", "x", "^{2}"], ["-", "7", "x"], ["-", "5"]], fs=MID_FS)
        answer.set_color(RES_C)
        fit(answer).move_to(MATH + DOWN * 0.15)
        middle_sum = ptex("-", "10", "x", "+", "3", "x", "=", "-", "7", "x", fs=SMALL_FS)
        middle_sum[-3:].set_color(RES_C)
        fit(middle_sum).move_to(MATH + DOWN * 1.05)
        self.say(
            line(f"The middle boxes are like terms: {E('−10x + 3x')} = {R('−7x')}.",
                 f"The two middle boxes are like terms: {BR} minus ten x plus three x is minus seven x."),
            anims=[Create(highlight), Indicate(products[1], color=EXP_C),
                   Indicate(products[2], color=EXP_C)],
            steps=[[TransformFromCopy(middle, middle_sum, run_time=1.0)],
                   [FadeOut(VGroup(grid, products, tags, highlight, middle_sum, product)),
                    FadeIn(answer, shift=UP * 0.25)]],
        )

        crossed = wrong.copy().move_to(MATH + UP * 1.25)
        crossed[-1].set_opacity(0)
        slash = Cross(crossed, stroke_color=WARN_C, stroke_width=5)
        self.say(
            line(f"The quick answer {W('missed two boxes')}.",
                 "So the quick answer missed two whole boxes."),
            anims=[FadeIn(crossed, shift=UP * 0.15), Create(slash, run_time=0.7)],
        )
        self.play(FadeOut(VGroup(answer, crossed, slash)), run_time=0.65)

        rule = ptex("(", "a", "+", "b", ")", "(", "c", "+", "d", ")",
                    "=", "a", "c", "+", "a", "d", "+", "b", "c", "+", "b", "d", fs=SMALL_FS)
        card = self.card(rule, title="EVERY TERM × EVERY TERM")
        self.say(
            line("Every term times every term.",
                 f"Every term times every term. {BR} FOIL is just a way to not miss one."),
            anims=[FadeIn(card, scale=0.94, run_time=0.9)],
        )
        self.outro()
