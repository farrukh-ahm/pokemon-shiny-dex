from django.shortcuts import render, redirect, get_object_or_404, reverse
from django.contrib.auth.models import User
from django.views import View
from .models import Game, Pokeball, Pokemon, User_Shiny
from .forms import *

# Create your views here.


class HomePage(View):

    def get(self, request, *args, **kwargs):
        return render(request, 'index.html')


class Dex(View):

    def get(self, request, *args, **kwargs):
        return render(request, 'dex.html')


class Profile(View):

    def get(self, request, *args, **kwargs):
        queryset = User.objects.all()
        profile = get_object_or_404(queryset, username=request.user)
        context = {
            'profile': profile,
        }
        return render(request, 'profile.html', context)


class Manage(View):

    def get(self, request, *args, **kwargs):
        games = Game.objects.all()
        gameform = GameForm()

        context = {
            'games': games,
            'gameform': gameform,
        }

        return render(request, 'manage.html', context)


class AddGame(View):

    def post(self, request, *args, **kwargs):
        gameform = GameForm(request.POST)
        if gameform.is_valid():
            gameform.save()
        
        else:
            gameform = GameForm()

        return redirect(reverse('manage'))