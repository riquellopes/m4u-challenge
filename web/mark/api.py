from django.conf import settings
from functools import wraps

BOOKMARK_API = settings.BOOKMARK_API


def validation():
    @wraps
    def auth(self, **kwargs):
        pass
    return auth


class BookmarkApi(object):

    def auth(self, user, password):
        pass

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

    def create(self):
        pass

    def get(self):
        pass

    def list(self):
        pass
