"""Part 7, video 2: factor expressions with fractional exponents using original examples."""

try:
    from .fcomp_common import *
except ImportError:  # Manim loading this file directly
    from fcomp_common import *


class FC2FractionalExponents(CompleteScene):
    PART = "2 / 3"

    def construct(self):
        given = poly([
            ["8", "x", "^{5/3}"],
            ["-", "12", "x", "^{2/3}"],
            ["+", "4", "x", "^{-1/3}"],
        ], fs=SMALL_FS)
        fit(given).move_to(MATH)
        question = chip("FACTOR OUT WHAT?", WARN_C).scale(0.78).next_to(given, DOWN, buff=0.55)
        self.say(
            line(
                f"Fractional exponents: what can all three terms share?",
                f"Which power can all three terms share? {BR} Compare five thirds, two thirds, and negative one third.",
            ),
            anims=[FadeIn(given, shift=UP * 0.2)],
            steps=[[FadeIn(question, scale=0.86)]],
        )
        self.play(FadeOut(VGroup(given, question)), run_time=0.5)

        axis = Line([-3.05, 2.45, 0], [2.6, 2.45, 0], color=MUTED, stroke_width=3)
        positions = (-2.35, -0.15, 2.05)
        exponents = ("-1/3", "2/3", "5/3")
        ticks = VGroup(*[
            Line([x, 2.28, 0], [x, 2.62, 0], color=INK, stroke_width=3) for x in positions
        ])
        labels = VGroup(*[
            ptex("x", f"^{{{power}}}", fs=62).move_to([x, 3.08, 0])
            for x, power in zip(positions, exponents)
        ])
        smallest_box = SurroundingRectangle(labels[0], color=EXP_C, buff=0.14,
                                             corner_radius=0.13, stroke_width=3)
        smallest = label(f"smallest exponent = {E('−1/3')}", fs=36, color=MUTED)
        smallest.move_to([CX, 1.45, 0])
        self.say(
            line(
                f"Factor out the {E('smallest exponent')}: x{sup('−1/3')}.",
                f"Factor out the power with the smallest exponent: {BR} X to the negative one third.",
            ),
            anims=[Create(axis), LaggedStart(*[Create(t) for t in ticks], lag_ratio=0.2, run_time=0.8)],
            steps=[[LaggedStart(*[FadeIn(m, shift=UP * 0.12) for m in labels], lag_ratio=0.2, run_time=0.9)],
                   [Create(smallest_box), FadeIn(smallest)]],
        )

        arrows = VGroup(
            CurvedArrow([positions[0], 2.1, 0], [positions[2], 2.1, 0], angle=0.42,
                        color=BASE_C, stroke_width=3, tip_length=0.16),
            CurvedArrow([positions[0], 1.82, 0], [positions[1], 1.82, 0], angle=0.42,
                        color=EXP_C, stroke_width=3, tip_length=0.16),
        )
        distances = VGroup(
            chip("DISTANCE 0", RES_C).scale(0.56),
            chip("DISTANCE 1", EXP_C).scale(0.56),
            chip("DISTANCE 2", BASE_C).scale(0.56),
        )
        for distance, x in zip(distances, positions):
            distance.move_to([x, 0.72, 0])
        leftovers = VGroup(
            tex("1", fs=55, color=RES_C),
            ptex("x", fs=55).set_color(RES_C),
            ptex("x", "^{2}", fs=55).set_color(RES_C),
        )
        for item, x in zip(leftovers, positions):
            item.move_to([x, -0.15, 0])
        down_arrows = VGroup(*[
            Arrow(eq.get_bottom(), item.get_top(), buff=0.08, color=RES_C,
                  stroke_width=2.5, tip_length=0.12)
            for eq, item in zip(distances, leftovers)
        ])
        self.say(
            line(
                f"Subtract exponents: the leftovers are x{sup('2')}, x, and 1.",
                f"Subtract the smallest exponent from each one. {BR} The leftovers are X squared, X, and one.",
            ),
            anims=[LaggedStart(*[Create(a) for a in arrows], lag_ratio=0.25, run_time=0.9)],
            steps=[[LaggedStart(*[FadeIn(d, shift=UP * 0.1) for d in distances], lag_ratio=0.18, run_time=1.0)],
                   [LaggedStart(*[GrowArrow(a) for a in down_arrows], lag_ratio=0.16, run_time=0.8),
                    LaggedStart(*[FadeIn(item, shift=UP * 0.1) for item in leftovers], lag_ratio=0.16, run_time=0.8)]],
        )
        number_line = VGroup(axis, ticks, labels, smallest_box, smallest, arrows,
                             distances, leftovers, down_arrows)
        self.play(FadeOut(number_line), run_time=0.55)

        step = ptex("4", "x", "^{-1/3}", "(", "2", "x", "^{2}", "-", "3", "x", "+", "1", ")",
                    fs=SMALL_FS)
        answer = ptex("4", "x", "^{-1/3}", "(", "2", "x", "-", "1", ")", "(", "x", "-", "1", ")",
                      fs=SMALL_FS)
        answer.set_color(RES_C)
        stack = fit_zone(VGroup(step, answer).arrange(DOWN, buff=0.72))
        self.say(
            line(
                f"Then factor 2x{sup('2')} − 3x + 1: {R('(2x − 1)(x − 1)')}.",
                f"The trinomial factors into {BR} two X minus one, times X minus one.",
            ),
            anims=[FadeIn(step, shift=UP * 0.15)],
            steps=[[FadeIn(answer, shift=UP * 0.18), Circumscribe(answer, color=RES_C, run_time=1.0)]],
        )
        self.play(FadeOut(stack), run_time=0.5)

        block = ptex("(", "x", "+", "4", ")", fs=68)
        block_box = SurroundingRectangle(block, color=BASE_C, buff=0.16,
                                         corner_radius=0.14, stroke_width=3)
        block_group = VGroup(block_box, block).move_to(MATH + UP * 1.55)
        exp_low = chip("POWER −3/5", EXP_C).scale(0.72).move_to([CX - 1.65, MATH_Y + 0.15, 0])
        exp_high = chip("POWER 2/5", BASE_C).scale(0.72).move_to([CX + 1.65, MATH_Y + 0.15, 0])
        difference = ptex("2/5", "-", "(", "-3/5", ")", "=", "1", fs=58)
        difference[-1].set_color(RES_C)
        difference.move_to(MATH + DOWN * 0.75)
        original_b = ptex(
            "x", "(", "x", "+", "4", ")", "^{-3/5}", "+",
            "(", "x", "+", "4", ")", "^{2/5}",
            fs=57,
        )
        fit(original_b).move_to(MATH + DOWN * 1.75)
        self.say(
            line(
                f"A whole block works too: factor out the smaller power, {E('−3/5')}.",
                f"Treat X plus four as one base. {BR} Pull out its smaller power, negative three fifths.",
            ),
            anims=[FadeIn(block_group, shift=UP * 0.15)],
            steps=[[FadeIn(exp_low), FadeIn(exp_high)], [FadeIn(difference, shift=UP * 0.1)],
                   [FadeIn(original_b, shift=UP * 0.12)]],
        )
        self.play(FadeOut(VGroup(block_group, exp_low, exp_high, difference, original_b)), run_time=0.55)

        factored_b = ptex(
            "(", "x", "+", "4", ")", "^{-3/5}",
            "[", "x", "+", "(", "x", "+", "4", ")", "]",
            fs=SMALL_FS,
        )
        simplified = ptex(
            "2", "(", "x", "+", "4", ")", "^{-3/5}", "(", "x", "+", "2", ")",
            fs=SMALL_FS,
        )
        simplified.set_color(RES_C)
        work_b = fit_zone(VGroup(factored_b, simplified).arrange(DOWN, buff=0.72))
        self.say(
            line(
                f"Inside: x + (x + 4) = 2(x + 2).",
                f"Inside the brackets, X plus X plus four is two X plus four, {BR} or two times the quantity X plus two.",
            ),
            anims=[FadeIn(factored_b, shift=UP * 0.15)],
            steps=[[FadeIn(simplified, shift=UP * 0.18), Circumscribe(simplified, color=RES_C, run_time=1.0)]],
        )
        self.play(FadeOut(work_b), run_time=0.5)

        rule = VGroup(
            label(f"1  Find the {E('smallest exponent')}", fs=35),
            label(f"2  {B('Subtract')} to get each leftover power", fs=35),
            label(f"3  Keep {R('factoring')} the expression inside", fs=35),
        ).arrange(DOWN, buff=0.28, aligned_edge=LEFT)
        card = self.card(rule, title="FRACTIONAL EXPONENTS")
        self.say(
            line(
                f"Factor out the {E('smallest exponent')}, then keep going.",
                f"With fractional exponents, factor out the smallest one, then keep factoring.",
            ),
            anims=[FadeIn(card, scale=0.94, run_time=0.9)],
        )
        self.outro()
