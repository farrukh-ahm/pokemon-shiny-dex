from django import forms
from .models import *


class GameForm(forms.ModelForm):

    class Meta:
        model = Game
        fields = ('game_version',)