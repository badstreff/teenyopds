# teenyopds

Small flask based opds catalog designed to serve a directory via OPDS, it has currently only been verified to work with KyBook 3 on iOS but should work with other OPDS compatible ereaders.

## Quickstart

`docker build . -t teenyopds`

`docker run -p 5000:5000 -v /path/to/content:/library teenyopds`

Navigate to `http://localhost:5000/catalog` to view opds catalog

## Configuration

Currently only a single option can be set via an environment variable `CONTENT_BASE_DIR` to server an alternative directory

## Other endpoints

`/heathz` will return "ok" if the service is up and running

## Supported Readers

Any reader that supports OPDS should work, however the following have been verified to work/not work

| App                                                                                                   | Android | iOS |
| ----------------------------------------------------------------------------------------------------- | ------- | --- |
| [KyBook 3](http://kybook-reader.com/)                                                                 | -       | ✔️  |
| Aldiko Next                                                                                           | ❌      | ✔️  |
| [PocketBook](https://pocketbook.ch/en-ch/app)                                                         | -       | ✔️  |
| [Moon+ Reader](https://play.google.com/store/apps/details?id=com.flyersoft.moonreader&hl=en_US&gl=US) | ✔️      | -   |

## TODO

Implement simple searching

Metadata lookup based either filename or some type of metadata file populated by the user, one idea is to just have the users put the ISBN in the filename

Support basic auth

I believe OPDS supports content compression however kybook doesn't like it so it's not implemented
