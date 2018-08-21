from django.db import models
from django.contrib.auth.models import AbstractUser, UserManager


class CustomUserManager(UserManager):
	pass
    # def get_by_natural_key(self, username):
    #     case_insensitive_username_field = '{}__iexact'.format(self.model.USERNAME_FIELD)
    #     return self.get(**{case_insensitive_username_field: username})


class User(AbstractUser):
    bio = models.TextField(max_length=500, blank=True)
    location = models.CharField(max_length=30, blank=True)

    objects = CustomUserManager()
