"""Part 7, video 3: factor four-term polynomials by grouping (Example 15)."""

try:
    from .fcomp_common import *
except ImportError:  # Manim loading this file directly
    from fcomp_common import *


class FC3Grouping(CompleteScene):
    PART = "3 / 3"

    def construct(self):
        given = poly([
            ["x", "^{3}"], ["+", "x", "^{2}"], ["+", "4", "x"], ["+", "4"],
        ], fs=MID_FS)
        fit(given).move_to(MATH + UP * 0.45)
        tag = label("EXAMPLE 15(a)", fs=29, color=MUTED, weight=BOLD).next_to(given, UP, buff=0.35)
        all_terms = SurroundingRectangle(given, color=WARN_C, buff=0.17,
                                         corner_radius=0.15, stroke_width=3)
        no_gcf = chip("NO GCF FOR ALL 4", WARN_C).scale(0.76).next_to(given, DOWN, buff=0.62)
        self.say(
            line(
                f"Four terms, but no factor is shared by all four. Now what?",
                f"No common factor works across all four terms. {BR} Try pairs.",
            ),
            anims=[FadeIn(given, shift=UP * 0.2), FadeIn(tag)],
            steps=[[Create(all_terms), FadeIn(no_gcf, scale=0.86)]],
        )

        pair1 = SurroundingRectangle(VGroup(*given.terms[0:2]), color=BASE_C, buff=0.14,
                                     corner_radius=0.14, stroke_width=3)
        pair2 = SurroundingRectangle(VGroup(*given.terms[2:4]), color=EXP_C, buff=0.14,
                                     corner_radius=0.14, stroke_width=3)
        pair_labels = VGroup(
            label(B("PAIR 1"), fs=31, weight=BOLD).next_to(pair1, DOWN, buff=0.24),
            label(E("PAIR 2"), fs=31, weight=BOLD).next_to(pair2, DOWN, buff=0.24),
        )
        self.say(
            line(
                f"When four terms resist, split them into {E('two pairs')}.",
                f"When four terms have no common factor, {BR} split them into two pairs.",
            ),
            anims=[FadeOut(VGroup(all_terms, no_gcf))],
            steps=[[Create(pair1), Create(pair2), FadeIn(pair_labels)]],
        )
        self.play(FadeOut(VGroup(given, tag, pair1, pair2, pair_labels)), run_time=0.5)

        pair_work = ptex(
            "x", "^{2}", "(", "x", "+", "1", ")", "+",
            "4", "(", "x", "+", "1", ")",
            fs=SMALL_FS,
        )
        fit(pair_work).move_to(MATH + UP * 0.75)
        shared1 = SurroundingRectangle(pair_work[2:7], color=BASE_C, buff=0.10,
                                       corner_radius=0.12, stroke_width=3)
        shared2 = SurroundingRectangle(pair_work[9:14], color=BASE_C, buff=0.10,
                                       corner_radius=0.12, stroke_width=3)
        shared_tag = chip("SAME BINOMIAL", RES_C).scale(0.76).move_to(MATH + DOWN * 0.75)
        self.say(
            line(
                f"Each pair reveals the same factor: {B('(x + 1)')}.",
                f"Factor each pair. {BR} Both reveal the same binomial: X plus one.",
            ),
            anims=[FadeIn(pair_work, shift=UP * 0.16)],
            steps=[[Create(shared1), Create(shared2)], [FadeIn(shared_tag, scale=0.86)]],
        )

        result_a = ptex("(", "x", "^{2}", "+", "4", ")", "(", "x", "+", "1", ")", fs=MID_FS)
        result_a.set_color(RES_C)
        fit(result_a).move_to(MATH + DOWN * 1.65)
        self.say(
            line(
                f"Pull it out: {R('(x² + 4)(x + 1)')}.",
                f"Pull out the shared X plus one. {BR} The other pieces become X squared plus four.",
            ),
            anims=[FadeOut(shared_tag)],
            steps=[[FadeIn(result_a, shift=UP * 0.18), Circumscribe(result_a, color=RES_C, run_time=1.0)]],
        )
        self.play(FadeOut(VGroup(pair_work, shared1, shared2, result_a)), run_time=0.55)

        given_b = poly([
            ["x", "^{3}"], ["-", "2", "x", "^{2}"], ["-", "9", "x"], ["+", "18"],
        ], fs=MID_FS)
        fit(given_b).move_to(MATH + UP * 1.25)
        pair_b1 = SurroundingRectangle(VGroup(*given_b.terms[0:2]), color=BASE_C, buff=0.13,
                                       corner_radius=0.13, stroke_width=3)
        pair_b2 = SurroundingRectangle(VGroup(*given_b.terms[2:4]), color=EXP_C, buff=0.13,
                                       corner_radius=0.13, stroke_width=3)
        factored_pairs = ptex(
            "x", "^{2}", "(", "x", "-", "2", ")", "-",
            "9", "(", "x", "-", "2", ")",
            fs=SMALL_FS,
        )
        fit(factored_pairs).move_to(MATH + DOWN * 0.65)
        minus_nine = SurroundingRectangle(factored_pairs[7:9], color=WARN_C, buff=0.09,
                                          corner_radius=0.11, stroke_width=3)
        tag_b = label("EXAMPLE 15(b)", fs=29, color=MUTED, weight=BOLD).next_to(given_b, UP, buff=0.3)
        self.say(
            line(
                f"Watch the sign: −9x + 18 = {W('−9(x − 2)')}.",
                f"Watch the sign: negative nine X plus eighteen {BR} is negative nine, times X minus two.",
            ),
            anims=[FadeIn(given_b, shift=UP * 0.15), FadeIn(tag_b)],
            steps=[[Create(pair_b1), Create(pair_b2)], [FadeIn(factored_pairs, shift=UP * 0.15)],
                   [Create(minus_nine)]],
        )
        self.play(FadeOut(VGroup(given_b, pair_b1, pair_b2, minus_nine, tag_b)), run_time=0.5)

        first_result = ptex("(", "x", "^{2}", "-", "9", ")", "(", "x", "-", "2", ")", fs=MID_FS)
        first_result.move_to(MATH + UP * 0.75)
        not_done = chip("FACTOR AGAIN", EXP_C).scale(0.76).next_to(first_result, DOWN, buff=0.48)
        final = ptex(
            "(", "x", "-", "3", ")", "(", "x", "+", "3", ")", "(", "x", "-", "2", ")",
            fs=SMALL_FS,
        )
        final.set_color(RES_C)
        fit(final).move_to(MATH + DOWN * 1.45)
        self.say(
            line(
                f"Grouping gives (x{sup('2')} − 9)(x − 2), but x{sup('2')} − 9 still splits.",
                f"Pull out X minus two. {BR} You get X squared minus nine, but that difference of squares still factors.",
            ),
            anims=[FadeOut(factored_pairs), FadeIn(first_result, shift=UP * 0.15)],
            steps=[[FadeIn(not_done, scale=0.86)], [FadeIn(final, shift=UP * 0.18)]],
        )

        self.say(
            line(
                f"Fully factored: {R('(x − 3)(x + 3)(x − 2)')}.",
                f"The complete answer is X minus three, times X plus three, times X minus two.",
            ),
            anims=[FadeOut(not_done), Circumscribe(final, color=RES_C, run_time=1.0)],
        )
        self.play(FadeOut(VGroup(first_result, final)), run_time=0.5)

        rule = VGroup(
            label(f"1  Split four terms into {B('pairs')}", fs=35),
            label(f"2  Factor each pair", fs=35),
            label(f"3  Pull out the {E('shared binomial')}", fs=35),
            label(f"4  {R('Factor again')} if possible", fs=35),
        ).arrange(DOWN, buff=0.24, aligned_edge=LEFT)
        card = self.card(rule, title="FACTOR BY GROUPING")
        self.say(
            line(
                f"Group into pairs, then pull out the binomial they share.",
                f"Group four terms into pairs, then pull out the binomial both pairs share.",
            ),
            anims=[FadeIn(card, scale=0.94, run_time=0.9)],
        )
        self.outro()
