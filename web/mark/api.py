import requests

from django.conf import settings

BOOKMARK_API = settings.BOOKMARK_API


class BookmarkUserApiException(Exception):
    pass


class BookmarkApi(object):

    def __init__(self, token):
        self.token = token

    def list(self):
        response = requests.get(
            "{}/bookmark/".format(BOOKMARK_API), headers={"x-access-token": self.token})

        if response.status_code == 200:
            json = response.json()
            return ({"url": bookmark['url'], "id": bookmark['_id']} for bookmark in json)
        return []

    def get(self, id_bookmark):
        response = requests.get(
            "{}/bookmark/{}".format(BOOKMARK_API, id_bookmark), headers={"x-access-token": self.token})

        if response.status_code == 200:
            return response.json()
        raise BookmarkUserApiException("Bookmark does not exist.")

    def delete(self, id_bookmark):
        response = requests.delete(
            "{}/bookmark/{}".format(BOOKMARK_API, id_bookmark), headers={"x-access-token": self.token})

        if response.status_code == 200:
            return True
        raise BookmarkUserApiException("Bookmark was not deleted.")

    def updated(self, id_bookmark, url):
        response = requests.put(
            "{}/bookmark/{}".format(BOOKMARK_API, id_bookmark),
            headers={"x-access-token": self.token}, data={"url": url})

        if response.status_code == 201:
            return True
        raise BookmarkUserApiException("Bookmark was not updated.")

    def create(self, url):
        response = requests.post(
            "{}/bookmark/".format(BOOKMARK_API), headers={"x-access-token": self.token}, data={"url": url})

        if response.status_code == 201:
            return True
        raise BookmarkUserApiException("Bookmark was not created.")

    def list_groupby(self):
        response = requests.get(
            "{}/bookmark/group-by".format(BOOKMARK_API), headers={"x-access-token": self.token})

        if response.status_code == 200:
            return response.json()
        raise BookmarkUserApiException("Bookmark does not exist.")


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

    def list(self, token):
        response = requests.get(
            "{}/user/".format(BOOKMARK_API), headers={"x-access-token": token})

        if response.status_code == 200:
            return response.json()
        raise BookmarkUserApiException("Users does not exist.")
