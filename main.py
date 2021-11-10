import os

from flask import Flask, send_from_directory, request
from opds import fromdir


CONTENT_BASE_DIR = "/library"
if "CONTENT_BASE_DIR" in os.environ:
    CONTENT_BASE_DIR = os.environ["CONTENT_BASE_DIR"]


app = Flask(__name__)


@app.route("/")
@app.route("/healthz")
def healthz():
    return "ok"


@app.route("/content/<path:path>")
def send_content(path):
    return send_from_directory(CONTENT_BASE_DIR, path)


@app.route("/catalog")
@app.route("/catalog/<path:path>")
def catalog(path=""):
    print(CONTENT_BASE_DIR)
    c = fromdir(request.root_url, request.url, CONTENT_BASE_DIR, path)
    return c.render()
