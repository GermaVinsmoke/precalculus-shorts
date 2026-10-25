"""Shared pieces for the Rational Exponents series (reuses the radical helpers)."""

import sys
from pathlib import Path

_PROJECT_ROOT = Path(__file__).resolve().parents[2]
if str(_PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(_PROJECT_ROOT))

from videos.radicals.rad_common import *


class RatScene(RadScene):
    TOPIC = "RATIONAL EXPONENTS"


def pw(base, exp, fs=BIG_FS, results=()):
    """base^exp with series colours; exp is LaTeX like '1/2'."""
    return auto(tex(base, "^{%s}" % exp, fs=fs), results=results)
