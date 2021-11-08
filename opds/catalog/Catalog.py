#!/usr/bin/env python
class Catalog:

    """
    Catalog class init
    """

    def __init__(
        self,
        title="Internet Archive OPDS",
        urn="urn:x-internet-archive:bookserver:catalog",
        url="http://bookserver.archive.org/catalog/",
        datestr="1970-01-01T00:00:00Z",
        author="Internet Archive",
        authorUri="http://www.archive.org",
        crawlableUrl=None,
    ):
        self._entries = []
        self._opensearch = None
        self._navigation = None
        self._title = title
        self._urn = urn
        self._url = url
        self._datestr = datestr
        self._author = author
        self._authorUri = authorUri
        self._crawlableUrl = crawlableUrl

    def addEntry(self, entry):
        self._entries.append(entry)

    def addNavigation(self, nav):
        self._navigation = nav

    def addOpenSearch(self, opensearch):
        self._opensearch = opensearch

    def getEntries(self):
        return self._entries

    def render(self):
        raise NotImplemented

    def setProvider(self, provider):
        provider(self)
