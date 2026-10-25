"""Shared pieces for the Radicals series.

Radicals are written as separate MathTex parts so the √ sign can be animated on its own:
    rtex(rt(3), "8", r"\\cdot", "27}")   →  ∛(8·27)
The part made by rt() holds [index, √ sign, bar]; the closing brace rides on the last inner part.
"""

import sys
from pathlib import Path

_PROJECT_ROOT = Path(__file__).resolve().parents[2]
if str(_PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(_PROJECT_ROOT))

from videos.common import *

BR = '<break time="0.2s" />'


class RadScene(NarratedScene):
    TOPIC = "RADICALS"
    WATERMARK = True


def rt(n=None) -> str:
    return r"\sqrt[%s]{" % n if n is not None else r"\sqrt{"


def rtex(*parts, fs=BIG_FS, digits=True, results=()) -> MathTex:
    """MathTex with series colours: contents blue, exponents and root indexes yellow, √ white."""
    m = auto(tex(*parts, fs=fs), digits=digits)
    for p, s in zip(m, m.tex_strings):
        if s.lstrip("{").startswith(r"\sqrt["):
            p.set_color(INK)
            p[0].set_color(EXP_C)
        elif s.lstrip("{").startswith(r"\sqrt{"):
            p.set_color(INK)
        elif re.fullmatch(r"[a-z]{2,3}", s.strip("{} ")):
            p.set_color(BASE_C)  # products like "ab" under a root
    for i in results:
        m[i].set_color(RES_C)
    return m


def check(fs=70) -> MathTex:
    return tex(r"\checkmark", fs=fs, color=RES_C)


def cross(fs=70) -> MathTex:
    return tex(r"\times", fs=fs, color=WARN_C)
