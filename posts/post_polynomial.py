"""Instagram post (1080×1350, 4:5): anatomy of a polynomial.

render: manim render -s --config_file post.cfg posts/post_polynomial.py PolynomialAnatomyPost
"""

try:
    from .post_roots import FH, FW, GAP, MARGIN, text
except ImportError:  # Manim loading this file directly
    from post_roots import FH, FW, GAP, MARGIN, text
from videos.polynomials.poly_common import *

INNER_W = FW - 2 * MARGIN


def box(w, h, stroke=CARD_STROKE):
    return RoundedRectangle(corner_radius=0.26, width=w, height=h, fill_color=CARD_FILL, fill_opacity=0.94,
                            stroke_color=stroke, stroke_width=2)


def callout(txt, target, at, color=INK, side=DOWN):
    """A label at `at` with a thin leader line to `target`."""
    lbl = text(txt, 19, color, BOLD).move_to(at)
    start = lbl.get_edge_center(side)
    lead = Line(start, target, color=color, stroke_width=2, stroke_opacity=0.8)
    dot = Dot(target, radius=0.04, color=color)
    return VGroup(lbl, lead, dot)


class PolynomialAnatomyPost(Scene):
    def construct(self):
        bg = ImageMobject(str(background_path(1080, 1350)))
        bg.height = FH
        self.add(bg)

        # ── Header ──────────────────────────────────────────────────────
        bars = VGroup(*[RoundedRectangle(corner_radius=0.03, width=0.5, height=0.08, fill_color=c, fill_opacity=1,
                                         stroke_width=0) for c in (BASE_C, EXP_C, RES_C)]).arrange(RIGHT, buff=0.1)
        kicker = text("POLYNOMIALS", 17, MUTED, BOLD, spacing=3200)
        title = fit(text(f"Anatomy of a {col('Polynomial', BASE_C)}", 52, INK, BOLD), INNER_W - 0.2)
        sub = text("Every part has a name.", 22, MUTED)
        header = VGroup(bars, kicker, title, sub).arrange(DOWN, buff=0.2)
        header.move_to([0, FH / 2 - 0.4 - header.height / 2, 0])

        # ── Main card: the labelled polynomial ──────────────────────────
        main_h = 4.15
        main = box(INNER_W, main_h)
        main.next_to(header, DOWN, buff=0.38)
        p = poly([["5", "x", "^{3}"], ["-", "3", "x", "^{2}"], ["+", "x"], ["-", "7"]], fs=120)
        fit(p, INNER_W - 1.6)
        p.move_to(main.get_center() + UP * 0.15)
        top, bot = p.get_top()[1], p.get_bottom()[1]
        lead = callout("leading coefficient", p[0].get_top() + UP * 0.05,
                       [p[0].get_x() + 1.0, top + 1.0, 0], INK)
        expo = callout("exponent", p[2].get_top() + UP * 0.04, [p[2].get_x() + 1.1, top + 0.35, 0], EXP_C,
                       side=LEFT)
        brace = Brace(p.terms[1], DOWN, buff=0.12, color=BASE_C)
        term = text("term", 19, BASE_C, BOLD).next_to(brace, DOWN, buff=0.08)
        var = callout("variable", p[8].get_bottom() + DOWN * 0.05, [p[8].get_x() + 0.1, bot - 0.55, 0], BASE_C,
                      side=UP)
        const = callout("constant term", p[10].get_bottom() + DOWN * 0.05,
                        [p[10].get_x() - 0.35, bot - 1.0, 0], INK, side=UP)
        degree = text(f"degree {col('3', RES_C)}: the highest exponent", 21, MUTED)
        degree.move_to([main.get_x(), main.get_bottom()[1] + 0.38, 0])
        labels = VGroup(lead, expo, brace, term, var, const)

        # ── Lower cards: naming, and what isn't a polynomial ────────────
        low_h = 3.0
        w = (INNER_W - GAP) / 2
        names = box(w, low_h)
        nots = box(w, low_h, stroke=WARN_C)
        VGroup(names, nots).arrange(RIGHT, buff=GAP).next_to(main, DOWN, buff=GAP)

        def card_title(t, c, b):
            return text(t, 19, c, BOLD).move_to(b.get_corner(UL) + RIGHT * (0.22 + 0.0) + DOWN * 0.38,
                                                aligned_edge=LEFT)

        n_title = card_title("Name it by its terms", INK, names)
        n_rows = VGroup()
        for terms, name in (([["9", "x", "^{5}"]], "monomial"),
                            ([["5", "x"], ["+", "1"]], "binomial"),
                            ([["2", "x", "^{2}"], ["-", "3", "x"], ["+", "4"]], "trinomial")):
            n_rows.add(VGroup(poly(terms, fs=44), text(name, 17, BASE_C, BOLD)).arrange(RIGHT, buff=0.25))
        n_rows.arrange(DOWN, buff=0.28, aligned_edge=LEFT)
        fit(n_rows, w - 0.45)
        if n_rows.height > low_h - 1.0:
            n_rows.scale_to_fit_height(low_h - 1.0)
        n_rows.next_to(n_title, DOWN, buff=0.3, aligned_edge=LEFT)

        x_title = card_title("Not polynomials", WARN_C, nots)
        x_rows = VGroup()
        for expr, why in ((rtex(rt(), "x}", "+", "10", fs=44, digits=False), "x to the 1/2"),
                          (ptex("{1", r"\over", "x}", fs=44), "x in the denominator"),
                          (ptex("x", "^{-2}", fs=44), "negative exponent")):
            x_rows.add(VGroup(expr, text(why, 16, MUTED)).arrange(RIGHT, buff=0.25))
        x_rows.arrange(DOWN, buff=0.22, aligned_edge=LEFT)
        fit(x_rows, w - 0.45)
        if x_rows.height > low_h - 1.0:
            x_rows.scale_to_fit_height(low_h - 1.0)
        x_rows.next_to(x_title, DOWN, buff=0.28, aligned_edge=LEFT)

        note = text(f"Coefficients keep their sign: the coefficient of x² is {col('−3', EXP_C)}.", 16, MUTED)
        fit(note, INNER_W - 1.4)
        note.move_to([-FW / 2 + MARGIN + note.width / 2, (names.get_bottom()[1] - FH / 2) / 2 + 0.05, 0])

        self.add(header, main, p, labels, degree, names, nots, n_title, n_rows, x_title, x_rows, note,
                 watermark(FW, FH, width=0.85, inset=0.3))
