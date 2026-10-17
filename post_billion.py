"""Instagram post (1080×1350, 4:5): How big is a billion? (Exercise 103)

render: manim render -s --config_file post.cfg post_billion.py BillionPost
"""

from common import *

FW, FH = 9, 11.25
MARGIN = 0.45
GAP = 0.22


def text(markup, fs, color=INK, weight=MEDIUM, spacing=None):
    if spacing:
        markup = f'<span letter_spacing="{spacing}">{markup}</span>'
    return MarkupText(markup, font=FONT, font_size=fs, color=color, weight=weight)


def card_box(w, h):
    return RoundedRectangle(corner_radius=0.26, width=w, height=h, fill_color=CARD_FILL, fill_opacity=0.94,
                            stroke_color=CARD_STROKE, stroke_width=2)


def money_card(title, exp, days_exp, years, w, h):
    box = card_box(w, h)
    head = text(title, 17, EXP_C, BOLD, spacing=2600)
    amount = tex(r"\$", "10", "^{%d}" % exp, fs=72)
    amount[1].set_color(BASE_C)
    amount[2].set_color(EXP_C)
    calc = tex(r"\div", r"\$", "10", "^{3}", r"\text{/day}", fs=34, color=MUTED)
    calc[2].set_color(BASE_C)
    calc[3].set_color(EXP_C)
    days = tex("=", "10", "^{%d}" % days_exp, r"\text{ days}", fs=40)
    days[1].set_color(BASE_C)
    days[2].set_color(EXP_C)
    result = text(years, 30, RES_C, BOLD)
    body = VGroup(head, amount, calc, days, result).arrange(DOWN, buff=0.16)
    body[4].shift(DOWN * 0.06)
    fit(body, w - 0.4)
    if body.height > h - 0.4:
        body.scale_to_fit_height(h - 0.4)
    return VGroup(box, body.move_to(box))


class BillionPost(Scene):
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
        kicker = text("SCIENTIFIC NOTATION", 17, MUTED, BOLD, spacing=3200)
        title = text(f"How big is a {col('billion', EXP_C)}?", 50, INK, BOLD)
        sub = text("Spend $1,000 every single day…", 22, MUTED)
        header = VGroup(bars, kicker, title, sub).arrange(DOWN, buff=0.2)
        header.move_to([0, FH / 2 - 0.4 - header.height / 2, 0])

        # ── Million vs billion ──────────────────────────────────────────
        w = (FW - 2 * MARGIN - GAP) / 2
        h = 2.75
        million = money_card("A MILLION", 6, 3, "≈ 2.7 years", w, h)
        billion = money_card("A BILLION", 9, 6, "≈ 2,738 years", w, h)
        pair = VGroup(million, billion).arrange(RIGHT, buff=GAP)
        pair.next_to(header, DOWN, buff=0.4)

        # ── 1,000 squares: one is a million, all of them a billion ──────
        cols, rows = 50, 20
        cell = (FW - 2 * MARGIN - 0.6) / cols
        squares = VGroup(
            *[
                Square(side_length=cell * 0.78, fill_color=BASE_C, fill_opacity=0.55, stroke_width=0)
                for _ in range(cols * rows)
            ]
        ).arrange_in_grid(rows=rows, cols=cols, buff=cell * 0.22)
        squares[0].set_fill(EXP_C, opacity=1)
        grid_caption = VGroup(
            text(f"Each square is {col('$1 million', EXP_C)}.", 20, INK),
            text(f"A billion is {col('all 1,000', BASE_C)} of them.", 20, INK),
        ).arrange(DOWN, buff=0.12)
        grid_body = VGroup(squares, grid_caption).arrange(DOWN, buff=0.32)
        grid_box = card_box(FW - 2 * MARGIN, grid_body.height + 0.55)
        grid_card = VGroup(grid_box, grid_body.move_to(grid_box))
        grid_card.next_to(pair, DOWN, buff=GAP)

        # ── Punchline ───────────────────────────────────────────────────
        punch = text(f"Start around 700 BC, and you'd {col('still be spending', RES_C)} today.", 21, INK)
        fit(punch, FW - 2 * MARGIN - 1.4)
        punch.next_to(grid_card, DOWN, buff=0.32).shift(LEFT * 0.55)

        self.add(header, pair, grid_card, punch, watermark(FW, FH, width=0.95, inset=0.3))
