# Generated by Django 2.1.3 on 2018-12-04 13:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0011_book_numbers_of_pages'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='binding',
            field=models.CharField(default=None, max_length=50, verbose_name='переплет'),
        ),
        migrations.AddField(
            model_name='book',
            name='format',
            field=models.CharField(default=None, max_length=50, verbose_name='формат'),
        ),
    ]
