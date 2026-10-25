try:
    from .sci_common import *
except ImportError:  # Manim loading this file directly
    from sci_common import *

TOP = MATH + UP * 1.85  # the question line
ROW = MATH + UP * 0.35  # the hopping digits
TAIL = [CX, MATH_Y - 0.95, 0]  # "× 10^k"


def eq_line(lhs, coef, exp, fs=MID_FS, solved=False):
    """lhs = coef × 10^exp ; '?' placeholders while unsolved."""
    m = tex(lhs, "=", coef, r"\times", "10", "^{%s}" % exp, fs=fs)
    m[4].set_color(BASE_C)
    m[5].set_color(RES_C if solved else EXP_C)
    if solved:
        m[2].set_color(RES_C)
    else:
        m[2].set_color(MUTED)
    return fit(m).move_to(TOP)


class S2Converting(SciScene):
    PART = "2 / 3"

    def construct(self):
        self.big_to_sci()
        self.small_to_sci()
        self.sci_to_big()
        self.sci_to_small()
        self.calculator()
        self.takeaway()
        self.outro()

    # ── Example 6(a): 56,920 = 5.692 × 10⁴ ──────────────────────────────
    def big_to_sci(self):
        q = eq_line(r"56{,}920", "?", "?")
        q[5].set_color(MUTED)
        self.say(
            line(f"How do you write 56,920 in scientific notation?",
                 "How do you write fifty-six thousand, nine hundred twenty, in scientific notation?"),
            anims=[FadeIn(q, shift=UP * 0.3, run_time=1.0)],
        )
        row = DecimalRow(5, fs=BIG_FS, center=ROW)
        digits = row.write(0, "56920")
        row.set_dot(4.5)
        counter = row.exponent_counter(0, 4.5, at=TAIL)
        self.say(
            line("Move the point left until one digit is in front:",
                 "Move the decimal point left, until just one digit is in front of it:"),
            line(f"{E('4')} places.", f"{BR} four places."),
            anims=[
                TransformFromCopy(q[0], digits, run_time=1.0),
                Succession(Wait(0.6), AnimationGroup(FadeIn(row.dot, scale=2), FadeIn(counter), run_time=0.6)),
            ],
            steps=[[row.hops(-4, step_time=0.4)]],
        )
        ans = eq_line(r"56{,}920", "5.692", "4", solved=True)
        self.say(
            line(f"So 56,920 = {R('5.692')} × {B('10')}{sup(R('4'))}.",
                 f"So it's five point six nine two, {BR} times ten to the fourth."),
            anims=[
                FadeOut(row.cells[4], shift=DOWN * 0.3),  # the trailing zero adds nothing
                ReplacementTransform(q, ans),
            ],
            run_time=1.2,
        )
        self.play(FadeOut(VGroup(ans, row.digits()[:4], row.dot, counter), shift=UP * 0.4), run_time=0.7)

    # ── Example 6(b): 0.000093 = 9.3 × 10⁻⁵ ─────────────────────────────
    def small_to_sci(self):
        q = eq_line("0.000093", "?", "?")
        q[5].set_color(MUTED)
        row = DecimalRow(7, fs=BIG_FS, center=ROW)
        digits = row.write(0, "0000093")
        row.set_dot(0.5)
        counter = row.exponent_counter(0, 0.5, at=TAIL)
        self.say(
            line(f"For a small number, move the point {E('right')}…",
                 "For a small number, move the point right."),
            anims=[
                FadeIn(q, shift=UP * 0.3, run_time=0.8),
                Succession(Wait(0.5), AnimationGroup(TransformFromCopy(q[0], VGroup(*digits)), FadeIn(row.dot),
                                                     FadeIn(counter), run_time=0.9)),
            ],
            steps=[[row.hops(5, step_time=0.4)]],
        )
        ans = eq_line("0.000093", "9.3", "-5", solved=True)
        self.say(
            line(f"…{E('5')} places: {R('9.3')} × {B('10')}{sup(R('−5'))}.",
                 f"Five places: {BR} nine point three, times ten to the negative fifth."),
            anims=[
                FadeOut(VGroup(*[row.cells[i] for i in range(5)]), shift=UP * 0.3),
                ReplacementTransform(q, ans),
            ],
            run_time=1.2,
        )
        self.play(FadeOut(VGroup(ans, row.cells[5], row.cells[6], row.dot, counter), shift=UP * 0.4),
                  run_time=0.7)

    # ── Example 7(a): 6.97 × 10⁹ = 6,970,000,000 ────────────────────────
    def sci_to_big(self):
        q = tex("6.97", r"\times", "10", "^{9}", "=", "?", fs=MID_FS)
        q[2].set_color(BASE_C)
        q[3].set_color(EXP_C)
        q[5].set_color(MUTED)
        q.move_to(TOP)
        row = DecimalRow(10, fs=90, center=ROW)
        digits = row.write(0, "697")
        row.set_dot(0.5)
        counter = row.exponent_counter(9, 0.5, at=TAIL)
        self.say(
            "Going back? Same move, in reverse.",
            line(f"{B('10')}{sup(E('9'))}: nine places right.", f"{BR} Ten to the ninth: {BR} nine places right."),
            anims=[
                FadeIn(q, shift=UP * 0.3, run_time=0.8),
                Succession(Wait(0.5), AnimationGroup(TransformFromCopy(q[0], VGroup(*digits)), FadeIn(row.dot),
                                                     FadeIn(counter), run_time=0.9)),
            ],
            steps=[
                [row.hops(9, step_time=0.28)],
                [ReplacementTransform(row.digits(), final := tex(r"6{,}970{,}000{,}000", fs=90, color=RES_C)
                                      .move_to(ROW)), FadeOut(row.dot), FadeOut(counter)],
            ],
        )
        self.play(FadeOut(VGroup(q, final), shift=UP * 0.4), run_time=0.7)

    # ── Example 7(b): 4.6271 × 10⁻⁶ = 0.0000046271 ──────────────────────
    def sci_to_small(self):
        q = tex("4.6271", r"\times", "10", "^{-6}", "=", "?", fs=MID_FS)
        q[2].set_color(BASE_C)
        q[3].set_color(EXP_C)
        q[5].set_color(MUTED)
        fit(q).move_to(TOP)
        row = DecimalRow(11, fs=84, center=ROW)
        digits = row.write(6, "46271")
        row.set_dot(6.5)
        counter = row.exponent_counter(-6, 6.5, at=TAIL)
        self.say(
            line(f"{B('10')}{sup(E('−6'))}: six places left.", f"And ten to the negative sixth: {BR} six places left."),
            anims=[
                FadeIn(q, shift=UP * 0.3, run_time=0.8),
                AnimationGroup(TransformFromCopy(q[0], VGroup(*digits)), FadeIn(row.dot), FadeIn(counter),
                               run_time=0.9),
            ],
            steps=[[row.hops(-6, step_time=0.36)], [row.digits().animate.set_color(RES_C), FadeOut(counter)]],
        )
        self.play(FadeOut(VGroup(q, row.digits(), row.dot), shift=UP * 0.4), run_time=0.7)

    # ── Calculator E notation ───────────────────────────────────────────
    def calculator(self):
        prompt = tex(r"1{,}111{,}111^2", fs=SMALL_FS, color=MUTED).move_to(MATH + UP * 1.9)
        screen_text = MarkupText("1.234568E12", font="Menlo", font_size=64, color=RES_C, weight=BOLD)
        screen = RoundedRectangle(corner_radius=0.2, width=screen_text.width + 1.0, height=screen_text.height + 0.8,
                                  fill_color="#0F1F18", fill_opacity=1, stroke_color=CARD_STROKE, stroke_width=3)
        lcd = VGroup(screen, screen_text.move_to(screen)).move_to(MATH + UP * 0.45)
        meaning = tex("1.234568", r"\times", "10", "^{12}", fs=MID_FS)
        meaning[2].set_color(BASE_C)
        meaning[3].set_color(EXP_C)
        meaning.move_to(MATH - UP * 1.25)
        e_part = screen_text[-3:]
        self.say(
            line(f"Calculators show this with an {E('E')}…", "Calculators show this with an E."),
            line(f"…{E('E12')} means times {B('10')}{sup(E('12'))}.", f"{BR} E twelve means times ten to the twelfth."),
            anims=[
                FadeIn(prompt, run_time=0.6),
                FadeIn(lcd, shift=UP * 0.2, run_time=0.9),
                Succession(
                    Wait(1.6),
                    Indicate(e_part, color=EXP_C, scale_factor=1.2, run_time=0.9),
                    AnimationGroup(TransformFromCopy(screen_text[:8], meaning[0]),
                                   TransformFromCopy(e_part[0], VGroup(meaning[1], meaning[2])),
                                   TransformFromCopy(e_part[1:], meaning[3]), run_time=1.2),
                ),
            ],
        )
        self.play(FadeOut(VGroup(prompt, lcd, meaning), shift=UP * 0.4), run_time=0.7)

    # ── Takeaway ────────────────────────────────────────────────────────
    def takeaway(self):
        big = label(f"Big number → {E('positive')} exponent", fs=40)
        small = label(f"Tiny number → {E('negative')} exponent", fs=40)
        card = self.card(VGroup(big, small).arrange(DOWN, buff=0.45, aligned_edge=LEFT), title="COUNT THE HOPS")
        self.say(
            "The exponent just counts the hops.",
            anims=[FadeIn(card, scale=0.94, run_time=1.0)],
            gap=1.2,
        )
