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
    game_url = models.URLField('Ссылка на игру',blank=True,null=True)
    game_trailer = models.FileField('Трейлер игры', upload_to='games_trailer/',
    blank=True, null=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Игра'
        verbose_name_plural = 'Игры'

# game = Games('Dota') ID = 1
# game = Game('GTA5') ID = 2

