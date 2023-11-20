from django.contrib import admin
from . import models


class UserAdmin(admin.ModelAdmin):
    list_display = ['username', 'email', 'mobile', ]
    list_editable = ['email', 'mobile']



admin.site.register(models.User, UserAdmin)
