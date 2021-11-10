class Entry(object):
    valid_keys = (
        "id",
        "url",
        "title",
        "content",
        "downloadsPerMonth",
        "updated",
        "identifier",
        "date",
        "rights",
        "summary",
        "dcterms_source",
        "provider",
        "publishers",
        "contributors",
        "languages",
        "subjects",
        "oai_updatedates",
        "authors",
        "formats",
        "links",
    )

    required_keys = ("id", "title", "links")

    def validate(self, key, value):
        if key not in Entry.valid_keys:
            raise KeyError("invalid key in opds.catalog.Entry: %s" % (key))

    def __init__(self, **kwargs):
        for key, val in kwargs.items():
            self.validate(key, val)

        for req_key in Entry.required_keys:
            if not req_key in kwargs:
                raise KeyError("required key %s not supplied for Entry!" % (req_key))

        self.id = kwargs["id"]
        self.title = kwargs["title"]
        self.links = kwargs["links"]
        self._data = kwargs

    def get(self, key):
        return self._data.get(key, None)

    def set(self, key, value):
        self.validate(key, value)
        self._data[key] = value
