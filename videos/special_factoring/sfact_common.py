"""Shared base and square-cut visual for Section 1.3, Part 6."""

import sys
from pathlib import Path

_PROJECT_ROOT = Path(__file__).resolve().parents[2]
if str(_PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(_PROJECT_ROOT))

from videos.polynomials.poly_common import *

BR = '<break time="0.2s" />'


class SpecialFactorScene(PolyScene):
    TOPIC = "SPECIAL FACTORING"
    BUILD_SUBDIR = "part_6_special_factoring"


def cut_square(a=2.45, b=0.8, left=-2.05, bottom=0.55):
    """A²−B² as two strips and a removed corner.

    The lower strip rotates into the right-hand B×(A−B) strip. The upper
    strip is A×(A−B); together they are (A+B)×(A−B).
    """
    top = Rectangle(width=a, height=a-b, fill_color=BASE_C,
                    fill_opacity=0.23, stroke_color=BASE_C, stroke_width=3)
    top.move_to([left+a/2, bottom+b+(a-b)/2, 0])
    lower = Rectangle(width=a-b, height=b, fill_color=EXP_C,
                      fill_opacity=0.29, stroke_color=EXP_C, stroke_width=3)
    lower.move_to([left+(a-b)/2, bottom+b/2, 0])
    missing = Rectangle(width=b, height=b, fill_color=CARD_FILL,
                        fill_opacity=1, stroke_color=WARN_C, stroke_width=3)
    missing.move_to([left+a-b/2, bottom+b/2, 0])
    label_a = ptex("a", "(", "a", "-", "b", ")", fs=56).move_to(top)
    label_strip = ptex("b", "(", "a", "-", "b", ")", fs=45).move_to(lower)
    label_missing = ptex("b", "^{2}", fs=48).move_to(missing)
    return top, lower, missing, label_a, label_strip, label_missing


def square_tiles(center=MATH):
    """One x² tile, two 3x strips and a 3² corner as a square."""
    a, b = 2.22, 0.86
    left = center[0] - (a+b)/2
    bottom = center[1] - (a+b)/2
    regions = VGroup()
    for w, h, x, y, color in (
        (a, a, left, bottom+b, BASE_C),
        (b, a, left+a, bottom+b, EXP_C),
        (a, b, left, bottom, EXP_C),
        (b, b, left+a, bottom, MUTED),
    ):
        tile = Rectangle(width=w-0.035, height=h-0.035, fill_color=color,
                         fill_opacity=0.24, stroke_color=color, stroke_width=3)
        tile.move_to([x+w/2, y+h/2, 0])
        regions.add(tile)
    labels = VGroup(*[ptex(*parts, fs=65 if i < 3 else 48) for i, parts in
                      enumerate((("x", "^{2}"), ("3", "x"), ("3", "x"), ("9",)))])
    for lab, tile in zip(labels, regions):
        fit(lab, tile.width-0.18).move_to(tile)
    top = VGroup(ptex("x", fs=52), ptex("3", fs=52))
    side = VGroup(ptex("x", fs=52), ptex("3", fs=52))
    for lab, x in zip(top, (left+a/2, left+a+b/2)):
        lab.move_to([x, bottom+a+b+0.28, 0])
    for lab, y in zip(side, (bottom+b+a/2, bottom+b/2)):
        lab.move_to([left-0.29, y, 0])
    return VGroup(regions, labels, top, side)


def cubes_formula(sign="-", fs=SMALL_FS):
    """A³ ± B³, preserving binary sign spacing in one MathTex."""
    other = "+" if sign == "-" else "-"
    return poly([["a", "^{3}"], [sign, "b", "^{3}"], ["="],
                 ["(", "a", sign, "b", ")"],
                 ["(", "a", "^{2}", other, "a", "b", "+", "b", "^{2}", ")"]], fs=fs)
