"""Shared pieces for the Rationalizing the Denominator series."""

from rad_common import *


class RatzScene(RadScene):
    TOPIC = "RATIONALIZING"


def meter(n, filled, width=None, height=0.55, color=EXP_C):
    """An exponent meter: n slots, the first `filled` coloured in."""
    width = width or min(0.75 * n, SAFE_W - 0.6)
    w = (width - 0.08 * (n - 1)) / n
    slots = VGroup(*[
        RoundedRectangle(corner_radius=0.08, width=w, height=height, stroke_color=MUTED, stroke_width=2.5,
                         fill_color=color if k < filled else CARD_FILL, fill_opacity=0.95 if k < filled else 0.6)
        for k in range(n)
    ]).arrange(RIGHT, buff=0.08)
    return slots
