"""Part 7, video 1: keep factoring until every factor is prime (Example 13)."""

try:
    from .fcomp_common import *
except ImportError:  # Manim loading this file directly
    from fcomp_common import *


class FC1FactorTree(CompleteScene):
    PART = "1 / 3"

    def construct(self):
        given = poly([["2", "x", "^{4}"], ["-", "8", "x", "^{2}"]], fs=BIG_FS)
        first_step = ptex("2", "x", "^{2}", "(", "x", "^{2}", "-", "4", ")", fs=MID_FS)
        work = VGroup(given, first_step).arrange(DOWN, buff=0.72).move_to(MATH)
        tag = label("EXAMPLE 13(a)", fs=29, color=MUTED, weight=BOLD).next_to(given, UP, buff=0.3)
        done = chip("DONE?", WARN_C).scale(0.82).next_to(first_step, DOWN, buff=0.5)
        self.say(
            line(
                f"2x{sup('4')} − 8x{sup('2')} = 2x{sup('2')}(x{sup('2')} − 4). {W('Done? Not yet.')}",
                f"Factor out two X squared. {BR} X squared minus four remains. Done? Not yet.",
            ),
            anims=[FadeIn(given, shift=UP * 0.2), FadeIn(tag)],
            steps=[[FadeIn(first_step, shift=UP * 0.18)], [FadeIn(done, scale=0.85)]],
        )
        self.play(FadeOut(VGroup(work, tag, done)), run_time=0.55)

        common = chip("1 · COMMON FACTOR", BASE_C).scale(0.82)
        special = chip("2 · SPECIAL FORM", EXP_C).scale(0.82)
        repeat = chip("3 · REPEAT", RES_C).scale(0.82)
        strategy = VGroup(common, special, repeat).arrange(DOWN, buff=0.3).move_to(MATH)
        arrows = VGroup(
            Arrow(common.get_bottom(), special.get_top(), buff=0.12, color=MUTED, stroke_width=3),
            Arrow(special.get_bottom(), repeat.get_top(), buff=0.12, color=MUTED, stroke_width=3),
        )
        self.say(
            line(
                f"Strategy: {B('common factor')}, {E('special forms')}, then {R('repeat')}.",
                f"The strategy is common factor first, then special forms, then repeat.",
            ),
            anims=[LaggedStart(*[FadeIn(c, shift=UP * 0.16) for c in strategy], lag_ratio=0.25, run_time=1.15)],
            steps=[[LaggedStart(*[GrowArrow(a) for a in arrows], lag_ratio=0.3, run_time=0.8)]],
        )
        self.play(FadeOut(VGroup(strategy, arrows)), run_time=0.5)

        root = factor_node(("2", "x", "^{4}", "-", "8", "x", "^{2}"), fs=47).move_to([CX, 3.55, 0])
        gcf = factor_node(("2", "x", "^{2}"), fs=47).move_to([-2.0, 2.1, 0])
        diff = factor_node(("x", "^{2}", "-", "4"), fs=47, color=EXP_C).move_to([1.25, 2.1, 0])
        minus = factor_node(("x", "-", "2"), fs=47).move_to([0.35, 0.55, 0])
        plus = factor_node(("x", "+", "2"), fs=47).move_to([2.25, 0.55, 0])
        e1, e2 = tree_edge(root, gcf), tree_edge(root, diff)
        e3, e4 = tree_edge(diff, minus), tree_edge(diff, plus)
        final_a = ptex("2", "x", "^{2}", "(", "x", "-", "2", ")", "(", "x", "+", "2", ")", fs=SMALL_FS)
        final_a.set_color(RES_C)
        fit(final_a).move_to(MATH + DOWN * 2.0)
        self.say(
            line(
                f"x{sup('2')} − 4 is a {E('difference of squares')}: (x − 2)(x + 2).",
                f"X squared minus four is a difference of squares: {BR} X minus two, times X plus two.",
            ),
            anims=[FadeIn(root, shift=UP * 0.12)],
            steps=[
                [Create(e1), Create(e2), FadeIn(gcf), FadeIn(diff)],
                [Create(e3), Create(e4), FadeIn(minus), FadeIn(plus)],
                lambda: prime_leaf(gcf) + prime_leaf(minus) + prime_leaf(plus),
                [FadeIn(final_a, shift=UP * 0.15)],
            ],
        )
        tree_a = VGroup(root, gcf, diff, minus, plus, e1, e2, e3, e4, final_a)
        self.play(FadeOut(tree_a), run_time=0.55)

        root_b = factor_node(("x", "^{5}", "y", "^{2}", "-", "x", "y", "^{6}"), fs=42).move_to([CX, 3.7, 0])
        gcf_b = factor_node(("x", "y", "^{2}"), fs=43).move_to([-2.0, 2.48, 0])
        fourths = factor_node(("x", "^{4}", "-", "y", "^{4}"), fs=43, color=EXP_C).move_to([1.18, 2.48, 0])
        b1, b2 = tree_edge(root_b, gcf_b), tree_edge(root_b, fourths)
        tag_b = label("EXAMPLE 13(b)", fs=29, color=MUTED, weight=BOLD).next_to(root_b, UP, buff=0.2)
        self.say(
            line(
                f"Harder: x{sup('5')}y{sup('2')} − xy{sup('6')} = xy{sup('2')}(x{sup('4')} − y{sup('4')}).",
                f"Pull out X Y squared, {BR} leaving X to the fourth minus Y to the fourth.",
            ),
            anims=[FadeIn(root_b, shift=UP * 0.12), FadeIn(tag_b)],
            steps=[[Create(b1), Create(b2), FadeIn(gcf_b), FadeIn(fourths)]],
        )

        diff2 = factor_node(("x", "^{2}", "-", "y", "^{2}"), fs=40, color=EXP_C).move_to([0.05, 1.16, 0])
        sum2 = factor_node(("x", "^{2}", "+", "y", "^{2}"), fs=40).move_to([2.5, 1.16, 0])
        minus_xy = factor_node(("x", "-", "y"), fs=42).move_to([-0.62, -0.12, 0])
        plus_xy = factor_node(("x", "+", "y"), fs=42).move_to([0.82, -0.12, 0])
        b3, b4 = tree_edge(fourths, diff2), tree_edge(fourths, sum2)
        b5, b6 = tree_edge(diff2, minus_xy), tree_edge(diff2, plus_xy)
        self.say(
            line(
                f"x{sup('4')} − y{sup('4')} splits twice; x{sup('2')} + y{sup('2')} stays prime.",
                f"The fourth powers split as two squares. {BR} The difference splits again; the sum of squares stays prime.",
            ),
            anims=[Circumscribe(fourths, color=EXP_C, run_time=0.9)],
            steps=[
                [Create(b3), Create(b4), FadeIn(diff2), FadeIn(sum2)],
                [Create(b5), Create(b6), FadeIn(minus_xy), FadeIn(plus_xy)],
                lambda: prime_leaf(gcf_b) + prime_leaf(sum2) + prime_leaf(minus_xy) + prime_leaf(plus_xy),
            ],
        )

        tree_b = VGroup(root_b, gcf_b, fourths, diff2, sum2, minus_xy, plus_xy,
                        b1, b2, b3, b4, b5, b6, tag_b)
        final_b = ptex(
            "x", "y", "^{2}", "(", "x", "^{2}", "+", "y", "^{2}", ")",
            "(", "x", "+", "y", ")", "(", "x", "-", "y", ")",
            fs=SMALL_FS,
        )
        final_b.set_color(RES_C)
        fit(final_b).move_to(MATH)
        tag_final = label("EXAMPLE 13(b) · FULLY FACTORED", fs=29, color=MUTED, weight=BOLD)
        tag_final.next_to(final_b, UP, buff=0.42)
        self.say(
            line(
                f"Collect the leaves: {R('xy²(x² + y²)(x + y)(x − y)')}.",
                f"Collect the leaves: X Y squared, X squared plus Y squared, {BR} X plus Y, and X minus Y.",
            ),
            anims=[FadeOut(tree_b), FadeIn(final_b, shift=UP * 0.18), FadeIn(tag_final)],
            steps=[[Circumscribe(final_b, color=RES_C, run_time=1.0)]],
        )
        self.play(FadeOut(VGroup(final_b, tag_final)), run_time=0.5)

        checklist = VGroup(
            label(f"1  Pull out the {B('GCF')}", fs=34),
            label(f"2  Use a {E('special pattern')}", fs=34),
            label(f"3  {R('Repeat')} until every factor is prime", fs=34),
        ).arrange(DOWN, buff=0.26, aligned_edge=LEFT)
        card = self.card(checklist, title="FACTOR COMPLETELY")
        self.say(
            line(
                f"Common factor first. {R('Repeat')} until every piece is prime.",
                f"Common factor first, then repeat until every factor is prime.",
            ),
            anims=[FadeIn(card, scale=0.94, run_time=0.9)],
        )
        self.outro()
