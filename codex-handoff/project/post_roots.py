"""Instagram post (1080×1350, 4:5): the properties of nth roots.

render: manim render -s --config_file post.cfg post_roots.py RootRulesPost
"""

from rad_common import *

FW, FH = 9, 11.25
MARGIN = 0.45
GAP = 0.22
PAD = 0.22
CARD_W = (FW - 2 * MARGIN - GAP) / 2

RULES = [
    ("Product", lambda: rtex(rt("n"), "ab}", "=", rt("n"), "a}", rt("n"), "b}", fs=50),
     r"\sqrt[3]{8\cdot 27} = \sqrt[3]{8}\,\sqrt[3]{27} = 6"),
    ("Quotient", lambda: rtex(rt("n"), "{a", r"\over", "b}}", "=", r"{\sqrt[n]{", "a}", r"\over", rt("n"), "b}}",
                              fs=50),
     r"\sqrt[4]{16/81} = 2/3"),
    ("Root of a root", lambda: rtex(rt("m"), rt("n"), "a}}", "=", rt("mn"), "a}", fs=50),
     r"\sqrt{\sqrt[3]{729}} = \sqrt[6]{729} = 3"),
    ("Odd n keeps the sign", lambda: rtex(rt("n"), "a", "^{n}}", "=", "a", fs=50),
     r"\sqrt[3]{(-5)^3} = -5"),
    ("Even n: absolute value", lambda: rtex(rt("n"), "a", "^{n}}", "=", "|a|", fs=50, results=[4]),
     r"\sqrt[4]{(-3)^4} = |{-3}| = 3"),
]


def text(markup, fs, color=INK, weight=MEDIUM, spacing=None):
    if spacing:
        markup = f'<span letter_spacing="{spacing}">{markup}</span>'
    return MarkupText(markup, font=FONT, font_size=fs, color=color, weight=weight)


def rule_card(badge_text, name, formula, example, h, accent=EXP_C, stroke=CARD_STROKE):
    box = RoundedRectangle(corner_radius=0.26, width=CARD_W, height=h, fill_color=CARD_FILL, fill_opacity=0.94,
                           stroke_color=stroke, stroke_width=2)
    badge = VGroup(
        Circle(radius=0.16, fill_color=CARD_FILL, fill_opacity=1, stroke_color=accent, stroke_width=2.5),
        text(badge_text, 17, accent, BOLD),
    )
    badge[1].move_to(badge[0])
    title = text(name, 19, INK, BOLD)
    head = VGroup(badge, title).arrange(RIGHT, buff=0.14)
    fit(head, CARD_W - 2 * PAD)
    head.move_to(box.get_corner(UL) + RIGHT * (PAD + head.width / 2) + DOWN * (PAD + head.height / 2))

    ex = tex(example, fs=28, color=MUTED)
    fit(ex, CARD_W - 2 * PAD)
    ex.move_to(box.get_bottom() + UP * (PAD + ex.height / 2 - 0.02))

    top, bottom = head.get_bottom()[1] - 0.1, ex.get_top()[1] + 0.1
    fit(formula, CARD_W - 2 * PAD - 0.1)
    if formula.height > top - bottom:
        formula.scale_to_fit_height(top - bottom)
    formula.move_to([box.get_x(), (top + bottom) / 2, 0])
    return VGroup(box, head, formula, ex)


class RootRulesPost(Scene):
    def construct(self):
        bg = ImageMobject(str(background_path(1080, 1350)))
        bg.height = FH
        self.add(bg)

        # ── Header ──────────────────────────────────────────────────────
        bars = VGroup(
            *[
                RoundedRectangle(corner_radius=0.03, width=0.5, height=0.08, fill_color=c, fill_opacity=1,
                                 stroke_width=0)
                for c in (BASE_C, EXP_C, RES_C)
            ]
        ).arrange(RIGHT, buff=0.1)
        kicker = text("RADICALS", 17, MUTED, BOLD, spacing=3200)
        title = text(f"The {col('5', EXP_C)} Root Rules", 62, INK, BOLD)
        sub = text(f"Every root {col('undoes a power', RES_C)}.", 22, MUTED)
        header = VGroup(bars, kicker, title, sub).arrange(DOWN, buff=0.2)
        header.move_to([0, FH / 2 - 0.4 - header.height / 2, 0])

        # ── Grid: five rules + one warning ──────────────────────────────
        top = header.get_bottom()[1] - 0.4
        bottom = -FH / 2 + 0.95  # leaves a footer strip for the note and the logo
        h = (top - bottom - 2 * GAP) / 3
        cards = [rule_card(str(i), name, make(), ex, h) for i, (name, make, ex) in enumerate(RULES, 1)]
        warn = rtex(rt(), "a", "+", "b}", r"\neq", rt(), "a}", "+", rt(), "b}", fs=50)
        warn[4].set_color(WARN_C)
        cards.append(rule_card("!", "Never over a plus sign", warn, r"\sqrt{9+16} = 5,\ \text{not } 7", h,
                               accent=WARN_C, stroke=WARN_C))
        grid = VGroup()
        for k, c in enumerate(cards):
            r, col_ = divmod(k, 2)
            x = -FW / 2 + MARGIN + CARD_W / 2 + col_ * (CARD_W + GAP)
            y = top - h / 2 - r * (h + GAP)
            c.move_to([x, y, 0])
            grid.add(c)

        note = text("Assumes every root exists.", 16, MUTED)
        note.move_to([-FW / 2 + MARGIN + note.width / 2, (bottom - FH / 2) / 2 + 0.05, 0])
        self.add(header, grid, note, watermark(FW, FH, width=0.85, inset=0.3))
