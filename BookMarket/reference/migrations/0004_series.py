# Generated by Django 2.1.3 on 2018-12-03 14:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reference', '0003_genre'),
    ]

    operations = [
        migrations.CreateModel(
            name='Series',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='')),
                ('description', models.CharField(max_length=200, verbose_name='об авторе')),
            ],
        ),
    ]
