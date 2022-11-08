from django.shortcuts import render, redirect, get_object_or_404
from django.views import View
from .models import Game, Pokeball, Pokemon, User_Shiny

# Create your views here.


class HomePage(View):

    def get(self, request, *args, **kwargs):
        return render(request, 'index.html')


class Dex(View):

    def get(self, request, *args, **kwargs):
        return render(request, 'dex.html')
