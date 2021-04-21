from decouple import config
from .base import *

STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'

MIDDLEWARE += [
    'whitenoise.middleware.WhiteNoiseMiddleware',
]

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': config('MYSQL_DB_NAME'),
        'PASSWORD': config('MYSQL_DB_PASSWORD'),
        'HOST': 'chuky1pilla.mysql.pythonanywhere-services.com',
        'OPTIONS': {
            'init_command': "SET sql_mode='STRICT_TRANS_TABLES'",
            # "init_command": "SET foreign_key_checks = 0;"
        }
    },
}
