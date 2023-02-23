from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.models import User
from django.views import View
from .models import Game, Pokeball, Pokemon, User_Shiny

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