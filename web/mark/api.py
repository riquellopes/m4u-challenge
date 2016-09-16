from django.conf import settings
from functools import wraps

BOOKMARK_API = settings.BOOKMARK_API


class BookmarkUserApiException(Exception):
    pass


def validation(func):
    @wraps(func)
    def auth(*args, **kwargs):
        self = args[0]
    return auth


class BookmarkApi(object):

    # @validation
    def list(self):
        pass

    # @validation
    def get(self, id_bookmark):
        pass

    # @validation
    def delete(self, id_bookmark):
        pass

    # @validation
    def updated(self, id_bookmark, url):
        pass


class BookmarkUserApi(object):

    def login(self, email, password):
        pass

    def logout(self):
        pass

    def create(self):
        pass

    def get(self):
        pass

    def list(self):
        pass

    def is_ok(self):
        pass
