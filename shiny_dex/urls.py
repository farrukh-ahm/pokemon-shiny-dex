from . import views
from django.urls import path


urlpatterns = [
    path('', views.HomePage.as_view(), name='home'),
    path('dex/<str:user>', views.Dex.as_view(), name='dex'),
    path('profile/<str:user>', views.Profile.as_view(), name='profile'),
    path('manage/', views.Manage.as_view(), name='manage'),
    path('manage/addgame', views.AddGame.as_view(), name='addgame'),
    path('manage/pokeball', views.AddBall.as_view(), name='addball'),
    path('manage/editpokemon/<slug:slug>', views.ManagePokemonEdit.as_view(), name='managepokemonedit'),
    path('manage/deletepokemon/<slug:slug>', views.ManagePokemonDelete.as_view(), name='deletepokemon'),
    path('add_shiny/<str:user>', views.UserShinyView.as_view(), name='addshiny'),
    path('add_shiny/edit/<str:user>/<slug:slug>', views.UserShinyEdit.as_view(), name='editshiny'),
    path('delete/<str:user>/<slug:slug>', views.UserShinyDelete.as_view(), name='deleteShiny'),
    path('userdex/<str:user>', views.UserShinyDex.as_view(), name='userdex'),
]
