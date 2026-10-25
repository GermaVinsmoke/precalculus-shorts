"""Part 5, video 2: factor x² + bx + c by product and sum (Examples 7, 9a)."""

try:
    from .fact_common import *
except ImportError:  # Manim loading this file directly
    from fact_common import *
from videos.multiplying.mult_common import area_model


class F2SumAndProduct(FactorScene):
    PART = "2 / 3"

    def construct(self):
        target = poly([["x", "^{2}"], ["+", "7", "x"], ["+", "12"]], fs=BIG_FS)
        fit(target).move_to(MATH + UP * 1.25)
        holes = ptex("(", "x", "+", r"\square", ")", "(", "x", "+", r"\square", ")", fs=MID_FS)
        fit(holes).move_to(MATH + DOWN * 0.65)
        tag = label("EXAMPLE 7", fs=29, color=MUTED, weight=BOLD).next_to(target, UP, buff=0.3)
        self.say(
            line(f"x{sup('2')} + 7x + 12: find two numbers.",
                 f"To factor X squared plus seven X plus twelve, {BR} you need two special numbers."),
            anims=[FadeIn(target, shift=UP * 0.2), FadeIn(tag), FadeIn(holes, shift=UP * 0.2)],
        )
        self.play(FadeOut(VGroup(target, holes, tag)), run_time=0.6)

        identity = poly([["(", "x", "+", "r", ")", "(", "x", "+", "s", ")"], ["="],
                         ["x", "^{2}"], ["+", "(", "r", "+", "s", ")", "x"],
                         ["+", "r", "s"]], fs=SMALL_FS)
        fit(identity).move_to(MATH + UP * 1.9)
        grid = area_model([["x"], ["r"]], [["x"], ["s"]],
                          center=MATH + DOWN * 0.4, cell_w=1.5, cell_h=0.85)
        cells = grid[0]
        entries = VGroup(*[ptex(*p, fs=48).move_to(cell) for p, cell in zip(
            (("x", "^{2}"), ("r", "x"), ("s", "x"), ("r", "s")), cells)])
        self.say(
            line(f"(x + r)(x + s) = x{sup('2')} + (r + s)x + rs.",
                 f"Here's why: {BR} X plus R, times X plus S, gives X squared, "
                 f"plus R plus S X, plus R S."),
            anims=[FadeIn(identity, shift=UP * 0.2)],
            steps=[[FadeIn(grid, shift=UP * 0.15),
                    LaggedStart(*[FadeIn(e, scale=0.8) for e in entries],
                                 lag_ratio=0.2, run_time=1.3)]],
        )
        self.play(FadeOut(VGroup(identity, grid, entries)), run_time=0.6)

        goals = VGroup(chip("PRODUCT 12", BASE_C), chip("SUM 7", EXP_C))
        goals.arrange(RIGHT, buff=0.3).move_to(MATH + UP * 0.25)
        self.say(
            line(f"So r · s = {B('12')} and r + s = {E('7')}.",
                 f"So the numbers multiply to twelve, {BR} and add to seven."),
            anims=[LaggedStart(*[FadeIn(g, scale=0.9) for g in goals], lag_ratio=0.3, run_time=1.0)],
        )
        self.play(goals.animate.move_to(MATH + UP * 2.0).scale(0.8), run_time=0.65)

        candidates = [pair_panel(r, s, 12, 7).move_to(MATH + DOWN * 0.3)
                      for r, s in ((1, 12), (2, 6), (3, 4))]
        self.say(
            line(f"Try pairs: {R('3 and 4')} work.",
                 f"Try the pairs: one and twelve, two and six, three and four. {BR} Three and four work."),
            anims=[FadeIn(candidates[0], scale=0.94)],
            steps=[[ReplacementTransform(candidates[0], candidates[1], run_time=0.85)],
                   [ReplacementTransform(candidates[1], candidates[2], run_time=0.85)],
                   [Circumscribe(candidates[2], color=RES_C, run_time=0.9)]],
        )
        result = ptex("(", "x", "+", "3", ")", "(", "x", "+", "4", ")", fs=BIG_FS)
        result.set_color(RES_C)
        fit(result).move_to(MATH + UP * 0.6)
        check = ptex("x", "^{2}", "+", "(", "3", "+", "4", ")", "x", "+", "12", fs=SMALL_FS)
        check.move_to(MATH + DOWN * 0.85)
        self.say(
            line(f"x{sup('2')} + 7x + 12 = {R('(x + 3)(x + 4)')}.",
                 f"So it's X plus three, times X plus four. {BR} Multiply back to check."),
            anims=[FadeOut(VGroup(candidates[2], goals)), FadeIn(result, shift=UP * 0.2)],
            steps=[[FadeIn(check, shift=UP * 0.2)]],
        )
        self.play(FadeOut(VGroup(result, check)), run_time=0.6)

        negative = poly([["x", "^{2}"], ["-", "2", "x"], ["-", "3"]], fs=SMALL_FS)
        negative.move_to(MATH + UP * 1.8)
        panel = pair_panel(-3, 1, -3, -2, width=5.4).move_to(MATH + DOWN * 0.15)
        factored = ptex("(", "x", "-", "3", ")", "(", "x", "+", "1", ")", fs=MID_FS)
        factored.set_color(RES_C)
        fit(factored).move_to(MATH + DOWN * 2.08)
        label_ = label("EXAMPLE 9(a)", fs=29, color=MUTED, weight=BOLD).next_to(negative, UP, buff=0.28)
        self.say(
            line(f"With negatives: x{sup('2')} − 2x − 3 = {R('(x − 3)(x + 1)')}.",
                 f"With negatives: multiply to negative three, add to negative two: {BR} "
                 f"negative three and one."),
            anims=[FadeIn(negative, shift=UP * 0.2), FadeIn(label_)],
            steps=[[FadeIn(panel, scale=0.92)], [FadeIn(factored, shift=UP * 0.15)]],
        )
        self.play(FadeOut(VGroup(negative, label_, panel, factored)), run_time=0.6)

        content = VGroup(label(f"{E('Multiply')} to c", fs=44),
                         label(f"{E('Add')} to b", fs=44)).arrange(DOWN, buff=0.45)
        card = self.card(content, title="TWO NUMBERS")
        self.say(
            line(f"{E('Multiply')} to c, {E('add')} to b.",
                 f"Find two numbers that multiply to C, {BR} and add to B."),
            anims=[FadeIn(card, scale=0.94, run_time=0.9)],
        )
        self.outro()
