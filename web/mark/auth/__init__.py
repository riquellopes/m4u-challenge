from django.conf import settings
from django.contrib.auth.backends import ModelBackend
from django.contrib.auth import get_user_model

from mark.api import BookmarkUserApi, BookmarkUserApiException


class BookmarkModelBackend(ModelBackend):

    def authenticate(self, **kwargs):
        UserModel = get_user_model()
        api = BookmarkUserApi()

        try:
            api.login(kwargs.get('username'), kwargs.get('password'))
        except BookmarkUserApiException:
            return None

        try:
            return UserModel.objects.get(username=api.username)
        except UserModel.DoesNotExist:
            create = UserModel.objects.create
            if api.is_admin:
                create = UserModel.objects.create_user
            return create(username=api.username, password=settings.BOOKMARK_DEFAULT_PASS)
