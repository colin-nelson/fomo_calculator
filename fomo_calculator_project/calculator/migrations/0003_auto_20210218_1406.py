# Generated by Django 3.1.6 on 2021-02-18 19:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('calculator', '0002_auto_20210217_2019'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mainpage',
            name='date',
            field=models.DateField(),
        ),
    ]
