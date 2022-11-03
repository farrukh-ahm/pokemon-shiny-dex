# Generated by Django 3.2.16 on 2022-11-03 11:00

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Game',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('game_version', models.CharField(max_length=50, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Pokeball',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pokeball_type', models.CharField(default='pokeball', max_length=50, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Pokemon',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dex_no', models.IntegerField(unique=True)),
                ('name', models.CharField(max_length=50, unique=True)),
                ('type_1', models.CharField(max_length=50)),
                ('type_2', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='User_Shiny',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('gender', models.IntegerField(choices=[(0, 'Male'), (1, 'Female'), (3, 'Genderless')], default=3)),
                ('encounters', models.IntegerField(null=True)),
                ('caught_on', models.DateField(null=True)),
                ('method', models.CharField(max_length=50)),
                ('game', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='game', to='shiny_dex.game')),
                ('pokeball', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='pokeball', to='shiny_dex.pokeball')),
                ('pokemon', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='pokemon', to='shiny_dex.pokemon')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]