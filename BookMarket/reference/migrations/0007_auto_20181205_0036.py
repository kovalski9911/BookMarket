# Generated by Django 2.1.3 on 2018-12-04 21:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('reference', '0006_auto_20181204_1410'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='author',
            options={'verbose_name_plural': 'Авторы'},
        ),
        migrations.AlterModelOptions(
            name='genre',
            options={'verbose_name_plural': 'Жанры'},
        ),
        migrations.AlterModelOptions(
            name='manufacturer',
            options={'verbose_name_plural': 'Изгатовители'},
        ),
        migrations.AlterModelOptions(
            name='publisher',
            options={'verbose_name_plural': 'Издательства'},
        ),
        migrations.AlterModelOptions(
            name='series',
            options={'verbose_name_plural': 'Серии'},
        ),
    ]
