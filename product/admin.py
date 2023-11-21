from django.contrib import admin
from . import models


class ProductAdmin(admin.ModelAdmin):
    list_display = ['title', 'price', 'short_description', 'long_description', 'is_active', 'image', 'slug']


class ProductCategoryAdmin(admin.ModelAdmin):
    list_display = ['title', 'url_title']


admin.site.register(models.Product, ProductAdmin)
admin.site.register(models.ProductCategory)
admin.site.register(models.ProductInformation)
