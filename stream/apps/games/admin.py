from django.contrib import admin
from .models import *

# Register your models here.

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name']
    prepopulated_fields = {'slug': ('name',)}

@admin.register(Games)
class GamesAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'image', 'created_at','game_trailer','game_url',
                    'download_count', 'views_count', 'rating', 'category']


