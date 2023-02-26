from django.shortcuts import render, redirect, get_object_or_404, reverse
from django.utils.text import slugify
from django.contrib import messages
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
        balls = Pokeball.objects.all()
        pokemon = Pokemon.objects.all()
        
        gameform = GameForm()
        ballform = PokeballForm()
        pokemonform = PokemonForm()

        context = {
            'games': games,
            'balls': balls,
            'pokemon': pokemon,
            'gameform': gameform,
            'ballform': ballform,
            'pokemonform': PokemonForm,
        }

        return render(request, 'manage.html', context)

    def post(self, request, *args, **kwargs):
        queryset = Pokemon.objects.all()
        pokemon_form = PokemonForm(request.POST, request.FILES)

        if pokemon_form.is_valid():
            pokemon = pokemon_form.save(commit=False)
            pokemon.slug = slugify(pokemon.name)
            pokemon.save()

            messages.success(request, 'Pokemon added!')

        else:
            pokemon_form = PokemonForm()
            messages.error(request, 'Error adding pokemon')

        return redirect(reverse('manage'))


class AddGame(View):

    def post(self, request, *args, **kwargs):
        gameform = GameForm(request.POST)
        if gameform.is_valid():
            gameform.save()

            messages.success(request, 'Game added!')

        else:
            gameform = GameForm()

        return redirect(reverse('manage'))


class AddBall(View):

    def post(self, request, *args, **kwargs):
        ballform = PokeballForm(request.POST)

        if ballform.is_valid():
            ballform.save()

            messages.success(request, 'Pokeball added!')

        else:
            ballform = PokeballForm()

        return redirect(reverse('manage'))
