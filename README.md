<div align="center">
    <h1>Hondana 『本棚』</h1>
    <p>Hondana is the Japanese word for "bookshelf".</p>
    <a href='https://hondana.readthedocs.io/en/latest/?badge=latest'>
        <img src='https://readthedocs.org/projects/hondana/badge/?version=latest' alt='Documentation Status' />
    </a>
    <a href='https://github.com/AbstractUmbra/Hondana/actions/workflows/build.yaml'>
        <img src='https://github.com/AbstractUmbra/Hondana/workflows/Build/badge.svg' alt='Build status' />
    </a>
    <a href='https://github.com/AbstractUmbra/Hondana/actions/workflows/lint.yaml'>
        <img src='https://github.com/AbstractUmbra/Hondana/workflows/Lint/badge.svg' alt='Build status' />
    </a>
</div>
<div align="center">
    <a href='https://api.mangadex.org/'>
        <img src='https://img.shields.io/website?down_color=red&down_message=offline&label=API%20Status&logo=MangaDex%20API&up_color=lime&up_message=online&url=https%3A%2F%2Fapi.mangadex.org%2Fping' alt='API Status'/>
    </a>
</div>
<br>

A lightweight and asynchronous wrapper around the [MangaDex v5 API](https://api.mangadex.org/docs.html).

## Features
**NOTE** This library is still in development, I will list off the API methods and their progress here:

| Feature          | Implemented? | Notes                                              |
| ---------------- | ------------ | -------------------------------------------------- |
| Chapter Upload   | [ ]          | Soon:tm:                                           |
| Manga            | [x]          | Done. (pending tests on some endpoints)            |
| Cover            | [x]          | Done. (pending tests on some endpoints)            |
| Author           | [/]          | Soon:tm:                                           |
| Search           | [x]          | Done.                                              |
| Auth             | [x]          | Authentication is done per request, token handled. |
| Scanlation Group | [ ]          | Soon:tm:                                           |
| Feed             | [ ]          | Soon:tm:                                           |
| CustomList       | [ ]          | Soon:tm:                                           |
| AtHome           | [x]          | Done.                                              |
| Legacy           | [x]          | Done.                                              |
| Infrastructure   | [x]          | Done.                                              |
| Upload           | [ ]          | Soon:tm:                                           |
| Account          | [x]          | Done.                                              |
| User             | [x]          | Done. (pending tests on some endpoints)            |
| Chapter          | [x]          | Done. (pending tests on some endpoints)            |
| Report           | [ ]          | Soon:tm:                                           |
| Ratelimits?      | [ ]          | Not part of the API spec but might be handy.       |


### In Progress: CustomList
| Endpoint                           | Implemented? | Notes    |
| ---------------------------------- | ------------ | -------- |
| Create CustomList                  | [ ]          | Soon:tm: |
| Get CustomList                     | [ ]          | Soon:tm: |
| Update CustomList                  | [ ]          | Soon:tm: |
| Delete CustomList                  | [ ]          | Soon:tm: |
| Add Manga in CustomList            | [ ]          | Soon:tm: |
| Remove Manga in CustomList         | [ ]          | Soon:tm: |
| Get logged in User CustomList list | [ ]          | Soon:tm: |
| Get User's CustomList list         | [ ]          | Soon:tm: |
| CustomList Manga feed              | [ ]          | Soon:tm: |
#### To Test: Manga
| Endpoint     | Tested? | Notes                              |
| ------------ | ------- | ---------------------------------- |
| Create Manga | [ ]     | Done. Unsure if I can test this... |
| Update Manga | [ ]     | Done. Unsure if I can test this... |
| Delete Manga | [ ]     | Done. Unsure if I can test this... |


#### To Test: Chapter
| Endpoint       | Tested? | Notes                               |
| -------------- | ------- | ----------------------------------- |
| Update Chapter | [ ]     | Done. Unsure if I can test this ... |
| Delete Chapter | [ ]     | Done. Unsure if I can test this ... |


#### To Test: Cover
| Endpoint   | Tested? | Notes                              |
| ---------- | ------- | ---------------------------------- |
| Edit Cover | [ ]     | Done. Unsure if I can test this... |


#### To Test: User

| Endpoint              | Tested? | Notes                              |
| --------------------- | ------- | ---------------------------------- |
| User List             | [ ]     | Done. Unsure if I can test this... |
| Get User              | [ ]     | Done.                              |
| Delete User           | [ ]     | Done. Unsure if I can test this... |
| Approve User Deletion | [ ]     | Done. Unsure if I can test this... |

## Examples
Please take a look at the [examples](../Hondana/examples/) directory for working examples.

**NOTE**: More examples will follow as the library is developed.

### API caveats to note

- There are no API endpoints for Artist. Currently, if you query a manga without the `"artist"` query includes then you will not receive artist data.
- The tags are locally cached since you **must** pass UUIDs to the api (and I do not think you're going to memorise those), there's a convenience method for updating the local cache as `Client.update_tags`
  - I have added [an example](../Hondana/../hondana/examples/updating_local_tags.py) on how to do the above.
