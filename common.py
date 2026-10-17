"""Shared look and feel for the Integer Exponents shorts.

Frame is 9 x 16 units (1080 x 1920 px, 120 px per unit).
"""

from __future__ import annotations

import json
import re
from pathlib import Path

import numpy as np
from manim import *

ROOT = Path(__file__).resolve().parent
ASSETS = ROOT / "assets"
BUILD = ROOT / "build"

# ── Palette ──────────────────────────────────────────────────────────────
BASE_C = "#58C4DD"  # base
EXP_C = "#FFD54F"  # exponent
RES_C = "#83C167"  # result
WARN_C = "#FC6255"  # trap / wrong
INK = "#ECEFF4"
MUTED = "#7D869C"
CARD_FILL = "#141824"
CARD_STROKE = "#2A3042"

FONT = "Avenir Next"

# ── Layout: platform safe zone ───────────────────────────────────────────
# Avoid the top 15 %, bottom 25 % and right 12 % of the frame.
SAFE_TOP = 8 - 0.15 * 16  # 5.6
SAFE_BOTTOM = -8 + 0.25 * 16  # -4.0
SAFE_RIGHT = 4.5 - 0.12 * 9  # 3.42
SAFE_LEFT = -3.9
SAFE_W = SAFE_RIGHT - SAFE_LEFT
CX = (SAFE_LEFT + SAFE_RIGHT) / 2

MATH_Y = 1.75  # centre of the math zone (upper-middle); keep content within ±2.4
CAP_Y = -2.45  # centre of the caption zone (lower-middle)
CAP_MAX_W = SAFE_W - 0.3
MATH = np.array([CX, MATH_Y, 0.0])
CAP = np.array([CX, CAP_Y, 0.0])

HERO_FS = 210
BIG_FS = 150
MID_FS = 110
SMALL_FS = 84
CAP_FS = 40
LABEL_FS = 38


# ── Caption markup helpers ───────────────────────────────────────────────
def col(s: str, c: str) -> str:
    return f'<span foreground="{c}">{s}</span>'


def B(s: str) -> str:
    return col(s, BASE_C)


def E(s: str) -> str:
    return col(s, EXP_C)


def R(s: str) -> str:
    return col(s, RES_C)


def W(s: str) -> str:
    return col(s, WARN_C)


def sup(s: str) -> str:
    return f"<sup>{s}</sup>"


_SUP = str.maketrans("0123456789-−+mn", "⁰¹²³⁴⁵⁶⁷⁸⁹⁻⁻⁺ᵐⁿ")


def plain(markup: str) -> str:
    """Markup → plain text, with <sup> rendered as Unicode superscripts."""
    markup = re.sub(r"<sup>(.*?)</sup>", lambda m: re.sub(r"<[^>]+>", "", m.group(1)).translate(_SUP), markup)
    return re.sub(r"<[^>]+>", "", markup)


def read_time(lines) -> float:
    words = sum(len(plain(l).split()) for l in lines)
    return float(np.clip(1.1 + 0.28 * words, 2.5, 3.8))


def _words(markup: str) -> list[str]:
    """Split on spaces outside tags and outside open <span>/<sup> elements."""
    words, cur, depth, in_tag = [], "", 0, False
    i = 0
    while i < len(markup):
        ch = markup[i]
        if ch == "<":
            in_tag = True
            depth += -1 if markup[i + 1] == "/" else 1
        elif ch == ">":
            in_tag = False
        if ch == " " and not in_tag and depth == 0:
            words.append(cur)
            cur = ""
        else:
            cur += ch
        i += 1
    return words + [cur]


def _cap_text(markup: str) -> MarkupText:
    return MarkupText(markup, font=FONT, font_size=CAP_FS, color=INK, weight=MEDIUM)


def wrap_caption(markup: str) -> list[str]:
    """One line if it fits, else the most balanced two-line split."""
    if _cap_text(markup).width <= CAP_MAX_W:
        return [markup]
    words = _words(markup)
    best = None
    for i in range(1, len(words)):
        a, b = " ".join(words[:i]), " ".join(words[i:])
        w = max(_cap_text(a).width, _cap_text(b).width)
        if best is None or w < best[0]:
            best = (w, [a, b])
    return best[1]


# ── Math helpers ─────────────────────────────────────────────────────────
def tex(*parts, fs=BIG_FS, color=INK, **kw) -> MathTex:
    return MathTex(*parts, font_size=fs, color=color, **kw)


def label(markup: str, fs=LABEL_FS, color=INK, weight=MEDIUM) -> MarkupText:
    return MarkupText(markup, font=FONT, font_size=fs, color=color, weight=weight)


def fit(m: Mobject, width=SAFE_W - 0.3) -> Mobject:
    if m.width > width:
        m.scale_to_fit_width(width)
    return m


MATH_MAX_H = 4.5  # tallest block the math zone can hold


def fit_zone(m: Mobject, width=SAFE_W - 0.3, height=MATH_MAX_H) -> Mobject:
    """Scale a math block down (never up) to fit the math zone, then centre it there."""
    fit(m, width)
    if m.height > height:
        m.scale_to_fit_height(height)
    return m.move_to(MATH)


def background_path(w=1080, h=1920) -> Path:
    p = ASSETS / ("bg.png" if (w, h) == (1080, 1920) else f"bg_{w}x{h}.png")
    if p.exists():
        return p
    from PIL import Image

    ASSETS.mkdir(exist_ok=True)
    y, x = np.mgrid[0:h, 0:w].astype(np.float32)
    d = np.sqrt((x - w * 0.47) ** 2 + (y - h * 0.40) ** 2) / h
    t = np.clip(d / 0.72, 0, 1) ** 1.35
    inner = np.array([21, 26, 38], np.float32)
    outer = np.array([8, 9, 13], np.float32)
    img = inner * (1 - t)[..., None] + outer * t[..., None]
    img += np.random.default_rng(7).normal(0, 0.9, img.shape)  # dither against banding
    Image.fromarray(np.clip(img, 0, 255).astype(np.uint8)).save(p)
    return p


# ── Base scene ───────────────────────────────────────────────────────────
LOGO = ASSETS / "logo.png"


def watermark(frame_w=9.0, frame_h=16.0, width=1.05, inset=0.32, opacity=0.85) -> ImageMobject:
    """Logo pinned to the bottom-right corner."""
    logo = ImageMobject(str(LOGO))
    logo.width = width
    logo.move_to([frame_w / 2 - inset - logo.width / 2, -frame_h / 2 + inset + logo.height / 2, 0])
    logo.set_opacity(opacity)
    logo.set_z_index(100)
    return logo


class ShortScene(Scene):
    TOPIC = "INTEGER EXPONENTS"
    PART = "1 / 3"
    WATERMARK = False

    def setup(self):
        bg = ImageMobject(str(background_path()))
        bg.height = config.frame_height
        bg.set_z_index(-100)
        self.header = self._make_header()
        self.add(bg, self.header)
        self.persistent = [bg, self.header]
        if self.WATERMARK:
            logo = watermark()
            self.add(logo)
            self.persistent.append(logo)
        self._cap = None
        self._cap_start = 0.0
        self._cap_min = 0.0
        self.marks = []
        self.snaps = []

    def snap(self):
        """Mark a storyboard key frame at the current time."""
        self.snaps.append(round(self.now, 3))

    @property
    def now(self) -> float:
        return self.renderer.time

    def _make_header(self) -> VGroup:
        topic = MarkupText(
            f'<span letter_spacing="2800">{self.TOPIC}</span>',
            font=FONT,
            font_size=24,
            color=MUTED,
            weight=BOLD,
        )
        part = MarkupText(
            f'<span letter_spacing="2800">{self.PART}</span>',
            font=FONT,
            font_size=24,
            color=INK,
            weight=BOLD,
        )
        row = VGroup(topic, part).arrange(RIGHT, buff=0.35)
        bars = VGroup(
            *[
                RoundedRectangle(
                    corner_radius=0.03,
                    width=0.42,
                    height=0.07,
                    fill_color=c,
                    fill_opacity=1,
                    stroke_width=0,
                )
                for c in (BASE_C, EXP_C, RES_C)
            ]
        ).arrange(RIGHT, buff=0.08)
        g = VGroup(row, bars).arrange(DOWN, buff=0.22)
        g.move_to([CX, SAFE_TOP - 0.45, 0])
        return g

    # Captions ---------------------------------------------------------
    def _make_caption(self, lines) -> VGroup:
        wrapped = [w for l in lines for w in wrap_caption(l)]
        assert len(wrapped) <= 2, f"caption needs {len(wrapped)} lines: {wrapped}"
        ms = VGroup(*[_cap_text(l) for l in wrapped])
        ms.arrange(DOWN, buff=0.32)
        fit(ms, CAP_MAX_W)  # safety net only; wrapping keeps the size fixed
        ms.move_to(CAP)
        return ms

    def cap(self, *lines, anims=(), run_time=None):
        """Swap the caption, playing `anims` at the same time.

        The previous caption is always held for its minimum reading time.
        """
        if self._cap is not None:
            elapsed = self.now - self._cap_start
            if self._cap_min - elapsed > 0.05:
                self.wait(self._cap_min - elapsed)
        self.marks.append({"t": round(self.now, 3), "caption": " / ".join(plain(l) for l in lines)})
        new = self._make_caption(lines)
        chars = [c for line in new for c in line]
        group = []
        if self._cap is not None:
            group.append(FadeOut(self._cap, shift=UP * 0.18, run_time=0.45))
        group.append(
            LaggedStart(
                *[FadeIn(c, shift=UP * 0.14) for c in chars],
                lag_ratio=0.025,
                run_time=0.9,
                rate_func=rate_functions.ease_out_cubic,
            )
        )
        start = self.now
        kw = {"run_time": run_time} if run_time else {}
        self.play(*group, *anims, **kw)
        self._cap = new
        self._cap_start = start
        self._cap_min = read_time(lines)
        self.snap()

    def hold(self, extra=0.0):
        """Wait until the current caption has been readable long enough."""
        elapsed = self.now - self._cap_start
        t = max(self._cap_min - elapsed, 0) + extra
        if t > 0.05:
            self.wait(t)
        self.snap()

    # Cards ------------------------------------------------------------
    def card(self, content: Mobject, title="KEY IDEA") -> VGroup:
        head = MarkupText(
            f'<span letter_spacing="3000">{title}</span>',
            font=FONT,
            font_size=26,
            color=EXP_C,
            weight=BOLD,
        )
        fit(content, SAFE_W - 1.0)
        inner = VGroup(head, content).arrange(DOWN, buff=0.55)
        box = RoundedRectangle(
            corner_radius=0.35,
            width=SAFE_W - 0.1,
            height=inner.height + 1.2,
            fill_color=CARD_FILL,
            fill_opacity=0.92,
            stroke_color=CARD_STROKE,
            stroke_width=2.5,
        )
        g = VGroup(box, inner)
        inner.move_to(box)
        g.move_to(MATH)
        return g

    def outro(self):
        """Clear back to the opening frame so the short loops cleanly."""
        self.hold(0.6)
        self.snap()
        rest = [m for m in self.mobjects if m not in self.persistent]
        self.play(*[FadeOut(m) for m in rest], run_time=0.9)
        self.wait(0.25)

    def tear_down(self):
        BUILD.mkdir(exist_ok=True)
        (BUILD / f"{type(self).__name__}.marks.json").write_text(
            json.dumps(
                {"duration": round(self.now, 3), "marks": self.marks, "snaps": self.snaps},
                indent=2,
            )
        )


# ── Narrated scenes (voiceover drives timing) ────────────────────────────
WPS = 2.5  # ElevenLabs narration at speed ~0.95 ≈ 150 words/min
_BREAK = re.compile(r'<break time="([\d.]+)s"\s*/>')


def speech_time(vo: str) -> float:
    pauses = sum(float(x) for x in _BREAK.findall(vo))
    words = len(_BREAK.sub(" ", vo).split())
    return words / WPS + pauses + 0.2


def line(sub: str, vo: str | None = None):
    """One subtitle card and the words spoken while it is on screen."""
    if vo is None:
        assert "<sup>" not in sub, f"needs spoken text: {sub}"
        vo = plain(sub)
    return (sub, vo)


def auto(m: MathTex, digits=True, results=()) -> MathTex:
    """Colour a MathTex by its parts: exponents yellow, bases blue."""
    depth = 0  # brace depth of an exponent still open from an earlier part, e.g. "^{-", "2}"
    for part, s in zip(m, m.tex_strings):
        core = s.strip("{} ")
        if depth > 0 or s.lstrip("{ ").startswith("^"):
            part.set_color(EXP_C)
            body = s if depth > 0 else s[s.index("^") + 1:]
            depth = max(depth + body.count("{") - body.count("}"), 0)
        elif re.fullmatch(r"[a-z]", core) or (digits and re.fullmatch(r"\(?-?\d+\)?", core)):
            part.set_color(BASE_C)
    for i in results:
        m[i].set_color(RES_C)
    return m


def chip(text: str, color=EXP_C) -> VGroup:
    t = MarkupText(
        f'<span letter_spacing="2500">{text}</span>', font=FONT, font_size=28, color=color, weight=BOLD
    )
    box = RoundedRectangle(
        corner_radius=0.22, width=t.width + 0.6, height=t.height + 0.36,
        fill_color=CARD_FILL, fill_opacity=0.95, stroke_color=color, stroke_width=2.5,
    )
    return VGroup(box, t.move_to(box))


class NarratedScene(ShortScene):
    """Beats are spoken lines. Subtitles and the ElevenLabs script come from the same text."""

    TOPIC = "LAWS OF EXPONENTS"
    GAP = 0.4  # silence after each beat

    def setup(self):
        super().setup()
        self._cards = []  # (card, window[t0, t1])
        self._lines = []  # (sub, vo, window)
        self._beats = []  # {"vo", "gap"}

    def say(self, *lines, anims=(), run_time=None, gap=None, steps=()):
        """Speak `lines` while playing `anims`, then each of `steps` in turn.

        A step is a list of animations (one play), a number (wait), or a callable. A callable runs
        when its turn comes; if it returns animations they are played then, so `.animate` targets
        are built from the state left by the previous steps.
        """
        lines = [l if isinstance(l, tuple) else line(l) for l in lines]
        gap = self.GAP if gap is None else gap
        start = t = self.now
        if self._cards:
            self._cards[-1][1][1] = start  # previous subtitle stays up until we speak again
        for c, w in self._cards:
            if w[1] + 0.5 < start:
                self.remove(c)
        self._cards = [(c, w) for c, w in self._cards if w[1] + 0.5 >= start]
        for sub, vo in lines:
            w = [t, t + speech_time(vo)]
            self._add_card(sub, w)
            self._lines.append((sub, vo, w))
            t = w[1]
        end = t
        self._cards[-1][1][1] = end + 30  # held until the next beat
        self.marks.append({"t": round(start, 3), "caption": " / ".join(plain(s) for s, _ in lines)})
        if anims:
            self.play(*anims, **({"run_time": run_time} if run_time else {}))
        for step in steps:
            if callable(step):
                result = step()
                if isinstance(result, Animation):
                    self.play(result)
                elif isinstance(result, (list, tuple)) and result:
                    self.play(*result)
            elif isinstance(step, (int, float)):
                self.wait(step)
            else:
                self.play(*step)
        rest = end + gap - self.now
        if rest > 0.05:
            self.wait(rest)
        self._beats.append({"vo": " ".join(vo for _, vo in lines), "gap": round(self.now - end, 2)})
        self.snap()

    def _add_card(self, sub, window):
        card = self._make_caption([sub])
        chars = [c for row in card for c in row]
        ys = [c.get_y() for c in chars]
        for c in chars:
            c.set_fill(opacity=0)

        def update(m, dt):  # "dt" marks it time-based for Manim
            t = self.now
            fade_out = np.clip((window[1] - t) / 0.2, 0, 1)
            for i, (c, y) in enumerate(zip(chars, ys)):
                a = rate_functions.ease_out_cubic(np.clip((t - window[0] - 0.012 * i) / 0.25, 0, 1))
                c.set_fill(opacity=a * fade_out)
                c.set_y(y - (1 - a) * 0.12)

        card.add_updater(update)
        self.add(card)
        self._cards.append((card, window))

    def outro(self):
        self.wait(0.6)
        self.snap()
        for card, w in self._cards:
            card.clear_updaters()
        rest = [m for m in self.mobjects if m not in self.persistent]
        self.play(*[FadeOut(m) for m in rest], run_time=0.9)
        self.wait(0.25)

    def tear_down(self):
        super().tear_down()
        name = type(self).__name__
        # ElevenLabs script: one paragraph per beat, silences as break tags (max 3 s each)
        paras = []
        for b in self._beats:
            text = b["vo"]
            g = b["gap"]
            while g > 0.1:
                text += f' <break time="{min(g, 3.0):.1f}s" />'
                g -= 3.0
            paras.append(text)
        (BUILD / f"{name}.voiceover.txt").write_text("\n\n".join(paras) + "\n")

        def ts(x):
            h, r = divmod(x, 3600)
            m, s = divmod(r, 60)
            return f"{int(h):02d}:{int(m):02d}:{int(s):02d},{int(round((s % 1) * 1000)):03d}"

        srt = []
        for i, (sub, _vo, w) in enumerate(self._lines, 1):
            end = min(w[1], self.now)
            srt.append(f"{i}\n{ts(w[0])} --> {ts(end)}\n{plain(sub)}\n")
        (BUILD / f"{name}.srt").write_text("\n".join(srt))
