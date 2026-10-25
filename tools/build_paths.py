"""Locate legacy build outputs or outputs scoped to a book part."""

from pathlib import Path

BUILD = Path(__file__).resolve().parents[1] / "build"


def scene_dir(scene: str, preferred: Path | None = None) -> Path:
    if preferred is not None and (preferred / f"{scene}.marks.json").is_file():
        return preferred
    scoped = list(BUILD.glob(f"*/{scene}.marks.json"))
    if len(scoped) > 1:
        raise ValueError(f"Multiple build folders contain {scene}: {scoped}")
    if scoped:
        return scoped[0].parent
    if (BUILD / f"{scene}.marks.json").is_file():
        return BUILD
    raise FileNotFoundError(f"No marks found for {scene} in {BUILD}")
