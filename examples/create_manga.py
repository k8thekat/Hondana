from __future__ import annotations

import asyncio
from typing import TYPE_CHECKING

import hondana

if TYPE_CHECKING:
    from hondana.types_.common import LocalizedString


async def main() -> None:
    """
    Here we will create a Manga in MangaDex.
    The process is multi-stage, so I will attempt to outline them here.
    """

    # Using the context manager will try and login if credentials are set, or act anonymously if not.
    # Authentication *is* needed for this example.
    async with hondana.Client(client_id="...", client_secret="...") as client:
        # Outline the needed attributes for this manga here
        manga_title: LocalizedString = {"en": "Some neat manga!", "ja": "本棚"}
        original_language = "en"
        status = hondana.MangaStatus.ongoing
        content_rating = hondana.ContentRating.safe

        # Create the manga with them:
        draft_manga = await client.create_manga(
            title=manga_title, original_language=original_language, status=status, content_rating=content_rating
        )

        # This manga is now created in "draft" state. This is outlined more here:
        # https://api.mangadex.org/docs.html#section/Manga-Creation
        # tl;dr it's to remove the spam creations and to ensure there's a cover on the manga... so let's do that now.
        with open("our_cover.png", "rb") as file:  # noqa: PTH123
            cover = file.read()

        # When we upload a cover, we need to attribute it to a manga, so lets use the draft one we created.
        uploaded_cover = await draft_manga.upload_cover(
            cover=cover, volume=None, description="My awesome cover", locale="en"
        )
        print(uploaded_cover)

        # Now that our manga is covered and uploaded, let's submit it for approval with a version of 1:
        submitted_manga = await draft_manga.submit_draft(version=1)
        print(submitted_manga)

        # NOTE: Something to note is that the version of draft MUST match the version of submitted manga during the approval stage.


# we don't log out as exiting the context manager provides a clean exit.
asyncio.run(main())
