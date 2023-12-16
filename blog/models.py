from django.db import models


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
    author = models.CharField(max_length=300, null=True, blank=True)
    author_image = models.ImageField(max_length=1000, upload_to='images/blogs', null=True, blank=True)
    selected_categories = models.ManyToManyField(BlogCategory)

    def __str__(self):
        return self.title

    # class Meta:
    #     verbose_name = ''
    #     verbose_name_plural = ''
