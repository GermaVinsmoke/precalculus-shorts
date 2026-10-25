"""Part 6 Instagram formula sheet (1080×1350).

render: manim render -s --config_file post.cfg -o <output.png> posts/post_special_factoring.py SpecialFactoringPost
"""

try:
    from .post_roots import FH, FW, MARGIN, text
except ImportError:  # Manim loading this file directly
    from post_roots import FH, FW, MARGIN, text
from videos.special_factoring.sfact_common import *


class SpecialFactoringPost(Scene):
    def construct(self):
        bg = ImageMobject(str(background_path(1080, 1350)))
        bg.height = FH
        self.add(bg)

        bars = VGroup(*[
            RoundedRectangle(corner_radius=0.03, width=0.5, height=0.08,
                             fill_color=c, fill_opacity=1, stroke_width=0)
            for c in (BASE_C, EXP_C, RES_C)
        ]).arrange(RIGHT, buff=0.1)
        kicker = text("SPECIAL FACTORING · SECTION 1.3", 17, MUTED, BOLD, spacing=1700)
        title = fit(text(f"{col('5 Formulas', EXP_C)} to Spot", 61, INK, BOLD), FW-2*MARGIN-0.12)
        subtitle = text("Reverse the patterns. Factor, then check.", 21, MUTED)
        header = VGroup(bars, kicker, title, subtitle).arrange(DOWN, buff=0.18)
        header.move_to([0, FH/2 - 0.40 - header.height/2, 0])

        rows = (
            ("01  DIFFERENCE OF SQUARES", BASE_C,
             ("a", "^{2}", "-", "b", "^{2}", "=", "(", "a", "-", "b", ")", "(", "a", "+", "b", ")")),
            ("02  SQUARE OF A SUM", EXP_C,
             ("a", "^{2}", "+", "2", "a", "b", "+", "b", "^{2}", "=", "(", "a", "+", "b", ")", "^{2}")),
            ("03  SQUARE OF A DIFFERENCE", EXP_C,
             ("a", "^{2}", "-", "2", "a", "b", "+", "b", "^{2}", "=", "(", "a", "-", "b", ")", "^{2}")),
            ("04  DIFFERENCE OF CUBES", BASE_C,
             ("a", "^{3}", "-", "b", "^{3}", "=", "(", "a", "-", "b", ")",
              "(", "a", "^{2}", "+", "a", "b", "+", "b", "^{2}", ")")),
            ("05  SUM OF CUBES", RES_C,
             ("a", "^{3}", "+", "b", "^{3}", "=", "(", "a", "+", "b", ")",
              "(", "a", "^{2}", "-", "a", "b", "+", "b", "^{2}", ")")),
        )
        cards = VGroup()
        for heading, color, pieces in rows:
            card = RoundedRectangle(corner_radius=0.21, width=FW-2*MARGIN, height=1.21,
                                    fill_color=CARD_FILL, fill_opacity=0.94,
                                    stroke_color=CARD_STROKE, stroke_width=2)
            heading_obj = text(heading, 17, color, BOLD, spacing=1050)
            formula = ptex(*pieces, fs=58)
            for part in formula[pieces.index("=")+1:]:
                part.set_color(RES_C)
            fit(formula, card.width-0.55)
            heading_obj.move_to([0, card.get_top()[1]-0.23, 0])
            formula.move_to([0, card.get_center()[1]-0.21, 0])
            cards.add(VGroup(card, heading_obj, formula))
        cards.arrange(DOWN, buff=0.115).next_to(header, DOWN, buff=0.30)

        reminder = text(f"{col('GCF FIRST', EXP_C)}  ·  FACTOR AGAIN IF POSSIBLE", 18, MUTED, BOLD, spacing=550)
        fit(reminder, FW-2*MARGIN)
        reminder.next_to(cards, DOWN, buff=0.32)
        footer = text("CUBE SIGNS: SAME · OPPOSITE · ALWAYS +", 16, MUTED, BOLD, spacing=430)
        fit(footer, FW-2*MARGIN-1.0)
        footer.move_to([-FW/2+MARGIN+footer.width/2, -FH/2+0.40, 0])
        self.add(header, cards, reminder, footer,
                 watermark(FW, FH, width=0.85, inset=0.3))
