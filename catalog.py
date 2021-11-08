from os.path import basename


class Catalog(object):
    def __init__(
        self,
        title,
        packager_name=None,
        author_name=None,
        author_uri=None,
        root_url=None,
        url=None,
    ):
        """Generates a catalog for the given passed data.
        Required parameters:
        :param title:
            The title of the catalog in human-readable form.
        Optional parameters:
        :param updated:
            A python date object describing when the OPDS has been
            generated (defaults to now).
        :param author_name:
            The name of the author.
        :param author_uri:
            An URI to retrieve more information about the author.
        :param packager_name:
            The name of the packager (most probably the entity running this
            script).
        """
        self.title = title
        self.packager_name = packager_name
        self.author_name = author_name
        self.author_uri = author_uri
        self.entries = []
        self.subcatalogs = []
        self.root_url = root_url
        self.url = url

    def add_subcatalog(self, c):
        self.subcatalogs.append(c)

    def add_entry(
        self,
        title,
        urls,
        issued=None,
        uuid=None,
        summary=None,
        author_name=None,
        author_uri=None,
        checksum=None,
        file_size=None,
        tags=(),
        requires_mimetypes=(),
        image=None,
        thumbnail=None,
        updated=None,
        rights=(),
        languages=("eng",),
        checksum_algorithm="sha256",
    ):
        """Adds an entry to the catalog.
        Required parameters:
        :param id:
            A human readable identifier for the resource. It's the same
            across versions (should be stable across time).
            MUST be prefixed by the packager name.
        :param title:
            The title of the resource.
        :param issued:
            A python datetime object describing when the resource was issued by
            its producer.
        :param urls:
            A dictionary with MimeTypes as keys and URLs as values.
        Optional keys:
        :param uuid:
            A unique identifier for the resource. (defaults to a generated UUID
            if not specified).
        :param summary:
            The description of the resource.
        :param author_name:
            The name of the author.
        :param author_uri:
            An URI to retrieve more information about the author.
        :param languages:
            A list of ISO-639-3 (3 characters) languages the resource uses.
        :param checksum:
            The checksum of the resource (by default a sha2566 value should be
            provided)
        :param checksum_algorithm:
            The checksum algorithm to use (defaults to sha256).
        :param file_size:
            The size of the file, in bytes.
        :param tags:
            A list of tags (specified as text values)
        :param requires_mimetypes:
            A list of mimetypes that if not supported will prevent this
            content from being played.
        :param image:
            An URI to an image (large) representation of the content.
        :param thumbnail:
            An URI to a thumbnail (small) representation of the content.
        :param updated:
            A python datetime object describing when the resource was last
            updated by its producer (defaults to the current date)
        :param rights:
            A list of rights associated with the content.
        """
        self.entries.append(
            dict(
                id=id,
                uuid=uuid,
                title=title,
                issued=issued,
                updated=updated or issued,
                rights=rights,
                urls=urls,
                summary=summary,
                author_name=author_name,
                author_uri=author_uri,
                checksum=checksum,
                file_size=file_size,
                tags=tags,
                requires_mimetypes=requires_mimetypes,
                image=image,
                thumbnail=thumbnail,
                languages=languages,
                checksum_algorithm=checksum_algorithm,
            )
        )


# def fromdir(path):
def fromdir(root_url, content_base_url, path):
    c = Catalog(basename(path), root_url=root_url, url="???")
    return c

    if path:
        c = Catalog(
            CONTENT_BASE_DIR.split("/")[-1],
            root_url=ROOT_URL + "/catalog",
            url=ROOT_URL + "/catalog/" + path,
        )
        populate_catalog(c, os.path.join(CONTENT_BASE_DIR, path))
    else:
        c = Catalog(
            CONTENT_BASE_DIR.split("/")[-1],
            root_url=ROOT_URL + "/catalog",
            url=ROOT_URL + "/catalog",
        )
        populate_catalog(c, CONTENT_BASE_DIR)
    return render_template(
        "catalog.opds.jinja2",
        catalog=c,
        uuid=None,
        updated=None,
        url=c.url,
        root_url=c.url,
    )
