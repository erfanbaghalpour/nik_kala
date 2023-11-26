from django.db import models


class ContactUs(models.Model):
    title = models.CharField(max_length=300, verbose_name='عنوان')
    email = models.EmailField(max_length=300, verbose_name='ایمیل')
    full_name = models.CharField(max_length=300, verbose_name='نام و نام خانوادگی')
    message = models.TextField(verbose_name='پیام', max_length=2000)
    created_date = models.DateTimeField(auto_now_add=True, verbose_name='ساخته شده در تاریخ')
    response = models.TextField(null=True, blank=True, verbose_name='پاسخ')
    is_read_by_admin = models.BooleanField(default=False, verbose_name='خوانده شده توسط ادمین')

    class Meta:
        pass

    def __str__(self):
        return self.title
