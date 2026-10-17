from sci_common import *


def color_tens(m: MathTex):
    """Blue 10s, yellow exponents; plain numbers stay white."""
    for part, s in zip(m, m.tex_strings):
        core = s.strip("{}() ")
        if core == "10":
            part.set_color(BASE_C)
        elif s.lstrip("{( ").startswith("^"):
            part.set_color(EXP_C)
    return m


class S3Calculating(SciScene):
    PART = "3 / 3"

    def construct(self):
        givens = self.hook()
        expr = self.setup_expression(givens)
        lanes = self.split(expr)
        self.solve(expr, lanes)
        self.takeaway()
        self.outro()

    # ── Hook: Example 8 ─────────────────────────────────────────────────
    def hook(self):
        a = color_tens(tex("a", "=", "0.00046", fs=SMALL_FS))
        b = color_tens(tex("b", "=", "1.697", r"\times", "10", "^{22}", fs=SMALL_FS))
        c = color_tens(tex("c", "=", "2.91", r"\times", "10", "^{-18}", fs=SMALL_FS))
        goal = tex(r"{ab \over c}", "=", "?", fs=MID_FS)
        goal[2].set_color(MUTED)
        rows = VGroup(a, b, c).arrange(DOWN, buff=0.32, aligned_edge=LEFT)
        block = fit_zone(VGroup(rows, goal).arrange(DOWN, buff=0.5), height=MATH_MAX_H - 0.4)
        self.say(
            line("Find a times b, divided by c.", f"Find a times b, {BR} divided by c."),
            line("That's a lot of zeros.", f"{BR} That's a lot of zeros."),
            anims=[
                LaggedStart(*[FadeIn(r, shift=RIGHT * 0.3) for r in rows], lag_ratio=0.35, run_time=1.5),
                Succession(Wait(1.4), FadeIn(goal, shift=UP * 0.3, run_time=0.8)),
            ],
        )
        a2 = color_tens(tex("a", "=", "4.6", r"\times", "10", "^{-4}", fs=SMALL_FS))
        a2.move_to(a, aligned_edge=LEFT)
        self.say(
            line(f"First, write {B('a')} in scientific notation: 4.6 × {B('10')}{sup(E('−4'))}.",
                 f"First, write a in scientific notation: {BR} four point six, times ten to the negative fourth."),
            anims=[Succession(Wait(1.6), TransformMatchingTex(a, a2, run_time=1.2))],
        )
        return VGroup(a2, b, c, goal)

    # ── The full expression ─────────────────────────────────────────────
    def setup_expression(self, givens):
        expr = color_tens(tex("{(", "4.6", r"\times", "10", "^{-4}", ")(", "1.697", r"\times", "10", "^{22}", ")",
                              r"\over", "2.91", r"\times", "10", "^{-18}}", fs=SMALL_FS))
        fit(expr).move_to(MATH + UP * 1.55)
        a2, b, c, goal = givens
        self.play(
            TransformFromCopy(a2[2:6], expr[1:5]),
            TransformFromCopy(b[2:6], expr[6:10]),
            TransformFromCopy(c[2:6], expr[12:16]),
            FadeIn(VGroup(expr[0], expr[5], expr[10], expr[11])),
            FadeOut(givens, shift=DOWN * 0.3),
            run_time=1.3,
        )
        return expr

    # ── Two lanes: numbers | powers of ten ──────────────────────────────
    def split(self, expr):
        nums = tex("{4.6", r"\cdot", "1.697", r"\over", "2.91}", fs=SMALL_FS)
        tens = color_tens(tex("{10", "^{-4}", r"\cdot", "10", "^{22}", r"\over", "10", "^{-18}}", fs=SMALL_FS))
        times = tex(r"\times", fs=SMALL_FS)
        lanes = VGroup(nums, times, tens).arrange(RIGHT, buff=0.45)
        fit(lanes).move_to(MATH - UP * 0.35)
        lane_boxes = VGroup(
            SurroundingRectangle(nums, color=INK, buff=0.22, corner_radius=0.16, stroke_width=2.5, stroke_opacity=0.6),
            SurroundingRectangle(tens, color=BASE_C, buff=0.22, corner_radius=0.16, stroke_width=2.5),
        )
        tags = VGroup(
            label("numbers", fs=30, color=INK).next_to(lane_boxes[0], DOWN, buff=0.18),
            label("powers of 10", fs=30, color=BASE_C).next_to(lane_boxes[1], DOWN, buff=0.18),
        )
        self.say(
            line("Split it in two: the numbers, and the powers of ten.",
                 f"Now split it in two: {BR} the numbers, {BR} and the powers of ten."),
            anims=[
                Succession(
                    AnimationGroup(
                        TransformFromCopy(expr[1], nums[0], path_arc=0.4),
                        TransformFromCopy(expr[6], nums[2], path_arc=0.4),
                        TransformFromCopy(expr[11], nums[3]),
                        TransformFromCopy(expr[12], nums[4], path_arc=-0.4),
                        FadeIn(nums[1]),
                        run_time=1.4,
                    ),
                    AnimationGroup(
                        TransformFromCopy(expr[3:5], tens[0:2], path_arc=-0.4),
                        TransformFromCopy(expr[8:10], tens[3:5], path_arc=-0.4),
                        TransformFromCopy(expr[11], tens[5]),
                        TransformFromCopy(expr[14:16], tens[6:8], path_arc=0.4),
                        FadeIn(tens[2]), FadeIn(times),
                        run_time=1.4,
                    ),
                    AnimationGroup(Create(lane_boxes), FadeIn(tags, shift=UP * 0.15), run_time=0.8),
                )
            ],
        )
        self.lane_extras = VGroup(lane_boxes, tags)
        return nums, times, tens

    # ── Solve each lane, combine, round ─────────────────────────────────
    def solve(self, expr, lanes):
        nums, times, tens = lanes
        boxes, tags = self.lane_extras
        p1 = color_tens(tex("10", r"^{-4+22-(-18)}", fs=SMALL_FS))
        p2 = color_tens(tex("10", "^{36}", fs=SMALL_FS))
        for m in (p1, p2):
            m.move_to(tens)
        self.say(
            line(f"Powers of {B('10')}: add the top exponents, subtract the bottom one…",
                 f"Powers of ten: {BR} add the top exponents, {BR} subtract the bottom one."),
            line(f"…{B('10')}{sup(E('36'))}.", f"{BR} Ten to the thirty-sixth."),
            anims=[FadeOut(VGroup(boxes, tags), run_time=0.5)],
            steps=[
                [ReplacementTransform(tens, p1, run_time=1.2)],
                1.2,
                [ReplacementTransform(p1, p2, run_time=1.0)],
            ],
        )
        n2 = tex(r"\approx 2.68", fs=SMALL_FS).move_to(nums)
        self.say(
            line("The numbers: about 2.68.", f"The numbers: {BR} about two point six eight."),
            anims=[ReplacementTransform(nums, n2, run_time=1.2)],
        )
        combined = color_tens(tex(r"\approx", "2.68", r"\times", "10", "^{36}", fs=MID_FS))
        combined.move_to(MATH - UP * 0.35)
        rounded = color_tens(tex(r"\approx", "2.7", r"\times", "10", "^{36}", fs=MID_FS))
        rounded[1].set_color(RES_C)
        rounded[3].set_color(RES_C)
        rounded[4].set_color(RES_C)
        rounded.move_to(combined)
        sig = chip("2 SIG FIGS", color=RES_C).next_to(rounded, DOWN, buff=0.5)
        least = SurroundingRectangle(expr[1], color=EXP_C, buff=0.08, corner_radius=0.08, stroke_width=3)
        self.say(
            line(f"The least precise number, {E('0.00046')}, has two significant figures…",
                 f"The least precise number, {BR} zero point zero zero zero four six, {BR} has two significant figures."),
            line(f"…so round to two: {R('2.7')} × {R('10')}{sup(R('36'))}.",
                 f"{BR} So round to two: {BR} two point seven, times ten to the thirty-sixth."),
            anims=[
                ReplacementTransform(VGroup(n2, times, p2), combined, run_time=1.1),
                Succession(Wait(1.2), Create(least, run_time=0.7)),
            ],
            steps=[[ReplacementTransform(combined, rounded), FadeIn(sig, shift=UP * 0.2)]],
        )
        self.play(Circumscribe(rounded, color=RES_C, buff=0.15), run_time=1.1)
        self.play(FadeOut(VGroup(expr, least, rounded, sig), shift=UP * 0.4), run_time=0.7)

    # ── Takeaway ────────────────────────────────────────────────────────
    def takeaway(self):
        lhs = color_tens(tex("(", "a", r"\times", "10", "^{m}", ")(", "b", r"\times", "10", "^{n}", ")", fs=MID_FS))
        rhs = color_tens(tex("=", "ab", r"\times", "10", "^{m+n}", fs=MID_FS))
        rule = VGroup(lhs, rhs).arrange(DOWN, buff=0.35)
        card = self.card(rule, title="MULTIPLYING")
        self.say(
            line(f"Numbers with numbers, powers of {B('10')} with powers of {B('10')}.",
                 f"Numbers with numbers, {BR} powers of ten with powers of ten."),
            anims=[FadeIn(card, scale=0.94, run_time=1.0)],
        )
