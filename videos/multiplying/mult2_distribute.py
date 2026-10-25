"""Part 3, video 2: distribute a binomial over a trinomial (Example 3)."""

try:
    from .mult_common import *
except ImportError:  # Manim loading this file directly
    from mult_common import *
from videos.add_subtract.add_common import BIN_X, bin_heads

BR = '<break time="0.2s" />'


class M2Distribute(MultScene):
    PART = "2 / 2"

    def construct(self):
        factors = poly([["("], ["2", "x"], ["+", "3"], [")"],
                        ["("], ["x", "^{2}"], ["-", "5", "x"], ["+", "4"], [")"]], fs=SMALL_FS)
        fit(factors).move_to(MATH + UP * 1.5)
        foil = chip("FOIL?", WARN_C).scale(0.7).move_to(MATH + DOWN * 0.45)
        example_tag = label("EXAMPLE 3", fs=27, color=MUTED, weight=BOLD)
        example_tag.move_to([CX, 4.55, 0])
        self.say(
            line(f"{W('FOIL')} needs two terms each. Now what?",
                 f"Two x plus three, times x squared minus five x plus four. {BR} "
                 "FOIL needs two terms each. Now what?"),
            anims=[FadeIn(example_tag), FadeIn(factors, shift=UP * 0.3, run_time=0.9),
                   Succession(Wait(0.8), FadeIn(foil, scale=0.8, run_time=0.6))],
        )
        self.play(FadeOut(foil), FadeOut(example_tag), factors.animate.move_to(MATH + UP * 1.95), run_time=0.7)

        row1 = poly([["2", "x", "^{3}"], ["-", "10", "x", "^{2}"], ["+", "8", "x"]], fs=SMALL_FS)
        row2 = poly([["3", "x", "^{2}"], ["-", "15", "x"], ["+", "12"]], fs=SMALL_FS)
        row1.move_to(MATH + DOWN * 0.35)
        row2.move_to(MATH + DOWN * 1.3)
        right = [factors.terms[i] for i in (5, 6, 7)]

        def distribute(source, output):
            actions = []
            for dst, term in zip(output.terms, right):
                arc = ArcBetweenPoints(source.get_bottom(), term.get_top(), angle=-0.5,
                                       color=EXP_C, stroke_width=3)
                actions.append([Create(arc, run_time=0.45),
                                Indicate(term, color=EXP_C, run_time=0.6)])
                actions.append([FadeOut(arc, run_time=0.2),
                                FadeIn(dst, shift=DOWN * 0.16, run_time=0.6)])
            return actions

        self.say(
            line(f"Same rule: {E('every term times every term')}.",
                 f"Same rule: every term times every term. {BR} Two x times each term: "
                 "two x cubed, minus ten x squared, plus eight x."),
            steps=distribute(factors.terms[1], row1),
        )
        self.say(
            line(f"Then {B('3')} times each term.",
                 f"Then three times each term: {BR} three x squared, minus fifteen x, plus twelve."),
            steps=distribute(factors.terms[2], row2),
        )

        heads = bin_heads(MATH_Y + 0.9)
        # Each row is a complete polynomial; the column copies are separate MathTex
        # objects so signs stay attached while the original rows move into the table.
        contents = [
            [ptex("2", "x", "^{3}", fs=57), None],
            [ptex("-", "10", "x", "^{2}", fs=57), ptex("+", "3", "x", "^{2}", fs=57)],
            [ptex("+", "8", "x", fs=57), ptex("-", "15", "x", fs=57)],
            [None, ptex("+", "12", fs=57)],
        ]
        table = VGroup()
        source_groups = [[row1.terms[0]], [row1.terms[1], row2.terms[0]],
                         [row1.terms[2], row2.terms[1]], [row2.terms[2]]]
        for x, col in zip(BIN_X, contents):
            for j, term in enumerate(col):
                if term is not None:
                    term.move_to([x, MATH_Y + 0.1 - j * 0.77, 0])
                    table.add(term)
        sums = [ptex("2", "x", "^{3}", fs=60), ptex("-", "7", "x", "^{2}", fs=60),
                ptex("-", "7", "x", fs=60), ptex("+", "12", fs=60)]
        for x, term in zip(BIN_X, sums):
            term.set_color(RES_C).move_to([x, MATH_Y - 1.52, 0])
        sums = VGroup(*sums)
        plus_line = Line([BIN_X[0] - 0.7, MATH_Y - 1.13, 0],
                         [BIN_X[-1] + 0.7, MATH_Y - 1.13, 0], color=MUTED, stroke_width=2)
        final = poly([["2", "x", "^{3}"], ["-", "7", "x", "^{2}"],
                      ["-", "7", "x"], ["+", "12"]], fs=MID_FS)
        final.set_color(RES_C)
        fit(final).move_to(MATH)
        self.say(
            line(f"Line them up by {E('power')}, like long multiplication.",
                 "Line them up by power, like long multiplication."),
            anims=[FadeOut(factors), FadeIn(heads, shift=DOWN * 0.15)],
            steps=[[LaggedStart(*[TransformFromCopy(src, dst, path_arc=-0.35)
                                  for srcs, col in zip(source_groups, contents)
                                  for src, dst in zip(srcs, [t for t in col if t is not None])],
                                 lag_ratio=0.15, run_time=2.0),
                    FadeOut(row1), FadeOut(row2)]],
        )
        self.say(
            line(f"Add each column: {R('2x³ − 7x² − 7x + 12')}.",
                 f"Add each column: {BR} two x cubed, minus seven x squared, minus seven x, plus twelve."),
            anims=[Create(plus_line), LaggedStart(*[FadeIn(s, shift=UP * 0.15) for s in sums],
                                                   lag_ratio=0.18, run_time=1.2)],
            steps=[[FadeOut(VGroup(heads, table, sums, plus_line)), FadeIn(final, shift=UP * 0.2)]],
        )

        tiles = VGroup()
        for text in ("2x³", "−10x²", "+8x", "+3x²", "−15x", "+12"):
            box = RoundedRectangle(corner_radius=0.13, width=1.85, height=0.68,
                                   stroke_color=BASE_C, stroke_width=2,
                                   fill_color=CARD_FILL, fill_opacity=0.92)
            txt = label(text, fs=32).move_to(box)
            tiles.add(VGroup(box, txt))
        tiles.arrange_in_grid(rows=2, cols=3, buff=(0.25, 0.3)).move_to(MATH + UP * 0.55)
        count = chip("2 × 3 = 6 PRODUCTS").scale(0.83).next_to(tiles, DOWN, buff=0.35)
        self.say(
            line(f"{E('2 terms × 3 terms')} = {R('6 products')}.",
                 f"Two terms times three terms: six products before combining. {BR} Count them to check."),
            anims=[FadeOut(final), LaggedStart(*[FadeIn(t, scale=0.85) for t in tiles],
                                                   lag_ratio=0.16, run_time=1.4)],
            steps=[[FadeIn(count, shift=UP * 0.18)]],
        )
        self.play(FadeOut(VGroup(tiles, count)), run_time=0.65)

        rule = label(f"{E('2 terms')} × {E('3 terms')} = {R('6 products')}", fs=46, weight=BOLD)
        hint = label("Then combine like terms.", fs=35, color=MUTED)
        card = self.card(VGroup(rule, hint).arrange(DOWN, buff=0.42), title="MULTIPLY EVERY PAIR")
        self.say(
            line("Every term × every term, then combine.",
                 f"Multiply every pair, {BR} then combine like terms."),
            anims=[FadeIn(card, scale=0.94, run_time=0.9)],
        )
        self.outro()
