from rat_common import *


def coef(m: MathTex, *idx):
    """Plain coefficients (the 2 and 3 in 2√x, 3∛x) stay white."""
    for i in idx:
        m[i].set_color(INK)
    return m


def pie(center, r=0.66, filled=(), color=BASE_C):
    """A circle cut into sixths; `filled` sector indexes are coloured in."""
    sectors = VGroup()
    for k in range(6):
        s = AnnularSector(inner_radius=0, outer_radius=r, angle=TAU / 6, start_angle=PI / 2 - (k + 1) * TAU / 6,
                          fill_color=color if k in filled else CARD_FILL, fill_opacity=0.9 if k in filled else 0.6,
                          stroke_color=MUTED, stroke_width=2)
        sectors.add(s)
    return sectors.move_to(center)


class Q3Translating(RatScene):
    PART = "3 / 3"

    def construct(self):
        t = self.hook_and_translate()
        prod = self.multiply(t)
        self.pies(prod)
        self.nested()
        self.takeaway()
        self.outro()

    # ── (2√x)(3∛x): radicals turn into exponents ────────────────────────
    def hook_and_translate(self):
        q = coef(rtex("(", "2", rt(), "x}", ")", "(", "3", rt(3), "x}", ")"), 1, 6)
        fit(q).move_to(MATH)
        self.say(
            line("How do you multiply 2√x by 3 · cube root of x?",
                 f"How do you multiply two root x, {BR} by three cube root x?"),
            anims=[LaggedStart(*[FadeIn(m, shift=UP * 0.3) for m in q], lag_ratio=0.1, run_time=1.6)],
        )
        t = coef(auto(tex("(", "2", "x", "^{1/2}", ")", "(", "3", "x", "^{1/3}", ")")), 1, 6)
        fit(t).move_to(MATH)
        self.say(
            line(f"Translate: √x is x{sup(E('1/2'))}, cube root of x is x{sup(E('1/3'))}.",
                 f"Translate each radical into an exponent: {BR} root x is x to the one half, "
                 f"{BR} cube root of x is x to the one third."),
            anims=[
                Succession(
                    Wait(1.6),
                    AnimationGroup(
                        *[ReplacementTransform(q[i], t[i]) for i in (0, 1, 4, 5, 6, 9)],
                        ReplacementTransform(q[3], t[2]),
                        ReplacementTransform(q[2], t[3], path_arc=-PI / 2),
                        run_time=1.4,
                    ),
                    Wait(1.0),
                    AnimationGroup(
                        ReplacementTransform(q[8], t[7]),
                        ReplacementTransform(q[7], t[8], path_arc=-PI / 2),
                        run_time=1.4,
                    ),
                )
            ],
        )
        return t

    # ── Multiply numbers, add exponents ─────────────────────────────────
    def multiply(self, t):
        prod = coef(auto(tex("6", "x", r"^{\frac12 + \frac13}", fs=BIG_FS)), 0)
        prod.move_to(MATH + UP * 1.3)
        self.say(
            line(f"Multiply the numbers, {E('add')} the exponents.", f"Multiply the numbers, {BR} and add the exponents."),
            anims=[t.animate(run_time=0.8).scale(0.8).move_to(MATH + DOWN * 0.4)],
            steps=[[TransformFromCopy(VGroup(t[1], t[6]), prod[0]),
                    TransformFromCopy(VGroup(t[2], t[7]), prod[1]),
                    TransformFromCopy(VGroup(t[3], t[8]), prod[2]),
                    FadeOut(t, shift=DOWN * 0.3)]],
        )
        return prod

    # ── Fraction pies: 1/2 + 1/3 = 5/6 ──────────────────────────────────
    def pies(self, prod):
        y = MATH_Y - 0.55
        xs = (CX - 2.45, CX, CX + 2.45)
        p1 = pie([xs[0], y, 0], filled=range(3), color=BASE_C)
        p2 = pie([xs[1], y, 0], filled=range(2), color=EXP_C)
        p3 = pie([xs[2], y, 0])
        plus = tex("+", fs=MID_FS).move_to([(xs[0] + xs[1]) / 2, y, 0])
        eq = tex("=", fs=MID_FS).move_to([(xs[1] + xs[2]) / 2, y, 0])
        l1 = tex(r"\tfrac12 = \tfrac36", fs=50, color=BASE_C).next_to(p1, DOWN, buff=0.22)
        l2 = tex(r"\tfrac13 = \tfrac26", fs=50, color=EXP_C).next_to(p2, DOWN, buff=0.22)
        l3 = tex(r"\tfrac56", fs=58, color=RES_C).next_to(p3, DOWN, buff=0.22)
        moved = VGroup(*[p1[k].copy() for k in range(3)], *[p2[k].copy() for k in range(2)])
        targets = [p3[k].copy().set_fill(BASE_C, 0.9) for k in range(3)] + \
                  [p3[k].copy().set_fill(EXP_C, 0.9) for k in (3, 4)]
        self.say(
            line("One half plus one third…", "One half plus one third:"),
            line("…is 3 sixths plus 2 sixths: five sixths.", f"{BR} that's three sixths plus two sixths, {BR} five sixths."),
            anims=[LaggedStart(FadeIn(p1, scale=0.8), FadeIn(plus), FadeIn(p2, scale=0.8), FadeIn(eq), FadeIn(p3, scale=0.8),
                               lag_ratio=0.25, run_time=1.6)],
            steps=[
                [FadeIn(l1, shift=UP * 0.15), FadeIn(l2, shift=UP * 0.15)],
                [*[Transform(m, tg, path_arc=-0.6) for m, tg in zip(moved, targets)]],
            ],
        )
        result = coef(auto(tex("6", "x", "^{5/6}", fs=BIG_FS), results=[1, 2]), 0)
        result[0].set_color(RES_C)
        result.move_to(prod)
        self.say(
            line(f"So it's {R('6x')}{sup(R('5/6'))}.", "So the answer is six x to the five sixths."),
            anims=[FadeIn(l3, shift=UP * 0.15, run_time=0.6), ReplacementTransform(prod, result, run_time=1.2)],
        )
        self.play(FadeOut(VGroup(p1, p2, p3, moved, plus, eq, l1, l2, l3, result), shift=UP * 0.4), run_time=0.7)

    # ── Example 13(c): √(x√x) = x^(3/4) ─────────────────────────────────
    def nested(self):
        l1 = rtex(rt(), "x", rt(), "x}}")
        l2 = auto(tex("=", "(", "x", r"\cdot", "x", "^{1/2}", ")", "^{1/2}", fs=MID_FS))
        l3 = auto(tex("=", "(", "x", "^{3/2}", ")", "^{1/2}", fs=MID_FS))
        l4 = auto(tex("=", "x", "^{3/4}", fs=MID_FS), results=[1, 2])
        stack = fit_zone(VGroup(l1, l2, l3, l4).arrange(DOWN, buff=0.3))
        self.say(
            line("Nested roots get easy too:", "Nested roots get easy too:"),
            line(f"x · √x is x{sup(E('3/2'))}, and the root of that is {R('x')}{sup(R('3/4'))}.",
                 f"{BR} x times root x is x to the three halves, {BR} and the square root of that is x to the three fourths."),
            anims=[FadeIn(l1, shift=UP * 0.3, run_time=0.9)],
            steps=[[FadeIn(l2, shift=UP * 0.2)], 0.8, [FadeIn(l3, shift=UP * 0.2)], 1.6, [FadeIn(l4, shift=UP * 0.2)]],
        )
        self.play(FadeOut(stack, shift=UP * 0.4), run_time=0.7)

    # ── Takeaway ────────────────────────────────────────────────────────
    def takeaway(self):
        rule = rtex(rt("n"), "a", "^{m}}", "=", "a", "^{m/n}", fs=BIG_FS)
        hint = label("…then let the Laws of Exponents work", fs=34, color=MUTED)
        card = self.card(VGroup(rule, hint).arrange(DOWN, buff=0.4), title="TRANSLATE FIRST")
        self.say(
            "Radicals into exponents,",
            line("then let the laws do the work.", f"{BR} then let the laws do the work."),
            anims=[FadeIn(card, scale=0.94, run_time=1.0)],
        )
