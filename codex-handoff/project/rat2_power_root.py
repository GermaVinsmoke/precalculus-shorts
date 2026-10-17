from rat_common import *

LANE_X = (CX - 1.85, CX + 1.85)
LANE_FS = 76


class Q2PowerAndRoot(RatScene):
    PART = "2 / 3"

    def construct(self):
        self.hook()
        self.anatomy()
        self.race()
        self.four_three_halves()
        self.catch()
        self.takeaway()
        self.outro()

    # ── Hook: 8^(2/3) ───────────────────────────────────────────────────
    def hook(self):
        q = pw("8", "2/3", fs=HERO_FS)
        q.move_to(MATH)
        self.q = q
        self.say(
            line(f"{B('8')}{sup(E('2/3'))}: what do the 2 and the 3 each do?",
                 f"Eight to the two thirds. {BR} What do the two and the three each do?"),
            anims=[FadeIn(q, shift=UP * 0.4, run_time=1.0)],
        )
        self.play(FadeOut(q, shift=UP * 0.4), run_time=0.6)

    # ── Top = power, bottom = root ──────────────────────────────────────
    def anatomy(self):
        a = auto(tex("a", "^{m/n}", fs=HERO_FS))
        a.move_to(MATH + UP * 0.75 + LEFT * 0.7)
        m, n = a[1][0], a[1][2]
        p_lbl = label(E("power"), fs=40, weight=BOLD).next_to(m, UP, buff=0.65)
        r_lbl = label(B("root"), fs=40, weight=BOLD).next_to(n, RIGHT, buff=0.7).shift(DOWN * 0.55)
        p_arr = Arrow(p_lbl.get_bottom(), m.get_top(), buff=0.08, color=EXP_C, stroke_width=4,
                      max_tip_length_to_length_ratio=0.3)
        r_arr = Arrow(r_lbl.get_left(), n.get_corner(DR), buff=0.08, color=BASE_C, stroke_width=4,
                      max_tip_length_to_length_ratio=0.3)
        forms = rtex("a", "^{m/n}", "=", "(", rt("n"), "a}", ")", "^{m}", "=", rt("n"), "a", "^{m}}", fs=MID_FS)
        fit(forms).move_to(MATH + DOWN * 1.25)
        self.say(
            line(f"The bottom of the fraction is a {B('root')}.", "The bottom of the fraction is a root."),
            line(f"The top is a {E('power')}, in either order.", f"{BR} The top is a power. {BR} In either order."),
            anims=[
                FadeIn(a, shift=UP * 0.3, run_time=0.8),
                Succession(Wait(0.8), AnimationGroup(GrowArrow(r_arr), FadeIn(r_lbl), Indicate(n, color=BASE_C),
                                                     run_time=1.0)),
                Succession(Wait(2.8), AnimationGroup(GrowArrow(p_arr), FadeIn(p_lbl), Indicate(m, color=EXP_C),
                                                     run_time=1.0)),
                Succession(Wait(4.2), LaggedStart(*[FadeIn(x, shift=UP * 0.2) for x in forms], lag_ratio=0.08,
                                                  run_time=1.6)),
            ],
        )
        self.play(FadeOut(VGroup(a, p_lbl, r_lbl, p_arr, r_arr, forms), shift=UP * 0.4), run_time=0.7)

    # ── Split-screen race: root first vs power first ────────────────────
    def race(self):
        top = pw("8", "2/3", fs=MID_FS).move_to(MATH + UP * 2.0)
        chips = VGroup(chip("ROOT FIRST", RES_C).scale(0.75).move_to([LANE_X[0], MATH_Y + 0.95, 0]),
                       chip("POWER FIRST", BASE_C).scale(0.75).move_to([LANE_X[1], MATH_Y + 0.95, 0]))
        divider = DashedLine([CX, MATH_Y + 1.35, 0], [CX, MATH_Y - 2.1, 0], color=CARD_STROKE, dash_length=0.12)
        left = VGroup(
            rtex("(", rt(3), "8}", ")", "^{2}", fs=LANE_FS),
            auto(tex("=", "2", "^{2}", fs=LANE_FS)),
            tex("=", "4", fs=LANE_FS),
        )
        right = VGroup(
            rtex(rt(3), "8", "^{2}}", fs=LANE_FS),
            rtex("=", rt(3), "64}", fs=LANE_FS),
            tex("=", "4", fs=LANE_FS),
        )
        for lane, x in zip((left, right), LANE_X):
            lane.arrange(DOWN, buff=0.35)
            fit(lane, 3.3)
            lane.move_to([x, MATH_Y - 0.85, 0])
        left[2][1].set_color(RES_C)
        right[2][1].set_color(RES_C)
        self.play(FadeIn(top, shift=DOWN * 0.2), FadeIn(chips), Create(divider), run_time=0.9)
        self.say(
            line("Root first: the cube root of 8 is 2, and 2² is 4.",
                 f"Root first: {BR} the cube root of eight is two, {BR} and two squared is four."),
            anims=[Succession(*[FadeIn(r, shift=DOWN * 0.2, run_time=0.8) for r in left], lag_ratio=1.6)],
        )
        self.say(
            line("Power first: 8² is 64, and the cube root of 64 is 4.",
                 f"Power first: {BR} eight squared is sixty-four, {BR} and the cube root of sixty-four is four."),
            anims=[Succession(*[FadeIn(r, shift=DOWN * 0.2, run_time=0.8) for r in right], lag_ratio=1.8)],
        )
        boxes = VGroup(*[SurroundingRectangle(l[2], color=RES_C, buff=0.14, corner_radius=0.12, stroke_width=3)
                         for l in (left, right)])
        self.say(
            "Same answer.",
            line(f"Root first just keeps the numbers {R('small')}.", f"{BR} Root first just keeps the numbers small."),
            anims=[Create(boxes, run_time=0.8), Indicate(left[1], color=RES_C, run_time=1.2)],
        )
        self.play(FadeOut(VGroup(top, chips, divider, left, right, boxes), shift=UP * 0.4), run_time=0.7)

    # ── Try it: 4^(3/2) = 8 ─────────────────────────────────────────────
    def four_three_halves(self):
        q = pw("4", "3/2", fs=BIG_FS)
        s1 = rtex("=", "(", rt(), "4}", ")", "^{3}", fs=MID_FS)
        s2 = auto(tex("=", "2", "^{3}", fs=MID_FS))
        s3 = tex("=", "8", fs=MID_FS)
        s3[1].set_color(RES_C)
        stack = fit_zone(VGroup(q, s1, s2, s3).arrange(DOWN, buff=0.3))
        slot = q.get_center()
        q.move_to(MATH)
        self.say(
            line(f"Try {B('4')}{sup(E('3/2'))}.", "Try four to the three halves."),
            anims=[FadeIn(q, shift=UP * 0.3, run_time=0.8)],
            gap=0.7,
        )
        self.say(
            line(f"Root first: √4 = 2, and 2³ = {R('8')}.", f"Root first: {BR} root four is two, {BR} and two cubed is eight."),
            anims=[Succession(q.animate(run_time=0.6).move_to(slot),
                              *[FadeIn(r, shift=DOWN * 0.2, run_time=0.7) for r in (s1, s2, s3)], lag_ratio=1.4)],
        )
        self.play(FadeOut(stack, shift=UP * 0.4), run_time=0.7)

    # ── Even root on the bottom: base can't be negative ─────────────────
    def catch(self):
        bad = rtex("(-4)", "^{1/2}", "=", rt(), "-4}", fs=MID_FS)
        mark = cross()
        und = label(W("undefined"), fs=40, weight=BOLD)
        row = fit(VGroup(bad, mark, und).arrange(RIGHT, buff=0.35)).move_to(MATH)
        self.say(
            line(f"One catch: an {E('even')} root on the bottom…", "One catch: with an even root on the bottom,"),
            line("…means the base can't be negative.", "the base can't be negative."),
            anims=[FadeIn(bad, shift=UP * 0.3, run_time=0.9),
                   Succession(Wait(2.4), AnimationGroup(GrowFromCenter(mark), FadeIn(und, shift=LEFT * 0.2),
                                                        run_time=0.8))],
        )
        self.play(FadeOut(row, shift=UP * 0.4), run_time=0.6)

    # ── Takeaway ────────────────────────────────────────────────────────
    def takeaway(self):
        forms = rtex("a", "^{m/n}", "=", "(", rt("n"), "a}", ")", "^{m}", "=", rt("n"), "a", "^{m}}", fs=MID_FS)
        hint = label(f"top: {E('power')}   ·   bottom: {B('root')}", fs=34, color=MUTED)
        card = self.card(VGroup(forms, hint).arrange(DOWN, buff=0.4), title="FRACTION EXPONENTS")
        self.say(
            line(f"Bottom: {B('root')}.", "Bottom: root."),
            line(f"Top: {E('power')}.", f"{BR} Top: power."),
            anims=[FadeIn(card, scale=0.94, run_time=1.0)],
        )
