from django import forms
from .models import *


class GameForm(forms.ModelForm):

    class Meta:
        model = Game
        fields = ('game_version',)


class PokeballForm(forms.ModelForm):

    class Meta:
        model = Pokeball
        fields = ('pokeball_type',)


class PokemonForm(forms.ModelForm):

    class Meta:
        model = Pokemon
        fields = ('dex_no', 'name', 'featured_image',
                  'type_1', 'type_2', 'gen',
                  )
