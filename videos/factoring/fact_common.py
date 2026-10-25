"""Shared visuals for factoring (Section 1.3, Part 5)."""

import sys
from pathlib import Path

_PROJECT_ROOT = Path(__file__).resolve().parents[2]
if str(_PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(_PROJECT_ROOT))

from videos.polynomials.poly_common import *

BR = '<break time="0.2s" />'


class FactorScene(PolyScene):
    TOPIC = "FACTORING"
    BUILD_SUBDIR = "part_5_factoring"


def pair_panel(r, s, target_product, target_sum, width=5.7, height=2.35):
    """A two-number search panel with live product/sum checks.

    Make a fresh panel for each candidate and transform between panels in the
    scene. The product and sum are calculated from the supplied pair, not typed.
    """
    match = r * s == target_product and r + s == target_sum
    stroke = RES_C if match else CARD_STROKE
    box = RoundedRectangle(corner_radius=0.27, width=width, height=height,
                           fill_color=CARD_FILL, fill_opacity=0.94,
                           stroke_color=stroke, stroke_width=2.5)

    def slot(n):
        rim = RoundedRectangle(corner_radius=0.16, width=1.0, height=0.76,
                               fill_color=CARD_FILL, fill_opacity=1,
                               stroke_color=RES_C if match else EXP_C, stroke_width=2.5)
        number = tex(str(n), fs=62, color=RES_C if match else INK)
        return VGroup(rim, number.move_to(rim))

    values = VGroup(slot(r), tex(r"\text{and}", fs=33, color=MUTED), slot(s))
    values.arrange(RIGHT, buff=0.23).move_to(box.get_top() + DOWN * 0.68)
    product = label(f"product: {r*s}   /   need {target_product}", fs=31,
                    color=RES_C if r*s == target_product else WARN_C)
    summation = label(f"sum: {r+s}   /   need {target_sum}", fs=31,
                      color=RES_C if r+s == target_sum else WARN_C)
    rows = VGroup(product, summation).arrange(DOWN, buff=0.12)
    fit(rows, width - 0.45)
    rows.move_to(box.get_bottom() + UP * 0.69)
    return VGroup(box, values, rows)
