# Generated by Django 2.1.3 on 2019-02-16 09:46

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0035_auto_20190211_2331'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='created',
            field=models.DateField(blank=True, default=datetime.date(2019, 2, 16), null=True, verbose_name='дата внесения в каталог'),
        ),
    ]