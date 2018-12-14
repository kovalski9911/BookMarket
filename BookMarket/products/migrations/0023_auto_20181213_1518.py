# Generated by Django 2.1.3 on 2018-12-13 12:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0022_auto_20181213_1515'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='created',
            field=models.DateTimeField(blank=True, default=None, null=True, verbose_name='дата внесения в каталог'),
        ),
        migrations.AlterField(
            model_name='book',
            name='date_of_published',
            field=models.DateField(blank=True, default=None, null=True, verbose_name='год издания'),
        ),
        migrations.AlterField(
            model_name='book',
            name='updated',
            field=models.DateTimeField(blank=True, default=None, null=True, verbose_name='дата последнего изменения карточки'),
        ),
    ]
