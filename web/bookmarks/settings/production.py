from .base import *

DEBUG = False

ALLOWED_HOSTS = ('*', )

STATIC_ROOT = os.environ.get("STATIC_ROOT", os.path.join(BASE_DIR, "staticfiles"))
