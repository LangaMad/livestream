from django.shortcuts import render
from .models import *
from django.views.generic import ListView, DetailView
# Create your views here.


class GamesListView(ListView):
    model = Games
    template_name = 'pages/game_list.html'
    context_object_name = 'games'
    queryset = Games.objects.all().order_by('-created_at')



