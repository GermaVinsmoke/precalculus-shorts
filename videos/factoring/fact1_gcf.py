"""Part 5, video 1: take out the greatest common factor (Example 6)."""

try:
    from .fact_common import *
except ImportError:  # Manim loading this file directly
    from fact_common import *


class F1CommonFactor(FactorScene):
    PART = "1 / 3"

    def construct(self):
        factors = ptex("(", "x", "-", "2", ")", "(", "x", "+", "3", ")", fs=MID_FS)
        expanded = poly([["x", "^{2}"], ["+", "x"], ["-", "6"]], fs=MID_FS)
        pair = VGroup(factors, expanded).arrange(DOWN, buff=1.05).move_to(MATH)
        arrow = DoubleArrow(factors.get_bottom() + DOWN * 0.14, expanded.get_top() + UP * 0.14,
                            color=EXP_C, stroke_width=4, buff=0.03, tip_length=0.16)
        self.say(
            line(f"Expanding goes {E('forward')}. Factoring goes {E('back')}.",
                 f"Expanding goes forward. {BR} Factoring goes back."),
            anims=[FadeIn(factors, shift=UP * 0.2)],
            steps=[[GrowArrow(arrow), FadeIn(expanded, shift=UP * 0.2)],
                   [Circumscribe(factors, color=RES_C, run_time=0.9)]],
        )
        self.play(FadeOut(VGroup(pair, arrow)), run_time=0.6)

        given = poly([["3", "x", "^{2}"], ["-", "6", "x"]], fs=BIG_FS)
        given.move_to(MATH + UP * 0.45)
        shared = VGroup(*[SurroundingRectangle(t, color=EXP_C, buff=0.12,
                                               corner_radius=0.13, stroke_width=3) for t in given.terms])
        common = label(f"both terms contain {E('3x')}", fs=42, color=MUTED)
        common.next_to(given, DOWN, buff=0.65)
        tag_a = label("EXAMPLE 6(a)", fs=29, color=MUTED, weight=BOLD).next_to(given, UP, buff=0.45)
        self.say(
            line(f"3x{sup('2')} − 6x: both terms share {E('3x')}.",
                 f"In three X squared minus six X, {BR} both terms share three X."),
            anims=[FadeIn(given, shift=UP * 0.25), FadeIn(tag_a)],
            steps=[[Create(shared), FadeIn(common, shift=UP * 0.15)]],
        )
        factored = ptex("3", "x", "(", "x", "-", "2", ")", fs=BIG_FS)
        factored[0:2].set_color(EXP_C)
        factored.move_to(MATH + UP * 0.45)
        check = ptex("3", "x", r"\cdot", "x", "-", "3", "x", r"\cdot", "2", fs=SMALL_FS)
        check.move_to(MATH + DOWN * 1.0)
        self.say(
            line(f"So it's {R('3x(x − 2)')}. Multiply back to check.",
                 f"So it's three X, times X minus two. {BR} Multiply back to check."),
            anims=[FadeOut(VGroup(given, shared, common)), FadeIn(factored, shift=UP * 0.2)],
            steps=[[FadeIn(check, shift=UP * 0.15)]],
        )
        self.play(FadeOut(VGroup(factored, check, tag_a)), run_time=0.6)

        big = poly([["8", "x", "^{4}", "y", "^{2}"], ["+", "6", "x", "^{3}", "y", "^{3}"],
                    ["-", "2", "x", "y", "^{4}"]], fs=SMALL_FS)
        fit(big).move_to(MATH + UP * 1.65)
        tag_b = label("EXAMPLE 6(b)", fs=29, color=MUTED, weight=BOLD).next_to(big, UP, buff=0.25)
        rows = VGroup(
            label(f"numbers:  8, 6, 2  →  {E('2')}", fs=33, color=MUTED),
            label(f"x powers:  4, 3, 1  →  {E('x')}", fs=33, color=MUTED),
            label(f"y powers:  2, 3, 4  →  {E('y²')}", fs=33, color=MUTED),
        ).arrange(DOWN, buff=0.24, aligned_edge=LEFT)
        panel = RoundedRectangle(corner_radius=0.25, width=SAFE_W - 0.45, height=2.28,
                                 fill_color=CARD_FILL, fill_opacity=0.94,
                                 stroke_color=CARD_STROKE, stroke_width=2)
        panel.move_to(MATH + DOWN * 0.45)
        rows.move_to(panel)
        self.say(
            line(f"Bigger: find the {E('GCF')} piece by piece.",
                 f"For a bigger one, build the common factor piece by piece."),
            anims=[FadeIn(big, shift=UP * 0.2), FadeIn(tag_b)],
            steps=[[FadeIn(panel), LaggedStart(*[FadeIn(r, shift=RIGHT * 0.2) for r in rows],
                                             lag_ratio=0.28, run_time=1.4)]],
        )
        result_b = ptex("2", "x", "y", "^{2}", "(", "4", "x", "^{3}", "+", "3", "x", "^{2}",
                        "y", "-", "y", "^{2}", ")", fs=SMALL_FS)
        result_b[0:4].set_color(RES_C)
        fit(result_b).move_to(MATH + DOWN * 1.6)
        self.say(
            line(f"Take the smallest power of each: {R('2xy²')}.",
                 f"Numbers: two. {BR} X: the smallest power, X. {BR} Y: Y squared. "
                 f"Together, two X Y squared."),
            anims=[Circumscribe(rows, color=EXP_C, run_time=1.1)],
            steps=[[FadeOut(VGroup(panel, rows)), FadeIn(result_b, shift=UP * 0.2)]],
        )
        self.play(FadeOut(VGroup(big, result_b, tag_b)), run_time=0.6)

        whole = ptex("(", "2", "x", "+", "4", ")", "(", "x", "-", "3", ")",
                     "-", "5", "(", "x", "-", "3", ")", fs=SMALL_FS)
        fit(whole).move_to(MATH + UP * 1.0)
        outlines = VGroup(*[SurroundingRectangle(whole[a:b], color=BASE_C, buff=0.09,
                                                  corner_radius=0.12, stroke_width=3)
                            for a, b in ((6, 11), (13, 18))])
        result_c = ptex("(", "2", "x", "-", "1", ")", "(", "x", "-", "3", ")", fs=MID_FS)
        result_c.set_color(RES_C)
        fit(result_c).move_to(MATH + DOWN * 0.8)
        tag_c = label("EXAMPLE 6(c)", fs=29, color=MUTED, weight=BOLD).next_to(whole, UP, buff=0.35)
        self.say(
            line(f"A common factor can be a {B('whole binomial')}.",
                 f"A common factor can even be a whole binomial: {BR} X minus three."),
            anims=[FadeIn(whole, shift=UP * 0.2), FadeIn(tag_c)],
            steps=[[Create(outlines)], [FadeIn(result_c, shift=UP * 0.2)]],
        )
        self.play(FadeOut(VGroup(whole, outlines, result_c, tag_c)), run_time=0.6)

        card_content = VGroup(label(f"Numbers + smallest variable powers", fs=36),
                              label(f"Then multiply back to {R('check')}.", fs=36)).arrange(DOWN, buff=0.35)
        card = self.card(card_content, title="GREATEST COMMON FACTOR")
        self.say(
            line(f"Pull out the {E('GCF')} first. Always check.",
                 f"Pull out the greatest common factor first, {BR} and always check by multiplying back."),
            anims=[FadeIn(card, scale=0.94, run_time=0.9)],
        )
        self.outro()
