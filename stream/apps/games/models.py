from django.db import models

# Create your models here.


class Category(models.Model):
    name = models.CharField('Название категории', max_length=100)
    slug = models.SlugField('slug')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'




class Games(models.Model):
    name = models.CharField('Название игры', max_length=100)
    description = models.TextField('Описание игры')
    image = models.ImageField('Изображение игры', upload_to='games/')
    created_at = models.DateTimeField('Дата добавления', auto_now_add=True)
    download_count = models.PositiveIntegerField('Количество скачиваний',
    default=0)
    views_count = models.PositiveIntegerField('Текущие зрители', default=0)
    rating = models.FloatField('Рейтинг игры', default=0.0)
    category = models.ForeignKey(Category, on_delete=models.CASCADE,
    related_name='games')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Игра'
        verbose_name_plural = 'Игры'

# games = [# Dota = Games(name='Dota 2', description='Описание игры Dota 2')
# # GTA5 = Games(name='GTA 5', description='Описание игры GTA 5')
# # Skyrim = Games(name='Skyrim', description='Описание игры Skyrim')
# ]
