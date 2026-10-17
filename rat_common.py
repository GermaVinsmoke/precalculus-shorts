"""Shared pieces for the Rational Exponents series (reuses the radical helpers)."""

from rad_common import *


class RatScene(RadScene):
    TOPIC = "RATIONAL EXPONENTS"


def pw(base, exp, fs=BIG_FS, results=()):
    """base^exp with series colours; exp is LaTeX like '1/2'."""
    return auto(tex(base, "^{%s}" % exp, fs=fs), results=results)
