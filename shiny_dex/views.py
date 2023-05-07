from django.shortcuts import render, redirect, get_object_or_404, reverse
from django.utils.text import slugify
from django.contrib import messages
from django.contrib.auth.models import User
from django.views import View
from .models import Game, Pokeball, Pokemon, UserShiny
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
        pokemons = Pokemon.objects.all()
        
        gameform = GameForm()
        ballform = PokeballForm()
        pokemonform = PokemonForm()

        context = {
            'games': games,
            'balls': balls,
            'pokemons': pokemons,
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


class ManagePokemonEdit(View):

    def get(self, request, slug, *args, **kwargs):
        queryset = Pokemon.objects.all()
        pokemon = get_object_or_404(queryset, slug=slug)
        pokemon_form = PokemonForm(instance=pokemon)

        context = {
            'pokemon': pokemon,
            'pokemon_form': pokemon_form,
        }

        return render(request, 'managepokemonedit.html', context)

    def post(self, request, slug, *args, **kwargs):

        queryset = Pokemon.objects.all()
        pokemon = get_object_or_404(queryset, slug=slug)

        pokemon_form = PokemonForm(request.POST, request.FILES, instance=pokemon)

        if pokemon_form.is_valid():
            pokemon_form.save()

            messages.success(request, 'Pokemon Data Updatd!')

        else:
            pokemon_form = PokemonForm()

            messages.error(request, 'Failed to update data')

        return redirect('manage')


class ManagePokemonDelete(View):

    def post(self, request, slug, *args, **kwargs):
        queryset = Pokemon.objects.all()
        pokemondel = get_object_or_404(queryset, slug=slug)
        pokemondel.delete()

        messages.warning(request, "Pokemon data deleted")
        return redirect(reverse('manage'))


class UserShinyView(View):

    def get(self, request, *args, **kwargs):
        error = "No data"
        queryset = UserShiny.objects.all().order_by('pokemon__dex_no')

        try:
            usershiny = queryset.filter(user=request.user)

        except queryset.DoesNotExist:
            usershiny = {}

        shiny_form = UserShinyForm()

        context = {
            'queryset': queryset,
            'usershiny': usershiny,
            'shiny_form': shiny_form,
            'error': error,
        }

        return render(request, 'addshiny.html', context)

    def post(self, request, *args, **kwargs):
        shinyform = UserShinyForm(request.POST)

        if shinyform.is_valid():
            shiny = shinyform.save(commit=False)
            shiny.user = request.user
            shiny.slug = slugify(f'{shiny.pokemon.name}-{shiny.user}')
            shiny.save()
            messages.success(request, 'Shiny Pokemon Added!')

        else:
            shinyform = UserShinyForm()
            messages.warning(request, "Couldn't add the data")

        return redirect(reverse('addshiny', args=[request.user]))
