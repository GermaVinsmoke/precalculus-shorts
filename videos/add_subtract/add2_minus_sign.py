try:
    from .add_common import *
except ImportError:  # Manim loading this file directly
    from add_common import *

P1 = [["("], ["x", "^{3}"], ["-", "6", "x", "^{2}"], ["+", "2", "x"], ["+", "4"], [")"]]
P2 = [["-"], ["("], ["x", "^{3}"], ["+", "5", "x", "^{2}"], ["-", "7", "x"], [")"]]


class A2MinusSign(AddScene):
    PART = "2 / 2"

    def construct(self):
        p1, p2 = self.hook()
        flipped = self.rule_and_wave(p2)
        self.combine(p1, flipped)
        self.takeaway()
        self.outro()

    # ── Hook: the one-sign mistake ──────────────────────────────────────
    def hook(self):
        p1 = poly(P1, fs=SMALL_FS)
        p2 = poly(P2, fs=SMALL_FS)
        lines = fit(VGroup(p1, p2).arrange(DOWN, buff=0.3)).move_to(MATH + UP * 1.8)
        wrong = poly([["-", "x", "^{3}"], ["+", "5", "x", "^{2}"], ["-", "7", "x"]], fs=SMALL_FS)
        wrong.next_to(lines, DOWN, buff=0.7)
        oops = VGroup(*[SurroundingRectangle(wrong.terms[i], color=WARN_C, buff=0.08, corner_radius=0.1,
                                             stroke_width=3) for i in (1, 2)])
        tag = label(W("only the first sign flipped"), fs=34, weight=BOLD).next_to(wrong, DOWN, buff=0.35)
        self.say(
            line("Subtract these two polynomials.", "Subtract these two polynomials."),
            anims=[LaggedStart(FadeIn(p1, shift=UP * 0.2), FadeIn(p2, shift=UP * 0.2), lag_ratio=0.5, run_time=1.2)],
            gap=0.2,
        )
        self.say(
            line(f"A common mistake: flipping {W('only the first')} sign.",
                 "A common mistake: flipping only the first sign."),
            anims=[FadeIn(wrong, shift=UP * 0.2, run_time=0.8),
                   Succession(Wait(1.6), AnimationGroup(Create(oops), FadeIn(tag, shift=UP * 0.15), run_time=0.8))],
        )
        self.play(FadeOut(VGroup(wrong, oops, tag), shift=DOWN * 0.3), run_time=0.6)
        return p1, p2

    # ── −(b + c) = −b − c, then the wave ────────────────────────────────
    def rule_and_wave(self, p2):
        rule = ptex("-", "(", "b", "+", "c", ")", "=", "-", "b", "-", "c", fs=MID_FS)
        rule[7].set_color(WARN_C)
        rule[9].set_color(WARN_C)
        fit(rule).move_to(MATH + DOWN * 0.35)
        minus_one = fit(label(f"the minus means {W('−1 ×')} everything inside", fs=34, color=MUTED))
        minus_one.next_to(rule, DOWN, buff=0.35)
        self.say(
            line(f"A minus before parentheses means {W('−1')} times everything inside…",
                 "A minus before parentheses means negative one, times everything inside."),
            line(f"…so {W('every')} sign flips.", "So every sign flips."),
            anims=[FadeIn(rule[0:6], shift=UP * 0.2, run_time=0.8),
                   Succession(Wait(2.4), FadeIn(minus_one, shift=UP * 0.15, run_time=0.6)),
                   Succession(Wait(4.0), FadeIn(rule[6:], shift=LEFT * 0.2, run_time=0.8))],
        )
        self.play(FadeOut(VGroup(rule, minus_one), shift=DOWN * 0.3), run_time=0.6)

        flipped = poly([["-", "x", "^{3}"], ["-", "5", "x", "^{2}"], ["+", "7", "x"]], fs=SMALL_FS)
        flipped.move_to(p2)
        for t in flipped.terms:
            t[0].set_color(WARN_C)
        marker = Circle(radius=0.28, color=WARN_C, stroke_width=4).move_to(p2.terms[0])

        def flip(src, dst):
            return [ReplacementTransform(src, dst), Flash(dst[0], color=WARN_C, flash_radius=0.25, run_time=0.6),
                    marker.animate.move_to(dst[0])]

        self.say(
            line(f"Watch it roll through: {W('−x³')}, {W('−5x²')}, {W('+7x')}.",
                 f"Watch the minus roll through: {BR} minus x cubed, {BR} minus five x squared, {BR} plus seven x."),
            anims=[Create(marker, run_time=0.5)],
            steps=[
                flip(VGroup(p2.terms[0], p2.terms[1], p2.terms[2]), flipped.terms[0]),
                0.5,
                flip(p2.terms[3], flipped.terms[1]),
                0.5,
                flip(p2.terms[4], flipped.terms[2]) + [FadeOut(p2.terms[5])],
                [FadeOut(marker), *[t[0].animate.set_color(INK) for t in flipped.terms]],
            ],
        )
        return flipped

    # ── Combine like terms: the x³ cancel ───────────────────────────────
    def combine(self, p1, flipped):
        heads = bin_heads(MATH_Y - 0.4)
        fs = 72
        cols = [
            [ptex("x", "^{3}", fs=fs), ptex("-", "x", "^{3}", fs=fs)],
            [ptex("-", "6", "x", "^{2}", fs=fs), ptex("-", "5", "x", "^{2}", fs=fs)],
            [ptex("+", "2", "x", fs=fs), ptex("+", "7", "x", fs=fs)],
            [ptex("+", "4", fs=fs)],
        ]
        for x, col in zip(BIN_X, cols):
            for k, m in enumerate(col):
                m.move_to([x, MATH_Y - 1.2 - 0.72 * k, 0])
        sources = [[p1.terms[1], flipped.terms[0]], [p1.terms[2], flipped.terms[1]],
                   [p1.terms[3], flipped.terms[2]], [p1.terms[4]]]
        zero = tex("0", fs=fs, color=MUTED).move_to([BIN_X[0], MATH_Y - 1.55, 0])
        merged = [ptex("-", "11", "x", "^{2}", fs=fs), ptex("+", "9", "x", fs=fs), ptex("+", "4", fs=fs)]
        for x, m in zip(BIN_X[1:], merged):
            m.set_color(RES_C).move_to([x, MATH_Y - 1.55, 0])
        final = poly([["="], ["-", "11", "x", "^{2}"], ["+", "9", "x"], ["+", "4"]], fs=MID_FS)
        final.set_color(RES_C)
        final.terms[0].set_color(INK)
        fit(final).move_to(MATH + DOWN * 0.6)
        self.say(
            "Now sort and combine like terms.",
            anims=[LaggedStart(*[FadeIn(h, shift=DOWN * 0.2) for h in heads], lag_ratio=0.2, run_time=1.0)],
            steps=[[LaggedStart(*[TransformFromCopy(s, d, path_arc=-0.5)
                                  for srcs, col in zip(sources, cols) for s, d in zip(srcs, col)],
                                lag_ratio=0.18, run_time=2.4)]],
        )
        self.say(
            line(f"The x{sup('3')} terms {E('cancel')} completely…", "The x cubed terms cancel completely."),
            anims=[ReplacementTransform(VGroup(*cols[0]), zero, run_time=1.0),
                   Succession(Wait(1.0), FadeOut(zero, scale=0.3, run_time=0.6))],
            gap=0.2,
        )
        self.say(
            line(f"…leaving {R('−11x² + 9x + 4')}.", f"Which leaves: {BR} negative eleven x squared, plus nine x, plus four."),
            anims=[*[ReplacementTransform(VGroup(*col), m) for col, m in zip(cols[1:], merged)]],
            run_time=1.2,
            steps=[0.6, [*[ReplacementTransform(m, t) for m, t in zip(merged, final.terms[1:])],
                         FadeIn(final.terms[0]), FadeOut(heads)]],
        )
        self.play(FadeOut(VGroup(p1, flipped, final), shift=UP * 0.4), run_time=0.7)

    # ── Takeaway ────────────────────────────────────────────────────────
    def takeaway(self):
        rule = ptex("-", "(", "b", "+", "c", ")", "=", "-", "b", "-", "c", fs=MID_FS)
        rule[7].set_color(WARN_C)
        rule[9].set_color(WARN_C)
        hint = label(f"The minus flips {W('every')} sign inside.", fs=36, color=MUTED)
        card = self.card(VGroup(rule, hint).arrange(DOWN, buff=0.4), title="SUBTRACTING")
        self.say(
            line(f"A minus before parentheses flips {W('every')} sign inside.",
                 "A minus before parentheses flips every sign inside."),
            anims=[FadeIn(card, scale=0.94, run_time=1.0)],
        )
