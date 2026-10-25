try:
    from .ratz_common import *
except ImportError:  # Manim loading this file directly
    from ratz_common import *


def over_root(num, rad, fs=BIG_FS):
    """num / √rad"""
    m = rtex("{" + num, r"\over", rt(), rad + "}}", fs=fs)
    m[0].set_color(INK)
    return m


def root_over(rad, den, fs=BIG_FS, results=()):
    """√rad / den"""
    m = rtex(r"{\sqrt{", rad + "}", r"\over", den + "}", fs=fs, results=results)
    if not results:
        m[3].set_color(INK)
    return m


class Z1DisguisedOne(RatzScene):
    PART = "1 / 2"

    def construct(self):
        self.hook()
        self.disguise()
        self.example()
        self.takeaway()
        self.outro()

    # ── Hook: 1/√2 vs √2/2 ──────────────────────────────────────────────
    def hook(self):
        a = over_root("1", "2")
        b = root_over("2", "2")
        q = tex("?", fs=BIG_FS, color=MUTED)
        row = VGroup(a, q, b).arrange(RIGHT, buff=0.7).move_to(MATH + UP * 0.45)
        da = tex(r"0.7071\ldots", fs=50, color=MUTED).next_to(a, DOWN, buff=0.45)
        db = tex(r"0.7071\ldots", fs=50, color=MUTED).next_to(b, DOWN, buff=0.45)
        eq = tex("=", fs=BIG_FS, color=RES_C).move_to(q)
        self.say(
            line("Which is bigger: 1/√2, or √2/2?", "Which is bigger: one over root two, or root two over two?"),
            anims=[LaggedStart(FadeIn(a, shift=UP * 0.3), FadeIn(q, scale=1.5), FadeIn(b, shift=UP * 0.3),
                               lag_ratio=0.4, run_time=1.6)],
        )
        self.say(
            line(f"{R('Neither.')} Both are 0.7071…", f"Neither. {BR} Both are zero point seven zero seven one."),
            anims=[FadeIn(da, shift=UP * 0.2, run_time=0.7), FadeIn(db, shift=UP * 0.2, run_time=0.7),
                   Succession(Wait(0.8), Transform(q, eq, run_time=0.7))],
        )
        bad = SurroundingRectangle(a[2:4], color=WARN_C, buff=0.1, corner_radius=0.1, stroke_width=3.5)
        good = SurroundingRectangle(b[3], color=RES_C, buff=0.1, corner_radius=0.1, stroke_width=3.5)
        tag = label(f"standard form: {R('no radical')} below", fs=34, color=MUTED).next_to(VGroup(da, db), DOWN,
                                                                                          buff=0.45)
        self.say(
            line(f"The second is in {R('standard form')}: no radical in the denominator.",
                 f"The second one is in standard form: {BR} no radical in the denominator."),
            anims=[Create(bad, run_time=0.8), Succession(Wait(0.9), Create(good, run_time=0.8)),
                   Succession(Wait(1.6), FadeIn(tag, shift=UP * 0.2, run_time=0.7))],
        )
        self.play(FadeOut(VGroup(a, q, b, da, db, bad, good, tag), shift=UP * 0.4), run_time=0.7)

    # ── Multiply by √2/√2 = 1 ───────────────────────────────────────────
    def disguise(self):
        m = rtex("{1", r"\over", rt(), "2}}", r"\cdot", r"{\sqrt{", "2}", r"\over", rt(), "2}}", fs=SMALL_FS)
        m[0].set_color(INK)
        m.move_to(MATH + UP * 1.5)
        mask = SurroundingRectangle(m[5:10], color=EXP_C, buff=0.14, corner_radius=0.14, stroke_width=3.5)
        one = tex("= 1", fs=60, color=EXP_C).next_to(mask, DOWN, buff=0.2)
        self.say(
            line(f"Multiply by √2/√2. That's just {E('1')} in disguise…",
                 f"To get there, multiply by root two over root two. {BR} That's just one, in disguise,"),
            line("…so the value doesn't change.", "so the value doesn't change."),
            anims=[FadeIn(m[0:4], shift=UP * 0.3, run_time=0.8),
                   Succession(Wait(1.6), FadeIn(m[4:], shift=LEFT * 0.3, run_time=0.9)),
                   Succession(Wait(3.6), AnimationGroup(Create(mask), FadeIn(one, shift=UP * 0.2), run_time=0.9))],
        )
        side = 1.2
        sq = Square(side, fill_color=BASE_C, fill_opacity=0.3, stroke_color=BASE_C, stroke_width=3)
        sq.move_to([CX - 1.55, MATH_Y - 0.95, 0])
        s_bot = rtex(rt(), "2}", fs=50).next_to(sq, DOWN, buff=0.12)
        s_left = rtex(rt(), "2}", fs=50).next_to(sq, LEFT, buff=0.12)
        area = tex("2", fs=72, color=RES_C).move_to(sq)
        result = rtex("=", r"{\sqrt{", "2}", r"\over", "2}", fs=SMALL_FS, results=[1, 2, 4])
        result[3].set_color(RES_C)
        result.next_to(m, DOWN, buff=0.25).set_x(CX + 1.4).match_y(sq)
        self.say(
            line(f"Below: √2 · √2 = {R('2')}. The radical is gone.",
                 f"Underneath, root two times root two is two. {BR} The radical is gone."),
            anims=[FadeOut(VGroup(mask, one), run_time=0.5),
                   DrawBorderThenFill(sq, run_time=1.0),
                   Succession(Wait(0.6), AnimationGroup(FadeIn(s_bot), FadeIn(s_left), run_time=0.7)),
                   Succession(Wait(1.6), FadeIn(area, scale=1.4, run_time=0.7))],
            steps=[[FadeIn(result, shift=LEFT * 0.3)]],
        )
        self.play(FadeOut(VGroup(m, sq, s_bot, s_left, area, result), shift=UP * 0.4), run_time=0.7)

    # ── Example 14(a): 2/√3 = 2√3/3 ─────────────────────────────────────
    def example(self):
        m = rtex("{2", r"\over", rt(), "3}}", r"\cdot", r"{\sqrt{", "3}", r"\over", rt(), "3}}", "=",
                 r"{2\sqrt{", "3}", r"\over", "3}", fs=BIG_FS, results=[11, 12, 13, 14])
        m[0].set_color(INK)
        fit(m).move_to(MATH)
        self.say(
            line("Same move for 2/√3: multiply by √3/√3…",
                 f"Same move for two over root three: {BR} multiply by root three over root three,"),
            line(f"…and you get {R('2√3/3')}.", "and you get two root three, over three."),
            anims=[FadeIn(m[0:4], shift=UP * 0.3, run_time=0.8),
                   Succession(Wait(2.0), FadeIn(m[4:10], shift=LEFT * 0.3, run_time=0.9)),
                   Succession(Wait(4.6), FadeIn(m[10:], shift=LEFT * 0.3, run_time=0.9))],
        )
        self.play(FadeOut(m, shift=UP * 0.4), run_time=0.7)

    # ── Takeaway ────────────────────────────────────────────────────────
    def takeaway(self):
        rule = rtex("{1", r"\over", rt(), "a}}", "=", r"{\sqrt{", "a}", r"\over", "a}", fs=MID_FS)
        rule[0].set_color(INK)
        hint = label(f"multiply by √a/√a = {E('1')}", fs=36, color=MUTED)
        card = self.card(VGroup(rule, hint).arrange(DOWN, buff=0.4), title="RATIONALIZING")
        self.say(
            line(f"Multiply by a disguised {E('1')}…", "Multiply by a disguised one,"),
            line("…and the radical leaves the denominator.", "and the radical leaves the denominator."),
            anims=[FadeIn(card, scale=0.94, run_time=1.0)],
        )
