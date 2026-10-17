"""Collect generated voiceover scripts and subtitles into one review document.

usage: export_scripts.py <out.md> <Scene> [<Scene> ...]
"""

import re
import sys
from pathlib import Path

BUILD = Path(__file__).resolve().parents[1] / "build"
out, scenes = Path(sys.argv[1]), sys.argv[2:]
doc = ["# Laws of Exponents — voiceover & subtitles (generated from the scenes)\n",
       "Paste each voiceover block into ElevenLabs as one generation. "
       "`<break>` tags work on Multilingual v2 / Turbo / Flash; on Eleven v3 replace them with \"…\".\n",
       "Subtitle timings are estimates (150 words/min) and will be re-synced to the real audio.\n"]
for sc in scenes:
    vo = (BUILD / f"{sc}.voiceover.txt").read_text().strip()
    srt = (BUILD / f"{sc}.srt").read_text().strip().split("\n\n")
    words = len(re.sub(r"<[^>]+>", " ", vo).split())
    doc.append(f"\n---\n\n## {sc}  ·  {words} words\n\n### Voiceover\n\n```text\n{vo}\n```\n\n### Subtitles\n")
    doc.append("| Time | Subtitle |\n|---|---|")
    for block in srt:
        lines = block.split("\n")
        start = lines[1].split(" --> ")[0][3:8]
        doc.append(f"| {start} | {' '.join(lines[2:])} |")
out.write_text("\n".join(doc) + "\n")
print(out)
