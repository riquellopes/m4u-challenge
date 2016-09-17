from django.conf import settings
from django.contrib.auth.backends import ModelBackend
from django.contrib.auth import get_user_model

from mark.api import BookmarkUserApi, BookmarkUserApiException
from mark.models import Profile


class BookmarkModelBackend(ModelBackend):

    def authenticate(self, **kwargs):
        UserModel = get_user_model()
        api = BookmarkUserApi()

        try:
            api.login(kwargs.get('username'), kwargs.get('password'))
        except BookmarkUserApiException:
            return None

        try:
            user = UserModel.objects.get(username=api.username)
        except UserModel.DoesNotExist:
            create = UserModel.objects.create
            if api.is_admin:
                create = UserModel.objects.create_superuser
            user = create(
                username=api.username, password=settings.BOOKMARK_DEFAULT_PASS, email=settings.BOOKMARK_DEFAULT_EMAIL)

        # Create profile
        try:
            profile = Profile.objects.get(user=user)
        except Profile.DoesNotExist:
            profile = Profile()
            profile.user = user
        profile.token = api.token
        profile.save()
        return user
