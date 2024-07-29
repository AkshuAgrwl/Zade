from __future__ import annotations
from typing import Literal, TypedDict, TYPE_CHECKING

if TYPE_CHECKING:
    from pathlib import Path


class TreeContainer(TypedDict):
    dir: Path
    files: list[Path]
    subdir: list[TreeContainer]


HTTP_METHODS = Literal[
    "GET",
    "POST",
    "PUT",
    "PATCH",
    "DELETE",
    "OPTIONS",
    "HEAD",
    "TRACE",
]
