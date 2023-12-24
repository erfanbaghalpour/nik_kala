from django.contrib.auth.models import AbstractUser, BaseUserManager, PermissionsMixin
from django.db import models


class User(AbstractUser):
    email = models.EmailField(unique=True, null=False)
    email_active_code = models.CharField(max_length=100, editable=False, unique=True, null=True)
    mobile = models.CharField(max_length=11, null=True, blank=True)
    username = models.CharField(max_length=100)
    about_user = models.TextField(null=True, blank=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    def __str__(self):
        if self.first_name is not None and self.last_name is not None:
            return self.get_full_name()
        return self.email

    # class Meta:
    #     verbose_name = ''
    #     verbose_name_plural = ''
