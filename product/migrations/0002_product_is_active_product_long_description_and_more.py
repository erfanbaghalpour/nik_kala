# Generated by Django 4.2.7 on 2023-11-18 15:47

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='is_active',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='product',
            name='long_description',
            field=models.CharField(max_length=2000, null=True),
        ),
        migrations.AddField(
            model_name='product',
            name='rating',
            field=models.IntegerField(default=1, validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(5)]),
        ),
        migrations.AddField(
            model_name='product',
            name='short_description',
            field=models.CharField(max_length=300, null=True),
        ),
    ]
