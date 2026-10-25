try:
    from .rat_common import *
except ImportError:  # Manim loading this file directly
    from rat_common import *

VAL_Y = MATH_Y + 0.5  # values row
POW_Y = MATH_Y - 0.5  # powers row (labels under the values)


class Q1WhatItMeans(RatScene):
    PART = "1 / 3"

    def construct(self):
        self.hook()
        self.staircase()
        self.laws_agree()
        self.examples()
        self.takeaway()
        self.outro()

    # ── Hook: 9^(1/2) = ? ───────────────────────────────────────────────
    def hook(self):
        q = auto(tex("9", "^{1/2}", "=", "?", fs=HERO_FS))
        q[3].set_color(MUTED)
        q.move_to(MATH)
        self.say(
            line(f"What does {B('9')}{sup(E('1/2'))} mean?", "What does nine to the one half mean?"),
            line("You can't multiply 9 by itself half a time.",
                 f"{BR} You can't multiply nine by itself half a time."),
            anims=[LaggedStart(FadeIn(q[0:2], shift=UP * 0.4), FadeIn(q[2:], shift=UP * 0.3),
                               lag_ratio=0.5, run_time=1.4)],
        )
        self.play(FadeOut(q, shift=UP * 0.4), run_time=0.6)

    # ── Two equal half-steps make one ×9 step ───────────────────────────
    def staircase(self):
        xs = [CX - 2.5, CX, CX + 2.5]
        vals = [tex("1", fs=BIG_FS), tex("?", fs=BIG_FS, color=MUTED), tex("9", fs=BIG_FS)]
        pows = [pw("9", "0", fs=SMALL_FS), pw("9", "1/2", fs=SMALL_FS), pw("9", "1", fs=SMALL_FS)]
        for x, v, p in zip(xs, vals, pows):
            v.move_to([x, VAL_Y, 0])
            p.move_to([x, POW_Y, 0])
        big = ArcBetweenPoints(pows[0].get_bottom() + DOWN * 0.2, pows[2].get_bottom() + DOWN * 0.2,
                               angle=PI * 0.5, color=BASE_C, stroke_width=4)
        big.add_tip(tip_length=0.2)
        big_lbl = tex(r"\times 9", fs=64, color=BASE_C).next_to(big, DOWN, buff=0.12)
        halves = VGroup()
        half_lbls = VGroup()
        for a, b in ((vals[0], vals[1]), (vals[1], vals[2])):
            arc = ArcBetweenPoints(a.get_top() + UP * 0.15, b.get_top() + UP * 0.15, angle=-PI * 0.6,
                                   color=EXP_C, stroke_width=4)
            arc.add_tip(tip_length=0.18)
            halves.add(arc)
            half_lbls.add(tex(r"\times\, ?", fs=56, color=EXP_C).next_to(arc, UP, buff=0.08))
        threes = VGroup(*[tex(r"\times 3", fs=56, color=RES_C).move_to(l) for l in half_lbls])
        answer = tex("3", fs=BIG_FS, color=RES_C).move_to(vals[1])

        self.say(
            line(f"From {B('9')}{sup(E('0'))} to {B('9')}{sup(E('1'))}, we multiply by 9.",
                 "From nine to the zero, to nine to the one, we multiply by nine."),
            anims=[
                LaggedStart(*[FadeIn(VGroup(v, p), shift=UP * 0.2) for v, p in zip(vals, pows)],
                            lag_ratio=0.3, run_time=1.5),
                Succession(Wait(1.8), AnimationGroup(Create(big), FadeIn(big_lbl), run_time=1.1)),
            ],
        )
        self.say(
            line("Two equal half steps: a number that, times itself, is 9.",
                 f"Two equal half steps need a number that, times itself, is nine."),
            anims=[LaggedStart(*[AnimationGroup(Create(h), FadeIn(l)) for h, l in zip(halves, half_lbls)],
                               lag_ratio=0.6, run_time=2.0)],
        )
        self.say(
            line(f"That's {R('3')}: {B('9')}{sup(E('1/2'))} is the square root of 9.",
                 f"That's three: {BR} nine to the one half is the square root of nine."),
            anims=[*[Transform(l, t) for l, t in zip(half_lbls, threes)],
                   Succession(Wait(1.2), ReplacementTransform(vals[1], answer, run_time=0.9))],
            run_time=None,
        )
        self.play(FadeOut(VGroup(*vals[0:1], *vals[2:], answer, *pows, big, big_lbl, halves, half_lbls),
                          shift=UP * 0.4), run_time=0.7)

    # ── The laws of exponents say the same thing ────────────────────────
    def laws_agree(self):
        chain = auto(tex("(", "a", "^{1/2}", ")", "^{2}", "=", "a", r"^{\frac12 \cdot 2}", "=", "a", "^{1}",
                         fs=MID_FS))
        fit(chain).move_to(MATH + UP * 1.25)
        concl = rtex("a", "^{1/2}", "=", rt(), "a}", fs=BIG_FS, results=[3, 4])
        concl[3][:].set_color(INK)
        concl[4].set_color(RES_C)
        concl.move_to(MATH - UP * 0.65)
        box = SurroundingRectangle(concl, color=RES_C, buff=0.22, corner_radius=0.16, stroke_width=3.5)
        gen = rtex("a", "^{1/n}", "=", rt("n"), "a}", fs=BIG_FS)
        gen.move_to(concl)
        self.say(
            line(f"The laws agree: (a{sup('1/2')}){sup('2')} = a, so a{sup('1/2')} = √a.",
                 f"The laws agree: {BR} a to the one half, squared, is a. {BR} So it's root a."),
            anims=[LaggedStart(*[FadeIn(m, shift=UP * 0.2) for m in chain], lag_ratio=0.1, run_time=1.8)],
            steps=[[FadeIn(concl, shift=UP * 0.3), Create(box)]],
        )
        self.say(
            line(f"In general, a{sup('1/n')} is the nth root.", "In general, a to the one over n is the nth root."),
            anims=[FadeOut(VGroup(chain, box), shift=UP * 0.3, run_time=0.6),
                   ReplacementTransform(concl, gen, run_time=1.2)],
        )
        self.play(FadeOut(gen, shift=UP * 0.4), run_time=0.6)

    # ── Example 11 (a), (c) ─────────────────────────────────────────────
    def examples(self):
        e2 = rtex("125", "^{-1/3}", "=", "{1", r"\over", rt(3), "125}}", "=", "{1", r"\over", "5}", fs=MID_FS,
                  results=[8, 9, 10])
        e2[3].set_color(INK)
        rows = fit(e2).move_to(MATH)
        self.say(
            line(f"With a negative: {B('125')}{sup(E('−1/3'))} = 1 / cube root of 125 = {R('1/5')}.",
                 f"And with a negative exponent: {BR} one twenty-five to the negative one third is one fifth."),
            anims=[LaggedStart(*[FadeIn(m, shift=UP * 0.2) for m in e2], lag_ratio=0.15, run_time=2.6)],
        )
        self.play(FadeOut(rows, shift=UP * 0.4), run_time=0.7)

    # ── Takeaway ────────────────────────────────────────────────────────
    def takeaway(self):
        rule = rtex("a", "^{1/n}", "=", rt("n"), "a}", fs=BIG_FS)
        card = self.card(rule, title="FRACTION EXPONENTS")
        self.say(
            line(f"An exponent of {E('1/n')} means the {E('nth root')}.",
                 "An exponent of one over n means the nth root."),
            anims=[FadeIn(card, scale=0.94, run_time=1.0)],
        )
