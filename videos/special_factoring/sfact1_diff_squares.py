"""Part 6, video 1: difference of squares (Examples 10a, 10b)."""

try:
    from .sfact_common import *
except ImportError:  # Manim loading this file directly
    from sfact_common import *


class SF1DifferenceOfSquares(SpecialFactorScene):
    PART = "1 / 3"

    def construct(self):
        hook = poly([["4", "x", "^{2}"], ["-", "25"]], fs=BIG_FS)
        hook.move_to(MATH)
        tag = label("EXAMPLE 10(a)", fs=29, color=MUTED, weight=BOLD).next_to(hook, UP, buff=0.33)
        self.say(
            line(f"4x{sup('2')} − 25: no middle term. Can it factor?",
                 f"Four X squared minus twenty-five. {BR} No middle term. Can it factor?"),
            anims=[FadeIn(hook, shift=UP*0.2), FadeIn(tag)],
        )
        self.play(FadeOut(VGroup(hook, tag)), run_time=0.55)

        top, lower, missing, a_label, strip_label, b_label = cut_square()
        a, b, left, bottom = 2.45, 0.8, -2.05, 0.55
        original_border = Square(side_length=a, stroke_color=MUTED, stroke_width=2,
                                 fill_opacity=0).move_to([left+a/2, bottom+a/2, 0])
        self.say(
            line(f"Remove a small {E('b²')} square from a big {B('a²')} square.",
                 f"Take a big square, A by A, {BR} then remove a small B by B square from its corner."),
            anims=[DrawBorderThenFill(top), DrawBorderThenFill(lower)],
            steps=[[FadeIn(a_label), FadeIn(strip_label)],
                   [Create(original_border), FadeIn(missing), FadeIn(b_label)]],
        )
        dest = [left+a+b/2, bottom+b+(a-b)/2, 0]
        outline = Rectangle(width=a+b, height=a-b, stroke_color=RES_C, stroke_width=3,
                            fill_opacity=0).move_to([left+(a+b)/2, dest[1], 0])
        length = ptex("a", "+", "b", fs=61).next_to(outline, DOWN, buff=0.26)
        height = ptex("a", "-", "b", fs=55).next_to(outline, LEFT, buff=0.22)
        rule = ptex("a", "^{2}", "-", "b", "^{2}", "=", "(", "a", "-", "b", ")",
                    "(", "a", "+", "b", ")", fs=SMALL_FS)
        fit(rule).move_to(MATH + DOWN*2.05)
        self.say(
            line(f"a{sup('2')} − b{sup('2')} = {R('(a − b)(a + b)')}.",
                 f"Rotate the bottom strip. {BR} The rectangle is A plus B by A minus B."),
            anims=[FadeOut(VGroup(missing, b_label, strip_label, original_border))],
            steps=[[lower.animate.rotate(PI/2).move_to(dest)],
                   [Create(outline), FadeIn(length), FadeIn(height), FadeIn(rule)]],
        )
        self.play(FadeOut(VGroup(top, lower, a_label, outline, length, height, rule)), run_time=0.55)

        original = poly([["4", "x", "^{2}"], ["-", "25"]], fs=MID_FS)
        squared = ptex("(", "2", "x", ")", "^{2}", "-", "5", "^{2}", fs=MID_FS)
        result = ptex("(", "2", "x", "-", "5", ")", "(", "2", "x", "+", "5", ")", fs=MID_FS)
        result.set_color(RES_C)
        work = fit_zone(VGroup(original, squared, result).arrange(DOWN, buff=0.42))
        tag = label("EXAMPLE 10(a)", fs=29, color=MUTED, weight=BOLD).next_to(original, UP, buff=0.2)
        self.say(
            line(f"4x{sup('2')} − 25 = (2x){sup('2')} − 5{sup('2')} = {R('(2x − 5)(2x + 5)')}.",
                 f"Four X squared is two X squared, and twenty-five is five squared. {BR} "
                 f"So the factors are two X minus five and two X plus five."),
            anims=[FadeIn(original, shift=UP*0.2), FadeIn(tag)],
            steps=[[FadeIn(squared, shift=UP*0.15)], [FadeIn(result, shift=UP*0.15)]],
        )
        self.play(FadeOut(VGroup(work, tag)), run_time=0.55)

        block = ptex("(", "x", "+", "y", ")", "^{2}", "-", "z", "^{2}", fs=MID_FS)
        answer = ptex("(", "x", "+", "y", "-", "z", ")", "(", "x", "+", "y", "+", "z", ")", fs=SMALL_FS)
        answer.set_color(RES_C)
        stack = fit_zone(VGroup(block, answer).arrange(DOWN, buff=0.7))
        box = SurroundingRectangle(block[1:4], color=BASE_C, corner_radius=0.13, buff=0.1)
        tag = label("EXAMPLE 10(b)", fs=29, color=MUTED, weight=BOLD).next_to(block, UP, buff=0.28)
        self.say(
            line(f"With a block: (x + y){sup('2')} − z{sup('2')} splits the same way.",
                 f"It even works with a whole block. {BR} Treat X plus Y as A, then split the squares."),
            anims=[FadeIn(block, shift=UP*0.15), FadeIn(tag)],
            steps=[[Create(box)], [FadeIn(answer, shift=UP*0.2)]],
        )
        self.play(FadeOut(VGroup(stack, box, tag)), run_time=0.55)

        formula = ptex("a", "^{2}", "-", "b", "^{2}", "=", "(", "a", "-", "b", ")",
                       "(", "a", "+", "b", ")", fs=SMALL_FS)
        note = label(f"{W('x² + 4')} is a sum: no real factors", fs=29)
        card = self.card(VGroup(formula, note).arrange(DOWN, buff=0.35), title="DIFFERENCE OF SQUARES")
        self.say(
            line(f"Difference of squares splits; {W('x² + 4')} does not.",
                 f"A difference of squares splits. {BR} But a sum like X squared plus four doesn't factor over the reals."),
            anims=[FadeIn(card, scale=0.94, run_time=0.9)],
        )
        self.outro()
