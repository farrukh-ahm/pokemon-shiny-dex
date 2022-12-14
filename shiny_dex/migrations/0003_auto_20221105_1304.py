# Generated by Django 3.2.16 on 2022-11-05 13:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shiny_dex', '0002_auto_20221105_1256'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pokemon',
            name='slug',
            field=models.SlugField(max_length=100, null=True, unique=True),
        ),
        migrations.AlterField(
            model_name='user_shiny',
            name='slug',
            field=models.SlugField(max_length=100, null=True, unique=True),
        ),
    ]
