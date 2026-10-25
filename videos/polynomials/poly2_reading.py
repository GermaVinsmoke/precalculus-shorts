try:
    from .poly_common import *
except ImportError:  # Manim loading this file directly
    from poly_common import *

P_TERMS = [["8"], ["-", "x"], ["+", "x", "^{2}"], ["-", r"\tfrac{1}{2}", "x", "^{3}"]]
COEFS = ["8", "-1", "1", r"-\tfrac12"]
EXPS = ["0", "1", "2", "3"]


class P2ReadingAPolynomial(PolyScene):
    PART = "2 / 3"

    def construct(self):
        p, q = self.hook()
        cols = self.terms(p)
        self.degree(p, q, cols)
        self.gotchas()
        self.takeaway()
        self.outro()

    # ── Hook: degree of 8 − x + x² − ½x³ ────────────────────────────────
    def hook(self):
        p = poly(P_TERMS, fs=MID_FS)
        fit(p).move_to(MATH + UP * 1.5)
        q = label(f"degree = {W("0")} ?", fs=48, weight=BOLD).move_to(MATH + DOWN * 2.55)
        self.say(
            line(f"What's the degree of 8 − x + x{sup('2')} − ½x{sup('3')}?",
                 f"What's the degree of eight minus x, {BR} plus x squared, {BR} minus one half x cubed?"),
            line("It starts with 8. Is the degree zero?", f"{BR} It starts with eight. {BR} Is the degree zero?"),
            anims=[LaggedStart(*[FadeIn(t, shift=UP * 0.3) for t in p.terms], lag_ratio=0.3, run_time=1.6),
                   Succession(Wait(5.0), FadeIn(q, shift=UP * 0.2, run_time=0.7))],
        )
        return p, q

    # ── Tiles, coefficients and exponents ───────────────────────────────
    def terms(self, p):
        tiles = VGroup(*[tile(t, buff=0.1) for t in p.terms])
        nums = VGroup(*[chip(str(i + 1), color=BASE_C).scale(0.7).next_to(tl, UP, buff=0.15)
                        for i, tl in enumerate(tiles)])
        nums.set_y(max(n.get_y() for n in nums))
        self.say(
            line(f"Split it into terms: {B('four')} of them.", f"Split it into terms: {BR} four of them."),
            line("Each term keeps its sign.", f"{BR} Each term keeps its sign."),
            anims=[LaggedStart(*[AnimationGroup(Create(tl), FadeIn(n, shift=DOWN * 0.1)) for tl, n in zip(tiles, nums)],
                               lag_ratio=0.35, run_time=2.0)],
        )
        y_coef = MATH_Y + 0.35
        y_exp = MATH_Y - 0.45
        coef = VGroup(*[tex(c, fs=60, color=INK).move_to([t.get_x(), y_coef, 0]) for c, t in zip(COEFS, p.terms)])
        exps = VGroup(*[tex(e, fs=60, color=EXP_C).move_to([t.get_x(), y_exp, 0]) for e, t in zip(EXPS, p.terms)])
        heads = label(f"number   ·   {E('exponent')}", fs=30, color=MUTED).move_to([CX, MATH_Y - 1.3, 0])
        self.say(
            line(f"Read each one: 8 is 8x{sup(E('0'))}, and −x is −1x{sup(E('1'))}.",
                 f"Read each term's number and exponent. {BR} Eight is eight x to the zero. "
                 f"{BR} Minus x is negative one x to the first."),
            anims=[FadeIn(heads, run_time=0.6),
                   LaggedStart(*[AnimationGroup(FadeIn(c, shift=UP * 0.15), FadeIn(e, shift=UP * 0.15))
                                 for c, e in zip(coef, exps)], lag_ratio=0.8, run_time=4.0)],
        )
        self.tiles, self.nums = tiles, nums
        return VGroup(heads, coef, exps)

    # ── Degree = the highest exponent, wherever it sits ─────────────────
    def degree(self, p, q, cols):
        heads, coef, exps = cols
        glow = SurroundingRectangle(VGroup(self.tiles[3], exps[3]), color=RES_C, buff=0.12, corner_radius=0.16,
                                    stroke_width=4)
        answer = label(f"degree = {R('3')}", fs=48, weight=BOLD).move_to(q)
        self.say(
            line(f"The degree is the {R('highest')} exponent, wherever it sits: {R('3')}.",
                 f"The degree is the highest exponent, {BR} wherever it sits: {BR} three."),
            anims=[LaggedStart(*[Indicate(e, color=EXP_C, scale_factor=1.25) for e in exps], lag_ratio=0.3,
                               run_time=1.6),
                   Succession(Wait(2.2), AnimationGroup(Create(glow), Transform(q, answer), run_time=0.9))],
        )
        self.play(FadeOut(VGroup(p, q, self.tiles, self.nums, cols, glow), shift=UP * 0.4), run_time=0.7)

    # ── Two quick traps from the book's table ───────────────────────────
    def gotchas(self):
        a = poly([["x", "^{8}"], ["+", "5", "x"]], fs=SMALL_FS)
        a_lbl = label(f"2 terms, degree {R('8')}", fs=38)
        b = ptex("6", "=", "6", "x", "^{0}", fs=SMALL_FS)
        b_lbl = label(f"degree {R('0')}", fs=38)
        r1 = VGroup(a, a_lbl).arrange(RIGHT, buff=0.55)
        r2 = VGroup(b, b_lbl).arrange(RIGHT, buff=0.55)
        rows = fit(VGroup(r1, r2).arrange(DOWN, buff=0.8, aligned_edge=LEFT)).move_to(MATH)
        self.say(
            line(f"x{sup('8')} + 5x has just two terms, but degree {R('8')}.",
                 "x to the eighth plus five x has just two terms, but degree eight."),
            anims=[FadeIn(a, shift=RIGHT * 0.2, run_time=0.8),
                   Succession(Wait(2.4), FadeIn(a_lbl, shift=LEFT * 0.2, run_time=0.6))],
        )
        self.say(
            line(f"And a plain 6 has degree {R('0')}: 6 = 6x{sup(E('0'))}.",
                 "And a plain six has degree zero, because six is six x to the zero."),
            anims=[FadeIn(b[0], shift=RIGHT * 0.2, run_time=0.6),
                   Succession(Wait(1.6), AnimationGroup(FadeIn(b[1:], shift=LEFT * 0.2), FadeIn(b_lbl), run_time=0.8))],
        )
        self.play(FadeOut(rows, shift=UP * 0.4), run_time=0.6)

    # ── Takeaway ────────────────────────────────────────────────────────
    def takeaway(self):
        l1 = label(f"{R('Degree')}: the highest exponent", fs=40)
        l2 = label("Coefficient: the number in front, sign included", fs=34, color=MUTED)
        card = self.card(VGroup(l1, l2).arrange(DOWN, buff=0.35), title="THE DEGREE")
        self.say(
            "The degree is the highest exponent.",
            line("The coefficient keeps its sign.", f"{BR} The coefficient keeps its sign."),
            anims=[FadeIn(card, scale=0.94, run_time=1.0)],
        )
