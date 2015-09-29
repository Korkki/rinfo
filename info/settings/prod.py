from urllib.parse import urlparse
import dj_database_url
from .base import *

DEBUG = False

DATABASES = {
    'default': dj_database_url.config()
}

redis_url = urlparse(os.environ.get('REDIS_URL'))
CACHES = {
    "default": {
        "BACKEND": "redis_cache.RedisCache",
        "LOCATION": "{0}:{1}".format(redis_url.hostname, redis_url.port),
        "OPTIONS": {
            "PASSWORD": redis_url.password,
            "DB": 0,
        }
    }
}

SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')

ALLOWED_HOSTS = ['*']

STATICFILES_STORAGE = 'whitenoise.django.GzipManifestStaticFilesStorage'

SECURE_SSL_REDIRECT = True

CSRF_COOKIE_SECURE = True
