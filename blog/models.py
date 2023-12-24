from django.db import models
from jalali_date import date2jalali

from userauths.models import User


class BlogCategory(models.Model):
    parent = models.ForeignKey('BlogCategory', on_delete=models.CASCADE, null=True, blank=True)
    title = models.CharField(max_length=200)
    url_title = models.CharField(max_length=200, unique=True)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.title

    # class Meta:
    #     verbose_name = ''
    #     verbose_name_plural = ''


class Blog(models.Model):
    title = models.CharField(max_length=300)
    slug = models.SlugField(max_length=400, db_index=True, allow_unicode=True)
    image = models.ImageField(max_length=1000, upload_to='images/blogs')
    short_description = models.CharField(max_length=1000)
    text = models.TextField()
    is_active = models.BooleanField(default=True)
    author = models.ForeignKey(User, max_length=300, null=True, blank=True, on_delete=models.CASCADE)
    # author = models.CharField(max_length=300, null=True, blank=True)
    author_image = models.ImageField(max_length=1000, upload_to='images/blogs', null=True, blank=True, editable=False)
    selected_categories = models.ManyToManyField(BlogCategory)
    create_date = models.DateTimeField(auto_now_add=True, editable=False, null=True, blank=True)

    def __str__(self):
        return self.title

    def get_jalali_create_date(self):
        return date2jalali(self.create_date)

    def get_jalali_create_time(self):
        return self.create_date.strftime('%H:%M')

    # class Meta:
    #     verbose_name = ''
    #     verbose_name_plural = ''


class BlogComment(models.Model):
    blog = models.ForeignKey(Blog, on_delete=models.CASCADE)
    parent = models.ForeignKey('BlogComment', on_delete=models.CASCADE, null=True, blank=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    create_date = models.DateTimeField(auto_now_add=True)
    text = models.TextField()


    # class Meta:
    #     verbose_name = ''
    #     verbose_name_plural = ''