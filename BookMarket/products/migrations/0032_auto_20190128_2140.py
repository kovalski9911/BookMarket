# Generated by Django 2.1.3 on 2019-01-28 18:40

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0031_auto_20190125_1449'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='created',
            field=models.DateField(blank=True, default=datetime.date(2019, 1, 28), null=True, verbose_name='дата внесения в каталог'),
        ),
        migrations.AlterField(
            model_name='book',
            name='date_of_published',
            field=models.IntegerField(blank=True, default=None, null=True, verbose_name='год издания'),
        ),
    ]
