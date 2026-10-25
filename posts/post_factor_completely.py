"""Part 7 Instagram post (1080×1350): a decision flowchart for factoring.

render: manim render -s --config_file post.cfg -o <output.png> posts/post_factor_completely.py FactorAnythingPost
"""

try:
    from .post_roots import FH, FW, MARGIN, text
except ImportError:  # Manim loading this file directly
    from post_roots import FH, FW, MARGIN, text
from videos.factor_completely.fcomp_common import *


class FactorAnythingPost(Scene):
    def construct(self):
        bg = ImageMobject(str(background_path(1080, 1350)))
        bg.height = FH
        self.add(bg)

        bars = VGroup(*[
            RoundedRectangle(corner_radius=0.03, width=0.5, height=0.08,
                             fill_color=c, fill_opacity=1, stroke_width=0)
            for c in (BASE_C, EXP_C, RES_C)
        ]).arrange(RIGHT, buff=0.1)
        kicker = text("FACTOR COMPLETELY · SECTION 1.3", 17, MUTED, BOLD, spacing=1250)
        title = fit(text(f"How to {col('Factor Anything', EXP_C)}", 58, INK, BOLD), FW - 2 * MARGIN)
        subtitle = text("A quick decision flowchart", 21, MUTED)
        header = VGroup(bars, kicker, title, subtitle).arrange(DOWN, buff=0.18)
        header.move_to([0, FH / 2 - 0.38 - header.height / 2, 0])

        inner_w = FW - 2 * MARGIN
        gcf_box = RoundedRectangle(corner_radius=0.24, width=inner_w, height=0.92,
                                   fill_color=CARD_FILL, fill_opacity=0.95,
                                   stroke_color=BASE_C, stroke_width=2.5)
        gcf_box.next_to(header, DOWN, buff=0.28)
        badge1 = text("1", 24, BASE_C, BOLD)
        badge1.move_to(gcf_box.get_left() + RIGHT * 0.48)
        gcf_title = text(f"Pull out the {col('GCF', BASE_C)} first", 29, INK, BOLD)
        gcf_hint = text("numbers + smallest variable powers", 17, MUTED)
        VGroup(gcf_title, gcf_hint).arrange(DOWN, buff=0.08).move_to(gcf_box)

        count_chip = chip("2 · COUNT THE TERMS", EXP_C).scale(0.72)
        count_chip.next_to(gcf_box, DOWN, buff=0.34)
        down_arrow = Arrow(gcf_box.get_bottom(), count_chip.get_top(), buff=0.07,
                           color=MUTED, stroke_width=3, tip_length=0.13)

        gap = 0.18
        card_w = (inner_w - 2 * gap) / 3
        card_h = 3.12
        card_y = count_chip.get_bottom()[1] - 0.28 - card_h / 2

        def route_card(number, heading, color, rows):
            box = RoundedRectangle(corner_radius=0.24, width=card_w, height=card_h,
                                   fill_color=CARD_FILL, fill_opacity=0.95,
                                   stroke_color=color, stroke_width=2.3)
            number_obj = text(number, 37, color, BOLD)
            heading_obj = text("TERMS", 16, MUTED, BOLD, spacing=1200)
            head = VGroup(number_obj, heading_obj).arrange(DOWN, buff=0.02)
            head.move_to(box.get_top() + DOWN * 0.43)
            divider = Line(box.get_left() + RIGHT * 0.22, box.get_right() + LEFT * 0.22,
                           color=CARD_STROKE, stroke_width=2)
            divider.move_to([box.get_x(), box.get_top()[1] - 0.82, 0])
            items = VGroup()
            for title_text, formula_parts in rows:
                title_obj = text(title_text, 16, color, BOLD, spacing=380)
                formula = ptex(*formula_parts, fs=39)
                fit(formula, card_w - 0.32)
                items.add(VGroup(title_obj, formula).arrange(DOWN, buff=0.08))
            items.arrange(DOWN, buff=0.25).move_to([box.get_x(), box.get_center()[1] - 0.43, 0])
            return VGroup(box, head, divider, items)

        two = route_card("2", "TWO TERMS", BASE_C, (
            ("SQUARES", ("a", "^{2}", "-", "b", "^{2}")),
            ("CUBES", ("a", "^{3}", r"\pm", "b", "^{3}")),
        ))
        three = route_card("3", "THREE TERMS", EXP_C, (
            ("PERFECT SQUARE", ("a", "^{2}", r"\pm", "2", "a", "b", "+", "b", "^{2}")),
            ("TRINOMIAL", ("x", "^{2}", "+", "b", "x", "+", "c")),
        ))
        four = route_card("4", "FOUR TERMS", RES_C, (
            ("GROUP PAIRS", ("a", "x", "+", "a", "y", "+", "b", "x", "+", "b", "y")),
            ("SHARED BINOMIAL", ("a", "(", "x", "+", "y", ")", "+", "b", "(", "x", "+", "y", ")")),
        ))
        cards = VGroup(two, three, four).arrange(RIGHT, buff=gap)
        cards.move_to([0, card_y, 0])

        branches = VGroup(*[
            Line(count_chip.get_bottom(), c[0].get_top(), color=MUTED, stroke_width=2.5)
            for c in cards
        ]).set_z_index(-1)

        repeat_box = RoundedRectangle(corner_radius=0.24, width=inner_w, height=0.94,
                                      fill_color=CARD_FILL, fill_opacity=0.95,
                                      stroke_color=RES_C, stroke_width=2.5)
        repeat_box.next_to(cards, DOWN, buff=0.28)
        badge3 = text("3", 24, RES_C, BOLD).move_to(repeat_box.get_left() + RIGHT * 0.48)
        repeat_title = text(f"{col('Repeat', RES_C)} on every factor", 28, INK, BOLD)
        repeat_hint = text("stop only when nothing splits again", 17, MUTED)
        VGroup(repeat_title, repeat_hint).arrange(DOWN, buff=0.07).move_to(repeat_box)
        repeat_arrows = VGroup(*[
            Arrow(c[0].get_bottom(), repeat_box.get_top(), buff=0.07,
                  color=MUTED, stroke_width=2.2, tip_length=0.12)
            for c in cards
        ]).set_z_index(-1)

        note = text(f"A {col('sum of squares', WARN_C)} usually stays prime over the reals.", 18, MUTED)
        fit(note, inner_w - 0.8)
        note.next_to(repeat_box, DOWN, buff=0.27)
        footer = text("GCF → PATTERN → REPEAT", 17, MUTED, BOLD, spacing=1000)
        fit(footer, inner_w - 1.2)
        footer.move_to([-FW / 2 + MARGIN + footer.width / 2, -FH / 2 + 0.40, 0])

        self.add(header, gcf_box, badge1, gcf_title, gcf_hint, down_arrow, count_chip,
                 branches, cards, repeat_arrows, repeat_box, badge3, repeat_title,
                 repeat_hint, note, footer, watermark(FW, FH, width=0.85, inset=0.3))
