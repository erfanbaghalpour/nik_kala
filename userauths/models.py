from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    email = models.EmailField(unique=True, null=False)
    mobile = models.CharField(max_length=11)
    username = models.CharField(max_length=100)

    USERNAME_FIELD = 'email'
