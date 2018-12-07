# Generated by Django 2.1.3 on 2018-12-04 12:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reference', '0006_auto_20181204_1410'),
        ('products', '0006_book_authors'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='book',
            name='authors',
        ),
        migrations.AddField(
            model_name='book',
            name='authors',
            field=models.ManyToManyField(to='reference.Author', verbose_name='автор'),
        ),
    ]
