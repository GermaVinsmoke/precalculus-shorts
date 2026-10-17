from common import *


def power_product(b1, e1, b2, e2, fs=BIG_FS):
    m = tex(b1, "^{%s}" % e1, r"\cdot", b2, "^{%s}" % e2, fs=fs)
    m[0].set_color(BASE_C)
    m[3].set_color(BASE_C)
    m[1].set_color(EXP_C)
    m[4].set_color(EXP_C)
    return m


class V2ProductRule(ShortScene):
    PART = "2 / 3"

    def construct(self):
        eq = self.hook()
        row, ticks = self.expand(eq)
        full = self.collapse(eq, row, ticks)
        self.generalize(full)
        self.example()
        self.caveat()
        self.takeaway()
        self.outro()

    # ── Hook: 5⁴ · 5² = ? ───────────────────────────────────────────────
    def hook(self):
        eq = tex("5", "^{4}", r"\cdot", "5", "^{2}", "=", "?")
        eq[0].set_color(BASE_C)
        eq[3].set_color(BASE_C)
        eq[1].set_color(EXP_C)
        eq[4].set_color(EXP_C)
        eq[6].set_color(MUTED)
        eq.move_to(MATH)
        self.cap(
            "Can you simplify this without a calculator?",
            anims=[
                LaggedStart(
                    *[FadeIn(m, shift=UP * 0.35) for m in eq],
                    lag_ratio=0.12,
                    run_time=1.3,
                )
            ],
        )
        self.cap(
            "There's a shortcut. Let's discover it.",
            anims=[Wiggle(eq[6], scale_value=1.3, run_time=1.2)],
        )
        return eq

    # ── (5·5·5·5)·(5·5) → six 5s in a row ───────────────────────────────
    def expand(self, eq):
        self.play(eq.animate.scale(0.72).move_to(MATH + UP * 1.75), run_time=0.9)
        parts = ["(", "5", r"\cdot", "5", r"\cdot", "5", r"\cdot", "5", ")", r"\cdot",
                 "(", "5", r"\cdot", "5", ")"]
        ex = tex(*parts, fs=MID_FS)
        for i in (1, 3, 5, 7, 11, 13):
            ex[i].set_color(BASE_C)
        for i in (0, 8, 10, 14):
            ex[i].set_color(MUTED)
        fit(ex).move_to(MATH + DOWN * 0.1)
        brace_a = Brace(ex[1:8], DOWN, buff=0.15, color=EXP_C)
        brace_b = Brace(ex[11:14], DOWN, buff=0.15, color=EXP_C)
        lab_a = tex("4", fs=SMALL_FS, color=EXP_C).next_to(brace_a, DOWN, buff=0.12)
        lab_b = tex("2", fs=SMALL_FS, color=EXP_C).next_to(brace_b, DOWN, buff=0.12)
        self.cap(
            "Write out every single factor.",
            anims=[
                TransformFromCopy(eq[0:2], ex[0:9], run_time=1.5),
                TransformFromCopy(eq[2], ex[9], run_time=1.5),
                TransformFromCopy(eq[3:5], ex[10:15], run_time=1.5),
            ],
        )
        self.play(
            GrowFromCenter(brace_a),
            GrowFromCenter(brace_b),
            TransformFromCopy(eq[1], lab_a),
            TransformFromCopy(eq[4], lab_b),
            run_time=1.1,
        )
        self.hold()

        row = tex(*(["5", r"\cdot"] * 5 + ["5"]), fs=MID_FS)
        for i in range(0, 11, 2):
            row[i].set_color(BASE_C)
        fit(row).move_to(MATH + DOWN * 0.1)
        fives_src = [ex[i] for i in (1, 3, 5, 7, 11, 13)]
        dots_src = [ex[i] for i in (2, 4, 6, 9, 12)]
        ticks = VGroup(
            *[
                tex(str(i + 1), fs=SMALL_FS * 0.8, color=EXP_C).next_to(row[2 * i], DOWN, buff=0.35)
                for i in range(6)
            ]
        )
        self.play(
            *[ReplacementTransform(s, row[2 * i]) for i, s in enumerate(fives_src)],
            *[ReplacementTransform(s, row[2 * i + 1]) for i, s in enumerate(dots_src)],
            *[FadeOut(ex[i], scale=0.6) for i in (0, 8, 10, 14)],
            FadeOut(VGroup(brace_a, brace_b, lab_a, lab_b)),
            run_time=1.2,
        )
        self.cap(
            f"Count them all: {E('6')} factors of {B('5')}.",
            anims=[
                LaggedStart(
                    *[
                        AnimationGroup(
                            Indicate(row[2 * i], color=BASE_C, scale_factor=1.15),
                            FadeIn(t, shift=UP * 0.2),
                        )
                        for i, t in enumerate(ticks)
                    ],
                    lag_ratio=0.45,
                    run_time=2.6,
                )
            ],
        )
        self.hold()
        return row, ticks

    # ── 5⁴·5² = 5^(4+2) = 5⁶ ────────────────────────────────────────────
    def collapse(self, eq, row, ticks):
        full = tex("5", "^{4}", r"\cdot", "5", "^{2}", "=", "5", "^{4+2}", "=", "5", "^{6}", fs=MID_FS)
        for i in (0, 3, 6, 9):
            full[i].set_color(BASE_C)
        for i in (1, 4, 7):
            full[i].set_color(EXP_C)
        full[9].set_color(RES_C)
        full[10].set_color(RES_C)
        fit(full).move_to(MATH + UP * 1.75)
        self.cap(
            f"{E('4')} factors plus {E('2')} factors makes {E('6')}.",
            anims=[
                *[ReplacementTransform(eq[i], full[i]) for i in range(6)],
                FadeOut(eq[6], scale=0.5),
                TransformFromCopy(eq[0], full[6]),
                TransformFromCopy(VGroup(eq[1], eq[4]), full[7]),
            ],
            run_time=1.4,
        )
        copies = [row[i].copy() for i in range(0, 11, 2)]
        self.play(
            *[Transform(c, full[9].copy(), path_arc=0.5) for c in copies],
            Transform(ticks[5], full[10], path_arc=-0.5),
            FadeOut(VGroup(*ticks[:5])),
            FadeOut(VGroup(*[row[i] for i in range(1, 11, 2)])),
            *[FadeOut(row[i]) for i in range(0, 11, 2)],
            run_time=1.6,
        )
        self.remove(*copies, ticks[5])
        self.add(full)
        self.hold(0.3)
        self.cap(
            f"Same {B('base')}? Just add the {E('exponents')}.",
            anims=[full.animate.scale(1.12).move_to(MATH)],
            run_time=1.0,
        )
        self.play(Circumscribe(full[7], color=EXP_C, buff=0.1, run_time=1.3))
        self.hold()
        return full

    # ── aᵐ·aⁿ = aᵐ⁺ⁿ ───────────────────────────────────────────────────
    def generalize(self, full):
        gen = tex("a", "^{m}", r"\cdot", "a", "^{n}", "=", "a", "^{m+n}")
        for i in (0, 3, 6):
            gen[i].set_color(BASE_C)
        for i in (1, 4, 7):
            gen[i].set_color(EXP_C)
        fit(gen, SAFE_W - 1.0).move_to(MATH)
        box = SurroundingRectangle(gen, color=RES_C, buff=0.3, corner_radius=0.2, stroke_width=4)
        self.cap(
            f"It works for any {B('base')}, with any {E('exponents')}.",
            anims=[
                *[ReplacementTransform(full[i], gen[i]) for i in range(8)],
                FadeOut(full[8:], shift=RIGHT * 0.4),
            ],
            run_time=1.4,
        )
        self.play(Create(box), run_time=1.0)
        self.hold()
        self.play(FadeOut(VGroup(gen, box), shift=UP * 0.4), run_time=0.8)

    # ── Example 3(a): x⁴·x⁷ = x¹¹ ───────────────────────────────────────
    def example(self):
        q = power_product("x", 4, "x", 7)
        step = tex("=", "x", "^{4+7}", fs=MID_FS)
        step[1].set_color(BASE_C)
        step[2].set_color(EXP_C)
        ans = tex("=", "x", "^{11}", fs=BIG_FS)
        ans[1:].set_color(RES_C)
        stack = fit_zone(VGroup(q, step, ans).arrange(DOWN, buff=0.5))
        q_slot = q.get_center()
        q.move_to(MATH)
        self.cap(
            f"Your turn: {B('x')}{sup(E('4'))} · {B('x')}{sup(E('7'))}",
            anims=[FadeIn(q, shift=UP * 0.3, run_time=1.0)],
        )
        self.hold(1.0)  # thinking pause
        self.cap(
            f"Add the exponents: {R('x')}{sup(R('11'))}.",
            anims=[
                Succession(
                    q.animate(run_time=0.7).move_to(q_slot),
                    AnimationGroup(
                        TransformFromCopy(q[0], step[1]),
                        TransformFromCopy(VGroup(q[1], q[4]), step[2]),
                        FadeIn(step[0]),
                        run_time=1.2,
                    ),
                    FadeIn(ans, shift=UP * 0.3, run_time=0.9),
                )
            ],
        )
        self.hold()
        self.play(FadeOut(stack, shift=UP * 0.4), run_time=0.8)

    # ── Same base only ──────────────────────────────────────────────────
    def caveat(self):
        bad = power_product("2", 3, "5", 2)
        bad.move_to(MATH)
        boxes = VGroup(
            *[
                SurroundingRectangle(bad[i], color=WARN_C, buff=0.12, corner_radius=0.1, stroke_width=4)
                for i in (0, 3)
            ]
        )
        tag = label(W("different bases"), fs=40, weight=BOLD).next_to(bad, DOWN, buff=0.6)
        self.cap(
            f"Careful: the {B('bases')} must match.",
            anims=[
                Succession(
                    FadeIn(bad, shift=UP * 0.3, run_time=0.9),
                    AnimationGroup(Create(boxes), FadeIn(tag, shift=UP * 0.2), run_time=0.9),
                )
            ],
        )
        self.hold()
        self.play(FadeOut(VGroup(bad, boxes, tag), shift=UP * 0.4), run_time=0.8)

    # ── Takeaway ────────────────────────────────────────────────────────
    def takeaway(self):
        rule = tex("a", "^{m}", r"\cdot", "a", "^{n}", "=", "a", "^{m+n}")
        for i in (0, 3, 6):
            rule[i].set_color(BASE_C)
        for i in (1, 4, 7):
            rule[i].set_color(EXP_C)
        card = self.card(rule)
        self.cap(
            f"Multiply powers? {E('Add')} the exponents.",
            anims=[FadeIn(card, scale=0.94, run_time=1.0)],
        )
