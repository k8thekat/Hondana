<h1 align="center">mangadex.py</h1>

<div align="center">
    <a href='https://mangadexpy.readthedocs.io/en/latest/?badge=latest'>
        <img src='https://readthedocs.org/projects/mangadexpy/badge/?version=latest' alt='Documentation Status' />
    </a>
    <a href='https://github.com/AbstractUmbra/mangadex.py/actions/workflows/build.yaml'>
        <img src='https://github.com/AbstractUmbra/mystbin.py/workflows/Build/badge.svg' alt='Build status' />
    </a>
    <a href='https://github.com/AbstractUmbra/mangadex.py/actions/workflows/lint.yaml'>
        <img src='https://github.com/AbstractUmbra/mangadex.py/workflows/Lint/badge.svg' alt='Build status' />
    </a>
</div>

<br>

A lightweight and asynchronous wrapper around the [MangaDex v5 API](https://api.mangadex.org/docs.html).

<br>

## Features
**NOTE** This library is still in development, I will list off the API methods and their progress here:

| Feature          | Implemented? | Notes                                              |
| ---------------- | ------------ | -------------------------------------------------- |
| Chapter Upload   | [ ]          | Soon:tm:                                           |
| Manga            | [/]          | Partially implemented.                             |
| Cover            | [ ]          | Soon:tm:                                           |
| Author           | [ ]          | Soon:tm:                                           |
| Search           | [ ]          | Soon:tm:                                           |
| Auth             | [x]          | Authentication is done per request, token handled. |
| Scanlation Group | [ ]          | Soon:tm:                                           |
| Feed             | [ ]          | Soon:tm:                                           |
| CustomList       | [ ]          | Soon:tm:                                           |
| AtHome           | [ ]          | Soon:tm:                                           |
| Legacy           | [ ]          | Soon:tm:                                           |
| Infrastructure   | [ ]          | Soon:tm:                                           |
| Upload           | [ ]          | Soon:tm:                                           |
| Account          | [ ]          | Soon:tm:                                           |
| User             | [ ]          | Soon:tm:                                           |
| Chapter          | [ ]          | Soon:tm:                                           |
| Report           | [ ]          | Soon:tm:                                           |
| Ratelimits?      | [ ]          | Not part of the API spec but might be handy.       |


## Examples
Please take a look at the [examples](../mangadex.py/mangadex/examples/) directory for working examples.

**NOTE**: More examples will follow as the library is developed.

### API caveats to note

- There are no API endpoints for Artist. Currently if you query a manga without the `"artist"` query includes then you will not recieve artist data.
- The tags are locally cached since you **must** pass UUIDs to the api (and I do not think you're going to memorise those), there's a convenience method for updating the local cache as `Client.update_tags`
