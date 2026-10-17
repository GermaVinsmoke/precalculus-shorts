"""Shared pieces for the Scientific Notation series."""

from common import *

BR = '<break time="0.2s" />'


class SciScene(NarratedScene):
    TOPIC = "SCIENTIFIC NOTATION"
    WATERMARK = True


class DecimalRow:
    """Digits on evenly spaced slots with a decimal point that hops between them.

    The point sits at position p = k + 0.5 (between slot k and k + 1). When it hops
    into empty territory, a 0 appears there, exactly like padding a number with zeros.
    """

    def __init__(self, n_slots, fs=72, center=MATH, gap=0.14):
        probe = tex("0", fs=fs)
        self.fs = fs
        self.slot = probe.width + gap
        self.digit_h = probe.height
        self.x0 = center[0] - (n_slots - 1) / 2 * self.slot
        self.y = center[1]
        self.cells = {}
        r = max(0.055 * fs / 72, 0.045)
        self.dot = Dot(radius=r, color=EXP_C)
        self.pos = None

    def x(self, i):
        return self.x0 + i * self.slot

    def put(self, i, ch, color=INK):
        m = tex(ch, fs=self.fs, color=color).move_to([self.x(i), self.y, 0])
        self.cells[i] = m
        return m

    def write(self, start, digits, color=INK):
        return VGroup(*[self.put(start + j, ch, color) for j, ch in enumerate(digits)])

    def dot_point(self, p):
        return np.array([self.x0 + p * self.slot, self.y - self.digit_h / 2 + self.dot.radius, 0])

    def set_dot(self, p):
        self.pos = p
        self.dot.move_to(self.dot_point(p))
        return self.dot

    def digits(self):
        return VGroup(*[self.cells[k] for k in sorted(self.cells)])

    def hops(self, steps, step_time=0.24):
        """Animations moving the point `steps` slots (negative = left), one hop at a time."""
        anims = []
        d = 1 if steps > 0 else -1
        for _ in range(abs(steps)):
            new = self.pos + d
            # an arc over the digit; the slot left in front of the point gets a 0 if empty
            path = ArcBetweenPoints(self.dot_point(self.pos), self.dot_point(new), angle=-PI * 0.75 * d)
            group = [MoveAlongPath(self.dot, path)]
            front = int(new - 0.5)
            if front not in self.cells:
                group.append(FadeIn(self.put(front, "0"), scale=0.5))
            anims.append(AnimationGroup(*group, run_time=step_time))
            self.pos = new
        return Succession(*anims)

    def exponent_counter(self, k0, base_pos, fs=SMALL_FS, at=None):
        """'× 10^k' whose k follows the point: the value of row × 10^k never changes."""
        times_ten = auto(tex(r"\times", "10", fs=fs), digits=False)
        times_ten[1].set_color(BASE_C)
        exp = Integer(k0, font_size=fs * 0.7, color=EXP_C)
        start_x = self.dot_point(base_pos)[0]

        def follow(m):
            k = k0 - round((self.dot.get_x() - start_x) / self.slot)
            if m.get_value() != k:
                m.set_value(k)
                m.set_color(EXP_C)
            m.next_to(times_ten[1], UR, buff=0.04).shift(DOWN * 0.18 * fs / SMALL_FS)

        g = VGroup(times_ten, exp)
        times_ten.move_to(at if at is not None else [CX, self.y - 1.2, 0])
        follow(exp)
        exp.add_updater(follow)
        return g
