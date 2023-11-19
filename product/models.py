from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from django.urls import reverse

class Product(models.Model):
    title = models.CharField(max_length=300)
    price = models.IntegerField()
    rating = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(5)], default=1)
    short_description = models.CharField(max_length=300, null=True)
    long_description = models.CharField(max_length=2000, null=True)
    is_active = models.BooleanField(default=False)
    image = models.ImageField(upload_to="media/images/products", max_length=500, default=False)

    def __str__(self):
        return f"{self.title} ({self.price})"

    def get_absolute_url(self):
        return reverse('product_detail', args=[self.id])


