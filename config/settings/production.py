from config.settings.base import *  # noqa
import os

DEBUG = False

ALLOWED_HOSTS = os.environ.get("ALLOWED_HOSTS", "127.0.0.1").split(",")


DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.mysql",
        "NAME": os.environ.get("DB_NAME", None),
        "USER": os.environ.get("DB_USER", None),
        "PASSWORD": os.environ.get("DB_PASSWORD", None),
        "HOST": os.environ.get("DB_HOST", None),
        "PORT": os.environ.get("DB_PORT", "3306"),
        "OPTIONS": {
            "charset": "utf8mb4",
        },
    }
}
