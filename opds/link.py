class Link(object):
    valid_keys = ("href", "type", "rel", "price", "currencycode", "formats")
    required_keys = ("href", "type", "rel")

    def validate(self, key, value):
        if key not in Link.valid_keys:
            raise KeyError("invalid key in opds.Link: %s" % (key))

    def __init__(self, **kwargs):
        for key, val in kwargs.items():
            self.validate(key, val)

        for req_key in Link.required_keys:
            if not req_key in kwargs:
                raise KeyError("required key %s not supplied for Link!" % (req_key))

        self.href = kwargs["href"]
        self.type = kwargs["type"]
        self.rel = kwargs["rel"]
        self._data = kwargs

    def get(self, key):
        return self._data.get(key, None)

    def set(self, key, value):
        self.validate(key, value)
        self._data[key] = value
