"""Instagram post (1080×1350, 4:5): the seven laws of exponents.

render: manim render -s --config_file post.cfg post_seven_laws.py SevenLawsPost
"""

from common import *

FW, FH = 9, 11.25
MARGIN = 0.45
GAP = 0.22
CARD_W = (FW - 2 * MARGIN - GAP) / 2
CARD_H = 1.9
PAD = 0.22

LAWS = [
    ("Product", ["a", "^{m}", r"\cdot", "a", "^{n}", "=", "a", "^{m+n}"],
     r"3^2\cdot 3^5 = 3^7"),
    ("Quotient", ["{a", "^{m}", r"\over", "a", "^{n}}", "=", "a", "^{m-n}"],
     r"3^5/3^2 = 3^3"),
    ("Power of a power", ["(", "a", "^{m}", ")", "^{n}", "=", "a", "^{mn}"],
     r"(3^2)^5 = 3^{10}"),
    ("Power of a product", ["(", "a", "b", ")", "^{n}", "=", "a", "^{n}", "b", "^{n}"],
     r"(3\cdot 4)^2 = 3^2\cdot 4^2"),
    ("Power of a quotient", [r"\left(", "{a", r"\over", "b}", r"\right)", "^{n}", "=", "{a", "^{n}", r"\over", "b",
                             "^{n}}"],
     r"(3/4)^2 = 3^2/4^2"),
    ("Flip the fraction", [r"\left(", "{a", r"\over", "b}", r"\right)", "^{-n}", "=", r"\left(", "{b", r"\over",
                           "a}", r"\right)", "^{n}"],
     r"(3/4)^{-2} = (4/3)^2"),
    ("Cross the bar", ["{a", "^{-n}", r"\over", "b", "^{-m}}", "=", "{b", "^{m}", r"\over", "a", "^{n}}"],
     r"3^{-2}/4^{-5} = 4^5/3^2"),
]


def text(markup, fs, color=INK, weight=MEDIUM, spacing=None):
    if spacing:
        markup = f'<span letter_spacing="{spacing}">{markup}</span>'
    return MarkupText(markup, font=FONT, font_size=fs, color=color, weight=weight)


def card_box():
    return RoundedRectangle(
        corner_radius=0.26, width=CARD_W, height=CARD_H,
        fill_color=CARD_FILL, fill_opacity=0.94, stroke_color=CARD_STROKE, stroke_width=2,
    )


def law_card(i, name, parts, example):
    box = card_box()
    badge = VGroup(
        Circle(radius=0.16, fill_color=CARD_FILL, fill_opacity=1, stroke_color=EXP_C, stroke_width=2.5),
        text(str(i), 17, EXP_C, BOLD),
    )
    badge[1].move_to(badge[0])
    title = text(name, 19, INK, BOLD)
    head = VGroup(badge, title).arrange(RIGHT, buff=0.14)
    head.move_to(box.get_corner(UL) + RIGHT * (PAD + head.width / 2) + DOWN * (PAD + head.height / 2))

    ex = tex(example, fs=28, color=MUTED)
    fit(ex, CARD_W - 2 * PAD)
    ex.move_to(box.get_bottom() + UP * (PAD + ex.height / 2 - 0.02))

    # the formula gets whatever space is left between the title and the example
    space_top = head.get_bottom()[1] - 0.1
    space_bottom = ex.get_top()[1] + 0.1
    formula = auto(tex(*parts, fs=44))
    fit(formula, CARD_W - 2 * PAD - 0.1)
    if formula.height > space_top - space_bottom:
        formula.scale_to_fit_height(space_top - space_bottom)
    formula.move_to([box.get_x(), (space_top + space_bottom) / 2, 0])
    return VGroup(box, head, formula, ex)


def key_card():
    box = card_box()
    title = text("Read the colors", 19, INK, BOLD)
    title.move_to(box.get_corner(UL) + RIGHT * (PAD + title.width / 2) + DOWN * (PAD + title.height / 2))
    power = auto(tex("a", "^{n}", fs=72))
    power.move_to(box.get_center() + LEFT * 0.85 + DOWN * 0.05)
    base = text("base", 19, BASE_C, BOLD).next_to(power[0], RIGHT, buff=0.85).shift(DOWN * 0.18)
    expo = text("exponent", 19, EXP_C, BOLD).next_to(power[1], RIGHT, buff=0.55).shift(UP * 0.1)
    base_line = Line(base.get_left() + LEFT * 0.08, power[0].get_right() + RIGHT * 0.06, color=BASE_C,
                     stroke_width=2.5)
    expo_line = Line(expo.get_left() + LEFT * 0.08, power[1].get_right() + RIGHT * 0.06, color=EXP_C,
                     stroke_width=2.5)
    note = text("a, b ≠ 0  ·  m, n integers", 15, MUTED)
    note.move_to(box.get_bottom() + UP * (PAD + note.height / 2))
    return VGroup(box, title, power, base, expo, base_line, expo_line, note)


class SevenLawsPost(Scene):
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
        kicker = text("LAWS OF EXPONENTS", 17, MUTED, BOLD, spacing=3200)
        title = text(f"The {col('7', EXP_C)} Laws", 66, INK, BOLD)
        sub = text(f"Every rule is just {col('counting factors', RES_C)}.", 22, MUTED)
        header = VGroup(bars, kicker, title, sub).arrange(DOWN, buff=0.2)
        header[2].shift(DOWN * 0.04)
        header.move_to([0, FH / 2 - 0.4 - header.height / 2, 0])

        # ── Grid: 7 laws + colour key ───────────────────────────────────
        cards = [law_card(i, *law) for i, law in enumerate(LAWS, 1)] + [key_card()]
        grid = VGroup()
        top = header.get_bottom()[1] - 0.4
        for k, c in enumerate(cards):
            r, col_ = divmod(k, 2)
            x = -FW / 2 + MARGIN + CARD_W / 2 + col_ * (CARD_W + GAP)
            y = top - CARD_H / 2 - r * (CARD_H + GAP)
            c.move_to([x, y, 0])
            grid.add(c)

        self.add(header, grid)
