"""Part 4, video 3: the 1–3–3–1 cube pattern (Example 4b)."""

try:
    from .sprod_common import *
except ImportError:  # Manim loading this file directly
    from sprod_common import *


def cube_formula(sign="+"):
    """A single polynomial MathTex, keeping binary-operator spacing intact."""
    return poly([["(", "a", sign, "b", ")", "^{3}"], ["="],
                 ["a", "^{3}"], [sign, "3", "a", "^{2}", "b"],
                 ["+", "3", "a", "b", "^{2}"], [sign, "b", "^{3}"]], fs=SMALL_FS)


class SP3Cubes(SpecialScene):
    PART = "3 / 3"

    def construct(self):
        given = ptex("(", "x", "^{2}", "-", "2", ")", "^{3}", fs=BIG_FS)
        given.move_to(MATH + UP * 1.35)
        repeats = VGroup(*[ptex("(", "x", "^{2}", "-", "2", ")", fs=59) for _ in range(3)])
        repeats.arrange(DOWN, buff=0.13).move_to(MATH + DOWN * 0.65)
        strike = Cross(repeats, stroke_color=WARN_C, stroke_width=5)
        self.say(
            line(f"(x{sup('2')} − 2){sup('3')}: multiply it out three times?",
                 f"X squared minus two, cubed. {BR} Do you really multiply it out three times?"),
            anims=[FadeIn(given, shift=UP * 0.2),
                   Succession(Wait(0.8), FadeIn(repeats, shift=UP * 0.2), Create(strike))],
        )
        self.play(FadeOut(VGroup(given, repeats, strike)), run_time=0.65)

        chips = VGroup(*[chip(str(i)).scale(0.77) for i in (1, 3, 3, 1)])
        chips.arrange(RIGHT, buff=0.38).move_to(MATH + UP * 0.3)
        caption = label("THE CUBE COEFFICIENTS", fs=31, color=MUTED, weight=BOLD)
        caption.next_to(chips, UP, buff=0.55)
        self.say(
            line(f"Cubes follow a pattern: {E('1, 3, 3, 1')}.",
                 f"No. Cubes follow a pattern: one, three, three, one."),
            anims=[LaggedStart(*[FadeIn(c, scale=0.8) for c in chips],
                                   lag_ratio=0.25, run_time=1.2), FadeIn(caption)],
        )
        self.play(FadeOut(VGroup(chips, caption)), run_time=0.6)

        formula = cube_formula("+")
        fit(formula).move_to(MATH + UP * 0.65)
        terms = formula.terms[2:]
        badges = VGroup()
        for number, term in zip((1, 3, 3, 1), terms):
            b = chip(str(number)).scale(0.48).next_to(term, UP, buff=0.45)
            badges.add(b)
        powers_a = label(f"{B('a')} power:  {E('3  →  2  →  1  →  0')}", fs=37)
        powers_b = label(f"{B('b')} power:  {E('0  →  1  →  2  →  3')}", fs=37)
        counters = VGroup(powers_a, powers_b).arrange(DOWN, buff=0.22).move_to(MATH + DOWN * 1.0)
        self.say(
            line(f"{B('a')}'s power goes {E('down')}; {B('b')}'s goes {E('up')}.",
                 "A's power counts down, while B's counts up."),
            anims=[FadeIn(formula.terms[:2], shift=UP * 0.2)],
            steps=[[LaggedStart(*[FadeIn(t, shift=UP * 0.15) for t in terms],
                                 lag_ratio=0.24, run_time=1.7),
                    LaggedStart(*[FadeIn(b, shift=DOWN * 0.15) for b in badges],
                                 lag_ratio=0.24, run_time=1.7)],
                   [FadeIn(counters, shift=UP * 0.15)]],
        )

        negative = cube_formula("-")
        fit(negative).move_to(formula)
        negative.terms[0][2].set_color(WARN_C)
        for group in (negative.terms[3], negative.terms[5]):
            group[0].set_color(WARN_C)
        signs = label(f"{E('plus')}  ·  {W('minus')}  ·  {E('plus')}  ·  {W('minus')}", fs=38)
        signs.move_to(counters)
        self.say(
            line(f"For a minus, the signs {W('alternate')}.",
                 "For a minus, the signs alternate: plus, minus, plus, minus."),
            anims=[FadeOut(formula), FadeIn(negative, shift=UP * 0.15),
                   FadeOut(counters), FadeIn(signs, shift=UP * 0.15)],
            steps=[[Circumscribe(negative.terms[3], color=WARN_C, run_time=0.9)]],
        )
        self.play(FadeOut(VGroup(negative, badges, signs)), run_time=0.65)

        given = ptex("(", "x", "^{2}", "-", "2", ")", "^{3}", fs=BIG_FS)
        given.move_to(MATH + UP * 1.15)
        assign = label(f"a = {B('x')}{sup(E('2'))}    ·    b = {B('2')}", fs=38, color=MUTED)
        assign.move_to(MATH + DOWN * 0.05)
        tag = label("EXAMPLE 4(b)", fs=29, color=MUTED, weight=BOLD).next_to(given, UP, buff=0.25)
        self.say(
            line(f"Here {B('a = x²')}, {B('b = 2')}.",
                 "Here A is X squared, and B is two."),
            anims=[FadeIn(given, shift=UP * 0.25), FadeIn(tag)],
            steps=[[FadeIn(assign, shift=UP * 0.15)]],
        )

        answer = poly([["x", "^{6}"], ["-", "6", "x", "^{4}"],
                       ["+", "12", "x", "^{2}"], ["-", "8"]], fs=SMALL_FS)
        answer.set_color(RES_C)
        fit(answer).move_to(MATH + DOWN * 0.65)
        self.say(
            line(f"{R('x⁶ − 6x⁴ + 12x² − 8')}.",
                 "So it's X to the sixth, minus six X to the fourth, plus twelve X squared, minus eight."),
            anims=[FadeOut(assign)],
            steps=[[LaggedStart(*[FadeIn(t, shift=UP * 0.18) for t in answer.terms],
                                 lag_ratio=0.3, run_time=2.2)],
                   [Circumscribe(answer, color=RES_C, run_time=0.9)]],
        )
        self.play(FadeOut(VGroup(given, tag, answer)), run_time=0.65)

        plus_card = cube_formula("+")
        minus_card = cube_formula("-")
        hint = label(f"{E('1  ·  3  ·  3  ·  1')}    ·    powers trade places", fs=33, color=MUTED)
        inside = VGroup(plus_card, minus_card, hint).arrange(DOWN, buff=0.32)
        card = self.card(inside, title="CUBE PATTERN")
        self.say(
            line(f"Cubes: {E('1, 3, 3, 1')}. Powers trade places.",
                 f"Cubes: one, three, three, one. {BR} Powers trade places."),
            anims=[FadeIn(card, scale=0.94, run_time=0.9)],
        )
        self.outro()
