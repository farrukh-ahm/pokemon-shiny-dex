from django.contrib import admin
from .models import Pokeball, Pokemon, Game, UserShiny

# Register your models here.
@admin.register(Pokeball)
class PokeballAdmin(admin.ModelAdmin):
    list_display = ['pokeball_type']


@admin.register(Game)
class GameAdmin(admin.ModelAdmin):
    list_display = ['game_version']


@admin.register(Pokemon)
class PokemonAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}
    list_display = ['dex_no', 'slug', 'name','type_1', 'type_2', 'gen']
    list_filter = ['type_1', 'type_2', 'gen']
    search_fields = ['dex_no', 'name']


@admin.register(UserShiny)
class UserShinyAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('user', 'pokemon')}
    list_display = ['user', 'slug', 'pokemon', 'nick_name', 'game', 'pokeball',
                            'gender', 'encounters', 'caught_on', 'method']
    list_filter = ['user']
    search_fields = ['user']
