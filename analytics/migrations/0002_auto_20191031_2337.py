# Generated by Django 2.2.6 on 2019-10-31 21:37

import analytics.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('analytics', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='image',
            field=models.ImageField(upload_to=analytics.models.upload_article_images_folder, verbose_name='Фотография'),
        ),
        migrations.AlterField(
            model_name='article',
            name='slug',
            field=models.SlugField(unique=True, verbose_name='Ссылка'),
        ),
        migrations.AlterField(
            model_name='category',
            name='slug',
            field=models.SlugField(unique=True, verbose_name='Ссылка'),
        ),
    ]
