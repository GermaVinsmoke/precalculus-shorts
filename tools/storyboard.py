"""Build a storyboard sheet from a rendered video and its caption marks.

One frame per caption beat, grabbed just before the next caption appears
(so each frame shows the finished state of that beat).

usage: storyboard.py <SceneName> <video.mp4>
"""

import json
import subprocess
import sys
import tempfile
import textwrap
from pathlib import Path

from PIL import Image, ImageDraw, ImageFont

from build_paths import BUILD, scene_dir

scene, video = sys.argv[1], Path(sys.argv[2])
build_dir = scene_dir(scene, video.parent)
data = json.loads((build_dir / f"{scene}.marks.json").read_text())
marks, duration = data["marks"], data["duration"]
snaps = data.get("snaps", [])
ends = [m["t"] for m in marks[1:]] + [duration]

tmp = tempfile.TemporaryDirectory(prefix=f"{scene}-storyboard-")
out_dir = Path(tmp.name)
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
sheet_path = (build_dir if build_dir != BUILD else BUILD / "storyboard") / f"{scene}_storyboard.png"
sheet_path.parent.mkdir(parents=True, exist_ok=True)
sheet.save(sheet_path)
tmp.cleanup()
print(sheet_path)
