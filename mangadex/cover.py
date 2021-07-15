"""
The MIT License (MIT)

Copyright (c) 2021-Present AbstractUmbra

Permission is hereby granted, free of charge, to any person obtaining a
copy of this software and associated documentation files (the "Software"),
to deal in the Software without restriction, including without limitation
the rights to use, copy, modify, merge, publish, distribute, sublicense,
and/or sell copies of the Software, and to permit persons to whom the
Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in
all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS
OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING
FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER
DEALINGS IN THE SOFTWARE.
"""
from __future__ import annotations

import datetime
from typing import TYPE_CHECKING, Literal, Optional


if TYPE_CHECKING:
    from .http import Client
    from .types.cover import GetCoverResponse


__all__ = ("Cover",)


class Cover:
    __slots__ = (
        "_http",
        "_data",
        "id",
        "volume",
        "file_name",
        "description",
        "version",
        "_created_at",
        "_updated_at",
        "relationships",
    )

    def __init__(self, http: Client, payload: GetCoverResponse) -> None:
        self._http = http
        data = payload["data"]
        attributes = data["attributes"]
        self._data = data
        self.id = data["id"]
        self.volume = attributes["volume"]
        self.file_name = attributes["fileName"]
        self.description = attributes["description"]
        self.version = attributes["version"]
        self._created_at = attributes["createdAt"]
        self._updated_at = attributes["updatedAt"]
        self.relationships = payload["relationships"]

    def __repr__(self) -> str:
        return f"<Cover id={self.id} filename={self.file_name}>"

    def __str__(self) -> str:
        return self.file_name

    @property
    def created_at(self) -> datetime.datetime:
        return datetime.datetime.fromisoformat(self._created_at)

    @property
    def updated_at(self) -> datetime.datetime:
        return datetime.datetime.fromisoformat(self._updated_at)

    def url(self, type: Optional[Literal["256", "512"]] = "512") -> Optional[str]:
        parent_manga = None
        for item in self.relationships:
            if item["type"] == "manga":
                parent_manga = item
                break

        if parent_manga is None:
            return

        parent_manga_id = parent_manga["id"]

        if type == "256":
            fmt = ".256.jpg"
        elif type == "512":
            fmt = ".512.jpg"
        else:
            fmt = ""

        return f"https://uploads.mangadex.org/covers/{parent_manga_id}/{self.file_name}{fmt}"
