from django.db import models
from django.contrib.auth.models import AbstractUser, PermissionsMixin

from users.managers import UserManager


class User(AbstractUser, PermissionsMixin):
    """Custom user model"""
    username = None
    email = models.EmailField(max_length=255, unique=True)
    name = models.CharField(max_length=255)
    is_superuser = models.BooleanField(default=False)

    objects = UserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []
