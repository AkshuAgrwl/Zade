from __future__ import annotations
from typing import TypedDict, TYPE_CHECKING

if TYPE_CHECKING:
    from pathlib import Path


class TreeContainer(TypedDict):
    dir: Path
    files: list[Path]
    subdir: list[TreeContainer]
