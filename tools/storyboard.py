"""Build a storyboard sheet from a rendered video and its caption marks.

One frame per caption beat, grabbed just before the next caption appears
(so each frame shows the finished state of that beat).

usage: storyboard.py <SceneName> <video.mp4>
"""

import json
import subprocess
import sys
import textwrap
from pathlib import Path

from PIL import Image, ImageDraw, ImageFont

ROOT = Path(__file__).resolve().parents[1]
BUILD = ROOT / "build"

scene, video = sys.argv[1], Path(sys.argv[2])
data = json.loads((BUILD / f"{scene}.marks.json").read_text())
marks, duration = data["marks"], data["duration"]
snaps = data.get("snaps", [])
ends = [m["t"] for m in marks[1:]] + [duration]

out_dir = BUILD / "storyboard" / scene
out_dir.mkdir(parents=True, exist_ok=True)
for old in out_dir.glob("*.png"):
    old.unlink()
frames = []
for i, (m, end) in enumerate(zip(marks, ends), 1):
    inside = [s for s in snaps if m["t"] < s <= end]
    t = (inside[-1] if inside else end) - 0.04
    p = out_dir / f"{i:02d}.png"
    subprocess.run(
        ["ffmpeg", "-y", "-loglevel", "error", "-ss", f"{t:.3f}", "-i", str(video),
         "-frames:v", "1", str(p)],
        check=True,
    )
    frames.append((p, m, t))

cols = 4
tw = 360
th = int(tw * 16 / 9)
pad = 28
text_h = 120
rows = (len(frames) + cols - 1) // cols
W = cols * tw + (cols + 1) * pad
H = rows * (th + text_h) + (rows + 1) * pad + 90
sheet = Image.new("RGB", (W, H), (18, 20, 26))
d = ImageDraw.Draw(sheet)
try:
    font = ImageFont.truetype("/System/Library/Fonts/Avenir Next.ttc", 22)
    title_font = ImageFont.truetype("/System/Library/Fonts/Avenir Next.ttc", 40)
except OSError:
    font = title_font = ImageFont.load_default()
d.text((pad, 24), f"{scene}  ·  {duration:.1f}s  ·  {len(frames)} beats", fill=(236, 239, 244), font=title_font)
for i, (p, m, t) in enumerate(frames):
    r, c = divmod(i, cols)
    x = pad + c * (tw + pad)
    y = 90 + pad + r * (th + text_h + pad)
    sheet.paste(Image.open(p).convert("RGB").resize((tw, th), Image.LANCZOS), (x, y))
    d.rectangle([x, y, x + tw - 1, y + th - 1], outline=(50, 56, 72))
    caption = f"{i + 1:02d} · {m['t']:.1f}s  {m['caption']}"
    for j, line in enumerate(textwrap.wrap(caption, 32)[:4]):
        d.text((x, y + th + 8 + j * 27), line, fill=(200, 205, 215), font=font)
sheet_path = BUILD / "storyboard" / f"{scene}_storyboard.png"
sheet.save(sheet_path)
print(sheet_path)
