# Generated by Django 2.1.3 on 2019-01-28 19:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0032_auto_20190128_2140'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='date_of_published',
            field=models.CharField(blank=True, default=None, max_length=4, null=True, verbose_name='год издания'),
        ),
    ]
