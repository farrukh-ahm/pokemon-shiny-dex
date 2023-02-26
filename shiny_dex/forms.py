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
