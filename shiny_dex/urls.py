from . import views
from django.urls import path


urlpatterns = [
    path('', views.HomePage.as_view(), name='home'),
    path('dex/<str:user>', views.Dex.as_view(), name='dex'),
    path('profile/<str:user>', views.Profile.as_view(), name='profile'),

]