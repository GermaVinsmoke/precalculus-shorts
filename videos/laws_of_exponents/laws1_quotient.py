import sys
from pathlib import Path

_PROJECT_ROOT = Path(__file__).resolve().parents[2]
if str(_PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(_PROJECT_ROOT))

from videos.common import *


class L1QuotientRule(NarratedScene):
    PART = "1 / 5"

    def construct(self):
        q = self.hook()
        row = self.cancel(q)
        full = self.subtract(q, row)
        law2 = self.connect(full)
        self.example(law2)
        self.takeaway()
        self.outro()

    # ── Hook: 3⁵/3² = 3^(5÷2)? ──────────────────────────────────────────
    def hook(self):
        q = auto(tex("{3", "^{5}", r"\over", "3", "^{2}}", "=", "3", r"^{5 \div 2}", "?"))
        q[8].set_color(WARN_C)
        q.move_to(MATH)
        self.say(
            line(f"{B('3')}{sup(E('5'))} over {B('3')}{sup(E('2'))}…", "Three to the fifth, over three squared."),
            line("Do we divide the exponents?"),
            anims=[
                Succession(
                    FadeIn(q[0:5], shift=UP * 0.4, run_time=0.9),
                    Wait(1.0),
                    LaggedStart(*[FadeIn(m, shift=UP * 0.3) for m in q[5:]], lag_ratio=0.2, run_time=1.0),
                )
            ],
        )
        return q

    # ── Factors over factors; pairs cancel ──────────────────────────────
    def cancel(self, q):
        parts = ["{3", r"\cdot", "3", r"\cdot", "3", r"\cdot", "3", r"\cdot", "3", r"\over", "3", r"\cdot", "3}"]
        ex = auto(tex(*parts, fs=MID_FS))
        fit(ex).move_to(MATH + DOWN * 0.6)
        top = q[0:5]
        self.say(
            "Write out the factors:",
            line(f"five {B('3')}s on top, two on the bottom.", "five threes on top, <break time=\"0.2s\" /> two on the bottom."),
            anims=[
                FadeOut(q[5:], shift=RIGHT * 0.4, run_time=0.6),
                Succession(
                    top.animate(run_time=0.8).scale(0.55).move_to(MATH + UP * 1.75),
                    AnimationGroup(
                        TransformFromCopy(top[0:2], ex[0:9]),
                        TransformFromCopy(top[2], ex[9]),
                        TransformFromCopy(top[3:5], ex[10:13]),
                        run_time=1.4,
                    ),
                ),
            ],
        )

        def slash(m):
            return Line(m.get_corner(DL) + LEFT * 0.06 + DOWN * 0.04, m.get_corner(UR) + RIGHT * 0.06 + UP * 0.04,
                        color=WARN_C, stroke_width=6)

        pairs = [(10, 0), (12, 2)]
        pair_anims = []
        slashes = []
        for b, t in pairs:
            sb, st = slash(ex[b]), slash(ex[t])
            slashes += [sb, st]
            link = ArcBetweenPoints(ex[b].get_top() + UP * 0.05, ex[t].get_bottom() + DOWN * 0.05, angle=-PI / 3,
                                    color=WARN_C, stroke_width=3)
            pair_anims.append(
                Succession(
                    AnimationGroup(Indicate(ex[b], color=WARN_C), Indicate(ex[t], color=WARN_C), Create(link)),
                    AnimationGroup(Create(sb), Create(st), FadeOut(link)),
                    AnimationGroup(ex[b].animate.set_opacity(0.25), ex[t].animate.set_opacity(0.25)),
                    run_time=1.8,
                )
            )
        self.say(
            line(f"Each {B('3')} on the bottom cancels one on top,", "Each three on the bottom cancels one on top,"),
            line(f"because {B('3')} over {B('3')} is {R('1')}.", "<break time=\"0.2s\" /> because three over three is one."),
            anims=[Succession(*pair_anims)],
        )
        row = auto(tex("3", r"\cdot", "3", r"\cdot", "3", "=", "3", "^{3}", fs=MID_FS), results=[6, 7])
        row.move_to(MATH + DOWN * 0.6)
        self.say(
            line(f"Three factors are left: {R('3')}{sup(R('3'))}.", "Three factors are left. <break time=\"0.2s\" /> That's three cubed."),
            anims=[
                Succession(
                    AnimationGroup(
                        FadeOut(VGroup(ex[0:4], ex[9:13], *slashes)),
                        *[ReplacementTransform(ex[i], row[i - 4]) for i in range(4, 9)],
                        run_time=1.1,
                    ),
                    FadeIn(row[5:], shift=LEFT * 0.3, run_time=0.9),
                )
            ],
        )
        return row

    # ── 3⁵/3² = 3^(5−2) = 3³ ────────────────────────────────────────────
    def subtract(self, q, row):
        full = auto(tex("{3", "^{5}", r"\over", "3", "^{2}}", "=", "3", "^{5-2}", "=", "3", "^{3}"), results=[9, 10])
        fit(full).move_to(MATH)
        self.say(
            line(f"{E('5')} minus {E('2')} is {E('3')}.", "Five minus two is three."),
            line(f"To divide, {E('subtract')} the exponents.", "<break time=\"0.2s\" /> To divide, subtract the exponents."),
            anims=[
                ReplacementTransform(q[0:5], full[0:5]),
                ReplacementTransform(row[0:5], full[9]),
                ReplacementTransform(row[5], full[8]),
                ReplacementTransform(row[6:8], full[9:11]),
                FadeIn(full[5:8], shift=DOWN * 0.2),
                Succession(Wait(1.4), Circumscribe(full[7], color=EXP_C, buff=0.1, run_time=1.3)),
            ],
        )
        return full

    # ── Law 1 vs Law 2 ──────────────────────────────────────────────────
    def connect(self, full):
        law1 = auto(tex("a", "^{m}", r"\cdot", "a", "^{n}", "=", "a", "^{m+n}"))
        law2 = auto(tex("{a", "^{m}", r"\over", "a", "^{n}}", "=", "a", "^{m-n}"))
        rows = VGroup(law1, law2).arrange(DOWN, buff=0.7)
        for r in rows:
            fit(r, SAFE_W - 1.2)
        rows.move_to(MATH)
        law1.set_opacity(0.55)
        self.say(
            "Multiplying adds the exponents.",
            line("Dividing undoes multiplying, so it subtracts.",
                 "<break time=\"0.2s\" /> Dividing undoes multiplying, <break time=\"0.2s\" /> so it subtracts them."),
            anims=[
                Succession(
                    AnimationGroup(
                        *[ReplacementTransform(full[i], law2[i]) for i in range(8)],
                        FadeOut(full[8:], shift=RIGHT * 0.3),
                        FadeIn(law1, shift=DOWN * 0.3),
                        run_time=1.3,
                    ),
                    Wait(0.6),
                    AnimationGroup(
                        Circumscribe(law1[7], color=EXP_C, buff=0.08),
                        law1.animate.set_opacity(1),
                        run_time=1.2,
                    ),
                    AnimationGroup(
                        Circumscribe(law2[7], color=EXP_C, buff=0.08),
                        law1.animate.set_opacity(0.55),
                        run_time=1.2,
                    ),
                )
            ],
        )
        self.play(FadeOut(rows, shift=UP * 0.4), run_time=0.7)

    # ── Example 3(c): c⁹/c⁵ = c⁴ ────────────────────────────────────────
    def example(self, _law2):
        qx = auto(tex("{c", "^{9}", r"\over", "c", "^{5}}"))
        step = auto(tex("=", "c", "^{9-5}", fs=MID_FS))
        ans = auto(tex("=", "c", "^{4}"), results=[1, 2])
        stack = fit_zone(VGroup(qx, step, ans).arrange(DOWN, buff=0.4))
        slot = qx.get_center()
        qx.move_to(MATH)
        self.say(
            line(f"Try it: {B('c')}{sup(E('9'))} over {B('c')}{sup(E('5'))}.",
                 "Try it: <break time=\"0.2s\" /> c to the ninth, over c to the fifth."),
            anims=[FadeIn(qx, shift=UP * 0.3, run_time=1.0)],
            gap=1.2,  # thinking pause
        )
        self.say(
            line(f"Nine minus five: {R('c')}{sup(R('4'))}.", "Nine minus five is four: <break time=\"0.2s\" /> c to the fourth."),
            anims=[
                Succession(
                    qx.animate(run_time=0.7).move_to(slot),
                    AnimationGroup(
                        FadeIn(step[0]),
                        TransformFromCopy(qx[0], step[1]),
                        TransformFromCopy(VGroup(qx[1], qx[4]), step[2]),
                        run_time=1.1,
                    ),
                    FadeIn(ans, shift=UP * 0.3, run_time=0.9),
                )
            ],
        )
        self.play(FadeOut(stack, shift=UP * 0.4), run_time=0.7)

    # ── Takeaway ────────────────────────────────────────────────────────
    def takeaway(self):
        law2 = auto(tex("{a", "^{m}", r"\over", "a", "^{n}}", "=", "a", "^{m-n}"))
        card = self.card(law2, title="LAW 2")
        self.say(
            "Dividing powers with the same base?",
            line(f"{E('Subtract')} the exponents.", "<break time=\"0.2s\" /> Subtract the exponents."),
            anims=[FadeIn(card, scale=0.94, run_time=1.0)],
        )
