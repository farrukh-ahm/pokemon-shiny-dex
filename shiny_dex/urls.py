from . import views
from django.urls import path


urlpatterns = [
    path('', views.HomePage.as_view(), name='home'),
    path('dex/', views.Dex.as_view(), name='dex'),

]