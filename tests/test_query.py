from __future__ import annotations

from hondana.query import (
    ArtistIncludes,
    AuthorIncludes,
    AuthorListOrderQuery,
    ChapterIncludes,
    CoverArtListOrderQuery,
    CoverIncludes,
    CustomListIncludes,
    FeedOrderQuery,
    MangaDraftListOrderQuery,
    MangaIncludes,
    MangaListOrderQuery,
    Order,
    ReportListOrderQuery,
    ScanlatorGroupIncludes,
    ScanlatorGroupListOrderQuery,
    UserListOrderQuery,
)


class TestOrderQuery:
    def test_author_list_order_query(self) -> None:
        query = AuthorListOrderQuery(name=Order.descending)
        assert query.to_dict() == {"name": "desc"}

    def test_cover_art_order_query(self) -> None:
        query = CoverArtListOrderQuery(created_at=Order.ascending)
        assert query.to_dict() == {"createdAt": "asc"}

        query = CoverArtListOrderQuery(updated_at=Order.descending)
        assert query.to_dict() == {"updatedAt": "desc"}

        query = CoverArtListOrderQuery(volume=Order.ascending)
        assert query.to_dict() == {"volume": "asc"}

    def test_feed_order_query(self) -> None:
        query = FeedOrderQuery(created_at=Order.ascending)
        assert query.to_dict() == {"createdAt": "asc"}

        query = FeedOrderQuery(updated_at=Order.ascending)
        assert query.to_dict() == {"updatedAt": "asc"}

        query = FeedOrderQuery(publish_at=Order.ascending)
        assert query.to_dict() == {"publishAt": "asc"}

        query = FeedOrderQuery(readable_at=Order.ascending)
        assert query.to_dict() == {"readableAt": "asc"}

        query = FeedOrderQuery(volume=Order.ascending)
        assert query.to_dict() == {"volume": "asc"}

        query = FeedOrderQuery(chapter=Order.ascending)
        assert query.to_dict() == {"chapter": "asc"}

    def test_manga_draft_list_order_query(self) -> None:
        query = MangaDraftListOrderQuery(title=Order.descending)
        assert query.to_dict() == {"title": "desc"}

        query = MangaDraftListOrderQuery(year=Order.descending)
        assert query.to_dict() == {"year": "desc"}

        query = MangaDraftListOrderQuery(created_at=Order.descending)
        assert query.to_dict() == {"createdAt": "desc"}

        query = MangaDraftListOrderQuery(updated_at=Order.descending)
        assert query.to_dict() == {"updatedAt": "desc"}

    def test_manga_list_order_query(self) -> None:
        query = MangaListOrderQuery(created_at=Order.descending)
        assert query.to_dict() == {"createdAt": "desc"}

        query = MangaListOrderQuery(title=Order.ascending)
        assert query.to_dict() == {"title": "asc"}

    def test_report_list_order_query(self) -> None:
        query = ReportListOrderQuery(created_at=Order.descending)
        assert query.to_dict() == {"createdAt": "desc"}

    def test_scanlator_group_list_order_query(self) -> None:
        query = ScanlatorGroupListOrderQuery(name=Order.descending)
        assert query.to_dict() == {"name": "desc"}

        query = ScanlatorGroupListOrderQuery(created_at=Order.descending)
        assert query.to_dict() == {"createdAt": "desc"}

        query = ScanlatorGroupListOrderQuery(updated_at=Order.descending)
        assert query.to_dict() == {"updatedAt": "desc"}

        query = ScanlatorGroupListOrderQuery(bookmarked_count=Order.descending)
        assert query.to_dict() == {"bookmarkedCount": "desc"}

        query = ScanlatorGroupListOrderQuery(relevance=Order.descending)
        assert query.to_dict() == {"relevance": "desc"}

    def test_user_list_order_query(self) -> None:
        query = UserListOrderQuery(username=Order.descending)
        assert query.to_dict() == {"username": "desc"}


class TestIncludes:
    def test_artist_includes(self) -> None:
        includes = ArtistIncludes(manga=False)
        assert includes.to_query() == []

        includes = ArtistIncludes(manga=True)
        assert includes.to_query() == ["manga"]

        includes = ArtistIncludes()
        assert includes.to_query() == ArtistIncludes.all().to_query()

    def test_author_includes(self) -> None:
        includes = AuthorIncludes(manga=False)
        assert includes.to_query() == []

        includes = AuthorIncludes(manga=True)
        assert includes.to_query() == ["manga"]

        includes = AuthorIncludes()
        assert includes.to_query() == AuthorIncludes.all().to_query()

    def test_chapter_includes(self) -> None:
        includes = ChapterIncludes(manga=False, user=False, scanlation_group=False)
        assert includes.to_query() == []

        includes = ChapterIncludes(manga=True, user=False, scanlation_group=False)
        assert includes.to_query() == ["manga"]

        includes = ChapterIncludes(manga=True, user=False, scanlation_group=True)
        assert includes.to_query() == ["manga", "scanlation_group"]

        includes = ChapterIncludes()
        assert includes.to_query() == ChapterIncludes.all().to_query()

    def test_cover_includes(self) -> None:
        includes = CoverIncludes.none()
        assert includes.to_query() == []

        includes = CoverIncludes(manga=False, user=False)
        assert includes.to_query() == []

        includes = CoverIncludes(manga=True, user=False)
        assert includes.to_query() == ["manga"]

        includes = CoverIncludes()
        assert includes.to_query() == CoverIncludes.all().to_query()

    def test_custom_list_includes(self) -> None:
        includes = CustomListIncludes.none()
        assert includes.to_query() == []

        includes = CustomListIncludes()
        assert includes.to_query() == ["manga", "owner", "user"]

        includes = CustomListIncludes(manga=False)
        assert includes.to_query() == ["owner", "user"]

    def test_manga_includes(self) -> None:
        includes = MangaIncludes()
        assert includes.to_query() == ["artist", "author", "cover_art", "manga"]

        includes = MangaIncludes.none()
        assert includes.to_query() == []

        includes = MangaIncludes(artist=False)
        assert includes.to_query() == ["author", "cover_art", "manga"]

    def test_scanlator_group_includes(self) -> None:
        includes = ScanlatorGroupIncludes.none()
        assert includes.to_query() == []

        includes = ScanlatorGroupIncludes()
        assert includes.to_query() == ["leader", "member"]

        includes = ScanlatorGroupIncludes(leader=False)
        assert includes.to_query() == ["member"]
