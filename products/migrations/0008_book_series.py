# Generated by Django 2.1.3 on 2018-12-04 13:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('reference', '0006_auto_20181204_1410'),
        ('products', '0007_auto_20181204_1545'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='series',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='reference.Series', verbose_name='серия'),
        ),
    ]
