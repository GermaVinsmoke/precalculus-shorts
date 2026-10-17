from common import *

BR = '<break time="0.2s" />'


def flip_sign(minus, digits, target, direction=UP):
    """Exponent travels to `target` while its minus sign flares red and drops off mid-flight."""
    return AnimationGroup(
        Succession(
            minus.animate(run_time=0.35).set_color(WARN_C).scale(1.4),
            FadeOut(minus, shift=direction * 0.5, scale=0.4, run_time=0.45),
        ),
        ReplacementTransform(digits, target, path_arc=PI * 0.6),
    )


class L4NegativeFractions(NarratedScene):
    PART = "4 / 5"

    def construct(self):
        h = self.hook()
        self.derive(h)
        self.law6()
        self.law7()
        self.example()
        self.takeaway()
        self.outro()

    # ── Hook: (3/4)⁻² = ? ───────────────────────────────────────────────
    def hook(self):
        h = auto(tex(r"\left(", "{3", r"\over", "4}", r"\right)", "^{-", "2}", "=", "?"))
        h[8].set_color(MUTED)
        h.move_to(MATH)
        self.say(
            line(f"({B('3')}/{B('4')}){sup(E('−2'))}?", "Three quarters, to the negative two?"),
            line("There's a neat trick.", f"{BR} There's a neat trick."),
            anims=[LaggedStart(FadeIn(h[0:7], shift=UP * 0.4), FadeIn(h[7:], shift=UP * 0.3),
                               lag_ratio=0.5, run_time=1.4)],
        )
        return h

    # ── Using a⁻ⁿ = 1/aⁿ ────────────────────────────────────────────────
    def derive(self, h):
        top = h[0:7]
        s1 = auto(tex("=", "{1", r"\over", r"\left(", r"\tfrac{3}{4}", r"\right)", "^{2}}", fs=MID_FS))
        s1[1].set_color(RES_C)
        s1[4].set_color(BASE_C)
        s2 = auto(tex("=", "{1", r"\over", r"\tfrac{9}{16}}", "=", r"\frac{16}{9}", fs=MID_FS))
        s2[1].set_color(RES_C)
        s3 = auto(tex("=", r"\left(", "{4", r"\over", "3}", r"\right)", "^{2}", fs=MID_FS), results=[2, 4, 6])
        for m in (s1, s2, s3):
            m.move_to(MATH + DOWN * 0.9)
        self.say(
            line(f"Remember: a negative exponent means {R('1')} over the power.",
                 "Remember: a negative exponent means one over the power."),
            anims=[
                FadeOut(h[7:], run_time=0.5),
                Succession(
                    top.animate(run_time=0.8).scale(0.45).move_to(MATH + UP * 1.6),
                    FadeIn(s1, shift=UP * 0.3, run_time=1.0),
                ),
            ],
        )
        self.say(
            line(f"One over 9/16 is 16/9…", f"One over nine sixteenths {BR} is sixteen ninths…"),
            line(f"…which is ({B('4')}/{B('3')}){sup(E('2'))}.", "…which is four thirds, squared."),
            anims=[
                Succession(
                    ReplacementTransform(s1, s2, run_time=1.0),
                    Wait(1.8),
                    ReplacementTransform(s2, s3, run_time=1.0),
                )
            ],
        )
        self.play(FadeOut(VGroup(top, s3), shift=UP * 0.4), run_time=0.7)

    # ── Law 6: the fraction flips ───────────────────────────────────────
    def law6(self):
        f = auto(tex(r"\left(", "{3", r"\over", "4}", r"\right)", "^{-", "2}", fs=HERO_FS))
        g = auto(tex(r"\left(", "{4", r"\over", "3}", r"\right)", "^{2}", fs=HERO_FS), results=[1, 3, 5])
        f.move_to(MATH)
        g.move_to(MATH)
        self.play(FadeIn(f, scale=0.9), run_time=0.8)
        self.say(
            line("The fraction flips, and the exponent turns positive.",
                 f"So the fraction flips, {BR} and the exponent turns positive."),
            anims=[
                Succession(
                    Wait(0.4),
                    AnimationGroup(
                        ReplacementTransform(f[1], g[3], path_arc=-PI * 0.9),
                        ReplacementTransform(f[3], g[1], path_arc=-PI * 0.9),
                        ReplacementTransform(f[0], g[0]),
                        ReplacementTransform(f[2], g[2]),
                        ReplacementTransform(f[4], g[4]),
                        flip_sign(f[5], f[6], g[5]),
                        run_time=1.8,
                    ),
                )
            ],
        )
        law6 = auto(tex(r"\left(", "{a", r"\over", "b}", r"\right)", "^{-n}", "=", r"\left(", "{b", r"\over",
                        "a}", r"\right)", "^{n}"))
        fit(law6).move_to(MATH)
        self.say(
            "That's Law 6.",
            anims=[FadeOut(g, shift=UP * 0.3, run_time=0.6), FadeIn(law6, shift=UP * 0.3, run_time=0.9)],
            gap=0.8,
        )
        self.play(FadeOut(law6, shift=UP * 0.4), run_time=0.6)

    # ── Law 7: factors hop across the bar ───────────────────────────────
    def law7(self):
        f = auto(tex("{3", "^{-", "2}", r"\over", "4", "^{-", "5}}", fs=HERO_FS))
        g = auto(tex("{4", "^{5}", r"\over", "3", "^{2}}", fs=HERO_FS))
        f.move_to(MATH)
        g.move_to(MATH)
        self.say(
            "Inside a fraction, a factor can hop across the bar…",
            line("…and its exponent changes sign.", f"{BR} …and its exponent changes sign."),
            anims=[
                Succession(
                    FadeIn(f, scale=0.9, run_time=0.8),
                    Wait(1.0),
                    AnimationGroup(
                        ReplacementTransform(f[0], g[3], path_arc=-PI * 0.8),
                        flip_sign(f[1], f[2], g[4], DOWN),
                        ReplacementTransform(f[4], g[0], path_arc=-PI * 0.8),
                        flip_sign(f[5], f[6], g[1], UP),
                        ReplacementTransform(f[3], g[2]),
                        run_time=2.0,
                    ),
                )
            ],
        )
        law7 = auto(tex("{a", "^{-n}", r"\over", "b", "^{-m}}", "=", "{b", "^{m}", r"\over", "a", "^{n}}"))
        law7.move_to(MATH)
        self.say(
            "That's Law 7.",
            anims=[FadeOut(g, shift=UP * 0.3, run_time=0.6), FadeIn(law7, shift=UP * 0.3, run_time=0.9)],
            gap=0.8,
        )
        self.play(FadeOut(law7, shift=UP * 0.4), run_time=0.6)

    # ── Example 5(a): 6st⁻⁴ / 2s⁻²t² = 3s³/t⁶ ───────────────────────────
    def example(self):
        e0 = auto(tex("{6", "s", "t", "^{-", "4}", r"\over", "2", "s", "^{-", "2}", "t", "^{2}}", fs=BIG_FS),
                  digits=False)
        e1 = auto(tex("{6", "s", "s", "^{2}", r"\over", "2", "t", "^{2}", "t", "^{4}}", fs=BIG_FS), digits=False)
        e2 = auto(tex("{3", "s", "^{3}", r"\over", "t", "^{6}}", fs=BIG_FS), digits=False)
        e2.set_color(RES_C)
        for m in (e0, e1, e2):
            m.move_to(MATH)
        self.say(
            line(f"Example: {B('t')}{sup(E('−4'))} hops down, {B('s')}{sup(E('−2'))} hops up.",
                 f"Example: {BR} t to the negative fourth hops down, {BR} s to the negative second hops up."),
            anims=[
                Succession(
                    FadeIn(e0, shift=UP * 0.3, run_time=0.9),
                    Wait(0.8),
                    AnimationGroup(
                        ReplacementTransform(e0[2], e1[8], path_arc=-PI * 0.8),
                        flip_sign(e0[3], e0[4], e1[9], DOWN),
                        run_time=1.5,
                    ),
                    AnimationGroup(
                        ReplacementTransform(e0[7], e1[2], path_arc=-PI * 0.8),
                        flip_sign(e0[8], e0[9], e1[3], UP),
                        *[ReplacementTransform(e0[i], e1[j]) for i, j in ((0, 0), (1, 1), (5, 4), (6, 5), (10, 6), (11, 7))],
                        run_time=1.5,
                    ),
                )
            ],
        )
        self.say(
            line(f"Then simplify: {R('3s')}{sup(R('3'))} over {R('t')}{sup(R('6'))}.",
                 f"Then simplify: {BR} three s cubed, over t to the sixth."),
            anims=[
                ReplacementTransform(VGroup(e1[0], e1[5]), e2[0]),
                ReplacementTransform(VGroup(e1[1], e1[2]), e2[1]),
                ReplacementTransform(e1[3], e2[2]),
                ReplacementTransform(e1[4], e2[3]),
                ReplacementTransform(VGroup(e1[6], e1[8]), e2[4]),
                ReplacementTransform(VGroup(e1[7], e1[9]), e2[5]),
            ],
            run_time=1.4,
        )
        self.play(FadeOut(e2, shift=UP * 0.4), run_time=0.7)

    # ── Takeaway ────────────────────────────────────────────────────────
    def takeaway(self):
        law6 = auto(tex(r"\left(", "{a", r"\over", "b}", r"\right)", "^{-n}", "=", r"\left(", "{b", r"\over",
                        "a}", r"\right)", "^{n}"))
        law7 = auto(tex("{a", "^{-n}", r"\over", "b", "^{-m}}", "=", "{b", "^{m}", r"\over", "a", "^{n}}"))
        rows = VGroup(law6, law7).arrange(DOWN, buff=0.5)
        law7.shift(RIGHT * (law6[6].get_x() - law7[5].get_x()))
        card = self.card(rows, title="LAWS 6 &amp; 7")
        self.say(
            "Negative exponent?",
            line("Flip it across the bar, and make it positive.", f"{BR} Flip it across the bar, and make it positive."),
            anims=[FadeIn(card, scale=0.94, run_time=1.0)],
        )
