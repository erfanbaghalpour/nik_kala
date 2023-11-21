from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from django.urls import reverse
from django.utils.text import slugify


class ProductCategory(models.Model):
    title = models.CharField(max_length=300, db_index=True)
    url_title = models.CharField(max_length=300, db_index=True)
    is_active = models.BooleanField()
    is_delete = models.BooleanField()

    def __str__(self):
        return self.title

    # class Meta:
    #     verbose_name = 'دسته بندی'
    #     verbose_name_plural = 'دسته بندی ها'


class ProductInformation(models.Model):
    color = models.CharField(max_length=200)
    size = models.CharField(max_length=200)

    def __str__(self):
        return f"{self.color} | {self.size}"

    # class Meta:
    #     verbose_name = 'دسته بندی'
    #     verbose_name_plural = 'دسته بندی ها'


class Product(models.Model):
    title = models.CharField(max_length=300)
    category = models.ManyToManyField(ProductCategory,
                                      related_name='product_categories')
    product_information = models.OneToOneField(ProductInformation, on_delete=models.CASCADE,
                                               related_name='product_information')
    # product_tags = models.ManyToManyField(ProductTag)
    price = models.IntegerField()
    # rating = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(5)], default=1)
    short_description = models.CharField(max_length=300, null=True, db_index=True)
    long_description = models.TextField(null=True, db_index=True)
    is_active = models.BooleanField(default=False)
    image = models.ImageField(upload_to="media/images/products", max_length=500, default=False)
    slug = models.SlugField(default="", null=False, db_index=True, blank=True, max_length=200, unique=True)
    is_delete = models.BooleanField()

    def __str__(self):
        return f"{self.title} ({self.price})"

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    def get_absolute_url(self):
        #     # return reverse('product_detail', args=[self.id])
        return reverse('product_detail', args=[self.slug])

    # class Meta:
    #     verbose_name = 'دسته بندی'
    #     verbose_name_plural = 'دسته بندی ها'


class ProductTag(models.Model):
    tag = models.CharField(max_length=300, db_index=True)
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='product_tags')
    is_delete = models.BooleanField()

    def __str__(self):
        return self.tag

    # class Meta:
    #     verbose_name = 'دسته بندی'
    #     verbose_name_plural = 'دسته بندی ها'
