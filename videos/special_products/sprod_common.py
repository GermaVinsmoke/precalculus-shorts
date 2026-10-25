"""Shared base and geometry for the Special Products shorts (Section 1.3, Part 4)."""

import sys
from pathlib import Path

_PROJECT_ROOT = Path(__file__).resolve().parents[2]
if str(_PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(_PROJECT_ROOT))

from videos.polynomials.poly_common import *

BR = '<break time="0.2s" />'


class SpecialScene(PolyScene):
    TOPIC = "SPECIAL PRODUCTS"
    BUILD_SUBDIR = "part_4_special_products"


def sum_square(side_a=2.35, side_b=1.0, center=MATH):
    """Four tiles making a square of side a+b, with individually addressable regions."""
    size = side_a + side_b
    left = center[0] - size / 2
    top = center[1] + size / 2
    regions = VGroup()
    for w, h, x, y, color in (
        (side_a, side_a, left, top - side_a, BASE_C),
        (side_b, side_a, left + side_a, top - side_a, EXP_C),
        (side_a, side_b, left, top - size, EXP_C),
        (side_b, side_b, left + side_a, top - size, MUTED),
    ):
        tile = Rectangle(width=w - 0.035, height=h - 0.035,
                         fill_color=color, fill_opacity=0.24,
                         stroke_color=color, stroke_width=3)
        tile.move_to([x + w / 2, y + h / 2, 0])
        regions.add(tile)
    labels = VGroup(*[ptex(*p, fs=68 if i != 3 else 56) for i, p in
                       enumerate((("a", "^{2}"), ("a", "b"), ("a", "b"), ("b", "^{2}")))])
    for label_, tile in zip(labels, regions):
        fit(label_, tile.width - 0.15)
        label_.move_to(tile)
    top_labels = VGroup(ptex("a", fs=55), ptex("b", fs=55))
    top_labels[0].move_to([left + side_a / 2, top + 0.30, 0])
    top_labels[1].move_to([left + side_a + side_b / 2, top + 0.30, 0])
    side_labels = VGroup(ptex("a", fs=55), ptex("b", fs=55))
    side_labels[0].move_to([left - 0.30, top - side_a / 2, 0])
    side_labels[1].move_to([left - 0.30, top - side_a - side_b / 2, 0])
    return VGroup(regions, labels, top_labels, side_labels)
