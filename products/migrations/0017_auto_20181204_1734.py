# Generated by Django 2.1.3 on 2018-12-04 14:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0016_auto_20181204_1720'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='created',
            field=models.DateTimeField(default=None, verbose_name='дата внесения в каталог'),
        ),
        migrations.AddField(
            model_name='book',
            name='rating',
            field=models.SmallIntegerField(default=None, verbose_name='рейтинг (0 - 10)'),
        ),
        migrations.AddField(
            model_name='book',
            name='updated',
            field=models.DateTimeField(default=None, verbose_name='дата последнего изменения карточки'),
        ),
        migrations.AlterField(
            model_name='book',
            name='available',
            field=models.BooleanField(default=False, verbose_name='доступен'),
        ),
    ]
