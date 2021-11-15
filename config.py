import os
from werkzeug.security import generate_password_hash

CONTENT_BASE_DIR = os.getenv("CONTENT_BASE_DIR", "/library")

TEENYOPDS_ADMIN_PASSWORD = os.getenv("TEENYOPDS_ADMIN_PASSWORD", None)
users = {}
if TEENYOPDS_ADMIN_PASSWORD:
    users = {
        "admin": generate_password_hash(TEENYOPDS_ADMIN_PASSWORD),
    }
else:
    print(
        "WANRNING: admin password not configured - catalog will be exposed was public"
    )
