# Generated by Django 4.2.7 on 2023-12-15 15:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('site_module', '0002_slider_alter_sitesetting_options'),
    ]

    operations = [
        migrations.AlterField(
            model_name='slider',
            name='image',
            field=models.ImageField(blank=True, max_length=1000, null=True, upload_to='images/sliders'),
        ),
    ]
