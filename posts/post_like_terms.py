"""Instagram post (1080×1350, 4:5): like terms or not?

render: manim render -s --config_file post.cfg posts/post_like_terms.py LikeTermsPost
"""

try:
    from .post_roots import CARD_W, FH, FW, GAP, MARGIN, rule_card, text
except ImportError:  # Manim loading this file directly
    from post_roots import CARD_W, FH, FW, GAP, MARGIN, rule_card, text
from videos.add_subtract.add_common import *

SEP = r",\quad"
PAIRS = [
    (True, "Like terms", ["3", "x", "^{2}", SEP, "5", "x", "^{2}"], r"\text{same variable, same power}"),
    (False, "Not like", ["x", "^{2}", SEP, "x"], r"\text{different powers}"),
    (True, "Like terms", ["4", "x", "y", SEP, "-2", "y", "x"], r"\text{order doesn't matter}"),
    (False, "Not like", ["x", "^{3}", SEP, "3", "x"], r"\text{an exponent isn't a coefficient}"),
    (True, "Like terms", ["7", SEP, "-3"], r"\text{both plain numbers}"),
    (False, "Not like", ["2", "x", "^{2}", "y", SEP, "2", "x", "y", "^{2}"], r"\text{powers on different letters}"),
]


class LikeTermsPost(Scene):
    def construct(self):
        bg = ImageMobject(str(background_path(1080, 1350)))
        bg.height = FH
        self.add(bg)

        bars = VGroup(*[RoundedRectangle(corner_radius=0.03, width=0.5, height=0.08, fill_color=c, fill_opacity=1,
                                         stroke_width=0) for c in (BASE_C, EXP_C, RES_C)]).arrange(RIGHT, buff=0.1)
        kicker = text("ADD &amp; SUBTRACT", 17, MUTED, BOLD, spacing=3200)
        title = fit(text(f"Like Terms {col('or Not?', EXP_C)}", 58, INK, BOLD), FW - 2 * MARGIN - 0.2)
        sub = text(f"Same variables, same powers: {col('combine', RES_C)}.", 22, MUTED)
        header = VGroup(bars, kicker, title, sub).arrange(DOWN, buff=0.2)
        header.move_to([0, FH / 2 - 0.4 - header.height / 2, 0])

        top = header.get_bottom()[1] - 0.4
        bottom = -FH / 2 + 0.95
        h = (top - bottom - 2 * GAP) / 3
        grid = VGroup()
        for k, (like, name, parts, why) in enumerate(PAIRS):
            pair = ptex(*parts, fs=58)
            accent = RES_C if like else WARN_C
            card = rule_card("✓" if like else "✗", name, pair, why, h, accent=accent, stroke=accent)
            r, c = divmod(k, 2)
            card.move_to([-FW / 2 + MARGIN + CARD_W / 2 + c * (CARD_W + GAP), top - h / 2 - r * (h + GAP), 0])
            grid.add(card)

        note = text("The numbers in front never matter. Only the variables and their powers.", 16, MUTED)
        fit(note, FW - 2 * MARGIN - 1.4)
        note.move_to([-FW / 2 + MARGIN + note.width / 2, (bottom - FH / 2) / 2 + 0.05, 0])
        self.add(header, grid, note, watermark(FW, FH, width=0.85, inset=0.3))
