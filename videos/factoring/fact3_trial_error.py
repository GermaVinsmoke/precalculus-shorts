"""Part 5, video 3: trial factoring and the middle-term test (Examples 8, 9b)."""

try:
    from .fact_common import *
except ImportError:  # Manim loading this file directly
    from fact_common import *


class F3TrialAndError(FactorScene):
    PART = "3 / 3"

    def construct(self):
        target = poly([["6", "x", "^{2}"], ["+", "7", "x"], ["-", "5"]], fs=BIG_FS)
        fit(target).move_to(MATH)
        tag = label("EXAMPLE 8", fs=29, color=MUTED, weight=BOLD).next_to(target, UP, buff=0.45)
        self.say(
            line(f"6x{sup('2')} + 7x − 5: now x{sup('2')} has a {E('6')}.",
                 f"Six X squared plus seven X minus five. {BR} Now the X squared has a six in front."),
            anims=[FadeIn(target, shift=UP * 0.25), FadeIn(tag)],
        )
        self.play(target.animate.move_to(MATH + UP * 1.5), tag.animate.shift(UP * 1.5), run_time=0.7)

        blanks = ptex("(", r"\square", "x", "+", r"\square", ")",
                      "(", r"\square", "x", "+", r"\square", ")", fs=SMALL_FS)
        blanks.move_to(MATH + DOWN * 0.25)
        front = label(f"front:   {E('6 = 6·1 or 3·2')}", fs=33, color=MUTED)
        last = label(f"last:   {E('−5 = 5·(−1)')}", fs=33, color=MUTED)
        choices = VGroup(front, last).arrange(DOWN, buff=0.23).move_to(MATH + DOWN * 1.55)
        self.say(
            line(f"Factors of {E('6')} go in front; factors of {E('−5')} go last.",
                 f"The factors of six go in front, {BR} and the factors of negative five go last."),
            anims=[FadeIn(blanks, shift=UP * 0.2)],
            steps=[[FadeIn(choices, shift=UP * 0.15)]],
        )
        self.play(FadeOut(VGroup(blanks, choices)), run_time=0.6)

        first = ptex("(", "6", "x", "+", "5", ")", "(", "x", "-", "1", ")", fs=MID_FS)
        fit(first).move_to(MATH + DOWN * 0.05)
        meter_bad = ptex("-", "6", "x", "+", "5", "x", "=", "-", "x", fs=SMALL_FS)
        meter_bad[-2:].set_color(WARN_C)
        meter_bad.move_to(MATH + DOWN * 1.25)
        need = chip("NEED +7x", EXP_C).scale(0.75)
        need.move_to([CX, MATH_Y - 2.2, 0])
        self.say(
            line(f"The middle term decides: this gives {W('−x')}, not {R('7x')}.",
                 f"Outer plus inner must make seven X. {BR} This guess gives negative X."),
            anims=[FadeIn(need), FadeIn(first, shift=UP * 0.2)],
            steps=[[FadeIn(meter_bad, shift=UP * 0.15)],
                   [Circumscribe(meter_bad[-2:], color=WARN_C, run_time=0.8)]],
        )

        correct = ptex("(", "3", "x", "+", "5", ")", "(", "2", "x", "-", "1", ")", fs=MID_FS)
        fit(correct).move_to(first)
        meter_ok = ptex("-", "3", "x", "+", "10", "x", "=", "7", "x", fs=SMALL_FS)
        meter_ok[-2:].set_color(RES_C)
        meter_ok.move_to(meter_bad)
        self.say(
            line(f"(3x + 5)(2x − 1): {R('−3x + 10x = 7x')}.",
                 f"Try three X plus five, times two X minus one: {BR} "
                 f"minus three X plus ten X is seven X."),
            anims=[ReplacementTransform(first, correct), ReplacementTransform(meter_bad, meter_ok)],
            steps=[[Circumscribe(meter_ok[-2:], color=RES_C, run_time=1.0)]],
        )
        self.play(FadeOut(VGroup(target, tag, need, correct, meter_ok)), run_time=0.6)

        big = ptex("(", "5", "a", "+", "1", ")", "^{2}", "-", "2", "(", "5", "a", "+", "1", ")",
                   "-", "3", fs=SMALL_FS)
        fit(big).move_to(MATH + UP * 1.35)
        tag_b = label("EXAMPLE 9(b)", fs=29, color=MUTED, weight=BOLD).next_to(big, UP, buff=0.32)
        outlines = VGroup(*[SurroundingRectangle(big[a:b], color=BASE_C, buff=0.1,
                                                  corner_radius=0.12, stroke_width=3)
                            for a, b in ((0, 6), (9, 15))])
        block = chip("u = 5a + 1", BASE_C).scale(0.85).move_to(MATH + DOWN * 0.35)
        self.say(
            line(f"Same shape, bigger pieces: treat {B('5a + 1')} as a block.",
                 f"Some problems just look hard. {BR} Treat five A plus one as one block."),
            anims=[FadeIn(big, shift=UP * 0.2), FadeIn(tag_b)],
            steps=[[Create(outlines), FadeIn(block, shift=UP * 0.15)]],
        )

        substitute = ptex("u", "^{2}", "-", "2", "u", "-", "3", "=",
                          "(", "u", "-", "3", ")", "(", "u", "+", "1", ")", fs=SMALL_FS)
        fit(substitute).move_to(MATH + DOWN * 0.05)
        result = ptex("(", "5", "a", "-", "2", ")", "(", "5", "a", "+", "2", ")", fs=MID_FS)
        result.set_color(RES_C)
        fit(result).move_to(MATH + DOWN * 1.35)
        self.say(
            line(f"u{sup('2')} − 2u − 3 = (u − 3)(u + 1) = {R('(5a − 2)(5a + 2)')}.",
                 f"Block squared, minus two blocks, minus three, factors like before. {BR} "
                 f"Unpack it: five A minus two, times five A plus two."),
            anims=[FadeOut(VGroup(big, tag_b, outlines, block)), FadeIn(substitute, shift=UP * 0.2)],
            steps=[[FadeIn(result, shift=UP * 0.2)]],
        )
        self.play(FadeOut(VGroup(substitute, result)), run_time=0.6)

        rule = VGroup(label(f"Try factor pairs for the {E('first')} and {E('last')} terms.", fs=32),
                      label(f"{R('Outer + inner')} must match the middle.", fs=32)).arrange(DOWN, buff=0.37)
        card = self.card(rule, title="THE MIDDLE TERM DECIDES")
        self.say(
            line(f"The {E('middle term')} decides.",
                 f"Try factor pairs, {BR} and let the middle term decide."),
            anims=[FadeIn(card, scale=0.94, run_time=0.9)],
        )
        self.outro()
