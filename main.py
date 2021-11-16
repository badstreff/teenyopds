from flask import Flask, send_from_directory, request
from flask_httpauth import HTTPBasicAuth
from werkzeug.security import check_password_hash
from gevent.pywsgi import WSGIServer

from opds import fromdir
import config

app = Flask(__name__, static_url_path="", static_folder="static")
auth = HTTPBasicAuth()


@auth.verify_password
def verify_password(username, password):
    if not config.TEENYOPDS_ADMIN_PASSWORD:
        return True
    elif username in config.users and check_password_hash(
        config.users.get(username), password
    ):
        return username


@app.route("/")
@app.route("/healthz")
def healthz():
    return "ok"


@app.route("/content/<path:path>")
@auth.login_required
def send_content(path):
    return send_from_directory(config.CONTENT_BASE_DIR, path)


@app.route("/catalog")
@app.route("/catalog/<path:path>")
@auth.login_required
def catalog(path=""):
    c = fromdir(request.root_url, request.url, config.CONTENT_BASE_DIR, path)
    return c.render()


if __name__ == "__main__":
    http_server = WSGIServer(("", 5000), app)
    http_server.serve_forever()
