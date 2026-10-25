try:
    from .rad_common import *
except ImportError:  # Manim loading this file directly
    from rad_common import *


def tile(fs=46):
    """One √3, drawn as a countable object."""
    t = rtex(rt(), "3}", fs=fs)
    box = RoundedRectangle(corner_radius=0.12, width=0.86, height=0.72, fill_color=CARD_FILL, fill_opacity=1,
                           stroke_color=BASE_C, stroke_width=2.5)
    return VGroup(box, t.move_to(box))


class R4Combining(RadScene):
    PART = "4 / 4"

    def construct(self):
        self.hook()
        self.triangle()
        self.like_radicals()
        self.example()
        self.takeaway()
        self.outro()

    # ── Hook: √9 + √16 = √25? ───────────────────────────────────────────
    def hook(self):
        q = rtex(rt(), "9}", "+", rt(), "16}", "=", rt(), "25}", "?")
        q[8].set_color(WARN_C)
        fit(q).move_to(MATH + UP * 0.5)
        v_left = tex("3", "+", "4", "=", "7", fs=MID_FS, color=INK)
        v_right = tex("5", fs=MID_FS, color=INK)
        v_left.next_to(VGroup(q[0:5]), DOWN, buff=0.7)
        v_right.next_to(VGroup(q[6:8]), DOWN, buff=0.7).match_y(v_left)
        neq = tex(r"\neq", fs=MID_FS, color=WARN_C).move_to(q[5])
        self.say(
            line("Is √9 + √16 the same as √25?",
                 "Is root nine plus root sixteen the same as root twenty-five?"),
            anims=[LaggedStart(*[FadeIn(m, shift=UP * 0.3) for m in q], lag_ratio=0.12, run_time=1.6)],
        )
        self.say(
            line(f"Check: 3 + 4 = 7, but √25 = 5.", f"Check it: {BR} three plus four is seven, {BR} but root twenty-five is five."),
            anims=[FadeIn(v_left, shift=UP * 0.2, run_time=0.9),
                   Succession(Wait(2.2), FadeIn(v_right, shift=UP * 0.2, run_time=0.7))],
            steps=[[Transform(q[5], neq), FadeOut(q[8]), v_left[4].animate.set_color(WARN_C),
                    v_right.animate.set_color(WARN_C)]],
        )
        self.play(FadeOut(VGroup(q, v_left, v_right), shift=UP * 0.4), run_time=0.7)

    # ── 3-4-5 triangle: legs vs the shortcut ────────────────────────────
    def triangle(self):
        u = 0.72
        a = np.array([CX - 1.5 * u, MATH_Y + 1.0 - 2 * u, 0])
        b = a + RIGHT * 3 * u
        c = b + UP * 4 * u
        tri = Polygon(a, b, c, stroke_color=MUTED, stroke_width=3, fill_color=CARD_FILL, fill_opacity=0.6)
        corner = VGroup(Line(b + LEFT * 0.25, b + LEFT * 0.25 + UP * 0.25), Line(b + LEFT * 0.25 + UP * 0.25,
                                                                                    b + UP * 0.25)).set_stroke(MUTED, 2)
        leg1 = Line(a, b, color=EXP_C, stroke_width=7)
        leg2 = Line(b, c, color=EXP_C, stroke_width=7)
        hyp = Line(a, c, color=RES_C, stroke_width=7)
        l1 = tex("3", fs=60, color=EXP_C).next_to(leg1, DOWN, buff=0.15)
        l2 = tex("4", fs=60, color=EXP_C).next_to(leg2, RIGHT, buff=0.15)
        walker = Dot(a, radius=0.1, color=EXP_C)
        legs_sum = tex("3", "+", "4", "=", "7", fs=64, color=EXP_C).next_to(l1, DOWN, buff=0.3)
        lh = rtex(rt(), "9", "+", "16}", "=", "5", fs=64, results=[5]).next_to(legs_sum, DOWN, buff=0.25)
        self.say(
            line("Walking along both legs: 3 + 4 = 7.", f"Here's why: {BR} walking along both legs is three plus four."),
            anims=[
                FadeIn(VGroup(tri, corner), run_time=0.8),
                Succession(
                    Wait(0.6),
                    AnimationGroup(Create(leg1), MoveAlongPath(walker, Line(a, b)), FadeIn(l1), run_time=1.1),
                    AnimationGroup(Create(leg2), MoveAlongPath(walker, Line(b, c)), FadeIn(l2), run_time=1.3),
                    FadeIn(legs_sum, shift=LEFT * 0.2, run_time=0.6),
                ),
            ],
        )
        self.say(
            line(f"Cutting across: √(9 + 16) = {R('5')}.",
                 f"Cutting straight across is the square root of nine plus sixteen: {BR} five."),
            anims=[Create(hyp, run_time=1.4), Succession(Wait(1.6), FadeIn(lh, shift=RIGHT * 0.2, run_time=0.8))],
        )
        rule = rtex(rt(), "a", "+", "b}", r"\neq", rt(), "a}", "+", rt(), "b}", fs=MID_FS)
        rule[4].set_color(WARN_C)
        fit(rule).move_to(MATH + DOWN * 0.2)
        self.say(
            line(f"So a root {W('never')} splits over a plus sign.", "So a root never splits over a plus sign."),
            anims=[FadeOut(VGroup(tri, corner, leg1, leg2, hyp, l1, l2, lh, walker, legs_sum), shift=UP * 0.3,
                           run_time=0.7),
                   Succession(Wait(0.5), FadeIn(rule, shift=UP * 0.3, run_time=0.9))],
        )
        self.play(FadeOut(rule, shift=UP * 0.4), run_time=0.6)

    # ── Like radicals add like objects ──────────────────────────────────
    def like_radicals(self):
        two = VGroup(*[tile() for _ in range(2)]).arrange(RIGHT, buff=0.14)
        five = VGroup(*[tile() for _ in range(5)]).arrange(RIGHT, buff=0.14)
        plus = tex("+", fs=MID_FS)
        top = VGroup(two, plus, five).arrange(RIGHT, buff=0.25)
        fit(top).move_to(MATH + UP * 0.7)
        seven = VGroup(*[tile() for _ in range(7)]).arrange(RIGHT, buff=0.14)
        fit(seven).move_to(MATH + UP * 0.7)
        eq = rtex("2", rt(), "3}", "+", "5", rt(), "3}", "=", "7", rt(), "3}", fs=MID_FS, results=[8, 10])
        eq[0].set_color(INK)
        eq[4].set_color(INK)
        fit(eq).move_to(MATH + DOWN * 0.9)
        self.say(
            "What you can add are like radicals.",
            line("Two √3s plus five √3s is seven √3s.",
                 f"{BR} Two root threes plus five root threes {BR} is seven root threes."),
            anims=[
                LaggedStart(*[GrowFromCenter(t) for t in two], FadeIn(plus), *[GrowFromCenter(t) for t in five],
                            lag_ratio=0.15, run_time=1.8),
            ],
            steps=[
                [*[ReplacementTransform(s, t) for s, t in zip([*two, *five], seven)], FadeOut(plus)],
                [FadeIn(eq, shift=UP * 0.2)],
            ],
        )
        self.play(FadeOut(VGroup(seven, eq), shift=UP * 0.4), run_time=0.7)

    # ── Example 10(a): √32 + √200 = 14√2 ────────────────────────────────
    def example(self):
        e1 = rtex(rt(), "32}", "+", rt(), "200}")
        e2 = rtex("=", rt(), "16", r"\cdot", "2}", "+", rt(), "100", r"\cdot", "2}", fs=SMALL_FS)
        e3 = rtex("=", "4", rt(), "2}", "+", "10", rt(), "2}", fs=SMALL_FS)
        e4 = rtex("=", "14", rt(), "2}", fs=MID_FS, results=[1, 3])
        for m in (e3, e4):
            for i, s in enumerate(m.tex_strings):
                if s in ("4", "10", "14"):
                    m[i].set_color(RES_C if m is e4 else INK)
        stack = fit_zone(VGroup(e1, e2, e3, e4).arrange(DOWN, buff=0.35))
        self.say(
            line("Sometimes you uncover them first:", "Sometimes you uncover them first:"),
            line("√32 is 4√2, and √200 is 10√2…",
                 f"{BR} root thirty-two is four root two, {BR} and root two hundred is ten root two."),
            anims=[FadeIn(e1, shift=UP * 0.3, run_time=0.8)],
            steps=[[FadeIn(e2, shift=UP * 0.2)], 0.6, [FadeIn(e3, shift=UP * 0.2)]],
        )
        self.say(
            line(f"…so together, {R('14√2')}.", f"So together: {BR} fourteen root two."),
            anims=[FadeIn(e4, shift=UP * 0.2, run_time=0.9)],
        )
        self.play(FadeOut(stack, shift=UP * 0.4), run_time=0.7)

    # ── Takeaway ────────────────────────────────────────────────────────
    def takeaway(self):
        add = rtex("a", rt(), "c}", "+", "b", rt(), "c}", "=", "(a+b)", rt(), "c}", fs=MID_FS)
        add[0].set_color(INK)
        add[4].set_color(INK)
        add[8].set_color(INK)
        never = rtex(rt(), "a", "+", "b}", r"\neq", rt(), "a}", "+", rt(), "b}", fs=MID_FS)
        never[4].set_color(WARN_C)
        card = self.card(VGroup(add, never).arrange(DOWN, buff=0.45), title="COMBINING RADICALS")
        self.say(
            "Add like radicals,",
            line("but never split a root over a plus sign.", f"{BR} but never split a root over a plus sign."),
            anims=[FadeIn(card, scale=0.94, run_time=1.0)],
        )
