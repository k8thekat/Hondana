from __future__ import annotations

import json
import pathlib
from copy import deepcopy
from typing import TYPE_CHECKING

from hondana.custom_list import CustomList
from hondana.http import HTTPClient
from hondana.utils import relationship_finder, to_snake_case


if TYPE_CHECKING:
    from hondana.types_.custom_list import GetSingleCustomListResponse

PATH: pathlib.Path = pathlib.Path(__file__).parent / "payloads" / "custom_list.json"

PAYLOAD: GetSingleCustomListResponse = json.load(open(PATH, "r"))
HTTP: HTTPClient = object()  # type: ignore # this is just for test purposes.


def clone_custom_list() -> CustomList:
    t = deepcopy(PAYLOAD)
    return CustomList(HTTP, t["data"])


class TestCustomList:
    def test_id(self):
        custom_list = clone_custom_list()

        assert custom_list.id == PAYLOAD["data"]["id"]

    def test_attributes(self):
        custom_list = clone_custom_list()
        for item in PAYLOAD["data"]["attributes"]:
            getattr(custom_list, to_snake_case(item))

    def test_owner(self):
        custom_list = clone_custom_list()

        assert custom_list.owner is not None

        owner_rel = relationship_finder(PAYLOAD["data"]["relationships"], "user", limit=1)
        assert owner_rel is not None

        assert custom_list.owner.id == owner_rel["id"]

    def test_mangas(self):
        custom_list = clone_custom_list()

        assert custom_list.manga is not None

        manga_rels = relationship_finder(PAYLOAD["data"]["relationships"], "manga", limit=None)
        assert manga_rels is not None

        assert len(custom_list.manga) == len(manga_rels)
