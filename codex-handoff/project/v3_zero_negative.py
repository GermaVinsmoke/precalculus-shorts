from common import *


def colorize(m: MathTex, bases=(), exps=(), results=()):
    for i in bases:
        m[i].set_color(BASE_C)
    for i in exps:
        m[i].set_color(EXP_C)
    for i in results:
        m[i].set_color(RES_C)
    return m


class V3ZeroNegative(ShortScene):
    PART = "3 / 3"

    def construct(self):
        rule = self.hook()
        self.zero(rule)
        self.negative(rule)
        self.pattern()
        self.example()
        self.takeaway()
        self.outro()

    # ── Hook: 2⁰ = 1 ?! ─────────────────────────────────────────────────
    def hook(self):
        eq = colorize(tex("2", "^{0}", "=", "1", fs=HERO_FS), bases=[0], exps=[1], results=[3])
        eq.move_to(MATH)
        self.cap(
            f"Why is {B('2')}{sup(E('0'))} equal to {R('1')} — and not 0?",
            anims=[
                LaggedStart(
                    FadeIn(eq[0:2], shift=UP * 0.4),
                    FadeIn(eq[2]),
                    FadeIn(eq[3], scale=1.6),
                    lag_ratio=0.35,
                    run_time=1.4,
                )
            ],
        )
        rule = colorize(
            tex("a", "^{m}", r"\cdot", "a", "^{n}", "=", "a", "^{m+n}", fs=SMALL_FS),
            bases=[0, 3, 6],
            exps=[1, 4, 7],
        )
        rule_box = SurroundingRectangle(
            rule, color=CARD_STROKE, fill_color=CARD_FILL, fill_opacity=0.9,
            buff=0.25, corner_radius=0.18, stroke_width=2.5,
        )
        ref = VGroup(rule_box, rule).move_to(MATH + UP * 1.95)
        self.cap(
            "The answer hides in the product rule.",
            anims=[
                FadeOut(eq, shift=DOWN * 0.4, run_time=0.8),
                FadeIn(ref, shift=DOWN * 0.3, run_time=1.0),
            ],
        )
        self.hold()
        return ref

    # ── 2⁰·2³ = 2³ → 2⁰ = 1 ─────────────────────────────────────────────
    def zero(self, ref):
        z1 = colorize(
            tex("2", "^{0}", r"\cdot", "2", "^{3}", "=", "2", "^{0+3}", "=", "2", "^{3}", fs=MID_FS),
            bases=[0, 3, 6, 9],
            exps=[1, 4, 7, 10],
        )
        fit(z1).move_to(MATH + UP * 0.25)
        self.cap(
            f"Let the rule work with a {E('0')} exponent:",
            anims=[
                LaggedStart(*[FadeIn(m, shift=UP * 0.25) for m in z1], lag_ratio=0.08, run_time=1.8)
            ],
        )
        self.hold()
        z2 = colorize(tex("2", "^{0}", r"\cdot", "8", "=", "8", fs=MID_FS), bases=[0], exps=[1])
        z2.move_to(MATH + DOWN * 1.25)
        z3 = colorize(tex("2", "^{0}", "=", "1", fs=BIG_FS), bases=[0], exps=[1], results=[3])
        z3.move_to(z2)
        box = SurroundingRectangle(z3, color=RES_C, buff=0.22, corner_radius=0.16, stroke_width=4)
        self.cap(
            f"Multiplying by {B('2')}{sup(E('0'))} leaves 8 unchanged…",
            anims=[
                TransformFromCopy(z1[0:3], z2[0:3], run_time=1.3),
                TransformFromCopy(z1[3:5], z2[3], run_time=1.3),
                TransformFromCopy(z1[8], z2[4], run_time=1.3),
                TransformFromCopy(z1[9:11], z2[5], run_time=1.3),
            ],
        )
        self.cap(
            f"…so {B('2')}{sup(E('0'))} has to be {R('1')}.",
            anims=[
                Succession(
                    ReplacementTransform(z2, z3, run_time=1.1),
                    Create(box, run_time=0.8),
                )
            ],
        )
        gen = colorize(tex("a", "^{0}", "=", "1", fs=BIG_FS), bases=[0], exps=[1], results=[3])
        note = label("(a ≠ 0)", fs=40, color=MUTED)
        g = VGroup(gen, note).arrange(RIGHT, buff=0.4, aligned_edge=DOWN).move_to(MATH + UP * 0.1)
        self.cap(
            f"Any nonzero {B('base')} to the {E('0')} equals {R('1')}.",
            anims=[
                FadeOut(z1, shift=UP * 0.3),
                FadeOut(box),
                ReplacementTransform(z3, gen),
                FadeIn(note, shift=LEFT * 0.2),
            ],
            run_time=1.3,
        )
        self.hold()
        self.play(FadeOut(g, shift=UP * 0.3), run_time=0.7)

    # ── 5⁴·5⁻⁴ = 5⁰ = 1 → 5⁻⁴ = 1/5⁴ ────────────────────────────────────
    def negative(self, ref):
        n1 = colorize(
            tex("5", "^{4}", r"\cdot", "5", "^{-4}", "=", "5", "^{4+(-4)}", fs=MID_FS),
            bases=[0, 3, 6],
            exps=[1, 4, 7],
        )
        n2 = colorize(tex("=", "5", "^{0}", "=", "1", fs=MID_FS), bases=[1], exps=[2], results=[4])
        fit(n1).move_to(MATH + UP * 0.35)
        n2.next_to(n1, DOWN, buff=0.45)
        self.cap(
            f"Now try a {E('negative')} exponent.",
            anims=[
                LaggedStart(*[FadeIn(m, shift=UP * 0.25) for m in n1], lag_ratio=0.1, run_time=1.6)
            ],
        )
        self.play(FadeIn(n2, shift=UP * 0.25), run_time=0.9)
        self.hold()
        n3 = colorize(tex("5", "^{-4}", "=", r"{1", r"\over", r"5", "^{4}}", fs=MID_FS),
                      bases=[0, 5], exps=[1, 6], results=[3])
        n3.move_to(MATH + DOWN * 0.45)
        box = SurroundingRectangle(n3, color=RES_C, buff=0.25, corner_radius=0.16, stroke_width=4)
        self.cap(
            f"The product is {R('1')}, so {B('5')}{sup(E('−4'))} = {R('1')} / {B('5')}{sup(E('4'))}.",
            anims=[
                FadeOut(VGroup(n1, n2), shift=UP * 0.3, run_time=0.8),
                Succession(Wait(0.4), FadeIn(n3, shift=UP * 0.3, run_time=1.0), Create(box, run_time=0.8)),
            ],
        )
        self.hold(0.6)
        self.play(FadeOut(VGroup(n3, box, ref), shift=UP * 0.3), run_time=0.8)

    # ── Pattern check: divide by 2 each step ────────────────────────────
    def pattern(self):
        data = [("2", "4"), ("1", "2"), ("0", "1"), ("-1", r"\frac{1}{2}"), ("-2", r"\frac{1}{4}")]
        xs = np.linspace(SAFE_LEFT + 0.45, SAFE_RIGHT - 0.45, len(data))
        fs = 78
        cols = []
        for x, (e, v) in zip(xs, data):
            p = colorize(tex("2", "^{%s}" % e, fs=fs), bases=[0], exps=[1])
            eq = tex("=", fs=fs, color=MUTED).rotate(PI / 2)
            val = tex(v, fs=fs)
            col_ = VGroup(p, eq, val).arrange(DOWN, buff=0.28)
            col_.move_to([x, MATH_Y + 0.6, 0])
            cols.append(col_)
        # line the rows up regardless of glyph heights
        top_y = max(c[0].get_center()[1] for c in cols)
        for c in cols:
            c[0].set_y(top_y)
            c[1].set_y(top_y - 0.85)
            c[2].set_y(top_y - 1.85)
        arrows, divs = VGroup(), VGroup()
        low = min(c[2].get_bottom()[1] for c in cols) - 0.2
        for a, b in zip(cols[:-1], cols[1:]):
            arc = CurvedArrow(
                [a[2].get_center()[0] + 0.1, low, 0],
                [b[2].get_center()[0] - 0.1, low, 0],
                angle=PI * 0.55,
                color=MUTED,
                stroke_width=3,
                tip_length=0.14,
            )
            arrows.add(arc)
            divs.add(tex(r"\div 2", fs=40, color=MUTED).next_to(arc, DOWN, buff=0.08))
        self.cap(
            f"Check the pattern: each step right divides by {B('2')}.",
            anims=[FadeIn(cols[0], shift=UP * 0.2, run_time=0.7)],
        )
        for i in range(1, len(cols)):
            self.play(
                Create(arrows[i - 1]),
                FadeIn(divs[i - 1]),
                FadeIn(cols[i], shift=LEFT * 0.2),
                run_time=0.7,
            )
        self.snap()
        hi = VGroup(cols[2], cols[3], cols[4])
        frame = SurroundingRectangle(hi, color=RES_C, buff=0.18, corner_radius=0.16, stroke_width=4)
        self.cap(
            f"Same answers: {B('2')}{sup(E('0'))} = {R('1')}, {B('2')}{sup(E('−1'))} = {R('½')}.",
            anims=[
                Create(frame, run_time=0.9),
                *[c[2].animate(run_time=0.9).set_color(RES_C) for c in hi],
            ],
        )
        self.hold(0.4)
        self.play(FadeOut(VGroup(*cols, arrows, divs, frame), shift=UP * 0.3), run_time=0.8)

    # ── Example 2(c): (−2)⁻³ = −1/8 ─────────────────────────────────────
    def example(self):
        q = colorize(tex("(-2)", "^{-3}"), bases=[0], exps=[1])
        s1 = colorize(tex("=", r"{1", r"\over", "(-2)", "^{3}}", fs=MID_FS), bases=[3], exps=[4])
        s2 = colorize(tex("=", r"-\frac{1}{8}", fs=MID_FS), results=[1])
        stack = fit_zone(VGroup(q, s1, s2).arrange(DOWN, buff=0.45))
        self.cap(
            f"Example: flip it, then cube {B('−2')}.",
            anims=[
                Succession(
                    FadeIn(q, shift=UP * 0.3, run_time=0.9),
                    FadeIn(s1, shift=UP * 0.3, run_time=1.0),
                )
            ],
        )
        self.hold(0.3)
        self.cap(
            f"{B('(−2)')}{sup(E('3'))} = −8, so the answer is {R('−1/8')}.",
            anims=[FadeIn(s2, shift=UP * 0.3, run_time=1.0)],
        )
        self.play(Circumscribe(s2[1], color=RES_C, buff=0.12, run_time=1.2))
        self.hold()
        self.play(FadeOut(stack, shift=UP * 0.4), run_time=0.8)

    # ── Takeaway ────────────────────────────────────────────────────────
    def takeaway(self):
        zero = colorize(tex("a", "^{0}", "=", "1", fs=MID_FS), bases=[0], exps=[1], results=[3])
        neg = colorize(tex("a", "^{-n}", "=", r"{1", r"\over", "a", "^{n}}", fs=MID_FS),
                       bases=[0, 5], exps=[1, 6], results=[3])
        rows = VGroup(zero, neg).arrange(DOWN, buff=0.5)
        x0 = zero[2].get_center()[0]
        neg.shift(RIGHT * (x0 - neg[2].get_center()[0]))
        card = self.card(rows)
        self.cap(
            f"Zero gives {R('1')}. Negative means {R('1')} over.",
            anims=[FadeIn(card, scale=0.94, run_time=1.0)],
        )
