from ratz_common import *

FS = SMALL_FS  # fractions containing radicals render tall


class Z2MissingPiece(RatzScene):
    PART = "2 / 2"
    GAP = 0.3

    def construct(self):
        q = self.hook()
        self.cube_root(q)
        self.seventh_root()
        self.takeaway()
        self.outro()

    # ── Hook: 1/∛5 — multiplying by ∛5 fails ────────────────────────────
    def hook(self):
        q = rtex("{1", r"\over", rt(3), "5}}", fs=MID_FS)
        q[0].set_color(INK)
        q.move_to(MATH + UP * 0.9)
        tryit = rtex(rt(3), "5}", r"\cdot", rt(3), "5}", "=", rt(3), "25}", fs=FS)
        tryit[6:].set_color(WARN_C)
        fail = cross(64)
        row = VGroup(tryit, fail).arrange(RIGHT, buff=0.35).move_to(MATH + DOWN * 0.9)
        self.say(
            line("Rationalize 1 over the cube root of 5.", "Rationalize one over the cube root of five."),
            line(f"Multiply by ∛5? Below you'd get ∛25: {W('still a radical')}.",
                 f"Multiply by cube root five? {BR} Underneath you'd get cube root twenty-five: {BR} still a radical."),
            anims=[FadeIn(q, shift=UP * 0.3, run_time=0.9),
                   Succession(Wait(2.6), FadeIn(tryit[0:5], shift=UP * 0.2, run_time=0.8)),
                   Succession(Wait(4.6), FadeIn(tryit[5:], shift=LEFT * 0.2, run_time=0.8)),
                   Succession(Wait(6.2), GrowFromCenter(fail, run_time=0.5))],
        )
        self.play(FadeOut(row, shift=DOWN * 0.3), q.animate.scale(0.75).move_to(MATH + UP * 1.75), run_time=0.8)
        return q

    # ── The exponent meter: 1 of 3 → fill 2 more ────────────────────────
    def cube_root(self, q):
        rad = rtex(rt(3), "5", "^{1}}", fs=FS)
        m = meter(3, 1, width=3.0)
        row = VGroup(rad, m).arrange(RIGHT, buff=0.5).move_to(MATH + UP * 0.2)
        count = label(f"{E('1')} of 3 slots", fs=34, color=MUTED).next_to(m, DOWN, buff=0.22)
        self.say(
            line(f"A cube root clears when the exponent inside reaches {E('3')}.",
                 "A cube root clears when the exponent inside reaches three."),
            line(f"5{sup('1')} fills just one slot.", f"{BR} Five to the first fills just one slot."),
            anims=[FadeIn(rad, shift=UP * 0.2, run_time=0.8),
                   Succession(Wait(1.4), AnimationGroup(LaggedStart(*[GrowFromEdge(s, LEFT) for s in m], lag_ratio=0.2),
                                                        run_time=1.0)),
                   Succession(Wait(3.4), FadeIn(count, shift=UP * 0.15, run_time=0.6))],
        )
        add = rtex(r"\cdot", rt(3), "5", "^{2}}", fs=FS, results=[2, 3])
        add.next_to(rad, RIGHT, buff=0.15)
        full = rtex("=", rt(3), "5", "^{3}}", "=", "5", fs=FS, results=[5])
        line2 = VGroup(rad.copy(), add.copy(), full).arrange(RIGHT, buff=0.15)
        fit(line2).move_to(MATH + DOWN * 1.45)
        self.say(
            line(f"So multiply by the cube root of 5{sup(R('2'))}: 1 + 2 = 3…",
                 f"So multiply by the cube root of five squared: {BR} one plus two is three,"),
            line(f"…and the cube root of 5{sup('3')} is {R('5')}.", "and the cube root of five cubed is five."),
            anims=[*[s.animate(run_time=0.8).set_fill(RES_C, 0.95) for s in m[1:]],
                   Transform(count, label(f"{R('3')} of 3: the root clears", fs=34, color=MUTED).move_to(count),
                             run_time=0.8)],
            steps=[[FadeIn(line2, shift=UP * 0.2)]],
        )
        result = rtex("{1", r"\over", rt(3), "5}}", "=", r"{\sqrt[3]{", "25}", r"\over", "5}", fs=FS,
                      results=[5, 6, 8])
        result[0].set_color(INK)
        result[8].set_color(RES_C)
        result.move_to(MATH + DOWN * 0.1)
        self.say(
            line(f"Answer: {R('∛25 / 5')}.", "So the answer is cube root twenty-five, over five."),
            anims=[FadeOut(VGroup(rad, m, count, line2), run_time=0.6),
                   ReplacementTransform(q, result[0:4], run_time=1.0),
                   Succession(Wait(0.8), FadeIn(result[4:], shift=LEFT * 0.3, run_time=0.9))],
            gap=0.2,
        )
        self.play(FadeOut(result, shift=UP * 0.4), run_time=0.7)

    # ── Example 14(c): ⁷√(1/a²) = ⁷√(a⁵)/a ─────────────────────────────
    def seventh_root(self):
        q = rtex("{1", r"\over", rt(7), "a", "^{2}}}", fs=FS)
        q[0].set_color(INK)
        q.move_to(MATH + UP * 1.6)
        m = meter(7, 2, width=SAFE_W - 0.8)
        m.move_to(MATH + DOWN * 0.05)
        count = label(f"a{sup(E('2'))}: {E('2')} of 7 slots", fs=34, color=MUTED).next_to(m, DOWN, buff=0.22)
        self.say(
            line("Harder: the 7th root of 1 over a².", "Harder: the seventh root of one, over a squared."),
            line(f"a{sup('2')} fills 2 of 7 slots…", f"{BR} a squared fills two of seven slots,"),
            anims=[FadeIn(q, shift=UP * 0.3, run_time=0.8),
                   Succession(Wait(2.6), LaggedStart(*[GrowFromEdge(s, LEFT) for s in m], lag_ratio=0.1, run_time=1.0)),
                   Succession(Wait(3.8), FadeIn(count, shift=UP * 0.15, run_time=0.6))],
        )
        result = rtex("=", r"{\sqrt[7]{", "a", "^{5}}", r"\over", "a}", fs=FS, results=[1, 2, 3, 5])
        result.next_to(q, RIGHT, buff=0.3)
        both = VGroup(q.copy(), result)
        fit(both)
        self.say(
            line(f"…so multiply by the 7th root of a{sup(R('5'))}.", "so multiply by the seventh root of a to the fifth."),
            anims=[LaggedStart(*[s.animate.set_fill(RES_C, 0.95) for s in m[2:]], lag_ratio=0.15, run_time=1.4),
                   Transform(count, label(f"{R('7')} of 7: the root clears", fs=34, color=MUTED).move_to(count),
                             run_time=0.8)],
            steps=[lambda: [q.animate.move_to(both[0]), FadeIn(result, shift=LEFT * 0.3)]],
        )
        self.play(FadeOut(VGroup(q, result, m, count), shift=UP * 0.4), run_time=0.7)

    # ── Takeaway ────────────────────────────────────────────────────────
    def takeaway(self):
        l1 = rtex(rt("n"), "a", "^{m}}", r"\cdot", rt("n"), "a", "^{n-m}}", fs=MID_FS)
        l2 = rtex("=", rt("n"), "a", "^{n}}", "=", "a", fs=MID_FS, results=[5])
        hint = label(f"Fill the exponent up to {E('n')}.", fs=36, color=MUTED)
        card = self.card(VGroup(l1, l2, hint).arrange(DOWN, buff=0.3), title="THE MISSING PIECE")
        self.say(
            line(f"Fill the exponent up to {E('n')}…", "Fill the exponent up to n,"),
            line("…and the root clears.", "and the root clears."),
            anims=[FadeIn(card, scale=0.94, run_time=1.0)],
        )
