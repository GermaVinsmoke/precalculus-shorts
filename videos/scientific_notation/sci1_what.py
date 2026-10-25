try:
    from .sci_common import *
except ImportError:  # Manim loading this file directly
    from sci_common import *


def sci(coef, exp, fs=BIG_FS):
    """coef × 10^exp with the series colours (10 blue, exponent yellow)."""
    m = tex(coef, r"\times", "10", "^{%s}" % exp, fs=fs)
    m[2].set_color(BASE_C)
    m[3].set_color(EXP_C)
    return m


class S1WhatIsIt(SciScene):
    PART = "1 / 3"

    def construct(self):
        self.hook()
        self.definition()
        self.big()
        self.tiny()
        self.summary()
        self.takeaway()
        self.outro()

    # ── Hook: two impossible numbers ────────────────────────────────────
    def hook(self):
        star = tex(r"40{,}000{,}000{,}000{,}000", fs=SMALL_FS)
        star_unit = label("km", fs=34, color=MUTED)
        star_tag = label("Distance to Proxima Centauri", fs=30, color=MUTED)
        atom = tex(r"0.000\,000\,000\,000\,000\,000\,000\,001\,66", fs=50)
        atom_unit = label("g", fs=34, color=MUTED)
        atom_tag = label("Mass of a hydrogen atom", fs=30, color=MUTED)
        fit(atom, SAFE_W - 0.6)
        r1 = VGroup(star, star_unit).arrange(RIGHT, buff=0.2, aligned_edge=DOWN)
        r2 = VGroup(atom, atom_unit).arrange(RIGHT, buff=0.15, aligned_edge=DOWN)
        block = VGroup(star_tag, r1, atom_tag, r2).arrange(DOWN, buff=0.3)
        block[2].shift(DOWN * 0.45)
        block[3].shift(DOWN * 0.45)
        block.move_to(MATH)
        self.say(
            line("The nearest star beyond the Sun is about 40 trillion km away.",
                 "The nearest star beyond the Sun is about forty trillion kilometers away."),
            anims=[
                FadeIn(star_tag, run_time=0.5),
                LaggedStart(*[FadeIn(g, shift=UP * 0.2) for g in star[0]], FadeIn(star_unit),
                            lag_ratio=0.12, run_time=2.0),
            ],
        )
        self.say(
            "And a hydrogen atom weighs this much, in grams.",
            anims=[
                FadeIn(atom_tag, run_time=0.5),
                LaggedStart(*[FadeIn(g, shift=UP * 0.15) for g in atom[0]], FadeIn(atom_unit),
                            lag_ratio=0.06, run_time=2.2),
            ],
        )
        zeros = [g for g in [*star[0], *atom[0]] if g.height > 0.15]
        self.say(
            line("Numbers like these are hard to read…", "Numbers like these are hard to read."),
            line(f"…so scientists use {E('scientific notation')}.", f"{BR} So scientists use scientific notation."),
            anims=[LaggedStart(*[Indicate(g, color=WARN_C, scale_factor=1.25) for g in zeros],
                               lag_ratio=0.03, run_time=2.2)],
        )
        self.play(FadeOut(block, shift=UP * 0.4), run_time=0.7)

    # ── x = a × 10ⁿ ─────────────────────────────────────────────────────
    def definition(self):
        f = tex("x", "=", "a", r"\times", "10", "^{n}", fs=BIG_FS)
        f[4].set_color(BASE_C)
        f[5].set_color(EXP_C)
        f.move_to(MATH)
        brace = Brace(f[2], DOWN, buff=0.2, color=INK)
        a_lbl = tex(r"1 \le a < 10", fs=58).next_to(brace, DOWN, buff=0.15)
        n_lbl = label(f"{E('n')} is an integer", fs=36).next_to(f[5], UP, buff=0.7)
        n_lbl.shift(LEFT * max(0, n_lbl.get_right()[0] - SAFE_RIGHT + 0.1))
        n_arrow = Arrow(n_lbl.get_bottom(), f[5].get_top(), buff=0.1,
                        color=EXP_C, stroke_width=4, max_tip_length_to_length_ratio=0.3)
        self.say(
            line(f"A number from 1 up to 10, times a power of {B('10')}.",
                 f"A number from one up to ten, {BR} times a power of ten."),
            anims=[
                Succession(
                    FadeIn(f, shift=UP * 0.3, run_time=1.0),
                    AnimationGroup(GrowFromCenter(brace), FadeIn(a_lbl, shift=UP * 0.2), run_time=0.9),
                    Indicate(f[4], color=BASE_C, run_time=0.9),
                )
            ],
        )
        self.say(
            line(f"The exponent {E('n')} is an integer.", f"The exponent, n, {BR} is an integer."),
            anims=[GrowArrow(n_arrow, run_time=0.8), FadeIn(n_lbl, shift=LEFT * 0.2, run_time=0.8)],
        )
        self.play(FadeOut(VGroup(f, brace, a_lbl, n_lbl, n_arrow), shift=UP * 0.4), run_time=0.7)

    # ── 4 × 10¹³: thirteen hops right ───────────────────────────────────
    def big(self):
        top = sci("4", 13, fs=MID_FS).move_to(MATH + UP * 1.75)
        row = DecimalRow(14, fs=66, center=MATH + UP * 0.15)
        four = row.write(0, "4")
        row.set_dot(0.5)
        counter = row.exponent_counter(13, 0.5, at=[CX, MATH_Y - 1.15, 0])
        final = tex(r"40{,}000{,}000{,}000{,}000", fs=66, color=RES_C).move_to(MATH + UP * 0.15)
        self.say(
            line(f"4 × {B('10')}{sup(E('13'))}: move the point {E('13')} places right.",
                 f"Four times ten to the thirteenth: {BR} move the decimal point thirteen places right."),
            anims=[
                FadeIn(top, shift=UP * 0.3, run_time=0.8),
                AnimationGroup(TransformFromCopy(top[0], four), FadeIn(row.dot), FadeIn(counter), run_time=0.8),
            ],
            steps=[[row.hops(13, step_time=0.24)]],
        )
        self.say(
            line("Forty trillion.", "Forty trillion."),
            anims=[ReplacementTransform(row.digits(), final), FadeOut(row.dot), FadeOut(counter)],
        )
        self.play(FadeOut(VGroup(top, final), shift=UP * 0.4), run_time=0.7)

    # ── 1.66 × 10⁻²⁴: twenty-four hops left ─────────────────────────────
    def tiny(self):
        top = sci("1.66", -24, fs=MID_FS).move_to(MATH + UP * 1.75)
        row = DecimalRow(27, fs=40, center=MATH + UP * 0.15, gap=0.07)
        digits = row.write(24, "166")
        row.set_dot(24.5)
        counter = row.exponent_counter(-24, 24.5, at=[CX, MATH_Y - 1.15, 0])
        self.say(
            line(f"A {E('negative')} exponent moves the point left…",
                 "A negative exponent moves the point left."),
            anims=[
                FadeIn(top, shift=UP * 0.3, run_time=0.8),
                Succession(Wait(0.5), AnimationGroup(TransformFromCopy(top[0], digits), FadeIn(row.dot),
                                                     FadeIn(counter), run_time=0.9)),
            ],
        )
        self.say(
            line(f"…{E('24')} places for the hydrogen atom.", f"Twenty-four places, {BR} for the hydrogen atom."),
            anims=[row.hops(-24, step_time=0.14)],
            steps=[[row.digits().animate.set_color(RES_C), FadeOut(counter)]],
        )
        self.play(FadeOut(VGroup(top, row.digits(), row.dot), shift=UP * 0.4), run_time=0.7)

    # ── Positive vs negative ────────────────────────────────────────────
    def summary(self):
        pos = VGroup(tex("10", "^{+}", fs=BIG_FS), label("point moves right:\nbig number", fs=36))
        neg = VGroup(tex("10", "^{-}", fs=BIG_FS), label("point moves left:\ntiny number", fs=36))
        for g in (pos, neg):
            g[0][0].set_color(BASE_C)
            g[0][1].set_color(EXP_C)
            g.arrange(RIGHT, buff=0.6)
        rows = VGroup(pos, neg).arrange(DOWN, buff=0.8, aligned_edge=LEFT).move_to(MATH)
        self.say(
            line(f"{E('Positive')} exponent: a big number.", "Positive exponent: a big number."),
            line(f"{E('Negative')} exponent: a tiny one.", f"{BR} Negative exponent: a tiny one."),
            anims=[
                FadeIn(pos, shift=RIGHT * 0.3, run_time=0.8),
                Succession(Wait(1.8), FadeIn(neg, shift=RIGHT * 0.3, run_time=0.8)),
            ],
        )
        self.play(FadeOut(rows, shift=UP * 0.4), run_time=0.7)

    # ── Takeaway ────────────────────────────────────────────────────────
    def takeaway(self):
        f = tex("x", "=", "a", r"\times", "10", "^{n}")
        f[4].set_color(BASE_C)
        f[5].set_color(EXP_C)
        cond = tex(r"1 \le a < 10", fs=60, color=MUTED)
        card = self.card(VGroup(f, cond).arrange(DOWN, buff=0.35), title="SCIENTIFIC NOTATION")
        self.say(
            "One digit before the point,",
            line(f"times a power of {B('10')}.", f"{BR} times a power of ten."),
            anims=[FadeIn(card, scale=0.94, run_time=1.0)],
        )
