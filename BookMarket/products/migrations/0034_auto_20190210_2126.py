# Generated by Django 2.1.3 on 2019-02-10 18:26

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0033_auto_20190128_2211'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='created',
            field=models.DateField(blank=True, default=datetime.date(2019, 2, 10), null=True, verbose_name='дата внесения в каталог'),
        ),
    ]
