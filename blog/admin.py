from django.contrib import admin
from django.http import HttpRequest

from . import models
from .models import Blog


class BlogCategoryAdmin(admin.ModelAdmin):
    list_display = ['title', 'url_title', 'parent', 'is_active']
    list_editable = ['url_title', 'is_active', 'parent']


class BlogAdmin(admin.ModelAdmin):
    list_display = ['title', 'slug', 'is_active', 'author']
    list_editable = ['is_active']

    def save_model(self, request: HttpRequest, obj: Blog, form, change):
        if not change:
            obj.author = request.user
        return super().save_model(request, obj, form, change)


admin.site.register(models.BlogCategory, BlogCategoryAdmin)
admin.site.register(models.Blog, BlogAdmin)
admin.site.register(models.BlogComment)
