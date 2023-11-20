from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from django.urls import reverse
from django.utils.text import slugify


class ProductCategory(models.Model):
    title = models.CharField(max_length=300)
    url_title = models.CharField(max_length=300)

    def __str__(self):
        return self.title


class Product(models.Model):
    title = models.CharField(max_length=300)
    category = models.ForeignKey(ProductCategory, on_delete=models.CASCADE, null=True, related_name='products')
    price = models.IntegerField()
    rating = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(5)], default=1)
    short_description = models.CharField(max_length=300, null=True)
    long_description = models.CharField(max_length=2000, null=True)
    is_active = models.BooleanField(default=False)
    image = models.ImageField(upload_to="media/images/products", max_length=500, default=False)
    slug = models.SlugField(default="", null=False, db_index=True, blank=True)

    def __str__(self):
        return f"{self.title} ({self.price})"

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    def get_absolute_url(self):
        #     # return reverse('product_detail', args=[self.id])
        return reverse('product_detail', args=[self.slug])
