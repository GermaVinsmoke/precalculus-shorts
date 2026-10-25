"""Shared pieces for the Polynomials series (Section 1.3, part 1)."""

import sys
from pathlib import Path

_PROJECT_ROOT = Path(__file__).resolve().parents[2]
if str(_PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(_PROJECT_ROOT))

from videos.radicals.rad_common import *


class PolyScene(NarratedScene):
    TOPIC = "POLYNOMIALS"
    WATERMARK = True


def ptex(*parts, fs=BIG_FS, results=()):
    """Polynomial colouring: variables blue, exponents yellow, coefficients white."""
    return auto(tex(*parts, fs=fs), digits=False, results=results)


def poly(terms, fs=BIG_FS):
    """One MathTex (so TeX spaces the signs properly) with `.terms`: one VGroup per term, sign included.

    terms: list of part-lists, e.g. [["2", "x", "^{2}"], ["-", "3", "x"], ["+", "4"]]
    """
    parts = [p for t in terms for p in t]
    m = ptex(*parts, fs=fs)
    groups, i = VGroup(), 0
    for t in terms:
        groups.add(VGroup(*m[i:i + len(t)]))
        i += len(t)
    m.terms = groups
    return m


def tile(m, color=BASE_C, buff=0.14):
    return SurroundingRectangle(m, color=color, buff=buff, corner_radius=0.14, stroke_width=3)
