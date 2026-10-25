try:
    from .poly_common import *
except ImportError:  # Manim loading this file directly
    from poly_common import *


class P1WhatIsAPolynomial(PolyScene):
    PART = "1 / 3"

    def construct(self):
        rows = self.hook()
        self.monomial(rows)
        self.scan(rows)
        self.naming()
        self.takeaway()
        self.outro()

    # ── Hook: which one is a polynomial? ────────────────────────────────
    def hook(self):
        e1 = poly([["2", "x", "^{2}"], ["-", "3", "x"], ["+", "4"]], fs=MID_FS)
        e2 = rtex(rt(), "x}", "+", "10", fs=MID_FS, digits=False)
        e3 = ptex("{y", "-", "2", "z", r"\over", "y", "^{2}", "+", "4}", fs=MID_FS)
        rows = fit_zone(VGroup(e1, e2, e3).arrange(DOWN, buff=0.55), height=MATH_MAX_H - 0.5)
        self.say(
            line(f"Only {E('one')} of these is a polynomial.", "Only one of these is a polynomial."),
            line("Which one?", f"{BR} Which one?"),
            anims=[LaggedStart(*[FadeIn(r, shift=RIGHT * 0.3) for r in rows], lag_ratio=0.4, run_time=1.8)],
        )
        return rows

    # ── Monomial: a·x^k with k a whole number ───────────────────────────
    def monomial(self, rows):
        mono = ptex("a", "x", "^{k}", fs=HERO_FS * 0.8)
        mono[0].set_color(INK)
        mono.move_to(MATH + UP * 0.4)
        k_lbl = label(f"{E('k')} = 0, 1, 2, 3, …", fs=40).next_to(mono, DOWN, buff=0.5)
        a_lbl = label("a is any number", fs=34, color=MUTED).next_to(k_lbl, DOWN, buff=0.25)
        self.say(
            line(f"A {B('monomial')} is a number times a power of x…", "A monomial is a number times a power of x,"),
            line(f"…where the exponent {E('k')} is a whole number.", "where the exponent is a whole number."),
            anims=[FadeOut(rows, shift=UP * 0.3, run_time=0.6),
                   Succession(Wait(0.4), FadeIn(mono, scale=0.9, run_time=0.9)),
                   Succession(Wait(2.6), FadeIn(k_lbl, shift=UP * 0.2, run_time=0.7)),
                   Succession(Wait(3.4), FadeIn(a_lbl, shift=UP * 0.2, run_time=0.6))],
        )
        self.say(
            line(f"A {B('polynomial')} is a sum of monomials.", "A polynomial is a sum of monomials."),
            anims=[Indicate(mono, color=BASE_C, run_time=1.0)],
            gap=0.2,
        )
        self.play(FadeOut(VGroup(mono, k_lbl, a_lbl), shift=UP * 0.3), FadeIn(rows, shift=UP * 0.3), run_time=0.9)

    # ── The scanner: check every exponent ───────────────────────────────
    def scan(self, rows):
        e1, e2, e3 = rows
        beam = Line(UP * 0.7, DOWN * 0.7, color=EXP_C, stroke_width=6).move_to(e1.get_left() + LEFT * 0.3)
        beam.set_stroke(opacity=0.9)
        hidden = VGroup(*[
            tex(str(k), fs=44, color=EXP_C).next_to(t, UP, buff=0.18) for k, t in zip((2, 1, 0), e1.terms)
        ])
        hidden.set_y(max(h.get_y() for h in hidden))
        ok = check(70).next_to(e1, RIGHT, buff=0.4)
        self.say(
            line("Scan the exponents: 2, 1, and 0. All whole numbers.",
                 f"Scan the exponents: {BR} two, one, and zero. {BR} All whole numbers."),
            line(f"{R('Polynomial.')}", "Polynomial."),
            anims=[FadeIn(beam, run_time=0.3),
                   beam.animate(run_time=2.8, rate_func=linear).move_to(e1.get_right() + RIGHT * 0.3),
                   Succession(Wait(0.6), *[FadeIn(h, scale=1.4, run_time=0.5) for h in hidden], lag_ratio=1.6),
                   Succession(Wait(4.6), GrowFromCenter(ok, run_time=0.5))],
        )
        half = ptex("x", "^{1/2}", "+", "10", fs=MID_FS).match_height(e2).move_to(e2)
        bad2 = cross(70).next_to(half, RIGHT, buff=0.5)
        self.say(
            line(f"√x is x{sup(E('1/2'))}, and ½ isn't a whole number.",
                 f"Root x is x to the one half, {BR} and one half isn't a whole number."),
            anims=[FadeOut(beam, run_time=0.3),
                   Succession(Wait(0.8), Transform(e2, half, run_time=1.0)),
                   Succession(Wait(3.2), GrowFromCenter(bad2, run_time=0.5))],
        )
        bad3 = cross(70).next_to(e3, RIGHT, buff=0.5)
        self.say(
            line("Dividing by a variable is not allowed either.", "And dividing by a variable isn't allowed either."),
            anims=[Indicate(e3[5:], color=WARN_C, run_time=1.2),
                   Succession(Wait(1.6), GrowFromCenter(bad3, run_time=0.5))],
        )
        self.play(FadeOut(VGroup(rows, hidden, ok, bad2, bad3), shift=UP * 0.4), run_time=0.7)

    # ── Mono / bi / tri ─────────────────────────────────────────────────
    def naming(self):
        specs = [([["9", "x", "^{5}"]], "monomial"),
                 ([["5", "x"], ["+", "1"]], "binomial"),
                 ([["2", "x", "^{2}"], ["-", "3", "x"], ["+", "4"]], "trinomial")]
        rows = VGroup()
        for terms, name in specs:
            r = poly(terms, fs=SMALL_FS)
            boxes = VGroup(*[tile(t, buff=0.08) for t in r.terms])
            lbl = label(f"{B(name)}", fs=36, weight=BOLD)
            rows.add(VGroup(VGroup(r, boxes), lbl))
        for r in rows:
            r.arrange(RIGHT, buff=0.5)
        rows.arrange(DOWN, buff=0.45, aligned_edge=LEFT)
        fit(rows).move_to(MATH)
        self.say(
            line("Name it by counting terms: one, two, or three…",
                 f"Count the terms to name it: {BR} one term, monomial. {BR} Two, binomial. {BR} Three, trinomial."),
            anims=[Succession(*[AnimationGroup(FadeIn(r[0][0], shift=RIGHT * 0.2), Create(r[0][1]), FadeIn(r[1]),
                                               run_time=0.9) for r in rows], lag_ratio=1.6)],
        )
        self.play(FadeOut(rows, shift=UP * 0.4), run_time=0.6)

    # ── Takeaway ────────────────────────────────────────────────────────
    def takeaway(self):
        f = ptex("a", "x", "^{k}", fs=MID_FS)
        f[0].set_color(INK)
        txt = label(f"a sum of terms with {E('whole-number')} exponents", fs=34, color=MUTED)
        card = self.card(VGroup(f, txt).arrange(DOWN, buff=0.35), title="POLYNOMIAL")
        self.say(
            "A polynomial: a sum of terms,",
            line("each with a whole-number exponent.", f"{BR} each with a whole-number exponent."),
            anims=[FadeIn(card, scale=0.94, run_time=1.0)],
        )
