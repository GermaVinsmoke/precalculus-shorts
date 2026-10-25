"""Visual helpers for multiplying algebraic expressions."""

import sys
from pathlib import Path

_PROJECT_ROOT = Path(__file__).resolve().parents[2]
if str(_PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(_PROJECT_ROOT))

from videos.polynomials.poly_common import *


class MultScene(PolyScene):
    TOPIC = "MULTIPLYING"
    BUILD_SUBDIR = "part_3_multiplying"


def area_model(top_terms, side_terms, *, center=MATH, cell_w=2.05, cell_h=1.12):
    """A 2-by-2 multiplication grid, with individually addressable cells.

    Rows follow side_terms, columns follow top_terms; products are deliberately
    separate so a scene can reveal them in FOIL order rather than grid order.
    """
    cells = VGroup()
    for row in range(2):
        for col_idx in range(2):
            color = (BASE_C, EXP_C, EXP_C, MUTED)[row * 2 + col_idx]
            box = RoundedRectangle(
                corner_radius=0.12, width=cell_w - 0.07, height=cell_h - 0.07,
                stroke_color=color, stroke_width=2.5, fill_color=color, fill_opacity=0.13,
            )
            box.move_to(np.array(center) + RIGHT * (col_idx - 0.5) * cell_w
                        + DOWN * (row - 0.5) * cell_h)
            cells.add(box)
    top = VGroup(*[ptex(*t, fs=58) for t in top_terms])
    side = VGroup(*[ptex(*t, fs=58) for t in side_terms])
    for col_idx, term in enumerate(top):
        term.move_to(cells[col_idx].get_top() + UP * 0.34)
    for row, term in enumerate(side):
        term.next_to(cells[row * 2], LEFT, buff=0.28)
    return VGroup(cells, top, side)
