"""Shared base and factor-tree visuals for Section 1.3, Part 7."""

import sys
from pathlib import Path

_PROJECT_ROOT = Path(__file__).resolve().parents[2]
if str(_PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(_PROJECT_ROOT))

from videos.polynomials.poly_common import *

BR = '<break time="0.2s" />'


class CompleteScene(PolyScene):
    TOPIC = "FACTOR COMPLETELY"
    BUILD_SUBDIR = "part_7_factor_completely"


def factor_node(expr, fs=52, color=CARD_STROKE, pad=0.18):
    """A compact expression node for a factor tree."""
    math = ptex(*expr, fs=fs) if isinstance(expr, (tuple, list)) else expr
    box = RoundedRectangle(
        corner_radius=0.16,
        width=math.width + 2 * pad,
        height=math.height + 2 * pad,
        fill_color=CARD_FILL,
        fill_opacity=0.94,
        stroke_color=color,
        stroke_width=2.5,
    )
    math.move_to(box)
    return VGroup(box, math)


def tree_edge(parent, child, color=MUTED):
    """A branch connecting two factor-tree nodes."""
    return Line(
        parent[0].get_bottom() + DOWN * 0.02,
        child[0].get_top() + UP * 0.02,
        color=color,
        stroke_width=3,
    ).set_z_index(-1)


def prime_leaf(node):
    """Animations that mark a factor-tree leaf as fully factored."""
    return [
        node[0].animate.set_stroke(RES_C, width=3.5),
        node[1].animate.set_color(RES_C),
    ]
