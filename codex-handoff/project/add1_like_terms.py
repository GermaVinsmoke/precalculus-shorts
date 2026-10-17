from add_common import *


def token(fs=58):
    t = ptex("x", "^{7}", fs=fs)
    box = RoundedRectangle(corner_radius=0.14, width=1.1, height=0.82, fill_color=CARD_FILL, fill_opacity=1,
                           stroke_color=BASE_C, stroke_width=2.5)
    return VGroup(box, t.move_to(box))


class A1LikeTerms(AddScene):
    PART = "1 / 2"

    def construct(self):
        self.hook()
        self.tiles()
        self.counts()
        self.example()
        self.takeaway()
        self.outro()

    # ── Hook: x² + x = x³? ──────────────────────────────────────────────
    def hook(self):
        q = ptex("x", "^{2}", "+", "x", "=", "x", "^{3}", "?", fs=HERO_FS * 0.75)
        q[7].set_color(WARN_C)
        fit(q).move_to(MATH)
        self.q = q
        self.say(
            line(f"Is x{sup('2')} + x the same as x{sup('3')}?", "Is x squared plus x the same as x cubed?"),
            anims=[LaggedStart(FadeIn(q[0:4], shift=UP * 0.3), FadeIn(q[4:], shift=UP * 0.3), lag_ratio=0.5,
                               run_time=1.4)],
        )

    # ── Algebra tiles: different shapes don't merge ─────────────────────
    def tiles(self):
        q = self.q
        sq = algebra_tile("x2", u=2.0)
        strip = algebra_tile("x", u=2.0)
        pair = VGroup(sq, strip).arrange(RIGHT, buff=1.1, aligned_edge=DOWN).move_to(MATH + DOWN * 0.45)
        no = cross(80).move_to(q[5:7].get_center() + DOWN * 0.05)
        self.say(
            line(f"Picture them as tiles: x{sup('2')} is a square, x is a thin strip.",
                 f"Picture them as tiles: {BR} x squared is a square, {BR} x is a thin strip."),
            anims=[q.animate(run_time=0.8).scale(0.6).move_to(MATH + UP * 1.9),
                   Succession(Wait(1.6), DrawBorderThenFill(sq, run_time=0.9)),
                   Succession(Wait(3.2), DrawBorderThenFill(strip, run_time=0.9))],
        )
        self.say(
            line(f"Different shapes: they {W('can’t merge')}.", "Different shapes. They can't merge into one."),
            anims=[Succession(
                AnimationGroup(sq.animate.shift(RIGHT * 0.65), strip.animate.shift(LEFT * 0.65), run_time=0.6),
                AnimationGroup(sq.animate.shift(LEFT * 0.65), strip.animate.shift(RIGHT * 0.65), run_time=0.4,
                               rate_func=rate_functions.ease_out_back),
            ), Succession(Wait(1.2), GrowFromCenter(no, run_time=0.5))],
        )
        self.play(FadeOut(VGroup(q, no, sq, strip), shift=UP * 0.4), run_time=0.7)

    # ── Like terms: add the counts, keep the power ──────────────────────
    def counts(self):
        five = VGroup(*[token() for _ in range(5)]).arrange(RIGHT, buff=0.1)
        three = VGroup(*[token() for _ in range(3)]).arrange(RIGHT, buff=0.1)
        plus = tex("+", fs=MID_FS)
        top = VGroup(five, VGroup(plus, three).arrange(RIGHT, buff=0.22)).arrange(DOWN, buff=0.3)
        fit(top).move_to(MATH + UP * 1.15)
        eight = VGroup(*[token() for _ in range(8)]).arrange_in_grid(2, 4, buff=(0.1, 0.3))
        fit(eight).move_to(top)
        eq = ptex("5", "x", "^{7}", "+", "3", "x", "^{7}", "=", "(5+3)", "x", "^{7}", "=", "8", "x", "^{7}",
                  fs=SMALL_FS, results=[12, 13, 14])
        fit(eq).move_to(MATH + DOWN * 0.75)
        not14 = label(f"not x{sup(W('14'))}: the power stays", fs=34, color=MUTED).next_to(eq, DOWN, buff=0.35)
        self.say(
            line(f"{B('Like terms')} have the same variable and the same power.",
                 "Like terms have the same variable, and the same power."),
            anims=[LaggedStart(*[GrowFromCenter(t) for t in five], FadeIn(plus), *[GrowFromCenter(t) for t in three],
                               lag_ratio=0.12, run_time=1.8)],
        )
        self.say(
            line(f"5x{sup('7')} + 3x{sup('7')} = {R('8x')}{sup(R('7'))}: add the counts.",
                 f"Five x to the seventh plus three x to the seventh {BR} is eight x to the seventh. {BR} Add the counts."),
            anims=[FadeIn(eq[0:7], shift=UP * 0.2, run_time=0.8)],
            steps=[[*[ReplacementTransform(s, t) for s, t in zip([*five, *three], eight)], FadeOut(plus),
                    FadeIn(eq[7:], shift=LEFT * 0.2)]],
        )
        self.say(
            line(f"The power {E('stays')} the same.", "The power stays the same."),
            anims=[FadeIn(not14, shift=UP * 0.2, run_time=0.7)],
        )
        self.play(FadeOut(VGroup(eight, eq, not14), shift=UP * 0.4), run_time=0.7)

    # ── Example 1(a): sort into bins, then combine ──────────────────────
    def example(self):
        p1 = poly([["("], ["x", "^{3}"], ["-", "6", "x", "^{2}"], ["+", "2", "x"], ["+", "4"], [")"]], fs=SMALL_FS)
        p2 = poly([["+"], ["("], ["x", "^{3}"], ["+", "5", "x", "^{2}"], ["-", "7", "x"], [")"]], fs=SMALL_FS)
        lines = fit(VGroup(p1, p2).arrange(DOWN, buff=0.3)).move_to(MATH + UP * 1.85)
        heads = bin_heads(MATH_Y - 0.4)
        fs = 72
        cols = [
            [ptex("x", "^{3}", fs=fs), ptex("x", "^{3}", fs=fs)],
            [ptex("-", "6", "x", "^{2}", fs=fs), ptex("+", "5", "x", "^{2}", fs=fs)],
            [ptex("+", "2", "x", fs=fs), ptex("-", "7", "x", fs=fs)],
            [ptex("+", "4", fs=fs)],
        ]
        for x, col in zip(BIN_X, cols):
            for k, m in enumerate(col):
                m.move_to([x, MATH_Y - 1.2 - 0.72 * k, 0])
        sources = [[p1.terms[1], p2.terms[2]], [p1.terms[2], p2.terms[3]], [p1.terms[3], p2.terms[4]], [p1.terms[4]]]
        merged = [ptex("2", "x", "^{3}", fs=fs), ptex("-", "x", "^{2}", fs=fs), ptex("-", "5", "x", fs=fs),
                  ptex("+", "4", fs=fs)]
        for x, m in zip(BIN_X, merged):
            m.set_color(RES_C).move_to([x, MATH_Y - 1.55, 0])
        final = poly([["="], ["2", "x", "^{3}"], ["-", "x", "^{2}"], ["-", "5", "x"], ["+", "4"]], fs=MID_FS)
        final.set_color(RES_C)
        final.terms[0].set_color(INK)
        fit(final).move_to(MATH + DOWN * 0.6)

        self.say(
            "Now add two polynomials.",
            anims=[LaggedStart(FadeIn(p1, shift=UP * 0.2), FadeIn(p2, shift=UP * 0.2), lag_ratio=0.5, run_time=1.2)],
            gap=0.2,
        )
        self.say(
            line(f"Sort the terms by type: x{sup('3')}, x{sup('2')}, x, and plain numbers…",
                 f"Sort the terms by type: {BR} x cubed, x squared, x, and plain numbers."),
            anims=[LaggedStart(*[FadeIn(h, shift=DOWN * 0.2) for h in heads], lag_ratio=0.2, run_time=1.0)],
            steps=[[LaggedStart(*[TransformFromCopy(s, d, path_arc=-0.5)
                                  for srcs, col in zip(sources, cols) for s, d in zip(srcs, col)],
                                lag_ratio=0.18, run_time=2.6)]],
        )
        self.say(
            line(f"…and combine each bin: {R('2x³ − x² − 5x + 4')}.",
                 f"Then combine each bin: {BR} two x cubed, minus x squared, minus five x, plus four."),
            anims=[*[ReplacementTransform(VGroup(*col), m) for col, m in zip(cols, merged)]],
            run_time=1.2,
            steps=[0.8, [*[ReplacementTransform(m, t) for m, t in zip(merged, final.terms[1:])],
                         FadeIn(final.terms[0]), FadeOut(heads)]],
        )
        self.play(FadeOut(VGroup(lines, final), shift=UP * 0.4), run_time=0.7)

    # ── Takeaway ────────────────────────────────────────────────────────
    def takeaway(self):
        eq = ptex("5", "x", "^{7}", "+", "3", "x", "^{7}", "=", "8", "x", "^{7}", fs=MID_FS, results=[8, 9, 10])
        hint = label("Same variable, same power: add the counts.", fs=34, color=MUTED)
        card = self.card(VGroup(eq, hint).arrange(DOWN, buff=0.4), title="LIKE TERMS")
        self.say(
            "Same variable, same power? Add the counts.",
            line("Different? Leave them alone.", f"{BR} Different? Leave them alone."),
            anims=[FadeIn(card, scale=0.94, run_time=1.0)],
        )
