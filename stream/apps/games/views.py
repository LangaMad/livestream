from django.shortcuts import render
from .models import *
from django.views.generic import ListView, DetailView
# Create your views here.


class GamesListView(ListView):
    model = Games
    template_name = 'pages/games_list.html'
    context_object_name = 'games'
    queryset = Games.objects.all().order_by('-created_at')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # context['categories'] = Category.objects.all()
        context['top_down'] = Games.objects.order_by('-download_count')[:6]
        return context
#               0        1        2
# CREATED_AT = ['19:40','19:45','19:55']
#              -3        -2      -1



class GameDetail(DetailView):
    model = Games
    template_name = 'pages/games_detail.html'
    context_object_name = 'game'
    queryset = Games.objects.all()

