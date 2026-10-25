try:
    from .rad_common import *
except ImportError:  # Manim loading this file directly
    from rad_common import *

ZONE = MATH + DOWN * 0.35  # below the reference question


class R3Simplifying(RadScene):
    PART = "3 / 4"

    def construct(self):
        q = self.hook()
        self.product()
        self.escape(q)
        self.example()
        self.takeaway()
        self.outro()

    # ── Hook: ∛(x⁴) = ? ─────────────────────────────────────────────────
    def hook(self):
        q = rtex(rt(3), "x", "^{4}}", "=", "?", fs=HERO_FS * 0.8)
        q[4].set_color(MUTED)
        q.move_to(MATH)
        self.say(
            line(f"How do you simplify the cube root of x{sup('4')}?",
                 "How do you simplify the cube root of x to the fourth?"),
            anims=[LaggedStart(FadeIn(q[0:3], shift=UP * 0.4), FadeIn(q[3:], shift=UP * 0.3),
                               lag_ratio=0.5, run_time=1.4)],
        )
        self.play(q.animate.scale(0.45).move_to(MATH + UP * 2.0), run_time=0.8)
        return q

    # ── Product: the √ sign splits in two ───────────────────────────────
    def product(self):
        p0 = rtex(rt(3), "8", r"\cdot", "27}", fs=SMALL_FS)
        p1 = rtex("=", rt(3), "8}", r"\cdot", rt(3), "27}", fs=SMALL_FS)
        p2 = rtex("=", "2", r"\cdot", "3", "=", "6", fs=SMALL_FS, results=[1, 3, 5])
        stack = VGroup(p0, p1, p2).arrange(DOWN, buff=0.4).move_to(ZONE)
        self.say(
            "First: a root splits over multiplication.",
            line("The cube root of 8 · 27 is 2 · 3 = 6.",
                 f"The cube root of eight times twenty-seven {BR} is two times three: {BR} six."),
            anims=[FadeIn(p0, shift=UP * 0.3, run_time=0.8)],
            steps=[
                [FadeIn(p1[0]), TransformFromCopy(p0[0], p1[1]), TransformFromCopy(p0[0], p1[4]),
                 TransformFromCopy(p0[1], p1[2]), TransformFromCopy(p0[2], p1[3]), TransformFromCopy(p0[3], p1[5])],
                [FadeIn(p2, shift=UP * 0.2)],
            ],
        )
        self.play(FadeOut(stack, shift=UP * 0.3), run_time=0.6)

    # ── Back to ∛(x⁴): a group of three escapes ─────────────────────────
    def escape(self, q):
        src = rtex(rt(3), "x", r"\cdot", "x", r"\cdot", "x", r"\cdot", "x}")
        src.move_to(ZONE)
        group = SurroundingRectangle(VGroup(src[1], src[5]), color=EXP_C, buff=0.14, corner_radius=0.14,
                                     stroke_width=4)
        trio = label(E("a group of three"), fs=34, weight=BOLD).next_to(group, DOWN, buff=0.25)
        tgt = rtex("x", rt(3), "x}").move_to(ZONE)
        tgt[0].set_color(RES_C)
        self.say(
            line(f"Back to x{sup('4')}: write out the four factors.",
                 "Back to x to the fourth: write out the four factors."),
            anims=[LaggedStart(*[FadeIn(m, shift=DOWN * 0.3) for m in src], lag_ratio=0.12, run_time=1.4)],
        )
        self.say(
            "A cube root frees every group of three:",
            line(f"one x {R('escapes')}, one stays inside.", f"{BR} one x escapes, {BR} and one stays inside."),
            anims=[Create(group, run_time=0.8), FadeIn(trio, shift=UP * 0.2, run_time=0.8)],
            steps=[
                [ReplacementTransform(VGroup(src[1], src[3], src[5]), tgt[0], path_arc=-PI / 3),
                 ReplacementTransform(src[0], tgt[1]), ReplacementTransform(src[7], tgt[2]),
                 FadeOut(VGroup(src[2], src[4], src[6], group, trio))],
            ],
        )
        final = rtex(rt(3), "x", "^{4}}", "=", rt(3), "x", "^{3}", r"\cdot", "x}", "=", "x", rt(3), "x}",
                     fs=MID_FS, results=[10, 12])
        final[11][0].set_color(EXP_C)
        fit(final).move_to(MATH)
        self.say(
            line(f"So it's {R('x')} times the cube root of x.", "So it's x, times the cube root of x."),
            anims=[
                ReplacementTransform(q[0:4], final[0:4]),
                FadeOut(q[4]),
                ReplacementTransform(tgt, final[10:13]),
                FadeIn(final[4:10], shift=DOWN * 0.2),
            ],
            run_time=1.3,
        )
        self.play(FadeOut(final, shift=UP * 0.4), run_time=0.7)

    # ── Example 9(b): ⁴√(81x⁸y⁴) = 3x²|y| ───────────────────────────────
    def example(self):
        l1 = rtex(rt(4), "81", "x", "^{8}", "y", "^{4}}")
        l2 = rtex("=", rt(4), "81}", r"\cdot", rt(4), "x", "^{8}}", r"\cdot", rt(4), "y", "^{4}}", fs=SMALL_FS)
        l3 = rtex("=", "3", "x", "^{2}", "|y|", fs=MID_FS, results=[1, 2, 3, 4])
        stack = fit_zone(VGroup(l1, l2, l3).arrange(DOWN, buff=0.45))
        self.say(
            line(f"One more: the 4th root of 81x{sup('8')}y{sup('4')}.",
                 f"One more: {BR} the fourth root of eighty-one, x to the eighth, y to the fourth."),
            anims=[FadeIn(l1, shift=UP * 0.3, run_time=0.9)],
            steps=[[FadeIn(l2[0]), FadeIn(l2[3]), FadeIn(l2[7]),
                    *[TransformFromCopy(l1[0], l2[i]) for i in (1, 4, 8)],
                    TransformFromCopy(l1[1], l2[2]), TransformFromCopy(l1[2:4], l2[5:7]),
                    TransformFromCopy(l1[4:6], l2[9:11])]],
        )
        self.say(
            line(f"81 gives {R('3')}, x{sup('8')} gives {R('x')}{sup(R('2'))}, y{sup('4')} gives {R('|y|')}.",
                 f"Eighty-one gives three, {BR} x to the eighth, x squared, {BR} "
                 "and y to the fourth, absolute value of y."),
            anims=[LaggedStart(*[FadeIn(m, shift=UP * 0.2) for m in l3], lag_ratio=0.35, run_time=2.4)],
        )
        self.play(FadeOut(stack, shift=UP * 0.4), run_time=0.7)

    # ── Takeaway ────────────────────────────────────────────────────────
    def takeaway(self):
        r1 = rtex(rt("n"), "ab}", "=", rt("n"), "a}", rt("n"), "b}", fs=MID_FS)
        note = label(f"Then pull out every group of {E('n')}.", fs=36, color=MUTED)
        card = self.card(VGroup(r1, note).arrange(DOWN, buff=0.4), title="SIMPLIFYING ROOTS")
        self.say(
            "Split the root,",
            line("then pull out the perfect powers.", f"{BR} then pull out the perfect powers."),
            anims=[FadeIn(card, scale=0.94, run_time=1.0)],
        )
