from rad_common import *


def iso_cube(edge=1.4, splits=2):
    """An isometric cube (three shaded faces) divided into splits³ small cubes."""
    ex = np.array([0.866, 0.5, 0]) * edge
    ey = np.array([-0.866, 0.5, 0]) * edge
    dn = np.array([0, -1, 0]) * edge
    o = ORIGIN
    faces = VGroup(
        Polygon(o, o + ex, o + ex + ey, o + ey, fill_color=BASE_C, fill_opacity=0.55),
        Polygon(o, o + ey, o + ey + dn, o + dn, fill_color=BASE_C, fill_opacity=0.32),
        Polygon(o, o + ex, o + ex + dn, o + dn, fill_color=BASE_C, fill_opacity=0.2),
    ).set_stroke(BASE_C, 2.5)
    lines = VGroup()
    for k in range(1, splits):
        t = k / splits
        for a, b in ((ex, ey), (ey, ex), (ey, dn), (dn, ey), (ex, dn), (dn, ex)):
            lines.add(Line(o + a * t, o + a * t + b, stroke_width=1.5, color=BASE_C))
    cube = VGroup(faces, lines)
    cube.left_edge = (o + ey + dn, o + ey)  # endpoints of the left vertical edge
    return cube


class R1WhatIsARoot(RadScene):
    PART = "1 / 4"

    def construct(self):
        self.hook()
        self.geometry()
        self.nth()
        self.even_odd()
        self.takeaway()
        self.outro()

    # ── Hook: √9 = ±3? ──────────────────────────────────────────────────
    def hook(self):
        s1 = auto(tex("3", "^{2}", "=", "9", fs=SMALL_FS))
        s2 = auto(tex("(-3)", "^{2}", "=", "9", fs=SMALL_FS))
        for s in (s1, s2):
            s[3].set_color(INK)
        squares = VGroup(s1, s2).arrange(RIGHT, buff=1.0)
        q = rtex(rt(), "9}", "=", r"\pm 3", "?")
        q[3].set_color(WARN_C)
        q[4].set_color(MUTED)
        block = VGroup(squares, q).arrange(DOWN, buff=0.9).move_to(MATH)
        self.say(
            line(f"{B('3')}{sup(E('2'))} = 9, and ({B('−3')}){sup(E('2'))} = 9 too.",
                 f"Three squared is nine. {BR} So is negative three squared."),
            line("So is √9 = ±3?", "So is the square root of nine, plus or minus three?"),
            anims=[
                LaggedStart(FadeIn(s1, shift=UP * 0.3), FadeIn(s2, shift=UP * 0.3), lag_ratio=0.6, run_time=1.6),
                Succession(Wait(2.6), FadeIn(q, shift=UP * 0.3, run_time=0.9)),
            ],
        )
        ans = rtex(rt(), "9}", "=", "3", results=[3]).move_to(q)
        rule = rtex(rt(), "a}", "=", "b", fs=54)
        rule_text = label(f"means  {B('b')}² = {B('a')}  and  {B('b')} ≥ 0", fs=32, color=MUTED)
        definition = VGroup(rule, rule_text).arrange(RIGHT, buff=0.35).next_to(ans, DOWN, buff=0.6)
        fit(definition)
        self.say(
            line(f"No. The √ symbol means only the {R('positive')} root…",
                 f"No. {BR} The root symbol means only the positive root:"),
            line(f"…so √9 = {R('3')}.", "three."),
            anims=[Wait(0.5), q[3].animate(run_time=0.5).scale(1.2)],
            steps=[
                [ReplacementTransform(q[0:3], ans[0:3]), ReplacementTransform(q[3], ans[3]), FadeOut(q[4]),
                 FadeOut(squares, shift=UP * 0.3)],
                [FadeIn(definition, shift=UP * 0.2)],
            ],
        )
        self.play(FadeOut(VGroup(ans, definition), shift=UP * 0.4), run_time=0.7)

    # ── Square of area 9, cube of volume 8 ──────────────────────────────
    def geometry(self):
        u = 0.62
        grid = VGroup(
            *[Square(u, fill_color=BASE_C, fill_opacity=0.35, stroke_color=BASE_C, stroke_width=2.5) for _ in range(9)]
        ).arrange_in_grid(3, 3, buff=0)
        grid.move_to([CX - 1.85, MATH_Y + 0.55, 0])
        area = label(f"area {B('9')}", fs=34).next_to(grid, DOWN, buff=0.3)
        side = Brace(grid, LEFT, buff=0.12, color=RES_C)
        side_lbl = tex("3", fs=60, color=RES_C).next_to(side, LEFT, buff=0.12)
        r_sq = rtex(rt(), "9}", "=", "3", fs=64, results=[3]).next_to(area, DOWN, buff=0.35)

        cube = iso_cube(1.35)
        c0 = cube.get_center()
        cube.move_to([CX + 1.85, MATH_Y + 0.5, 0])
        offset = cube.get_center() - c0
        p_lo, p_hi = (np.array(p) + offset for p in cube.left_edge)
        edge = BraceBetweenPoints(p_lo, p_hi, direction=LEFT, color=RES_C, buff=0.08)
        edge_lbl = tex("2", fs=60, color=RES_C).next_to(edge, LEFT, buff=0.1)
        vol = label(f"volume {B('8')}", fs=34).next_to(cube, DOWN, buff=0.3).match_y(area)
        r_cube = rtex(rt(3), "8}", "=", "2", fs=64, results=[3]).next_to(vol, DOWN, buff=0.35)

        self.say(
            line("Picture it: a square with area 9 has side 3.", f"Picture it: {BR} a square with area nine has side three."),
            anims=[
                LaggedStart(*[GrowFromCenter(s) for s in grid], lag_ratio=0.08, run_time=1.4),
                Succession(Wait(1.2), AnimationGroup(FadeIn(area), GrowFromCenter(side), FadeIn(side_lbl),
                                                     run_time=0.8)),
                Succession(Wait(2.2), FadeIn(r_sq, shift=UP * 0.2, run_time=0.8)),
            ],
        )
        self.say(
            line("And a cube with volume 8 has edge 2: the cube root of 8.",
                 f"And a cube with volume eight has edge two. {BR} That's the cube root of eight."),
            anims=[
                DrawBorderThenFill(cube[0], run_time=1.4),
                Create(cube[1], run_time=1.0),
                Succession(Wait(1.3), AnimationGroup(FadeIn(vol), GrowFromCenter(edge), FadeIn(edge_lbl),
                                                     run_time=0.8)),
                Succession(Wait(2.4), FadeIn(r_cube, shift=UP * 0.2, run_time=0.8)),
            ],
        )
        self.play(FadeOut(VGroup(grid, area, side, side_lbl, r_sq, cube, vol, edge, edge_lbl, r_cube),
                          shift=UP * 0.4), run_time=0.7)

    # ── nth roots ───────────────────────────────────────────────────────
    def nth(self):
        gen = rtex(rt("n"), "a}", "=", "b")
        means = tex(r"\iff", fs=MID_FS, color=MUTED)
        power = auto(tex("b", "^{n}", "=", "a"))
        top = fit(VGroup(gen, means, power).arrange(RIGHT, buff=0.4)).move_to(MATH + UP * 0.9)
        ex = rtex(rt(4), "81}", "=", "3", fs=MID_FS, results=[3])
        because = auto(tex(r"\text{since }", "3", "^{4}", "=", "81", fs=60))
        because[0].set_color(MUTED)
        because[4].set_color(INK)
        bottom = VGroup(ex, because).arrange(DOWN, buff=0.3).move_to(MATH + DOWN * 0.95)
        self.say(
            line("In general, the nth root undoes the nth power.", "In general, the nth root undoes the nth power."),
            line("The 4th root of 81 is 3.", "The fourth root of eighty-one is three."),
            anims=[
                LaggedStart(FadeIn(gen, shift=UP * 0.2), FadeIn(means), FadeIn(power, shift=UP * 0.2),
                            lag_ratio=0.4, run_time=1.6),
                Succession(Wait(2.8), FadeIn(ex, shift=UP * 0.2, run_time=0.8), Wait(0.3),
                           FadeIn(because, shift=UP * 0.2, run_time=0.7)),
            ],
        )
        self.play(FadeOut(VGroup(top, bottom), shift=UP * 0.4), run_time=0.7)

    # ── Odd roots take negatives, even roots don't ──────────────────────
    def even_odd(self):
        odd = rtex(rt(3), "-8}", "=", "-2", fs=MID_FS, results=[3])
        odd_chk = check()
        odd_why = auto(tex("(-2)", "^{3}", "=", "-8", fs=50))
        odd_why[0].set_color(MUTED)
        odd_why[2:].set_color(MUTED)
        r1 = VGroup(VGroup(odd, odd_chk).arrange(RIGHT, buff=0.45), odd_why).arrange(DOWN, buff=0.2)
        even = rtex(rt(), "-8}", fs=MID_FS)
        even_x = cross()
        undefined = label(W("undefined"), fs=40, weight=BOLD)
        r2 = VGroup(even, even_x, undefined).arrange(RIGHT, buff=0.4)
        rows = VGroup(r1, r2).arrange(DOWN, buff=0.9).move_to(MATH)
        self.say(
            line(f"Odd roots handle negatives: the cube root of −8 is {R('−2')}.",
                 f"Odd roots can handle negatives: {BR} the cube root of negative eight is negative two."),
            anims=[
                FadeIn(odd, shift=UP * 0.3, run_time=0.9),
                Succession(Wait(2.4), AnimationGroup(FadeIn(odd_why, shift=UP * 0.2), GrowFromCenter(odd_chk),
                                                     run_time=0.8)),
            ],
        )
        self.say(
            "But no real number squared is negative…",
            line(f"…so √−8 is {W('undefined')}.", "so root negative eight is undefined."),
            anims=[
                FadeIn(even, shift=UP * 0.3, run_time=0.9),
                Succession(Wait(2.2), AnimationGroup(GrowFromCenter(even_x), FadeIn(undefined, shift=LEFT * 0.2),
                                                     run_time=0.8)),
            ],
        )
        self.play(FadeOut(rows, shift=UP * 0.4), run_time=0.7)

    # ── Takeaway ────────────────────────────────────────────────────────
    def takeaway(self):
        gen = rtex(rt("n"), "a}", "=", "b", fs=MID_FS)
        means = tex(r"\iff", fs=MID_FS * 0.8, color=MUTED)
        power = auto(tex("b", "^{n}", "=", "a", fs=MID_FS))
        top = VGroup(gen, means, power).arrange(RIGHT, buff=0.35)
        note = label(f"{E('Even')} n: a ≥ 0 and b ≥ 0", fs=32, color=MUTED)
        card = self.card(VGroup(top, note).arrange(DOWN, buff=0.4), title="ROOTS UNDO POWERS")
        self.say(
            "A root undoes a power.",
            line("Even roots need non-negative numbers.", f"{BR} Even roots need numbers that aren't negative."),
            anims=[FadeIn(card, scale=0.94, run_time=1.0)],
        )
