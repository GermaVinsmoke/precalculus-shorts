"""Shared pieces for Adding & Subtracting Polynomials."""

from poly_common import *

BIN_X = [CX - 2.55, CX - 0.85, CX + 0.85, CX + 2.55]
BIN_NAMES = [("x", "^{3}"), ("x", "^{2}"), ("x",), ("1",)]


class AddScene(PolyScene):
    TOPIC = "ADD &amp; SUBTRACT"


def algebra_tile(kind, u=0.9):
    """x² = big square, x = long strip, 1 = unit square."""
    if kind == "x2":
        shape = Square(u, fill_color=BASE_C, fill_opacity=0.55, stroke_color=BASE_C, stroke_width=3)
        lbl = ptex("x", "^{2}", fs=50 * u / 0.9)
    elif kind == "x":
        shape = Rectangle(width=u, height=u * 0.32, fill_color=EXP_C, fill_opacity=0.55, stroke_color=EXP_C,
                          stroke_width=3)
        lbl = ptex("x", fs=44 * u / 0.9)
    else:
        shape = Square(u * 0.32, fill_color=MUTED, fill_opacity=0.6, stroke_color=MUTED, stroke_width=3)
        lbl = tex("1", fs=40 * u / 0.9)
    lbl.set_color(INK).move_to(shape)
    if kind != "x2":
        lbl.next_to(shape, DOWN, buff=0.08)
    return VGroup(shape, lbl)


def bin_heads(y):
    heads = VGroup()
    for x, name in zip(BIN_X, BIN_NAMES):
        t = ptex(*name, fs=54)
        box = RoundedRectangle(corner_radius=0.16, width=1.5, height=0.72, fill_color=CARD_FILL, fill_opacity=0.95,
                               stroke_color=CARD_STROKE, stroke_width=2)
        heads.add(VGroup(box, t.move_to(box)).move_to([x, y, 0]))
    return heads


def term(*parts, fs=SMALL_FS, results=()):
    return ptex(*parts, fs=fs, results=results)
