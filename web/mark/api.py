from django.conf import settings
from functools import wraps

import requests

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

    def _set_user(self, json):
        self.username = json['user']['username']
        self.id = json['user']['_id']
        self.token = json['token'] if "token" in json else None
        self.is_admin = json['user']['is_admin']
        return json

    def login(self, username, password):
        try:
            response = requests.post(
                "{}/user/auth".format(BOOKMARK_API), data={"username": username, "password": password})

            if response.status_code == 200:
                return self._set_user(response.json())
            raise BookmarkUserApiException("User does not exist.")
        except:
            raise BookmarkUserApiException("User does not exist.")

    def logout(self):
        pass

    def create(self, username, password):
        response = requests.post(
            "{}/user".format(BOOKMARK_API), data={"username": username, "password": password})

        if response.status_code == 201:
            return self._set_user(response.json())
        raise BookmarkUserApiException("User does not created.")

    def get(self):
        pass

    def list(self):
        pass

    def is_ok(self):
        pass
