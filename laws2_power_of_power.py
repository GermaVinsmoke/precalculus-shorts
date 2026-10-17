from common import *

BR = '<break time="0.2s" />'


class L2PowerOfPower(NarratedScene):
    PART = "2 / 5"

    def construct(self):
        h = self.hook()
        cols, grid = self.groups(h)
        full = self.count(h, cols, grid)
        self.contrast(full)
        self.example()
        self.takeaway()
        self.outro()

    # ── Hook: (3²)⁵ = 3⁷? ───────────────────────────────────────────────
    def hook(self):
        h = auto(tex("(", "3", "^{2}", ")", "^{5}", "=", "3", "^{7}", "?"))
        h[8].set_color(WARN_C)
        h.move_to(MATH)
        self.say(
            line(f"({B('3')}{sup(E('2'))}){sup(E('5'))}…", "Three squared, all to the fifth."),
            line(f"Is it {B('3')}{sup(E('7'))}?", "Is it three to the seventh?"),
            anims=[
                Succession(
                    FadeIn(h[0:5], shift=UP * 0.4, run_time=0.9),
                    Wait(0.9),
                    LaggedStart(*[FadeIn(m, shift=UP * 0.3) for m in h[5:]], lag_ratio=0.2, run_time=1.0),
                )
            ],
        )
        return h

    # ── Five copies → a grid of 5 groups × 2 ────────────────────────────
    def groups(self, h):
        copies = auto(tex(*(["(", "3", "^{2}", ")"] * 5), fs=MID_FS))
        fit(copies).move_to(MATH + DOWN * 0.3)
        top = h[0:5]
        self.say(
            line(f"To the fifth means five copies of {B('3')}{sup(E('2'))}.",
                 "To the fifth means five copies of three squared."),
            anims=[
                FadeOut(h[5:], shift=RIGHT * 0.4, run_time=0.6),
                Succession(
                    top.animate(run_time=0.8).scale(0.6).move_to(MATH + UP * 1.85),
                    LaggedStart(
                        *[TransformFromCopy(top[0:4], copies[4 * i:4 * i + 4]) for i in range(5)],
                        lag_ratio=0.25,
                        run_time=1.8,
                    ),
                ),
            ],
        )
        xs = np.linspace(CX - 2.8, CX + 2.8, 5)
        cols = VGroup()
        boxes = VGroup()
        for x in xs:
            c = VGroup(tex("3", fs=MID_FS, color=BASE_C), tex("3", fs=MID_FS, color=BASE_C)).arrange(DOWN, buff=0.2)
            c.move_to([x, MATH_Y - 0.25, 0])
            cols.add(c)
            boxes.add(SurroundingRectangle(c, color=EXP_C, buff=0.16, corner_radius=0.16, stroke_width=3))
        grid = VGroup(cols, boxes)
        lbl = label(f"{E('5')} groups × {E('2')} factors", fs=40).next_to(grid, DOWN, buff=0.35)
        self.say(
            line(f"Each one is two factors of {B('3')}.", "Each one is two factors of three."),
            line("Five groups of two.", f"{BR} Five groups of two."),
            anims=[
                LaggedStart(
                    *[
                        FadeTransform(copies[4 * i:4 * i + 4], VGroup(boxes[i], cols[i]))
                        for i in range(5)
                    ],
                    lag_ratio=0.2,
                    run_time=2.0,
                ),
                Succession(Wait(2.2), FadeIn(lbl, shift=UP * 0.2, run_time=0.7)),
            ],
        )
        self.lbl = lbl
        return cols, grid

    # ── 5 × 2 = 10 factors → 3¹⁰ ────────────────────────────────────────
    def count(self, h, cols, grid):
        threes = [t for c in cols for t in c]
        ticks = VGroup(
            *[
                tex(str(i + 1), fs=40, color=EXP_C).next_to(t, UR, buff=0.02).shift(LEFT * 0.12)
                for i, t in enumerate(threes)
            ]
        )
        full = auto(tex("(", "3", "^{2}", ")", "^{5}", "=", "3", r"^{2 \cdot 5}", "=", "3", "^{10}"),
                    results=[9, 10])
        fit(full).move_to(MATH)
        copies = [t.copy() for t in threes]
        self.say(
            line(f"Five times two: ten factors.", f"That's five times two: {BR} ten factors."),
            line(f"{R('3')}{sup(R('10'))}.", "Three to the tenth."),
            anims=[
                Succession(
                    LaggedStart(*[FadeIn(t, scale=1.5) for t in ticks], lag_ratio=0.25, run_time=2.2),
                    AnimationGroup(
                        ReplacementTransform(h[0:5], full[0:5]),
                        *[Transform(c, full[9].copy(), path_arc=0.4) for c in copies],
                        FadeOut(VGroup(grid, ticks, self.lbl)),
                        FadeIn(full[5:9]),
                        FadeIn(full[10], shift=DOWN * 0.2),
                        run_time=1.4,
                    ),
                )
            ],
        )
        self.remove(*copies)
        self.add(full)
        self.play(Circumscribe(full[7], color=EXP_C, buff=0.1), run_time=1.2)
        return full

    # ── Add (Law 1) vs multiply (Law 3) ─────────────────────────────────
    def contrast(self, full):
        prod = auto(tex("3", "^{2}", r"\cdot", "3", "^{5}", "=", "3", "^{2+5}", "=", "3", "^{7}"))
        rows = VGroup(prod, full.copy()).arrange(DOWN, buff=0.8)
        for r in rows:
            fit(r)
        rows.move_to(MATH)
        self.say(
            line(f"Multiplying {B('3')}{sup(E('2'))} by {B('3')}{sup(E('5'))} adds: {B('3')}{sup(E('7'))}.",
                 "Three squared times three to the fifth adds, to three to the seventh."),
            line(f"A power of a power {E('multiplies')}.", f"{BR} But a power of a power multiplies."),
            anims=[
                Succession(
                    AnimationGroup(
                        full.animate.move_to(rows[1]).match_width(rows[1]),
                        FadeIn(prod, shift=DOWN * 0.3),
                        run_time=1.0,
                    ),
                    Circumscribe(prod[7], color=EXP_C, buff=0.08, run_time=1.2),
                    Wait(1.2),
                    Circumscribe(full[7], color=EXP_C, buff=0.08, run_time=1.2),
                )
            ],
        )
        self.play(FadeOut(VGroup(prod, full), shift=UP * 0.4), run_time=0.7)

    # ── Example 3(d): (b⁴)⁵ = b²⁰ ───────────────────────────────────────
    def example(self):
        qx = auto(tex("(", "b", "^{4}", ")", "^{5}"))
        step = auto(tex("=", "b", r"^{4 \cdot 5}", fs=MID_FS))
        ans = auto(tex("=", "b", "^{20}"), results=[1, 2])
        stack = fit_zone(VGroup(qx, step, ans).arrange(DOWN, buff=0.4))
        slot = qx.get_center()
        qx.move_to(MATH)
        self.say(
            line(f"Try it: ({B('b')}{sup(E('4'))}){sup(E('5'))}.", f"Try it: {BR} b to the fourth, all to the fifth."),
            anims=[FadeIn(qx, shift=UP * 0.3, run_time=1.0)],
            gap=1.2,
        )
        self.say(
            line(f"Four times five: {R('b')}{sup(R('20'))}.", f"Four times five: {BR} b to the twentieth."),
            anims=[
                Succession(
                    qx.animate(run_time=0.7).move_to(slot),
                    AnimationGroup(
                        FadeIn(step[0]),
                        TransformFromCopy(qx[1], step[1]),
                        TransformFromCopy(VGroup(qx[2], qx[4]), step[2]),
                        run_time=1.1,
                    ),
                    FadeIn(ans, shift=UP * 0.3, run_time=0.9),
                )
            ],
        )
        self.play(FadeOut(stack, shift=UP * 0.4), run_time=0.7)

    # ── Takeaway ────────────────────────────────────────────────────────
    def takeaway(self):
        law3 = auto(tex("(", "a", "^{m}", ")", "^{n}", "=", "a", "^{mn}"))
        card = self.card(law3, title="LAW 3")
        self.say(
            "A power of a power?",
            line(f"{E('Multiply')} the exponents.", f"{BR} Multiply the exponents."),
            anims=[FadeIn(card, scale=0.94, run_time=1.0)],
        )
