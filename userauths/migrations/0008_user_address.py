# Generated by Django 4.2.7 on 2023-12-30 17:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('userauths', '0007_user_about_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='address',
            field=models.TextField(blank=True, null=True),
        ),
    ]