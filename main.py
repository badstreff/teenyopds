import os
import re
import uuid

from urllib.parse import quote

from flask import Flask, send_from_directory, request, render_template
from pprint import pprint

import metadata
from catalog import Catalog, fromdir


CONTENT_BASE_DIR = "/mnt/c/Users/adamf/Google Drive/Library"
ROOT_URL = "http://192.168.88.254:5000"


app = Flask(__name__, template_folder="templates")


@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"


@app.route("/content/<path:path>")
def send_content(path):
    return send_from_directory(CONTENT_BASE_DIR, path)


# @user.route('/<user_id>', defaults={'username': None})
# @user.route('/<user_id>/<username>')


@app.route("/catalog")
@app.route("/catalog/<path:path>")
def catalog(path=""):
    # return Catalog(os.path.join(CONTENT_BASE_DIR, path)).render()
    # content_path = os.path.join(CONTENT_BASE_DIR, path)
    # content_base_url = request.root_url + "/content/" + path
    # c = catalog.fromdir(request.root_url, content_base_url, content_path)
    # return c.render()
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
    )


def populate_catalog(catalog, content_path):
    populate_catalog_files(catalog, content_path)
    populate_catalog_subcatalogs(catalog, content_path)


def populate_catalog_subcatalogs(catalog, content_path):
    onlydirs = [
        f
        for f in os.listdir(content_path)
        if not os.path.isfile(os.path.join(content_path, f))
    ]
    print(onlydirs)
    for dirname in onlydirs:
        c = Catalog(
            dirname,
            root_url=catalog.root_url,
            url=catalog.url + "/" + quote(dirname),
            parent_catalog=catalog,
        )
        catalog.add_subcatalog(c)


def populate_catalog_files(catalog, content_path):
    onlyfiles = [
        f
        for f in os.listdir(content_path)
        if os.path.isfile(os.path.join(content_path, f))
    ]
    for filename in onlyfiles:
        fn = quote(os.path.join(content_path, filename)[len(CONTENT_BASE_DIR) :])
        catalog.add_entry(
            uuid=str(uuid.uuid4()),
            title=filename.split(".")[0],
            urls={mimetype(filename): f"{ROOT_URL}/content/{fn}"},
        )


def mimetype(path):
    extension = path.split(".")[-1].lower()
    if extension == "pdf":
        return "application/pdf"
    elif extension == "epub":
        return "application/epub"
    else:
        return "application/unknown"


if __name__ == "__main__":

    f = []
    BASE_DIR = "/mnt/c/Users/adamf/Google Drive/Library"
    for (dirpath, dirnames, filenames) in os.walk(BASE_DIR):
        for filename in filenames:
            f.append(quote(os.path.join(dirpath, filename)[40:]))
    pprint(f)
    for filename in f:
        isbn = re.search("(\d{13}|\d{10})", filename, re.IGNORECASE)
        if isbn:
            print(isbn.group(1))
            pprint(metadata.fromisbn(isbn.group(1)))
