# Generated by Django 4.2.7 on 2023-12-15 15:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('site_module', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Slider',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('image', models.ImageField(blank=True, null=True, upload_to='images/sliders')),
            ],
        ),
        migrations.AlterModelOptions(
            name='sitesetting',
            options={},
        ),
    ]
