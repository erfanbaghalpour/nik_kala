from django.db import models


class ContactUs(models.Model):
    title = models.CharField(max_length=300)
    email = models.EmailField(max_length=300)
    full_name = models.CharField(max_length=300)
    message = models.TextField()
    created_date = models.DateTimeField(auto_now_add=True)
    response = models.TextField(null=True, blank=True)
    is_read_by_admin = models.BooleanField()

    class Meta:
        pass

    def __str__(self):
        return self.title
