# Generated by Django 3.1.6 on 2021-02-18 01:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('calculator', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mainpage',
            name='date',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]