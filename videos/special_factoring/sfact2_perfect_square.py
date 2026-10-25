"""Part 6, video 2: perfect-square trinomials (Example 11)."""

try:
    from .sfact_common import *
except ImportError:  # Manim loading this file directly
    from sfact_common import *


class SF2PerfectSquare(SpecialFactorScene):
    PART = "2 / 3"

    def construct(self):
        given = poly([["x", "^{2}"], ["+", "6", "x"], ["+", "9"]], fs=BIG_FS)
        fit(given).move_to(MATH)
        tag = label("EXAMPLE 11(a)", fs=29, color=MUTED, weight=BOLD).next_to(given, UP, buff=0.29)
        self.say(
            line(f"x{sup('2')} + 6x + 9: a {E('square')} in disguise?",
                 f"Is X squared plus six X plus nine {BR} a square in disguise?"),
            anims=[FadeIn(given, shift=UP*0.2), FadeIn(tag)],
        )
        self.play(FadeOut(VGroup(given, tag)), run_time=0.55)

        outer = ptex("x", "^{2}", "+", "6", "x", "+", "3", "^{2}", fs=MID_FS)
        outer.move_to(MATH+UP*0.75)
        roots = VGroup(chip("ROOT: x", BASE_C), chip("ROOT: 3", EXP_C)).arrange(RIGHT, buff=0.4)
        roots.move_to(MATH+DOWN*0.85)
        self.say(
            line(f"Outer terms are squares: {B('x²')} and {E('3²')}.",
                 f"The outer terms are squares: {BR} X squared and three squared."),
            anims=[FadeIn(outer, shift=UP*0.2)],
            steps=[[FadeIn(roots, shift=UP*0.15)]],
        )
        check = ptex("2", r"\cdot", "x", r"\cdot", "3", "=", "6", "x", fs=MID_FS)
        fit(check).move_to(MATH+DOWN*0.85)
        self.say(
            line(f"Middle check: 2 · x · 3 = {R('6x')} ✓",
                 f"Check the middle. {BR} Two times X times three is six X."),
            anims=[FadeOut(roots), FadeIn(check, shift=UP*0.15)],
            steps=[[Circumscribe(check[6:], color=RES_C, run_time=0.9)]],
        )
        self.play(FadeOut(VGroup(outer, check)), run_time=0.55)

        tiles = square_tiles(center=MATH+DOWN*0.15)
        regions, labels, top, side = tiles
        result = ptex("(", "x", "+", "3", ")", "^{2}", fs=MID_FS)
        result.set_color(RES_C)
        result.move_to(MATH+DOWN*2.47)
        self.say(
            line(f"The tiles close into a square: {R('(x + 3)²')}.",
                 f"One X squared tile, two three X strips and nine units {BR} make a square with side X plus three."),
            anims=[FadeIn(regions[0], scale=0.9)],
            steps=[[LaggedStart(*[FadeIn(t, shift=UP*0.23) for t in regions[1:]],
                                 lag_ratio=0.22, run_time=1.2)],
                   [FadeIn(labels), FadeIn(top), FadeIn(side)],
                   [FadeIn(result, shift=UP*0.13)]],
        )
        self.play(FadeOut(VGroup(tiles, result)), run_time=0.6)

        negative = poly([["4", "x", "^{2}"], ["-", "4", "x", "y"], ["+", "y", "^{2}"]], fs=MID_FS)
        roots = ptex("a", "=", "2", "x", r"\quad", "b", "=", "y", fs=SMALL_FS)
        middle = ptex("2", "(", "2", "x", ")", "y", "=", "4", "x", "y", fs=SMALL_FS)
        answer = ptex("(", "2", "x", "-", "y", ")", "^{2}", fs=MID_FS)
        answer.set_color(RES_C)
        stack = fit_zone(VGroup(negative, roots, middle, answer).arrange(DOWN, buff=0.34))
        tag = label("EXAMPLE 11(b)", fs=29, color=MUTED, weight=BOLD).next_to(negative, UP, buff=0.22)
        self.say(
            line(f"4x{sup('2')} − 4xy + y{sup('2')} = {R('(2x − y)²')}.",
                 f"Four X squared minus four X Y plus Y squared. {BR} "
                 f"The roots are two X and Y: twice their product is four X Y."),
            anims=[FadeIn(negative, shift=UP*0.15), FadeIn(tag)],
            steps=[[FadeIn(roots), FadeIn(middle)], [FadeIn(answer, shift=UP*0.15)]],
        )
        self.play(FadeOut(VGroup(stack, tag)), run_time=0.55)

        wrong = poly([["x", "^{2}"], ["+", "5", "x"], ["+", "9"]], fs=MID_FS)
        expectation = ptex("2", r"\cdot", "x", r"\cdot", "3", "=", "6", "x", r"\neq", "5", "x", fs=SMALL_FS)
        expectation[-2:].set_color(WARN_C)
        miss = chip("MISSING 1x", WARN_C).scale(0.86)
        stage = fit_zone(VGroup(wrong, expectation, miss).arrange(DOWN, buff=0.5))
        self.say(
            line(f"x{sup('2')} + 5x + 9? The middle should be {E('6x')}, not {W('5x')}.",
                 f"But X squared plus five X plus nine? {BR} The middle should be six X. It is not a perfect square."),
            anims=[FadeIn(wrong, shift=UP*0.2)],
            steps=[[FadeIn(expectation, shift=UP*0.1)], [FadeIn(miss, scale=0.85)]],
        )
        self.play(FadeOut(stage), run_time=0.55)

        rule = ptex("a", "^{2}", r"\pm", "2", "a", "b", "+", "b", "^{2}", "=",
                    "(", "a", r"\pm", "b", ")", "^{2}", fs=SMALL_FS)
        card = self.card(rule, title="CHECK THE MIDDLE")
        self.say(
            line(f"Middle = {E('2ab')}? Then it's {R('(a ± b)²')}.",
                 f"If the middle is plus or minus twice A B, {BR} it is a perfect square."),
            anims=[FadeIn(card, scale=0.94, run_time=0.9)],
        )
        self.outro()
