"""Part 6, video 3: sum and difference of cubes (Example 12)."""

try:
    from .sfact_common import *
except ImportError:  # Manim loading this file directly
    from sfact_common import *


class SF3Cubes(SpecialFactorScene):
    PART = "3 / 3"

    def construct(self):
        given = poly([["27", "x", "^{3}"], ["-", "1"]], fs=BIG_FS)
        given.move_to(MATH+UP*0.8)
        hidden = ptex("(", "3", "x", ")", "^{3}", "-", "1", "^{3}", fs=MID_FS)
        hidden.move_to(MATH+DOWN*0.65)
        tag = label("EXAMPLE 12(a)", fs=29, color=MUTED, weight=BOLD).next_to(given, UP, buff=0.28)
        self.say(
            line(f"27x{sup('3')} − 1: a {E('difference of cubes')}.",
                 f"Twenty-seven X cubed minus one: {BR} three X cubed minus one cubed."),
            anims=[FadeIn(given, shift=UP*0.2), FadeIn(tag)],
            steps=[[FadeIn(hidden, shift=UP*0.15)]],
        )
        self.play(FadeOut(VGroup(given, hidden, tag)), run_time=0.55)

        formula = cubes_formula("-")
        fit(formula).move_to(MATH+UP*0.65)
        split = VGroup(chip("a − b", BASE_C), chip("a² + ab + b²", EXP_C)).arrange(RIGHT, buff=0.24)
        fit(split).move_to(MATH+DOWN*0.85)
        self.say(
            line(f"a{sup('3')} − b{sup('3')} = {R('(a − b)(a² + ab + b²)')}.",
                 f"A cubed minus B cubed {BR} is A minus B, times A squared plus A B plus B squared."),
            anims=[FadeIn(formula, shift=UP*0.15)],
            steps=[[LaggedStart(*[FadeIn(c, scale=0.84) for c in split],
                                 lag_ratio=0.28, run_time=1.0)]],
        )
        same = chip("S · SAME", BASE_C).scale(0.70)
        opposite = chip("O · OPPOSITE", EXP_C).scale(0.70)
        positive = chip("AP · ALWAYS +", RES_C).scale(0.70)
        mnemonic = VGroup(same, opposite, positive).arrange(DOWN, buff=0.22)
        mnemonic.move_to(MATH+DOWN*1.05)
        first_sign = formula.terms[3][2]
        second_sign = formula.terms[4][3]
        last_sign = formula.terms[4][6]
        for sign, color in ((first_sign, WARN_C), (second_sign, EXP_C), (last_sign, RES_C)):
            sign.set_color(color)
        self.say(
            line(f"Signs: {B('same')}, {E('opposite')}, {R('always positive')}. (SOAP)",
                 f"Remember the signs with S O A P. {BR} Same, opposite, always positive."),
            anims=[FadeOut(split), LaggedStart(*[FadeIn(c, shift=UP*0.12) for c in mnemonic],
                                lag_ratio=0.2, run_time=1.0)],
            steps=[[Circumscribe(VGroup(first_sign, second_sign, last_sign),
                                color=EXP_C, run_time=1.0)]],
        )
        self.play(FadeOut(VGroup(formula, mnemonic)), run_time=0.55)

        roots = ptex("a", "=", "3", "x", r"\qquad", "b", "=", "1", fs=SMALL_FS)
        original = poly([["27", "x", "^{3}"], ["-", "1"]], fs=MID_FS)
        answer = ptex("(", "3", "x", "-", "1", ")", "(", "9", "x", "^{2}",
                      "+", "3", "x", "+", "1", ")", fs=SMALL_FS)
        answer.set_color(RES_C)
        work = fit_zone(VGroup(original, roots, answer).arrange(DOWN, buff=0.55))
        tag = label("EXAMPLE 12(a)", fs=29, color=MUTED, weight=BOLD).next_to(original, UP, buff=0.25)
        self.say(
            line(f"a = 3x, b = 1: {R('(3x − 1)(9x² + 3x + 1)')}.",
                 f"Here A is three X, B is one. {BR} "
                 f"The factors are three X minus one, and nine X squared plus three X plus one."),
            anims=[FadeIn(original, shift=UP*0.15), FadeIn(tag)],
            steps=[[FadeIn(roots, shift=UP*0.1)], [FadeIn(answer, shift=UP*0.16)]],
        )
        self.play(FadeOut(VGroup(work, tag)), run_time=0.55)

        hidden_plus = poly([["x", "^{6}"], ["+", "8"]], fs=MID_FS)
        cubes = ptex("(", "x", "^{2}", ")", "^{3}", "+", "2", "^{3}", fs=MID_FS)
        plus_formula = cubes_formula("+", fs=SMALL_FS)
        fit(plus_formula).move_to(MATH+DOWN*1.2)
        stack = fit_zone(VGroup(hidden_plus, cubes).arrange(DOWN, buff=0.48))
        tag = label("EXAMPLE 12(b)", fs=29, color=MUTED, weight=BOLD).next_to(hidden_plus, UP, buff=0.25)
        self.say(
            line(f"x{sup('6')} + 8 = (x{sup('2')}){sup('3')} + 2{sup('3')}.",
                 f"X to the sixth plus eight hides a sum of cubes: {BR} X squared cubed plus two cubed."),
            anims=[FadeIn(hidden_plus, shift=UP*0.2), FadeIn(tag)],
            steps=[[FadeIn(cubes, shift=UP*0.15)]],
        )
        self.play(FadeOut(VGroup(stack, tag)), run_time=0.55)

        result = ptex("(", "x", "^{2}", "+", "2", ")", "(", "x", "^{4}", "-",
                      "2", "x", "^{2}", "+", "4", ")", fs=SMALL_FS)
        result.set_color(RES_C)
        fit(result).move_to(MATH+UP*0.78)
        sop = VGroup(chip("S: +", BASE_C), chip("O: −", EXP_C), chip("AP: +", RES_C))
        sop.scale(0.73).arrange(RIGHT, buff=0.23).move_to(MATH+DOWN*0.82)
        self.say(
            line(f"x{sup('6')} + 8 = {R('(x² + 2)(x⁴ − 2x² + 4)')}.",
                 f"Same, opposite, always positive: {BR} "
                 f"X squared plus two, times X to the fourth minus two X squared plus four."),
            anims=[FadeIn(result, shift=UP*0.16)],
            steps=[[LaggedStart(*[FadeIn(c, scale=0.85) for c in sop],
                                 lag_ratio=0.2, run_time=0.9)]],
        )
        self.play(FadeOut(VGroup(result, sop)), run_time=0.55)

        minus = cubes_formula("-", fs=SMALL_FS)
        plus = cubes_formula("+", fs=SMALL_FS)
        title = label(f"{B('SAME')}  ·  {E('OPPOSITE')}  ·  {R('ALWAYS +')}", fs=29, weight=BOLD)
        card = self.card(VGroup(minus, plus, title).arrange(DOWN, buff=0.30), title="CUBES: S-O-AP")
        self.say(
            line(f"Cubes: {B('same')}, {E('opposite')}, {R('always positive')}.",
                 f"For sums and differences of cubes: {BR} same, opposite, always positive."),
            anims=[FadeIn(card, scale=0.94, run_time=0.9)],
        )
        self.outro()
