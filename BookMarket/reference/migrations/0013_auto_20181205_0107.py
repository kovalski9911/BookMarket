# Generated by Django 2.1.3 on 2018-12-04 22:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reference', '0012_auto_20181205_0103'),
    ]

    operations = [
        migrations.AlterField(
            model_name='author',
            name='name',
            field=models.CharField(default=None, max_length=50, verbose_name='автор'),
        ),
    ]
