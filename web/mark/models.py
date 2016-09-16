from django.contrib.auth.models import AbstractBaseUser
from django.db.models import TextField, EmailField


class BookmarkUser(AbstractBaseUser):
    has_usable_password = False
    id_sso_user = TextField('BookmarkUser', unique=True)
    email = EmailField('BookmarkEmail', unique=True)

    USERNAME_FIELD = "id_sso_user"

    # class Meta:
    #     app_label = 'mark'
