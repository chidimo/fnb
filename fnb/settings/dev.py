from decouple import config
from .base import *

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql",
        "NAME": config("POSTGRES_USER"),
        "USER": config("POSTGRES_USER"),
        "HOST": config("POSTGRES_HOST"),
        "PASSWORD": config("POSTGRES_PASSWORD"),
        "PORT": config("POSTGRES_PORT"),
    }
}
