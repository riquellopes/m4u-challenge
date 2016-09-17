from django.db import models
from django.contrib.auth.models import User


class Profile(models.Model):
    user = models.OneToOneField(User, unique=True, related_name='profile')
    token = models.TextField(editable=False)

    def __str__(self):
        return 'Profile of user: {}'.format(self.user.username)
