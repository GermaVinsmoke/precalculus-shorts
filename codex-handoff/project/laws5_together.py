from common import *

BR = '<break time="0.2s" />'


def expr(*parts, fs=SMALL_FS, results=()):
    return auto(tex(*parts, fs=fs), digits=False, results=results)


class L5PuttingItTogether(NarratedScene):
    PART = "5 / 5"

    def construct(self):
        start = expr("(", "2", "a", "^{3}", "b", "^{2}", ")", "(", "3", "a", "b", "^{4}", ")", "^{3}", fs=MID_FS)
        fit(start)
        slot = MATH + UP * 1.4
        start.move_to(MATH)
        steps = [
            ("LAW 4", expr("=", "(", "2", "a", "^{3}", "b", "^{2}", ")", "(", "3", "^{3}", "a", "^{3}",
                           "(", "b", "^{4}", ")", "^{3}", ")")),
            ("LAW 3", expr("=", "(", "2", "a", "^{3}", "b", "^{2}", ")", "(", "27", "a", "^{3}", "b", "^{12}", ")")),
            ("GROUP", expr("=", "(", "2", r"\cdot", "27", ")", "(", "a", "^{3}", "a", "^{3}", ")",
                           "(", "b", "^{2}", "b", "^{12}", ")")),
            ("LAW 1", expr("=", "54", "a", "^{6}", "b", "^{14}", fs=MID_FS, results=range(1, 6))),
        ]
        for _, m in steps:
            fit(m).move_to(MATH + DOWN * 0.15)

        # ── Hook ────────────────────────────────────────────────────────
        self.say(
            "Looks messy?",
            line("Four moves, one law at a time.", f"{BR} Four moves, {BR} one law at a time."),
            anims=[FadeIn(start, shift=UP * 0.3, run_time=1.0)],
        )
        self.play(start.animate.move_to(slot), run_time=0.8)

        tag = None
        work = None
        narration = {
            "LAW 4": [
                line(f"{E('Law 4')}: the cube goes to every factor inside.",
                     f"Law four: {BR} the cube goes to every factor inside."),
            ],
            "LAW 3": [
                line(f"{E('Law 3')}: ({B('b')}{sup(E('4'))}){sup(E('3'))} = {B('b')}{sup(E('12'))}.",
                     f"Law three: {BR} b to the fourth, cubed, is b to the twelfth."),
                line(f"And 3{sup('3')} = 27.", f"{BR} And three cubed is twenty-seven."),
            ],
            "GROUP": [
                line(f"Group the numbers, the {B('a')} terms, and the {B('b')} terms.",
                     f"Now group the numbers, {BR} the A terms, {BR} and the B terms."),
            ],
            "LAW 1": [
                line(f"{E('Law 1')}: add the exponents.", f"Law one: {BR} add the exponents."),
                line(f"{R('54')}{R('a')}{sup(R('6'))}{R('b')}{sup(R('14'))}.",
                     f"{BR} Fifty-four, A to the sixth, B to the fourteenth."),
            ],
        }
        for name, m in steps:
            new_tag = chip(name).next_to(m, DOWN, buff=0.55)
            anims = []
            if work is None:
                anims.append(TransformMatchingTex(start.copy(), m, path_arc=0, run_time=1.6))
            else:
                anims.append(TransformMatchingTex(work, m, run_time=1.6))
            anims.append(FadeIn(new_tag, shift=UP * 0.2) if tag is None else ReplacementTransform(tag, new_tag))
            self.say(*narration[name], anims=anims)
            work, tag = m, new_tag
        self.play(Circumscribe(work, color=RES_C, buff=0.15), run_time=1.2)
        self.play(FadeOut(VGroup(start, work, tag), shift=UP * 0.4), run_time=0.7)

        # ── All seven laws ──────────────────────────────────────────────
        laws = [
            r"a^m a^n = a^{m+n}",
            r"\frac{a^m}{a^n} = a^{m-n}",
            r"(a^m)^n = a^{mn}",
            r"(ab)^n = a^n b^n",
            r"\left(\frac{a}{b}\right)^n = \frac{a^n}{b^n}",
            r"\left(\frac{a}{b}\right)^{-n} = \left(\frac{b}{a}\right)^n",
            r"\frac{a^{-n}}{b^{-m}} = \frac{b^m}{a^n}",
        ]
        rows = []
        for i, s in enumerate(laws, 1):
            num = MarkupText(str(i), font=FONT, font_size=30, color=EXP_C, weight=BOLD)
            f = tex(s, fs=52)
            rows.append(VGroup(num, f).arrange(RIGHT, buff=0.25))
        left = VGroup(*rows[:4]).arrange(DOWN, buff=0.38, aligned_edge=LEFT)
        right = VGroup(*rows[4:]).arrange(DOWN, buff=0.38, aligned_edge=LEFT)
        grid = VGroup(left, right).arrange(RIGHT, buff=0.55, aligned_edge=UP)
        card = self.card(grid, title="THE 7 LAWS")
        if card.height > MATH_MAX_H + 0.5:
            card.scale_to_fit_height(MATH_MAX_H + 0.5).move_to(MATH)
        self.say(
            "Seven laws, one big idea:",
            line(f"{E('count the factors')}.", f"{BR} count the factors."),
            anims=[
                FadeIn(card[0], scale=0.96, run_time=0.8),
                Succession(
                    Wait(0.3),
                    FadeIn(card[1][0], run_time=0.4),
                    LaggedStart(*[FadeIn(r, shift=UP * 0.15) for r in rows], lag_ratio=0.25, run_time=2.2),
                ),
            ],
        )
        self.wait(1.0)
        self.outro()
