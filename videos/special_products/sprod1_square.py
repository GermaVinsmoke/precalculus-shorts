"""Part 4, video 1: why a squared sum has a middle term (Example 4a)."""

try:
    from .sprod_common import *
except ImportError:  # Manim loading this file directly
    from sprod_common import *


class SP1SquareOfSum(SpecialScene):
    PART = "1 / 3"

    def construct(self):
        hook = ptex("(", "x", "+", "5", ")", "^{2}", "=", "x", "^{2}", "+", "25", "?", fs=MID_FS)
        hook[6:].set_color(WARN_C)
        fit(hook).move_to(MATH)
        self.say(
            line(f"Is (x + 5){sup('2')} just x{sup('2')} + 25?",
                 "Is x plus five, squared, equal to x squared plus twenty-five?"),
            anims=[FadeIn(hook, shift=UP * 0.3, run_time=1.0)],
        )

        square = sum_square(center=MATH + DOWN * 0.35)
        tiles, labels, top, side = square
        self.say(
            line(f"Draw a square with side {B('a + b')}.",
                 f"Draw a square with side A plus B. {BR} It splits into four pieces."),
            anims=[FadeOut(hook), LaggedStart(*[DrawBorderThenFill(t) for t in tiles],
                                                    lag_ratio=0.18, run_time=1.5)],
            steps=[[FadeIn(top, shift=DOWN * 0.2), FadeIn(side, shift=RIGHT * 0.2)]],
        )
        self.say(
            line(f"a{sup('2')}, b{sup('2')}, and {E('two ab rectangles')}.",
                 f"A squared, B squared, {BR} and two A B rectangles: the ones people forget."),
            anims=[LaggedStart(*[FadeIn(m, scale=0.8) for m in labels], lag_ratio=0.15, run_time=1.1)],
            steps=[[Indicate(tiles[1], color=EXP_C, run_time=0.9),
                    Indicate(tiles[2], color=EXP_C, run_time=0.9)]],
        )
        self.play(FadeOut(square, shift=UP * 0.3), run_time=0.65)

        plus = poly([["("], ["a"], ["+", "b"], [")", "^{2}"], ["="],
                     ["a", "^{2}"], ["+", "2", "a", "b"], ["+", "b", "^{2}"]], fs=SMALL_FS)
        minus = poly([["("], ["a"], ["-", "b"], [")", "^{2}"], ["="],
                      ["a", "^{2}"], ["-", "2", "a", "b"], ["+", "b", "^{2}"]], fs=SMALL_FS)
        rows = VGroup(plus, minus).arrange(DOWN, buff=0.65)
        fit_zone(rows)
        middle_plus = plus.terms[-2]
        middle_minus = minus.terms[-2]
        middle_plus[1].set_color(EXP_C)
        middle_minus[1].set_color(EXP_C)
        self.say(
            line(f"(a + b){sup('2')} = a{sup('2')} + {E('2ab')} + b{sup('2')}.",
                 f"A plus B, squared, is A squared plus two A B plus B squared. {BR} "
                 "With a minus, the middle term turns negative."),
            anims=[FadeIn(plus, shift=UP * 0.3, run_time=0.9)],
            steps=[[Circumscribe(middle_plus, color=EXP_C, run_time=1.0)],
                   [FadeIn(minus, shift=UP * 0.2, run_time=0.85)],
                   [Circumscribe(middle_minus, color=WARN_C, run_time=0.9)]],
        )
        self.play(FadeOut(rows, shift=UP * 0.3), run_time=0.65)

        wrong = ptex("(", "x", "+", "5", ")", "^{2}", "=", "x", "^{2}", "+", "25", fs=SMALL_FS)
        wrong.set_color(WARN_C)
        correct = poly([["x", "^{2}"], ["+", "10", "x"], ["+", "25"]], fs=MID_FS)
        correct.set_color(RES_C)
        proof = ptex("2", r"\cdot", "x", r"\cdot", "5", "=", "10", "x", fs=SMALL_FS)
        proof[0].set_color(EXP_C)
        proof[-2:].set_color(EXP_C)
        block = fit_zone(VGroup(wrong, correct, proof).arrange(DOWN, buff=0.5))
        cross_wrong = Cross(wrong, stroke_color=WARN_C, stroke_width=4)
        self.say(
            line(f"(x + 5){sup('2')} = {R('x² + 10x + 25')}.",
                 f"So x plus five, squared, is x squared plus ten x plus twenty-five."),
            anims=[FadeIn(wrong, shift=UP * 0.2), Create(cross_wrong)],
            steps=[[FadeIn(correct, shift=UP * 0.2), FadeIn(proof, shift=UP * 0.2)]],
        )
        self.play(FadeOut(VGroup(block, cross_wrong)), run_time=0.65)

        given = ptex("(", "3", "x", "+", "5", ")", "^{2}", fs=BIG_FS)
        answer = poly([["9", "x", "^{2}"], ["+", "30", "x"], ["+", "25"]], fs=MID_FS)
        answer.set_color(RES_C)
        assign = label(f"a = {B('3x')}   ·   b = {B('5')}", fs=36, color=MUTED)
        group = fit_zone(VGroup(given, assign, answer).arrange(DOWN, buff=0.53))
        tag = label("EXAMPLE 4(a)", fs=29, color=MUTED, weight=BOLD).next_to(given, UP, buff=0.25)
        self.say(
            line(f"Example 4(a): (3x + 5){sup('2')} = {R('9x² + 30x + 25')}.",
                 f"With A as three x and B as five: {BR} nine x squared, plus thirty x, plus twenty-five."),
            anims=[FadeIn(given, shift=UP * 0.25), FadeIn(tag)],
            steps=[[FadeIn(assign, shift=UP * 0.15)], [FadeIn(answer, shift=UP * 0.2)]],
        )
        self.play(FadeOut(VGroup(group, tag)), run_time=0.65)

        formula = poly([["("], ["a"], [r"\pm", "b"], [")", "^{2}"], ["="],
                        ["a", "^{2}"], [r"\pm", "2", "a", "b"], ["+", "b", "^{2}"]], fs=SMALL_FS)
        formula.terms[-2][1].set_color(EXP_C)
        card = self.card(formula, title="DON'T FORGET THE MIDDLE")
        self.say(
            line(f"Squaring a sum? Don't forget {E('2ab')}.",
                 f"Squaring a sum? {BR} Don't forget the two A B."),
            anims=[FadeIn(card, scale=0.94, run_time=0.9)],
        )
        self.outro()
