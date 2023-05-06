from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField


# Create your models here.
GENDER = ((0, "Male"), (1, "Female"), (3, "Genderless"))


class Game(models.Model):
    game_version = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.game_version


class Pokeball(models.Model):
    pokeball_type = models.CharField(max_length=50, unique=True, default='pokeball')

    def __str__(self):
        return self.pokeball_type


class Pokemon(models.Model):
    dex_no = models.IntegerField(unique=False)
    name = models.CharField(max_length=50, unique=True)
    slug = models.SlugField(max_length=100, unique=True, null=True)
    featured_image = models.ImageField(upload_to='shinydex/', default='placeholder')
    type_1 = models.CharField(max_length=50)
    type_2 = models.CharField(max_length=50, null=True)
    gen = models.IntegerField(default=1)

    class Meta:
        ordering = ['dex_no']

    def __str__(self):
        return f'{self.dex_no}: {self.name}'


class UserShiny(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user')
    pokemon = models.ForeignKey(Pokemon, on_delete=models.CASCADE, related_name='pokemon')
    slug = models.SlugField(max_length=100, unique=True, null=True)
    nick_name = models.CharField(max_length=50, null=True, unique=False)
    game = models.ForeignKey(Game, on_delete=models.PROTECT, related_name='game')
    pokeball = models.ForeignKey(Pokeball, on_delete=models.PROTECT, related_name='pokeball')
    gender = models.IntegerField(choices=GENDER, default=3)
    encounters = models.IntegerField(null=True)
    caught_on = models.DateField(null=True)
    method = models.CharField(max_length=50)

    def __str__(self):
        return f'{self.pokemon}: {self.game}, {self.encounters}'
