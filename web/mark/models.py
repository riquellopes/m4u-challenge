# from __future__ import unicode_literals
#
# from django.contrib.auth.models import UserManager
# from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
# from django.db.models import EmailField, TextField, CharField
#
#
# class BookmarkUser(AbstractBaseUser, PermissionsMixin):
#     has_usable_password = False
#
#     id_user_bookmark = TextField("BookmarkUserId", unique=True)
#     email = EmailField('BookmarkEmail', unique=True)
#     username = CharField(unique=True, max_length=20)
#
#     objects = UserManager()
#
#     USERNAME_FIELD = "email"
#     REQUIRED_FIELDS = ["username", ]
#
#     class Meta:
#         app_label = 'mark'
