# Generated by Django 2.1.3 on 2018-12-04 11:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reference', '0005_auto_20181204_1405'),
    ]

    operations = [
        migrations.CreateModel(
            name='Manufacturer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='изгатовитель')),
                ('description', models.CharField(max_length=200, verbose_name='об изгатовителе')),
            ],
            options={
                'verbose_name_plural': 'Manufacturers',
            },
        ),
        migrations.AlterField(
            model_name='author',
            name='name',
            field=models.CharField(max_length=50, verbose_name='автор'),
        ),
        migrations.AlterField(
            model_name='genre',
            name='name',
            field=models.CharField(max_length=50, verbose_name='жанр'),
        ),
        migrations.AlterField(
            model_name='publisher',
            name='name',
            field=models.CharField(max_length=50, verbose_name='издательство'),
        ),
        migrations.AlterField(
            model_name='series',
            name='description',
            field=models.CharField(max_length=200, verbose_name='о серии'),
        ),
        migrations.AlterField(
            model_name='series',
            name='name',
            field=models.CharField(max_length=50, verbose_name='серия'),
        ),
    ]
