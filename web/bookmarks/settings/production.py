from .base import *

DEBUG = False

ALLOWED_HOSTS = ('*', )

STATIC_ROOT = os.environ.get("STATIC_ROOT", os.path.join(BASE_DIR, "staticfiles"))


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': os.getenv('DB_NAME', 'bookmarks'),
        "USER": os.environ.get("DB_USER", "root"),
        "PASSWORD": os.environ.get("DATABASE_PASSWORD"),
        "HOST": os.environ.get("DB_PASS", "localhost"),
        "PORT": os.environ.get("DB_HOST", 3306)
    }
}
