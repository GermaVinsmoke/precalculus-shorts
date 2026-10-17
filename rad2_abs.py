from rad_common import *


def number_line(center, unit=0.66, span=5):
    """A number line split into a negative half and a non-negative half (so one can fold)."""
    o = np.array(center, dtype=float)
    neg, pos = VGroup(), VGroup()
    neg.add(Line(o + LEFT * (span + 0.35) * unit, o, color=MUTED, stroke_width=3))
    pos.add(Line(o, o + RIGHT * (span + 0.35) * unit, color=MUTED, stroke_width=3))
    neg_labels, pos_labels = VGroup(), VGroup()
    for x in range(-span, span + 1):
        p = o + RIGHT * x * unit
        tick = Line(p + DOWN * 0.1, p + UP * 0.1, color=MUTED, stroke_width=3)
        num = tex(str(x), fs=40, color=MUTED).next_to(tick, DOWN, buff=0.16)
        (neg if x < 0 else pos).add(tick)
        (neg_labels if x < 0 else pos_labels).add(num)
    return neg, pos, neg_labels, pos_labels, o


class R2AbsoluteTrap(RadScene):
    PART = "2 / 4"

    def construct(self):
        q = self.hook()
        self.tests(q)
        self.fold()
        self.general()
        self.takeaway()
        self.outro()

    # ── Hook: √(x²) = x? ────────────────────────────────────────────────
    def hook(self):
        q = rtex(rt(), "x", "^{2}}", "=", "x", "?", fs=HERO_FS * 0.85)
        q[5].set_color(WARN_C)
        q.move_to(MATH)
        self.say(
            line(f"Is √(x{sup('2')}) just x?", "Is the square root of x squared just x?"),
            anims=[LaggedStart(FadeIn(q[0:3], shift=UP * 0.4), FadeIn(q[3:5]), FadeIn(q[5], scale=1.6),
                               lag_ratio=0.45, run_time=1.6)],
        )
        return q

    # ── x = 4 works, x = −4 breaks ──────────────────────────────────────
    def tests(self, q):
        t1 = rtex(rt(), "4", "^{2}}", "=", rt(), "16}", "=", "4", fs=SMALL_FS, results=[7])
        ok = check(60)
        tag1 = label(f"x = {B('4')}", fs=34, color=MUTED)
        r1 = VGroup(tag1, VGroup(t1, ok).arrange(RIGHT, buff=0.3)).arrange(DOWN, buff=0.18, aligned_edge=LEFT)
        t2 = rtex(rt(), "(-4)", "^{2}}", "=", rt(), "16}", "=", "4", fs=SMALL_FS)
        bad = tex(r"\neq", "-4", fs=SMALL_FS, color=WARN_C)
        tag2 = label(f"x = {B('−4')}", fs=34, color=MUTED)
        r2 = VGroup(tag2, VGroup(t2, bad).arrange(RIGHT, buff=0.25)).arrange(DOWN, buff=0.18, aligned_edge=LEFT)
        rows = VGroup(r1, r2).arrange(DOWN, buff=0.6, aligned_edge=LEFT)
        fit(rows).move_to(MATH + DOWN * 0.5)
        self.play(q.animate.scale(0.5).move_to(MATH + UP * 1.95), run_time=0.8)
        self.say(
            line(f"Try x = 4: √16 = 4. {R('Works.')}", f"Try x equals four: {BR} root sixteen is four. {BR} Works."),
            anims=[
                FadeIn(VGroup(tag1, t1), shift=UP * 0.3, run_time=1.0),
                Succession(Wait(2.6), GrowFromCenter(ok, run_time=0.5)),
            ],
        )
        self.say(
            line("Now x = −4: (−4)² is 16…", f"Now try x equals negative four. {BR} Negative four squared is sixteen,"),
            line(f"…and √16 = 4, {W('not −4')}.", "and root sixteen is four, not negative four."),
            anims=[
                FadeIn(VGroup(tag2, t2), shift=UP * 0.3, run_time=1.0),
                Succession(Wait(4.6), FadeIn(bad, shift=LEFT * 0.2, run_time=0.7)),
            ],
        )
        self.play(FadeOut(VGroup(q, rows), shift=UP * 0.4), run_time=0.7)

    # ── Fold the number line: absolute value ────────────────────────────
    def fold(self):
        neg, pos, neg_lbl, pos_lbl, o = number_line([CX, MATH_Y + 0.55, 0])
        unit = 0.66
        d_neg = Dot(o + LEFT * 4 * unit, radius=0.13, color=WARN_C)
        d_pos = Dot(o + RIGHT * 4 * unit, radius=0.13, color=RES_C)
        neg.add(d_neg)
        pos.add(d_pos)
        t_neg = tex("-4", fs=50, color=WARN_C).next_to(d_neg, UP, buff=0.22)
        t_pos = tex("4", fs=50, color=RES_C).next_to(d_pos, UP, buff=0.22)
        t_abs = tex("|{-4}|", "=", "4", fs=56, color=RES_C).next_to(d_pos, UP, buff=0.22)
        result = rtex(rt(), "x", "^{2}}", "=", "|x|", fs=MID_FS, results=[4])
        result.move_to(MATH + DOWN * 1.15)
        box = SurroundingRectangle(result, color=RES_C, buff=0.22, corner_radius=0.16, stroke_width=3.5)
        self.say(
            line(f"A square root always lands on the {R('positive')} side…",
                 "A square root always lands on the positive side."),
            line(f"…that's absolute value: √(x{sup('2')}) = |x|.",
                 f"That's absolute value: {BR} the square root of x squared is the absolute value of x."),
            anims=[
                FadeIn(VGroup(neg, pos, neg_lbl, pos_lbl), run_time=0.9),
                Succession(Wait(0.6), FadeIn(VGroup(t_neg, t_pos), shift=DOWN * 0.15, run_time=0.6)),
            ],
            steps=[
                [FadeOut(neg_lbl), FadeOut(t_neg), FadeOut(t_pos)],
                [Rotate(neg, PI, axis=UP, about_point=o, run_time=1.6, rate_func=rate_functions.ease_in_out_cubic)],
                [Flash(d_pos, color=RES_C, flash_radius=0.4, run_time=0.7), FadeIn(t_abs, shift=DOWN * 0.15)],
                lambda: [VGroup(neg, pos, pos_lbl, t_abs).animate.shift(LEFT * 2.5 * unit),
                         FadeIn(result, shift=UP * 0.3), Create(box)],
            ],
        )
        self.play(FadeOut(VGroup(neg, pos, pos_lbl, t_abs, result, box), shift=UP * 0.4), run_time=0.7)

    # ── Even roots vs odd roots ─────────────────────────────────────────
    def general(self):
        e1 = rtex(rt(4), "(-3)", "^{4}}", "=", "|{-3}|", "=", "3", fs=SMALL_FS, results=[5])
        e2 = rtex(rt(3), "(-5)", "^{3}}", "=", "-5", fs=SMALL_FS, results=[3])
        c1 = chip("EVEN")
        c2 = chip("ODD", color=BASE_C)
        r1 = VGroup(c1, e1).arrange(RIGHT, buff=0.4)
        r2 = VGroup(c2, e2).arrange(RIGHT, buff=0.4)
        rows = VGroup(r1, r2).arrange(DOWN, buff=0.8, aligned_edge=LEFT)
        fit(rows).move_to(MATH)
        self.say(
            line(f"Same for any {E('even')} root: the 4th root of (−3)⁴ is 3.",
                 f"Same for any even root: {BR} the fourth root of negative three, to the fourth, is three."),
            anims=[FadeIn(r1, shift=RIGHT * 0.3, run_time=1.0)],
        )
        self.say(
            line(f"{B('Odd')} roots keep the sign: the cube root of (−5)³ is −5.",
                 f"Odd roots keep the sign: {BR} the cube root of negative five, cubed, is negative five."),
            anims=[FadeIn(r2, shift=RIGHT * 0.3, run_time=1.0)],
        )
        self.play(FadeOut(rows, shift=UP * 0.4), run_time=0.7)

    # ── Takeaway ────────────────────────────────────────────────────────
    def takeaway(self):
        even = VGroup(chip("EVEN n"), rtex(rt("n"), "a", "^{n}}", "=", "|a|", fs=MID_FS)).arrange(RIGHT, buff=0.4)
        odd = VGroup(chip("ODD n", color=BASE_C), rtex(rt("n"), "a", "^{n}}", "=", "a", fs=MID_FS)).arrange(
            RIGHT, buff=0.4)
        rows = VGroup(even, odd).arrange(DOWN, buff=0.45, aligned_edge=LEFT)
        card = self.card(rows, title="THE ABSOLUTE VALUE TRAP")
        self.say(
            "Even root of an even power?",
            line(f"Use the {R('absolute value')}.", f"{BR} Use the absolute value."),
            anims=[FadeIn(card, scale=0.94, run_time=1.0)],
        )
