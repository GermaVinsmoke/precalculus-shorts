import sys
from pathlib import Path

_PROJECT_ROOT = Path(__file__).resolve().parents[2]
if str(_PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(_PROJECT_ROOT))

from videos.common import *

BR = '<break time="0.2s" />'


class L3ProductQuotient(NarratedScene):
    PART = "3 / 5"

    def construct(self):
        self.hook()
        self.product()
        self.quotient()
        self.examples()
        self.warning()
        self.takeaway()
        self.outro()

    # ── Hook: (3x)³ = 3x³? ──────────────────────────────────────────────
    def hook(self):
        h = auto(tex("(", "3", "x", ")", "^{3}", "=", "3", "x", "^{3}", "?"))
        h[9].set_color(WARN_C)
        h.move_to(MATH)
        self.say(
            line(f"Is ({B('3x')}){sup(E('3'))} the same as {B('3x')}{sup(E('3'))}?",
                 f"Is three x, all cubed, {BR} the same as three x cubed?"),
            line("Let's start simpler.", f"{BR} Let's start simpler."),
            anims=[
                Succession(
                    FadeIn(h[0:5], shift=UP * 0.4, run_time=0.9),
                    Wait(0.7),
                    LaggedStart(*[FadeIn(m, shift=UP * 0.3) for m in h[5:]], lag_ratio=0.2, run_time=1.0),
                )
            ],
        )
        self.play(FadeOut(h, shift=UP * 0.4), run_time=0.7)

    # ── Law 4: (3·4)² = (3·4)(3·4) = (3·3)(4·4) = 3²·4² ─────────────────
    def product(self):
        p = auto(tex("(", "3", r"\cdot", "4", ")", "^{2}"))
        p.move_to(MATH + UP * 1.6)
        a = auto(tex("=", "(", "3", r"\cdot", "4", ")", "(", "3", r"\cdot", "4", ")", fs=MID_FS))
        b = auto(tex("=", "(", "3", r"\cdot", "3", ")", "(", "4", r"\cdot", "4", ")", fs=MID_FS))
        c = auto(tex("=", "3", "^{2}", r"\cdot", "4", "^{2}", fs=MID_FS), results=[1, 2, 4, 5])
        for m in (a, b, c):
            fit(m).move_to(MATH + DOWN * 0.3)
        self.say(
            line(f"({B('3')} · {B('4')}){sup(E('2'))} means two copies of {B('3')} · {B('4')}.",
                 f"Three times four, squared, {BR} means two copies of three times four."),
            anims=[
                Succession(
                    FadeIn(p, shift=UP * 0.3, run_time=0.9),
                    AnimationGroup(
                        FadeIn(a[0]),
                        TransformFromCopy(p[0:5], a[1:6]),
                        TransformFromCopy(p[0:5], a[6:11]),
                        run_time=1.3,
                    ),
                )
            ],
        )
        # the signature move: factors swap places
        mapping = {0: 0, 1: 1, 2: 2, 3: 3, 4: 7, 5: 5, 6: 6, 7: 4, 8: 8, 9: 9, 10: 10}
        self.say(
            line("Rearrange: threes together, fours together.",
                 f"Rearrange: {BR} threes together, {BR} fours together."),
            anims=[
                Succession(
                    Wait(0.6),
                    AnimationGroup(
                        *[
                            ReplacementTransform(a[i], b[j], path_arc=(-PI * 0.7 if i == 4 else PI * 0.7)
                                                 if i in (4, 7) else 0)
                            for i, j in mapping.items()
                        ],
                        run_time=1.6,
                    ),
                )
            ],
        )
        self.say(
            line(f"So the power goes to each factor: {B('3')}{sup(E('2'))} · {B('4')}{sup(E('2'))}.",
                 f"So the square goes to each factor: {BR} three squared, times four squared."),
            anims=[
                ReplacementTransform(b[0], c[0]),
                ReplacementTransform(b[1:6], c[1:3]),
                ReplacementTransform(b[6:11], c[3:6]),
            ],
            run_time=1.3,
        )
        self.play(FadeOut(VGroup(p, c), shift=UP * 0.4), run_time=0.7)

    # ── Law 5: (3/4)² = 3/4 · 3/4 = (3·3)/(4·4) = 3²/4² ─────────────────
    def quotient(self):
        p = auto(tex(r"\left(", "{3", r"\over", "4}", r"\right)", "^{2}", fs=MID_FS))
        p.move_to(MATH + UP * 1.5)
        a = auto(tex("=", "{3", r"\over", "4}", r"\cdot", "{3", r"\over", "4}", fs=MID_FS))
        b = auto(tex("=", "{3", r"\cdot", "3", r"\over", "4", r"\cdot", "4}", fs=MID_FS))
        c = auto(tex("=", "{3", "^{2}", r"\over", "4", "^{2}}", fs=MID_FS), results=[1, 2, 4, 5])
        for m in (a, b, c):
            m.move_to(MATH + DOWN * 0.7)

        def merge(src, dst):
            """Fly `src` into `dst` and disappear (dst is already drawn by another transform)."""
            return src.animate.move_to(dst).set_opacity(0)

        self.say(
            "Fractions work the same way:",
            line("the power goes to the top and the bottom.", f"{BR} the power goes to the top, and to the bottom."),
            anims=[FadeIn(p, shift=UP * 0.3, run_time=0.8)],
            steps=[
                [FadeIn(a[0]), FadeIn(a[4]), TransformFromCopy(p[1:4], a[1:4]), TransformFromCopy(p[1:4], a[5:8])],
                [
                    ReplacementTransform(a[0], b[0]),
                    ReplacementTransform(a[1], b[1]),
                    ReplacementTransform(a[4], b[2]),
                    ReplacementTransform(a[5], b[3], path_arc=PI * 0.5),
                    ReplacementTransform(a[2], b[4]),
                    merge(a[6], b[4]),
                    ReplacementTransform(a[3], b[5], path_arc=-PI * 0.5),
                    FadeIn(b[6]),
                    ReplacementTransform(a[7], b[7]),
                ],
                lambda: self.remove(a[6]),
                [
                    ReplacementTransform(b[0], c[0]),
                    ReplacementTransform(b[1], c[1]),
                    merge(b[2], c[1]),
                    merge(b[3], c[1]),
                    ReplacementTransform(b[4], c[3]),
                    ReplacementTransform(b[5], c[4]),
                    merge(b[6], c[4]),
                    merge(b[7], c[4]),
                    FadeIn(c[2], shift=DOWN * 0.15),
                    FadeIn(c[5], shift=DOWN * 0.15),
                ],
                lambda: self.remove(b[2], b[3], b[6], b[7]),
            ],
        )
        self.play(FadeOut(VGroup(p, c), shift=UP * 0.4), run_time=0.7)

    # ── Back to the hook + Example 3(f) ─────────────────────────────────
    def examples(self):
        e1 = auto(tex("(", "3", "x", ")", "^{3}", "=", "3", "^{3}", "x", "^{3}", "=", "27", "x", "^{3}"),
                  results=[11, 12, 13])
        e2 = auto(tex(r"\left(", "{x", r"\over", "2}", r"\right)", "^{5}", "=", "{x", "^{5}", r"\over", "2",
                      "^{5}}", "=", "{x", "^{5}", r"\over", "32}"), results=[13, 14, 16])
        e2[15].set_color(RES_C)
        rows = VGroup(fit(e1), fit(e2)).arrange(DOWN, buff=0.75)
        fit_zone(rows)
        self.say(
            line(f"So ({B('3x')}){sup(E('3'))} is {R('27x')}{sup(R('3'))}, not {B('3x')}{sup(E('3'))}.",
                 f"So three x, all cubed, {BR} is twenty-seven x cubed."),
            anims=[LaggedStart(*[FadeIn(m, shift=UP * 0.2) for m in e1], lag_ratio=0.08, run_time=2.0)],
        )
        self.say(
            line(f"And ({B('x')}/{B('2')}){sup(E('5'))} is {R('x')}{sup(R('5'))} over {R('32')}.",
                 f"And x over two, to the fifth, {BR} is x to the fifth, over thirty-two."),
            anims=[LaggedStart(*[FadeIn(m, shift=UP * 0.2) for m in e2], lag_ratio=0.06, run_time=2.0)],
        )
        self.play(FadeOut(rows, shift=UP * 0.4), run_time=0.7)

    # ── Never for sums ──────────────────────────────────────────────────
    def warning(self):
        wrong = auto(tex("(", "a", "+", "b", ")", "^{2}", r"\neq", "a", "^{2}", "+", "b", "^{2}"))
        wrong[6].set_color(WARN_C)
        n1 = tex("(1+2)^2 = 9", fs=SMALL_FS)
        n2 = tex("1^2 + 2^2 = 5", fs=SMALL_FS)
        nums = VGroup(n1, n2).arrange(DOWN, buff=0.35, aligned_edge=LEFT)
        rows = fit_zone(VGroup(fit(wrong), nums).arrange(DOWN, buff=0.8))
        self.say(
            line(f"Careful: this {W('never')} works for sums.", f"Careful: {BR} this never works for sums."),
            line("(1 + 2)² is 9, not 5.", f"One plus two, squared, is nine, {BR} not five."),
            anims=[
                Succession(
                    FadeIn(wrong, shift=UP * 0.3, run_time=1.0),
                    Wait(1.0),
                    FadeIn(n1, shift=UP * 0.2, run_time=0.7),
                    Wait(0.6),
                    FadeIn(n2, shift=UP * 0.2, run_time=0.7),
                )
            ],
        )
        self.play(FadeOut(rows, shift=UP * 0.4), run_time=0.7)

    # ── Takeaway ────────────────────────────────────────────────────────
    def takeaway(self):
        law4 = auto(tex("(", "a", "b", ")", "^{n}", "=", "a", "^{n}", "b", "^{n}"))
        law5 = auto(tex(r"\left(", "{a", r"\over", "b}", r"\right)", "^{n}", "=", "{a", "^{n}", r"\over", "b",
                        "^{n}}"))
        rows = VGroup(law4, law5).arrange(DOWN, buff=0.5)
        law5.shift(RIGHT * (law4[5].get_x() - law5[6].get_x()))
        card = self.card(rows, title="LAWS 4 &amp; 5")
        self.say(
            "A product or quotient to a power?",
            line("Give the power to every factor.", f"{BR} Give the power to every factor."),
            anims=[FadeIn(card, scale=0.94, run_time=1.0)],
        )
