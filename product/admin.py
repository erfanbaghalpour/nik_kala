from django.contrib import admin
from . import models


class UserAdmin(admin.ModelAdmin):
    list_display = ['title', 'price', 'rating', 'short_description', 'long_description', 'is_active', 'image']


admin.site.register(models.Product, UserAdmin)
