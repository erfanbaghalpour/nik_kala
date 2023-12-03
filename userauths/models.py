from django.contrib.auth.models import AbstractUser, BaseUserManager, PermissionsMixin
from django.db import models


class User(AbstractUser):
    email = models.EmailField(unique=True, null=False)
    email_active_code = models.CharField(max_length=100, editable=False, unique=True, null=True)
    mobile = models.CharField(max_length=11)
    username = models.CharField(max_length=100)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    def __str__(self):
        return self.username

    # class Meta:
    #     verbose_name = ''
    #     verbose_name_plural = ''
