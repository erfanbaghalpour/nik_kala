# Generated by Django 4.2.7 on 2023-12-22 17:53

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0006_alter_blog_author'),
    ]

    operations = [
        migrations.AddField(
            model_name='blog',
            name='crerate_date',
            field=models.DateTimeField(auto_now_add=True, default=datetime.date(2023, 12, 22)),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='blog',
            name='author_image',
            field=models.ImageField(blank=True, editable=False, max_length=1000, null=True, upload_to='images/blogs'),
        ),
    ]
