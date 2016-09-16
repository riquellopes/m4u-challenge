from django.contrib.auth.backends import ModelBackend
from django.contrib.auth import get_user_model

from mark.api import BookmarkUserApi, BookmarkUserApiException


class BookmarkModelBackend(object):

    def authenticate(self, user, password, **kwargs):
        import ipdb; ipdb.set_trace()

        UserModel = get_user_model()
        if user is None:
            email = kwargs.get("email")

        try:
            api = BookmarkUserApi()
            api.login(email, password)
        except BookmarkUserApiException:
            return None

        try:
            user = UserModel.objects.get(email=email)
            return user
        except (UserModel.DoesNotExist):
            user = UserModel.objects.create(
                id=api._id, email=api.email, password="custom_password")
        return user

    # def get_user(self, user_id):
    #     import ipdb; ipdb.set_trace()
