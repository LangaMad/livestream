from .views import *
from django.urls import path

urlpatterns = [
    path('game_list/', GamesListView.as_view(), name='game_list'),
    path('game_detail/', GameDetail.as_view(), name='game_detail'),
]