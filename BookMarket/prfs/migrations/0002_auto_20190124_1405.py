# Generated by Django 2.1.3 on 2019-01-24 11:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('prfs', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='prf',
            name='delivery_address',
            field=models.TextField(default='Заполнить', verbose_name='Адрес доставки'),
        ),
    ]