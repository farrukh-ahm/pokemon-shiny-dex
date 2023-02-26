from . import views
from django.urls import path


urlpatterns = [
    path('', views.HomePage.as_view(), name='home'),
    path('dex/<str:user>', views.Dex.as_view(), name='dex'),
    path('profile/<str:user>', views.Profile.as_view(), name='profile'),
    path('manage/', views.Manage.as_view(), name='manage'),
    path('manage/addgame', views.AddGame.as_view(), name='addgame'),
    path('manage/pokeball', views.AddBall.as_view(), name='addball')

]