"""Part 4, video 2: conjugates cancel their middle products (Example 5)."""

try:
    from .sprod_common import *
except ImportError:  # Manim loading this file directly
    from sprod_common import *
from videos.radicals.rad_common import rt, rtex


class SP2SumTimesDifference(SpecialScene):
    PART = "2 / 3"

    def construct(self):
        factors = poly([["("], ["x"], ["+", "7"], [")"],
                        ["("], ["x"], ["-", "7"], [")"]], fs=BIG_FS)
        fit(factors).move_to(MATH + UP * 0.8)
        slots = VGroup(*[chip(s).scale(0.73) for s in "FOIL"]).arrange(RIGHT, buff=0.23)
        slots.move_to(MATH + DOWN * 0.85)
        self.say(
            line("(x + 7)(x − 7): four products, only two survive.",
                 f"X plus seven, times X minus seven. {BR} Four products, but only two survive."),
            anims=[FadeIn(factors, shift=UP * 0.3),
                   LaggedStart(*[FadeIn(s, scale=0.8) for s in slots], lag_ratio=0.2, run_time=1.0)],
        )

        expansion = poly([["x", "^{2}"], ["-", "7", "x"], ["+", "7", "x"], ["-", "49"]], fs=MID_FS)
        fit(expansion).move_to(MATH + UP * 0.45)
        answer = poly([["x", "^{2}"], ["-", "49"]], fs=BIG_FS)
        answer.set_color(RES_C)
        answer.move_to(MATH + DOWN * 0.45)
        cancels = VGroup(expansion.terms[1], expansion.terms[2])
        marks = VGroup(*[Cross(term, stroke_color=WARN_C, stroke_width=4) for term in cancels])
        self.say(
            line(f"x{sup('2')} − 7x + 7x − 49: the middle terms {E('cancel')}.",
                 f"Multiply it out: X squared, minus seven X, plus seven X, minus forty-nine. "
                 f"{BR} The middle terms cancel."),
            anims=[FadeOut(VGroup(factors, slots)), FadeIn(expansion, shift=UP * 0.2)],
            steps=[[Create(marks), Circumscribe(cancels, color=EXP_C, run_time=1.0)],
                   [FadeOut(VGroup(expansion, marks), run_time=0.5)],
                   [FadeIn(answer, shift=UP * 0.25, run_time=0.65)]],
        )
        self.play(FadeOut(answer), run_time=0.65)

        rule = ptex("(", "a", "+", "b", ")", "(", "a", "-", "b", ")", "=",
                    "a", "^{2}", "-", "b", "^{2}", fs=MID_FS)
        fit_zone(rule)
        self.say(
            line(f"(a + b)(a − b) = {R('a² − b²')}.",
                 f"That's the rule: {BR} A plus B, times A minus B, is A squared minus B squared."),
            anims=[FadeIn(rule, shift=UP * 0.2)],
            steps=[[Circumscribe(rule[11:], color=RES_C, run_time=1.0)]],
        )
        self.play(FadeOut(rule), run_time=0.6)

        root_pair = rtex("(", "2", "x", "-", rt(), "y}", ")", "(", "2", "x", "+", rt(), "y}", ")",
                         fs=SMALL_FS)
        fit(root_pair).move_to(MATH + UP * 1.2)
        root_answer = poly([["4", "x", "^{2}"], ["-", "y"]], fs=BIG_FS)
        root_answer.set_color(RES_C)
        root_answer.move_to(MATH + DOWN * 0.75)
        tag_a = label("EXAMPLE 5(a)", fs=29, color=MUTED, weight=BOLD)
        tag_a.next_to(root_pair, UP, buff=0.32)
        self.say(
            line(f"Example 5(a): (2x − √y)(2x + √y) = {R('4x² − y')}.",
                 f"With A as two X and B as root Y: {BR} four X squared, minus Y."),
            anims=[FadeIn(root_pair, shift=UP * 0.2), FadeIn(tag_a)],
            steps=[[FadeIn(root_answer, shift=UP * 0.25)]],
        )
        self.play(FadeOut(VGroup(root_pair, root_answer, tag_a)), run_time=0.65)

        hidden = ptex("(", "x", "+", "y", "-", "1", ")", "(", "x", "+", "y", "+", "1", ")",
                      fs=SMALL_FS)
        fit(hidden).move_to(MATH + UP * 1.0)
        boxes = VGroup(*[SurroundingRectangle(hidden[a:b], color=BASE_C, buff=0.1,
                                               corner_radius=0.13, stroke_width=3) for a, b in ((1, 4), (8, 11))])
        a_label = label(f"{B('A = x + y')}", fs=38, weight=BOLD).move_to(MATH + DOWN * 0.65)
        tag_b = label("EXAMPLE 5(b)", fs=29, color=MUTED, weight=BOLD)
        tag_b.next_to(hidden, UP, buff=0.32)
        self.say(
            line(f"Hidden pattern: treat {B('x + y')} as one block A.",
                 f"It can hide: {BR} treat X plus Y as one block."),
            anims=[FadeIn(hidden, shift=UP * 0.2), FadeIn(tag_b)],
            steps=[[Create(boxes), FadeIn(a_label, shift=UP * 0.15)]],
        )

        simplified = ptex("(", "x", "+", "y", ")", "^{2}", "-", "1", fs=SMALL_FS)
        result = poly([["x", "^{2}"], ["+", "2", "x", "y"], ["+", "y", "^{2}"], ["-", "1"]],
                      fs=SMALL_FS)
        result.set_color(RES_C)
        fit_zone(VGroup(simplified, result).arrange(DOWN, buff=0.55))
        self.say(
            line(f"A{sup('2')} − 1 = {R('x² + 2xy + y² − 1')}.",
                 f"Then it's A squared minus one: {BR} X squared, plus two X Y, plus Y squared, minus one."),
            anims=[FadeOut(VGroup(hidden, boxes, a_label, tag_b)), FadeIn(simplified, shift=UP * 0.2)],
            steps=[[FadeIn(result, shift=UP * 0.2)]],
        )
        self.play(FadeOut(VGroup(simplified, result)), run_time=0.65)

        formula = ptex("(", "a", "+", "b", ")", "(", "a", "-", "b", ")", "=",
                        "a", "^{2}", "-", "b", "^{2}", fs=SMALL_FS)
        card = self.card(formula, title="DIFFERENCE OF SQUARES")
        self.say(
            line("Sum times difference = difference of squares.",
                 f"Sum times difference? {BR} The middle cancels, leaving a difference of squares."),
            anims=[FadeIn(card, scale=0.94, run_time=0.9)],
        )
        self.outro()
