import sys
from pathlib import Path

_PROJECT_ROOT = Path(__file__).resolve().parents[2]
if str(_PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(_PROJECT_ROOT))

from videos.common import *


class V1ExponentialNotation(ShortScene):
    PART = "1 / 3"

    def construct(self):
        self.hook()
        power = self.build_power()
        self.name_parts(power)
        self.example()
        self.trap()
        self.takeaway()
        self.outro()

    # ── Hook: (−3)⁴ vs −3⁴ ──────────────────────────────────────────────
    def hook(self):
        a = tex("(", "-3", ")", "^{4}")
        a[3].set_color(EXP_C)
        q = tex(r"\overset{?}{=}", fs=MID_FS, color=MUTED)
        b = tex("-", "3", "^{4}")
        b[2].set_color(EXP_C)
        pair = VGroup(a, q, b).arrange(RIGHT, buff=0.5).move_to(MATH)
        self.cap(
            "These two look almost identical…",
            anims=[
                LaggedStart(
                    FadeIn(a, shift=UP * 0.4),
                    FadeIn(q, scale=0.6),
                    FadeIn(b, shift=UP * 0.4),
                    lag_ratio=0.3,
                    run_time=1.3,
                )
            ],
        )
        neq = tex(r"\neq", fs=MID_FS, color=WARN_C).move_to(q)
        self.cap(
            f"…but they are {W('not')} equal.",
            anims=[Transform(q, neq, run_time=0.8)],
        )
        self.cap(
            "First: what does an exponent mean?",
            anims=[FadeOut(pair, shift=UP * 0.5, run_time=0.8)],
        )

    # ── 5·5·5 → 5³ ──────────────────────────────────────────────────────
    def build_power(self):
        fives = [tex("5", color=BASE_C) for _ in range(3)]
        dots = [tex(r"\cdot") for _ in range(2)]
        row = VGroup(fives[0], dots[0], fives[1], dots[1], fives[2])
        row.arrange(RIGHT, buff=0.32).move_to(MATH + UP * 0.4)
        self.cap(
            f"Take {B('5')} and multiply it by itself…",
            anims=[
                LaggedStart(
                    *[FadeIn(m, shift=DOWN * 0.5) for m in row],
                    lag_ratio=0.25,
                    run_time=1.8,
                    rate_func=rate_functions.ease_out_cubic,
                )
            ],
        )
        ticks = VGroup(
            *[
                tex(str(i + 1), fs=SMALL_FS, color=EXP_C).next_to(f, UP, buff=0.3)
                for i, f in enumerate(fives)
            ]
        )
        self.cap(
            f"…{E('3')} factors of {B('5')} in total.",
            anims=[
                LaggedStart(
                    *[
                        AnimationGroup(
                            Indicate(f, color=BASE_C, scale_factor=1.15),
                            FadeIn(t, shift=DOWN * 0.25),
                        )
                        for f, t in zip(fives, ticks)
                    ],
                    lag_ratio=0.55,
                    run_time=2.4,
                )
            ],
        )
        self.hold()

        top = VGroup(row, ticks)
        power = tex("5", "^{3}", fs=HERO_FS)
        power[0].set_color(BASE_C)
        power[1].set_color(EXP_C)
        power.move_to(MATH + DOWN * 1.15)
        self.play(top.animate.shift(UP * 0.8), run_time=0.8)
        copies = [f.copy() for f in fives]
        exp_src = ticks[2].copy()
        self.cap(
            f"We write it compactly as {B('5')}{sup(E('3'))}.",
            anims=[
                *[
                    Transform(c, power[0].copy(), path_arc=-0.6, run_time=1.6)
                    for c in copies
                ],
                Transform(exp_src, power[1], path_arc=0.4, run_time=1.6),
            ],
        )
        self.remove(*copies, exp_src)
        self.add(power)
        self.hold()
        self.play(
            FadeOut(top, shift=UP * 0.4),
            power.animate.move_to(MATH + UP * 0.35),
            run_time=1.0,
        )
        return power

    # ── base / exponent labels ──────────────────────────────────────────
    def name_parts(self, power):
        base_lbl = label(B("base"), fs=44, weight=BOLD)
        base_lbl.next_to(power[0], DOWN, buff=0.8)
        base_arrow = Arrow(
            base_lbl.get_top(),
            power[0].get_bottom(),
            buff=0.15,
            color=BASE_C,
            stroke_width=5,
            max_tip_length_to_length_ratio=0.3,
        )
        self.cap(
            f"{B('Base')}: what gets multiplied. {E('Exponent')}: how many times.",
            anims=[
                GrowArrow(base_arrow, run_time=0.9),
                FadeIn(base_lbl, shift=UP * 0.2, run_time=0.9),
                Indicate(power[0], color=BASE_C, scale_factor=1.08, run_time=1.2),
            ],
        )
        exp_lbl = label(E("exponent"), fs=44, weight=BOLD)
        exp_lbl.next_to(power[1], UP, buff=0.8)
        exp_arrow = Arrow(
            exp_lbl.get_bottom(),
            power[1].get_top(),
            buff=0.15,
            color=EXP_C,
            stroke_width=5,
            max_tip_length_to_length_ratio=0.3,
        )
        self.play(
            GrowArrow(exp_arrow, run_time=0.9),
            FadeIn(exp_lbl, shift=DOWN * 0.2, run_time=0.9),
            Indicate(power[1], color=EXP_C, scale_factor=1.15, run_time=1.2),
        )
        self.hold(1.0)
        self.play(
            FadeOut(VGroup(power, base_lbl, base_arrow, exp_lbl, exp_arrow), shift=UP * 0.4),
            run_time=0.8,
        )

    # ── Example 1(a): (½)⁵ = 1/32 ───────────────────────────────────────
    def example(self):
        top = tex(r"\left(\frac{1}{2}\right)", "^{5}", fs=MID_FS)
        top[0].set_color(BASE_C)
        top[1].set_color(EXP_C)
        parts = ["="]
        for i in range(5):
            parts.append(r"\tfrac{1}{2}")
            if i < 4:
                parts.append(r"\cdot")
        mid = tex(*parts, fs=SMALL_FS)
        for i in range(1, len(parts), 2):
            mid[i].set_color(BASE_C)
        res = tex("=", r"\frac{1}{32}", fs=MID_FS)  # scaled with the stack by fit_zone
        res[1].set_color(RES_C)
        fit(mid)
        stack = fit_zone(VGroup(top, mid, res).arrange(DOWN, buff=0.45))
        self.cap(
            f"Example: five factors of {B('½')}…",
            anims=[FadeIn(top, shift=UP * 0.3, run_time=1.0)],
        )
        self.play(
            LaggedStart(
                *[FadeIn(m, shift=DOWN * 0.3) for m in mid],
                lag_ratio=0.12,
                run_time=1.8,
            )
        )
        self.cap(
            f"…multiplied together give {R('1/32')}.",
            anims=[FadeIn(res, shift=UP * 0.3, run_time=1.0)],
        )
        self.play(Circumscribe(res[1], color=RES_C, buff=0.15, run_time=1.2))
        self.hold()
        self.play(FadeOut(stack, shift=UP * 0.4), run_time=0.8)

    # ── Back to the trap ────────────────────────────────────────────────
    def trap(self):
        pa = tex("(", "-3", ")", "^{4}")
        pa[1].set_color(BASE_C)
        pa[3].set_color(EXP_C)
        pa.move_to(MATH + UP * 1.6)
        rect_a = SurroundingRectangle(
            pa[0:3], color=BASE_C, buff=0.12, corner_radius=0.12, stroke_width=4
        )
        self.cap(
            f"Back to the puzzle. Here the {B('base')} is {B('−3')}.",
            anims=[
                Succession(
                    FadeIn(pa, shift=UP * 0.3, run_time=0.9),
                    Create(rect_a, run_time=0.9),
                )
            ],
        )
        exp_a = tex("=", "(-3)", "(-3)", "(-3)", "(-3)", fs=SMALL_FS)
        for i in range(1, 5):
            exp_a[i].set_color(BASE_C)
        exp_a.move_to(MATH + UP * 0.1)
        res_a = tex("=", "81", fs=BIG_FS)
        res_a[1].set_color(RES_C)
        res_a.move_to(MATH + DOWN * 1.3)
        self.play(
            LaggedStart(*[FadeIn(m, shift=DOWN * 0.3) for m in exp_a], lag_ratio=0.2, run_time=1.6)
        )
        self.cap(
            f"Four negatives multiply to {R('+81')}.",
            anims=[FadeIn(res_a, shift=UP * 0.3, run_time=1.0)],
        )
        self.hold()

        sum_a = tex("(", "-3", ")", "^{4}", "=", "81", fs=MID_FS)
        sum_a[1].set_color(BASE_C)
        sum_a[3].set_color(EXP_C)
        sum_a[5].set_color(RES_C)
        sum_a.move_to(MATH + UP * 1.8)
        self.play(
            ReplacementTransform(pa, sum_a[0:4]),
            ReplacementTransform(res_a[0], sum_a[4]),
            ReplacementTransform(res_a[1], sum_a[5]),
            FadeOut(rect_a),
            FadeOut(exp_a),
            run_time=1.1,
        )

        pb = tex("-", "3", "^{4}")
        pb[1].set_color(BASE_C)
        pb[2].set_color(EXP_C)
        pb.move_to(MATH + UP * 0.05)
        rect_b = SurroundingRectangle(
            pb[1], color=BASE_C, buff=0.12, corner_radius=0.12, stroke_width=4
        )
        self.play(FadeIn(pb, shift=UP * 0.3), run_time=0.9)
        self.cap(
            f"Without them, the exponent only grabs the {B('3')}.",
            anims=[Create(rect_b, run_time=1.0), pb[0].animate(run_time=1.0).set_color(WARN_C)],
        )
        exp_b = tex("=", "-", "(", r"3 \cdot 3 \cdot 3 \cdot 3", ")", fs=SMALL_FS)
        exp_b[1].set_color(WARN_C)
        exp_b[3].set_color(BASE_C)
        exp_b.move_to(MATH + DOWN * 1.35)
        self.play(FadeIn(exp_b, shift=DOWN * 0.3), run_time=1.0)
        self.hold()
        res_b = tex("=", "-81", fs=BIG_FS)
        res_b[1].set_color(RES_C)
        res_b.move_to(exp_b)
        self.cap(
            f"The minus waits outside: {R('−81')}.",
            anims=[ReplacementTransform(exp_b, res_b, run_time=1.1)],
        )
        self.hold()

        sum_b = tex("-", "3", "^{4}", "=", "-81", fs=MID_FS)
        sum_b[1].set_color(BASE_C)
        sum_b[2].set_color(EXP_C)
        sum_b[4].set_color(RES_C)
        sum_b.move_to(MATH + UP * 0.4)
        self.play(
            ReplacementTransform(pb, sum_b[0:3]),
            ReplacementTransform(res_b[0], sum_b[3]),
            ReplacementTransform(res_b[1], sum_b[4]),
            FadeOut(rect_b),
            run_time=1.1,
        )
        both = VGroup(sum_a, sum_b)
        self.play(both.animate.move_to(MATH), run_time=0.7)
        self.cap(
            "Parentheses change the base — and the answer.",
            anims=[
                Circumscribe(sum_a[5], color=RES_C, buff=0.15, run_time=1.4),
                Circumscribe(sum_b[4], color=RES_C, buff=0.15, run_time=1.4),
            ],
        )
        self.hold(0.4)
        self.play(FadeOut(both, shift=UP * 0.4), run_time=0.8)

    # ── Takeaway ────────────────────────────────────────────────────────
    def takeaway(self):
        row = tex("a", "^{n}", "=", "a", r"\cdot", "a", r"\cdot", r"\cdots", r"\cdot", "a", fs=MID_FS)
        for i in (0, 3, 5, 9):
            row[i].set_color(BASE_C)
        row[1].set_color(EXP_C)
        brace = Brace(row[3:], DOWN, buff=0.2, color=EXP_C)
        n_lbl = label(f"{E('n')} factors", fs=38).next_to(brace, DOWN, buff=0.2)
        card = self.card(VGroup(row, brace, n_lbl))
        self.cap(
            f"In general, {B('a')}{sup(E('n'))} means {E('n')} factors of {B('a')}.",
            anims=[FadeIn(card, scale=0.94, run_time=1.0)],
        )
