# Generated by Django 3.2.16 on 2022-11-05 13:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shiny_dex', '0003_auto_20221105_1304'),
    ]

    operations = [
        migrations.AddField(
            model_name='user_shiny',
            name='nick_name',
            field=models.CharField(max_length=50, null=True),
        ),
    ]
