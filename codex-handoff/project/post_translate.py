"""Instagram post (1080×1350, 4:5): translating between radicals and fraction exponents.

render: manim render -s --config_file post.cfg post_translate.py TranslatorPost
"""

from post_roots import FH, FW, GAP, MARGIN, CARD_W, rule_card, text
from rat_common import *

RULES = [
    ("1 over n = a root", lambda: rtex("a", "^{1/n}", "=", rt("n"), "a}", fs=56),
     r"4^{1/2} = \sqrt{4} = 2"),
    ("Root first", lambda: rtex("a", "^{m/n}", "=", "(", rt("n"), "a}", ")", "^{m}", fs=56),
     r"8^{2/3} = (\sqrt[3]{8})^2 = 4"),
    ("Power first", lambda: rtex("a", "^{m/n}", "=", rt("n"), "a", "^{m}}", fs=56),
     r"8^{2/3} = \sqrt[3]{64} = 4"),
    ("Negative: flip it", lambda: rtex("a", "^{-m/n}", "=", "{1", r"\over", "a", "^{m/n}}", fs=56),
     r"125^{-1/3} = 1/5"),
    ("The laws still work", lambda: auto(tex("a", "^{1/2}", r"\cdot", "a", "^{1/3}", "=", "a", "^{5/6}", fs=56)),
     r"(2\sqrt{x})(3\sqrt[3]{x}) = 6x^{5/6}"),
]


class TranslatorPost(Scene):
    def construct(self):
        bg = ImageMobject(str(background_path(1080, 1350)))
        bg.height = FH
        self.add(bg)

        bars = VGroup(
            *[
                RoundedRectangle(corner_radius=0.03, width=0.5, height=0.08, fill_color=c, fill_opacity=1,
                                 stroke_width=0)
                for c in (BASE_C, EXP_C, RES_C)
            ]
        ).arrange(RIGHT, buff=0.1)
        kicker = text("RATIONAL EXPONENTS", 17, MUTED, BOLD, spacing=3200)
        title = fit(text(f"Radicals {col('⇄', EXP_C)} Exponents", 56, INK, BOLD), FW - 2 * MARGIN - 0.2)
        sub = text(f"Bottom of the fraction: {col('root', BASE_C)}. Top: {col('power', EXP_C)}.", 22, MUTED)
        header = VGroup(bars, kicker, title, sub).arrange(DOWN, buff=0.2)
        header.move_to([0, FH / 2 - 0.4 - header.height / 2, 0])

        top = header.get_bottom()[1] - 0.4
        bottom = -FH / 2 + 0.95
        h = (top - bottom - 2 * GAP) / 3
        cards = [rule_card(str(i), name, make(), ex, h) for i, (name, make, ex) in enumerate(RULES, 1)]
        warn = rtex("(-4)", "^{1/2}", "=", rt(), "-4}", fs=56)
        cards.append(rule_card("!", "Even root, negative base", warn, r"\text{not a real number}", h,
                               accent=WARN_C, stroke=WARN_C))
        grid = VGroup()
        for k, c in enumerate(cards):
            r, col_ = divmod(k, 2)
            x = -FW / 2 + MARGIN + CARD_W / 2 + col_ * (CARD_W + GAP)
            y = top - h / 2 - r * (h + GAP)
            c.move_to([x, y, 0])
            grid.add(c)

        note = text("Here m/n is in lowest terms.", 16, MUTED)
        note.move_to([-FW / 2 + MARGIN + note.width / 2, (bottom - FH / 2) / 2 + 0.05, 0])
        self.add(header, grid, note, watermark(FW, FH, width=0.85, inset=0.3))
