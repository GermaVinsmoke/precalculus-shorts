from poly_common import *


class P3TermsVsFactors(PolyScene):
    PART = "3 / 3"

    def construct(self):
        self.hook()
        p = self.shared_factor()
        out = self.step_outside(p)
        self.check_back(out)
        self.takeaway()
        self.outro()

    # ── Hook: 2 + 3 vs 2 · 3 ────────────────────────────────────────────
    def hook(self):
        add = tex("2", "+", "3", fs=HERO_FS * 0.7)
        mul = tex("2", r"\cdot", "3", fs=HERO_FS * 0.7)
        pair = VGroup(add, mul).arrange(RIGHT, buff=1.4).move_to(MATH + UP * 0.6)
        t_lbl = label(B("terms"), fs=44, weight=BOLD).next_to(add, DOWN, buff=0.7)
        f_lbl = label(E("factors"), fs=44, weight=BOLD).next_to(mul, DOWN, buff=0.7)
        t_arr = VGroup(*[Arrow(t_lbl.get_top(), add[i].get_bottom(), buff=0.12, color=BASE_C, stroke_width=4,
                               max_tip_length_to_length_ratio=0.25) for i in (0, 2)])
        f_arr = VGroup(*[Arrow(f_lbl.get_top(), mul[i].get_bottom(), buff=0.12, color=EXP_C, stroke_width=4,
                               max_tip_length_to_length_ratio=0.25) for i in (0, 2)])
        self.say(
            line("In 2 + 3 and 2 · 3, the 2 has a different name.",
                 f"In two plus three, and two times three, {BR} the two has a different name."),
            anims=[LaggedStart(FadeIn(add, shift=UP * 0.3), FadeIn(mul, shift=UP * 0.3), lag_ratio=0.5, run_time=1.4),
                   Succession(Wait(2.6), AnimationGroup(Indicate(add[0]), Indicate(mul[0]), run_time=0.9))],
        )
        self.say(
            line(f"Things you add are {B('terms')}.", "Things you add are terms."),
            line(f"Things you multiply are {E('factors')}.", f"{BR} Things you multiply are factors."),
            anims=[AnimationGroup(FadeIn(t_lbl, shift=UP * 0.2), *[GrowArrow(a) for a in t_arr], run_time=0.9),
                   Succession(Wait(1.8), AnimationGroup(FadeIn(f_lbl, shift=UP * 0.2), *[GrowArrow(a) for a in f_arr],
                                                        run_time=0.9))],
        )
        self.play(FadeOut(VGroup(pair, t_lbl, f_lbl, t_arr, f_arr), shift=UP * 0.4), run_time=0.7)

    # ── ax + 2ay: both terms contain a ──────────────────────────────────
    def shared_factor(self):
        p = poly([["a", "x"], ["+", "2", "a", "y"]], fs=HERO_FS * 0.75)
        p.move_to(MATH + UP * 0.45)
        tiles = VGroup(*[tile(t, buff=0.14) for t in p.terms])
        tags = VGroup(*[label(B("term"), fs=32, weight=BOLD).next_to(tl, UP, buff=0.15) for tl in tiles])
        inside = VGroup(
            ptex("a", r"\cdot", "x", fs=60).next_to(tiles[0], DOWN, buff=0.45),
            ptex("2", r"\cdot", "a", r"\cdot", "y", fs=60).next_to(tiles[1], DOWN, buff=0.45),
        )
        self.say(
            line("Here are two terms…", "Here are two terms."),
            anims=[FadeIn(p, shift=UP * 0.3, run_time=0.9),
                   Succession(Wait(0.6), AnimationGroup(Create(tiles), FadeIn(tags, shift=DOWN * 0.1), run_time=0.9))],
            gap=0.2,
        )
        self.say(
            line(f"Look inside: each one has a factor of {E('a')}.", "Look inside: each one has a factor of a."),
            anims=[FadeIn(inside, shift=DOWN * 0.2, run_time=0.9),
                   Succession(Wait(1.4), AnimationGroup(
                       p[0].animate.set_color(EXP_C), p[4].animate.set_color(EXP_C),
                       inside[0][0].animate.set_color(EXP_C), inside[1][2].animate.set_color(EXP_C),
                       run_time=1.1))],
        )
        self.play(FadeOut(VGroup(tiles, tags, inside)), run_time=0.6)
        return p

    # ── The shared factor steps outside ─────────────────────────────────
    def step_outside(self, p):
        out = ptex("a", "(", "x", "+", "2", "y", ")", fs=HERO_FS * 0.75)
        out[0].set_color(EXP_C)
        out.move_to(MATH + UP * 0.45)
        self.say(
            line("A factor shared by every term can step outside…",
                 "A factor shared by every term can step outside:"),
            line(f"…{E('a')}(x + 2y).", f"{BR} a, times x plus two y."),
            anims=[Wait(0.8)],
            steps=[[
                ReplacementTransform(VGroup(p[0], p[4]), out[0], path_arc=-PI / 3),
                ReplacementTransform(p[1], out[2]), ReplacementTransform(p[2], out[3]),
                ReplacementTransform(p[3], out[4]), ReplacementTransform(p[5], out[5]),
                FadeIn(out[1]), FadeIn(out[6]),
            ]],
        )
        return out

    # ── Multiply back to check ──────────────────────────────────────────
    def check_back(self, out):
        arcs = VGroup(
            CurvedArrow(out[0].get_top() + UP * 0.05, out[2].get_top() + UP * 0.05, angle=-PI / 2, color=EXP_C,
                        stroke_width=3, tip_length=0.15),
            CurvedArrow(out[0].get_top() + UP * 0.05, VGroup(out[4], out[5]).get_top() + UP * 0.05, angle=-PI / 2,
                        color=EXP_C, stroke_width=3, tip_length=0.15),
        )
        back = ptex("=", "a", "x", "+", "2", "a", "y", fs=MID_FS, results=[1, 2, 4, 5, 6])
        back[3].set_color(RES_C)
        back.next_to(out, DOWN, buff=0.8)
        self.say(
            line(f"Multiply back to check: {R('ax + 2ay')}. Same thing.",
                 f"Multiply back to check: {BR} a x, plus two a y. {BR} Same thing."),
            anims=[LaggedStart(*[Create(a) for a in arcs], lag_ratio=0.6, run_time=1.4),
                   Succession(Wait(1.6), FadeIn(back, shift=UP * 0.2, run_time=0.9))],
        )
        self.play(FadeOut(VGroup(out, arcs, back), shift=UP * 0.4), run_time=0.7)

    # ── Takeaway ────────────────────────────────────────────────────────
    def takeaway(self):
        rows = VGroup(
            label(f"{B('Terms')} are added", fs=40),
            label(f"{E('Factors')} are multiplied", fs=40),
            label(f"A shared factor can step {R('outside')}", fs=40),
        ).arrange(DOWN, buff=0.3)
        card = self.card(rows, title="TERMS VS FACTORS")
        self.say(
            "Pulling out a shared factor is called factoring.",
            line("It's the first step of everything that comes next.",
                 f"{BR} It's the first step of everything that comes next."),
            anims=[FadeIn(card, scale=0.94, run_time=1.0)],
        )
