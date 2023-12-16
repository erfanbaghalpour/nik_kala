from django.contrib import admin
from . import models


class BlogCategoryAdmin(admin.ModelAdmin):
    list_display = ['title', 'url_title', 'parent', 'is_active']
    list_editable = ['url_title', 'is_active', 'parent']


admin.site.register(models.BlogCategory, BlogCategoryAdmin)
admin.site.register(models.Blog)
