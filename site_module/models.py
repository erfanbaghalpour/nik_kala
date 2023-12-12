from django.db import models


class SiteSetting(models.Model):
    site_name = models.CharField(max_length=200)
    site_url = models.CharField(max_length=200)
    address = models.CharField(max_length=400)
    phone = models.CharField(max_length=400, null=True, blank=True)
    fax = models.CharField(max_length=400, null=True, blank=True)
    email = models.CharField(max_length=400, null=True, blank=True)
    copy_right = models.TextField()
    site_logo = models.ImageField(upload_to='images/site-setting')
    about_us_text = models.TextField()
    is_main_setting = models.BooleanField()

    def __str__(self):
        return self.site_name

    # class Meta:
    #     verbose_name = ""
    #     verbose_name_plural = ""
