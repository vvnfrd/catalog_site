# Generated by Django 5.0.6 on 2024-05-10 12:19

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('materials', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='material',
            name='create_at',
            field=models.DateField(auto_now_add=True, default=django.utils.timezone.now, verbose_name='дата создания'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='material',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='materials/', verbose_name='изображение продукта'),
        ),
        migrations.AddField(
            model_name='material',
            name='publish',
            field=models.BooleanField(default=True, verbose_name='опубликован'),
        ),
        migrations.AddField(
            model_name='material',
            name='views_counter',
            field=models.PositiveIntegerField(default=0, help_text='укажите количество просмотров', verbose_name='количество просмотров'),
        ),
    ]
